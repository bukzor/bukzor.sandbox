---
label: GH_HIERARCHY
standing: user
authority:
  address: "sandbox-create (f39ab32c)"
  words: "agreed, and approved."
  about: "the proposal in chat: the tree keyed by subject, stage kept in the name, SANDBOX_SUBPATH written to GitHub by push, dotted names declined"
why:
  - ../../design.kb/architecture.kb/binding.md
  - ../../design.kb/architecture.kb/tree-axis.md
  - ../../design.kb/goals.kb/hierarchy.md
---

# How GitHub carries each sandbox's place in the hierarchy

Each sandbox's repository carries the Actions variable
`SANDBOX_SUBPATH`, holding the directory of its record within
`sandbox-repo.kb/` (`sandbox-subpath-variable.md`).
GitHub data alone then recovers the tree: the variable's presence
marks a repository as a sandbox, and its value joined to the
repository's name is the record's path.

The record stays the authority. The variable is written from it, and
checked against it; the two may drift between those moments, and
nothing reads the variable as a source of truth over the record.

The declined alternative is dotted names (`../declined.kb/dotted-names.md`).
The constraint that decided between them: the tree is keyed by subject
(`../../design.kb/architecture.kb/tree-axis.md`), and a name's leading segment is its stage.
