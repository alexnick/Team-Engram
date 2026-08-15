# Team Engram Context Map

This committed file is the short router for Team Engram. Keep it small. Cursor regenerates the complete local catalog at `Engram/INDEX.md` when needed.

## Start here

- [Quickstart](QUICKSTART.md)
- [User Guide](USER-GUIDE.md)
- [Team Engram corpus context](Engram/CONTEXT.md)
- [Task guide index](docs/README.md)
- [Team Engram Protocol](Protocols/Team-Engram-Protocol.md)

## Corpus

- [Knowledge](Engram/Knowledge/) — reusable maintained organizational synthesis.
- [Decisions](Engram/Decisions/) — consequential accepted choices and supersession history.
- [Raw sources](Engram/Sources/Raw/) — immutable Markdown snapshots or locator records.
- [Source records](Engram/Sources/Records/) — editable analysis linked to raw sources.
- `Engram/INDEX.md` — generated local catalog; gitignored and not evidence.

## Common actions

- [Ask](docs/ASKING-TEAM-ENGRAM.md)
- [Add or update Knowledge](docs/ADDING-OR-UPDATING-KNOWLEDGE.md)
- [Ingest a source](docs/INGESTING-A-SOURCE.md)
- [Audit](docs/AUDITING-TEAM-ENGRAM.md)
- [Create or update a shared skill](docs/CREATING-OR-UPDATING-A-SHARED-SKILL.md)
- [Publish](docs/PUBLISHING-A-CHANGE.md) and [merge](docs/MERGING-A-CHANGE.md)

## Maintenance

- Run local index generation before discovery-heavy work when the Index is stale or missing.
- Run local lint before publication.
- Do not add an operation log or turn this router into a full catalog; Git and GitLab preserve shared history.
- Add a new corpus area only after real content demonstrates a navigation or lifecycle need.
