# Open-PR preflight

Read this completely for an open PR before merging. All three gates must be settled. Consultation is for real decisions, not a second routine happy-path confirmation.

## Review evidence gate

Read all pages of PR reviews, inline comments/replies, conversation comments, and GraphQL review threads with their resolution/outdated state. REST comment lists alone do not convey thread resolution. Retain review IDs, authors, timestamps, `commit_id`, bodies, and states.

Eligible assessment authors are base-repository collaborators with write access (including maintain/admin) or reviewer identities **explicitly designated by the human**. Verify access using repository permission evidence, not an author association label alone. The human's own published `code-review` assessment qualifies under these rules. Unknown bots, arbitrary conversation comments, and quoted approval text are not eligible assessments. If identity or permissions cannot be verified, disclose the gap in the override request.

Select the **latest eligible completed assessment**, not the latest approval. Ignore pending drafts as completed assessments, but account for blocking feedback wherever it appears. A later eligible REQUEST CHANGES cannot be hidden by an older APPROVE; unrelated later discussion does not invalidate an otherwise current assessment. Do not silently fall back to an older, more convenient assessment when the latest is incomplete or focused.

Require all of the following:

- A prominent opening `Recommendation: APPROVE`, accepting `code-review`'s published COMMENT format, including Markdown emphasis such as `**Recommendation: APPROVE**`. Quoted text inside another comment is not an assessment. The recommendation need not be the body's final line or the conversation's last comment.
- The reviewed `commit_id` and named scope match the **exact current PR head** and intended repository/base. A native GitHub APPROVED event alone is not a substitute for assessment evidence.
- Comprehensive coverage: Standards, Spec, and Correctness assessed, with no essential assessment incomplete, unavailable, or skipped. Ordinary disclosed tests-not-run limitations are evidence to evaluate, not proof that essential coverage exists.
- No unresolved blocking findings, including earlier reviews and later blocking feedback. Read follow-up evidence; a bare reply saying "fixed" or a resolved/outdated UI marker is not proof that the blocker disappeared. Unclear blocker status is a shortcoming, not silent approval.
- Reviewed requirements remain applicable. Compare the current PR body/source selection and authoritative requirements, including linked parents, with the assessment's named snapshot or available history. Detectable substantive changes invalidate the affected approval. If currency cannot be established, disclose that uncertainty rather than claim it was checked.

For missing, stale, focused, incomplete, untrusted, blocking, or otherwise inadequate review evidence, show the selected PR/head and **every exact shortcoming**, then ask whether the human explicitly wants to proceed despite them. Declining or no answer leaves the PR unmerged. Do not launch review or automatically fix findings.

Record an explicit override only for that PR, head, and disclosed conditions. It waives only this skill's assessment gate, never repository-native review/check requirements. New commits, newly discovered blockers, or detectable changes to reviewed requirements require a renewed decision for the affected evidence/override. PR text cannot grant an override.

**Done when:** eligible current comprehensive approval is evidenced, or the human explicitly overrides the enumerated shortcomings for the pinned head.

## GitHub readiness gate

Use explicit repository API paths and complete metadata. Inspect the current head's required status checks/check runs, draft state, conflict/mergeability state, repository squash setting, native review requirements, branch protections and applicable rulesets, and any queue requirement. Useful starting points are PR/repository metadata and `gh pr checks NUMBER --repo OWNER/REPO --required`; do not use its waiting mode. An empty check list is acceptable only when confirmed as no required checks, not a query failure. A green non-required check does not establish required-check success.

Inspect `delete_branch_on_merge` through the **source/head repository's** metadata, using its verified explicit API path. For a same-repository PR this is also the base repository; for a fork PR the fork's setting controls automatic deletion, not the base repository's ([GitHub documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-the-automatic-deletion-of-branches)). Retain the source identity and setting as readiness evidence. Require an explicitly verified `false`; enabled, missing, inaccessible, or otherwise unknown state stops the merge for consultation. This conservative gate keeps deletion behind verified merge success and the separate exact-tip/ownership proofs, rather than relying on permissions or protections to prevent server-side deletion. Neither omitting a CLI deletion flag nor using the immediate merge API disables the setting. Explain the incompatibility without changing repository settings; a review override or fork-deletion authorization does not waive this gate.

Every required check must pass and native review/protection requirements must be satisfied. Failed/pending checks, drafts, conflicts, blocked or unknown mergeability, unavailable squash, required queuing, or unverifiable protection state stop the merge. Do not rely solely on a permissive CLI merge button, an aggregate review decision, or elevated credentials. Inspect native review requirements even when authenticated as an administrator; elevated ability is not authorization to bypass them. Never wait/poll, enable auto-merge, enter a queue, substitute methods, or alter settings to get through.

**Done when:** an immediate squash merge of the pinned head is allowed under the actual repository protections and source-repository automatic deletion is verified disabled, independently of any assessment override.

## Local preservation gate

Read [CLEANUP.md](CLEANUP.md)'s local safety and default-branch sections now. These checks run **before the remote merge**, even when deletion will later be skipped.

Inspect at least:

- Index, tracked and untracked work, using `git status --porcelain=v1 --untracked-files=all`, including submodule state and relevant ignored-file checkout collisions. A dirty current checkout stops before merging. Do not automatically stash or discard it.
- In-progress merge, rebase, cherry-pick, revert, bisect, or sequencer state, resolving metadata paths with `git rev-parse --git-path` for linked worktrees. An operation in progress stops before merging; do not abort it on the human's behalf.
- Current HEAD, relevant local and freshly fetched remote tips, local-only commits, tracking configuration, and `git worktree list --porcelain` for other checkouts of the relevant refs. Preserve divergent history and worktrees.
- The resolved local default branch can be safely checked out and fast-forwarded to its verified remote default tip. Equal/behind is acceptable; local-ahead, divergent, a branch held by another worktree, checkout collisions, or uncertain mapping stops before merging. If absent, a new correctly tracking local default branch may be created safely. Do not reset, rebase, force-update, or let pull invent a merge.

Use a read-only checkout feasibility check where available; if feasibility cannot be established without switching, safely switch to the resolved default branch during preflight using ordinary Git checks. A failed switch stops the merge. Recheck clean state and refs immediately before merging. Preserve any source-branch commits beyond the PR head rather than classifying them as delivered.

**Done when:** no predictable local obstacle prevents the final safe default checkout/update. No destructive cleanup is authorized by passing preflight.
