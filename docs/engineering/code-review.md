## What it does

`code-review` checks the full committed branch diff along separate **Standards** and **Spec** axes. Comprehensive mode adds **Correctness**, including bugs, security, and material performance regressions that the requirements never anticipated.

PR input publishes a GitHub Comment review; local branch or commit input reports only in chat. The review recommends APPROVE or REQUEST CHANGES prominently, but never submits either formal GitHub verdict or merges code.

## When to reach for it

Type `/code-review`, or the agent reaches for it when a review request fits. No hooks or CI automation are installed.

| Situation | Request |
| --- | --- |
| Routine PR feedback | `Review PR #123` |
| Broader review before merging | `Comprehensive review PR #123` or `Pre-merge review PR #123` |
| Private preview of a PR review | `Review PR #123, draft only` |
| Local branch feedback | `Review the current branch` |
| Explicit comparison base | `Review this branch against release` |

Select your [model](https://www.aihero.dev/ai-coding-dictionary/model) and reasoning level before invoking. Both modes keep that selection; comprehensive means additional coverage, not an automatic model change.

## Prerequisites

Git history must be available. PR review also requires an authenticated `gh` CLI and permission to submit reviews. The configured issue tracker supplies the workflow for fetching referenced requirements; use [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) when it is missing.

| Review input | Spec source |
| --- | --- |
| PR number or URL, including draft-only | Explicitly selected source; otherwise a single native GitHub-linked issue; then inline Spec or the legacy whole-description fallback |
| Local branch or commit | Issue references in commits, an explicitly provided spec path, then matching files under `docs/`, `specs/`, or `.scratch/` |

A self-contained PR description needs no tracker setup. A Spec issue link is sufficient without copying its requirements; a single native linked issue also works without repeating its link in the description. Incidental issue mentions are supporting context, not automatic source selections. Multiple candidates need clarification unless a source is explicitly designated.

Empty Spec placeholders, inaccessible or unusable requirements, and source conflicts prompt for clarification or an explicitly incomplete affected Spec assessment. An explicitly selected source does not erase a conflict. Only your confirmation that no spec exists permits skipping that axis.

## Separate axes, shared scope

| Axis | Coverage |
| --- | --- |
| Standards | Mandatory repo rules and optional Fowler smell heuristics; repo rules override heuristics |
| Spec | Missing requirements, incorrect implementations, and scope creep |
| Correctness, comprehensive only | Concrete defects beyond stated requirements |

Each axis uses a separate [subagent](https://www.aihero.dev/ai-coding-dictionary/subagent) with a fresh [context window](https://www.aihero.dev/ai-coding-dictionary/context-window) where supported. If the [harness](https://www.aihero.dev/ai-coding-dictionary/harness) lacks subagents, the skill discloses sequential passes instead. Findings are validated before delivery and remain grouped by axis.

| Base source | Priority |
| --- | --- |
| Your explicit base | First |
| Associated PR target | Second |
| Unambiguous evidence of the original branch | Third |
| `main` when the original branch is gone or cannot be established | Fallback |

Git does not reliably store the original branch name. The skill announces the selected base and evidence instead of presenting guesses as facts. A commit identifies the review head; the scope remains the full branch diff from the merge-base.

## Common questions

**Where does the review go?**

PR input produces one Comment review with new actionable findings inline and an overall summary in its body. Exact replacements may use GitHub suggestion blocks. Local input and explicit draft-only produce chat output without GitHub writes. Neither route edits source files.

**Do I have to copy the issue spec into the PR?**

No. The review fetches the authoritative issue from an explicit Spec link or a single native GitHub-linked issue. Without an issue, inline Spec contents work; older PRs can still use the whole description. Explicit user-selected overrides remain supported and are named in the report. Local reviews retain their existing issue/path/file lookup.

**What if the PR only implements part of the issue?**

Declare the agreed slice and deferred requirements in the PR. The reviewer assesses that scope against the issue rather than demanding every parent requirement. It cannot infer permission to omit requirements from the implementation itself.

**Does the reviewer fix conflicting requirements?**

No. It reports the conflict and marks the affected Spec assessment incomplete, while retaining independently demonstrable findings. Review is read-only: it edits neither issues nor PR descriptions.

**Can an approval still include suggestions?**

Yes. Optional naming improvements and possible smells do not block approval. Concrete bugs, unmet requirements, material regressions, and mandatory rule violations warrant a REQUEST CHANGES recommendation. That recommendation remains text, not a formal blocking review event. Missing evidence and skipped checks are visible qualifications.

**What happens when I review the same PR again?**

The skill reads previous reviews, replies, and thread state, examines changes since the previous reviewed commit, and reassesses the full current diff. It links unchanged open findings rather than duplicating them, identifies resolved issues, and includes remaining blockers in the recommendation.

**Does it review uncommitted changes?**

No. Staged and working-tree changes are excluded and disclosed. Commit the work first. The skill does not stage, stash, reset, or amend it for you.

**Can I trust the findings?**

They are evidence-backed recommendations, not proof. The skill checks findings against source and reports limitations, but you still decide what to act on and whether to merge. Prefer a fresh reviewing session to reduce the influence of authoring assumptions.

## It's working if

- The opening scope names the mode, comparison base, reviewed commit, and destination.
- PR findings appear beside relevant changed lines, with a prominent recommendation in the review body.
- Local and draft-only reviews never post to GitHub.
- Repeated reviews account for replies and fixes without duplicating unchanged findings.
- Separate axis summaries state skipped checks, missing requirements, and remaining blockers.
- A PR review names its actual authoritative source and agreed slice, and refreshes affected findings when issue requirements or the PR change before publication.

## Where it fits

This is a build-chain review step and a standalone review tool. [implement](https://aihero.dev/skills-implement) supplies local commits; [pr](https://aihero.dev/skills-pr) publishes intended work and its authoritative requirements before a separately requested review. Prefer a fresh reviewing [session](https://www.aihero.dev/ai-coding-dictionary/session), with your chosen model and reasoning level. Neither publication nor review starts an automatic fix loop or merge. [retro](https://aihero.dev/skills-retro) turns review misses into environment improvements.

[ask-matt](https://aihero.dev/skills-ask-matt) routes across the whole set.
