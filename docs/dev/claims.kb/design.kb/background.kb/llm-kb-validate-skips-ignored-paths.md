---
label: LLMKB_SKIPS_IGNORED
standing: bare
verify: "grep -n 'is in submodule\\|def ignored_by_git' ~/.claude/skills/llm-kb/lib/python/llmd/frontmatter_validate.py"
---

# llm.kb-validate skips what git ignores and what sits inside a submodule

The validator's walk filters what it finds through
`git check-ignore`, asked of the repository holding the walk's root.
A path git ignores is scratch and is skipped; a path git refuses to
answer for because it is inside a submodule is skipped on the same
grounds. Any other path is walked, a nested plain clone included,
whose own `.kb/` directories would then be validated as part of the
outer corpus.

So a repository inside a collection is invisible to the validator iff
the outer repository ignores it or holds it as a submodule. Being a
repository is not, by itself, enough.
