# Create or Update a Shared Skill

## Purpose

Create or materially improve reusable Cursor behavior that should be shared across projects and versioned with Team Engram.

## Prerequisites

- The behavior is reusable across projects; project-only behavior belongs in the project repository.
- Team Engram is open and repository skill discovery works.
- `writing-great-skills` is available under `.agents/skills/`.
- No attached project uses the same skill name.
- Unrelated local changes are understood and will remain untouched.

## Cursor prompt

```text
Create or materially update a shared Team Engram skill for <reusable task>. First load and follow writing-great-skills. Confirm that the behavior is shared rather than project-specific, search all attached roots for duplicate skill names, use .agents/skills/<skill-name>/SKILL.md as the canonical path, validate the skill and links locally, and show the changed files and semantic behavior change. Do not commit, push, create a Merge Request, or merge.
```

## What Cursor does and where it stops

Cursor creates a focused `skill/<slug>` branch, loads the skill-authoring standard, inspects existing skills and naming collisions, prepares the local change, and runs applicable deterministic validation. It must not create a duplicate adapter under `.cursor/skills/`.

The request authorizes local preparation only. Explicit `Publish this change` confirmation is required before commit, push, and MR creation or update. Merge is separate.

## Expected result

- One self-contained shared skill exists under `.agents/skills/<skill-name>/SKILL.md`.
- Its trigger is clear and its procedure is testable.
- It contains no project-only path, company secret, employee-specific path, or personal example.
- No attached root silently shadows its name.
- Validation output and behavior changes are summarized.

## Verification

Ask Cursor in a fresh context if practical:

```text
List the Team Engram shared skills you discover, explain when <skill-name> triggers, and validate it against writing-great-skills. Check links, referenced files, naming collisions across attached roots, and repository-specific content. Do not edit or publish.
```

Test the skill on a safe non-company example and compare the observed behavior with its documented procedure.

## Common errors

- **The skill is project-specific:** move it to that project and use a project-qualified name.
- **The name duplicates an attached project skill:** rename one explicitly; do not rely on precedence.
- **The skill is copied into `.cursor/skills/`:** `.agents/skills/` is canonical.
- **`writing-great-skills` was not loaded:** stop and restart the authoring pass with it.
- **Examples contain local absolute paths or private content:** replace them with portable placeholders.
- **Only Markdown syntax was checked:** test the trigger and procedure behavior.

## Safe recovery

- Revise the same local branch and revalidate.
- If the behavior belongs to one project, remove only the unpublished Team Engram draft and recreate it under that project's rules.
- If a name collision appears after attachment, stop using the ambiguous name until a qualified rename is reviewed.
- If the change was published but should not merge, close the MR; follow [Abandon or recover](ABANDONING-OR-RECOVERING-A-CHANGE.md).

Rules: [Team Engram Protocol](../Protocols/Team-Engram-Protocol.md). Publication: [Publish](PUBLISHING-A-CHANGE.md).
