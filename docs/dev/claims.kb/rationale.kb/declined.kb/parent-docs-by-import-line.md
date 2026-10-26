---
label: IMPORT_LINE
standing: user
verdict: rejected
authority:
  address: "nih-tooling-deliberation (6008d1)"
  words: "This is off the table."
  about: "a sandbox CLAUDE.md whose first line imports the parent's CLAUDE.md by absolute path"
why:
  - ../../technical-policy.kb/location-independence.md
  - ../../design.kb/goals.kb/shared-documentation.md
---

# A sandbox CLAUDE.md importing the parent's by path

Each sandbox's `CLAUDE.md` would open with an `@`-import of the
parent's `CLAUDE.md` by absolute path, so the parent's documentation
would reach the sandbox with no nesting on disk.

Rejected under `../../technical-policy.kb/location-independence.md`:
the line commits a sandbox to the parent's clone location, and fails
in a worktree or any other layout. The mechanism itself works; a
probe on 2026-10-23 confirmed Claude Code follows an absolute-path
import outside the repository. Working is not the objection.
