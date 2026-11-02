## What it does

`ask-matt` is the router over this fork's personal active selection. You describe the situation you are in (an idea you cannot start, something broken, a [session](https://www.aihero.dev/ai-coding-dictionary/session) that has run long), and it names the skill or the sequence of skills that fits, plus where the human decisions in that sequence sit.

It recommends and stops. It reads skill definitions before describing their behavior, but does not grill, write a [spec](https://www.aihero.dev/ai-coding-dictionary/spec), or fire the skill it just named; what you get back is the next thing to type, and you type it. It is a hand-written map, not a scan of every installed skill. Recommendations follow this fork's [active registry](https://github.com/brucepucci/skills/blob/main/enabled-skills.json); the [parked registry](https://github.com/brucepucci/skills/blob/main/parked-skills.json) keeps deselected alternatives discoverable without presenting them as active.

## When to reach for it

You invoke this by typing `/ask-matt`; the agent won't reach for it on its own.

| Your situation | What the router gives back |
| --- | --- |
| An idea, and no idea where to start | The head of the main flow, and whether an existing issue has adequate requirements or needs spec work first |
| Something is broken | The [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) on-ramp for a hard bug or regression |
| An idea whose size is unclear | [grill-me](https://aihero.dev/skills-grill-me) for an idea you can hold in one session; explicitly choose [wayfinder](https://aihero.dev/skills-wayfinder) for a large uncertain effort |
| A deselected alternative you want to reconsider | Its entry in the parked registry and its preserved definition, not an installed active workflow |
| A long session and a decision about the [context](https://www.aihero.dev/ai-coding-dictionary/context) | The ordered tree over the five options at a phase boundary |
| A skill you have already picked | Nothing useful. Invoke that skill directly. |

## Prerequisites

The router names skills; it does not install them. The active registry is the sole personal activation authority. The parked registry is informational, and the broader reference docs and plugin distribution still include those preserved skills. Follow this fork's [personal selection guidance](https://github.com/brucepucci/skills#personal-pi-selection) to apply changes; editing the registries alone changes no live discovery links.

The tracker-dependent routes (`to-spec`, `to-tickets`, `implement`, and `wayfinder`) assume [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) has configured an issue tracker in the repo.

## Flows, not skills

For the compact visual map of this fork's active feature route, use the [personal workflow reference](https://github.com/brucepucci/skills/blob/main/docs/workflow.md). It shows alternate entry, optional splitting, review-fix and scope-deferral routes, and successful or partial finish states. Connections are human-chosen next actions, not automatic invocation.

The skill's leading word is **flow**, a path *through* the skills rather than a single skill. When you name your situation, the router places you at a step on a flow. That is a different answer from "here is the skill that matches your keywords". There are five kinds of route, and the skill itself describes them in full:

- **The main flow**, idea to ship: `grill-me` → `to-spec` → optional `to-tickets` → `implement` → `pr` → comprehensive `code-review` → `merge-and-cleanup`. Start with the conversation-only interview even when working in a repo, record issue-backed requirements, then build. [implement](https://aihero.dev/skills-implement) takes one explicitly selected issue through spec validation, a safe feature branch, verification, and a local commit with an unpushed issue handoff. Once requirements and testing are settled, it announces and automatically creates a safe local branch from `main` or the default branch; suitable existing branches are reused. New suggestions honor explicit names and repository conventions, otherwise using a purpose prefix, issue identifier, and very short description. Collisions, obvious mismatches, ambiguity, and unsafe state still pause. Publication with [pr](https://aihero.dev/skills-pr) and review with [code-review](https://aihero.dev/skills-code-review) are separately chosen steps, not automatic continuations. `pr` uses the same naming guidance only when a suggestion is needed, but retains confirmation before creating a branch and does not cosmetically rename suitable existing branches. An unqualified `/pr` authorizes publication; a review-fix request or an existing PR alone does not. It verifies the intended candidate tree in isolation and publishes matching contents with an authoritative issue link or approved inline requirements. Existing-PR follow-ups get one overall delta update and replies to demonstrably addressed inline findings, linking published fixing commits. It leaves uncertain feedback explicit and thread state untouched, resumes missing artifacts without duplicates, and reports partial failures. Explicit preview, body-only, and local-only limits remain binding. It then hands back the URL and a manual comprehensive-review suggestion without implementing more findings. The reviewer resolves those published requirements without relying on the authoring conversation. After review, explicitly choose [merge-and-cleanup](https://aihero.dev/skills-merge-and-cleanup) to squash-merge and safely finish branches and fully delivered issues; neither publication, review, nor this router invokes it automatically. Its normal safe path authorizes completion of clearly identified, fully delivered implementation issues without a second routine confirmation, including issues selected only in the authoritative PR Spec. It trusts applicable comprehensive approval covering each issue's full current requirements rather than reviewing again. Partial or unclear delivery prompts consultation before any merge, even without automatic closing references. Review shortcomings need an explicit head-scoped override, which does not itself authorize issue completion, and GitHub protections still apply. [retro](https://aihero.dev/skills-retro) feeds what the build taught back into the agent's environment. The planning choices are:
  - Use a prototype detour when a question needs runnable code to settle it.
  - Split a larger spec into issues when the build spans sessions, then explicitly select one issue per implementation run.
  - For a small build, select one issue with adequate requirements; a manually authored spec works, but conversation alone does not.
- **On-ramps**, for something broken or an effort too foggy and too large to hold in one session. The latter calls for explicitly choosing `wayfinder`, not an automatic escalation from a small feature.
- **Codebase health**, upkeep rather than feature work. [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) surveys the code for deepening opportunities, and each one it finds re-enters the main flow as an idea.
- **Standalones**, which sit off every flow and which you use on their own: the prototype, the research run, or the message repair with [wait-what](https://aihero.dev/skills-wait-what).
- **A vocabulary layer underneath**, the two references the other skills pull in when the words rather than the process are the problem.

`wayfinder`, `improve-codebase-architecture`, `handoff`, `retro`, and `wait-what` still require explicit user entry. Their supporting calls can proceed normally once started; model-invoked supporting skills also remain independently available.

## The phase boundary

The skill's other key idea is the **phase boundary**. A phase is a chunk of work inside a session (the [grilling](https://www.aihero.dev/ai-coding-dictionary/grilling), the implementation, the QA), and the boundary between two of them is the only place the question "what do I do with this context?" belongs. Mid-phase there is nothing to decide: continue, or split what is left into [subagents](https://www.aihero.dev/ai-coding-dictionary/subagent).

| Option | Take it when |
| --- | --- |
| **Continue** | The next phase wants this one verbatim, or you have [smart zone](https://www.aihero.dev/ai-coding-dictionary/smart-zone) left. It is the only move that keeps the session as a [primary source](https://www.aihero.dev/ai-coding-dictionary/primary-source), so rule it out first |
| **`/clear`** | Everything behind you is disposable. The cheapest option, and you cannot undo it if you were wrong |
| **[handoff](https://aihero.dev/skills-handoff)** | Something has to travel: a new [harness](https://www.aihero.dev/ai-coding-dictionary/harness), a new directory, a colleague, a side task forked mid-phase |
| **Subagent** | The task is scoped tightly enough to run with you [away from the keyboard](https://www.aihero.dev/ai-coding-dictionary/afk) |
| **`/compact`** | None of the above. It is the default, and the tree often ends here |

People often get two of these wrong, which is why the router gives the order and not only the list. `/handoff` looks like the general way to move between context windows, but it is not. All it gives you is portability. `/compact` is the last option in the tree, not the first, because each of the four options above it is cheaper or more precise.

## Common questions

**Isn't there just a list of the skills in the right order?**

This fork now has one canonical visual workflow, linked above and from the README's Personal Pi selection section. It maps idea capture through merge and cleanup, with handoff artifacts and human choices on the connections or in notes. An adequate existing issue can enter directly at `implement`; a conversation-only plan cannot. The broader router still covers situations outside that feature chart, and both references are maintained by hand against the skill definitions.

**It told me half the skills aren't installed.**

User-invoked skills can be installed without appearing in the skill list injected into the agent's context. That list alone does not prove a skill is missing. For this fork's personal selection, check the active registry and the applied discovery links. A parked entry is deliberately deselected, not merely hidden by invocation metadata. For a general plugin installation, its manifest describes the distributed set instead; that is a different installation route.

**It described a skill's behaviour, and the skill doesn't do that.**

This has happened when the router answered from its own one-line summary rather than from the skill. The instructions now require reading the target `SKILL.md` first. One detailed report tracked three instances in a single session, including a recommendation to skip [to-spec](https://aihero.dev/skills-to-spec) based only on the summary "turn the thread into a spec". The router never opened `to-spec/SKILL.md`. In every case it verified only after the user pushed back, and never on its own initiative. Skipping `to-spec` there cost a real seam check, and the tickets that came out undercounted the work. When the router states something about another skill that you will act on, ask it to open that `SKILL.md` first. The same applies to questions the map does not cover at all, such as whether to use [plan mode](https://www.aihero.dev/ai-coding-dictionary/agent-mode): that answer is the [model](https://www.aihero.dev/ai-coding-dictionary/model)'s inference, not something written down here.

**Why is it prose instead of a numbered checklist?**

Use the personal workflow for a quick next-invocation answer along the active feature route. The router's prose carries the wider conditional map: exploration detours, standalone tools, and context decisions. The chart keeps the main route dominant and places optional paths alongside it, with short notes for prerequisites and exceptions rather than another box for every check.

**Can it route over my own skills, or another author's?**

No. Three separate proposals have asked for a router that reads your local `skills/` directory and recommends from whatever is installed. `ask-matt` is not that. It is a map of one set, maintained by hand, and it knows nothing about skills you wrote or installed from elsewhere.

**It told me to edit a SKILL.md.**

That advice is often correct, but the edit rarely lasts. Someone asked it how to make [implement](https://aihero.dev/skills-implement) close tickets, was told to add a line to the skill, and saw the problem at once. `npx skills update` overwrites the file, and the plugin install is read-only. Put standing behaviour in your own `CLAUDE.md` or `AGENTS.md`, or say it in the invocation. Changes you make in the prompt survive updates. People point the flow at Linear instead of GitHub this way, or ask it which open tickets could run in parallel.

**What happened to the six parked skills?**

They are personally deselected, not deprecated or deleted. Their definitions, companion files, and general reference pages remain available. The parked registry lists their paths; [issue #3](https://github.com/brucepucci/skills/issues/3) records why each was parked and when to reconsider it. To re-enable one, move its path from parked to active, check its supporting dependencies, and use the normal apply and reload process. The parked registry never activates skills.

**It named a skill I don't have, or missed one I do.**

Check the personal registries for deliberate deselection and the changelog for a rename before assuming it is gone. `writing-great-skills` became [writing-for-agents](https://aihero.dev/skills-writing-for-agents) with no alias, `to-prd` became [to-spec](https://aihero.dev/skills-to-spec), and `pathfinder` became [wayfinder](https://aihero.dev/skills-wayfinder). Four skills were retired outright into the skills that absorbed them: `ubiquitous-language`, `design-an-interface`, `qa` and `request-refactor-plan`. If it misses a skill you have, that is the router's own lag, described above.

## It's working if

- It ends by naming what to type and stops there, instead of starting the work itself.
- The route it gives back mentions where to clear or compact context and where you are expected to review, not just a list of skill names.
- The main route starts at `grill-me`, and parked alternatives are clearly distinguished from active recommendations.
- Publication, comprehensive review, and merging remain separate choices you make.
- Any claim it makes about another skill's behaviour shows up in the trace as it reading that skill's `SKILL.md`.
- You recognise your own situation in what it hands back, rather than the nearest generic scenario.

## Where it fits

`ask-matt` is a **standalone router** that sits over the whole set. It is never a step in a chain. It points into every chain, and the other docs pages link back to it so none of them has to redraw the graph. From here you most often land on [grill-me](https://aihero.dev/skills-grill-me), the active head of the main flow, or [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs), the on-ramp for something broken. Parked alternatives stay in the registry and general reference docs rather than the active route.

It is a [secondary source](https://www.aihero.dev/ai-coding-dictionary/secondary-source) over the skills it describes. Where the router and a `SKILL.md` disagree, the `SKILL.md` is right.
