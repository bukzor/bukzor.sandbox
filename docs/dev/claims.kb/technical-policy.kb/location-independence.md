---
label: LOCATION_INDEPENDENCE
standing: user
force: must
authority:
  address: "nih-tooling-deliberation (6008d1)"
  words: "Errors and malfunction due to unexpected git-clone locations is a terrible smell. Just as a single example, your proposal is deeply incompatible with worktrees."
  about: "a sandbox CLAUDE.md importing the parent's by absolute path"
why:
  - ../design.kb/goals.kb/graduation-is-a-rename.md
---

# A sandbox never depends on where another repo is cloned

Nothing committed inside a sandbox refers to the on-disk location of
any other repository, the parent included. A sandbox checked out
alone, in a worktree, or under a different directory layout behaves
identically.

The coupling this forbids breaks under worktrees and under any clone
layout other than the one the author had. It would also make
graduation more than a rename, since the graduate would carry a
reference to a parent it no longer has.
