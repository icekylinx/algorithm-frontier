# Computing the residual configuration relaxation for count-box players

The subsequent [residual-configuration-bounded-support-xp-solver.md](residual-configuration-bounded-support-xp-solver.md)
improves the bounded-support comparator to q^{O(r)} time by representing
the aggregate polytopes implicitly. The present fully enumerated-row
proof remains a simpler prerequisite for its strict pricing and
interior-ball arguments.

For arbitrary recipient polymatroids, the new subset-cut configuration
relaxation can be approximately optimized without expanding numerical
capacities when each player's local family is a coordinate box. The
runtime proved here is single exponential in the **number q of potential
players**, not in the selection rank r:

$$
2^{O(q)}\mathrm{poly}(H,\epsilon^{-1}).
 \tag{W1}
$$

The output is a fractional configuration point attaining at least
(1-epsilon) times the optimum of that relaxation. This is not a
(1+epsilon)-approximation algorithm for the integer allocation problem.
The separate allocation algorithm retains its factor-four guarantee and
its better dependence on r. Nor does the present pricing argument apply
to an arbitrary local downward-closed oracle: only count boxes are used.

The proof has three explicit parts: a binary convex-cost knapsack
scheme; a strict dual-pricing oracle; and an ellipsoid/Farkas reduction
with an explicit finite row set. A special positive direction in this
LP gives a uniform interior ball for every infeasible finite primal.
This makes finite primal extraction independent of an affine-hull
oracle or a lower-dimensional exact-feasibility convention.

## 1. Assumptions and the explicit row set

Assume selection rank r>=1 and a rational accuracy 0<epsilon<=1/2.
A requested accuracy in (1/2,1) may be replaced by 1/2. Rank zero is
handled separately by returning the empty allocation; the bounded
optimization statement below concerns positive rank.

For every player p and type j, give a binary upper quota F_pj, with
0<=F_pj<=f_j({p}). The local configurations are exactly the integer
vectors 0<=n_j<=F_pj. Unit values v_j are common nonnegative rationals.
At target T, only configurations with sum_j v_j n_j>=T are allowed.
The case F_pj=f_j({p}) is the unrestricted local model.

Use all subset-marginal resource inequalities from
[recipient-polymatroid-subset-cut-compression.md](recipient-polymatroid-subset-cut-compression.md):

$$
\sum_{p,n}\mu_{pn}\bigl(n_j-m_{pj}(S)\bigr)_+\le f_j(S),
 \qquad m_{pj}(S)=f_j(S\cup\{p\})-f_j(S).
 \tag{W2}
$$

For each player-matroid subset S, include

$$
\sum_{p\in S,n}\mu_{pn}\le r_M(S),
$$

and include the lower total-mass inequality

$$
-\sum_{p,n}\mu_{pn}\le-r.
 \tag{W3}
$$

The player inequality for S=P supplies the matching upper total bound.
Together with mu>=0, these are precisely the player-basis conditions.

The aggregate resource inequalities y_.j(S)<=f_j(S) are already implied
by (W2): for p in S, the marginal m_pj(S) is zero, so the left side
of (W2) includes y_.j(S), plus nonnegative outside terms. They may be
included redundantly without affecting the proof.

Enumerate the O((t+1)2^q) rows explicitly. All f_j values and player
matroid ranks on subsets are obtained by the supplied paid oracles;
the number of queries is exponential only in q. Each column is still
implicit and represents one bounded integer configuration of one player.
All row and column coefficients are integers of polynomial bit length:
unit values and T determine which columns are allowed, not the entries
of their resource or player constraint columns.

## 2. The convex pricing cost has finitely many binary segments

A nonnegative weighting of the upper resource inequalities assigns
player p a cost function of the form

$$
G_p(n)=\sum_j g_{pj}(n_j),\qquad
 g_{pj}(a)=\ell_{pj}a+
              \sum_h b_{pjh}(a-s_{pjh})_+,
 \tag{W4}
$$

where ell and b are nonnegative rational prices and every breakpoint
s is an integer between zero and the resource singleton bound. In
(W2) alone, ell can be zero; redundant aggregate resource constraints
contribute a nonnegative linear term. Breakpoints beyond F_pj do not
affect this player's configurations and can be discarded.

The incremental unit costs g(k)-g(k-1) are nonnegative and
nondecreasing. Sorting the breakpoints partitions the integer interval
1,...,F_pj into a number of segments at most one more than the number
of explicit positive-price hinge terms. Each segment has a binary
integer capacity, constant marginal cost, and common per-unit value
v_j. The interval is never expanded into individual units.

One may temporarily ignore the requirement that earlier segments of
the same type be filled before later ones. This is exact for the
pricing optimum: any selected units of one type can be moved to the
cheapest prefix of that type without changing their count or value,
and without increasing cost. Conversely a legal count vector uses
the prefix segments and is allowed in the relaxed segment model.
Both models therefore have the same optimum value under a cost budget.

## 3. A fully polynomial value approximation with an exact cost budget

Consider maximizing sum_j v_j n_j under G_p(n)<=C and 0<=n<=F_p.
Split every constant-cost segment of capacity d into binary chunks
whose sizes are 1,2,4,... and a final remainder. There are O(log(d+1))
chunks, and every integer count from zero to d is represented by a
subset of them. A chunk has its size times the segment's unit value
and unit cost. The total chunk count N is polynomial in the explicit
pricing description and the binary quota lengths.

This produces an ordinary zero-one knapsack instance. Select all
zero-cost chunks of positive value. Remove positive-cost chunks whose
cost exceeds C; they cannot occur in any feasible solution. If no
positive-value chunk remains, the free chunks are optimal. For C=0,
this directly handles the whole problem.

Otherwise let Pmax be the largest remaining chunk value. Every such
chunk individually fits, so the optimum remaining profit P* is at
least Pmax. For rational 0<epsilon<=1/2, put

$$
\Delta=\epsilon Pmax/N,
                 \widehat P_i=\lfloor P_i/\Delta\rfloor.
 \tag{W5}
$$

Every rounded profit is at most N/epsilon. Dynamic programming stores
the minimum exact rational cost for each total rounded profit and
selects the largest attainable rounded total with cost at most C.
There are O(N^2/epsilon) totals and O(N^3/epsilon) elementary updates.
The exact rational costs retain polynomial encoding length.

For an optimal feasible chunk set O, rounding loses at most N Delta.
The DP solution has rounded profit at least that of O and therefore
actual remaining value at least

$$
P^*-N\Delta
                  \ge(1-\epsilon)P^*.
$$

Adding the free chunks preserves the same multiplicative guarantee.
Compressing the chosen units of each type to its cheapest prefix gives
a genuine count vector, keeps its value and only lowers its cost.
The resulting algorithm has the two properties

$$
G_p(n)\le C,\qquad
 v\cdot n\ge(1-\epsilon)
         \max\{v\cdot a:G_p(a)\le C,\ 0\le a\le F_p\}.
 \tag{W6}
$$

Thus the cost budget is satisfied exactly; only the objective value
is approximated. No iteration depends on the magnitude of F_pj.

## 4. Strict dual inequalities are handled on an exact rational grid

A dual column violation for player p asks whether there is a
configuration with value at least T and G_p(n)<w_p, where the player
threshold w_p is rational and may be nonpositive. If w_p<=0, no such
configuration exists because G_p>=0.

For w_p>0, choose a common integer denominator D for every rational
cost coefficient in (W4). Its bit length is at most the sum of their
denominator bit lengths. Every integer configuration cost belongs to
the grid (1/D)Z. Set

$$
C_p={\lceil Dw_p\rceil-1\over D}.
 \tag{W7}
$$

This is the largest attainable cost-grid point strictly below w_p.
Apply (W6) at budget C_p. If its returned value is at least
(1-epsilon)T, return that configuration. Its value and cost satisfy

$$
v\cdot n\ge(1-\epsilon)T,
                     \qquad G_p(n)<w_p.
 \tag{W8}
$$

If its value is smaller, there is no configuration of value at least T
with G_p(n)<w_p. Otherwise such a configuration would be feasible for
budget C_p and the approximation guarantee would force the returned
value to reach (1-epsilon)T.

This is a complete weak pricing oracle: it either proves that no
target-T column violates the dual condition, or returns a genuinely
violated column at target (1-epsilon)T. It never mistakes equality of
cost and threshold for strict violation. All comparisons use rational
arithmetic with the paid encoding lengths.

## 5. A finite-row Farkas formulation

Let L be the number of explicit rows, and write the target-T LP as

$$
A_T\mu\le b,\qquad\mu\ge0.
 \tag{W9}
$$

All columns and b have integer entries bounded in absolute value by
some B>=1 of polynomial encoding length. The only negative row
coefficients and right side needed in our presentation are the total
mass row (W3). By Farkas' lemma, (W9) is infeasible exactly when there
is a nonnegative vector beta with

$$
\beta^T A_T\ge0,\qquad \beta^T b\le-1.
 \tag{W10}
$$

Scaling normalizes a strictly negative certificate to beta^T b=-1.
A basic feasible certificate is defined by at most L independent
active equations with integer coefficients bounded by B. Cramer's
rule therefore gives a uniform upper bound

$$
0\le\beta_i\le U_0=(LB+1)^{L+1}.
 \tag{W11}
$$

The generous displayed bound suffices; its bit length is polynomial
in L and log B. The same bound applies to **every subset of configuration
columns**, and to every target, since their coefficient bounds are
the same. This uniformity is needed for primal extraction below.

For a configuration column belonging to p, the inequality
beta^T A_(p,n)>=0 has exactly the form G_p(n)>=w_p. Nonnegative
resource-row multipliers give the convex costs (W4). Player-subset
row multipliers give a configuration-independent nonnegative sum;
the multiplier of (W3) is subtracted from that sum. Moving the latter
terms to the other side produces rational w_p, with no negative
resource cost coefficient.

## 6. Certifying weak feasibility and extracting a primal point

### 6.1. A uniform interior ball for every infeasible finite primal

Let theta have every coordinate equal to one, except that its
coordinate for the player upper-total row S=P is two. For every
configuration column A_(p,n),

$$
\theta^T A_{(p,n)}\ge 2-1=1,
             \qquad \theta^T b\le(L+1)B.
 \tag{W14}
$$

Indeed, the lower-total row is the only negative column entry, and
all other entries are nonnegative. This observation holds for every
configuration, without regard to its value or target.

Consider any finite collection H of allowed configuration columns
whose finite primal A_H mu<=b, mu>=0 is infeasible. By Section 5 there
is beta_0>=0 with beta_0^T A_H>=0, beta_0^T b=-1 and beta_0<=U_0.
Set

$$
\gamma={1\over4(L+1)B},\qquad
 \beta_* =2\beta_0+\gamma\theta,\qquad
 \delta={\gamma\over2LB}.
 \tag{W15}
$$

The point beta_* has slack at least gamma in each column inequality
and in each coordinate lower bound. Its normalization obeys
beta_*^T b<=-7/4, so its slack from the inequality beta^T b<=-1 is
at least 3/4. Since U_0>=1 and gamma theta_i<=1/2, each coordinate
has slack at least U_0 from the upper bound 4U_0.

Every column coefficient vector and b has Euclidean norm at most
LB. Consequently the entire Euclidean ball of radius delta about
beta_* is contained in

$$
K_H=\{\beta:0\le\beta\le4U_0,\quad
              \beta^T b\le-1,\quad\beta^T A_H\ge0\}.
 \tag{W16}
$$

For column and normalization rows, moving by delta changes a row
value by at most LB delta=gamma/2. Coordinate bounds have still
more slack. The radius bound is uniform over every finite column
set H. Its logarithm, and the logarithm of 4U_0, are polynomial in
L and log B.

### 6.2. Ellipsoid cuts and finite primal extraction

Run the ordinary rational ellipsoid method in L dimensions, initially
inside a ball of radius R=4LU_0 containing the box [0,4U_0]^L. The
system searched is the Farkas system for the **weaker** target
T'=(1-epsilon)T, with this enlarged box and beta^T b<=-1. Explicit
bound or normalization violations are separated directly. At a
remaining query point, apply Section 4 to each player:

* If a violated T'-configuration column is returned, use its exact
  inequality as a separating cut and retain that column.
* If every player is certified to have no violated target-T column,
  the current beta satisfies (W10) for T. Return a valid certificate
  that the target-T relaxation is infeasible.

Every cut in the first case is valid for the weaker-target Farkas
system. Retain each returned T'-configuration column. The maintained
ellipsoid contains K_H for the current set H of retained columns:
the explicit rows always define K_H, and every generated cut comes
from one of its column inequalities. Standard rational rounding of
the ellipsoid updates preserves containment and the usual polynomial
volume-reduction bound.

If no hard-target infeasibility certificate has been returned, stop
after enough cuts that the ellipsoid has volume strictly smaller
than that of an L-dimensional ball of radius delta. The number of
iterations is polynomial in L and log(R/delta). If the finite primal
using the retained columns H were infeasible, Section 6.1 would put
a delta-ball inside K_H and hence inside the maintained ellipsoid.
That contradicts the volume bound. The finite primal is therefore
feasible, even though no exact lower-dimensional feasibility oracle
has been invoked. Solve it by an ordinary rational LP algorithm to
obtain explicit
configuration weights satisfying **all original enumerated rows**.
Every retained column has value at least T'.

The procedure therefore returns one of two correct outcomes:

$$
\boxed{\begin{array}{l}
 \text{the target-T residual configuration LP is infeasible, or}\\
 \text{an explicit feasible point for target }(1-\epsilon)T.
 \end{array}}
 \tag{W12}
$$

The algorithm is allowed to return either outcome when both are true.
It does not certify infeasibility merely because the hard target is
not represented among its generated columns. The uniform Farkas
bound and the positive column direction (W14) make the weak-column
primal extraction sound. In particular, the proof does not assume
that an arbitrary Farkas polyhedron has an interior ball: the ball
has been constructed for this constraint matrix.

## 7. Runtime, output size and approximate optimization

The explicit row count is L=O((t+1)2^q). The rational ellipsoid uses
a number of iterations polynomial in L and the coefficient bit bounds.
Every queried price has polynomially bounded encoding length in those
parameters. Its hinge description has polynomial size in L and H,
and the binary-chunk knapsack routine is polynomial in that description
and epsilon^(-1). Hence the total weak-feasibility cost is (W1).
The produced fractional point uses only polynomially many generated
columns in L and H and has the same single-exponential output bound.

Let OPT_LP be the optimum target of the full subset-cut relaxation.
For positive rank, it is at most V=sum_j v_j f_j(P). All configuration
values lie on the common rational unit-value grid, and OPT_LP lies
on that grid because the finite configuration families change only
at those values. Start target search at zero, with its explicit empty-
bundle basis point, and at an upper grid point greater than
V/(1-epsilon). The latter cannot return a feasible weak target, so it
supplies a sound failed endpoint.

At every intermediate target use (W12), save any returned weak feasible
point as a success, and treat only the hard-target infeasibility outcome
as a failure. Failures are sound for the original target LP. At adjacent
grid endpoints, the successful trial target is at least OPT_LP, even
though success need not mean feasibility of that trial's hard target.
Its saved point therefore has value at least

$$
(1-\epsilon)\mathrm{OPT}_{LP}.
 \tag{W13}
$$

The number of trials is polynomial in the value encoding. This proves
the claimed single-exponential approximate optimizer for the strengthened
LP. It is a fractional computation. Applying the separate rounding/
search theorem still incurs its stated allocation approximation factor.

## 8. Limitations and classical primitives

The same runtime and pricing proof also apply if any explicitly
specified subfamily of resource subset cuts is retained, provided
that all aggregate resource inequalities y_.j(S)<=f_j(S) are then
included explicitly. Those aggregate rows ensure a valid resource
relaxation and contribute only the nonnegative linear terms already
allowed in (W4). The row count remains O((t+1)2^q), and the sign
structure used in Section 6 is unchanged. This includes the weaker
bounded-support relaxation needed by the rank-r allocation proof.

The exponent in this note is in q, the total number of potential
players. Enumerating only bounded-support resource cuts does not by
itself yield a q^{O(r)} complete LP optimizer: the player-base and
aggregate resource interfaces need an additional implicit-row argument.
That separate argument is now proved in
[residual-configuration-bounded-support-xp-solver.md](residual-configuration-bounded-support-xp-solver.md), using greedy
aggregate vertices, signed pricing and a finite mixed-primal extraction.

The player local family must be a coordinate box. General downward-
closed families supplied only through the original common-value
available-count oracle need not admit the convex-cost pricing scheme.
Additional local matroids, knapsacks or other restrictions are not
silently included. Capacities remain binary throughout; only their
logarithms enter segment splitting.

The profit-scaling dynamic program is a standard knapsack technique;
see Lawler, [*Fast Approximation Algorithms for Knapsack Problems*,
Mathematics of Operations Research 4(4), 1979](https://pubsonline.informs.org/doi/10.1287/moor.4.4.339).
The rational ellipsoid method and its volume bounds are classical;
see Groetschel, Lovasz and Schrijver,
[*The ellipsoid method and its consequences in combinatorial optimization*,
Combinatorica 1, 1981](https://ir.cwi.nl/pub/10046/10046D.pdf). Only the
ordinary bounded, positive-interior-radius volume argument is needed
here. The present note supplies the particular convex pricing
reduction, exact strict-cost grid, hard/weak target direction,
uniform Farkas bound and interior-ball construction needed here.
No claim is made that these classical primitives themselves are new.

The full derivation has passed root and independent mathematical reviews;
the interior-ball argument was supplied and independently checked
during those reviews.
No implementation, formal verification, external peer review, or
exhaustive publication-priority determination is claimed.
