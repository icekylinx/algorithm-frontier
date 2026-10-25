# An exact terminal solver for the cycle-ratio recursion

**Elementary deterministic base case.** This note makes the small-graph
oracle in both numerical routes explicit. It uses ordinary Bellman--Ford
negative-cycle detection with exact integer arithmetic. No algebraic
randomization, isolation assumption or approximate final comparison is
needed. The method is a standard reduction, not a publication-priority
claim.

## 1. Input and optimum

Let an undirected multigraph have total size b=|V|+|E|. Every edge has
a fixed orientation, an integral signed gradient g_e and a positive
integral length ell_e. Preserve physical edge IDs, including parallel
edges and loops. If there are no edges, return OPT=0 immediately.
Otherwise put G=max_e |g_e| and Lmax=max_e ell_e.

For a nonzero circulation d define its absolute ratio by

    |sum_e g_e d_e| / sum_e ell_e |d_e|.

The optimum is zero if no circulation has nonzero gradient. Otherwise
it is attained by a simple directed cycle in the bidirected edge
representation. To see this, orient a circulation's used edges by its
signs, reverse the entire circulation if necessary, and decompose the
nonnegative directed flow into sign-compatible simple cycles. The full
ratio is a length-weighted average of those cycle ratios.

A simple maximizing cycle has at most b edges. Its numerator and
denominator are integers and its positive denominator is at most

    D=b Lmax.

Two distinct possible simple-cycle ratios therefore differ by at
least 1/D^2. A positive one is at least 1/D, and every ratio is at
most G because ell_e>=1.

## 2. A decision procedure at a dyadic threshold

For threshold tau>=0, replace an oriented edge e=(u,v) by two directed
arcs, each retaining e and a sign:

    u -> v: cost tau ell_e-g_e,
    v -> u: cost tau ell_e+g_e.

A loop gives the analogous two signed loop arcs. A negative directed
cycle exists if and only if OPT>tau. One direction follows by using
an optimizing circulation's sign-compatible cycle. Conversely a negative
cycle has positive gradient exceeding tau times its literal length;
its physical projection is a nonzero circulation with at least that
ratio. A zero physical projection has gradient zero and cannot give a
negative cost at a nonnegative threshold.

A directed simple cycle can use both orientations of the SAME
physical nonloop edge only as the two-arc return walk. That walk has
cost 2 tau ell_e>=0. Thus a returned negative simple cycle has no
physical cancellation of that form; parallel edges with different IDs
remain legitimate distinct edges. Its literal length equals the norm
of its signed physical projection.

Initialize all Bellman--Ford distances at zero, equivalently adding a
zero-cost super-source. A relaxation on the |V|-th full pass detects a
negative cycle in any component. Starting from the LAST vertex relaxed
on that full pass, follow predecessor edges |V| times to enter such a
cycle, which is then listed by its directed edge IDs.
All ties and arc scans use a fixed deterministic order.

For dyadic tau, multiply all arc costs by its common power-of-two
denominator. All comparisons and predecessor operations then use
integers and preserve the sign of every cycle cost.

## 3. Exact recovery

If G=0 or the threshold-zero test finds no negative cycle, return
OPT=0. Otherwise initialize lower=0 and upper=G; retain any negative
cycle found at threshold zero. Maintain

    lower < OPT <= upper.

Test their dyadic midpoint. If a negative cycle is found, set lower
to that midpoint and retain the returned cycle. Otherwise set upper
to the midpoint. Continue until

    upper-lower < 1/(2D^2).

The retained cycle has ratio r>lower and r<=OPT. If r were strictly
smaller than OPT, the rational separation bound would give
OPT-r>=1/D^2, contradicting the final interval width. Hence the
retained cycle is exactly optimal.

Its raw certificate is simply the sum of its listed positive edge
lengths. Choose its orientation for positive numerator. The output is
an explicit unit-coefficient cycle; no hidden real multiplicity needs
to be decomposed or rounded by the parent representation.

## 4. Cost and use in the recursion

There are O(log(2+G D)) midpoint tests. Each Bellman--Ford run takes
O(b^2) relaxations and O(b) space; predecessor-cycle extraction takes
O(b). Intermediate integer lengths have
O(log(2+bGLmax)) bits, up to a fixed constant factor from the dyadic
denominator. Exact multiword arithmetic is charged accordingly.

When b<=k A and all input quantities have O_a(log M) bits, the
initialization and recomputation cost is at most

    k^2 A^O(1) polylog_a M,

and certainly within the conservative k^3 A^O(1) base envelope used
by the routing route. The degree-sensitive distance route uses
b<=4k Delta and its larger local polynomial envelope likewise covers
this solver. The explicit cycle has at most b pieces. Private search
trees need not be added to the maintained occurrence forest.

The method does not improve the large-graph problem by itself. It
provides a finite, deterministic and exact base implementation for
`constant_degree_steiner_bridge.md` and
`distance_backend_general_matching_integration.md`.
