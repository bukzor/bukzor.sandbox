# bukzor.sandbox

A home for work that has no home: the parent of many throwaway
sandbox repos. The parent holds the bindings to its sandboxes, the
documentation that unifies them, and the tooling that operates on
them. No experiment lives here directly.

| path                              | what                                              |
| --------------------------------- | ------------------------------------------------- |
| `docs/dev/claims.kb/`             | the design, as a claim ledger (`Skill(llm-claims-kb)`) |
| `packages/bukzor-sandbox-tools/`  | the `bukzor-sandbox` command                      |
| `sandbox-repo.kb/`                | one record per sandbox; each clone sits beside its record |

## Use

```bash
uv sync
bukzor-sandbox create --private -p sandbox-repo.kb/llm/foo
```

That makes the GitHub repository `foo`, the record
`sandbox-repo.kb/llm/foo.md`, and the clone `sandbox-repo.kb/llm/foo.git/`.
The record is left unstaged; commit it like any file.

## Develop

```bash
uv sync
uv run pre-commit install
uv run pre-commit run --all-files

# required before editing docs/dev/claims.kb/: the ledger's validators
uv tool install --editable ~/.claude/skills/llm-kb
uv tool install --editable ~/.claude/skills/llm-claims-kb
```

The ledger tools (`llm.kb-validate`, `llm-claims-kb-mentions`,
`llm-claims-kb-ownership --trespass`, ...) install as uv tools, not
into `.venv`: `uv sync` removes from `.venv` whatever the lockfile
does not list, and the lockfile cannot list them, because their source
lives outside this repo, where CI has no copy.

One package per tool under `packages/`, each independently buildable;
the root `pyproject.toml` is the uv workspace that ties them together
and carries the shared lint and test configuration. Whether a package
is published is the package's own business (its classifiers), not its
position in the tree.
