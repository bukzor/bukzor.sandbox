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
  - ../architecture.kb/hierarchy-on-github.md
---

# diff

Compares the sandboxes GitHub knows about with the record files in
`sandbox-repo.kb/`, in both directions, and reports:

- repositories carrying `SANDBOX_SUBPATH` with no record;
- records whose repository is gone or renamed;
- repositories whose `SANDBOX_SUBPATH` differs from their record's
  directory -- what `push` would change.

GitHub and the record are two stores that drift, and this is the
reconciliation. On GitHub's side, a sandbox is a repository carrying
`SANDBOX_SUBPATH` (`../architecture.kb/hierarchy-on-github.md`).
