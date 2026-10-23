---
label: TOPIC_ONLY
standing: user
verdict: rejected
authority:
  address: "nih-tooling-deliberation (6008d1)"
  words: "I'd assume this results in a flat collection, which is explicitly what I'm here to get away from."
  about: "ghorg clone by topic, the mechanism this candidate rests on"
why:
  - ../binding.md
  - ../../goals.kb/hierarchy.md
  - ../../background.kb/github-lists-repos-flat.md
---

# No nesting: the parent is documentation and tooling, the index is a GitHub topic

The parent would carry no record at all. Every sandbox would carry a
GitHub topic, the index would be `gh repo list --topic`, and sandboxes
would stay flat on disk beside everything else.

Rejected because GitHub lists an owner's repositories flat, so a
topic can say which repositories are sandboxes and nothing about how
they are arranged. The hierarchy has to be recorded in the parent,
and once the parent holds a record, the topic is at most an index on
the GitHub side, which is a separate question
(`../../../technical-policy.kb/every-sandbox-carries-the-sandbox-topic.md`).
