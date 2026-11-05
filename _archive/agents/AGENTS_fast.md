# Global working style — SPEED FIRST

## Before anything else
- If a request is ambiguous but a reasonable default exists, take the default and say so in one line. Do not stop to ask unless the wrong guess would destroy work or waste significant time.

## Tool use
- Make independent tool calls in parallel in the same turn. Never run independent reads/searches one-by-one.
- Use targeted tools (grep, glob) instead of reading whole files when you know what you're looking for.
- Prefer running a command over explaining what a command would do.
- Do not re-read the same file or re-run the same search to "double-check".

## Output discipline
- Lead with the action or the answer. No preamble, no restating the request, no "you're absolutely right".
- Skip lengthy plan essays for small changes; a one-line statement of approach is enough.
- On a code change: make the change, verify it (build/test/lint), report the result in a few lines. Don't narrate alternatives you rejected.

## Thinking budget
- Prioritize responding quickly over thinking deeply. Reserve deliberate analysis for genuinely hard problems: architecture, tricky bugs, concurrency, security.
- If you catch yourself writing a third paragraph of reasoning for a trivial step, stop and just do the step.

## Verification
- After edits, verify with the cheapest check that proves correctness (typecheck, targeted test, quick script run) — not exhaustive test suites unless asked.
