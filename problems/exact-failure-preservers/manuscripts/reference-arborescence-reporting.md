# A supplied-baseline realization of arborescence reporting

The [reference backend](../reference/arborescence_reporting.py) implements
the rooted directed model of the
[ordinary companion](exact-single-failure-arborescences-and-matroid-intersection.md),
Sections 4–6. It accepts an explicit directed multigraph on vertices
`0,...,n-1`, an arbitrary designated root, fixed nonnegative rational costs,
and original arc IDs forming a supplied minimum-cost root-spanning
arborescence. This is a baseline-optimality promise. Input shape and exact
number types are checked; loops and root-entering arcs are discarded only
after validation. Discarding these arcs changes no rooted arborescence.
The empty one-vertex case is handled directly by the same API.

The [initialized ordinary wrapper](reference-ordinary-matroid-reporting.md)
now discharges this lower-level entry point's supplied-baseline promise
through canonical weighted intersection on the graph's graphic/partition
matroids. This note describes the HLD/reporting component after that supply;
the wrapper's slower polynomial initialization is accounted for separately.

**Realization proposition.** Under this input promise, `build` constructs
the companion's exact one-original-arc-deletion support and reporting oracle.
Queries return original arc IDs or a rank-infeasibility flag and use only
the final stored records. The implementation uses dense exact shortest paths
instead of the faster shortest-path preprocessing of the companion. Its
baseline computation is outside the implementation.

**Proof.** The rooted directed interpretation is the graphic/partition
common-base construction of Goemans, *Lecture notes on matroid intersection*
(2 May 2017), Section 6.1.2. Opposite and parallel original arcs are distinct
graphic elements. The partition exchange for an outside arc is the baseline
arc entering its head. The graphic exchanges are the baseline edges on its
undirected endpoint path. A common basis is a directed root-spanning tree,
not an arbitrary undirected tree. The backend validates exactly that
baseline shape, and preserves original directed arc IDs throughout.

`_auxiliary` roots the supplied directed tree, computes subtree sizes and
heavy children, and numbers edges along heavy chains. An endpoint path
becomes a union of heavy-chain edge intervals; its least common ancestor's
incoming edge is excluded. Canonical segment-tree covers represent each
interval exactly. Every normal plus-node has one departure to its edge's
leaf with primary length equal to minus its baseline cost. Segment arcs
ascend toward the root with zero length. A canonical cover node has a
labeled arc to the minus-node of the outside arc's head-parent, with primary
length equal to the outside cost and secondary length one. Split arcs have
both lengths zero. Thus every consecutive normal-node transition is exactly
a feasible graphic/partition exchange of the stated cost, including parallel
outside candidates. Conversely every such exchange is represented. A
segment tree on `k=n-1>0` leaves has `2k-1` nodes; the split normal nodes
contribute `2k`, proving the stated `4k-1` auxiliary vertex count.

Every directed auxiliary cycle contains a labeled arc and projects to a
nonempty exchange closed walk. The companion's tangent-direction lemma
gives nonnegative primary cycle length, and the secondary length is
positive. Consequently there is no lexicographically nonpositive directed
cycle. `_distances` computes exact Floyd–Warshall distances in this ordered
additive group. It stores both a first and a last original auxiliary arc for
every finite nontrivial distance. These arcs are tight for the final
distances. Choosing tight arcs toward or away from any fixed hub cannot
create a cycle: its tight-distance equalities would give total length zero.
The stored choices therefore define valid shortest-path trees, even with
primary cost ties and zero-length segment arcs. A negative exchange cycle
causes rejection as a defensive check on baseline supply.

`_sparsify` initially fixes one shortest simple path per finite demand.
For a phase with `p` remaining demands and `A` auxiliary vertices, it uses
the exact integer threshold `L=ceil(A/sqrt(p))`. It stores paths of at most
`L` arcs and then makes at most `ceil(A/L)` greedy hub selections. Every
remaining long path has more than `L` vertices, so a largest-incidence hub
hits at least the fraction `L/A` of the unhit paths. After the phase at most
the fraction `exp(-1)` remains. Explicit paths and complete hub trees use
`O(A sqrt(p))` records in that phase. Summing over the geometric decrease of
`p` gives `O(A sqrt(k))` records, including copied tree records and demand
descriptors. This is the deterministic specialization of the slack-to-complete
argument behind Bodwin, *A Note on Distance-Preserving Graph Sparsification*,
arXiv:2001.07741v3, Lemma 1 and Theorem 3.

For a demand assigned to a hub, its stored in-tree prefix and out-tree suffix
have total length exactly the optimum demand distance because the hub lies
on its fixed shortest path. Their concatenation cannot repeat a vertex:
removing the resulting strictly positive cycle would improve this optimum.
It therefore has at most `A-1` arcs. Split endpoints ensure that it projects
to a minimum-primary-cost, minimum-exchange-hop cycle through the failed
baseline arc. The companion's Section 4 literal-update lemma proves that
its labels and removals are distinct and the literal toggle is an optimum
surviving directed spanning arborescence. `Oracle.query` performs precisely
that toggle. The support includes the baseline and every label in every
stored path or tree, so it contains every query output. Unreachable demands
are stored as infeasible. Outside-baseline failures return the baseline.

Floyd–Warshall uses `O(A^3)` exact additions/comparisons and quadratic
temporary tables. First/last tables let each hub tree be copied in `O(A)`
work, without rescanning all original auxiliary arcs. The naive greedy
incidence scans take `O(A p^(3/2))` work over a phase and hence at most
`O(A^3)` across all phases, since `p<=k<=A`. Auxiliary construction adds
`O(M)` work and records with `M=O(n+m log^2 n)`. Baseline-shape validation
is at most quadratic in the number of original vertices plus input scanning.
After baseline supply, the reference therefore has the claimed cubic dense
preprocessing contract, quadratic-plus-auxiliary temporary storage, sparse
final records, and linear reporting. These are exact-arithmetic and record
bounds; bit work uses actual rational encodings. QED.

The [finite checker](../verify/check_arborescence_reporting.py) separately
enumerates small directed arborescences and tests direct graphic exchanges.
It also exercises long hub-reported repairs on larger bidirected-path
fixtures with independently forced minimum-hop optima. These checks support
the implementation connection; they do not prove the arbitrary-matroid or
valuated companions or certify an optimized preprocessing implementation.

Primary references: [Goemans, Section 6.1.2](https://math.mit.edu/~goemans/18453S17/matroid-intersect-notes.pdf),
[Bodwin, v3](https://arxiv.org/pdf/2001.07741).

**Attribution:** icekylinx and GPT-6 Astra Pro.
