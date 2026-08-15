from __future__ import annotations

import io
import json
import re
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from urllib.parse import unquote

import engram  # pyright: ignore[reportImplicitRelativeImport]


VALID_DOCUMENTS = {
    "Knowledge/note.md": """---
type: knowledge
status: active
topics: [operations]
---

# Maintained Practice

A reusable organizational practice.
""",
    "Decisions/decision.md": """---
type: decision
id: ORG-DEC-001
date: 2026-08-15
status: accepted
topics: [operations]
---

# Adopt the Practice
""",
    "Sources/Raw/article.md": """---
type: source-raw
status: immutable
source_type: article
retrieved: 2026-08-15
url_or_path: https://example.com/article
topics: [operations]
---

# Raw Article

Original article text.
""",
    "Sources/Records/article-record.md": """---
type: source-record
status: ingested
source_type: article
retrieved: 2026-08-15
raw_materials: ['[Raw article](../Raw/article.md)']
topics: [operations]
---

# Article Record
""",
}


def make_workspace(root: Path, documents: dict[str, str] | None = None) -> None:
    schema_source = Path(__file__).parents[1] / "Schemas" / "team-engram.schema.json"
    schema_target = root / "Schemas" / "team-engram.schema.json"
    schema_target.parent.mkdir(parents=True, exist_ok=True)
    schema_target.write_text(schema_source.read_text(encoding="utf-8"), encoding="utf-8")
    for directory in ("Knowledge", "Decisions", "Sources/Raw", "Sources/Records"):
        (root / "Engram" / directory).mkdir(parents=True, exist_ok=True)
    for relative, content in (documents or {}).items():
        path = root / "Engram" / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


class SchemaTests(unittest.TestCase):
    def test_schema_is_json_and_describes_all_supported_types(self) -> None:
        schema_path = Path(__file__).parents[1] / "Schemas" / "team-engram.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))

        self.assertEqual(schema["schema_version"], 1)
        self.assertEqual(schema["common_required"], ["type", "status", "topics"])
        self.assertEqual(
            set(schema["types"]),
            {"knowledge", "decision", "source-raw", "source-record"},
        )
        self.assertEqual(schema["types"]["knowledge"]["statuses"], ["active", "disputed", "superseded", "archived"])
        self.assertEqual(schema["types"]["decision"]["statuses"], ["accepted", "rejected", "superseded"])

    def test_templates_use_supported_type_status_and_required_fields(self) -> None:
        root = Path(__file__).parents[1]
        templates = {
            "Knowledge.md": "knowledge",
            "Decision.md": "decision",
            "Source-Raw.md": "source-raw",
            "Source.md": "source-record",
        }
        schema = engram.load_schema(root)

        for filename, expected_type in templates.items():
            with self.subTest(filename=filename):
                parsed = engram.parse_frontmatter((root / "Templates" / filename).read_text(encoding="utf-8"))
                self.assertIsNone(parsed.error)
                self.assertEqual(parsed.metadata["type"], expected_type)
                required = set(schema["common_required"] + schema["types"][expected_type]["required"])
                self.assertTrue(required.issubset(parsed.metadata))
                self.assertIn(parsed.metadata["status"], schema["types"][expected_type]["statuses"])

    def test_project_map_ticket_template_requires_qualified_id(self) -> None:
        template = (Path(__file__).parents[1] / "Templates" / "Project-Map" / "TICKET.md").read_text(encoding="utf-8")
        self.assertIn("PROJECT-001", template)
        self.assertNotIn("PM-000", template)


class FrontmatterTests(unittest.TestCase):
    def test_parses_dependency_free_yaml_subset(self) -> None:
        parsed = engram.parse_frontmatter("---\ntype: knowledge\ntopics:\n  - alpha\n  - 'two words'\n---\n# Title\n")
        self.assertTrue(parsed.has_frontmatter)
        self.assertIsNone(parsed.error)
        self.assertEqual(parsed.metadata["topics"], ["alpha", "two words"])
        self.assertEqual(parsed.body.strip(), "# Title")

    def test_reports_malformed_frontmatter(self) -> None:
        parsed = engram.parse_frontmatter("---\ntype knowledge\n---\n# Title\n")
        self.assertIn("key: value", parsed.error or "")
        self.assertEqual(parsed.error_line, 2)


class LintTests(unittest.TestCase):
    def test_valid_team_corpus_is_clean(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            make_workspace(root, VALID_DOCUMENTS)
            self.assertEqual(engram.lint_workspace(root), [])

    def test_common_required_fields_and_type_specific_status_are_errors(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            make_workspace(root, {"Knowledge/bad.md": "---\ntype: knowledge\nstatus: draft\n---\n# Bad\n"})
            messages = [issue.message for issue in engram.lint_workspace(root)]
            self.assertTrue(any("missing required field 'topics'" in message for message in messages))
            self.assertTrue(any("invalid status 'draft'" in message for message in messages))

    def test_unknown_type_and_wrong_directory_are_errors(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            make_workspace(root, {"Knowledge/bad.md": "---\ntype: decision\nid: ORG-001\ndate: 2026-08-15\nstatus: accepted\ntopics: [x]\n---\n# Bad\n"})
            issues = engram.lint_workspace(root)
            self.assertTrue(any("does not match directory" in issue.message for issue in issues))

    def test_superseded_page_requires_superseded_by(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            make_workspace(root, {"Knowledge/old.md": "---\ntype: knowledge\nstatus: superseded\ntopics: [x]\n---\n# Old\n"})
            self.assertTrue(any("superseded_by" in issue.message for issue in engram.lint_workspace(root)))

    def test_decision_ids_are_valid_and_unique(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            first = VALID_DOCUMENTS["Decisions/decision.md"]
            make_workspace(root, {"Decisions/one.md": first, "Decisions/two.md": first})
            issues = engram.lint_workspace(root)
            self.assertTrue(any("duplicate decision ID ORG-DEC-001" in issue.message for issue in issues))

            (root / "Engram" / "Decisions" / "two.md").unlink()
            (root / "Engram" / "Decisions" / "one.md").write_text(first.replace("ORG-DEC-001", "DEC"), encoding="utf-8")
            self.assertTrue(any("invalid decision id" in issue.message for issue in engram.lint_workspace(root)))

    def test_raw_artifact_requires_existing_path_and_content_hash(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            raw = VALID_DOCUMENTS["Sources/Raw/article.md"].replace("topics: [operations]", "artifact_path: article.txt\ntopics: [operations]")
            make_workspace(root, {"Sources/Raw/article.md": raw})
            messages = [issue.message for issue in engram.lint_workspace(root)]
            self.assertTrue(any("artifact_path does not exist" in message for message in messages))
            self.assertTrue(any("content_hash" in message for message in messages))

    def test_unreferenced_raw_artifact_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            make_workspace(root)
            artifact = root / "Engram" / "Sources" / "Raw" / "orphan.bin"
            artifact.write_bytes(b"orphan")

            issues = engram.lint_workspace(root)

            self.assertTrue(any(issue.path == artifact and "no source-raw manifest" in issue.message for issue in issues))

    def test_raw_gitkeep_is_not_treated_as_an_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            make_workspace(root)
            (root / "Engram" / "Sources" / "Raw" / ".gitkeep").write_text("", encoding="utf-8")

            self.assertEqual(engram.lint_workspace(root), [])

    def test_article_scale_inline_markdown_snapshot_is_supported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            article = VALID_DOCUMENTS["Sources/Raw/article.md"] + ("Article paragraph.\n\n" * 5000)
            make_workspace(root, {"Sources/Raw/article.md": article})
            self.assertEqual(engram.lint_workspace(root), [])

    def test_source_record_requires_nonempty_raw_link_to_raw_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            bad = VALID_DOCUMENTS["Sources/Records/article-record.md"].replace("['[Raw article](../Raw/article.md)']", "[]")
            make_workspace(root, {"Sources/Records/record.md": bad})
            self.assertTrue(any("raw_materials" in issue.message for issue in engram.lint_workspace(root)))

    def test_broken_markdown_link_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            make_workspace(root)
            readme = root / "README.md"
            readme.write_text("# Readme\n\n[Missing](missing.md)\n", encoding="utf-8")
            issues = engram.lint_workspace(root)
            self.assertTrue(any(issue.path == readme and "broken relative link" in issue.message for issue in issues))

    def test_knowledge_provenance_is_optional(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            make_workspace(root, {"Knowledge/note.md": VALID_DOCUMENTS["Knowledge/note.md"]})
            self.assertFalse(any("provenance" in issue.message for issue in engram.lint_workspace(root)))


class IndexTests(unittest.TestCase):
    def test_index_only_scans_engram_and_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            make_workspace(root, VALID_DOCUMENTS)
            (root / "Projects").mkdir()
            (root / "Projects" / "project.md").write_text("# Must Not Appear\n", encoding="utf-8")

            first = engram.build_index(root)
            second = engram.build_index(root)

            self.assertEqual(first, second)
            self.assertNotIn("Must Not Appear", first)
            self.assertNotIn("Projects/", first)
            self.assertIn("topics: `operations`", first)
            for destination in re.findall(r"\[[^]]+\]\(([^)]+)\)", first):
                self.assertTrue((root / "Engram" / unquote(destination)).exists())

    def test_index_write_and_check_do_not_rewrite_stable_content(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            make_workspace(root, {"Knowledge/note.md": VALID_DOCUMENTS["Knowledge/note.md"]})
            self.assertEqual(engram.update_index(root), 0)
            index_path = root / "Engram" / "INDEX.md"
            before = index_path.read_bytes()
            self.assertEqual(engram.update_index(root, check=True), 0)
            self.assertEqual(index_path.read_bytes(), before)


class StatusAndCliTests(unittest.TestCase):
    def test_status_has_only_team_corpus_counts(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            make_workspace(root, VALID_DOCUMENTS)
            lines = engram.status_lines(root)
            self.assertEqual(lines, ["Knowledge: 1", "Decisions: 1", "Sources: raw=1, records=1"])
            self.assertNotRegex("\n".join(lines), r"Captures|Inbox|Sessions|Health|Projects")

    def test_cli_has_index_lint_status_and_no_log_command(self) -> None:
        parser = engram.build_parser()
        help_text = parser.format_help()
        self.assertIn("index", help_text)
        self.assertIn("lint", help_text)
        self.assertIn("status", help_text)
        self.assertNotIn("log", help_text)

    def test_lint_cli_reports_exact_clean_summary(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            make_workspace(root)
            output = io.StringIO()
            with redirect_stdout(output):
                result = engram.main(["lint"], root=root)
            self.assertEqual(result, 0)
            self.assertEqual(output.getvalue(), "Lint: 0 error(s), 0 warning(s)\n")


if __name__ == "__main__":
    unittest.main()
