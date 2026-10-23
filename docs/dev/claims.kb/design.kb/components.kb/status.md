---
label: STATUS
standing: user
todo: true
authority:
  address: "nih-tooling-deliberation (6008d1)"
  words: "status -- show if local is out of date"
  about: "the minimal set of verbs for sandbox repos"
why:
  - ../components.md
  - ../architecture.kb/collocation.md
---

# status

Reports, per clone, whether the checkout is behind or ahead of its
remote, and whether it has uncommitted work. One line per sandbox,
walking the record and looking beside each file for its clone.
