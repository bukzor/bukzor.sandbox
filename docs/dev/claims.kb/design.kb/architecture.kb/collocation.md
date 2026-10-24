---
label: COLLOCATION
standing: user
authority:
  address: "nih-tooling-deliberation (6008d1)"
  words: "beside the file inside the collection. collocation is a Good Thing"
  about: "where a sandbox's clone lands relative to its record file"
why:
  - binding.kb/llm-kb-record.md
---

# A sandbox's clone sits beside its record file, inside the collection

The clone of a sandbox is a directory beside the file that records it,
named for the same stem plus `.git`: `sandbox-repo.kb/llm/prototype.stet.md`
describes the checkout at `sandbox-repo.kb/llm/prototype.stet.git/`. Record
and checkout are found by one `ls`, and the hierarchy of the collection
is the hierarchy on disk.

> [!@bukzor] nih-tooling-deliberation (6008d1)
> what if we change convention a bit. clones go to <name>.git, then we
> can have a scoped gitignore of *.git/ -- adopted.

The suffix names what the directory is, a git checkout, and is what
lets one ignore pattern find every clone at any depth
(`clones-gitignored.md`). Hierarchy directories need no suffix of their
own. Cloning must name the target directory explicitly, since
`git clone` strips a trailing `.git` from its default.

The alternative was a mirror tree outside the collection, keeping the
record pure and the checkouts visibly a cache. Collocation won on the
operator's preference for finding the two together.
