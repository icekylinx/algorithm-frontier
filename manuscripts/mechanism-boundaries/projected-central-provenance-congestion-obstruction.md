# A congestion obstruction with literal first-touched central provenance

**Separate construction, 24 October 2026.** The arbitrary-ambient
example in
[congested-greedy-support-and-dynamic-boundary.md](congested-greedy-support-and-dynamic-boundary.md)
does not by itself settle the more restricted dynamic-repair
interface. Here we realize a comparable obstruction by an actual
old route table and a legal sequence of native vertex splits.
Every preliminary image has the required form
```math
\overleftarrow{P_e^u}\ \oplus e\ \oplus P_e^v,
 \tag{1}
```
with its OWN distinct genuine central native edge $`e`$.
The exterior prefixes are in a retained lower-layer graph, and
the two anchors are literally the first touched vertices of the
old route after the splits.

This disproves the proposed additive ambient guarantee for the
UNCHANGED congested-greedy selection, even on this restricted
class. It is not a lower bound on a different ambient-aware
selection algorithm. Nor does it claim that the currently used
deterministic static sparsifier will choose the specific initial
table constructed below.

## 1. The projected graph that will arise

Let $`L\geq2`$ be even, let $`T`$ be a full binary tree of height
$`4L`$, and put
```math
n=|V(T)|=2^{4L+1}-1,\qquad J=T^L,\qquad q=2^{L/2}.
 \tag{2}
```
As before,
```math
2^L\leq\Delta_J\leq3(2^L-1).
 \tag{3}
```
Each bottom subtree of height $`L/2`$ supplies a group of $`q`$
leaves. Choose a sign $`\chi(v)\in\{-,+\}`$ on the vertices of
$`T`$, putting exactly half of each such leaf group on each
side. Internal tree vertices can have either sign.

The congested-greedy order will process the $`n-1`$ TREE IDs first.
Every later $`J`$-edge has its unique tree route of length at most
$`L`$, and each tree edge has fewer than $`L2^L`$ route users.
At threshold $`\tau=4\Delta_JL`$, no edge saturates. Thus this
order selects exactly the abstract support $`T`$, of maximum
degree three. This is the same fully checked native argument
as in the earlier note.

## 2. Two native port systems and private central edges

All native edges in this section have unit length. Every tree is
an explicitly generated balanced binary tree with separate edge
IDs. Its root is attached by one edge to the indicated anchor;
its leaves are private ports. Constant-size cases can use a
subdivided edge. Every native vertex has degree at most three.

For each $`v\in V(T)`$, make one anchor $`z_v`$. It joins TWO
separate port systems:

* a prefix port tree $`P_v`$, attached to $`z_v`$ by one edge;
* a blue port tree $`B_v`$, attached to $`z_v`$ by one edge.

The anchor itself therefore initially has degree two.

### The shared prefix tree

Make a binary tree $`X`$ with two binary halves joined by one
distinguished central edge $`f`$. Reserve a separate port $`t_v`$
in side $`\chi(v)`$ for every $`v`$. Connect $`t_v`$ to a dedicated
leaf of $`P_v`$. The prefix trees and $`X`$, together with these
attachments, form one tree.

For every TREE edge $`e=uv`$, orient it from its tree parent
$`u`$ to its child $`v`$. Reserve a private leaf $`a_e`$ in
$`P_u`$ and a private leaf $`b_e`$ in side $`\chi(u)`$ of $`X`$.
Add the genuine central native edge
```math
e=a_eb_e .
 \tag{4}
```
Thus this selected candidate's OWN central edge stays entirely
on side $`\chi(u)`$ of the distinguished cut.

For every NON-TREE edge $`e=uv`$ of $`J`$, choose an orientation
and reserve private leaves $`a_e\in P_u`$, $`b_e\in P_v`$.
Add the genuine central native edge $`e=a_eb_e`$.
All these central edge IDs and all their endpoint ports are
distinct. These central edges are NOT initially selected.

Each side of $`X`$ needs only $`O(n)`$ reserved ports: the
$`t_v`$'s and at most one $`b_e`$ for each tree edge. Taking the
next power of two and leaving unused leaf ports harmlessly
present gives $`O(n)`$ actual vertices and depth $`O(\log n)`$.

### The blue connector graph

For every edge $`e=uv`$ of $`J`$, use one private leaf in $`B_u`$
and one private leaf in $`B_v`$, and join them by a blue edge
$`d_e`$. These IDs are distinct from every central ID $`e`$.
The blue connector, with its two endpoint-port paths, joins
anchors $`z_u,z_v`$.

Let $`H_0`$ contain ALL prefix-system edges, all blue-system
edges, and both attachment edges at every anchor. It excludes
the genuine central edges (4) and their non-tree analogues.
The full native graph consists of $`H_0`$ plus those central
edges. Both its vertex and edge inventories are
$`\Theta(|E(J)|+n)`$: in particular the blue system alone
has two separate port leaves for every $`J`$-edge.
The graph $`H_0`$ has linear size in its actual
native vertex inventory. There is no unidentified copied
central edge and no high-degree native vertex hidden in the
construction.

## 3. A valid, short initial lower-layer table

Every edge of $`H_0`$ uses its own identity route.
For a central edge $`e=uv`$, its old route is:

1. from $`a_e`$ to $`z_u`$, through $`P_u`$;
2. from $`z_u`$ through $`B_u`$, its OWN blue connector
   $`d_e`$, and $`B_v`$, to $`z_v`$;
3. from $`z_v`$ to $`b_e`$ through the prefix system.

For a non-tree $`e`$, step 3 stays inside $`P_v`$.
For a tree $`e=uv`$, step 3 runs through $`P_v`$, $`t_v`$,
the unique path in $`X`$, and the private port $`b_e`$.
These paths are simple and lie in $`H_0`$.
All have length
```math
\Lambda=O(\log n).
 \tag{5}
```

Their vertex-occurrence congestion, counting all initial native
input edge domains, is $`O(n)`$. At a blue or local prefix port
tree, at most $`\Delta_J`$ central routes occur, apart from
constantly many identity-route incidences. At a vertex of $`X`$,
only the $`n-1`$ TREE central routes can occur, again apart from
identity-route incidences. No non-tree central route uses $`X`$.
Therefore
```math
C_{\rm old}=O(n).
 \tag{6}
```
In particular these are low-length routes with an explicit
occurrence inventory, rather than compressed routes with
unaccounted multiplicity.

## 4. Legal splits produce exactly the desired preliminary images

For every anchor $`z_v`$, perform one native binary split:
its attachment to $`P_v`$ belongs to $`z_v^P`$, and its
attachment to $`B_v`$ belongs to $`z_v^B`$.
Both resulting vertices are touched. No edge is inserted or
deleted, and no central edge endpoint changes. The touched
set is exactly
```math
S=\{z_v^P,z_v^B:v\in V(T)\},
                         \qquad |S|=2n .
 \tag{7}
```
The native graph continues to have maximum degree three.

After ALL these splits, the blue system is a separate connected
component: its vertices are the $`B_v`$'s, the blue connectors,
and the $`z_v^B`$'s. Its only former links toward the prefix
system passed through the unsplit anchors, and those links have
all been severed by partitioning the two incidences. Every
genuine central edge has both endpoints in the prefix system
(possibly one endpoint in $`X`$). Thus there is no surviving
blue bypass, even in the full current native graph.

Each central old route is now genuinely broken at its two
anchors. Starting at $`a_e`$, its first touched vertex is
$`z_u^P`$. Starting at $`b_e`$, its first touched vertex is
$`z_v^P`$. No exterior prefix contains any other touched
vertex: the blue-side anchors lie in the disconnected middle
piece of the broken old route.

Consequently its projected edge is precisely
```math
\widehat e=z_u^Pz_v^P.
 \tag{8}
```
The preliminary image is the retained prefix from $`z_u^P`$
to $`a_e`$, the OWN central edge $`e=a_eb_e`$, and the retained
prefix from $`b_e`$ to $`z_v^P`$. It is simple.

For a tree ID this image goes through $`X`$; for a non-tree ID
it uses only its endpoint prefix trees and its central edge.
The nonloop projected graph is thus EXACTLY $`J=T^L`$.
The identity route of an $`H_0`$ edge incident to a split
anchor projects only to a loop at that edge's actual
descendant anchor; its normalized preliminary image is empty.
Other base identity routes are unaffected. There are no extra
nonloop projected blue edges and no unmentioned usable
old connector between prefix anchors.

More explicitly, an attachment edge has exactly one touched
current endpoint, either $`z_v^P`$ or $`z_v^B`$, and an
untouched port-tree root as its other endpoint. In its
one-edge identity route, the nearest touched vertex from
BOTH ends is that SAME current descendant. The preliminary
image goes out and immediately back along the same ID,
so normalization leaves an empty route WITH the anchor
annotation. No other base edge is incident to a touched
vertex. This accounts for every additional affected base
domain.

The preliminary normalized table satisfies
```math
L(W')=O(\log n),\qquad C(W')=O(n),
                       \qquad\Delta(J)\leq3\cdot2^L.
 \tag{9}
```
All images retain typed central IDs. In fact normalization
does not erase the central ID in this particular input table.

## 5. Greedy selection creates a true ambient cut bottleneck

Apply the unchanged congested-greedy algorithm to this projected
graph, in the order of Section 1. It selects the abstract tree
$`T`$. The actual repaired support therefore consists of the
current lower graph $`H_0`$ and only the genuine central IDs
corresponding to TREE edges.

Assign every prefix tree $`P_v`$, its anchor $`z_v^P`$, and
its attachment to side $`\chi(v)`$. The two halves of $`X`$
have their indicated sides. Every selected TREE central edge
joins $`P_u`$ to its port $`b_e`$ in the SAME side $`\chi(u)`$.
The entire blue component can be assigned arbitrarily to
one side, since after the splits it has no edge to the
prefix component. Thus the ONLY edge of this actual repaired
support crossing the distinguished partition is $`f`$.

For every leaf pair $`u,v`$ in one bottom group with opposite
signs, its genuine non-tree central edge has endpoint ports
in opposite sides. Any repaired route for that demand in the
selected support MUST cross $`f`$, regardless of its chosen
abstract tree orientation or subsequent loop erasure.
There are
```math
(2^{4L}/q)\,(q^2/4)
                         =\Omega(n2^{L/2})
 \tag{10}
```
such simultaneous demands.

Combining (9)--(10), the output congestion is larger than
$`C(W')+\Delta(J)`$ by a factor $`\Omega(2^{L/2})`$.
Since $`n=\Theta(2^{4L})`$, this is a polynomial
$`\Omega(n^{1/8})`$ factor. It is not a backtracking artifact:
a nonempty cut must still be crossed after normalization.
It is also not due to a shared or omitted central edge:
every central lifetime is distinct and genuine.

## 6. Initial-base bounds and the exact scope boundary

The degree-three construction proves that the SPECIAL
prefix--own-central--suffix provenance, legal first-touched
anchors, short old routes, sparse lower support, and bounded
current native degree do not force the desired additive
ambient bound for congested greedy.

One must distinguish (6) from an even stronger possible
fresh-base guarantee $`C_{\rm old}\leq\Gamma\Delta_{\rm native}`$
when the actual native degree is three. The displayed table
has $`C_{\rm old}=\Theta(n)`$, so it is not asserted to be
the output of a particular fresh-base algorithm having a much
smaller congestion guarantee at that actual degree.

If degree-proportional initial bounds are required at a
declared core degree cap $`k`$, one may take $`n\leq k`$
and append an UNTOUCHED disjoint auxiliary component with
actual native degree $`\Theta(n)`$ and a sparse, explicit
base routing table. For example, on the next power-of-two
number of auxiliary vertices, use the complete graph as
input, its bit-coordinate hypercube as selected support,
and fixed-coordinate-order cube paths as routes.
The paths have length $`O(\log n)`$, each cube edge has
at most $`O(n)`$ route occurrences, and every cube vertex
has at most $`O(n\log n)`$ occurrences. The selected degree
is $`O(\log n)`$, so no large selected star is introduced.

The combined actual native degree is $`\Theta(n)\leq O(k)`$,
and the whole initial table has
```math
\Lambda=O(\log n),\qquad
      C_{\rm old}=O(n\log n)
                      =O(\Delta_{\rm native}\log n).
 \tag{11}
```
For a static initial call with the identity ambient embedding,
its input congestion is at most $`\Delta_{\rm native}`$.
The constructed $`H_0,R_0`$ therefore meets the usual size,
length and additive-congestion OUTPUT contracts with
$`\Gamma_0=O(\log n)`$, after increasing a fixed constant:
its support is sparse, its paths have length $`O(\log n)`$,
and its congestion is $`O(\Gamma_0\Delta_{\rm native})`$.
Consequently a black-box deduction using only those contracts
cannot exclude this initial table.
The auxiliary component receives no split and contributes
no nonloop projected demand. The obstruction (10) is unchanged;
even relative to the combined initial bound it loses a factor
$`\Omega(2^{L/2}/\log n)`$. All inventories remain polynomial
in $`n`$, and the lower selected support is sparse. Additional
untouched components may enlarge a declared parent period
without changing this local calculation.

The size variables must remain distinct. The gadget has
$`\Theta(m_J)`$ native vertices, where $`m_J=|E(J)|`$, but
only $`n`$ anchor splits and $`2n`$ touched vertices.
A parent/core application with shrink parameter $`k\geq n`$
must supply a sufficiently large actual parent inventory.
For example the combinatorial size inequalities are satisfied
if
```math
m_{\rm parent}\geq c k m_J ,
 \tag{12}
```
for a fixed sufficiently large $`c`$: the allowed
$`m_{\rm parent}/k`$ core-vertex inventory can contain the
gadget and the $`n`$ split events, and the auxiliary complete
graph's $`O(n^2)`$ native edges also fit this parent bound.
This is only a size check. Constructing the exact preceding
low-stretch-forest/ASZ execution, and proving that its
deterministic initialization returns this table, would be
ADDITIONAL requirements; they are not established by padding
with untouched components.

Thus this is a literal legal route-table/update-history
realization with the standard degree and length envelopes.
It does NOT establish that the specific current initialization
routine, including its deterministic tie breaking, produces
these tables, or that every ambient-aware variant fails.
It identifies the missing positive invariant precisely:
the selected central support and its CURRENT routes must
control shared LOWER-PREFIX resources. Separate native-edge
load caps on the projected graph do not see those resources.

### A necessary ambient-cut condition for a replacement

Let $`A`$ be any cut of the actual native ambient graph,
and let $`D_A`$ count current demand IDs whose genuine
endpoints lie on opposite sides. If the repaired support is
$`H_0\cup E_{\rm sel}`$ and its routes have edge congestion
at most $`\rho`$, then necessarily
```math
D_A\leq
               \rho\,|\partial_{H_0\cup E_{\rm sel}}A|.
 \tag{13}
```
The same necessary inequality follows from a vertex-occurrence
congestion bound, since that bounds each edge's occurrence
load too. It is simply the fact that every crossing demand
must traverse a support edge of the cut.

In the displayed example $`H_0`$ contributes only the edge
$`f`$ to the cut and the greedy-selected central IDs contribute
NONE. A repair with target
$`\rho=\Gamma(C_{\rm old}+\Delta_J+\Delta_{\rm native})`$
must therefore select additional genuine central IDs that
cross this ambient cut (or otherwise change the lower
support). Merely having many selected PROJECTED tree edges
cross the anchor partition does not suffice: those tree
edges cross the ambient cut through their shared lower
prefix, while their own central edges stay inside one side.

Condition (13) is only necessary, not a claimed sufficient
multicommodity-routing theorem. It pinpoints the additional
structure an ambient-aware dynamic selection must maintain,
without ruling out that such a construction is possible.
