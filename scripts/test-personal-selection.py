#!/usr/bin/env python3
"""Verify issue #3's selection through the existing dotfiles apply hook.

Usage: python3 scripts/test-personal-selection.py /path/to/dotfiles
Requires chezmoi; all discovery changes and chezmoi state stay in a scratch home.
"""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
ACTIVE = {
    "ask-matt", "code-review", "codebase-design", "diagnosing-bugs",
    "domain-modeling", "grill-me", "grilling", "handoff", "implement",
    "improve-codebase-architecture", "merge-and-cleanup", "pr", "prototype",
    "research", "retro", "setup-matt-pocock-skills", "tdd", "to-spec",
    "to-tickets", "wait-what", "wayfinder", "writing-for-agents",
}
PARKED = {
    "grill-with-docs", "implement-spec", "teach", "to-questionnaire", "triage",
    "wizard",
}


def content(directory):
    return {str(p.relative_to(directory)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in directory.rglob("*") if p.is_file()}


def registry(root, filename, expected):
    entries = json.loads((root / filename).read_text())
    assert isinstance(entries, list), f"{filename}: expected an array"
    assert all(isinstance(p, str) for p in entries), f"{filename}: expected paths"
    assert len(entries) == len(set(entries)), f"{filename}: duplicate paths"
    for entry in entries:
        path = Path(entry)
        assert not path.is_absolute() and all(
            part not in ("", ".", "..") for part in entry.split("/")), entry
        directory = (root / path).resolve(strict=True)
        assert directory.is_relative_to(root.resolve()) and directory != root.resolve(), entry
        assert directory.is_dir() and (directory / "SKILL.md").is_file(), entry
        assert (directory / "SKILL.md").resolve().is_relative_to(root.resolve()), entry
    assert {Path(p).name for p in entries} == expected, filename
    assert len(entries) == len(expected), filename
    return set(entries)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    dotfiles = Path(sys.argv[1]).resolve(strict=True)
    assert (dotfiles / "run_before_90-skill-links.sh.tmpl").is_file()
    assert (dotfiles / "scripts/pi-skills.py").is_file()
    assert shutil.which("chezmoi"), "chezmoi is required"
    with tempfile.TemporaryDirectory(prefix="personal-selection-") as work:
        home = (Path(work) / "home with spaces").resolve()
        repo = home / "gh/skills"
        repo.mkdir(parents=True)
        shutil.copytree(ROOT / "skills", repo / "skills")
        shutil.copy2(ROOT / "enabled-skills.json", repo / "enabled-skills.json")
        if (ROOT / "parked-skills.json").exists():
            shutil.copy2(ROOT / "parked-skills.json", repo / "parked-skills.json")
        before = content(repo / "skills")
        links = home / ".agents/skills"
        links.mkdir(parents=True)
        # Model the 28-skill baseline before personal deselection.
        directories = {p.parent.name: p.parent for p in (repo / "skills").glob("*/*/SKILL.md")}
        for name in ACTIVE | PARKED:
            (links / name).symlink_to(directories[name], target_is_directory=True)
        outside = home / "unrelated-source"
        outside.mkdir()
        (outside / "SKILL.md").write_text("unrelated source\n")
        (links / "foreign-link").symlink_to(outside, target_is_directory=True)
        (links / "foreign-broken").symlink_to(home / "missing", target_is_directory=True)
        (links / "user-skill").mkdir()
        (links / "user-skill/SKILL.md").write_text("user content\n")
        lock = home / ".agents/.skill-lock.json"
        lock.write_text("unmanaged lock\n")

        def snapshot():
            return {p.name: ("link", str(p.readlink()), p.lstat().st_ino)
                    if p.is_symlink() else ("directory", content(p))
                    for p in links.iterdir()}

        env = dict(os.environ, HOME=str(home), XDG_CONFIG_HOME=str(home / ".config"),
                   XDG_CACHE_HOME=str(home / ".cache"), XDG_DATA_HOME=str(home / ".local/share"),
                   XDG_STATE_HOME=str(home / ".local/state"))
        command = ["chezmoi", "--source", str(dotfiles), "--destination", str(home),
                   "--config", str(home / "chezmoi.toml"),
                   "--cache", str(home / ".cache/chezmoi"),
                   "--persistent-state", str(home / "chezmoi-state.boltdb"),
                   "--no-tty", "apply", "--include=scripts"]

        def apply(*extra):
            result = subprocess.run(command + list(extra), env=env, cwd=home,
                                    capture_output=True, text=True)
            assert result.returncode == 0, result.stdout + result.stderr

        initial = snapshot()
        apply("--dry-run")
        assert snapshot() == initial, "dry-run changed discovery"
        apply()
        unrelated = {"foreign-link", "foreign-broken", "user-skill"}
        discovered = {p.name for p in links.iterdir()} - unrelated
        assert discovered == ACTIVE, f"wrong discovery: {discovered ^ ACTIVE}"
        for name in ACTIVE:
            assert (links / name).is_symlink()
            assert (links / name).resolve() == directories[name].resolve()
            assert (links / name / "SKILL.md").is_file()
        for name in PARKED:
            assert not (links / name).is_symlink(), f"parked link survived: {name}"
        for name in unrelated:
            assert snapshot()[name] == initial[name], f"unrelated skill changed: {name}"
        assert (outside / "SKILL.md").read_text() == "unrelated source\n"
        assert lock.read_text() == "unmanaged lock\n"
        assert content(repo / "skills") == before, "skill source content changed"
        first = snapshot()
        apply()
        assert snapshot() == first, "reconciliation was not idempotent"
        assert content(repo / "skills") == before
        # Public path-only contracts, independent of the consumer's internals.
        active = registry(repo, "enabled-skills.json", ACTIVE)
        parked = registry(repo, "parked-skills.json", PARKED)
        assert active.isdisjoint(parked), "registries overlap"
        assert len(active | parked) == 28
        # Parking is informational: even an empty active manifest selects none.
        (repo / "enabled-skills.json").write_text("[]\n")
        apply()
        assert set(snapshot()) == unrelated, "parked registry activated skills"
        assert content(repo / "skills") == before
        assert lock.read_text() == "unmanaged lock\n"
        print("PASS: 22 active, six parked, dry-run, owned-link pruning, unrelated "
              "preservation, source preservation, idempotence, and registry contracts")


if __name__ == "__main__":
    main()
