# Branch naming and local creation validation

Scope: [brucepucci/skills#8](https://github.com/brucepucci/skills/issues/8). This change updates skill instructions, human docs, discovery summaries, and router guidance. No runtime naming module, tracker integration, dependency, or permanent test framework was added.

## Executed behavioral scenarios

Ran `python3 /tmp/skills-issue-8.Z4daYg/validate-branches.py`: **19/19 passed**, comprising 18 updated-skill cases and one unchanged-main baseline. Each invocation started a fresh context window, not a fork of this conversation, using Pi 1.4.0 with `openai-codex/gpt-6.1-sol`, reasoning `high`, and only `read,bash` tools. Discovered skills, extensions, MCP, context files, and prompt templates were disabled. Full supplied skill text was included in each prompt.

These are live, **bounded skill-invocation tests at branch handling**, not full implementation or publication runs. Prompts supplied already-fetched authoritative issue snapshots and settled preceding-phase decisions, except the deliberately unresolved case. Agents inspected and mutated real disposable Git repositories with local bare origins; hosting API calls and tracker writes were not exercised. Each run stopped after branch handling or a user-decision pause. No expected branch outcome was supplied to the agent.

The runner compared HEAD, every existing ref, index tree, tracked/untracked file bytes, and porcelain status before and after. Pause/reuse cases required unchanged refs and current branch. Creation cases required the expected purpose/identifier or explicit/conventional name, valid Git syntax, and preserved pre-existing refs and contents. Generated defaults were also checked against Conventional Branch grammar. The completed text and ordered tool traces were inspected for announcement before creation, appropriate explanations/questions, meaningful short slugs, and absence of destructive recovery.

| Case | Observed outcome |
| --- | --- |
| Unchanged `main` instructions, feature issue on `main` | Suggested `feat/issue-42-invoice-csv-export` but asked permission and left `main` unchanged, reproducing the old confirmation gate |
| Updated `implement`, feature issue on `main` | Announced and created `feat/issue-42-invoice-csv-export` without another approval |
| Ordinary fix on actual default `trunk` | Announced and created `fix/issue-42-invoice-rounding` |
| Verbose maintenance title beginning "To do: please" | Created `chore/issue-42-update-dev-dependencies`, dropping boilerplate |
| Urgent production credential fix | Created `hotfix/issue-42-api-credentials` |
| Release preparation | Created `release/issue-42-2.3.0`, including valid dotted version components |
| Representative configured non-GitHub key `PAY-317` | Created `fix/pay-317-invoice-rounding`, retaining the recognizable lowercase key |
| Explicit repository convention `feature/GH<number>-<short-description>` | Created `feature/GH42-invoice-csv-export`; repository convention overrode default lowercase/identifier formatting |
| Explicit safe name | Announced and created exactly `feature/invoice-export` |
| Suitable existing branch with different style | Reused `invoice-export-work` unchanged, without a cosmetic rename or permission round |
| Requested name colliding with an existing local branch | Explained the collision and asked whether to reuse the named branch; stayed on `main`, with no silent reuse or suffix |
| Requested name colliding with a remote-tracking ref | Explained the collision and offered a user choice of reuse or `feat/issue-42-invoice-csv-export`; no ref changed |
| Obviously unrelated current branch | Explained `fix/unrelated-login-timeout` mismatch, proposed `feat/issue-42-invoice-csv-export`, and asked permission; original branch preserved |
| In-progress operation | Synthetic `MERGE_HEAD` sentinel made Git report an unfinished merge; agent explained the obstacle and asked how to resolve it, with no branch/working-file change |
| Ambiguous ownership of an existing edit | Asked whether `notes.txt` belonged to the issue; no branch created and both tracked and untracked work preserved |
| Known unrelated edits/untracked file plus intended local commit ahead of origin | Created the feature branch at the unchanged current commit, carrying the files unchanged and leaving local `main` and its history intact |
| Unresolved CSV columns and testing seam | Reported validation blockers and requested decisions before branch creation; clean `main` unchanged |
| Direct `pr` on `main` | Suggested `feat/issue-42-invoice-csv-export` and asked permission before creation; refs unchanged |
| `pr` on suitable existing different-style branch | Reused `invoice-export-work` unchanged and stopped at the requested boundary |

Temporary artifacts live under `/tmp/skills-issue-8.Z4daYg`: runner, per-case prompt and skill snapshot, exact CLI command, JSONL tool events, spoken output, before/after snapshots, and results. They are local diagnostic artifacts, not published evidence or permanent repository tooling.

Validated instruction SHA-256 values:

- `skills/engineering/implement/SKILL.md`: `9c15f9d29a06dd9c56528980a60a5b6bda0fe427c5569083294519e0fdf73164`
- `skills/engineering/pr/SKILL.md`: `829acff6aa221768cc44af6b2ecb80fc28dae25e02ff3f2a1db829bb7e24b551`

## Repository verification

- `ruby /tmp/skills-issue-8.Z4daYg/check-metadata.rb`: **passed**. Checked changed-file em-dash prohibition and local reference targets, invocation metadata, affected docs' required section order and absolute links, exact 28-skill promoted plugin membership, discovery links/docs, automatic-versus-confirmed creation guidance, and preservation of the local-only boundary. Human comparison also checked naming precedence, mismatch pauses, and reuse guidance across skills, docs, READMEs, and router.
- `npm run check-plugin-version`: **passed**, version 1.3.2 remains synchronized. The patch changeset leaves versioning to the existing release workflow.
- `git diff --check` and `git diff --cached --check`: **passed**.
- `claude plugin validate . --strict`: **failed** on the existing root `CLAUDE.md` warning, because strict mode treats warnings as errors. It also emitted the existing missing-icon advisory. The same warning, advisory, and exit 1 were reproduced in an unchanged `main` archive at `/tmp/skills-issue-8.Z4daYg/baseline-plugin`; only checkout paths differed. Neither manifest was modified, and this unrelated baseline problem was left intact.
- Re-fetched issue #8 before committing. Its title, body, and update timestamp remained unchanged (`2026-11-02T12:53:21Z`); no spec edits were needed. The separate explicit implementation invocation satisfied the issue's prior implementation hold.

## Limitations and checks not run

- One live sample per fixture on one model/reasoning configuration is not a guarantee of future agent behavior. No full end-to-end issue fetching, implementation, handoff, publication, or cross-harness evaluation was run in these fixtures.
- The non-GitHub identifier used a supplied configured-tracker snapshot, not a live external tracker integration. The remote collision used a real remote-tracking ref, not a hosting-side race. In-progress-operation detection used a synthetic sentinel, not a real conflicted merge.
- No live remote collision race, Git operation race, permission failure, case-insensitive ref collision, conflicting ref-path fixture, multi-worktree obstacle, invalid explicit-name case, or explicitly misnamed requested-name case was exercised. Those safety paths were checked against the instructions only.
- No test or typecheck script exists in `package.json`; none was claimed as run. Code-level TDD is not applicable to this instruction-only change at the approved skill/Git-state seam; no runtime module was introduced to manufacture such a seam.
- Deployed docs and all external links were not checked. FAQ updates were grounded in issue #8, related repository issue titles, and relevant changelog entries; the optional local audience wiki and dictionary checkout were absent.
- No skill was added, removed, or renamed, so skill relinking was unnecessary and personal harness selection was untouched. No push, PR publication, review, merge, or issue closure was performed by this implementation.
