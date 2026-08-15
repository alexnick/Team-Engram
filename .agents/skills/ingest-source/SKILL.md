---
name: ingest-source
description: Use when preserving a source and deriving reusable knowledge.
---

# Ingest Source

Preserve source identity and retrieved material, create an editable source record, and integrate only warranted reusable knowledge. Publication is a later, explicit boundary.

## Procedure

1. Load `publish-team-engram-change` and complete its preparation checks. Confirm the source was actually accessed; never claim inaccessible content was read.
2. Establish the ingestion goal from the request. Ask one concise question only when the intended use is genuinely unclear.
3. Regenerate the ignored Index and search for an existing source record and related Knowledge before creating files.
4. Preserve one immutable raw record under `Engram/Sources/Raw/`:
   - store an ordinary article-scale text source as a Markdown snapshot when accessible and permitted; or
   - store a Markdown locator for large, binary, restricted, or externally retained material.
5. Record source type, retrieval date, URL or path, and topics. Record `artifact_path` and `content_hash` when an artifact is stored. A later retrieval creates a new dated record; never rewrite the old payload to represent changed content.
6. Create or update an editable record under `Engram/Sources/Records/` that links to at least one raw snapshot or locator. Separate direct claims, evidence or method, attributed opinion, quotations with locators, limitations, contradictions, and agent inference.
7. Decide whether reusable synthesis warrants a Knowledge update. Search for the canonical page first. It is valid to report `Knowledge changes: none`.
8. Keep project-specific implications in the project repository and publish that repository independently.
9. Run `python Tools/engram.py index` and `python Tools/engram.py lint`.
10. Use `publish-team-engram-change` to summarize raw records, source records, optional Knowledge changes, validation, and open questions, then stop for explicit publication confirmation.

## Completion

Account for source access, every raw and derived file, hashes for stored artifacts, citations and locators, contradictions, optional Knowledge integration, and validation. Do not report complete when required material is inaccessible or a record is missing.
