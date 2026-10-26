---
label: COMMAND
standing: agent
why:
  - tooling-is-a-workspace-package.md
  - ../../design.kb/components.md
---

# The command is `bukzor-sandbox`

The package's one console script is `bukzor-sandbox`, and each verb is
a subcommand of it. Invoked without a verb, or with one it does not
know, it prints usage and exits 2.

The name is the repo's own, free on every platform. A bare `sandbox`
was declined: policycoreutils ships a command of that name on
Fedora-family systems.
