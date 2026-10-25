# Local exact projection from a priced-step interface

**Status.** This is a mathematical reconstruction of the local projection
in OAI Section 4. It proves the locality, threshold certificates, exact
output, and client work from an explicit priced-step contract and an exact
static flow primitive. It does not prove either numerical primitive here.
In particular, the exact flow existence argument below is not being used
as an uncharged global flow algorithm. The parent ledger and partition are
frozen throughout a projection call.

Primary framework and source passages:

- [OAI preprint source](https://github.com/openai/math/tree/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026),
  Section 3, *Exact exchange projection*; Section 4, *A local exact
  projection*; Section 5, *Priced logarithmic steps*.
- The elementary small-total-violation argument is Section 2, *Integral
  cuts from a small total violation*. Its proof is included below.

The proof is independent of how an integral parent is represented.
Persistent transportation carriers can provide the point interface, but
must not change the frozen version read by the tests.

## 1. Input, arithmetic, and the two imported primitives

Fix a master size S=2^s and a sufficiently large fixed integer a. Put

    B = 2^ceil(s/a),    q = B^(-100),
    delta = S^(-1000), epsilon = S^(-3000).

The row/bin graph is a partition state of a graph of maximum physical
degree three on at most S physical vertices. A bin d has positive integer
weight w_d and contains 2w_d-1 physical vertices. A row has at most three
physical bin incidences. Parallel incidences have different permanent
identifiers. Enumerating a bin and its incident rows costs its physical
weight times a polylogarithmic overhead; reading a row's incidences costs
polylogarithmic time. The partition remains unchanged during this call.

For every incidence e=(r,d), an integral allocation x_e is nonnegative,
and the allocations at each row sum to a positive integer L. Write

    y_d = L - sum_(e at d) x_e.

The input has nonnegative integral debts p_d and satisfies the stronger
floor

    y_d + p_d >= (c+1) w_d,                 (1)

where c>=1 is an integer. Let P=sum_d p_d. The intended phase supplies
L=O_a(S), c=O_a(1), and P=O_a(S). These magnitude bounds, or equivalent
explicit polynomial-magnitude bounds compatible with the priced-step
interface, are necessary arithmetic premises. A statement allowing an
arbitrarily long binary encoding of L would not have the claimed time.

Identifiers have O_a(log S) bits, or a charged polylogarithmic equivalent.
The data interface supplies exact point access to x,y,w,p, an index of
the positive debts and their sum, and sparse indexed updates. Each access
and physical-identifier translation has polylogarithmic overhead. The
version read by every threshold test and by final recovery is the same
immutable parent. Later edits are made on a separate child version.

### Priced-step contract

We import the following part of OAI Section 5. A represented oriented
graph has variables on the epsilon grid and objective terms

    log(f-D1) + log(D2-f),    or    -W log(T-f).

At a current feasible logarithmic argument, let g be the objective
gradient. Let lambda_e be the sum of the absolute derivatives of the
individual logarithmic terms on coordinate e, including their weights.
In particular, lambda is not the absolute value of the sum g_e.

For a nominal lifetime size R with R+B<=S^(1+2/a), the interface:

1. Never returns LOW when a nonzero circulation d satisfies
   g^T d >= (1/2) sum_e lambda_e |d_e|, except by an explicitly reported
   failure or suspension.
2. Otherwise performs an exact circulation increment h with
   sum_e lambda_e |h_e|<=q/100, and increases the objective by at least
   a fixed positive constant times q^2. All arguments remain positive.
3. After settlement, exposes registers fhat_e satisfying
   lambda_e(fhat_e)|f_e-fhat_e|<=q/100. Descriptor changes can reanchor
   exactly. Register refreshes are reported through a dirty-entry list;
   their number is at most the number of successful steps times
   S^(O(1/a)+o_a(1)), apart from explicit client operations.
4. Costs (R+B+Q)S^(O(1/a)+o_a(1)) for Q external operations, including
   point reads, descriptor changes, topology edits, and pricing calls.
   Maintenance without a step causes no primal motion.

All polynomial-magnitude and argument-range prerequisites are checked.
The source also supplies finite loose operation guards and their
eventual adequacy. The proof below closes the corresponding client
counts; it does not require a global coordinate scan after a step.

### Static flow contract

For an explicitly represented directed graph of size Z with integral
capacities of O_a(log S) bits, import a deterministic exact maximum-flow
algorithm returning an explicit integral flow and residual min-cut. Its
time, after padding Z to at least B, is

    (Z+B) S^(o_a(1)).

Only zero lower bounds are required algorithmically. To reduce large
capacities on a small local graph to one fixed polynomial-capacity
implementation, process capacity bits. In a digit round c'=2c+xi, an old
minimum cut shows that the residual augmentation over twice the old flow
is at most the number A of original arcs. An optimum residual augmentation
can have its cycles discarded, after which each residual arc carries at
most A. Truncate residual capacities at A and use the fixed primitive.
There are O_a(log S) digit rounds. This establishes the stated local
capacity reduction without choosing a new algorithm from the ratio of
log S to log Z.

## 2. Full exchange network and local regions

Set

    b_d = max(cw_d-y_d,0),
    u_d = max(y_d-cw_d,0),
    beta = sum_d b_d.

The full exchange graph has arcs

    s -> d : capacity b_d,
    d -> t : capacity u_d,
    d -> r : capacity x_e       for every physical incidence e=(r,d),
    r -> d : capacity L+1       for the same incidence e.

The last two arcs are separate identified arcs, including when several
physical incidences have the same row and bin endpoints. All lower
bounds are zero. Since (1) implies b_d<=p_d, beta<=P.

A **seed** satisfies p_d>=w_d/2. The total seed weight is at most 2P.
Because debts are integral, their positive index has at most P entries;
listing it finds every seed and computes beta. Every positive deficit is
a seed: y_d<cw_d and (1) imply p_d>w_d.

Initialize by expanding all seeds before any pricing step. Expanding a
bin exposes all its bin-to-row incidence arcs, its true source and sink
capacities, and every row-to-bin incidence arc and endpoint of the rows
thus discovered. Repeated discoveries retain the original arc identifier
and do not insert a second copy. An unexpanded represented bin is a
boundary. It is not a seed, has b_d=0, and satisfies

    u_d = y_d-cw_d >= w_d-p_d > w_d/2.       (2)

In particular u_d is an integer at least one.

Two graphs are associated with a region:

- The **true graph** uses the represented arcs and the true sink capacity
  u_d at every represented bin.
- The **optimistic graph** instead gives each boundary a sink capacity
  beta+1. Expanded bins keep their true capacities.

The true graph is a subnetwork of the full graph. The optimistic graph
has maximum value at least the full maximum. For the latter assertion,
take a full integral source-to-sink flow, decompose it into paths after
discarding cycles, and truncate each path at its first boundary. Send its
remaining value directly from that boundary to t. Every path begins at
a seed, and every prefix through expanded bins and discovered rows is
represented. The total value is at most beta, smaller than beta+1.

This is a global flow-value domination argument. It does not assume that
beta+1 exceeds the true spare of each boundary; a boundary with u_d much
larger than beta is harmless.

If beta=0, the unchanged allocation already has y>=cw. Return it with
empty child debt. Below assume beta>0, and hence P>=1.

## 3. A threshold test with permanent sink locks

Fix an integer 1<=b<=beta. Start a fresh region and multiply every
ordinary capacity by 16. Add a return arc t->s with variable z. Define

    T=16b,                 W=20000(P+1).

For an ordinary arc, write its current unpadded bounds as l_e,U_e.
Initially l_e=0. Its positive pads are zeta_e^-,zeta_e^+. Use

    Phi(F,z) = sum_(ordinary e)
               [log(F_e-l_e+zeta_e^-)+log(U_e+zeta_e^+-F_e)]
               - W log(T-z).                              (3)

Start every flow at zero. New ordinary arcs also start at zero. No
client operation changes any existing flow value: only the imported
circulation steps move the point. Thus conservation is exact even while
the represented topology grows or sink bounds change.

### Pads, conservation, and the return arc

Start each pad at 4delta. When a cached argument is at most 3delta,
increase that side's pad by 4delta and reanchor exactly. Descriptor
changes also reanchor. With tau=q/100<=1/100, the register guarantee
bounds the error in an individual positive argument by tau times its
cached value. The step bound similarly bounds its relative change by
tau. Therefore the service keeps arguments above delta before steps and
above delta/10 at refreshes, with substantial slack.

A pad increase changes no other argument adversely and causes no motion.
Once repaired, a side cannot require another repair without further
motion or a bound change. Dirty-entry lists and newly inserted or
changed descriptors suffice; no complete scan is used.

Under the loose S^100 external-operation guard, the total current pad sum
satisfies, including the first guarded attempted operation,

    alpha = sum_e (zeta_e^-+zeta_e^+) < S^(-800).             (4)

Indeed O(S^100) settings of size O(delta) contribute O(S^(-900)). This
preliminary estimate uses the finite guard, not the later sharp step or
region bound, so the locality proof is not circular. All ordinary
unpadded violations sum to at most alpha. Exact source conservation
then gives

    -alpha <= z <= 16beta+alpha.                            (5)

At a loop test, read z exactly. Stop successfully if z>=T-1/4. Otherwise
T-z>1/4, and a priced step obeys

    W |Delta z|/(T-z) <= tau.

It cannot cross T, and after even the last successful step T-z>=1/8.
Consequently the return logarithm stays in its required domain and has
a polynomially bounded argument at every loop or service state.

### Boundary service and its quantitative margin

Before another priced step, expand every boundary whose cached sink
flow is at least 8u_d. Replace its optimistic sink interval by

    [4u_d,16u_d],                                          (6)

and retain the lower lock for the rest of this test. Its newly discovered
arcs have zero flow. Pads may be reset when the bounds change.

For an unlocked boundary, its lower logarithmic argument is F_e+zeta^-.
The register contract implies

    |F_e-Fhat_e| <= tau(Fhat_e+zeta^-).

Because u_d>=1 and zeta^-<=alpha, an untriggered boundary has actual
flow less than 8.2u_d. During one step,

    |Delta F_e| <= tau(F_e+zeta^-),

so its post-step flow is less than 8.3u_d, and in particular less than
10u_d. At the first trigger, actual flow exceeds 7.9u_d, and in
particular exceeds 7u_d. The new lower and upper bounds (6) therefore
have a constant interior margin. Bound changes require no primal
correction to install the lock.

Service all triggered entries before the next step. Checking new and
dirty registers suffices: a cached value cannot newly cross the trigger
without its register changing. The register-error bound controls the
unreported movement. No-motion reanchoring preserves the same estimates.

If success is detected immediately after a step, a newly triggered
boundary need not be expanded. It still has F_e<10u_d<16u_d, below its
true scaled capacity. This avoids an uncharged final boundary scan.

## 4. The explored region has O(P) cumulative volume

At any loop or service state, let H contain all expanded or triggering
nonseed bins. A previously locked sink has F_d>=4u_d-zeta_d^-; a newly
triggering sink has F_d>7u_d>4u_d. Every other sink has flow at least its
negative pad violation. Since the sink flows sum to z, (4)--(5) give

    4 sum_(d in H) u_d <= 16beta+2alpha.

Combining with (2),

    sum_(d in H) w_d < 8beta+alpha <= 8P+alpha.

Seeds contribute at most 2P. Thus all expanded bins together have total
weight below 10P+alpha, and certainly at most 11(P+1).

This is a cumulative bound: a bin is expanded only once and the region
never shrinks during a test. It also bounds the work of a triggering bin
before the next pricing call. A high-weight boundary can be read by point
access, but cannot become an uncharged high-weight expansion.

For expanded weight V, physical degree three gives at most 6V discovered
bin-to-row incidences, at most 18V row-to-bin incidences, and at most 18V
boundary occurrences. Expanded bins, boundaries, and their source/sink
arcs therefore give fewer than 1000(P+1) ordinary arcs. Every ordinary
arc is born once; every sink is locked at most once. Logical endpoint and
vertex births obey the same O(P+1) bound. A nominal engine lifetime size
8192(P+1) is sufficient.

For fixed parameters P=O_a(S), this nominal size plus B eventually obeys
R+B<=S^(1+2/a). The source's phase magnitude bounds also imply that
capacities, flow values, W and logarithmic descriptors have the required
guarded polynomial magnitudes. All input and output integers have
O_a(log S) bits.

## 5. The threshold certificate

We use the following elementary fact.

**Small total violation.** Suppose every arc has integral lower and upper
bounds l_e<=U_e. If an exactly conserved real vector has total bound
violation less than one, an exactly feasible integral circulation exists.

For any vertex set X, conservation says that the difference between
the sum of its leaving lower bounds and its entering upper bounds is
at most the total violation. A positive difference would be an integer
at least one. Thus every circulation cut inequality holds. Subtracting
lower bounds and using the integral max-flow/min-cut theorem gives an
integral feasible circulation. No algorithmic lower-bounded flow call is
needed for this existential argument.

### LOW cannot occur above the threshold

At a loop state impose the current integral ordinary bounds, including
locks, and return interval [0,16beta]. Ordinary violation is at most
alpha and return violation at most alpha by (5). Their total is less
than one. Hence a feasible integral circulation for these bounds exists.

Starting from its ordinary source-to-sink flow, one can reach the
**unlocked** optimistic maximum while preserving all locks. If its value
is smaller than that maximum, the ordinary residual graph has a simple
source-to-sink augmenting path. The only extra lower bounds are on arcs
entering t. Their reverse arcs leave t and cannot lie on a simple path
whose first arrival at t is its endpoint. Thus the augmentation respects
the lower bounds. Repeating proves the assertion, also for a starting
flow containing internal cycles.

Suppose the unlocked optimistic scaled maximum is at least T. There is
therefore a comparator (F',z') satisfying every ordinary unpadded bound
and lock, with z'>=T. Its difference from the current point is a nonzero
circulation. For an ordinary lower logarithm, a negative directional
derivative has absolute value less than one because F'_e>=l_e; the
corresponding statement for an upper logarithm follows from F'_e<=U_e.
There are fewer than 2000(P+1) ordinary logarithmic terms. The return
term contributes

    W(z'-z)/(T-z) >= W = 20000(P+1)

positively. If A+ and A- denote the sums of positive and absolute negative
individual contributions, then

    A+ >= 20000(P+1),       A- < 2000(P+1).

Because lambda sums the individual absolute derivatives,

    g^T(F'-F,z'-z) / ||lambda(F'-F,z'-z)||_1
      = (A+-A-)/(A++A-) > 1/2.

The priced-step contract excludes LOW. Evaluating (3) at the comparator
is unnecessary: z'>=T is outside its logarithmic domain, but its direction
at the current point is well-defined and is all the argument uses.

### Success certifies a true flow

At success, replace every boundary's optimistic upper capacity by its
true scaled upper capacity and impose return interval [T,16beta]. An
unexpanded boundary is below its true upper capacity by Section 3,
including one just triggered by the last step. All positive source
capacities were seeded. Ordinary violation is still at most alpha.
Return violation is at most 1/4+alpha, so the **total**, including the
return arc, is less than one.

The small-violation fact gives an integral scaled circulation of value
at least T. Discard the locks and divide its flow by 16. This is a
feasible fractional unscaled flow of value at least b. The unscaled
capacities are integral, so their maximum has an integral realization
and is at least b. It is not necessary that each edge of the divided
flow itself be integral.

### Exact checks isolate the numerical interface

On LOW, compute an exact integral maximum flow in the current unlocked
optimistic graph and require its value to be below b. On success,
compute one in the true graph and require value at least b. A contrary
result suspends the branch. The proved certificates exclude such a
contradiction under the priced-step contract.

Every verified test is a decision for the full graph: optimistic
domination proves a negative threshold answer, and true-subgraph
containment proves a positive one. The numerical iterate is never
accepted as the output exchange flow. Even an incorrect numerical
LOW/success is caught by these exact checks, provided the region and
capacity construction are performed correctly. The fast time bound
still requires the priced-step contract.

## 6. Termination, operation counts, and no hidden scans

At all loop and service states, the absolute value of (3) is
O_a((P+1)log S). There are O(P+1) ordinary logarithms with arguments
between delta/10 and a guarded polynomial bound. The return gap lies
between 1/8 and a polynomial bound, and W=O(P+1).

Pad increases do not decrease the objective. Inserting an ordinary arc
or replacing a sink's bounds decreases it by at most O(log S). There
are O(P+1) such lifetime touches. Since a successful pricing step
increases it by Omega(q^2), the number of successful steps is

    O_a((P+1) q^(-2) log S).                                (7)

If the full maximum is at least b, LOW is unavailable. If it is below b,
success is unavailable. Together with the finite step bound this proves
termination at a valid threshold outcome, unless the primitive explicitly
fails or suspends.

The client's charged operations are exactly:

- Initial positive-debt enumeration and seed expansion.
- Point reads of a newly encountered bin's weight, residual and debt;
  physical scans when that bin is actually expanded; one insertion per
  represented identified arc.
- One exact return-arc read per loop, local pad/descriptor changes,
  register notifications and the boundary queue they update.
- The final static exact check and its explicit local graph construction.

New descriptors and bound changes are explicitly reanchored. The engine
settles pending flags, and the client settles resulting dirty entries
before another step. No operation examines all represented coordinates
after a path update. A boundary is not physically scanned merely because
it has been named by a represented row.

Let the common engine/notification overhead be S^rho, where
rho=O(1/a)+o_a(1). The external-operation count is at most

    O_a((P+1)q^(-2) log S) S^rho + O(P+1).

Together with the engine time and the padded exact static check, the
cost of one threshold is

    (P+B) S^(O(1/a)+o_a(1)),                                (8)

because q^(-2)=O_a(S^(200/a)). The absolute coefficient in O(1/a)
absorbs the finitely many engine overhead factors.

This sharper count also justifies the loose guards used to establish
(4). For every sufficiently large fixed a, the step count is below
S^20 and the external count below S^100 at all sufficiently large S.
The same bounds apply to a prefix through a first attempted guard
crossing, since all local batches have the bounds above. Consequently
the guards cannot first fail in that fixed-parameter range.

## 7. Two small regions recover the exact full flow and cut

Use verified threshold tests to binary-search the full unscaled maximum
v, where 0<=v<=beta. Retain a true success region at threshold v when
v>0. Its true maximum is exactly v: it supplies v and embeds in the
full graph. If v<beta, retain an unlocked optimistic failure region at
threshold v+1. Its maximum is exactly v, since it is integral, below
v+1, and at least the full maximum v. A constant number of extra tests
retrieves these regions if the binary search did not retain them.

Assume first that v<beta. Let Q be a minimum source side in the failure
region. No boundary can belong to Q: its outgoing sink arc alone has
capacity beta+1>v. Hence every bin of Q is expanded. All full arcs
leaving such a bin are represented with their true capacities. Every
represented row has all its outgoing row-to-bin arcs, and every positive
source arc is represented because all deficits are seeds. Therefore the
same set Q is a cut of capacity v in the full graph.

Take the union of the available regions, deduplicating **by original
arc identifier**, and use true capacities throughout. Its maximum is v:
the success region supplies v when v>0, and the full cut Q bounds it
above; when v=0 only the failure region is needed. If v=beta, use the
success region alone and the total source capacity as the upper bound.
Compute an exact integral maximum flow F on this union and extend it by
zero to unrepresented full arcs. It is an exact full maximum flow.

When v<beta, equality with the capacity of Q forces every full outgoing
cut arc to be saturated and every incoming cut arc to carry zero flow.
Thus no residual arc leaves Q. All full positive-capacity forward arcs
needed inside Q are represented: bins in Q are expanded and rows in Q
have all outgoing incidences. Every needed reverse residual arc comes
from positive flow on a represented union arc. Residual reachability
computed locally is therefore exactly the full residual source
reachability. Let R0 be its bin part.

The argument is valid for any exact union maximum flow, including one
with cycles, and with separate parallel incidence arcs. It does not
assume that the two region flows agree or attempt to splice them.

## 8. Exact support, peel weight, and ledger updates

The union has O(P+1)=O(P) arcs and vertices. Its explicit flow supports
all allocation changes

    x'_e = x_e - F_(d,r)(e) + F_(r,d)(e).

Absent union arcs have zero flow. If an incidence's reverse-direction
arc alone was represented at a boundary, its parent x_e can simply be
read by point access when forming the change. There are still only
O(P) such entries. Row conservation keeps every row sum L; nonnegativity
follows from F_(d,r)(e)<=x_e. Column residual changes are obtained from
the represented source and sink arc flows.

If v<beta, R0 lies within the expanded bins of the failure region, so
its total weight is O(P). There is also a stronger purely algebraic
bound. The exact exchange residual argument gives

    L h(R0) < c w(R0),

where h(X)=|X|-|{r:N(r) is contained in X}|. For the original parent,
captives imply y(R0)<=Lh(R0). Combining this with (1),

    (c+1)w(R0)-p(R0) <= y(R0) <= Lh(R0) < cw(R0),

so w(R0)<p(R0)<=P. This bound does not rely on numerical flow values.

For completeness, the failed-floor identity follows directly from the
exact union maximum flow. Each row receives at most its total incoming
capacity L, so every outgoing row-to-bin arc of capacity L+1 is
unsaturated. The combined bin-to-row residual on an incidence is x'_e.
If a row allocates positively into a reachable bin, that row and all its
neighbors are reachable. Thus the rows allocating into R0 are precisely
its captives, giving y'(R0)=Lh(R0). Every reachable spare sink arc is
saturated, and some reachable deficit source arc is unsaturated. Summing
y'_d=y_d+F_(s,d)-F_(d,t) gives the strict inequality above.

Outside R0 every deficit is saturated, so y'>=cw. No noncaptive row
allocates positively into R0. Removing R0 and its assigned rows therefore
leaves a zero-debt floor-c ledger; exterior load freed by removed rows
can only improve its residuals. With the frozen injection's point and
inverse interface, listing those assigned rows and their at most three
incidences costs O(w(R0)) times polylogarithmic overhead. Preserving
deletions on other ledgers are separate local transactions.

No unexpanded high-weight boundary and no unchanged parent allocation
needs a physical scan. Final exact changes can be applied to a child
copy, then normalized, while the parent version used by the calculation
remains intact.

## 9. Conditional local projection theorem

Under the input and arithmetic premises of Section 1 and its two
imported numerical interfaces, exact exchange projection uses
O(log S) priced-step instances and total time

    (P+B) S^(O(1/a)+o_a(1)).

It returns an exact full maximum exchange flow through O(P) changed
incidences and, when v<beta, the complete residual reachable bin set
of weight less than P. Alternatively it reports an imported explicit
failure or suspension. In the eventual fixed-parameter range, the
client's size, precision and operation guards are adequate.

The proof establishes the local projection client and its full-cut
recovery. Remaining fast-time dependencies are the priced-step
implementation and the deterministic exact static flow primitive,
including their finite-word costs. The exact threshold checks provide
additional protection for correctness, but do not remove those time
dependencies.
