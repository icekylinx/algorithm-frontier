# Unrelated-value allocation near two through a joint light/heavy LP

This theorem permits a resource type to be valuable to one player and
less valuable to another. Its units may consequently serve both light
and heavy roles. One joint original-resource LP handles those roles at
every omission node, and a single cost-preserving rounding preserves
at least one unit at each heavy player. No independent allocation of
two overlapping copies of the resource is performed.

For arbitrary nonnegative player-type values, arbitrary integral
recipient polymatroids, and one exact nonnegative assignment budget,
the result is a deterministic `(2+eta)` approximation in strictly
sub-two-base exponential time in the number of players. An optional
original player matroid is allowed by an exact dual-resource reduction
that leaves the player ground unchanged. For compulsory players with
pair values in `{0,u,a}`, the same joint treatment gives exact factor
two at whole-ground base `50/27`.

## 1. Model and the main theorem

There are q>=1 players P and m resource types. Type j has a normalized
monotone integral submodular rank f_j on P. Its allocated integer
count vector x_j lies in P(f_j). A unit assigned to player p has
nonnegative rational value v_pj and nonnegative rational cost c_pj.
There is one exact assignment budget

```math
\sum_{p,j}c_{pj}x_j(p)\le C,
                         \qquad C\ge0.
 \tag{J1}
```

Units may be left unused. Initially every player is compulsory, and
OPT is the maximum possible minimum utility over all players. The
extension to a genuine basis of an original player matroid is in
Section 10. Numerical ranks, values and costs are binary encoded; no
resource multiplicity is expanded into individual units. H includes
the explicit player-type data and the paid polynomial resource,
submodular-minimization and exact-LP oracle work.

Define, for R>1,

```math
\alpha=1-1/R,\qquad
       \Gamma(R)=\frac{R^R}{(R-1)^{R-1}},\qquad
       B(R)=2-1/\Gamma(R).
 \tag{J2}
```

**Theorem J.** For every fixed rational R>1, there is a deterministic
algorithm returning a legal integer allocation satisfying J1 and
having minimum utility at least

```math
\frac{\alpha}{2}\,\mathrm{OPT}
                  \quad\text{in time}\quad
 B(R)^q\,2^{O(q\log\log(q+2)/\log(q+2))}\mathrm{poly}(H),
 \tag{J3}
```

using polynomial workspace. The theorem holds for compulsory players
and for a genuine basis of an original player matroid, with q the
original nonloop player ground in the latter case.

For fixed rational eta>0 choose R=(2+eta)/eta. The factor is exactly
2+eta and the time is `B(R)^(q+o(q)) poly(H)`. Examples are factor four
at base 7/4, factor three at base 50/27, and factor five halves at base
5994/3125. These are whole-ground bounds without a small-corank,
heavy-support, intrinsic-value or price-diversity promise.

An additional conditional parameterized theorem follows from the same
proof. For compulsory players, if some integer optimum has at most K
recipients of units with value at least alpha*OPT/2, the guarantee in
J3 is obtained in `Gamma(R)^K poly(H)` time. For an original rank-r
player matroid, the corresponding sufficient running time is
`Gamma(R)^(q-r+K) poly(H)`. The support is evaluated in that optimum
at the specified near-half threshold. No original-corank-only claim
is made for arbitrary values.

## 2. Pair-value masks and safe preprocessing

Pairs with f_j({p})=0 cannot receive a positive count. Pairs with
v_pj=0 may also be set to count zero without changing an optimum:
discarding their counts preserves resource feasibility, does not
increase cost, and changes no utility. Retain all other pairs,
including pairs whose whole-unit cost exceeds C; fractional LP
comparators may use a fraction of such a unit.

If no eligible positive pair remains, zero counts are optimal and the
algorithm returns them directly, choosing any original player basis
when selection is optional. No minimum positive value or nonempty
threshold list is assumed in that case.

Choose a positive threshold theta and divide the remaining pairs into

```math
\mathcal L=\{(p,j):0<v_{pj}<\theta\},\qquad
        \mathcal H=\{(p,j):v_{pj}\ge\theta\}.
 \tag{J4}
```

Eligibility f_j({p})>=1 is implicit. The algorithm enumerates every
distinct mask induced by the finitely many positive pair values,
including the heavy-empty mask. Equality belongs to the heavy side.
Only the mask, not the numerical unknown optimum threshold, is used
by the algorithm.

Write u_L for the largest light-pair value, or zero if there is none;
write a_H for the smallest heavy-pair value, or infinity if there is
none. For the mask induced by theta*,

```math
u_L<\theta^*\le a_H.
 \tag{J5}
```

The same type j may have pairs in both classes. The original f_j
continues to govern all its allowed counts jointly.

## 3. The joint fractional region at an omission node

The current set Q consists of players still allowed to receive light
service. Every player outside Q is forced into a heavy role. Define

```math
A_j(Q)=\{p\in Q:(p,j)\in\mathcal L\}
           \ \cup\ \{p\notin Q:(p,j)\in\mathcal H\},
         \qquad f_j^Q(S)=f_j(S\cap A_j(Q)).
 \tag{J6}
```

These masked ranks are normalized monotone integral submodular
functions. Their independent vectors are exactly original-resource
independent vectors with zero counts on the forbidden pairs. In
particular, masking does not create two separate copies of a shared
type's capacity.

Let X_Q consist of the fractional vectors satisfying

```math
\begin{aligned}
        x_j&\in P(f_j^Q) &&(j=1,\ldots,m),\\
        \sum_j x_j(p)&=1 &&(p\notin Q),\\
        \sum_{p,j}c_{pj}x_j(p)&\le C.
 \end{aligned}
 \tag{J7}
```

Every forced heavy player receives exactly one fractional unit, all
on its allowed heavy pairs. For p in Q there is no count equality.
Define the normalized light service projection

```math
U_Q=\{z\in\mathbb R_+^Q:\exists x\in X_Q,\quad
                 z_p\le\sum_jv_{pj}x_j(p)\text{ for all }p\in Q\}.
 \tag{J8}
```

First test whether X_Q is empty. If it is, reject the node. This
feasibility check is necessary: forced heavy roles need not admit
any affordable joint assignment. If X_Q is nonempty, U_Q contains
zero, is compact and convex, and is downward in service. Decreasing
z preserves its witness. Counts at light players may also be dropped
without changing the heavy equalities or increasing cost.

The region changes with Q in both its masks and its forced equalities.
It need not be nested under deletion. The proof below uses a fixed
protected witness at every surviving node instead of claiming one
common region throughout the recursion.

## 4. Exact nonnegative separation and uniform bit bounds

All LPs involving X_Q have polynomial dimension. For each type,
submodular minimization separates P(f_j^Q); the heavy equalities and
the assignment budget are explicit. Exact rational LP therefore
checks feasibility, optimizes a linear objective, and reconstructs
a feasible queried service vector in polynomial oracle time.

For nonempty X_Q and a>=0 on Q, its service support is

```math
h_Q(a)=\max_{x\in X_Q}
                         \sum_{p\in Q,j}a_p v_{pj}x_j(p).
 \tag{J9}
```

The optimizing x can be chosen at a vertex by exact lexicographic
refinement, preserving the uniform polynomial-bit vertex bound used
by the outer separator. This support value is nonnegative because
U_Q contains zero. Let V be a uniform
upper bound on any original player's total possible utility, for
example `V=sum_j (max_p v_pj) f_j(P)`. For a queried z>=0, solve

```math
\max\{a\cdot z-h:\ a\ge0,\ a(Q)=1,\ 0\le h\le V,
           \ h\ge a\cdot u(x)\text{ for every }x\in X_Q\},
 \tag{J10}
```

where u(x) is its utility vector restricted to Q. Separation of the
last family is exactly the support LP J9. At an optimum h=h_Q(a).

If J10 has positive optimum, recompute h_Q(a) exactly and return the
strictly violated valid packing row `a*z<=h_Q(a)`, with a>=0. If its
optimum is nonpositive, z belongs to U_Q. Indeed, strong separation
of an external nonnegative z from a compact downward region allows
the negative coordinates of the normal to be replaced by zero;
downward closure preserves its support value, and z cannot decrease
the separating objective. Normalize the nonzero positive normal to
sum one, contradicting a nonpositive optimum in J10.

The last branch is **nonpositive**, not only zero: the normalized
support objective can be negative for a feasible interior query.
The Q-empty case is handled separately by the all-heavy unit gate,
so its simplex normalization is never requested.

All vertices of X_Q have a uniform polynomial-bit bound from exact
rational LP and Cramer's rule in its polynomial dimension. Its rank
inequality coefficients, numerical ranks, equality right sides one,
values and costs have polynomial encoding, uniformly over every mask
and Q. The support constraints in J10 consequently have uniform
polynomial-bit coefficients, and exact outer LP returns a
polynomial-bit row. Query targets also have polynomial encoding.
No enumeration of fractional resource units or numerical denominators
is required. This is the support-separation proof used in the
unrelated-value budget note, with the additional heavy equalities
retained inside the primal support LP.

## 5. The fixed-witness gap and its forced-omission interface

Fix an exact promised heavy cardinality k<q and put s=q-k. For
rational full target t>0 and output target b=alpha*t, a full witness
consists of an actual s-set I* and one fractional allocation x* such
that:

* every player in I* uses only light pairs and has utility at least t;
* every player in P\I* uses only heavy pairs and has total count one;
* all original resource inequalities and the single budget hold
  jointly for x*.

Start the gap on Q=P, or on P\Z for a forced omitted set Z of size
at most k. Require |Q|>=s. Test J7 for emptiness, then query b*1_Q
in J8. On membership, return Q and its actual joint fractional
witness. On nonmembership, use the nonnegative row from Section 4
and enumerate the weighted first-density-crossing omission
certificates with ratio R=t/(t-b). Recurse on the corresponding
smaller Q. Reject at zero remaining deficit if the weak query fails.

To prove completeness, fix one full witness I*,x* and suppose
I* is contained in Q. Retain x* on I* and on P\Q, and discard its
counts on Q\I*. The discarded players were heavy in the full
witness but are not forced heavy yet at this node. The retained
counts respect J6; every player outside Q still has exactly one
heavy unit; resource counts and cost only decrease. Thus

```math
t\,1_{I^*}\in U_Q.
 \tag{J11}
```

In particular the empty-X_Q gate cannot reject this protected node.
If a row a*z<=U is violated by b*1_Q, J11 gives

```math
t a(I^*)\le U<b a(Q),\qquad
              a(Q\setminus I^*)>\frac1R a(Q).
 \tag{J12}
```

The same layer-cake and first-density-crossing argument as in
[Single-exponential corank time for weighted packing through first-violation prefixes](../whole-ground-allocation/selection.md) supplies an enumerated
certificate contained in Q\I*. Its deletion preserves I*, so
J11 holds again for the new masks and heavy equalities. At deficit
zero Q=I*, its full witness directly implies weak-query membership.
Consequently a full promised input cannot fail.

The local prefix-free counting inequality depends only on R and
the remaining deficit |Q|-s. It does not require one fixed service
region if every protected node satisfies J11. The complete time is

```math
\Gamma(R)^{k-|Z|}\mathrm{poly}(H)
 \tag{J13}
```

after forced omissions Z, including every failed feasibility gate,
support LP and off-promise branch. The polynomial bounds of Section 4
are uniform. Depth-first traversal uses polynomial workspace.

A success may occur with |Q|>s, so fewer than k players are heavy
in the returned allocation. This is legal for the original
compulsory-player objective. The exact cardinality k is a property
of the protected full witness, not a required output equality. If
the global wrapper records a selected s-set, attach any s-subset
of Q as auxiliary metadata; all Q players still keep their returned
light allocations. The relaxed output remains a valid solution
of the original problem.

## 6. Cost-preserving rounding also preserves count floors

We need the following additional consequence of the existing lower
rounding construction.

**Count-floor rounding lemma.** Given any fractional allocation in
integral recipient polymatroids, nonnegative per-player values and
one nonnegative assignment-cost objective, a polynomial algorithm
returns an integer allocation of no larger cost such that, at every
player p and every prefix L of its own decreasing value order,

```math
\sum_{j\in L}x'_j(p)
                      \ge\left\lfloor\sum_{j\in L}x_j(p)\right\rfloor.
 \tag{J14}
```

It therefore loses at most the largest eligible unit value u_p in
utility and, for the full prefix, preserves at least the floor of
the player's total fractional count.

Here is the complete relevant argument. Apply the free-disposal
extension from [Unrelated-value allocation with an exact budget and a fractional comparator](../unrelated-values-additive/proof.md)
to turn each independent x_j into a base without changing any real
count or cost. Use its integral complement rank, with singleton
vector a_j and fractional dual base y_j=a_j-x_j. For each player
impose every prefix bound
`sum_(j in L)y'_j(p)<=ceil(sum_(j in L)y_j(p))`, including the full
prefix. These bounds form the integral sum-of-prefix-maxima
polymatroid. Intersect it with the direct sum of the dual resource
polymatroids and choose an integer vector on the maximum-total
face maximizing the actual cost coefficients applied to y'.
The original fractional y lies on that face, so complementing
back gives original cost at most the fractional cost.

Since A_L=sum_(j in L)a_j(p) is an integer,

```math
\begin{aligned}
 \sum_{j\in L}x'_j(p)
    &=A_L-\sum_{j\in L}y'_j(p)\\
    &\ge A_L-\left\lceil A_L-\sum_{j\in L}x_j(p)\right\rceil
      =\left\lfloor\sum_{j\in L}x_j(p)\right\rfloor.
 \end{aligned}
 \tag{J15}
```

Telescoping each player's nonincreasing value order then gives
`utility(x',p)>=utility(x,p)-u_p`. The types may be ordered differently
at different players. The product ground and all counts, prefix
ceilings and rank totals have polynomial binary encoding.

Apply this lemma **once to the jointly masked ranks f_j^Q** and the
joint witness J7. Forbidden pairs remain zero throughout rounding.
Every player outside Q had total fractional count exactly one, so
J14 gives at least one integer heavy unit there. Keep any one of
those units and discard the rest. Nonnegative costs and downward
resource constraints make this trimming safe. Every player in Q
retains utility at least b-u_L. Hence the final integer allocation
has actual total cost at most C and minimum utility at least

```math
\min\{a_H,b-u_L\}.
 \tag{J16}
```

The heavy and light resource capacities are never split or rounded
separately. Masks must be applied before the disposal/complement
construction; otherwise rounding could reintroduce a forbidden pair.

## 7. Zero-role feasibility, all-heavy coverage and finite benchmarks

For a fixed pair-value mask, the cheapest assignment of one heavy
unit to each of k distinct players is polynomially computable.
Use the direct sum of the heavy-restricted Boolean recipient
matroids on the pair ground, intersected with the partition
matroid allowing at most one pair per player, and minimize actual
assignment cost at cardinality k. The pair ground has at most qm
elements. Boolean-cap ranks use the integral box formula and paid
submodular minimization; no binary supply is expanded.

Let nu_C be the largest k whose minimum cost is at most C.
Minimum costs are nondecreasing with k because a feasible
assignment can be trimmed, so nu_C and a witness for each needed
k are obtained in polynomial time. If a fractional exact-k
zero-light-service role witness exists, fixing its heavy recipient
set and using the integral one-unit assignment intersection gives
an integer heavy witness of no larger cost. Thus skipping k>nu_C
loses no positive full-target role witness either.

For k<q with k<=nu_C, initialize the corresponding actual k-heavy
unit assignment and zero allocation on all other players. This is
a legal original allocation, of minimum utility zero. Choose a
positive rational grid g dividing every original pair value. For
this fixed mask and exact k, define X as the largest g-grid target
T admitting a full witness from Section 5. The zero-role witness
exists by the preceding gate, and downward closure in light
service makes the benchmark downward in T.

Because at least one light player is promised, X<=V, where V is
the bound in Section 4. V is a g-grid number. Use external upper
target V+g and perform one-sided maximization: a weak success
saves its actual joint witness and raises the lower endpoint;
total gap failure lowers the upper endpoint and certifies T>X.
At adjacent grid endpoints the saved lower target is at least X.
Successes need not be monotone or certify full feasibility at their
nominal targets. The number of calls is polynomial in the binary
input length. Round the saved witness using Section 6.

When k=q the light set is empty, so a full-light-target benchmark
would be unbounded. Do not create that benchmark. Test all-heavy
one-unit coverage by the same minimum-cost matroid intersection at
cardinality q, and record its actual allocation directly if
affordable. It has value at least a_H at every player. This also
handles a light-empty mask without any artificial infinite target.
The heavy-empty mask has nu_C=0 and uses only k=0.

At every recursive child, still perform the local empty-X_Q check;
global affordability of some k-heavy assignment does not imply that
the particular forced heavy players P\Q can be served jointly.

## 8. Approximation and all-instance global time

Assume OPT>0 and set theta*=alpha*OPT/2. The algorithm enumerates its
pair mask. Fix any integer optimal allocation. Let F* be the
players originally receiving at least one unit on a heavy pair.
Keep one such original heavy unit at each player in F*, keep all
original light counts at players in I*=P\F*, and drop every other
count. Resource constraints and cost only decrease.

If k=|F*|<q, this is a full witness at target OPT for the fixed
mask/k benchmark, so X>=OPT. The saved light target b is at least
alpha*OPT. By J5 and J16, light players retain more than theta*
and heavy players retain at least theta*. If k=q, the all-heavy
gate is affordable and gives the same guarantee. No extension
of the optimum's actual heavy support or replacement of its
original types is used in this promise argument.

For a supplied support cap K, enumerating k<=min{K,nu_C} gives
time Gamma(R)^K times a polynomial, and the same guarantee
whenever an optimum has |F*|<=K. Every recorded solution remains
legal even if the support promise fails; zero counts initialize
an unconditional legal output. OPT=0 needs no threshold at zero.

For an unconditional whole-q guarantee, enumerate every exact
k=0,...,nu_C, using the separate k=q gate. For each finite
benchmark target apply [A polynomial-space conversion from corank gaps to global exponential time](../whole-ground-allocation/global-conversion.md)
to the forced-omission routine J13. A protected full witness has
an omitted heavy set of exactly k elements; the block cover
contains a seed in that set. Every original k is covered by its
own wrapper. The early relaxed success with fewer heavy players
is legal, as explained in Section 5.

The global target algorithm has precisely the same sound full-
target failure and legal relaxed success interfaces, so the same
fixed-benchmark search is valid. The number of masks, cardinalities
and target calls is polynomial. The result is J3 with polynomial
workspace. No raw-corank fallback with a larger whole-q running
time is needed or run.

For fixed rational R, the exact Gamma comparisons used by the
block cover are justified by
`Gamma(a/b)^b=a^a/[b^b*(a-b)^(a-b)]`. If accuracy is a varying
binary input, one may instead supply the safe rational upper
bound A=3R>Gamma(R) to obtain the uniform base `2-1/(3R)` without
hiding numerical expansion of huge powers. The sharp J3 displays
are fixed-accuracy statements, as in the conversion manuscript.

## 9. Compulsory two-valued unrelated instances: exact factor two

Suppose every pair value belongs to {0,u,a}, with 0<u<a. The
original resource types may have u-valued recipients and a-valued
recipients simultaneously. Every player remains compulsory, costs
are arbitrary nonnegative rationals, and the budget is exact.

**Theorem J2.** This model has a deterministic exact-factor-two
algorithm in

```math
(50/27)^q\,
       2^{O(q\log\log(q+2)/\log(q+2))}\mathrm{poly}(H)
 \tag{J17}
```

time and polynomial space. It also has the corresponding
`(27/4)^nu_C poly(H)` bound, where nu_C is the largest affordable
one-a-unit recipient set. The zero-value pairs are unused.

For a target T with u<T<2a, set K=ceil(T/u)>=2 and b=ceil(K/2).
Use the mask of u-pairs as light and a-pairs as heavy. The joint
region is J7, but its service coordinates now count light units,
not their utility. A genuine target-T allocation promises K
light units at each small-only player after one large unit per
other player is retained. The protected-witness argument is
identical, with t=K and weak quota b, and

```math
K/(K-b)\le3.
 \tag{J18}
```

At success, trim each light player's fractional count to exactly
b; every forced heavy player already has count exactly one.
These are integer per-player quotas d_p. On the masked product
ground intersect the direct sum of the original resource ranks
with the partition-cap polymatroid imposing
`sum_j x_j(p)<=d_p` for every p. Its maximum total is at most
sum_p d_p, and the trimmed fractional witness attains that total.
The maximum-total face of this intersection is integral. Choose
a minimum-cost integral point on that face. Its cost is no larger
than the fractional cost, and the total equality forces every
player's quota to hold exactly.

Thus all light players receive b units of value u and all heavy
players one unit of value a. Both values are at least T/2. This
is a joint quota recovery on the original shared types; it has
no additive u loss. Equivalently J14 already guarantees at least
these integral total counts, followed by safe trimming, but the
direct heterogeneous-quota intersection gives an explicit exact
minimum-cost recovery as well.

For T<=u, use the exact minimum-cost one-positive-unit coverage
gate on all eligible positive pairs. Any integer positive-target
allocation supplies such a cover by trimming. An accepted cover
has utility at least u>=T. For T>=2a, solve the original joint
fractional allocation LP with utility at least T for every player.
If infeasible, no integer full target exists. Otherwise apply
the original cost-preserving lower rounding once to obtain value
at least T-a>=T/2. These boundary procedures are polynomial.

For u<T<2a enumerate every k<=nu_C; handle k=q by direct all-a
coverage and k<q by the joint gap. Total failure excludes every
integer target-T allocation because its actual a-recipient set
has one of these affordable cardinalities. A rational grid
dividing u and a contains integer OPT. The usual external upper
bound V+g and one-sided maximization consequently return value
at least OPT/2. Zero optimum and a missing positive value class
are covered by the same initialization and gates; a one-value
compulsory instance can also be solved exactly by its fixed-player
minimum-cost quota intersection.

The local count-gap exponent is at most nu_C with uniform base
27/4; its global forced-omission conversion gives J17. This is
the earlier compulsory two-value theorem extended to genuinely
unrelated pair values and shared original types.

## 10. Optional original player matroid without increasing q

Let the selected players instead be a genuine basis of a rank-r
matroid M, with r>=1. Delete its loops and restrict all resource
ranks accordingly, leaving q nonloop candidates and c=q-r. Let
OPT_M denote the original integer optimum with the same assignment
budget and unrelated values.

Choose a common grid g for the original values and the bound
`V=sum_j(max_p v_pj)f_j(P)`. Set D=V+g. Add one zero-cost resource
whose recipient matroid is M*, the dual of the original player
matroid, and whose value is D at every player. Its counts are
zero or one per recipient and its rank is c. Now make all q
players compulsory and run Theorem J. The original player ground
and every original resource remain unchanged.

The integer optima of these two problems are equal. In the
forward direction, an original M-basis B and its allocation
extend to a compulsory allocation by putting a dummy-resource
unit on every player in P\B. That complement is an M*-basis,
the dummy cost is zero, and D exceeds every possible original
player utility. Hence this extension preserves the original
minimum value.

Conversely, take any integer compulsory output and let S be its
actual dummy-resource recipient set. This S is M*-independent,
possibly smaller than a dual basis. The dual rank identity gives

```math
r_{M^*}(S)=|S|+r_M(P\setminus S)-r_M(P)=|S|,
                    \quad\text{so }r_M(P\setminus S)=r.
 \tag{J19}
```

Find an original M-basis B contained in the dummy-free set P\S.
Its players received no dummy utility, so they retain at least
the compulsory output's minimum using original resources alone.
Discard every original count outside B and remove the dummy
resource. Nonnegative assignment costs cannot increase, and
downward resource feasibility is preserved. This proves equality
of integer optima and transfers the approximation guarantee.

The dual rank oracle is polynomial, and D has polynomial binary
length on the same original g-grid. No candidate player is added,
so the global exponent remains q. If an original optimum has K
heavy recipients at theta*=alpha*OPT_M/2, its canonical extension
uses c dummy recipients plus those K original recipients. The
dummy value D is certainly heavy at that threshold. Thus the
conditional parameterized bound is Gamma(R)^(c+K), as stated.

This adapter transfers the general near-two theorem, not the
exact-two two-value theorem automatically: D introduces another
positive pair value. It also does not charge setup fees only to
the originally selected players. Such fees would be incorrectly
charged to dummy-covered unselected players by a naive compulsory
translation and require a separate argument.

## 11. Constraints preserved and limits of the extension

The theorem returns integer allocations in the original recipient
polymatroids. Every heavy/light role is realized on an allowed
original pair, and one actual global assignment-cost budget is
preserved. The count-floor and utility inequalities are obtained
at the same integral rounded point. There is no separate rounding
or cost accounting for overlapping copies of a resource.

Only one scalar assignment budget is claimed. The multiple-budget
obstruction in [Why arbitrary many exact assignment budgets cannot be added for free](../../manuscripts/mechanism-boundaries/multiple-exact-assignment-budgets-obstruction.md)
already encodes Independent Set with one compulsory player; even
the natural fractional LP has an unbounded largest-unit recovery
gap. The additional rows here are fixed integer per-player count
conditions handled by integral polymatroid intersection, not
arbitrary independent assignment budgets.

The oracle lower bounds in
[Global exponential-time allocation, scheduling and selected-flow transfers](../whole-ground-allocation/proof.md), Section 10,
still apply to these more general models through their intrinsic
zero-cost subclasses. In particular, a factor strictly below two
requires `2^(q-O(log q))` rank-value queries on the balanced hidden
instances. The exact-two two-value result at base 50/27 is
consistent with that threshold; its exponential base is not
proved optimal. The bounds are for arbitrary recipient rank
oracles and do not automatically describe explicit ordinary item
instances.

## 12. References and relationship to prior results

The deterministic time conversion and its base `2-1/A` are public
monotone-local-search background from Fomin, Gaspers, Lokshtanov
and Saurabh,
[*Exact Algorithms via Monotone Local Search*](https://arxiv.org/abs/1512.01621).
Polynomial space here uses the separately proved streamed
logarithmic-block representation in
[A polynomial-space conversion from corank gaps to global exponential time](../whole-ground-allocation/global-conversion.md).

Cost-preserving additive allocation rounding is public background;
see Rohwedder, Rouhani and Wennmann,
[*Cost Preserving Dependent Rounding for Allocation Problems*,
ICALP 2025](https://doi.org/10.4230/LIPIcs.ICALP.2025.127).
The full recipient-polymatroid complement implementation, arbitrary
per-player value orders, and exact-budget disposal construction
are proved and independently audited in the project's unrelated
value additive notes. J14--J15 explicitly extract the total-count
floor that their complete prefix system already guarantees.

The earlier arbitrary-cost near-two manuscript required intrinsic
values so separately recovered light and heavy allocations used
disjoint resource types. This manuscript replaces that interface by a
single masked joint LP and a surviving full-allocation witness.
Its changing regions are justified by J11, not by an assumed
nonnegative separator for a signed joint selection projection.
Original types may therefore serve both roles without capacity
double spending.

The root read and the separate audits
[Unrelated-value allocation near two through a joint light/heavy LP](proof.md) and
[Unrelated-value allocation near two through a joint light/heavy LP](proof.md) passed the empty-region
gate, masked support LP, adaptive witness, total-count-floor
recovery, exact-cardinality global cover with early relaxed
success, all target-search boundaries, and the optional-M dummy
adapter. No formal verification, external peer review or
exhaustive publication-priority claim is asserted.

---

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
