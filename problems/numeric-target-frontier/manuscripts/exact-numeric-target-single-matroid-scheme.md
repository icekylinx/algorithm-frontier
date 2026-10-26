# Exact single-polymatroid optimization in square-root numeric-target time

**25 October 2026. Complete theorem and proof; full root and independent
internal reviews passed.** This is an exact numeric-parameter consequence of
the profile method, distinct from its approximation-accuracy bound.

For a nonnegative integer objective and one exact scalar side constraint,
all seven nontrivial single-matroid variants admit exact target decision
in

$$
2^{O(\sqrt{T+1})}\operatorname{poly}(H)
\tag{NT1}
$$

time and polynomial binary space. Here `T` is the queried integer
objective threshold, included in the input encoding. The proof covers
one arbitrary integral polymatroid with binary capacities. Exact
optimization follows in `2^{O(sqrt(OPT+1))} poly(H)` time. The hidden
equal-sum family in the separately audited lower-bound note gives a
matching square-root exponent in this numeric parameter, in the oracle
model. No publication-priority claim is made.

## 1. Model and exact gates

Let `F` be a normalized monotone integral submodular rank on an explicit
coordinate ground `E`, with `R=F(E)`. The integer feasible resource
vectors are either those of `P(F)` or those of `B(F)`. Original
eligibility restrictions are given. A base must retain the original
rank after such restrictions. The objective coefficients satisfy

$$
v_e\in\mathbb Z_{\ge0}.
\tag{NT2}
$$

There is one nonnegative rational side vector `w`, a nonnegative rational
threshold `L`, and a chosen side relation `w*x<=L` or `w*x>=L`.
The objective is minimized or maximized. The integer `T>=0` is an
objective threshold; it is not the side threshold `L`.

The exact target questions are:

1. MIN: does a legal integer vector satisfy `v*x<=T`?
2. MAX: does a legal integer vector satisfy `v*x>=T`?

A successful gate returns an actual original legal vector. Complete
failure means the corresponding exact target is impossible.

The optional independent-vector family is first represented as a base
using a free zero-objective, zero-side-weight disposal coordinate `0`.
On `E union {0}` define `Fhat(S)=F(S)` when `0` is absent and
`Fhat(S)=R` when `0` is present. This is an integral polymatroid rank,
and `x in P(F)` extends to its base by setting `x_0=R-x(E)`; projecting
any such base gives exactly `P(F)`. This transformation is exact in
both side directions and adds one coordinate of binary capacity.
Original mandatory bases do not receive free disposal. Hence it is
enough to prove both gates for a base family, with its full original
total `R`.

Exact side feasibility is tested by minimum or maximum `w` on that
base face, according to the required side direction. If it fails, the
original constrained family is empty. Otherwise it gives a legal
initializer. Rank zero is immediate. The encoding `H` includes all
binary data, `T`, and paid polynomial oracle/LP/intersection work.

## 2. Exact count profiles and a polynomial integral subproblem

Suppose the current ground is divided into groups `D_a` of identical
nonnegative integer auxiliary objective coefficient `a`. Enumerate
counts `h_a` only for occupied positive groups. For a prescribed
positive-count profile, put

$$
m=\sum_{a>0}h_a,\qquad W=\sum_{a>0}a h_a,
 \qquad h_0=R-m.
\tag{NT3}
$$

Profiles with `m>R` are rejected. The zero group contains every current
coordinate with auxiliary value zero. It may be empty, in which case
a positive required `h_0` will simply make the profile infeasible.

The inequalities `x(D_a)<=h_a`, including the zero group, define an
integral partition-count polymatroid `K_h`. Its rank on a subset is
the sum of `h_a` over the groups that the subset meets. On a matroid
resource, ordinary partition-matroid capacities give the same
intersection because the resource already enforces singleton bounds
one.

Intersect `P(F_current)` with `P(K_h)` at the required total `R`.
The total-`R` intersection is an integral maximum-total face whenever
it is nonempty: resource rank bounds the total by `R`, and two
integral polymatroids have an integral intersection. Since the group
caps sum to `R`, every one of them is tight on this face. Thus the
profile imposes **exact** group counts, not only upper bounds.

Minimize `w*x` on this integral face for an upper side inequality,
or maximize it for a lower one. Comparing the attained value with `L`
decides whether an integer vector with this profile meets the side row.
If so, an integral optimizer is a valid witness. This is polynomial
work per profile in the exact oracle model. The side inequality is
enforced by scalar optimization; it is not assumed to preserve
integrality when added as a halfspace.

## 3. A cumulative partition bound with polynomial space

For an integer `U>=1`, the number of nonnegative count profiles with

$$
\sum_{a>0}a h_a\le U
\tag{NT4}
$$

is at most the number of integer partitions of all weights up to `U`.
There is one group for each distinct occupied positive coefficient,
so the mapping to partitions is injective. Its generating-function
bound, for any `t>0`, is

$$
\#\text{profiles}
 \le e^{tU}\prod_{j\ge1}(1-e^{-tj})^{-1},
 \qquad
 \log\prod_{j\ge1}(1-e^{-tj})^{-1}
 =\sum_{\ell\ge1}\frac1{\ell(e^{t\ell}-1)}\le\frac2t.
\tag{NT5}
$$

Taking `t=1/sqrt(U)` gives at most `exp(3 sqrt(U))` profiles.
For `U=0` there is only the all-zero positive profile.

This is also the all-input enumeration bound. Stream the occupied
positive values in any fixed order. At a state of current count `m`
and weight `W`, enumerate the next value's count in the range

$$
0\le h_a\le
       \min\{R-m,\lfloor(U-W)/a\rfloor\}.
\tag{NT6}
$$

Every generated partial profile has an all-zero positive completion
meeting the combinatorial count and weight caps. At a fixed depth,
distinct prefixes have distinct such complete profiles. The total
traversal therefore has only a polynomial factor more nodes than
complete profiles. The proof does not require those profiles to be
resource-feasible; their failed integral subproblems are included.

Only input-occupied values are stored. Profile counts, `h_0`, partial
weights and rank values are binary. The algorithm uses neither a
table of length `U` nor an expansion into `R` unit copies. All per-state
work and working space are polynomial in the full binary encoding.

## 4. Exact MIN target gate

For a target `T`, forbid every coordinate of original coefficient
`v_e>T`, retaining the required total `R`. No integer vector of
objective at most `T` can use such a coordinate. If the resulting
rank falls below `R`, the target fails.

Group the remaining coordinates by their exact original integer value.
Enumerate profiles with `W<=T` using NT6 and `U=T`. On each, apply the
integral scalar-side optimization of Section 2. A successful profile
returns an original legal base of objective exactly `W<=T`. Conversely,
any original integer target witness has one of these exact count
profiles and passes its side test.

This proves an exact gate in

$$
\exp(3\sqrt T)\operatorname{poly}(H)
\tag{NT7}
$$

time for `T>=1`, and polynomial time for `T=0`. The zero case is just
the original-total side-feasibility optimization on zero-value
coordinates. Both side directions are supported.

## 5. Exact MAX target gate with charged passive copies

The target `T=0` is resolved by original feasibility. Assume `T>=1`.
Replace each current coordinate by an active and a passive copy with
shared rank

$$
F^{\uparrow}(S)=F(\pi(S)).
\tag{NT8}
$$

Their aggregate `x_e=z_{e^a}+z_{e^p}` is in `B(F)` exactly when the
lifted vector is in `B(Fup)`. Both copies retain the original side
weight `w_e`. Give the active copy integer auxiliary value
`min(v_e,T)` and the passive copy value zero. The original objective
after aggregation is at least the auxiliary objective.

If an original integer base has objective at least `T`, capping retains
that target. In an arbitrary order of its positive capped units, mark
only a first-reaching prefix active and mark all remaining units
passive. The active sum is an integer `W` satisfying

$$
T\le W\le2T-1.
\tag{NT9}
$$

No original count or side contribution changes. In particular this
operation is valid with a lower covering side row and with a mandatory
base. It is an existence argument; no unit list is materialized.

Group lifted coordinates by their exact auxiliary integer values.
Enumerate all positive profiles with `W<=2T-1`, count at most `R`,
and retain those with `W>=T`. The passive and other zero-value
coordinates form the zero group with prescribed count `R-m`.
Apply Section 2's original-total integral side optimization.

Success returns a full lifted base of auxiliary objective exactly
`W>=T` and with the required side row. Aggregation gives an original
legal base of objective at least `T`. Conversely, the marking of an
original target witness supplies a retained profile, so complete
failure is sound. The exact target gate takes at most

$$
\exp(3\sqrt{2T-1})\operatorname{poly}(H)
\tag{NT10}
$$

time and polynomial space. In originally optional problems, project
away only the separate free disposal coordinate after aggregation.

## 6. Exact optimization depends on the integer optimum

After original feasibility is decided, exact objective optimization
does not need a large numeric upper bound in its exponent.

For MIN, first test target zero. If it fails, query targets
`1,2,4,...` until the first success. The first successful target is
at most `2 OPT`, and all previous targets are smaller. Binary-search
the integer interval between the last failure and the first success
using the exact gate. The final successful target is OPT, and its
saved actual vector is optimal.

For MAX, query targets `1,2,4,...` until the first failure. If the
first fails, OPT is zero. Otherwise the first failed target is at
most `2 OPT`, and the last success is a lower bound. Exact binary
search between them ends at OPT and returns its saved exact witness.

The number of calls is polynomial in the binary encoding since
`OPT<=R*max(v)`. All queried targets are `O(OPT+1)`. Therefore both
directions, and hence all seven variants, have exact optimization time

$$
2^{O(\sqrt{\mathrm{OPT}+1})}
                    \operatorname{poly}(H)
\tag{NT11}
$$

and polynomial workspace. The trivial minimum-independent-upper-budget
case is solved by zero as usual.

## 7. Exact objective equality and an arbitrary scalar objective

The same profile mechanism also solves `v*x=T` over a required base:
use the original-value groups and retain only profiles of exact weight
`T`. On every resulting integral face one may minimize or maximize a
separate rational functional `w`; take the best across profiles.
Thus exact-weight feasibility and scalar optimization over an exact-
weight base family have time `2^{O(sqrt(T+1))} poly(H)` and polynomial
space for nonnegative integer exact-weight coefficients.

This is an equality statement, not a claim that general signed exact
weights have the same parameterization. Negative exact-weight
coefficients can cancel, invalidating NT4's bounded partition weight.

## 8. Matching numeric-target oracle exponent

The separately reviewed
[single-matroid-accuracy-lower-bound-audit.md](single-matroid-accuracy-lower-bound-audit.md) constructs rank-`k`
matroids on `n` labels with a hidden equal-sum `k`-set. For every one
of the seven variants, its unique optimum has integer objective
`B=Theta(n^2)`, and all other feasible outputs are at least one integer
unit worse. The rank oracle differs from a feasible reference instance
only on the hidden set, among `2^{n-O(log n)}` possibilities.

Set the queried objective threshold to `T=B`. Exact MIN or MAX target
decision distinguishes the hidden instance from the reference:
the former meets the objective threshold and the latter does not.
The same indistinguishability argument yields

$$
2^{\Omega(\sqrt T)}
\tag{NT12}
$$

worst-case rank queries. This includes randomized decision algorithms
with success probability at least `2/3` on every instance: use the
distribution assigning probability `1/2` to the reference and `1/2`
to a uniformly random hidden instance. For a fixed random seed, at
most `Q` candidates can be hit by the reference transcript of `Q`
queries. The two transcript distributions have total variation at
most `Q/N`, where `N=2^{n-O(log n)}` is the candidate count, so average
decision success is at most `1/2+Q/(2N)`. Consequently `Q>=N/3` is
necessary. A constant success threshold no larger than `1/2` would
not suffice for this binary-decision conclusion.

Exact optimization must return the hidden optimum and has the same
barrier in `sqrt(OPT)` on these instances, by the output-search
argument in the lower-bound note. The exact equality problem also
inherits the original equal-sum construction directly, with target
`alpha=Theta(n^2)`.

Hence the square-root order in the numeric exponent is tight in the
oracle model. This does not specify an optimal constant in that
exponent and does not imply the same lower bound for a particular
explicit matroid class.

## 9. Primary baseline and the accuracy gap

Eisenbrand, Rohwedder and Wegrzycki,
*Sensitivity, Proximity and FPT Algorithms for Exact Matroid Problems*,
arXiv v2 (24 August 2024), Theorem 3, gives an FPT algorithm in the
number of exact-weight dimensions and the maximum absolute coefficient.
Its introduction explicitly credits the approach of guessing counts
for each weight vector and then using a partition-matroid intersection.
Thus count-profile intersection is an established technique. The
numeric target `T`, nonnegative coefficient condition, scalar side
optimization, and binary polymatroid scope above are the parameters
and interfaces proved here, not a first count-enumeration claim.

Primary source:
<https://arxiv.org/pdf/2404.03747>.

The 2024 oracle no-pseudopolynomial theorem is consistent with NT1:
`2^{O(sqrt(T))}` is not polynomial in the numeric target. Its hidden
family supplies the matching exponent just explained. This bounded
source comparison does not establish publication priority.

Finally, NT11 is not an approximation scheme with square-root accuracy
dependence. Scaling arbitrary objective coefficients to integers
usually introduces the number of selected units into the scaled
objective bound. The current EPTAS profiles instead have weighted
integer size of order `1/epsilon^2`, whose partition bound is
`2^{O(1/epsilon)}`. A new argument would be needed to obtain a uniformly
smaller accuracy exponent. The numeric-target and accuracy parameters
must not be interchanged.
