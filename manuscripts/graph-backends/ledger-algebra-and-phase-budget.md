# Ledger algebra, exact exchange and the structural phase budget

**Self-contained algebra for the row/bin matching state.** This note
derives the margin and debt identities used in the current construction.
The state organization and projection network originate in OAI Sections
3--4. The separate fast implementation of a LOCAL exact projection and
the priced logarithmic client remain named dependencies; an exact-flow
existence proof alone does not establish their running time.

Source framework:

<https://github.com/openai/math/tree/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026>.

## 1. Ledgers and bottom surplus

Bins are disjoint odd physical blocks of size 2w_d-1 with positive
integer weights. Rows are physical singleton vertices with at most
three bin incidences and a valid injection into incident bins. The
remaining vertices are paired or are unmatched blockers. For a bin
set X define A(X)={r:N(r) is contained in X} and h(X)=|X|-|A(X)|.

Each row allocates L units among its physical bin incidences. In a
ledger of floor c, write

    y_d = L-load(d),     p_d>=0,     y_d+p_d>=c w_d.

The allocations are nonnegative. Below the top numerical level they
are integral. The bottom settled floor is c=1 and its debt is zero.
For any nonempty bin set X, every captive row allocates all L units
inside X. Therefore

    L h(X) >= y(X) >= w(X)>0.

In particular h(X)>=1, every bin weight is at most L, and every tight
set has weight at most L. These facts use column loads and row sums,
not individual allocation coordinates. Any nonnegative transportation
cycle pivot preserving those margins preserves all these conclusions.

## 2. Contraction and expansion arithmetic

Contract a tight set X, so it has |X|-1 captive rows. Removing those
rows deletes exactly L(|X|-1) load from X. The surviving load on the
new bin is load(X)-L(|X|-1), and its residual is consequently

    L-[load(X)-L(|X|-1)] = L|X|-load(X) = y(X).

The new weight is w(X), its debt is p(X), and hence its floor inequality
is the sum of the old inequalities. The top slack aggregates in the
same way. Existing exterior incidence values are preserved; newly
created integral incidences start at zero.

On an expansion, a paired physical vertex becomes a row and its mate
becomes a singleton bin. In an integral ledger of floor c, put all L
units of the new row on that child's assigned edge and give the child
debt c. Its residual is zero, so its floor holds with equality. The
other new incidences have value zero. Only O(1) records are new, apart
from already charged changes in physical edge classification.

At the top, the source uses C+1 units on the trigger-parent incidence
and L-C-1 on the child incidence. An eligible parent has actual slack
at least 3C, leaving it positive; the new child has slack one and no
initial debt. The tiny positive padding of any other top incidence
is part of the separately specified positivity service. That service
adds total debt below epsilon_0=S^(-800) on a guarded phase prefix.

## 3. Preserving deletion and its exact debt identity

Let R be bins to be erased, using one fixed current injection. Remove
every row assigned into R. Let f be the number of free bins in R;
exactly |R|-f rows are removed.

For each surviving row, redirect all its allocation into R to its
assigned exterior bin, adding the same amount of debt there. The row
sum and the exterior floor inequality are preserved: added load reduces
y by exactly the debt increase. Deleting removed rows only increases
the exterior residuals.

Let O be total redirected mass and I the total allocation from removed
rows into exterior bins. The old load into R was
L(|R|-f)-I+O, so

    y(R)=Lf+I-O,
    O=I+Lf-y(R).

Every captive row of R is among the removed rows. Only
(|R|-f)-|A(R)|=h(R)-f other removed rows can contribute to I. Thus

    I <= L(h(R)-f).

Deleting old debt p(R) and adding O gives net total-debt change

    Delta p_total = O-p(R) <= Lh(R)-c w(R).

At a gain, R consists of the two bins just made free, so h(R)<=2 and
the debt increase is at most 2L. The terminal gain of a phase need
not repair its ledgers. A peel moves each free exposure to the blocker
list; a gain matches the two free exposures along its joining edge.
All other structural operations preserve matching cardinality.

## 4. Exact exchange to a weaker floor

Start from an integral ledger and seek floor c with zero debt. Put

    b_d=max{cw_d-y_d,0},
    u_d=max{y_d-cw_d,0},
    beta=sum_d b_d.

Create source-to-bin arcs of capacity b_d, bin-to-sink arcs of capacity
u_d, and for every incidence e=(r,d) two separate arcs:

    d -> r with capacity x_e,
    r -> d with capacity L+1.

All lower bounds are zero. Let F be an exact integral maximum flow.
Define the new allocation

    x'_e = x_e-F_(d,r)(e)+F_(r,d)(e).

It is nonnegative because F_(d,r)(e)<=x_e. At a row the total incoming
capacity is L; conservation preserves its allocation sum L and bounds
its total outgoing exchange flow by L. No row-to-bin arc of capacity
L+1 is saturated. At a bin,

    y'_d = y_d+F_(source,d)-F_(d,sink).

If the maximum value is beta, all deficits are filled and spares lose
at most u_d. Thus y'>=cw everywhere, producing the desired zero-debt
ledger.

## 5. Failed exchange yields a paid peel

Otherwise take ALL bins R reachable from the source in the residual
network of F. For a physical incidence, the combined residual capacity
from its bin to its row is exactly x'_e: it is the unused forward
capacity plus reverse flow on the companion arc. Hence any row with
positive allocation into R is reachable. Every neighbor of a reachable
row is reachable, since its row-to-bin arcs are unsaturated.

The rows allocating into R are exactly its captives, each contributing
L. Consequently y'(R)=Lh(R). Every reachable spare-to-sink arc is
saturated; some reachable source deficit remains unsaturated. Summing
the bin identity of Section 4 gives

    Lh(R)=y'(R)<c w(R).

Outside R all deficit source arcs are saturated, so y'>=cw there.
A surviving row has no positive x' into R, or it would be captive and
removed. Erase bins R and their assigned rows. Restricting x' to the
remaining graph therefore gives a valid zero-debt floor-c ledger.

Any preserved coarser ledger has floor c_old>=c+1. Its separate
preserving deletion obeys

    Delta p_total <= Lh(R)-c_old w(R) < -w(R).

Thus each such ledger loses at least w(R) net debt. Also f<=h(R),
because every captive row is assigned into R. If c<=C, the new blocker
count satisfies

    f <= h(R) < C w(R)/L.

When the parent itself satisfies y+p>=(c+1)w, each positive deficit
b_d is at most p_d. Therefore beta<=P, where P=sum p_d. This is the
starting parameter for the separate local-projection algorithm; it
does not on its own prove that only O(P) graph records need be explored.

## 6. Phase debt and structural counts

Fix 1<=K<=N, C=a+1, and

    L=ceil(10000 C N/K),
    g_*=max{1,floor(K/(100 C))}.

Before the terminal g_*-th gain, at most g_*-1 gains repair their
ledgers. Top expansions create no ordinary top debt, contractions
preserve its sum, priced circulations leave debt unchanged, and the
positivity service adds less than epsilon_0. Each repaired gain adds
at most 2L, while each peel consumes at least its weight from the top.
Nonnegativity of remaining debt gives

    sum_(peels R) w(R) <= 2L(g_*-1)+epsilon_0.

Summing the strict blocker inequality and using integrality yields at
most 2C(g_*-1) blockers, since C epsilon_0/L<1 at the guarded sizes.
In particular g_*=1 permits no positive-weight peel before its gain.

Each erased bin has 2w_d-1 physical vertices, and at most one removed
assigned row per bin accompanies it. Materialized volume is at most
2w(R). A gain erases two bins, each of weight at most L. Thus total
volume returned to the paired remainder is O(L g_*), including the
terminal gain. Each expansion consumes one matched pair from that
remainder, whose initial population is at most N. Expansions number
O(N+L g_*).

There are initially at most N bins, and each expansion adds one. A
contraction of arity k>=2 reduces the count by k-1; gains and peels
only reduce it further. Therefore the sum of contraction arities is
O(N+L g_*). Charging one tick per expansion or contraction and L
per repaired gain gives the same order for the tick total.

Finally L g_*=O_a(N). If K<100C, g_*=1 and L<=10000CN+1.
Otherwise Lg_*<=(10000CN/K+1)K/(100C)=O(N). All structural counts,
total peeled weight and materialized volume are consequently O_a(N).

## 7. Physical incidence work by retaining the largest bin

At each contraction retain the live identifier and member list of a
largest child bin. Move the members of the smaller child bins into it,
and add the swallowed singleton rows. When a physical vertex moves
from a smaller child, the new bin has at least twice that child's
physical size. During a stay in the bin system, its bin size can only
increase by contractions until the vertex is erased to the paired
remainder or becomes a blocker. It therefore moves at most O(log N)
times in that stay.

Count a new stay when an initial unmatched vertex forms a singleton
bin, or when an expansion moves a matched pair out of the remainder.
A row's later absorption into a contracted bin adds only its constant
degree incidences. Section 6 bounds initial population, expansion
count and erased physical volume by O_a(N). Thus the total number of
charged stays and row absorptions is O_a(N), and all member moves cost
O_a(N log N).

The original physical graph is subcubic. Scanning the at-most-three
physical incidences of a moved, absorbed or erased vertex therefore
accounts for all changed bin labels, new row-bin incidences, vanished
internal contacts and updated distinct-bin/remainder contact records.
Maintain these records in dictionaries and linked lists. A change in
one bin's cached slack updates its eligibility flag without scanning
the bin's entire contact list. This adds only logarithmic record costs.

The largest bin's immutable OLD witness is retained as a child-record
pointer when creating a new contraction record. Reusing its live bin
identifier does not overwrite that saved child record or the historical
incidence data of a persistent carrier version. Only the live partition
map uses the retained identifier. These two notions of identity must
remain distinct.

Applying the same structural incidence batch to a fixed number a of
integral levels multiplies this bound only by a parameter-dependent
constant. Fresh projection support is charged separately to its local
flow-size bound. Canonical assignment switches do not change physical
partition labels or edge classifications and do not incur a hidden
global incidence traversal.

## 8. Relation to persistent normalization and the fast theorem

Every integral carrier pivot preserves each row sum and each column
load, and leaves debts and weights untouched. It preserves every
identity and inequality used above. Apply a complete structural or
projection batch before pivoting. Use the same frozen injection and
overlay for all assigned-row deletion decisions in an event.

The exact factor-critical witnesses and materialization cost are in
[factor-critical-contractions.md](factor-critical-contractions.md). Sparse persistent updates are in
[persistent-integral-ledger-carrier.md](persistent-integral-ledger-carrier.md). The phase still needs the
fast local projection, valid numerical pricing/progress, guarded-size
analysis and physical bookkeeping. Their time charges are stated in
[Deterministic Exact General Matching through Persistent Integral Carriers and Normalized Routing](../../problems/general-matching/proof.md); this algebraic note does
not substitute an uncharged global flow for those local routines.
