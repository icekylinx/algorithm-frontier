# Independent audit: compressed largest-job slots and binary-space corank scheduling

**25 October 2026. Full independent review of S1--S28 passed.**

Reviewed manuscript:
`compressed_large_slots_corank_makespan.md`.
The review concentrates on the conceptual-slot reduction, exact
count-pattern enumeration, the binary-encoded corank space issue,
and the one-sided budgeted optimization. No mathematical correction
was required.

## 1. Accepted guarantee and parameter

The theorem always keeps the public additive schedule of makespan
at most OPT+a. If the optimum's total available largest-job slot
count minus its required largest-job rank is at most k, it also
returns a schedule of makespan at most

\[
                              (1+\epsilon)\mathrm{OPT}+u
\]

in Gamma(1/epsilon)^k poly(H) time and polynomial workspace, for
0<epsilon<=1/2. The slot count and k may be binary-large. The
theorem does not assume one largest unit per machine, and it keeps
both its parameter condition and its additive smaller-job term.

The no-job, zero-largest-rank, and one-size cases are separately
handled. In the nontrivial branch h>0 implies OPT>=a>0, so zero
is a valid failed target for minimization search.

## 2. The target construction is on the full physical ground

The large box cap s_p=min(f_b({p}),floor(T/a)) is necessary for
every target-T integer schedule. Its total retained-rank test is
the correct polymatroid box formula. If rank h survives, N-h is a
nonnegative conceptual matroid corank. Negative values at earlier
infeasible targets are never used as recursion budgets.

The smaller-workload scaling Delta=g/A gives integral multipliers,
integral target cap C=T/Delta, and exact quotas t=a/Delta,
b=(1-epsilon)t with t>b. The ratio is exactly 1/epsilon, without
an integer-rounding exception.

An original target schedule's smaller-workload vector is a base
of the summed workload polymatroid F. The cap C preserves its
total rank whenever the target is feasible. The complement dual
f_T is then a valid integral polymatroid, formed once on all
physical machines. Every later deletion keeps this same f_T.
Re-dualizing after a count deletion would not preserve the
original target implication; the manuscript explicitly avoids it.

## 3. The conceptual slot model and count promise agree

The natural large-job matroid on s_p slots per owner is valid:
slot independence is precisely independence of its owner-count
vector in P(f_b). Its augmentation follows from integral
polymatroid augmentation, and its total rank is the retained box
rank h. The lifted recipient function f_T(owners(Z)) is monotone
and submodular: owner unions are exact, while the owners of an
intersection form a subset of the intersection of owner sets.

Uniform t units on a selected slot set are feasible in the lifted
recipient polymatroid exactly when the aggregated vector t*x is
feasible in P(f_T). One direction tests all slots belonging to
each owner subset; the other bounds a partial slot subset by its
full selected owner counts. Owners with no available slots have
zero selected count and are harmless by monotonicity.

The original target inequality gives y*_p>=t*x*_p for the dual
base y*. Downward closure proves the exact per-slot promise. The
slot universe is only a proof device; the implemented recursion
uses q-dimensional binary count vectors throughout.

## 4. The compressed omission recursion is complete

At remaining counts n, box rank h guarantees that some original
large base remains. The separation function f_T(R)-b*n(R) is
submodular on the q physical machines. If no violation exists,+b*n is resource independent, and any boxed large base x<=n
provides a valid output.

For a violated owner set R, m=n(R) and
ell=m-floor(f_T(R)/t) satisfy 1<=ell<=m. A promised base x*
omits at least ell available slots inside R and exactly d=n(P)-h
slots in total. The guard ell>d is therefore a sound rejection
before enumeration. Removing zero-count owners from R can only
decrease the submodular objective, so the simplified deficient set
remains valid.

Every integer pattern z supported on R with z<=n and total ell
is considered. The omitted count vector n-x* has enough capacity
inside R to dominate at least one such pattern. That child still
contains x*, retains large rank h and keeps its stronger quota
promise. Induction on d proves every failure is sound and every
returned base is valid on both promised and unpromised inputs.

## 5. Pattern count and polynomial delay are both paid

Map each deletion pattern to the first z_p slots of each owner.
This is an injection into the ell-subsets of m conceptual slots.
The strict deficit gives ell>m/R_0, where R_0=1/epsilon, hence
the number of patterns is at most Gamma(R_0)^ell. Attempted
patterns whose child rank test fails are counted as terminal
children of remaining measure d-ell. The resulting computation
tree bound is (c+1)Gamma(R_0)^c.

The exact-sum iterator is also correct. At a partial assignment,
its next-coordinate interval is precisely the range whose
remaining sum fits in the remaining total capacities. Integer
interval capacities realize every intermediate sum, so every
generated partial node extends a valid output pattern. At each
fixed depth distinct partial choices extend distinct leaves.
Thus total iterator work is polynomial per emitted pattern; no
unpaid rectangular search is used in the small-corank recursion.
Only binary remaining sums and capacities are stored.

## 6. The hybrid implementation establishes binary polynomial space

This is a necessary part of the theorem. If c<q^2, the recursive
depth is below q^2, and each frame stores only q-dimensional
count vectors, an owner set and a polynomial-space iterator.
Consequently the stack is polynomial in the physical input.

For c>=q^2, the manuscript instead enumerates omission vectors
directly with q binary counters. Even a rectangular scan has at
most (c+1)^q candidates. The inequality

\[
                              (c+1)^q\le e^c
\]

holds for every integer q>=1 and c>=q^2. Indeed the function
c-q log(c+1) is increasing there, and at q^2 its value is
q[q-log(q^2+1)]>=0; x-log(x^2+1) is increasing for x>=1 and
positive at x=1. Since epsilon<=1/2, Gamma(1/epsilon)>=4>e.
This direct count scan therefore fits the claimed time and uses
polynomial space even when c is exponentially large numerically.

Every promised large base appears in that scan as z=s-x* with
sum c, and each z_p is automatically at most c. Testing the two
physical-ground inequalities certifies every returned candidate.
Neither numerical h nor c is used as a stack depth in this branch.
The small-case factor c+1 is absorbed only after c<q^2 has been
established, so it is not silently treated as polynomial in the
binary encoding in the large-corank branch.

## 7. Reconstruction preserves all jobs and the load estimate

Complete b*x to a dual base on the full physical ground. Its
coordinate bound C makes w=C*1-y nonnegative, and complement
duality puts w in B(G). The preserved total rank makes it a base
of F as well. The reviewed compressed decomposition yields
fractional bases of every original smaller-job polymatroid;
upper rounding gives integer bases with per-machine additive u.
No job units are discarded in this scheduling reconstruction.

The retained large assignment x is a full original base and can
be decomposed among original largest-size types. On every machine,

\[
 a x_p+\Delta w_p+u
     \le T+\epsilon a x_p+u
     \le(1+\epsilon)T+u,
\]

where the last inequality uses x_p<=floor(T/a). This is valid
with any number of largest units on that machine. It does not
replace x_p by one or import a T<2a assumption.

## 8. The budget prefix and target search are sound

N(T) is nondecreasing, so N(T)<=h+k defines an initial segment of
the original load grid. The largest capped target in [0,V] can be
found with polynomially many binary comparisons. The grid is
polynomial-bit and V is a genuinely feasible upper makespan from
the total workload.

An over-budget target is never called infeasible. If the capped
endpoint has a successful schedule, ordinary one-sided grid
minimization is valid: failed targets are strictly below OPT,
successful targets have recorded approximate schedules, and at
adjacency the successful upper target is at most OPT. Monotone
success is unnecessary.

Under the theorem's parameter condition, OPT lies in the budget
prefix. The capped endpoint is then at least OPT and is genuinely
feasible, so all necessary-rank tests and the complete promise
routine must succeed there. This proves entry into the stronger
search under the stated hypothesis. If it fails outside that
hypothesis, the public additive fallback remains intact.

The small-unit consequence u<=epsilon OPT gives factor
1+2epsilon exactly as stated. The earlier exact 3/2 two-size
theorem avoids this additive rounding and is correctly identified
as a distinct result. All S1--S28 claims pass this independent audit.
