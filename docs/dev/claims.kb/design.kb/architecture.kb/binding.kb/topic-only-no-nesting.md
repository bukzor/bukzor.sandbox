---
label: TOPIC_ONLY
standing: open
why:
  - ../binding.md
---

# No nesting: the parent is documentation and tooling, the index is a GitHub topic

The parent carries no gitlinks and no manifest. Every sandbox carries
a GitHub topic, and the index is `gh repo list --topic`. Sandboxes
stay flat on disk beside everything else.

Appeal: the cheapest possible parent; graduate and delete touch
nothing in it.

Cost: no on-disk nesting, so the parent `CLAUDE.md` reaches a sandbox
only through explicit wiring, such as the sandbox's own `CLAUDE.md`
importing the parent's by path.

Would win if that wiring proves as cheap as nesting.
