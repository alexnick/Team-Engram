# Team Engram Glossary

## Purpose

Use this glossary when a guide, Cursor summary, or GitLab page uses an unfamiliar term.

## Prerequisites

None. Reading the glossary changes nothing.

## Cursor prompt

```text
Explain the Team Engram term <term> in plain English, give one safe example, and link the guide that uses it. Do not change files.
```

## Terms

- **Attached project:** an independent project repository added locally to the same Cursor multi-root workspace. It is not copied into Team Engram.
- **Branch:** an isolated line of local or remote work for one focused change. Team Engram uses names such as `knowledge/<slug>`, `source/<slug>`, `skill/<slug>`, and `system/<slug>`.
- **Canonical:** the current shared state on `main`. A local draft or open Merge Request is not canonical.
- **Corpus:** the maintained Markdown content under `Engram/`.
- **Cursor:** the primary editor and agent interface used to operate Team Engram.
- **Decision:** a consequential accepted choice recorded under `Engram/Decisions/`.
- **Derived source record:** editable analysis under `Engram/Sources/Records/` that points to raw source material and distinguishes claims, evidence, interpretation, inference, and limits.
- **Deterministic validation:** a repeatable local check, such as schema, structure, or link lint, whose result does not depend on subjective judgment.
- **Fast-forward-only update:** a safe local update that advances `main` without creating a merge commit or overwriting divergent local history.
- **Focused change:** one coherent purpose with only the files needed for that purpose.
- **Generated Index:** `Engram/INDEX.md`, a deterministic local discovery catalog. It is ignored by Git, is not edited by hand, and is not evidence.
- **Git:** the version-history system used locally and by GitLab.
- **GitLab:** the shared remote, visible diff, discussion, Merge Request, merge action, and history service used by the work collaboration flow.
- **Knowledge:** maintained reusable organizational synthesis under `Engram/Knowledge/`.
- **Local preparation:** Cursor's inspected, focused file change and validation before publication. Other users cannot see it.
- **Main:** the canonical shared branch.
- **Mechanical conflict:** a conflict whose combined correct text is unambiguous, such as compatible link or formatting edits.
- **Merge:** the separate human-triggered GitLab action that accepts an MR into `main`.
- **Merge Request (MR):** GitLab's visible proposal containing a branch diff, discussion, local validation record, and merge action.
- **Multi-root workspace:** one local Cursor workspace that opens Team Engram and independent project repositories side by side.
- **Provenance:** traceable origin information required when content claims derivation, verification, quotation, or attribution from named evidence.
- **Publish:** after explicit `Publish this change` confirmation, commit and push a focused branch and create or update its GitLab MR. Publish does not mean merge.
- **Raw snapshot:** an immutable Markdown preservation of source text under `Engram/Sources/Raw/`. A changed source receives a new snapshot.
- **Semantic conflict:** a disagreement about meaning, truth, lifecycle, decision, or competing canonical edits. Cursor must not resolve it by guessing.
- **Semantic summary:** a plain-language account of what meaning or behavior changes, not merely a file or line count.
- **Shared skill:** reusable agent behavior under `.agents/skills/` that applies across projects.
- **Source locator:** a raw Markdown record that identifies an externally stored item without adding a large or binary payload to Git.
- **Squash merge:** a GitLab merge option that records a focused MR as one canonical commit.
- **Working tree:** the files currently checked out locally, including uncommitted edits.

## What Cursor does and where it stops

A glossary explanation is read-only. If a term appears to be used inconsistently, Cursor reports the inconsistency; it does not silently edit guides or protocol rules.

## Expected result

A plain-English explanation linked to the relevant guide or protocol.

## Verification

Compare the explanation with the term above and the linked task guide. The [Team Engram Protocol](../Protocols/Team-Engram-Protocol.md) controls if a short glossary definition omits an edge case.

## Common errors

- **Publish and merge are treated as synonyms:** they are separate confirmation boundaries.
- **The Index is treated as canonical content:** it is generated discovery state.
- **An open MR is treated as accepted Knowledge:** only merged `main` is canonical.
- **Project truth is treated as shared Knowledge:** attach projects but keep their implementation truth there.

## Safe recovery

Ask Cursor to cite the exact guide or protocol section. If documentation genuinely conflicts, run a read-only [Audit](AUDITING-TEAM-ENGRAM.md) and prepare a focused documentation correction separately.
