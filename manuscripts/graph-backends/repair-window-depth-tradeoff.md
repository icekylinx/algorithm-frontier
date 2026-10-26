# Repair-window depth and the cost of bypassing layers

**Separate exploration, 24 October 2026.** This note studies the
particular touched-set repair architecture used by the current
distance sparsifier. It gives two precise obstacles to improving
its quality by rearranging existing layers or replacing only their
route records. It is not a lower bound for dynamic spanners or
minimum-ratio-cycle algorithms. The reviewed $4/5$ matching
composition is unchanged.

The starting constructions are
[normalized-projected-route-composition.md](normalized-projected-route-composition.md)
and
[amortized-static-base-distance-sparsifier.md](amortized-static-base-distance-sparsifier.md).
The source repair is Chen et al.,
[arXiv:2311.18295v1](https://arxiv.org/pdf/2311.18295),
Definition 7.13 and Algorithm 7.

## 1. Why one repair uses the preceding window

Suppose a lower collection of selected layers last supplied a valid
route for every demand at time $\tau$. At current time $t$, its
stored routes may be broken. The repair uses all vertices touched
since $\tau$, not just vertices touched since the last invocation
of the repair itself. Exterior prefixes up to the first touched
vertex remain valid. A projected demand connects the two first
touched anchors, and its preliminary image consists of those
prefixes and its own current central input edge.

If the lower certificate can be $A$ edits old, a new projected
instance can therefore have $\Theta(A)$ touched vertices.
Rebuilding the upper repair every $B$ edits gives the selected
membership budget
$$
O(\Gamma A/B)
 \tag{1}
$$
per edit, apart from the established fixed polynomial factors.
This statement uses the actual initial history when shorter than
$A$, as in the prefix-safe source construction.

The dependence on the touched-set size is not merely a consequence
of representing routes explicitly. A projected instance can be a
tree on its touched vertices whose distinct central IDs do not
already belong to the retained lower layers. Any subgraph routing
every projected edge must then retain all tree edges. Thus there
are individual legal projected instances requiring
$\Omega(|S|)$ selected central IDs.

This observation does not assert that every window in one
adversarial update sequence simultaneously realizes that extreme.
It explains why a proof using only the existing static-subgraph
interface must retain the $A/B$ factor in its worst-case budget.

## 2. A telescoping lemma for reparented window dependencies

Consider a chain of repair dependencies with declared window
lengths
$$
A_0=T>A_1>\cdots>A_d=1.
 \tag{2}
$$
At step $i$, a repair scheduled every $A_i$ edits relies on a
certificate whose validity can be $A_{i-1}$ edits old. Put
$$
r_i=A_{i-1}/A_i.
$$
Then, exactly,
$$
\prod_{i=1}^d r_i=T.
 \tag{3}
$$
Consequently:

**Window-depth lemma.** If every dependency is budgeted at window
ratio at most $R$, then
$$
d\geq\frac{\log T}{\log R}.
 \tag{4}
$$
If the sum of its window-ratio budgets is at most $B$, then
AM--GM gives
$$
B\geq d\,T^{1/d}.
 \tag{5}
$$

The same statement holds on any chosen base-to-current dependency
path in a directed acyclic organization of windows. Parallel
branches do not change the telescoping equality on such a path.
The hypotheses require each dependency to be certified by the
existing first-touched-prefix argument; a new validity invariant
could fall outside this model.

The ordinary radix construction has $T=\rho^K$ and essentially
all $r_i=\rho$. It is already balanced for (5).

### Skipping several layers

If a new repair bypasses $b$ ordinary levels, its lower window is
$\rho^b$ times its own rebuilding interval. Its budget in (1)
becomes $O(\Gamma\rho^b)$, while the number of static
compositions on a dependency chain decreases by a factor of about
$b$. Thus the elementary substitution
$$
K\longmapsto K/b,\qquad
                \rho\longmapsto\rho^b
 \tag{6}
$$
does not create a new quality/recourse tradeoff. It changes the
effective radix parameter.

In particular, replacing $K$ serial dependencies by
$O(\log K)$ dependencies through ordinary reparenting forces some
window ratio to be at least $T^{1/O(\log K)}$. A balanced binary
picture of the same chronological windows does not by itself
avoid this cost.

For the current $4/5$ choice,
$$
\log T=\Theta(U),\quad
 K=\Theta((U/h)^{2/5}),\quad h=\Theta(\log U),
$$
reducing dependency depth to $O(\log K)$ this way would give a
logarithmic recourse budget of order $U/\log U$. This is larger
than the retained $O(U^{4/5}h^{1/5})$ total overhead. This is a
comparison inside the declared-window model, not a universal
lower bound.

## 3. A fixed selected support cannot always be shortcut geometrically

A separate proposal is to leave every selected central membership
unchanged and periodically replace the demand routes by better
paths. Such an operation may reduce a poor chosen route, but it
cannot improve the distance of the selected graph itself.

For a concrete example, let the native graph consist of a unit
path
$$
v_0v_1,\ v_1v_2,\ \ldots,\ v_{L-1}v_L
$$
and one extra unit edge $e=v_0v_L$, with $L\geq2$.
Let the selected support contain exactly the path edges. Every
endpoint-preserving walk for $e$ in that support has length at
least $L$, and its unique simple route has length exactly $L$.
No loop erasure, route-owner change, inverse-index rebuilding, or
shortest-path calculation changes that fact.

This support satisfies an abstract stretch upper bound
$\Gamma^K$ whenever $L\leq\Gamma^K$. Therefore a black-box
contract that promises only this upper bound cannot justify
replacing it by $\Gamma^{O(\log K)}$ using route-only work.
This example does not show that the current deterministic repair
algorithm reaches this support from its particular initial base.
A reachability proof or a stronger maintained-distance invariant
would be needed for that claim.

Adding the missing unit edge $e$ solves this one example. In the
actual dynamic construction, adding such edges changes selected
memberships, native degree feedback, child topology, and possibly
child metric records. Those effects require a recourse bound; they
cannot be charged as a pure local demand reroute.

## 4. What a positive replacement would have to add

The current route recurrence
$$
L_{\rm new}\leq c\Gamma L_{\rm old}
$$
is an upper bound on an explicit valid walk. Improving it could
follow from any of the following genuinely additional statements:

1. a repair algorithm with a touched-set validity certificate that
   does not inherit the full preceding window;
2. an incremental merge of projected instances whose membership
   cost is below recomputing an entire preceding touched window;
3. a maintained selected support with substantially better actual
   distances than the present $\Gamma^{O(K)}$ guarantee, together
   with an efficient procedure finding those shorter routes;
4. a cycle-comparison theorem that pays less than the largest
   geometric stretch, even when the retained support has a long
   route for an individual native edge.

The fourth possibility is different from changing window schedules.
It must account for the numerator and raw traversal of all
correction circulations. Exact telescoping alone does not establish
it. The separate comparison investigation should keep that scope
distinct from (1)--(6).

Neither a balanced redraw of the existing window chain nor a
route-only refresh currently proves a new quantitative exponent.
