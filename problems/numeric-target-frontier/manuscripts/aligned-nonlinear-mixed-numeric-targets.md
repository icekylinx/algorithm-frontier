# Exact aligned nonlinear numeric targets under one global polymatroid

**25 October 2026. Complete incremental theorem and proof;
full root and independent internal reviews passed.** This note transfers the mixed
numeric-target algorithms to explicitly compressed separable nonlinear
functions. The target rows may overlap arbitrarily. It does not claim
that arbitrary nonlinear equality constraints can be linearized.

Companion proofs are [compressed-nonlinear-marginal-band-transfers.md](compressed-nonlinear-marginal-band-transfers.md)
(NB), [fixed-dimensional-mixed-numeric-targets.md](fixed-dimensional-mixed-numeric-targets.md) (MD),
[mixed-target-cover-chain-compression.md](mixed-target-cover-chain-compression.md) (CC), and
[variable-dimension-total-target-classification.md](variable-dimension-total-target-classification.md) (VT). The reduction
and the exact comparison argument are proved below, including the
binary-capacity implementation and the equality limitation.

## 1. The theorem

Let F be one normalized monotone integral polymatroid rank on an
explicit coordinate ground E. Write

```math
P(F)=\{x\ge0:x(S)\le F(S)\text{ for every }S\subseteq E\},
 \quad R=F(E),\qquad B(F)=\{x\in P(F):x(E)=R\}.
 \tag{AN1}
```

The resource vector x is integer and belongs either to P(F) or to
B(F). Every coordinate has a binary integer domain 0<=x_e<=d_e,
and an original eligibility mask is allowed. A mandatory base always
retains the original total R in AN1, including after domain and
eligibility restrictions.

For j=1,...,d, prescribe a nonnegative integer target T_j and a row

```math
A_j(x)=\sum_{e\in E} A_{je}(x_e)\ \rho_j\ T_j,
 \qquad \rho_j\in\{\le,=,\ge\},\qquad
 T=\sum_{j=1}^d T_j.
 \tag{AN2}
```

Every A_je is zero at zero, nondecreasing, and given by an explicit
list of constant nonnegative **integer marginal slopes** on integer
intervals. The function shapes must agree with the row directions:

| Row | Required shape of every coordinate function |
|---|---|
| A_j(x)<=T_j | Discretely convex: marginal slopes are nondecreasing |
| A_j(x)>=T_j | Discretely concave: marginal slopes are nonincreasing |
| A_j(x)=T_j | Linear: A_je(k)=a_je k for one nonnegative integer a_je |

The scalar objective is

```math
W(x)=\sum_e W_e(x_e).
 \tag{AN3}
```

It is zero at zero, nondecreasing, and given by explicit rational
nonnegative marginal slopes. For **MIN W**, require convex W_e.
For **MAX W**, require concave W_e. All functions on a coordinate
use the same integer ordering of its resource units. Their
breakpoints need not initially agree.

There is an exact deterministic algorithm that detects infeasibility
and computes the chosen scalar optimum, together with an actual
integer resource vector. For fixed d its running time is

```math
\exp\!\bigl(O_d((T+1)^{d/(d+1)})\bigr)
                                  \mathrm{poly}(H).
 \tag{AN4}
```

When d is part of the input, the running time is

```math
2^{O((T+1)\log(T+2))}\mathrm{poly}(H).
 \tag{AN5}
```

Both statements use **polynomial binary workspace**, uniformly in
the full input encoding for AN5. H includes all explicit marginal
bands, their binary lengths and slopes, the rows and targets, and
the paid polynomial rank-oracle, submodular-minimization and weighted
polymatroid-intersection operations. There is no expansion into
individual resource units.

The sharper fixed-dimensional bound keeps the individual targets.
After removing zero targets as described below, let

```math
U_j=\begin{cases}T_j,&\rho_j\in\{\le,=\},\\
                  2T_j-1,&\rho_j=\ge,
       \end{cases}
 \qquad
 K(U)=\max_{\varnothing\ne S\subseteq[d']}
             \left(\prod_{j\in S}U_j\right)^{1/(|S|+1)}.
 \tag{AN6}
```

Here d' is the number of positive remaining caps. If d'=0 the
problem is polynomial. Otherwise the bound is exp(O_d(K(U)))
poly(H). The constants are for fixed d; AN5 is the separate
uniform statement for variable d.

An additional exact constraint W(x)<=C is decided by **MIN W**
when W is convex, and W(x)>=L is decided by **MAX W** when W is
concave. This is one side condition on the same scalar being
optimized. No second unrelated scalar objective under that
additional condition is asserted. Other nonlinear constraints
can be among AN2 when their marginal slopes and target magnitudes
meet its stated conditions; their targets then contribute to T.

## 2. Explicit domains and common marginal refinement

Each supplied function must be defined on the whole integer interval
{0,...,d_e}. A missing tail is not extrapolated. If d_e>F({e}),
truncate its unreachable tail to F({e}); a smaller supplied domain
is a real cap, not a change in the original mandatory total. A
coordinate with domain zero is forced to zero and has no bands.

Merge the breakpoints of all d row functions and the scalar function
at each coordinate. Write the common refinement as

```math
0=b_{e0}<b_{e1}<\cdots<b_{em_e}=d_e,
 \qquad \ell_{ei}=b_{ei}-b_{e,i-1}>0.
 \tag{AN7}
```

Let a^j_ei be the row-j marginal and w_ei the scalar marginal
on the i-th interval. Refinement preserves every monotonicity
direction. It has at most the sum of the original numbers of
breakpoints; storing the d+1 slopes on each refined interval
has polynomial size in the full explicit input. Binary interval
lengths are not replaced by that many coordinates.

For an integer count k define its canonical prefix representation

```math
z^*_{ei}(k)=\min\{\ell_{ei},\max\{0,k-b_{e,i-1}\}\}.
 \tag{AN8}
```

Then A_je(k)=sum_i a^j_ei z^*_ei(k) and
W_e(k)=sum_i w_ei z^*_ei(k), exactly. All-zero bands and bands
with zero target coefficients but nonzero scalar weight remain
available. Such bands can be necessary for a mandatory total or
an optimal scalar value.

## 3. One shared, box-capped resource rank

Let D={(e,i)} be the explicit band ground and let pi forget the
band index. Put H_0(S)=F(pi(S)). This is an integral polymatroid
rank. Indeed, projection preserves unions and maps intersections
into intersections; submodularity and monotonicity of F give
submodularity of H_0.

For z>=0, put x_e=sum_i z_ei. The full inverse image of any
original set proves one implication, and
z(S)<=x(pi(S)) proves the other in

```math
z\in P(H_0)\quad\Longleftrightarrow
                  \quad x\in P(F).
 \tag{AN9}
```

Impose the binary band capacities through the rank

```math
G(S)=\min_{Y\subseteq S}\{H_0(Y)+\ell(S\setminus Y)\}.
 \tag{AN10}
```

This is normalized, monotone, integral and submodular, with

```math
P(G)=P(H_0)\cap\{0\le z\le\ell\}.
 \tag{AN11}
```

For completeness, monotonicity follows by intersecting a minimizer
for a larger set with the smaller set. Submodularity follows by
using minimizers Y_A,Y_B for A,B: submodularity of H_0 and the
modular identity for the remaining capacities bound their sum
below the candidates Y_A union Y_B and Y_A intersect Y_B.
For AN11, a vector on the right satisfies z(S)<=H_0(Y)+
ell(S minus Y) for every Y. Conversely G(S)<=H_0(S), and
G({i})<=ell_i gives all box constraints.

A rank query needs only submodular minimization on the original
ground, because

```math
G(S)=\min_{A\subseteq E}
     \left\{F(A)+\sum_{e\notin A}
                     \ell(S\cap\pi^{-1}(e))\right\}.
 \tag{AN12}
```

Once a set Y contains any S-band of e, including every other
S-band of e does not change its projected rank and can only
reduce the remaining modular cost. Thus a minimizing Y may be
taken to be a union of whole fibers inside S. Conversely, any
original A supplies just such a candidate; removing coordinates
outside pi(S) cannot increase F. This proves AN12. Its minimized
function is submodular plus a modular term and a constant.

In particular,

```math
\{\mathrm{agg}z:z\in P(G)\}
           =P(F)\cap\{0\le x\le d\}.
 \tag{AN13}
```

The reverse inclusion uses the canonical vector AN8; the forward
inclusion uses AN9 and the band caps. The statement is exact
both for real vectors and for integer vectors.

Restrict D to fibers of the original eligibility mask. In the
mandatory case a feasible original resource base exists only if
the restricted G-rank equals the original R; if it does, its
total-R base is the required representation. All subsequent
internal row masks retain R. In the optional case use P(G) on
the eligible band ground. If a base representation is wanted,
one legitimate zero-row, zero-scalar disposal coordinate fills
its missing total up to the rank of that eligible band domain.
It is not an original mandatory resource unit.

## 4. Canonical repacking improves all directions simultaneously

Take any band vector 0<=z<=ell and fix an original coordinate e.
Let k=sum_i z_ei. For every h<m_e, its cumulative prefix satisfies

```math
Z_h=\sum_{i\le h}z_{ei}\le\min\{k,b_{eh}\}
                       =\sum_{i\le h}z^*_{ei}(k)=Z^*_h.
 \tag{AN14}
```

For any slope sequence v_i, summation by parts gives

```math
\sum_i v_i(z^*_{ei}-z_{ei})
       =\sum_{h<m_e}(v_h-v_{h+1})(Z^*_h-Z_h).
 \tag{AN15}
```

The total difference is zero, so there is no final-boundary term.
Consequently the same prefix vector has every one of these
properties:

- It weakly decreases each convex upper-row contribution.
- It weakly increases each concave lower-row contribution.
- It preserves each linear equality-row contribution exactly.
- It weakly decreases a convex scalar cost being minimized.
- It weakly increases a concave scalar reward being maximized.

Repacking keeps the aggregate x unchanged, and hence keeps all
original resource constraints, domains, support and mandatory
totals unchanged. Computing AN8 for every band takes polynomial
arithmetic time; no unit-by-unit exchange sequence is needed.

This agreement of directions is the meaning of “aligned.” It
does not require the slopes of different functions to be equal.
Convex and concave rows may coexist on the same coordinate,
because their required inequality directions are opposite.

## 5. Exact feasibility and scalar optimum correspondence

Consider the following linear band instance:

```math
z\in P(G)\cap\mathbb Z^D
       \quad\text{or the required total-R base},\qquad
   \sum_{e,i}a^j_{ei}z_{ei}\ \rho_j\ T_j,
 \qquad \text{optimize }\sum_{e,i}w_{ei}z_{ei}.
 \tag{AN16}
```

Every original feasible integer x has the canonical lift AN8,
which preserves **all** row values and the scalar value exactly.
Conversely, every feasible integer z in AN16 aggregates to an
original integer resource vector x. Repacking AN15 shows that
x satisfies every original inequality and every equality.

For MIN, W(x)<=wz. Therefore the minimum of AN16 is at most
the original minimum by canonical embedding, and the original
minimum is at most the minimum of AN16 by decoding. They are
equal. For MAX, W(x)>=wz; the two inequalities reverse, with
the same equality conclusion. Infeasibility is equivalent as
well. An optimal linear output decodes to an original optimum:
if its scalar value improved strictly, its own canonical lift
would contradict linear optimality.

The decoding of a nonoptimal output need not preserve its
scalar value exactly; it improves it in the relevant direction.
This suffices for an exact original upper cost budget or lower
reward requirement. It does **not** preserve an equality on a
genuinely nonlinear scalar.

The linear target algorithm may internally forbid an individual
band because a nonnegative integer row coefficient exceeds an
upper or equality target. Canonical repacking can later use
another band of the same original coordinate. This is harmless:
an internal band mask is not an original eligibility restriction,
and AN15 proves the original target condition after repacking.
Every original feasible witness initially has a canonical lift
that survives such masks. Whole-fiber original eligibility is
always retained.

## 6. Applying the exact mixed-target algorithms

All target coefficients in AN16 are nonnegative integers and
the scalar coefficients are rational. Thus it is an instance
of the linear mixed-target theorem with exactly the same
row count and right-hand sides. Its resource rank is one G,
not an intersection of two unrelated resource ranks.

Here is the relevant implementation, to make the variable-d
workspace claim explicit. Remove covering rows with target
zero. Upper and equality rows with zero target mask every
positive-coefficient band and are then removed. Retain every
required base total; a rank loss in a mandatory representation
certifies infeasibility. All remaining row targets are positive,
so their count is at most T.

Let s be the number of covering rows. Stream all s! permutations
of them. For one permutation create only its decreasing chain
of s+1 active subsets, and s+1 shared copies of each current
band. The shared rank forgets the chain index and evaluates G.
All chain copies retain the true scalar slope. Upper and
equality rows retain their coefficient in every copy. A
covering row receives min(a^j_ei,T_j) in copies where it is
active and zero otherwise.

Completeness needs only one conceptual common order of the
resource units. For each covering row mark its first-reaching
prefix in that common order after coefficient capping. Its
integer sum lies in [T_j,2T_j-1]. Sorting the stopping positions
gives one streamed chain; ties yield empty intermediate layers.
No unit list is constructed. Conversely, credited covering
totals are never larger than true linear covering totals.

For a chain, group coordinates by their complete auxiliary
coefficient vector b. Guess the counts h_b for occupied nonzero
vectors, enforcing every component upper cap U_j and the
required total. A single zero-vector group fills the remaining
resource total. Intersect the shared rank with the partition-
count rank and take the original full-total face. Their integral
intersection and the equality of total prescribed capacities
force every group count to be exact. Exact scalar optimization
on that integral face supplies a valid integer output or a
proof that this profile is empty.

For fixed d, the number of component-capped vector profiles is
bounded by the multivariate-partition estimate

```math
\log\mathcal P(U)\le
 \sum_j t_jU_j+
       2\sum_{\varnothing\ne S\subseteq[d']}
                          \prod_{j\in S}t_j^{-1}.
 \tag{AN17}
```

Set t_j=K(U)/U_j. Each product is at most K(U), giving
log P(U)<= (d'+2(2^{d'}-1)) K(U). The s! factor is constant
for fixed d. Alternatively the total-target form gives AN4.
These analytic real parameters are used only in counting;
the algorithm uses exact integer upper bounds on profile
counts.

For variable d, put U=sum_j U_j<=2T. A profile injects into
a partition of U distinguished colored tokens plus one marker:
each vector occurrence becomes a block with its color counts,
and the unused tokens accompany the marker. Reading the
nonmarker blocks recovers the profile. Therefore

```math
\mathcal P(U_1,\ldots,U_{d'})\le
        \mathrm{Bell}(U+1)\le(U+1)^{U+1},
 \qquad s!\le T!.
 \tag{AN18}
```

These bounds prove AN5. The tokens are only a counting device.
No object of numeric length T is materialized.

## 7. All-input binary time, space and zero cases

For the next occupied vector b, the streamed depth-first count
range is bounded by the remaining resource total and by

```math
\min_{j:b_j>0}
                   \left\lfloor\frac{U_j-W_j}{b_j}\right\rfloor,
 \tag{AN19}
```

where W_j is the current component total. Every visited partial
profile has a zero completion satisfying these upper caps.
At each depth those completions are distinct. Thus all visited
states, including failed target filters and failed integral
subproblems, are charged by the same profile count up to a
polynomial occupied-depth factor. Bounding only the total l1
weight and checking component caps at the end would not prove
the dimension-free AN18 bound.

At most (d+1)|D| shared chain coordinates are stored at once,
each with d row entries. Refinement, chain construction, rank
queries, sorting occupied vectors, and exact integral subproblems
all have polynomial full-input encoding. Count registers are
binary and bounded by rank or targets; recursion depth is the
number of occupied vectors. The ground is independent of the
sum of band lengths and of the numeric value of T. Nested rank
queries call AN12 and therefore use polynomially many original
oracle operations per ordinary subproblem. Chains and profiles
are processed one at a time.

When T=0, the zero upper/equality masks and removal of zero
covering rows leave only scalar optimization on one rank with
its legitimate total convention. This is polynomial; AN5 is
well defined there. If R=0, only x=0 is possible, so every
positive covering demand fails and every zero-normalized
scalar has value zero. Empty band grounds and zero domains
are handled by the same rules.

Functions may have zero slopes and repeated slopes. A mandatory
base must retain zero-row and zero-scalar coordinates when they
carry necessary resource mass. No free deletion is used in
the mandatory reduction.

## 8. Rational row scaling and parameter interpretation

The main theorem assumes integer target slopes and integer
targets. If a row instead has rational nonnegative slopes on
a known positive common grid g_j, divide that row by g_j.
For an upper target use floor(T_j/g_j); for a lower target use
ceil(T_j/g_j). For a linear equality, a nongrid target makes
the instance infeasible; otherwise divide it exactly.

The running-time parameter is the sum of these **scaled integer
targets**, not an unscaled sum of rational demands. The row
grids may be found by rational arithmetic from the explicitly
listed slopes. Their binary encoding is polynomial, but their
numeric rescaling can be large and is not hidden in AN4 or AN5.
The rational scalar slopes do not contribute to T; their full
bit lengths are paid in H.

No approximation-accuracy exponent follows from these exact
numeric-target bounds. T is a demand parameter, not 1/epsilon.

## 9. Tightness inherited from linear subclasses

Every linear row is both convex and concave, and every linear
scalar of nonnegative coefficients is admissible for both
scalar directions. The rank-oracle lower constructions of MD
and VT therefore remain subclasses of the present theorem.

For each fixed d, d linear equality rows on ordinary matroid
bases give the lower bound

```math
\exp(\Omega_d(T^{d/(d+1)})).
 \tag{AN20}
```

It concerns the worst-case target-exponent order; it does not
assert a matching lower bound for every anisotropic target
vector. The same fixed-d lower family can be phrased using d
covering rows and one exact convex scalar cost budget. If the
original equality targets sum to T, replace them by covers and
give a coordinate cost equal to the sum of its row coefficients.
The budget is T. All covers and that budget together force
every original equality. Costs are nonnegative and linear.

For arbitrary d, VT's perfect-matching-label oracle family uses
only 0/1 linear rows with all targets one. It gives
2^{Omega(T log T)} queries, even for pure covering rows on
independent sets or bases, or pure upper rows on bases. A zero
scalar objective is admissible. Thus AN5 has tight target-
exponent order in this oracle model, without needing any
genuinely nonlinear function.

The lower bounds apply to bounded-error randomized decision
as stated in their source proofs. They concern an arbitrary
matroid given by a rank oracle, not an explicitly represented
graphic, linear or laminar matroid. This note makes no stronger
lower claim for those representations.

## 10. Why nonlinear equalities and misaligned directions are excluded

Take one optional coordinate with capacity two and concave
utility marginals 2,1. Its possible actual utility values are
0,2,3. The nonlinear equality A(x)=1 is infeasible. In the
band representation, one unit placed only in the second band
has linear value one and is resource feasible. Repacking moves
it to the first band and changes the actual value to two.
Thus allowing a nonlinear equality would introduce a false
positive. Convex marginals 1,2 give the analogous failure at
target two. The optional counterexample suffices; a mandatory
version adds a zero-valued coordinate and a shared total-two
rank, so the unused one unit can fill the mandatory total.

The scalar shape restriction is also substantive. With one
coordinate of capacity two, the linear row x<=1, and convex
scalar marginals 1,2, maximizing the unrestricted band scalar
chooses one unit in the second band with value two. The actual
convex scalar at every allowed original count is at most one.
Thus a convex MAX objective would not have the exact optimum
correspondence. The reversed MIN shape fails analogously.

There is one global resource rank. Adding an unrelated second
resource rank would generally leave three ranks in the exact
profile intersection and invalidate its integral recovery
argument. All marginal descriptions are explicit; no polynomial
compression of an arbitrary nonlinear value oracle is assumed.
These boundaries are properties of the proof, not claims that
every excluded model is impossible.

## 11. Public antecedents and comparison scope

Eisenbrand, Rohwedder and Wegrzycki, *Sensitivity, Proximity and
FPT Algorithms for Exact Matroid Problems*, arXiv:2404.03747v2,
Theorem 3, studies exact vector-weight matroid bases parameterized
by coefficient magnitude and dimension. Its introduction
explicitly describes guessing counts of weight vectors and
imposing them by partition-matroid intersection. That recovery
technique is an established antecedent, not a new claim here.
Primary full text:
<https://arxiv.org/html/2404.03747v2>.

Shioura, *Polynomial-Time Approximation Schemes for Maximizing
Gross Substitutes Utility Under Budget Constraints*, Mathematics
of Operations Research 40(1), 192--225, studies nonlinear budgeted
optimization in the more general M-natural-concave setting.
Its primary publisher abstract states PTAS results, including
a sum of two such functions under a single budget. The present
result instead uses explicit separable marginal bands and an
exact nonnegative numeric-target parameter. This is a model
and parameter comparison, not a claim to the first nonlinear
budget algorithm or a full runtime comparison with that paper.
Primary publisher page:
<https://pubsonline.informs.org/doi/abs/10.1287/moor.2014.0668>.

The claimed increment is the exact simultaneous canonical
repacking interface, with binary band capacities, original
mandatory totals, compatible overlapping nonlinear inequalities,
and the inherited tight numeric-target exponents. No publication-
priority claim is made.
