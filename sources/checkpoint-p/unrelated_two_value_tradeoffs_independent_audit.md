# Independent audit of unrelated two-value integer-quota tradeoffs

**25 October 2026. Full independent read of UQ1--UQ5 and all five sections: passes.**

The manuscript `unrelated_two_value_integer_tradeoffs.md` composes the
reviewed quota-ratio tradeoff with the reviewed joint-role allocation
interface. I independently checked the complete composition rather than
assuming that intrinsic-value results transfer automatically.

## 1. The target branches cover every positive value

For fixed integer d>=2, the high-target condition
T>=d*a/(d-1) makes the public largest-unit loss satisfy T-a>=T/d.
The original full-player LP retains shared capacities and the exact
assignment budget, and the accepted one-objective rounding preserves that
budget. LP failure is a sound integer full-target rejection.

Below this cutoff, set K=ceil(T/u). If K<=d, then T<=du and a minimum-cost
one-positive-unit coverage supplies at least u>=T/d. Every positive
integer full-target allocation can be trimmed to such a coverage, so a
failure is sound. A success is correctly treated only as a weak target
witness, not as proof of K-unit feasibility.

The remaining targets satisfy K>=d+1 and T<da. Thus one heavy unit of
value a suffices for the weak guarantee. With b=ceil(K/d), the identity
K=jd+s, 1<=s<=d, gives

\[
 \frac{K}{K-b}\le\frac{d+1}{d-1}.
\]

Every denominator is positive and the worst case is K=d+1. The small-K
gate removes the cases that would otherwise spoil this sharper constant.

## 2. The current LP never separates shared type capacities

At a node Q, the one original rank for type j is masked to its u-valued
pairs on Q and its a-valued pairs outside Q. The latter players each have
count exactly one. The assignment budget is a single joint inequality.
This represents resource use by both roles simultaneously; the same type
is not duplicated into separate light and heavy resources.

If a fixed original target witness has heavy support F* of size k, its
complement I* receives at least K small units each. At any node preserving
I*, keep those original small counts and the retained heavy units outside
Q, while dropping the heavy units on Q\I*. The resulting allocation obeys
the current masks and heavy equalities, and resource use and cost only
decrease. Hence the full K-target on I* belongs to the current projected
region at every protected node.

The empty-region gate is consequently sound. Every failed weak query has
the required nonnegative omission row, and the same weighted first-crossing
recurrence applies with remaining measure k-|Z|. Uniform LP bit bounds and
all failed gates are inherited from the fully reviewed joint-role proof.

## 3. The integer recovery is exact for the heterogeneous quotas

Trim the returned light counts to b at every p in Q. Outside Q the total
is already one. These integer quotas form a partition-cap polymatroid on
the masked player-type product ground. The fractional point attains the
sum of all caps, so the intersection with the original resource direct
sum has a nonempty integral maximum-total face.

A minimum-cost integer optimum on this face costs no more than the
fractional point, and total equality forces every quota to be exact.
The same type is recovered only once, even if it supplies both values.
All light players therefore have utility bu>=T/d and all heavy players
have utility a>T/d. There is no additive unit loss in this branch.

The proof does not assume that a budget row preserves integrality. The
budget is preserved through a scalar cost minimization on an integral
face. Its use remains limited to one assignment budget.

## 4. Cardinalities, optimization, and global time are consistent

The largest affordable heavy support nu_C is computed by minimum-cost
one-unit matroid intersection on the heavy pair ground. Any original
integer allocation supplies such a support after trimming. Every exact
k<=nu_C is considered, and k=q uses direct all-heavy coverage. No finite
light benchmark is assigned to an empty light set.

If all k calls fail at a hard target, its actual original heavy support
cannot exist, so the full integer target is infeasible. All success
branches return a legal allocation of value at least T/d. The common
value grid, external upper endpoint V+g, and one-sided maximization thus
give at least OPT/d without assuming monotone successes or exact nominal
target feasibility.

For global time, the cover is separately applied to each exact promised
omission count k. A forced seed inside that actual heavy set preserves
the same witness with the new masks. The all-input extension cost is
A_d^(k-|Z|), so the accepted polynomial-space block conversion applies
without a second approximation loss. The number of target and support
loops is polynomial. No slower raw-corank fallback is included in the
stated unconditional global implementation.

## 5. Scope and disposition

The constants agree with QT: factor two has global base 50/27, factor
three has 7/4, and the displayed factors four and five have the stated
algebraic bases. The sharp global statements are for fixed d, with binary
counts and polynomial space. Missing positive classes reduce to the exact
compulsory one-value algorithm; zero value and zero budget are safe.

The optional-matroid dummy adapter is correctly not imported into this
exact-d two-value statement, because it can add a third positive value.
No unrelated-machine scheduling or multi-budget extension is inferred.
The result is a valid direct composition of the two independently reviewed
interfaces, with no substantive correction requested and no exhaustive
publication-priority claim.
