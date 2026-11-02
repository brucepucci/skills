# Personal workflow reference validation

Scope: [brucepucci/skills#4](https://github.com/brucepucci/skills/issues/4). One canonical chart lives at `docs/workflow.md`; README, `ask-matt`, and its human docs link to it. No skill behavior, activation registry, invocation metadata, plugin manifest, dependency, or runtime infrastructure changed.

## Acceptance walkthroughs

Manually traced the reference against the current definitions of `grill-me`, `to-spec`, `to-tickets`, `implement`, `pr`, `code-review`, and `merge-and-cleanup`, including its preflight, issue-outcome, and cleanup references. These are document-content walkthroughs, not executed skill workflows or rendered-layout tests.

| Scenario | Observed route and handoff |
| --- | --- |
| 1. Draft entry | Entry table uses an ordinary sketch-issue request, says it needs human specification, then names `grill-me`. It invents neither a skill nor a draft label. |
| 2. Existing-spec entry | Entry table permits direct `implement` for one adequate issue, including manually authored requirements. Notes distinguish configured local issue records from loose documents or conversation. |
| 3. Single issue | Solid route separates settled requirements, local commit and unpushed issue handoff, explicit `pr`, fresh comprehensive review with human-selected model/reasoning, and separately invoked finishing. Notes preserve spec/testing validation and safe branch handling without an extra routine branch-name gate. |
| 4. Child issue | Dashed splitting route ends in human selection of one unblocked child. Notes combine parent requirements with explicit child criteria/slice/deferred scope, repeat the cycle per selected child, and leave parent completion independent. |
| 5. Review fixes | Dashed review-to-implementation route selects in-scope fixes on the same issue, stops locally, then reuses separately invoked publication and review. Review itself stays read-only; neither fixing findings nor finding an existing PR grants publication authority. |
| 6. Deferred scope | Separate rows distinguish new work from unmet requirements. Human-approved authoritative edits and a linked follow-up for still-wanted work precede reconciliation, publication, and fresh review. A follow-up alone cannot complete the current PR. Ordinary requests, not a new skill or `to-spec` update behavior, handle edits/capture. |
| 7. Successful finish | Outcome annotation names verified merge, safe source-branch cleanup, fully delivered implementation-issue closeout, and safely updated actual default checkout. Notes qualify review overrides and non-default-target delivery. |
| 8. Blocked or partial finish | Finish table preserves work and distinguishes unmerged blockers from verified merge with partial cleanup/closeout. It reports remaining state and safe actions rather than full success. |

All eight content walkthroughs matched the documented contracts. Planning remains in one context window; each implementation and review starts fresh from durable artifacts. The chart has only active skill nodes and uses solid/dashed routes with an explicit possible-action, no-automation legend. The initial run did not establish visual acceptance; the completed GitHub-rendered inspection is recorded below.

## Executed checks

- `npm run check-plugin-version`: passed, version `1.3.2` remains synchronized.
- `python3 /tmp/skills-issue4.7g6e3s/check-reference.py`: passed local link-target checks, absolute docs-link syntax, changed-prose guards, entry-point links, chart-node membership in the active selection, human-doc section order, and unchanged manifests/selection. This temporary static check is not a Mermaid parser or a behavioral test.
- `gh api --method POST markdown --input -`, with the complete page, `mode=gfm`, and explicit `context=brucepucci/skills`: passed Markdown processing, returning tables and a Mermaid enrichment container. Saved HTML is at `/tmp/skills-issue4.7g6e3s/github-markdown-preview.html`. This preview renders no diagram by itself and creates no issue, comment, branch, or PR.
- `git diff --check` and `git diff --cached --check`: passed.
- `gh issue view 4 --repo brucepucci/skills --json number,title,body,url,updatedAt,state`: re-fetched the authoritative issue before commit; its identifier, title, URL, and full requirements were unchanged from the initial snapshot, and it remained open.
- `claude plugin validate . --strict`: failed with exit 1 on the existing root `CLAUDE.md` warning; it also emitted the existing missing-icon advisory. Repeated against the candidate and a disposable `git archive HEAD` baseline using absolute directory paths. Output and exit status matched exactly after root-path normalization. Logs are `/tmp/skills-issue4.7g6e3s/candidate-plugin.txt` and `baseline-plugin.txt`. This is baseline debt, not a passing check or a fix in this issue.

## Initial inspection limitation

At the initial handoff, GitHub-rendered visual inspection was not completed. The Markdown API returned only a container requiring GitHub's client-side Mermaid renderer. A Safari WebDriver session attempt failed with `session not created` because Allow Remote Automation was disabled. No browser setting was changed, no renderer dependency was installed, and nothing was pushed or posted as a rendering test. This was the outstanding acceptance requirement identified in [PR #21's blocking finding](https://github.com/brucepucci/skills/pull/21#discussion_r4447705541), not a passing inspection.

Local link targets existed, but deployed pages, dictionary links, and final GitHub navigation were initially unchecked. The follow-up below supersedes these inspection gaps without rewriting the historical results.

The FAQ refresh used the selected issue, this fork's related issue titles, existing reader questions, and relevant `CHANGELOG.md` entries. The optional local audience wiki and dictionary checkout were absent. The workflow is a GitHub-facing reference, not another published skill page; the existing `ask-matt` docs retain their page structure and absolute links.

There is no repository test or typecheck script in `package.json`. Runtime TDD does not apply at the approved human-facing documentation seam. No live implementation, PR publication, review, merge, cleanup, or issue-closure workflow was executed for validation. The issue handoff is a separate authorized tracker comment, not a behavioral test. No skill was added, renamed, or removed, so harness linking was not rerun. Temporary evidence may not survive later cleanup.

## Completed GitHub-rendered inspection

On 2026-11-02, inspected [the actual GitHub page at reviewed head `fbbec06`](https://github.com/brucepucci/skills/blob/fbbec061bcd6f87f164a5acb59c9496065c8163b/docs/workflow.md). The inspected file's Git blob is `a7b71c771704703a976727caf287a0aed23b3f41`; this follow-up changes only this validation record, so the rendered page, diagram source, entry points, and supporting notes remain byte-identical.

### Method and evidence

Used the operating system's existing AppKit/WebKit frameworks through temporary Swift inspection scripts on macOS 27.2 (Swift 6.4.2). A `WKWebView` loaded the live, public GitHub commit URL and executed GitHub's own client-side renderer, including its `viewscreen.githubusercontent.com/markdown/mermaid` iframe. This was not the Markdown API preview, a local Mermaid replacement, or an inferred render. No Safari setting, repository dependency, skill behavior, or permanent testing infrastructure changed.

Commands and observed outputs:

- `swift /tmp/skills-issue4-render.9ZITcP/inspect.swift https://github.com/brucepucci/skills/blob/fbbec061bcd6f87f164a5acb59c9496065c8163b/docs/workflow.md /tmp/skills-issue4-render.9ZITcP`: loaded the live GitHub page and rendered iframe; captured `chart-full.png`, `reference-full.png`, `page.json`, and `render-frame.json`. The final capture used a 1500 CSS-pixel-wide view with extra vertical space for full-page snapshots. The rendered diagram had viewBox `-36 -36 673 1296`. Inspected the chart image and readable crops of the supporting notes, not just DOM text or renderer-ready flags.
- `swift /tmp/skills-issue4-render.9ZITcP/navigation.swift /tmp/skills-issue4-render.9ZITcP`: clicked the rendered README's Personal Pi selection link and the rendered `ask-matt/SKILL.md` routing link. Both reached the exact same commit-pinned workflow URL and a ready rendered chart; both results passed in `navigation.json`.
- `python3 /tmp/skills-issue4-render.9ZITcP/check-links.py`: a standard-library HTTP check of all 14 outgoing, non-anchor reference links returned successful responses: ten GitHub targets returned HTTP 206 to range requests, and the four dictionary targets returned HTTP 200. Results are in `links.json`.

After recording the inspection, reran `npm run check-plugin-version`, `python3 /tmp/skills-issue4.7g6e3s/check-reference.py`, and `git diff --check`: all passed. `claude plugin validate . --strict` still exited 1 with the same baseline warnings; its follow-up output is in `/tmp/skills-issue4-render.9ZITcP/plugin.txt`. The staged whitespace check is also run before commit.

The browser/navigation scripts are temporary inspection tools, not repository test commands or an automated skill-evaluation system. The GitHub-generated screenshots and JSON evidence remain under `/tmp/skills-issue4-render.9ZITcP`; the observations and pinned source identity here are the durable record.

### Observed acceptance results

| Subject | Actual rendered result |
| --- | --- |
| Render and readability | All seven skill boxes and their handoff labels rendered legibly. No syntax error, clipped label, or overlapping box was observed. The long finishing skill name wraps inside its box without losing meaning. |
| Main route | The solid route is traceable top-to-bottom from `grill-me` through publication and comprehensive review to `merge-and-cleanup`. Its thicker node borders distinguish it from the optional split node. |
| Optional routes | Splitting appears to the right of the main route; review-fix and deferral arrows return alongside it. Dashed connections are visibly distinct, their directions are readable, and their labels identify selection, same-issue fixes, approved scope edits/follow-up, and republishing/re-review. |
| Legend and outcomes | The visible legend distinguishes solid and dashed routes and explicitly says possible next actions, not automatic invocation. The successful-finish annotation and blocked/partial/non-default-target table render clearly below the chart. |
| Entry and notes | The entry table and supporting lists/tables render without lost content. Re-walked all eight scenarios above on the rendered page: direct adequate-issue entry, child selection/inheritance, local-only fixes, separate publication/review, approved deferral, and exact finish states remain distinguishable. |
| Required entry navigation | Both required entry-point clicks reached the canonical workflow at the inspected head. Its active-selection, skill-reference, and dictionary links all returned successful HTTP responses. |

No chart or routing-content correction was needed after inspection. This completes the previously missing rendered inspection and records the actual result; it is not reviewer approval or a claim of live workflow execution.

### Remaining bounded limitations

- Inspected the desktop/light presentation in WebKit only, not a browser/device/theme matrix. Diagram interaction controls were not exhaustively tested.
- The human-facing `ask-matt` docs intentionally link to `blob/main/docs/workflow.md`. An explicit live check returned HTTP 404 because this new page has not merged to main. The commit-pinned page and both required relative entry routes work. The main URL must be rechecked after delivery to main; no pre-merge availability is claimed and no issue scope was changed to excuse it.
- HTTP link checks establish reachability, not a content audit of every external page or the eventual aihero.dev deployment.
- The existing strict-plugin warning remains baseline debt. No runtime test/typecheck script exists. No review was invoked, no review thread was resolved, and no publication, merge, branch cleanup, or issue closure was performed by this implementation follow-up.
