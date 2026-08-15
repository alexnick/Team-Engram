# Add or Update Knowledge

## Purpose

Create or improve reusable organizational synthesis in `Engram/Knowledge/` without duplicating an existing canonical page or importing project-only truth.

## Prerequisites

- Team Engram is open and your working tree has been inspected.
- You can explain the reusable subject in plain language.
- Any named sources are available or their limits are known.
- Unrelated local changes, if any, have been identified and will remain untouched.

## Cursor prompt

```text
Add or update Team Engram Knowledge about <subject>. First search for an existing canonical page and explain whether to update it or create a new one. Keep only reusable knowledge that remains useful without an attached project. Preserve provenance for every claim derived from a named source. Prepare one focused local change, regenerate the ignored Index, run local validation, and show the files and semantic summary. Do not commit, push, create a Merge Request, or merge.
```

For a correction:

```text
Update the canonical Team Engram page about <subject> to reflect <correction>. Identify any conflicting or superseded claim, preserve relevant provenance, validate locally, and stop with a reviewable summary. Do not publish.
```

## What Cursor does and where it stops

Cursor inspects local state, safely updates local `main` when appropriate, creates a focused `knowledge/<slug>` branch, searches for existing Knowledge, prepares only the requested local change, refreshes the ignored Index, and runs local checks.

The request authorizes local preparation. Cursor must stop before commit, push, Merge Request creation or update, and merge. Publication requires the separate confirmation described in [Publishing](PUBLISHING-A-CHANGE.md).

## Expected result

- One existing canonical page is updated, or one justified new page is created.
- Required metadata and links are valid.
- Named-source derivation is traceable; independently authored synthesis is not forced to invent a source.
- Project-specific implementation detail remains in the project repository.
- Cursor reports changed files, semantic impact, validation, and unresolved concerns.

## Verification

Review the rendered Markdown and ask:

```text
Verify this local Knowledge change against the Team Engram schema and protocol. Check for duplicate canonical pages, unsupported attribution, broken relative links, project-only content, secrets, and unrelated changed files. Do not fix or publish anything; report findings first.
```

## Common errors

- **A new page duplicates an existing one:** update the canonical page instead.
- **A project plan is copied into Team Engram:** synthesize only the reusable lesson.
- **A source is invented for original knowledge:** provenance is conditional, not ceremonial.
- **A named-source claim has no traceable record:** add or repair source provenance through Ingest.
- **A speculative folder or domain is created:** structure must respond to real retrieval or lifecycle pressure.
- **Generated `Engram/INDEX.md` appears in the diff:** it must remain ignored.

## Safe recovery

- Revise the same branch and re-run validation.
- If the change belongs in a project, remove only the Team Engram draft after confirming the intended destination.
- If validation fails, do not publish; ask Cursor to explain each error before fixing.
- If the branch became stale, follow [Resolve conflicts](RESOLVING-CONFLICTS.md).
- To pause or discard safely, follow [Abandon or recover](ABANDONING-OR-RECOVERING-A-CHANGE.md).

Rules: [Team Engram Protocol](../Protocols/Team-Engram-Protocol.md). Sources: [Ingest](INGESTING-A-SOURCE.md).
