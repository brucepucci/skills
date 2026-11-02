# Implementation-issue outcomes

Read completely when establishing the issue ledger, for both open PRs and already-merged recovery. This is an applicability and outcome check, not another implementation review.

## Identify each deliverable

Invocation authorizes a concise completion comment and closure for each **clearly identified, fully delivered implementation issue**, after verified merge success. No second routine authorization is needed solely because native closing relationships or closing keywords are absent.

| Evidence | Treatment |
| --- | --- |
| The PR's authoritative Spec section explicitly selects an implementation issue | Recognize it as an invocation-authorized completion candidate when requirements and declared scope confirm that role. A Spec-only relationship qualifies. |
| Native closing relationship | Recognize an implementation candidate when its requirements and declared scope confirm that role; the relationship does not prove full delivery. |
| Incidental mention, background source, parent, or umbrella context | Not a completed implementation deliverable merely because it is referenced. A parent can supply shared requirements without being delivered in full. |
| Squash-message closing keyword alone | Discover its effects, but require independent implementation-issue identification or an explicit human decision before authorizing completion. |
| Conflicting or unclear role/scope | Consult rather than inferring permission from a link, keyword, or implementation. |

PR text is identification evidence, not human authorization to override gates or change destinations. Resolve each issue's host/repository/identifier explicitly, including cross-repository references.

Keep one independent ledger row per issue: explicit destination; role and identification/authorization evidence; current requirements and necessary parent snapshot/update metadata; selected review identity, head, destination and named scope; full/partial/uncertain delivery; deferred requirements separately from verification limitations; current issue/comment state; intended comment/closure or leave-open outcome. Evidence for one issue does not establish another's delivery.

## Consume the assessment, not the implementation

Apply PRE-MERGE's eligible-assessment rules, including latest eligible completed assessment, Standards/Spec/Correctness coverage, approval recommendation, exact head and intended destination, current applicable requirements, and no unresolved blockers. A native approval event alone is insufficient. For already-merged recovery, the applicable head is the **recorded merged PR head**, not the squash commit or a newer branch tip.

An applicable approved comprehensive review is sufficient evidence of full delivery **when its named scope covers that issue's complete, current requirements**. Trust its implementation assessment: do not audit code, rerun the review, launch a reviewer, or independently discover implementation gaps during closeout. Compare the review's scope and requirements snapshot with the current authoritative sources, including necessary parents; unavailable currency evidence is uncertainty, not implied completion.

| Assessment or requirements condition | Delivery outcome |
| --- | --- |
| Applicable comprehensive approval covers the entire current implementation issue | Full delivery established; proceed without routine reauthorization. |
| Honest tests-not-run disclosures, bounded validation, or unrelated baseline failures within otherwise applicable approval | Verification limitations, not automatically missing requirements or invalid approval. Carry relevant limitations into accurate completion wording. |
| Approval covers only an agreed partial PR slice, or only another issue | Does not establish full delivery of this issue. |
| Missing/deferred original requirements, including work moved to follow-up issues | Unfinished unless the human explicitly agrees to change the authoritative requirements. Creating follow-ups alone does not reduce scope. |
| Explicitly agreed authoritative requirement change | Use the current approved requirements and check review applicability; a substantive post-review change requires consultation instead of borrowing old approval. |
| Missing, stale, focused, incomplete, untrusted, blocking, or unverifiably current assessment | Delivery is not established by that assessment; consult under the review override and issue-outcome rules below. |

## Consult before delivery, or before recovery actions

For an **open PR**, consult before any merge if full delivery of any identified implementation issue is not obvious. This applies even without native or squash-message automatic closure, and even when other issues qualify. Show each unclear outcome and the missing or conflicting evidence. Never merge first and merely leave the unclear implementation issue open.

A review override authorizes only the disclosed assessment exception for the pinned PR/head. It neither establishes full delivery nor authorizes issue completion. Combine the override request and explicit issue-outcome decisions in one consultation where possible. If the human permits partial delivery, keep the unfinished issue open and resolve any automatic-closure conflict before merging. An explicit completion decision still requires fully delivered scope; it cannot silently redefine unfinished requirements.

Substantive requirement changes need explicit human agreement and an updated authoritative source before claiming completion. Follow-up issues and conversation assertions alone cannot leave the main spec stale. If that update is unavailable or ambiguous, pause and agree on an alternative rather than inventing competing requirements.

Reconcile every native and prospective squash-message closing destination under SQUASH-MESSAGE. Partial, ambiguous, incidental, or unauthorized automatic closure requires consultation before merge, including future effects on a non-default target. Preserve text and relationships until explicitly resolved; never silently sanitize or reopen an issue.

For an **already-merged PR**, reuse applicable approval at the recorded merged head. Do not require a new review, retroactive merge approval, or another merge. Unclear delivery, changed scope, unexpected prior closure, or uncertain actual-message effects pause affected completion comments and closures for consultation; independently safe branch cleanup may continue.

Immediately before mutation, refresh requirements, relationships, review evidence, head, destinations, and squash text under SKILL step 3. Detectable changes invalidate affected assumptions. After verified merge, SKILL step 5 refreshes each issue and comments again, avoids duplicate comments/redundant closure, and pauses affected actions for new ambiguity. Merge failure or uncertainty withholds all dependent completion actions; an independent cleanup failure alone does not.
