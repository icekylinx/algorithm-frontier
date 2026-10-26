# Matroid union removes the largest-item penalty

This manuscript combines the current-blocker allocation algorithm with a
matroid-union reduction. The input may have arbitrary resource sizes.
The comparison is the integral optimum of the original player-basis
allocation problem, not its compact fractional LP at arbitrary item
sizes. The result applies to an arbitrary player matroid given by an
independence oracle; it does not require selecting every player.

The optional addendum [Configuration-LP comparison for the player-matroid union reduction](configuration-comparator.md)
strengthens the comparator to the configuration LP on the same
player matroid. Its separate proof requires neither a fractional
input nor enumeration of configurations; the algorithm below and
its paid oracle implementation are unchanged.

## 1. Model and result

There are q players, an arbitrary matroid M of rank r>=1 on them,
and indivisible resources with nonnegative rational intrinsic values.
A player values a resource at its intrinsic value if the explicit
liking incidence is present, and at zero otherwise. Select a basis
of M and disjoint liked-resource bundles for its players. Maximize
the minimum value received by a selected player; call this optimum
OPT. Let P denote the explicit input volume and b the total rational
input bit length. Unit-time calls to the original independence oracle
are counted separately and obey the same asymptotic bound.

Put

$$
d_r=4-3/r,\qquad \theta_r=1/d_r=\frac r{4r-3}.
 \tag{U1}
$$

The deterministic construction gives:

* a basis allocation of value at least OPT/d_r in
  poly(P,b) times 2^{O(r)} time and oracle calls;
* for every positive rational eta, a basis allocation of value at
  least OPT/(d_r+eta) in

$$
\mathrm{poly}(P,b+\mathrm{bits}(\eta))
 \min\!\left\{2^{O(r)},
 (r+1)^{O((1+\eta^{-1})\log(r+1))}\right\}
 \tag{U2}
$$

time and oracle calls. Space is polynomial. For fixed eta this is
quasipolynomial in rank, with polynomial dependence on the explicit
input, and it is in particular a 4+eta guarantee for all ranks.
The exact factor d_r is strictly below four at every finite rank,
but approaches four as the rank grows. There is no fixed positive
constant improvement below four uniformly over unbounded ranks.

The rank-one case can also be solved directly by choosing the best
nonloop player and giving that player all liked resources. Rank zero
is returned as an empty basis without defining a minimum over an
empty selected set. Zero-valued items may be removed. The zero-OPT
case causes no difficulty.

The polynomial input factor in this wrapper is intentional. Derived
matroid union and duality queries have polynomial cost in q and in
the explicit fat-resource graph. They are not treated as unit-cost
original-oracle queries, and this wrapper does not retain the inner
algorithm's linear input multiplier.

## 2. Fat resources and the auxiliary player matroid

Fix a positive target T. A resource is fat if its value is at least
theta_r T, and small otherwise. Let N be the transversal matroid
on players in the bipartite graph joining them to liked fat resources.
Thus a player set is independent in N precisely when its players
can receive distinct fat resources.

Let M* be the dual of the original player matroid, and define

$$
U=M^*\vee N.                       \tag{U3}
$$

This is the ordinary matroid union on the player ground set. An
independent set of U has a disjoint decomposition D union F with
D independent in M* and F independent in N. A decomposition can
be computed, not merely tested for existence.

Run the current-blocker bundle allocation algorithm on U*, using
only small resources and target T in its compact relaxation. Let
r' be the rank of U*. Since the union contains all independent
sets of M*,

$$
r(U)\ge q-r,
 \qquad r'=q-r(U)\le r.                                    \tag{U4}
$$

Thus passing to the auxiliary matroid never increases the rank
parameter. If r'=0, there are no players needing small bundles.

## 3. Why an original optimum supplies the required small-instance promise

Assume there is a basis I of M with disjoint allocations of value
at least T. Its complement D=P_players minus I is a basis of M*.
Partition I into F, the players receiving at least one fat resource,
and S, the remaining players. Choose one allocated fat resource for
each player in F. These resources are distinct, so F is independent
in N.

The disjoint union D union F is therefore independent in U. Extend
it to a basis B of U. Its complement S'=P_players minus B is a
basis of U* and satisfies

$$
S'\subseteq S.                  \tag{U5}
$$

Every player in S' retains its original all-small bundle, still of
value at least T. Those bundles are disjoint. They give an integral
feasible point, hence a feasible point, of Q_{U*}(T).

This argument uses the original integral allocation only as an
existence witness. The algorithm is not given that allocation, a
configuration-LP solution, or a feasible fractional solution of the
auxiliary instance. Its inner failure certificate is sufficient:

$$
Q_{U^*}(T)\text{ infeasible}\quad\Longrightarrow\quad
                         \mathrm{OPT}<T.                   \tag{U6}
$$

No claim is made that an arbitrary feasible point of the original
compact Q_M(T), with unrestricted resource sizes, survives this
reduction. That stronger assertion would require additional work.

## 4. The rank-aware inner threshold

The general sharp-star lemma is proved separately in
[Sharper star charging and rank-sensitive quality for matroid allocation](../../manuscripts/allocation-and-scheduling/matroid-allocation-sharp-star-rank-quality.md). The special case
needed here also has the following short direct proof.

Use the same layers, earliest-circuit exchanges, free-center cascades
and integer signatures as in the main allocation theorem, for an
arbitrary positive bundle threshold B<=T. Let a completed maximal
layer have previous blocker count s, new blocker count y, and current
matching size k<r'. Put

$$
w=r'-k+s,\qquad \rho_r=(r-1)/r.
$$

Since s<=k<r'<=r,

$$
\frac{s}{w}\le\frac{r'-1}{r'}\le\rho_r.
 \tag{U7}
$$

Minimal bundles and current blocker ownership give

$$
v(F)\le(2B+u)(s+y),                       \tag{U8}
$$

where u is the largest small resource, with u=0 if none exist, and
u<theta_r T. The empty
cover is included in this weak form. Maximality and the compact
fractional rank constraints give the strict inequality

$$
v(F)>(T-B)w                              \tag{U9}
$$

whenever Q_{U*}(T) is feasible. Strictness follows because the
available value outside F is strictly below B for each eligible
player and the fractional mass of eligible players is at least w>=1.
This remains valid when B=T.

### 4.1 Exact rank factor

Set B=theta_r T and test completed layers for y>0. If y=0, then
(U7)--(U8) imply

$$
v(F)\le3\theta_r T\rho_r w=(T-B)w,
$$

using theta_r(1+3rho_r)=1. This contradicts (U9). Hence every
completed layer either has a blocker or supplies an infeasibility
certificate. The rank-bounded composition count proves termination
in 2^{O(r')} times a polynomial input factor. At r'=0 no inner
augmentation is needed. The r=1 boundary is also covered by the
strict inequality, or by the direct algorithm in Section 1.

For a certificate at this sharper boundary, verify the available
value inequalities and v(F)<=(T-B)(r'-|J_0|). A weak cover inequality
is enough because the LP lower bound is strict. The older main
theorem's stronger strict cover certificate is not assumed here.

### 4.2 Positive error and quasipolynomial time

Choose 0<epsilon<theta_r and use

$$
B=(\theta_r-\epsilon)T,
              \gamma=\epsilon/4.                           \tag{U10}
$$

Put A=2B+u. It satisfies

$$
A<3T,\qquad B+\rho_r A\le
            T-\epsilon(1+2\rho_r)T\le T-\epsilon T.
$$

If y<=gamma w, then v(F)<=A(rho_r+gamma)w, strictly less than
(T-B)w. Thus every passing completed layer has

$$
y>\gamma w\ge\gamma(1+s).            \tag{U11}
$$

Current growth, earliest-span preservation and last-layer refresh
give depth O(epsilon^{-1} log(r'+1)). Counting all micro-signatures
gives the quasipolynomial bound, and the independent composition
count still gives 2^{O(r')}. Every scan and cascade is paid as in
the inner theorem; only the numerical growth threshold changed.

For a requested ratio d_r+eta take

$$
\epsilon=\frac1{d_r}-\frac1{d_r+\eta}
          =\frac{\eta}{d_r(d_r+\eta)}.
 \tag{U12}
$$

Then B=T/(d_r+eta), while every fat resource has value at least
theta_r T>=B. Also epsilon^{-1}=O(1+eta^{-1}), proving (U2).

## 5. Recovering an original basis allocation

Suppose the inner algorithm returns a basis S'' of U* with disjoint
small allocations, each worth at least B. Its complement B'' is a
basis of U. Compute a disjoint matroid-union decomposition

$$
B''=D''\mathbin{\dot\cup}F'',\qquad
 D''\in\mathcal I(M^*),\quad F''\in\mathcal I(N).
$$

Find a matching of F'' to distinct liked fat resources, and allocate
those resources. Extend D'' to any basis D''' of M*. This extension
may use players of F'' or S''. Discard their allocations if it does.
The remaining player set

$$
I''=P_{\rm players}\setminus D'''
$$

is a basis of the original M and is contained in F'' union S''.
Every remaining player therefore already has either its small
bundle or its fat resource. Dropping some previously supplied
players cannot create any conflict or reduce another player's
value. Fat and small resources are disjoint by definition. Each
player in I'' receives value at least B.

It is not necessary that D'' was already a full dual basis, or that
the extension avoid all small players. The permitted deletion of
their allocations is precisely why this recovery is valid.

## 6. Oracles, rank computation and decomposition are paid

The only supplied oracle is for the original M. Its rank on any
subset can be computed by greedy independence queries. Dual rank
is obtained from

$$
r_{M^*}(X)=|X|+r_M(P_{\rm players}\setminus X)-r_M(P_{\rm players}).
$$

This implements dual independence queries in polynomial time.
Independence and rank in the fat-resource transversal matroid use
ordinary deterministic bipartite matching on the explicit incidence
graph. Standard matroid union/partition algorithms compute ranks,
maximum union-independent sets and their two-part decompositions
using polynomially many queries to those two matroids. The same
dual-rank formula implements queries to U*.

One may use a conservative polynomial implementation throughout.
All oracle substitutions, finding a fat matching, extending D''
to a dual basis, constructing query sets and rebuilding the fat
graph for a new target are charged. The resulting polynomial factor
is independent of r in its exponent. This is sufficient for a
rank-parameterized bound and for (U2); no unit-cost union oracle or
unreported free basis decomposition is assumed.

For a primary reference on explicit polynomial matroid partition
and oracle complexity, see Tatsuya Terao, *Faster Matroid Partition
Algorithms*, ICALP 2023:
<https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2023.104>.
The algorithmic use of union and duality is public. The quality
guarantee here comes from the current-blocker rounding and its
rank-aware analysis.

## 7. Finding the target without a feasibility oracle for OPT

All resource values lie on an explicitly computable rational grid
Delta=1/D, where D can be the least common multiple, or simply the
product, of their input denominators. Its bit length is at most
their total input bit length. Every integral bundle value and OPT
lie on this grid. Write V for the sum of all resource values.

For each positive target T on that grid, run the fixed-target
procedure above. A success returns a basis allocation of value at
least aT, where a=theta_r in the exact version and
a=1/(d_r+eta) in the approximate version. A failure implies OPT<T
by (U6). Success is not required to imply T<=OPT.

Initialize the lower target to zero with an arbitrary original
basis and empty allocations. Choose a grid upper target U0>V/a.
At that target no basis of positive rank can be supplied at value
aU0>V, so the procedure must fail. For the exact version 4V+Delta
is a sufficient choice. The upper target has polynomial bit length.

Perform ordinary integer binary search on grid indices. At a
success, replace the lower target and store its returned allocation.
At a failure, replace the upper target. The key invariant is
upper>OPT; it follows from failure soundness, even if the success
predicate is not monotone above OPT.

When the targets are adjacent grid points, the grid-valued OPT and
upper>OPT imply lower>=OPT. The stored successful allocation is
therefore worth at least a lower>=a OPT. If lower is still zero,
the same reasoning implies OPT=0 and the trivial allocation suffices.

The search uses polynomially many target trials in the numerical
encoding length and log P. Rebuilding the derived matroids on each
trial is included in the polynomial multiplier. This step needs
neither a numerical limit argument nor a monotone approximate
decision oracle that the algorithm has not actually supplied.

## 8. Public comparison and the boundary of this result

The configuration-LP addendum proves the same guarantee relative
to that relaxation's optimum, and shows that the public inner
theorem composed below has the same strengthened comparator. This
does not assert the corresponding claim for the unconditioned
compact Q_M(T) at unrestricted item sizes.

Davies--Rothvoss--Zhang v4, Theorem 2, prints the smaller-resource
guarantee (T-u)/5-epsilon T in polynomial time. Applying the same
matroid-union reduction with a threshold near T/6 gives a polynomial
6+eta consequence for the general player-basis problem relative to
integer OPT. This composed consequence is distinct from the paper's
printed ordinary-Santa-Claus theorem. The public comparison note
records the earlier one-third/four-factor history and the later
correction; it does not silently use a superseded version as current.

For ordinary restricted Santa Claus, all players must be supplied.
Cheng--Mao already give a polynomial 4+eta algorithm, and further
topological gap bounds are not automatically algorithms. The present
claim concerns arbitrary player-matroid basis selection and its rank
parameter. It does not assert a uniformly better-than-four ordinary
Santa Claus algorithm or a proved global priority claim.

The original unrestricted general-graph maximum-matching target is
separate. Nothing in this allocation reduction changes its accepted
four-fifths time exponent.

Primary comparison:
<https://arxiv.org/html/1807.07189v4>.

---

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
