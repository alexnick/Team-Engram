---
name: update-team-engram
description: Use when adding or updating reusable Team Engram knowledge.
---

# Update Team Engram

Prepare a focused local Knowledge or Decision change. Publication is a later, explicit boundary.

## Procedure

1. Load `publish-team-engram-change` and complete its preparation checks before editing.
2. Confirm the material belongs in Team Engram: it must remain useful without the originating project attached. Keep project implementation truth in the project repository.
3. Regenerate the ignored Index when stale. Search for the canonical page before creating a file.
4. Choose the smallest change:
   - update an existing page when it already owns the subject;
   - create a page only for a standalone subject with an independent lifecycle or cross-context reuse;
   - propose new structure only for a demonstrated navigation, retrieval, naming, vocabulary, or lifecycle problem.
5. Apply the requested local change using the current schema and template. Merged Knowledge defaults to `active`; unfinished work stays in the branch. Require provenance only for claims of derivation, verification, quotation, or attribution.
6. Keep maintained knowledge, source claims, decisions, and agent inference distinct. Preserve contradictions and supersession explicitly.
7. Run `python Tools/engram.py index` and `python Tools/engram.py lint`, plus any checks relevant to changed system files.
8. Use `publish-team-engram-change` to show the semantic summary and stop for explicit publication confirmation.

## Pitfalls

Do not copy project documents into Team Engram, create a duplicate because wording differs, rewrite raw source records, add speculative domains, or treat the original writing request as publication confirmation.

## Completion

Every requested semantic change is represented in the focused diff; every changed file is reported; local validation results and unresolved concerns are explicit; no commit, push, or Merge Request occurs before fresh confirmation.
