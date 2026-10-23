---
label: SINGLE_COMMAND_UNWRAPPED
standing: user
force: must
authority:
  address: "nih-tooling-deliberation (6008d1)"
  words: "Let's not wrap single commands without adding any value."
  about: "a proposed bump subcommand that would have been git commit -a"
why:
  - ../design.kb/goals.kb/the-parent-stays-thin.md
---

# A script exists only where it composes several commands

The parent's tooling adds a subcommand only where the operation is
several commands that belong together. An operation that is one git
or gh command is invoked as that command. Two cases are settled:

- Recording child state in the parent is `git commit -a`.
- Unbinding a sandbox from the parent is `git rm` of its record plus
  deleting the clone. Deleting the GitHub repository is a separate
  act, always explicit, never a side effect of unbinding.

> [!@bukzor] nih-tooling-deliberation (6008d1)
> I think git-rm handles this just fine. I don't intend to ever
> gh-repo-rm except very explicitly.
