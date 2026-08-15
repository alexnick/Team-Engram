---
type: context
status: active
topics: [team-engram, knowledge-management]
---

# Team Engram Corpus Context

## Purpose

This corpus stores reusable organizational knowledge that remains useful without an originating project repository attached. It begins empty and acquires content and structure through real use.

## Current state

- `Knowledge/` holds maintained reusable synthesis.
- `Decisions/` holds consequential accepted decisions.
- `Sources/Raw/` holds immutable Markdown snapshots or stable locator records.
- `Sources/Records/` holds editable source analysis linked to raw material.
- `INDEX.md` is generated locally for discovery and is ignored by Git.

## Working boundaries

- Project-specific implementation truth remains in project repositories.
- Original organizational Knowledge may be authored without external proof.
- Provenance is required when a page claims derivation, verification, quotation, or attribution from named evidence.
- Complete article-scale text may be preserved as a Markdown raw snapshot; large or binary artifacts remain external.
- Merged Knowledge is active unless explicitly disputed, superseded, or archived.
- Structure emerges from demonstrated content pressure; the corpus does not begin with predefined domains.

## Collaboration

Cursor prepares and validates focused local changes. Explicit `Publish this change` confirmation is required before commit, push, and GitLab Merge Request creation or update. Merge is a separate human-triggered action. Git and GitLab provide shared history; the corpus has no operation log.

## Navigation

Use the repository [Context Map](../CONTEXT-MAP.md) as the committed router and regenerate the local `INDEX.md` when it is missing or stale. The Index supports discovery but is not evidence for substantive claims.
