## What it does

`implement` turns one selected issue into verified work and a local commit. It requires a durable, adequate [spec](https://www.aihero.dev/ai-coding-dictionary/spec) in the configured issue tracker, not just a plan in the conversation. It fetches and announces the issue, checks the requirements, and works on a suitable feature branch. Once requirements and testing decisions are settled, it announces and safely creates a local branch from `main` or the default branch without another routine approval.

The run ends with an issue handoff, not publication or review. It leaves the issue open and never automatically pushes, opens or updates a PR, runs [code-review](https://aihero.dev/skills-code-review), or fixes review findings.

## When to reach for it

You invoke this by typing `/implement`, and the [agent](https://www.aihero.dev/ai-coding-dictionary/agent) won't reach for it on its own. Reach for it when you have chosen one issue and want its agreed behavior implemented.

| Your starting point | What to do |
| --- | --- |
| One issue with an adequate spec | Pass its reference, such as `/implement owner/repo#42`; an unambiguous earlier selection also works |
| A child issue with acceptance criteria and a linked parent spec | Select the child; the run fetches the necessary shared requirements too |
| A small plan that lives only in conversation or a loose document | Publish it as an issue first; [to-spec](https://aihero.dev/skills-to-spec) can synthesize the conversation |
| A build too large for one issue | Use [to-tickets](https://aihero.dev/skills-to-tickets) to split it, then select one issue per run |
| One concrete behavior you want test-first without an issue | Use [tdd](https://aihero.dev/skills-tdd) directly |
| Work already built and ready to inspect | Request [code-review](https://aihero.dev/skills-code-review) separately |

## Prerequisites

The repository needs a configured issue tracker, normally established by [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills). GitHub and other existing configured trackers work, including a local tracker: a local issue record qualifies, but a loose spec file outside that tracker does not.

The issue must settle the relevant outcomes, acceptance criteria, implementation constraints, testing decisions, and exclusions. Testing uses pre-agreed **seams**, the public boundaries where behavior is observed. An unresolved seam is a question to settle before writing tests, not permission to invent one.

## The issue is the source of truth

Validation follows the substance of [to-spec](https://aihero.dev/skills-to-spec), not its exact headings or who wrote the issue. Small changes need proportionate detail, not an enormous story list. Child issues can inherit shared requirements without copying the parent, but must declare their own slice and acceptance criteria.

Material gaps pause implementation. You approve substantive changes, then the authoritative spec is updated and a comment records what changed and why. A comment cannot substitute for a stale spec. Once requirements, testing decisions, and the branch are settled, there is no extra approval round for a routine implementation plan.

Requirements are fetched again before the final commit and handoff. Material changes during the run are reconciled with you rather than silently ignored or folded into extra work.

## Local-only completion

| Checkpoint | What you see |
| --- | --- |
| Starting on `main` or the default branch | After requirements and testing are settled, an announced branch name and automatic safe local creation before implementation |
| Already on a suitable feature branch | That branch is reused, even with a different naming style; unrelated work stays intact and outside the commit |
| Explicitly requested branch name | Your name is honored, subject to validity, collision, obvious-mismatch, and safety checks |
| Collision, obviously unrelated branch, ambiguity, or unsafe state | An explanation and a pause for your decision, not an arbitrary suffix, silent rename, stash, or history rewrite |
| Verification | Applicable repository checks, with actual commands, results, and limitations rather than assumed success |
| Handoff | A local commit and an issue comment naming the branch, SHA, verification, and limitations, explicitly marked unpushed |
| Publication and review | Separate decisions you make after implementation; neither runs automatically |

## Common questions

**Will it ask me to approve a branch name?**

Not for routine safe creation from `main` or the default branch. Your implementation request authorizes that once requirements and testing decisions are settled. Collisions, obvious naming mismatches, ambiguous choices, and unsafe state still pause. [pr](https://aihero.dev/skills-pr) retains its separate confirmation before branch creation.

**What names does it choose?**

- Your explicit name wins, subject to safety checks; an established repository convention overrides the generated default.
- Otherwise it uses a purpose prefix, issue identifier, and very short description, such as `feat/issue-8-branch-names`. Fixes normally use `fix/`, maintenance uses `chore/`, and urgent fixes or releases use `hotfix/` or `release/` only when warranted.
- Other configured trackers retain a recognizable lowercase issue key. Title boilerplate such as "To do" is dropped, and generated names follow [Conventional Branch](https://conventionalbranch.org/) and Git naming rules.
- A suitable existing branch is reused without cosmetic renaming.

**Does my issue have to come from `to-spec`?**

No. A manually authored issue qualifies if its requirements are adequate. The validator checks substance, distinguishes irrelevant sections from unresolved decisions, and accepts linked parent requirements. `implement` carries its own validation checklist, so neither installing nor invoking `to-spec` is required.

**`/implement #2` worked on something unrelated. How do I avoid that?**

The reference must resolve through the configured tracker, not another numbered list. The run announces the tracker/repository, identifier, title, and reference before work begins, and asks about ambiguity. An issue URL or `owner/repo#2` makes your selection clearer. In a fork, verify that the announced destination is your repository, not upstream.

**Why is my issue still open after the commit?**

That is deliberate. The completion comment records local work, not a published or reviewed artifact. You choose when to publish with [pr](https://aihero.dev/skills-pr), request review, and eventually close the issue. If recording the comment fails, the run reports that failure and preserves the local commit.

**Will it review its own changes or open a PR?**

No. Automatic review and the old review-before-commit behavior are removed. The run stops after local implementation and handoff; publication, review, and any review-fix session are separately chosen work.

**Can it pick an issue from my queue or implement all my issues?**

No. One invocation covers one explicitly selected issue. Missing selection produces a question, not an automatically created issue or queue choice. It does not orchestrate parallel implementers; the separate [implement-spec](https://aihero.dev/skills-implement-spec) workflow is unchanged by this skill's local-only contract.

## It's working if

- The announced issue identity and repository match the work you selected.
- Material spec gaps stop work until approved corrections reach the authoritative issue, with an explanatory comment.
- From the default branch, safe local branch creation is announced and proceeds without a routine approval round; implementation waits for settled requirements and testing.
- Suitable existing branches, unrelated changes, and local commits remain intact; collisions and unsafe choices pause instead of triggering silent recovery.
- Verification results name the actual commands and distinguish passed checks from unavailable or unrun checks.
- The issue receives a local-only branch/commit handoff and stays open, with no automatic push, PR, or review.

## Where it fits

`implement` is the local build step after issue-backed planning. [to-spec](https://aihero.dev/skills-to-spec) can produce the requirements; [to-tickets](https://aihero.dev/skills-to-tickets) can split a larger spec into selectable issues. It uses [tdd](https://aihero.dev/skills-tdd) at agreed seams where applicable.

After the local commit, you separately choose publication with [pr](https://aihero.dev/skills-pr) and review with [code-review](https://aihero.dev/skills-code-review). [ask-matt](https://aihero.dev/skills-ask-matt) is the router when you need help choosing the next step.
