---
name: pr
description: "Prepare and publish a PR, or update an existing PR, with authoritative requirements, verification evidence, and a manual review handoff. Use when the user asks to publish changes, open/update a PR, or write its body."
metadata:
  credits:
    skill: show-me
    author: Dex Horthy
    organisation: Humanlayer
    url: "https://github.com/humanlayer/skills/blob/main/plugins/show-me/skills/show-me/SKILL.md"
---

Prepare and publish the intended work against the **authoritative spec**, then stop at a manual review handoff. This skill does not review, fix findings, or merge. It does not require `to-spec` or automatically create an issue.

For a request only to write or preview a body, resolve scope and requirements, read [BODY.md](BODY.md), and return prepared text with honest evidence. That request authorizes no branch/history mutations, commits, pushes, or publication. Publication requests follow the full workflow below. Use the user's domain language from `GLOSSARY.md` where available.

## 1. Resolve destination and inspect scope

Inspect repository instructions, working tree (including staged and untracked changes), current branch, remotes, default branch, and history. Explicitly resolve the intended publication repository and push remote; never assume the skills distribution repository or trust GitHub CLI's fork/upstream inference. Verify the destination and use explicit `--repo OWNER/REPO` or API paths on GitHub operations.

Look for the current branch's open PR in that destination before creating one. Reuse it when unambiguous. For an existing PR, use its target branch as the base; for a new one, normally use the intended repository's default branch. Clarify ambiguous repository, remote, base, or PR selection. Network/authentication errors are not evidence that no PR exists.

Fetch the relevant remote refs without overwriting local branches. Inspect the full commit list and complete branch diff against the selected base, as well as uncommitted changes. Check the merge-base and detect truncated output. A clean working tree does not mean the branch contains only intended work. Announce repository, remote, branch, base, existing PR if any, and intended scope. Pause for unrelated existing commits or ambiguous ownership; preserve unrelated work rather than silently including or discarding it.

## 2. Confirm a feature branch

On `main` or the repository's default branch, warn and pause before committing or creating a branch. Suggest a descriptive feature-branch name; let the user accept or replace it and obtain confirmation before creation. Reuse an appropriate existing feature branch; clarify an unsuitable branch rather than silently switching.

Preserve intended local commits and uncommitted work on the confirmed feature branch. Never blindly stage all changes, discard unrelated work, amend existing commits, force-push, or rewrite remote default-branch history.

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

For an existing PR, snapshot its current description and published head before editing or pushing. Preserve approved requirements and hand-written content while refreshing implementation details and verification evidence. Show conflicts and ask before overwriting existing content; do not replace the entire body blindly. Recheck the current remote state before writing if it could have changed.

Inspect the final working tree and full branch diff again. Confirm the starting HEAD, candidate tree, and verification status (including any authorized draft exception) still match the recorded snapshot, then commit only that candidate on the confirmed feature branch after the verification gate. Preserve unrelated work and staging; do not newly select files or hunks after checks. Verify the resulting commit's tree OID (`git rev-parse HEAD^{tree}`) equals the verified candidate OID; a mismatch blocks normal publication and requires preparing/verifying the actual candidate again. Reuse intended existing commits rather than amending them or creating an empty commit. Check that the prepared description accurately represents the whole delivery, not only the latest edits.

## 6. Publish or update once

Reconfirm repository, remote, branch, base, and PR state before pushing. Pin the exact commit to push and confirm its tree OID matches the verified candidate; a later candidate change invalidates verification and returns to step 4. Verify the remote branch/PR head equals that pinned commit after pushing. If a draft exception was authorized, match the pushed tree to the recorded candidate and label its verification incomplete, never passed. An authorized draft exception requires a new draft PR or converting the existing PR to draft before pushing updates; pause if draft status cannot be established. Push only the confirmed feature branch to the resolved remote, without force. Create a PR only if there is no matching open one; update the existing one otherwise. Use explicit repository selection, and verify the returned URL and head/base belong to the intended destination. Preserve an existing draft unless the user authorizes marking it ready; disclose its status.

For a substantive existing-PR update, add one concise comment describing changes since the previously published version, relevant new verification, and explicitly approved requirement changes. Compare against the saved published snapshot, not only the latest local commit. No-op reruns need no comment. Inspect the PR, branch, and existing comments before retrying an uncertain write so retries do not duplicate PRs or update comments.

If a commit, push, or GitHub write fails, report the exact partial state and preserve local work and prepared text. Do not claim publication succeeded or silently change destinations.

## 7. Hand off manual review

Return the PR URL, verification summary/limitations, and this suggested next step:

> In a fresh session, select your review model and reasoning level, then request: `/code-review comprehensive <PR URL>`.

Stop here. Do not invoke `code-review`, change model/reasoning, poll for review, apply review fixes, or merge. Review and any follow-up remain user-triggered.
