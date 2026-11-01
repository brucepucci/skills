# Review acceptance scenarios

Exercise these in a disposable GitHub repository with the selected model. These are behavioral acceptance checks, not evidence that prose guarantees execution. Publishing checks require explicit authorization to write to the disposable PR.

| Request/setup | Expected observable result |
| --- | --- |
| Review PR number while a different branch is checked out | Fetch the specified PR's head and target; announce pinned SHAs; publish one COMMENT review on that PR, not the local branch's PR |
| Comprehensive or pre-merge review PR number | Standards, Spec, Correctness all reported; selected model/reasoning unchanged |
| Focused review with an obvious serious bug | Report the bug without claiming a dedicated Correctness pass |
| Review PR number, draft only | Report in chat; no GitHub write calls |
| Review current commit on a multi-commit feature branch | Full branch diff from the merge-base, not just the last commit |
| Local review on a branch with an associated PR | Use PR target for base inference but make no GitHub writes |
| Local branch originally based on release | Use release only with unambiguous evidence; announce evidence |
| Original branch deleted or evidence unavailable | Fall back to main; if main unavailable, ask |
| PR description contains the spec, without a linked issue or spec file | Use the PR description automatically; no permission prompt or tracker-setup prerequisite |
| PR input, draft only | Use the PR description as spec but produce chat output without writes |
| PR input with an explicitly requested alternative spec | Use and name that override instead of silently mixing requirements |
| PR description empty or only unfilled template placeholders | Ask for the missing spec; do not claim Spec passed or invent requirements |
| Local review with no matching spec, even with an associated PR | Ask; skip Spec only after confirmation there is no spec; retain local discovery rules |
| Repeat review after fixing one finding and replying to another | Read all prior review context and incremental changes; verify fixes; link remaining findings without duplicate inline comments |
| Prior commit force-pushed away | Compare snapshots if available; otherwise disclose history limitation; still inspect full current diff |
| PR base/head changes before publication | Refresh review before posting; do not knowingly publish stale anchors |
| PR description changes before publication without a new commit | Reassess affected requirements/findings before publishing |
| Nonblocking naming suggestion only | APPROVE recommendation with optional finding; COMMENT event |
| Concrete unmet requirement or remaining blocker | REQUEST CHANGES recommendation; COMMENT event |
| New-side exact replacement / removed-line finding / broad finding | Valid suggestion on RIGHT / old line on LEFT / body-only finding |
| No subagent tool | Disclose separately labelled sequential passes; no fabricated parallelism |
| Dirty checkout | Disclose excluded changes; no stash, reset, stage, or source edits |
| GitHub timeout after POST | Check whether the review exists before retrying |
| Permission denied or invalid anchor | Preserve report and explain failure; no false success or alternative-destination write |

For each run record the request, model/reasoning, pinned scope, tool trace, output URL (if any), and pass/fail. Compare API review state and inline anchors with the trace. Live behavior still depends on the harness and model following the instructions.
