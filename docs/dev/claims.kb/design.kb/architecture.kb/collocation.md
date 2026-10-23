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
named for the same stem: `sandbox-repo.kb/graphics/opus.md` describes
the checkout at `sandbox-repo.kb/graphics/opus/`. Record and checkout
are found by one `ls`, and the hierarchy of the collection is the
hierarchy on disk.

The alternative was a mirror tree outside the collection, keeping the
record pure and the checkouts visibly a cache. Collocation won on the
operator's preference for finding the two together.
