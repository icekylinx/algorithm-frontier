# Independent audit of arbitrary-processing bucket scheduling

**25 October 2026. Reviewer: allocation_four. Full fresh read of
arbitrary_processing_bucket_scheduling.md, AB1--AB13 and all nine
sections.**

## Verdict

The complete mathematical chain passes. In the stated full
recipient-polymatroid oracle model, with all original type bases
mandatory and one exact assignment-cost budget, the manuscript proves
the deterministic tradeoff

\[
 \gamma_k=\frac{3\cdot2^k-1}{2^{k+1}-1},
 \qquad
 (k+1)^q\operatorname{poly}(H+k)
\]

with polynomial space. In particular k=1 gives factor 5/3 in
2^q polynomial time, k=2 gives 11/7 in 3^q, and increasing k gives
3/2+epsilon in the stated logarithmic-in-accuracy machine-label base.

This is an exponential-time theorem. The audit does not establish
publication priority, a polynomial-time improvement for unrestricted
unrelated scheduling, or an algorithmic lower bound at the limiting
factor three halves.

## 1. Correct input ground and mandatory totals

The coordinate ground is the explicit collection of eligible
machine-type pairs. A coordinate is an integer count, so large binary
job multiplicities do not expand the ground.

Type j originally requires n_j=f_j(P). Masking assignments can lower
the rank available to that type, but never lowers its original required
total. In the resource direct sum every type total is at most n_j.
Consequently the global equality

\[
                        \sum_{p,j}x_j(p)=\sum_jn_j
\]

forces every individual type total to equal its original n_j. A lost
unit of one type cannot be replaced by an extra unit of another.
This remains true in the rounding intersection after the mask.

A mask that reduces a type's available rank below n_j is genuinely
infeasible. The manuscript does not silently remove the unavailable
mandatory jobs.

## 2. The full-total minimum-cost face preserves the budget

For a fixed feasible fractional vector, the resource direct sum and
the machine polymatroid constructed from that vector are both integral
polymatroids on exactly the same coordinate ground. Their intersection
is integral. The fractional vector has total N, while the resource
direct sum bounds the total by N, so the total-N face is nonempty and
integral.

Minimizing the actual one scalar assignment cost on that face has an
integer optimum whose cost is no larger than the feasible fractional
cost. Thus the resulting integer schedule respects the supplied budget
exactly.

This argument uses cost minimization over an integral face. It does
not require the generally false assertion that adding an arbitrary
budget inequality to an integral polytope preserves integrality.
The single-objective nature of this recovery is essential to the stated
scope.

## 3. Independent derivation of the chain rank

Within one ordered group, let U_h be the nondecreasing integer prefix
ceilings. The proposed rank is

\[
            r_G(S)=\max\{U_h:e_h\in S\},\qquad r_G(\varnothing)=0.
\]

This formula is correct. If h is the largest index in a nonempty S,
the prefix constraint bounds x(S) by U_h. Conversely, all mass U_h
can be placed at e_h while respecting every prefix, so this value is
the actual rank of S. Applying the rank constraint to each prefix
recovers its original prefix cap, hence the two descriptions coincide.

The maximum of the weights of selected elements is normalized,
monotone and submodular. One direct representation is a sum of
nonnegative increments times indicators of hitting nested suffixes.
The rank is integral and its oracle uses only a maximum over the
explicit group. It does not depend on expanding any of the U_h slots.

## 4. The upper-load rounding inequality

For v_1>=...>=v_m>=0, put v_(m+1)=0. Summation by parts gives

\[
 \sum_i v_i x'(e_i)
 =\sum_h(v_h-v_{h+1})x'(\{e_1,\ldots,e_h\}).
\]

Every coefficient is nonnegative. Replacing each prefix by its ceiling
adds at most

\[
                 \sum_h(v_h-v_{h+1})=v_1.
\]

Thus the integral group load is at most the fractional group load plus
the largest processing time in that group. Empty groups have zero
load; zero-time entries have zero contribution even when their counts
are large. The full-total equality still retains these zero-time jobs.

No assumption that a fractional count is at most one is used for a
small-job group. That matters for binary job-polymatroid supplies.

## 5. Bucket arithmetic and disjointness

Writing B=2^k and D=2B-1, the thresholds are

\[
                    l_i=\frac{B+2^i-1}{D}.
\]

They strictly increase from l_0=B/D>1/2 to l_k=1. Direct substitution
gives l_0=gamma_k-1 and

\[
                      l_i+2(1-l_{i-1})=\gamma_k.
\]

A positive label therefore has disjoint big and small groups. Every
allowed big pair lies in a bucket whose upper endpoint is at most T.
The explicit upper bound by T is necessary and is present in the
manuscript; a lower-threshold test by itself would be insufficient.

Ties are correctly assigned: a time exactly l_i T belongs to bucket i,
and a time exactly l_0 T belongs to label zero. Small-group thresholds
are inclusive. Forbidden intermediate processing times cannot occur
among the remaining jobs of the corresponding full-target machine.

## 6. Full-target completeness with one unchanged schedule

In a full-T integer schedule, a machine has at most one job unit with
time greater than l_0 T, because l_0>1/2. This statement concerns units,
so two copies of the same type are also excluded from that big group.

If there is no such unit, label zero contains every assigned pair and
the fractional load constraint T is satisfied by the original integer
schedule. Otherwise the unique large unit belongs to a unique bucket i.
Its time is strictly greater than l_(i-1)T, so the total load of all
other jobs is strictly below (1-l_(i-1))T. Each individual remaining
nonnegative processing time obeys the same bound.

The original entire schedule therefore satisfies one enumerated label
vector, all unchanged original resource bases, and the same cost
budget. This is a simultaneous label witness, with no independent
per-machine resource choices or copied jobs.

For k=0, label zero admits all pairs of time at most T. Every full-T
schedule is feasible for that ordinary load LP, as required.

## 7. Legal recovery for every feasible label LP

A label-zero machine receives its one prefix chain. Its final load is
at most T+l_0 T=gamma_k T.

A label-i machine receives a capacity-one group for all big coordinates
and a disjoint prefix chain for all small coordinates. These are
combined with every other machine in one direct sum, then intersected
with the single original resource direct sum. Hence the rounding is
joint even when a type is big on one machine and small on another.

The integer big count is zero or one and its load is at most l_i T.
The small fractional load and maximum small processing time are both
at most (1-l_(i-1))T. Their recovered load is at most twice that amount.
The total is bounded by gamma_k T.

No lower bound on big count is needed. If the integer result uses no
big job on a positive-label machine, its load only decreases. Every
mandatory original unit is nevertheless retained by the global
full-total equality.

## 8. Initialization, the zero gate, and one-sided minimization

Minimum-cost assignment of all original resource bases on the initial
eligibility mask is integral and polynomial in the paid oracle model.
It either detects that no budget-feasible schedule exists at any load,
or supplies a valid finite upper schedule.

The zero-time test restricts to zero-time pairs but retains every
original total. It exactly determines whether makespan zero is
possible. This avoids trying to infer positive lower bounds when zero
processing times are present.

After zero has failed, a common rational processing grid g exists with
polynomial bit length. Every integer schedule load, and therefore OPT,
is a multiple of g. The initial schedule supplies a saved upper target U.

In the subsequent search, a rejected target T is strictly below OPT,
because total label failure excludes every full-T schedule. Weak success
only supplies a schedule of load at most gamma_k T; it is not a full-T
decision. Keeping the failed lower endpoint L preserves L<OPT even when
algorithmic successes are nonmonotone.

At adjacency U=L+g, grid integrality yields U<=OPT. The saved output
then has load at most gamma_k U<=gamma_k OPT. The initial saved schedule
also satisfies its required weak bound, so there is no missing
initialization case. The number of target calls is polynomial in the
binary size of N, the processing times and g.

## 9. Time, space, and the limiting template

There are exactly (k+1)^q label vectors; each is processed in polynomial
time in H+k. The threshold coefficients use O(k) bits. A streamed
radix counter, one LP/intersection workspace and one best schedule
suffice, proving polynomial space.

The identity

\[
                \gamma_k-\tfrac32
                   =\frac1{2(2^{k+1}-1)}
\]

proves the stated logarithmic choice of k for a rational accuracy
request. No exponential-in-job-count identity enumeration is hidden
inside one label.

The scope-limited optimality calculation also passes. If only the
upper bounds 1+l_0 and l_i+2(1-l_(i-1)) are used, a common factor gamma
imposes

\[
 l_0\le\gamma-1,\qquad l_i\le2l_{i-1}+\gamma-2.
\]

Iterating and requiring l_k>=1 yields gamma>=gamma_k. This is
optimality of that template and those load bounds. It does not rule
out other rounding constraints, finer state descriptions, or different
algorithms below the limit.

## 10. Scope clarification communicated to the author

The inherited oracle barrier below factor three halves should be read
with its original polynomial/corank-FPT parameterization. Its hidden-set
query bound is at most 2^q, so it cannot exclude arbitrary
machine-parameterized time F(q) times a polynomial. In particular it
does not establish three halves as an impossibility threshold for
general q-exponential algorithms.

The manuscript already separates its exponential time from
polynomial-time unrelated scheduling and makes no first-result claim.
The ordinary unrelated-job specialization has substantial public
fixed-machine approximation literature. The present audit establishes
the full stated mathematical model and explicit time-quality tradeoff,
not an exhaustive priority comparison.
