---
label: DOTTED_NAMES
standing: user
verdict: rejected
authority:
  address: "sandbox-create (f39ab32c)"
  words: "do we really want to live with three, four, five dotted-segment repos? ... do we really want to organize by `prototype` etc at the top of our hierarchy? -- agreed, and approved."
  about: "the repository name spelling the record's path, dots for slashes"
why:
  - ../deferred.kb/hierarchy-on-github.md
  - ../../design.kb/architecture.kb/tree-axis.md
  - ../../design.kb/goals.kb/add-organization-remove-none.md
---

# Dotted names: the repository name spells the record's path

The record `sandbox-repo.kb/research/graphics/opus.md` would be the
repository `research.graphics.opus`, each dot a directory. The tree
would show in every flat listing, the owner page included, with no
store but the name, and the existing prefixed repositories would bind
at `prototype/`, `research/`, and so on with no rename.

Rejected because a name's leading segment is its stage, so the tree
would be keyed by stage, and the tree is keyed by subject
(`../../design.kb/architecture.kb/tree-axis.md`). Subject first would rename every existing
sandbox, against `../../design.kb/goals.kb/add-organization-remove-none.md`.
The scheme's other costs, each smaller:

- Every reorganization is a public rename.
- No sandbox name may contain a dot of its own.
- Names of three segments and more become routine.
