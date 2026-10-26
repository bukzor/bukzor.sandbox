---
label: GH_FLAT
standing: bare
---

# GitHub lists an owner's repositories flat

GitHub presents an owner's repositories as one flat list. Topics are
tags on a repository, filterable but not nested; there is no
container between an owner and a repository. Any hierarchy among an
owner's repositories must be recorded somewhere other than GitHub.

Check: `gh repo list <owner>` has no grouping option, and a topic
filter (`--topic`) narrows the flat list without arranging it.
