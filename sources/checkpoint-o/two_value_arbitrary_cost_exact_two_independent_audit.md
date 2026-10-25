# Independent audit of unrestricted-cost two-value exact-two allocation

**25 October 2026. Full independent read of C1--C9 and every algorithmic
gate in `two_value_arbitrary_cost_exact_two_allocation.md`.**

The theorem passes. For compulsory players, two common intrinsic positive
resource values, arbitrary integral recipient polymatroids, arbitrary
nonnegative assignment costs, and one exact total assignment budget, the
manuscript gives a deterministic factor-two allocation in
`(27/4)^h_C poly(H)` time and polynomial space. The comparator is the
original integer optimum. The parameter is the maximum affordable
cardinality of an actual one-large-unit assignment to distinct players.
Neither a price-diversity bound nor equal small assignment costs is needed.

This audit independently checks the new application of the adaptive
residual-budget lemma, its exact integer recovery, and its optimization.
The underlying adaptive lemma and one-value cost-recovery lemma have
separate full audits in
`adaptive_residual_budget_corank_independent_audit.md` and
`one_value_exact_budget_corank_independent_audit.md`.

## 1. The affordable large-support parameter has the claimed meaning

For each large type, the zero-one cap of its integral polymatroid is a
matroid. Taking the direct sum on eligible player-type pairs preserves
the distinction between types and their costs. Intersecting this with
the partition matroid allowing at most one pair for each player represents
exactly assignments of one feasible large unit to distinct recipients.

Minimum-weight intersection at cardinality k consequently computes the
minimum *actual assignment cost* for that support size. The minimum costs
are nondecreasing in k: deleting a pair from a larger feasible solution
preserves both matroid constraints and cannot increase cost. Infeasible
cardinalities are treated as having infinite cost. Thus the largest
cardinality affordable within C is computable in polynomial time.

Every budget-feasible integer allocation gives such a witness by retaining
one of its original large units at each large recipient and deleting all
other units. Recipient feasibility is downward and costs are nonnegative.
Its number of large recipients is therefore at most h_C. This deduction
uses the actual types of the retained units; it does not replace them by
the cheapest possible assignment to an unpriced support set.

Dropping the cost constraint gives the Boolean-cap rank of the aggregate
large polymatroid, so the stated upper bound on h_C is valid. Costs can
make the inequality strict. Numerical resource supply never needs to be
expanded into unit copies to compute this parameter.

## 2. Every completion oracle returns an attaining compatible assignment

Fix k and a current allowed small ground Q. The oracle's first matroid
is the player partition matroid on small labels in Q and all original
eligible large pairs. The second is the direct sum of the uniform small
cap q-k and the rank-k truncation of the large type-matroid direct sum.
A common independent set of size q must cover every player once and
saturate both category caps. It consequently has exactly q-k small labels
and k feasible large pairs, with the large recipients including P\Q.

Giving a small label weight zero and a large pair its original assignment
cost makes weighted matroid intersection compute h_k(Q) exactly. Its
returned pair I_Q,H_Q attains that cost, and I_Q is a subset of Q. This
is a stronger interface than a feasibility selector or a lower bound on
the cost of a completion, and the implementation supplies it.

When Q shrinks, only small labels are removed. All original large pairs
remain present, including pairs owned by deleted small candidates. Thus
an original protected pair I*,H* remains a candidate whenever I* is a
subset of Q. Deleting these large pairs as well would invalidate the
proof; the manuscript's construction does not do so.

The support size remains exactly k throughout. There is no extension to
a large-recipient basis that could spend additional budget or alter the
small-recipient complement. The case k=q is handled by direct affordable
all-large coverage, rather than an empty-set positive quota problem.

## 3. Current-budget separation preserves the same protected pair

The small count region keeps every original small type and its actual
assignment costs. For a nonnegative residual budget D it is the lower
projection of a bounded rational allocation polytope with a zero point.
It is convex and downward: reducing service can be realized by reducing
assigned counts, which also cannot raise the budget consumption. The
previous exact support and reconstruction construction therefore applies.

This projection must not be replaced by the sum of the small recipient
ranks alone. That sum would forget which type supplies a unit and the
cost of using it. The current manuscript retains the full coupled
capacity-and-cost region.

If a protected pair I*,H* and small allocation x* satisfy the full count
target t and combined cost C, then at every Q containing I*,

\[
 h_k(Q)\le c(H^*),\qquad
 c(x^*)\le C-c(H^*)\le C-h_k(Q).
\]

The original full target t on I* is therefore feasible in the *current*
small region. A nonnegative packing row separating b on all of Q is valid
for this same protected target. Its weighted omission certificate has a
child deleting only players outside I*. The original H* then bounds the
new minimum completion cost again, so the invariant continues.

This is a direct paired-witness argument. It does not assume the service
region is fixed during recursion. At success, service at b on every member
of Q can be restricted to the particular attaining I_Q. Adding the same
H_Q gives combined fractional cost at most C. An unrelated large
completion could cost more and would not justify this conclusion.

Every h_k(Q) is a sum of at most k original rational costs. Its encoding,
and that of C-h_k(Q), has a fresh uniform polynomial bound independent of
the recursion depth. The support LP's dimension, recipient-row encodings,
and exact separator lengths thus retain the polynomial bounds of the
underlying projected-count construction. Zero residual budget is allowed.

## 4. Exact integer small quotas close the budget without rounding loss

The successful quota b is integral. First discard fractional small counts
outside I_Q and trim each selected player's total to b. Downward recipient
constraints and nonnegative costs make both operations legitimate.

On the player-type product ground, intersect the direct sum of the
restricted small recipient polymatroids with the partition polymatroid
having total cap b at each selected player. Integral polymatroid
intersection is integral. The supplied fractional point has total
b|I_Q|, the partition's maximum total. Hence the maximum-total face is
nonempty and integral.

Minimizing the original small assignment cost on this face gives an
integer optimum of cost at most that of the supplied fractional point.
Its total b|I_Q|, together with the separate b caps, forces exactly b units
at every selected player. It costs at most C-h_k(Q), so adding the original
attaining H_Q meets the exact total budget.

The argument optimizes a linear objective on an integral face. It does
not intersect an integral polytope with a cost inequality and incorrectly
claim that the intersection stays integral. This distinction is essential
when assignment costs are arbitrary. The construction has no additive
loss of one small unit and is precisely why the final ratio remains two.

## 5. All hard targets have the required half-quota promise

For 0<T<2a, let K=ceil(T/u). If K>=2, take t=K and
b=ceil(K/2). The inequality

\[
 \frac{K}{K-\lceil K/2\rceil}\le3
\]

holds for every such integer K; equality occurs at K=3. Thus the weighted
prefix-free omission core has at most the factor Gamma(3)^k=(27/4)^k.
The arithmetic is valid even when K is binary encoded and numerically
large. The actual recovered small utility satisfies bu>=T/2, while one
large unit has value a>T/2.

If an original integer T-allocation exists, let R be its actual set of
large recipients. Retain one of its original large units at every member
of R and remove the other counts there. Every player outside R had only
small units and hence at least K of them. Retain or trim those small
counts. This produces a full t=K protected pair, does not increase cost,
and has k=|R|<=h_C. The algorithm tests this k, so that call cannot fail.

Consequently failure of every support-size call soundly excludes the
original full target T. A success only promises T/2 and is never promoted
to a certificate that T itself is attainable.

## 6. The one-unit and large-target gates are exact in the needed direction

For K=1, every positive unit has utility at least T. An integer allocation
of positive target T can be trimmed to one unit per compulsory player,
without increasing cost. Conversely, such a coverage immediately serves
the target. Weighted intersection of all type Boolean matroids with the
player partition, at cardinality q, therefore decides this gate exactly.
The gap routine is not called with equal quotas t=b=1.

For T>=2a, the original all-player fractional feasibility LP has a fixed
known player set. Its failure excludes the original integer target. Its
success can be rounded by the accepted free-disposal, cost-preserving
lower-rounding construction. Optimizing the dual cost on the full-total
integral face gives no increase in the original assignment cost and loses
at most the largest value a per player. Thus T-a>=T/2, including equality
at T=2a.

This LP must retain all original assignment coordinates, including a
coordinate whose individual unit cost exceeds C: a fractional amount may
still be affordable. The manuscript does not impose an unsupported
integer-only pruning on this fractional gate. The gate also does not
assert that unknown optional player selection can be handled by the
same LP; compulsory service is part of its valid scope.

## 7. One-sided optimization and all boundary cases are sound

The original positive value grid g divides both u and a. Every integer
utility, and therefore the integer optimum, belongs to this grid. The
total resource value V bounds the optimum, so V+g is a certified external
upper grid point, independently of how the gap routine might answer it.
The zero allocation supplies the initial lower witness.

Every actual failure excludes the full target T. Thus the upper endpoint
stays strictly above OPT_C, even if successes are nonmonotone or nominally
above OPT_C. When the endpoints are adjacent grid points, the saved lower
target L satisfies L>=OPT_C. Its saved allocation has utility at least
L/2, which proves the exact factor two. If the saved target is zero,
the same argument implies OPT_C=0.

The number of calls is polynomial in the binary length of V/g. At each
hard target there are at most h_C+1<=q+1 support sizes. The largest
exponent is h_C; their sum only changes the polynomial factor. Failed
completion calls and unpromised target calls are already included in the
prefix-free time accounting. The omission depth is at most q, and all
other state is polynomial in the original encoding, giving polynomial
space. No dependence on the numerical size of K or supplies is hidden
as an expanded ground set.

If no positive resource remains, the zero allocation is optimal. For one
positive value, fixing all players makes the direct-sum/partition
intersection an exact minimum-cost test for every integer quota; binary
search obtains the exact optimum. Arbitrary assignment costs among these
types cause no issue. The cases h_C=0, h_C=q, C=0, and zero assignment
costs are all covered by these gates and completion conventions.

## 8. The strict-below-two obstruction uses the same parameter

In the stated hidden-set instance, all costs and C are zero and the large
recipient matroid is U_(h,q), where h=q-r. Thus h_C=h exactly. The hidden
allocation has two small units at every member of A and one value-two
large unit at every member of its complement. Its minimum is two.

Total available utility is 2r+2h=2q, so the optimum cannot exceed two.
An approximation factor strictly smaller than two must give every player
integer utility at least two. At most h players receive large units;
there are therefore at least r small-only players. They each need two
small units, and the total small rank 2r forces exactly r such players
with two units each. Their set I must satisfy f_A(I)>=2r, which among
r-subsets holds only for I=A.

An output with the required guarantee thus identifies A. All other rank
queries have answers independent of A. If two unqueried candidate sets
remain, the same transcript cannot yield a correct identifying output
for both. This gives the claimed deterministic lower bound of
binom(q,r)-1=binom(q,h_C)-1 queries. Taking a fixed h_C larger than a
proposed uniform polynomial degree and increasing q rules out a
factor-strictly-below-two F(h_C)poly(H) algorithm in this recipient-oracle
model.

This is an approximation threshold, not a lower bound on the exponential
base 27/4. It does not exclude exact factor two and does not establish
hardness for explicit ordinary eligibility instances. The manuscript
states these distinctions correctly.

## 9. Audit conclusion and retained restrictions

All new interfaces pass: affordable support is computed from actual
assignments; the current residual budget protects one fixed original
pair; success uses its own attaining cheapest completion; integer small
recovery incurs no utility loss or budget violation; the exact gates
cover both quota boundaries; and target search compares against the
original integer optimum.

The accepted scope is compulsory players, two common intrinsic positive
values, arbitrary integral recipient polymatroids, arbitrary nonnegative
assignment costs, and one total assignment budget. The result is
deterministic and parameterized by h_C; it does not claim an unparameterized
polynomial factor two, multiple independent exact assignment budgets, or
the same multiplicative guarantee against a fractional optimum.
