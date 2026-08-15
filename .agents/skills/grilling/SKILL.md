---
name: grilling
description: Use to pressure-test a plan through dependency-ordered questions.
---

# Grilling

Interview the user relentlessly until you reach shared understanding. Map the problem as a **design tree** whose **frontier** contains every decision whose prerequisites are settled.

## Rounds

Ask the whole frontier in one numbered round and give a recommended answer for each question. Wait for the user's answers, reshape the tree, recompute the frontier, and continue. A question that depends on another open answer belongs to a later round.

Finding facts is the agent's job. Look them up or delegate independent investigation without blocking unrelated frontier questions. Decisions remain the user's.

If the user asks to slow down, use rounds of one question; use `explore` when that is the better continuing mode.

## Ephemeral by design

The design tree and frontier live only in conversation. This skill writes no Team Engram session or other persistent file and does not act on conclusions. It ends when the frontier is empty and the user confirms shared understanding.

After confirmation, route project-specific results to the project repository under its rules and reusable organizational synthesis to `update-team-engram`. A durable write is optional.
