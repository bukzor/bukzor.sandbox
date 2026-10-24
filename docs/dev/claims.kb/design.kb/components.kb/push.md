---
label: PUSH
standing: user
todo: true
authority:
  address: "sandbox-create (f39ab32c)"
  words: "A `push` would/could update gha's SANDBOX_SUBPATH to match local definitions. -- agreed, and approved."
  about: "a verb writing the record's hierarchy to GitHub"
why:
  - ../components.md
  - ../architecture.kb/hierarchy-on-github.md
  - diff.md
---

# push

Writes the record's hierarchy to GitHub: for each record file in
`sandbox-repo.kb/`, sets its repository's `SANDBOX_SUBPATH` to the
record's directory wherever the two differ. A record moved locally
reaches GitHub at the next `push`; `diff` shows what a `push` would
change.
