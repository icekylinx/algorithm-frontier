# Verification note

**Curated source path:** `sources/checkpoint-p/matroid_quality_and_union_root_audit.md`

The source audit follows.

# Root audit of sharp matroid quality and the fat-resource reduction

**25 October 2026. Accepted mathematical refinement.**

This note audits `matroid_allocation_sharp_star_rank_quality.md`
and `matroid_union_fat_resource_allocation.md`. Both inherit the
fully specified current-blocker algorithm, whose individual matroid
eligibility, earliest-circuit exchanges, current maximality and
micro-signature were checked separately. Two reviewers also checked
the union reduction and its implementation contracts.

## 1. The sharper star coefficient

For an inclusion-minimal B-bundle, a resource of value at least B
forces the bundle to be that singleton. If such a selected center
has a matching blocker, that blocker must be the same singleton.
Its star therefore has one blocker and value at most u, not B+u
plus another B. For a nonsingleton center, every item is below B;
its value is below B+min(u,B), while each blocker's value outside
it is below B. Thus the correct general coefficient is

\[
                 C(B,u)=\max\{u,2B+\min(u,B)\}.
\]

Every current blocker has one center, and every retained center is
blocked. Summing stars gives v(F)<=C(B,u)|Y|. A singleton may
attain equality, so replacing this by a universally strict inequality
would be wrong.

The compact LP supplies the needed strict inequality in the opposite
direction. Outside F, every eligible player's total liked value is
strictly below B. The eligible fractional mass is at least one.
Therefore v(F)>(T-B)x(U), including at B=T. A weak upper bound
v(F)<=(T-B)(r-|J_0|) is consequently a valid infeasibility witness.

## 2. Rank is useful for quality as well as time

Let k<r be the current matching size and s the previous blocker
count. With w=r-k+s, one has s/w<=(r-1)/r. Hence an empty new
maximal layer gives a certificate whenever

\[
           B+\frac{r-1}{r}C(B,u)\le T.
\]

The three displayed branches of B_r^*(T,u) solve this continuous
strictly increasing expression exactly: the first has B>=u, the
middle has B<=u<=3B, and the last has u>=3B. Their endpoints agree.
For r>=2 the positive domain is u<rT/(r-1); rank one permits B=T
for every u. The example with r players and r-1 shared resources
of value rT/(r-1) has a feasible Q(T) but cannot supply every player
with any positive integral value, verifying the stated domain boundary.

Subtracting epsilon T from B_r^* leaves at least epsilon T margin
in B+rho C. Throughout the positive domain C<=3T. The revised
growth threshold (epsilon/4)(r-k+s) therefore follows from the same
current-state certificate. Earlier growth statements survive because
k and their blocker prefixes remain unchanged. All exchanges and
signature events are the previously audited ones. The time is the
minimum of the rank-exponential and rank-quasipolynomial counts,
with the same linear explicit-input factor as the inner theorem.

The local-star examples correctly limit this certificate mechanism.
The maximal-state example is not claimed reachable from the fixed
empty-start scan policy, and it has an allocation close to its LP
value. It is therefore not an integrality-gap lower bound near three.

## 3. Both directions of the matroid-union reduction

Let M be the original player matroid, N the fat-resource transversal
matroid, and U=M* union N. An integral optimal basis I at target T
has a discarded complement D that is a basis of M*. Its players
receiving fat items form an N-independent set F, disjoint from D.
Extending D union F to a U basis can only shrink the remaining
small-only player set. Its complement is therefore a U* basis with
the original small allocations of value at least T. This proves the
auxiliary Q(T) promise without supplying the optimum to the algorithm.

Conversely, an allocated U* basis S has complement a U basis.
Decompose the latter into D independent in M* and F matchable to fat
items. Extend D to a full M* basis. Some already served players may
be discarded, but all retained players still have their disjoint fat
or small allocation. The retained set is exactly an original M basis.
Nothing requires the extension to avoid S, and nothing is assigned
to an unserved new player.

Since U contains M*, the auxiliary rank r' is at most r. Zero
auxiliary rank is handled by an empty small basis, followed by the
same decomposition and recovery. An empty small resource set has
u=0; positive auxiliary rank then produces the correct failure
certificate. No assertion is made that the original arbitrary-size
compact Q_M(T) implies the auxiliary LP promise. The proved comparator
is the original integer optimum.

## 4. Exact and approximate factors

Take theta=r/(4r-3) as the fat threshold relative to T. The small
instance has u<theta T. Its rank factor is no greater than
rho=(r-1)/r. At B=theta T, the star coefficient is at most 3B,
and B+3rho B=T. The exact rank-exponential algorithm therefore
supplies value theta T to every small player; every fat player
gets at least that value as well. This proves factor 4-3/r.

For positive epsilon, take B=(theta-epsilon)T. The coefficient
2B+u alone already leaves margin at least epsilon T after multiplying
by rho. Growth threshold epsilon/4 pays the extra current blockers.
Choosing epsilon=1/d-1/(d+eta), d=4-3/r, gives factor d+eta and
epsilon^{-1}=d+d^2/eta=O(1+eta^{-1}), uniformly in r.

Thus the main note's rank-quasipolynomial exponent and exact
rank-exponential boundary are justified. The finite-rank factor
approaches four; there is no uniform fixed constant improvement
below four for unbounded rank.

## 5. Oracle costs and target search

Original dual queries use the standard dual rank formula and greedy
rank queries. The fat transversal oracle uses explicit bipartite
matching. Polynomial matroid union computes ranks and a disjoint
decomposition. Applying duality again supplies the actual U* oracle.
All substitutions are paid by a polynomial in the explicit input
whose exponent does not depend on r. This supports a rank-FPT
claim, but does not preserve the inner theorem's input-linear factor.

For rational values, a common denominator has polynomial bit length
in the total input encoding. OPT lies on the resulting grid. Every
failed target exceeds OPT, while a successful target need not be
below it. Binary search nevertheless keeps its upper endpoint
strictly above OPT. When the two endpoints are adjacent grid values,
the stored successful lower endpoint is at least OPT. Returning
its approximation preserves the factor. The initial upper target
is chosen so that the promised allocation would exceed the total
resource value, forcing failure. This is a sound search with the
actual one-sided oracle, not a presumed monotone decision procedure.

## 6. The configuration-LP addendum also passes

The separate **matroid_union_configuration_lp_addendum.md** upgrades
the comparator without changing the algorithm. For a feasible original
configuration point, let x be its player base vector and f the mass
of configurations containing a fat item. Selecting one fat item
from each such configuration yields a fractional fat matching, so
f belongs to the transversal-matroid independent polytope. The vector
d=1-x is in the original dual base polytope. Since d+f<=1, the
union rank formula proves d+f belongs to the union independent
polytope. Extending it coordinatewise to a base z' gives a dual
base x'=1-z' no larger than the all-small configuration mass h=x-f.

Small-resource marginals conditioned on the all-small configurations
are bounded by h playerwise and supply value at least T h. Scaling
them by x'/h, with zero in the h=0 case, proves the auxiliary compact
LP promise. This correctly uses configuration conditioning; it does
not import an invalid h bound from arbitrary assignment marginals.

Every configuration threshold is a rational subset sum, and only
finitely many different configuration systems occur. The maximum
feasible target is attained on the common input grid and obeys
r T_conf<=V. The same one-sided grid search therefore returns the
claimed approximation relative to T_conf. No configuration enumeration
or LP solution is required as input or as an uncharged subroutine.
The inner infeasibility witness, together with the fixed reduction,
is a polynomially oracle-checkable certificate for the original
configuration LP. The source can still have an exponential dual;
no such dual is asserted to be printed.

## 7. Comparison discipline

The accepted result is a quality/time tradeoff for arbitrary
player-matroid selection and restricted intrinsic resource values.
The current printed DRZ one-fifth theorem, composed with the same
public matroid-union wrapper, supplies a polynomial six-factor
baseline up to positive slack. Historical one-third/four-factor
statements and their revision remain explicitly documented.
Ordinary Santa Claus already has a polynomial four-factor-plus-slack
algorithm and parameterized approximation schemes in other parameters.
Neither an unrestricted additive-valuation result nor a uniform
below-four ordinary Santa Claus algorithm is claimed.

All these allocation results are separate from deterministic exact
maximum matching in arbitrary general graphs, whose accepted research
exponent remains 4/5.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
