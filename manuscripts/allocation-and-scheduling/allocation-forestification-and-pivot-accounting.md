# Forestifying allocations: one paid batch and the remaining pivot problem

**Research boundary and preprocessing lemmas, 25 October 2026.**

Removing allocation logarithms makes an ordinary cycle circulation
neutral for the slack objective. It is then natural to replace the
large allocation support by a forest basis. This note separates three
claims:

* one floor-preserving forestification batch is feasible and can be
  implemented in near-linear time;
* off-basis receiving incidences must still be searched;
* repeated basis changes are not paid by the existing slack-progress
  or allocation-register argument.

These statements do not solve full-graph path discovery or improve
the general-matching exponent.

## 1. One finite-grid forestification batch

Fix a feasible positive ordinary allocation ledger
$$
\sum_{e\ni r}x_e=L_r,\qquad
 \sum_{e\ni d}x_e+s_d=b_d.
$$
Choose a common dyadic epsilon with
$$
0<\epsilon<\min_e x_e .
$$
There is a deterministic O(m polylog S) transformation preserving
every row sum and every bin load, hence every slack, such that the
incidences with x_e>epsilon form a forest. All other incidences
have allocation exactly epsilon and remain physically present.

The transformation uses only alternating ordinary cycle flows.
It changes no bin capacity, debt, matching cardinality, or physical
support edge. Therefore it does not require an invented equality
between distinct integral-floor ledgers. Any other ledger on the
unchanged physical support can remain as it was.

The transformation is a separately paid primal batch. It is not
asserted to have positive slack-objective progress.

## 2. An explicit dynamic-forest implementation

Process incidence IDs once, in a fixed order. Maintain a forest F
containing all already processed incidences whose current value
exceeds epsilon.

For the next incidence e:

1. If its value is epsilon, do nothing.
2. If its endpoints are in distinct F components, link it.
3. Otherwise, its addition closes one ordinary bipartite cycle.

In the third case orient the cycle so that e decreases. Along the
opposite F path its actual donor coordinates decrease and its
receiver coordinates increase. Choose
$$
\delta=\min\{x_e-\epsilon,\,
          \min_{\text{donors on that F path}}(x_f-\epsilon)\}.
$$
The minimum over an empty donor set is infinity. Apply the cycle
transfer. Every coordinate remains at least epsilon, every row
sum and bin load is unchanged, and at least one coordinate reaches
epsilon.

Report all forest donor edges reaching epsilon, then cut them.
If e remains above epsilon, link it. Its endpoints are now in
different components because at least one edge of their old
unique path was cut. The processed active support is again a
forest. All other processed incidences are fixed at epsilon.

The required path data are simpler than the priced watcher:
maintain directional minima of donor residual x-epsilon and
a signed path-add tag. A forward path transfer subtracts delta
from forward donor residuals and adds delta to reverse donor
residuals; inapplicable direction entries are infinity.
Point-querying an edge recovers its current value.

When several edges hit epsilon at once, find and mark all such
edges while the old path topology is still fixed, then perform
the cuts. A marking field excludes an already reported edge
from another minimum query. No path query is made through a
topology already broken by an earlier cut of the same batch.

Every input edge is processed once. Every forest edge cut at
epsilon was already processed and is never linked again in this
batch. Thus there are O(m) links, cuts and reports in total.
Standard dynamic-tree path/minimum operations give the stated
near-linear work. No long cycle is enumerated.

During this batch there is no need to maintain the numerical
shortest-path DP or issue one price notification after every
intermediate motion. At completion, materialize the O(m) native
values and initialize the next numerical data structure and its
registers in O(m polylog S) work. That cost is explicitly charged
to this batch.

## 3. Tiny off-basis donors can be excluded; receivers cannot

Suppose epsilon is below one third of the current minimum slack.
Any path passing the conservative one-quarter threshold satisfies,
for every actual donor,
$$
x_e>s_{\rm start}/3.
$$
It therefore cannot use an epsilon edge as a donor. A true path
of ratio above one half has the still stronger donor requirement
x_e>s_start.

Thus the epsilon incidences may be treated as receiver-only for
these threshold searches. This does not make the search graph a
forest. Every off-basis incidence still supplies its zero-cost
row-to-bin receiving arc.

If exact zero values were used instead, the donor direction would
be absent and the receiver would remain. That exact-zero variant
would require a new nonnegative-coordinate contract; the existing
positive-coordinate guards and prices do not silently define 1/0.
The epsilon construction avoids that issue while exposing the
same receiving-arc obstruction.

## 4. Forest positive support can still encode a directed graph

For a generic allocation ledger, take one bin v and one row r_v
per vertex of an arbitrary directed graph of out-degree at most
two. Give row r_v its owner incidence to bin v and one incidence
to bin w for each directed arc v-to-w.

Put epsilon on the latter incidences and
L-outdeg(v)*epsilon on the owner incidence. The owner incidences
form a disjoint-edge forest. Set each bin capacity equal to its
resulting load plus any prescribed positive polynomial-range slack.

A two-edge path
$$
v\to r_v\to w
$$
uses the large owner donor and the epsilon receiver. Its donor
cost is approximately 1/L. By taking epsilon small relative to
the minimum slack, no off-owner donor can occur on a strong path.

The resulting strong-path search contains the directed graph's
route-discovery problem, even though all large allocations form
a forest and every row has degree at most three. Ignoring the
epsilon receivers would lose those routes.

This encoding is a statement about the generic numerical ledger
interface. It is not asserted to be a reachable debt-free matching
state or a complexity lower bound. Its role is to identify the
missing interface rather than transfer an unproved hardness claim
to matching.

## 5. A matching-shaped cycle cancellation has large unpriced motion

A more directly relevant example shows why ordinary cycle pivots
cannot be charged to slack progress or to their single topological
support change.

Take a cycle with rows r_0,...,r_(t-1) and bins d_0,...,d_(t-1).
Row r_i has incidences to d_i and d_(i+1), with indices modulo t.
Add a free bin f adjacent to r_0. Rows have degree at most three,
and bins have degree at most two.

Every bin has capacity L-C. Give each cycle bin slack 2C, and
put z=3tC on incidence r_0 f. Write a_i for x_(r_i,d_i) and b_i
for x_(r_i,d_(i+1)). Choose
$$
a_0=L/2-3tC,\qquad
 a_i=a_0+3(t-i)C\quad(1\le i<t),
$$
$$
b_0=L-a_0-3tC=L/2,\qquad b_i=L-a_i\quad(i\ne0).
$$
Then each row sums to L and each cycle-bin load is L-3C.
The free-bin slack is L-(3t+1)C. All coordinates are positive
for L sufficiently larger than tC; the usual matching phase
scale L=10000CN has ample room.

Now decrease every a_i by
$$
\delta=a_0-\epsilon
$$
and increase every b_i by the same amount. All slacks stay
exactly fixed. Only a_0 reaches epsilon. For i>=1,
$$
a_i'=3(t-i)C+\epsilon.
$$
Thus one cycle cancellation removes just one active support
edge, while changing Theta(t) other allocations by a large
relative factor.

For example,
$$
\sum_i\log(a_i/a_i')
 \ge (t-1)\log\!\left(
       \frac{L/2-3tC}{3tC+\epsilon}\right).
$$
At the stated phase scale this is Omega(t), although
Delta Phi=0. If the initial registers are ell_i=3a_i/4,
Theta(t) donor records cross their hysteresis boundary in this
one batch. A priced numerical structure would have to process
that many notifications unless the whole batch is separately
rebuilt and paid.

The lower integral floors also admit the same form of ledger:
replace C by a floor c_0 in the load construction and keep the
required residuals at least c_0. No top-versus-bottom equality
is used.

This example does not prove that a carefully chosen pivot rule
must repeatedly incur large work. It refutes only an automatic
charge of every ordinary cycle cancellation to its slack gain
or to O(1) basis-edge edits.

## 6. Why repetition still needs a new theorem

A single preprocessing batch is affordable. Repeating such a
batch after every accepted path may cost m work per step.

Once a path increases an off-basis receiver above epsilon,
positive support may again contain cycles. Choosing a new basis
can cause large negative allocation-log motion without changing
the slack objective. That motion is absent from the previous
bound which charged negative log variation only to accepted
one-sided numerical paths.

Unrestricted zero-objective basis pivots can even alternate
between different extreme allocations of one cycle. Their
slacks and Phi do not change. Consequently no bound on their
number or their price notifications follows merely from
bounded Phi or from the fact that each pivot drops an edge.

A useful sufficient next lemma would have to provide a specific
pivot policy and show, for example, that its total notifications
and actual forest edits are bounded by
$$
(m+\text{accepted numerical work}
                   +\text{structural transcript})\mathrm{polylog}S,
$$
while continuing to search all off-basis receiving directions.
Alternatively, it could give a different price data structure
that supports the entire zero-objective pivot without enumerating
its many threshold crossings.

Neither requirement is supplied by forestification alone.
The exact forest and feedback-edge clients therefore remain
parameterized tools, not a complete solution on general graphs.
