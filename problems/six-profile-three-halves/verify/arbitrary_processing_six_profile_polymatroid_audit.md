# Verification note

**Curated source path:** `sources/checkpoint-q/arbitrary_processing_six_profile_polymatroid_audit.md`

The source audit follows.

# Independent audit of the six-profile three-halves refinement

**25 October 2026. Full independent read of
`arbitrary_processing_six_profile_three_halves.md`, SX1–SX8 and all
seven sections. Result: the stated 6^q theorem passes; no substantive
correction requested.**

The seven-profile predecessor and its separate audit remain valid
history. This review checks the new quarter-threshold classification
and also checks the complete algorithmic interfaces in the new file.

## 1. What the refinement proves

For q physical machines, arbitrary nonnegative machine-dependent
processing times, mandatory original integral recipient-polymatroid
bases, binary supplies, and one exact nonnegative assignment-cost
budget, the algorithm gives a factor-3/2 schedule in

    6^q poly(H) time and poly(H) space,

or detects that the original budget-feasible family is empty. No
small structural parameter or two-processing-value assumption is
used. The improvement from seven to six concerns the local profile
cover; it does not change the underlying model or relax the budget.

## 2. The quarter-threshold classification is exhaustive

Normalize a full-target machine load by T>0. If every unit has time
at most 1/2, profile 0 covers the whole machine. Otherwise there is
one unique unit b>1/2.

There cannot be two additional units above 1/4: together with b
their sum would be strictly greater than one. This establishes the
claimed stronger classification without assuming unit identities,
distinct types, or a bound on the number of very small jobs.

If no additional unit exceeds 1/4, b is either in (1/2,3/4] or
(3/4,1]. The remaining small load is respectively below 1/2 or
below 1/4. These are exactly profiles 1 and 2, whose small group
contains all remaining jobs.

If there is one additional unit a>1/4, then

    1/4<a<1/2,       1/2<b<3/4.

Split the a range at 3/8 and the b range at 5/8. The combination
a>3/8 and b>5/8 is impossible because it has load above one.
The other three combinations are precisely profiles 3, 4 and 5.
Their sums of open lower endpoints are 3/4, 7/8 and 7/8, so the
remaining small load fits the stated caps 1/4, 1/8 and 1/8.

Every equality case has the required ownership. Time 1/4 is small.
Time 3/8 or 5/8 belongs to its lower interval, so equality a+b=1
is not accidentally excluded. Time 1/2 is handled by profile 0
unless a separate larger unit exists, in which case such a second
1/2 unit is already impossible in a full target. Time 3/4 with
another >1/4 unit is likewise impossible; a lone 3/4 unit belongs
to profile 1. Time one belongs to profile 2 and leaves only
zero-time jobs.

Thus all full-target cases are covered. Choosing the appropriate
profile at each machine leaves the original schedule unchanged,
which preserves the coupled resource restrictions, mandatory totals
and cost simultaneously.

## 3. Independent check of all weak-output bounds

Profile 0 imposes fractional load at most one on coordinates of
time at most 1/2. Its upper-prefix recovery has load at most 3/2.

For each other profile, the small group has maximum time 1/4.
The upper-prefix estimate increases its load by at most 1/4.
Every big group has its own integer count cap one. Therefore the
normalized recovered load bounds are

    1: 3/4       +1/2+1/4 =3/2,
    2: 1         +1/4+1/4 =3/2,
    3: 3/8+5/8   +1/4+1/4 =3/2,
    4: 3/8+3/4   +1/8+1/4 =3/2,
    5: 1/2+5/8   +1/8+1/4 =3/2.

These use upper count caps only. If recovery leaves a big group
empty, its load is smaller. No unproved lower-count requirement
is being used. Conversely, the mandatory jobs cannot disappear,
because full original totals are imposed globally throughout.

The small-group prefix constraints have the integral maximum-prefix
rank described in the manuscript. Big groups have constant rank one
on every nonempty subset. Groups within a machine are disjoint,
and their direct sum over machines is one integral polymatroid
containing the fractional solution.

## 4. Resource sharing, exact cost and masked rank loss

All profile masks act on the original machine-type coordinates.
The original type count n_j never changes. Its masked resource rank
is at most n_j, so total N=sum_j n_j forces every individual type
to reach its original total. A mask that destroys a mandatory base
causes infeasibility rather than a reduced job supply.

Intersecting the resource direct sum with the machine polymatroid
gives an integral intersection. The face of total N is an integral
maximum-total face. Minimizing the actual scalar assignment cost
on this face returns an integral solution of cost no greater than
the fractional LP witness. This is enough to retain the exact
budget C; integrality of a separate added budget inequality is
neither needed nor asserted.

All machine groups are recovered at once. Different processing
classes of a type do not receive independent resource copies, and
the cost is not charged across independently rounded schedules.
These facts are essential for the arbitrary recipient-polymatroid
claim, and they remain explicit in the six-profile proof.

## 5. Optimization, zero cases, and full running time

Original full-total minimum-cost optimization correctly detects
global rank or budget infeasibility and otherwise gives an actual
initial schedule. N=0 returns the empty schedule. For N>0, the
separate restriction to zero-time pairs exactly tests OPT=0, retaining
all original type totals; only positive targets are normalized.

For T>0, a feasible profile LP gives a legal weak output of load
at most 3T/2. Exhaustive failure implies OPT>T by the full-target
cover. These are exactly the one-sided properties used by the
grid search. A failed lower endpoint L stays strictly below OPT;
an upper endpoint U stores an actual weak output. At U=L+g,
integrality of all schedule loads on the rational grid gives
U<=OPT. Hence the saved output has load at most (3/2)OPT.
No monotonicity of weak success is required.

All thresholds use constant denominators, and targets, ranks and
binary counts have polynomial encoding. The initial makespan is
at most N times the largest eligible finite time, so the number
of target calls is polynomial in H. Every one of the 6^q label
vectors, including failed masks and infeasible LPs, is charged
polynomial work. A radix-six counter, the current exact solver
state and the saved schedule use polynomial space.

The complete factor-3/2, 6^q polynomial-space theorem is therefore
accepted. The manuscript appropriately makes no optimal-base,
multiple-budget, optional-machine, robust-scenario or publication-
priority claim.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
