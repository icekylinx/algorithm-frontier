#!/usr/bin/env python3
"""Build the compact homepage and complete canonical manuscript index.

catalogue.json owns concise summaries; problem manuscripts own mathematics.
--check verifies exact coverage and current generated indexes, not proofs.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import sys
from normalize_math import normalize_markdown
from math_presentation import present_markdown

ROOT = Path(__file__).resolve().parents[1]


def title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            # Manuscript titles may retain plain formulas, but the generated
            # public index presents these labels as literal copyable data.
            parts = re.split(r"(`[^`]+`|\$[^$]+\$|<code\b[^>]*>.*?</code>)", line[2:].strip())
            for index in range(0, len(parts), 2):
                parts[index] = parts[index].replace("fixed-k", "fixed-`k`")
                parts[index] = re.sub(r"\bO\([^()]+\)|\b\d+/\d+\b",
                                      lambda match: "`" + match.group() + "`", parts[index])
            return "".join(parts)
    return path.stem.replace("-", " ")


def anchor(text: str) -> str:
    return re.sub(r"[^a-z0-9 -]", "", text.lower()).replace(" ", "-")


def read_catalogue() -> dict:
    data = json.loads((ROOT / "catalogue.json").read_text(encoding="utf-8"))
    if data.get("schema_version") != 3:
        raise ValueError("unsupported catalogue schema")
    groups = data["groups"]
    ids = [r["id"] for g in groups for r in g["records"]]
    if len(ids) != len(set(ids)):
        raise ValueError("a problem appears more than once")
    actual = {p.parent.name for p in (ROOT / "problems").glob("*/README.md")}
    if set(ids) != actual:
        raise ValueError(f"omitted={sorted(actual-set(ids))}; missing={sorted(set(ids)-actual)}")
    featured = data.get("featured", [])
    if len(featured) > 4 or len(featured) != len(set(featured)):
        raise ValueError("feature at most four distinct result families")
    if set(featured) - set(ids):
        raise ValueError("featured result missing from the problem catalogue")
    for g in groups:
        for r in g["records"]:
            if set(r) != {"id", "title", "result", "quantity", "scope", "randomness", "quantity_purposes"}:
                raise ValueError(f"invalid record fields: {r['id']}")
            validate_quantity_purposes(r)
            if not r["randomness"].strip():
                raise ValueError(f"missing randomness contract: {r['id']}")
            for field, text in r.items():
                if field == "quantity_purposes":
                    continue
                if any(ord(c) < 32 for c in text):
                    raise ValueError(f"control byte in {r['id']}.{field}")
                if "|" in text:
                    raise ValueError(f"ambiguous vertical bar in {r['id']}.{field}; use TeX delimiters")
    supporting = data.get("supporting_results", [])
    supporting_ids = [r["id"] for r in supporting]
    if len(supporting_ids) != len(set(supporting_ids)):
        raise ValueError("a supporting result appears more than once")
    for record in supporting:
        if set(record) != {"id", "path", "title", "result", "quantity", "scope", "randomness", "quantity_purposes"}:
            raise ValueError(f"invalid supporting fields: {record['id']}")
        validate_quantity_purposes(record)
        if not (ROOT / record["path"]).is_file():
            raise ValueError(f"missing supporting manuscript: {record['path']}")
        if not record["randomness"].strip():
            raise ValueError(f"missing randomness contract: {record['id']}")
        for field, text in record.items():
            if field == "quantity_purposes":
                continue
            if any(ord(c) < 32 for c in text) or "|" in text:
                raise ValueError(f"invalid summary text in {record['id']}.{field}")
    return data


def validate_quantity_purposes(record: dict) -> None:
    purposes = record["quantity_purposes"]
    formulas = re.findall(r"\$([^$]+)\$", record["quantity"])
    if (not isinstance(purposes, list) or len(purposes) != len(formulas)
            or any(not isinstance(purpose, str) or purpose not in {"showcase", "literal"}
                   for purpose in purposes)):
        raise ValueError(f"invalid quantity purposes: {record['id']}")


def quantity_paragraphs(text: str, purposes: list[str]) -> list[str]:
    """Present each formula according to its explicitly reviewed purpose.

    Catalogue values stay renderer-independent Markdown. Semicolons outside
    mathematics separate incomparable bounds. A showcased result becomes an
    SVG even when short; a parameter or machine-readable expression stays
    literal even when long. Delimiter placement and length do not choose roles.
    """
    validate_quantity_purposes({"id": "quantity", "quantity": text,
                                "quantity_purposes": purposes})
    roles = iter(purposes)
    clauses: list[str] = []
    start = 0
    in_math = False
    for index, char in enumerate(text):
        if char == "$" and (index == 0 or text[index - 1] != "\\"):
            in_math = not in_math
        elif char == ";" and not in_math:
            clauses.append(text[start:index].strip())
            start = index + 1
    clauses.append(text[start:].strip())
    out: list[str] = []

    def sentence(fragment: str) -> str:
        fragment = fragment.strip().lstrip(", ")
        if fragment and fragment[0].islower() and not fragment.startswith("coNP"):
            fragment = fragment[0].upper() + fragment[1:]
        return fragment.rstrip(".") + "."

    for clause in clauses:
        cursor = 0
        pending = ""
        for match in re.finditer(r"\$([^$]+)\$", clause):
            pending += clause[cursor:match.start()]
            formula = match[1]
            if next(roles) == "showcase":
                lead = pending.strip().rstrip(",:")
                if lead:
                    # Literal parameters can belong to the caption of a
                    # showcased conclusion. Keep their qualification with
                    # that conclusion instead of making a broken sentence.
                    out += [sentence(lead).rstrip(".") + ":", ""]
                out += ["$$", formula, "$$", ""]
                pending = ""
            else:
                pending += match[0]
            cursor = match.end()
        pending += clause[cursor:]
        if pending.strip().strip(","):
            out += [sentence(pending), ""]
    return out


def render_record(record: dict, path: str, *, level: int = 4) -> list[str]:
    return [
        f"{'#' * level} [{record['title']}]({path})", "",
        record["result"].rstrip(".") + ".", "",
        "**Randomness.** " + record["randomness"], "",
        "**Quantitative result.**", "",
        *quantity_paragraphs(record["quantity"], record["quantity_purposes"]),
        "**Model and scope.** " + record["scope"].rstrip(".") + ".", "",
    ]


def render_readme(data: dict) -> str:
    groups = data["groups"]
    supporting = data.get("supporting_results", [])
    count = sum(len(g["records"]) for g in groups)
    out = [
        "# Algorithm Frontier", "",
        "Algorithms and proofs in combinatorial optimization, number theory, algebraic complexity, "
        "dynamic graphs, and sparsification. Each problem page gives the theorem, complexity, "
        "randomness, dependencies, and verification evidence.", "",
        "[![Repository checks](https://github.com/icekylinx/algorithm-frontier/actions/workflows/curation.yml/badge.svg)]"
        "(https://github.com/icekylinx/algorithm-frontier/actions/workflows/curation.yml) "
        "[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)", "",
        f"**{count} problem families · {len(supporting)} supporting results** · [Proof index](CONTENTS.md) · "
        "[Review and verification](reviews/README.md) · "
        "[Citation](CITATION.cff)", "",
        "## Selected results", "",
        "Selected deterministic algorithmic results, with conditional premises stated explicitly. The linked "
        "problem pages give "
        "the full statements, proof dependencies, executable coverage and review status.", "",
    ]
    by_id = {r["id"]: r for g in groups for r in g["records"]}
    for problem_id in data.get("featured", []):
        record = by_id[problem_id]
        out += [f"### [{record['title']}](problems/{problem_id}/)", "",
                record['result'].rstrip('.') + '.', "",
                *quantity_paragraphs(record['quantity'], record['quantity_purposes']),
                record['scope'].rstrip('.') + '.', ""]
    out += [
        "## Results", "",
        "Categories follow the selected-result topics, then related methods and applications. Selected families lead each category; other titles are alphabetized. Each link opens its statement, proof and dependencies. "
        "[Computational models](docs/COMPLEXITY.md) and "
        "[randomness contracts](docs/RANDOMNESS.md) explain how to compare bounds.", "",
    ]
    for g in groups:
        out += [f"### {g['title']}", ""]
        for r in g["records"]:
            out.append(f"- [{r['title']}](problems/{r['id']}/)")
        out.append("")
    if supporting:
        out += ["### Supporting results", "",
                f"The [complete index](CONTENTS.md#supporting-results) also lists {len(supporting)} "
                "supporting algorithms, structural theorems, and scoped lower bounds. "
                "[Shared manuscripts](CONTENTS.md#shared-manuscripts) collect reusable proofs "
                "and backend interfaces.", ""]
    out += [
        "## Reading and verification", "",
        "Within each problem: `README.md` → `proof.md` → `sources.md` → "
        "`verify/README.md`. The [review registry](reviews/README.md) distinguishes "
        "manuscript review from executable checks and identifies their exact scope.", "",
        "```sh", "python3 tools/check_repository.py", "```", "",
        "See [Contributing](CONTRIBUTING.md) for the full verification mode and "
        "maintenance conventions. No external peer review or proof-assistant "
        "verification is claimed.", "",
        "icekylinx and GPT-6 Astra Pro. *Algorithm Frontier* (2026). "
        "Cite the relevant problem path and commit; the [citation protocol](PROTOCOL.md) "
        "and [import provenance](provenance/README.md) retain the applicable "
        "licenses and notices.", "",
    ]
    return normalize_markdown("\n".join(out))


def render_contents(data: dict) -> str:
    groups = data["groups"]
    out = ["# Complete proof index", "",
           "Every current problem manuscript and shared dependency is listed below. "
           "The [README](README.md) gives selected results and a compact problem index; this page provides the "
           "complete reading path without duplicate checkpoint copies.", ""]
    for group in groups:
        out += [f"## {group['title']}", ""]
        for record in group["records"]:
            directory = ROOT / "problems" / record["id"]
            prefix = directory.relative_to(ROOT).as_posix()
            out += [
                f"### [{record['title']}]({prefix}/)", "",
                f"[Statement]({prefix}/README.md) · [Main proof]({prefix}/proof.md) · "
                f"[Sources]({prefix}/sources.md) · [Verification]({prefix}/verify/README.md)", "",
            ]
            companions = sorted(p for p in directory.rglob("*.md")
                if p.name not in {"README.md", "proof.md", "sources.md", "NOTICE.md"}
                and "verify" not in p.relative_to(directory).parts)
            for path in companions:
                out.append(f"- [{title(path)}]({path.relative_to(ROOT).as_posix()})")
            if companions:
                out.append("")
    out += ["## Supporting results", "",
            "These entries extend the problem families with additional algorithms, "
            "structural results, and scoped boundaries. Their linked manuscripts "
            "state the full models and assumptions.", ""]
    for record in data.get("supporting_results", []):
        out += render_record(record, record["path"], level=3)
    out += ["## Shared manuscripts", "",
            "These proofs and scoped interface analyses are used across problem records. "
            "An obstruction concerns the precise mechanism stated in its manuscript, "
            "rather than an unrestricted algorithmic lower bound.", ""]
    shared = ROOT / "manuscripts"
    if shared.is_dir():
        for directory in sorted(p for p in shared.iterdir() if p.is_dir()):
            out += [f"### {directory.name.replace('-', ' ').capitalize()}", ""]
            for path in sorted(directory.rglob("*.md")):
                if path.name != "README.md":
                    out.append(f"- [{title(path)}]({path.relative_to(ROOT).as_posix()})")
            out.append("")
    out += ["## Evidence and provenance", "",
            "- [Verification registry](reviews/README.md)",
            "- [Import provenance and canonical paths](provenance/README.md)",
            "- [Complexity and computational models](docs/COMPLEXITY.md)",
            "- [Randomness contracts](docs/RANDOMNESS.md)",
            "- [Maintenance and validation](CONTRIBUTING.md)",
            "- [Change history](HISTORY.md)", ""]
    return normalize_markdown("\n".join(out))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        data = read_catalogue()
    except (ValueError, KeyError) as exc:
        print(f"catalogue check failed: {exc}", file=sys.stderr)
        return 1
    stale = []
    groups = data["groups"]
    for name, content in {"README.md": render_readme(data), "CONTENTS.md": render_contents(data)}.items():
        path = ROOT / name
        content = present_markdown(content, path)
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                stale.append(name)
        else:
            path.write_text(content, encoding="utf-8")
    # The catalogue owns the concise randomness contract on both reading
    # surfaces. Editing it once must update the homepage and the result card.
    for group in groups:
        for record in group["records"]:
            path = ROOT / "problems" / record["id"] / "README.md"
            before = path.read_text(encoding="utf-8")
            block = normalize_markdown("**Randomness**\n\n" + record["randomness"] + "\n\n")
            block = present_markdown(block, path)
            if re.search(r"(?m)^\*\*Randomness\*\*$", before):
                after = re.sub(r"(?ms)^\*\*Randomness\*\*\n\n.*?(?=^\*\*Time\*\*$)",
                               lambda _: block, before, count=1)
            else:
                after = before.replace("**Time**\n", block + "**Time**\n", 1)
            if args.check:
                if after != before:
                    stale.append(path.relative_to(ROOT).as_posix())
            else:
                path.write_text(after, encoding="utf-8")
    if stale:
        print("stale generated indexes: " + ", ".join(stale) +
              "; run python3 tools/build_catalogue.py", file=sys.stderr)
        return 1
    count = sum(len(g["records"]) for g in groups)
    print(f"catalogue {'checked' if args.check else 'built'}: {count} result families; "
          f"{len(data.get('supporting_results', []))} supporting results")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
