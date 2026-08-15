# Audit Team Engram

## Purpose

Check deterministic structure and semantic quality without silently repairing the corpus.

## Prerequisites

- Team Engram is open in Cursor.
- The working tree state is known.
- The local Index may be regenerated before the audit.
- You have chosen the scope: whole corpus, selected pages, sources, links, or shared skills.

## Cursor prompt

```text
Audit Team Engram. Regenerate the ignored local Index, run the deterministic lint and applicable tests, then inspect for duplicate canonical pages, broken provenance, raw/derived mixing, stale or conflicting claims, unsupported structure, secrets, and project-only content. Report findings by severity with file links and evidence. Do not edit, commit, push, create a Merge Request, or merge.
```

For a narrow audit:

```text
Audit only <path or topic> for <concern>. Distinguish deterministic failures from semantic review findings. Do not fix anything.
```

## What Cursor does and where it stops

Cursor may refresh generated local state and run read-only validation. It reports deterministic tool output separately from semantic findings and uncertainty. Audit does not authorize fixes, even when they appear obvious.

To fix findings, choose specific items and use [Add or update Knowledge](ADDING-OR-UPDATING-KNOWLEDGE.md), [Ingest](INGESTING-A-SOURCE.md), or [Shared skill](CREATING-OR-UPDATING-A-SHARED-SKILL.md). Publication remains separate.

## Expected result

A report containing:

- scope and repository state;
- commands or checks actually run;
- pass/fail results for deterministic checks;
- semantic findings with severity, evidence, and affected files;
- items not verified and why;
- no unrequested corpus changes.

## Verification

Ask:

```text
Show the exact local validation results and confirm whether any tracked file changed during the audit. For each semantic finding, link the evidence and state whether it is certain or needs human judgment.
```

Confirm that `Engram/INDEX.md` remains ignored and no repair commit or MR exists.

## Common errors

- **Audit edits files:** findings and fixes must be separate actions.
- **Semantic guesses are reported as deterministic failures:** label the kind of evidence.
- **Only the generated Index is checked:** audit the actual pages.
- **A stale source is called false without evidence:** report staleness or conflict precisely.
- **Unrelated dirty work is included in a fix:** stop and separate scopes.

## Safe recovery

- If an audit changed tracked files unexpectedly, stop and inspect the diff; do not reset unrelated work.
- If tooling fails, report the command, error, and unverified checks. Do not replace missing output with a plausible result.
- If the scope is too broad, narrow by content type, path, or topic and rerun.
- Prepare fixes on focused branches only after the user selects findings.

Rules: [Team Engram Protocol](../Protocols/Team-Engram-Protocol.md). Recovery: [Abandon or recover](ABANDONING-OR-RECOVERING-A-CHANGE.md).
