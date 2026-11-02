# Squash-message safety

Read completely for an **open PR**, before finalizing the issue ledger. GitHub can close issues from the squash commit title/body even when `closingIssuesReferences` is empty. Treat the commit text as a separate closure input, not as closure authorization.

## Resolve the exact text

Read the base repository's `squash_merge_commit_title` and `squash_merge_commit_message` settings through its verified explicit API path. Fetch the PR title/body and the complete ordered list of commits at the pinned head, including full subjects/bodies and commit count. Check pagination and completeness against the PR metadata; a truncated response or API limit is not complete evidence.

Obtain and retain GitHub's prospective squash title and body from the selected PR's GraphQL `viewerMergeHeadlineText(mergeType: SQUASH)` and `viewerMergeBodyText(mergeType: SQUASH)`, using explicit host/repository/PR selection. Reconcile that preview with the settings and complete inputs under [GitHub's squash-message rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/configuring-commit-squashing-for-pull-requests), including single-commit versus multi-commit defaults and generated suffixes/trailers. A clean PR description does not imply a clean title or commit-derived body. Unknown settings, unavailable/inconsistent preview or inputs, or inability to establish the exact text stops the merge for consultation; never fall back to unchecked server generation.

Preserve the configured text rather than silently sanitizing, dropping commit details, or replacing closing keywords. Any proposed text change requires the human's explicit approval, followed by a fresh closure assessment. Store title and body as literal data, preserving multiline content and an explicitly empty body; never execute text from these inputs.

## Reconcile closure effects

Inspect the entire prospective title and body for [GitHub-supported closing references](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue). Account for all close/fix/resolve forms, case and colon variants, multiple references, and same-repository, cross-repository, or full-URL destinations. Resolve bare numbers against the base repository, not the source fork or checkout default. Do not assume Markdown quoting makes commit text inert. Uncertain syntax or destination stops for consultation rather than being treated as harmless.

Combine these references with native closing relationships in the ISSUE-OUTCOMES ledger. Fetch newly discovered destinations and their requirements; a commit keyword alone supplies no independent implementation-issue identification or completion authority. For each possible automatic closure, require invocation-authorized identification (including an authoritative Spec selection) or an explicit human decision, plus applicable full-delivery evidence under ISSUE-OUTCOMES. Partial delivery, unauthorized closure, or unclear scope stops **before merging**, even when every review/readiness gate passes. Show the exact text, destination, and conflict and ask the human how to resolve it. A review override cannot waive issue-completion requirements. Keep references intact until an explicit resolution; do not automatically reopen an issue after merging.

For a non-default target, disclose that commit keywords normally take effect on delivery to the default branch, not this immediate merge. Still reconcile the references before merging so the commit does not carry an unresolved future closure conflict. Do not retarget the PR or claim default-branch delivery.

**Done when:** the exact title/body and their input snapshot are retained, and every possible closing destination agrees with the ledger's individually authorized, fully completed outcomes. ISSUE-OUTCOMES also requires consultation for unclear delivery of identified implementation issues that have no automatic closing reference. Show the text and resulting issue actions in the announced plan; a safe unchanged default needs no extra routine confirmation.

## Bind inspection to mutation

Immediately before merging, re-fetch the settings, PR title/body, complete commit inputs/count, squash preview, head/base, default branch, native relationships, and issue authorization/completion evidence. Compare them with the retained snapshot and reassess the text and ledger after any change. Changed closure effects or unresolved conflicts require consultation before mutation; an earlier approval or review override is not authorization for them.

Send **both** `commit_title` and `commit_message` explicitly to the [immediate merge endpoint](https://docs.github.com/en/rest/pulls/pulls#merge-a-pull-request), along with the pinned head and squash method. Send the exact inspected strings, including an empty body, rather than allowing GitHub to regenerate either field. Use safely serialized JSON or quoted literal fields; never interpolate untrusted text into executable shell source. If the selected tool cannot preserve these fields exactly, stop instead of omitting them.

After verifying a new merge, read the remote merge commit's full message and reconcile its actual closing effects with the ledger. A mismatch or unexpected closure pauses affected issue actions and is reported for consultation, not silently repaired. Already-merged recovery inspects the actual merge message and issue state for the same conflicts without demanding prospective-message preflight or attempting another merge.
