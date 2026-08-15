---
name: audit-team-engram
description: Use when auditing Team Engram structure and meaning.
---

# Audit Team Engram

Run deterministic validation first, then perform a read-only semantic audit. Audit may refresh the ignored Index but never edits tracked meaning.

## Procedure

1. Read the protocol and inspect Git status so pre-existing work is distinguishable from findings.
2. Run `python Tools/engram.py index` and record its outcome.
3. Run `python Tools/engram.py lint`; capture the exact command, exit status, errors, and warnings. Never fabricate a pass when the command fails.
4. Scope semantic reading to the user's request. A repository-wide request permits broad Markdown inspection but not unrelated binaries, attached projects, caches, or secrets.
5. Check for:
   - contradictions, duplicate canonical pages, stale or superseded meaning, and knowledge gaps;
   - project-specific truth copied into Team Engram or reusable knowledge trapped in project material supplied for comparison;
   - source-derived claims without provenance or maintained synthesis presented as external proof;
   - raw records rewritten in place, source analysis mixed into raw snapshots, or stored artifacts without hashes;
   - speculative domains, empty taxonomy, unsupported page types, or structure without demonstrated pressure;
   - broken or misleading links, stale routing, and Index drift;
   - instructions or skills that conflict with the protocol, publication boundary, equal-user model, or English artifact policy.
6. Report findings without editing files.

## Report format

- **Deterministic checks** — commands, exit status, concise output;
- **Findings** — severity, exact file and line, evidence, consequence;
- **Clean checks** — meaningful checks that passed;
- **Proposed fixes** — focused changes, clearly separated from the audit.

## Completion

Every file in the requested scope is accounted for, uncertainty is labeled, and no tracked file, branch, stage, commit, remote, or Merge Request was changed. If the user requests fixes, hand off to `update-team-engram` or `manage-shared-skill` as appropriate.
