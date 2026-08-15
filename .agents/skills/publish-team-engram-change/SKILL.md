---
name: publish-team-engram-change
description: Internal helper for preparing and publishing a Team Engram change.
disable-model-invocation: true
---

# Publish a Team Engram Change

This internal helper enforces the two-boundary contribution flow: prepare and validate locally, then publish only after fresh explicit confirmation. It never merges.

## Phase 1: Prepare

1. Inspect the current branch, working tree, staged state, and remotes. Identify every pre-existing change.
2. Preserve unrelated work. Never reset, clean, stash, overwrite, stage, or include it. If the requested change cannot be isolated safely, stop and report the blocker.
3. Before new edits, update clean local `main` by fast-forward only when safe, then create one focused branch:
   - `knowledge/<slug>`;
   - `source/<slug>`;
   - `skill/<slug>`;
   - `system/<slug>`.
4. If requested edits already exist, verify they are isolated on a suitable branch. Do not move or rewrite unrelated work merely to satisfy the preferred sequence.
5. Run applicable local validation. Team Engram has no CI or remote status checks.
6. Show:
   - semantic summary;
   - affected files;
   - validation commands and exact outcomes;
   - unresolved concerns;
   - proposed commit message and Merge Request title.
7. Stop and ask for explicit confirmation such as `Publish this change`. The original edit request, branch request, or prior publication approval is not confirmation for the current summarized diff.

## Phase 2: Publish after confirmation

1. Recheck the diff and working tree. If scope or meaning changed after the summary, summarize again and obtain fresh confirmation.
2. Stage only the reported files and verify the staged diff.
3. Create one focused English commit.
4. Push the focused branch, never `main`.
5. Create or update a GitLab Merge Request using verified available tooling. If automation or authentication is unavailable, provide the manual GitLab fallback and report publication as incomplete rather than guessing credentials or success.
6. Report the commit, remote branch, Merge Request URL or manual fallback, and validation state.
7. Stop. Never click, call, or automate merge.

## Recovery

Fix local validation on the same branch. Refresh a stale branch from `main`; resolve only unambiguous mechanical conflicts. Present semantic conflicts to the user. Closing a Merge Request or deleting local or remote branches requires explicit confirmation.

## Completion

Preparation is complete only when the diff is focused, validation is reported, and the confirmation stop is visible. Publication is complete only when commit, push, and Merge Request creation or update are verified. Merge is always outside this skill.
