---
name: implement
description: "Implement one selected issue from a validated spec, verify it, and hand off a local commit."
disable-model-invocation: true
---

Implement **one explicitly selected issue** from the repository's configured issue tracker. The authoritative issue spec defines success; conversation context can clarify it, but cannot replace it. Finish with a local commit and an issue handoff, leaving publication and review to the user.

## 1. Select and fetch the issue

- Accept a reference in the invocation or an issue unambiguously selected earlier in the conversation. If none is selected, ask for one and stop. The user chooses the issue: do not create one, select from a queue, or expand the run to multiple issues.
- Resolve the reference through the repository's configured tracker and fetch the issue. A number refers to that tracker, not another numbered list. A local document qualifies only if it is an issue record in the configured local tracker, not a loose spec file.
- Clarify ambiguous identifiers, repository destinations, or tracker configuration instead of guessing. If configuration is missing, surface it and tell the user to follow the repository's established setup path (normally `/setup-matt-pocock-skills`). Retain support for configured trackers without adding integrations.
- Announce the tracker/repository context, identifier, title, and reference before implementation. Verify the destination for tracker reads and writes; the repository distributing these skills is not an implicit destination. With GitHub, check the repository explicitly and use `--repo <owner/repo>` on issue commands, since automatic discovery in a fork can select upstream.

## 2. Validate the spec

Validate with the self-contained checklist below, based on the spec substance defined by `to-spec`. Installing or invoking `to-spec` is not required. Manually authored issues qualify. Judge substance, not authorship, literal headings, prose length, or an extensive story list; scale the detail to the change.

Account for:

- The problem, proposed solution, user outcomes/stories, and verifiable acceptance criteria.
- Implementation decisions, relevant constraints, and exclusions.
- Testing decisions, including agreed seams, and any requirements in further notes.

Distinguish genuinely irrelevant sections from missing decisions. An unresolved question is not irrelevant merely because it would block work.

A child may inherit shared requirements from a linked parent spec. Fetch the necessary parent requirements and combine them with the child's explicit acceptance criteria, agreed slice, and deferred scope. Duplication of the parent spec is unnecessary; undeclared scope, conflicting sources, or inaccessible required sources are blockers. Never infer requirements or a child's scope from implementation choices or existing code to make it appear compliant.

**Gate:** the combined authoritative requirements define clear intended outcomes, verifiable acceptance criteria, constraints, and adequate testing decisions. Otherwise continue with gap resolution, not implementation.

## 3. Resolve material gaps

Present material gaps, contradictions, unclear acceptance criteria, and unresolved testing/seam decisions with proposed resolutions. Pause implementation until they are settled. Obtain the user's approval before substantive requirement changes, including changes discovered later during implementation.

After approval, update the authoritative issue spec and add an issue comment summarizing what changed and why. A comment alone must not leave the main spec stale. For inherited requirements, update the actual authoritative parent source only with approval, and record the clarification where needed for the selected issue. If updating that source is unavailable or ambiguous, pause and agree on an explicit alternative instead of creating competing requirements in conversation or comments.

Once the spec, testing decisions, and feature branch are settled, this invocation is sufficient authorization to proceed. Do not require approval of another routine implementation plan. Make ordinary implementation choices within the agreed spec; ask again for material changes or decisions outside it.

## 4. Confirm a feature branch and preserve existing work

Before implementation changes, inspect the current branch, repository default branch, working tree, and existing history.

- On `main` or the repository's default branch, warn and pause. Suggest a feature-branch name; let the user accept or replace it, and obtain confirmation before creating it or making implementation changes.
- Reuse an appropriate existing feature branch when already selected. Clarify an unsuitable or ambiguous branch rather than silently switching or proceeding. Confirm the intended branch before work starts.
- Distinguish intended work from unrelated changes. Preserve unrelated work and history; ask when ownership or scope is ambiguous. Never blindly stage all changes, discard unrelated work, amend unrelated commits, or rewrite history to make the branch look ready. Local-main cleanup belongs to the separate publishing workflow, not this skill.

## 5. Implement and verify

Implement the agreed behavior. Call the Skill tool with "tdd" where applicable, at pre-agreed seams. If testing or seam decisions are unresolved, return to gap resolution before writing tests at an unconfirmed seam.

Discover and run the target repository's applicable required verification. Run focused checks regularly and final full verification as appropriate to the project and change, including typechecking and tests where provided. Use actual repository commands rather than inventing checks the project does not provide. Keep track of commands, results, failures, unavailable checks, checks not run, and limitations; unverified work is not verified completion.

## 6. Recheck requirements and commit locally

Before the final commit/handoff, re-fetch the authoritative issue requirements, including necessary parent requirements. Compare them with the requirements used during implementation and check the work against the current acceptance criteria. Continuous polling is unnecessary. If requirements changed materially, pause and reconcile them with the user before committing or handing off; neither silently finish against a stale spec nor expand scope to match it.

Inspect the final diff and working tree, verify that the confirmed feature branch is still current, and stage only intended work. Commit locally on that branch. Report verification failures or limitations honestly rather than claiming successful completion.

**Local-only boundary:** never automatically push, create a remote branch, open or update a PR, invoke `code-review`, fix review findings, close the issue, or merge. Publication and user-triggered review are separate steps.

## 7. Record the handoff

On successful implementation, add a concise comment to the selected issue containing:

- The local branch name and final commit SHA.
- Actual verification commands and results, including failures, unavailable or unrun checks, and remaining limitations.
- An explicit statement that the branch and commit remain local and have not been pushed by this skill. Do not link an unavailable commit or present local work as a remote artifact.

Use the configured equivalent for a local tracker rather than assuming comments exist. Leave the issue open and do not claim PR review or approval. If recording the handoff fails, preserve the local work and report the failure instead of claiming it was published.

End with a concise summary and the next manual steps: the user separately chooses when to publish with `pr` and request `code-review`. Never call those steps automatically.
