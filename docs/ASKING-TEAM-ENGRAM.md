# Ask Team Engram

## Purpose

Use Ask when you want an answer from maintained Team Engram content, with links to the pages and source records used.

## Prerequisites

- Team Engram is open in Cursor.
- The repository is readable.
- The visible starting state may include a missing or stale local `Engram/INDEX.md`; Cursor can regenerate it.

## Cursor prompts

```text
What does Team Engram know about <topic>? Distinguish maintained organizational Knowledge, accepted Decisions, named source claims, and your new inference. Link every durable page you rely on. If the corpus does not answer the question, say so. Do not change corpus files.
```

For exact provenance:

```text
Find the maintained answer about <topic>, then trace each source-derived claim to its source record and raw snapshot or locator. Quote only when exact wording matters. Do not edit anything.
```

## What Cursor does and where it stops

Cursor starts at `CONTEXT-MAP.md`, refreshes the ignored local Index if needed, locates relevant maintained pages, and opens raw sources only when exact wording or provenance matters. Ask is read-only: it must not silently create Knowledge, repair pages, or publish changes.

Regenerating the ignored Index is local maintenance, not a corpus change and not a publication request.

## Expected result

A useful answer that:

- links the relevant repository pages;
- distinguishes maintained synthesis from external claims and new inference;
- states uncertainty and contradictions;
- says clearly when Team Engram lacks an answer.

## Verification

Open the linked pages and check that they support the answer. Ask Cursor:

```text
For each substantive sentence in your answer, identify the supporting Team Engram page or label it as your inference. Do not change files.
```

## Common errors

- **The Index is treated as evidence:** it is only a discovery aid.
- **A source summary is presented as accepted fact:** source claims and maintained Knowledge are different.
- **No links are provided:** ask Cursor to link repository-relative pages.
- **The answer guesses past missing content:** absence should be reported, not filled from model memory.
- **Query scans attached project code unnecessarily:** narrow the task to Team Engram unless project evidence was requested.

## Safe recovery

- Regenerate the local Index and repeat the question with a narrower topic.
- Ask Cursor to show search terms and candidate pages before answering.
- If content is missing, switch to [Add or update Knowledge](ADDING-OR-UPDATING-KNOWLEDGE.md) or [Ingest a source](INGESTING-A-SOURCE.md); do not let Ask silently become a write.
- If an answer exposed sensitive material, stop and review the underlying repository scope before sharing it further.

Rules: [Team Engram Protocol](../Protocols/Team-Engram-Protocol.md). Navigation: [Context Map](../CONTEXT-MAP.md).
