# Checkpoint R: exact numeric targets and broader resource models

**25 October 2026. Incremental research checkpoint.**
Only additions since checkpoint Q are included. All algorithms
in this checkpoint are deterministic.

## 1. Arbitrarily many overlapping rows: a tight target exponent

For one arbitrary integral polymatroid, integer vectors may belong
to its independent region or its full base. Allow any explicitly
listed number of overlapping nonnegative integer rows, each with
an upper, equality or covering relation. If T is the sum of
their integer targets, one arbitrary rational scalar objective
can be minimized or maximized exactly in

\[
       2^{O((T+1)\log(T+2))}\operatorname{poly}(H)
\]

time and polynomial binary space, uniformly in the row count.
An upper or lower side condition on that scalar is decided by
its corresponding exact extremum.

The order T log T is necessary in the general rank-oracle
model, already with 0/1 coefficients and targets all one.
The lower proof covers pure covering rows on independent
sets or bases, pure upper rows on bases, and exact scalar
maximization under pure upper rows on independent sets.

The new space-saving construction orders resource units
conceptually and uses the covering rows' first-reaching
prefixes. Their stopping order defines a chain. Only s+1
copies per coordinate are needed at a time. Exact vector
counts give an integral two-polymatroid subproblem. A
colored-token partition bound counts every visited profile
without materializing the tokens or resource units.

Full proof: variable_dimension_total_target_classification.md.

## 2. Fixed dimension and unequal targets

For fixed d overlapping rows the smaller time bound is

\[
       \exp\!\bigl(O_d((T+1)^{d/(d+1)})\bigr)
                         \operatorname{poly}(H),
\]

with a matching exponent-order query lower bound.
The first three dimensions give square-root, two-thirds
and three-quarters numeric exponents.

The strongest upper formula uses U_j=T_j for upper or
equality rows and U_j=2T_j-1 for positive covering rows.
After zero-cap preprocessing set

\[
 K(U)=\max_{\varnothing\ne S\subseteq[d']}
           \left(\prod_{j\in S}U_j\right)^{1/(|S|+1)}.
\]

The time is exp(O_d(K(U))) poly(H). For two caps,
K=max(sqrt(U_1),sqrt(U_2),(U_1U_2)^{1/3}); caps (1,N)
therefore have a square-root exponent in N. No pointwise
matching lower bound at every unequal-cap vector is claimed.

Full proof: fixed_dimensional_mixed_numeric_targets.md.

## 3. Exact optimization in the original optimum

All seven nontrivial single-matroid linear-constraint variants,
and their integral-polymatroid versions, admit exact target
decision in 2^{O(sqrt(T+1))} poly(H) and exact optimization
in 2^{O(sqrt(OPT+1))} poly(H) for integer objectives.
Space is polynomial. Both side directions remain exact;
mandatory bases retain every original required unit.
The square-root numeric exponent has a matching rank-oracle
lower bound. Exact objective equality with scalar optimization
is also covered.

For disjoint utility/load blocks under one global rank,
the exact mechanism gives

\[
       {q\choose r}\exp\!\bigl(O(r\sqrt{T+1})\bigr)
                         \operatorname{poly}(H).
\]

The selected blocks form an actual rank-r matroid basis.
Optional-resource fairness, mandatory-base fairness and
mandatory scheduling have separate complete proofs. One
global zero/passive group retains mandatory resource mass.
Shared setup-plus-assignment cost is exact. For compulsory
blocks put r=q and omit the binomial factor.

For a rational objective grid g, the optimization parameter
is OPT/g. This is an original numeric parameter, not
inverse approximation accuracy.

Full proofs: exact_numeric_target_single_matroid_scheme.md
and block_global_exact_numeric_target_schemes.md.

## 4. All-seven accuracy improvement

For rational 0<epsilon<=1, the refined scheme takes

\[
 \frac1\epsilon
 \exp\!\left(\frac{141}{50\epsilon}+7\right)
                         \operatorname{poly}(H_\epsilon).
\]

It gives (1+epsilon) for MIN and (1-epsilon) for MAX,
with the side inequality and mandatory-base requirement
exact. Binary polymatroids and polynomial space are supported.

The directly checked public unified bound displays
(1/epsilon^2)^{O(1/epsilon)}. The new proof removes its
displayed logarithmic factor from the upper exponent;
EPTAS existence and the seven-case formulation have
public antecedents.

The accompanying lower proof gives
2^{Omega(epsilon^-1/2)} rank queries for every variant.
The checked 2024 full version already announces a
quarter-power quantitative observation, which is credited.
The square-root lower and linear inverse-error upper
exponents remain different.

Full proofs: seven_variant_single_matroid_profile_scheme.md,
refined_single_matroid_accuracy_constants.md and
single_matroid_accuracy_lower_bound_audit.md.

## 5. Global resource coupling and mandatory fairness

One resource rank may couple all assignment coordinates;
it need not split by type. The approximation profiles
extend to this model. Mandatory-base fairness uses
charged active/passive copies sharing the same capacity.
Surplus units retain their true cost, so no mandatory
resource is deleted.

The max-min guarantee is (1-epsilon) in
binomial(q,r) exp(O(r/epsilon)) poly(H_epsilon) time.
Explicit adaptive scenarios may share one actual selected
basis while using separate resource vectors. Their gate
times add after fixing that basis. Every scenario retains
its own rank and exact budget.

Full proofs: global_polymatroid_profile_transfers.md,
mandatory_base_fair_allocation_passive_lift.md and
global_robust_profile_composition.md.

## 6. Compressed nonlinear models

Explicit binary-length marginal bands allow concave
utilities, convex assignment costs and convex processing
loads. Bands share original resource capacity. Canonical
prefix filling improves the required directions, yielding
equal original and lifted integer optima without unit
expansion.

For overlapping exact numeric targets the allowed shapes are:

| Row or objective | Coordinate shape |
|---|---|
| Upper target | Convex, nondecreasing, integer marginals |
| Covering target | Concave, nondecreasing, integer marginals |
| Equality target | Nonnegative integer linear coefficient |
| Scalar MIN | Convex, nondecreasing, rational marginals |
| Scalar MAX | Concave, nondecreasing, rational marginals |

These inherit the fixed-dimensional, unequal-target and
arbitrary-dimensional exact bounds, with polynomial
binary space. Linear subclasses inherit the lower bounds.
Genuinely nonlinear equalities are excluded by an explicit
false-positive example.

Full proofs: compressed_nonlinear_marginal_band_transfers.md
and aligned_nonlinear_mixed_numeric_targets.md.

## 7. Evidence and comparison status

The manuscripts contain complete proofs and have undergone
internal full-read mathematical review. No formal-verification,
external-peer-review or publication-priority claim is implied.
The source notes credit prior count-profile methods,
rank-FPT algorithms and lower bounds, recent randomized
kernels for structured intersections, and nonlinear PTASs.

The new guarantees are stated in the precise parameters
and representations actually proved. In particular, a
special case already having k^{O(k)} randomized time
is not presented as a new rank-FPT breakthrough.

Source notes: single_matroid_accuracy_primary_baselines.md
and numeric_target_primary_baselines.md.

## 8. Parent archive

Parent Q snapshot: 25 October 2026, 11:09:22 UTC.
Parent ZIP SHA-256:

    8ff7b58aafa78cf67747fcd58433f98d8968a11d03ee61c3041497b3b7fc96e5

The parent is not embedded. This package contains English
mathematical manuscripts, source notes and a manifest.
It contains no Lean, PDF, executable code or test bundle.
