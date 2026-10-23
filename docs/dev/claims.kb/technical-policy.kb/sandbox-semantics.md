---
label: SANDBOX_SEMANTICS
standing: user
force: should
authority:
  address: "sandbox-create (f39ab32c)"
  words: "SANDBOX_SEMANTICS <- \"reuse preexisting semantics\": we reuse filesystem semantics for create, move errors"
  about: "the error behavior of the verbs that place a sandbox"
why:
  - reuse-preexisting-semantics.md
  - ../design.kb/architecture.kb/collocation.md
---

# A sandbox's path follows filesystem semantics

Creating or moving a sandbox fails where creating or moving a
filesystem entry at the same path would, on the same conditions and
with the same messages: `create` follows `mkdir`, and `move` follows
`mv`. Paths resolve against the working directory, as theirs do.

The filesystem is the closest analogue because a sandbox occupies
a path in `sandbox-repo.kb/`, and the hierarchy on disk is the
hierarchy of sandboxes (`../design.kb/architecture.kb/collocation.md`).

> [!DRAFT] sandbox-create (f39ab32c)
> One departure: `mv` silently replaces an existing file at its
> target. A sandbox move onto an existing sandbox fails instead, as
> `mv` does onto a non-empty directory, because the entry it would
> replace is a repository.
