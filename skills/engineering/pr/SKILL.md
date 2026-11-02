---
name: pr
description: "Publish prepared changes, create/update a PR, and reply to demonstrably addressed review feedback. Use for publication or PR-update requests; explicit preview, body-only, or local-only requests retain their limits. Fixing review findings alone is not publication authorization."
metadata:
  credits:
    skill: show-me
    author: Dex Horthy
    organisation: Humanlayer
    url: "https://github.com/humanlayer/skills/blob/main/plugins/show-me/skills/show-me/SKILL.md"
---

Publish prepared work against the **authoritative spec**, then stop at a manual review handoff. An unqualified `/pr` invocation authorizes the full publication workflow, not merely proposed text. Honor explicit limits:

| Request | Authority |
| --- | --- |
| `/pr` or a publication/update request | Verify, commit intended changes if needed, publish, and finish PR updates/replies below |
| Body-only or preview | Resolve scope/requirements, read [BODY.md](BODY.md), return text with honest evidence; no branch/history changes or remote writes |
| Local-only | Stay local and honor the stated local mutation limits; clarify any unclear permission before mutation |

Ordinary implementation, a request to fix findings, and discovery of an open PR grant no publication authority. This skill consumes prepared fixes; it reads feedback for publication context, not to start another implementation or review-fix loop. Review, approval, thread resolution, and merge remain separately authorized. It does not require `to-spec` or automatically create an issue. Use the user's domain language from `GLOSSARY.md` where available.

## 1. Resolve destination and inspect scope

Inspect repository instructions, working tree (including staged and untracked changes), current branch, remotes, default branch, and history. Explicitly resolve the intended publication repository and push remote; never assume the skills distribution repository or trust GitHub CLI's fork/upstream inference. Verify the destination and use explicit `--repo OWNER/REPO` or API paths on GitHub operations.

Look for the current branch's open PR in that destination, matching its head repository/owner and branch, before creating one. Reuse it when unambiguous. For an existing PR, use its target branch as the base; for a new one, normally use the intended repository's default branch. Clarify ambiguous repository, remote, base, or PR selection and unexpected closed/merged state. Network/authentication errors are not evidence that no PR exists.

For an existing PR, read [FOLLOW-UP.md](FOLLOW-UP.md) now: snapshot the description and published head, read the complete review conversation, and retain a recovery record before mutation. Follow its gates for description preservation, feedback dispositions, post-publication replies, and retries.

Fetch the relevant remote refs without overwriting local branches. Inspect the full commit list and complete branch diff against the selected base, as well as uncommitted changes. Check the merge-base and detect truncated output. A clean working tree does not mean the branch contains only intended work. Announce repository, remote, branch, base, existing PR if any, and intended scope. Pause for unrelated existing commits or ambiguous ownership; preserve unrelated work rather than silently including or discarding it.

## 2. Confirm a feature branch

On `main` or the repository's default branch, warn and pause before committing or creating a branch. Suggest a name using the guidance below; let the user accept or replace it and obtain explicit confirmation before creation. Unlike `implement`, a publication request does not authorize automatic branch creation. Reuse and announce a suitable existing feature branch, even if its naming style differs; this is not a routine branch-renaming filter.

When a new suggestion is needed, honor an explicitly requested name; otherwise follow an established target-repository convention from instructions or consistent branch history, not one stray name. Without one, use purpose-based [Conventional Branch](https://conventionalbranch.org/) naming:

- Prefer `feat/`, `fix/`, or `chore/`; reserve `hotfix/` for urgent fixes and `release/` for release preparation. Default to the work's purpose, not an agent/vendor prefix.
- For a fetched GitHub issue, use `<type>/issue-<number>-<very-short-description>`, such as `feat/issue-8-branch-names`. For another configured tracker, retain its recognizable, lowercase-normalized issue key instead of `issue-<number>`; no new integration is needed. For inline requirements without an issue, omit the identifier rather than invent one.
- Derive very few meaningful words from the fetched issue's intended change (or agreed inline requirements). Drop title boilerplate such as "To do" instead of mechanically slugifying the title; no rigid word count is needed. If the issue is not fetched yet, fetch it before deriving a suggestion.
- Generated defaults use lowercase alphanumerics and single hyphens, with one slash after the type. Dots may separate alphanumeric version components, never adjacent to a hyphen or another dot; descriptions start and end alphanumerically. Validate any new name with `git check-ref-format --branch` as well as the applicable naming convention.

Before creation, check for collisions with existing local and remote branches, including conflicting ref paths. A collision, obviously misnamed current or requested branch, ambiguous choice, invalid requested name, or unsafe state requires an explanation, a suitable proposed name or safe next step, and a pause for the user's decision. An explicit name does not waive these gates. Never silently rename, switch to a colliding branch, or append an arbitrary suffix.

Preserve intended local commits and uncommitted work on the confirmed feature branch. Never automatically stash, reset, force a switch, blindly stage all changes, discard unrelated work, amend existing commits, force-push, or rewrite remote default-branch history.

### Optional local-main cleanup

Only after work is safely preserved, offer cleanup if local main/default-branch history needs restoring. Publishing is not permission to reset main. Fetch and verify its corresponding remote-tracking tip; propose that exact tip, not an assumed last merge. Show the local ref, current SHA, proposed SHA, commits that would leave the ref, and how all work is preserved. Obtain **separate explicit confirmation** before moving the local ref. Leave main untouched if the target, preservation, or ownership is uncertain. Do not reset the user's working tree or alter remote main.

## 3. Establish the authoritative spec

Prefer explicitly agreed requirements. Fetch a supplied issue through the configured tracker workflow, including necessary linked parent requirements. If tracker configuration is needed but absent, tell the user to run `/setup-matt-pocock-skills`; a self-contained inline spec needs no tracker setup. Manually authored issues qualify.

- **Issue-backed:** the PR's Spec section links the authoritative issue rather than copying its requirements. Keep requirements in that issue.
- **No suitable issue:** include approved inline requirements. Reconstruct missing requirements from the agreed conversation, not the implementation, and ask for approval before publication. If the conversation lacks sufficient intent, ask rather than infer it from code.
- **Already agreed spec:** faithful formatting needs no extra approval. Substantive changes always do.
- **Partial issue implementation:** explicitly state the agreed slice and deferred requirements in the description alongside the issue link. Obtain agreement on that scope rather than deriving it from the diff.

Keep detail proportional: intended behavior and verifiable acceptance criteria, with constraints and exclusions as applicable. An implementation sketch is supporting context, not requirements. The reviewer must be able to recover intent from published artifacts without this conversation.

Compare the full intended delivery with the spec. If they differ, pause for a choice: correct the implementation or approve a substantive requirement change. Never rewrite intent merely to make code pass. Before editing issue-backed requirements, obtain approval, then update the authoritative issue itself. If that is unavailable, pause and agree on an explicit alternative; do not introduce a competing PR-only override. Requirements conflicts block publication. Record approved changes in the PR update history without duplicating the spec.

## 4. Prepare and verify the candidate tree

Select the exact intended files and hunks before verification. Assemble the **candidate tree** from the confirmed HEAD plus those changes, excluding unrelated staged, unstaged, and untracked work. Preserve the user's working files and unrelated staging; use a temporary index/snapshot when needed rather than stashing or resetting their checkout. Record the starting HEAD and candidate Git tree OID. Existing local commits do not waive this gate; with no new changes, the candidate is HEAD's tree.

Discover the repository's applicable required verification, including tests and typechecking where provided. Run its actual commands in an isolated materialization of the candidate tree, not the mixed working tree. Use repository-prescribed setup for dependencies, generated files, and required Git metadata/submodules; do not copy excluded source edits or local build artifacts into the verification environment. If faithful isolation or required setup is unavailable, treat verification as unavailable under the gate below. Record the candidate tree OID, commands, results, failures, unavailable checks, and checks not run in Evidence.

Confirm checks did not alter the candidate's source inputs. Changed candidate contents, newly selected changes, or a changed starting HEAD invalidate the results: prepare the candidate again and rerun required verification. Dispose only of temporary resources owned by this run.

Required verification failure or unavailability stops normal committing, pushing, and publication. The user may **explicitly authorize a draft exception**; record that authorization and all failed, unavailable, or unperformed required checks in Evidence. Never silently convert failure to a draft or claim readiness. Successful verification normally produces a ready-for-review PR.

Use before/after evidence only when it actually exists. Missing baseline output, screenshots, or failing test runs must be disclosed, never reconstructed as if executed.

## 5. Prepare the description and commit the candidate

Read [BODY.md](BODY.md) for section format and optional visual guidance. Newly prepared descriptions use **Spec**, optional **Implementation**, **Evidence**, and **Merge Danger** in that order. Respect repository-required content while making these sections discoverable.

For an existing PR, prepare the preserved-content description and overall update against the saved published snapshot using FOLLOW-UP.md. Re-fetch authoritative requirements, including necessary parent sources, before publication; changed intent or conflicting description edits require reconciliation with the user, not a silent overwrite.

Inspect the final working tree and full branch diff again. Confirm the starting HEAD, candidate tree, and verification status (including any authorized draft exception) still match the recorded snapshot, then commit only that candidate on the confirmed feature branch after the verification gate. Preserve unrelated work and staging; do not newly select files or hunks after checks. Verify the resulting commit's tree OID (`git rev-parse HEAD^{tree}`) equals the verified candidate OID; a mismatch blocks normal publication and requires preparing/verifying the actual candidate again. Reuse intended existing commits rather than amending them or creating an empty commit. Check that the prepared description accurately represents the whole delivery, not only the latest edits.

## 6. Publish or update once

Reconfirm repository, remote, branch, base, and PR state before pushing. Unexpected destination/head/base changes require reconciliation, not a blind push. Pin the exact commit to push and confirm its tree OID matches the verified candidate; a later candidate change invalidates verification and returns to step 4.

An authorized draft exception requires converting an existing PR to draft before pushing updates, or creating a new draft PR. Pause if required draft status cannot be established. Match the published tree to the recorded candidate and label its verification incomplete, never passed. Preserve an existing draft unless the user authorizes marking it ready; disclose its status.

If the exact intended commit is already remote, skip the push and finish only missing PR artifacts. Otherwise push only that pinned commit from the confirmed feature branch to the explicit destination branch/remote, without force or history rewriting. Verify the remote branch and existing PR head equal that pinned commit. Create a PR only if there is no matching open one; update the existing one otherwise. Use explicit repository selection, and verify the returned URL and head/base belong to the intended destination, including the pinned head after new-PR creation. Confirm these identities before describing a fix as published.

After verified publication, finish the existing PR's description, one substantive overall update, and demonstrably addressed inline replies using FOLLOW-UP.md. Keep updates on the PR: add no redundant issue implementation handoff and close no linked issue. A fully current rerun creates no commit, push, body edit, or duplicate comment.

If a commit, push, or GitHub write fails, inspect actual state before retrying an uncertain operation. Preserve local work, prepared text, and the recovery record; report exact partial progress rather than claiming completion or changing destinations. Never undo a successful push because a later write failed. Clearly independent, already-authorized safe replies may continue; dependent or uncertain actions wait.

## 7. Hand off manual review

Return the PR URL, published commit/head, verification summary/limitations, feedback dispositions, any incomplete publication steps, and this suggested next step:

> In a fresh session, select your review model and reasoning level, then request: `/code-review comprehensive <PR URL>`.

Stop here. Do not invoke `code-review`, change model/reasoning, poll for review, apply review fixes, or merge. Review and any follow-up remain user-triggered.
