# Exact minimum-spanning-forest certificates under correlated color failures

**Abstract.** We give a deterministic polynomial-time construction of exact minimum-spanning-forest certificates for correlated vertex and edge failures. The certificate preserves every prefix of one fixed weight order. Vertex colors admit the sharp componentwise bound below; mixed colors and overlapping lists admit incidence-sensitive extensions.

The main theorem gives a deterministic polynomial-time construction of an exact weighted certificate for arbitrary vertex color classes, with the sharp bound

```math
|E(H)|\le \sum_{C}\left(n_C k_C-\binom{k_C+1}{2}\right),
  \qquad k_C=\min\{h+1,q_C\}.
\tag{G1}
```

Here a query deletes at most $`h`$ colors, a color can occur on arbitrarily many vertices, and $`C`$ ranges over the original connected components, with $`n_C`$ vertices and $`q_C`$ colors. The certificate contains the canonical minimum spanning forest after **every** allowed query. All edge weights may be signed, and ties are resolved by fixed original edge IDs.

The ordinary individual-vertex-failure specialization, including its sharp constant and extremal example, is already due to Sorkin--Steger--Zenklusen. The extension here treats the extension to arbitrary correlated color classes with a polynomial construction. The algebraic matrix is a specialization of Kalai's hyperconnectivity matrix; we claim no invention of that matrix. Sections 6--8 give mixed-color and overlapping-list extensions.

## 1. Model and precise output

The input is an undirected graph, optionally with parallel edges. Each vertex has one color. Each original edge has a fixed signed rational weight and a distinct permanent ID. The graph need not be connected. Loops may be deleted because they never belong to a forest.

A failure set $`F`$ removes every vertex whose color belongs to $`F`$, together with all incident edges. We require $`|F|\le h`$. All retained edges keep their original endpoints, weights, and IDs.

The returned subgraph $`H`$ has the following stronger property: for every failure set and every prefix of the total edge order `(weight, ID)`, the surviving prefix of $`H`$ has the same connected-component partition as the surviving prefix of the original graph. Consequently the canonical Kruskal forest is literally the same on both graphs.

This is an exact forest and connectivity guarantee. It is not a metric-spanner stretch guarantee, and the retained-edge bound is not an auxiliary-workspace bound.

## 2. A general linear-activation lemma

Let every vertex $`v`$ have a vector $`z_v\in\mathbb F^t`$, with the vectors spanning $`\mathbb F^t`$. Suppose every allowed query $`Q`$ has a common linear functional $`\ell_Q`$ such that

```math
a_v(Q):=\ell_Q(z_v)\ne0
  \quad\Longleftrightarrow\quad
  v\text{ survives }Q.
\tag{G2}
```

Orient each edge arbitrarily. Define its lifted column by

```math
b_{uv}[u]=z_v,\qquad b_{uv}[v]=-z_u,
 \qquad b_{uv}[w]=0\ (w\notin\{u,v\}).
\tag{G3}
```

Take the greedy column basis of this matrix in the fixed edge order. Let $`H`$ be its original edge set.

For a fixed query, define a linear row map blockwise by

```math
x\text{ in block }u\ \longmapsto\
        a_u(Q)\ell_Q(x)e_u.
\tag{G4}
```

It sends $`b_{uv}`$ to

```math
a_u(Q)a_v(Q)(e_u-e_v).
\tag{G5}
```

For a failed edge endpoint this is zero; otherwise it is a nonzero scalar multiple of the ordinary incidence column. Since a greedy basis spans every ordered prefix of its full input matrix, applying (G4) shows that the two surviving incidence-prefix spaces agree. Graphic rank and connectivity therefore agree at every ordered prefix. In particular every edge accepted by canonical Kruskal occurs in $`H`$, proving the claimed exact forest guarantee.

There is also a rank saving. For every symmetric $`t\times t`$ matrix $`S`$, the block row vector $`(Sz_v)_v`$ annihilates (G3), because

```math
z_u^TSz_v-z_v^TSz_u=0.
\tag{G6}
```

The map from $`S`$ to this row vector is injective: the $`z_v`$'s span the whole space. Thus there are $`\binom{t+1}{2}`$ independent row dependencies, and

```math
|E(H)|\le nt-\binom{t+1}{2}.
\tag{G7}
```

The same proof works componentwise and with any exact finite field, including characteristic two. This explicit specialized matrix need not represent the generic hyperconnectivity matroid. No generic-matroid independence algorithm or polynomial-identity-testing assertion is used.

## 3. Arbitrary vertex color classes

Assign distinct field elements $`a_c`$ to the colors. In a component with $`q`$ colors, use

```math
k=\min(h+1,q),\qquad
   z_c=(1,a_c,a_c^2,\ldots,a_c^{k-1}).
\tag{G8}
```

At least $`k`$ distinct color vectors occur and span the whole space by the Vandermonde determinant. A query that removes all component colors leaves an empty graph and is automatic. Otherwise, let $`F_C`$ be the failed colors occurring in the component and put

```math
p_{F_C}(T)=\prod_{c\in F_C}(T-a_c).
\tag{G9}
```

Its degree is at most $`\min(h,q-1)\le k-1`$. Its coefficient vector defines a linear functional on (G8), nonzero exactly at the surviving colors. Apply Section 2. This proves (G1) and the ordered-prefix guarantee.

A useful special case has $`q\ll h`$: the bound depends on $`q`$, not the larger failure allowance. A one-color connected component needs only its ordinary minimum spanning tree.

## 4. Polynomial construction, query work, and representation

For a static component choose any prime exceeding its number of colors, assign distinct residues, form the explicit columns, and run exact finite-field elimination in edge order. A prime of polynomial magnitude can be found by a deterministic polynomial procedure; rational Vandermonde arithmetic is an alternative. The cost sorting uses the original rational weights and IDs, independently of the finite field.

With $`R=\sum_C n_Ck_C`$, elementary incremental elimination takes $`O(mR^2)`$ field operations after sorting, with $`O(R^2)`$ field elements of workspace. This deliberately conservative bound is sufficient for deterministic uniform polynomial preprocessing. Sparse or faster linear algebra can improve it but is not part of this manuscript's guarantee.

For a query, delete the failed-color vertices from the retained ordered edge list and run Kruskal. The query processes only the certificate and the failure description. The original graph's canonical forest is returned exactly, including the same original edge IDs. Every ordered threshold connectivity relation, and hence every pair's bottleneck-path value, is preserved as well.

The statement is about the number of retained original edges. It does not claim linear preprocessing time or $`O(nh)`$ total arithmetic workspace. Arbitrary later changes to the edge cost order are outside the theorem.

## 5. Sharpness inherited from ordinary vertex failures

Let $`k=\min(h+1,n)`$, give all vertices distinct colors, make a clique on $`k`$ core vertices with weight 1, and join each other vertex to every core vertex with weight 2. The graph has

```math
k(n-k)+\binom{k}{2}
        = nk-\binom{k+1}{2}
\tag{G10}
```

edges. Every outer-to-core edge is compulsory after the other $`k-1`$ core vertices fail. Every core edge is compulsory in a minimum forest after the other $`k-2`$ core vertices fail: omitting the weight-1 core edge requires an additional weight-2 edge or loses connectivity. The cases $`k=1`$ and $`k=n`$ obey the same formula with empty edge classes interpreted naturally.

This is the standard extremal construction already given after Theorem 1 in Sorkin--Steger--Zenklusen. It certifies that (G1)'s worst-case coefficient cannot improve even in the ordinary-vertex special case. It is not a new lower-bound construction, nor a lower bound for arbitrary compressed encodings.

## 6. Mixed vertex and edge colors

Now both vertices and edges have one color from the same palette. A failed color removes its vertices and all edges carrying that color. The total number of failed colors is at most $`h`$.

The lifted block below depends on the edge as well as on the endpoint, so it
uses the following direct extension of Section 2. For an oriented edge $`uv`$,
let its block at $`u`$ be $`x_{u,e}`$, its block at $`v`$ be
$`-x_{v,e}`$, and suppose a query functional $`L_F`$ evaluates these blocks
to the survival factors of the opposite endpoint and of the edge. Multiplying
the $`u`$-block by the survival factor of $`u`$, and the $`v`$-block by that
of $`v`$, sends the lifted column to a nonzero scalar times the ordinary
incidence column exactly when the edge survives, and to zero otherwise. The
same prefix-span argument as in Section 2 applies to the greedy basis of this
edge-dependent matrix. Its row count is $`n`$ times the block dimension; no
vertex-only vector $`z_v`$ is assumed in this variant.

For each endpoint/edge pair define the monic quadratic

```math
g_{v,e}(T)=(T-a_{c(v)})(T-a_{c(e)}).
\tag{G11}
```

Let $`\phi(v,e)`$ list every monomial of total degree at most $`h`$ in its two nonleading coefficients. Its dimension is

```math
D=\binom{h+2}{2}.
\tag{G12}
```

Lift $`e=uv`$ to block $`\phi(v,e)`$ at $`u`$ and block $`-\phi(u,e)`$ at $`v`$. For a failure set $`F`$, the expression

```math
\prod_{c\in F}g_{v,e}(a_c)
\tag{G13}
```

is a linear functional $`L_F`$ of the feature vector, because it is a polynomial of degree at most $`|F|\le h`$ in the two coefficients. With $`p_F(T)=\prod_{c\in F}(T-a_c)`$, its value is $`p_F(a_{c(v)})p_F(a_{c(e)})`$. Apply $`p_F(a_{c(u)})L_F`$ at the block of vertex $`u`$. Each edge column maps to

```math
p_F(a_{c(u)})p_F(a_{c(v)})p_F(a_{c(e)})(e_u-e_v).
\tag{G14}
```

This is nonzero precisely for a surviving edge. The edge-dependent activation
argument above therefore gives an exact weighted certificate with at most

```math
n\binom{h+2}{2}
\tag{G15}
```

edges, in deterministic polynomial time. Repeated colors at the two endpoints or on the edge cause repeated factors but no problem. In a static instance one can cap $`h`$ at the number of occurring colors minus one, since removing every occurring color leaves no vertices.

### A symmetric-cubic rank refinement

Put $`k=h+1`$. The feature functions in (G11)--(G12) span exactly the symmetric bivariate polynomials whose degree in each variable is at most $`h`$. Indeed, the elementary-symmetric basis $`(x+y)^a(xy)^b`$, $`a+b\le h`$, and the symmetric-monomial basis $`x^iy^i`$, $`x^iy^j+x^jy^i`$, $`0\le i<j\le h`$, span the same $`D`$-dimensional space. The recurrence for $`x^m+y^m`$ proves this without division.

Write $`z_x=(1,x,\ldots,x^h)`$. Every symmetric trilinear form $`S`$ gives a row dependency by putting the coefficients of $`S(z_{c(u)},\cdot,\cdot)`$ in the block of $`u`$. On edge $`uv`$, the two contributions are $`S(z_u,z_v,z_e)`$ and $`-S(z_v,z_u,z_e)`$, so they cancel.

If the occurring vertex vectors span $`t`$ dimensions, this supplies

```math
\binom{k+2}{3}-\binom{k-t+2}{3}
\tag{G16}
```

independent row dependencies. The map from symmetric trilinear forms to these
row dependencies has kernel consisting of forms on the quotient by the
vertex-vector span; an arbitrary sparse input graph may have additional row
dependencies. Thus (G15) can be reduced by (G16), componentwise. In
particular, with at least $`h+1`$ distinct vertex colors the bound is

```math
n\binom{h+2}{2}-\binom{h+3}{3}.
\tag{G17}
```

No exact optimum for all mixed instances is asserted.

### Leading-order mixed lower bound for multigraphs

Let $`q=h+2`$ core vertices have colors $`1,\ldots,q`$, and let all other vertices have color 0. For every outer vertex and pair $`a<b`$ in $`[q]`$, put an edge to core $`a`$ with edge color $`b`$. Add the core clique, with edge color 0. Give all edges unit weight.

For a fixed pair $`a<b`$, fail every color of $`[q]\setminus\{a,b\}`$. Each
outer vertex now has exactly its edge indexed by $`\{a,b\}`$, attached to
core $`a`$; the surviving core clique may still contain cycles, but every
outer vertex has degree one. Hence that surviving outer edge is compulsory
for connectivity. Every original edge is compulsory under one of these
queries.

Therefore these multigraphs need

```math
\binom{h+2}{2}(n-h-1)
\tag{G18}
```

retained edges, even for unweighted connectivity. This matches the leading term in (G15) when $`n/h`$ tends to infinity. Parallel edges are used; this is not a simple-graph lower bound as written.

## 7. Overlapping lists of vertex colors

Let vertex $`v`$ carry an arbitrary set $`\sigma(v)`$ of at most $`d`$ colors, and fail whenever $`\sigma(v)\cap F\ne\varnothing`$. Color classes can overlap arbitrarily. Reduce an oversized encoded $`d`$ to the largest list actually supplied; cap $`h`$ at the number of occurring colors. For $`h=0`$, the ordinary minimum spanning forest already suffices. Choose an extra code $`a_0`$ never queried and set

```math
g_v(T)=(T-a_0)^{d-|\sigma(v)|}
                \prod_{c\in\sigma(v)}(T-a_c).
\tag{G19}
```

Let $`z_v`$ consist of all monomials of degree at most $`h`$ in the $`d`$ nonleading coefficients of $`g_v`$. Its length is

```math
D_v=\binom{h+d}{d}.
\tag{G20}
```

For every query, $`\prod_{c\in F}g_v(a_c)`$ is a linear functional of $`z_v`$ and is nonzero exactly when $`v`$ survives. Apply the general linear-activation lemma. If the vertex feature vectors have rank $`t`$, the retained size is

```math
nt-\binom{t+1}{2},
          \qquad t\le\min(n,D_v).
\tag{G21}
```

In particular the simple bound is $`n\binom{h+d}{d}`$, rather than using the union of both endpoint lists and paying $`n\binom{h+2d}{2d}`$ in a direct per-edge feature lift. That comparison is to the direct lifting construction, not a claim that the latter is the best published list-model algorithm.

For uniform polynomial construction when $`h,d`$ are binary parameters, first test whether $`D_v\ge n`$. In that case keep only the cheapest ordered edge of each parallel class and return that simple graph. It has at most $`\binom n2`$ edges, within (G21)'s upper envelope at $`t=n`$, and preserves every query because parallel edges have identical endpoint failure conditions. When $`D_v<n`$, the explicit feature matrix is polynomial in the input, including all coefficient calculations. The actual-rank refinement (G21) is claimed when the features are computed; the identity branch only claims the displayed parameter upper envelope with $`t=\min(n,D_v)`$.

### Leading-order list lower bound on simple graphs

Let $`D_v=\binom{h+d}{d}`$, $`n\ge D_v`$, and make one core vertex for each $`d`$-subset $`S`$ of $`[h+d]`$. Give that vertex exactly the labels $`S`$. The other $`n-D_v`$ vertices have no labels. Take the complete bipartite graph between these two groups, with unit weights.

Fail $`[h+d]\setminus S`$, a set of $`h`$ labels. The sole surviving core vertex is the one indexed by $`S`$, so its entire star is compulsory. Varying $`S`$ shows that every one of the

```math
D_v(n-D_v)
\tag{G22}
```

edges must be retained. Thus the leading $`nD_v`$ dependence is unavoidable on simple graphs when $`n/D_v`$ tends to infinity. This is a retained-subgraph lower bound.

The color-lists model itself is already present in the January 2026 journal version of *Color Fault-Tolerant Spanners*. Its full list-model parameter comparison needs a final source check; this manuscript does not claim to introduce overlapping-color failures.

## 8. Vertex lists together with edge lists

Suppose vertex lists have size at most $`d_v`$, edge lists at most $`d_e`$, and a single failure set of at most $`h`$ colors removes an object when any of its listed colors fails. Use separately padded monic polynomials $`g_v`$ and $`g_e`$. For edge $`uv`$, put the coefficient-monomial features of $`g_vg_e`$ at block $`u`$, and the negative features of $`g_ug_e`$ at block $`v`$.

The degree of either product is $`d_v+d_e`$, so the block dimension is

```math
D_{v,e}=\binom{h+d_v+d_e}{d_v+d_e}.
\tag{G23}
```

The failure-evaluation functional, multiplied at $`u`$ by $`\prod_{c\in F}g_u(a_c)`$, maps an edge column to the nonzero surviving scalar

```math
\prod_{c\in F}g_u(a_c)g_v(a_c)g_e(a_c)\,(e_u-e_v).
\tag{G24}
```

Hence a cost-ordered basis retains at most $`nD_{v,e}`$ edges and gives the same exact weighted-prefix guarantee. The apparent duplication of a shared color only raises its factor's multiplicity; zeros still encode the union of all three failure lists.

For a uniform polynomial static construction, if $`nD_{v,e}\ge m`$, simply retain the input. Otherwise $`D_{v,e}<m`$, and, for $`h\ge1`$, $`d_v+d_e<D_{v,e}`$; explicit polynomial construction and feature enumeration are polynomial in the input. When $`h=0`$, retain the ordinary minimum spanning forest. When $`d_v+d_e=0`$, there are no relevant failures and the same branch applies. An oversized encoded list bound can first be reduced to the maximum list length actually present.

### Matching leading coefficient already on simple graphs

The apex construction in the accompanying boundary-lift manuscript also gives a simple-graph lower bound for (G23). Put $`q=\binom{h+d_v+d_e}{d_v+d_e}`$, take a palette of $`h+d_v+d_e`$ colors, and create one apex $`x_S`$ for each $`(d_v+d_e)`$-subset $`S`$ of the palette. Split $`S=A_S\mathbin{\dot\cup}B_S`$, with $`|A_S|=d_v`$, $`|B_S|=d_e`$. Give $`x_S`$ vertex list $`A_S`$. Add $`t`$ base vertices with empty lists, join every apex to every base vertex, and give all edges incident to $`x_S`$ edge list $`B_S`$. All weights are one.

For the query $`F=\text{palette}\setminus S`$, an apex-to-base edge at $`x_{S'}`$ survives exactly when $`S'\cap F=\varnothing`$, hence exactly when $`S'=S`$. Some other apex vertices may themselves survive, but they are isolated. The unique nontrivial surviving component is therefore the star centered at $`x_S`$, and every one of its $`t`$ edges is compulsory even for connectivity. Varying $`S`$ forces all $`qt=q(n-q)`$ original edges into any certificate. Thus the leading coefficient $`D_{v,e}`$ in (G23) is sharp on simple graphs as $`n/D_{v,e}`$ tends to infinity. Taking $`d_v=d_e=1`$ also supplies a simple-graph leading-order lower bound for Section 6; its finite additive term differs from the multigraph example there.

## 9. Near-linear construction and a difference oracle for one failed color

This is a separate low-time corollary for $`h=1`$. It applies to the overlapping vertex/edge lists of Section 8, and avoids the large matrix elimination. Let

```math
a=2d_v+d_e,
       \qquad r=|T_0|\le n-1,
\tag{G25}
```

where $`T_0`$ is the canonical original minimum spanning forest. Interpret the list union on an edge as the colors whose individual failure destroys that edge. Count each edge/color incidence once; the total number $`A`$ of these incidences satisfies $`A\le am`$.

For every occurring color $`c`$, let $`D_c`$ be its destroyed edges, let $`T_c`$ be the canonical forest of $`G-D_c`$, and define $`R_c=T_c\setminus T_0`$. Then

```math
T_c=(T_0\setminus D_c)\mathbin{\dot\cup}R_c,
       \qquad |R_c|\le |T_0\cap D_c|.
\tag{G26}
```

To see the containment, a surviving edge of $`T_0`$ increased the rank of its original ordered prefix. Deleting other edges cannot connect its endpoints in that prefix, so it is still accepted by Kruskal. The size bound follows because deleting edges cannot increase graphic rank. Summing (G26),

```math
\sum_c |R_c|\le ar.
\tag{G27}
```

Use the deterministic fully dynamic MSF structure of Holm--de Lichtenberg--
Thorup, with $`O(\log^4 n)`$ amortized update time and an implementation
interface that reports the forest exchanges. Initialize the full graph. For
each color, delete the edges of $`D_c`$, record the current forest edges
outside $`T_0`$, and restore the same edges. Track the current non-$`T_0`$
forest in a dictionary using the reported forest insertions and deletions.
Only the dictionary at a completed color-deletion batch is enumerated.
Intermediate forests are not added to the output. If a chosen dynamic MSF
implementation exposes only the maintained forest and not exchange events,
the same corollary requires an explicit augmentation to report those events.

There are $`m+2A`$ original edge updates including initialization, and the total enumeration work is $`O(ar)`$ by (G27), rather than one full forest per color. Parallel edges can be handled with a priority queue for each endpoint pair: a change of its cheapest surviving edge induces at most a constant number of simple-graph MSF updates and $`O(\log(m+2))`$ additional work. IDs break all weight ties permanently.

Thus, after forming the color-incidence lists, the update and forest-recording work is

```math
O\!\left((m+A)\left[\log^4(n+2)+\log(m+2)\right]+ar\right).
\tag{G28}
```

Input reading and dictionary construction are additional near-linear work in the encoded vertex and edge label incidences. This is deterministic near-linear preprocessing when the maximum list sizes are fixed; arithmetic and comparisons on the given rational costs must be charged in the chosen bit model.

The output $`T_0\cup\bigcup_cR_c`$ is the exact union of the canonical forests for no failure and one failed color. It is a subgraph of every certificate that contains all these canonical forests. Therefore it inherits the sharper bounds proved above: at most $`2n-3`$ edges in a connected single-vertex-color instance with at least two colors; at most $`3n`$ in the mixed single-color instance, or the applicable rank-refined bound. The direct general-list bound $`(a+1)r`$ also follows from (G27).

Store the baseline cost $`w(T_0)`$, each $`R_c`$, and

```math
V_c=w(T_0)-w(T_0\cap D_c)+w(R_c).
\tag{G29}
```

An indexed single-color query returns its exact MSF value in $`O(1)`$ lookup time, or its forest as the baseline-minus-destroyed-edges representation together with $`R_c`$. Writing the entire forest costs its output size plus the baseline scan. All replacement lists together contain at most $`ar`$ edge IDs. Colors destroying no baseline-forest edge have $`R_c=\varnothing`$ and the unchanged value, so they need no nondefault difference record.

This corollary uses standard dynamic MSF machinery and does not claim priority for single-failure sensitivity oracles. It does not replace the all-$`h`$ construction: running these batches for all $`h`$-color subsets would reintroduce color-universe enumeration.

## 10. Related work and comparison

The comparison currently supported by the inspected primary sources is:

| Model | Inspected baseline | This manuscript |
|---|---|---|
| Ordinary individual vertex failures | Sorkin--Steger--Zenklusen: sharp $`nk-\binom{k+1}{2}`$ union bound and polynomial construction | Recovered as a specialization; not a new claim |
| Arbitrary single vertex colors | Petruschka--Sapir--Tzalik: $`O(hn)`$ existence; April 2026 Theorem 4.2 supplies an $`O(hn\log n)`$ polynomially computable connectivity certificate | Deterministic polynomial construction, sharp (G1), and exact fixed-order weighted MSF preservation |
| Mixed single vertex/edge colors | ITCS 2024 gives $`O(h^2n)`$ existence and, via its efficient spanner result at logarithmic stretch parameter, a polynomial $`O(h^2n\log^2 n)`$ connectivity certificate | Deterministic polynomial construction with (G15), optionally (G17); exact weighted MSF preservation |
| Overlapping color lists | Explicitly treated in the 2026 TALG journal version | Explicit (G20)--(G24), with a simple-graph leading-order lower (G22); no claim that the model is new |

PST's weighted construction processes edges in increasing order and discards an edge only after certifying an earlier-edge surviving path for every allowed failure set (ITCS 2024, Section 5, "Handling Weights"). That observation already implies ordered-prefix connectivity and canonical-MSF preservation, although their theorem is phrased as a spanner result. The proposed improvement over that construction is the removal of the logarithmic size losses, together with the explicit sharp vertex-color bound; weighted-MSF preservation by itself is not claimed as a first result.

The algorithm does not require finding a minimum color cut. It computes a basis of an explicitly instantiated matrix. The reachability/forest claims follow from a query-dependent linear image, which is enough even if the lift retains edges that no optimal queried forest actually uses.

The comparisons above distinguish existence from polynomial construction. They do not establish priority against every later journal refinement, a new exponent for ordinary individual failures, or a new metric-spanner bound.

## References

1. Gregory B. Sorkin, Angelika Steger, Rico Zenklusen. *A tight bound on the collection of edges in MSTs of induced subgraphs*. Theorem 1, the following sharpness example, and the polynomial construction following Theorem 5. https://arxiv.org/pdf/0705.2439
2. Asaf Petruschka, Shay Sapir, Elad Tzalik. *Color Fault-Tolerant Spanners*. ITCS 2024, Theorem 3 and the efficient constructions of Section 5. https://drops.dagstuhl.de/storage/00lipics/lipics-vol287-itcs2024/LIPIcs.ITCS.2024.88/LIPIcs.ITCS.2024.88.pdf
3. Asaf Petruschka, Shay Sapir, Elad Tzalik. *Connectivity Labeling in Faulty Colored Graphs*. Distributed Computing 39, Article 14, published 7 April 2026, Theorem 4.2. https://link.springer.com/article/10.1007/s00446-026-00506-1
4. Asaf Petruschka, Shay Sapir, Elad Tzalik. *Color Fault-Tolerant Spanners*. ACM Transactions on Algorithms 22(1), Article 6, January 2026, DOI 10.1145/3750728. Institutional abstract explicitly records the color-lists extension: https://weizmann.elsevierpure.com/en/publications/color-fault-tolerant-spanners-2/
5. Dániel Garamvölgyi, Bill Jackson, Tibor Jordán, Soma Villányi. *Sufficient conditions for bipartite rigidity, symmetric completability and hyperconnectivity of graphs*, arXiv:2511.00298, Section 1 and Lemma 1.1. This source credits Kalai's 1985 matrices and records the hyperconnectivity matrix and generic maximum rank. https://arxiv.org/html/2511.00298v1
6. Jacob Holm, Kristian de Lichtenberg, Mikkel Thorup. *Poly-logarithmic deterministic fully-dynamic algorithms for connectivity, minimum spanning tree, 2-edge, and biconnectivity*. Journal of the ACM 48(4), 2001. The deterministic fully dynamic MSF bound is $`O(\log^4 n)`$ amortized per edge update. Author manuscript copy: https://www.cs.princeton.edu/courses/archive/fall09/cos521/Handouts/polylogarithmic.pdf

The manuscript gives proofs of its algebraic specializations and does not require treating the generic hyperconnectivity matroid as efficiently recognizable.
