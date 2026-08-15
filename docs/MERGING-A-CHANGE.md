# Merge a Change

## Purpose

Accept a published Team Engram Merge Request into canonical `main` after reviewing its visible diff and local validation evidence.

## Prerequisites

- The GitLab Merge Request is open and targets `main`.
- Its branch is current enough to merge or has been safely refreshed.
- The diff contains only the intended focused change.
- Local validation results are present and acceptable.
- Any discussion or semantic disagreement is resolved.
- You have permission to self-merge. Peer review is optional, not mandatory.

## Cursor prompt

Before acting in GitLab, ask:

```text
Review this Team Engram Merge Request for merge readiness: <MR URL>. Compare its diff with the stated purpose, check the recorded local validation, identify unresolved discussions or semantic conflicts, and tell me whether it is safe to self-merge. Do not push, update, or merge anything.
```

## What Cursor does and where it stops

Cursor performs a read-only readiness review. It may recommend merge, revision, optional peer review, or abandonment. It must not trigger merge based on publication approval or a general request to review.

The human user performs the merge in GitLab. Select **Squash commits** and **Delete source branch** when available, then click **Merge**. This explicit GitLab action is the merge boundary.

## Expected result

- GitLab marks the Merge Request as merged.
- The focused change is present on `main` as a squashed change when configured.
- The remote source branch is deleted when selected.
- The MR remains the visible coordination and discussion record.

## Verification

In GitLab, open the merged commit and confirm the changed files. Then ask Cursor:

```text
Confirm that Merge Request <MR URL> is merged into Team Engram main. Do not change local files yet. Report the merge commit and whether the source branch still exists.
```

After verification, follow [Update your local copy](UPDATING-YOUR-LOCAL-COPY.md).

## Common errors

- **The user expects a pipeline:** Team Engram uses local validation and has no GitLab CI.
- **Merge is attempted with unresolved semantic conflict:** do not guess; revise or discuss first.
- **The wrong target branch is selected:** change the MR target to `main` before merge.
- **Unrelated files appear:** return the MR for correction.
- **The source branch remains:** it can be deleted later after verifying the merge.
- **A peer approval is treated as mandatory:** peer review is optional unless users choose it for that change.

## Safe recovery

- If not ready, leave the MR open and request a focused revision.
- If the change should not proceed, close the MR without merging and follow [Abandon or recover](ABANDONING-OR-RECOVERING-A-CHANGE.md).
- If an incorrect MR was merged, do not rewrite shared history. Prepare a focused revert or corrective MR and review it normally.
- If sensitive content was merged, contact a repository administrator immediately; ordinary revert does not remove it from history.

Rules: [Team Engram Protocol](../Protocols/Team-Engram-Protocol.md). Publication: [Publish](PUBLISHING-A-CHANGE.md).
