---
label: BINDING
standing: user
authority:
  address: "nih-tooling-deliberation (6008d1)"
  words: "all looks good. approved."
  about: "the ledger rendered in chat, RECORD and COLLOCATION signed ! within it"
why:
  - binding.kb/llm-kb-record.md
  - ../goals.kb/hierarchy.md
  - ../../technical-policy.kb/location-independence.md
---

# What binds a subordinate to the parent

A sandbox is bound to the parent by a record file in the parent's
`sandbox-repo.kb/` collection (`binding.kb/llm-kb-record.md`). The
file's existence is the membership, its position in the collection is
the sandbox's place in the hierarchy, and its frontmatter carries the
metadata existence cannot.

The candidates, chosen and declined, are in `binding.kb/`. The two
constraints that decided among them: the hierarchy has one
authoritative record, able to nest and to carry free-form metadata,
and nothing committed in a sandbox may name the parent's location.
GitHub holds a copy of each sandbox's place, written from the record
(`hierarchy-on-github.md`).
