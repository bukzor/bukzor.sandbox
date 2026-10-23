---
label: CLONES_IGNORED
standing: user
todo: true
authority:
  address: "nih-tooling-deliberation (6008d1)"
  words: "all looks good. approved."
  about: "the ledger rendered in chat, this claim signed + and flagged as correcting a stated premise"
why:
  - collocation.md
  - ../background.kb/llm-kb-validate-skips-ignored-paths.md
  - ../goals.kb/the-parent-stays-thin.md
---

# The parent gitignores every clone

Every sandbox checkout inside `sandbox-repo.kb/` is ignored by the
parent's git. The parent's history holds record files and never
checkouts, and the kb validator skips the clones.

The ignore is what makes both true. The validator skips paths git
ignores and paths inside submodules, and walks anything else
(`../background.kb/llm-kb-validate-skips-ignored-paths.md`); a clone
that is neither would be walked, and its own `.kb/` directories
validated as if they were the parent's.
