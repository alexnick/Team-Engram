# Resolve Conflicts

## Purpose

Safely reconcile a focused branch with newer canonical changes while distinguishing mechanical text conflicts from disagreements about meaning.

## Prerequisites

- The conflicting branch and its Merge Request, if published, are known.
- The working tree has been inspected for unrelated changes.
- The latest GitLab `main` has been fetched.
- You can review the intended meaning of both sides or identify someone who can.

## Cursor prompt

```text
Refresh this Team Engram branch from the latest GitLab main and inspect every conflict. Classify each as mechanical or semantic. Resolve only mechanical conflicts whose combined result is unambiguous. For semantic conflicts between claims, decisions, provenance, lifecycle status, or competing canonical edits, stop and show both versions, their sources, and the decision needed. Do not guess, publish, merge, reset, clean, or discard unrelated work.
```

## What Cursor does and where it stops

Cursor compares the branch with current `main`, reports the affected files, and may resolve formatting, ordering, or link conflicts only when the combined result is objectively clear. It stops at any conflict about meaning or authority and requests a user decision.

After all conflicts are resolved, Cursor reruns local validation and shows the semantic diff. Updating the remote branch still requires explicit [publication](PUBLISHING-A-CHANGE.md); merge remains separate.

## Expected result

- Every conflict is accounted for.
- Mechanical resolutions preserve both intended non-competing changes.
- Semantic choices are made by a user, not guessed by Cursor.
- Validation passes after resolution or failures are fully reported.
- The branch remains focused and unrelated work remains untouched.

## Verification

Ask:

```text
List each resolved conflict, classify it, explain the chosen result, and link the competing pages or source records. Confirm that no conflict marker remains, run local validation, and show the final semantic diff against current main. Do not publish.
```

Search the affected files for conflict markers and review rendered Markdown.

## Common errors

- **All conflicts are called mechanical:** wording differences may hide contradictory claims or lifecycle states.
- **Cursor chooses the newest text automatically:** recency does not establish correctness.
- **A raw snapshot is combined or rewritten:** preserve immutable versions separately.
- **Unrelated dirty work enters the resolution:** stop and separate scope.
- **Validation is skipped after conflict resolution:** links and metadata often break during merges.
- **Resolved local work is pushed without confirmation:** use the publication boundary.

## Safe recovery

- Before publication, leave the branch unchanged if the semantic decision is unavailable; document what blocks it.
- If conflict resolution is in progress and appears wrong, stop and inspect repository state before aborting. Do not run destructive cleanup blindly.
- Ask a peer for optional review when the meaning is consequential or disputed.
- If the branch is no longer worth resolving, follow [Abandon or recover](ABANDONING-OR-RECOVERING-A-CHANGE.md).
- If an incorrect result was merged, prepare a corrective MR rather than rewriting shared history.

Rules: [Team Engram Protocol](../Protocols/Team-Engram-Protocol.md). Update first: [Update local copy](UPDATING-YOUR-LOCAL-COPY.md).
