---
name: project-map
description: Use for large multi-session projects and decision maps.
---

# Project Map

Maintain a low-resolution map for a project too broad for one conversation. The map routes decisions and investigations; it does not replace canonical specifications, decisions, source records, or implementation plans.

## Location and scope

Store the map and tickets in the attached project repository by default, following that repository's rules. Team Engram has no internal project-storage area. Put a map in Team Engram only when Team Engram itself is the project being changed.

Use `Templates/Project-Map/MAP.md` and `Templates/Project-Map/TICKET.md`. Every ticket ID must have a globally distinctive project prefix such as `TEF-001`; never use generic repository-wide IDs such as `PM-001`.

## Procedure

1. Read the owning repository's instructions, context, and existing map. For cross-repository work, keep Team Engram and project changes separate.
2. Define the destination and account for existing inputs without loading every linked file.
3. Maintain these map sections: Destination, Inputs, Notes, Decisions so far, Current frontier, Blocked, Fog, Out of scope, and Operating rules.
4. Size each ticket for one decision or investigation. Use `grilling`, `explore`, `research`, `prototype`, or `task` as the ticket type.
5. Work the named ticket or the next unblocked frontier item. Independent research may run in parallel; otherwise keep one active ticket.
6. Resolve the ticket as a decision, canonical project update, blocked item, graduated fog item, or out-of-scope ruling.
7. Update the map and ticket. Promote results into canonical project artifacts only under that project's change rules. Promote reusable organizational synthesis into Team Engram through `update-team-engram`, never by copying the project document.
8. Run the owning repository's structural validation and report every changed planning and canonical file separately.

## Completion

The resolved ticket records its evidence and outcome, the map frontier is dependency-correct, blocked and fog items remain explicit, IDs are project-qualified, and no project-specific truth was moved into Team Engram.
