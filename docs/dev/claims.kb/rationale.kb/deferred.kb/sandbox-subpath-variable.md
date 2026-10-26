---
label: SUBPATH_VARIABLE
standing: user
authority:
  address: "sandbox-create (f39ab32c)"
  words: "what if we additional-purposed actions variables to contain a ... \"sandbox-subpath\" ... I'm just examining whether we can find a \"onto\" mapping from our filesystem to github data. -- agreed, and approved."
  about: "an Actions variable holding each sandbox's place, against dotted names"
why:
  - hierarchy-on-github.md
  - ../../design.kb/architecture.kb/tree-axis.md
  - ../../technical-policy.kb/exact-string-equality.md
---

# An Actions variable, `SANDBOX_SUBPATH`, holds the record's directory

The repository variable `SANDBOX_SUBPATH` holds the directory of the
sandbox's record, relative to `sandbox-repo.kb/`: the repository
`prototype.stet` recorded at `sandbox-repo.kb/llm/prototype.stet.md`
carries `SANDBOX_SUBPATH=llm`.

- **The directory, without the name.** GitHub renames leave variables
  untouched, so a value carrying the name would go stale at every
  graduation.
- **`.` at the top of the tree**, the filesystem's own name for the
  current directory (`../../technical-policy.kb/reuse-preexisting-semantics.md`).
- **Underscores in the name**, because variable names admit only
  letters, digits, and underscores, case-insensitively, and must not
  begin with a digit or `GITHUB_`; the
  difference from the hyphenated spelling is forced
  (`../../technical-policy.kb/exact-string-equality.md`).

Actions variables exist to configure CI, and this use is arguably an
abuse. It is the one key-value store a personal account's repository
has: custom properties are for organization repositories only (the
API answers 404 for `bukzor/bukzor.sandbox`), and topics hold neither
keys nor slashes. The variable is readable through the API with the
owner's credentials. The owner page and `gh repo list` do not show it,
and filtering on it costs one API call per repository.
