# Team Engram Agent Contract

You are operating inside a shared, Markdown-first organizational knowledge repository.

## Normative sources

Before substantial work:

1. Read `Protocols/Team-Engram-Protocol.md` as the normative storage, lifecycle, collaboration, and safety contract.
2. Read `CONTEXT-MAP.md`, then `Engram/CONTEXT.md`.
3. Regenerate the ignored local `Engram/INDEX.md` when it is missing or stale, then load only the pages required for the request.
4. Read local instructions in attached project repositories before changing their files.
5. Inspect the Git working tree and current branch before any write.

Do not recursively scan the corpus unless the user requests an Audit or another explicitly repository-wide operation.

## Language

Every repository artifact is English: content, instructions, skills, implementation, documentation, examples, commits, and Merge Requests. Conversation may use the user's preferred language. Preserve source-language text when an immutable source snapshot or exact quotation requires it.

## Repository boundary

Team Engram stores reusable organizational knowledge that remains useful without an originating project attached. Project-specific implementation, plans, configuration, current-state documentation, and project-only skills stay in the project repository.

When project work yields reusable knowledge, keep project truth in place and propose a standalone Team Engram synthesis. Publish changes to each repository independently under that repository's rules.

## Canonical state and content classes

Merged `main` is canonical. Unfinished work belongs on a focused branch and, after publication, in a Merge Request.

The initial corpus contains only:

- `Engram/Knowledge/` — maintained reusable organizational understanding;
- `Engram/Decisions/` — accepted, rejected, or superseded choices and rationale;
- `Engram/Sources/Raw/` — immutable Markdown snapshots or locator records;
- `Engram/Sources/Records/` — editable source-grounded analysis.

Create new structure only when real content demonstrates an independent lifecycle or repeated navigation, retrieval, naming, or progressive-loading problem. Do not create empty domains, speculative taxonomies, or catch-all folders.

## Knowledge and evidence

Independently authored organizational Knowledge may originate with a person or agent and does not require external proof. Provenance is required when content claims derivation, verification, quotation, or attribution from named evidence.

Keep these categories explicit:

- maintained knowledge;
- source claims;
- accepted or rejected decisions;
- agent inference.

Never invent citations, quotations, dates, authors, measurements, paths, source locations, or access to unavailable material. Preserve meaningful contradictions and uncertainty.

## Raw sources

A requested Ingest may preserve a complete ordinary article-scale text source, including a multi-screen Confluence article, as an immutable Markdown snapshot. URLs and large, binary, restricted, or externally stored artifacts use immutable locator records. A stored artifact requires its recorded hash.

A changed retrieval creates a new dated raw record or explicit addendum. Never rewrite an existing raw payload or locator to represent changed source content. Editable source records link to raw records. Ingest creates or updates canonical Knowledge only when reusable synthesis is warranted.

## Navigation

`CONTEXT-MAP.md` is the short committed router. `Engram/INDEX.md` is deterministic local generated state and is ignored by Git. Regenerate it before Query, Audit, and applicable writing work. Neither navigation file is substantive evidence.

Use real relative Markdown links and load context progressively.

## Local change and publication boundary

A request to add, update, ingest, or change a shared skill authorizes a focused local proposal within that scope. It does not authorize publication or merge.

Before writing:

1. inspect status, branch, and remotes;
2. preserve unrelated changes without reset, cleanup, hiding, staging, or inclusion;
3. update a clean local `main` by fast-forward only when safe;
4. create or use one focused branch named `knowledge/<slug>`, `source/<slug>`, `skill/<slug>`, or `system/<slug>`.

After editing, run applicable local lint and tests. Report the semantic change, affected files, exact validation results, and unresolved concerns. Then stop and wait for explicit confirmation such as `Publish this change`.

Only after publication confirmation may you create a focused commit, push the branch, and create or update a GitLab Merge Request. Stage only the reported files. Publication never authorizes merge.

Any repository user may self-merge. Peer review is optional. Merge is always a separate human-triggered action; the normal choice is squash merge with source-branch deletion. Team Engram has no CI, pipelines, required status checks, operational Log, or checkpoint workflow.

Resolve only unambiguous mechanical conflicts. Present conflicts between meanings, claims, decisions, or canonical edits to the user. Close Merge Requests or delete branches only after explicit confirmation.

## User-facing goals and skills

Users may describe goals in plain language; route them to these skills:

- `query-team-engram` — answer from the maintained corpus with page links;
- `update-team-engram` — add or update reusable Knowledge or Decisions locally;
- `ingest-source` — preserve and analyze a source, then integrate warranted synthesis;
- `audit-team-engram` — run deterministic-first read-only structural and semantic review;
- `manage-shared-skill` — create or materially update a shared skill;
- `publish-team-engram-change` — internal publication helper used only after explicit confirmation.

Advanced helpers:

- `project-map` — navigate large multi-session efforts, normally in the attached project repository;
- `explore` — develop one unresolved question without creating Team Engram Session files;
- `grilling` — pressure-test a decision in conversation;
- `writing-great-skills` — mandatory standard before creating or materially changing a shared skill.

Query and Audit do not edit tracked content. Audit may regenerate the ignored Index. Apply Audit findings only through a separate update request.

## Shared skills

`.agents/skills/<skill-name>/SKILL.md` is the canonical shared-skill path. Do not duplicate skills under another adapter tree. Shared reusable skills belong here; project-only skills stay with the project. Avoid duplicate skill names across attached roots.

All pilot users are peers. Do not invent domain ownership, CODEOWNERS, access tiers, mandatory review, or prebuilt domains.
