# Team Engram

**A shared, Markdown-first knowledge base maintained with Cursor and GitLab.**

Team Engram keeps reusable organizational knowledge available across projects and conversations. Cursor is the primary interface, Markdown is the durable state, and GitLab Merge Requests provide visible collaboration history.

Start with an empty corpus. Add real knowledge only when it is useful, and let the structure emerge from repeated use.

## What belongs here

Team Engram contains knowledge that remains useful when the originating project is not attached:

- reusable explanations, practices, and models;
- consequential organizational decisions;
- source records and article-scale Markdown snapshots;
- shared Cursor skills used across projects.

Project implementation truth stays in the project repository: code, plans, configuration, current project status, deployment instructions, and project-only skills. See [Working with projects](docs/WORKING-WITH-PROJECTS.md).

## Five everyday goals

| Goal | Start here |
|---|---|
| Ask what the team knows | [Ask Team Engram](docs/ASKING-TEAM-ENGRAM.md) |
| Add or improve reusable knowledge | [Add or update Knowledge](docs/ADDING-OR-UPDATING-KNOWLEDGE.md) |
| Preserve and analyze a source | [Ingest a source](docs/INGESTING-A-SOURCE.md) |
| Check structure, links, and consistency | [Audit Team Engram](docs/AUDITING-TEAM-ENGRAM.md) |
| Create or improve shared agent behavior | [Create or update a shared skill](docs/CREATING-OR-UPDATING-A-SHARED-SKILL.md) |

Describe the goal in plain English. You do not need to memorize skill names or Git commands.

## How collaboration works

1. Cursor checks your local copy and creates one focused branch.
2. Cursor prepares the change and validates it locally.
3. Cursor shows the changed files, a semantic summary, validation results, and unresolved concerns.
4. Only after you explicitly say **`Publish this change`** may Cursor commit, push, and create or update a GitLab Merge Request.
5. Any repository user may review and self-merge the Merge Request. Merge is a separate human-triggered action.
6. Update local `main` after the merge.

Team Engram intentionally has no GitLab CI, pipeline, required status check, mandatory reviewer, or automatic merge. See [Publishing](docs/PUBLISHING-A-CHANGE.md) and [Merging](docs/MERGING-A-CHANGE.md).

## Quick start

Open the repository in Cursor and follow [Quickstart](QUICKSTART.md). The first-use path verifies shared skills, asks one question, prepares one local Knowledge change, and walks through publication and self-merge.

For a stable multi-root setup with attached project repositories, use [Cursor setup](docs/CURSOR-SETUP.md) and the included [`team-engram.code-workspace.example`](team-engram.code-workspace.example).

## Repository layout

```text
Team-Engram/
├── .agents/skills/          shared reusable Cursor skills
├── Engram/
│   ├── Knowledge/           maintained reusable knowledge
│   ├── Decisions/           consequential accepted decisions
│   └── Sources/
│       ├── Raw/             immutable snapshots or locator records
│       └── Records/         editable source analysis
├── Protocols/               authoritative operating rules
├── Templates/               supported page templates
├── Tools/engram.py          local index, status, and lint tooling
└── docs/                    task-oriented guides
```

`CONTEXT-MAP.md` is the short committed router. `Engram/INDEX.md` is generated locally, is ignored by Git, and must not be edited by hand. Team Engram has no operation log; Git commits and GitLab Merge Requests are the shared history.

## Sources and Confluence

Ordinary article-scale text, including complete multi-screen Confluence articles, may be preserved as Markdown snapshots. Ingest them incrementally when useful. Keep PDFs, archives, videos, and other large or binary artifacts outside the repository and store stable locator information instead. Do not begin with a bulk migration, importer, or predefined taxonomy.

## Documentation

- [Quickstart](QUICKSTART.md)
- [User Guide](USER-GUIDE.md)
- [Context Map](CONTEXT-MAP.md)
- [Cursor setup](docs/CURSOR-SETUP.md)
- [Task guide index](docs/README.md)
- [Team Engram Protocol](Protocols/Team-Engram-Protocol.md)
- [Glossary](docs/GLOSSARY.md)
- [Changelog](CHANGELOG.md)

## License

Team Engram retains the public product's [MIT License](LICENSE).

## Acknowledgements

Engram stands on existing ideas we learned from and adapted:

- **[LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)** by [Andrej Karpathy](https://karpathy.bearblog.dev/) — the core architecture of an LLM-maintained Markdown knowledge base with immutable raw sources, a derived wiki, and Ingest/Query/Lint operations. Engram is a direct implementation of this idea.
- **[mattpocock/skills](https://github.com/mattpocock/skills)** by [Matt Pocock](https://github.com/mattpocock) — the dependency-ordered interview pattern inspired the `grilling` skill.
