# Independent audit: complete one-sided separation on an allocation forest

**25 October 2026.** Audited main construction:
`complete_unrestricted_forest_one_sided_client.md`, Sections 1--7.

**Verdict:** the complete static numerical client and the stated
forest-preserving structural-transcript extension pass this audit.
For the optional potential query, delete isolated zero-total rows or
define their source-offer value separately; they do not participate in
any feasible numerical direction. This is a local forest-support
result and supplies no automatic bound for a general matching graph.

## 1. The separation problem really is complete on the ambient forest

Both directions of every ordinary incidence are present. A receiver
has zero cost and a donor has its conservative positive cost. The
ordinary support, not just a chosen routing subgraph, is a forest.
Consequently every ordered pair of bins has at most one underlying
simple path. Every directed walk between them reduces to that path
after deleting backtracks, and deleting a backtrack cannot increase
the path cost.

The directed constant-state cluster DP therefore searches the whole
ordinary path problem. Its existing boundary joins do not assume
that the two orientations of an edge have equal cost or that one
orientation is forbidden. The pendant source/sink price leaves keep
mutable bin prices out of high-degree vertex summaries. Standard
top-tree expose and local-update interfaces are the same ones audited
for `bidirected_potential_compatible_forest_matching_interface.md`;
the primary dynamic-tree source is
[Alstrup et al., top trees, Theorems 1--3 and 7](https://arxiv.org/html/cs/0310065v2).

## 2. Sign-compatible circulation decomposition is the right interface

Orient an allocation coordinate from its row to its bin and a slack
coordinate from the auxiliary vertex z to its bin. The difference
between two feasible allocations has zero divergence at every row
and bin. Summing the row and bin equations also gives zero divergence
at z. Reversing the coordinates with negative difference produces a
nonnegative residual circulation.

Decompose that residual circulation into simple directed cycles.
Only one direction of any physical coordinate is present, so the
decomposition never counts artificial cancellation along the same
coordinate. Charges are linear on this fixed sign pattern: negative
allocation differences cost `1/x_e`, positive allocation differences
cost zero, and slack differences in either direction cost `1/s_d`.
The objective derivative and the one-sided charge both add exactly
over the decomposition.

A cycle avoiding z has zero slack gain. A simple cycle containing z
visits it once, enters a bin a, follows an ordinary simple path to
a bin b, and returns to z. Its gain and charge are precisely

\[
 G=1/s_a-1/s_b,
 \qquad C=1/s_a+1/s_b+\sum_{e\text{ donor}}1/x_e.
\]

If every such cycle has `G<=C/2`, their nonnegative weighted sum
does too. Conversely, a feasible comparison exceeding one half must
contain a path exceeding one half. The static forest DP finds a
positive conservative offer for every such path. Thus its empty
answer certifies the asserted LOW condition on all feasible
comparisons, rather than only on paths compatible with an old label
vector.

The matching comparison numbers in the main note give
`(P-Q_s)/(P+Q_s+Q_x)>(P-N)/(P+4N)>11/16` when
`P>12N`, `Q_s<=N`, and `Q_x<=3N`. Their contradiction to LOW
is valid, conditional on that comparison being available at the
settled matching state as explicitly stipulated.

## 3. Gain, rounding and lower guards

Write `A=1/s_a`, `B=1/s_b` and `L=bar L/H`. A positive
integer offer implies

\[
 \tfrac34 A-\tfrac54 B-L>0,
 \qquad A-B>\tfrac14(A+B+4L)=V_{\rm up}/4.
\]

For a step with `eta V_up<=1/256`, the quadratic remainder in
`log(1+eta A)+log(1-eta B)` is smaller than half this first-order
gain. This proves the stated positive constant objective increase
when `eta V_up>=1/512`. No label feasibility enters the argument.

The same offer gives `A>(5/3)B`; hence the decreasing terminal
slack remains larger than the old starting slack after the small
step. The global minimum slack cannot decrease on a static ledger.
For each donor, its individual cost is below the entire positive
source budget, so

\[
 1/(4x_e)\le\bar c_e/H<3/(4s_a),
 \qquad x_e>s_a/3.
\]

Also `V_up>=1/x_e`, and thus `eta<=x_e/256`. Its allocation
after the step is at least `(255/256)x_e`, explaining the precise
floor factor in the main proof. An allocation already below this
source-slack scale cannot be used as a donor of an accepted path.
Guards chosen strictly below the initial range therefore cannot
create a permanent third outcome between a path and LOW.

For completeness of the rounded search, the register inequalities
give `bar c_e/H<1/(2x_e)+1/H`. A true ratio above one half has
enough positive margin to pay all path and endpoint rounding errors.
The required number of errors is at most the ambient forest vertex
bound plus two, which the declared H budget explicitly covers.

## 4. Implicit current potentials are optional and well defined

For any component containing a bin, the maximum source offer
`I(v)=max_a {sigma_a-dist(a,v)}` is finite. Nonnegative arc lengths
and deletion of backtracks imply every ordinary Bellman inequality.
At LOW the sink inequalities hold as well. Thus `D*(v)=A0-I(v)`
is a feasible current threshold potential, and the displayed slack
excess bound follows from `I(d)<=tau_d` and the ceiling error.

This potential is supplied as a query, not maintained numerically
after every path step. Exposing a vertex reads the relevant boundary
state. Materializing all values is an optional one-time linear-tree
pass. An isolated zero-total row has no relevant constraints and
may be removed; alternatively assign it an arbitrary isolated value.

## 5. The runtime account survives unrestricted receiving steps

The static objective width is `O(number_of_bins log S)` and each
step increases it by a constant. Hence there are only that many
steps. Every step has bounded total negative allocation log variation.
The endpoint-free sum of allocation logs telescopes, so total positive
variation is bounded by the negative variation plus its polynomial
range width. A register crossing consumes constant absolute log
variation between consecutive resets.

Unrestricted receiving traversals can decrease donor prices. This is
already supported by the bidirectional watcher: a reset, regardless
of its trigger direction, updates the one physical donor-price entry
in the DP. No price change is skipped as an off-forest event.
Consequently the claimed total register count, and linear-input
times polynomial-logarithmic static work, follow.

For structural batches, all changed coordinates and affected slacks
are explicit charged records. Their births, removals and external
settings bound the downward objective variation and the external
allocation-log variation. All cuts precede new links, and every link
can be checked for acyclicity. The displayed total depends on the
actual transcript sizes `A_T,A_x,A_s`; there is no free high-degree
retirement, retargeting, feasibility restoration, or general matching
expansion.

The final limitation is essential: a degree-three expansion can
connect two vertices already linked by an ordinary path and create
a cycle. The ambient forest hypothesis would then fail. The audit
does not transfer the near-linear numerical bound to that general
case.

