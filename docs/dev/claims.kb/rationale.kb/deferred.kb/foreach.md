---
label: FOREACH
standing: user
todo: true
authority:
  address: "nih-tooling-deliberation (6008d1)"
  words: "foreach -- run a command against each"
  about: "the minimal set of verbs for sandbox repos"
why:
  - ../../design.kb/components.md
  - ../../design.kb/architecture.kb/collocation.md
---

# foreach

Runs a given command in every clone, walking the record and looking
beside each file for its checkout. The other walking verbs are this
one with a fixed command.
