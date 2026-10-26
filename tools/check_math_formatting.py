#!/usr/bin/env python3
"""Regression checks for TeX-preserving GitHub Markdown normalization.

These examples exercise the exact punctuation that GitHub's Markdown parser
can consume before MathJax: escaped braces, negative spacing, row separators,
and underscore/star pairs. This checks source preservation and lint behavior,
not arbitrary TeX semantics or mathematical correctness.
"""
from __future__ import annotations

import json
import unittest

from check_latex_delimiters import check_text
from normalize_math import normalize_catalogue, normalize_markdown


class GitHubMathFormatting(unittest.TestCase):
    def test_inline_backslashes_and_emphasis_are_preserved(self):
        body = r"\left\{x_i,y_j\right\}\quad f^*_i\ne g^*_j\;\exp\!(-x)"
        self.assertEqual(normalize_markdown("Before $" + body + "$ after."),
                         "Before $`" + body + "`$ after.")

    def test_adjacent_inline_math(self):
        self.assertEqual(normalize_markdown("$C$-$C$ edges and $a$/$b$."),
                         "$`C`$-$`C`$ edges and $`a`$/$`b`$.")

    def test_display_alignment_bytes_are_preserved(self):
        body = "\\begin{aligned}\na_1&=b_1\\\\\na_2&=\\left\\{0,1\\right\\}\n\\end{aligned}\n\\tag{A1}"
        expected = "```math\n" + body + "\n```\n"
        self.assertEqual(normalize_markdown("$$\n" + body + "\n$$\n"), expected)
        self.assertEqual(check_text(expected), [])

    def test_list_display_indentation(self):
        before = "1. A claim.\n\n   $$\n   a=b\n   $$\n"
        after = "1. A claim.\n\n   ```math\n   a=b\n   ```\n"
        self.assertEqual(normalize_markdown(before), after)
        self.assertEqual(check_text(after), [])

    def test_code_and_comments_are_unchanged(self):
        before = "A `$x$` example.\n\n```python\nprint('$x$')\n```\n<!-- $x$ -->\n"
        self.assertEqual(normalize_markdown(before), before)

    def test_four_backtick_documentation_fence(self):
        before = "````markdown\n```math\n\\left\\{x\\right\\}\n```\n````\n"
        self.assertEqual(normalize_markdown(before), before)
        self.assertEqual(check_text(before), [])

    def test_math_fence_and_inline_are_idempotent(self):
        text = "A $`x_i+y_j`$ value.\n\n```math\n\\left\\{0,1\\right\\}\n```\n"
        self.assertEqual(normalize_markdown(text), text)
        self.assertEqual(check_text(text), [])

    def test_table_pipes_require_named_tex_delimiters(self):
        self.assertTrue(check_text("| quantity | $`|S|`$ |\n"))
        self.assertFalse(check_text(r"| quantity | $`\lvert S\rvert`$ |" + "\n"))

    def test_inline_newline_is_joined(self):
        self.assertEqual(normalize_markdown("$a+\n b$"), "$`a+ b`$")

    def test_catalogue_remains_a_single_line_input(self):
        data = {"quantity": r"$\min\{x,y\}$; $O(n)$"}
        self.assertEqual(json.loads(normalize_catalogue(json.dumps(data))), data)

    def test_plain_dollars_are_reported(self):
        self.assertTrue(check_text("$x$"))
        self.assertTrue(check_text("$$\nx\n$$\n"))

    def test_protected_body_is_still_checked(self):
        self.assertTrue(check_text(r"$`\frac{x}{y`$"))
        self.assertTrue(check_text("```math\n\\frac{x}{y\n```\n"))
        self.assertTrue(check_text("$`a+\nb`$"))

    def test_escaped_dollar_stays_in_formula(self):
        self.assertEqual(normalize_markdown(r"$\text{cost }\$4$"),
                         r"$`\text{cost }\$4`$")


if __name__ == "__main__":
    unittest.main()
