---
label: REUSE_SEMANTICS
standing: user
force: should
authority:
  address: "sandbox-create (f39ab32c)"
  words: "reuse preexisting semantics: where behavior is underdetermined, find a preexisting analogue to pull prior precedent from"
  about: "how open details of the verbs get settled"
---

# Underdetermined behavior takes a preexisting analogue's precedent

Where the design leaves a behavior open -- a flag, a default, an error,
an edge case -- it is settled by finding an existing tool that does
the analogous thing and adopting its answer, spellings included
(`exact-string-equality.md`). Invention is the fallback for when no
analogue fits.

The operator's knowledge of the analogue then predicts the behavior,
the precedent has already been argued and tested by the analogue's
users, and the record settles an edge case by citing the analogue
instead of arguing it afresh.

> [!DRAFT] sandbox-create (f39ab32c)
> The analogue is the tool that does the same operation on the
> closest kind of object. A sandbox's place in the hierarchy is a
> path, so placement follows the filesystem
> (`sandbox-semantics.md`); a property of the GitHub repository
> follows `gh`.
