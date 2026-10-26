# Exact persistent homology under correlated failures

## 1. Theorem

Let a finite complex have top dimension $p\ge1$, $N$ top simplices, and top boundary matrix $A$ of rank $r$ over the rationals or an explicitly represented finite field. Each vertex has at most $a$ failure labels; each top simplex has at most $b$ extra labels. At most $h$ labels fail, removing their vertices and cofaces and their labeled top simplices.

A deterministic uniformly polynomial construction retains at most
$$
\min\left\{N,r\binom{h+a+b}{a+b}\right\}
$$
original top simplices, together with the full original lower skeleton. For one supplied filtration, the inclusions induce isomorphisms of persistence modules in all degrees at most $p-1$, after every allowed failure. A separate cost-ordered construction contains every canonical minimum-cost surviving boundary basis. Independent filtration and cost orders require separate constructions.

## 2. Incidence lemma

Give each row $i$ a label set $R_i$, each column $e$ a label set $C_e$, and assume
$$
A_{ie}\ne0\Longrightarrow R_i\subseteq C_e,\qquad |C_e\setminus R_i|\le d.
$$
At most $r\binom{h+d}{d}$ columns suffice to preserve every surviving span at every prefix of one specified order.

**Proof.** Assign distinct nonzero field points $x_\lambda$ and define $g_S(T)=\prod_{\lambda\in S}(1-T/x_\lambda)$. For deficit $\Delta=C_e\setminus R_i$, list all degree-at-most-$h$ monomials $\Phi(\Delta)$ in its at most $d$ nonconstant coefficients. Failure evaluation $\prod_{\lambda\in F}g_\Delta(x_\lambda)$ is a linear functional $\ell_F$ of them.

Select $r$ independent original rows; their projection $\pi$ is injective on the full column span. Lift column $e$ to blocks $A_{ie}\Phi(C_e\setminus R_i)$ and retain an ordered greedy basis. At a query, apply $\ell_F$ in block $i$, multiplied by $\prod_{\lambda\in F}g_{R_i}(x_\lambda)$. The column image is
$$
\left(\prod_{\lambda\in F}g_{C_e}(x_\lambda)\right)\pi(A_e).
$$
It vanishes exactly on failed columns. Apply the map to prefix-span relations and use injectivity of $\pi$. The dimension is $r\binom{h+d}{d}$, proving the lemma. $\square$

The dimension gate returns the input before a larger-than-input lift is enumerated. Rational and finite-field implementations use exact polynomial-bit arithmetic as specified in the complete proof.

## 3. Homology and naturality

For a facet $\tau\subset\sigma$, use its vertex-label union as $R_\tau$, and all vertex and own top labels as $C_\sigma$. The deficit contains labels of only the missing vertex and the top labels, so it has size at most $a+b$.

At each surviving filtration state, the lemma gives the same top-boundary image. All chain groups through dimension $p-1$, lower coordinates, and lower boundary maps are literally identical. Their cycle spaces and boundary quotients therefore agree. These coordinate identifications commute with filtration inclusions, proving persistence modules rather than only Betti numbers. Compatible relative complexes and zigzag sequences of allowed inclusion states follow identically.

The lower skeleton is retained, and the chosen coefficient field matters. Top-dimensional homology, integral torsion, and homotopy type are outside the claim.

## 4. Exterior refinements and sharpness

With one color per vertex and no extra top labels, let $\ell$ count colors and $k=\min\{h+1,\ell\}$. Count one additional never-failing color for safe vertices. Then
$$
|H_p|\le\min\left\{N,kr,\binom n{p+1}-\binom{n-k}{p+1}\right\}.
$$
Use contractions by the covectors with values $1,a_c,\ldots,a_c^{k-1}$ at a vertex of color $c$. Failure-polynomial evaluation annihilates failed columns. Each contraction block is a diagonal rescaling of the boundary and has rank $r$; stacking gives $kr$. Their common kernel on the complete exterior universe is $\bigwedge^{p+1}W$, where $W$ is the common kernel of the $k$ independent covectors. Rank-nullity gives the binomial difference.

For sharpness, filter the complete top skeleton by the minimum vertex of each simplex, and fail the earlier singleton-colored vertices. Each surviving star at its birth is an independent cone basis. The union of these states forces exactly the top simplices meeting the first $k$ vertices.

For overlapping vertex labels without extra top labels, replace $k$ by the actual coefficient-feature rank $s$. The same contraction argument gives $sr$ and the binomial difference at $s$. A labeled-cone construction makes the general coefficient $\binom{h+a+b}{a+b}$ asymptotically necessary.

## Complete proofs

[Exact persistence, envelopes, and lower bounds](manuscripts/correlated-fault-boundary-and-persistence-sparsifiers.md); [separate fixed-weight real spectral theorem](../correlated-spectral-regression/manuscripts/graded-incidence-and-simplicial-spectral-sparsification.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
