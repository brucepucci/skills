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

## PR #11 requested-change walkthroughs

Addressed [the blocking automatic-deletion finding](https://github.com/brucepucci/skills/pull/11#discussion_r4438544501) within issue #10's existing verify-before-delete, exact-tip, and fork-authorization requirements. No authoritative requirements changed. [GitHub's documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-the-automatic-deletion-of-branches) confirms that fork PRs use the head repository's setting and automatic deletion requires the merger to have write access there.

The following paths were manually walked through against PRE-MERGE's readiness gate and SKILL step 3. These are instruction-level checks, not automated behavioral tests or live GitHub execution.

| Condition | Decision path and externally visible outcome |
| --- | --- |
| Same repository; automatic deletion verified `false` | Readiness records the explicit source identity/setting. The gate passes; all other review/readiness/local requirements still apply, followed by verified merge and separate cleanup proofs. |
| Same repository; automatic deletion enabled | Readiness stops before merging and explains that server-side deletion would bypass the cleanup gate. Omitting a deletion flag or using the immediate API is not treated as disabling the setting. No settings change occurs. |
| Base disabled; contributor's fork enabled; merger has fork write access but no separate deletion authorization | The explicit head-repository lookup finds the fork's enabled setting and stops before merging. Base metadata, merge permission, and a review override cannot authorize the automatic deletion. Separate fork-deletion authorization would still not waive verified-merge/exact-tip sequencing. |
| Base enabled; source fork disabled | The source fork's verified `false`, not the base setting, settles this gate. Other preflight requirements remain binding; cleanup still checks exact tips and fork-deletion authorization separately. |
| Source setting enabled but merger lacks fork write access | The conservative gate still stops and explains the incompatible setting rather than relying on permission state to prevent automatic deletion. |
| Source metadata inaccessible, missing the setting, or otherwise unknown | Failed discovery never becomes `false`. Readiness stops for consultation without merging or changing settings. |
| Setting changes from disabled to enabled, or becomes unverifiable, after initial preflight | SKILL step 3 explicitly re-fetches and reapplies the source setting gate immediately before mutation. The merge stops despite the earlier passing snapshot. A changed source identity also stops for a refreshed plan. |
| Already-merged PR, including one with an already-removed source branch | SKILL step 1 still enters verified cleanup-only recovery without a new merge or retroactive preflight. Missing refs are already-clean outcomes; remaining refs still need CLEANUP's independent safety proofs. |

Router guidance was re-read and remains accurate: this fix changes a readiness safeguard, not the skill's role or invocation boundary. Human docs now explain the stop and the fork/base distinction. Git mechanism instructions and invocation/distribution metadata are unchanged.

### Checks executed for the requested change

- `npm run check-plugin-version`: passed (1.3.2).
- `ruby /tmp/skills-pr-11-fix.93nKBD/check-metadata.rb`: passed repository JSON/YAML, exact 28-skill promoted plugin set, paired invocation, discovery/docs, router/changeset, prose, and local reference checks. This is a temporary check, not new repository infrastructure.
- The first metadata run additionally asserted external harness symlinks and failed because `~/.agents/skills/merge-and-cleanup` is absent; the Claude link exists. The rerun excludes external installation assertions. No skill was added/renamed/removed in this revision, so `scripts/link-skills.sh` was not rerun and personal harness state was left unchanged. The earlier implementation's linking evidence above is historical, not a claim that both links still exist.
- `git diff --check` and `git diff 753c84fda08650fef86e0b3150af0c0dc3b674f5 --check`: passed.
- `claude plugin validate . --strict`: failed on the existing root `CLAUDE.md` warning, with the existing missing-icon advisory. Reproduced the same failure by running the command in an unchanged `30e11403ebd82d2f22cfdd3ef7ecf34185b6370e` archive at `/tmp/skills-pr-11-fix.93nKBD/baseline`.
- Re-fetched authoritative issue #10 before committing; its requirements and update timestamp were unchanged. No spec edit was needed.
- Git mechanism fixtures were not rerun because their instructions did not change. No live merge/deletion, repository-setting mutation, end-to-end agent evaluation, deployed-docs check, or PR review was run. No test/typecheck script exists; TDD does not apply to this instruction-only change at the approved seams. Repository settings can still change after the immediate read; this is not an atomic GitHub settings/merge transaction.

## PR #11 squash-message closure follow-up

Addressed [Correctness C1 and its matching spec blocker](https://github.com/brucepucci/skills/pull/11#discussion_r4438670829) within issue #10's existing individually authorized/full-delivery issue rules. No authoritative requirements changed. The new `SQUASH-MESSAGE.md` reference owns prospective text resolution, closure reconciliation, and binding the inspected strings to the merge request. SKILL steps 2 and 3 require it before mutation, and recovery examines the actual message instead.

### Before/after instruction trace

Before the edit, a two-commit PR titled `Fixes #123`, with an empty native closing list and a body declaring partial delivery of #123, could pass step 2's relationship check. Step 3 omitted both squash text fields, permitting GitHub's configured default to include the closing title. This reproduces the review's missing instruction gate, not a live issue closure.

After the edit, step 2 loads the full squash-message reference, reads the base settings and complete PR/commit inputs, obtains GitHub's squash preview, and reconciles every possible closing destination with the issue ledger. The example now stops before mutation for consultation. The merge request explicitly carries the inspected title/body, rather than regenerating them from uninspected defaults. No keyword is silently removed and no review override authorizes partial closure.

The following 13 paths were manually walked through against the edited instructions. These are decision-path checks, not automated behavioral tests or end-to-end agent execution.

| Condition | Decision path and externally visible outcome |
| --- | --- |
| Two commits, title-only `Fixes #123`, empty native closing list, partial delivery | The prospective title enters closure reconciliation independently of native relationships. The partial issue blocks merging; the user sees the exact text and destination. |
| Single-commit defaults inherit a closing subject or body absent from the PR description | Full commit subject/body and the squash preview are required. A commit keyword alone supplies no closure authorization; partial or unauthorized closure stops. |
| Multi-commit `COMMIT_MESSAGES` body contains a closing reference only in commit details | Complete ordered subjects/bodies and count are checked, not only summaries or the first API page. Any closing reference that survives into the prospective body enters the ledger. |
| `PR_BODY` configuration copies a description keyword absent from native discovery | The actual prospective body is inspected independently. An empty native list cannot hide a copied closing reference or authorize it. |
| Fully delivered commit-only issue, first without and then with explicit human authorization | Without authorization, merging pauses despite complete delivery. With explicit authorization and verified full scope, unchanged text may pass; all other gates still apply and there is no extra routine confirmation. |
| Several destinations, including a cross-repository issue, with only one partial/unauthorized issue | Bare numbers resolve against the base, not the source fork. Each destination is fetched independently; one conflicting automatic closure blocks the merge, not merely that issue's later close command. |
| Uppercase/colon variants, multiple keywords, full URLs, quoted text, or uncertain syntax | The complete title/body is checked for all supported forms; quoting is not assumed inert. Unknown syntax/destinations pause rather than disappearing from the ledger. |
| PR title/body, settings, preview, default branch, or issue evidence changes at the same head | The immediate recheck includes those inputs, not just the head SHA. Changed effects are reassessed; conflicts need consultation. Both explicit text fields bind the request to the inspected strings. |
| Missing settings, inaccessible preview, inconsistent inputs, truncated commits, or API limits | Text resolution stops before mutation. No fallback to unchecked generation or a silently shortened message is allowed. |
| Configured empty body, multiline body, or shell-looking literal text | Both fields are supplied explicitly, including an empty body. Quoted fields or serialized JSON preserve data without executing it; inability to preserve exact content stops. This serialization path was walked through, not tested against a live merge. |
| Non-default target with a closing reference for partial work | The skill discloses deferred keyword effects and resolves the future closure conflict before merging. It neither retargets nor claims default-branch delivery. |
| Unexpected actual merge text/closure, including already-merged recovery | The remote full message and issue states are reconciled. A conflict pauses affected issue actions for consultation without automatic reopening, another merge, or a retroactive review gate. |
| Safe message with no closing references and an otherwise eligible PR | The text is shown in the announced plan and passed explicitly, preserving the normal happy path. Review, protections, automatic-deletion, local preservation, and exact-tip cleanup gates remain independently binding. |

All 18 original acceptance paths and the eight automatic-deletion follow-up paths were rechecked against the edited instructions. Their gates remain in place; issue scenarios 13 and 14 now also cover squash-message references, and recovery scenario 16 uses actual message evidence. Router guidance was re-read and remains accurate: this is a closure safeguard, not a new role or invocation boundary. Human docs answer the observed title/commit-message question. The existing minor changeset still covers this unreleased feature; discovery, manifests, and invocation metadata did not change.

### Evidence and checks executed

- Read GitHub's current primary documentation for squash defaults, commit-keyword issue closure, and the immediate merge endpoint. The defaults depend on repository settings and commit count; commit-message closure need not create a native PR link. The endpoint accepts explicit `commit_title` and `commit_message`.
- Read-only `gh api graphql` schema inspection confirmed `PullRequest.viewerMergeHeadlineText` and `viewerMergeBodyText` accept `mergeType`. A read-only query of PR #11 with `mergeType: SQUASH` returned its exact current headline (including `(#11)`) and commit-derived multiline body at head `9aae6852a0b4083b0b262ec33a4ec2a9c043a576`. No merge was attempted. Evidence: `/tmp/skills-pr11-squash.x8pOvA/squash-preview.json`.
- `python3 /tmp/skills-pr11-comprehensive.vG75NH/git-mechanisms.py`: passed disposable Git/bare-remote fixtures for squash ancestry rejection, guarded local deletion, unrelated refs, stale-tip local/remote preservation, successful exact leased deletion, worktree protection, non-main fast-forward, ahead/divergent history, and dirty tracked/untracked detection. These unchanged mechanisms are not a test of GitHub closure semantics.
- `npm run check-plugin-version`: passed (1.3.2).
- `ruby /tmp/skills-pr-11-fix.93nKBD/check-metadata.rb`: passed repository JSON/YAML, exact 28-skill promoted plugin set, paired invocation, discovery/docs/router/changeset, changed tracked-file prose, and local references. The new reference is included in local-reference inspection.
- `python3 /tmp/skills-pr11-squash.x8pOvA/check-prose.py`: passed the em-dash guard across all 13 branch-changed or untracked files and confirmed strict-validator output matches the unchanged base after normalizing root paths.
- `git diff --check` and `git diff 753c84fda08650fef86e0b3150af0c0dc3b674f5 --check`: passed.
- `claude plugin validate . --strict`: failed on the existing root `CLAUDE.md` warning and reports the existing missing-icon advisory. Reproduced on an unchanged base `753c84fda08650fef86e0b3150af0c0dc3b674f5` archive at `/tmp/skills-pr11-squash.x8pOvA/baseline`; outputs differ only in paths. This is not a new validation failure.
- Re-fetched authoritative issue #10 before committing and compared its full body, title, URL, and update metadata with the initial snapshot: unchanged. No spec edit was needed.
- No new framework, dependency, repository test infrastructure, live merge/deletion/closure, settings mutation, deployed-docs check, PR publication/update, or PR review was performed. No test/typecheck script exists, and TDD does not apply at the approved instruction-only seams. No skill was added/renamed/removed, so harness relinking was not rerun. Preview/input reads and merge are not atomic with concurrent PR/issue/settings edits; explicit fields pin text but not all GitHub lifecycle state.

## Coverage limits and scope choices

- Instruction walkthroughs are not end-to-end agent compliance tests. Local fixtures establish Git mechanisms, not review interpretation, GitHub authorization behavior, API races, or issue completion behavior in a live run.
- No live GitHub merge, branch deletion, issue closure, PR publication, reviewer invocation, or destructive end-to-end test was performed. The implementation handoff comment on the selected issue is separate from testing the finishing skill.
- There is no test or typecheck script in this repository's package scripts; none was invented. TDD did not apply to this instruction-only implementation at the approved seams.
- Published docs links were checked for absolute syntax, not deployed-site availability. The new published route depends on later publication of the docs.
- The personal Pi `enabled-skills.json` selection remains unchanged: it is an explicit personal opt-in list, distinct from the promoted plugin set and required local harness links. No changes to the dotfiles repository or cached Pi snapshots were made.
- Strict plugin validation remains a known baseline failure, not a passed check or claim of fully verified completion.
