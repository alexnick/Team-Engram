# Team Engram User Guide

Team Engram is a shared Markdown knowledge corpus operated primarily through Cursor. This guide explains the mental model and routes each task to one detailed guide. The [Team Engram Protocol](Protocols/Team-Engram-Protocol.md) is the authoritative source for storage, lifecycle, safety, and collaboration rules.

## The simple model

### Maintained knowledge

`Engram/Knowledge/` contains reusable organizational synthesis. A page may be independently authored; it does not need an external source merely to be useful. If it claims to derive from, verify against, quote, or attribute a named source, it must link to provenance.

### Decisions

`Engram/Decisions/` records consequential accepted choices. A decision should have a stable identity and preserve supersession relationships when a later decision replaces it.

### Sources

`Engram/Sources/Raw/` preserves immutable Markdown snapshots or stable locator records. `Engram/Sources/Records/` contains editable analysis of those sources. A raw source is evidence of what a source contained, not automatic proof that every claim is true.

Complete article-scale text—including multi-screen Confluence content—may be stored as Markdown. Large or binary artifacts remain external.

### Shared skills

`.agents/skills/` contains reusable agent behavior that should travel with Team Engram. Project-only build, deployment, coding, and domain workflows stay in their project repositories.

## What does not belong here

Keep project-specific truth in the project repository:

- source code and configuration;
- current implementation plans and task status;
- deployment and environment instructions;
- project-only decisions that are meaningless without the project;
- project-only skills.

Promote a reusable lesson by synthesis, not by copying a project document. See [Working with projects](docs/WORKING-WITH-PROJECTS.md).

## Three visible states of a change

1. **Local:** Cursor has prepared files on a focused branch. Other users cannot see them. Local preparation does not authorize publication.
2. **Published:** Cursor has committed and pushed the branch and created or updated a GitLab Merge Request after explicit `Publish this change` confirmation. The proposal is visible but not canonical.
3. **Merged:** a user has triggered merge in GitLab. Content on `main` is canonical; merged Knowledge is active unless explicitly disputed, superseded, or archived.

Git commits and Merge Requests are the authoritative change history. There is no Team Engram operation log.

## Everyday tasks

| Goal | Primary guide | Does it change files? |
|---|---|---|
| Set up Cursor | [Cursor setup](docs/CURSOR-SETUP.md) | Creates only a local workspace file when requested |
| Attach or remove projects | [Working with projects](docs/WORKING-WITH-PROJECTS.md) | Local workspace file only |
| Ask a question | [Ask Team Engram](docs/ASKING-TEAM-ENGRAM.md) | No corpus change; local Index may refresh |
| Add or update Knowledge | [Add or update Knowledge](docs/ADDING-OR-UPDATING-KNOWLEDGE.md) | Focused local corpus change |
| Preserve and analyze a source | [Ingest a source](docs/INGESTING-A-SOURCE.md) | Focused local source change |
| Audit the repository | [Audit Team Engram](docs/AUDITING-TEAM-ENGRAM.md) | Read-only unless you separately request fixes |
| Create or update shared behavior | [Shared skill](docs/CREATING-OR-UPDATING-A-SHARED-SKILL.md) | Focused local skill change |
| Make a local change visible | [Publish](docs/PUBLISHING-A-CHANGE.md) | Commit, push, and MR after confirmation |
| Accept a published change | [Merge](docs/MERGING-A-CHANGE.md) | Separate human-triggered GitLab action |
| Refresh after a merge | [Update local copy](docs/UPDATING-YOUR-LOCAL-COPY.md) | Updates local Git state and Index |
| Handle concurrent edits | [Resolve conflicts](docs/RESOLVING-CONFLICTS.md) | Only approved, reviewed conflict resolution |
| Pause, discard, or restore work | [Abandon or recover](docs/ABANDONING-OR-RECOVERING-A-CHANGE.md) | Depends on explicit choice |

## Cursor's normal safety boundary

For a writing task, Cursor may inspect, create a focused branch, prepare the requested local files, regenerate the ignored Index, and run local validation. Before publication it must show:

- the branch and affected files;
- a semantic summary, not only line counts;
- local validation results;
- unresolved questions or conflicts;
- any unrelated pre-existing changes it left untouched.

Only explicit publication confirmation authorizes commit, push, and Merge Request creation or update. Merge remains a separate human action. Rules and edge cases live in the [protocol](Protocols/Team-Engram-Protocol.md), not in every guide.

## Navigation and history

- Start discovery at [Context Map](CONTEXT-MAP.md).
- Let Cursor regenerate `Engram/INDEX.md` when missing or stale.
- Never edit or publish the generated Index.
- Use GitLab Merge Requests to inspect discussions and prior changes.
- Use Git file history when exact authorship or evolution matters.

## Structure grows only when needed

The starter corpus has Knowledge, Decisions, Sources/Raw, and Sources/Records. Do not create domains, catch-all folders, ownership trees, or new page types in advance. Propose structure only when a coherent real-content cluster has an independent lifecycle or repeatedly causes retrieval, naming, navigation, or context-loading problems.

## Advanced work

Project Map, Explore, and Grilling remain available for larger decisions and investigations. They support thinking; they do not bypass Team Engram's local validation, publication confirmation, or merge boundaries. Material shared-skill work must follow the [shared skill guide](docs/CREATING-OR-UPDATING-A-SHARED-SKILL.md).

## First use

Follow [Quickstart](QUICKSTART.md), then keep the [Glossary](docs/GLOSSARY.md) nearby while the collaboration terms become familiar.
