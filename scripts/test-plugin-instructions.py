#!/usr/bin/env python3
"""Verify repository instructions and plugin discovery with real CLI diagnostics.

Usage: python3 scripts/test-plugin-instructions.py [--baseline REF]
Requires Claude Code and Codex (with `debug prompt-input`). No model calls or login.
Optionally pass --pi-sdk /path/to/pi-coding-agent/dist/index.js to check Pi as well.
An optional pre-fix Git ref also proves the original strict-validation failure and
byte-for-byte preservation. All checkouts, home directories, and state are temporary.
"""
import argparse
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tarfile
import tempfile

ROOT = Path(__file__).resolve().parent.parent
ROOT_WARNING = "CLAUDE.md at the plugin root is not loaded as project context"


def checkout(destination):
    paths = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT).split(b"\0")
    for name in filter(None, paths):
        name = os.fsdecode(name)
        source = ROOT / name
        if not source.exists() and not source.is_symlink():
            continue
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.is_symlink():
            target.symlink_to(source.readlink())
        else:
            shutil.copy2(source, target)


def inventory(directory):
    return {str(p.relative_to(directory)): ("link", str(p.readlink()))
            if p.is_symlink() else ("file", p.read_bytes())
            for p in directory.rglob("*") if p.is_file() or p.is_symlink()}


def run(command, cwd, env):
    result = subprocess.run(command, cwd=cwd, env=env, stdin=subprocess.DEVNULL,
                            capture_output=True, text=True, timeout=90)
    print(f"{cwd.name}: {' '.join(command)} -> exit {result.returncode}")
    return result


def checked(command, cwd, env):
    result = run(command, cwd, env)
    assert result.returncode == 0, result.stdout + result.stderr
    return result.stdout


def context(cwd, env, *extra):
    output = checked(["claude", "-p", "/context", "--output-format", "stream-json",
                      "--verbose", "--setting-sources", "project",
                      "--strict-mcp-config", *extra], cwd, env)
    events = [json.loads(line) for line in output.splitlines()]
    init, = [e for e in events if e.get("subtype") == "init"]
    usage, = [e["context_usage"] for e in events if "context_usage" in e]
    result, = [e for e in events if e.get("type") == "result"]
    assert not result["is_error"] and result["duration_api_ms"] == 0, result
    return init, usage


def memory_paths(usage):
    return {Path(m["path"]).resolve() for m in usage["memory_files"] if m["tokens"] > 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", help="pre-fix Git ref, such as 098fe03")
    parser.add_argument("--pi-sdk", type=Path, help="installed Pi SDK dist/index.js")
    args = parser.parse_args()
    for tool in ("claude", "codex"):
        assert shutil.which(tool), f"{tool} is required"
    with tempfile.TemporaryDirectory(prefix="plugin-instructions-") as work:
        home = Path(work).resolve() / "home with spaces"
        repo = home / "checkout"
        consumer = home / "consumer"
        repo.mkdir(parents=True)
        consumer.mkdir()
        (home / ".codex").mkdir()
        checkout(repo)
        before = inventory(repo)
        # Inherit no credentials, agent markers, custom endpoints, or user config.
        env = {k: os.environ[k] for k in ("PATH", "LANG", "TMPDIR") if k in os.environ}
        env.update(HOME=str(home), CLAUDE_CONFIG_DIR=str(home / ".claude"),
                   CODEX_HOME=str(home / ".codex"),
                   XDG_CONFIG_HOME=str(home / ".config"),
                   XDG_CACHE_HOME=str(home / ".cache"),
                   XDG_DATA_HOME=str(home / ".local/share"),
                   XDG_STATE_HOME=str(home / ".local/state"),
                   ANTHROPIC_API_KEY="diagnostics-only-not-a-real-key",
                   CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC="1")
        for tool in ("claude", "codex"):
            print(checked([tool, "--version"], consumer, env).strip())

        if args.baseline:
            baseline = home / "baseline"
            baseline.mkdir()
            archive = subprocess.check_output(["git", "archive", args.baseline], cwd=ROOT)
            with tarfile.open(fileobj=io.BytesIO(archive)) as files:
                files.extractall(baseline, filter="data")
            result = run(["claude", "plugin", "validate", ".", "--strict"], baseline, env)
            assert result.returncode == 1, result.stdout + result.stderr
            assert ROOT_WARNING in result.stdout + result.stderr, result.stdout + result.stderr
            assert (baseline / "CLAUDE.md").read_bytes() == (repo / "AGENTS.md").read_bytes()
            for directory in (".claude-plugin", "skills"):
                assert inventory(baseline / directory) == inventory(repo / directory), directory
            print("PASS: original warning and exit 1; payload, manifests, and skills preserved")

        result = run(["claude", "plugin", "validate", ".", "--strict"], repo, env)
        output = result.stdout + result.stderr
        assert result.returncode == 0, output
        assert ROOT_WARNING not in output, output
        print("PASS: isolated strict validation, no root instruction warning")

        canonical = repo / "AGENTS.md"
        entry = repo / ".claude/CLAUDE.md"
        assert canonical.is_file() and not canonical.is_symlink()
        assert not (repo / "CLAUDE.md").exists() and not (repo / "CLAUDE.md").is_symlink()
        _, usage = context(repo, env)
        assert memory_paths(usage) == {canonical, entry}, usage["memory_files"]
        print("PASS: fresh Claude project discovery loads the nested entry and canonical instructions")

        # Prove relative import loading, independently of any AGENTS.md fallback.
        probe = repo / "repository-policy-probe.md"
        original_entry = entry.read_bytes()
        assert original_entry.strip() == b"@../AGENTS.md", "expected a relative canonical import"
        try:
            canonical.rename(probe)
            entry.write_text("@../repository-policy-probe.md\n")
            _, usage = context(repo, env)
            assert memory_paths(usage) == {entry, probe}, usage["memory_files"]
        finally:
            probe.rename(canonical)
            entry.write_bytes(original_entry)
        print("PASS: nested entry imports a non-autodiscovered relative instruction file")

        prompt = json.loads(checked(["codex", "debug", "prompt-input"], repo, env))
        user_text = "\n".join(c.get("text", "") for item in prompt
                              if item.get("type") == "message" and item.get("role") == "user"
                              for c in item.get("content", []))
        assert canonical.read_text() in user_text, "Codex did not load the complete instruction payload"
        print("PASS: Codex model-visible prompt contains the complete canonical instructions")

        if args.pi_sdk:
            env.update(PI_CODING_AGENT_DIR=str(home / ".pi/agent"), PI_OFFLINE="1",
                       PI_TELEMETRY="0", PI_SKIP_VERSION_CHECK="1")
            checked(["node", "--input-type=module", "-e", """
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { pathToFileURL } from 'node:url';
const { DefaultResourceLoader, createAgentSession, SessionManager } =
  await import(pathToFileURL(process.argv[1]));
const cwd = process.cwd(), agentDir = process.env.PI_CODING_AGENT_DIR;
const loader = new DefaultResourceLoader({ cwd, agentDir, noExtensions: true,
  noSkills: true, noPromptTemplates: true, noThemes: true });
await loader.reload();
const files = loader.getAgentsFiles().agentsFiles;
const payload = readFileSync(cwd + '/AGENTS.md', 'utf8');
assert.deepEqual(files.map(f => f.path), [cwd + '/AGENTS.md']);
assert.equal(files[0].content, payload);
const { session } = await createAgentSession({ cwd, agentDir, resourceLoader: loader,
  sessionManager: SessionManager.inMemory(), noTools: 'all' });
try { assert.ok(session.systemPrompt.includes(payload)); }
finally { session.dispose(); }
""", str(args.pi_sdk.resolve(strict=True))], repo, env)
            print("PASS: Pi default discovery and fresh SDK session contain the complete canonical instructions")

        manifest = json.loads((repo / ".claude-plugin/plugin.json").read_text())
        prefix = manifest["name"] + ":"
        expected = {prefix + Path(p).name for p in manifest["skills"]}
        assert len(expected) == len(manifest["skills"]) == 28
        init, usage = context(consumer, env, "--plugin-dir", str(repo))
        for field in ("skills", "slash_commands"):
            discovered = [name for name in init[field] if name.startswith(prefix)]
            assert set(discovered) == expected and len(discovered) == 28, discovered
        plugins = [p for p in init["plugins"] if p["name"] == manifest["name"]]
        assert len(plugins) == 1 and Path(plugins[0]["path"]).resolve() == repo, plugins
        assert usage["memory_files"] == [], "plugin injected repository instructions into the consumer"
        print("PASS: runtime plugin discovery exposes exactly the 28 manifest skills and no repository memory")
        assert inventory(repo) == before, "verification changed checkout content"
        print("PASS: checkout unchanged; temporary checkout, home, and plugin state removed on exit")


if __name__ == "__main__":
    main()
