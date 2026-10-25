# Public comparison for the factor-four recipient-polymatroid transfer

**25 October 2026. Source and derived-baseline scope check.**

This note updates the comparison after prefix normalization reduced
the research factor from five to four and the contraction-loss proof
extended the model from recipient matroids to arbitrary integral
recipient polymatroids. It distinguishes printed theorems, elementary
consequences, and the new internally reviewed construction.

## 1. Current research claim

Let M be an arbitrary player-selection matroid of rank r on q explicit
players. Each resource type has a common intrinsic unit value and an
arbitrary integral recipient polymatroid, supplied by a rank-value
oracle with binary-encoded capacities. Unused capacity is permitted.
With exact available-count optimization, the reviewed research bound is

\[
 \begin{array}{ll}
 4-3/r & \text{in }2^{O(r)}\operatorname{poly}(H),\\
 4-3/r+\eta & \text{in }\operatorname{poly}(H)
   \min\{2^{O(r)},(r+1)^{O((1+\eta^{-1})\log(r+1))}\}.
 \end{array}
\]

The initial comparator for full recipient polymatroids is integer optimum.
The stronger residual-capacity configuration relaxation now also has
the stated bound, by `recipient_polymatroid_residual_configuration_relaxation.md`.
That relaxation adds valid residual cuts, and no polynomial separation
or optimization theorem for all its cuts is claimed.
The weaker aggregate count-configuration LP does not admit this constant
comparison; its explicit gap is recorded in the separate gap note.
For one-service recipient matroids, the stronger coupled configuration
comparator is retained. For supplied scaled-matroid components, the
separate component comparator is retained as proved in its own note.

The proof is different from merely increasing the running time of a
printed public local search. It maintains independence of every
unmarked matching block after contraction of every ordered center
prefix, actively releases every currently redundant center, and charges
the current rank deficit. This repairs the failure of historical
birth-time charges and makes the coefficient 2B+min(u,B) available.

## 2. The printed general-recipient baseline

Bamas, Lindermayr, Megow, Rohwedder and Schloeter,
*Santa Claus meets Makespan and Matroids: Algorithms and Reductions*,
arXiv:2307.08453v1 (SODA 2024), Theorem 4, state polynomial
8+epsilon for general values and polynomial 4+epsilon for two values
in their resource-matroid model, including its polymatroid formulation.
Their Corollary 5 gives polynomial 7/4+epsilon for two-size
job-matroid makespan. The primary manuscript is
<https://arxiv.org/html/2307.08453v1>.

Thus the new general-value result improves the approximation quality
in a different time regime. It is not a polynomial-time dominance
claim. On the two-value special case, the public polynomial
4+epsilon theorem already has the limiting coefficient four.

## 3. Arbitrary player selection is already a public consequence

For the basic model without additional player-local bundle restrictions,
the public compulsory-player model extends to arbitrary player
selection by adding a dummy resource whose recipient matroid is M*.
Give it value H larger than the sum of all original available values.
An original M-basis allocation extends to an all-player allocation by
giving a dummy unit to its complementary M*-basis. Original recipient
independent count vectors can be extended to bases on the complete
player ground set without decreasing any value.

Conversely, extend the dummy receiving set to an M*-basis and retain
only its complementary M-basis. None of those retained players uses
the dummy resource, so their original-resource values satisfy the
all-player guarantee. Restricting original recipient counts preserves
polymatroid feasibility. The integer optima agree.

This adapter uses polynomial dual-oracle work. It means the research
factor four is not the first constant approximation for arbitrary
player selection. The adapter can add a third value to an original
two-value instance, so the public two-value factor four must not be
applied to that setting without checking the resulting value set.

## 4. Some easy special cases and stronger exponential baselines

If all players are compulsory and all units have the same value,
aggregate their recipient polymatroids. A target quota k is feasible
exactly when k times the all-ones vector lies in the aggregate
polymatroid. This is a polynomial submodular-minimization test, followed
by integral decomposition. The hard unit-core theorem instead chooses
a basis of an arbitrary player matroid; it must not be confused with
this compulsory all-unit special case.

If all players are compulsory and there are two values, count
enumeration and the public largest-unit additive rounding yield a
(1-epsilon) value guarantee in
(1+epsilon^-1)^{O(q)}poly(H). The full derivation is in
`unit_quota_three_transfer_and_discrete_time_gate.md`, Section 7.
The corresponding two-size scheduling baseline gives makespan
1+epsilon in the same machine-count regime.

These are elementary derived baselines, not statements attributed
verbatim to the public paper. They prevent calling a constant
approximation exponential in all q players a new quality breakthrough.
They do not replace the new dependence on selection rank r, fat-cover
deficit k, or the large-job rank h in the scheduling transfer when those
parameters are much smaller than q.

## 5. What the source search established

The checked primary public theorem gives the general-recipient
8+epsilon and two-value 4+epsilon bounds above. Searches for a later
resource-matroid/polymatroid factor-four general-value theorem or a
matching rank-quasipolynomial statement did not verify such a theorem.
This is a report of the performed source check, not an exhaustive
publication-priority certification.

Older ordinary Santa Claus results, player-matroid variants with
ordinary physical items, and common matroid-rank valuation results
must retain their narrower resource models. A historical abstract or
talk announcing an improved coefficient is not a substitute for the
current corrected full manuscript. The existing detailed public
parameter audit records that version distinction.

No theorem here rests on a claimed impossibility of improving the
public proof. The prior comparison only establishes the constants
of one named overprovisioning certificate and its value-reduction
wrapper. It does not establish a lower bound for the allocation
problem or for all local-search algorithms.
