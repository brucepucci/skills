## What it does

`pr` prepares and publishes intended changes, or updates their existing pull request, against the authoritative [spec](https://www.aihero.dev/ai-coding-dictionary/spec). It checks the whole delivery, runs required verification, safely handles the branch and commits, and publishes requirements and evidence a reviewer can use without the authoring conversation.

It stops at a manual review handoff. Publication does not launch a reviewer, select a review [model](https://www.aihero.dev/ai-coding-dictionary/model), fix findings, or merge. A body-only request produces text without permission to commit, push, or publish.

## When to reach for it

Type `/pr`, or the [agent](https://www.aihero.dev/ai-coding-dictionary/agent) reaches for it when you ask to publish changes, open/update a PR, or write its body.

| Your situation | Reach for |
| --- | --- |
| Local work is ready to publish | `pr`, with the intended issue or agreed requirements |
| An existing PR needs new commits or evidence | `pr`, reusing the open PR |
| You only want draft description text | Ask `pr` for a body only |
| You want feedback, not publication of the branch | [code-review](https://aihero.dev/skills-code-review) |

## Prerequisites

Publication needs Git history, authenticated GitHub access, and permission to push to the intended repository. Issue-backed work uses the configured tracker; [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) establishes it. Inline requirements need no issue tracker setup.

## One authoritative spec

The spec captures intent, not a description reverse-engineered from code. That prevents the reviewer from checking whether the implementation matches an account of what it already does.

| Requirements available | What the PR carries |
| --- | --- |
| An authoritative issue | Its link, not a duplicate of its full requirements |
| An agreed partial issue delivery | The issue link, agreed slice, and deferred requirements |
| Approved requirements without a suitable issue | An inline Spec section; no automatic issue creation |
| Requirements reconstructed from conversation | Your approval before publication |

Faithful formatting of already agreed requirements needs no extra approval. Substantive changes do. Approved issue-backed changes update the issue itself; conflicting sources pause publication rather than introducing a second competing spec.

New descriptions contain **Spec**, optional **Implementation**, **Evidence**, and **Merge Danger**. A small diagram or shaped diff can clarify implementation, but visuals are optional supporting context. Evidence reports actual commands and results. Merge Danger states reversibility (a one-way or two-way door) and blast radius.

## Safety before publication

The scope check includes existing branch commits, not just uncommitted edits. A branch created from the wrong feature branch can carry unrelated history even when its working tree is clean.

- On `main` or the default branch, the skill pauses for a feature-branch name and confirmation before creating it.
- Unrelated work is preserved, and ambiguous ownership pauses the run.
- Local-main cleanup is optional, only after preserving work, and needs separate confirmation showing the exact move to the verified remote-tracking tip.
- Failed or unavailable required verification stops normal committing, pushing, and publication. You may explicitly authorize a draft exception; Evidence records the exception and missing checks.
- An existing PR is updated without blindly replacing approved requirements or hand-written content. Substantive updates get a concise change comment; no-op reruns do not.

## Common questions

**Does it open the PR for me now?**

Yes. In this fork, `pr` owns publication as well as the description. [implement](https://aihero.dev/skills-implement) still stops with a local commit. You separately choose when to publish and when to review.

**Do I have to use `to-spec` first?**

No. A manually authored issue or approved inline requirements work. Reconstructed requirements come from your conversation and need approval; they are not inferred from the diff.

**What if I have no before-change screenshot or failing test output?**

The skill says so. It reports checks actually run, including failures and limitations, rather than fabricating a before/after story. A passing check is useful evidence even without a captured baseline.

**Can it sort through review comments or fix them automatically?**

No. It updates the PR's intended changes and evidence, then returns its URL and a suggested comprehensive-review request. Choose the model and reasoning level yourself in a fresh reviewing [session](https://www.aihero.dev/ai-coding-dictionary/session). Findings and fixes remain separate decisions.

**Can I trust the door call?**

Treat it as an assessable claim. Reverting a commit will not unsend emails or necessarily undo a data migration. Read the reversibility and blast-radius explanation, not just the size of the diff.

## It's working if

- The PR points to the agreed requirements without copying an issue's full spec.
- The scope matches the whole branch delivery, not only the latest edits.
- Evidence names real checks and their limitations, including any draft exception.
- Reruns preserve your edits and avoid duplicate PRs or no-op comments.
- You receive the PR URL and a manual review suggestion, with no reviewer launched or merge performed.

## Where it fits

This is a publication chain step: [implement](https://aihero.dev/skills-implement) produces verified local commits; `pr` publishes when you choose; [code-review](https://aihero.dev/skills-code-review) separately assesses the published work against the authoritative requirements. Both skills also work outside that chain.

[ask-matt](https://aihero.dev/skills-ask-matt) routes across the whole set.
