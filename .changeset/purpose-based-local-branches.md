---
"mattpocock-skills": patch
---

`implement` now announces and automatically creates a safe local feature branch from `main` or the default branch after requirements and testing decisions are settled. New suggestions in `implement` and `pr` honor explicit names and repository conventions, otherwise using a purpose prefix, issue identifier, and very short description. Suitable existing branches are reused; collisions, obvious mismatches, ambiguity, and unsafe state pause without destructive recovery. `pr` retains confirmation before branch creation, and `implement` retains its issue-backed, local-only handoff. Documentation and router guidance match these boundaries.
