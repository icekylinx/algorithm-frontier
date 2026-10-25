# Root audit: binary large-slot surplus and general-size scheduling

**25 October 2026. Completed full review of S1--S28.**

The theorem in `compressed_large_slots_corank_makespan.md` passes
this root review and two independent full reviews. For largest
job size a, largest strictly smaller size u, and a supplied budget
k, it always retains the public OPT+a schedule and additionally
achieves (1+epsilon)OPT+u whenever the optimum's largest-job slot
surplus is at most k. For 0<epsilon<=1/2 its time is
Gamma(1/epsilon)^k poly(H), with polynomial workspace in the
physical binary input. No slot or resource-supply expansion occurs.

## 1. The surplus is defined only after a genuine rank test

At target T, the largest-job slot bound is

    s_p(T)=min(f_b({p}),floor(T/a)),    N(T)=sum_p s_p(T).

Every original target schedule has a largest-job base inside this
box. If its capped rank is below h=f_b(P), failure is genuine.
Otherwise its natural slot matroid has rank h and corank
c=N(T)-h>=0. The budget condition is written N(T)<=h+k, even at
infeasible targets where N(T)-h may be negative. The algorithm
never places a negative number into an exponential bound.

The model allows arbitrarily many smaller job sizes and arbitrarily
many largest units on one machine. Equal largest-size types may
be aggregated and decomposed again. Empty and one-size instances
have separate polynomial algorithms.

## 2. The full-machine workload dual gives a linear per-slot promise

Choose the exact original size grid g and write 1-epsilon=B/A.
Then Delta=g/A makes all smaller-size multipliers integral and
sets t=a/Delta, b=(1-epsilon)t to positive integers with ratio
t/(t-b)=1/epsilon. At a g-grid target, C=T/Delta is also integral.

Aggregate the smaller workload, cap it at C, and test preservation
of its total rank. Only then form the complement dual f_T on all
physical machines. In an original target schedule, its largest
base x* and smaller workload w* obey

    C*1-w* >= t*x*.

Thus t*x* is independent in f_T. The lifted rank
f_T(owners(Z)) is a valid polymatroid on conceptual slots, and
uniform service to the selected slots is equivalent to service
proportional to their owner counts. This is an explanatory
expansion only. The implemented algorithm works with those
counts and never materializes the slots.

The same full-ground dual is retained during all count deletions.
Machines with no remaining largest slot stay available for smaller
jobs in the original resource and its final completion.

## 3. Count-only deficient-set branching is complete

For remaining counts n, test that the large box retains rank h,
then separate b*n from f_T by minimizing f_T(R)-b*n(R) over
physical machine subsets. If it is nonnegative, any largest-job
base x<=n satisfies b*x in P(f_T).

Otherwise put m=n(R), ell=m-floor(f_T(R)/t), and d=n(P)-h.
Every promised x* leaves at least ell omitted slots inside R.
The ell>d guard is therefore sound and is checked before
enumeration. If ell<=d, an exact-sum deletion pattern z supported
on R, bounded by n and of total ell, can be chosen below n-x*.
That branch preserves x*. Induction proves target completeness.

Each count pattern injects into an ell-subset of the conceptual
m slots by selecting the first z_p slots of each owner. Deficiency
gives ell>m epsilon, so there are at most
Gamma(1/epsilon)^ell attempted patterns. Failed rank tests are
counted as terminal children. The complete attempted recursion
has at most (c+1)Gamma(1/epsilon)^c nodes, including unpromised
targets.

The exact-sum iterator is necessary. At a coordinate, its feasible
interval is bounded below by the remaining total minus all later
capacities and above by the smaller of its capacity and the
remaining total. Every permitted partial choice has a completion,
so the enumeration has polynomial delay per emitted pattern.
An unrestricted rectangular enumeration in this small-corank
branch would not justify the claimed bound; the manuscript does
not use one.

## 4. Binary corank requires a separate space argument

Unlike an explicit-element corank, c may be exponentially large
in its binary encoding. A recursion stack of c frames would not
be polynomial space. The manuscript addresses this directly.

When c<q^2, the count recursion has polynomial depth. When
c>=q^2, enumerate all q-dimensional deletion vectors bounded by
c and the slot capacities, retaining those of total c. There
are at most (c+1)^q rectangular candidates. For all integers
q>=1 and c>=q^2,

    (c+1)^q<=e^c<=4^c<=Gamma(1/epsilon)^c.

The first inequality follows from q log(c+1)<=c at c=q^2 and
monotonicity thereafter; the last uses epsilon<=1/2. Every
promised largest base appears in this enumeration, and exact
physical-ground separation tests each candidate. Its counters
occupy only q times logarithmic numerical space.

This hybrid implementation proves the advertised polynomial
workspace in the original physical input. The entropy expression
is an analysis bound and is not numerically evaluated.

## 5. Reconstruction preserves all original jobs

Complete b*x to an integer base y of the fixed dual. Its
complement w=C*1-y is an integer base of the capped smaller
workload and, by the rank test, of the original aggregate workload.
The separately proved player-by-type intersection decomposes
that workload into fractional original smaller-job bases without
expanding multipliers. Upper rounding preserves each type's
full integer base and adds at most u per machine.

The largest assignment x remains integral and is bounded by
s_p(T)<=floor(T/a). Each final load is therefore at most

    T+(a-b Delta)x_p+u
       =T+epsilon a x_p+u <=(1+epsilon)T+u.

This computation retains x_p throughout; it does not assume
x_p<=1. Every original job type is reconstructed as a full base.
The +u is a real rounding loss, which cannot be deleted to claim
an unconditional approximation scheme.

## 6. The budget cap never becomes a false infeasibility certificate

N(T) is nondecreasing. On the original size grid up to the total
workload V, compute the largest T_cap with N(T_cap)<=h+k.
This is a search-budget predicate, not an original-feasibility
predicate. If the true optimum satisfies the parameter bound,
then T_cap>=OPT and the full target routine must succeed there.

If that first routine fails, return the independently computed
public additive fallback. If it succeeds, run a one-sided
minimization search entirely below T_cap. All failures are actual
original infeasibility conclusions. Adjacent failed-lower and
successful-upper grid points force the saved successful target
at most OPT, giving the strong bound. This remains valid when
the first routine succeeds even though the sufficient parameter
condition did not hold.

All endpoint, midpoint and slot computations have polynomial bit
length. The procedure makes polynomially many target calls and
keeps the better actual schedule. At no point is an over-budget
target declared infeasible or a success assumed monotone.

## 7. Exact scope of the improvement

The theorem is useful when the potential largest-job positions
at OPT are nearly saturated. It includes the earlier Boolean
corank when OPT<2a but also allows many largest units per machine.
Under the additional explicit condition u<=epsilon OPT, it gives
(1+2epsilon)OPT. Without that condition it is an additive result.

The separate exact three-halves two-size theorem remains stronger
in other regimes and is retained as an independent candidate.
There is no claim of a uniform better-than-two polynomial
algorithm for all job-size instances, an optimal exponential
base, or an exhaustive priority comparison.
