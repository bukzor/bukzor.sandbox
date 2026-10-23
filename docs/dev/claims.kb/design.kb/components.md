---
label: COMPONENTS
standing: user
todo: true
authority:
  address: "nih-tooling-deliberation (6008d1)"
  words: "all looks good. approved."
  about: "the ledger rendered in chat, including this rung proposed + beneath architecture"
why:
  - architecture.md
  - ../technical-policy.kb/own-scripts.md
ontology:
  - verb
---

# Components

**How do we implement the architecture?**

The parent's tooling is one script whose subcommands are the *verbs*
below, one claim per verb in `components.kb/`. A verb is a named
operation on the set of sandboxes that composes several `gh` and
`git` commands; an operation that is one command is not a verb
(`../technical-policy.kb/single-command-unwrapped.md`).

A verb claim states what the operation does to the record, the
clones, and GitHub. It carries `todo: true` until the subcommand
exists, and `standing: open` while whether it should exist at all is
undecided.
