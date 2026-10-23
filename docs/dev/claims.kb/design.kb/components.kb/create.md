---
label: CREATE
standing: user
todo: true
authority:
  address: "nih-tooling-deliberation (6008d1)"
  words: "My rough first draft: - create"
  about: "the minimal set of verbs for sandbox repos"
why:
  - ../components.md
  - ../architecture.kb/binding.kb/llm-kb-record.md
  - ../architecture.kb/collocation.md
---

# create

Brings a new sandbox into existence at a chosen place in the
hierarchy: creates the GitHub repository with `gh repo create`, writes
the record file at the given path in `sandbox-repo.kb/`, and clones
the new repository beside it. Afterwards the sandbox is a member, has
a place, and has a checkout.
