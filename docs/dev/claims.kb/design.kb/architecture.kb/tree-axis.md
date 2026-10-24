---
label: TREE_AXIS
standing: user
authority:
  address: "sandbox-create (f39ab32c)"
  words: "agreed, and approved."
  about: "the proposal in chat: the tree keyed by subject, stage kept in the name, SANDBOX_SUBPATH written to GitHub by push, dotted names declined"
why:
  - ../goals.kb/hierarchy.md
  - ../goals.kb/shared-documentation.md
  - ../goals.kb/graduation-is-a-rename.md
  - ../goals.kb/add-organization-remove-none.md
---

# The tree groups sandboxes by subject; stage stays in the name

Directories in `sandbox-repo.kb/` name subjects -- `llm/`,
`graphics/` -- so documentation shared across a subject is written
once, in its directory. A sandbox's stage -- `prototype`, `research`,
`ideation`, `scratch` -- stays the dotted prefix of its GitHub name,
where it is today: `sandbox-repo.kb/llm/prototype.stet.md`.

Subject cuts across stage. `research.llm-tooling` and
`prototype.llm-stet` share a subject and differ in stage, so a tree
keyed by stage would copy subject documentation into each stage.

Stage is also the attribute that changes: graduation is a stage
change, and so is an ideation becoming a prototype. Keeping stage in
the name makes such a change a rename, which graduation already is
(`../goals.kb/graduation-is-a-rename.md`). A change of subject is a
move within the parent, which renames nothing on GitHub.
