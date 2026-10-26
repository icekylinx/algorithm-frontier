# Recursive cycle quality: an exact budget and a product-loss obstruction

**Separate mathematical analysis, 24 October 2026.** This note studies
whether the multiplicative raw-cycle quality loss can be removed just
by combining the exact normalized correction identities. It does not
change the current 4/5 matching candidate or any delivered checkpoint.

There are two conclusions.

1. A global telescoping argument can charge the SUM of the actual
   cumulative routed masses. It need not insert the worst stretch
   bound afresh in its notation.
2. Local stretch bounds alone do not control that sum by the sum or
   maximum of the local stretches. An explicit nested-shortcut
   example has zero-gradient local and composite corrections, but
   its best terminal cycle loses exponentially in the number of
   constant-stretch stages. The obstruction survives degree three,
   positive integer lengths, exact native gradients, and simple
   route normalization.

The example is an obstruction to selecting or averaging the separate
correction and terminal alternatives. It is NOT a lower bound for
general matching, min-ratio cycles, or every implementation of the
specific distance hierarchy. Optimizing arbitrary combinations of
corrections can cancel the long route and recover the original short
cycle; Section 5 identifies exactly what that additional task entails.

## 1. A settled chain of exact route maps

Let
$$
G_0\supseteq G_1\supseteq\cdots\supseteq G_d
 \tag{1}
$$
be nested undirected graphs on native vertex IDs. Edges have fixed
orientations, positive lengths $\ell_e$, and gradients $g_e$;
selected subgraphs retain these labels. For every edge
$e=(u,v)\in E(G_i)$, a route $R_i(e)$ is an explicitly oriented
walk in $G_{i+1}$ from the SAME native $u$ to the SAME native
$v$. Selected edges may use identity routes. Extend $R_i$
linearly to signed edge vectors, and define
$$
D_i(e)=e-R_i(e).
 \tag{2}
$$
Native boundary preservation makes (2) a circulation.

For an original circulation $c_0$, put
$$
c_{i+1}=R_i(c_i).
 \tag{3}
$$
Coalesce coefficients by native edge ID after each operation.
Each $c_i$ remains a circulation. In this nested-subgraph model
all vectors already have literal interpretations in $G_0$, so
there is no ambiguity about lifts or gauges.

The elementary identity from
[../graph-backends/normalized-route-cycle-comparison.md](../graph-backends/normalized-route-cycle-comparison.md)
telescopes to
$$
c_0=\sum_{i=0}^{d-1}\sum_{e\in E(G_i)}
                           (c_i)_eD_i(e)+c_d.
 \tag{4}
$$
Taking the gradient is exact, for arbitrary signed coefficients.
Neither old route tables nor eventual physical aliases are used.

## 2. The cumulative-mass comparison lemma

Define the net mass and the charged raw image mass at stage $i$:
$$
W_i=\sum_e\ell_e|(c_i)_e|,\qquad
 A_i=\sum_e|(c_i)_e|\ell_{\rm raw}(R_i(e)).
 \tag{5}
$$
They satisfy $W_{i+1}\leq A_i$. The correction family in round
$i$ has total positive charge at most $W_i+A_i$.
The terminal circulation has charge $W_d$. Therefore the
complete charge in (4) is at most
$$
{\cal B}(c_0)
                       =\sum_{i=0}^{d-1}(W_i+A_i)+W_d.
 \tag{6}
$$
Identity-route terms are actually zero and may be omitted;
(6) is a convenient upper bound.

If $g^\top c_0>0$, some oriented local correction or terminal
cycle has gradient divided by its positive length at least
$$
\frac{g^\top c_0}{{\cal B}(c_0)}.
 \tag{7}
$$
Indeed, if all those ratios were below $r$, the absolute
numerator of every term in (4) would be below $r$ times its
charge, contradicting (4) with $r=g^\top c_0/{\cal B}$.
Local coefficient decomposition into simple directed cycles
does not worsen that comparison.

One may avoid repeated net cancellation by retaining the full
occurrence expansion of the original edge routes. Let
$\overline W_i$ be the total positive mass of that expanded
representation of $c_i$, before native cancellations. Then
$W_i\leq\overline W_i$, and the occurrencewise charge in
round $i$ is at most
$\overline W_i+\overline W_{i+1}$. Consequently
$$
{\cal B}(c_0)
                  \leq W_0+2\sum_{i=1}^d\overline W_i
 \tag{8}
$$
when the same occurrence representation is used for its
correction decomposition. This version includes multiplicity
and does not cancel different physical copies.

### A sufficient stronger invariant

If a new construction proves
$$
\overline W_i\leq A\,W_0
                    \quad\text{for every }i\leq d
 \tag{9}
$$
for every relevant comparator, then (8) gives loss at most
$1+2dA$. An edgewise bound on every COMPOSED route,
$$
\ell_{\rm raw}(R_{i-1}\cdots R_0(e))\leq A\ell_e,
 \tag{10}
$$
is sufficient for (9), although it can be stronger than needed.
Approximations in the local or terminal cycle solvers would
multiply this bound by their explicit solver loss.

This is a positive, exact interface for removing a product.
It requires a cumulative bound such as (9), not merely the
one-stage inequalities
$$
\ell_{\rm raw}(R_i(e))\leq\delta_i\ell_e.
 \tag{11}
$$
Those only imply
$\overline W_i\leq(\prod_{j<i}\delta_j)W_0$. Inserting
that estimate into (8) restores a product-sized denominator.

The same bookkeeping can be used with lifetime-fixed root
lifts whose physical raw lengths are dominated by their
stored charges. It cannot create a smaller charge than the
actual composed images. A specific vertex-sparsification
construction could supply additional structure; that would
be a new hypothesis beyond (2), (11), and raw domination.

## 3. An explicit simple-graph counterexample

Fix integers $b\geq2$, $d\geq1$, and $N=b^d$. Make
vertices
$$
v_0,v_1,\ldots,v_N,z.
 \tag{12}
$$
Include the oriented base path $v_j\to v_{j+1}$ for
$0\leq j<N$, and a two-edge return path
$v_0\to z\to v_N$. Every edge has length one.

For $i=0,\ldots,d-1$, add the shortcut edges
$$
e_{i,r}:v_{r b^{d-i}}\longrightarrow v_{(r+1)b^{d-i}},
                 \qquad 0\leq r<b^i.
 \tag{13}
$$
All these are distinct genuine edges; their spans are at
least two, so none duplicates a base edge. The return path
uses its fresh vertex $z$. Thus the graph is simple.
It has $O(N)$ edges and vertices.

Assign gradients
$$
\begin{array}{c|c}
 \text{edge}&g_e\\ \hline
 v_j\to v_{j+1}&1\\
 e_{i,r}&b^{d-i}\\
 v_0\to z,\ z\to v_N&0 .
 \end{array}
 \tag{14}
$$
These are integers of at most $O(\log N)$ bits.
On the entire graph excluding the return path, $g$ is
the exact difference of the potential $p(v_j)=j$.

Let $G_i$ retain the base and return paths and all shortcut
levels $i,i+1,\ldots,d-1$. The map $R_i$ replaces
each level-$i$ shortcut by its $b$ consecutive children
at level $i+1$, or by its $b$ base edges at the last
level. It fixes every other edge. Every route is simple and
has stretch at most $b$. Moreover,
$$
g^\top R_i(e)=g_e
                          \quad\text{for every edge }e.
 \tag{15}
$$
Therefore
$$
g^\top D_i(e)=0
                      \quad\text{for all }i,e.
 \tag{16}
$$
All composite corrections $e-R_{d-1}\cdots R_0(e)$
also have zero gradient. Decomposing any of these corrections
into simple cycles cannot reveal a nonzero numerator: each
is supported away from $z$, where (14) is a potential.

### Original optimum versus terminal optimum

The cycle consisting of the top shortcut $e_{0,0}$ and
the reversed return path has length three and gradient $N$.
Its ratio is
$$
\beta_0=N/3.
 \tag{17}
$$
This is the original optimum. A simple cycle that avoids $z$
has gradient zero. Any simple cycle using $z$ consists of
the return path and a $v_0$-to-$v_N$ path in the
nonreturn graph; its gradient has absolute value $N$,
and its length is at least three. General circulations
cannot improve on the best simple cycle.

The final graph $G_d$ is a single cycle, the base path
plus the return path. Every nonzero circulation is a
multiple of it, and its best ratio is exactly
$$
\beta_d=N/(N+2).
 \tag{18}
$$
Consequently the best ratio among ALL separate local
correction cycles and ALL terminal cycles loses the factor
$$
\frac{\beta_0}{\beta_d}
                                      =\frac{b^d+2}{3}.
 \tag{19}
$$
This is exponential in $d$, even for fixed $b=2$.
An additive $O(\sum_i\delta_i)$, a maximum-local-stretch
bound, or a polynomial-in-depth replacement is false under
these interfaces.

For the comparator in (17), its stage-$i$ image uses
$b^i$ shortcuts and the return path. Its net AND raw
mass is $b^i+2$. There is no route self-intersection to
erase and no distinction between physical raw length and
the terminal cycle's net length. The failure is genuine
geometric expansion of the surviving representative.

### 3.1 The usual priced-gradient bound does not remove the example

The obstruction also satisfies $|g_e|\leq\ell_e$, with a
root optimum bounded below by an absolute constant. Set every
edge length to $N$, retain the nonreturn gradients in (14),
and set each oriented return-edge gradient to $-N$.
Then every gradient and length is an $O(\log N)$-bit integer,
and
$$
|g_e|\leq\ell_e\quad\text{for every }e.
 \tag{19a}
$$
The top cycle has numerator $3N$ and length $3N$,
so its ratio is exactly one, which is optimal under (19a).
The final cycle has the same numerator and length
$N(N+2)$, hence ratio $3/(N+2)$. The same loss
$(N+2)/3$ remains. All correction numerators are still zero,
since the return edges use identity routes.

Thus bounding every priced gradient by its length, or requiring
an original comparator of ratio at least $1/2$, does not
justify the proposed additive comparison. This checks those
necessary numerical-client conditions; it does not assert
that every such gradient vector is produced by a particular
matching client's objective trajectory.

## 4. Degree three and strictly positive integer labels

The preceding example has maximum degree $O(d)$. It can
be converted to maximum degree three without changing the
conclusion.

For each vertex $v$, make one leaf for each incident real
edge, and join those leaves by a balanced binary tree.
Unused leaves up to the next power of two may be retained.
Every internal degree is at most three, and every leaf has
one tree edge and at most one real edge. The total number
of vertices remains $O(N)$.

Let $h_f\geq1$ bound all fiber heights, so
$h_f=O(\log(d+2))$, and set $H=8h_f$.
Every original real edge receives length $H$ and its
gradient from (14). Fiber edges have length one and
gradient zero. A route between two leaves in one fiber
has length at most $2h_f$.

Retain every fiber tree at every stage. Replace a removed
shortcut by its $b$ child real edges and the connecting
fiber paths, from the exact old leaf to the exact old leaf.
Its length is at most
$$
bH+2h_f(b+1)\leq2bH,
 \tag{20}
$$
so each stage has stretch at most $2b$. Open-edge
gradient equality (15) still holds. Extend $p(v_j)=j$
constantly over each fiber; every correction remains
supported where $g$ is this exact potential.

The original short cycle has three real edges and at most
three fiber paths. Its length is at most
$$
3H+6h_f\leq4H,
 \tag{21}
$$
so its ratio is at least $N/(4H)$.
After all shortcuts are removed, contracting the fiber
trees gives the single base-plus-return cycle. The terminal
cycle has $N+2$ real edges, so its ratio is at most
$$
N/((N+2)H)\leq1/H.
 \tag{22}
$$
Thus the loss is at least $N/4=b^d/4$.

The graph is simple, every current graph has degree at most
three, every length is a positive integer, and gradients
have $O(\log N)$ bits. Native route endpoints are literal
leaf IDs. The example needs no zero-length edge, frozen
gradient mismatch, invalid alias contraction, or unstable
callback. All real and fiber lifetimes can stay fixed
through the entire settled comparison.

For a degree-three version satisfying (19a) with constant
root ratio, instead choose $H=8h_fN$. Multiply every
nonreturn gradient in (14) by $8h_f$, and give each
oriented return edge gradient $-H$. Fiber gradients
remain zero and fiber lengths remain one. Real gradients
are at most $H$ in magnitude. Every correction still
has zero numerator, and (20) still bounds local stretch.
The top cycle has numerator $3H$, length at most
$3H+6h_f$, and therefore ratio at least $4/5$.
The terminal ratio is at most $3/(N+2)$. The loss
is again $\Omega(N)$, with polynomial magnitudes and
no short-word exception.

## 5. What arbitrary combinations could recover

The example does NOT rule out a procedure that optimizes
COMBINATIONS of candidates. In fact, summing all the
appropriate zero-gradient corrections cancels the long
base route and restores the top shortcut:
$$
\text{top cycle}
    =\text{terminal cycle}
        +\sum_{i=0}^{d-1}\sum_{r=0}^{b^i-1}D_i(e_{i,r}).
 \tag{23}
$$
Every correction has zero numerator, yet their addition
reduces the final net norm from $N+2$ to three.
Positive-charge averaging cannot exploit that cancellation.

More generally, let $Z(G)$ be the circulation space of
a graph. Equation (4) proves the exact spanning identity
$$
Z(G_0)=
   \mathrm{span}\{D_i(e):0\leq i<d,\ e\in E(G_i)\}
                  +Z(G_d).
 \tag{24}
$$
The reverse inclusion holds because all displayed generators
are genuine root circulations. Thus unrestricted optimization
of the root ratio over arbitrary linear combinations of
these generators is EXACTLY the original root min-ratio
cycle optimization problem.

This is an algebraic equality, not a computational lower
bound. It identifies the missing algorithmic task: efficiently
choose a low-norm representative after cancellations among
many ancestor corrections. In the zero-gradient case one
may formulate the special task as
$$
\min_{z\in{\cal K}}\|L(c_d+z)\|_1,\qquad
       {\cal K}=\mathrm{span}\{D_i(e)\}.
 \tag{25}
$$
The numerator is constant on this affine space.
A fast solver for the structured instance (25), or a
provably sufficient candidate-specific shortcut operation,
could improve the current hierarchy. The decomposition
identity alone supplies no such solver or running-time
bound.

For example, a lifted walk can sometimes be shortened by
recognizing a complete contiguous image $R_i(e)$ and
substituting $e$. For a general terminal simple cycle,
however, native cancellation and cycle decomposition may
have mixed images from several original edges. No existing
proof guarantees that the required shortcuts appear as
complete contiguous substrings. A dictionary of route
images is therefore only a possible data-structure input,
not a completed recovery algorithm.

### 5.1 A valid shortcut gives a useful local alternative

There is a precise positive rule when a whole route image IS
available as a contiguous subwalk. Suppose a current oriented
closed walk contains $R(e)$, with
$$
L_R=\ell_{\rm raw}(R(e))\geq2\ell_e.
 \tag{25a}
$$
Replace that occurrence by $e$, preserving its native
endpoints and orientation. Fix a target ratio $\lambda>0$.
Write $q=g^\top(e-R(e))$. If
$$
q\geq-\lambda(L_R-\ell_e),
 \tag{25b}
$$
the replacement does not decrease the surplus
$g^\top C-\lambda\ell_{\rm raw}(C)$. Any further valid
native cancellation can only improve its denominator.

If (25b) fails, the reverse correction has positive ratio
$$
\frac{-q}{\|L(e-R(e))\|_1}
   \geq\frac{-q}{L_R+\ell_e}
   >\lambda\,\frac{L_R-\ell_e}{L_R+\ell_e}
   \geq\lambda/3.
 \tag{25c}
$$
An explicit simple-cycle component attains at least this
ratio, with the usual orientation convention.
Thus a strong valid shortcut either preserves a target
surplus or exposes a constant-quality local alternative.

This rule is endpoint and gradient exact. It supplies no
guarantee that an available candidate walk contains enough
whole route images, nor a bound on the cost of finding them.

### 5.2 Even complete-route substring replacement is insufficient

There is a one-stage example in a degree-three native
multigraph. Let $Q_1,Q_2$ be internally disjoint $x$-to-$y$
paths of the same length $L\geq2$. Add stems $u x$ and
$y v$, and two distinct parallel edge IDs $e_1,e_2$
from $u$ to $v$. Every edge has length one.

Let $H$ contain the two paths and two stems. Its unique
simple cycle is $Q_1-Q_2$; neither $u$ nor $v$
lies on that cycle. Set
$$
R(e_1)=ux\oplus Q_1\oplus yv,\qquad
 R(e_2)=ux\oplus Q_2\oplus yv,
 \tag{25d}
$$
and use identity routes on $H$. Give $Q_1$ total
gradient one, $Q_2$ and the stems gradient zero, and
set $g_{e_1}=1$, $g_{e_2}=0$. All nonzero gradient
can be placed on one edge of $Q_1$, so labels are
integers in $\{0,1\}$.

Both corrections have zero gradient. The original
two-edge cycle $e_1-e_2$ has ratio $1/2$, while
the terminal cycle has ratio $1/(2L)$.
Neither complete nonidentity route in (25d), in either
orientation, is a contiguous subwalk of the terminal
simple cycle: each contains both stems, which are
absent from every simple cycle of $H$.

Thus a procedure that only replaces COMPLETE stored
route substrings in the returned terminal cycle makes
no nontrivial substitution here. The improvement needs
the joint cancellation
$$
e_1-e_2=(Q_1-Q_2)+D(e_1)-D(e_2).
 \tag{25e}
$$
The common stems cancel between the two different
corrections. They are not an alias artifact.

This is an obstruction to that particular local shortcut
rule, not to all efficient representative optimizers.
The parallel edges are genuine native IDs, as permitted
by the recursive core interface. Section 4 already gives
a simple, degree-three obstruction to the broader
separate-candidate comparison.

## 6. Exact gradients, aliases, and the scope of the obstruction

All correction zeroes in the construction are gauge
invariant. If
$$
g'=g+B^\top\pi,
 \tag{26}
$$
then $g'^\top c=g^\top c$ for every native circulation.
No choice of frozen vertex potential creates a useful
local numerator in (16). Correct zero-link contraction
and gradient-preserving raw lifts cannot change this fact.

Conversely, replacing a selected edge's gradient by the
gradient of an old or incorrectly projected route is not
an allowed shortcut. A replacement must have the same
IMMEDIATE boundary. Equal eventual physical images of
two aliases do not make an open path a circulation.
The fiber construction already uses exact immediate
endpoints, so that identity issue cannot explain away
the lower ratio.

This note isolates what follows from local path stretch,
exact corrections, and raw domination. It does not prove
that the particular KMPG stable-forest construction can
be forced to realize every nested route table above.
Vertex reduction, multiple forest choices, local ASZ
alternatives, and comparator-dependent averaging might
supply an additional cumulative-mass invariant. Such an
invariant must be stated and proved explicitly; it is
not a consequence of exact gradient telescoping.

For the current bottleneck, the concrete alternatives are
therefore:

* prove a cumulative bound such as (9), using additional
  structure of the actual hierarchy; or
* recover short root representatives by a new efficient
  cancellation/shortcut algorithm such as a structured
  version of (25).

Without one of these additions, replacing the full recursive
quality product by an additive or maximum local loss is
unsupported and is false for the stated local interfaces.
