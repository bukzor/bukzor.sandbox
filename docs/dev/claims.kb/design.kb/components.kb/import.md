---
label: IMPORT
standing: user
todo: true
authority:
  address: "nih-tooling-deliberation (6008d1)"
  words: "let's reuse the terraform conventional verb here: \"import\""
  about: "the verb that binds an already-existing repository"
why:
  - ../components.md
  - ../architecture.kb/llm-kb-record.md
  - ../architecture.kb/collocation.md
  - ../goals.kb/both-populations.md
---

# import

Binds a repository that already exists on GitHub: writes the record
file at the given path in `sandbox-repo.kb/`, places a checkout beside
it, cloning afresh or moving an existing checkout. The record's stem
is the repository's name. The verb is Terraform's, for the same
operation: adopting a resource that was made elsewhere into the
record. It is how the existing prefixed siblings migrate in.
