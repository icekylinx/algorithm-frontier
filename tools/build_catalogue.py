#!/usr/bin/env python3
"""Build the complete results catalogue and canonical manuscript index.

catalogue.json owns concise summaries; problem manuscripts own mathematics.
--check verifies exact coverage and current generated indexes, not proofs.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip().replace("|", r"\|")
    return path.stem.replace("-", " ")


def anchor(text: str) -> str:
    return re.sub(r"[^a-z0-9 -]", "", text.lower()).replace(" ", "-")


def read_catalogue() -> dict:
    data = json.loads((ROOT / "catalogue.json").read_text(encoding="utf-8"))
    if data.get("schema_version") != 2:
        raise ValueError("unsupported catalogue schema")
    groups = data["groups"]
    ids = [r["id"] for g in groups for r in g["records"]]
    if len(ids) != len(set(ids)):
        raise ValueError("a problem appears more than once")
    actual = {p.parent.name for p in (ROOT / "problems").glob("*/README.md")}
    if set(ids) != actual:
        raise ValueError(f"omitted={sorted(actual-set(ids))}; missing={sorted(set(ids)-actual)}")
    for g in groups:
        for r in g["records"]:
            if set(r) != {"id", "title", "result", "quantity", "scope", "randomness"}:
                raise ValueError(f"invalid record fields: {r['id']}")
            if not r["randomness"].strip():
                raise ValueError(f"missing randomness contract: {r['id']}")
            for field, text in r.items():
                if any(ord(c) < 32 for c in text):
                    raise ValueError(f"control byte in {r['id']}.{field}")
                if "|" in text:
                    raise ValueError(f"ambiguous vertical bar in {r['id']}.{field}; use TeX delimiters")
    supporting = data.get("supporting_results", [])
    supporting_ids = [r["id"] for r in supporting]
    if len(supporting_ids) != len(set(supporting_ids)):
        raise ValueError("a supporting result appears more than once")
    for record in supporting:
        if set(record) != {"id", "path", "title", "result", "quantity", "scope", "randomness"}:
            raise ValueError(f"invalid supporting fields: {record['id']}")
        if not (ROOT / record["path"]).is_file():
            raise ValueError(f"missing supporting manuscript: {record['path']}")
        if not record["randomness"].strip():
            raise ValueError(f"missing randomness contract: {record['id']}")
        for field, text in record.items():
            if any(ord(c) < 32 for c in text) or "|" in text:
                raise ValueError(f"invalid summary text in {record['id']}.{field}")
    return data


def quantity_paragraphs(text: str) -> list[str]:
    """Give long bounds their own line without splitting a TeX expression.

    Catalogue values stay renderer-independent Markdown. Semicolons outside
    mathematics separate incomparable bounds; short formula fragments remain
    inline, while substantial expressions get the full page width.
    """
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
        # Do not promote identifiers or tiny arithmetic expressions. Isolating
        # only the long expressions also prevents Markdown emphasis from
        # interfering with subscripts, stars and products in headline bounds.
        cursor = 0
        pending = ""
        for match in re.finditer(r"\$([^$]+)\$", clause):
            pending += clause[cursor:match.start()]
            formula = match[1]
            if len(formula) >= 36 or clause == match[0]:
                lead = pending.strip().rstrip(",:")
                if lead:
                    # A preceding complete formula is a separate definition,
                    # rather than the label of the following display.
                    if "$" in lead:
                        out += [sentence(lead), ""]
                    else:
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
        *quantity_paragraphs(record["quantity"]),
        "**Model and scope.** " + record["scope"].rstrip(".") + ".", "",
    ]


def render_readme(data: dict) -> str:
    groups = data["groups"]
    supporting = data.get("supporting_results", [])
    count = sum(len(g["records"]) for g in groups)
    out = [
        "# Algorithm Frontier", "",
        "Research manuscripts on deterministic algorithms, combinatorial optimization, "
        "dynamic graphs, and sparsification. The catalogue below lists every result "
        "family; each entry opens a precise statement, complete proofs, and its "
        "computational assumptions.", "",
        "[![Repository checks](https://github.com/icekylinx/algorithm-frontier/actions/workflows/curation.yml/badge.svg)]"
        "(https://github.com/icekylinx/algorithm-frontier/actions/workflows/curation.yml) "
        "[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)", "",
        f"**{count} result families · {len(supporting)} supporting results** · [Complete proof index](CONTENTS.md) · "
        "[Complexity conventions](docs/COMPLEXITY.md) · [Verification evidence](reviews/README.md) · "
        "[Citation](CITATION.cff)", "",
        "## Results", "",
        *[f"- [{g['title']}](#{anchor(g['title'])})" for g in groups],
        "- [Supporting results](#supporting-results)", "",
        "A displayed conditional composition includes its named backend hypotheses. "
        "Oracle bounds, explicit-input algorithms, support sizes, query costs, and "
        "existence theorems keep their distinct meanings. Exact rational constants "
        "and complete parameter ranges are stated on the linked cards.", "",
        "Every entry states its [randomness contract](docs/RANDOMNESS.md): "
        "deterministic, Monte Carlo, Las Vegas, or a separately identified "
        "existence theorem, structural result or lower bound. A supplied "
        "randomized backend must retain its own confidence and adversary assumptions.", "",
    ]
    for g in groups:
        out += [f"### {g['title']}", "", g["note"], ""]
        for r in g["records"]:
            out += render_record(r, f"problems/{r['id']}/")
    if supporting:
        out += ["## Supporting results", "",
                "These additional algorithms, structural lemmas and scoped boundaries "
                "have their own complete manuscripts. Further refinements are listed "
                "with their parent result in the [proof index](CONTENTS.md).", ""]
        for record in supporting:
            out += render_record(record, record["path"], level=3)
    out += [
        "## Reading and verification", "",
        "Start with a result card, then read its `proof.md`. Longer derivations are "
        "linked as companion manuscripts. Shared graph interfaces, allocation "
        "lemmas, and explicit obstruction constructions are indexed in "
        "[Contents](CONTENTS.md#shared-manuscripts). The source map names the "
        "dependencies used by that result.", "",
        "Each `verify/README.md` explains the available evidence and its limits. "
        "Exact finite certificates check specified identities, finite examples, "
        "or certified domains; they do not by themselves establish every "
        "asymptotic theorem. The repository does not claim proof-assistant "
        "verification or external peer review.", "",
        "The [maintenance guide](CONTRIBUTING.md) gives the single local check "
        "command and the rules for updating statements, proof dependencies, "
        "and this generated catalogue.", "",
        "## Citation and attribution", "",
        "Yilin Liu and GPT-6 Astra Pro. *Algorithm Frontier* (2026). "
        "Cite the relevant problem path and commit; the [citation protocol](PROTOCOL.md) "
        "and [import provenance](provenance/README.md) retain the applicable "
        "licenses and notices.", "",
    ]
    return "\n".join(out)


def render_contents(groups: list[dict]) -> str:
    out = ["# Complete proof index", "",
           "Every current problem manuscript and shared dependency is listed below. "
           "The [README](README.md) compares the results; this index provides the "
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
    return "\n".join(out)


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
    for name, content in {"README.md": render_readme(data), "CONTENTS.md": render_contents(groups)}.items():
        path = ROOT / name
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
            block = "**Randomness**\n\n" + record["randomness"] + "\n\n"
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
