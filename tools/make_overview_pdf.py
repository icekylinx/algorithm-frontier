#!/usr/bin/env python3
"""Compile the checked-in LaTeX overview into ``overview.pdf``.

The source is intentionally kept as a normal article (``overview.tex``), so
the catalogue can be read and rebuilt without a Python PDF layout engine.
Build files are written to a temporary directory and are never left in the
repository.
"""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "tools" / "overview.tex"
OUT = ROOT / "overview.pdf"


def find_engine() -> str:
    for candidate in ("pdflatex", "xelatex", "lualatex"):
        path = shutil.which(candidate)
        if path:
            return path
    raise SystemExit("No LaTeX engine found (tried pdflatex, xelatex, lualatex).")


def main() -> None:
    engine = find_engine()
    with tempfile.TemporaryDirectory(prefix="algorithm_frontier_latex_") as build:
        build_dir = Path(build)
        command = [
            engine,
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-file-line-error",
            f"-output-directory={build_dir}",
            str(TEX),
        ]
        # Two passes keep references and the bibliography stable if the
        # article is extended with cross-references in a later revision.
        for _ in range(2):
            subprocess.run(command, cwd=ROOT, check=True)
        built = build_dir / "overview.pdf"
        if not built.is_file():
            raise SystemExit("LaTeX completed without producing overview.pdf")
        shutil.copy2(built, OUT)
    print(f"wrote {OUT} using {Path(engine).name}")


if __name__ == "__main__":
    main()
