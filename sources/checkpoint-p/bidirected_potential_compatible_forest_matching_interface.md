# Bidirectional searches in a potential-compatible matching forest

**Research extension, 25 October 2026. Root and independent mathematical
and data-structure reviews completed.**

This note strengthens the local forest interface in
potential_compatible_dynamic_forest_matching_interface.md.
One physical allocation incidence still appears at most once in
the underlying undirected forest. On that edge, however, its donor
direction is always available, and its receiving direction is
available whenever it is tight for the fixed feasible potential.

Thus a forest edge may be used in either direction on different
accepted paths without being cut or relinked. Search still ranges
over simple paths of the underlying forest. The price and lazy
update structures below retain constant-size cluster state.

This is a local data-structure result. It supplies neither an
ambient replacement-edge search nor a bound on potential
refreshes. The exact general-matching exponent remains four fifths.

## 1. Imported numerical and identity contract

Use the fixed ledger interval, bounded integer labels D and A,
common dyadic grid, guard bounds, and persistent registers of
the preceding forest interface. In particular,

\[
 \ell_e<x_e<2\ell_e,\qquad
 \bar c_e=\left\lceil H/(4\ell_e)\right\rceil,\qquad
 \sigma_d=\left\lfloor3H/(4s_d)\right\rfloor,\quad
 \tau_d=\left\lceil5H/(4s_d)\right\rceil.
 \tag{1}
\]

All labels and arithmetic have O(log S) bits. The full threshold
graph remains feasible for the fixed D:

\[
 D(d)\le D(r)\le D(d)+\bar c_e,\qquad
 D(d)\le A-\sigma_d .
 \tag{2}
\]

The ordinary maintained object is now an undirected forest of
physical incidence IDs. At most one forest edge owns any live
allocation coordinate. The endpoints are its actual row and bin;
logical copies cannot introduce a second owner.

For a forest incidence e=(r,d), its available scored directions
are

\[
 \begin{array}{c|c|c}
 \text{direction}&\text{availability}&\text{score}\\
 d\longrightarrow r&\text{always}&-\bar c_e\\
 r\longrightarrow d&D(r)=D(d)&0 .
 \end{array}
 \tag{3}
\]

The receiver-availability flag is fixed during this D interval.
A physical edge with two available directions is still just
one underlying edge and one allocation coordinate.

An allowed path follows available directions on the unique
underlying simple path between its endpoints. It does not traverse
an edge twice. The existence of two opposite available arcs on
one physical edge does not authorize a two-edge walk back and
forth.

Ordinary link/cut operations only modify the physical forest.
A link must connect distinct components and use an unselected
coordinate ID. Equation (3) then supplies its two availability
flags automatically. No orientation choice or role-change
operation is required.

## 2. The directed path DP needs no new asymptotic state

Use the two pendant endpoint-price leaves per bin from the
preceding note. Its source terminal has its one outgoing score
sigma_d, and its target terminal has its one incoming score
-tau_d. Ordinary leaf clusters use the directional scores (3).

For every at-most-two-boundary cluster C, retain the same entries:

* W_C(u,v), the score of the unique u-to-v path if every
  direction is available, and minus infinity otherwise;
* I_C(v), the best source-terminal-to-boundary path score;
* O_C(v), the best boundary-to-target-terminal path score;
* F_C, the best source-terminal-to-target-terminal path score.

Keep zero-edge boundary paths and the same constant-size
terminal witness metadata. In a base ordinary cluster, both
W_C(d,r) and W_C(r,d) can now be finite. This is the only
change to the scored base initialization.

All join formulas in Section 4 of the preceding note remain
valid. In particular, for children C_1,C_2 meeting only at v,

\[
 F_C=\max\{F_{C_1},F_{C_2},
          I_{C_1}(v)+O_{C_2}(v),
          I_{C_2}(v)+O_{C_1}(v)\}.
 \tag{4}
\]

Each cross term uses disjoint edge sets on the two sides of v.
It cannot create a two-cycle or revisit a physical edge. The
within-child candidates already satisfy the same simple-path
restriction inductively. Thus finite entries describe exactly
the intended simple directed paths even though some individual
edges admit both directions.

The data structure returns a maximum-score ordered bin pair
with score

\[
        \sigma_a-\tau_b-\bar L_F(a,b),
 \tag{5}
\]

where bar L sums the donor costs in the actual a-to-b direction.
Source and target gadget edges have only their indicated
direction, so they introduce no extra interior use of an
endpoint price.

The threshold guarantees are unchanged: a positive score gives
true one-sided ratio greater than one quarter, and any available
forest path of true ratio greater than one half has positive
score under the same rounding budget.

The component maximum dictionary and point-edge edits use the
settled-transaction convention of the preceding note. A donor
price may now decrease as well as increase on a selected physical
edge; the point-update DP supports both cases.

## 3. Two directional buffers for one physical coordinate

For every selected incidence retain both register buffers

\[
        w_D=x_e-\ell_e,\qquad
        w_R=2\ell_e-x_e,
        \qquad w_D+w_R=\ell_e,
 \tag{6}
\]

and both guard buffers

\[
        g_D=x_e-\chi_e,\qquad
        g_R=U_e-x_e,
        \qquad g_D+g_R=U_e-\chi_e .
 \tag{7}
\]

The subscripts denote physical donor and receiving directions.
They do not denote a dynamic-tree parent or a temporary internal
root.

On a transfer eta through the edge:

* if the actual path direction is donor, x decreases by eta;
  w_D and g_D decrease by eta, while w_R and g_R increase by eta;
* if the actual direction is receiving, x increases by eta;
  w_R and g_R decrease by eta, while w_D and g_D increase by eta.

Equivalently, the buffer for traversing the path forward always
decreases by eta, and the buffer for traversing it backward
always increases by eta. This identity holds edge by edge and
does not require all edges of the path to have the same role.

## 4. Ordered-cluster lazy update

Maintain a separate ordinary-forest top tree for the allocation
watcher. It has no endpoint-price leaves.

For a path cluster C with two boundary vertices p,q, choose a
fixed local order of those boundaries, for example by vertex ID.
Store:

* the minimum register buffer along the path when traversed
  p-to-q, and the corresponding minimum for q-to-p;
* the two analogous guard minima;
* the two directional sums of donor costs;
* one signed lazy transfer tag t_C.

Directional minima and sums include only the cluster path,
never an off-path branch. The two directional versions are
different fields even if a special instance gives equal values.

A positive tag delta means transfer in the stored p-to-q
direction. Applying it updates

\[
 \begin{array}{c|cc}
       &p\text{-to-}q&q\text{-to-}p\\ \hline
 w_{\min}&-\delta&+\delta\\
 g_{\min}&-\delta&+\delta
 \end{array}
 \tag{8}
\]

and adds delta to t_C. A negative tag is the same operation
in the reverse direction. Donor-cost sums do not change until
a register event is discovered and processed.

### 4.1 Split and join

When a tagged cluster is split, propagate its tag only to its
path children. For each such child, the top-tree join record
identifies the order in which the parent path crosses the
child's two boundaries. Give the child +delta if that order
agrees with its stored order, and -delta otherwise.
Point children and off-path children receive no transfer tag.

The child's own signed tag composes by addition. Its forward
and backward minima change according to (8). This is the
usual exposed-path lazy discipline with two directional
aggregates and an orientation sign; it introduces only
constant state per cluster.

When clusters are joined, initialize the parent tag to zero.
Its directional path minima are the minima of the relevant
oriented path-child minima, and its directional donor sums
are the corresponding sums. Swap a child's two fields when
its stored order opposes the parent's traversal.

This uses only the local join boundary identities. A data
structure's internal evert or cluster reorder changes that
interpretation metadata; it never changes whether a physical
bin-to-row traversal is a donor.

### 4.2 Applying a returned path

For the returned ordered bin pair a,b, expose exactly its
ordinary underlying path. If the root cluster's stored order
is a,b, use tag +eta; otherwise use -eta. The DP guarantees
that all directions needed for this path are available.

Before committing, query the guard minimum in the actual
a-to-b direction and check the endpoint slack guards.
After committing, search for a nonpositive register buffer
in that same actual direction. Descend only through the
appropriate oriented path children, pushing tags as needed.

All buffers were positive in the preceding settled state.
During this update the opposite directional buffers only
increase, and off-path buffers do not change. Therefore every
new register crossing is found by this forward-direction
search. No enumeration of positive edges is needed.

At a reported edge, recover x from either physical formula
in (6), set ell=3x/4, and replace both directional buffers:

\[
                w_D=x/4,\qquad w_R=x/2.
 \tag{9}
\]

Recompute its one donor price bar c and notify:

1. the unique scored physical edge, whose donor directional
   score is now -bar c;
2. the watcher's directional donor-cost sums.

This notification is necessary even when the current path
used that edge in its receiving direction. The opposite
donor direction is present in the scored forest, so unlike
the single-direction interface its price cannot be treated
as an off-forest value.

Repeat until all forward register buffers on the updated
path are positive. Each event costs polynomial logarithmic
time. The final state satisfies both inequalities in (1)
on every selected edge.

### 4.3 Ownership across forest edits

Before cutting a physical edge, point-query its current
buffers, materialize its one x value, and store it in the
native allocation record. Remove that edge from both
representations. Other coordinates remain lazy.

On a link, reuse the native x and persistent ell, initialize
both (6) and (7), and assign the two directional DP scores
from (3). No register is reset just because the edge was
previously absent, appears at a different internal root, or
was last traversed in the opposite direction.

## 5. Feasibility and arithmetic

The finite-grid step rule is unchanged:

\[
 V_{\rm up}=1/s_a+1/s_b+4\bar L_F(a,b)/H,\qquad
       1/512\le\eta V_{\rm up}\le1/256.
 \tag{10}
\]

All directed bin-to-bin paths alternate physical donors
and receivers at their internal rows. They therefore
preserve the row/bin equations exactly. Coordinate
injectivity ensures that no x is changed twice by one
simple path.

Fixed-D feasibility is preserved for the complete threshold
graph.

* On a donor traversal, x decreases; its register can only
  move down at that step, making the donor price increase.
* On a receiving traversal, x increases; its donor price
  can decrease, but that direction is allowed only when
  D(row)=D(bin), so every nonnegative reverse donor price
  remains feasible.
* A physical edge can switch between these two behaviors
  on different steps. Each decrease is individually
  justified by tightness, so no monotonicity assumption
  across its entire history is needed.

The endpoint-source argument is again

\[
 D(b)\le D(a)+\bar L_F(a,b)
       \le A-\sigma_a+\bar L_F(a,b)<A-\tau_b.
 \tag{11}
\]

This pays the terminal price increase; the start's source
cost increases. The global maximum reciprocal does not
increase, so A remains valid. Update the endpoint-price
leaves and the two terms of the semantic E screen.

The constant positive objective progress and the safe
E<=5N LOW conclusion follow as in the preceding note.
An empty bidirectional forest search still does not imply
LOW after the state has evolved.

The signed tags, buffers, and point resets use the same
fixed dyadic denominators. A cluster's unapplied transfer
is the net change of any one edge on its nonempty path,
up to its fixed orientation sign since that tag was last
pushed. The guarded coordinate range bounds its magnitude.
Any internal operation changing only part of that path first
splits the cluster and pushes its tag. Thus the updates still
represented by an unpushed tag all cover that same whole path;
they are not mixed with unrecorded updates on only a subpath.
Repeated transfers or reversals do not create an
unbounded-denominator representation.

## 6. Event accounting and exact achieved result

A register reset is still triggered only after a constant
amount of absolute log variation since the previous reset.
Traversing an edge in the opposite direction does not
itself reset ell. The one-sided negative log variation
per accepted path is O(1) by (10), regardless of the
individual edges' earlier roles.

The accounting potential sum log x consequently gives
the same global reset bound

\[
       R=O\bigl(J+(N+A_{\rm ext})\log S\bigr).
 \tag{12}
\]

For J accepted steps, P supplied physical link/cut edits,
and Q extra queries, local work after the initial labels
and forest have been supplied is

\[
        (\nu+J+P+Q+R)\operatorname{polylog}S .
 \tag{13}
\]

This includes every selected donor-price change, including
those caused by receiving traversals. It includes explicit
guard discovery and the materialization of a cut
coordinate. The same price leaves and component records
give linear forest space.

The interface now searches every potential-compatible
simple path supported by the current physical forest.
In particular, it can move backward over a tight receiving
parent edge as a donor, then forward through another
branch, without a preliminary orientation pivot.

What remains absent is a controlled method for finding
useful physical edges outside the forest or for repairing
the fixed potential when a useful receiving direction is
not tight. Those tasks are not charged by (12) or supplied
by the constant-size cluster DP.

The completed reviews are
`bidirected_potential_forest_independent_audit.md` and
`bidirected_potential_forest_root_audit.md`.
