# Work with Project Repositories

## Purpose

Attach a project repository to the stable Team Engram Cursor workspace without copying project truth into Team Engram or committing machine-specific paths.

## Prerequisites

- [Cursor setup](CURSOR-SETUP.md) is complete.
- The project repository already exists in its own local folder.
- `team-engram.code-workspace` is a gitignored local file.
- You know whether the task changes Team Engram, the project, or both.

## Cursor prompt

```text
Add the local project repository at <local project path> to my gitignored Team Engram multi-root workspace. Keep Team Engram as the first stable folder. Do not copy or move project files, do not change either repository, and do not publish the workspace file. Then explain which repository's instructions govern each root.
```

For a cross-repository question:

```text
Use the attached project as evidence, but keep project-specific implementation truth in that project. Propose only reusable synthesis for Team Engram, and report changes and validation separately for each repository.
```

## What Cursor does and where it stops

Cursor edits only the local workspace file and opens both independent roots. Team Engram instructions govern Team Engram files; project instructions govern project files. A cross-repository task must preserve both scopes and treat publication in each repository separately.

Adding a folder to the local workspace does not authorize edits, commits, pushes, Merge Requests, or copying content between repositories.

## Expected result

- Both repositories appear as separate top-level folders in Cursor.
- Neither repository is nested inside the other.
- Project source code, plans, configuration, status, and project-only skills remain in the project.
- Any Team Engram proposal is standalone and reusable without the project attached.

## Verification

Ask:

```text
List the workspace roots, their repository boundaries, their applicable instruction files, and any duplicate skill names. Confirm that the workspace file is ignored and that no repository file changed.
```

## Common errors

- **Project files were copied into Team Engram:** attaching a folder is not importing content.
- **A project path was committed:** employee-specific paths belong only in the local ignored workspace file.
- **Rules are mixed:** Team Engram rules do not override project implementation rules.
- **The same skill name appears in both roots:** use a project-qualified name for the project specialization.
- **A project document is proposed as shared Knowledge unchanged:** synthesize the reusable lesson and link stable evidence when appropriate.

## Safe recovery

- Remove the project folder entry from the local workspace; this does not delete the repository.
- If files were copied, stop and identify them before deletion. Do not clean or reset unrelated work.
- If both repositories were changed, review and validate each diff separately. Publish neither until each scope is understood.
- Use [Abandon or recover](ABANDONING-OR-RECOVERING-A-CHANGE.md) for accidental repository changes.

Rules: [Team Engram Protocol](../Protocols/Team-Engram-Protocol.md). Related: [Shared skills](CREATING-OR-UPDATING-A-SHARED-SKILL.md).
