# Weighted distance spanners: a packing implication and its width boundary

**Conditional mechanism analysis, 24 October 2026.** This note examines
one possible replacement for the static ambient router. It gives a
positive packing calculation, then identifies an interface that is
missing from the proposed shortcut. It is not a running-time lower
bound for weighted spanners, multiplicative weights, or matching.

## 1. The weighted-response hypothesis

Let J have q nonloop demand edges and let each input edge e have a
simple path Pi(e) in an immediate ambient graph with resource set X.
Put R=|X| and assume R>=1. The input table has congestion at most C0.
Distinct native IDs remain distinct demands.
The path endpoints respect one fixed native-to-ambient vertex map,
so consecutive native edges have concatenable ambient images.
If q=0 there are no routes to choose; below assume q>=1. Write Delta
for the maximum degree of J.

For any supplied positive resource prices w_x, assign the native
edge cost
$$
c_w(e)=\sum_{x\in\Pi(e)}w_x.
$$
Suppose a deterministic weighted-spanner oracle returns a selected
subgraph H with at most s edges and, for every e=uv, an explicit H-path
P_e satisfying
$$
\sum_{f\in P_e}c_w(f)\leq\alpha c_w(e).       \tag{1}
$$
Any desired bound on the number of native edges in P_e must be a
separate oracle guarantee; weighted distance alone does not provide it.

Expand P_e using the supplied Pi table, then loop-erase the resulting
ambient walk. With positive prices this does not increase its cost.
Loop erasure uses immediate ambient vertex IDs, never a later
identification of distinct aliases through their physical images.
Let a_x be the number of resulting simple ambient paths using x. Then
$$
0\leq a_x\leq q,\qquad
 \sum_x w_x a_x
       \leq\alpha\sum_e c_w(e)
       \leq\alpha C_0\sum_x w_x.                           \tag{2}
$$
Thus a weighted distance oracle gives a low-cost aggregate response.
It does not give a bound a_x=polylog(R)(C0+Delta) for each resource.

## 2. A literal multiplicative-weights construction

Start with w_x=1. After response a^(t), update
$$
w_x\leftarrow w_x(1+a_x^{(t)}/q).
                                                                    \tag{3}
$$
This is a mathematical packing calculation; exact products in (3)
would have T-dependent bit size, which a fast implementation would
also have to address. From (2), the total weight after T responses is
at most
$$
R(1+\alpha C_0/q)^T
                    \leq R\exp(T\alpha C_0/q).
$$
For 0<=z<=1, ln(1+z)>=z ln 2. Comparing one coordinate's weight with
the total gives
$$
\max_x\frac1T\sum_{t=1}^T a_x^{(t)}
       \leq\frac{\alpha C_0+q\ln R/T}{\ln 2}.             \tag{4}
$$
For example, let D=gamma(C0+Delta) with gamma>=4 alpha, and take
$$
T\geq\max\{1,4q\ln R/D\}.
$$
Then the average response has congestion below D. The union of the
T native selected subgraphs has at most Ts selected IDs. Keep every
candidate as a pair: its native H-path P_e and its loop-erased ambient
record. The latter lies in the EXPANDED support formed by the images
Pi(f) of those selected IDs; it need not itself be a native path in
the union. For each demand, choose uniformly from its T supplied
simple ambient records. Apply the deterministic sparse path-selection
lemma with group weight one, equal candidate masses, and individual
resource bound one. It makes these choices integral with load at most
2D+log(8R+8), while retaining the associated native path and its
selected-ID support.

This congestion bound is for the NORMALIZED ambient records. Ambient
loop erasure can remove only part of an input edge image, so the
chosen record need not equal the literal un-erased composition
Pi(P_e). The calculation alone does not prove the same bound for
that composition. An application requiring that stronger typed
interface needs an additional argument. The selection step also
cannot remove the cost of obtaining the explicit response inventory
or its selected-support union.

This is a useful conditional construction. Its currently certified
number of oracle responses contains the width q/D. Merely replacing
the oracle by a faster distance-spanner algorithm does not remove
that term or the Ts support bound. Nor does (4) prove that a particular
instance actually requires that many iterations.

## 3. Linear width is consistent with all the distance guarantees

Take two full binary trees, each with Q=2^h leaves, and join their
roots by an edge f. Let T be this tree. Add a simple D0-regular
bipartite graph between the two leaf sets, where 4<=D0<=Q; a union
of D0 distinct cyclic perfect matchings is an explicit choice.
The resulting native graph J has
$$
n=4Q-2,\qquad q=4Q-3+D_0Q,\qquad
 \Delta=\max\{3,D_0+1\}.
$$
Use J itself as the ambient graph, take EDGE resources X=E(J),
and use the identity input images,
so C0=1. At uniform resource prices, H=T is an alpha-spanner with
alpha=2h+1. Every demand path has at most alpha native edges; H has
n-1 edges and maximum selected degree three.

Nevertheless the response load on f is
$$
a_f=D_0Q+1.                         \tag{5}
$$
All of these routes are already simple ambient paths, so loop
erasure does not reduce (5). For D0 growing with Q, the input is
also substantially denser than the selected tree. Relative to the
desired target D=gamma(C0+Delta), (5) gives
$$
a_f/D=\Omega(n/\gamma).
$$
Taking gamma to be a fixed polynomial in log n leaves a polynomial
width. Given an otherwise valid all-price oracle whose allowed
stretch is at least 2h+1 and whose support cap is at least n-1,
overriding only its uniform-price response with this H preserves
those guarantees. This does not assert the existence of an all-price
oracle with the exact support cap n-1; the tree's smaller size and
degree three are properties of the displayed response.
Hence a pointwise width guarantee cannot be deduced from (1), even
when explicit short paths and selected degree three are supplied.

The example does NOT assert that every oracle selects this tree,
that a particular multiplicative-weights execution is slow, or that
an ambient-aware construction cannot avoid it. It establishes the
logical gap in invoking a width-free packing conclusion from the
distance contract alone.

## 4. The missing improvement

To turn this route into a smaller matching exponent, one would need
at least one additional mechanism: a response oracle with suitably
bounded ambient load, a faster packing method with a charged explicit
path inventory and controlled union support, or a dynamically maintained
support that absorbs price changes with the required selected-ID
recourse. Each must preserve native provenance and normalized routes.

The existing static provider supplies its ambient load through a more
specific routing and weighted-selection construction. The present
calculation does not replace that construction or prove a smaller
matching exponent. Related native/ambient distinctions appear in
[the congestion-capped greedy note](congested-greedy-support-and-dynamic-boundary.md)
and [the central provenance example](projected-central-provenance-congestion-obstruction.md).
The deterministic selection step, when a suitable response inventory
has actually been supplied, is proved in
[the nonuniform path-selection lemma](../graph-backends/nonuniform-fractional-path-selection.md).
