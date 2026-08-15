---
name: manage-shared-skill
description: Use when creating or changing a shared Team Engram skill.
---

# Manage a Shared Skill

Create or materially change the canonical skill under `.agents/skills/`. Shared skills are reusable across the organization; project-only skills stay in their project repositories.

## Procedure

1. Load `writing-great-skills` and `publish-team-engram-change` before editing.
2. Confirm the skill is shared. Keep build, deployment, codebase, and project-domain behavior in the owning project repository.
3. Search `.agents/skills/` for an existing capability and attached roots for a naming collision. Extend a suitable shared skill instead of creating a duplicate. Qualify project specializations rather than shadowing a Team Engram skill.
4. Store canonical content only at `.agents/skills/<skill-name>/SKILL.md`. Do not create `.cursor/skills/`, workflow wrappers, or synchronization adapters.
5. Choose invocation deliberately. Give a model-invoked skill a concise trigger description; use `disable-model-invocation: true` for a user-only reference skill.
6. Write predictable steps with checkable completion criteria. Keep one source of truth, remove sediment, and disclose branch-specific reference material behind explicit pointers.
7. Validate every changed skill:
   - YAML frontmatter starts at byte zero and contains `name` and `description`;
   - directory and `name` match and use lowercase hyphenated names;
   - linked files and referenced skills exist;
   - examples, paths, and repository artifacts are English;
   - no obsolete Team Engram operation or project-local assumption remains.
8. Run `python Tools/engram.py lint` and any repository skill validation available.
9. Use `publish-team-engram-change` to report behavior changes, files, validation, and unresolved concerns, then stop for explicit publication confirmation.

## Completion

The shared-versus-project boundary is satisfied, the canonical skill has no duplicate adapter, every changed file is accounted for, and publication has not occurred without fresh confirmation.
