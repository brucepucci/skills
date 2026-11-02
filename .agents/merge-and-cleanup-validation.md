# merge-and-cleanup validation

Scope: [brucepucci/skills#10](https://github.com/brucepucci/skills/issues/10). This is a validation record, not an executable evaluation suite. The implementation is instructions plus existing Git and `gh` tools; no runtime code, dependencies, hooks, framework, or testing infrastructure was added.

## Scenario walkthroughs

All 18 acceptance scenarios were manually walked through against the finished instructions. Each row records the decision path and expected externally visible outcome, not a live agent execution or GitHub mutation.

| # | Input/condition walked through | Instruction path and outcome |
| --- | --- | --- |
| 1 | Supplied number, URL, omitted argument, ambiguous match, discovery error | SKILL step 1 resolves explicit input or the current branch's unique tracked-remote match only. Missing/ambiguous selection and failed discovery ask and stop rather than select another PR. |
| 2 | Fork checkout with CLI upstream inference | SKILL step 1 independently verifies base/source repository, host, fetch/push URLs, issue destinations, and explicit API/CLI selection. No distributing repository is hardcoded. |
| 3 | Current comprehensive trusted COMMENT assessment and green protections | PRE-MERGE accepts the opening recommendation, including Markdown emphasis, checks commit identity and all three axes, then permits SKILL step 3's head-pinned immediate squash without a second routine prompt. Native approval requirements remain independent. |
| 4 | Missing, stale, focused, incomplete, untrusted, or blocking assessment | PRE-MERGE enumerates shortcomings and asks for an explicit override for the shown PR/head. Declining/no answer leaves it unmerged. A native APPROVED event alone cannot fill missing assessment evidence. |
| 5 | New head, new blocker, changed requirements, or unrelated later discussion | PRE-MERGE and SKILL step 3 compare current evidence/requirements with the snapshot and invalidate affected approval/override. Latest eligible assessment wins, earlier blockers remain relevant, and unrelated discussion alone does not invalidate approval. |
| 6 | Pending/failed checks, conflict, draft, unknown/unmet protections, no squash, or required queue | PRE-MERGE stops without waiting, scheduling, bypassing, changing settings/methods, reviewing, or fixing. The immediate merge endpoint is pinned to the checked head. |
| 7 | Tracked/untracked dirt, operation underway, default branch ahead/divergent, or other-worktree obstacle | PRE-MERGE applies CLEANUP local safety before merging. Unsafe default checkout/update stops the merge without automatic stash/reset/rebase/discard. Local fixtures cover dirt, operation metadata, ahead/divergence, and worktree use. |
| 8 | Failed or timed-out merge response | SKILL step 3 reads actual remote PR/commit state before retry or cleanup. Unverified merge state preserves branches and blocks dependent issue completion. This path was walked through, not fault-injected against GitHub. |
| 9 | Squash merge exact-tip source versus additional commits | CLEANUP requires verified delivery and exact tip, then permits narrow local compare-and-delete despite failed ancestry deletion. Local fixtures exercised ordinary rejection, exact-tip deletion, and preservation of added local/remote commits. |
| 10 | Different tips, similarly prefixed branch, default/protected branch, another worktree | CLEANUP per-ref proofs preserve everything outside the selected source ref, with current protection/default/worktree checks. Local fixtures verify extra-tip rejection, unrelated-ref preservation, and worktree detection; GitHub protection policy was not live-tested. |
| 11 | User-owned fork versus another contributor's fork | CLEANUP remote authorization distinguishes authenticated ownership from merge access. Another contributor's ref requires separate human authorization; unknown ownership is preserved pending consultation. |
| 12 | Default named trunk; PR targeting release instead | CLEANUP resolves actual default and uses local-to-remote ancestry plus fast-forward-only update. SKILL announces release delivery without retargeting or claiming default delivery. The trunk/fast-forward mechanism was exercised locally; release-target disclosure was walked through. |
| 13 | Several issues: fully completed native relationship, explicit human authorization, incidental mention, spec-only link, partial slice | SKILL steps 2 and 5 decide each destination independently. Only fully complete, authorized issues receive concise linked comments and closure; no inference from mere mentions or the implementation. |
| 14 | Partial delivery plus native closing relationship | SKILL step 2 requires consultation before merge, with no silent relationship edits or reopening. Recovery surfaces an already-completed conflict instead of silently repairing it. |
| 15 | Auto-closed issue, no-op rerun, uncertain comment/close response | SKILL step 5 reads current state and all comments, skips equivalent comments/redundant closure, and inspects uncertain writes before retry. Comment length is one or two short sentences, not a verification report. |
| 16 | Already merged (including non-squash history) versus closed-unmerged PR | SKILL step 1 sends verified merged PRs directly to cleanup-only recovery without retrospective review gating. Closed-unmerged PRs stop. Missing merged-head evidence preserves refs. |
| 17 | Remote deletion denied after verified merge; default switch fails; uncertain ownership | SKILL step 6 and CLEANUP partial success continue only independent authorized safe steps. A failed switch blocks deleting the checked-out branch; uncertainty/authorization gaps require consultation. Exact partial state remains in the report. |
| 18 | Promotion and workflow boundaries | Metadata checks confirmed the 28-skill promoted plugin set, both invocation restrictions, discovery grouping, docs, router, changeset, and local links. Router guidance places explicit finishing after separately requested review. Existing publication/review workflows were not changed to invoke it. |

## Executed checks

- `python3 /tmp/skills-issue-10.MFXZ0N/git-fixtures.py`: passed all disposable local Git mechanism fixtures. Repositories and bare remotes were created with `TemporaryDirectory` and removed on completion. The script was temporary, not added to this repository.
  - Ordinary ancestry-based deletion rejects the squash-merged source; exact-tip `git update-ref -d REF EXPECTED_SHA` succeeds afterward.
  - An added local commit makes compare-and-delete fail, preserving its ref; a similarly prefixed unrelated branch remains unchanged.
  - Other-worktree branch use is visible through porcelain worktree metadata, and ordinary forced branch deletion rejects it. Atomic `update-ref` itself bypasses that protection, which is why the instructions explicitly require a separate worktree guard.
  - An added remote commit defeats an expected-tip deletion lease; an unchanged remote ref is deleted successfully through the guarded deletion refspec.
  - A behind branch updates by `--ff-only`, and a non-`main` default (`trunk`) finishes clean and equal to its verified remote tip.
  - Local-ahead and divergent histories fail the allowed local-to-remote ancestry predicate and remain preserved. A divergent `--ff-only` update fails without moving HEAD.
  - Tracked/untracked dirt is detected without stashing or discarding. An actual merge conflict exposes in-progress operation metadata; linked-worktree paths resolve without assuming `.git` is a directory.
- `ruby /tmp/skills-issue-10.MFXZ0N/check-metadata.rb`: passed. This temporary check parsed JSON/YAML and checked exact promoted plugin membership, discovery links and invocation groups, paired invocation metadata, docs presence, new-page section order and absolute-link syntax, router synchronization, minor changeset, changed-file em-dash prohibition, local skill reference targets, and both new harness symlinks.
- `npm run check-plugin-version`: passed; package and plugin versions remain 1.3.2. The minor changeset defers versioning to the existing release workflow.
- `git diff --check` and the staged equivalent `git diff --cached --check`: passed.
- `scripts/link-skills.sh`: passed; the new skill is linked into `~/.claude/skills` and `~/.agents/skills`.
- `claude plugin validate . --strict`: **failed** because the existing root `CLAUDE.md` warning is an error in strict mode. It also reports the existing missing-icon advisory, which the validator says does not change the directory-check result. The identical output/failure was reproduced in an unchanged `HEAD` archive under `/tmp/skills-issue-10.MFXZ0N/baseline`. Those unrelated baseline issues were not changed.

## Coverage limits and scope choices

- Instruction walkthroughs are not end-to-end agent compliance tests. Local fixtures establish Git mechanisms, not review interpretation, GitHub authorization behavior, API races, or issue completion behavior in a live run.
- No live GitHub merge, branch deletion, issue closure, PR publication, reviewer invocation, or destructive end-to-end test was performed. The implementation handoff comment on the selected issue is separate from testing the finishing skill.
- There is no test or typecheck script in this repository's package scripts; none was invented. TDD did not apply to this instruction-only implementation at the approved seams.
- Published docs links were checked for absolute syntax, not deployed-site availability. The new published route depends on later publication of the docs.
- The personal Pi `enabled-skills.json` selection remains unchanged: it is an explicit personal opt-in list, distinct from the promoted plugin set and required local harness links. No changes to the dotfiles repository or cached Pi snapshots were made.
- Strict plugin validation remains a known baseline failure, not a passed check or claim of fully verified completion.
