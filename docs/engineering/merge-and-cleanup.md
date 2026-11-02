## What it does

`merge-and-cleanup` finishes one selected GitHub pull request: squash merge, verified source-branch cleanup, completion of fully delivered issues, and a safe update of the actual default branch.

It is a separately invoked finishing step. Publishing a PR or receiving an approval recommendation never starts it automatically. Its defining constraint is **verified delivery before deletion**: squash history alone cannot prove that a local branch is safe to remove.

## When to reach for it

You invoke this by typing `/merge-and-cleanup`, and the [agent](https://www.aihero.dev/ai-coding-dictionary/agent) won't reach for it on its own.

| Your situation | What to choose |
| --- | --- |
| A reviewed PR is ready to finish | `/merge-and-cleanup <PR number or URL>` |
| The current branch has exactly one PR identifiable through its tracked remote | `/merge-and-cleanup` without an argument |
| A merge succeeded but cleanup was interrupted | Invoke it again for that merged PR; it resumes cleanup without merging again |
| Local work still needs publishing | [pr](https://aihero.dev/skills-pr) |
| You want an assessment rather than a merge | [code-review](https://aihero.dev/skills-code-review), requested separately in comprehensive mode |

## Prerequisites

A Git checkout, authenticated GitHub CLI (`gh`), and permission for the requested operations. The first version supports GitHub only. Repository, source fork, target branch, default branch, and issue destinations are resolved explicitly rather than inherited from CLI defaults.

## Verified delivery, bounded cleanup

Invocation authorizes the resolved safe happy path, including completion comments and closure of clearly identified, fully delivered implementation issues, without another routine confirmation. An authoritative PR Spec selection can identify the issue without native closing links. Applicable comprehensive approval covering the issue's complete, current requirements is sufficient delivery evidence; closeout consumes that assessment rather than reviewing the implementation again.

The latest eligible completed assessment must recommend approval for the exact current head, cover Standards, Spec, and Correctness, and leave no unresolved blockers. Assessment authors need repository write access or your explicit designation. A `code-review` Comment review qualifies; a native approval alone is insufficient evidence.

| Condition | Outcome |
| --- | --- |
| Missing, stale, focused, incomplete, untrusted, or blocking assessment | You see the exact shortcomings and choose whether to override them for the shown head |
| Failed or pending required checks, conflicts, drafts, or unmet protections | Stops without bypassing protections, waiting, scheduling auto-merge, or substituting a merge method |
| Source repository's automatic head-branch deletion is enabled or cannot be verified disabled | Stops before merging without changing settings, so deletion stays behind the verified-delivery safeguards |
| Dirty checkout, in-progress operation, or unsafe default-branch update | Stops before merging and preserves your work |
| Source branch has extra commits, is protected/default, or is used by another worktree | Preserves that branch and reports incomplete cleanup |
| Another contributor owns the source fork | Asks for separate remote-deletion authorization |
| Identified implementation issue has applicable full-scope approval | Completes it after verified merge without another routine confirmation, including a Spec-only relationship |
| Identified implementation issue has partial, uncertain, or stale delivery evidence | Consults before any merge, even without automatic closing references; explicit partial delivery leaves it open |
| Incidental mention, background source, or parent/umbrella context | Receives no completion action merely because it is referenced; conflicting native or squash-message closing effects require consultation |

A review override does not waive GitHub checks or protections, establish full issue delivery, or authorize issue completion. Issue outcomes are resolved explicitly in the same consultation where possible. New commits, newly discovered blockers, or detectable changes to reviewed requirements require a new decision. The skill never launches review or fixes findings for you.

## Common questions

**Does the implementation issue need a closing keyword or another confirmation?**

No. A clearly identified implementation issue selected in the authoritative PR Spec qualifies without native closing syntax. Applicable full-scope comprehensive approval establishes delivery, and invocation authorizes its completion after the merge is verified. Each implementation issue needs its own applicable scope evidence.

**Do testing limitations or follow-up issues prevent completion?**

- Disclosed bounded validation, tests not run, and unrelated baseline failures do not by themselves negate otherwise applicable comprehensive approval. Closeout does not repeat the review.
- Deferred requirements remain unfinished unless you explicitly agree to change the authoritative requirements. Opening follow-up issues alone does not make the original issue complete. Partial or unclear delivery prompts consultation before merging.

**Will a squash merge erase commits that exist only on my local branch?**

Cleanup requires the branch tip to equal the recorded merged PR head exactly. Extra local or remote commits stay preserved. An exact-tip branch can be deleted after verified delivery even when Git's ordinary ancestry check rejects deletion after a squash merge.

**Why does GitHub's automatic branch deletion block this workflow?**

It can remove the source branch during merging, before verified delivery and exact-tip/ownership checks. The skill requires automatic deletion to be verified disabled both during preflight and immediately before merging. For a fork PR, the fork's setting matters, not the base repository's. It never changes that setting for you.

**Can a PR title or commit message close an issue that is meant to stay open?**

Yes. GitHub can put closing keywords from those inputs into the squash commit even when the PR has no native closing links. The skill inspects the exact squash title/body and their configured inputs, checks each closing destination against the issue plan, and sends that inspected text explicitly when merging. Partial or unauthorized closure stops for your decision; it never silently removes keywords to get through.

**What happens when the merge works but cleanup fails?**

The merge remains intact. Independent safe, already-authorized steps can finish, and the report lists what failed or remains. A rerun checks actual state and existing issue comments before retrying, rather than merging again or duplicating completion comments. Recovery reuses applicable approval at the recorded merged head, not a new post-merge commit. Unclear issue delivery pauses affected comments and closures for consultation while safe branch cleanup can continue.

## It's working if

- Before mutation, you see the exact PR, source fork/branch, target, head, default branch, and intended issue outcomes.
- A review shortcoming produces an explicit override decision rather than a surprise merge or an automatic reviewer.
- Additional commits and other worktrees remain untouched, even when cleanup cannot finish.
- Before merging, you see the squash title/body and any closing-reference conflict, including one found only in the title or source commit text.
- A fully delivered Spec-selected implementation issue gets one short completion comment linking the PR and merge commit, then closure without routine reauthorization; incidental mentions receive no completion action.
- Unclear or partial implementation-issue delivery prompts consultation before merging, even when no keyword would close it automatically.
- The final report names retained branches and failures, and shows the actual checkout/update state. A non-default target is never presented as default-branch delivery.

## Where it fits

This is the finishing **chain step** after [pr](https://aihero.dev/skills-pr) publishes and a separately requested [code-review](https://aihero.dev/skills-code-review) assesses the result. Neither invokes it. You choose when to merge, and an already-merged PR can use it solely for recovery.

[ask-matt](https://aihero.dev/skills-ask-matt) maps the whole flow and its human decision points.
