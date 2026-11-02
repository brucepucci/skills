# Repository instruction and plugin validation

Scope: [brucepucci/skills#22](https://github.com/brucepucci/skills/issues/22). Baseline: `098fe03b85571579c8743445d69733de4767f99f`. The root regular `CLAUDE.md` caused a strict-validation warning. Repository instructions now live in regular [`AGENTS.md`](../AGENTS.md), with [`.claude/CLAUDE.md`](../.claude/CLAUDE.md) importing that canonical file. No repository-policy skill or plugin context was added.

## Repeatable integration check

[`scripts/test-plugin-instructions.py`](../scripts/test-plugin-instructions.py) runs real external commands, following the existing standalone Python integration-check pattern. It requires Claude Code and Codex; Pi verification optionally uses an already-installed SDK, without adding a dependency.

Commands run successfully:

```sh
python3 scripts/test-plugin-instructions.py
python3 scripts/test-plugin-instructions.py --baseline 098fe03
python3 scripts/test-plugin-instructions.py --baseline 098fe03 --pi-sdk /opt/homebrew/Cellar/pi-coding-agent/1.4.0/libexec/lib/node_modules/@earendil-works/pi-coding-agent/dist/index.js
claude plugin validate . --strict
npm run check-plugin-version
git diff --check
git diff --exit-code HEAD -- .claude-plugin skills enabled-skills.json parked-skills.json
```

The SDK path above is specific to this machine. Omit `--pi-sdk` to run the Claude/Codex checks only, or supply your installed Pi SDK's `dist/index.js`. `--baseline` is optional and expects an original-layout ref, not a subsequent release with intentionally changed instructions or skills.

Environment: Claude Code **2.1.309**, Codex CLI **0.166.0**, Pi **1.4.0**, Node **v26.13.0**, Python **3.15.2**, macOS. Diagnostics use no model inference, paid API calls, or real credentials.

## Results at the agreed seams

| Seam | Observed result |
|------|-----------------|
| Original failure | Before the layout change, the new regression check failed on the exact root warning. The real validator exited 1. The final integration check repeated this against an untouched full `git archive` of the baseline, asserting both exit 1 and the specific warning. |
| Strict validation | The candidate full checkout passed `claude plugin validate . --strict`, exit 0, with the original root warning absent. The working checkout also passed. No override, suppression, validator change, or unrelated invalid metadata was used. |
| Claude project discovery | A fresh `claude -p /context --output-format stream-json --verbose --setting-sources project --strict-mcp-config` session reported both `.claude/CLAUDE.md` and `AGENTS.md` as nonempty project memory in its structured `context_usage.memory_files`. No explicit context-file startup flag was supplied. |
| Relative import control | In the disposable copy only, moved the payload to a non-autodiscovered `repository-policy-probe.md` and adjusted the relative import. A new session reported the nested entry and that file. This checks actual import loading independently of Claude's AGENTS fallback. Restored both files afterward. |
| Codex loading | `codex debug prompt-input` produced the model-visible prompt with the entire canonical payload present in user instructions. This was CLI inspection, not a model claiming it read the file. |
| Pi loading | The installed SDK's `DefaultResourceLoader` discovered exactly the regular canonical file with its complete content. A fresh in-memory `createAgentSession` included the complete payload in `session.systemPrompt`. Tools, extensions, skills, prompts, and themes were disabled for this context-only inspection; context discovery itself used the default loader without an override. |
| Plugin discovery | From a separate neutral consumer directory, started a fresh `/context` diagnostic with the supported `--plugin-dir <candidate>` surface. Runtime init identified the candidate plugin path, and both `skills` and `slash_commands` exposed exactly all 28 manifest-declared namespaced skills, with no additional plugin skills. Consumer `memory_files` was empty. |

The remaining missing-icon advisory is unchanged and explicitly does not affect the validator result. It is outside this issue's scope.

## Preservation, references, and isolation

- `AGENTS.md` exactly matches baseline `CLAUDE.md`: **4,206 bytes**, SHA-256 `49be3ee6ecd6122a75cd9db494a5b8f0eda3c2b472ddef184ac09d99834ad6b2`. It is a directly readable regular file; no root `CLAUDE.md` file or symlink remains. The nested entry contains only `@../AGENTS.md`.
- Compared both manifests and the entire `skills/` tree byte-for-byte against the baseline. All are unchanged, including invocation metadata. Active/parked selection files are unchanged. No skill behavior, router mapping, docs-page behavior, installation route, version, or finishing workflow changed.
- Audited repository occurrences of `CLAUDE.md` and Markdown instruction-file links. No live repository link needed retargeting: relative links in the canonical payload still resolve from the root. Generic guidance for other projects and historical changelog, ADR, and validation references retain their original meaning.
- Narrowed `.gitignore` only enough to track `.claude/CLAUDE.md`. `git check-ignore` still ignores `.claude/settings.local.json` and `.claude/skills/probe/SKILL.md`, while the new entry is not ignored.
- Each integration run uses full temporary repository copies and isolated HOME, XDG, Claude, and Codex directories, including a home path containing spaces. It inherits no credentials, custom endpoints, user config, or parent-agent markers. The optional Pi check uses its own agent directory and offline mode. A dummy API-key string enables local Claude diagnostics without keychain authentication; the script asserts zero API time.
- Baseline archives and import-control fixtures stay temporary. The script compares candidate contents before and after verification, and temporary homes, checkouts, and plugin state are removed on exit. Normal plugins, settings, instructions, discovery links, and external checkouts were not changed. No relinking was needed.

## Limitations and exploratory failures

- Plugin verification exercised supported session-local runtime discovery, not a marketplace install/update, remote marketplace resolution, or all plugin-consuming harnesses. The manifests and install routes were intentionally unchanged. Claude, Codex, and Pi instruction loading were observed; no model compliance claim follows from loading alone.
- Headless `/memory` returned “isn't available in this environment.” Used the supported structured `/context` diagnostic instead. An initial Codex probe failed because its scratch `CODEX_HOME` did not yet exist; creating the isolated directory fixed the probe. Exploratory Claude documentation requests returned HTTP 403; CLI help and actual diagnostics supplied the verification boundaries.
- There is no repository test or typecheck script in `package.json`; none was invented. The new standalone check is an integration regression at the agreed CLI/loading seams, not a general evaluation framework.
- No skill workflow, PR review, publication, merge, branch deletion, or issue closure was executed for testing. The selected issue's implementation handoff is a separately authorized tracker comment.
