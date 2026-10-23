---
label: PUBLICATION_IN_CONFIG
standing: agent
force: should
why:
  - ../design.kb/deliverables.kb/tooling-is-a-workspace-package.md
  - ../design.kb/goals.kb/graduation-is-a-rename.md
---

# Whether a package is published is its own configuration

A package's position under `packages/` says nothing about whether it
is published. Publication is declared in the package's own
`pyproject.toml`: a repo-local package carries the classifier
`Private :: Do Not Upload`, which PyPI refuses to accept, and a
published one has had that line removed and a trusted publisher
registered.

Separate trees for local and published packages would make a first
release a directory move, and a move renames every path that cites
the package: workspace sources, README links, CI tag matching.
Graduation in this design is a rename and nothing more
(`../design.kb/goals.kb/graduation-is-a-rename.md`); a package's
graduation to published should cost one line.
