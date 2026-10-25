# Verification note

**Curated source path:** `sources/checkpoint-o/unrestricted_budget_allocation_root_audit.md`

The source audit follows.

# Root audit: unrestricted assignment costs, exact budgets and near-two allocation

**25 October 2026. Full mathematical review for checkpoint O.**

This review accepts the one-value theorem O, the changing-residual-budget
lemma RB, the arbitrary-value theorem R, and the compulsory two-value
theorem C. The complete corresponding manuscripts are:

* `one_value_exact_budget_corank_two_allocation.md`;
* `adaptive_residual_budget_corank_gap.md`;
* `arbitrary_cost_residual_budget_near_two_allocation.md`;
* `two_value_arbitrary_cost_exact_two_allocation.md`.

Each application has full independent audits. RB and the global
conversion also have independently checked counting and encoding
arguments. The acceptance here is internal mathematical review,
not external peer review or formal verification.

## 1. Main disposition

The arbitrary assignment costs are now fully supported. Neither
proportional light costs nor a bounded number of prices is required
by R or C. The accepted statements are:

| Model | Guarantee | Corank/support time |
|---|---|---|
| One common value; arbitrary original player matroid | At least ceil(K*/2) units per selected player; exact budget | (27/4)^c poly(H) |
| Arbitrarily many intrinsic values; arbitrary original player matroid | Factor 2+eta when one optimum has at most K heavy recipients at the stated threshold | Gamma((2+eta)/eta)^(c+K) poly(H) |
| Two intrinsic values; compulsory players | Exact factor two; arbitrary assignment costs; exact budget | (27/4)^h_C poly(H) |

All have polynomial workspace and binary resource counts. The
global omission wrapper supplies separate all-instance whole-ground
time statements; those do not assume c, K or h_C is small.

The two-value exact-two theorem is compulsory-player. It must not
be substituted for an exact-two theorem with an arbitrary optional
player basis. The general arbitrary-value theorem remains 2+eta.

## 2. Exact unit quotas can be recovered without an additive loss

The budgeted count projection is downward and has the explicit
nonnegative support separator from B. Its normalized support LP
must accept every nonpositive optimum; an interior point can give
a negative value because the normal has simplex sum one. The final
O manuscript correctly uses this condition.

For an output integer quota b and an actual chosen player set I,
trim the reconstructed fractional counts to exactly b at every
member of I. Nonnegative assignment costs make this operation
budget-safe. On player-type coordinates, intersect the integral
direct-sum recipient polymatroid with the integral partition
polymatroid imposing at most b units per player.

The trimmed point attains total b|I|, the partition upper bound.
Its maximum-total face is therefore nonempty and integral.
Minimizing actual cost on that face has an integer optimizer no
more expensive than the fractional point. Saturation of the total
forces exactly b units at every selected player. No cost inequality
is added with an unsupported claim of integrality; the proof uses
one objective on an already integral face.

Counts b and b|I| can be large but remain encoded integers. The
product ground is only |I| times the number of types. This is an
exact quota recovery argument, not a unit-copy expansion or a
largest-unit-loss rounding argument.

At K=1, the positive-gap core is inapplicable. Weighted intersection
of the parallel lift of the original player matroid and the direct
sum of resource Boolean matroids finds a minimum-cost one-unit
assignment on a genuine player basis. This is exactly two matroids.
For compulsory players its first matroid is the player partition
matroid. Adding another arbitrary player matroid is not automatic.

## 3. The completion oracle is polynomial and retains its actual witness

For fixed heavy cardinality k and allowed light ground Q, use zero-
weight light copies only for Q and retain all original eligible heavy
pairs. The first matroid is the original player's parallel lift.
The second is the direct sum of the light uniform cap r-k and
the heavy resource direct sum truncated to k.

A common independent set of total cardinality r has exactly the
two required class sizes. Its owners are distinct and form an
original basis. Weighting only the heavy pairs by their original
assignment costs computes the minimum h_k(Q), together with an
attaining light set I_Q and heavy assignment H_Q.

Deleting a light candidate must not delete its heavy options.
The manuscripts retain those options. The cost h_k(Q) is a sum
of at most k original costs, so every newly formed residual right
side C-h_k(Q) has a fresh uniform polynomial bit bound. The support
LPs never accumulate old generated coefficients recursively.

At a success the algorithm must return this attaining pair.
Substituting some other permissible heavy completion would invalidate
the budget reservation. The actual construction keeps H_Q unchanged.

## 4. A fixed protected pair justifies the changing service region

Let an original promised pair I*,H* have full light service t and
combined cost at most C. At every Q containing I*, its same heavy
assignment remains a candidate, giving

\[
       h_k(Q)\le c(H^*),\qquad
       c(x^*)\le C-c(H^*)\le C-h_k(Q).
\]

Hence t*1_(I*) belongs to the current light region. A violated
nonnegative row at b*1_Q still implies that Q\I* contains more
than a 1/R fraction of the row weight. A first-crossing certificate
contained in that omitted set is enumerated, preserving the same
pair into its child. The comparison is proved again at the child
using its newly computed minimum cost.

This is sufficient for completeness. A globally fixed packing
region was a sufficient interface in the earlier theorem, not a
necessary hypothesis after this protected-pair proof is supplied.
The first-crossing prefix count, unfinished-word bound and recursive
Gamma charge are local and remain unchanged. All failed completion
calls and all unpromised branches are included in the same time bound.

At success, light service b on all Q can be restricted to I_Q
without increasing its cost. Its budget was C-h_k(Q), and the
actual H_Q costs h_k(Q). Integer light recovery preserves that
cost, so the combined budget is exact.

## 5. Why the resource partition and scalar budget matter

Intrinsic values partition whole resource types into light and
heavy classes. Their recipient capacities therefore do not overlap.
Arbitrary assignment costs remain inside the light projection and
the heavy objective; no proportionality is needed.

With player-dependent values, the same type may be light at one
player and heavy at another. A cheaper heavy assignment can then
consume a different portion of the light resource capacity, so
the protected light witness need not remain feasible. R does not
make that extension. The earlier unrelated-value additive theorem
retains its separate valid scope.

Likewise, minimizing two completion cost coordinates separately
need not give a single witness attaining both minima. The scalar
reservation argument and the one-objective rounding do not preserve
arbitrary multiple assignment budgets. This limitation is distinct
from continuous flow, where several routing-only budgets require
no integral rounding.

## 6. Searches, thresholds and support parameters

For R, each fixed value split and k has its own joint benchmark:
an actual selected basis, an integral one-unit heavy assignment,
and fractional light service at a g-grid value T, all under the
same budget. It is downward in T. A failed adaptive call excludes
that benchmark at T; it need not exclude other splits or k values.
The outer one-sided grid search is consequently sound and does
not assume monotone successes.

At theta=(1-epsilon)OPT_C/2, retaining one original heavy unit per
heavy recipient and the original light-only players supplies the
joint full-OPT_C witness. The lower rounding loses at most u_L,
strictly below theta. The retained heavy assignments have value
at least theta. This proves factor 2/(1-epsilon), hence 2+eta
for epsilon=eta/(2+eta).

An optimum's actual heavy support is retained; it is never completed
to a larger heavy basis at extra cost. The affordable maximum h_C(theta)
is computed by minimum-cost common independent sets on heavy pairs.
Their costs are nondecreasing with cardinality. Any M-independent
heavy support extends to an original basis with zero-cost light
labels, so h_C(theta)=max{k:h_k(P)<=C}. This gives the stated
computable sufficient support bound without changing the stronger
existence-of-one-optimum hypothesis.

For C, the hard target range is 0<T<2a. The small target K=ceil(T/u)
is reduced to b=ceil(K/2); R<=3 and Gamma(3)=27/4. Exact small-quota
recovery gives b*u>=T/2 without an additive error. For T>=2a, a
fixed all-player fractional LP plus cost-preserving rounding gives
T-a>=T/2. This high-target argument is where compulsory players
are essential. K=1 has its exact coverage gate. Zero resources,
one value, zero budget, pure-heavy and empty-light cases are handled
explicitly. The grid maximization retains a saved actual allocation
and an upper endpoint strictly above integer OPT_C.

## 7. Lower bounds, global time and attribution

The zero-cost hidden-rank examples remain valid inside these
budgeted models. They force a strict-below-two algorithm to identify
one hidden subset, yielding binom(q,c)-1 or binom(q,h_C)-1 oracle
queries in the stated parameterizations. Balanced instances make
these bounds 2^(q-O(log q)). They do not prove the base 27/4 or
the converted base 50/27 optimal for exact factor two.

The whole-ground block wrapper is applicable because a forced
omitted set only removes possible light recipients, leaving the
original heavy ground, resource ranks and cardinality unchanged.
The corank time then depends on the remaining omissions. Its
known monotone-local-search base formula is attributed to the
primary literature; its explicit polynomial-space implementation
has its own complete proof and independent audits.

Classical ordinary-item cost-preserving rounding and the checked
ICALP 2025 logarithmic budgeted approximation are acknowledged
public background. These new deterministic bounds are exponential
or parameterized time results. They are not unconditional polynomial
constant-factor improvements for arbitrary Budgeted Santa Claus.

**Disposition:** the unrestricted-cost O, R and C theorems and their
adaptive-budget interface are accepted with the exact model and
parameter boundaries above. Earlier proportional and price-profile
proofs are valid weaker routes, not conditions of the new theorem.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
