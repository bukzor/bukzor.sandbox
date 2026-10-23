---
label: DIFF
standing: user
todo: true
authority:
  address: "nih-tooling-deliberation (6008d1)"
  words: "diff -- compare my gh-repo-list to what's in this repo"
  about: "the minimal set of verbs for sandbox repos"
why:
  - ../components.md
  - ../architecture.kb/binding.kb/llm-kb-record.md
  - ../../technical-policy.kb/every-sandbox-carries-the-sandbox-topic.md
---

# diff

Compares the sandboxes GitHub knows about with the record files in
`sandbox-repo.kb/`, in both directions: repositories with no record,
and records whose repository is gone or renamed. GitHub and the
record are two stores that drift, and this is the reconciliation.

Which GitHub repositories count as sandboxes on GitHub's side is a
predicate this verb needs and does not own: the name-prefix
convention, a topic, or both. The topic question is open
(`../../technical-policy.kb/every-sandbox-carries-the-sandbox-topic.md`).
