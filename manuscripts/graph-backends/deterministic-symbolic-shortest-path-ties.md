# Deterministic symbolic ties for globally consistent shortest paths

**Static finite-word lemma, 24 October 2026.** Nonnegative shortest
paths can be made unique and globally consistent without constructing
an integer with one bit per edge. The method uses an exact, persistent
binary representation of the tie signature and deterministic
canonicalization. It is a per-source shortest-path construction,
not an all-pairs or dynamic shortest-path theorem.

## 1. Input and exact tie convention

Let the graph have $n$ vertices and $m$ genuine ranked edge
records. In a directed graph these are directed arc IDs. In an
undirected graph they are genuine physical edge IDs, with the SAME
rank used for both traversal orientations of one edge. Different
parallel edges have different IDs.

Fix an injective rank function into $\{1,\ldots,m\}$, once for
the graph and all its sources. Distinct immediate native aliases
must remain distinct even when their eventual physical images
coincide. A real edge is not identified with another edge or with
a null image for purposes of this order.
Every actual native graph edge, including a zero-length connector
or an edge with null eventual physical image, receives its own
genuine ID and rank under this convention.

Lengths are nonnegative integers with at most $b$ bits, or have
the form
$$
\ell_e=a_e/D,\qquad
       0\le a_e<2^b,\quad 1\le D<2^b,
 \tag{1}
$$
on ONE declared common denominator. All true-distance computations
can then use the integer numerators. Arbitrary unrelated per-edge
$b$-bit denominators do not give the same arithmetic bound:
their common denominator may have $\Theta(mb)$ bits. In that
case the actual common-grid encoding length must be charged.

For a walk $P$, including repeated traversals, define the
MATHEMATICAL additive perturbation
$$
\tau(P)=\sum_{e\text{ traversed in }P}
                                     2^{-\mathrm{rank}(e)}.
 \tag{2}
$$
For undirected edges the orientation does not change this
positive tie cost. Order walks lexicographically by
$$
(\ell(P),\tau(P)).
 \tag{3}
$$
The first component has absolute priority. This does not alter
the ordinary shortest-distance value.

Equation (2) defines an additive cost on ALL walks, with
multiplicity. Its numerical value need not be represented.
The algorithm below only stores signatures of simple paths.

## 2. Existence, uniqueness, and consistency

Every edge has strictly positive cost in the lexicographic order:
its true length is nonnegative and its tie contribution is positive.
Consequently deleting a closed nonempty subwalk strictly decreases
(3), even when that subwalk has true length zero. Every optimal
walk is therefore a vertex-simple path.

A simple path uses any genuine ranked edge at most once. Its tie
signature is a zero-one vector. For two different such signatures,
let $r$ be their first differing rank. The contribution $2^{-r}$
strictly exceeds the sum of every later available contribution:
$$
\sum_{j=r+1}^{m}2^{-j}<2^{-r}.
 \tag{4}
$$
Thus the first differing bit determines the exact comparison;
zero is smaller than one. Distinct finite zero-one signatures
never have equal tie cost.

For fixed ordered endpoints, the edge-ID set of a vertex-simple
path determines that path. In a directed graph its selected arcs
form a directed chain. In an undirected graph its selected edges
form an undirected chain, whose orientation is determined by the
ordered endpoints. Hence every reachable ordered pair has a
UNIQUE minimum under (3).

This uniqueness is globally subpath-consistent. If a subpath of
the selected $s$-to-$t$ path could be replaced by a cheaper
path between its endpoints, additive costs would give a cheaper
$s$-to-$t$ walk. Removing any resulting cycles could only
decrease its cost further, a contradiction. Therefore the selected
subpath is the path selected when its own endpoints are used as
source and target.

For an undirected graph, using one rank in BOTH orientations also
gives reversal consistency:
$$
P(v,u)=P(u,v)^{\rm rev}.
 \tag{5}
$$
If separate directed arc ranks are assigned to the two orientations
instead, directed subpath consistency remains true but (5) need
not hold. That alternate convention must not be used when a
distance-oracle interface needs undirected reversal consistency.

## 3. The exact canonical signature data structure

Let
$$
H=\lceil\log_2\max\{1,m\}\rceil,\qquad
                              T=2^H.
$$
Use a complete conceptual binary segment tree on positions
$1,\ldots,T$. Positions above $m$ always remain zero.
No full tree or length-$T$ bit array is allocated.

There are two canonical leaf records, for bits zero and one.
A node of height $h>0$, with child identifiers $L,R$, is
interned by the exact key
$$
(h,L,R).
 \tag{6}
$$
Store keys in an ordinary deterministic balanced search tree.
A successful lookup returns the already existing canonical node;
otherwise allocate one fresh node ID and store its two child
pointers. This is exact structural interning, sometimes called
hash-consing, but it uses no hash value, random seed, or collision
assumption.

The all-zero node of height $h$ is obtained recursively from
two references to the all-zero node of height $h-1$.
Only one such node per height is necessary. Initialization uses
$O(\log(m+2))$ nodes and dictionary operations.

By induction on height, two stored nodes of the same height have
the same identifier if and only if they encode the same bit
vector. Node IDs are collision-free names, not probabilistic
fingerprints. Node records are immutable.

### Appending a new ranked edge

Given a path root and an edge rank not yet present, follow the
root-to-leaf search for that rank, replace its zero leaf by the
one leaf, and intern the rebuilt ancestors. This changes at
most $H+1$ nodes. The old root remains a valid persistent
version.

There are $O(\log(m+2))$ canonical-node updates, each implemented
by a balanced-map operation. With $K_{\rm nodes}$ currently
stored nodes, the word-operation cost is
$O(\log(m+2)\log(K_{\rm nodes}+2))$.

### Comparing two signatures

If their root IDs are equal, the signatures are equal.
Otherwise compare their left-child IDs. Descend left if they
differ, and right if they agree. Repeat until the first differing
leaf is reached. Equation (4) then determines the exact order.
This takes $O(\log(m+2))$ node reads and ID comparisons.

The tree is balanced by its fixed conceptual shape. No
probabilistic balancing or data-dependent rotation of this
signature tree is used; only the interning dictionary needs an
ordinary deterministic balanced-map implementation.

## 4. Dijkstra only requests simple signatures

Run Dijkstra with the pair (3) as its key. A finite tentative
label stores:

* its exact integer true-distance numerator;
* its canonical tie-signature root;
* its predecessor vertex and genuine edge ID.

Unreachable labels are separate infinity records. The source
starts at the zero numerator and the all-zero signature.

When a vertex $u$ is settled, scan its outgoing arcs. Relax
$u\to v$ only if $v$ is still unsettled. All vertices on
the settled predecessor path to $u$ are already settled:
each predecessor was settled before its label was installed,
and every edge is strictly positive in the pair order.
Consequently $v$ is NOT on that predecessor path.

The candidate path obtained by appending $u\to v$ is therefore
vertex-simple. In particular, the appended genuine edge ID
has not already appeared in the path. Its signature update
really is a zero-to-one change, rather than a multiset update
with a binary carry. A self-loop has a settled head and is
skipped. The two traversal orientations of one undirected
edge cause no problem for the same reason.

This proves inductively that every stored finite label and every
candidate that is compared has a zero-one signature. Rejected
candidates may leave interned nodes behind; there are still only
linearly many candidate attempts.

The usual Dijkstra proof applies to the lexicographically ordered
additive costs, since every edge cost is nonnegative in that order.
Skipping relaxations into settled vertices is therefore correct.
Zero true-length edges are harmless: their positive tie weights
ensure strict increase in the complete key along each predecessor
edge.

The final predecessor paths are precisely the unique paths of
Section 2. Different sources can use separate canonicalization
dictionaries; the semantic global rank order, not pointer equality
between different dictionaries, supplies their consistency.

## 5. Space, arithmetic, and per-source time

Each directed arc is scanned at most once from a settled tail.
For an undirected edge there are at most two orientation scans.
Thus there are $O(m)$ candidate attempts. Each creates at most
$O(\log(m+2))$ canonical nodes, giving
$$
K_{\rm nodes}=O(m\log(m+2)+1)
 \tag{7}
$$
per source, including discarded tentative labels. Canonical node
IDs consequently use $O(\log(m+2))$ bits. There is no hidden
$m$-bit integer arithmetic.

After compacting the nonisolated part, at most $2m$ vertices
are incident to edges; an isolated source is handled directly.
A simple path has $O(m)$ edges, so its true-distance numerator
uses
$$
O(b+\log(m+2))
 \tag{8}
$$
bits. An ordinary binary heap makes
$O((m+n_{\rm active})\log(n_{\rm active}+2))$ key comparisons.
A key comparison uses a comparison of (8)-bit integers, followed
when needed by the $O(\log(m+2))$ signature comparison.
Interning costs $O(m\log^2(m+2))$ balanced-map word operations.
Integer addition and every map/key operation have their ordinary
charged finite-bit costs.

Thus on the compact graph the total work is
$$
O\bigl((m+1)\mathrm{poly}
                                  (b+\log(m+2))\bigr)
 \tag{9}
$$
bit operations, with a fixed polynomial. Supplied isolated
vertices require $O(n)$ additional output/bookkeeping records.
If full uncompressed input identifiers are charged bit by bit,
their actual identifier length must also be included; one safe
full statement is
$$
O\bigl((n+m+1)\mathrm{poly}
                              (b+\log(n+m+2))\bigr).
 \tag{10}
$$
In a word-RAM representation with passive original IDs, one
linear cleanup handles those labels and (9) is the substantive
per-source bound. The compact numerical applications already
supply the required identifier bound.

If several sources share one interning table, its node-ID bit
length depends on the TOTAL number of nodes built for those
sources. Alternatively each source uses its own table and has
the bound (7). Cross-source pointer sharing is not needed for
global consistency.

### 5.1 Truncated-search implementation used by local balls

The same algorithm can stop after a prescribed number of settled
vertices or at a prescribed true-distance radius. Suppose it scans
A actual outgoing arc records and reaches V_A vertex records before
stopping. Its candidate-node count is O((A+1) log(m+2)), and its
work is

$$
(A+V_A+1)\mathrm{poly}(b+\log(m+2)),
$$

using the already assigned global ranks. Store tentative labels and
visited flags in sparse dictionaries of reached IDs; do not clear an
n-entry array or rebuild the rank map for every local search. Only
O(log(m+2)) all-zero signature nodes are initialized per run. Every
settled path still has its globally defined unique meaning. This
justifies the use in bounded-ball constructions when their own
analysis bounds A and V_A; it does not supply that exploration bound.

## 6. Stability under deletions

Fix the genuine native IDs, their rank order, and all surviving
true lengths. Let $P$ be the selected path in a graph $G$.
If a subgraph $G'$ deletes no vertex or edge of $P$, then
$P$ remains available with the same cost. Every competing
path of $G'$ was already a path of $G$. By uniqueness in
$G$, none can tie or beat $P$, so $P$ remains selected
in $G'$.

The same reasoning permits increases of lengths only on edges
outside $P$. It does not cover inserting new competitors,
decreasing their lengths, changing ranks, or retiring an edge
lifetime used by $P$. Preserving only an eventual physical
image is insufficient: distinct native aliases and replacement
lifetimes are distinct ranked objects.

For a deletion sequence the original rank universe may be kept;
its logarithm is charged to that fixed lifetime universe.
No new rank array is cleared or reallocated after each deletion.
The statement concerns the identity of the mathematically selected
path, not the cost of dynamically maintaining all affected paths.

## 7. Scope for shortest-path and routing constructions

This lemma supplies globally additive deterministic ties,
unique shortest paths, subpath consistency, undirected reversal
consistency under the proper rank convention, and selected-path
persistence under avoiding deletions.

It does NOT support arbitrary signature addition by bitset union.
If two stored paths share an edge, their concatenation has a
multiplicity in (2), and its perturbation may have carries.
The zero-one data structure is justified only because the
Dijkstra candidates in Section 4 are simple. A different
algorithm comparing arbitrary concatenated walks needs a
separate representation and arithmetic proof.

Likewise, this lemma alone does not repair a cone-cluster
geometry argument, produce a dynamic shortest-path oracle,
or compute all-pairs distances in the per-source time (9).
Running it from many sources pays for every such run. It is
a precision and deterministic tie-selection component that
may be inserted into an otherwise justified AN/KMPG local
shortest-path construction.
