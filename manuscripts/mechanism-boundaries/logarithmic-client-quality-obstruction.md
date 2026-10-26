# Exact logarithmic client states can hide good cycles behind recursive routes

**Separate mathematical analysis, 24 October 2026.** This note strengthens
[recursive-cycle-quality-obstruction.md](recursive-cycle-quality-obstruction.md).
It uses EXACT gradients of the permitted separable logarithms and an
EXACTLY conserved, positive, integer-valued flow. Every local correction
has exactly zero gradient, including after ordinary integer pricing.
Nevertheless a chain of constant-stretch native routes leaves terminal
cycle quality exponentially smaller than the original optimum.

Two objective profiles use the same graph and route chain. The first
uses only $`\log f`$. The second is a literal valid frozen state of the
all-expanded two-sided logarithmic maximum-flow threshold client:
integral ordinary capacities, the prescribed equal pads, one weighted
negative logarithm on the return arc, and a legitimate threshold.

This does not prove that the particular ASZ/stable-forest hierarchy
will choose these route tables. Nor does it claim that the fixed
step-selection implementation reaches this exact state. It proves
that separable logarithmic gradients and exact conservation, by
themselves, do not imply the stronger cumulative norm bound needed
to replace the recursive quality product.

## 1. One exactly conserved logical graph

Fix $`d\geq2`$, and put
```math
N=2^d-1,\qquad h=2^{d-1}.
 \tag{1}
```
There are ordered vertices $`w_0,\ldots,w_N`$. The even-indexed
vertices form $`A`$, the odd-indexed vertices form $`B`$, and both
sets have cardinality $`h`$. Add two distinct vertices $`s,t`$.

The ordinary directed multigraph has:

* every edge $`a\to b`$, for $`a\in A,b\in B`$;
* $`h`$ distinct parallel edges from $`s`$ to each $`a\in A`$;
* $`h`$ distinct parallel edges from each $`b\in B`$ to $`t`$.

There are $`M=3h^2`$ ordinary edge IDs. Add one return edge
$`e_{\rm ret}:t\to s`$. Set
```math
f_e=1\quad(e\text{ ordinary}),\qquad
                            f_{\rm ret}=h^2.
 \tag{2}
```
This flow is exactly conserved. Every $`a`$ has $`h`$ units
entering and $`h`$ leaving; the same holds at every $`b`$.
Source and sink both have total ordinary flow $`h^2`$, balanced
by the return coordinate.

All values in (2) are integers, hence belong to the numerical
$`\varepsilon`$-grid. For a master $`S`$ above the actual size,
they lie within the client's polynomial magnitude envelope.
Every parallel edge retains its own lifetime and price.

## 2. A nested route chain of stretch at most three

Let $`G_0`$ be the whole graph and write $`L_0=N`$. For
$`i=1,\ldots,d-1`$, put
```math
L_i=2^{d-i}-1.
 \tag{3}
```
The graph $`G_i`$ retains:

* the inner edges whose endpoint index distance is at most $`L_i`$;
* one fixed source edge $`s\to w_0`$;
* one fixed sink edge $`w_N\to t`$;
* the return edge.

Thus $`G_{d-1}`$ is the alternating path
$`w_0,w_1,\ldots,w_N`$, its source and sink edges, and the
return edge. It has exactly one undirected simple cycle.

Every removed edge is routed using genuine selected native IDs.
An inner edge joins an even to an odd index, so its index distance
is odd. Between stages $`i`$ and $`i+1`$, the old distance cap is
```math
L_i=2L_{i+1}+1.
 \tag{4}
```
An odd distance at most $`L_i`$ is either at most $`L_{i+1}`$,
or is a sum of three positive odd distances at most $`L_{i+1}`$.
For the latter case, use distances
```math
L_{i+1},\quad1,\quad
                                      q-L_{i+1}-1.
 \tag{5}
```
The corresponding monotone-in-index path has three edges.
Reference orientations alternate along it, but its endpoints
are correct. Retained edges may use identity routes.

At the first stage the source and sink edges also have short
routes. An even index distance from $`w_0`$ to any $`a\in A`$
is at most $`2L_1`$ and is a sum of two positive odd distances
at most $`L_1`$, unless it is zero. Route
$`s\to a`$ through the retained $`s\to w_0`$ edge and those
at most two inner edges. Similarly route $`b\to t`$ through
at most two inner edges to $`w_N`$, then the retained sink
edge. Parallel copies at the retained endpoints use its
one selected genuine edge.

Consequently every nonidentity route has at most THREE ordinary
edges. The return uses its identity route. All routes are simple
and preserve their exact immediate endpoints.

## 3. Why uniform ordinary gradients make every correction zero

Suppose every ordinary gradient equals some common number $`a`$.
Define a potential on the acyclic ordinary graph by
```math
p(s)=0,\quad p(A)=a,\quad p(B)=2a,\quad p(t)=3a.
 \tag{6}
```
Every ordinary reference edge has gradient equal to its endpoint
potential difference. Therefore EVERY ordinary route of Section 2
has the same signed gradient as its input edge:
```math
g^\top R_i(e)=g_e.
 \tag{7}
```
The return gradient may be arbitrary; its route is always the
identity. It follows that
```math
g^\top(e-R_i(e))=0
                        \quad\text{at every stage and edge}.
 \tag{8}
```
All composite corrections have the same property.

Suppose also that all ordinary lengths equal $`\ell>0`$, while
the return length is $`\ell_{\rm ret}>0`$ and gradient
$`g_{\rm ret}>0`$. Section 2 then has weighted stretch at
most three. Any simple cycle avoiding the return has gradient
zero. Any cycle using the return has gradient of absolute value
$`3a+g_{\rm ret}`$, because its ordinary $`s`$-to-$`t`$ path
telescopes (6).

The original graph has ordinary paths of three edges. Hence,
when $`a\geq0`$, its exact optimum is
```math
\beta_0=\frac{3a+g_{\rm ret}}
                                    {3\ell+\ell_{\rm ret}}.
 \tag{9}
```
The terminal graph's unique cycle has $`N+2`$ ordinary edges,
so its exact optimum is
```math
\beta_{d-1}=
                    \frac{3a+g_{\rm ret}}
                                {(N+2)\ell+\ell_{\rm ret}}.
 \tag{10}
```
No local correction supplies another nonzero numerator.
The ratio gap is
```math
\frac{\beta_0}{\beta_{d-1}}
              =\frac{(N+2)\ell+\ell_{\rm ret}}
                                    {3\ell+\ell_{\rm ret}}.
 \tag{11}
```
If $`\ell_{\rm ret}/\ell`$ is bounded by an absolute
constant, this is $`\Omega(N)=\Omega(2^d)`$.

This loss is present even in the BEST terminal cycle, measured
by its net norm. It is not caused by a raw representation
that failed to remove some backtracking.

## 4. Exact profile A: only positive logarithms

Give every logical coordinate the permitted objective
```math
\phi_e(f_e)=\log f_e.
 \tag{12}
```
At (2), ordinary edges have $`g_e=\lambda_e=1`$, while
```math
g_{\rm ret}=\lambda_{\rm ret}=1/h^2.
 \tag{13}
```
Take lengths $`\lambda`$. Equations (9)--(10) give
```math
\beta_0=1,\qquad
 \beta_{d-1}
       =\frac{3+1/h^2}{N+2+1/h^2}
       =\Theta(1/N).
 \tag{14}
```
Every logarithmic argument is positive and every logical value
is exactly conserved.

There is an additional POSITIVE observation specific to this
profile. If all coordinates are $`\log f_e`$, $`f_e>0`$, and
$`Bf=0`$, then
```math
g^\top f=\sum_e1=\|\lambda f\|_1.
 \tag{15}
```
Thus the current flow itself is a ratio-one circulation,
and a directed cycle of its positive support also has ratio one.
A different algorithm could exploit that fact. The example
does not rule out such a client-specific bypass. It shows
that (15) does not force the selected recursive route
representatives to retain a comparable ratio.

The matching top client generally has fixed nonzero divergence,
and the projection client has two-sided terms. Their complete
algorithm is not reduced to this special positive-circulation
observation.

## 5. Exact profile B: the all-expanded threshold objective

This profile has the literal ordinary bounds and return term
from Section 7 of
[../graph-backends/near-feasible-rounding-and-exact-projection.md](../graph-backends/near-feasible-rounding-and-exact-projection.md).

Assign original capacity one to every ordinary arc. Its scaled
upper capacity is 16, and lower capacity is zero. The total
original source capacity is
```math
\beta=h^2.
 \tag{16}
```
There is no ordinary arc entering $`s`$ or leaving $`t`$,
and there are no self-loops, so the global preprocessing
requirements hold.

Use the legitimate threshold $`b=\beta/2=h^2/2`$, which
is integral because $`h`$ is a power of two and $`d\geq2`$.
It is also the ordinary first midpoint of the initial
$`[0,\beta]`$ search interval. Set
```math
T=16b=8h^2,\qquad
         W=20000(M+1)=20000(3h^2+1).
 \tag{17}
```
Let the two pads on every ordinary arc equal
$`\zeta=4\delta`$, as at initialization. The objective is
```math
\Phi(f,z)=
    \sum_{e\ {\rm ordinary}}
       [\log(f_e+\zeta)+\log(16+\zeta-f_e)]
                      -W\log(T-z).
 \tag{18}
```
Evaluate it at the exact flow (2), so $`z=h^2`$.
All ordinary flows lie strictly within their true bounds,
and $`T-z=7h^2>0`$. This is far before the success condition.

Every ordinary coordinate has the identical exact derivative
and price
```math
a=\frac1{1+\zeta}-\frac1{15+\zeta},\qquad
 \ell=\lambda=
       \frac1{1+\zeta}+\frac1{15+\zeta}.
 \tag{19}
```
For $`\zeta\leq1/100`$, safe absolute bounds are
```math
4/5<a<1,\qquad1<\ell<2.
 \tag{20}
```
The return derivative equals its absolute price:
```math
g_{\rm ret}=\ell_{\rm ret}
       =\frac{W}{7h^2}
       =\frac{60000}{7}+\frac{20000}{7h^2}.
 \tag{21}
```
It lies between two fixed positive constants, independently
of $`h`$. Thus (8) holds EXACTLY and (11) is $`\Omega(N)`$.
The original ratio in (9) is bounded below by an absolute
constant greater than $`1/2`$, whereas (10) is $`O(1/N)`$.

This state satisfies more than the generic $`|g|\leq\lambda`$
inequality: it has exactly the prescribed common padding,
integral ordinary capacities, the actual integral threshold
weight $`W`$, and exact flow conservation. No coordinate
descriptor has been reverse-engineered to obtain an arbitrary
gradient.

The straight ray
```math
f_e(t)=t,\qquad z(t)=t h^2,
                           \qquad0\leq t\leq1,
 \tag{22}
```
is conserved and feasible throughout. All ordinary derivatives
and the return derivative are positive on this ray, so the
objective increases strictly with $`t`$. Grid points on it
are exact feasible states. This is not a proof that a fixed
backend's canonical step rule visits $`t=1`$; that stronger
reachability statement is unnecessary for the claimed failure
of an implication based only on the displayed state conditions.

## 6. Integer pricing, exact cancellation, and native port paths

At an exact anchor the client uses
```math
\ell^{\rm int}_e=\lceil H_{\rm price}\lambda_e\rceil,
             \qquad
        \gamma_e=\mathrm{round}(H_{\rm price}g_e),
                      \qquad H_{\rm price}=S^{100}.
 \tag{23}
```
In profile A, $`h^2`$ is a power of two dividing
$`H_{\rm price}`$ when $`S`$ is a sufficiently large power
of two. Thus every price in (13) is represented exactly.

In profile B, all ordinary $`\gamma_e`$ are the SAME
integer $`\gamma`$, and all ordinary lengths are the SAME
integer $`\ell^{\rm int}`$. Define the native potential
```math
0,\ \gamma,\ 2\gamma,\ 3\gamma
 \tag{24}
```
on the four layers. Each route still has exactly its own
input gradient. Every correction numerator is exactly
zero after rounding, not merely small. The return's
rounded label is immaterial to (8), because it is never
rerouted. The positive optimum and $`\Omega(N)`$ ratio
gap survive the rounding by fixed constants.

Apply the actual port-PATH degree reduction of the priced
client, from Section 3 of
[../graph-backends/priced-logarithmic-steps-from-raw-cycles.md](../graph-backends/priced-logarithmic-steps-from-raw-cycles.md).
Each real incidence has its own port, and ports of one
logical vertex are joined by the prescribed private path.
Connectors have length one and gradient zero. There are
$`O(M)`$ such records, all genuine real lifetimes stay fixed,
and the resulting backend graph has maximum degree three.

The route of a removed real edge consists of at most three
ordinary selected edges and a constant number of port
subpaths. Its connector cost is $`O(M)`$. Every ordinary
integer length is $`\Omega(H_{\rm price})`$; hence local
stretch is still bounded by an absolute constant. The
exact signed integer gradient is preserved because
connector gradients vanish and (24) telescopes.

The original short cycle has only a constant number of
real edges and at most $`O(M)`$ connector cost. The
terminal graph, after contracting its port paths, has
exactly the unique cycle used in (10). Every nonzero
terminal cycle therefore traverses all its $`N+2`$
ordinary real edges. Positive connector lengths can
only worsen its ratio. Since $`H_{\rm price}\gg M`$,
the original constant ratio and exponential gap survive.

These connectors are the numerical engine's private
conservation representation. They are not additional
logarithmic coordinates, and no extra descriptor is
assigned to them. Logical conservation (2) and the
engine's exact increment lift are the relevant interface.
Open native paths are never erased merely because their
logical or eventual physical images coincide.

## 7. Consequence for a possible improvement

Both exact profiles satisfy the numerical state properties
that motivated this check. Profile B also has the literal
all-expanded objective and bounds. Therefore none of
those properties alone implies a small cumulative route
mass, or an additive/max replacement for recursive
stretch in the separate-candidate comparison.

A stronger algorithm might use its actual forest family,
ASZ alternatives, a special reachable-state invariant,
or the positive-support observation (15) in a suitable
subcase. It might also optimize combinations of zero-
gradient corrections to shorten a terminal representative.
Those are additional algorithmic mechanisms, not
consequences of gradient telescoping or conservation.

### 7.1 A positive special case exposed by this example

The example itself has an efficient STATIC alternative. Suppose a
graph consists of ordinary edges and one distinguished return edge
$`t\to s`$, all lengths are positive, and
```math
g_{uv}=p(v)-p(u)
                      \quad\text{on every ordinary edge}.
 \tag{25}
```
Ordinary traversals may use either orientation, with the corresponding
signed gradient. Put
```math
d_\ell=\mathrm{dist}_{\ell,{\rm ordinary}}(s,t),
 \qquad \kappa=g_{\rm ret}+p(t)-p(s).
```
If $`s,t`$ are connected in the ordinary graph, the exact maximum
absolute cycle ratio is
```math
\frac{|\kappa|}
                               {\ell_{\rm ret}+d_\ell}.
 \tag{26}
```
Every ordinary cycle has zero numerator. Every simple cycle containing
the return edge has numerator of absolute value $`|\kappa|`$, so a
shortest ordinary $`s`$-to-$`t`$ path attains (26). The potential can
be checked by a graph traversal, and a shortest path can be found in
$`O((n+m)\log(n+2))`$ scalar operations. This is a static bypass,
not a claim that a complete such scan is affordable at every
numerical query.

There is also an approximate version. If a supplied potential satisfies
```math
|g_{uv}-(p(v)-p(u))|\leq\epsilon\ell_{uv}
                       \quad\text{on every ordinary edge},
 \tag{27}
```
then the shortest-return-cycle candidate has ratio within
$`2\epsilon`$ of the global optimum. Indeed, for any circulation $`c`$,
the ordinary length is at least $`d_\ell|c_{\rm ret}|`$, by the
shortest-path Lipschitz potential. Its numerator is at most
```math
|\kappa|\,|c_{\rm ret}|
                  +\epsilon\|\ell c_{\rm ordinary}\|_1.
```
The optimum is therefore at most the quantity in (26) plus
$`\epsilon`$. In particular, circulations omitting the return edge
have ratio at most $`\epsilon`$, so they are included in this bound.
The shortest-return cycle has ratio at least (26)
minus $`\epsilon`$, proving the claim.

Thus the two-sided example does not rule out algorithms that exploit
additional gradient structure. It shows that merely passing this
structure to independently stretch-bounded route maps does not
automatically exploit it.

The present example does not claim that all nested
tables in Section 2 arise from the actual maintained
distance hierarchy. That remains the exact scope boundary.
It does show that an improvement must use more than
the general priced-logarithmic interface, even when its
values, gradients, integrality, native IDs, and flow
conservation are all respected.
