# Set Up Team Engram in Cursor

## Purpose

Use this guide the first time you open Team Engram on a machine, when shared skills are not discovered, or when you want a stable multi-root workspace.

## Prerequisites

- Cursor is installed.
- You can clone or open the Team Engram repository.
- You have access to the team's GitLab project for collaboration tasks.
- The visible starting state is either Cursor's welcome screen or an open Team Engram folder.

## Cursor prompt

After opening Team Engram, ask:

```text
Read the instructions that govern this Team Engram repository. List the shared skills you discover under .agents/skills and confirm whether writing-great-skills is available. Check that the local generated Index is ignored by Git. Do not edit, commit, push, or publish anything.
```

## What Cursor does and where it stops

Cursor reads repository instructions, inspects `.agents/skills/`, checks Git ignore behavior, and reports its findings. This is read-only. It may not install software, change settings, edit files, or publish anything without a separate request.

To create a local multi-root workspace, copy `team-engram.code-workspace.example` to `team-engram.code-workspace`, then edit only the local copy. Ask:

```text
Create my gitignored local Team Engram workspace file from team-engram.code-workspace.example. Keep Team Engram as the first stable folder. Do not add a project path yet and do not publish the local workspace file.
```

Creating the gitignored local workspace file is authorized by that request. No corpus or repository publication is authorized.

## Expected result

- Cursor recognizes Team Engram as the primary repository.
- Team Engram shared skills are visible, including `writing-great-skills`.
- A local `team-engram.code-workspace` exists only if requested and does not appear in Git changes.
- `Engram/INDEX.md` is treated as generated local state.

## Verification

Ask:

```text
Show whether team-engram.code-workspace and Engram/INDEX.md are ignored. Then list the instruction and skill locations that apply to Team Engram files. Do not change anything.
```

Open the local workspace file in Cursor and confirm Team Engram is the first folder.

## Common errors

- **Skills are missing:** the repository root may not be open, or the installed Cursor version may not have refreshed repository skills.
- **A local workspace file appears in Git:** it has an unexpected name or `.gitignore` is stale.
- **The example contains an absolute path:** do not publish it; shared examples must be portable.
- **A project skill has the same name as a Team Engram skill:** rename the project specialization with a project-qualified name instead of relying on shadowing.

## Safe recovery

1. Keep the repository files unchanged.
2. Close and reopen the Team Engram folder or workspace, then ask Cursor to rescan skills.
3. If the local workspace file is tracked, stop before commit; rename it to `team-engram.code-workspace` and verify ignore behavior.
4. If setup remains uncertain, use Team Engram as a single-folder workspace until discovery is verified. Do not duplicate skills under `.cursor/skills/` as a workaround.

Next: [Working with projects](WORKING-WITH-PROJECTS.md), [Quickstart](../QUICKSTART.md), or the [protocol](../Protocols/Team-Engram-Protocol.md).
