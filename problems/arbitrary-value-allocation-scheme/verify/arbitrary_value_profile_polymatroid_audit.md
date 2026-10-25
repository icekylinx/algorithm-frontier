# Verification note

**Curated source path:** `sources/checkpoint-q/arbitrary_value_profile_polymatroid_audit.md`

The source audit follows.

# Independent polymatroid audit of the arbitrary-value allocation scheme

**25 October 2026. Full independent read of
`arbitrary_value_profile_allocation_approximation_scheme.md`, PA1–PA20
and all twelve sections. Result: the stated theorem passes; no
substantive correction requested.**

This review independently checks the disposal and complement ranks,
the sign of the cost objective, every large-value prefix boundary,
integer-target completeness, all-input profile enumeration and exact
target optimization. It is separate from the author's derivation and
the other reviewers' reports.

## 1. Accepted model and theorem

The output selects one actual rank-r basis of an arbitrary original
player matroid on q nonloop players. Resources have arbitrary integral
recipient polymatroids and can be left unused. Values and nonnegative
assignment costs depend on both player and type. Nonnegative setup
fees and assignment costs share one budget that must hold exactly.

For supplied rational 0<epsilon<=1, the theorem returns value at least
(1-epsilon)OPT in

    binomial(q,r) exp(O(r/epsilon)) poly(H+size(epsilon))

time and polynomial binary space. The comparator is the original
integer optimum with a genuine selected basis. The proof does not
claim the same target-capping completeness for a fractional optimum.

The selected basis is fixed before each LP and its rounding. This
both justifies charging its setup fee as a constant and avoids any
cross-rounding change of the selected player set. There is no hidden
small-corank, common-value, limited-price-diversity or support promise.

## 2. Feasibility at zero and legitimate preprocessing

A minimum-setup M-basis with zero real allocation is legal exactly
when its setup fee is at most C. Since assignment costs are
nonnegative and resources may be unused, excessive minimum setup
cost certifies that no original solution is feasible, even at value
zero. Conversely, an affordable basis with zero counts is always a
valid initializer.

Original player loops cannot belong to a selected basis and may be
removed. Allocations outside the selected basis and zero-value
assignments can be deleted because resource feasibility is downward
closed and costs are nonnegative. These deletions do not remove
utility from a selected player. They would require reconsideration
in a mandatory-job or signed-cost model, neither of which is claimed.

Rank zero is explicitly excluded from the nonempty minimum-utility
statement and handled by a separate chosen objective convention.
Zero-rank resources and forbidden coordinates cause no difficulty
in any later construction.

## 3. Integer target capping and the retained big-count bound

At target T>0, replace each value v by w=min(v,T). For an integer
allocation whose utility at a player is at least T, either some
assigned unit has original value at least T, in which case that one
capped unit supplies T, or all assigned values are unchanged. Thus
capping preserves the existence of a full integer target witness.

For a fractional allocation, a fraction of a very large-value unit
could have supplied T before capping and less than T afterward.
The manuscript correctly marks this distinction and does not use a
fractional comparator at the completeness step.

Every big capped unit has value greater than delta*T and at most T,
where delta=epsilon/3. If the total big utility is at least T, retain
the first prefix of any unit ordering that reaches T. Its utility is
less than 2T. Before its last unit the utility is below T, so if its
retained count is m,

    m-1<1/delta,       hence m<=ceil(1/delta)=K.

If total big utility is below T, its entire count is strictly below
1/delta and therefore at most K as well. This checks both reciprocal-
integer and nonintegral reciprocal cases.

The resulting coordinate counts are obtained only by deletion from
the original integer allocation. The big-only first-reaching case
also deletes all small units; the other case retains the original
small allocation. Resource feasibility and nonnegative cost are
preserved, and the selected setup fee is unchanged.

## 4. Bins, profile LP, and full-target completeness

The open-lower, closed-upper intervals partition (delta,1] exactly.
Their widths are at most delta^2. A value exactly delta*T is small;
an internal endpoint belongs to the preceding bin; a value capped
at T belongs to the final bin. Constructing only bins with actual
eligible coordinates loses no possible assigned unit.

For retained counts h_i, the lower load L=sum lambda_i h_i is below
two, so it is among the enumerated profiles L<=2, sum h_i<=K. The
upper load U=sum mu_i h_i bounds the actual capped big utility from
above. If the retained big utility reaches T, then U>=1 and no small
utility is needed. Otherwise the original small utility is at least
T minus actual big utility and therefore at least max(0,1-U)T.

Hence a full original integer target supplies one affordable actual
basis and one feasible joint profile LP. The LP uses exact big-bin
count equalities, not merely upper bounds. All types are still governed
by their original recipient polymatroids on the masked coordinates;
there are no separate resource copies for big and small assignments.

The LP is bounded by resource ranks. Its dimension is the explicit
coordinate ground, and all subset inequalities have zero-one
coefficients and polynomially encoded rank right-hand sides. Along
with the explicit rational profile, utility and cost rows, this
provides the usual uniform polynomial witness encoding for the stated
exact LP/separation model.

## 5. The disposal extension is a valid rank and preserves optionality

Fix a masked resource rank f on its current real ground Q and write
n=f(Q). Introduce one disposal coordinate 0. Define fhat(S)=f(S)
when 0 is absent, and fhat(S)=n when 0 is present.

Normalization, integrality and monotonicity are immediate. For
submodularity, if neither set contains 0, use submodularity of f;
if both do, every relevant rank is n. If just A contains 0, the
inequality reduces to f(B)>=f(A intersect B), which is monotonicity.
Thus fhat is indeed an integral polymatroid rank.

For any independent real x, assign n-x(Q)>=0 to disposal. Subsets
not containing disposal obey the original inequalities. A subset
containing disposal has total at most the entire count n. Hence
this is a base of fhat. Conversely, deleting disposal from any
fhat-base leaves a feasible independent vector of f.

The auxiliary n is the rank of the current masked resource. It is
not a newly imposed mandatory real supply. All unused units can
remain in disposal and are later removed at zero cost. This is why
the base-completion argument is valid in the original optional-
resource model even when masks reduce available rank.

## 6. Complementation and the cost direction, checked in both directions

On the augmented ground E let d_e=fhat({e}) and

    g(S)=fhat(E minus S)+d(S)-n.

This rank is normalized because fhat(E)=n. It is integral and
submodular by complementation and addition of the modular d. Its
marginal at e is d_e minus a marginal of fhat, which lies between
zero and d_e. Therefore g is monotone and nonnegative.

For xhat in B(fhat), singleton caps give xhat<=d, so y=d-xhat is
nonnegative. It has total d(E)-n=g(E), and

    y(S)=d(S)-n+xhat(E minus S)
         <=d(S)-n+fhat(E minus S)=g(S).

Thus y belongs to B(g). Conversely, y in B(g) satisfies
y_e<=g({e})<=d_e, so xhat=d-y is nonnegative. Its total is n, and
using the inequality on E minus S shows xhat(S)<=fhat(S). This
proves the exact base bijection used in PA14, including all
coordinate nonnegativity conditions.

Across types, take the direct sum of these complement resources.
At each real player's chosen type order, impose ceiling-prefix caps
ceil(y(S)). These are the integral maximum-prefix ranks. Give each
disposal coordinate its cap d_e. Their direct sum is another integral
polymatroid and contains the original y.

The common full-total face at sum_j g_j(E_j) is nonempty and integral.
Because each complement resource individually bounds its total,
equality keeps every one of them a base. Maximize the original
assignment coefficients a on y over this face, with zero disposal
coefficient. The complemented real cost is

    a*xhat = a*d-a*y.

The constant a*d is unchanged. Maximizing a*y therefore gives a
cost no greater than that of the original fractional allocation.
This verifies the objective sign and exact-budget direction.
Discarding only the free disposal coordinates does not raise cost.

No arbitrary cost-row integrality assertion is needed: the one
cost objective is optimized on an already integral full-total face.
All constructions use one disposal coordinate per resource and
binary counts, not a unit expansion.

## 7. Simultaneous lower-prefix floors follow at the same integer point

For any real player prefix S, the machine-side cap gives
y'(S)<=ceil(y(S)). Since d(S) is an integer,

    x'(S)=d(S)-y'(S)
          >=d(S)-ceil(y(S))
          =floor(d(S)-y(S))
          =floor(x(S)).

Every prefix and the preceding cost comparison hold simultaneously
for this one integral point. The construction does not independently
choose one rounding for cost and a different rounding for utility.
The selected actual basis remains unchanged throughout.

## 8. Exact big-bin prefixes remove every large-value boundary error

Assign surrogate value lambda_i*T to every big coordinate in bin i,
and retain true values on small coordinates. Put big bins in
decreasing surrogate order before all small coordinates. Every big
surrogate is at least delta*T, every small value is at most delta*T,
and big-first tie breaking gives a valid nonincreasing order.

In the summation-by-parts lower bound, the only possible rounding
loss at position h is

    (s_h-s_(h+1))*(X_h-floor(X_h)).

Inside a big bin the value difference vanishes. At the end of a big
bin, X_h is the sum of the integer fractional big-bin totals already
required by the LP. Its fractional part therefore vanishes. This
includes the final big-bin boundary before the small group. Empty
bins can simply be omitted without changing either observation.

Consequently all loss terms with a large-value coefficient are zero.
The remaining differences are inside the small group and telescope
to its largest value, at most delta*T. This establishes PA17 even
if an original pair value was arbitrarily greater than T. If there
are no big coordinates it becomes the standard small-value bound;
if there are no small coordinates the loss is zero.

The output does not have to retain every big-bin count exactly.
The simultaneous prefix lower bounds are sufficient for the
surrogate utility inequality. Requiring extra integer bin equalities
after rounding would be an unnecessary and unproved stronger step;
the manuscript correctly avoids it.

## 9. Quantitative approximation and exact shared budget

The fractional surrogate utility at a player is at least

    [L+max(0,1-U)]T.

The bin width bound gives 0<=U-L<=K*delta^2. If U<=1 the displayed
quantity is [1-(U-L)]T. If U>1 it is LT=[U-(U-L)]T, which is no
smaller than [1-K*delta^2]T. After the small-prefix loss, actual
utility is at least

    (1-delta-K*delta^2)T.

Actual values dominate the surrogate values, including at every
capped original coordinate. Since K<=1/delta+1,

    delta+K*delta^2 <=2delta+delta^2
       =2epsilon/3+epsilon^2/9
       <=7epsilon/9<=epsilon.

Thus every profile success gives at least (1-epsilon)T. The recovery
does not increase assignment cost, and the original selected basis
has the same setup fee. The one shared setup-plus-assignment budget
therefore holds exactly at the same output point.

## 10. Enumeration, partition count, and polynomial binary space

The next occupied-bin count is enumerated only through

    min(K-s, floor((2-L)/lambda)).

Every generated partial vector already satisfies both monotone
profile inequalities and has an all-zero completion. At each depth,
different partial vectors give different zero completions. This
bounds actual traversal nodes by a polynomial factor per complete
profile, including all failed LP profiles. The Cartesian product
over selected players has the same property.

Including all potential bins and ignoring L<=2 gives the stated
binomial(b_delta+K,K) bound. For the stronger bound, set
J=floor(1/delta). Since lambda_i>=delta^2(J+i), a valid profile maps
injectively to a partition with h_i parts of size J+i and total at
most floor(2/delta^2)<2(J+1)^2. The cumulative partition generating
function at t=1/(J+1) has logarithm at most

    t*floor(2/delta^2)+2/t <4(J+1).

Thus the count is at most exp(4(J+1)). This is a cumulative count
over all allowed totals, so no omitted numerical factor is needed.
The generating function is used only for analysis.

All r-subsets are streamed, with nonbases and unaffordable setup
sets rejected in polynomial time. Every accepted basis has at most
the displayed number of profiles per selected player. This yields
both PA5 bounds, including all bad candidate bases and profiles.

Only occupied bins are stored, at most the explicit input
coordinates. Counters, bin IDs, endpoints, partial sums and all
resource and disposal counts are binary. The recursion depth is
bounded by the input coordinate count. The full supplied rational
accuracy encoding H+size(epsilon), rather than log(1/epsilon)
alone, bounds the polynomial workspace and arithmetic.

## 11. Exact maximization search and final conclusion

The zero initializer is an actual legal basis and zero allocation.
If no eligible positive values remain, it is optimal. Otherwise a
positive rational grid g dividing all positive original values has
polynomial encoding, and every integer utility total and OPT is
on that grid. The displayed total-value bound V is finite, is on
the same grid, and upper-bounds OPT.

Initialize L=0 with the legal zero output and external U=V+g>OPT.
At a positive midpoint, exhaustive failure excludes a full integer
target by Section 4, so T>OPT and U may be lowered to T. Success
raises L and saves an actual original solution of value at least
(1-epsilon)L. The latter is a weak-success invariant, not a claim
that L is a feasible full target.

At adjacent endpoints U=L+g, U>OPT and grid integrality imply
L>=OPT. The saved output then has value at least (1-epsilon)OPT.
If L remains zero, the saved legal initializer supplies the required
boundary case. Weak successes need not be monotone. Capping and
binning can depend on the target because only the one-sided
completeness statement is used.

The number of targets is polynomial in the original binary data;
no extra multiplicative loss is introduced. The full optional-player,
unrelated-value, integral recipient-polymatroid, one-shared-budget
approximation scheme therefore passes this independent audit.
Its integer comparator and accuracy-dependent exponential time are
essential scope statements and are correctly retained in the note.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
