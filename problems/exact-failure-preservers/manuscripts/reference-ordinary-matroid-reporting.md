# Initialized ordinary two-matroid failure reporting

The [reference](../reference/matroid_reporting.py) completes the ordinary
fixed-rank construction of the
[canonical companion](exact-single-failure-arborescences-and-matroid-intersection.md),
Sections 2–6, using the canonical weighted-intersection initializer and the
existing [distance/hub reporter](reference-arborescence-reporting.md).
This implementation uses ordinary independence oracles and fixed signed
rational element costs. It does not implement the valuated companion.

## 1. Full input and output contract

The explicit ground is `range(N)`, indexed by the original cost-list
positions. Two paid callbacks are valid ordinary matroid independence
oracles on frozensets of these original IDs. Costs are fixed signed
integers/Fractions. A supplied nonnegative binary integer specifies the
prescribed cardinality `k`. No baseline optimum or finite-domain basis is
supplied. Each query independently deletes at most one original element;
costs and the matroids are unchanged between queries.

**Realization theorem.** The constructor returns `None` if no original
common independent set of cardinality `k` exists. Otherwise it returns
an exact single-deletion oracle whose support and record bounds are those
of the ordinary companion. A query returns an optimum surviving original
common `k`-set or an infeasibility answer, with no independence, optimization
or shortest-path calls. Rank zero has its empty optimum and constant query
cost. The constructor is deterministic and polynomial in the explicit
ground, encoded costs and paid oracle work. It uses the dense polynomial
reference routines, not the faster arborescence preprocessing algorithm.

## 2. Weighted initialization and initial infeasibility

The constructor calls `minimum_cost` in the
[canonical weighted-intersection backend](../../robust-bounded-certificates/reference/bounded.py)
and checks the resulting potential/cut certificate through that module's
search-free verifier. Its
[realization Proposition 2](../../robust-bounded-certificates/reference-realization.md#2-exact-weighted-augmentation-and-its-certificate)
identifies the exact classical dependency: Bárász, Bérczi, Király, Oki,
Yamaguchi and Yokoi, *Matroid Intersection under Minimum Rank Oracle*,
[arXiv:2407.03229v2, Definition 2.2, Algorithm 2 and Lemma 2.5](https://arxiv.org/html/2407.03229v2#S2).
With source weights equal to negative original costs, shortest cheapest
exchange augmentation gives an optimum at each successive cardinality.
Potential inequalities prove absence of negative exchange cycles and hence
fixed-cardinality optimality. A rank-sum cut proves maximum cardinality
when the requested size cannot be reached. This named theorem applies to
the full original exchange graph and arbitrary ordinary matroids, including
loops, with the loop convention justified in that canonical realization.

Thus successful initialization supplies exactly the optimum `B` required
by the companion. An underfull verified certificate proves initial
infeasibility; deletions cannot increase common rank. A requested rank
larger than the explicit ground is rejected as infeasible by cardinality
alone before constructing a rank-sized graph.

The initializer's full potential/cut and original callback references are
local preprocessing state. Only its chosen original IDs proceed to the
compact reporting construction. No ground-sized initialization certificate
is retained in the final oracle.

## 3. Compressed exchanges and the literal update

For every original element outside `B`, the implementation lists its
feasible single exchanges separately in the two matroids. It tests these
on the original callback ground. Each pair of an eligible first-matroid
removal and second-matroid removal gives a directed compressed candidate.
It keeps the lowest outside element cost for each ordered pair, including
loops, breaking cost ties by original ID. Since the removed tail's cost is
fixed for that ordered pair, this is exactly the minimum arc-length rule
in the companion's Equations D2–D3.

Every basis element is split into minus/plus nodes, with a zero split arc.
An exchange arc goes from its tail's plus-node to its head's minus-node,
has primary cost equal to outside cost minus removed-tail cost, and has
secondary length one. It records both original insertion and removal IDs.
There are exactly `2k` nodes and at most `k^2+k` arcs. This graph is formed
after truncating conceptually to size `k`; the original independence tests
on the size-`k` exchanges implement that truncation exactly.

The companion's tangent-direction argument proves nonnegative primary
cycle lengths from optimum `B`, despite signed original costs and repeated
outside labels on arbitrary compressed cycles. Every cycle has positive
secondary length. `_finish` therefore applies exact lexicographic dense
shortest paths and the existing deterministic phased hub construction
unchanged. Its shortest demand path is the minimum-cost, minimum-hop cycle
through the failed baseline element.

The companion's Section 4 support/value identity first supplies an optimum
basis supported on the cycle labels. The separate minimum-hop lemma then
forces every label distinct and proves that the entire literal toggle is
feasible. An arbitrary cheapest cycle is not assumed toggleable merely
from its value identity. Each compressed exchange arc stores its own
tail-removal ID, whereas the HLD graph stores the removal on the departure
to its segment leaf. The same final reporter reads these tags and inserts
exactly the labels. A shortest simple path uses each baseline vertex only
once, so both encodings produce the proved literal cycle update.

The retained support contains `B` and every outside original ID appearing
in stored short paths or hub trees. Every returned optimum uses this
support. Baseline-external failures return `B`; unreachable baseline
demands have precomputed infeasibility flags. All exact optimum values are
stored during preprocessing. The final `Oracle` has the same fields in
both implementations and keeps no original cost list or callback.

The phased hitting proof in the existing reporter gives the sparse
support/record bound and linear explicit reporting. Its shortest-path
prefix/suffix concatenation cannot repeat a split vertex because every
directed cycle is strictly positive in the lexicographic order. There is
no list of all full failure solutions hidden in the final structure.

## 4. Automatically initialized rooted arborescences

The graph wrapper keeps the existing nonnegative rational graph model.
It validates all original arcs and costs, treating loops and root-entering
arcs as loops of both initializer matroids. Other arcs are distinct elements,
including opposite and parallel original records. The first oracle tests
an underlying undirected forest; the second permits at most one incoming
arc per nonroot vertex.

The common independent sets of size `n-1` are precisely spanning
arborescences directed away from the designated root, by the
[Goemans Section 6.1.2 formulation](https://math.mit.edu/~goemans/18453S17/matroid-intersect-notes.pdf).
Their linear costs are exactly the original directed arc costs. The
weighted initializer consequently supplies an optimum directed rooted
tree, or correctly reports its absence. The wrapper passes that original
baseline to the existing HLD/segment-tree construction. This discharges
the lower-level supplied-optimum-baseline interface without enumerating
trees. The one-vertex empty baseline and initial no-tree cases are included.

The sparse HLD construction, its original-arc support and its query bound
are unchanged. This wrapper's initialization is polynomial weighted
intersection and is slower than the optimized arborescence algorithm of
the research theorem. The generic matroid API permits signed costs;
the graph wrapper does not enlarge its existing nonnegative model.

## 5. Actual preprocessing, final space and bit work

Let `N` be the original element count. The shared weighted initializer has
at most `N` successful augmentations and one final unsuccessful attempt.
Each exchange graph makes at most quadratically many independence calls.
Each shortest-path pass has at most linearly many rounds on that graph;
its exact labels retain explicit paths of at most `N` IDs. Even charging
linear record copying/comparison for each path gives the conservative
`O(N^5)` record/rational-operation and `O(N^3)` independence-call bounds.
The certificate verification is within those bounds. Its graph and path
tables occupy quadratic records, besides paid oracle workspace. No loop
iterates over the numerical magnitude of a cost or a requested rank.

After baseline supply, the compressed construction uses `O(Nk)` independence
tests, `O(Nk^2)` set/elementary processing, and the dense reporter adds
`O(k^3)` arithmetic work and quadratic temporary graph/path records.
These bounds are additional to the initializer. The graph wrapper pays
for its explicit graphic and partition tests, then the existing auxiliary
graph construction and dense reporter; its complete preprocessing remains
polynomial in the original graph and encoded costs.

The final bound is in records and original element IDs, independent of
the original ground except their encoding length. Exact retained costs,
their sums and input IDs are charged by actual bit length. Shortest-path
values and initializer potentials are sums of polynomially many original
rational costs, so their encodings have polynomial size. The algorithm is
not a parameter-only bit kernel, a valuated-matroid implementation, a
rank-drop objective interface, or a multiple-failure oracle.

## 6. Independent executable evidence

The [initialized checker](../verify/check_matroid_reporting.py) compares
every constructor, baseline and single-failure answer to explicit common-set
enumeration on bipartite partition matroids, binary represented matroid
pairs and an independently axiom-checked sparse-paving fixture. It checks
minimum outside-label counts among optimum repairs, not just their values.
Directed graph outputs are compared against the existing independent rooted
tree enumerator. Long signed matching cycles exercise hub trees. A much
larger original ground than rank checks that no ground-sized initializer
state escapes into the final reporter and disables callbacks/producers
after clearing the caller's cost list. These finite checks do not replace
the arbitrary-matroid initialization and literal-update proofs above.

**Attribution:** icekylinx and GPT-6 Astra Pro.
