---
label: MANIFEST_TOOL
standing: open
why:
  - ../binding.md
---

# A manifest plus a multi-repo tool

The parent holds a manifest listing its sandboxes, and a tool from the
manifest-and-sync family (Android `repo`, `west`, `tsrc`, `mani`,
`myrepos`) clones, lists, and runs commands across them.

Appeal: bulk commands across the set, and a reproducible checkout.
Cost: a third tool to install and learn; nesting on disk, and so the
inherited `CLAUDE.md`, depends on how the tool lays out clones.

Would win if a bulk-command need shows up at bootstrap. The user
reports disliking `repo` from prior experience; which behavior bit is
not yet on record and would weigh here.
