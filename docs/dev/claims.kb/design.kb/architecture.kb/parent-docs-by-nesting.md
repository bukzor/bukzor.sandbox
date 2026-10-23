---
label: DOCS_BY_NESTING
standing: user
authority:
  address: "nih-tooling-deliberation (6008d1)"
  words: "all looks good. approved."
  about: "the ledger rendered in chat, this claim signed + within it"
why:
  - collocation.md
  - ../goals.kb/shared-documentation.md
  - ../background.kb/claude-code-loads-ancestor-claude-md.md
  - ../../technical-policy.kb/location-independence.md
---

# An agent in a sandbox sees the parent's CLAUDE.md because the parent is an ancestor directory

The parent's `CLAUDE.md` reaches a sandbox through directory nesting
alone. Claude Code loads a `CLAUDE.md` from every ancestor of its
working directory, and collocation puts every clone below the parent.
No file inside a sandbox names the parent or its location, so the
sandbox checked out elsewhere simply sees less, and nothing breaks.

The declined mechanism is beside this one
(`parent-docs-by-import-line.md`).
