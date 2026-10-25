# Verification note

**Curated source path:** `sources/checkpoint-q/gomory_hu_adapter_independent_audit.md`

The source audit follows.

# Independent audit of the general-graph Gomory--Hu adapters

**25 October 2026.** This note checks Sections 2--8 of
`gomory_hu_seven_eighths_dependency_audit.md` independently of its
author. The strong-forest construction, its source-rooted parent rule,
and the finite MWU estimates also have separate audit notes. The
external recursion and public-baseline comparison are separate
obligations; this note does not certify an unspecified almost-linear
black box.

The audit found no blocking defect in the adapters below under their
stated strong-forest and augmented-tree interfaces. This is a
mathematical research check, not an implementation or external
verification.

## 1. General degrees are handled at the correct boundary

Replace each current vertex by an incidence path and give every
connector capacity one plus the sum of the current original capacities.
Each port has at most one original incidence and at most two path
incidences. Thus the expanded graph has maximum degree three and
linear size, including one node for an isolated vertex.

A cut that separates two original terminals has a whole-fiber lift
of capacity at most the total original capacity. A minimum such cut
therefore cannot split a connector. This proves exact preservation of
all terminal-pair minimum cuts and the minimum terminal cut.

The terminal sparsifier's upper cut guarantee is applied to the
whole-fiber lift of each queried original cut. Its lower terminal
mincut guarantee uses the exact preservation just proved. The output
can consequently be renamed to the original terminal set.

The expansion is repeated at every guide-packing entry. This is
necessary because the later Gomory--Hu contractions can create
arbitrary degrees. A degree bound proved only for the initial graph
would not justify its internal strong-forest calls. All subsequent
null-fiber work is measured against this expanded physical graph.

Empty or singleton terminal sets need no packing iteration. Disconnected
inputs are processed componentwise; zero cuts between components are
handled directly. In particular, a minimum over an empty Steiner tree
is never requested.

## 2. Fixed geometric copies give a literal decremental input

For each monotonically increasing positive integer length, retain a
fixed geometric ladder of all lengths above its current value. The
smallest retained length is a multiplicative upper approximation.
Each level is deleted at most once. A price refresh that stays in one
level does not submit a new structural update to the forest oracle.

The integer ladder in the main note starts at a sufficiently large
fixed denominator multiplier. This makes its successive ratios lie
between `1+eta/2` and `1+eta`, including at the bottom of the range.
There is no assumption that rounding a tiny geometric value preserves
that ratio without an initial-scale convention.

Parallel copies are then replaced by fixed binary port trees. The
physical input to this step already has degree three, so each tree
has only `O(log N)` leaves. The positive connector cost per original
path edge is `O(log log N)`; multiplying real lengths by a sufficiently
large `O(eta^-1 log log N)` integer absorbs that cost. The resulting
proxy is degree three, has polynomial integer aspect ratio, and
undergoes only edge deletions.

The lower metric inequality follows by projecting a proxy walk and
dropping connector length. The upper inequality follows by lifting an
original shortest path with the cheapest surviving copy on every edge.
It is a pathwise proof, not an inference from the number of bits in a
length representation.

## 3. Projection preserves canonical identities and controls work

After the strong forest is built on the proxy, only the designated
proxy node for an original physical vertex remains distinguished.
Other proxy canonical nodes become auxiliary occurrences. A true-null
component contains aliases of exactly one physical vertex and at most
one distinguished node.

Contract each such component at the final physical root. A component
with a distinguished node keeps that same record as its representative,
including when a later deletion splits the component. This preserves
the permanent canonical injection. Contracting existing forest edges
preserves acyclicity and cannot merge different source components.

Every original physical edge has only a logarithmic number of proxy
types. Hence both vertex and edge occurrence bounds gain only a
polynomial logarithm. Since the physical graph at this projection is
degree three, the real incidences of a null fiber are bounded by a
constant times the physical edge occurrence bound. Rebuilding affected
quotient components is therefore covered by a fixed power of the
strong-forest overhead. The argument would not hold if this last
degree bound referred only to the proxy graph rather than the physical
image graph.

## 4. The helper MST proof does not require exact Voronoi cells

The rooted forest assigns every canonical physical vertex to a unique
canonical source. Give forest edges helper key zero. For every physical
edge `uv`, add a helper edge between canonical `u` and `v` with key
`dhat(u)+length(uv)+dhat(v)`. Each estimate is an upper approximation
to distance to the source set. No claim that its assigned source is
the exact nearest source is needed.

Consider any partition of the sources, and take a shortest physical
path between its two sides. The canonical assignment changes sides
on some edge of that path. Each endpoint's nearest-source distance is
at most the corresponding prefix or suffix length. The helper key at
that crossing is therefore at most `1+epsilon` times the whole path
length.

For every cut of the terminal set, the helper graph's minimum crossing
key is thus at most the corresponding minimum metric-closure crossing
key times `1+epsilon`. At any Kruskal threshold, a component of the
helper graph cannot split a component of the rescaled metric closure:
otherwise this cut inequality would provide a crossing helper edge
below the threshold. Integrating the number of components proves the
MST-weight comparison in the main note.

All forest edges have zero helper key and form an acyclic set, whereas
the additional keys are strictly positive. An MSF therefore includes
the forest. Expanding its nonzero edges by their two paths to the
canonical source roots gives a connected subgraph containing all
terminals. Its physical cost is bounded by the sum of those expansion
costs, even when physical edges repeat. The unique terminal subtree
can only cost less. Combining with the metric-MST doubling bound
gives the required `2+O(epsilon)` Steiner approximation.

## 5. Labels and physical occurrences are different update charges

Changing a forest edge can alter many root-path lengths, so forest
recourse alone does not pay for maintaining all helper keys. The
construction instead exposes the monotone ES candidate labels already
updated by the approximate-ball algorithm. Their actual label-change
transcript is included in its work bound. Each canonical label change
updates only constantly many native helper keys because the physical
input has degree three.

A fine-grid physical-price refresh updates the physical-length data
on all current occurrences, and it updates its one additional helper
edge key. This can cost the occurrence bound, which is paid explicitly.
It is not treated as a constant-time operation.

The augmented dynamic-tree interface retains pending loads on edges
outside the current MSF as well as inside it. Changing MSF membership
therefore does not discard a pending value or force a new physical
price. Retiring an actual helper occurrence does flush its pending
load before its physical-image metadata is removed.

## 6. The numerical feedback count is not circular

Threshold flushes are paid by actual normalized physical load. Tiny
retirement flushes are instead paid by explicit occurrence deletions.
They may cause further price refreshes, but the forest receives only
geometric level deletions, of which there are only `O(m log N)`.
Its recourse bound consequently applies to the entire adaptive queue,
independently of how many small flushes occur.

All queues settle before another packing increment. During a queue,
flushing only moves load from a pending field to an exact accumulated
field. It does not increase total load or the conceptual full-load
potential. This preserves the overshoot bound in the independent
finite-MWU audit. The constants there take the multiplicity cap with
enough slack to make each whole packing iteration a small normalized
increment.

## 7. Finite prices and one common skeleton scale

Every packing increment has denominator equal to one fixed power of
two. All loads and Euler-tour weights therefore have a common grid;
their bit lengths do not grow by multiplication of unrelated rational
denominators. Recomputing an exponential from the exact accumulated
load, with certified additive error on a common grid, avoids cumulative
rounding error. Taking the maximum with the previous approximation
preserves the same error bound because the underlying price increases.

Fixed internal accuracy makes both the initial price and the smallest
grid quantum inverse polynomial in the master size. The actual
structural lengths after division by the grid quantum are therefore
polynomially bounded integers. This is stronger than a bound on the
magnitude of exact rational prices.

After the common feasible scaling, every terminal-sparsifier edge has
weight `b_e/(2 alpha Z)` for an integer `b_e`. Supplying the graph of
integer capacities `b_e` to the skeleton procedure is exactly one
common rescaling of every cut. The original units need not be recovered
when constructing guide trees. Both the skeleton's edge count and its
unweighted minimum-cut value are charged before calling tree packing.

## 8. Remaining provenance

The strong-forest proof is checked in
`separated_metric_forest_independent_audit.md`; its multi-source
construction is checked in
`multisource_rooted_approximate_ball_forest.md`. The exact finite-MWU
inequalities and Li's updated skeleton theorem are checked in
`finite_mwu_and_li_skeleton_independent_audit.md`.

The final quantitative Gomory--Hu consequence additionally requires
the fixed-power audit of the external SSMC, expander, hitting-family,
and recursive-inventory components. Those source dependencies and
the strongest verified public comparison must be read alongside this
adapter audit. A smaller exponent is not established by substituting
a faster static maxflow theorem into an unquantified reduction.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
