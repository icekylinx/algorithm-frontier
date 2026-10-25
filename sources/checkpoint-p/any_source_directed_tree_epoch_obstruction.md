# A reachable obstruction for a directed any-source tree epoch

**25 October 2026. New construction; root review and independent checks completed.**

The later-epoch checks are in
**tight_dag_and_directed_epoch_independent_audit.md**. The explicit
preparation and its terminal-selection qualification are part of
the root review; no claim is made about every preparation policy.

This note gives a genuine general-matching ledger in which an exact
conservative source SPT has linearly many current records, but exhausting
all of its directed ancestor-to-descendant threshold paths earns only
polylogarithmic numerical and price credit. The fixed semantic certificate
remains far above LOW, and an explicit strong direction survives outside
that directed path family.

The obstruction is to the **directed** forest interface in
`any_source_fixed_tree_matching_interface.md`. Reversing one tight receiving
edge gives an immediate escape. In particular, this is not an obstruction
to a compatible bidirected-forest interface, to local cut/link repairs, or
to an improved matching algorithm. It does not prove that a full refresh
is necessary.

Preparation below uses legal structural priorities and exact conservative
source paths to explicitly selected terminal bins. It does not assume that
an arbitrary improving allocation is automatically returned by an exact
source oracle. A particular algorithm that fixes a different global
terminal-selection policy is not asserted to follow this preparation.

## 1. Physical graph, current matching and record counts

Fix an integer \(q\) tending to infinity. One copy of the construction
contains an odd cycle on \(2q+1\) vertices. Initially match \(q\) disjoint
cycle edges, leaving one cycle vertex free. Eventually this cycle will be
contracted to one free factor-critical bin \(W\), of weight

\[
                         w_W=q+1.
\]

Attach \(q\) distinct external rows \(r_i\) at distinct physical cycle
ports. Row \(r_i\) also has an assigned singleton leaf \(d_i\) and a free
singleton leaf \(w_i\). Its three physical edges are therefore

\[
                        r_iW,\quad r_id_i,\quad r_iw_i.
\]

The notation \(r_iW\) denotes one physical edge to its specified cycle
port, not an edge to a new physical supervertex.

There are four additional matched row/child pairs

\[
                         (s,b),\quad(u,g),\quad(r,a),\quad(t,c),
\]

and two additional free singleton bins \(f,h\). Their physical incidences
are

\[
\begin{array}{c|l}
\text{row}&\text{neighbouring bins or future bins}\\\hline
s&f,b\\
u&h,g\\
r&W,a,b\\
t&g,c,b.
\end{array}                                                     \tag{O1}
\]

The port of \(rW\) is distinct from the \(q\) branch ports. There are
enough cycle vertices to choose all of these ports with at most one
external incidence at each physical vertex. Every physical vertex has
degree at most three. The bin \(b\) has degree three, through \(s,r,t\).

Use two disjoint copies of this graph, with distinguished contacts
\(a,a'\), and add a matched remainder pair \(p,q_*\) with physical
edges

\[
                         ap,\quad pq_*,\quad q_*a'.             \tag{O2}
\]

These are the only remaining paired-remainder contacts after preparation.
The physical graph is connected and nonbipartite because of its odd cycles.

One copy has \(5q+11\) physical vertices: \(2q+1\) cycle vertices,
\(q+4\) external rows, and \(2q+6\) external singleton bins. Thus the
whole graph has

\[
                         N=10q+24.                              \tag{O3}
\]

After contraction, each copy still has \(q+4\) rows and \(2q+7\) bins,
including \(W\). Its ordinary directed allocation graph has
\(\Theta(q)=\Theta(N)\) current records. The argument is therefore not
based merely on the physical volume hidden inside one contracted bin.

The current matching has all \(q\) internal cycle matches and all
\(q+4\) row/child matches in each copy, plus \(pq_*\). It has size
\(4q+9\). Exposing the physical port of \(rW\) as the free base of the
factor-critical cycle gives the augmenting path

\[
                         W,r,a,p,q_*,a',r',W'.                   \tag{O4}
\]

Internal cycle matchings can expose these prescribed ports. Conversely,
any matching uses at most \(q\) internal edges in each odd cycle, at
most one remaining edge per external row, and at most two further edges
incident to \(p,q_*\). Hence its size is at most \(4q+10\). The true
matching gap is exactly one.

Take the legitimate phase target \(K=1\), and

\[
                       L=10000CN,
\]

where \(C\) is the usual logarithmic phase parameter. We restrict to
sufficiently large members of the family, so \(C\ge128\). All small
padding is on the guarded dyadic grid and is negligible compared with the
strict constant margins below.

## 2. Creating the odd bin is a legal operation

Write the cycle as alternating matched pairs
\((z_1,v_1),\ldots,(z_q,v_q)\), with free vertex \(v_0\), path edges
\(v_{i-1}z_i,z_iv_i\), and closing edge \(v_qv_0\).

Choose the central port of \(rW\) to be \(z_1\). Start cycle growth by
expanding \((z_1,v_1)\) from \(v_0\). Consequently \(z_1\) is an actual
row throughout the subsequent cycle growth. The still paired vertex \(r\)
does not acquire an eligible bin contact there before the cycle contracts.
Its other current possible parent, \(b\), has slack approximately one.
This prevents the contact \(a\) from being born prematurely.

First expand the external pairs \((r_i,d_i)\) from their free bins
\(w_i\). This is a legal choice among eligible expansions. It puts
\(C+1\) units on \(r_iw_i\), \(L-C-1\) on \(r_id_i\), and gives
\(d_i\) slack one. The cycle-port incidence is born with tiny padding
when its port first becomes a bin, or when that port is later swallowed
as a row by the contraction.

Grow the two exposed arms of the odd cycle. Whenever an exposed frontier
is eligible, expand the next matched pair. When neither frontier is
eligible, query the original free-bin endpoint \(v_0\) in the exact
conservative source graph. An unfinished frontier has slack at most
\(5C\) by the no-eligible-contact guarantee. Its path to \(v_0\) uses
large assigned donors and gives a source offer at least
\(.149/C\), for the declared \(L\) and sufficiently large scale.
Every exact winning source then has pre-step slack below \(5.04C\),
and post-step slack below \(6C\). External leaves have no other
remainder contacts, so raising them is harmless.

Here is a direct check of the large-donor induction used in that bound.
Each old nonfree cycle bin has slack at most \(6C\), and each attached
external row sends at most \(6C\) plus tiny padding to its current cycle
port. Its singleton residual contributes a further \(C\). Telescoping
the column equations along an arm of at most \(q\) rows therefore
bounds every complementary parent allocation by
\(20(q+1)C\), with room for endpoints and all padding. Its assigned
donor is at least \(L-20(q+1)C\ge .99L\). The same summed equations
give that lower bound for the free-bin slack. A path has at most \(q\)
such donors, so (A1) of
the independent interface audit bounds its conservative price by
\(q/(2(.99L))+q/H\), much less than \(.001/C\). This closes the offer
and slack induction. Finite-grid rounding is below the displayed margins.

If no next expansion ever became eligible, the unfinished frontier would
keep supplying a passing constant-ratio answer. Constant objective
progress and the bounded positive-slack objective rule out infinitely many
such numerical steps. Thus all cycle pairs are eventually expanded. This
preparation is finite; no fast preparation bound is claimed.

The final physical collision edge, at which the two growing arms meet,
joins two bins. It need not be the initially designated edge
\(v_qv_0\). The remaining row-labelled path formed by the two arms has
these collision bins as its endpoints. The entire cycle bin set
has \(q+1\) bins and \(q\) captive cycle rows, so its Hall surplus is
one. A proper set containing both collision endpoints has at least two
components in the remaining row-labelled cycle path and hence surplus at
least two. Adding external star leaves cannot reduce this surplus: each
external row requires both of its outside leaves to become captive and
adds two bins for only one row. Therefore the inclusion-minimal tight set
containing the collision edge is exactly the cycle bin set. The two
endpoints cannot both be freed, and the legal operation is its
factor-critical contraction.

After contraction the top capacity of \(W\) is

\[
            L-C(q+1),\qquad
 s_W=L-C(q+1)-\sum_i x_{r_iW}-x_{rW},                 \tag{O5}
\]

up to the explicitly tiny positivity debt. In particular, \(s_W\) is
not set equal to the slack of an ordinary singleton free bin. All external
loads in (O5) are \(O(qC)\), so \(s_W\ge .99L\) throughout the
preparation after increasing the harmless fixed constants if necessary.

The new contact from \(W\) to \(r\) is eligible. Expand \((r,a)\) from
\(W\), giving \(a\) slack one and assigning \(C+1\) to \(rW\).
The extra incidence \(rb\) receives only tiny padding. The pairs
\((s,b)\) and \((u,g)\) were already expanded from \(f,h\); their
singleton children still have slack approximately one. The pair \((t,c)\)
is still unexpanded because both of its bin contacts \(b,g\) are small.

## 3. Exact-source preparation of the star and gate

The following three stages operate independently in each copy.

### 3.1 Raise all star leaves to at least eight

Repeatedly query terminal \(W\) in the exact conservative source graph
until every \(d_i\) and \(a\) has slack at least eight. Bin \(a\) was
just born with slack one in the central expansion after contraction;
unlike some older branch leaves, it was not present during cycle pricing.
A leaf below
eight has a direct one-row path to \(W\), with its assigned donor at
least \(.99L\); its offer is at least \(3/32-O(1/L)\).

Every competitive source is a leaf \(d_i\) or \(a\), and its path is
exactly that one-row path. The free bins have offer \(O(1/L)\). Bin
\(b\) can reach \(W\) only through its tiny donor \(b\to r\), whose
cost is prohibitive; the \(g,h\) component is still separate. A winning
leaf of slack near the threshold remains below \(8.1\) after its step.
Leaves that were raised beyond eight during cycle preparation do not need
to be raised again.

This process terminates by the same constant-progress argument. A leaf
never serves as a terminal during cycle or star preparation, and its
\(w_i\) incidence stays fixed at \(C+1\). Thus every branch row now has

\[
                       x_{r_iW}\ge7-o(1),\qquad s_{d_i}\ge8.
                                                                  \tag{O6}
\]

The contact \(a\) remains below \(3C\), and no paired-remainder
expansion is forced.

### 3.2 Raise b by exact queries to f

Query terminal \(f\) repeatedly until \(b\)'s slack first reaches
\(2C\). While it is below that threshold, its direct path
\(b\to s\to f\) has large donor and terminal values and offer at least
\(.37/C\). Every exact winning source therefore has pre-step slack below
\(2.03C\), and post-step slack below \(2.1C\). In particular, neither
contact \(a\) nor contact \(b\) becomes eligible. The only possible
winning sources are \(b,a\), or some of the \(d_i\). Every donor on
the direct \(b\)-path remains large because total moved mass is
\(O(qC)\ll L\).

At the first crossing of \(2C\), the last path starts at \(b\). Just
before that step, \(s_b>1.99C\). Compare this winning exact path with
the alternative source path

\[
                        a\to r\to b\to s\to f.
\]

The additional donor \(a\to r\) has allocation at least
\(L-O(C)\), hence conservative cost \(O(H/L)\). Exact optimality
therefore gives

\[
                 \sigma_a\le\sigma_b+O(H/L),
                 \qquad s_a\ge1.9C.                              \tag{O7}
\]

Every increase of \(a\) during this stage uses the one-row transfer
\(a\to r\to b\), followed by the large \(b\)-donor. Since \(a\)
started this stage below \(8.1\), (O7) implies that the gate incidence
\(rb\) acquires at least \(C\) units for large enough \(C\). Any
branch-leaf source also increases \(rb\), while decreasing \(rW\).
The initial \(rW\) allocation and the total increase of \(a\) bound
the gate from above. At the end of this stage,

\[
 \begin{gathered}
 C\le x_{rb}\le4C,\qquad 1.9C\le s_a\le2.1C,
 \\ 2C\le s_b\le2.01C,
 \qquad s_W,\ s_{w_i},\ s_f\ge .99L.
 \end{gathered}                                                   \tag{O8}
\]

All branch incidences into \(W\) only increase during this stage, so
(O6) is preserved. Existing leaves with slack above \(2.1C\) need not
participate; all leaves still have slack at least eight.

### 3.3 Introduce a fresh dominant source from a separate component

The \(u,g,h\) allocation component is still separate. Query terminal
\(h\) and increase \(g\) until its contact to \(t\) becomes eligible.
Every such exact path starts at \(g\). Its actual slack at the first
eligibility is between the standard contact bounds \(3C\) and
\(5C+o(C)\). Expand \((t,c)\) from \(g\), with

\[
 x_{tg}=C+1,\qquad x_{tb}=\epsilon,
 \qquad x_{tc}=L-C-1-\epsilon.                         \tag{O9}
\]

The new bin \(c\) has slack \(1+\epsilon\); \(g\) has slack between
\(2C-1\) and \(4.1C\). Bin \(b\) changes only by the tiny padding.
The two copies can be prepared separately before beginning the tested
epoch. The remaining pair (O2) does not join their ordinary allocation
components.

## 4. Lower ledgers and the settled matching state

Every displayed top update preserves exact row sums and bin equations.
All coordinates are positive, polynomially bounded, and on the fixed grid.
The only top debt needed is the existing negligible positivity-service
debt. No contact has slack at least \(3C\) when the tested epoch begins:
the only remainder contacts are \(a,a'\), each of slack at most
\(2.1C\). There is no physical edge between two distinct current bins.

The current allocation graph also admits explicit debt-free integral
ledgers at every floor \(c_0\le C\). Give each branch row \(L-c_0\)
to \(d_i\), \(c_0\) to \(w_i\), and zero to \(W\). Give row \(r\)
values \(L-c_0\) at \(a\), \(c_0\) at \(W\), and zero at \(b\).
Give \(s\) values \(L-c_0,c_0\) at \(b,f\); give \(t\) values
\(L-c_0,c_0,0\) at \(c,g,b\); and give \(u\) values
\(L-2c_0,2c_0\) at \(g,h\). Each singleton's residual is at least
\(c_0\), while the residual of \(W\) is \(L-c_0\), which exceeds
\(c_0(q+1)\). The cycle preparation has the analogous arm ledgers
used in `root_only_sp_tree_epoch_counterexample.md`.

This checks the actual floor constraints. It does not impose a nonexistent
coordinatewise equality between different integral floors. The operations
are ordinary ledger expansions, exact pricing transfers, and the minimal
tight contraction; no artificial feasibility repair is being used to
create the state.

## 5. A large exact conservative SPT with one source child

Start the operative interface with its persistent registers. They obey
\(x/2<\ell<x\), so every donor price divided by \(H\) is at most
\(1/(2x)+1/H\). From \(c\), the routes to all bins in its copy use
at most one large donor, the gate donor of allocation at least \(C\),
and one branch donor of allocation at least \(7-o(1)\). Other routes
through \(s\) or \(u\) use only large donors.

Thus the total conservative path price is below \(.09H\), and the
offer from \(c\) is greater than \(.65H\) everywhere, for large enough
\(C,H\). Every other direct source offer is at most
\((3/32+o(1))H\), because all other small bins have slack at least
eight. The singleton bins \(a,b,g\) have the still larger slacks in
(O8)--(O9).

Consequently \(c\) is the unique source child of the exact SPT in its
ordinary component. The underlying allocation support is a tree, so all
ordinary paths from \(c\) have the following orientation:

\[
 \begin{array}{l}
 c\to t\to b\to r\to W\to r_i\to\{d_i,w_i\},\\
 b\to s\to f,\qquad t\to g\to u\to h,
 \qquad r\to a.
 \end{array}                                                     \tag{O10}
\]

Every \(d_i\), every \(w_i\), and \(a,f,h\) is a leaf of this
directed tree. There are linearly many of them. Its receiving arcs are
tight in the fixed old labels, and the old potential satisfies

\[
                          \pi_v\ge .65                           \tag{O11}
\]

at every ordinary bin. Both copies give such a tree in the forest.

## 6. Any directed-tree choice earns only polylogarithmic credit

Freeze the forest (O10), and allow **all** of its ancestor-bin to
descendant-bin passing paths. This is the full original any-source
interface, not a restriction to \(c\).

Only the bins \(c,b,g\) can be starts of accepted paths in one copy.
All other small bins are leaves. To see that \(W\) cannot start one,
use induction. Until its first putative start, every numerical transfer
into its star from above crosses the gate donor \(b\to r\). That donor
only decreases and starts with at most \(4C\) units. Thus each large
star bin has slack at least \(.99L-4C>.98L\). A descendant free leaf
has slack at most \(L\), so the reciprocal ratio is below \(5/3\),
already excluding the threshold. A descendant \(d_i\) has small slack,
which gives negative gain from \(W\). No first accepted start at \(W\)
can therefore occur.

Every other slack has only nonpositive changes. Since each of the three
possible positive-slack coordinates is at most \(L+o(1)\), the total
objective gain in one copy is at most \(O(\log L)\). The operative
step rule gives a fixed positive gain per accepted step. Hence **every**
sequence of directed-tree choices has only

\[
                           O(\log L)                              \tag{O12}
\]

accepted steps before TREE-EMPTY. The same bound holds for both copies.

No uncharged guard event is needed. Initially the minimum slack is
approximately one; acceptance and the normalized step keep the global
minimum slack nondecreasing. If a donor lies on an accepted path, then
\(\bar c/H\ge1/(4x)\) and threshold acceptance force
\(x>s_{\rm start}/3\). Its small decrease therefore leaves it bounded
away from the tiny positivity guard. All upper magnitudes remain bounded
by row sums. The contacts \(a,a'\) only lose slack, so no structural
action becomes eligible.

Each path in (O10) has constant ordinary length. Only \(O(\log L)\)
allocation records are changed at all. Their motion directions are fixed
throughout the epoch, and their magnitudes stay in the fixed polynomial
range. Total logarithmic allocation variation and the number of register
notifications are therefore at most

\[
                          O(\log L\log S),                         \tag{O13}
\]

which is polylogarithmic. There is no linear price credit hidden in a long
path application.

## 7. Semantic excess and an actual tree-external comparison survive

Every free branch leaf still has slack at least \(.98L\). By (O11),
the fixed certificate has

\[
 E\ge q\bigl(.65(.98L)-5/4\bigr)=\Omega(qL),                       \tag{O14}
\]

in each copy. This is far above the operative five-N LOW threshold.

The actual one-row path

\[
                               a\to r\to W                         \tag{O15}
\]

survives. Its donor allocation is \(L-O(C)\), and \(W\) has slack
at least \(.98L\). Its starting slack never exceeds \(2.1C\).
Moving \(L/10\) units on (O15) gives a nonnegative feasible comparison
with

\[
 P\ge\frac{L}{21C}>12N,\qquad Q_s<1,\qquad Q_x<1.                 \tag{O16}
\]

Thus this is not merely an isolated positive direction with negligible
normalized mass. It has the matching comparison's required absolute
margin, and the physical graph independently has the actual gap one.

Path (O15) is absent from the directed family only because \(a\) is a
child of row \(r\): its first donor reverses the old receiving tree
arc \(r\to a\). All following receiving arcs are old-label tight.

## 8. The repair boundary is explicit

Cut the old tree edge \(b\to r\), and reroot that component at \(a\).
Only the edge \(ra\) changes orientation. The resulting directed
component begins \(a\to r\to W\), with the same old potential feasible
on every ordinary arc. The reversed edge has equal old labels at its
endpoints, and \(r\to W\) remains a tight receiving arc. A new direct
source arc at \(a\) is already feasible; it need not be tight.

Equivalently, one can permit a path to start by reversing its parent's
tight receiving edge and then continue downward. A compatible bidirected
underlying-forest search includes (O15) without needing a global SPT
refresh. For example, row \(r\) can expose the local starting offer
\(\sigma_a-\bar c_{a\to r}\).

Therefore the established conclusion is only that exhausted **directed**
any-source epochs do not universally earn linear objective or price
credit, even on reachable top matching ledgers with exact-source
preparation. The construction does not obstruct the stronger compatible
forest interface, and it does not charge or require a global rebuild.
