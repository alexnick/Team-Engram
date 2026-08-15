# Changelog

All notable changes to Team Engram are recorded here. The project is pre-release; earlier product work is summarized without assigning unsupported release dates.

## Unreleased

### Added

- English, zero-experience task guides for Cursor setup, attached projects, Ask, Add or Update, Ingest, Audit, shared skills, Publish, Merge, local update, conflicts, abandonment or recovery, and terminology.
- A tracked multi-root Cursor workspace example paired with a gitignored local workspace file.
- A GitLab Merge Request template for focused, locally validated changes.
- GitLab-oriented self-merge, synchronization, and recovery guidance with concrete Cursor prompts.

### Changed

- Reframed the product as Team Engram: a shared organizational knowledge corpus rather than a personal Brain.
- Reduced the starter corpus to Knowledge, Decisions, Sources/Raw, Sources/Records, corpus Context, and a locally generated Index.
- Made `.agents/skills/` the canonical location for shared reusable skills; project-only skills remain in project repositories.
- Established Cursor as the primary interface and Team Engram as the stable root of a local multi-root workspace.
- Replaced automatic or implicit publication with a two-boundary flow: local preparation, then explicit `Publish this change` confirmation for commit, push, and GitLab Merge Request creation or update. Merge remains separately human-triggered.
- Defined local validation, optional peer review, squash self-merge, and branch cleanup without GitLab CI or pipelines.
- Allowed complete article-scale text, including multi-screen Confluence articles, to be preserved incrementally as Markdown snapshots while large or binary artifacts remain external.
- Made `CONTEXT-MAP.md` the committed router and `Engram/INDEX.md` deterministic, local, generated, and gitignored.
- Replaced duplicated operation history with Git commits and GitLab Merge Requests.
- Rewrote README, Quickstart, User Guide, Context Map, corpus Context, and public documentation for the shared pilot.

### Removed

- Personal, Health, Inbox, Entities, Events, Sessions, Learning, Feedback, Dashboard, review-state, and internal Project starter areas.
- Capture, Review, Checkpoint, Teach, and product/private synchronization guidance from the Team Engram path.
- The append-only `Engram/LOG.md` and committed generated Index.
- Predefined domains, personal examples, and assumptions that a repository user has a privileged ownership role.
- GitLab CI, pipelines, required status checks, mandatory review, and automatic merge from the pilot design.

## Previous public Engram work

### Added

- Markdown-first durable knowledge with raw and derived source separation.
- Ingest, Query, Sync, Lint, Project Map, Explore, Grilling, and skill-authoring workflows.
- Templates, deterministic local tooling, agent instructions, and MIT licensing.

### Changed

- Renamed the earlier product from Life Workspace to Engram and standardized `Engram/`, `Tools/engram.py`, and English public artifacts.
- Consolidated onboarding and documented product/private maintenance boundaries before the Team Engram fork.
