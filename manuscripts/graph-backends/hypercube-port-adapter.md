# An elementary hypercube port adapter for the sequential router

**Optional correctness simplification, 24 October 2026.** The sequential
router can avoid importing a constant-degree expander family for its
incidence fibers. Explicit hypercube fibers give a graph of maximum
degree O(log m), with only a polylogarithmic change to work and
conductance. The fixed polynomial degree factors already paid by the
virtual hierarchy absorb this change. The stated 4/5 matching envelope
does not change.

The constant-degree adapter in
[degree-split-token-routing-interface.md](degree-split-token-routing-interface.md)
remains an alternative. This note is a self-contained replacement for
that local graph construction, not a new routing or matching theorem.

## 1. Actual vertices, edge IDs, and construction cost

Let G be a connected loopless undirected multigraph with m>=1 genuine
edge IDs, no isolated vertices, and conductance at least 0<phi<=1.
For each v, put d_v=deg_G(v) and let a_v be the least power of two
at least d_v. Thus d_v<=a_v<2d_v, except that equality a_v=d_v
is permitted. Construct a cube of dimension log_2(a_v), with a_v
vertices, as the fiber of v. A one-vertex fiber has no internal edge.

Assign the d_v real incidences of v to distinct fiber vertices.
For every original edge e=uv, join its assigned u-port to its assigned
v-port by one external edge carrying the original ID e.
The other a_v-d_v fiber vertices have no external edge.

The graph P has

```math
|V(P)|=\sum_v a_v\leq4m,\qquad
 |E(P)|=m+\frac12\sum_v a_v\log_2(a_v)
                          =O(m\log(m+2)).
 \tag{1}
```

Every port has at most one external edge, and

```math
\Delta(P)\leq B:=1+\lceil\log_2(2m+1)\rceil.
 \tag{2}
```

The graph is simple even if G has parallel edges: different original
edge IDs use different real incidence ports, and fiber edges stay
inside one original vertex. G has no loops, so a fiber edge is never
an external edge. P is connected because every cube is connected
and G is connected.

Vertices and edges are generated directly by bit flips in each
ACTUAL cube. Construction takes O(m log(m+2)) word operations.
There is no padding to a master-size graph. The less-than-two
rounding of each actual incidence count is the only enlargement.

## 2. A self-contained cube cut bound

For the q-dimensional cube Q_q and every subset S, its internal
edge boundary is at least

```math
\min\{|S|,2^q-|S|\}.
 \tag{3}
```

Here is an induction requiring no explicit-expander theorem.
By complementation assume |S|<=2^{q-1}, and write its intersections
with the two (q-1)-dimensional halves as S_0,S_1. Put
H=2^{q-1}, a=|S_0|, b=|S_1|, and exchange halves if needed
so a>=b. The edges joining the halves contribute
|S_0 triangle S_1|>=a-b. The induction hypothesis gives

```math
|\partial S|\geq
        \min(a,H-a)+\min(b,H-b)+(a-b).
 \tag{4}
```

If a<=H/2, then b<=H/2, and the right-hand side is at least
a+b. Otherwise b<=H-a<=H/2, and the right-hand side is
H>=a+b. This proves (3). The one-vertex base is vacuous.

## 3. Conductance of the whole port graph

Take a nontrivial port cut S. In every fiber round its intersection
to that fiber's majority side, breaking ties deterministically.
Let T be the resulting union of full fibers, let z=|S triangle T|,
and put w=min(|S|,|V(P)\S|).

Equation (3), summed over fibers, gives at least z INTERNAL crossing
edges. The rounded original cut is some vertex set A in G.
Since d_v>=a_v/2,

```math
\min\{\mathrm{vol}_G(A),
               \mathrm{vol}_G(\overline A)\}
       \geq \frac12\min\{|T|,|V(P)\setminus T|\}
       \geq \frac12(w-z).
 \tag{5}
```

This inequality is still valid if T or its complement is empty:
then w-z<=0. Original conductance and the fact that changing a
port's side changes at most one external crossing imply

```math
\begin{aligned}
 |\partial_{\rm external} S|
   &\geq \frac{\phi}{2}(w-z)-z\\
   &=\frac{\phi}{2}w-(1+\phi/2)z.
 \end{aligned}
 \tag{6}
```

If z>=phi w/8, the internal edges already suffice. Otherwise (6)
is at least 5phi w/16, because phi<=1. In either case,

```math
|\partial_P S|\geq\phi w/8.
 \tag{7}
```

The smaller port volume is at most B w by (2). Therefore

```math
\Phi(P)\geq\frac{\phi}{8B}.
 \tag{8}
```

We use conductance only after excluding the empty or full cut,
as usual. P has no isolated vertex: a one-vertex fiber has its
genuine external edge.

## 4. Tokens and original paths

Suppose starts and destinations separately have multiplicity at most
D deg_G(v) at every original v, for an integer D>=1.
Distribute each list cyclically over the d_v REAL incidence ports.
Every such port gets at most D starts and at most D destinations.
Unused fiber vertices get none.

A router with per-port load D is therefore sufficient. It is allowed
to create its usual dummy tokens on all the vertices in (1);
their total volume is still O(mD), before the already charged
polylogarithmic factors.

Project every internal cube move to the empty move at its original
vertex. Project every external move to its genuine original edge ID.
An explicit port walk becomes an endpoint-correct walk in G.
Loop erasure with IMMEDIATE original native vertex IDs makes it
simple without increasing length or original-edge occurrence load.
Opposite orientations and repeated original IDs are treated as actual
traversals before erasure; physical aliases are not identified.

## 5. Why the accepted quantitative envelopes are unchanged

In the range used by
[sequential-expander-routing-tradeoff.md](sequential-expander-routing-tradeoff.md),
the actual inventories have size at most 2^{O(U)}, and
h=ceil(log_2(U+4)). Equations (1), (2), and (8) change the relevant
input bounds only by

```math
m_P=O(mU),\qquad
        \Delta(P)=O(U),\qquad
        \log(\Phi(P)^{-1})\leq\log(\phi^{-1})+O(h).
 \tag{9}
```

The recursive virtual-hierarchy proof already allows an arbitrary
stated host degree at its root. Its local short-path, spectral,
coarse-merge, and one-root-embedding bounds have FIXED polynomial
dependence on that degree. At every nonroot cut-player call the
host remains a union of O(log m) matchings, independently of which
fiber construction was used at the physical root.

Consequently the proof in
[virtual-expander-hierarchy-reconstruction.md](virtual-expander-hierarchy-reconstruction.md)
retains a fixed inverse-phi power and a factor U^{O(p)}.
The physical root's extra polynomial in U occurs once, not once
per depth. Its virtual graph degree stays polynomial in U.
The leaf test and all token-rounding size inequalities use actual
vertex counts and are unaffected except for fixed constants.

Applying that general-degree proof to P, the preprocessing and
query bounds remain

```math
\begin{aligned}
 P_{\rm work}&\leq
       m\exp O(U/p+ph+\log\phi^{-1})\mathrm{poly}(U),\\
 Q_{\rm quality}&\leq\exp O(ph+\log\phi^{-1}),\\
 Q_{\rm work}&\leq mD Q_{\rm quality}\mathrm{poly}(U).
 \end{aligned}
 \tag{10}
```

The extra O(U) host-edge volume, O(U) maximum degree, and O(h)
inverse-conductance logarithm are all included in (10).
No exponent depends on p in an uncharged polynomial degree.

This gives an elementary finite construction for every actual
incidence inventory. It reduces a local source dependency; it does
not establish the remaining hierarchy, dynamic, numerical-client,
or matching proof obligations by itself.
