---
name: query-team-engram
description: Use when asking Team Engram for organizational knowledge.
---

# Query Team Engram

Answer from maintained Team Engram content with direct links and explicit epistemic boundaries. This skill is read-only.

## Procedure

1. Read `Protocols/Team-Engram-Protocol.md`, `CONTEXT-MAP.md`, and `Engram/CONTEXT.md`.
2. Run `python Tools/engram.py index` when the ignored Index is missing or stale. Use `Engram/INDEX.md` and narrow search to identify candidate pages.
3. Read relevant Knowledge, Decisions, and source records. Read raw snapshots or locators only when exact wording, attribution, or a disputed claim requires them.
4. Answer with the smallest useful set of direct page links. Separate, when present:
   - **Maintained knowledge**;
   - **Source claims**;
   - **Decisions**;
   - **Agent inference**.
5. Surface material contradictions, scope, dates, and uncertainty. Say when Team Engram does not answer the question.

## Project boundary

Use attached project material when the question requires it, but identify project truth as project truth. Do not present it as Team Engram's reusable model unless a maintained Team Engram page says so.

## Citations

Cite actual corpus pages with resolvable relative Markdown links and useful anchors. The Index and Context Map are discovery aids, not evidence. Never invent a citation or imply that unsourced maintained knowledge is externally verified.

## Completion

Report the answer, cited basis, and any important gap or contradiction. Do not edit tracked files, Git state, or metadata merely because a query produced a useful idea; offer `update-team-engram` only when the user wants that idea made durable.
