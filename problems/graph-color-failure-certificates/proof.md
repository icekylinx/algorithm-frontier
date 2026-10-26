# Exact colored-graph certificates

## 1. Sharp vertex-color theorem

Fix an undirected graph with signed rational weights and permanent edge-ID tie breaking. Every vertex has one color. For each original component $`C`$, let $`n_C,q_C`$ count its vertices and colors, and put $`k_C=\min\{h+1,q_C\}`$. Deterministic polynomial preprocessing retains at most
```math
\sum_C\left(n_Ck_C-\binom{k_C+1}{2}\right)
```
original edges, preserving the connectivity partition of every surviving ordered prefix after any at most $`h`$ color failures. It therefore contains the exact canonical minimum spanning forest. The bound is worst-case sharp.

## 2. Activation lemma

Suppose vertex vectors $`z_v\in\mathbb F^t`$ span the space, and each query has a linear functional $`\ell_F`$ with $`a_v=\ell_F(z_v)\ne0`$ exactly at surviving vertices. Orient an edge $`uv`$ and give it block column
```math
b_{uv}[u]=z_v,\qquad b_{uv}[v]=-z_u.
```
Retain the fixed-order greedy basis.

**Proof of prefix preservation.** Map block $`x`$ at vertex $`u`$ to $`a_u\ell_F(x)e_u`$. The edge maps to $`a_ua_v(e_u-e_v)`$, zero on failures and a nonzero multiple of its incidence column otherwise. Applying this map to every prefix-span relation proves equality of surviving incidence-prefix spaces. Canonical Kruskal thus accepts the same original edges. $`\square`$

**Proof of the size bound.** Every symmetric $`t`$-by-$`t`$ matrix $`S`$ gives a row dependency $`(Sz_v)_v`$, because
```math
z_u^\top Sz_v-z_v^\top Sz_u=0.
```
The map from $`S`$ is injective since the $`z_v`$'s span. These dependencies have dimension $`\binom{t+1}{2}`$, so the lift has rank at most $`nt-\binom{t+1}{2}`$. This also works in characteristic two. $`\square`$

In a component use $`z_c=(1,a_c,\ldots,a_c^{k_C-1})`$ at distinct color points. Vandermonde independence gives full span. Unless every color fails, $`\prod_{c\in F\cap C}(T-a_c)`$ has degree at most $`k_C-1`$ and supplies the functional. If all fail, the component is empty. Apply the lemma componentwise.

For sharpness, take a clique on $`k`$ distinctly colored core vertices with weight one and join every outer vertex to each core vertex with weight two. Deleting all other cores forces each outer edge; retaining only a pair of cores forces its clique edge in the minimum forest. The number forced is $`nk-\binom{k+1}{2}`$, the classical Sorkin–Steger–Zenklusen example.

## 3. List and mixed extensions

For vertex lists of degree $`d_v`$, use coefficient monomials of the padded label-root polynomials through total degree $`h`$. If their actual rank is $`t`$, the same lemma gives
```math
nt-\binom{t+1}{2},\qquad
t\le\min\left\{n,\binom{h+d_v}{d_v}\right\}.
```
When that feature dimension is gated out, retain the cheapest edge of every parallel class and claim the parameter envelope at $`t=n`$; the actual-rank refinement requires computing the features.

With extra edge lists of degree $`d_e`$, put the feature of $`g_vg_e`$ at endpoint $`u`$, and its opposite-endpoint analogue at $`v`$. Multiplying each block evaluation by its own vertex factor yields the same scalar on the incidence column, nonzero exactly for surviving edges. The bound is
```math
n\binom{h+d_v+d_e}{d_v+d_e}.
```
For one color per vertex and edge, symmetric trilinear forms subtract
```math
\binom{h+3}{3}-\binom{h-t+3}{3}
```
from $`n\binom{h+2}{2}`$, where $`t`$ is the vertex-color-vector rank in dimension $`h+1`$. With full rank this gives $`n\binom{h+2}{2}-\binom{h+3}{3}`$. The complete proof gives the dependency injection and lower examples.

## 4. One failed color in near-linear preprocessing time

Let $`T_0`$ be the canonical original forest, $`D_c`$ the edges destroyed by color $`c`$, and $`T_c`$ the forest after its failure. Every surviving baseline edge remains accepted by Kruskal, since deletion cannot connect its endpoints earlier. Thus
```math
T_c=(T_0\setminus D_c)\mathbin{\dot\cup}R_c,\qquad
|R_c|\le|T_0\cap D_c|.
```
With $`a=2d_v+d_e`$ and $`r=|T_0|`$, summing gives $`\sum_c|R_c|\le ar`$. A deterministic dynamic MSF structure with exchange reporting can delete and restore each color batch while maintaining the nonbaseline forest in a dictionary. Enumerate it only at completed batches.

If $`A\le am`$ is the edge/color incidence count, this costs
```math
O\bigl((m+A)(\log^4(n+2)+\log(m+2))+ar\bigr),
```
plus input organization. The output is the exact union of canonical forests and inherits the algebraic support bounds. Indexed cost lookup is $`O(1)`$; full output additionally scans the baseline and writes the result. Exchange reporting is an explicit backend requirement.

## Complete proof

[Activation, mixed/list bounds, sharpness, and MSF implementation](manuscripts/colored-graph-and-vertex-failure-certificates.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
