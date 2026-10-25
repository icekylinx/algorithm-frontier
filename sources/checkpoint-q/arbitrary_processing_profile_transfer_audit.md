# Independent review of the exact-budget scheduling approximation scheme

**25 October 2026. Reviewer: transfer_frontier. Full mathematical review of
`arbitrary_processing_profile_approximation_scheme.md`, PS1--PS19 and all
thirteen sections: PASS.**

The review covers arbitrary nonnegative rational machine-type processing
times, arbitrary integral recipient-polymatroid bases, binary mandatory
counts, an exact assignment-cost budget, and binary-encoded rational
accuracy. It does not specialize the argument to ordinary explicit jobs.
This is an internal mathematical review, not a formal verification or a
publication-priority claim.

## 1. Original totals and the common recovery operation

Every original type has an upper total n_j=f_j(P). Masking machine-type
pairs never increases this bound, and the algorithm still requires total
N=sum_j n_j. Consequently attaining N forces every original type to
attain its own n_j; no missing mandatory jobs can be replaced by another
type. This remains true after a target mask or a zero-time mask.

The resource direct sum and the integer machine-cap direct sum have an
integral polymatroid intersection. Total N is an upper bound from the
resource side, so the nonempty total-N face is integral. Minimizing the
actual scalar assignment cost on that face gives an integral full
schedule of cost no greater than the fractional witness. The proof uses
a cost objective on an integral face, not an unsupported integrality
claim after adding a budget row. There is one joint recovery across all
types and machines, including a type that is small on one machine and
big on another.

The small-coordinate prefix rank is also correct. For nondecreasing
integer caps U_h=ceil(X_h), the rank max{U_h:h in S} is equivalent to all
the prefix inequalities. It is a normalized monotone submodular integer
rank. Summation by parts bounds the rounded small load by its fractional
load plus the largest allowed small processing time. The full prefix
includes zero-time coordinates and preserves their count constraints.

## 2. Exact bin boundaries and binary representations

For delta=epsilon/2, the intervals

    (delta+i delta^2, min{1,delta+(i+1)delta^2}]

partition exactly (delta,1]. The ceiling-minus-one index formula assigns
an internal boundary to the preceding bin. A normalized time equal to
delta is small; a time equal to one lies in the last big bin. The last
interval has strictly positive width because of the defining ceiling
in B. Pairs with time greater than the positive target are forbidden,
with the original type counts retained.

Only bins containing actual eligible coordinates are stored. There are
at most as many such bins as input machine-type pairs. Bin indices and
endpoints are computed by exact rational arithmetic, so neither the
possibly enormous bin universe nor individual job copies are expanded.

The use of H_epsilon=H+size(epsilon) is necessary and correct. A rational
accuracy close to one can have a long numerator and denominator even
when log(1/epsilon) is small. The theorem charges that full encoding
length, as well as all target and resource data.

## 3. Full-target witnesses and legal weak outputs

For a full target-T schedule, let h_i be the actual number of big units
in bin i on one machine. Since each is strictly larger than delta T,
their count is strictly smaller than 1/delta and hence at most
K=floor(1/delta). Their total actual load is at least T times the sum
L of their lower bin endpoints. Therefore L<=1 and the remaining small
load is at most (1-L)T. The unchanged original schedule satisfies the
enumerated profile LP. Its actual occupied bins are all present in the
input grouping, so no full witness is lost by omitting empty bins.

Conversely, a feasible profile LP is rounded using an integer cap h_i
on each big bin and a separate small prefix chain. These groups are
disjoint and form an integral machine polymatroid. The resulting
integer big load is at most

    T sum_i (lambda_i+delta^2)h_i
       <= LT+delta^2 KT <= LT+delta T.

The integer small load is at most (1-L)T+delta T. Thus their sum is at
most (1+2delta)T=(1+epsilon)T. The profile caps are only upper bounds;
using fewer big units cannot invalidate the estimate. No lower count
constraints or predetermined job identities are required.

The joint full-total minimum-cost operation then preserves every
original job and the exact budget. Consequently exhaustive failure
at T is a sound assertion OPT>T, while success only certifies the
actual returned weak schedule. The later search uses precisely this
one-sided guarantee.

## 4. The stronger profile count is valid

The direct composition count binomial(B+K,K) bounds the same algorithm
without using its weighted load restriction. For the sharper count,
write n=floor(delta^(-2)). Since K=floor(delta^(-1)),

    n < (K+1)^2,
    lambda_i >= delta^2(K+i).

Every valid profile therefore has integer weight
sum_i(K+i)h_i<=n. Mapping h_i to multiplicities of the integer part K+i
is injective: distinct bin indices give distinct part sizes. Empty bins
only restrict this family. This step counts the actual capacity
profiles, not possible job identities.

For t>0, each partition of weight at most n contributes at least
exp(-tn) to the convergent partition generating product, giving

    p_(<=n) <= exp(tn) product_{j>=1}(1-exp(-tj))^(-1).

Its logarithm is

    sum_{ell>=1} 1/[ell(exp(t ell)-1)]
       <= (1/t) sum_{ell>=1} ell^(-2) <= 2/t.

All terms are nonnegative, so the series interchange is justified.
Choosing t=1/(K+1) proves p_(<=n)<=exp(3(K+1)). This is a complete
elementary counting proof; no external asymptotic partition estimate
or table is needed. With K<=2/epsilon, the global count is
2^{O(q/epsilon)}.

## 5. Counting feasible profiles also bounds actual enumeration work

The enumerator does not first generate all unweighted compositions.
At every occupied bin it allows exactly the counts satisfying both
the remaining count bound and the remaining lower-load bound. Every
generated partial vector is feasible and extends to a full feasible
profile by zeroing later bins. At any fixed depth, different prefixes
have different zero completions. Thus an m-bin enumeration tree has
at most (m+1) times as many nodes as full profiles.

This proves polynomial delay and polynomial amortized work per actual
output, including the input on which every profile LP fails. The same
zero-extension argument applies to the product over all machines.
Binary counters are increased only across generated children. Their
values may be large, but their bit lengths are polynomial in the
input accuracy encoding. The recursion depth is the number of occupied
input bins rather than B or K.

This is the substantive implementation point connecting the partition
bound to the actual running time. Merely checking L<=1 after generating
all compositions would not justify the stronger bound.

## 6. Initialization, zero times and exact optimization

Minimum cost over the eligible original type bases decides feasibility
without a load bound and supplies an integral initial schedule when
feasible. A separate full-total test on zero-time pairs correctly
decides whether OPT=0; it is needed even if the initially chosen
minimum-cost schedule has positive load. The empty-job case is handled
separately, and the positive-target bin construction never divides by
zero.

A common rational processing-time grid has polynomial encoding length.
Every integer schedule load and OPT belong to that grid. The initial
upper load is at most N times the largest finite eligible time, so the
number of grid-search calls is polynomial in binary input size, not
in numerical N or 1/g.

Every failed target keeps the lower endpoint strictly below OPT. Every
weak success saves its actual (1+epsilon)-bounded output at the new
upper endpoint. At adjacent grid endpoints U=L+g, integrality gives
U<=OPT; the saved schedule is therefore within 1+epsilon of OPT. This
does not assume monotone weak successes and incurs no additional
accuracy loss. The initial saved feasible schedule satisfies the same
weak-output invariant.

## 7. Complete complexity and scope

Grouping, exact LP work, machine-rank construction and one scalar-cost
intersection are polynomial per profile in H_epsilon. The streamed
profile families, polynomially many target calls and the two verified
count bounds yield both stated bounds in PS5, and hence PS1. Only
current counters, the exact optimization workspace and one saved
schedule are stored. Neither partitions, the bin universe, the whole
profile collection nor binary job units are materialized. Polynomial
space therefore holds in the full supplied encoding even for a very
small binary rational epsilon.

For epsilon>=1 the factor-two branch is sufficient, while the main
theorem covers 0<epsilon<=1. The earlier bucket theorem can have a
smaller explicit base at a weaker ratio; the new scheme provides every
fixed accuracy. Its multi-bin machine caps lie outside the earlier
one-big-group template, so there is no conflict with that template's
three-halves limit.

The known hidden-set oracle query requirement of order 2^q does not
contradict an algorithm exponential in q with an accuracy-dependent
constant. The manuscript also correctly avoids a claim of the first
ordinary fixed-machine approximation scheme. Multiple independent
budgets on the same integer assignment and optional active-machine
bases are not inferred from this result.

## 8. Verdict

The full theorem and implementation pass this review. In particular,
the improved 2^{O(q/epsilon)} time bound, exact single budget, original
mandatory totals and polynomial binary-input space all hold together.
No substantive mathematical correction is requested.
