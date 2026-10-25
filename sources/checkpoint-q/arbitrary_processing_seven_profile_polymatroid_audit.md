# Independent audit of the seven-profile three-halves scheduling theorem

**25 October 2026. Full independent read of
`arbitrary_processing_seven_profile_three_halves.md`, SP1–SP11 and all
seven sections. Result: the exact factor-three-halves theorem passes;
no substantive correction requested.**

This review checks both the numerical seven-label cover and its full
oracle-model implementation. It does not claim that seven is the
minimum possible number of labels or that the resulting time base is
optimal.

## 1. Model and accepted claim

The result uses q physical machines, arbitrary machine-dependent
nonnegative processing times and assignment costs, arbitrary integral
recipient polymatroids, mandatory original type bases, binary counts,
and one exact assignment-cost budget. It either detects that no
original budget-feasible schedule exists or returns a schedule of
makespan at most (3/2)OPT in

    7^q poly(H) time and poly(H) space.

All physical machines participate in the exponent. There is no
heavy-support, rank-deficiency, two-size, or processing-time-diversity
promise. Zero processing times are allowed and handled explicitly.

The mandatory-base and one-budget interfaces are the same as in the
fully audited arbitrary-processing approximation scheme. They are
rechecked below because a correct interval table alone would not
suffice to establish the stated model.

## 2. The fixed-label LP and integer recovery remain joint

After a label restricts permitted pairs, every type has available
rank at most its original n_j. The total requirement N=sum_j n_j
therefore forces each original type to retain exactly n_j units.
No label is allowed to shrink a type's mandatory supply to its new
masked rank.

For label 0, the recovery uses a prefix chain on all permitted
coordinates, ordered by processing time. For a positive label, each
allowed big group receives its integer count-one cap and the small
group receives its own prefix chain. The groups are disjoint within
the machine; taking their direct sum across machines gives one
integral machine polymatroid containing the fractional LP solution.

The masked resource direct sum is a second integral polymatroid on
the same original pair ground. Their intersection is integral, and
the nonempty maximum-total face at N is integral. Minimizing the
one actual cost on that face produces an integer solution no more
expensive than the fractional point. This simultaneously preserves
every original resource base and the exact cost budget.

In particular, a type that has different processing classes on
different machines remains one recipient polymatroid. No capacities
are copied between profile groups, and no separately rounded cost
objectives are combined afterward.

The prefix chain has rank max_{h in S}ceil(X_h). Its prefix caps are
equivalent to those rank inequalities. Summation by parts bounds
its rounded load by its fractional load plus the largest time in
the group. Zero-time coordinates retain count caps and mandatory
totals even though their load contribution is zero.

## 3. All seven weak-output load bounds are exact

Normalize by a positive target T. Label 0 allows times at most 1/2
and requires fractional total load at most one. Prefix recovery
therefore has load at most 3/2.

Every positive label allows small times at most 1/3. Its small
rounded load is at most the listed fractional small-load cap plus
1/3. Each disjoint big group has count at most one, so its load is
at most that group's closed upper endpoint. The complete sums are

| Label | Maximum big load | Small cap | Prefix allowance | Total |
| --- | --- | --- | --- | --- |
| 1 | 2/3 | 1/2 | 1/3 | 3/2 |
| 2 | 5/6 | 1/3 | 1/3 | 3/2 |
| 3 | 1 | 1/6 | 1/3 | 3/2 |
| 4 | 5/12+7/12 | 1/6 | 1/3 | 3/2 |
| 5 | 5/12+2/3 | 1/12 | 1/3 | 3/2 |
| 6 | 1/2+7/12 | 1/12 | 1/3 | 3/2 |

These bounds use only upper count caps. A recovered schedule that
uses zero units in an allowed big group satisfies an even smaller
load bound. Exact or positive lower group counts are unnecessary.
All jobs remain present through the separate global total-N face.

Thus every feasible fixed-label LP gives a legal weak schedule of
makespan at most 3T/2, regardless of whether the label vector arose
from any full-T integer schedule.

## 4. Exhaustive cover of a full-target witness

Consider the unchanged job multiset on one machine in a full-T
integer schedule.

If every unit has time at most T/2, label 0 covers the entire machine
and its fractional load bound. This case includes two jobs near T/2,
so they do not need to fit any of the positive labels.

Otherwise there is exactly one unit greater than T/2. At most two
units can be greater than T/3. These statements concern units, even
when two units have the same type; their counts can still be stored
without expansion.

If only one unit exceeds T/3, it lies in exactly one of

    (1/2,2/3], (2/3,5/6], (5/6,1]

after normalization. Choosing label 1, 2 or 3 puts every other unit
in the small group. Its total load is at most one minus the actual
big time and hence at most one minus the interval's lower endpoint.
Those bounds are exactly 1/2, 1/3 and 1/6.

If there are two units above T/3, write the smaller first. It is
at most T/2, whereas the larger is strictly greater than T/2. In
width-1/12 bins with lower endpoints 1/3+i/12, the smaller therefore
has index i in {0,1} and the larger has index j>=2. Both actual
times strictly exceed their respective lower endpoints. Hence

    2/3+(i+j)/12<1,

or i+j<4. The only possible pairs are (0,2), (0,3), and (1,2).
These are exactly labels 4, 5 and 6. Their lower sums are 5/6,
11/12 and 11/12, which give the table's residual small caps 1/6,
1/12 and 1/12.

The apparently missing pair (1,3) has lower sum one. Since both
lower endpoints are open, it cannot occur in a full-T schedule.
This strict endpoint fact is needed for completeness and is correct
as written. Times exactly T/3 are small; T/2 can belong to label 0
or the first group of label 6, and is never in an interval whose
lower endpoint is T/2. Internal upper endpoints likewise have the
declared closed ownership. There is no uncovered equality case.

All machine labels can be chosen independently from the original
full schedule. The schedule remains the same feasible joint point,
so its shared resource restrictions and cost remain valid. Therefore
some one of the 7^q LPs is feasible whenever a full-T schedule exists.
Exhaustive LP failure soundly certifies OPT>T.

## 5. Initialization, zero target, and one-sided minimization

Before using profiles, the original full-total minimum-cost problem
detects rank or budget infeasibility without a load bound. A feasible
integral minimizer supplies a finite initial schedule. The empty
schedule solves N=0.

For N>0, a separate exact zero-target test keeps only zero-time pairs
and preserves all original totals. This detects OPT=0 even if the
initial cost minimizer happened to have positive load. The positive
target normalization is used only after this test fails.

All processing times have a common positive rational grid g with
polynomial bit length. Integer count schedules, including those with
binary-large supplies, have grid loads. The search keeps a certified
failed lower endpoint L<OPT and a saved actual weak output at upper
endpoint U. Total profile failure raises L; weak success lowers U
and saves its schedule.

The upper endpoint need not remain above OPT. What is required is
the weak-output invariant. At adjacent grid endpoints U=L+g,
integrality gives U<=OPT, and the retained output consequently has
load at most (3/2)OPT. Weak success monotonicity is not assumed.
The initial actual schedule already satisfies the weak-output
invariant. Its load is bounded by N times the largest finite pair
time, so binary search makes only polynomially many target calls.

## 6. All-input time, space, and scope

There are exactly seven candidate labels per machine. A radix-seven
counter streams all vectors using polynomial workspace. This counts
bad labels, masked rank failures and infeasible budget LPs as well
as successful cases. Each LP, prefix construction and full-total
minimum-cost recovery uses the stated polynomial exact-oracle work.
All interval denominators are constants, and all target and count
encodings remain polynomial in H.

Consequently the total running time is 7^q poly(H), with polynomial
space and without materializing resource units. The theorem's exact
three-halves endpoint follows from its finite table, without taking
an accuracy limit or hiding an extra parameter in the exponent.

The accepted claim concerns one exact assignment-cost budget and
mandatory job-polymatroid bases on fixed physical machines. It does
not extend the same rounding to multiple budgets, optional machine
selection, or scenarios. Nor does it establish an optimal time base
at factor three halves. Within its stated scope, the manuscript's
complete theorem passes this independent audit.
