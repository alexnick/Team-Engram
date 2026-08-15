# Team Engram Quickstart

This path assumes no Git or AI-agent experience. Cursor performs the mechanical work and explains what it finds. Normal use does not require you to type Git commands.

## 1. Clone and open Team Engram

In Cursor, choose **Clone Repository**, paste your team's GitLab repository URL, choose a local folder, and open the cloned repository.

If the repository is already on your machine, choose **Open Folder** and select it.

Then ask Cursor:

```text
Read the Team Engram instructions for this repository. Confirm that you can see the shared skills under .agents/skills, including writing-great-skills. Do not change any files.
```

**Expected result:** Cursor identifies Team Engram as the stable repository, reports the discovered skills, and makes no changes.

If skill discovery fails, stop and follow [Cursor setup](docs/CURSOR-SETUP.md).

## 2. Check the empty or current corpus

Ask:

```text
Check Team Engram's local status, regenerate the local Index if needed, and run the deterministic audit. Do not fix or publish anything. Summarize the result in plain English.
```

**Expected result:** `Engram/INDEX.md` exists locally but does not appear as a change for publication. Cursor reports whether lint passed and whether unrelated local changes already exist.

If unexplained changes exist, do not let Cursor reset or hide them. Use [Abandoning or recovering a change](docs/ABANDONING-OR-RECOVERING-A-CHANGE.md).

## 3. Ask Team Engram

```text
What does Team Engram currently know about reviewing shared knowledge? Link every maintained page and source record you use. If the repository does not contain an answer, say so clearly. Do not change files.
```

**Expected result:** a read-only answer grounded in repository pages, or a clear statement that the corpus does not yet answer the question.

Learn more in [Ask Team Engram](docs/ASKING-TEAM-ENGRAM.md).

## 4. Prepare one local Knowledge change

Choose a small reusable fact or practice that is appropriate for this repository's audience. For a clean public starter, use this generic example:

```text
Prepare a Team Engram Knowledge page explaining that a shared glossary should define unfamiliar collaboration terms in plain language. Search for an existing canonical page first. Make only the focused local change, regenerate the local Index, run validation, and show me the changed files and semantic summary. Do not commit, push, create a Merge Request, or merge.
```

**Expected result:** Cursor creates or updates one Knowledge page on a focused branch, validates it locally, and stops with a reviewable summary. The request authorizes local preparation only.

Read [Add or update Knowledge](docs/ADDING-OR-UPDATING-KNOWLEDGE.md) before using real content.

## 5. Review before publication

Check Cursor's summary and open the changed Markdown file. Confirm that:

- the content is reusable outside one project;
- it contains no secret, unintended personal data, or material outside this repository's authorized audience;
- the diff contains only the intended files;
- local validation passed, or every failure is explained;
- `Engram/INDEX.md` is not included.

To revise, say:

```text
Revise the local change as follows: <your correction>. Re-run validation and show the updated summary. Do not publish.
```

To discard or pause it, use [Abandoning or recovering a change](docs/ABANDONING-OR-RECOVERING-A-CHANGE.md).

## 6. Publish to GitLab

When the local change is correct, say exactly:

```text
Publish this change.
```

**Confirmation boundary:** this authorizes Cursor to commit the focused change, push its branch, and create or update a GitLab Merge Request. It does **not** authorize merge.

**Expected result:** Cursor returns the Merge Request link, branch name, commit summary, and final local validation results. If automatic MR creation is unavailable, Cursor should push the branch and give you the exact GitLab fallback steps without inventing a link.

See [Publishing a change](docs/PUBLISHING-A-CHANGE.md).

## 7. Review and self-merge

Open the Merge Request in GitLab, review the diff, and optionally ask a peer to review. If it is correct, use GitLab's **Squash commits** and **Delete source branch** options, then click **Merge** yourself.

Merge is deliberately separate from publication. Cursor must not merge because you said `Publish this change`.

See [Merging a change](docs/MERGING-A-CHANGE.md).

## 8. Refresh your local copy

After GitLab shows the Merge Request as merged, ask:

```text
Update my local Team Engram main branch from GitLab using a fast-forward-only update. Remove the merged local branch only if it is safe. Do not discard unrelated work.
```

**Expected result:** local `main` contains the merged page, the obsolete local branch is removed when safe, the local Index is refreshed, and the working tree is clean except for explained local-only state.

Next: [User Guide](USER-GUIDE.md) or the [task guide index](docs/README.md).
