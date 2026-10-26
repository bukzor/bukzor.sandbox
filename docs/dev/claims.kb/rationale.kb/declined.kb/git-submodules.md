---
label: SUBMODULES
standing: user
verdict: rejected
authority:
  address: "nih-tooling-deliberation (6008d1)"
  words: "all looks good. approved."
  about: "the ledger rendered in chat, this claim struck within it"
why:
  - ../../design.kb/architecture.kb/binding.md
  - ../../design.kb/architecture.kb/llm-kb-record.md
---

# Git submodules, with lazily bumped pointers

Each sandbox would be a git submodule of the parent, its gitlink
pointer bumped lazily, on the policy that already governs the
`~/.claude/sessions.kb` submodule in `bukzor/dotfiles`.

Rejected because a gitlink is a second record beside the kb record
(`../../design.kb/architecture.kb/llm-kb-record.md`), and one that pins a commit nobody wants pinned:
every child commit makes the parent report the child as modified. The
one thing submodules offered that nothing else does, GitHub rendering
the parent as a clickable tree, did not outweigh carrying two records.
