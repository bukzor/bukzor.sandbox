---
label: RECORD
standing: user
authority:
  address: "nih-tooling-deliberation (6008d1)"
  words: "Left to my own devices, I'd probably use a sandbox-repo.kb hierarchical /llm-kb collection, where the frontmatter gives any necessary metadata beyond what the file existance already gives."
  about: "what file holds the path map, against a manifest of some tool's format"
why:
  - ../../goals.kb/hierarchy.md
  - ../../background.kb/github-lists-repos-flat.md
  - ../../../technical-policy.kb/location-independence.md
---

# The record is an llm-kb collection, `sandbox-repo.kb/`

The set of sandboxes and their hierarchy is `sandbox-repo.kb/` in the
parent, a collection in the sense of `Skill(llm-kb)`. One file per
sandbox. A sandbox is a member iff its file exists. Directory nesting
within the collection is the hierarchy. Frontmatter carries what
existence cannot, the GitHub URL first, under the collection's schema.

The record lives in the parent because GitHub cannot hold a hierarchy
and a sandbox may not hold a reference to the parent. It is a kb
rather than a tool's manifest because each entry can carry free-form
metadata and a prose body, and because the collection's validator
already exists.
