# Recent deterministic routing primitives: exact interfaces and remaining gaps

This note records a targeted primary-source check made after the `4/5`
checkpoint. It does not change that checkpoint or promote a new exponent.
The target is a deterministic, sequential, explicit-path primitive whose
structural output cost is smaller than its preprocessing cost. Bounds of
the form `m^(1+o(1))`, without a quantified rate or the necessary output
interface, are not substituted into the quantitative matching theorem.

Write `U = log M` for the master size logarithm. The current provider
separates output `log Gamma = O((p+r) log U)` from preprocessing containing
`U/p + U/r + r^2 log U`. The following are source-interface conclusions,
not lower bounds on all possible algorithms using these papers.

## 1. Disjoint paths through hypergraph perfect matching

[Bucic, He, Huang and Saranurak, arXiv:2511.02214v1](https://arxiv.org/html/2511.02214v1)
give deterministic edge-disjoint paths in a conductance-`phi` graph of
minimum degree `delta`, for pair load at most `k` per vertex. Their fast
version needs `phi^3 delta >= n^(o(1)) k`. The more explicit short-path
version has length `18 log n / phi` but time
`m n^(1+o(1)) min(k,1/phi)`.

The tunable hypergraph statement, Lemma 3.5, requires Haxell strength
`24 alpha d r^2` and `d >= 4 alpha`. Given the approximate half-layer
oracle, its iteration factor is

    exp(O(log n / sqrt(log d))).

The path-hypergraph construction supplies strength proportional to
`phi delta / k`. Thus the large parameter `d` has an actual resource
cost in a use that duplicates graph capacity or splits the demand into
many batches. The theorem does not give an unconstrained,
degree-proportional token router.

### Why high degree alone does not supply our present interface

In one degree band, a witness edge has weight `rho`, and its endpoint
degree is proportional to `deg_J(v)/rho`. The copied candidate inventory
used by the current ambient sparsifier asks for `ceil(rho)` candidates
per witness edge. Its endpoint token load is therefore proportional to
`deg_J(v)`. On an approximately regular band, the ratio between minimum
degree and demand load remains constant as the degree increases. This
does not create the required Haxell slack.

Asking for only one path per witness edge changes the premise: high
degree may then make the disjoint-path theorem applicable. It also
changes the conclusion needed by the ambient sparsifier. That one path
carries weight `rho`. Even if native graph edges are used at most once,
an ambient vertex occurring in the fixed images of `C_0` such edges can
receive weighted load `rho C_0`. The desired bound is a small factor
times `C_0 + Delta`, not `rho C_0`. The copied inventory and weighted
selection were the mechanism that removed this multiplicative weight.

This distinction persists if low-degree pieces are retained directly.
A new ambient-aware weighted routing theorem could change the situation;
the published disjointness guarantee by itself does not.

At the purely quantitative level, making the displayed iteration factor
at most `exp(O(U/p))` asks for `log d = Omega(p^2)`. Paying `d` in output
congestion is larger than the current `exp(O(p log U))` output factor in
the parameter range used by the `4/5` checkpoint.

## 2. Low-step multicommodity flow emulators

[Haeupler, Hershkowitz, Li, Roeyskoe and Saranurak,
arXiv:2406.14384v1](https://arxiv.org/html/2406.14384v1), Definition 9.1 and
Theorems 10.1--10.5, return an implicit flow oracle. A query specifies a
set of commodities and returns the aggregate edge-flow vector for that
set. Construction and each oracle query have work
`(m + support(D)) N^(poly(epsilon))`; the approximation/length factor is
`exp(poly(1/epsilon))`, for epsilon above a stated inverse-polylogarithmic
threshold. These are deterministic work bounds, not just round bounds.

The stated oracle is insufficient as an explicit token-path black box.
Querying each commodity separately can multiply the graph-size term by
the number of commodities. A support-size bound counts flow paths and
does not itself charge expansion of all their original-edge sequences.

The representation adapter is now reconstructed in
[hhl_shared_path_dag_and_conditional_tradeoff.md](hhl_shared_path_dag_and_conditional_tradeoff.md).
Refining every local emulator edge into one capacity-weighted parallel
copy per local embedding path preserves its stated path-count envelope.
Section 5 then gives a shared acyclic concatenation representation;
Section 7's explicit `SplitFlow` and `ConcatFlow` operations add only
sparse record births. The note proves this structural accounting and
keeps primitive arithmetic/epsilon dependencies separate. Short records
can be extracted without expanding long ones, by
[compressed_fractional_path_extraction.md](compressed_fractional_path_extraction.md).
This is an adapter to the actual construction, not an additional
guarantee of Definition 9.1's opaque oracle interface.

### Quantitative source boundary

The dependency
[Haeupler, Hershkowitz and Tan, arXiv:2404.13446v2](https://arxiv.org/html/2404.13446v2)
provides a tunable length-constrained expander decomposition. Its
Theorem 15.1 displays a two-parameter work expression containing
`(1/epsilon)^(O(1/(epsilon epsilon')))` and length slack
`(1/epsilon)^(O(1/epsilon'))`.

The literal proof on PDF page 80 also prints

    s_i = epsilon^(-2) s_(i-1)^(1 + O(1/epsilon)),

then bounds all `s_i` over `1/epsilon'` recursive levels by the latter
single-exponential expression. That bound does not follow from the
printed recurrence alone. A neighboring reciprocal inequality is also
printed in the wrong direction for its use. These may be indexing or
presentation errors; this note does not infer that the theorem is false.
They do prevent an independently reconstructed sharper quantitative
rate from being obtained by reading those displays literally.

The newer, exact-definition investigation found two additional literal
intermediate-proof issues, both still present in the checked v2.
Lemma 14.3 drops the arboricity loss from the sum of sequential demand
sizes; a fixed K8 example violates its factor-one inequality. The
monotonicity of largest sparse-cut demand size used in Lemma 14.4 also
fails under a legal sparse cut, even at arbitrarily large admissible
slacks. Full finite examples and the precise scope are in
[hht_literal_sequence_and_parameter_boundary.md](hht_literal_sequence_and_parameter_boundary.md).
These are not asserted to refute the paper's top-level theorem, but a
repair needs more than a corrected exponent index.

The published `poly(epsilon)` / `poly(1/epsilon)` notation also does not
specify the exponent ratio needed for a comparison with the `4/5`
envelope. A successful use would have to fix that ratio, the valid
shrinking-epsilon range, and the path-record representation together.
No such improved provider is asserted here. The shared-DAG note gives
an explicit conditional target in terms of specified work/quality
exponents a,b and observes that the unchanged classical decomposition
channel independently retains the current 4/5 balance.

## 3. Stronger decomposition quality with slower quantified work

[Chuzhoy, arXiv:2211.10556v2](https://arxiv.org/pdf/2211.10556)
gives a deterministic decomposition with conductance
`Omega(delta / log^(9+o(1)) n)` after deleting a `delta` fraction of
edges, in `m^(1+o(1))/delta` time (Theorem 2.10).
Its tunable cut-player analysis has expansion loss
`2^(O(1/epsilon^6))` and a restriction
`epsilon > 2/(log n)^(1/24)`; Section 11.4 uses a very slowly shrinking
epsilon to obtain the displayed polylogarithmic quality.

The excellent decomposition quality is therefore not an immediate
faster quantitative preprocessing bound for the current construction.
In particular, neither the bare `o(1)` notation nor its stated
polylogarithmic output theorem supplies preprocessing
`exp(O(U^(4/5) (log U)^(1/5)))` above linear time. This is a limitation
of the verified import, not a claim of optimality for that source's
techniques.

## 4. Other recent sources checked

| Primary source | Precise reason it is not a replacement here |
| --- | --- |
| [Bansal--Jambulapati--Saranurak, 2602.15015v2](https://arxiv.org/html/2602.15015v2) | Near-optimal flow-expander decomposition overhead, but a polynomial-time construction using concurrent-flow optimization. No near-linear sequential work / explicit-path tradeoff is supplied. |
| [Agassy--Dorfman--Kaplan, 2511.06574v1](https://arxiv.org/html/2511.06574v1) | The main near-linear tree-sparsifier and balanced-cut primitives are explicitly randomized with high probability. |
| [Chen--Meierhans--Probst Gutenberg--Saranurak, 2410.13451v2](https://arxiv.org/html/2410.13451v2) | The near-optimal parallel/distributed expander decomposition is randomized. A work bound does not remove this randomness. |
| [Bodwin--Haeupler--Hershkowitz--Tan, 2510.10227v1](https://arxiv.org/html/2510.10227v1) | The improved length-constrained decomposition/union bounds are structural; the checked theorem does not provide the required fast deterministic construction. |
| [Li--Vaughn, 2608.13910v1](https://arxiv.org/html/2608.13910v1) | Deterministic spectral sparsification has an additive approximately quadratic vertex term and does not supply the required explicit ambient route embeddings. |
| [Chuzhoy--Parter, 2601.20718v1](https://arxiv.org/abs/2601.20718v1) | The dynamic spanner is a different interface: its stated parameter range is `k <= (log n)^(1/49)`, with stretch `poly(k) 2^(O(1/delta^6))`. Native splits and our selected-edge/provenance/ambient route guarantees are not automatic consequences. |

These checks found no ready-to-import improvement to the current
deterministic sequential provider. The constructive compressed-flow
route remains a specific possible research direction; it is not part
of the accepted matching chain.

The exact Chuzhoy--Parter comparison is expanded in
[chuzhoy_parter_2026_interface_boundary.md](chuzhoy_parter_2026_interface_boundary.md).
It distinguishes a maintained subgraph with an existential native routing
certificate from the explicit ambient paths, native split accounting,
and demand-route notifications required here. Its published parameter
range also does not improve the current charged time envelope.

A different proposed shortcut, using weighted distance spanners as
packing responses, is analyzed in
[weighted_spanner_packing_width_boundary.md](weighted_spanner_packing_width_boundary.md).
The positive packing inequality is explicit, but a linear per-response
width is compatible with short paths and a sparse selected tree. This
does not give an iteration lower bound; it identifies the missing
width or union-support guarantee.
