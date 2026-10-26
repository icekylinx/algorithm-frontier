#!/usr/bin/env python3
"""Regression tests for source-preserving static mathematical presentation."""
from __future__ import annotations

import unittest
from pathlib import Path

from math_presentation import present_markdown, restore_markdown, transform

ROOT = Path('/example')
PAGE = ROOT / 'problems' / 'example' / 'proof.md'


class StaticMathematics(unittest.TestCase):
    def present(self, text):
        return present_markdown(text, PAGE, root=ROOT)

    def source(self, text):
        return restore_markdown(text, PAGE, root=ROOT)

    def test_inline_is_literal_code_with_escaped_markup(self):
        result = self.present(r'$x_i<y_j\quad a&b\quad |S|$')
        self.assertEqual(result, '<code class="math">x_i&lt;y_j\\quad a&amp;b\\quad &#124;S&#124;</code>')
        self.assertEqual(self.source(result), r'$x_i<y_j\quad a&b\quad |S|$')

    def test_protected_input_has_no_live_math(self):
        result = self.present('$`C`$-$`C`$ and $`\\left\\{x\\right\\}`$.')
        self.assertNotIn('$', result)
        self.assertNotIn('```math', result)
        self.assertEqual(self.source(result), '$C$-$C$ and $\\left\\{x\\right\\}$.')

    def test_display_source_and_relative_image(self):
        tex = '\\begin{aligned}\nx&=y\\\\\na&=b\n\\end{aligned}\n\\tag{1}'
        before = '```math\n' + tex + '\n```\n'
        result = self.present(before)
        self.assertIn('](../../assets/math/', result)
        self.assertIn(tex, result)
        self.assertEqual(self.source(result), '$$\n' + tex + '\n$$\n')
        self.assertEqual(self.present(result), result)

    def test_indented_display_round_trips(self):
        before = '1. Claim\n\n   $$\n   x=y\n   $$\n\nNext.\n'
        result = self.present(before)
        self.assertIn('\n   ![Formula]', result)
        self.assertEqual(self.present(result), result)
        self.assertEqual(self.source(result), before)

    def test_ordinary_code_and_comments_stay_unchanged(self):
        text = 'Use `$x$`.\n\n````md\n```math\nx=y\n```\n````\n<!-- $q$ -->\n'
        self.assertEqual(self.present(text), text)
        self.assertEqual(self.source(text), text)

    def test_source_change_rebinds_image(self):
        first = self.present('$$\nx=y\n$$\n')
        second = self.present(first.replace('\nx=y\n', '\nx=z\n'))
        self.assertNotEqual(first.split('![Formula]')[1], second.split('![Formula]')[1])
        self.assertEqual(self.source(second), '$$\nx=z\n$$\n')

    def test_all_formula_records_keep_exact_values(self):
        records = []
        transform('$n$ and\n\n$$\n\\frac{1}{2}\n$$\n', PAGE, records=records, root=ROOT)
        self.assertEqual([item['tex'] for item in records], ['n', r'\frac{1}{2}'])
        self.assertEqual([item['display'] for item in records], [False, True])

    def test_missing_image_is_rejected(self):
        with self.assertRaises(ValueError):
            self.present('<!-- math-display: missing\nx=y\n-->\n')


if __name__ == '__main__':
    unittest.main()
