---
label: EXACT_STRING
standing: user
force: should
authority:
  address: "sandbox-create (f39ab32c)"
  words: "exact string equality is a Good Thing -- we don't have two differing strings for \"the same thing\" unless we must"
  about: "how a sandbox's GitHub name, record, and clone relate, among other names"
---

# One thing, one string

Where two places name the same thing, they spell it identically.
A differing spelling is admitted only where something outside the
project forces it, and then as the smallest change the constraint
demands -- a suffix appended, never a rewrite.

Equal strings make a name its own index: a reader, or `grep`, that
finds it in one place finds every other place it names the same
thing, and no mapping between spellings has to be learned,
documented, or kept in sync. A rename is then one string replaced
everywhere, with nothing to translate.

A sandbox is the worked case. Its name is the GitHub repository's
name, the record's stem (`<name>.md`), and the clone's stem
(`<name>.git/`); the two suffixes are forced, because one directory
cannot hold two entries called `<name>`.
