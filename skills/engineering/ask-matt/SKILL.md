---
name: ask-matt
description: Ask which skill or flow fits your situation. A router over the skills in this repo.
disable-model-invocation: true
---

# Ask Matt

You don't remember every skill, so ask.

This fork's personal recommendations follow [`enabled-skills.json`](../../../enabled-skills.json), the sole activation authority. Read it before recommending a workflow. [`parked-skills.json`](../../../parked-skills.json) records personally deselected alternatives, not installed active workflows. Both use paths relative to the repository root. General reference docs and skill definitions remain available even when a skill is parked.

Before stating what a skill does or recommending a step be skipped, read that skill's SKILL.md: the summaries here are for orientation only. User-invoked skills can be installed without appearing in the model's skill list; that list alone is not evidence of deselection.

Only the user starts `/wayfinder`, `/improve-codebase-architecture`, `/handoff`, `/retro`, and `/wait-what`. After explicit entry, their documented supporting calls proceed normally. Model-invoked supporting skills are also independently available; they need no new per-call permission gate.

A **flow** is a path through the skills. Most paths run along one **main flow**, and two **on-ramps** merge onto it. Everything else is standalone, or a vocabulary layer that runs underneath.

## The main flow: idea → ship

The route most work travels. You have an idea and want it built.

1. **`/grill-me`** sharpens the idea by interview, with or without a working directory. It runs the `/grilling` primitive and keeps the discussion in the conversation rather than writing `GLOSSARY.md` or ADRs. This is the active interview entry; record the settled requirements with `/to-spec`.
2. **Branch: can you settle every question in conversation?** If a question needs a runnable answer (state, business logic, a UI you have to see), detour through a prototype, bridged by **`/handoff`** in both directions (a prototype lives in its own directory, which is exactly what `/handoff` is for; see Phase boundaries):
   - **`/handoff`** out, then open a fresh session against that file,
   - **`/prototype`** to answer the question with throwaway code,
   - **`/handoff`** back what you learned, and reference it from the original idea thread.
3. **Branch: is this a multi-session build?**
   - **Yes** → **`/to-spec`** (publish the thread as an issue-backed spec), then **`/to-tickets`** to split it into tracer-bullet issues, each declaring its **blocking edges**. Use **`/implement`** for one explicitly selected issue per run, **`/clear`ing context between runs**. Choose an issue whose blockers are done; the skill does not select from the queue. The issue can inherit a linked parent spec, but must declare its own acceptance criteria and agreed slice. A configured local tracker record qualifies too.
   - **No** → select an existing issue with an adequate spec, or use **`/to-spec`** to publish the conversation first, then invoke **`/implement`** for that issue. A manually authored issue works; a conversation-only plan or loose spec document does not.

   **`/implement`** fetches and announces the selected issue, validates the spec substance, and pauses for material gaps. Approved requirement changes update the authoritative spec and get an explanatory issue comment. Once requirements and testing are settled, it announces and safely creates a local feature branch from `main` or the default branch without another routine approval; suitable existing branches are reused. New names honor an explicit name or repository convention, otherwise using a purpose prefix, issue identifier, and very short description (for example `feat/issue-8-branch-names`). Collisions, obvious mismatches, ambiguity, and unsafe state pause for the user's decision. It drives **`/tdd`** where applicable at agreed seams, verifies, rechecks requirements, commits locally, and records an explicitly unpushed issue handoff. It leaves the issue open. With spec, testing, and branch settled, no separate routine plan approval is needed.

   After `/implement`, the user separately chooses when to publish with **`/pr`** and request **`/code-review`**. Neither is an automatic continuation. An unqualified `/pr` authorizes publication; a review-fix request or an existing PR alone does not. **`/pr`** uses the same naming guidance when a suggestion is needed, but keeps confirmation before branch creation and reuses suitable existing branches without cosmetic renaming. It verifies the exact candidate tree in isolation from excluded local edits, binds the committed/pushed tree to those results, commits intended changes if needed, and pushes/opens or updates the PR in the explicitly resolved repository. Its description links the authoritative issue, or carries approved inline requirements, followed by optional Implementation, honest Evidence, and Merge Danger. It pauses for substantive requirement changes, unsafe scope, or failed required checks (unless the user explicitly authorizes a draft). For an existing PR it reads inline and ordinary feedback, refreshes the preserved-content description, posts one overall update covering all newly published commits, and replies in demonstrably addressed inline threads with published fixing-commit links. Deferred, disputed, unverified, or uncertain mappings stay explicit; it neither fixes more findings nor resolves threads. Interrupted updates resume only missing artifacts, and current reruns write nothing. Publication ends with the URL, exact partial state if needed, and a manual comprehensive-review suggestion, not an automatic reviewer or fix loop. It's model-invoked for publication/update requests; explicit preview/body-only requests stay text-only and local-only requests retain their limits. Reach for **`/tdd`** alone for concrete behavior test-first without an issue.

   Reach for **`/code-review`** separately to review a full branch diff locally or publish feedback on a PR. Request **comprehensive** review before merging in the main flow. Focused mode checks Standards + Spec; an explicit comprehensive or pre-merge request adds Correctness. PR input resolves an explicitly selected spec or a single native GitHub-linked issue, then inline Spec or the legacy whole-description fallback, and publishes a Comment review with inline findings and a recommendation. It fetches authoritative requirements, respects an explicitly agreed slice, and reports conflicts read-only; local input keeps issue/path/file spec discovery and stays in chat. Select the model and reasoning level before invoking.

   After the separately requested review, the human may explicitly invoke **`/merge-and-cleanup`** with a GitHub PR number or URL (or an unambiguous current-branch/tracked-remote match). This user-invoked-only finishing step resolves destinations, requires current comprehensive approval evidence or an explicit head-scoped override, respects GitHub protections, squash-merges, verifies remote success, and safely removes only the PR's source branches. Invocation authorizes completion comments and closure of clearly identified, fully delivered implementation issues, including an authoritative Spec selection without native closing links. Applicable comprehensive approval covering each issue's complete, current requirements is sufficient delivery evidence; closeout does not repeat the review or treat disclosed verification limits alone as unfinished requirements. Partial or unclear delivery requires consultation before any merge, even without automatic closure; a review override alone does not settle issue outcomes. Incidental references and parent/umbrella context are not completed deliverables merely because they are linked. It finishes on the actual default branch via a safe fast-forward. Already-merged recovery reuses applicable approval at the recorded merged head; unclear issue delivery pauses affected completion actions while safe cleanup may proceed. Uncertain or unsafe work is preserved and partial success is reported. The resolved safe happy path needs no routine reauthorization. Neither publication, review, nor this router invokes it automatically.

4. **`/retro`**, when explicitly requested, closes the loop. After a build, and especially one that went sideways, it looks back over the session and suggests changes to the agent's **environment**, not the code: navigation pointers, automated checks, the coding standards `/code-review` enforces, steering files, tooling. Mechanical mistakes become deterministic checks; judgement calls become coding standards. The next build then starts from a better environment.

### Context hygiene

Keep planning in steps 1–3 in **one unbroken context window** through `/to-spec` and any `/to-tickets`, so the grilling, spec, and issues build on the same thinking. Each `/implement` can then start fresh, working from its explicitly selected issue and any linked parent spec. If you choose `/retro`, run it in the session it's looking back on, before you clear; after clearing, point it at that session's log instead.

The limit on this is the **[smart zone](https://www.aihero.dev/ai-coding-dictionary/smart-zone)**: the window (~150k tokens on state-of-the-art models) within which the model still reasons sharply. If a session approaches it before `/to-tickets`, don't push on degraded; `/compact` at the nearest phase boundary and carry on (see Phase boundaries).

## On-ramps

A starting situation that generates work, then merges onto the main flow.

- **Something's broken** → **`/diagnosing-bugs`**. For the hard ones: the bug that resists a first glance, the intermittent flake, the regression that crept in between two known-good states. It refuses to theorise until it has a **tight feedback loop** (one command that already goes red on *this* bug), then fixes with a regression test. Once the fix is in, you can explicitly request **`/retro`** in the same session to ask what would have prevented the bug; where the real finding is that there's no good seam to lock it down, that's a job for **`/improve-codebase-architecture`**.

- **A huge, foggy effort: a greenfield project or a huge feature build, too big for one session** → **`/wayfinder`**, the most cognitively demanding flow here. When the way from here to the destination isn't visible yet, it charts a **shared map** of **decision tickets** on the issue tracker and resolves them one at a time, producing **decisions, not deliverables**, until the fog is pushed back and the way is clear. Where **`/grill-me`** sharpens an idea you can hold in one session, wayfinder is for the idea you can't, and it's slower and denser, so save it for exactly that, never a well-scoped feature.

  When the map clears, **it hands off, it doesn't build**: merge onto the main flow at **`/to-spec`**, which collapses the map's linked decisions into a buildable plan, then `/to-tickets` and `/implement` as usual. Looping the map straight into `/implement` skips that collapse and throws the linked detail away. Even a small effort needs an explicitly selected issue with an adequate spec before `/implement`; size does not let a conversation or map replace those requirements.

## Codebase health

Not feature work, just upkeep.

- Explicitly invoke **`/improve-codebase-architecture`** when you want to survey architectural friction and keep the codebase good for agents to operate in. It surfaces **deepening opportunities**; picking one _generates an idea_ you can take into the main flow at `/grill-me`. It's the survey that finds the candidates; **`/codebase-design`** (below) is the bench you design the chosen one on.

## Vocabulary underneath

Two model-invoked references that run *beneath* the other skills, each the single source of truth for its vocabulary. Reach for them directly when the **words**, not the process, are the problem; or let the skills above pull them in.

- **`/domain-modeling`**: sharpen the project's *domain* language: challenge a fuzzy term, resolve an overloaded word ("account" doing three jobs), record a hard-to-reverse decision as an ADR. It remains available directly and supports `/wayfinder` and `/improve-codebase-architecture`.
- **`/codebase-design`** is the deep-module vocabulary (module, interface, depth, seam, adapter, leverage, locality) for designing a module's *shape*: a lot of behaviour behind a small interface at a clean seam. `/tdd` and `/improve-codebase-architecture` both speak it.

## Phase boundaries

A **phase** is a chunk of work inside a session: the grilling, the implementation, the QA. At the **boundary** between two of them you have five options, and picking between them is the fuzziest decision in this whole map:

- **Continue**: stay put. Costs nothing, loses nothing.
- **`/clear`**: empty the window, when nothing here matters to what's next.
- **`/handoff`** writes a portable markdown file. Narrow: only for a **new harness**, a **new directory**, a **colleague**, or forking a side task **mid-phase**. What it buys is portability.
- **Subagent**: send a tightly-scoped task to a fresh context window and get a report back.
- **`/compact`** compresses this context and seeds a fresh session with it. The **default**, at the bottom of the tree rather than the first reach.

Read [PHASE-BOUNDARIES.md](PHASE-BOUNDARIES.md) for the ordered tree: the five questions, the reasoning behind each branch, and why the primary-source cost makes **Continue** the one to rule out first. Make the decision **at** a boundary; mid-phase, continue or split the rest into subagents.

## Standalone

Off the main flow entirely.

- **`/grilling`** is the interview primitive itself: rounds, the frontier, facts are the agent's job and decisions are yours. `/grill-me` is the active named entry, and `/wayfinder` and `/improve-codebase-architecture` run it internally. It is also independently model-invoked when the task fits.
- **`/prototype`** is a small, throwaway program that answers one design question: does this state model feel right, or what should this UI look like. Throwaway is a constraint on how the code is written, not a promise to destroy it: the answer folds into the real code, and the prototype itself is kept as a **primary source** on a `prototype/<name>` branch out of main, pointed at from the implementation issue. It's the detour in step 2 of the main flow, but reach for it any time a design question is hard to settle on paper.
- **`/research`**: delegate reading legwork to a **background agent**: it investigates a question against **primary sources**, then leaves a cited Markdown file in the repo. Keep working while it reads. The file it produces is something to take *into* the main flow at `/grill-me`, since research feeds the thinking rather than replacing it.
- **`/wait-what`** is the corrective for a message that didn't land. Use it mid-conversation, inside any other skill, and the agent re-pitches what it just said with the context you were missing, in plain English, using the `GLOSSARY.md` vocabulary. It repairs that message; reach for `/domain-modeling` separately when the underlying problem is shared terminology.
- **`/writing-for-agents`** is the reference for writing documents agents consume: skills, AGENTS.md, pointed-at docs.

## Parked alternatives

For alternatives outside the active selection, consult [`parked-skills.json`](../../../parked-skills.json), then read the listed skill's definition if the user wants to explore it. Treat these as discoverability references, not active recommendations. Parking reasons and reconsideration triggers live in [issue #3](https://github.com/brucepucci/skills/issues/3).

Re-enabling means moving the directory entry from the parked registry into `enabled-skills.json`, checking supporting dependencies, and using the normal apply and reload process in the repository README. Neither discussing a parked skill nor editing a registry installs it. Skill content, invocation metadata, and general plugin distribution are unchanged by parking.

## Precondition

**`/setup-matt-pocock-skills`**: run before your first engineering flow to configure the issue tracker, triage labels, and doc layout the other skills assume. Custom issue trackers also work.
