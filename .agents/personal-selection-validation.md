# Personal selection validation

Scope: [brucepucci/skills#3](https://github.com/brucepucci/skills/issues/3). The change parks six personal selections without changing their definitions, companion files, invocation metadata, buckets, or general plugin distribution.

## Behavioral seam

Run from this repository:

```bash
python3 scripts/test-personal-selection.py /path/to/dotfiles
```

The test requires an existing `brucepucci/dotfiles` checkout and `chezmoi`. It copies the candidate skill content and manifests into a disposable home, seeds checkout-owned discovery links for the previous 28 selections, and exercises the existing dotfiles hook with real `chezmoi apply --include=scripts`. HOME, XDG directories, chezmoi cache, configuration, and persistent state are isolated. The dotfiles checkout is only a source; no packages are installed.

Observed with dotfiles at `74008f4`:

- **Red:** before changing the manifests, discovery still included exactly the six intended parked names, so the expected active-selection assertion failed.
- **Green:** the candidate exposed all 22 active skills through links to their copied source directories and removed all six parked checkout-owned links.
- Dry-run left discovery unchanged. A second apply left link targets and inodes unchanged.
- An unrelated directory, external symlink, broken external symlink, and unmanaged skill lock were preserved.
- Hashes of all copied skill files stayed unchanged across reconciliation, including parked companion files.
- Both registries passed array, relative-path, containment, existing-directory, uniqueness, exact membership, and disjointness checks.
- With the active manifest set to an empty array only in the disposable fixture, no parked skill was activated. Unrelated skills and source files remained intact.

The test uses the existing local-checkout consumer, not a simulated installer or a private helper. It does not run a full dotfiles configuration apply, launch agent workflows, or test Pi reload. No real-home discovery links were reconciled.

## Static and documentation checks

Inline Python assertions and manual inspection confirmed:

- The registries' union equals the existing 28-entry baseline manifest, retaining `merge-and-cleanup` and every approved support dependency.
- `wayfinder`, `improve-codebase-architecture`, `handoff`, `retro`, and `wait-what` retain byte-identical skill definitions and OpenAI metadata, including both explicit-entry restrictions.
- `grilling`, `tdd`, `codebase-design`, `writing-for-agents`, `domain-modeling`, `research`, and `prototype` remain independently model-invoked and selected. The retained skills' explicit supporting calls target available skills.
- Only `ask-matt/SKILL.md` changes under `skills/`; parked sources and their general docs stay intact. Plugin manifests are unchanged.
- The router starts at `grill-me`, retains one-issue implementation and separate publication, comprehensive review, and merge steps, and points to the informational parked registry rather than recommending parked execution routes.
- Re-enable guidance moves entries from parked to active, accounts for supporting dependencies, and keeps apply/reload separate. The personal README now describes the existing checkout-link consumer rather than its obsolete remote-cache predecessor.
- Changed prose has no em-dashes; local Markdown links resolve.

The docs question hunt used this fork's issues (`gh issue list --repo brucepucci/skills --search ask-matt --state all`), the selected issue, existing reader questions on the page, and relevant `CHANGELOG.md` entries. The optional audience wiki and dictionary checkout were absent.

## Repository checks and limitations

- `python3 scripts/test-personal-selection.py /Users/bp/gh/dotfiles`: passed repeatedly after the manifest change.
- `npm run check-plugin-version`: passed.
- `git diff --check`: passed.
- `claude plugin validate .`: passed with the existing root `CLAUDE.md` warning and missing-icon advisory.
- `claude plugin validate . --strict`: failed with status 1 on the existing root `CLAUDE.md` warning. Reproduced the same failure with `claude plugin validate <baseline-directory> --strict` in a disposable `git archive` of unchanged baseline `88a7703`. This is the pre-existing problem in [issue #13](https://github.com/brucepucci/skills/issues/13), not verified success or a regression fixed here.
- No repository typechecking or general test command is provided in `package.json`. No new package installation or test framework was added.
- `git -C /Users/bp/gh/dotfiles status --short --branch`: remained clean on `main` after verification.
- Live apply/reload, publication, PR review, and merging were not performed.
