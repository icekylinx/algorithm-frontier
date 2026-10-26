# General resource matroids through all-subsets reservations

**25 October 2026. Explicit-subset construction; independent review passed.**

**Later development in this checkpoint:**
[general-resource-all-remaining-blockers.md](general-resource-all-remaining-blockers.md) maintains the universal
reservation invariant implicitly by conservative completion. It removes
the resource subset-enumeration factor for the main factor-five result.
The algorithm and sharper certificate in this note remain valid, but
their explicit enumeration is not a necessary cost or a lower bound.
The later [general-resource-relevant-blocker-addendum.md](general-resource-relevant-blocker-addendum.md) also recovers
the sharp compact coefficient with polynomial work per search state.

This note removes the laminar hypothesis on resource matroids by paying
an explicit exponential factor in a reservation width. Without a
resource-rank restriction, this is bounded by the selected-player
rank. The factor multiplies an already rank-exponential signature
bound, and therefore preserves a total 2^{O(r)} dependence. A sharper
resource-rank parameter also gives the mixed bound below; it is not
an unconditional general-resource quasipolynomial algorithm.

## 1. Model and claimed result

There is an arbitrary player-selection matroid M of rank r on an
explicit player ground set P. Every resource j has a common intrinsic
nonnegative rational value v_j and an arbitrary recipient matroid R_j
on P. A resource can be supplied at most once to a given player; its
whole receiving-player set must be independent in R_j. Liking
restrictions are encoded as loops. All matroids have independence
oracles, whose work is charged.

The output selects a basis of M and supplies each chosen player a
set of resources, maximizing the minimum common additive value.
Resources may serve several players when their own matroids permit
it. This is not a representation by independent physical item slots.
Let H denote the full explicit input size plus its numerical bit
length. The construction below gives

$$
\boxed{\text{factor }5-4/r\text{ in }
                        2^{O(r)}\mathrm{poly}(H)}
 \tag{G1}
$$

for r>=1. The oracle interpretation is explicit throughout. The
comparison can be strengthened to the natural configuration LP for
this same model. Rank zero gives the empty allocation; rank one is
exact. There is no unconditional general-resource quasipolynomial-time
claim. Section 7.1 gives the explicit resource-rank tradeoff.

Player-local downward-closed bundle families may also be supplied
with an exact available-bundle oracle. With a certified factor-lambda
available oracle, the corresponding factor is

$$
\lambda^{-1}+4-4/r,
 \tag{G2}
$$

with the oracle cost and parameters paid. The proof below first
uses unrestricted liked resource sets, then records this adapter.

## 2. The compact relaxation and resource availability

For target T use the relaxation

$$
\begin{split}
 &x\in P_{\mathcal B(M)},\qquad
       y_{\cdot j}\in P_{\mathcal I(R_j)}\quad\text{for each }j,\\
 &0\le y_{pj}\le x_p,\qquad
       \sum_j v_j y_{pj}\ge T x_p\quad\text{for each }p.
 \end{split}
 \tag{G3}
$$

No feasible point is required as input. All current allocated and
selected bundles are minimal above a chosen threshold B>0.

Retain the accepted player-side layer notation. The current matching
of bundles has owner set I, |I|=k<r. Its selected centers form X;
each center c has a disjoint group B(c) of current matching bundles
designated as its blockers. Thus Y is the disjoint union of these
groups. The group can be empty only during an immediately processed
free cascade. For resource j write

$$
X_j=\{p(c):c\in X,\ j\in c\},\qquad
 Y_j=\{p(b):b\in Y,\ j\in b\}.
 \tag{G4}
$$

In a last-layer scan, resource j is available to player p exactly when

$$
p\notin\mathrm{cl}_{R_j}(X_j\cup Y_j).
 \tag{G5}
$$

For an earlier layer its own prefix X_<=i,Y_<=i is used. All these
closures are on sets of at most 2r current names and can be computed
by greedy rank tests. A complete scan considers the player-side
eligible owners outside cl_M(I minus earlier blocker owners).
For a player, select available liked resources until value B is
reached, then prune to minimality. A failed scan says that every
eligible player's available total is strictly below B.

The nontrivial new issue is implementing a candidate without allowing
later exchanges to introduce hidden blockers of old centers. Equation
(G5) alone does not solve that issue. The following invariant does.

## 3. Reserve every actual subset of selected centers

For Z subseteq X let B(Z) be the union of their designated blocker
groups, and let X_j(Z) be their receiving-player set at j. Let M_j
be the current matching's receiving-player set at j. Maintain, for
every Z subseteq X and every resource j,

$$
Q_j(Z)=
  \bigl(M_j\setminus\mathrm{owners}(B(Z))\bigr)
                 \mathbin{\dot\cup} X_j(Z)
             \quad\text{independent in }R_j.
 \tag{G6}
$$

The dotted union requires distinct receiving names. Maintain the
stronger explicit invariant that different selected centers using j
have different owners and that X_j is disjoint from M_j. Thus (G6)
does not silently identify two services to the same player-resource
pair. It asserts simultaneous feasibility for every actual subset
of selected bundles after its own recorded blockers are removed.

There are at most 2^{|X|} subsets. They are enumerated explicitly;
the note does not compress this enumeration into an unproved oracle.
Each tested receiving set has O(r) names. The empty subset records
the feasibility of the current allocation itself.

Initially X is empty and the invariant holds. The next two sections
prove its preservation under all search operations.

## 4. Inserting a new blocked candidate

Let c have eligible owner p and a minimal set of resources selected
using (G5). We construct a new blocker group D, initially empty,
from current matching bundles outside Y.

For each Z subseteq X and each resource j in c, test

$$
\left[(M_j\setminus\mathrm{owners}(B(Z)\cup D))
                  \mathbin{\dot\cup}X_j(Z)\right]\cup\{p\}.
 \tag{G7}
$$

Only the matching portion loses the owners of D; selected services
are not deleted by a matching-owner name operation. The old tested
set before adjoining p is independent. If (G7) is
dependent, extract its fundamental circuit through p. This circuit
contains a receiver b belonging to a current matching bundle outside
Y and outside D. Indeed every other possible name belongs to X_j
or Y_j. If the circuit contained only those other names, it would
put p in cl_Rj(X_j union Y_j), contradicting (G5).

Add the matching bundle owned by b to D. Deleting b removes that
circuit; further deletions can never invalidate a previously passed
independence test. Continue through all subsets and resources. At
most k-|Y| bundles can be added. Fundamental circuits on O(r) names
are obtained by testing deletions, with polynomially many independence
queries per test.

Distinctness also holds. Equation (G5) excludes p from X_j and Y_j.
If p is already a current matching owner, player-side eligibility
forces its own matching bundle to belong to the earlier blocker
prefix. Therefore its old resources already put p in the corresponding
Y_j and are unavailable. For every new resource j, p is absent from
M_j as well. The new service is not a duplicate.

After these tests, setting B(c)=D proves (G6) for every new subset
Z union {c}; the old subsets are unchanged. If D is nonempty, append
c and its new blockers in the last layer. These blockers are disjoint
from every old group. If D is empty, c is a free candidate and is
processed immediately, without creating a stable unblocked center.

Each chosen blocker really receives some resource in c: it was chosen
from M_j during a test at j in c. This fact will be used in the sharp
value charge. A blocker is not required to be a physical intersection.

## 5. A free exchange preserves every retained reservation

Suppose c is free, either freshly constructed with D empty or stored
with its last designated blocker just removed. For a stored c, (G6)
applied to Z union {c} says that c is jointly feasible with every
subset Z of the other centers. For a fresh c this is precisely (G7).

The accepted player-side operation either augments I, or removes the
owner y of a matching bundle in the earliest permitted blocker layer
and inserts owner p(c). In the latter case truncate higher layers,
remove y from its one designated blocker group, and retain the lower
centers. If p(c) is already matched, the removed bundle is its own.
If p(c) is new but spanned, choose the earliest fundamental-circuit
blocker as in the accepted player-matroid construction.

Take any subset Z of retained centers and any resource j. Its new
reservation Q'_j(Z) is a subset of the old reservation for Z together
with c's service at j. Removing y only deletes a receiving element,
or removes a blocker that had already excluded that same element.
No other blocker group changes. If j is not in c, the new reservation
is simply a subset of the old one.

The old all-subsets invariant with Z union {c}, or the fresh tests,
therefore proves the independence and distinctness of Q'_j(Z).
The current matching itself is the case Z empty. The inserted bundle
creates no additional designated blocker of a retained center, and
the invariant guarantees that this bookkeeping remains valid.

Only the one center whose blocker group contained y can become free.
Process it immediately; each cascade exchange moves to an earlier
layer. This is the same finite cascade rule as the accepted algorithm.
The stronger X_j disjoint from M_j invariant also survives: a fresh
candidate's new resources exclude every retained occurrence of its
owner by (G5); a stored candidate has a distinct owner from the other
centers using each of its resources. Its old matching bundle, if
present, is removed. No retained service is identified with the new
matching service.

For every strictly lower retained layer, its selected bundles and
blocker bundles are unchanged. Consequently its resource closures in
(G5) are literally unchanged. The earliest player circuit also
preserves its player eligibility flat. Its completed availability
inequality survives verbatim. Only the last retained layer is
refreshed before another growth test.

This is the missing invariant in the failed single-circuit resource
transfer. Pairwise reservations alone would not establish (G6) for
all future combinations; the explicit subset enumeration is essential
to the present proof.

## 6. Rank cover and sharp value coefficient

At a completed layer, let J_0 be the player independent set after
removing earlier blockers and let w=r-|J_0|>0. If (G3) is feasible
and B<=T, a failed available-bundle scan requires excluded-resource
mass strictly larger than (T-B)w.

For resource j, every unavailable player belongs to
U_j=cl_Rj(X_j union Y_j). Its fractional receiving mass is at most

$$
y_{\cdot j}(U_j)\le r_{R_j}(U_j)
       =r_{R_j}(X_j\cup Y_j)\le |X_j|+|Y_j|.
 \tag{G8}
$$

After multiplying by v_j and summing, the excluded value is at most
the sum of selected-bundle values plus blocker-bundle values. Every
stable selected center has a nonempty, disjoint blocker group, so
|X|<=|Y|. The coarse bound is 2(B+u)|Y|, where u=max_j v_j
and u=0 on an empty resource set.

A sharper bound follows by grouping each center with its own
blockers. If a center is a singleton of value at least B, every
blocker receives that same resource. Minimality forces each such
blocker also to be a singleton. Their combined charge is at most
2u times the blocker count. If the center is not a singleton, all
its resources have value below B. Every blocker shares a resource
with it and therefore cannot be a singleton of value at least B.
Each bundle in this group has value below B+min{u,B}. Thus

$$
\text{excluded value}\le C_R(B,u)|Y|,\qquad
 C_R(B,u)=\max\{2u,\ 2B+2\min(u,B)\}.
 \tag{G9}
$$

The charge uses actual service occurrences. No false physical-item
intersection subtraction is made.

Put rho=(r-1)/r. With k<r and s earlier blockers, s/(r-k+s)<=rho.
An empty new layer is impossible for a feasible LP whenever

$$
B+\rho C_R(B,u)\le T.
 \tag{G10}
$$

Strictness of the lower LP bound makes equality valid. Every
nonterminal stable layer therefore has a new blocker.

## 7. Termination and the explicitly paid exponential factor

Use the accepted last-layer refresh, earliest-circuit exchange and
integer signature (-|X_1|,|Y_1|,...,infinity). A blocked insertion,
layer append or free exchange strictly decreases it with the same
truncation convention. Every transient state has O(r) selected
centers and at most r-1 distinct matching blockers; a fresh free
candidate is not stored. The previous integer-composition argument
bounds the number of charged states by 2^{O(r)} per phase.

One candidate's reservation tests cost at most 2^{O(r)} times a
polynomial in the full input, r and oracle costs. Availability scans,
circuits and minimality pruning have a polynomial multiplier. There
are at most r augmentation phases. Multiplying these costs still
gives 2^{O(r)} poly(H), not a doubly exponential bound. Subsets can
be enumerated one at a time, so the stored state is polynomial in
the input and r, plus the supplied oracle's workspace.

A positive growth margin reduces the number of layer signatures but
does not remove the subset tests. Laminar token reservations give a
separate compact implementation in their restricted resource class.

### 7.1 Resource-rank width of the required subset tests

For a fixed resource j, let X(j) be the selected centers using j.
It suffices to test subsets of X(j). Indeed, for any Z subseteq X,
put Z_j=Z intersect X(j). The selected receivers at j are the same
for Z and Z_j, while B(Z) contains B(Z_j). Hence

$$
Q_j(Z)\subseteq Q_j(Z_j).
 \tag{G13}
$$

Deletion of the new blocker group D preserves this inclusion. Thus
all the required new-center tests follow from at most 2^{|X(j)|}
tests at resource j. This is a proof of the full invariant, not a
replacement by a pairwise condition.

Equation (G6) for the whole selected set implies that X_j itself is
independent in R_j. Selected owners at j are distinct, so
|X(j)|=|X_j|<=r(R_j). Define kappa=max_j r(R_j). All subset work
per charged state is therefore at most
2^{min{r,kappa}} times a polynomial input and oracle multiplier.
The rank bound can be computed by greedy oracle calls or supplied
as a valid upper bound.

After the fat reduction, let tau=1/lambda (or one for an exact
oracle), rho=(r-1)/r, d=tau+4rho, B_0=T/d and B=T/(d+eta).
For small resources Cbar=2(B+B_0) bounds C_R(B,u). Its gap is

$$
T-\tau B-\rho\overline C
       =(\tau+2\rho)(B_0-B).
 \tag{G14}
$$

Since tau>=1>=rho, tau+2rho>=3d/5, and Cbar<=4T/d. Therefore
the gap divided by Cbar is at least
3 eta d/[20(d+eta)] >= 3 min{eta,1}/40. A completed layer
with at most gamma(r-k+|Y_<i|) new blockers contradicts its
strict rank-cover bound for gamma=min{eta,1}/64. This proves
the usual O((1+eta^-1)log(r+1)) layer-depth bound.

Consequently factor d+eta has the explicit mixed running time

$$
\mathrm{poly}(H,\text{oracle work})
 \min\left\{2^{O(r)},
  2^{\min\{r,\kappa\}}
     (r+1)^{O((1+\eta^{-1})\log(r+1))}\right\}.
 \tag{G15}
$$

The hidden rank-exponent constant is independent of lambda; its
oracle and parameter bits are paid. The first branch runs the exact
factor-d algorithm. The second branch charges every actual resource
subset test. In particular bounded or logarithmic resource rank
gives a quasipolynomial branch without assuming laminar or transversal
representations. For unrestricted kappa this remains exponential in
the worst case. The derived small-instance player rank and restricted
resource ranks only decrease.

## 8. Fat resources, arbitrary sizes and the configuration LP

For target T put d=1+4rho=5-4/r and B_0=T/d. A resource is fat
when v_j>=B_0. Let N be the union of the fat recipient matroids,
with singleton feasibility in a local bundle family also enforced
as a restriction. An independent set of N is exactly a set of
players that can each be assigned one fat resource, with each
resource's receiving set independent. The matroid union and a
decomposition into the individual resource matroids are polynomial
oracle operations, explicitly paid.

Use U=M* union N and run the small-resource construction on U*.
Its rank r' is at most r. Every small resource has value u<B_0,
so C_R(B_0,u)<=4B_0 and

$$
B_0+\rho_{r'}C_R(B_0,u)
                     \le(1+4\rho)B_0=T.
 \tag{G11}
$$

The dual-union complement argument and decomposition give a basis
of the original M, all of whose players receive value at least B_0.
Removing other players from a resource preserves independence.
When r'=0 the inner search is unnecessary. All derived dual and
union oracle costs are charged to the polynomial multiplier.

For clarity, the natural configuration relaxation has local feasible
configurations C of value at least T, variables z_pC, a player base
vector x_p=sum_C z_pC, and recipient marginals
y_pj=sum_{C containing j}z_pC in P_I(R_j). Choose one fat resource
from each fat-containing configuration. Its recipient vector f^j is
coordinatewise bounded by y_.j, hence is in P_I(R_j). Their sum f
has coordinates at most x<=1 and lies in P_I(N) by the matroid
union rank inequalities. Combine f with 1-x in P_B(M*) and extend
coordinatewise to a base vector of U. The complementary vector x'
is coordinatewise bounded by the all-small configuration mass.

Scale each player's all-small configuration marginals to mass x'_p.
Their resource columns only decrease, so remain in P_I(R_j);
their value is at least T x'_p and their individual coordinates are
at most x'_p. This proves feasibility of the inner small-resource
relaxation. It also preserves any supplied local downward-closed
perspective constraints. Thus (G1) compares against the configuration
LP without solving or enumerating it.

The feasible configuration thresholds belong to the finite common
rational value grid and are bounded. The established one-sided
target search applies: failure implies target infeasibility, while
success need not imply target feasibility. Use an upper target
exceeding d times the total possible utility
sum_j r(R_j)v_j. Its encoding length is polynomial. The final
guarantee does not assume monotone success decisions.

## 9. Local constraints and approximate available oracles

For a player-local downward-closed family, apply its oracle to the
set of resources satisfying (G5). Restricting each bundle in a
perspective decomposition to that set remains feasible. If a certified
factor-lambda oracle returns value below B on a fresh complete scan,
the true available optimum is below B/lambda. The strict cover becomes
(T-B/lambda)w, provided B<=lambda T.

Accordingly replace (G10) by

$$
B/\lambda+\rho C_R(B,u)\le T.
 \tag{G12}
$$

The exact fat threshold uses d=lambda^-1+4rho and B_0=T/d;
(G11) is unchanged after replacing B_0 by B_0/lambda in its
first term. A positive singleton feasibility test is exact with any
lambda>0 feasible oracle. The rank-exponential reservation count does
not depend on the approximation quality, except through the paid
oracle and numerical work. Exact rank-one optimization is asserted
only when lambda=1.

## 10. Scope and remaining work

The result includes arbitrary recipient matroids, arbitrary
player-selection matroids, and arbitrary intrinsic resource sizes.
It is a constant-quality, rank-exponential algorithm, with the mixed
resource-rank branch (G15). It is not a polynomial-time improvement
over the named public resource-matroid baseline or an unconditional
quasipolynomial theorem for general resource matroids. Recipient
polymatroids with repeated units per player are not silently included.

The next algorithmic gate is to test and maintain the all-subsets
reservation system faster, or to replace it by a weaker invariant
with the same exchange and rank-cover properties. Laminar tokens
provide one positive structured case. Merely checking one circuit,
individual centers, or pairs does not prove the full invariant used
here. The original general-graph maximum-matching exponent remains
unchanged by this allocation transfer.
