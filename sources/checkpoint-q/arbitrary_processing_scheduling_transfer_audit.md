# Independent review of the arbitrary-processing bucket scheduling theorem

**25 October 2026. Reviewer: transfer_frontier. Full mathematical review of
`arbitrary_processing_bucket_scheduling.md`, including AB1--AB13 and all
remaining sections: PASS.**

The main theorem has arbitrary nonnegative rational machine-dependent
processing times, mandatory original recipient-polymatroid bases, and
one exact assignment-cost budget. This review checks that full model,
not merely ordinary explicit jobs or common job sizes. It is an internal
mathematical review, not a formal verification or a publication-priority
claim.

## 1. The mandatory-total and exact-cost interface

Every original type j has mandatory count n_j=f_j(P). Masking forbidden
pairs can only decrease its available rank. Requiring total N=sum_j n_j
over the masked resource direct sum therefore forces every type to keep
its original n_j; one type cannot compensate for another type's rank
loss. This is the correct interface for scheduling mandatory jobs.

An integral machine-cap polymatroid intersects the resource direct sum
in an integral polytope. A fractional point of total N certifies that
the maximum-total face at N is nonempty. Minimizing the actual scalar
assignment cost on that face returns an integer full schedule whose
cost is no larger. This proves exact budget preservation without the
incorrect assumption that adding a budget inequality preserves
integrality. All later rounding uses this same full-total face.

This argument uses ranks and caps in binary and one coordinate per
machine-type pair. It requires no expansion of individual job copies.

## 2. Prefix ceilings really give the claimed integral polymatroid

Within one group, processing times are in nonincreasing order and
U_h=ceil(sum_{i<=h} x_i) is a nondecreasing sequence of integers. The
rank

    r(S)=max{U_h : e_h in S},  r(empty)=0

is normalized, monotone and submodular. It is equivalent to the full
set of prefix caps: every subset S lies inside the prefix ending at its
largest index, whose cap is exactly r(S), and every prefix is itself a
rank constraint. This checks both directions of the rank description,
including repeated or zero caps.

Summation by parts gives

    sum_i v_i x'_i
      <= sum_h (v_h-v_{h+1}) ceil(X_h)
      <= sum_i v_i x_i + v_1.

The nonnegative coefficient differences telescope to v_1. Zero-time
coordinates have no load contribution but remain subject to the full
prefix count cap and, ultimately, to the original mandatory totals.
Disjoint machine groups combine by direct sum, so prefix rounding for
one group and a count-one cap for another group can be imposed in one
integral intersection.

## 3. Exact bucket arithmetic and coverage

For k>=1 let D=2^(k+1)-1. Direct substitution gives

    gamma_k=(3*2^k-1)/D,
    l_i=(2^k+2^i-1)/D,
    l_0=gamma_k-1>1/2,
    l_k=1,
    l_i+2(1-l_{i-1})=gamma_k.

The l_i are strictly increasing. Thus the big intervals
(l_{i-1}T,l_iT] partition exactly (l_0T,T]. For a positive label, the
small upper bound (1-l_{i-1})T is strictly below the big lower bound,
so the two allowed groups are disjoint. The upper bound l_iT<=T on
the big group is explicit and essential.

Any integer target-T schedule either has no job above l_0T on a
machine, or has exactly one: two such units exceed T because l_0>1/2.
In the latter case the unique big job determines its label. Every
other job, and the sum of all those other processing times, is at most
T minus that big processing time and hence strictly below the allowed
small bound. Nonnegative times justify passing from the sum bound to
each individual pair. Therefore one enumerated label vector retains
the original schedule unchanged, including every type total and its
exact cost.

For k=0, the separate definition is consistent: there is only label
zero, its size cutoff is T, and gamma_0=2. No positive-label argument
is needed in that case.

## 4. Every feasible label LP yields a legal weak schedule

For a label-zero machine, the original fractional load is at most T
and its largest allowed time is at most l_0T. The prefix estimate
therefore gives load at most (1+l_0)T=gamma_kT.

At a label-i machine, the integer big group has at most one unit,
whose time is at most l_iT. The small group has fractional load and
largest allowed time each at most (1-l_{i-1})T. Its rounded load is
at most twice that quantity. The total is consequently at most

    [l_i+2(1-l_{i-1})]T=gamma_kT.

There is no requirement that an integer output use a big unit on
every positive-label machine. An empty big group only improves this
bound. All machines and types are rounded in the same intersection,
so there is neither duplicated resource capacity nor discarded work.
The scalar cost argument from Section 1 preserves the budget jointly.

It follows that total failure at T is a sound assertion OPT>T, while
success only certifies the returned gamma_kT schedule. The manuscript
uses exactly that one-sided implication.

## 5. Feasibility, zero times and target optimization

Minimum-cost original resource bases on the supplied eligible pairs
give an exact feasibility test without a load bound. Rank loss or a
minimum cost above C certifies infeasibility of the original instance.
Otherwise the saved integral schedule supplies a finite upper target.

The separate zero-time test is necessary and correct. Restricting to
zero-time pairs while retaining all original totals and minimizing
cost decides whether OPT=0. Only after that test fails does the
algorithm use zero as a failed lower endpoint. The N=0 and all-times-
zero cases are therefore covered without an implicit positive-time
assumption.

A common rational grid g for the positive input processing times has
polynomial encoding length: a common denominator may be a product of
input denominators, whose bit length is their total bit length. Every
integer load is on the g grid. The initial upper load is bounded by N
times the largest finite time, so its grid index also has polynomial
bit length.

In the one-sided minimization search, every failure raises a lower
endpoint L that remains strictly below OPT. Weak successes lower the
upper endpoint and save their actual output, without asserting full
target feasibility. At adjacent grid endpoints, U=L+g<=OPT, so the
saved output is at most gamma_kOPT. The initial feasible upper
schedule satisfies the same saved-output invariant. No monotonicity
of weak successes is used and no grid-rounding approximation is lost.

## 6. Time, space and the limiting curve

There are exactly (k+1)^q label vectors. One exact bounded rational LP
and one cost-preserving integral full-total recovery per vector use
polynomial oracle work and polynomial space. The thresholds have O(k)
bits, and all counts remain binary. Streaming the label vectors and
retaining only the current LP workspace and best output establishes
the stated

    (k+1)^q poly(H+k) time,  poly(H+k) space.

The exact approximation gap is

    gamma_k-3/2=1/[2(2^(k+1)-1)].

Choosing k logarithmic in 1+1/epsilon gives the stated
[O(1+log(1+1/epsilon))]^q dependence. No finite k is claimed to attain
the limiting factor three halves. The table values 2, 5/3, 11/7,
23/15 and 47/31 check directly.

## 7. The limited optimality statement and public scope

Within the exact template analyzed in the manuscript, a common bound
gamma implies l_0<=gamma-1 and l_i<=2l_{i-1}+gamma-2. Induction gives

    l_k <= (2^(k+1)-1)gamma-(3*2^k-2).

Requiring l_k>=1 yields gamma>=gamma_k. The displayed thresholds
attain equality. This is an optimality result for those specific
recovery inequalities and that contiguous one-big-group template; it
is not a lower bound against other scheduling algorithms.

The source and scope qualifications are appropriate. Cost-preserving
additive rounding for ordinary unrelated jobs is public background;
ordinary unbudgeted machine-parameterized approximation schemes also
exist. The manuscript's claim concerns the explicitly stated full
recipient-oracle model, exact budget, and bucket curve, with no claim
of the first fixed-parameter constant approximation or of optimal
exponential bases. The inherited oracle obstruction strictly below
three halves does not rule out stronger algorithms at or above that
threshold.

## 8. Verdict

All sections pass. The proof retains mandatory jobs, a single exact
assignment budget, polynomial binary arithmetic and polynomial space
through the full target search. No substantive mathematical correction
is requested.
