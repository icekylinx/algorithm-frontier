# Local metric growth without a root-forest bootstrap

**Conditional metric lemma, 24 October 2026.** This note proves a local
length bound for the proposed aspect-removal variant. It does not assume
that every deep recursive edge has already been installed as a canonical
path in a root exposed forest. The bound follows from the parent
tree-cycle graph and its compressed Steiner paths.

The separate prerequisites are: a valid maintained quotient by true
null edges in an SNC exported forest; the modified HRG comparison with
short auxiliary links; and the unchanged geometric, port, pool and
lifetime construction. This note does not prove their dynamic recourse.

## 1. Immediate input metrics and the permitted contractions

Consider one recursive degree-three general-cycle input `G_i` with
positive integral edge lengths at most `L_i`. Retain the current
integer gradients, including any frozen-gauge corrections inherited
from its parent.

Assume an exported SNC forest is modified as follows:

* Contract only an edge explicitly classified as **true null in the
  immediate flat map into `G_i`**. Such an edge has no input-edge
  image, equal endpoint images and zero gradient.
* A genuine forest edge with input-edge image `e` receives exactly
  `ell_e`, with the same oriented gradient. Its input edge identity
  is retained.
* Marked vertices and flat images descend through the quotient.

A genuine input edge is not contracted merely because its gradient is
zero, its endpoints have equal images at an earlier recursion level,
or its ultimate root projection is null. For example, a degree-port
connector is a genuine edge of the next input graph, even though it
projects to a vertex of its parent. Confusing these two notions of
nullity would invalidate this construction.

The quotient of a forest by a subforest of true-null edges remains a
forest. Genuine surviving edges do not become graph loops: their
endpoints could lie in one contracted null component only if the old
forest contained a cycle. This statement does not discard genuine
physical self-loop images, whose forest endpoints can be distinct
occurrences of the same input vertex.

Give every new HRG linking edge length one and gradient zero. Give
each paired off-tree edge length two and gradient zero. These assignments
have the correct physical meaning. In the source's Definition 4.28,
a paired edge joins two out-neighbors of the **same** vertex of `V_j`.
Both endpoints have the same immediate input image, and the represented
two-link path is physically null. Original off-tree edges in `E_graph`
retain their original lengths and gradients.

Consequently every edge of each resulting tree-cycle graph `J_i` has
length at most

$$
\widehat L_i=\max\{L_i,2\}.         \tag{1}
$$

The source passage for the paired-edge identity is Chen, Kyng, Liu,
Meierhans and Probst Gutenberg,
[arXiv:2311.18295v1, Definitions 4.2 and 4.28](https://arxiv.org/abs/2311.18295v1).
The ability to use the shorter lengths in the complete HRG comparison
is a separate mathematical prerequisite; an identity of physical
images alone does not establish that comparison theorem.

## 2. Every compressed geometric edge has only O(k) parent edges

Fix a portal period in `J_i`. Let `T_0` be its initial tree forest,
and let `P` be the set of permanent portals. The initial partition
counts tree vertices in its volume, not only off-tree incidences:
each portal-free component or piece has `O(k)` vertices.
All portals are terminals of the maintained geometric Steiner forest.

The geometric construction maintains

$$
K=(K_0\text{ with retired initial edges suppressed})
          \cup\{\text{current noninitial tree edges}\},
                                                               \tag{2}
$$

where `K_0` is the compressed Steiner forest of `T_0` on the current
terminal set. Before a tree edge is edited, both its endpoints are
promoted. Thus a retired initial edge is a direct `K_0` edge for the
rest of the period, and each newly inserted tree edge is direct
between terminals.

A compressed `K_0` edge has no portal in its interior, because every
portal is permanently a terminal. Its interior therefore stays in one
initial portal-free component of `O(k)` vertices. Including its two
boundary endpoints costs only an absolute additive constant. The same
argument applies to an initially small zero-portal component if it is
later activated. Noninitial edges in (2) have one edge each.

Hence, for an absolute constant `c_K`, every current geometric tree
edge is the compression of at most `c_K k` current parent tree edges.
Its stored length is their actual sum, so it is at most

$$
c_K k\widehat L_i.              \tag{3}
$$

Retained spanner aliases are coalesced into one central edge for each
original off-tree edge lifetime. That central edge retains its original
`J_i` length, not the stored length of an alias. Thus all edges of the
geometric child `K union E_star` satisfy (3), after enlarging `c_K`.

These are the local invariants proved in
[the geometric bridge, Sections 3--4](constant-degree-steiner-bridge.md)
and [the disconnected-component construction](disconnected-routing-components.md).
No root occurrence count is used in this argument.

## 3. A logarithmic port scale suffices

Let each geometric vertex have a fixed binary port tree with at most
`C` leaves. A passage between two ports uses at most `2 ceil(log_2 C)`
connector edges. Set

$$
H=2^{\left\lceil\log_2\!\bigl(
        \max\{2,4\lceil\log_2 C\rceil\}\bigr)\right\rceil}.
                                                               \tag{4}
$$

Multiply the length and gradient of every nonfiber geometric edge by
this same `H`, and give fiber connectors length one and gradient zero.
All child lengths remain positive integers.

A geometric circulation lifts through the fibers with added connector
length at most

$$
2\lceil\log_2 C\rceil\sum_e|d_e|
       \le H\sum_e\ell_e|d_e|,
$$

because every geometric edge has length at least one. The expanded
length is at most twice its scaled geometric length, while its
numerator is exactly multiplied by `H`. Conversely a child cycle
projects to the geometric graph with its numerator divided by `H`
and raw length at most its child length divided by `H`. Fiber edges
have zero physical charge. Thus the same constant quality loss as in
the old large-scale port construction is sufficient.

In particular the much larger scale `S^10` is not needed for this
specific port comparison. If another component requires a larger
scale, that requirement must be accounted for separately; it is not
part of the inequality just proved.

Equations (1)--(4) give the local recurrence

$$
L_{i+1}\le c_K k H\max\{L_i,2\}.                           \tag{5}
$$

The scales affect lengths and gradients together. Every returned
certificate must divide **both** quantities by `H` on this lift.

## 4. O(U) length bits through all outer levels

Let `2^U` be the common master bound and assume
`L_0<=2^(c_0 U)` for fixed `c_0`. Use the same `k` and `C` throughout
the recursion, with

$$
\log_2 H=O(\log U),\qquad
 U^\eta\le\log_2 k=O(U)
$$

for one fixed `eta>0`. Suppose the size-shrink argument independently
bounds depth by `d<=c_d U/log_2 k+c_d`, with absolute `c_d`.
For the proposed subpolynomial hierarchies these are precisely the
common master parameter and depth bounds.

Iterating (5),

$$
\begin{split}
 \log_2\max\{L_i,2\}
 &\le(c_0+1)U
    +i[\log_2 k+\log_2 H+O(1)]\\
 &=O_{c_0}(U),\qquad 0\le i\le d.
\end{split}
\tag{6}
$$

Indeed `d log k=O(U)`, while
`d log H=O(U log U/log k)=o(U)`. The hidden constants are independent
of the depth. There is no appeal to a root forest, root canonical
path, or an upper bound on the number of their currently existing
occurrences.

For a simultaneous hierarchy induction, impose the computable depth
guard `ceil(8U/log_2 k)+10` first and derive (6) throughout that prefix.
The resulting metric bound can then be used to verify the local factor
`A` and the shrink `m A/k`; geometric shrinking proves that the depth
guard is not reached. This orders the argument without presuming the
running-time conclusion that the metric estimate helps establish.

The same bound controls portal alias lengths. A stored alias is priced
from at most two simple parent tree legs and one off-tree edge; its
birth price is at most `(2m_T+1) max{L_i,2}`, up to a dyadic constant.
Here `m_T` counts that local tree-cycle graph, whose size is polynomial
in the master. Historical aliases retain such historical bounds.
Thus their prices also have `O(U)` bits. Their possibly larger prices
do not enter (5), because the recursive geometric child uses original
central-edge lengths and actual compressed-tree lengths instead.

## 5. Frozen-gauge gradients can remain longer

The conclusion concerns the metric, not every scalar field. Retain
the existing frozen-gradient gauges. A gauge subtracts endpoint
potentials formed by a parent tree-path sum. Even with `O(U)` length
bits, its gradients can obey only the conservative recurrence

$$
B_{g,i+1}\le B_{g,i}+O(U),
$$

including the common scale (4). Hence `B_g=O(U(d+1))` is allowed.
This does not enter the cover radius or `gamma_diam`, which depend
on lengths. Exact path-gradient sums, integer comparisons and the
small-graph cycle solver incur a fixed polynomial in `B_g`, which
must remain in the ordinary bit-cost allowance.

There is therefore no need to remove a correct frozen gauge merely
to improve the metric bound. New tree edges continue to carry their
actual frozen-gauge residual; a physically null projected edge need
not have zero gauged gradient in an intermediate representation.

## 6. Conditional parameter consequence

With SNC exponent `p=41/42` and (6), the aspect term is `O(U/kappa)`
instead of `O(U d/kappa)`. Set

$$
\beta=83/84,\quad \alpha=167/168,\quad
 \kappa\asymp U^{1/84}/\log U,
$$

and use `log k=Theta(U^alpha)`, `log C=Theta(U^beta)` and
`log A=Theta(U^beta(log U)^2)`. Then both the tree-family logarithm
and aspect-routing logarithm are `O(U^beta log U)`, and

$$
\beta+1-\alpha=\alpha.
$$

Thus the previously established depth-independent recurrences would
give common factor `exp(O(U^(167/168)(log U)^2))`. This last statement
is conditional on the proposed null-quotient and cheap-HRG-metric
construction actually satisfying the maintained cover, comparison,
recourse and lifetime interfaces. The local length proof does not
settle those prerequisites or claim a new complete matching theorem.
