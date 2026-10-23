---
label: CLONES_IGNORED
standing: user
todo: true
authority:
  address: "nih-tooling-deliberation (6008d1)"
  words: "adopted."
  about: "a scoped gitignore of *.git/ in sandbox-repo.kb, matching the <name>.git clone convention"
why:
  - collocation.md
  - ../background.kb/llm-kb-validate-skips-ignored-paths.md
  - ../goals.kb/the-parent-stays-thin.md
---

# The parent gitignores every clone, by its `.git` suffix

`sandbox-repo.kb/.gitignore` holds the one pattern `*.git/`, which
matches every clone at every depth of the collection. The parent's
history holds record files and never checkouts, and the kb validator
skips the clones.

The ignore is needed even though git treats an untracked nested repo
as one opaque entry. Without it, `git add -A` in the parent records
the clone as an embedded-repo pointer, with only a warning, and the
validator walks into the clone and reports its kb as the parent's
(`../background.kb/llm-kb-validate-skips-ignored-paths.md`).

A consequence worth knowing: tools that honor gitignore, Claude Code's
search among them, do not see sandbox contents from the parent. Search
across sandboxes goes through `foreach`, or starts inside a sandbox.

Probed 2026-10-23 in a scratch repo with clones at three depths:
status, `git add -A`, the validator, and `rg` all saw records only,
and git inside a `*.git` checkout reported it as not bare.
