# Exact mixed numeric targets controlled by original support patterns

**25 October 2026. Complete incremental theorem and proof; root and independent
full mathematical reviews passed.** This note removes the column-arity restriction
from the support-pattern refinement. It retains arbitrary mixed upper,
equality and covering rows, one global integral polymatroid, binary
resource counts, one exact rational scalar optimization, and uniform
polynomial binary workspace.

Let T be the sum of integer targets and Q the number of distinct
nonempty positive supports of the original eligible coefficient
columns, after the explicit zero-target preprocessing below. For T>0,
the new bound is

```math
\boxed{\exp\!\left(O\!\left(T\log\left(2+\frac QT\right)\right)\right)
                     \mathrm{poly}(H).}
 \tag{UP1}
```

The constant in O is independent of the row count and the maximum
column support size. In particular Q=O(T) gives singly exponential
time even when every column touches arbitrarily many rows.

For pure upper/equality rows there is no cover representation step,
and the sharper explicit bound is

```math
2^T\binom{Q+T}{T}\mathrm{poly}(H).
 \tag{UP2}
```

The main new ingredient for mixed rows is a support-block prefix
representation. It keeps at most the total covering demand in
conceptual useful units, but stores them through only polynomially
many binary-length intervals. Exact interval-count rows control the
new support catalogue. No covering row is marked a second time
inside the bounded-profile solver.

Dependencies are the exact-profile recovery and support-composition
lemma in [row-overlap-density-numeric-target-refinement.md](row-overlap-density-numeric-target-refinement.md) (RD),
and the mixed-target/chain results MD and VT. This manuscript proves
the new representation and parameter accounting; it does not modify
those prior increments or claim that count-profile intersection is new.

## 1. Model, preparation, and the pattern parameter

Let F be a normalized monotone integral polymatroid rank on an explicit
ground E. Integer vectors belong to P(F), or to B(F) with original
required total R=F(E). Rank values and counts are binary encoded.
Original eligibility restrictions are permitted. An arbitrary rational
linear scalar c x is to be minimized or maximized exactly; its
coefficients may have either sign.

There are explicit nonnegative integer coefficients a^j_e, targets
T_j>=0, and relations rho_j in {<=,=,>=}. Set T=sum_j T_j. The
scalar c is separate from these numeric rows and their support count.

Use the standard exact preparation. Optional vectors can be represented
by adding one zero-row, zero-scalar disposal coordinate and completing
to the original rank R. Mandatory original bases receive no disposal.
Mask every coordinate whose coefficient exceeds an upper or equality
target; with integer nonnegative counts such a coordinate cannot be
used by a feasible solution. Remove zero-target cover rows, which are
automatic, and zero upper/equality rows after their positive columns
have been masked. Keep the original required total throughout and
reject rank loss in its base representation.

Let F_0 be the prepared resource rank of total R. All remaining targets
are positive integers, so the number of remaining rows is at most T.
If none remains, scalar optimization on the prepared rank is polynomial.
All-zero coefficient columns, including any legitimate disposal, remain
available; they may be essential for a base or a signed scalar optimum.

For a nonzero column define its positive support

```math
S_e=\{j:a^j_e>0\},\qquad
        \mathcal S=\{S_e:S_e\ne\varnothing\},\qquad Q=|\mathcal S|.
 \tag{UP3}
```

Repeated supports are counted once, even when their positive coefficient
values differ. Q is not the number of distinct coefficient vectors, the
maximum number of nonzeros in a column, or a bound on the resource
rank. The support catalogue and its blocks E_S={e:S_e=S} are explicitly
computable in polynomial time.

Let C be the set of covering rows, s=|C|, and put

```math
T_C=\sum_{j\in C}T_j,\qquad
 U_j=\begin{cases}T_j,&j\notin C,\\2T_j-1,&j\in C,\end{cases}
 \quad U=\sum_jU_j=T+T_C-s.
 \tag{UP4}
```

Let Q_C count the patterns S meeting C. Let Q_0 count the distinct
nonempty sets S minus C over all original patterns. Thus
Q_C<=Q, Q_0<=Q and s<=T_C<=T. When C is empty, Q_C=s=T_C=0,
Q_0=Q, and U=T.

## 2. The direct bounded-profile lemma

The following interface is a direct consequence of RD, and is the
only integer recovery solver used inside the new construction.

Suppose an explicit coefficient ground has one integral resource
polymatroid with required total R, nonnegative integer coefficient
vectors b, and finite row intervals L_j<=b^j z<=V_j whose integer
endpoints satisfy 0<=L_j<=V_j. Equalities are
allowed by L_j=V_j. Put V=sum_j V_j and let q_* be the number of
distinct nonempty supports of its actual coefficient vectors.
Then exact scalar optimization takes

```math
2^V\binom{q_*+V}{V}\mathrm{poly}(H_*),
 \tag{UP5}
```

with polynomial binary space. No cover-copy wrapper is applied here:
every row already has a finite upper allowance V_j.

To recall the count, a multiset of vectors on one exact support of
size t and total entry weight w can be encoded by sorting its vectors
and flattening their t positive entries. The composition of w records
the vector count and the multiset, giving at most 2^w possibilities.
If h supports are used, their positive weights summing to at most V
have binomial(V,h) choices. Consequently the full count is at most

```math
2^V\sum_h\binom{q_*}{h}\binom Vh
                       =2^V\binom{q_*+V}{V}.
 \tag{UP6}
```

For a profile, prescribe the count of every occupied nonzero coefficient
vector. One global zero-vector group receives the remaining count to R.
The intersection of the resource polymatroid with that partition-count
polymatroid is integral; on its total-R face all group caps are tight.
Weighted intersection optimizes the original scalar exactly on the
profile or proves it empty. An absent zero group with positive required
remainder simply makes the face empty.

The generator traverses only occupied vector classes. It bounds each
next multiplicity by the remaining resource total and every component's
remaining upper allowance. Every partial profile has a zero completion
within the upper caps, and distinct partial profiles at the same depth
have distinct completions. Thus all failed filters and empty resource
subproblems are charged by UP6 up to a polynomial depth factor. Neither
V nor R is expanded into a unit list. This also proves UP2 directly.

## 3. A supplementary high-arity occurrence bound

For pure upper/equality rows, let M be the number of distinct nonzero
coefficient vectors. Every vector with support S contributes at least
one unit to each row in S. Therefore the number m of nonzero vector
occurrences in any upper-cap profile is at most

```math
\kappa=\min\left\{R,\left\lfloor
 \max\left\{\sum_{S\in\mathcal S}y_S:
          y\ge0,\ \sum_{S\ni j}y_S\le T_j\ \forall j\right\}
                                  \right\rfloor\right\}.
 \tag{UP7}
```

This is an explicit rational linear program of polynomial size. It is
only an upper bound on the profile occurrence count; no integrality of
this auxiliary packing polytope is assumed. The number of profiles is
also at most

```math
\binom{M+\kappa}{\kappa}.
 \tag{UP8}
```

The same streamed generator may impose m<=kappa, so its entire traversal
is bounded by the minimum of UP2's profile factor and UP8, with polynomial
space. A simpler bound is kappa<=min(R,floor(T/a_min)), where a_min
is the minimum nonempty support size. If Q=1, then
kappa<=min_{j in S} T_j. For constant such minimum, exact optimization
is polynomial in the input, even with unbounded row count and arity.

This can be substantially stronger than an exponential-in-T estimate
in particular dense-support instances. It is not claimed as an original
resource-count bound for unrestricted covering rows, whose actual
contributions can exceed their targets by an arbitrary amount.

## 4. Useful prefixes in a common order of support blocks

We now prove the mixed-row theorem. Fix one order of the Q_C support
patterns incident with covers, for example lexicographic order. Take
any original feasible integer base x. Conceptually list its units
blockwise by this support order, and in any fixed order within each
block. Units with no covering incidence can be placed elsewhere; they
have no effect on the following argument. This is an existence proof,
not an expanded input representation.

Use capped positive contributions

```math
\bar a^j_e=\min\{a^j_e,T_j\}
                             \quad(j\in C).
 \tag{UP9}
```

Their full sum still reaches every covering target. If a used unit has
coefficient at least T_j it alone reaches the capped target; otherwise
all used coefficients in that row remain unchanged.

During the blockwise scan, maintain the integral residual demand

```math
D_j=\max\{T_j-\text{processed capped sum in row }j,0\}.
 \tag{UP10}
```

Call a unit useful if, immediately before it, at least one incident
covering row has positive residual demand. It reduces such a demand
by at least one because every positive capped coefficient is an integer
at least one. The sum of residuals starts at T_C and never increases.
Hence the number K of useful units satisfies

```math
K\le T_C.
 \tag{UP11}
```

All units in one support block have exactly the same positive incident
cover rows. While any such row remains unfinished, the next unit is
useful; once all are finished, no later unit in that block is useful.
The useful units of that block therefore form a prefix of length k_S.
Rows already satisfied before a block never require that block's units.
A block with no covering incidence has k_S=0 by definition.

This proves a crucial completeness invariant: a discarded block tail
is discarded only after **every** incident cover row is already
satisfied. In particular, no positive occurrence preceding any row's
first target crossing is discarded. All original units are retained
as resource units; “discarded” here means only that the unit receives
no auxiliary covering credit and will use a passive copy.

For each cover row j, let nu_j be the ordinal of its first-reaching
positive occurrence among the useful units. Nonincident units are not
counted in that ordinal. Since each preceding positive occurrence
contributes at least one,

```math
1\le\nu_j\le T_j.
 \tag{UP12}
```

Deleting the passive tails does not change this ordinal. The capped
contribution through that occurrence lies in [T_j,2T_j-1].

## 5. Guessing a compressed prefix template

The algorithm enumerates all binary integer vectors

```math
k_S\ge0\quad(S\cap C\ne\varnothing),
                     \qquad K=\sum_Sk_S\le T_C,
 \tag{UP13}
```

and every choice nu_j in {1,...,T_j} for j in C. The number of
such templates is at most

```math
\binom{Q_C+T_C}{T_C}\prod_{j\in C}T_j.
 \tag{UP14}
```

The useful support word is implicit: pattern S appears k_S times in
the fixed block order. To locate row j's proposed stopping occurrence,
sum k_S over the earlier patterns containing j, and find the block
where that positive-occurrence count first reaches nu_j. Its local
position is the difference from the earlier count. If there are too
few such occurrences, reject this template. All arithmetic is binary;
no useful word of length K is written out.

In a positive-length block S, split {1,...,k_S} immediately after each
proposed row-stop position inside it. Include the end k_S and omit
empty intervals. Within each resulting interval, the set of covering
rows that still credit a unit is constant: rows before their stopping
block still credit it, rows after that block do not, and the stopping
unit itself is credited before the row is removed. Tied stops share
one boundary.

There are at most

```math
J\le |\{S:k_S>0\}|+s\le Q_C+s
 \tag{UP15}
```

positive intervals. Their lengths are positive binary integers summing
to K. Thus a template has a polynomial-size interval description even
when K and the original rank are exponentially large numerically.

## 6. Shared interval copies and exact interval counts

For every original coordinate e with pattern S, create one copy for
each interval of S and one passive copy. Coordinates in zero-length
blocks or with no covering incidence need only the passive copy.
Let pi forget the copy label. All copies have shared resource rank

```math
F^\uparrow(Y)=F_0(\pi(Y)).
 \tag{UP16}
```

Projection preserves unions and maps intersections into intersections,
so monotonicity and submodularity of F_0 prove that this is an integral
polymatroid rank. Aggregation x_e=sum_{copies of e}z_copy gives exact
independent-region and original-total base equivalences. Full inverse
images prove one direction; z(Y)<=x(pi(Y)) proves the other. Every
copy retains the original scalar coefficient c_e.

Every upper or equality row retains a^j_e on all copies of e. A cover
row receives bar a^j_e on an interval copy exactly when it credits that
interval, and zero otherwise. Every passive copy has zero covering
credits. Rows not incident with e have zero coefficients throughout.

For each interval I introduce a new exact count row. It has coefficient
one on all copies labeled I and zero elsewhere, and target equal to
the binary interval length ell_I. Thus the interval receives exactly
ell_I units, collectively from all original coordinates in its block.
The sum of these added targets is K.

The original covering rows now require their **bounded credited**
totals in [T_j,2T_j-1]; upper and equality rows keep their original
requirements. The new rows are exact interval counts. This is a
direct bounded-profile instance for UP5. It is not passed to a
generic cover wrapper that would generate another family of marks.

## 7. Why interval multisets suffice

For completeness, take the feasible witness from Section 4 and its
template in Section 5. Assign each useful unit to its actual interval
and every other unit to its passive copy. The intervals contain their
prescribed numbers of units. The credited covering sums are the
first-reaching sums in [T_j,2T_j-1]. Upper/equality totals and scalar
value are unchanged, and shared aggregation preserves the original
resource base. Every original feasible scalar value therefore has a
representative in one enumerated bounded-profile instance.

Conversely, take any integer solution of one such instance. Aggregate
its copies. The result is an original resource base of total R. All
upper and equality values agree exactly. The true value of every
covering row dominates its credited value, so the original cover is
satisfied. Scalar value agrees exactly, including for signed costs.
Projecting a legitimate optional disposal coordinate gives the
original independent-vector interpretation.

There is no need to order the recovered units inside an interval or
to certify that its assigned coefficients would reach the target
for the first time at the guessed stop. That property was used only
to show that every original witness has some template. Soundness of
an arbitrary output follows from bounded credited totals and their
domination by original values. The solver chooses interval multisets
through exact coefficient-vector counts and a single integral resource
intersection. It does not enumerate permutations within intervals.

Taking the best scalar value over all templates therefore gives the
exact original optimum, with equivalent infeasibility reporting.
No resource units or real scalar contributions are lost in this
representation.

## 8. Support count and the complete running time

Within one interval all original coordinates belong to its same
support block S. Their positive coefficient magnitudes may differ,
but their noncover support is S minus C and their active cover
support is fixed by the interval. They also share that interval's
unique positive count-row marker. Hence each interval contributes
exactly one possible positive support pattern, independently of
the number of original coordinates or coefficient values there.

Passive copies have support S minus C, so their distinct nonempty
supports number at most Q_0. Thus the prepared support count is

```math
q_*\le Q_0+J\le Q_0+Q_C+s.
 \tag{UP17}
```

Its sum of row upper allowances is

```math
V=U+K\le U+T_C=T+2T_C-s\le3T.
 \tag{UP18}
```

Combining UP5 and UP14 gives the explicit all-input time bound

```math
\boxed{
 \binom{Q_C+T_C}{T_C}
 \left(\prod_{j\in C}T_j\right)
 2^{U+T_C}
 \binom{Q_0+Q_C+s+U+T_C}{U+T_C}
                      \mathrm{poly}(H).
 }
 \tag{UP19}
```

It specializes to UP2 when C is empty. For T>0, use
Q_C,Q_0<=Q, T_C<=T, s<=T and
prod_j T_j<=exp(T_C-s). Together with
binomial(a+b,b)<=[e(1+a/b)]^b, these inequalities show that
the logarithm of UP19's nonpolynomial factor is

```math
O\!\left(T\log\left(2+\frac QT\right)\right),
 \tag{UP20}
```

with an absolute constant. For example the inner rank of the
binomial estimate has b=U+T_C between T and 3T, and its other
parameter is at most 2Q+T, so its logarithm has the claimed form.
The same estimate applies to the outer binomial factor; the product
of ordinals and the powers of two add only O(T). This proves UP1.

## 9. Uniform binary workspace and failure accounting

Stream k_S vectors by a depth-first traversal under sum k_S<=T_C.
Every partial vector has a zero completion, so its total generated
states are charged by a polynomial factor times the first factor in
UP14. Stream the stopping ordinals with binary counters. Invalid
stop locations are rejected in polynomial time per template.

There are at most Q_C+s intervals and at most s+2 copies per original
coordinate. All copied coefficients, interval lengths, row targets
and ranks have polynomial binary encoding. The prepared number of
rows and coordinates is polynomial in the original H, uniformly in
the number of cover rows and their arity. The exact-profile generator
uses occupied coefficient classes and componentwise remaining caps;
its failed branches are charged as in Section 2. Run one exact
intersection at a time and retain only the best feasible scalar and
its compressed output.

The original base rank may be binary-large. The added interval counts
may also be binary-large. Neither creates a loop of that length in
the resource ground or the workspace. The possibly large number of
templates is charged to UP19, while each template's stored state is
polynomial. No list of all templates, useful units, or profiles is
stored. Aggregating the output copies is polynomial-time arithmetic.

When T=0, the initial masks leave only exact scalar optimization and
the algorithm returns without any expression involving Q/T. Rank
zero, absent zero-vector groups and impossible positive rows are
handled by the same preparation and integral-face tests. Signed
scalar coefficients do not affect the counting or the proof because
all resource mass and all original scalar terms are retained.

## 10. When this is an improvement

The new parameter is the number of distinct positive supports,
regardless of their cardinalities or their coefficient magnitudes.
When Q=O(T), UP1 gives 2^{O(T)} time for arbitrary mixed rows. The
previous unrestricted variable-dimensional summary was
2^{O(T log(T+2))}; the new estimate removes that logarithm in this
regime. A single pattern can touch all rows, so bounded arity is
not required and the row-intersection graph may even be complete.

For pure upper/equality rows with one pattern, the occurrence bound
UP7 can be sharper still: the number of resource occurrences with
nonzero coefficients is at most the smallest target on that support.
The exact algorithm is polynomial for a fixed such bound, even with
arbitrarily many rows. This concrete endpoint also prevents treating
the general singly exponential estimate as a tight bound for every
small-Q instance.

For fixed small dimension, the older anisotropic partition estimate
can be smaller. In one dimension it gives a square-root target
exponent, while UP2 is only singly exponential in that target.
The dimension-free VT bound can also be better when Q is very large.
These remain valid alternatives. Deterministically dovetailing the
new algorithm with the existing uniform-space chain algorithm gives
the minimum of their proven running times up to a constant factor,
without evaluating enormous counting bounds as stored integers.
The chain algorithm also retains its sharper fixed-dimensional
analysis when that dimension is fixed.

Actual-support generating-function estimates and componentwise
catalogue counts can replace UP5's support-composition estimate
on a prepared ground. However, the new exact interval rows can
change that ground's row structure. There is no automatic claim
that a fine bound on the original rows survives interval marking
unchanged; those estimates remain separately applicable analyses.

The RD disjoint-clique hidden-matching families have original support
count Q=T(b-1)/2 and require
exp(Omega(T log(2+Q/T))) oracle queries. They remain subclasses here.
The CS support-one family has Q=T/5 and requires 2^{Omega(T)}
queries. Thus these inherited matching-order families range from
Q=Theta(T) to Q=Theta(T^2). The separate increment
[one-support-pattern-target-lower-bounds.md](one-support-pattern-target-lower-bounds.md) also proves the Q=1
endpoint: it has a growing number 2 log_2(r)+1 of rows, targets r
and 3r/2, total T=Theta(r log r), and an explicit ground of r^2
elements. It gives 2^{Omega(T)} oracle queries and excludes
2^{o(T)} encoded-input time under ETH. This is a worst-case endpoint,
not a lower bound at fixed dimension, at every prescribed target
vector, or when the minimum-target occurrence bound is constant.

## 11. Limits and interfaces

The exact scalar is one optimization direction, or one threshold
decided by optimizing that same scalar. An additional unrelated
unbounded scalar constraint is not silently combined with another
objective. Every numeric row has nonnegative integer coefficients;
the useful-unit charging and finite profile counts do not apply to
cancellation by signed row entries.

One resource polymatroid is retained. Exact interval counts are
enforced through the coefficient-vector profile and its one
partition-count rank; no third independent resource rank is added.
The arbitrary scalar can remain signed because passive copies carry
their original scalar weight.

The aligned nonlinear transfer can first build its compressed band
rank and then apply this theorem. In that corollary Q counts the
eligible **band-column** support patterns, and targets must be
integer after any stated scaling. Convex upper rows, concave lower
rows, linear equalities, and the compatible scalar direction remain
necessary to that earlier exact transfer. This statement does not
extend it to nonlinear equalities.

## 12. Public comparison and attribution

Eisenbrand, Rohwedder and Wegrzycki, *Sensitivity, Proximity and FPT
Algorithms for Exact Matroid Problems*, arXiv:2404.03747v2,
Theorem 3, studies exact vector-weight bases through coefficient
magnitude and dimension. Its introduction explicitly credits the
earlier method of guessing each coefficient-vector multiplicity
and imposing the result through partition-matroid intersection.
That method is an established antecedent. Q here counts only
supports, so it can be much smaller than the number of coefficient
vectors even when positive magnitudes vary. Primary full text:
<https://arxiv.org/html/2404.03747v2>.

Knop, Pilipczuk and Wrochna, *Tight complexity lower bounds for
integer linear programming with few constraints*, arXiv:1811.01296v3,
studies ILP parameters including the number of rows, coefficient
magnitude and dual treedepth. The latter uses the graph joining two
rows when a column meets both. These are different structural
parameters and a different resource model. One support touching
all rows has Q=1 while that row graph is a clique; thus a small
support catalogue does not mean shallow row interaction.
Primary paper record and abstract:
<https://arxiv.org/abs/1811.01296v3>.

The new proved step is the useful-prefix and exact-interval
representation that prevents cover marking from destroying the
original-support bound while preserving full resource mass and
uniform polynomial workspace. A bounded primary-source comparison
does not establish publication priority, and no such claim is made.
