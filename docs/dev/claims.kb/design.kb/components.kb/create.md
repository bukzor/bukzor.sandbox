---
label: CREATE
standing: user
todo: true
authority:
  address: "nih-tooling-deliberation (6008d1)"
  words: "My rough first draft: - create"
  about: "the minimal set of verbs for sandbox repos"
why:
  - ../components.md
  - ../architecture.kb/binding.kb/llm-kb-record.md
  - ../architecture.kb/collocation.md
  - ../../technical-policy.kb/sandbox-semantics.md
  - ../../technical-policy.kb/exact-string-equality.md
---

# create

Brings new sandboxes into existence, as `mkdir` brings directories:

    bukzor-sandbox create [-p|--parents] (--public|--private|--internal) PATH...

Each `PATH` resolves against the working directory and lands inside a
`sandbox-repo.kb/`. Its last component, `<name>`, is the sandbox's name
on GitHub and on disk alike. For each `PATH`, `create`:

- creates the empty GitHub repository `<name>` with `gh repo create`,
  under `gh`'s default owner, at the given visibility;
- writes the record `PATH.md`;
- clones the repository into `PATH.git/`.

Afterwards the sandbox is a member, has a place, and has a checkout.

> [!DRAFT] sandbox-create (f39ab32c)
> Derived from `../../technical-policy.kb/sandbox-semantics.md` and
> `../../technical-policy.kb/reuse-preexisting-semantics.md`; vetoable.
>
> - Errors are `mkdir`'s, reported per `PATH`; the other paths
>   proceed, and the exit status is 1 if any failed.
>   - `File exists` -- `PATH.md`, `PATH.git/`, or the GitHub
>     repository `<name>` already exists. All three are checked before
>     any is made.
>   - `No such file or directory` -- the directory `PATH` names as its
>     parent is missing; `--parents` creates it, as `mkdir -p` does.
> - The visibility flags are `gh repo create`'s own, required as `gh`
>   requires them when it cannot prompt.
> - The record is left unstaged, as `mkdir` leaves a directory
>   untracked; adding and committing it is the operator's.
