# Exact factor three halves for arbitrary processing times with seven profiles

**25 October 2026. Root and independent full mathematical reviews completed; valid seven-profile predecessor.**

The profile approximation scheme admits a substantially smaller explicit
state family at factor three halves. Seven labels per physical machine
suffice for arbitrary machine-dependent processing times, mandatory
integral recipient-polymatroid bases, binary supplies and one exact
assignment-cost budget.

## 1. Model and theorem

Let P be q>=1 physical machines. Every type j has a normalized monotone
integral submodular recipient rank f_j and mandatory original count

    n_j=f_j(P),  N=sum_j n_j.                                      (SP1)

A schedule consists of integer vectors x_j in B(f_j). Eligible pairs
(p,j) have arbitrary nonnegative rational processing times ell_pj and
nonnegative rational assignment costs c_pj. Additional eligibility masks
are allowed but never reduce the original n_j. The one cost budget is

    sum_(p,j) c_pj x_j(p) <= C,  C>=0.                             (SP2)

OPT is the minimum makespan among original schedules satisfying SP2.
H denotes the binary input and the paid polynomial rank, SFM, exact LP
and polymatroid-intersection work. Counts are not expanded into unit
copies.

**Theorem SP.** A deterministic algorithm either detects infeasibility
even without a load bound or returns an integer schedule of makespan
at most (3/2)OPT, preserving every original mandatory type base and
the exact budget, in

    7^q poly(H) time and poly(H) space.                           (SP3)

This is an all-instance theorem in the stated oracle model. The number
q counts physical machines, with no small-corank, small-heavy-support,
eligibility-width or processing-time-diversity assumption.

The exact three-halves ratio here is attained by finitely many profiles.
It is separate from the earlier one-big-group bucket theorem, whose
particular finite-label curve approaches three halves from above.

## 2. One joint integral recovery and the small-group estimate

Use one coordinate per eligible machine-type pair. After any mask, the
available rank of type j is at most its original n_j. Requiring total

    sum_(p,j) x_j(p)=N                                           (SP4)

therefore forces every type to attain its original total. A type that
loses available rank cannot be repaired by increasing another type.

Intersect the masked resource direct sum with one integral machine-cap
polymatroid containing a fractional point of total N. The intersection
and its total-N face are integral. Minimizing the actual assignment
cost on that face gives an integer full schedule of no larger cost.
Thus a fractional witness with cost at most C produces a schedule
with the budget exact. This uses a scalar objective on an integral
face, not integrality after adding a budget constraint.

For completeness, an upper-prefix chain for one machine group is built
by sorting its processing times v_1>=...>=v_m>=0 and setting

    X_h=sum_(i<=h) x_i,  U_h=ceil(X_h).

The integer prefix caps have rank max{U_h:e_h in S}, with empty rank
zero, and define an integral polymatroid. Summation by parts gives

    sum_i v_i x'_i
       <= sum_h (v_h-v_(h+1)) ceil(X_h)
       <= sum_i v_i x_i + v_1,  v_(m+1)=0.                       (SP5)

Hence a small group loses at most its largest allowed processing time
in upper rounding. A count-one cap on a disjoint big group is another
integral polymatroid. All such groups and all machines are combined
by direct sum in the same recovery, so resource sharing and the budget
remain joint.

## 3. The seven target-T profiles

Fix T>0. All interval endpoints and loads in this section are normalized
by T. A notation such as (a,b] means aT<ell_pj<=bT. Every pair not in
one of the allowed groups for its machine's label is forbidden.

Profile 0 permits every pair of time at most T/2. Its fractional total
load is capped at T. It receives one upper-prefix chain on all allowed
coordinates, so its integer load is at most

    T+T/2=3T/2.                                                  (SP6)

The other six profiles have small group 0<=ell_pj<=T/3. Their big
groups and normalized fractional small-load caps are as follows.
Every displayed big group has its own **integer count cap one**.

| Profile | Allowed big group 1 | Allowed big group 2 | Small-load cap divided by T |
| --- | --- | --- | --- |
| 1 | (1/2, 2/3] | none | 1/2 |
| 2 | (2/3, 5/6] | none | 1/3 |
| 3 | (5/6, 1] | none | 1/6 |
| 4 | (1/3, 5/12] | (1/2, 7/12] | 1/6 |
| 5 | (1/3, 5/12] | (7/12, 2/3] | 1/12 |
| 6 | (5/12, 1/2] | (1/2, 7/12] | 1/12 |

All groups within a row are disjoint. Exact endpoint ownership is
specified by the open lower and closed upper endpoints. In particular,
time T/3 is always small; time T/2 is permitted in profile 0 and may
belong to the first big group of profile 6, but never to a big group
whose lower endpoint is T/2. These overlaps across different profiles
are harmless.

For a chosen label at every machine, solve a single rational LP with
the original resource constraints, original mandatory totals, SP2,
the table's count caps and fractional small-load caps, and profile 0's
load cap where appropriate. Skip an empty LP. No type total is reduced
when its permitted pairs are insufficient.

## 4. Every feasible profile LP rounds within three halves

On a positive-profile machine, keep each big group's count-one cap
and construct an upper-prefix chain on its small coordinates. This
integral machine polymatroid contains the fractional point. Use the
joint full-total minimum-cost recovery from Section 2.

The integer big load is at most the sum of the listed upper endpoints,
since each big group contains at most one unit. By SP5 the integer
small load is at most the table's small-load cap plus T/3. Thus all
six estimates, normalized by T, are

    Profile 1:  2/3        + 1/2  + 1/3 = 3/2,
    Profile 2:  5/6        + 1/3  + 1/3 = 3/2,
    Profile 3:  1          + 1/6  + 1/3 = 3/2,
    Profile 4:  5/12+7/12  + 1/6  + 1/3 = 3/2,
    Profile 5:  5/12+2/3   + 1/12 + 1/3 = 3/2,
    Profile 6:  1/2+7/12   + 1/12 + 1/3 = 3/2.                  (SP7)

Empty big groups only improve these bounds. There is no need to require
one unit in every allowed big group. All original type counts and the
budget are preserved by the same integral point; no mandatory job is
discarded during or after rounding.

Together with SP6, every feasible fixed-label LP therefore supplies a
legal schedule of makespan at most 3T/2.

## 5. Every full target schedule is covered

Consider an original integer schedule of makespan at most T and cost
at most C. Fix a machine.

If it has no job larger than T/2, choose profile 0. Its original
fractional load cap and pair mask are satisfied without changing the
schedule.

Otherwise it has a unique job larger than T/2. There are at most two
jobs larger than T/3, because three such units have total load greater
than T. Multiple units of the same type count separately for this
argument, but no individual unit identity is needed by the algorithm.

### 5.1 Exactly one job above T/3

The unique such job is above T/2. Its time lies in exactly one of
(T/2,2T/3], (2T/3,5T/6], or (5T/6,T], giving profile 1, 2 or 3.
Every other job is in the small group. Its total load is at most T
minus the actual big time, and hence at most T times one minus the
lower endpoint of the chosen interval. This is the corresponding
small-load cap in the table.

### 5.2 Two jobs above T/3

One exceeds T/2; the other lies between T/3 and T/2. Partition the
large range into width-T/12 bins with normalized lower endpoints

    lambda_i=1/3+i/12,  i=0,1,2,... .                            (SP8)

The smaller job has index 0 or 1, and the larger has index at least 2.
If their indices are i and j, both actual processing times strictly
exceed their lower endpoints. A full-T schedule therefore requires

    lambda_i+lambda_j<1,
    i+j<4.                                                       (SP9)

The only ordered-by-size possibilities are

    (i,j)=(0,2), (0,3), (1,2).                                   (SP10)

They are exactly profiles 4, 5 and 6. In particular, the apparent
pair (1,3) has lower sum one, so its actual processing sum would be
strictly greater than T and is impossible. The remaining jobs have
time at most T/3 and total load at most T minus the two actual big
times, hence at most T times one minus their lower-endpoint sum.
Those are precisely the listed small-load caps.

This exhausts all machines and keeps the original schedule unchanged.
Thus at least one of the 7^q fixed-label LPs is feasible whenever
the original full target T is feasible. Exhaustive failure implies

    OPT>T.                                                       (SP11)

A weak success need not certify makespan T, and no such inference is
used.

## 6. Initialization, zero times and exact target search

First minimize assignment cost over the original resource bases on
eligible pairs, preserving every original n_j. Failure of full totals
or a minimum cost above C certifies original infeasibility even with
unbounded load. Otherwise retain an integral minimum-cost schedule
as a finite initial upper bound. When N=0, return the empty schedule.

Test zero makespan exactly by keeping only zero-time pairs and using
the same original full-total minimum-cost optimization. On success
return that zero-load schedule. On failure, OPT>0, so zero is a sound
failed lower endpoint.

Choose a positive rational g dividing every positive finite processing
time. A common denominator and the gcd of scaled numerators give such
a grid in polynomial bit length. All integer loads, including OPT,
belong to g times the nonnegative integers.

Initialize L=0 and U equal to the makespan of the saved feasible
schedule. At grid midpoints T run all seven-profile label vectors.
A total failure raises L and preserves L<OPT by SP11. A weak success
lowers U and saves its actual schedule of makespan at most 3T/2.
At adjacent endpoints U=L+g, grid integrality gives U<=OPT. The
saved schedule consequently has makespan at most (3/2)OPT.

The initial feasible upper schedule satisfies the same weak-output
invariant, and no monotonicity of weak successes is assumed. Zero
times, zero capacities, empty groups and masked rank loss are all
handled by the full-total tests. The initial upper load is at most
N times the largest finite time, so the number of target calls is
polynomial in the binary input, not in the numerical job count.

## 7. Time, space and the comparison boundary

At each target there are 7^q label vectors. One exact LP, the prefix
caps and the integral minimum-cost recovery use polynomial paid
oracle work per vector. The interval denominators are constants and
all target arithmetic has polynomial bit length. Labels are streamed
with a radix-seven counter; only the current workspace and best
schedule are retained. Polynomially many target calls prove SP3 and
polynomial space, without expanding binary supplies.

The preceding `arbitrary_processing_bucket_scheduling.md` gives smaller
bases for weaker ratios, including 5/3 in 2^q and 11/7 in 3^q. The
present theorem supplies the exact 3/2 endpoint in 7^q. The broader
`arbitrary_processing_profile_approximation_scheme.md` supplies
(1+epsilon) approximation in 2^{O(q/epsilon)} polynomial time, with a
larger general-purpose profile bound. On two-size and per-machine
two-time instances, the separate omission-based results achieve exact
three halves with a base below two and remain stronger there.

The existing full-oracle hidden-set lower bound for factors strictly
below three halves is consistent with all these statements. It does
not prove the base seven optimal at factor three halves, and no such
optimality or publication-priority claim is made. Ordinary fixed-machine
approximation schemes and cost-preserving upper rounding are public
background; this note isolates a finite-profile consequence in the
stated full recipient-oracle and exact-budget model.
