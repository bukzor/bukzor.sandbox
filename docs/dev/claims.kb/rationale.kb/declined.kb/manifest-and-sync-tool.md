---
label: MANIFEST_TOOL
standing: user
verdict: rejected
authority:
  address: "nih-tooling-deliberation (6008d1)"
  words: "all looks good. approved."
  about: "the ledger rendered in chat, each tool struck within it"
why:
  - ../../design.kb/architecture.kb/binding.md
  - ../../design.kb/architecture.kb/llm-kb-record.md
  - ../../design.kb/goals.kb/hierarchy.md
---

# A manifest plus a multi-repo tool

The parent would hold a manifest in some tool's format, and the tool
would clone, list, and run commands across the set.

Rejected as a family: every member is a second record beside the kb
record (`../../design.kb/architecture.kb/llm-kb-record.md`), carrying less per entry than a kb file
can, in exchange for three prewritten operations that are a short
`xargs` walk over the kb. Per tool, as of 2026-10-23:

- Android `repo` (brew core): manifest must live in its own git repo;
  `repo sync` resets child checkouts by default.
- `myrepos` / `mr` (brew core): config is executable shell, so any
  `.mrconfig` outside the home directory must be listed in
  `~/.mrtrust`; last release 2018.
- `mani` (brew core, static Go binary): the closest fit, one YAML with
  path, description, and tags per project, and still a second record
  with flat-string metadata.
- `gita` (brew core): record lives in `~/.config/gita`, outside the
  parent.
- `ghorg`: clones every topic match into one flat directory, by
  construction. No hierarchy.
- `vcstool`, `tsrc`, `meta`, `grm`: not in Homebrew core.
