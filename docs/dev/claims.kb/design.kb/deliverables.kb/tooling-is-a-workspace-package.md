---
label: TOOLING_PACKAGE
standing: user
authority:
  address: "sandbox-packages (6e70b50e)"
  words: "let's prep this repo to host a \"sub-package\" named bukzor-sandbox-tools. I think the going convention is packages/<name> or packages/python/<name>"
  about: "where the parent's tooling lives; the flat form, as built, ratified with 'good work'"
why:
  - ../components.md
  - ../../technical-policy.kb/own-scripts.md
  - ../goals.kb/the-parent-stays-thin.md
---

# The tooling is a Python package under `packages/`

The parent's script ships as the Python distribution
`bukzor-sandbox-tools` at `packages/bukzor-sandbox-tools/`, a member
of the uv workspace rooted at the parent's `pyproject.toml`. The root
is a workspace and nothing more: it builds no distribution of its
own, and `uv sync` installs the members it names into `.venv/`, which
direnv puts on `PATH`.

One package per tool, flat under `packages/`, each independently
buildable: hatchling, the module under `lib/`, tests beside the code
they test and excluded from the wheel. This is the layout
`bukzor/bukzor-tools` already uses. A language tier,
`packages/python/<name>`, buys nothing until a second language
arrives; when one does, its workspace joins beside the first.
