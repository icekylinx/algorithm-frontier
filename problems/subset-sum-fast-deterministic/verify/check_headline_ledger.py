#!/usr/bin/env python3
"""Bind the current displayed Subset Sum exponent to its exact scalar ledger.

This is a presentation consistency check, not an independent theorem proof.
It reads the top theorem, abstract, problem card and source map. Explicitly
named historical exponents may remain in the manuscript. The explicitly
historical Part I calculation uses a local E, which must equal Theorem 1's
E_0; outside that scope, one symbol must have one exact rational value.
"""
from __future__ import annotations

from fractions import Fraction as F
import html
import importlib.util
import inspect
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
PROBLEM = ROOT / "problems/subset-sum-fast-deterministic"


def require(condition, message):
    if not condition:
        raise ValueError("Subset Sum headline/ledger mismatch: " + message)


def math_text(text):
    text = html.unescape(text)
    text = re.sub(r"</?code(?:\s+[^>]*)?>", "", text)
    text = re.sub(r"\\(?:mathrm|text|mathsf|mathtt)\{([^{}]*)\}", r"\1", text)
    return re.sub(r"\\(?:rm|sf|tt)\b\s*", "", text)


ASSIGNMENT = re.compile(
    r"\bE(?P<suffix>_(?:\{[A-Za-z0-9_\s]+\}|[A-Za-z0-9]+))?\s*=\s*"
    r"(?:\\frac\s*\{\s*(?P<n>\d+)\s*\}\s*\{\s*(?P<d>\d+)\s*\}"
    r"|(?P<sn>\d+)\s*/\s*(?P<sd>\d+))"
)


def assignments(text):
    result = []
    for match in ASSIGNMENT.finditer(math_text(text)):
        suffix = re.sub(r"[\s_{}]", "", match["suffix"] or "")
        numerator = match["n"] or match["sn"]
        denominator = match["d"] or match["sd"]
        result.append(("E" + suffix, F(int(numerator), int(denominator))))
    return result


def section(text, heading):
    start = text.find(heading)
    require(start >= 0, "missing section " + heading)
    start += len(heading)
    finish = text.find("\n## ", start)
    return text[start:finish if finish >= 0 else len(text)]


def check_documents(documents, exponent, base_exponent):
    proof, card, sources = (documents[key] for key in ("proof", "card", "sources"))
    theorem = re.search(r"^\*\*Theorem F(?P<level>\d*)\b", proof, re.M)
    require(theorem is not None, "missing current Theorem F/F3 heading")
    symbol = "E" + theorem["level"]
    start = theorem.start()
    following = re.search(r"^\*\*Theorem\b|^## ", proof[theorem.end():], re.M)
    finish = theorem.end() + following.start() if following else len(proof)
    current_theorem = proof[start:finish]
    regions = {
        "top theorem": current_theorem,
        "abstract": section(proof, "## Abstract"),
        "source map current theorem": section(sources, "## Current theorem"),
    }
    for name, text in regions.items():
        values = [value for assigned, value in assignments(text) if assigned == symbol]
        require(values and all(value == exponent for value in values),
                name + " must declare " + symbol + "=" + str(exponent))

    require("**Time**" in card and "**Space**" in card, "card time and space fields")
    time_field = card.split("**Time**", 1)[1].split("**Space**", 1)[0]
    exact_card = [value for assigned, value in assignments(time_field) if assigned == symbol]
    require(all(value == exponent for value in exact_card), "card exact rational exponent")
    rounded = re.search(r"2\s*\^\s*\{\s*(0?\.\d+)\s*n\s*\}", math_text(time_field))
    require(rounded is not None, "card must display its rounded exponential time")
    literal = rounded.group(1)
    denominator = 10 ** len(literal.split(".")[1])
    expected_rounded = F(-((-exponent.numerator * denominator) // exponent.denominator),
                         denominator)
    require(F(literal) == expected_rounded,
            "card rounded exponent is stale or is not the upward rounding at its displayed precision")

    # Part I is the historical Theorem 1 derivation. Its local E is not the
    # current headline E: bind it to the explicitly named E_0 instead of
    # silently ignoring it or rejecting the documented historical scope.
    part_i = proof.find("# Part I.")
    part_ii = proof.find("# Part II.")
    require(0 <= part_i < part_ii, "historical Part I and current Part II scopes")
    historical_values = [value for assigned, value in assignments(proof[:part_i])
                         if assigned == "E0"]
    require(historical_values and len(set(historical_values)) == 1,
            "Theorem 1 must name one exact historical E_0")
    historical_exponent = historical_values[0]
    local_values = [value for assigned, value in assignments(proof[part_i:part_ii])
                    if assigned == "E"]
    require(local_values and all(value == historical_exponent for value in local_values),
            "historical Part I local E must equal the declared E_0")
    global_documents = dict(documents)
    global_documents["proof"] = proof[:part_i] + proof[part_ii:]
    declared = {}
    for name, text in global_documents.items():
        for assigned, value in assignments(text):
            declared.setdefault(assigned, set()).add(value)
    # Only the explicitly checked local bare E receives a historical scope.
    # Named exponents inside Part I still participate in global consistency.
    for assigned, value in assignments(proof[part_i:part_ii]):
        if assigned != "E":
            declared.setdefault(assigned, set()).add(value)
    require(all(len(values) == 1 for values in declared.values()),
            "one exponent symbol has conflicting exact values")
    require(declared.get(symbol) == {exponent}, "current exponent symbol across documents")
    if theorem["level"] and int(theorem["level"]) >= 3:
        require("Enew" not in declared,
                "historical Part II exponent must be named E_2, not the ambiguous E_new")
        if "E2" in declared:
            require(declared["E2"] == {base_exponent}, "historical E_2 ledger")
    return dict(current_symbol=symbol, exact_exponent=str(exponent),
                historical_part_i_local_exponent=str(historical_exponent),
                card_rounded_exponent=str(F(literal)), card_exact_declarations=len(exact_card),
                named_exponents={key:str(next(iter(values)))
                                 for key,values in sorted(declared.items())})


def regression_checks(documents, exponent, base_exponent):
    """Reproduce the actual stale-headline risk without changing any file."""
    rejected = 0
    denominator = str(exponent.denominator)
    for field in ("proof", "sources"):
        changed = dict(documents)
        changed[field] = changed[field].replace(denominator, str(exponent.denominator - 2), 1)
        try:
            check_documents(changed, exponent, base_exponent)
        except ValueError:
            rejected += 1
        else:
            raise AssertionError("a stale rational headline was accepted")
    changed = dict(documents)
    time_field = changed["card"].split("**Time**", 1)[1].split("**Space**", 1)[0]
    literal = re.search(r"2\s*\^\s*\{\s*(0?\.\d+)\s*n\s*\}", math_text(time_field)).group(1)
    digits = len(literal.split(".")[1])
    stale = F(literal) + F(1, 10 ** digits)
    stale_literal = f"{stale.numerator * 10**digits // stale.denominator:0{digits+1}d}"
    stale_literal = stale_literal[:-digits] + "." + stale_literal[-digits:]
    changed["card"] = changed["card"].replace(literal, stale_literal, 1)
    try:
        check_documents(changed, exponent, base_exponent)
    except ValueError:
        rejected += 1
    else:
        raise AssertionError("a stale but still larger rounded exponent was accepted")
    changed = dict(documents)
    changed["proof"] = changed["proof"].replace(
        "# Part I.", "E_0=1/2\n\n# Part I.", 1)
    try:
        check_documents(changed, exponent, base_exponent)
    except ValueError:
        rejected += 1
    else:
        raise AssertionError("a conflicting named historical exponent was accepted")
    return rejected


def main():
    if not __debug__:
        raise SystemExit("Run mathematical verification without python -O.")
    path = ROOT / "tools/verify_subset_sum_scalars.py"
    spec = importlib.util.spec_from_file_location("subset_sum_headline_scalars", path)
    scalar = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(scalar)
    exponent = F(scalar.ledger()["exponent"])
    parameters = inspect.signature(scalar.ledger).parameters
    base_exponent = (F(scalar.ledger(include_third=False)["exponent"])
                     if "include_third" in parameters else exponent)
    documents = {key:(PROBLEM / filename).read_text()
                 for key,filename in (("proof","proof.md"),("card","README.md"),("sources","sources.md"))}
    result = check_documents(documents, exponent, base_exponent)
    result.update(status="PASS", rejected_stale_displays=regression_checks(documents, exponent, base_exponent),
                  scope="Displayed current and named historical exponents agree with the exact scalar ledger; this is not an independent theorem verification.")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
