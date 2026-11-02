---
"mattpocock-skills": minor
---

`pr` now verifies and safely publishes intended changes, creates or updates a PR with an authoritative issue link or approved inline requirements, and stops at a manual review handoff. Verification runs on an isolated intended candidate tree, with committed/pushed tree identity checks and fresh verification whenever candidate contents change. Body-only requests remain text-only. `code-review` resolves PR requirements from explicit sources or native linked issues, snapshots requirements and agreed partial scope, and rechecks changing sources before publication without editing requirements. Local review discovery, review modes, and Comment-review semantics are unchanged. Documentation and routing reflect the separate implementation, publication, and user-triggered review steps.
