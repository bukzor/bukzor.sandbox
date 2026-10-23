# bukzor.sandbox

A home for work that has no home: the parent of many throwaway
sandbox repos. The parent holds the bindings to its sandboxes, the
documentation that unifies them, and the tooling that operates on
them. No experiment lives here directly.

| path                              | what                                              |
| --------------------------------- | ------------------------------------------------- |
| `docs/dev/claims.kb/`             | the design, as a claim ledger (`Skill(llm-claims-kb)`) |
| `packages/bukzor-sandbox-tools/`  | the `bukzor-sandbox` command                      |

## Develop

```bash
uv sync
uv run pre-commit install
uv run pre-commit run --all-files
```

One package per tool under `packages/`, each independently buildable;
the root `pyproject.toml` is the uv workspace that ties them together
and carries the shared lint and test configuration. Whether a package
is published is the package's own business (its classifiers), not its
position in the tree.
