---
label: ANCESTOR_MEMORY
standing: bare
why:
  - ../background.md
---

# Claude Code loads CLAUDE.md from every ancestor directory

Claude Code loads a `CLAUDE.md` from each ancestor directory of its
working directory, up to the filesystem root, without regard to git
repository boundaries. A repo nested on disk under this parent
therefore sees the parent's `CLAUDE.md` with no wiring of its own.

Check: start a session in any directory below one that holds a
`CLAUDE.md` and is outside the session's git repo; the file appears in
`/context` as project instructions. Observed with
`/home/bukzor/CLAUDE.md` from a session in
`/home/bukzor/repo/github.com/bukzor.sandbox`.
