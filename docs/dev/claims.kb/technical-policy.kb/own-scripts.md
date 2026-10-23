---
label: OWN_SCRIPTS
standing: user
force: should
authority:
  address: "nih-tooling-deliberation (6008d1)"
  words: "all looks good. approved."
  about: "the ledger rendered in chat, this claim signed + within it"
why:
  - ../design.kb/architecture.kb/binding.kb/llm-kb-record.md
  - ../design.kb/architecture.kb/binding.kb/manifest-and-sync-tool.md
  - single-command-unwrapped.md
---

# The parent's tooling is scripts in this repo over gh and git

The operations the parent performs on its sandboxes are implemented
here, as scripts composed from `gh` and `git`. No third-party
multi-repo tool is a dependency.

Every surveyed tool in the manifest-and-sync family sells two things:
a manifest of its own, and status, update, and foreach over it. The
manifest is what the record already is
(`../design.kb/architecture.kb/binding.kb/llm-kb-record.md`), so
adopting a tool would mean either a second record or a generated copy
of the first. The three prewritten operations amount to a short walk
over the record with `xargs`. The per-tool grounds are in the struck
candidate (`../design.kb/architecture.kb/binding.kb/manifest-and-sync-tool.md`).
