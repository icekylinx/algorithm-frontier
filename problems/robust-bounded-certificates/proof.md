# Robust unit allocation with bounded minimal infeasibility certificates

The general robust unit model has a difficult positivity gate: selecting
one common player basis that can receive even one integer unit in every
scenario is already a Hitting Set obstruction. This manuscript supplies a
precise structural condition under which that gate becomes solvable.
It then restores an exact multiplicative approximation, including
optimum one, by combining the gate with the accepted positive-quota
algorithm.

The condition concerns minimal infeasible sets of recipients for
**aggregate, budget-feasible one-unit service in a scenario**. It is
preserved under every allowed-player restriction. A width violation
is an explicit separate outcome, rather than an unsound declaration
that no robust basis exists.

## 1. Model, certificate width, and main statement

Use the robust model of
robust_unit_allocation_additive_and_promised_two.md. An original player
matroid M has rank r>=1 on an explicit set P of q nonloop players, and
c=q-r. A single actual M-basis I must be chosen for all scenarios. The
scenario list Omega is explicit and nonempty. In scenario omega, type j
has an integral recipient-polymatroid rank f_(omega,j), nonnegative
rational assignment costs a_(omega,p,j), and one nonnegative rational
budget C_omega. Every retained allocated unit has the same value u>0.
Allocations may depend on the scenario; unused units are permitted.

Zero-valued or ineligible pairs are masked out before the construction.
Player-matroid loops can also be removed: no selected basis contains
them, and counts assigned there can be discarded without increasing
cost. All subsequent restrictions retain the original masked resource
constraints and budgets. They do not contract resources.

For C subseteq P define

$$
C\in\mathcal F_\omega
 \quad\Longleftrightarrow\quad
 \text{scenario omega has an integer allocation giving exactly one
 unit to each p in C, at total cost at most }C_\omega.
 \tag{BW1}
$$

Counts outside C can be set to zero. Each family F_omega is hereditary
and contains the empty set. Indeed, discard the units belonging to
removed recipients; the remaining vector stays in each polymatroid and
its nonnegative cost does not increase.

For a supplied integer w>=1, the **unit-certificate width condition** is

$$
\text{every inclusion-minimal set }
 C\notin\mathcal F_\omega
 \text{ has }|C|\le w,\qquad\text{for every }\omega.
 \tag{BW2}
$$

It is enough to require BW2 for such C that are independent in M.
Every certificate generated below lies in an actual M-basis. The
stronger version BW2 is convenient for recognizing the concrete
models in Section 9.

Let K* be the robust integer optimum minimum unit count. For a fixed
integer d>=2 define

$$
R_d=\frac{d+1}{d-1},\qquad
 A_d=\Gamma(R_d)
     =\frac{R_d^{R_d}}{(R_d-1)^{R_d-1}},\qquad
 A=\max\{w,A_d\}.
 \tag{BW3}
$$

**Theorem BW.** Under BW2, a deterministic polynomial-space algorithm
returns an actual common M-basis and legal integer allocations in all
scenarios, preserving each scenario budget exactly, with robust minimum
count at least

$$
\left\lceil K^*/d\right\rceil.
 \tag{BW4}
$$

Its running time is either

$$
A^c\mathrm{poly}(H)
 \tag{BW5}
$$

or

$$
(2-1/A)^q\,
 2^{O(q\log\log(q+2)/\log(q+2))}\mathrm{poly}(H).
 \tag{BW6}
$$

Here H includes the explicit scenario list, original binary numerical
data, matroid/rank oracle descriptions, and the paid polynomial
intersection and LP work. For fixed w,d, BW6 is
$(2-1/A)^{q+o(q)}\mathrm{poly}(H)$. In particular the utility
approximation is exactly d, without an additive unit loss.

The width-guarded implementation has these same time bounds on every
input. Outside BW2 it may instead return a specific scenario and an
inclusion-minimal infeasible set of size greater than w. Such an output
certifies violation of the stated structural condition; it is not
reported as robust allocation infeasibility. A successful allocation
and any fully exhausted infeasibility declaration remain sound even
when the width promise has not been supplied.

The empty-rank case is handled separately by returning the empty basis
and zero allocations with the chosen empty-objective convention. The
nonempty theorem assumes r>=1 so K* is a finite integer.

## 2. Exact polynomial unit tests for a prescribed set

Fix a scenario omega and C subseteq P. For each type j, use its
Boolean-cap matroid on eligible owners:

$$
\mathcal I_{\omega,j}^{\,1}
   =\{S\subseteq C:\mathbf 1_S\in P(f_{\omega,j})\}.
 \tag{BW7}
$$

This is a matroid: intersecting an integral polymatroid with the unit
box produces a matroid independence polytope. Its rank, if needed, is

$$
\rho_{\omega,j}(S)
   =\min_{T\subseteq S}
           \bigl[f_{\omega,j}(T)+|S\setminus T|\bigr].
 \tag{BW8}
$$

Rank or independence evaluation uses polynomial submodular minimization
with original binary rank values. There is no expansion into individual
resource units.

Use the explicit eligible type-player pair ground. One matroid is the
direct sum of the type matroids in BW7; the other is the partition
matroid with capacity one for every owner p in C. A common independent
set of cardinality |C| covers every owner exactly once. Give pair (p,j)
its actual cost a_(omega,p,j) and find a minimum-cost common independent
set of that cardinality.

If no such set exists, C is unit-infeasible. If one exists, C belongs
to F_omega exactly when its minimum cost is at most C_omega. This is
an exact polynomial test with an actual integer allocation at every
success. The pair ground has at most q times the number of scenario
types elements. Binary supplies and large budgets do not enlarge it.

Any positive integer allocation on C can be reduced to one unit per
player, choosing one originally assigned type at each player and
discarding all other units. Hence the test also correctly detects
whether C can receive at least one unit each.

The budget is handled by minimizing cost on the integral common-set
family. No claim is made that adding a budget inequality preserves
polytope integrality.

## 3. Extracting a minimal failed unit certificate

Suppose the test rejects a set I. Initialize C=I. Scan its players in
any fixed order; when p is still present, test C minus p and delete p
if that smaller set is still infeasible. This uses at most |I| exact
tests.

The final C is nonempty, because the empty set is feasible. It is
infeasible by construction. If p was retained when examined, the
then-current C minus p was feasible. Later deletions only make that
set smaller, so heredity implies that the final C minus p is feasible.
Thus every single deletion makes the final C feasible. Heredity then
shows that every proper subset is feasible, proving inclusion-minimality.

The certificate can be checked by rerunning the exact unit test on C
and on each C minus p. Feasible deletion witnesses can also be retained.
This has polynomial encoding and verification work in the original
oracle model.

In particular, the certificate is minimal for the original F_omega,
not merely for a differently restricted resource system. This is why
BW2 applies at every recursive node and every forced-omission seed.

## 4. The exact robust one-unit extension algorithm

For an allowed set Q subseteq P, retain the original required rank r
and put h=|Q|-r. If h<0, fail immediately. Otherwise proceed as follows.

1. Use matroid restriction to find an actual M-basis I_Q contained in Q.
   If rank_M(Q)<r, fail.
2. Test I_Q in every F_omega using Section 2. If every test succeeds,
   return that same I_Q and its actual unit allocation in each scenario.
3. Choose a failed scenario and use Section 3 to obtain a minimal
   infeasible set C contained in I_Q.
4. If |C|>w, return the separate outcome **WIDTH VIOLATION**, with omega
   and C. This outcome may be propagated immediately to the top level.
5. If h=0, fail. Otherwise branch on every p in C, recursively allowing
   Q minus p, and return any successful child. A width violation is
   propagated; if all children fail, fail.

Every success is an actual legal robust unit solution. The width guard
never occurs on an instance satisfying BW2, because C is a minimal
infeasible set and, in fact, is independent in M.

For completeness, let I* subseteq Q be any robust unit-feasible
M-basis. It cannot contain C: heredity would make C feasible in the
failed scenario. Therefore

$$
C\setminus I^*\ne\varnothing.
 \tag{BW9}
$$

For some p in this difference, the child Q minus p retains the entire
same I*. Its player rank is still r. Follow that child; after at most h
deletions a success must occur. If h=0, Q itself is the only possible
r-element basis, so a failed scenario on I_Q=Q correctly implies failure.

This argument proves exact one-unit feasibility or infeasibility on
the width class, rather than a positive-gap promise. It also proves
that a fully exhausted failure is sound on arbitrary inputs: whenever
a larger certificate would prevent the bounded branching, the procedure
returns width violation instead of false failure.

## 5. Complete running time, forced omissions, and global conversion

At residual deficit h, each nonterminal node has at most w children
and each child reduces h by one. Count every attempted child, including
one rejected immediately by its rank test. If N(h) is the maximum
number of such nodes, then

$$
N(0)\le1,\qquad N(h)\le1+wN(h-1),\qquad
 N(h)\le\sum_{i=0}^h w^i\le(h+1)w^h.
 \tag{BW10}
$$

Shrinking, all scenario tests, rank tests and certificate reconstruction
cost polynomial time at a node. The width guard enforces this bound
even on inputs outside the promised class. The polynomial factor is
uniform over nodes and forced seeds. Depth-first traversal stores only
O(q) polynomial-size node records, so space is polynomial.

Starting with forced omissions Z, |Z|<=c, means Q=P minus Z and
h=c-|Z|. The original ranks, costs, budgets and required player rank
stay fixed. Any original robust unit basis avoiding Z survives, and
the time is

$$
w^{\,c-|Z|}\mathrm{poly}(H).
 \tag{BW11}
$$

For w>1 the streamed inclusion-cover construction from
polynomial_space_global_gap_conversion.md applies with both full
and output quota equal to one. It gives exact robust unit feasibility
in

$$
(2-1/w)^q
 2^{O(q\log\log(q+2)/\log(q+2))}\mathrm{poly}(H).
 \tag{BW12}
$$

The wrapper propagates width violation as a separate outcome. It must
not count such a call as an ordinary failed seed. On valid width
instances no seed can trigger it, including seeds that omit part of
every robust unit solution. This supplies the required all-input
extension bound and the unpromised-seed semantics.

If w=1, BW10 is already polynomial; no A>1 conversion is invoked for
that gate. Also, C always lies in an r-element basis, so the supplied
width can be replaced by min(w,r). Its numerical value does not cause
a loop with more than q actual branch choices.

## 6. Positive integer quotas and exact scenario recovery

Compute the exact robust unit gate once. If it fails, K*=0, since any
positive robust integer solution could be trimmed to one unit per
selected player in every scenario. Return any M-basis and zero
allocations. If the gate succeeds, retain its unit witness.

For every nominal target 1<=K<=d, that saved witness is a legal weak
success with count ceil(K/d)=1. A full K-unit solution is not asserted.

For K>=d+1, set b=ceil(K/d). Let U_omega be the downward fractional
count-service region of scenario omega, including all its original
resource constraints and its one assignment budget. Query the fixed
intersection

$$
U=\bigcap_{\omega\in\Omega}U_\omega.
 \tag{BW13}
$$

Each scenario has the exact nonnegative packing separator from
one_value_exact_budget_corank_two_allocation.md. Test all scenarios;
a rejected scenario supplies a row valid for the intersection, and
acceptance supplies a separate fractional witness for each scenario.
The explicit scenario list is part of H. This introduces no common
allocation across scenarios.

The quota calculation is

$$
\frac{K}{K-\lceil K/d\rceil}
                         \le\frac{d+1}{d-1}=R_d.
 \tag{BW14}
$$

For clarity, write K=jd+s with j>=1 and 1<=s<=d. Then b=j+1 and
the left side is (jd+s)/(j(d-1)+s-1). It decreases as s increases,
and at s=1 is d/(d-1)+1/[j(d-1)], maximized at j=1.
Thus K>b and the weighted prefix-free gap is valid.

A full robust integer K solution yields one actual M-basis I* with
K times its incidence vector in U. The accepted weighted gap therefore
returns an actual basis I with b times its incidence vector in U, or
soundly excludes every full K basis. Its time on every forced seed Z
is at most A_d^(c-|Z|) times polynomial work, including inputs without
a full witness.

At success fix I once. In each scenario separately, discard counts
outside I and trim every selected total to exactly b. On the product
ground of that scenario's types and the selected players, intersect
the direct sum of its recipient polymatroids with the player partition
polymatroid of capacity b. The trimmed fractional vector has total br,
the maximum possible total. The full-total face is integral.

Minimize the scenario's actual assignment cost on this face and choose
an integral minimizer. Its cost is no larger than that of the fractional
witness, and every selected player receives exactly b units. Repeat for
each scenario, keeping I unchanged. This gives exact quotas and exact
scenario budgets without any additive rounding loss.

The separate integer recoveries are legitimate because the allocations
are adaptive scenario decisions. The argument does not preserve several
arbitrary cost inequalities on one common integer allocation.

## 7. Integer optimization, the combined bases, and bit complexity

A sound integer upper bound is

$$
U_0=\min_{\omega\in\Omega}
                \left\lfloor\frac{\sum_j f_{\omega,j}(P)}{r}
                \right\rfloor.
 \tag{BW15}
$$

After unit-gate success, use lower nominal target L=0 with a legal zero
allocation, external upper target U_0+1, and binary integer search.
Targets K<=d use the saved unit witness; larger targets use Section 6.
Save the actual allocation on every weak success and raise L to K;
on failure lower the upper target to K.

Every failure excludes a full K-unit robust solution. Hence the upper
target remains strictly greater than K*, independent of whether weak
successes are monotone. At adjacent endpoints the saved nominal L is
at least K*. Every positive success supplies ceil(L/d), so the best
saved actual allocation, including the unit witness, has at least
ceil(K*/d). If U_0=0, only zero is possible; if U_0<=d, the unit witness
already gives the desired result.

The number of search calls is polynomial in the binary length of U_0.
All intersections use explicit type-player coordinates, and all ranks,
costs, quotas, bounds, and separating rows have polynomial bit length
in the existing exact-oracle model. No unary resource expansion occurs.

The local time is the sum of the one-time unit gate and the positive
quota searches:

$$
\bigl(w^c+A_d^c\bigr)\mathrm{poly}(H)
                    \le 2A^c\mathrm{poly}(H).
 \tag{BW16}
$$

Apply the global wrapper separately to the unit gate and each positive
quota gap. Since the map a to 2-1/a is increasing, their sum is bounded
by BW6. When w=1 the unit gate is polynomial and A=A_d>1 still controls
the positive-quota calls. Thus no A=1 misuse is hidden in the statement.

For fixed d, A_d is a fixed algebraic number with exact constant-degree
comparisons; the block wrapper can compare the relevant integer powers
as in the quota-tradeoff manuscript. A variable integer w can be clipped
to r and compared exactly with this fixed A_d. The explicit BW6 bound
continues to hold, while a uniform base bounded away from two requires
a bound on w.

If d is instead a binary input, BW4 and the local analytic bound remain
valid without computing Gamma or iterating d times. For an elementary
uniform rational global implementation one may replace A_d by 3R_d,
obtaining A=max(w,3R_d). The sharper fixed-d bases are not claimed to
require manipulation of degree proportional to a binary-large d.

## 8. Exact factor two and coarser tradeoffs

At d=2, R_d=3 and A_d=27/4. Consequently every fixed width
w<=6 retains

$$
(27/4)^c\mathrm{poly}(H)
 \quad\text{and}\quad
 (50/27)^{q+o(q)}\mathrm{poly}(H)
$$

for exact factor two, including K*=1. For wider certificates use
A=max(w,27/4) explicitly.

At d=3, R_d=2 and A_d=4. Every fixed width w<=4 therefore permits
exact factor three in 4^c polynomial time, or
(7/4)^(q+o(q)) polynomial time and polynomial space.

Increasing d decreases the high-quota base A_d. The one-unit gate
eventually becomes the limiting term when w>A_d. The correct combined
base is the maximum in BW3, not a product: the expensive gate is solved
once, and its successful allocation is reused for all small targets.

If the original aggregate recipient capacity at every player is at
most one in at least one scenario, then K* is at most one. In that
case the exact unit gate alone optimizes the entire robust problem,
and BW10/BW12 are sharper than the combined approximation bound.

## 9. Concrete structural models and their limits

### 9.1 Zero-cost scenarios and aggregate unit matroids

If all assignment costs are zero (or the unit budget is redundant), a
set belongs to F_omega exactly when it can be partitioned among the
type Boolean-cap matroids in BW7. Therefore F_omega is the independence
family of their matroid union N_omega. Minimal unit-infeasible sets
are exactly the circuits of this **aggregate one-unit matroid**.

The condition that every circuit of N_omega has size at most w,
for every scenario, is thus a sufficient and exact interpretation of
BW2 in this case. The polynomial unit test supplies its independence
oracle without materializing the union.

The condition is not implied by bounding circuits of each individual
resource. For example, m resource matroids each equal to U_(1,n) have
only two-element circuits, but their union is U_(m,n), whose circuits
have size m+1 when n>m. Similarly, arbitrary assignment budgets must
be incorporated into F_omega before its minimal certificates are
bounded. An unbudgeted circuit bound alone does not control a costly
minimal unit cover.

### 9.2 Genuine Boolean graph-conflict scenarios

Suppose each scenario has one Boolean partition-matroid resource with
capacity one in each nonloop parallel class, with zero assignment
costs. Its minimal infeasible sets are loops and pairs in the same
class. Across scenarios, let F contain the loop-forced players and
let G contain an edge for every incompatible pair.

A common M-basis I is unit-feasible exactly when it avoids F and
contains no edge of G. Equivalently its complement D=P minus I is
an M*-basis that contains F and covers every edge of G. Branching on
a violated pair is precisely the w=2 unit algorithm, with rank tests
retaining the original player-basis condition.

Because the original resources in these scenarios are Boolean,
each player receives at most one unit. Hence K* belongs to {0,1},
and this specialization is solved **exactly**, not merely within
factor two, in

$$
2^c\mathrm{poly}(H)
 \quad\text{or}\quad
 (3/2)^q2^{O(q\log\log(q+2)/\log(q+2))}
       \mathrm{poly}(H),
$$

with polynomial space. Singleton loops are forced-deletion branches;
if deleting one destroys player rank, infeasibility is correctly
detected. This is a recognizable vertex-cover branching application,
and no priority or fastest-known claim is attached to these bases.

The graph condition concerns feasible recipient sets. It does not
assert that an arbitrary graph-independent-set family is itself one
matroid: the graph is the union of conflicts from several scenarios.

### 9.3 Partition pools with high quotas still possible

Take zero assignment costs, or budgets that are redundant for one-unit
service. For each scenario, partition P into pools B and let pool B have
integer capacity b_B>=0. One recipient polymatroid with rank

$$
f_\omega(S)
                     =\sum_{B:S\cap B\ne\varnothing}b_B
$$

allows exactly the count constraints x(B)<=b_B. It is a sum of
submodular coverage terms, hence is an integral polymatroid. Its
one-unit matroid is the partition matroid with block rank
min(b_B,|B|).

Every minimal unit-infeasible set is a (b_B+1)-set in one pool with
b_B<|B|. Thus BW2 holds if every pool is either nonbinding for one-unit
service, b_B>=|B|, or has b_B<=w-1. Nonbinding pools can have arbitrary
binary capacities; they may still constrain higher quotas. Different
scenarios may use different partitions.

This gives actual high-quota robust models to which the combined
factor-d theorem applies. It does not reduce every such instance to
the Boolean graph case.

### 9.4 A bounded-budget sufficient condition with modular unit prices

Suppose in a scenario every eligible unit at player p has the same
nonnegative integer cost a_p, independent of its type. Assume the
aggregate resource unit matroid has circuit size at most w_0 and
the scenario budget is an integer at most U. A set C is unit-feasible
exactly when it is independent in that aggregate matroid and
sum_(p in C) a_p is at most the budget.

A minimal infeasible C that is resource-dependent must itself be a
resource circuit: a contained circuit would otherwise be a smaller
infeasible subset. It has size at most w_0. If C is resource-independent,
it is a minimal budget cover. No member can have zero cost, and
removing any one member leaves cost at most U. The remaining |C|-1
positive integer prices sum to at least |C|-1, giving |C|<=U+1.
Consequently w=max(w_0,U+1) suffices.

This is a numerical structural condition, not a claim for arbitrary
type-dependent prices or arbitrary binary-large budgets. In particular
a small row width in an input description does not by itself bound
minimal infeasibility certificates after projection or resource union.

## 10. Relation to the robust obstruction and public baselines

The Hitting Set family in
robust_unit_allocation_corank_obstruction.md has one minimal failed
recipient set S in its corresponding scenario. Its width can grow with
the input. Bounding that width restores the familiar bounded-branching
mechanism instead of contradicting the unrestricted obstruction.

The conversion from an A^c extension algorithm to base 2-1/A is
established monotone-local-search background. The cited source is
Fomin, Gaspers, Lokshtanov and Saurabh, *Exact Algorithms via Monotone
Local Search*, Theorem 1.2; our accepted block-wrapper note provides
the particular deterministic polynomial-space construction used here:
https://sites.cs.ucsb.edu/~daniello/papers/monotoneLocalSearch19.pdf

For the graph specialization, Huang and Sellier's
*Matroid-Constrained Vertex Cover* studies maximizing covered edge
weight under a matroid independent-set constraint:
https://arxiv.org/abs/2306.04342
After preprocessing forced vertices, the present unit feasibility
equivalence is its all-edges-covered decision target with the dual
player matroid and an actual basis. Specifically, first test that the
forced set F is independent in M*, contract F there, and discard edges
already covered by F. Extending an independent cover in this contraction
to a basis preserves coverage, and adjoining F recovers a dual basis.
No improvement to that paper's approximation ratios or general graph
algorithms is inferred from this elementary correspondence.

The contribution of this manuscript is the complete bounded-certificate
interface for the budgeted robust allocation model, its guarded
all-input extension bound, and its coupling to exact integer-quota
recovery. No first-public-result claim is made.

---

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
