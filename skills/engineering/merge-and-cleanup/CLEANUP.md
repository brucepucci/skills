# Verified-merge cleanup

Read completely before cleanup, and read the first two sections during open-PR local preflight. Cleanup applies only to the selected PR's exact source refs. Keep a per-action ledger; missing refs are no-ops and failures remain visible.

## Local safety

Inspect current status (index, tracked/untracked files, submodules), in-progress operations, current HEAD, relevant history, tracking configuration, and all worktrees. Check Git operation metadata through `git rev-parse --git-path`, not an assumed `.git` directory. Preserve dirty work, local-only commits, ignored files that obstruct checkout, and operations in progress. No automatic stash, reset, rebase, file discard, force checkout, or worktree removal.

On a new run, inability to safely finish on the default branch blocks merging before irreversible progress. During already-merged recovery or after a merge, unsafe local state pauses affected local actions; clearly independent authorized steps can still proceed. Never undo the merge.

## Finish on the actual default branch

Resolve the base repository's current default branch and its verified remote counterpart. Match fetch/push URLs to repository identity rather than assuming `origin` or `main`. Fetch without overwriting local branches; compare local default history with the fetched tip:

| State | Safe action |
| --- | --- |
| Equal | Switch normally if clean and not held by another worktree. |
| Strictly behind | Switch normally, then `git merge --ff-only VERIFIED_REMOTE_DEFAULT_SHA`. |
| No local default | Create it normally from the verified remote tip with correct tracking, if the name and worktree are available. |
| Ahead, divergent, obstructed, or uncertain | Preserve it and consult the human. No history repair is authorized. |

Check ancestry in the **local-to-remote** direction, for example `git merge-base --is-ancestor LOCAL_DEFAULT_SHA REMOTE_DEFAULT_SHA`; remote-to-local success would also admit local-ahead history and is insufficient. Check relevant branch use with `git worktree list --porcelain` before switching. Recheck cleanliness and refs before actions. When feasibility is uncertain in preflight, perform the safe ordinary switch then, before merging, rather than gambling on it afterward.

After the merge, fetch the default again, repeat the equal/behind-only test, and fast-forward safely. Verify checkout name, clean state, and HEAD equal the fetched verified default tip. Report that snapshot, not a promise the remote will remain unchanged. Do not use a pull that can silently merge/rebase. For a non-default-target PR, update the default anyway but disclose that it may not contain this PR's changes. Do not retarget or deliver to another branch.

## Per-ref deletion proof

Before **each** deletion, require verified GitHub merged state and the remote merge commit, recorded merged PR head SHA, exact candidate ref/repository identity, current tip, ownership/authorization, protection status, and worktree safety. Revalidate rather than relying on the earlier plan. For already-merged recovery, recover the recorded head from PR/merge evidence; if unavailable, preserve refs instead of inferring delivery from names or ancestry.

- Only the selected PR's source branch is a candidate. A matching local name alone is insufficient: verify its relationship to the source repository/ref. Never sweep other branches or similarly prefixed names.
- Preserve local and remote default branches and protected branches. Inspect source-repository default metadata and protection/ruleset evidence for the exact source ref, plus local repository policy where applicable. Unknown protection/ownership state is a reason to preserve, not delete. A non-default PR target is not itself a cleanup candidate.
- A candidate must point **exactly** to the recorded merged PR head. Different tips, including added local-only or remote commits, remain preserved even if Git calls them merged. Exact-tree similarity is insufficient. If refs changed since the plan, inspect and consult before changing scope.
- Preserve any local branch used by another worktree. Switch safely off a currently checked-out PR branch to the resolved default before deleting it. Do not remove another worktree to make deletion possible.
- Cross-repository remote deletion is authorized by invocation only when the fork is owned by the authenticated human. Another contributor's fork needs separate explicit human authorization for that exact repository/ref. Merge access or maintainer-edit permission alone is insufficient. Uncertain personal/organization ownership requires consultation.

### Local branch

After the default checkout/update and all per-ref proofs succeed, try ordinary branch deletion. Squash merging usually fails ordinary ancestry checks because the squash commit is not the PR head's descendant. Verified remote delivery **plus exact-tip and work-preservation evidence**, not ancestry alone, permits narrowly scoped forced local deletion of that source branch.

Recheck tip and worktree use immediately before a forced action. Prefer an atomic compare-and-delete to protect against concurrent ref changes:

```bash
git update-ref -d refs/heads/EXACT_SOURCE_BRANCH RECORDED_MERGED_HEAD_SHA
```

This is the narrowly scoped local forced-deletion fallback, not permission to reset work, force-push, or discard additional commits. `update-ref` bypasses branch-use protections, so explicitly prove it is not checked out in **any** worktree first. Ordinary `git branch -d` is usable only with the same safety proofs and a fresh tip check. If compare-and-delete fails, preserve the new ref and inspect before retrying. Remove only that branch's stale local tracking configuration after successful deletion, if necessary; preserve unrelated configuration.

### Remote branch

Resolve a push destination whose actual URL matches the **source** repository, not the base repository by convenience. Query the full remote ref and require its tip equals the merged head. Revalidate source default/protection/ownership checks. Use an exact expected-tip lease so a concurrent push is preserved:

```bash
git push --force-with-lease=refs/heads/EXACT_SOURCE_BRANCH:RECORDED_MERGED_HEAD_SHA \
  VERIFIED_SOURCE_REMOTE :refs/heads/EXACT_SOURCE_BRANCH
```

The lease is a compare-and-delete guard, not authorization to force-push new history. Never use a bare force or an unguarded remote delete. If the ref is absent, record already removed; if changed, preserve it. If the lease or permission check fails, inspect actual state before retrying and report any retained branch. Do not use a merge command's automatic branch-deletion flag because it bypasses this separate proof.

## Partial success

A failed remote deletion need not block independent safe local deletion, issue completion, or the default update. A failed default switch blocks deletion of the still-checked-out branch. Unknown merge state blocks **all** deletion and issue completion based on that merge. Scope/ownership ambiguity stops affected actions for consultation even when other work succeeded. Record remaining refs, failures, and exact checkout/update state; incomplete cleanup is not complete success.
