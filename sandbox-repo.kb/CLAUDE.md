# sandbox-repo.kb -- one record per sandbox

A sandbox is a member iff its record `<name>.md` is here. Its directory
is its subject, and its clone is the sibling `<name>.git/`, which the
`.gitignore` here keeps out of the parent's history.

- Make a sandbox with `bukzor-sandbox create (--public|--private|--internal) [-p] PATH`,
  not by hand: the record's `url:` is whatever `gh` reports.
- Directories name subjects (`llm/`, `graphics/`), never stages. The
  stage stays the dotted prefix of the repository name (`prototype.`,
  `research.`, ...). A `CLAUDE.md` in a subject directory reaches every
  sandbox beneath it.
- Not here: sandbox contents, or why the parent works this way. The
  clones are the sandboxes; the reasons are in `docs/dev/claims.kb/`.
