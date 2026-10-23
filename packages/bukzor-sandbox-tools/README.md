# bukzor-sandbox-tools

The parent repo's tooling: one command, `bukzor-sandbox`, whose
subcommands are the verbs in the design record
(`docs/dev/claims.kb/design.kb/components.kb/`). Each verb composes
several `gh` and `git` commands over the set of sandboxes; anything
that is one command stays one command.

Repo-local: the `Private :: Do Not Upload` classifier keeps it off
PyPI. Install from the parent repo:

```bash
uv sync                       # into .venv; direnv puts it on PATH
uv tool install --editable .  # or onto ~/.local/bin
```
