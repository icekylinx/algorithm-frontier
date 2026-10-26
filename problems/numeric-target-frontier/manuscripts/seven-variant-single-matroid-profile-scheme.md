# Single-exponential accuracy for all seven matroid linear-constraint variants

**25 October 2026. Complete theorem and proof; three independent
internal full mathematical reviews passed.**

For a single matroid, all seven nontrivial combinations of minimizing
or maximizing a nonnegative linear objective, choosing an independent
set or a basis, and imposing one upper or lower linear constraint admit
a deterministic approximation scheme with time

    2^{O(1/epsilon)} poly(H_epsilon)

and polynomial binary workspace. The side constraint is exact. The
proof also covers an arbitrary integral polymatroid with binary
capacities. It uses the reviewed profile-count and prefix-recovery
interfaces, not a rounding of the side-constraint threshold.

The principal new accuracy comparison is with the displayed
(1/epsilon^2)^{O(1/epsilon)} bound in the identified 2026 unified
single-matroid paper. This note does not claim the first EPTAS, a
fully polynomial scheme, an exhaustive fastest-known result, or a
tight accuracy exponent. Sections 8 and 9 give two independent
MAX-base constructions, so the mandatory-base part does not rely
on deleting low-priority elements of a required basis.

## 1. Exact input and theorem

Let E be an explicit coordinate ground and let F:2^E -> Z_>=0 be
normalized, monotone and submodular, supplied by an exact rank oracle.
Define

    P(F)={x>=0: x(S)<=F(S) for every S subset E},
    R=F(E),  B(F)={x in P(F):x(E)=R}.                           (SV1)

The input contains two nonnegative rational vectors v,w and a
nonnegative rational threshold L. Choose a direction opt in
{min,max}, a family in {P(F),B(F)}, and a side direction in
{<=,>=}. The objective is

    opt v*x over integer x in the chosen family,
    subject to w*x <= L or w*x >= L, as specified.               (SV2)

An additional eligibility mask may fix coordinates to zero. For
P(F), it is an ordinary restriction. For B(F), it must retain the
original total R; if the mask has rank below R, it is infeasible.

H includes the coordinate list, binary rational data, full-rank
encoding and paid polynomial exact rank, submodular minimization,
LP and polymatroid-intersection work. Put

    H_epsilon=H+size(epsilon),  0<epsilon<=1,                    (SV3)

including the entire rational numerator and denominator. Let OPT
be the original integer optimum on a feasible instance.

**Theorem SV.** A deterministic algorithm detects infeasibility or
returns an original integer feasible vector, preserving the chosen
side inequality exactly, with

    v*x <= (1+epsilon)OPT   for minimization,
    v*x >= (1-epsilon)OPT   for maximization,                   (SV4)

in 2^{O(1/epsilon)} poly(H_epsilon) time and poly(H_epsilon) space.

For a matroid rank, integer independent vectors and bases are
incidence vectors of independent sets and bases. Thus SV proves
all seven nontrivial single-matroid variants. The remaining
(min, independent, <=) variant has the zero vector as an exact
optimum because L>=0.

| Objective | Family | Side constraint | Output guarantee |
| --- | --- | --- | --- |
| max | independent | <= | at least (1-epsilon)OPT |
| max | independent | >= | at least (1-epsilon)OPT |
| max | base | <= | at least (1-epsilon)OPT |
| max | base | >= | at least (1-epsilon)OPT |
| min | independent | >= | at most (1+epsilon)OPT |
| min | base | <= | at most (1+epsilon)OPT |
| min | base | >= | at most (1+epsilon)OPT |

Only one side row is present on any one recovered integer point.
The theorem does not add a second resource matroid or several
independent hard linear inequalities.

## 2. Optional independent vectors can be represented by bases

After legitimate eligibility restriction in the independent-vector
case, write n=F(E). Add a free disposal coordinate 0 and define

    Fhat(S)=F(S) if 0 is not in S,
    Fhat(S)=n    if 0 is in S.                                 (SV5)

Give that coordinate v_0=w_0=0. The rank is normalized, monotone,
integral and submodular. For two sets containing 0 submodularity
is equality; for exactly one, it reduces to monotonicity of F;
for neither, it is inherited from F.

Every original independent vector x extends to a base by setting
x_0=n-x(E), and every base projects back to an independent vector
by deleting coordinate 0. Objective and side weight are unchanged
in both directions. This is an exact representation, including
covering constraints. It adds one binary-capacity coordinate, not
n individual unit copies.

Consequently it suffices to prove the theorem for a full base of
one integral polymatroid. When the original family already requires
a base, this free disposal extension is not used to discard its
mandatory units. The separate active/passive construction below
keeps the full original total and all actual side contributions.

Henceforth F denotes the resulting base rank and R its required
total. Zero-value coordinates, including any free disposal
coordinate, must remain available: a mandatory base or a covering
constraint may need them.

## 3. Exact feasibility and degenerate cases

First test that the eligibility mask has rank R. On its total-R
base face optimize the one weight w:

- For w*x<=L, compute an integral minimum-w base and compare with L.
- For w*x>=L, compute an integral maximum-w base and compare with L.

These linear optimizations are polynomial in the exact oracle
model. If the appropriate optimum fails the inequality, no original
feasible vector exists. Otherwise save that actual feasible base
as an initializer. This gate is independent of objective v and
is not a bicriteria relaxation.

If R=0, the zero vector is the only base; the preceding comparison
decides its side feasibility and its objective is zero. If all
eligible v values are zero, every feasible base has objective zero.
In minimization, a zero optimum can also occur when positive values
exist elsewhere. Test it by masking all positive-v coordinates,
retaining the original R, and repeating the side-weight optimization.
A success is an exact zero-objective optimum.

All remaining minimization instances have OPT>0. Maximization
needs no separate positivity decision: any saved feasible base is
a valid zero-target output, and the target routine handles a
positive optimum whenever one exists.

## 4. One scalar side row is preserved on an integral face

### 4.1 Upper-prefix recovery

Let a fractional base x of a restricted F be given, with original
total R. Suppose an integral polymatroid K contains x. Then

    P(F) intersect P(K) intersect {z(E)=R}                     (SV6)

is a nonempty integral face. The total cannot exceed F(E)<=R,
so the displayed equality is a maximum-total face of the integral
two-polymatroid intersection.

For an upper side row, minimize w*z on this face; for a lower
side row, maximize w*z. An integral optimizer satisfies the
same required inequality whenever x does. The side row is not
added as a halfspace to assert integrality.

For an ordered group with v_1>=...>=v_m>=0, set
X_h=sum_(i<=h)x_i and U_h=ceil(X_h). The integral prefix caps
z({1,...,h})<=U_h have rank max_{h in S}U_h on a nonempty subset
S. Summation by parts gives

    sum_i v_i z_i <= sum_i v_i x_i + v_1.                     (SV7)

Disjoint count-cap groups and one such small-value chain form
the machine-side polymatroid K used for minimization.

### 4.2 Lower-prefix recovery while retaining the entire base

For an arbitrary integral base rank F on a current ground D, set
d_e=F({e}) and

    G(S)=F(D minus S)+d(S)-F(D).                               (SV8)

The singleton marginal bound proves that G is normalized,
monotone, integral and submodular. Box complementation is a
bijection

    y=d-x in B(G)  iff  x in B(F).                            (SV9)

In particular, y_e<=G({e})<=d_e gives nonnegative recovered
x_e, and the inequality on D minus S gives x(S)<=F(S).

Choose a nonincreasing surrogate-value order of all coordinates.
On y impose ceiling-prefix caps ceil(y(S)). They form one integral
chain polymatroid containing y. Intersect it with P(G) at the
full total G(D). This is a nonempty integral maximum-total face.

The correct scalar objective on this complement face is:

| Required original side | Optimize on complement face |
| --- | --- |
| w*x<=L | maximize w*y |
| w*x>=L | minimize w*y |

Indeed w*x=w*d-w*y, with the first term constant. An integral
optimizer therefore preserves the required side direction relative
to x. Complementing back retains a full original base and gives
simultaneously for every prefix S

    x'(S)>=d(S)-ceil(y(S))=floor(x(S)).                        (SV10)

For surrogate values s_1>=...>=s_m>=0 and s_(m+1)=0,

    s*x' >= s*x
       - sum_h (s_h-s_(h+1)) (X_h-floor(X_h)).                 (SV11)

This argument also handles zero-value coordinates, which stay
inside the required base and inside the side-weight objective.

Exact integral optimizers can be obtained by standard weighted
polymatroid-intersection optimization or by polynomially many exact
lexicographic LP optimizations on the integral face. Large integer
capacities are not expanded.

## 5. The weighted profile-count lemma

Let 0<delta<=1/2, J=floor(1/delta), and partition (delta,1] into

    (lambda_i,mu_i],
    lambda_i=delta+i*delta^2,
    mu_i=min(1,delta+(i+1)*delta^2),
    0<=i<ceil((1-delta)/delta^2).                              (SV12)

An internal endpoint belongs to the preceding interval. Delta
itself is small and one belongs to the last interval. Only bins
with an actual input coordinate are materialized.

Profiles are nonnegative integer vectors h with a prescribed
count cap K<=J+1 and lower-load cap

    sum_i h_i<=K,   sum_i lambda_i h_i<=b,                     (SV13)

where b is one or two. Since
lambda_i>=delta^2(J+i), map h_i copies of bin i to h_i parts
of integer size J+i. This is an injective map to integer partitions
of weight at most N=floor(b/delta^2)<b(J+1)^2.

For any t>0, the number of partitions of weight at most N is at most

    exp(tN) product_(j>=1) (1-exp(-tj))^(-1).

The log of the product is

    sum_(l>=1) 1/[l(exp(tl)-1)] <= 2/t,

using exp(a)-1>=a and sum_l 1/l^2<=2. Taking t=1/(J+1)
bounds the profile count by

    exp((b+2)(J+1)).                                          (SV14)

The proof does not compute an infinite product or a partition table.

To obtain the same all-input algorithmic bound, enumerate occupied
bins recursively. With partial count a and lower load ell, the
next count ranges exactly over

    0 <= h <= min(K-a, floor((b-ell)/lambda_i)).                (SV15)

Every generated prefix can be completed by zeros. At any fixed
depth distinct prefixes have distinct all-zero completions, so
the complete traversal has at most (m+1) times as many nodes as
valid profiles, where m is the occupied-bin count. It is insufficient
to enumerate all unweighted compositions and test load afterward.

All bin indices, counters and sums are binary. Stored positions
are bounded by the input coordinate count, even when epsilon is
exponentially small in its binary encoding.

## 6. MIN: exact side constraint and upper profile rounding

Fix a positive target T and delta=epsilon/2, K=floor(1/delta).
Forbid coordinates with v_e>T while keeping the original required
total R. If the available rank is below R, this target fails.
Let small coordinates have v_e<=delta*T and bin the remaining
normalized values by SV12.

Enumerate profiles satisfying SV13 with b=1. Let
ell=sum_i lambda_i h_i. For one profile solve the fractional LP:

    x in the restricted P(F),  x(E)=R,
    w*x has its original required relation to L,
    x(big bin i)<=h_i,
    sum_(small e) v_e x_e <= (1-ell)T.                         (SV16)

Any integral feasible base of objective at most T supplies a
profile through its actual big-bin counts. Its big count is at
most K, its lower big load at most one, and its small load fits
the residual cap. No unit is deleted, so the side constraint is
unchanged. Therefore exhaustive profile failure excludes every
original full-T solution.

For a feasible LP point, retain the integral big-bin caps and
build an upper-prefix chain on the small coordinates. Apply SV6
with the appropriate min/max side-weight objective. The resulting
integer original base satisfies the side constraint exactly. Its
large objective contribution is at most

    (ell+K delta^2)T <= (ell+delta)T,

and its small contribution is at most

    (1-ell)T+delta*T.

The output objective is therefore at most (1+epsilon)T. Both
directions of the side inequality use the same load proof.

The number of target profiles is at most exp(3(K+1)), and all
failed profiles and their work are included in this count.

## 7. MIN target optimization, including zero

Use the exact feasibility and zero-objective gates from Section 3.
After the zero test fails, OPT>0. Choose a positive rational grid
g dividing all positive original v values. It can be computed from
a common denominator and integer gcd with polynomial bit length.
All original integer objectives are multiples of g.

Set the failed lower target to zero and the upper target to the
objective of the saved exactly feasible base. At grid midpoints,
run the complete routine from Section 6. Failure certifies T<OPT
and raises the lower endpoint. Success saves its actual original
base and lowers the upper endpoint.

At adjacent grid endpoints, the failed lower endpoint is strictly
below OPT, so the saved upper target is at most OPT. Its output
value is at most (1+epsilon)OPT. Weak successes need not be
monotone, and no extra approximation factor is introduced.

The initial upper objective is at most R*max_e v_e. The grid and
this magnitude have polynomial bit length, so polynomially many
target calls suffice. This proves SV for every MIN variant after
the exact optional-to-base reduction.

## 8. MAX: active/passive marking preserves mandatory units

The main MAX proof turns deletion in an optional allocation witness
into a marking of mandatory units. It does not discard any part
of an original base or its real side weight.

### 8.1 An exact parallel lift of the resource rank

Replace each current coordinate e by two coordinates e^a and e^p,
called active and passive. Let pi(S) be the original coordinates
represented in a lifted set S and set

    F'(S)=F(pi(S)).                                            (SV17)

The rank is normalized, monotone and integral. To check submodularity,
pi(A union B)=pi(A) union pi(B), whereas pi(A intersect B) is
contained in pi(A) intersect pi(B). Original submodularity followed
by monotonicity proves the required inequality for F'.

For a lifted vector z, define x_e=z_(e^a)+z_(e^p). Then

    z in P(F') iff x in P(F),
    z in B(F') iff x in B(F).                                 (SV18)

The forward direction tests all copies of any original subset.
The reverse direction uses z(S)<=x(pi(S))<=F(pi(S)). Full totals
agree, so bases also correspond. Any integer split of an original
integer base is therefore a lifted integer base.

Give both copies the SAME actual side weight w_e. Their aggregate
side weight is exactly w*x. Active utility is v_e and passive
utility is zero; this is only an analysis/LP surrogate. The final
original objective counts v_e on both merged copies and is at
least the active utility.

This construction shares one original capacity. It is not two
independent copies of the resource. Every zero-value and passive
coordinate is kept and still carries its actual side weight.

### 8.2 Integer full targets provide small active profiles

Fix T>0, delta=epsilon/3 and K=ceil(1/delta). Cap active utility
at T. An original integer base of objective at least T still has
total capped utility at least T: either one unit reaches T or no
unit value is changed.

Classify its capped units as big above delta*T or small otherwise.
If the big total reaches T, mark active only a first-reaching
prefix of big units and mark every other unit passive. The active
big total is strictly below 2T and its count is at most K.
If the big total is below T, keep all big and all small units
active; the big count is again at most K and its total below T.

No original unit is removed. Marking preserves the full original
base and the exact real side weight by SV18. It is an existence
proof on integer counts, not an expansion into unit identities.

Bin active big values by SV12 and enumerate exact counts h with
b=2 in SV13. Put

    ell=sum_i lambda_i h_i,  u=sum_i mu_i h_i.                  (SV19)

For a fixed profile solve the LP

    z in B(F'), retaining its original full total R,
    actual lifted w*z has the original relation to L,
    z(active big bin i)=h_i,
    active small utility >= max(0,1-u)T.                      (SV20)

The marked original full-T witness supplies a feasible profile
LP. If its active big utility already reaches T then u>=1;
otherwise the original small utility satisfies the displayed
requirement. Hence exhaustive failure excludes every original
integer base with objective at least T and the required side row.

### 8.3 Lower-prefix recovery and projection

Assign active big bin i the constant surrogate value lambda_i*T,
keep actual capped small values, and assign all passive coordinates
zero. Order active big bins by decreasing surrogate, followed by
small coordinates in decreasing order and zero coordinates last.
Put big coordinates first at ties.

Apply the DIRECT full-base complement recovery SV8--SV11 on F'.
There is no free deletion or new disposal of mandatory units at
this step. The scalar complement objective preserves the side
constraint in its original direction.

Every big-bin boundary prefix has integer fractional total because
the bin totals in SV20 are integers. Within a bin the surrogate
value is constant. Therefore every large-value contribution to
the error sum SV11 is zero, including the last big/small boundary.
Only the small part can lose value; its drops telescope to at
most delta*T. Passive zero coordinates add no error.

The fractional surrogate objective is at least

    [ell+max(0,1-u)]T >= (1-K delta^2)T.

Thus the recovered integral lifted base has active surrogate
utility at least

    (1-delta-K delta^2)T >= (1-epsilon)T,                       (SV21)

because delta+K delta^2<=2delta+delta^2<=epsilon for the chosen
delta and 0<epsilon<=1. Merge active and passive counts. The
result is an original full base with exactly the recovered side
weight. Its true objective dominates active surrogate utility,
proving the desired MAX target guarantee.

The state count is exp(4(floor(1/delta)+1)) by SV14. Coordinate
dimension has only doubled. This proof is valid for both side
directions and does not assume optional units can be dropped.

### 8.4 Exact one-sided maximization search

The initial exactly feasible base supplies a nominal zero-target
output. If R=0 or all eligible values are zero, it is optimal.
Otherwise let g divide all positive original values and set
V=R*max_e v_e, a grid value bounding every original objective.
Initialize lower target a=0 and external upper target b=V+g.

At each positive grid midpoint T use all profiles in SV20. Total
failure implies OPT<T and lowers b. Success saves its actual
projected original solution and raises a. The upper endpoint
always remains strictly above OPT. At adjacency b=a+g, integrality
of original objective values implies a>=OPT, so the saved output
is worth at least (1-epsilon)OPT.

There is no assertion that weak success means full-T feasibility.
All target and profile arithmetic has polynomial bit length, and
the number of target calls is polynomial. This proves all MAX
variants after the exact optional-to-base representation.

## 9. Independent MAX-base proof using dyadic objective scales

This second derivation avoids active/passive coordinates and does
not cap or trim an original mandatory basis. It is useful as a
separate check of the MAX-base and side-direction conclusions.

If some original v_e>0, let v_min be the smallest positive value
and v_max the largest. Enumerate V=2^i v_min until the first
value at least R*v_max. The number of scales is polynomial in
the original encoding. For OPT>0, it is at least v_min, so
one scale satisfies

    OPT<=V<2OPT.                                               (SV22)

For each scale use delta=epsilon/4 and K=floor(1/delta). Mask
values above V, retaining the original total, and bin big values
above delta*V. Enumerate profiles with lower-load cap one and
count cap K. Require exact big-bin counts and the original side
row, but instead of a small-utility threshold simply maximize
the true fractional objective v*x over this base LP.

For the good scale SV22, an original optimum uses no coordinate
above V, and its big counts supply an enumerated profile. Its
total big lower load is at most one, so the fractional optimum
for that profile has value at least OPT.

Give big coordinates their lower-bin surrogate and keep small
true values. Replacing big values loses at most K delta^2 V.
Direct base complement lower-prefix recovery loses at most
delta V because integer big-bin counts eliminate all large
boundary errors. With the appropriate complement side objective,
the result is an exactly feasible original base of value at least

    OPT-(delta+K delta^2)V
       >= OPT-2delta V >= (1-epsilon)OPT.                     (SV23)

No total-v upper constraint is required in this fractional LP.
Even if its optimum exceeds V, the big replacement loss is
controlled by its exact prescribed bin counts and the prefix
loss by the largest small value.

Keep the best actual output across all scales and retain the
initial feasible solution throughout. If OPT=0, that initializer
already meets the guarantee; a separate positivity test is
unnecessary. Other scales can fail or produce weak outputs without
affecting the protected good-scale argument.

SV14 bounds the per-scale state count by exp(3(K+1)). This again
gives 2^{O(1/epsilon)} polynomial time and polynomial space.
Zero-value coordinates remain in the required base throughout.

## 10. Complete oracle, bit and workspace accounting

The current rank is accessed by polynomial transformations of the
original oracle. Restriction evaluates F on a subset. Free disposal
adds one coordinate. The active/passive lift evaluates F on its
projected subset. A complement rank uses one current rank query
and a known modular sum. Each step preserves polynomial ground
size and binary rank length. Complement total rank is at most
the number of coordinates times R.

Resource-polytope separation minimizes F(S)-x(S), an exactly
specified submodular function. All profile equalities, side rows,
totals and utility rows have polynomial-size rational descriptions.
Every LP has polynomial dimension, and all extreme-point
denominators have the usual polynomial bit bound in the exact
oracle model. Weighted integral-face optimization and lexicographic
vertex selection require only polynomial work per state.

All failed rank masks, infeasible side rows, profiles, target calls
and scale attempts are counted. SV15 prevents an uncharged larger
enumeration of rejected compositions. The analysis uses only
occupied bins; no array of size 1/epsilon or R is stored.

The algorithm retains one target or scale, one binary profile,
one LP/recovery workspace and the best original vector. Its
space is polynomial in H_epsilon. The exponential accuracy factor
appears in time, not memory. Exact full feasibility and zero
objective tests are polynomial and included in the displayed
bound.

## 11. Consequences, public comparison and limits

For a graphic matroid, the base versions include minimizing
spanning-tree weight under an exact bound on another tree weight,
and the corresponding lower-threshold variant. The independent
versions include budgeted maximum-weight forests and minimum-cost
matroid cover. Arbitrary independence-oracle matroids and binary
integral polymatroids are covered; graph representation is not
required by the proofs.

Doron-Arad, Shachnai and Shmerler,
[*Tight Approximation Results for Matroid Optimization with a Linear Constraint*, APPROX/RANDOM 2026](https://drops.dagstuhl.de/storage/00lipics/lipics-vol392-approx-random2026/LIPIcs.APPROX-RANDOM.2026.18/LIPIcs.APPROX-RANDOM.2026.18.pdf),
state a unified EPTAS with accuracy dependence
(1/epsilon^2)^{O(1/epsilon)} for the seven single-matroid variants.
The theorem here improves that displayed dependence to
2^{O(1/epsilon)} and proves its own recovery. Existing EPTAS
existence, the descriptor family, and the general use of bucket
counts are credited to public antecedents. This is a comparison
of identified bounds, not a first-EPTAS or exhaustive-priority
claim.

The separate public-profile pruning audit gives another way to
see the same counting improvement. The present proofs do not
depend on that paper's Lagrangian exchange-path implementation.

No optimality claim about the remaining 1/epsilon exponent is
made. The separately investigated oracle accuracy lower bounds
must be reported with their actual epsilon-to-ground-size relation.
Nor does this theorem handle two independent resource matroids,
several exact side rows, or arbitrary overlapping objective groups:
its integral recovery has one resource rank and one chain/partition
rank. Such extensions need additional proofs.

The active/passive mechanism also admits a separate blockwise
mandatory-base fairness theorem; that broader statement and its
selection/initialization details are proved in its own manuscript.
This note's complete theorem is the one-block seven-variant claim.
No Lean, PDF or experimental validation is used as a substitute
for the mathematical arguments above.
