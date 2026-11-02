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

All eight content walkthroughs matched the documented contracts. Planning remains in one context window; each implementation and review starts fresh from durable artifacts. The chart has only active skill nodes and uses solid/dashed routes with an explicit possible-action, no-automation legend. **Actual visual dominance, readability, connection placement, and Mermaid syntax/rendering remain unverified.**

## Executed checks

- `npm run check-plugin-version`: passed, version `1.3.2` remains synchronized.
- `python3 /tmp/skills-issue4.7g6e3s/check-reference.py`: passed local link-target checks, absolute docs-link syntax, changed-prose guards, entry-point links, chart-node membership in the active selection, human-doc section order, and unchanged manifests/selection. This temporary static check is not a Mermaid parser or a behavioral test.
- `gh api --method POST markdown --input -`, with the complete page, `mode=gfm`, and explicit `context=brucepucci/skills`: passed Markdown processing, returning tables and a Mermaid enrichment container. Saved HTML is at `/tmp/skills-issue4.7g6e3s/github-markdown-preview.html`. This preview renders no diagram by itself and creates no issue, comment, branch, or PR.
- `git diff --check` and `git diff --cached --check`: passed.
- `gh issue view 4 --repo brucepucci/skills --json number,title,body,url,updatedAt,state`: re-fetched the authoritative issue before commit; its identifier, title, URL, and full requirements were unchanged from the initial snapshot, and it remained open.
- `claude plugin validate . --strict`: failed with exit 1 on the existing root `CLAUDE.md` warning; it also emitted the existing missing-icon advisory. Repeated against the candidate and a disposable `git archive HEAD` baseline using absolute directory paths. Output and exit status matched exactly after root-path normalization. Logs are `/tmp/skills-issue4.7g6e3s/candidate-plugin.txt` and `baseline-plugin.txt`. This is baseline debt, not a passing check or a fix in this issue.

## Unavailable inspection and limits

GitHub-rendered **visual inspection was not completed**. The Markdown API only returns a container that requires GitHub's client-side Mermaid renderer. A Safari WebDriver session attempt failed with `session not created` because Allow Remote Automation is disabled. No browser setting was changed, no renderer dependency was installed, and nothing was pushed or posted as a rendering test. Rendered chart inspection remains a manual prerequisite to claiming the reference fully validated; the eight walkthroughs above evaluate content only.

Local targets of added links exist, including the canonical page and every linked skill. Absolute workflow URLs under `blob/main` become available only after publication to that branch. Deployed docs, external dictionary links, and final GitHub page navigation were not checked.

The FAQ refresh used the selected issue, this fork's related issue titles, existing reader questions, and relevant `CHANGELOG.md` entries. The optional local audience wiki and dictionary checkout were absent. The workflow is a GitHub-facing reference, not another published skill page; the existing `ask-matt` docs retain their page structure and absolute links.

There is no repository test or typecheck script in `package.json`. Runtime TDD does not apply at the approved human-facing documentation seam. No live implementation, PR publication, review, merge, cleanup, or issue-closure workflow was executed for validation. The issue handoff is a separate authorized tracker comment, not a behavioral test. No skill was added, renamed, or removed, so harness linking was not rerun. Temporary evidence may not survive later cleanup.
