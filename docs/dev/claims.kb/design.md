---
label: DESIGN
standing: agent
ontology:
  - mission
  - goals
  - architecture
  - components
  - deliverables
non-claim-tokens:
  - DAG
  - CLAUDE
  - QUESTION
  - URL
  - YAML
  - README
  - PATH
  - DRAFT
  - SANDBOX_SUBPATH
stale-when: a rung nothing cites and nothing fills -- the chain was copied rather than chosen, and the stratification wants re-deriving from what this project actually argues about
---

# bukzor.sandbox -- the design, as a ledger

What this repo is for and how it is built, kept as a claim ledger
(`Skill(llm-claims-kb)`): one claim per file, label and standing in
frontmatter, one theory per collection. Argue with a claim by editing
its file; the git diff is the strikethrough.

Five rungs. This repo is a parent of throwaway repos, and what it
decides is why it exists, what it adds, what binds a subordinate to
it, what operations it performs on them, and how the tooling for
those operations ships. The skill's remaining rung (`requirements`)
joins when a claim wants it.

| Rung | The question it answers |
|---|---|
| `mission` | What problem are we solving? Who benefits? |
| `goals` | How do we accomplish the mission? |
| `architecture` | What is the parent, and what binds a sandbox to it? |
| `components` | What operations does the parent perform on its sandboxes? |
| `deliverables` | How is the tooling built, named, and installed? |

Beside the rungs, `background` holds what the design assumes but does
not argue: prior art and checkable facts about the tools in play.

Priors are a DAG, not a ladder: a claim's `why:` names whatever claims
it would be revisited over.

## Scans

```bash
grep -rH '^standing:' docs/dev/claims.kb/     # who signed what
grep -rl '^todo: true' docs/dev/claims.kb/    # decided, not yet built
grep -rl 'QUESTION' docs/dev/claims.kb/       # undecided; never implement these
llm-claims-kb-flatten docs/dev/claims.kb/design.kb   # the whole ledger as one text
```
