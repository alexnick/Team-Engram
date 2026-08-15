# Abandon or Recover a Change

## Purpose

Pause, discard, restore, or continue local or published work without losing unrelated changes or rewriting shared history.

## Prerequisites

- Identify whether the change is local only, published as an open MR, or already merged.
- Inspect the current branch, working tree, changed files, commits, and related GitLab MR.
- Identify unrelated work and leave it untouched.
- Decide whether you want to pause, continue, close, discard, or correct the change.

## Cursor prompts

Start with a read-only inventory:

```text
Inspect this Team Engram change and classify it as local-only, published, or merged. Show the branch, changed files, commits, Merge Request state, validation state, and unrelated work. Propose safe options to pause, continue, abandon, or recover it. Do not reset, clean, stash, delete branches, close a Merge Request, push, revert, or merge.
```

To pause:

```text
Leave this change safely on its current branch and give me a concise resume note with the branch, purpose, validation state, and next step. Do not publish or delete anything.
```

To abandon after reviewing the inventory:

```text
Abandon only the identified Team Engram change. Close its open Merge Request if one exists, and remove its remote and local branches only after showing me the exact actions and receiving my confirmation. Preserve all unrelated work and shared history.
```

## What Cursor does and where it stops

Cursor first inventories state and proposes non-destructive options. Pausing requires no publication. Closing an MR, deleting a remote branch, deleting a local branch, discarding uncommitted edits, or creating a corrective revert are distinct actions and require explicit confirmation of the exact scope.

Cursor never uses reset, clean, stash, force-push, or history rewriting merely to simplify recovery.

## Expected result

Depending on the chosen path:

- **Pause:** work remains on a named branch with a clear resume note.
- **Continue:** the branch is safely refreshed, validated, and ready for review or publication.
- **Abandon unpublished:** only the confirmed local draft and branch are removed.
- **Abandon published:** the MR is closed and branches are removed only when confirmed.
- **Correct merged work:** a new focused corrective or revert MR preserves history.

## Verification

Ask:

```text
Show the final branch and working-tree state, confirm the Merge Request state, list any remaining branches related to this change, and prove that unrelated files were not modified or deleted. Do not take further action.
```

Check GitLab directly for MR and remote-branch state.

## Common errors

- **Closing an MR is assumed to erase its commits:** GitLab history may retain them.
- **A local branch is deleted before unpublished work is reviewed:** inventory first.
- **Reset or clean removes unrelated files:** these destructive shortcuts are not normal recovery.
- **A merged change is force-removed from history:** use a corrective MR instead.
- **Sensitive content is treated as ordinary abandonment:** contact an administrator; branch deletion is not sufficient remediation.
- **An unknown branch is called stale and deleted:** compare it with GitLab and `main` first.

## Safe recovery

- When uncertain, pause rather than delete.
- Copy the resume summary outside transient chat if work will continue later, but do not create an operation log in Team Engram.
- If an action was only partially completed, re-inventory real local and GitLab state before retrying.
- For conflicts, use [Resolve conflicts](RESOLVING-CONFLICTS.md).
- For merged mistakes, create a transparent corrective MR through [Publish](PUBLISHING-A-CHANGE.md) and [Merge](MERGING-A-CHANGE.md).

Rules: [Team Engram Protocol](../Protocols/Team-Engram-Protocol.md).
