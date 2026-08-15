# Ingest a Source

## Purpose

Preserve a source with stable identity, create an editable source record, and add reusable Knowledge only when warranted. Use this for articles, complete multi-screen Confluence pages, web pages, and external artifact locators.

## Prerequisites

- You are authorized to store or reference the source.
- The source is available in full, or missing portions are explicitly identified.
- Team Engram is open and unrelated local changes are understood.
- For internal content, you have checked that repository access is appropriate for the material.

## Cursor prompts

For a complete article:

```text
Ingest this complete article into Team Engram: <source or pasted Markdown>. Preserve the full article-scale text as a new immutable Markdown snapshot, including title, stable source identity, retrieval details, and all sections in order. Create or update the derived source record, search for existing canonical Knowledge before proposing synthesis, validate locally, and show the changed files and semantic summary. Do not commit, push, create a Merge Request, or merge.
```

For a long Confluence article supplied in parts:

```text
Begin an incremental ingest of the Confluence article <title and stable URL>. I will provide multiple sections. Preserve each section in order in one local Markdown snapshot, track which sections are still missing, and do not claim the snapshot is complete until I confirm the final section. Do not derive Knowledge or publish yet.
```

For a large or binary artifact:

```text
Ingest this source as an external locator only: <stable URL or repository locator>. Do not copy the binary into Team Engram. Preserve stable identity and retrieval metadata, then prepare the derived source record and validate locally. Do not publish.
```

## What Cursor does and where it stops

Cursor creates a focused `source/<slug>` branch, preserves a new raw snapshot or immutable locator record, creates or updates the editable source record, and separates source claims, evidence, limitations, user interpretation, and agent inference. It may propose reusable Knowledge only after searching for an existing canonical page.

The ingest request authorizes local source preparation. Cursor stops before publication. A raw snapshot is not silently rewritten to represent changed source content; a later source version gets a new dated raw record.

## Expected result

- Full practical text is preserved without screen-based truncation.
- Missing sections are explicit until the user confirms completeness.
- Raw material and editable source analysis remain separate.
- The source record links to the raw snapshot or locator.
- Knowledge is created only when a standalone reusable model is justified.
- Local validation and the affected-file summary are visible.

## Verification

For a long article, compare the source's heading sequence, first paragraph, last paragraph, tables or lists, and section count against the snapshot. Then ask:

```text
Verify source completeness and provenance. List every source section in order, identify any omitted or uncertain content, confirm that raw and derived files are separate, check relative links and schema fields, and report whether any binary or secret was added. Do not publish or rewrite the raw snapshot.
```

## Common errors

- **Only the visible screen was captured:** continue incrementally until the full article is supplied.
- **Cursor claims success while sections are missing:** keep status incomplete and do not derive definitive Knowledge.
- **A PDF, archive, video, or other clone-heavy file is added:** store it externally and preserve a locator record.
- **A changed article overwrites the old snapshot:** create a new dated snapshot.
- **Source claims are promoted directly to facts:** preserve attribution and synthesize carefully.
- **A duplicate Knowledge page is created:** update the canonical page when appropriate.

## Safe recovery

- If ingest is interrupted, keep the branch local, record which section was last preserved, and resume from the next section.
- If the source is inaccessible, preserve only a truthful locator and limitation; never invent content.
- If unauthorized or sensitive content was copied, stop before publication and remove it from the local unpublished change after confirming scope. If it was already pushed, treat it as an incident and contact the repository administrator; deleting a branch is not sufficient history erasure.
- If raw text was accidentally edited after publication, restore the published snapshot and create a new corrected or later-version record.
- Use [Abandon or recover](ABANDONING-OR-RECOVERING-A-CHANGE.md) for incomplete local work.

Rules: [Team Engram Protocol](../Protocols/Team-Engram-Protocol.md). Publication: [Publish](PUBLISHING-A-CHANGE.md).
