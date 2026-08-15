# Update Your Local Copy

## Purpose

Bring local Team Engram `main` up to date after other users merge changes, without overwriting local work.

## Prerequisites

- Team Engram is open in Cursor.
- You know whether the working tree contains local or untracked work.
- You are not in the middle of an unresolved merge or rebase.
- The GitLab remote is reachable.

## Cursor prompt

```text
Inspect my local Team Engram repository, explain any uncommitted or unpublished work, and update local main from GitLab using a fast-forward-only update. Do not reset, clean, stash, overwrite, rebase, or include unrelated work. If anything prevents a safe update, stop and explain it. After a successful update, regenerate the ignored local Index and run the quick local status check.
```

## What Cursor does and where it stops

Cursor inspects status first. If safe, it switches to `main`, fetches the remote, and performs only a fast-forward update. It refreshes generated local state afterward. It may remove a merged local branch only when the branch is fully accounted for and deletion is safe.

The prompt does not authorize discarding, hiding, publishing, or resolving conflicting local work. Cursor stops when the update cannot be fast-forwarded safely.

## Expected result

- Local `main` matches the current GitLab `main`.
- No unrelated local work is lost or hidden.
- `Engram/INDEX.md` is refreshed locally and remains ignored.
- Merged local branches are removed only when safe and requested or clearly covered.

## Verification

Ask:

```text
Show the current branch, whether local main matches GitLab main, the working-tree summary, and whether the generated Index is ignored. List any remaining local branches and explain which are merged, open, stale, or unknown. Do not change anything.
```

## Common errors

- **Local edits block switching to `main`:** identify their branch and purpose; do not reset them.
- **Fast-forward-only update fails:** local `main` has divergent commits or remote history changed; investigate before acting.
- **A stale feature branch is mistaken for lost work:** compare it with its MR and `main`.
- **The generated Index appears dirty:** verify `.gitignore` and regenerate it; do not commit it.
- **Cursor stashes automatically:** Team Engram does not hide unexplained work as a convenience.

## Safe recovery

- Keep local work on its current branch and update only after its status is understood.
- If local `main` diverged, ask Cursor to identify the commits and propose a non-destructive recovery; do not force-push or reset.
- If an open branch needs the new `main`, update the branch and follow [Resolve conflicts](RESOLVING-CONFLICTS.md) when necessary.
- If branch ownership or purpose is unclear, leave it in place and use [Abandon or recover](ABANDONING-OR-RECOVERING-A-CHANGE.md).

Rules: [Team Engram Protocol](../Protocols/Team-Engram-Protocol.md).
