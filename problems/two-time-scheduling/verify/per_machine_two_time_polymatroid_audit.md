# Verification note

**Curated source path:** `sources/checkpoint-q/per_machine_two_time_polymatroid_audit.md`

The source audit follows.

# Independent audit of two processing times per machine

**25 October 2026. Full independent read of
`per_machine_two_time_costed_scheduling.md`, HT1--HT14.
The theorem passes.**

This review checks the extension beyond one global pair of processing
times. The proof permits each physical machine to use a different
positive pair and preserves one original mandatory-job polymatroid
per type and one exact assignment budget. Its scaled spare-capacity
argument and its simultaneous mixed-cap recovery are both valid.

## 1. Masks preserve original mandatory amounts

Every type's total remains the original n_j throughout all masks,
including removal of pairs whose processing time exceeds the queried
target T. A full target-T integer schedule cannot use such a pair,
so this preprocessing preserves every relevant witness.

A masked type's independent rank is at most n_j. Requiring the
resource direct sum to attain total N=sum_j n_j forces all original
type equalities, because no other type has capacity above its own
n_j. A masked rank loss correctly causes rejection. The proof
never changes the job supply to the rank of a restricted ground.

Initial minimum-cost base optimization is independent across
types before load constraints. It therefore either detects budget
infeasibility or supplies an actual integral feasible schedule.
Its load is at most N times the largest input processing time.
The positive-time and nonempty-job assumptions used to declare
target zero infeasible are explicit; N=0 is handled separately.

## 2. Target-dependent machine classes preserve full schedules

After removing pairs longer than T, a machine may have zero, one,
or two remaining positive times. Zero remaining times means all
its coordinates are forced to zero. One time s_p admits the exact
integer count cap floor(T/s_p). Physical machines remain in the
original resource ground even when they leave the role-search
ground or become empty.

For a machine with two remaining times 0<u_p<a_p<=T, the easy
condition a_p<=(d-1)T/d gives an additive rounding allowance a_p
within the required factor rho_d=2-1/d. The complementary hard
condition is strict. For d>=2 it implies 2*a_p>T, so a full
target schedule has at most one large unit there.

With C_p=floor(T/u_p) and delta_p=a_p+C_p*u_p-T, one has

\[
 0<\delta_p\le a_p\le T,\qquad
 K_p=C_p-\left\lfloor\frac{T-a_p}{u_p}\right\rfloor
     =\lceil\delta_p/u_p\rceil,\qquad 1\le K_p\le C_p.
\tag{AH1}
\]

The strict positivity follows from a_p>u_p and
T-u_p*C_p<u_p. A large recipient in the full schedule has at
most C_p-K_p small units. These identities do not require common
u_p, a_p or K_p across machines.

## 3. Low quotas are handled without a zero-gap invocation

If K_p<=d, the fixed laminar caps large count<=1 and total
count<=C_p contain every full target schedule: at a large
recipient the total is at most 1+C_p-K_p<=C_p.

At an integer recovered point a large recipient has load at most

\[
 T+\delta_p-u_p
     \le T+(1-1/d)\delta_p\le\rho_d T,
\tag{AH2}
\]

because delta_p<=K_p*u_p<=d*u_p. Without a large unit, load is
at most T. This gate is exact at K_p=1 and merely relaxed for
larger K_p<=d. Neither fact is misstated as full target feasibility
upon a weak success. No quota routine with full and relaxed
targets both equal to one is invoked.

## 4. The service region remains a valid downward projection

Let H_T consist only of hard machines with K_p>=d+1. At a node
Q subseteq H_T, large H_T pairs are permitted only at Q. Small
pairs on all physical machines and every non-H_T constraint are
retained. In particular easy machines keep their fractional load
bound T and low-quota machines keep the fixed laminar caps.

The joint region X_Q contains all original resource base
equalities and the one cost budget. Its emptiness is tested
before using a service separator. If it is nonempty, the spare
projection has coordinates 0<=z_p<=C_p-small_count_p(x). It
contains zero, is convex, compact and downward.

For nonnegative lambda the support is exactly

\[
 \sum_{p\in Q}\lambda_p C_p
   -\min_{x\in X_Q}\sum_{p\in Q}\lambda_p
                                  \operatorname{small}_p(x).
\tag{AH3}
\]

Signed coefficients in this bounded inner optimization do not
give signed packing rows. The support capacity is nonnegative,
and the normalized outer support-gap LP yields a strict row
with a nonnegative normal when the query is outside the region.
Nonpositive optimum implies membership, including lower-
dimensional cases, by the established positive-part separator
argument. Direct feasibility recovers the same joint fractional
witness needed for rounding.

Resource rows are zero-one rank inequalities. All additional
load, count, base-total and budget coefficients have polynomial
bit length from the input and the current rational target.
Uniform extreme-point bounds therefore justify the outer support
LP encoding. The node recomputes these bounded quantities; it
does not recursively accumulate long symbolic descriptions.

## 5. Unequal quotas give the correct weighted omission certificate

Fix one full target-T integer schedule and let I* be precisely
its large recipients within H_T. If I* is contained in Q, every
large pair forbidden at this node was unused in that schedule.
The complete original schedule is still in X_Q: no job, cost or
resource count was discarded. It supplies spare K_p at every
p in I* and zero on the remaining coordinates.

For K_p>=d+1, the integer quota identity gives
b_p=ceil(K_p/d) with b_p/K_p<=beta=2/(d+1). Suppose a row
lambda*z<=W rejects the weak vector (b_p) on Q. Set
w_p=lambda_p*K_p. Then

\[
 w(I^*)\le W<\sum_{p\in Q}\lambda_p b_p
                 \le\beta w(Q),
 \qquad w(Q\setminus I^*)>w(Q)/R_d.
\tag{AH4}
\]

The total w(Q) is positive on a failed query because W>=0.
Every K_p is a positive binary integer, so weight scaling and
sorting retain polynomial bit complexity. AH4 is exactly the
weighted first-crossing condition at the single common ratio
R_d=(d+1)/(d-1). No equality of per-machine targets is hidden
inside this step.

The certificate family includes a deletion wholly outside I*.
Its child keeps the same entire schedule, so the invariant is
reproved after every change of Q. At zero deficit Q=I*, each
b_p<=K_p, making the query feasible. Empty-region and rank gates
cannot reject such a protected node.

## 6. One full-total integral face handles all machine classes

The recovery constructs one machine polymatroid as a direct sum
over physical machines. Its components are:

| Machine class | Integral constraints used at recovery |
|---|---|
| Empty | Zero coordinate caps |
| One remaining time | Exact total-count cap |
| Easy two-time | Ceiling caps on large prefix and full prefix |
| Hard with K_p<=d | Large<=1, total<=C_p |
| p in Q | Large<=1, small<=C_p-b_p |
| p in H_T outside Q | Large=0, small<=C_p |

Every component is an integral partition or nested-cap
polymatroid. Different classes occupy disjoint machine
coordinates, so mixing them preserves the direct-sum property.
The same successful fractional point satisfies all these caps.
Intersecting with the one original masked resource direct sum
and retaining total N gives an integral face. Minimum actual
cost on that face is at most the fractional cost. The budget
is handled as an objective comparison, not as an extra row
assumed to preserve integrality.

For an easy machine, its local upper-prefix ceilings add at most
a_p to its original fractional load. For p in Q,

\[
 a_p+(C_p-b_p)u_p
   =T+\delta_p-b_pu_p
   \le T+(1-1/d)\delta_p\le\rho_dT.
\tag{AH5}
\]

The low-quota and other classes have the bounds already checked.
Thus all machine inequalities, all original job totals and the
budget hold at the same integer point. There is no separate
rounding of overlapping type capacities by machine class.

## 7. Empty role sets, all cardinalities and exact target search

Testing Q empty through the joint LP and recovery handles k=0,
including H_T empty. It avoids normalizing a support normal on
an empty coordinate set. If a full schedule has no large
recipient in H_T, that schedule witnesses this branch even if
it has large assignments on non-H_T machines.

For k>=1 every exact cardinality up to h=|H_T| is tried. A weak
output may have a different actual number of large recipients,
which is legal because the original schedule imposes no such
cardinality requirement. All recovered assignments are kept.

The forced-seed omission time is A_d^(h-k-|Z|)*poly(H), including
all failed nodes. Global inclusion covers apply to each fixed
target and cardinality and give B_d^h*E(h)*poly(H). A monotone
subexponential upper envelope bounds this by B_d^q*E(q)*poly(H).
The target-dependent change of H_T causes no problem: this is a
separate sound gap invocation at each target, not an application
of the fixed-family rational-comparator lemma to changing families.

Choose an original common value grid g dividing every positive
processing time. Integer loads and OPT lie on it. Each failed
target remains below OPT; a weak success is saved with its actual
schedule. At adjacent endpoints the successful upper nominal
target is at most OPT. Its schedule consequently has makespan
at most rho_d*OPT. The initialization and binary lengths make
the number of target calls polynomial, regardless of numerical
job multiplicities.

The sharp algebraic time bases are correctly restricted to fixed
d. For varying binary d, the stated rational upper bound avoids
unpaid expansion of huge algebraic powers. All depth-first and
streamed-cover data have polynomial space.

## 8. Verdict and scope

All HT1--HT14 claims pass this full independent review. The
hypothesis is at most two positive times at each machine; it
allows different pairs at different machines, but does not
silently cover arbitrary many distinct times at one machine.
The theorem does not add optional active-machine selection,
startup fees, several exact assignment budgets or robust common
allocations. Those would require separate interfaces.

The ordinary cost-preserving upper-rounding comparison and
its existing multiplicity compression are documented in
`unrelated_two_size_scheduling_polymatroid_audit.md`. The extra
content of HT is the unequal-quota scaling, target-dependent
machine classification and simultaneous mixed-cap recovery on
the original physical-machine ground. No substantive correction
is requested.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
