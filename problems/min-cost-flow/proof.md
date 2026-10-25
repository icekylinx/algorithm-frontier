# Proof note

This file is the curated proof record for the result in `README.md`. The original source note follows.

**Original source:** `sources/checkpoint-q/moving_box_log_barrier_flow.md`

# A moving-box logarithmic client for exact minimum-cost flow

**Research theorem and proof, 25 October 2026.** This note transfers the
current deterministic raw-cycle construction to a second optimization
problem. The numerical argument below is new to this checkpoint. It uses
only rational arithmetic, a pure logarithmic potential, and a small,
monotone expansion of the capacity box. In particular, it does not need
to evaluate fractional powers or to assume that the matching theorem
itself is a minimum-cost-flow oracle.

The imported algorithmic boundary is the complete raw-cycle and lifetime
interface proved in the previous checkpoint. As with that construction,
this remains a research proof, rather than an independently certified
implementation. The quantitative conclusion depends on that boundary,
not on the ability to check the final answer.

## 1. Statement and input conventions

Let an oriented multigraph have at most N edge records over its lifetime.
Parallel arcs, directed loops, arbitrary vertex degrees, and disconnected
graphs are permitted. Each arc has an integer capacity u_e >= 0 and an
integer cost c_e. The divergence vector d is integral. Original edge IDs
are retained. We first assume an explicit integral initial flow f^0
satisfying B^T f^0=d and 0 <= f^0 <= u on the initial graph. New arcs are
inserted with flow zero. Section 12 supplies an initial flow for arbitrary
demands without assuming original feasibility.

For an integral threshold F, the threshold problem asks, after each
insertion, whether some flow x satisfies

    B^T x=d,       0 <= x <= u,       c^T x <= F.             (1.1)

Once (1.1) becomes feasible, a retained feasible witness remains valid
under subsequent insertions. Explicitly writing a new full flow after
every update is a separate output cost.

Choose an exact power of two S large enough that S >= 16 and that N,
all capacities, absolute costs, initial-flow values, the absolute
threshold, and the number of nonisolated vertices are bounded by S.
Increasing S by a fixed power to absorb the artificial initialization in
Section 12 is allowed. No array of size S is allocated. For polynomially
bounded input numbers, log S=O(log(N+2)). A separate O(n+m) scan accounts
for all input vertices, including isolated vertices.

### Raw backend assumption

For every degree-three numerical graph of actual size at most S^2, assume
a deterministic backend with a computable common cap E=E(S). The cap
bounds initialization work per actual record, amortized update and query
work, complete representation logs, occurrence multiplicity, answer
piece count, and inverse raw ratio quality. It holds for adaptive
polynomial-length histories with positive integer lengths and integer
gradients of magnitude at most S^1200.

A query returns unit signed physical edges and paths in an exposed
forest. The signed physical projection is a circulation. Its numerator
is the sum of physical integer gradients; its raw denominator counts all
mapped traversals before cancellation. For optimum ratio OPT>0, the
answer has |numerator|/raw_denominator >= OPT/E. Forest edges have
lifetime-fixed physical images, true null edges have empty physical
images, and retirement callbacks retain old metadata. Dormant copies
remain counted. The numerical client maintains signed and absolute
motion on all copies and retirement buckets.

This is the interface of the following previous-checkpoint notes:

* `current_checkpoint/quantitative_matching_4_5_composition.md`,
  Sections 1--7, for the raw backend cap;
* `current_checkpoint/decoupled_numerical_client.md`, for pricing,
  degree-three ports, complete copy accounting, and refresh costs;
* `current_checkpoint/numerical_backend_lifetime_and_loops.md`, for
  transactions and immutable occurrence metadata;
* `current_checkpoint/distance_oracle_raw_lift.md`, for raw rather than
  net-length domination.

We use only these backend and numerical maintenance statements; the
matching reduction, blossom state, and matching optimality verifier are
not assumptions of the flow theorem.

**Client theorem.** On a branch satisfying the stated raw interface, the
threshold problem has a deterministic exact algorithm taking

    O((N+1) E(S)^4 poly(log S))                             (1.2)

total time, including one explicit integral feasible witness when the
answer first becomes YES. Its stored numerical values have O(log S)
bits. A failed numerical guard suspends a branch and is never interpreted
as a NO answer.

With the previous construction's cap

    E(S)=exp O((log S)^(4/5) (log log(S+4))^(1/5)),          (1.3)

the total cost is (N+1) times the same exponential order. Polynomial
powers of E do not change either exponent in (1.3).

## 2. Parameters and the expanded box

Let

    D=pow2ceil(max(16,4E)),     q=1/(16D),
    delta=S^(-1000),           epsilon=S^(-3000),
    H=S^100,                  tau=S^(-10),
    A=40N.                                                   (2.1)

If N=0, solve the instance directly. We check q >= S^(-1), D <= S^2,
and a fixed polynomial history limit S^100. These hold on a favorable
branch for all sufficiently large S; finite exceptions can be handled
by the fallback in Section 14. All parameters are integers or dyadic
rationals. Increasing fixed constants to cover a finite initial range
has no asymptotic effect.

For each currently present arc maintain outer bounds

    a_e <= 0,                  b_e >= u_e.

At birth set a_e=-8 delta and b_e=u_e+8 delta. At an exact anchor refresh,
let f_e be the current coordinate value. If f_e-a_e <= 4 delta, replace
a_e by a_e-8 delta. If b_e-f_e <= 4 delta, replace b_e by b_e+8 delta.
The flow is not changed. Then immediately price the coordinate at this
exact value under its new bounds.

The rule runs only at settled exact anchors, never halfway through a
path-list application. A coordinate whose descriptor changes is reset
and repriced as one transaction. A price replacement uses the same
logical endpoint ports and does not count as a new original arc birth.

Each anchored slack is at least 4 delta. The drift bounds proved below
then keep every current slack above 3 delta. If a refreshed slack was
small, one expansion suffices, since its old value was already positive
and the expansion adds 8 delta.

Under the history guard, the total allowed violation of the original
box obeys

    V_box := sum_e (-a_e + b_e-u_e)
            <= 16N delta + 8 delta S^100
            <= S^(-890)                                    (2.2)

for all sufficiently large S. The precise exponent is immaterial; it
is a fixed, very small inverse polynomial. The proof of the running
time subsequently shows that the favorable execution stays far inside
this history guard. Thus (2.2) is a bootstrap guard, not an assumption
that omits the cost of repeated expansions.

## 3. A pure logarithmic potential and a strong direction

While z:=c^T f-F exceeds tau, define the proof-only potential

    Psi(f;a,b)=-A log z
               + sum_e [log(f_e-a_e)+log(b_e-f_e)].          (3.1)

The algorithm does not evaluate a logarithm. At settled states put

    s_e=f_e-a_e,       t_e=b_e-f_e,
    beta_e=1/s_e-1/t_e,
    lambda_e=1/s_e+1/t_e,
    g_e=-A c_e/z+beta_e.                                    (3.2)

The following elementary inequality is the main numerical observation.
For any y in the original interval [0,u_e] and v=y-f_e,

    beta_e v >= lambda_e |v|-2.                             (3.3)

If v>=0, the difference between the right-hand length term and the
left-hand side is 2v/t_e <= 2, since y<=u_e<=b_e. If v<0, the difference
is 2(-v)/s_e <= 2, since y>=0>=a_e.

Suppose x satisfies (1.1), and let v=x-f. It is a circulation. Moreover
c^T v <= -z. Summing (3.3) gives

    g^T v >= A + ||Lambda v||_1-2|E|
            >= ||Lambda v||_1+38N.                         (3.4)

In particular v is nonzero and has positive ratio at least one. This
holds even when f lies slightly outside the original box. It uses only
that the expanded box contains the entire original feasible box.

Equation (3.4) is stronger than the inverse-polylogarithmic comparison
usually used with a power barrier. The small original-box violation is
removed exactly in Section 11.

## 4. Frozen cost gaps and coordinate anchors

Maintain an epoch gap r>0 and coordinate anchors fhat_e. At the start of
an epoch, read the entire current flow, service all small-slack bounds,
set every fhat_e=f_e, and set r=z. Between complete rebuilds, use

    Ghat_e=-A c_e/r + beta_e(fhat_e;a_e,b_e),
    lambdahat_e=1/(fhat_e-a_e)+1/(b_e-fhat_e).               (4.1)

The scalar cost term in (4.1) is frozen during an epoch. Only a notified
coordinate needs a new gradient and length. Check the exact cost after
every complete circulation update. If

    |z/r-1| > q/10000,                                     (4.2)

start a new epoch before another raw query. Insertion of a zero-flow arc
and an outer-bound change do not change z.

The occurrence machinery maintains

    lambdahat_e |f_e-fhat_e| <= q/100                       (4.3)

at every settled query state. When a logarithmic argument changes by a
relative amount at most q/100, its reciprocal changes by at most a fixed
multiple of q times its old reciprocal. Consequently

    lambda_e = (1+O(q)) lambdahat_e,
    |beta_e-beta_e(fhat_e)| <= (q/40) lambdahat_e            (4.4)

after enlarging the harmless fixed constants in the drift thresholds
if necessary. We may, for example, use q/1000 in place of q/100 in the
copy threshold construction to obtain the displayed q/40 bound.

The important cancellation is

    g_e-(r/z)Ghat_e
       = beta_e-(r/z) beta_e(fhat_e).                        (4.5)

The potentially large term involving c_e cancels exactly. Thus, by
(4.2)--(4.4),

    |g_e-(r/z)Ghat_e| <= (q/20) lambdahat_e.                (4.6)

This does not assert |Ghat_e|<=lambdahat_e, which would be false. That
distinction is the reason for normalizing the step by its numerator in
Section 7.

## 5. Integer prices, ports, and the LOW test

At an exact anchor compute using rational arithmetic

    ell_e=ceil(H lambdahat_e),
    gamma_e=round(H Ghat_e).                                (5.1)

All argument bounds remain polynomial in S. In particular

    S^(-2) <= lambdahat_e <= S^1002,
    |Ghat_e| <= S^1003,
    ell_e >= S^98,        ell_e, |gamma_e| <= S^1104         (5.2)

with ample room in the constants. They fit the original raw numerical
cap S^1200; no power-barrier price bound is invoked.

Use the degree-three port-path reduction from the previous client.
Each original logical endpoint birth receives a new port. A real arc
joins its two ports; path connectors have integer length one and
gradient zero. Repricing keeps the ports. A circulation v lifts with
additional connector length at most 2M sum_e |v_e|, where the actual
port graph has M<=S^2. The real-edge lengths in (5.2) make this overhead
negligible compared with sum_e ell_e|v_e|.

By (3.4), (4.6), integer rounding, and this port lift, feasibility of
(1.1) implies an integer-priced raw optimum of at least 1/2. Let a raw
query return a list with signed projected circulation c, integer
numerator T=gamma^T c, and raw traversal denominator V. Orient the whole
list so that T>=0. Accept it exactly when

    V>0,                      T >= 2q V.                  (5.3)

The favorable backend supplies T/V >= 1/(2E) whenever (1.1) is
feasible. Since q<=1/(64E), that answer passes (5.3). Therefore a failed
test may return NO for the current threshold instance. A structural
failure, invalid lifetime, or exceeded numerical guard is suspension,
never NO.

A defensive endpoint check may verify that the compact list projects
to a circulation by adding the imbalances of its path endpoints. It
does not replace the raw approximation hypothesis.

## 6. Additional cost aggregates and atomic transactions

Give each exposed forest occurrence of a real edge the immutable
physical cost c_e with its orientation; a true null occurrence has
cost zero. In addition to integer-gradient and length aggregates,
maintain signed cost sums along forest paths. This is one more additive
dynamic-tree aggregate. A returned list's physical cost C_list is
computed without expanding its paths.

Keep the exact total cost c^T f in a scalar. A full update by mu times
the list changes it by mu C_list. Values are exact common-grid dyadic
rationals. Full flow extraction uses all occurrence and retirement
buckets, as in the previous client.

Treat each complete cycle list as an atomic transaction:

1. Complete all no-motion backend representation changes and retain the
   old metadata needed by their callbacks.
2. Read T, V, and C_list on the returned final forest.
3. Apply the same scalar mu to every signed piece. Threshold detection
   may flag copies, but no price, descriptor, or topology update is
   interleaved with the application.
4. Settle notifications, service bounds, and rebuild the epoch if needed
   before the next query.

Individual pieces need not be circulations. The temporary scalar cost
may even put c^T f-F below zero between pieces, because a cost potential
on vertices can make open-path costs large. No logarithm, LOW decision,
or gradient is evaluated at such an intermediate state. The potential
proof concerns the straight segment between the two settled flows,
which is a segment of circulations. Coordinate slacks remain positive
even during the literal piece-by-piece implementation, by raw motion.

## 7. Numerator-normalized dyadic steps

For an accepted list choose a positive power of two mu with

    q^2/400 <= mu T/H <= q^2/200.                           (7.1)

An interval of ratio two contains such a power of two. Combining (7.1)
and (5.3) gives

    mu V/H <= q/400.                                       (7.2)

Let h=mu c be the complete physical circulation. Integer-rounding
error is at most (2H)^(-1) times the total number of traversals. By
ell_e>=S^98 and q>=S^(-1), this is negligible compared with qV/H.
Equations (4.6), (7.1), and (7.2) imply

    g^T h >= 0.9 mu T/H >= q^2/500.                        (7.3)

The total current logarithmic relative absolute motion, before any
cancellation of physical edge images, is at most 1.1mu V/H. In
particular every partial coordinate movement is at most q/300 times
its current logarithmic slack. All coordinate arguments stay positive.

For each logarithm, log(1+x)>=x-x^2 whenever |x| is sufficiently small.
The total quadratic loss is at most a fixed constant times the square
of the total relative absolute motion, hence at most q^2/100000 after
the above constants are fixed. The term -A log z is convex in z, so its
value on the complete update is at least its tangent-line value as long
as the final gap is positive. Therefore

    Psi(f+h;a,b)-Psi(f;a,b) >= q^2/1000.                    (7.4)

The positivity of the settled cost gap follows independently below.

### Why the older denominator-normalized step cannot be copied

It would be incorrect here to choose mu from mu V/H=Theta(q), without
also checking the numerator. The frozen cost term makes T/V potentially
large. Equation (7.1) bounds both objective motion and raw coordinate
motion, and is essential to this transfer.

## 8. Cost-gap motion and the number of full rebuilds

From (4.1), for the complete list,

    A c^T h/r = beta(fhat)^T h-Ghat^T h.

Using the signed cost aggregate, integer-rounding error, (7.1), and
(7.2), we obtain

    |c^T h|/r <= (2mu V/H + 2mu T/H)/A <= q/(100A).        (8.1)

Only conservative constants matter. Since r and z were within
1+q/10000 before the step, (8.1) implies z+h_cost>0, and in fact it is
within a factor 1+O(q/A) of the old positive gap. This also justifies
using the convex tangent bound in (7.4).

After an epoch reset, changing z/r by q/10000 requires Omega(A)=Omega(N)
accepted steps, by (8.1). Intermediate changes of either sign cannot
shorten this lower bound: total absolute motion bounds net motion.
Arc insertions, anchor updates, and box expansions do not change the
cost. Thus with J accepted steps there are

    O(1+J/N)                                                (8.2)

full epochs. A complete flow read, bound scan, repricing, and raw-backend
initialization costs O(N D poly(log S)) per epoch, up to the already
included cap E<=D. Their total is O((N+J)D poly(log S)).

## 9. Potential accounting, refreshes, and the history bootstrap

Before termination, z>tau=S^(-10). The magnitude assumptions and (2.2)
give z<=S^4 and all slacks<=2S. Hence

    Psi <= O(N log S).                                     (9.1)

If the last accepted step crosses the stopping threshold, (8.1) still
leaves its final gap at least tau/2. The same upper bound therefore
covers this last step as well; equivalently it can be charged as one
additional step after the bound for all preterminal steps.

Initially all slacks are at least 8delta, giving
Psi_initial >= -O(N log S). The two logarithms of an inserted zero-flow
arc contribute at least -O(log S). Summed over all insertions, the
possible downward jumps total O(N log S).

An outward box expansion strictly increases its logarithm and therefore
increases Psi. Reanchoring and changing r do not change the mathematical
potential at all. Consequently (7.4) implies

    J=O(N q^(-2) log S)=O(N D^2 log S).                    (9.2)

The old complete-copy threshold construction applies because (7.2) is
at most the raw-motion budget allowed there. At a fresh price anchor use
a threshold within a fixed factor of qH/(D ell_e), with a sufficiently
small fixed coefficient. Every genuine report consumes Omega(q/D)
new weighted absolute motion. A step creates O(q) such motion. Thus

    number of ordinary coordinate reports = O(DJ),         (9.3)

apart from original settings and the O(N+J) complete-epoch scans.
Retirement moves old motion and does not create new credit. Disabled
and dormant copies stay in the bookkeeping. Resetting a coordinate
clears all of its old drift before applying its new descriptor.

The previous numerical accounting gives

    T <= O(ND + QD + D^2J) poly(log S),                    (9.4)

where Q counts the explicitly serviced client operations and excludes
an uncharged global scan. Here Q=O(N+DJ)poly(log S), and complete epochs
have already been paid in (8.2). Substituting (9.2) gives

    T=O((N+1)D^4 poly(log S)),                              (9.5)

as claimed.

For E=S^o(1), the bounds on J, reports, bound expansions, all numerical
requests, and representation logs are eventually smaller than S^10,
well below the S^100 history cap. This closes the bootstrap that was
used for the tiny expanded-box violation in (2.2).

## 10. Finite arithmetic

No value of Psi is computed. The algorithm uses rational reciprocal
slacks, the exact rational reciprocal r^(-1), integer additions and
products, dyadic comparisons, and forest aggregates.

All flow changes are common dyadic multiples of epsilon. The root raw
numerator and denominator satisfy the previous occurrence bound

    V <= M E^2 max ell_e,       T <= M E^2 max |gamma_e|.   (10.1)

With M<=S^2, E<=S, and (5.2), T,V<=S^1110 after harmless enlargement.
Then the interval (7.1), q>=S^(-1), and H=S^100 imply mu>=S^(-1012),
up to an absolute constant. A power of two of this magnitude is an
integer multiple of epsilon=S^(-3000). The drift thresholds likewise
lie far above epsilon. All flow, anchor, bound, gradient-price, cost,
and absolute-motion records use O(log S) bits, with a fixed coefficient.

Intermediate rational operations on reciprocals of common-grid
arguments also have O(log S) bit complexity up to a fixed polynomial:
each coordinate contains only two reciprocal slacks and one reciprocal
epoch gap. No product of the denominators of all graph coordinates is
formed. In particular, rational step sizes Gamma/(g^T c) with unrelated
denominators are not accumulated across iterations; the common
power-of-two step in (7.1) prevents that problem.

## 11. Exact recovery by affine-penalty circulation rounding

Stop the numerical phase as soon as the settled exact cost obeys

    c^T f <= F+tau.                                        (11.1)

The divergence is exactly integral. Also each coordinate lies in its
original interval [0,u_e] up to the total violation (2.2).
Let

    B0=sum_e |c_e|(u_e+1),
    P=2B0+2|F|+10,
    J_pen(x)=c^T x + P sum_e max(0,-x_e,x_e-u_e).           (11.2)

The input bounds give P<=S^10 for sufficiently large S. Thus

    J_pen(f) <= F+tau+P V_box < F+1/4.                     (11.3)

On every open unit interval (floor(f_e),ceil(f_e)), the coordinate
penalty in (11.2) is affine, because all its breakpoints are integral.
Keep every coordinate within its initial floor/ceiling interval.
Repeatedly choose a cycle in the fractional-edge support, orient its
motion so that the affine objective does not increase, and move until
at least one coordinate becomes integral. Fix integral coordinates and
continue. Exact conservation is preserved throughout.

Treat a fractional directed loop as a one-edge cycle. If the remaining
fractional support were a nonempty forest, one of its
leaves would have a single strictly fractional incident contribution,
contradicting its integral divergence after subtracting the already
integral edges. Thus the process ends at an integral flow x with
the same divergence and J_pen(x)<=J_pen(f).

The standard dynamic-forest implementation performs O(m) insertions and
deletions, path affine-objective sums, path residual minima, and path
adds. Each coordinate becomes integral once. All new integer edges
hit on a path are listed and removed; they are not revisited in later
fractional cycles. This gives O(m polylog(m+S)) deterministic bit work.
This is also the floor/ceiling cycle-rounding mechanism used in the
previous checkpoint's exact-projection note.

Since V_box<1/4, every final coordinate is in [-1,u_e+1]. If any
coordinate violates the original box, its integer violation is at least
one, and

    J_pen(x) >= P-B0 > F+1/4,

contradicting (11.3). Thus x is exactly feasible in the original box.
Its cost is integral and below F+1/4, so c^T x<=F. We return this explicit
original-edge flow and check its capacity, divergence, and cost by a
linear scan.

## 12. Arbitrary demands and initial feasibility

First remove isolated zero-demand vertices after an O(n+m) input scan.
If the demand sum is nonzero, or if an isolated vertex has nonzero
demand, the instance is infeasible. A vertex demand whose absolute value
exceeds the sum of its incident capacities is also an immediate
infeasibility certificate.

For the remaining instance add a hub r. With the convention that d_v is
net inflow, add an artificial arc r->v of capacity d_v when d_v>0,
and an artificial arc v->r of capacity -d_v when d_v<0. Put |d_v| flow
on it. Give every original arc flow zero. This is an explicit integral
flow with divergence d at the original vertices and zero at r.

Let B_orig=sum_original |c_e|u_e, and give every artificial arc the
same positive integer cost P_art=4B_orig+1 (or any larger integer).
The augmented graph has O(m+n_active) records and polynomially bounded
data when the original data are polynomially bounded.

Every original feasible flow extends by zero artificial flow. Its cost
is between -B_orig and B_orig. Every integral augmented flow with a
positive artificial flow has cost at least P_art-B_orig>B_orig.
Therefore the augmented optimum uses no artificial flow exactly when
the original problem is feasible. If it does, its restriction is an
optimal original flow.

For an incremental fixed-threshold problem with F<=B_orig, a YES
augmented witness automatically has zero artificial flow. One may use
a fixed bound on the final original data when choosing P_art. Thresholds
outside the original possible objective range are handled by a
feasibility query or by their immediate comparison meaning.

If initial padded cost already meets the target, perform the exact
recovery and check immediately; there is no need to evaluate log z.

## 13. Static optimization and the new quantitative application

The augmented problem always has a feasible initial flow. Its optimum
is an integer between -B_orig and the known initial augmented cost.
Binary search with the exact threshold algorithm needs O(log S) calls.
Each call starts afresh on the same actual graph and retains an explicit
feasible upper-end witness. The final witness is an optimal augmented
flow; Section 12 either returns the optimal original flow or correctly
reports infeasibility.

Thus, for polynomially bounded integer capacities, costs, and demands,
the proposed deterministic algorithm for arbitrary directed multigraphs
has total time

    O(n+m)+(m+1) exp O((log(m+2))^(4/5)
                          (log log(m+4))^(1/5)).           (13.1)

It returns an exact explicit minimum-cost flow, or reports infeasibility.
There is no sparsity, bounded-degree, acyclicity, bipartiteness, or
perfect-feasibility promise on the input. Maximum flow and capacitated
bipartite min-cost flow are standard direct specializations.

The incremental threshold algorithm has the same total exponent with N
equal to the total original record bound, on the fixed correct backend
parameter choice. Unknown final N can be handled by ordinary doubling
and complete restarts on the current graph, retaining already found YES
witnesses. Such restarts add only the usual geometric-series overhead.
The separate online uniformization issue is discussed in Section 14.

## 14. Final optimality verification and uniform static acceptance

For a proposed integral augmented flow x, first check capacities and
divergence. Form its directed residual graph: an arc of cost c_e exists
when x_e<u_e, and a reverse arc of cost -c_e exists when x_e>0. A feasible
flow is optimal exactly when this residual graph has no negative-cost
cycle. Add a zero-cost supersource to every vertex.

Haeupler, Jiang, and Saranurak, *Deterministic Negative-Weight Shortest
Paths in Nearly Linear Time via Path Covers*, arXiv:2511.08551v1,
Theorem 1.1, supplies deterministic negative-cycle detection or shortest
distances in O(m log^8 n log(nW)) time for integer weights of magnitude
at most W. On the no-negative-cycle case, the returned potential pi is
checked explicitly on every residual arc:

    cost(u,v)+pi(u)-pi(v) >= 0.                             (14.1)

Check that every potential value is a finite integer and that (14.1)
holds on every residual arc, with its original direction and cost.
The augmentation has polynomial cost magnitude, so this verifier costs
only (n+m)polylog(n+m+S), which is absorbed by (13.1). A negative cycle,
invalid flow, or failed inequality rejects the candidate.

This supplies a safe static analogue of the previous matching
acceptance construction. Run fixed-constant candidate programs under
deterministic interleaving, with a terminating classical min-cost-flow
fallback. Keep each candidate's threshold decisions private. A worker
may be accepted only after its final integral augmented flow passes
(14.1). One fixed favorable worker has the proved cost (13.1); its
constant execution share and verifier do not change that exponent.
Other workers cannot cause an incorrect accepted answer. The augmented
optimum also certifies original infeasibility as in Section 12.

This argument does not validate every online NO answer of an arbitrary
unproved worker. The incremental theorem uses the fixed parameter tuple
justified by the backend proof. Rechecking a full optimal flow after
every insertion would not preserve the claimed incremental total time.

Primary verifier source:
<https://arxiv.org/html/2511.08551v1>.

## 15. What is established by this note

The reusable new statement is a complete reduction from the stated raw
cycle-and-occurrence interface to exact capacitated minimum-cost flow,
with polynomial loss in E and O(log S)-bit stored data. The proof gives
an explicit constant-strength comparison direction, a correct
numerator-normalized dyadic step, an epoch rule for the global cost
coefficient, tiny monotone box expansions, and exact integer recovery.

The 4/5 quantitative conclusion additionally uses the previous raw
backend construction. Its public comparison and the provenance of
every external primitive are recorded separately in the transfer
baseline note. This numerical proof neither claims a new result for
negative-weight static shortest paths nor relies on a matching
certificate to establish flow optimality.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
