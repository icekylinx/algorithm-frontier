# Two limitations on substituting sparsification primitives

This note isolates two mathematical scope checks used in developing the
separated static construction. Neither statement is a lower bound for
general-graph matching or for a suitably designed ambient-aware sparsifier.

## 1. Own-graph congestion does not preserve ambient congestion additively

For every integer $`r\geq2`$, let the demand graph $`J`$ consist of $`r`$
disjoint cliques, each on $`r+1`$ vertices. In each clique choose a center
$`c`$ and a distinguished leaf $`a`$. Embed the distinguished edge
$`ca`$ by the two-edge ambient path $`cxa`$, using the SAME new
ambient vertex $`x`$ for all cliques. Embed every other demand edge
$`uv`$ through its own private new middle vertex $`z_{uv}`$.

Every input path has length two. Each original vertex belongs to
exactly $`r`$ input paths, $`x`$ belongs to exactly $`r`$ input
paths, and each private middle vertex belongs to one. Thus
```math
L_0=2,\qquad C_0=r,\qquad\Delta(J)=r.
```

Choose as the sparse subgraph the star centered at $`c`$ in each
clique. Route each clique edge along its unique star path. These
routes have length at most two and own-graph edge congestion at
most $`r=\Delta(J)`$. Nevertheless, in each clique all $`r`$
demands incident to $`a`$ use the distinguished spoke. After
composing with the original ambient paths, all of them use $`x`$.
The composed ambient congestion at $`x`$ is therefore
```math
r^2.
```

Consequently, a guarantee consisting only of constant path length,
linear-size selected support, and own-graph edge congestion
$`O(\Delta(J))`$ does not imply ambient vertex congestion
$`O(L_0(C_0+\Delta(J)))`$. The ordinary composition inequality
multiplies own-graph edge congestion by the old ambient congestion;
it does not turn the product into a sum.

This is a counterexample to that inference, not to existence of a
better selected subgraph. A construction that sees the ambient
embedding can make different choices. In particular, it does not
rule out using a newer own-graph primitive together with a new
ambient-aware selection argument.

The literal ambient guarantee used in the current construction is
[van den Brand et al., arXiv:2309.16629v1, Theorem 8.1](https://arxiv.org/pdf/2309.16629v1):
it explicitly retains the factor $`L_0`$ multiplying
$`C_0+\Delta(J)`$. The source-to-source discrepancy between this
statement and a length-free restatement is recorded separately in
[the static-base note](short-period-static-spanner-base.md).

## 2. A conservative old parameter guard can itself limit a balance

Suppose an older instantiation enforces the finite guard
```math
K^7\leq\log m
```
at every nonbase recursive instance. Let the smallest nonbase
logarithmic size be of order $`x=\log k`$. On the power scale,
write $`K=U^t`$ and $`x=U^z`$. The guard requires
```math
7t\leq z.
```
If recursive update propagation still charges
$`(U/x)(U/K)`$, fitting this term into logarithmic overhead
$`U^z`$ requires
```math
z\geq2-z-t,
 \qquad\text{or}\qquad t\geq2-2z.
```
Together these imply $`z\geq14/15`$, irrespective of whether
some separate output factor has been improved.

This observation applies only to that guarded instantiation.
It is not an intrinsic restriction of deterministic routing.
The new
[explicitly clocked short-period construction](amortized-static-base-distance-sparsifier.md)
reconstructs its repairs and amortized feedback directly, and does
not import this unrelated guard. Its own static-call parameter
conditions are checked in
[the separated parameter note](separated-static-sparsifier-parameters.md).

## 3. What the new separation changes

The new proposal neither replaces ambient congestion by
own-graph congestion nor deletes the input-path-length factor.
It proves a smaller output envelope $`\Gamma`$ while allowing
a larger construction-work envelope $`F`$. Only $`\Gamma`$
enters the route-length and route-congestion recurrence; $`F`$
is charged as local work. This is a different change from the
two invalid substitutions excluded above.

Its prospective $`6/7`$ balance is a separate conditional
composition. The model-optimality calculation is in
[the parameter-balance note](backend-exponent-balance.md), and
the complete numerical and matching obligations are recorded in
[the conditional matching composition](conditional-matching-6-7-composition.md).
