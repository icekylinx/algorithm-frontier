# Late public-baseline audit: Krampl's July 2026 dynamic spanner thesis

## Verdict

Martin Krampl's *Deterministic Fully-Dynamic Spanners with Low Worst-Case
Update Time* is a relevant public baseline that was absent from the earlier
spanner comparison. Its two displayed update bounds are at least linear in
the vertex count, for every positive-integer parameter choice. They do not
give the subpolynomial amortized update guarantees of the tracked-terminal
`4/5` construction, nor the insertion-independent low-recourse guarantee of
the fully dynamic `5/6` wrapper.

This is not a statement that one result dominates the other in every
coordinate. The thesis provides worst-case update guarantees, allows much
smaller stretches, and handles positive weighted graphs directly. These
advantages must remain visible in the comparison. The thesis is included on
the strength of its mathematical statements; its publication format is not
a reason to exclude it.

## 1. Primary source and scope

- Official repository record:
  <https://repository.tugraz.at/publications/1jwmj-4fy55>.
- Official thesis PDF:
  <https://repository.tugraz.at/publications/marc21/1jwmj-4fy55/files/101036.pdf?download=1>.
- DOI: `10.3217/1jwmj-4fy55`.
- The record states July 2026, version 1, and records public upload on
  September 22, 2026. The audit was performed on October 25, 2026.
- Local primary-source text:
  `sources/krampl_dynamic_spanners_2026.txt`; original PDF:
  `sources/krampl_dynamic_spanners_2026.pdf`.

Definition 2.1 uses a simple undirected graph, with an edge a two-element
vertex subset. Definition 2.20 assigns a positive real edge weight. Section
2.3 allows insertions and deletions; a weight change is represented by one
deletion and one insertion. Vertex changes are not part of the stated
interface. The algorithms are deterministic, hence their guarantees do not
require an oblivious update sequence.

Section 4.1 explicitly gives the integer parameter domain `k,h in N+`.
The stretch is **`(2k-1)^h`**, not `(2k-1)h`; superscripts are lost in some
search-index snippets. The thesis counts weight operations in its algorithmic
model and does not supply a separate arbitrary-precision bit complexity.

## 2. Exact displayed guarantees

Let `n` denote the number of vertices. The thesis uses `m` for input/update
volume in its theorem statements; this table preserves that convention.

| Source | Stretch | Maximum number of spanner edges | Initialization | Worst-case update time |
|---|---:|---:|---:|---:|
| Theorem 1, introduction p. 8 and full statement p. 35; Lemmas 4.3–4.4 | `(2k-1)^h` | `O(k n^(1+1/k))` | `O(k^2 m)` | `O(h k^2 n^(1+1/k+1/h-1/(kh)))` |
| Theorem 3, introduction p. 8 and full statement p. 45; Lemmas 4.6–4.8 | `(2k-1)^h` | `O(k n^(1+1/k))` | `O(h k m)` | `O(k^2 n^(2(hk+h+k-1)/(2hk+k-1)))` |

The first algorithm partitions original edges among leaves of a
sparsification tree. An update recomputes static spanners along one
leaf-to-root path. The second algorithm uses a two-dimensional topology tree
to reduce the sizes of intermediate subgraphs. Both use the deterministic
weighted static spanner construction cited as RTZ05 in the thesis.

Theorem 2, pp. 36–37, states that for any superconstant target stretch one
can obtain `n^(1+o(1))` size and `n^(1+o(1))` worst-case update time, with
near-linear initialization. That `n^(1+o(1))` update bound must not be
transcribed as `n^o(1)`.

The statements quantify over integer parameters, while the constructions
write real-valued branching factors and the superconstant-stretch proof
writes real-valued choices of `k,h`. This audit has not independently
reproved every rounding and uniformity detail, or the sparse-initialization
accounting. None of these unresolved implementation details is used to
discount the source: the comparison below grants the displayed guarantees
with their stated parameter freedom.

## 3. Why growing parameters do not give the checkpoint time regime

For positive integers `k,h`, the two powers of `n` in the displayed bounds
are respectively

\[
 1+\frac{h+k-1}{kh},\qquad
 1+\frac{2h+k-1}{2hk+k-1}.
\]

Both are strictly greater than one. Growing parameters may make their
excess over one tend to zero, but cannot remove the leading linear factor.
Consequently even granting fully uniform parameter choice does not derive
a subpolynomial update bound from these formulas.

This is a comparison of proved upper-bound formulas, not a general lower
bound for dynamic spanners. There is also a concrete reason in this
construction: Section 4.3, p. 47, explains that the root spanner is recomputed
entirely after each update. On a connected graph, an explicitly reconstructed
spanning subgraph contains at least `n-1` edges. A different incremental
implementation of that root computation would require a new analysis.

## 4. Recourse and the two checkpoint interfaces

The thesis does not state a separate low-recourse theorem for either new
algorithm. Section 4.3, p. 47, explicitly warns that the entire output spanner
may change after one update. A safe immediate bound from output size is
`O(k n^(1+1/k))` symmetric-difference recourse per update. This is an upper
bound; this audit does not assert a matching recourse lower-bound example.

The checkpoint interfaces have different objectives:

| Interface | Update guarantee | Stretch and size regime | Recourse accounting |
|---|---|---|---|
| Krampl Theorems 1 and 3 | Worst-case; the formulas above retain a linear `n` factor | Can give constant stretch with polynomial size loss, or arbitrarily slowly growing stretch with `n^(1+o(1))` size; positive weighted graphs | No separate low-recourse theorem; full replacement is allowed |
| Tracked-terminal flat-forest construction | Total work `(n+m0+I+D) exp(O(U^(4/5) h^(1/5)))` | Stretch and size overhead `exp(O(U^(4/5) h^(1/5)))`; unweighted construction with a separate dyadic-class extension to positive polynomial-range integer lengths | Total recourse charged to the same full update volume, including insertions |
| Fully dynamic low-recourse wrapper | Total work `(n+m0+I+D) exp(O(U^(5/6) h^(1/6)))` | Stretch and size overhead `exp(O(U^(5/6) h^(1/6)))` | Total recourse `(n+D) exp(O(U^(5/6) h^(1/6)))`, independent of the number of insertions |

Here the checkpoint notation is `U=log N`, `h=log log N`; this lowercase
`h` is unrelated to the thesis's integer hierarchy-height parameter. `N`
is the common master bound, and `I,D` count inserted and deleted input edges.

Thus this additional source does not change the named-pipeline numerical
comparisons already established for the checkpoint. It does strengthen the
public-baseline coverage and the explanation of why no global fastest or
all-parameter domination claim is made. In particular, the checkpoint's
amortized bounds should never be described as an improvement of this
thesis's worst-case guarantee at the same constant stretch.

## 5. Operative references inside this checkpoint

- `tracked_terminal_flat_spanner_four_fifths.md`.
- `tracked_terminal_spanner_public_flat_comparator_audit.md`.
- `fully_dynamic_spanner_five_sixths.md`.
- `fully_dynamic_spanner_independent_audit.md`.
- `dynamic_spanner_public_baseline_audit.md`.

This late audit is an additive baseline clarification. It does not modify
previously delivered checkpoint ZIP files.

The root directly read the official PDF's abstract, Theorems 1 and 3,
and the Section 4.3 discussion, and checked the two exponent identities.
The conclusion grants the source's displayed parameter freedom and does
not rely on rejecting unexamined rounding details. The separate weighted
extension of the checkpoint construction remains part of its scope.
