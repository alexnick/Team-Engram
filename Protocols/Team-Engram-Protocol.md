# Team Engram Protocol

This protocol is the normative contract for Team Engram content, agent behavior, and collaboration during the pilot.

## 1. Purpose and language

Team Engram is a shared, Markdown-first corpus of reusable organizational knowledge. Every repository artifact—including content, instructions, examples, commits, and Merge Requests—is written in English. Conversation may use the user's preferred language; preserve exact source-language quotations where evidence requires them.

All repository users are equal peers with full content control. The pilot starts with no predefined domains and has no domain owners, CODEOWNERS, access tiers, mandatory peer review, CI, pipelines, or required status checks.

## 2. Repository boundary

Project-specific implementation, plans, configuration, current-state documentation, and project-only skills stay in the project repository. Team Engram contains standalone synthesis, shared terminology, decisions, sources, procedures, and skills that remain useful without the originating project attached.

When project work yields reusable knowledge:

1. keep project truth in the project repository;
2. search Team Engram for an existing canonical page;
3. propose a self-contained synthesis rather than copying project documentation;
4. link stable project evidence when useful and accessible; and
5. publish each repository's change independently under its own rules.

Team Engram is the stable root in a local multi-root workspace. Attached project rules govern project files; Team Engram rules govern Team Engram files.

## 3. Corpus and canonical state

`Engram/` contains only these initial content classes:

- `Knowledge/` — maintained reusable organizational understanding;
- `Decisions/` — consequential organizational choices and rationale;
- `Sources/Raw/` — immutable source snapshots or locator records;
- `Sources/Records/` — editable source-grounded analysis.

`main` is the merged canonical state. Unfinished work belongs on a focused branch and, after publication, in a Merge Request. Merged Knowledge is `active` unless explicitly marked `disputed`, `superseded`, or `archived`. Proposed decisions stay in a branch or Merge Request; merged decision records state `accepted`, `rejected`, or `superseded`.

Git commits and GitLab Merge Requests are the authoritative authorship, change, discussion, and rollback history. Team Engram has no operational Log or checkpoint workflow.

## 4. Knowledge, evidence, and provenance

Merged active Knowledge is the maintained organizational model, not automatic proof of an external fact. Independently authored organizational Knowledge does not require an external source.

Provenance is required when content claims derivation, verification, quotation, or attribution from named evidence. In answers and edits, distinguish:

- **Maintained knowledge** — what merged Team Engram pages currently say;
- **Source claim** — what named evidence says, with a direct page link and locator when available;
- **Decision** — an accepted or rejected choice in its stated scope;
- **Agent inference** — reasoning not already present in maintained knowledge or evidence.

Never invent citations, quotations, dates, authors, measurements, file paths, source locations, or access to unavailable material. Preserve contradictions and uncertainty when they affect meaning. Resolve mechanical conflicts when the combined result is unambiguous; present semantic conflicts to the user rather than guessing.

## 5. Source preservation

A requested ingest may preserve:

- an ordinary article-scale text source as an immutable Markdown snapshot in Git; or
- an immutable Markdown locator for a URL, PDF, archive, video, large binary, restricted document, or other externally stored artifact.

A stored artifact requires its recorded hash. A new or changed retrieval creates a new dated raw record or snapshot; existing raw payloads and locators are not rewritten to represent new content. Corrections use a new record or explicit addendum.

Editable source records link to at least one raw snapshot or locator. The raw layer preserves identity and retrieved material; the source record contains analysis. Canonical Knowledge is created or updated only when reusable synthesis is warranted. Ingesting a source does not require manufacturing a Knowledge page.

## 6. Structure and navigation

Create a canonical page when its subject stands alone, has an independent lifecycle, or is reused from multiple contexts. Otherwise update the existing page.

Create a folder, context, domain, or page type only when a coherent real-content cluster has an independent lifecycle or vocabulary, or repeatedly causes demonstrated navigation, retrieval, naming, or progressive-loading problems. The proposal must name the problem and account for routing, templates, validation, and onboarding. Do not create empty taxonomies or catch-all folders.

`CONTEXT-MAP.md` is the short committed router. `Engram/INDEX.md` is deterministic, locally generated, and ignored by Git. Regenerate a missing or stale Index before Query, Audit, and applicable writing work. The Index and Context Map aid discovery; they are not substantive evidence.

Use resolvable relative Markdown links. Do not invent targets. Load context progressively and avoid broad scans except for an explicitly broad audit or repository-wide change.

## 7. Local change and publication lifecycle

A user's request to add, update, ingest, or change a shared skill authorizes a focused local branch proposal within that scope. It does not authorize publication or merge.

Before writing, the agent:

1. inspects the working tree and current branch;
2. preserves all unrelated changes without reset, cleanup, hiding, staging, or inclusion;
3. updates clean local `main` by fast-forward only when safe; and
4. creates or uses one focused branch named `knowledge/<slug>`, `source/<slug>`, `skill/<slug>`, or `system/<slug>`.

After editing, the agent runs applicable local validation and reports the semantic change, affected files, results, and unresolved concerns. The agent then stops and waits for explicit publication confirmation such as `Publish this change`.

Only after that confirmation may the agent create a focused commit, push the branch, and create or update a GitLab Merge Request. It stages only the reported files. Publication confirmation never authorizes merge.

Any repository user may review and self-merge in GitLab; peer review is optional. Merge is always a separate human-triggered action. The normal choice is squash merge with source-branch deletion.

## 8. Validation and recovery

Validation is local. Use repository lint and relevant tests; report exact commands and outcomes. Generated ignored state must not enter a commit.

- Fix failed validation on the same branch before publication.
- Update an existing Merge Request with focused follow-up commits after a new publication confirmation.
- Refresh stale branches from `main` and report conflicts.
- Stop for user direction on conflicting claims, decisions, or canonical meanings.
- Close a Merge Request or delete local or remote branches only after explicit confirmation.
- If unrelated work prevents safe isolation, stop and explain the blocker without altering it.

Query and Audit are read-only with respect to tracked content. Audit may regenerate the ignored local Index. Audit reports proposed fixes; a separate update request applies them.

## 9. Shared skills

`.agents/skills/<skill-name>/SKILL.md` is the canonical and Cursor-recognized shared-skill location. Do not duplicate skills under another adapter tree.

Shared reusable skills belong in Team Engram. Project-only build, deployment, codebase, or product-domain skills belong in the relevant project. Avoid duplicate skill names across attached roots; qualify a project specialization instead of shadowing a shared skill.

Load `writing-great-skills` before creating or materially changing a shared skill. Shared-skill changes use the same focused local validation and publication lifecycle as knowledge changes.
