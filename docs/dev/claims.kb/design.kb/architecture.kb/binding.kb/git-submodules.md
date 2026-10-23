---
label: SUBMODULES
standing: agent
why:
  - ../binding.md
  - ../../background.kb/claude-code-loads-ancestor-claude-md.md
---

# Git submodules, with lazily bumped pointers

Each sandbox is a git submodule of the parent. The gitlink pointer is
bumped lazily, when something outside the parent needs it current,
never after every sandbox commit. The same policy already governs the
`~/.claude/sessions.kb` submodule in `bukzor/dotfiles`.

Appeal: built in, no third tool. GitHub renders the parent as a
clickable index. Nesting on disk delivers the parent `CLAUDE.md` to
every sandbox with no per-sandbox wiring.

Cost: one gitlink per sandbox, which graduate and delete must remove.
Agent-recommended; the user's ruling is pending.
