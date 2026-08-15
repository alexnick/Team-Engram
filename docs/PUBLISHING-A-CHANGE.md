# Publish a Change

## Purpose

Make a focused, validated local change visible in GitLab as a Merge Request. Publication does not make the change canonical and does not authorize merge.

## Prerequisites

- The change is on one focused branch such as `knowledge/<slug>`, `source/<slug>`, `skill/<slug>`, or `system/<slug>`.
- Cursor has shown the affected files and a semantic summary.
- Local validation has passed, or every unresolved result is understood and intentionally disclosed.
- The diff excludes unrelated work, secrets, employee-specific paths, `Engram/INDEX.md`, and local workspace files.
- A GitLab remote and authentication are available, or you accept the documented manual MR fallback.

## Cursor prompts

First review without publishing:

```text
Prepare the publication summary for this Team Engram branch. Show the semantic change, every affected file, local validation results, unresolved concerns, and any unrelated local changes you left untouched. Do not commit, push, create a Merge Request, or merge.
```

When satisfied, give the explicit confirmation:

```text
Publish this change.
```

## What Cursor does and where it stops

The exact confirmation authorizes Cursor to create a focused commit, push the current branch, and create or update one GitLab Merge Request. Cursor uses the repository MR template and reports what it actually completed.

Publication confirmation does **not** authorize Cursor to merge, enable CI, change branch protection, include unrelated files, rewrite history, or delete branches. If authentication or MR tooling is unavailable, Cursor stops after the safe completed step and provides truthful manual GitLab instructions.

## Expected result

- The focused branch exists on the GitLab remote.
- One Merge Request targets `main` and describes purpose, scope, local validation, boundaries, and unresolved concerns.
- Cursor returns the real MR URL when it created one.
- The MR is open and unmerged.

## Verification

Open the GitLab Merge Request and confirm:

- target branch is `main`;
- the file list matches the local publication summary;
- no generated Index, local workspace, secret, or unrelated file is present;
- local checks are recorded honestly;
- no pipeline is expected or required;
- the merge button has not been triggered.

Ask Cursor:

```text
Compare the open GitLab Merge Request with my local branch and report any difference. Do not push, update, or merge it.
```

## Common errors

- **`Publish this change` was interpreted as merge:** publication stops at an open MR.
- **Local validation is described as GitLab CI:** Team Engram has no pipeline; record local checks.
- **The MR includes unrelated changes:** close or correct it before merge; never hide unrelated work.
- **Automatic MR creation fails:** use the pushed branch in GitLab's New Merge Request page and copy the template accurately.
- **The branch is stale:** update it safely and resolve conflicts before publication or merge.
- **A generated or local-only file is included:** remove it from the focused branch and update the MR.

## Safe recovery

- Revise an open MR by preparing validated focused changes on the same branch, then explicitly publish the update.
- If publication was accidental, do not merge. Close the MR; delete remote or local branches only after explicit confirmation.
- If sensitive content was pushed, stop normal recovery and contact a repository administrator. Closing the MR or deleting the branch does not erase Git history.
- For stale work or conflicts, use [Resolve conflicts](RESOLVING-CONFLICTS.md).
- For rejection or abandonment, use [Abandon or recover](ABANDONING-OR-RECOVERING-A-CHANGE.md).

Rules: [Team Engram Protocol](../Protocols/Team-Engram-Protocol.md). Next: [Merge](MERGING-A-CHANGE.md).
