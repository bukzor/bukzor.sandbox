# design.kb -- where a new file goes

One claim per file, under the rung whose question it answers. The
rung's own `.md` defines it; the claims it holds live in its `.kb/`.

- A claim answering a rung's question -> that rung's `.kb/`.
- A claim that would be revisited if some other claim collapsed ->
  name that claim in `why:`, whatever rung it sits on.
- A word this project stipulates -> the `ontology:` of the outermost
  rung whose claims all need it.
- A cross-cutting imperative -> `../technical-policy.kb/`.
- Anything that is not needed to use the tool today goes beside the
  design, in `../rationale.kb/`, and no claim in this directory cites
  it: content the design assumes but does not argue (domain
  background, prior art) -> `background.kb/`; an option weighed and
  refused, kept struck so it is not re-proposed -> `declined.kb/`;
  decided or proposed, but nothing yet needs it -> `deferred.kb/`.
  A deferred claim returns here, with its arrows, when something does.
