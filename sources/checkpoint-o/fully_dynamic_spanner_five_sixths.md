# A fully dynamic spanner with explicit five-sixths overhead

**Research proof assembly, 25 October 2026. Root and independent
mathematical audits of the full-horizon construction completed.**

This note supplies the full update horizon for the clipped-walk spanner
transfer. It reconstructs the batching argument in the published version
of Kyng--Meierhans--Zoecklein (KMZ),
[ICALP 2025, Section 5](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.111/LIPIcs.ICALP.2025.111.html),
with nested integer clocks, initialization, and actual edge lifetimes
made explicit. It then substitutes the numerical hierarchy audited in
`clipped_walk_queries_and_dynamic_spanner.md`.

The conclusion is deterministic maintenance of a spanner of
an arbitrary-degree undirected graph, with

\[
 \begin{array}{ll}
 \text{stretch}&\exp O(U^{5/6}h^{1/6}),\\
 \text{current number of edges}&n\exp O(U^{5/6}h^{1/6}),\\
 \text{total initialization/update work}
     &(n+m_0+I+D)\exp O(U^{5/6}h^{1/6}),\\
 \text{total output recourse}
     &(n+D)\exp O(U^{5/6}h^{1/6}).
 \end{array}                                                \tag{F1}
\]

Here `m_0` is the actual initial number of edges, `I,D` count subsequent
insertions and deletions, `N` is a declared polynomial history cap,
`U=log(N+4)`, and `h=log(U+4)`. The vertex set is fixed with size `n`.
Lengths are unweighted, or positive polynomial-range integers handled
by separate unweighted length classes. Edge IDs distinguish physical
lifetimes and parallel edges. Self-loops are irrelevant and discarded.
All displayed guarantees hold after complete external updates; time
is amortized, not worst case.

The statement does not obtain arbitrary deletion sequences by rebuilding
a dense graph after every `n` deletions. Such a procedure could pay an
unacceptable `m_current D/n` term. The nested clocks below are essential.

## 1. The single-instance contract, without a deletion-horizon assumption

Fix one instance on `n` vertices, congestion cap `K >= 2`, and path
threshold `T=Gamma L`, where `L=2 ceil(log_2(n+4))`. Let
`R=ceil(T)`. The instance uses the algorithm and clipped reporting proof
in `clipped_walk_queries_and_dynamic_spanner.md`, Sections 1--6, but
now sets its saturation cap to the integer `K`.

Suppose this instance receives `F` insertions and `D_0` deletions before
it is retired. Initial edges are inserted into a fresh empty instance
and are included in `F`. No condition `D_0 <= F/K` is required for the
following accounting:

\[
 \begin{aligned}
 \#\text{assignments}&\le F+K D_0,\\
 \#\text{blocked edge lifetimes}&\le R(F+K D_0)/K,\\
 |H|&\le c\bigl(n+(R/K)F+R D_0\bigr),\\
 \#\text{insertions into }H
    &\le c\bigl(n+(R/K)F+R D_0\bigr).
 \end{aligned}                                             \tag{F2}
\]

The last line follows because an edge leaves this instance's `H` only
on a genuine input deletion. Increase the absolute constant `c` to
include those `D_0` deletions. The eligible graph has girth greater
than `L` and therefore `O(n)` edges throughout.

With numerical update factor `alpha=exp O(B)`, numerical query cost
`poly(U)`, and clipped report cost `R poly(U)`, its full work is at most

\[
 \operatorname{poly}(U)\left[
   R(F+K D_0)
   +\alpha\bigl(n+(R/K)F+R D_0\bigr)\right].           \tag{F3}
\]

This includes initialization of `n` vertex handles, creation and
retirement of routes and inverse lists, all eligible-graph updates,
and destruction of the instance's actual records. Every stored route
incidence is created and retired at most once. It does not charge a
numerical oracle update for every edge of the instance's dense input.
That input is accessed through numerical queries; only the sparse
eligible graph is the oracle's dynamic graph.

For a public clipped implementation with an additional reporting factor
`Q_path=exp O(dh)`, replace the first term of (F3) by
`Q_path R(F+K D_0)`. It changes the final logarithmic work by `O(dh)`,
not the numerical threshold or the output stretch.

## 2. Capacity and exact rebuild clocks

Let `M >= n` be a known bound on the maximum number of simultaneously
living input edges, also covering the initial graph. It is distinct
from cumulative insertions. For a simple graph one may take
`M=max(n,n(n-1)/2)`; for a multigraph use a declared current-edge cap.
It suffices that `M <= N^{O(1)}`. No `M`-edge padding is allocated.

Choose a power-of-two integer `K >= 2` and define

\[
 s=\max\{1,\lceil\log_K(M/n)\rceil\},\qquad
 M'=nK^s,\qquad t_i=M'/K^i\quad(1\le i\le s).          \tag{F4}
\]

Then `M' >= M`, `M' <= K max(M,n)`, each clock is an integer,
`t_{i-1}=K t_i`, and the final clock is exactly `t_s=n`.
`M'` is a clock bound only; its unused portion is never materialized.

Maintain `H_0=G`, and let layer `i` maintain a spanner `H_i` of
`H_{i-1}` using Section 1. Every ordinary change in `H_{i-1}` is
forwarded to layer `i`. Count **original external deletions only**
in a global integer clock. Whenever that count becomes a multiple of
`t_i`, retire layers `i,...,s`, then rebuild them from the settled
current `H_{i-1}`. Use the smallest such index `i`; the other required
rebuilds are already included. Initialize each replacement instance
empty, then seed it with actual current parent edges.

After a triggering original update, one may first finish ordinary
forwarding and then perform this replacement. Intermediate forests
and spanners are private; publish only the final settled `H_s`.
Retired descendant structures are destroyed without forwarding their
artificial deletions as ordinary input deletions to new instances.
Their actual destruction and replacement work is counted below.

The clocks are nested. Consequently a parent's replacement is always
on a child's replacement boundary. During the lifetime of any one
layer-`i` instance, its parent does not undergo an internal replacement.
Inside that interval parent edges disappear only when the corresponding
physical input edge is externally deleted. Thus layer `i` sees at most
`t_i` genuine input deletions in one lifetime and at most `D` over all
its lifetimes. This remains true when a deletion fails to appear in a
particular parent spanner; it then causes no deletion there.

## 3. Current-size induction

Choose a sufficiently large absolute constant `c_0` and put

\[
                    V_i=(c_0R)^i M'/K^i.                \tag{F5}
\]

We claim `|H_i| <= V_i` after every settled operation in a layer
lifetime. The base holds because `|G| <= M <= M'`.

Within one layer-`i` lifetime, include its initial seeding in its input
insertion count `F_i^{life}`. Its parent has current size at most
`V_{i-1}`, and within that interval removes edges only on the at most
`t_i` original deletions. The identity
`initial edges + new insertions = final edges + deletions`
therefore gives, for every chronological prefix,

\[
                      F_i^{life}\le V_{i-1}+t_i.        \tag{F6}
\]

Use (F2), `D_i^{life} <= t_i`, and `n <= M'/K^i` for `i <= s`.
It gives

\[
 |H_i|\le c\left[n+(R/K)V_{i-1}+(R/K)t_i+Rt_i\right]
       \le(c_0R)^i M'/K^i
\]

when `c_0` is large enough. The argument applies during initialization
as well: inserting a prefix of the actual seed cannot exceed the same
count. At the final layer,

\[
                         |H_s|\le n(c_0R)^s.           \tag{F7}
\]

No induction assumes that the number of ordinary insertions is bounded
by a constant times the number of deletions. Arbitrarily many successive
insertions are permitted, subject to the living-edge cap `M`.

## 4. Total initialization, rebuilding, and update work

Write `I_*=m_0+I`. Let `F_i` count all input insertions processed by
all layer-`i` instances, including seeding after every replacement.
Let `O_i` count all insertions into their output spanners, including
outputs constructed privately during initialization. Layer `i` has
exactly `1+floor(D/t_i)` instances. Since `t_i >= n`,

\[
 n\bigl(1+\lfloor D/t_i\rfloor\bigr)\le n+D.           \tag{F8}
\]

Apply the last line of (F2) to each of these instances and sum. Genuine
deletions total at most `D`, as proved in Section 2. This gives

\[
               O_i\le c\left[n+D+(R/K)F_i+R D\right]. \tag{F9}
\]

Layer 1 receives the original updates and is additionally seeded from
`G` when its clock fires. Thus

\[
                  F_1\le I_*+(D/t_1)M\le I_*+DK.      \tag{F10}
\]

For a subsequent layer, ordinary insertions from its parent are
included in `O_i`. The first initialization can also be charged to
the parent's corresponding initial output insertions. Each later
replacement of the child seeds at most `V_i` edges. Hence the safe
bound, allowing harmless double charges at coincident replacements, is

\[
 \begin{aligned}
 F_{i+1}&\le O_i+(D/t_{i+1})V_i\\
        &\le O_i+DK(c_0R)^i.                            \tag{F11}
 \end{aligned}
\]

No `+1` times the potentially dense capacity `M` is introduced in
(F10) or (F11). The first input is its actual `m_0` edges; an empty
initial graph seeds no edges. Every later capacity-sized seeding is
charged to a completed interval of genuine original deletions.

Choose a sufficiently large absolute `c_1`. Induction using
(F9)--(F11) proves

\[
                  F_i\le(c_1R)^i(I_*+n+DK).             \tag{F12}
\]

For example, the coefficient `(cR/K)` in (F9) is at most `cR`, and
both `c_0R` and this coefficient are dominated by a sufficiently
smaller fixed fraction of `c_1R`. The remaining `O(R(n+D))` is
paid by the initial `I_*+n+DK` allowance. Summing over layers loses
only another fixed power of `(c_1R)^s`.

Equations (F3), (F8), and (F12) now imply

\[
 \begin{split}
 T_{\rm total}
   &\le (I_*+n+DK)(c_2R)^{c_2s}
             (\alpha+Q_{\rm path})\operatorname{poly}(U)\\
   &\le (n+m_0+I+D)K(c_2R)^{c_2s}
             (\alpha+Q_{\rm path})\operatorname{poly}(U).
 \end{split}                                             \tag{F13}
\]

The constant `c_2` is absolute. In the new positive native hierarchy,
`Q_path=poly(U)`; in the public positive-port implementation it is
`exp O(dh)`. All `n`-vertex oracle initializations and their retirements
are included in (F8). All actual route-list retirement is included in
(F3). The clocks are numbers, not instructions to initialize artificial
edges up to their caps.

An inner numerical oracle is run only on the eligible subgraph of its
one spanner instance. It always has `O(n)` active edges. Instance input
edges that are not in that eligible graph incur numerical queries and
stored routes, not an insertion into the inner oracle. This is why
(F13) does not contain the current dense edge capacity multiplied by
every ordinary numerical update factor.

## 5. Output stretch and recourse

At every settled state, `H_i` is a subgraph and an `R`-spanner of
`H_{i-1}`. The hierarchy therefore gives stretch at most `R^s`.
Equation (F7) bounds the final size by `n(c_0R)^s`.

The last layer is replaced after every `n` original deletions.
Between successive replacements, its output loses edges only on those
at most `n` physical deletions. Its ordinary insertions are at most
its maximum size plus those deletions. At a replacement the change
between the old and new published edge sets is at most the sum of
their sizes. Repeated physical edge IDs need not actually change,
but charging both is safe. Consequently

\[
 \operatorname{recourse}(H_s)
        \le (n+D)(c_3R)^s.                              \tag{F14}
\]

Physical graph edges retain their IDs through all layers. A copy of
an eligible edge in an inner degree adapter is not an additional
output edge of `H_s`. Different parallel physical edges may be
selected, but the eligible graph contains no parallel pair forming a
short cycle, so the girth and sparsity proof remains valid. No output
edge other than a current input edge is introduced.

For weighted inputs, maintain this complete hierarchy separately in
each dyadic length class. The final union has twice the unweighted
stretch and a polynomial-logarithmic factor in the other quantities.
Clipping occurs in each unweighted class graph. It never enumerates
`Gamma` times the numerical value of a large original edge weight.

## 6. Quantitative substitution

Put `z=log K`. Since `log(M/n)=O(U)`, (F4) gives
`s=O(1+U/z)`. Let `A=log Gamma`, so `log R=O(A+h)`.
Equations (F7), (F13), and (F14) give the separate logarithmic bounds

\[
 \begin{aligned}
 Z_{\rm time}&=O\left(B+z+(1+U/z)(A+h)+h\right),\\
 Z_{\rm stretch}, Z_{\rm size}, Z_{\rm recourse}
      &=O\left((1+U/z)(A+h)\right).
 \end{aligned}                                           \tag{F15}
\]

The public reporting factor `O(dh)` is added to the first line if
needed; it is smaller than the displayed terms at the comparisons
below. The literal threshold still uses the actual `Gamma`.

For the main new conclusion it is enough to use the conservative,
already audited no-reset hierarchy from
`steiner_pool_no_reset_strong_forest.md`. With
`p=r=d=Theta(t)`, local repair depth `K_repair=Theta(t^2)`, and
`x=Theta(U/t)`, it has

\[
                 B=O(U/t+t^5h),\qquad A=O(t^4h).       \tag{F16}
\]

The `t^5 h` term is the old `K_repair^2 g` repair work. Thus the
main five-sixths conclusion does **not** require strengthening the
repair recurrence to its normalized `K_repair g` version. That
version would only lower a non-dominating term here.

Choose

\[
 t=\Theta((U/h)^{1/6}),\qquad
 z=\Theta(U/t),\qquad K=2^{\lceil z\rceil}.             \tag{F17}
\]

Then `U=Theta(t^6h)`, `B=O(t^5h)`, `A=O(t^4h)`, and
`s=O(t)`. Therefore every bound in (F15) is at most

\[
                         O(t^5h)=O(U^{5/6}h^{1/6}).     \tag{F18}
\]

The hierarchy's inner shrink guard has slack: `x=Theta(t^5h)`
dominates `log P=O(t^4h)` and all `O(dh)` degree charges. The
outer cap `K` eventually exceeds every needed fixed multiple of `R`.
All finitely many small values are handled directly. The represented
integers and clocks have polynomial bit length in `U`.

The total encoded history and intermediate inventories are at most
the input history times `exp O(U^{5/6}h^{1/6})`. A fixed polynomial
increase of the declared history cap covers these records and the
positive root degree adapters. It changes `U` by only a fixed constant
factor. This is a bound on actual records, not padded instances.

Equations (F13), (F14), and (F18) prove conclusion (F1), with the
explicitly retained research-provider imports. The completed audits are
**fully_dynamic_spanner_independent_audit.md** and
**fully_dynamic_spanner_root_audit.md**.

## 7. Public comparison at the same output guarantees

The jointly reconstructed public APSP provider has the family

\[
             B_{\rm pub}=O(U/t+t^6h),\qquad
             A_{\rm pub}=O(t^5h),                      \tag{F19}
\]

proved in `public_apsp_joint_retuning_audit.md` and independently
audited there. The positive-port clipped-report lemma from Section 8
of the companion note supplies its missing application-level accounting:
the reporting factor is `exp O(dh)`, which is smaller than the terms
in (F19). Thus this public hierarchy can be used in the same batching
proof. It is not excluded merely because its first theorem was stated
for numerical queries.

Taking `t=Theta((U/h)^{1/7})` and `z=Theta(U/t)` gives a fully
dynamic public composite whose time, stretch, density, and recourse
overheads all have logarithm `O(U^{6/7}h^{1/7})`. This is a derived
composition from public ingredients, not a printed six-sevenths
spanner theorem.

There is a more precise matched comparison. Require the common output
stretch, size overhead, and recourse overhead to have logarithm

\[
                         S_0=U^{5/6}h^{1/6}.
\]

In the public family choose

\[
 t_{\rm pub}=\Theta((U/h)^{5/36}),\qquad
 z_{\rm pub}=\Theta(U/t_{\rm pub}).
\]

Then `s=O(t_pub)`, its output logarithmic stretch is `O(t_pub^6 h)
= O(S_0)`, and its logarithmic work is

\[
                  O(U/t_{\rm pub}+t_{\rm pub}^6h)
                     =O(U^{31/36}h^{5/36}).             \tag{F20}
\]

| Construction | Logarithmic time overhead | Common logarithmic stretch, density and recourse overhead |
|---|---|---|
| Reconstructed public APSP plus public batching | `O(U^(31/36) h^(5/36))` | `O(U^(5/6) h^(1/6))` |
| Research provider plus positive witnesses and the same batching proof | `O(U^(5/6) h^(1/6))` | `O(U^(5/6) h^(1/6))` |

Both rows support arbitrary edge insertions and deletions throughout
the same polynomial history, the same fixed vertex set, physical edge
IDs, and arbitrary input degrees. Their work is amortized. Choosing
fixed constants against a sufficiently large common allowed stretch
envelope makes the comparison on that scale; hidden stretch constants
are not claimed numerically equal without this adjustment.

There is also an elementary baseline that must not be omitted. If the
entire living-edge cap already satisfies `M <= n exp O(S_0)`, keeping
`H=G` gives stretch one, constant work per input edit, and recourse
`m_0+I+D <= M+2D`. It already meets the permitted output density and
recourse scale. A new maintenance theorem at that density is useful
on inputs whose living graph can be denser. In particular, for
`M=n^{1+epsilon}` with fixed `epsilon>0`, the target
`n exp O(U^{5/6}h^{1/6})` is asymptotically smaller than `M` under
the standard polynomial-history convention. That is a substantive
dense-graph regime of the comparison. No improvement over `H=G`
is claimed in its valid sparse regime.

The primitive five-sixths exponent is not itself a new exact matching
exponent. The new application here is a dynamic sparse subgraph with
explicit multiplicative distance stretch and low output recourse.
The new proof contribution is the quantitative witness/batching
composition. The batching operations themselves are public KMZ ideas.

## 8. What nonuniform tuning can and cannot change in this accounting

These calculations optimize specified positive-charge formulas. They
are not algorithmic lower bounds and do not prove that an upper-bound
term must be incurred by every implementation.

For these worst-case parameter comparisons take `N=n^{Theta(1)}`,
so the oracle's root logarithm is comparable to `U`, and consider
polynomially dense allowed inputs. This qualification is needed:
a small actual graph or a loose much larger history cap does not
force `Omega(U)` useful density reduction.

For the public hierarchy, Section 6 of
`same_stretch_apsp_comparison_and_root_audit.md` proves, even with
nonuniform inner parameters while local log-size remains comparable
to `U`, that a work budget `B` dominates charges satisfying

\[
              B^7\gtrsim U^6h,\qquad
              A_{\rm charge}\gtrsim U^5h/B^5.           \tag{F21}
\]

In an outer reconstruction with logarithmic density reduction `z`,
the number of layers is `Omega(U/z)` on a worst-case polynomially
dense input. With a time budget `Z` paying both `B` and `z`, and a
claimed logarithmic output metric budget `S`, the charged formula
therefore requires

\[
 S\gtrsim U^6h/Z^6,
 \qquad
 Z\gtrsim\max\{U^{6/7}h^{1/7},\ U(h/S)^{1/6}\}.        \tag{F22}
\]

For `S=S_0`, the second term gives precisely `U^(31/36)h^(5/36)`.
The balanced choice `S=Z` gives `Z^7 >= Omega(U^6h)`.

The same comparison survives varying the outer parameters between
layers, within the same accounting. Suppose the successive logarithmic
density reductions are `z_i`, each charged at most `Z`, and they
sum to `Omega(U)` before reaching near-linear size. Then there are
`j=Omega(U/Z)` layers. Each uses an `n`-vertex oracle with the
comparable root logarithm `U` on such a worst-case instance, and its
inner work is at most `Z`. Equation (F21) gives
`A_i >= Omega(U^5 h/Z^5)` for every one. Summing the metric charges
again gives `S >= Omega(U^6h/Z^6)`. Small final levels or a sublinear
`o(U)` saving in the target density do not remove the initial
`Omega(U)` total reduction obligation.

For the research provider, the corresponding inner metric charge from
`nonuniform_parameter_budget_frontiers.md` is

\[
                         A_i\gtrsim U^4h/B_i^4.         \tag{F23}
\]

The same outer argument yields `S >= Omega(U^5h/Z^5)`.
The displayed work formula also pays the cumulative metric charge,
so balancing all overheads requires `Z^6 >= Omega(U^5h)`. This
reproduces the five-sixths point within the chosen composition,
including nonuniform clocks and inner parameter choices. It does not
rule out a different maintenance rule that avoids the cumulative
metric cost, a different provider, or an application-specific path
selection argument.

The uniform families already certify the sufficient curves

\[
 \begin{aligned}
 Z_{\rm new}(S)&=O\left(
       \max\{U^{5/6}h^{1/6},\ U(h/S)^{1/5}\}\right),\\
 Z_{\rm pub}(S)&=O\left(
       \max\{U^{6/7}h^{1/7},\ U(h/S)^{1/6}\}\right),
 \end{aligned}                                           \tag{F24}
\]

for `h << S = o(U)`, in the parameter range where the respective
source shrink and uniformity guards hold. If a larger `S` is allowed,
one may keep the smaller balanced output stretch; the formulas do
not force using all of the allowed stretch budget.

## 9. Source and status boundary

The primary batching source is the **published** ICALP 2025 paper,
Section 5 and Theorem 18. Its earlier arXiv v1 does not contain this
extension. Sections 1--5 above are a direct counted reconstruction,
so no unexamined indexing convention in a rebuild sentence is needed.
The single-instance counting specializes its Corollary 10 and Lemma 11.

`dynamic_spanner_public_baseline_audit.md` separately checks newer
primary results, including the parameter domain of Chuzhoy--Parter
and the randomized status of the MGS/BvdBPG+ route. Those checks must
remain attached to any final novelty summary. This note establishes
a comparison with the explicitly reconstructed public composition;
it does not claim to have optimized every public spanner framework.

The provider, no-reset native hierarchy, positive length/bits, and
small-component interfaces are named imports from this research
checkpoint. The clipped reporting and batching calculations above
are newly assembled here. Their completed independent and root audits
are linked after (F18). This is an internally audited research proof
assembly, not a formal or externally reviewed verification.
