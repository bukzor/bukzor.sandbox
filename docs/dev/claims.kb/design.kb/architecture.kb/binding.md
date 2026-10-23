---
label: BINDING
standing: open
why:
  - ../goals.kb/the-parent-stays-thin.md
  - ../goals.kb/add-organization-remove-none.md
---

# What binds a subordinate to the parent?

> [!QUESTION]
> Undecided. An answer settles three things at once: whether the
> parent carries a gitlink per sandbox, whether a sandbox is nested
> on disk under the parent, and what the create, graduate, and
> delete procedures must touch in the parent. The candidates are in
> `binding.kb/`, chosen and declined alike once ruled; until then
> nothing here is implemented.

What any answer must provide:

- an index: every sandbox findable from the parent
- inherited documentation: an agent working in a sandbox sees the
  parent's `CLAUDE.md`
- a cheap create, and a graduate and a delete that leave no debris
  in the parent

What no answer needs to provide: a reproducible checkout of the whole
set, or bulk commands across it. The first is an anti-goal for
throwaways; the second is not yet a need.
