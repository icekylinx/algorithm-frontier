#!/usr/bin/env python3
"""Regression tests for source-preserving static mathematical presentation."""
from __future__ import annotations

import unittest
from pathlib import Path
import tempfile

from math_presentation import present_markdown, restore_markdown, transform
from build_math_assets import validate_svg
from build_catalogue import quantity_paragraphs
from check_public_math import BARE_MATH, prose_lines

ROOT = Path('/example')
PAGE = ROOT / 'problems' / 'example' / 'proof.md'


class StaticMathematics(unittest.TestCase):
    def test_public_prose_rejects_unmarked_symbolic_expressions(self):
        for source in ('Work O(n).', 'Assume n>=h+3.', 'Degree w²−1.',
                       'Probability 2/3.', 'The field has size p^n.',
                       'For x<y and y>z.', 'The function K(w).'):
            with self.subTest(source=source):
                self.assertTrue(any(BARE_MATH.search(line) for _, line in prose_lines(source)))

    def test_public_prose_preserves_literal_and_source_containers(self):
        source = '''The parameter `n>=h+3` and <code class="math">O(n)</code>.
<!-- math-display: fixture
O(n^2)
-->
![Formula](assets/math/fixture.svg)
```text
K(w)=2^w
```
[check_values.py](verify/check_values.py) and [Theorems 3.2/3.8](proof.md).
'''
        self.assertFalse(any(BARE_MATH.search(line) for _, line in prose_lines(source)))

    def test_public_prose_does_not_treat_comparisons_as_html_tags(self):
        lines = list(prose_lines('<em>Work</em> x<y and y>z.'))
        self.assertIn('x<y and y>z', lines[0][1])
        self.assertTrue(BARE_MATH.search(lines[0][1]))

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

    def test_svg_title_preserves_encoded_source_whitespace(self):
        source = 'x ' + '\n' + 'y'
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'formula.svg'
            template = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">'
                        '<title>{}</title><path d="M0 0L1 1"/></svg>\n')
            path.write_text(template.format(source))
            with self.assertRaisesRegex(ValueError, 'trailing whitespace'):
                validate_svg(path, source)
            path.write_text(template.format(source.replace(' \n', '&#32;\n')))
            validate_svg(path, source)

    def test_quantity_purpose_overrides_expression_length(self):
        text = r'Work $O(n)$; parameter $E(N)=\exp(O((\log(N+2))^{4/5}(\log\log(N+4))^{1/5}))$'
        prepared = '\n'.join(quantity_paragraphs(text, ['showcase', 'literal']))
        result = self.present(prepared)
        self.assertEqual(result.count('![Formula]'), 1)
        self.assertIn('\nO(n)\n', result)
        self.assertIn('<code class="math">E(N)=', result)
        recovered = []
        transform(result, PAGE, source=True, records=recovered, root=ROOT)
        self.assertEqual([r['tex'] for r in recovered], [
            'O(n)', r'E(N)=\exp(O((\log(N+2))^{4/5}(\log\log(N+4))^{1/5}))'])

    def test_quantity_roles_reject_stale_or_invalid_annotations(self):
        for purposes in ([], ['showcase', 'literal'], ['automatic'], 'showcase'):
            with self.assertRaises(ValueError):
                quantity_paragraphs('$O(n)$', purposes)

    def test_literal_quantity_keeps_punctuation_and_tex(self):
        result = self.present('\n'.join(quantity_paragraphs(
            r'Parameter $N=w^2-1$; degree $2p(w-1)$', ['literal', 'showcase'])))
        self.assertIn('<code class="math">N=w^2-1</code>', result)
        self.assertIn('\n2p(w-1)\n', result)
        self.assertEqual(result.count('![Formula]'), 1)


if __name__ == '__main__':
    unittest.main()
