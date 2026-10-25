# A conservative constant-depth distance-oracle backend

**Research construction, 24 October 2026.**
This is the preferred formulation of the 2026 distance-oracle backup.
It uses constant depth and the conservative squared-degree bounds
actually appearing in the local maintenance proofs. It does not require
an independent justification of the stronger full-depth linear-degree
recurrence stated in KMPG Theorem 3.1. The primary 2023 backend remains
a separate route.

The raw cycle-quality argument is in
`distance_oracle_raw_lift.md`. The detailed gauge correction,
source discrepancy, and stable-map discussion are in
`distance_backend_general_matching_integration.md`. This note makes the weaker
but sufficient parameter recurrence explicit.

The complete mathematical composition with the current carrier and
uniform matching construction is in
[distance backend integration](distance_backend_general_matching_integration.md).
It also gives explicit integer degree/recourse caps and a common
geometrically growing pool capacity, so the executable parameter
family does not need the constants hidden in the asymptotic factors
used for analysis below.

For arbitrary disconnected inputs, all the bounds in this note use the
[disconnected-component wrapper](disconnected_component_backend_wrapper.md).
Its common roots and pivots for small initial components, constructive
empty-loop convention, and first-use child activation are part of the
algorithm. The small local roots are not charged to a literal
`O(m/k)` forest-root bound; every actually inserted child slot, including
one that later becomes isolated, is counted in the recursive size.

## 1. Goal and local constructive inputs

The input is a dynamic degree-three graph of nominal lifetime size at
most `M`, with positive integral lengths, integral gradients of polynomial
magnitude, and `O(log M)` bits. The integration note derives integral
recursive lengths from the constructive fixed stretch labels; it does
not clear arbitrary edge denominators by one global multiplier.
Let `eta>0` be a sufficiently small **fixed** rational. The goal
is a deterministic raw-certified cycle backend with

    initialization M^(1+O(eta)+o_eta(1)),
    amortized updates and queries M^(O(eta)+o_eta(1)),
    quality and answer-piece count M^(O(eta)+o_eta(1)),
    occurrence multiplicity M^(O(eta)+o_eta(1)).

The constants multiplying `eta` are absolute. This is enough for the
matching phase after fixing `eta` sufficiently small compared with its
fixed parameter `a`; a near-linear exponent is unnecessary.

The source inputs are the constructive algorithms in KMPG, *A Dynamic
Shortest Paths Toolbox*, arXiv:2311.06402v1, and DO26, *A Simpler and
Faster Min-Cost Flow Solver via Min-Ratio Cycles from Distance Oracles*,
arXiv:2609.23852v1. In particular we use the forests, explicit spanner
routes, degree feedback, and actual edge-edit transcript. These are
stronger than a distance-only black box.

For a parent graph of size `m`, maximum degree `Delta`, and reduction
parameter `k`, the conservative one-level bounds used below are:

1. During a period of at most `n/k` parent edge edits, the child
   has size at most `O(m R/k)` and maximum degree at most `R`.
2. Over every prefix of `t` parent edits, the emitted child edge edits
   are at most `O(R t)`, including those needed to emulate a retained
   spanner vertex split. This is an amortized/prefix-total guarantee;
   an individual batch may be larger than R.
3. Here

       R = Delta^2 A,
       A = M^(4/K_sp+o(1)),

   with `K_sp` fixed. Enlarging the harmless `M^o(1)` factor absorbs
   logarithms, constant factors, and fixed powers of the source
   low-stretch parameter.
4. Parent forest components, local balls, clusters, candidate cycles,
   and explicit correction routes have the sizes stated by the local
   constructions. All local candidate maintenance can be bounded by
   `k^10 (Delta A)^40 M^o(1)` per edit and `m` times this quantity at
   initialization. This deliberately loose polynomial envelope is
   justified in Section 5.
5. The explicit flat-forest lift has stable physical vertex maps.
   To avoid relying on a sharp constant in its displayed recourse
   expression, we allow a factor `R^4 M^o(1)` for its congestion and
   local record changes. This dominates direct enumeration of the
   source's forest copies and their cut/root-merge changes.

The `Delta^2` bound is used even though the statement of KMPG
Theorem 3.1 claims the stronger linear-degree form. The literal
quadratic form is sufficient at the constant depth chosen here.

## 2. Fixed parameters and degree recurrence

The source's demand-route vertex congestion is not used to infer
physical occurrence multiplicity. A core can have `O(k Delta)`
parallel demands through one root, so its demand congestion may
contain a factor `k`. Such route/incidence work is local and fits
`W=k^10(Delta A)^40 M^o(1)`. Only selected spanner degree and the
emitted child-edit count must remain free of that factor. The
root-pool argument below supplies the separate occurrence bound.

Set

    k = ceil(M^eta),
    D = ceil(2/eta)+2,
    K_sp = ceil(2^(4D)/eta).

All three exponents/parameters are fixed before the graph is supplied;
only `k` depends on its size. The very large value of `K_sp` is an
asymptotic construction parameter, not an input-dependent advice string.
For sufficiently large `M`, the source condition
`K_sp=o(log^(1/6) M/log log M)` holds. For active subinstances of size
at least `k`, their logarithms are at least `eta log M`, so the same
eventual condition holds uniformly. Smaller instances are handled
directly.

Write `c=4/K_sp`. For the current hierarchy, let `Delta_i` bound the
degree of the level-`i` graph, and write `d_i=log_M Delta_i`. The
conservative recurrence is

    d_0=o(1),
    d_(i+1) <= 2 d_i+c+o(1).

Because `D,K_sp,eta` are fixed, every `o(1)` remains `o(1)` after at
most `D` such operations. Consequently

    d_i <= (2^i-1)c+o(1).

The accumulated graph-edit propagation exponent through level `j`
is at most

    sum_(i=0)^(j-1) (2d_i+c)
      <= (2^(j+1)-j-2)c+o(1).

Let

    theta = 2^(D+4)/K_sp.

Our fixed choice makes `theta < eta/1000` (with ample room). Therefore
for every `j<=D`,

    Delta_j <= M^(theta+o(1)),
    product_(i<j) R_i <= M^(theta+o(1)).

Allowing fourth powers in the flat-forest copy accounting gives at
most `M^(4theta+o(1))`. Thus a quadratic degree recurrence is harmless
at this fixed depth. No full-depth recurrence with
`D=(log M)^(1/21)` is asserted here.

## 3. Size decrease and stopping rule

Here `m_i=n_i+e_i` counts all actual resident input vertex slots and
edges; `n_i` includes retained isolated slots. Take `Delta_i>=1`. Since
`m_i <= (1+Delta_i/2)n_i`, a parent with
`m_i>4k Delta_i` can be restarted after

    Q_i = floor(m_i/(4k Delta_i))

edits, with `1<=Q_i<=n_i/k`. This respects the `n/k` horizon explicitly
stated in DO26 Lemma 4.1; it does not assume that its theorem supplies
an `m/k` horizon. Over one such period, its child's initialization size and
all subsequent births are at most

    m_(i+1) <= O(m_i R_i/k).

The [disconnected-component wrapper](disconnected_component_backend_wrapper.md)
keeps logical small-component roots but inserts child slots only as
endpoints of retained positive nonloop edges. Once inserted, an isolated
slot remains an actual child input vertex and is counted until parent
rebuild. Only private never-inserted activation records and completely
retired-instance metadata are excluded. Rebuild when the advertised
local period ends, even if
the actual graph has shrunk. Use the period's initial size as its
capacity bound, with a constant safety margin. The size recurrence
then gives

    m_i <= M^(1-i eta+theta+o(1)).

Stop and use a direct exact or crude cycle algorithm as soon as the
resident size is at most `4k Delta_i`. The hierarchy must have stopped before
depth `D`, since otherwise the displayed bound at `D` is eventually
less than one. There is no need to prescribe a negative or subunit
rebuild period for later levels.

This local-period implementation is the ordinary recursive rebuilding
version of the source hierarchy. It needs amortized time, which is
sufficient for the OAI numerical client. It does not require the
source's more elaborate worst-case rebuilding schedule.

## 4. Initialization and amortized edit recurrence

Let

    W = M^(10 eta+40 theta+o(1))

be a common upper bound on all one-level work, including the local
candidate lists and the flat-lift bookkeeping. The local factors
`Delta_i,A`, their fixed powers, and the `M^o(1)` spanner factors are
absorbed by the conservative `40theta+o(1)` term. Increasing the
absolute constant 40, if necessary, would not change any conclusion
or the fixed-parameter choice.

Initialization satisfies

    I_i <= O(m_i W)+I_(i+1).

Since each active child is eventually smaller by at least
`M^(eta/2)`, the geometric sum gives

    I_i = O(m_i W).

Let `T_i` be amortized processing time for one parent edit at level
`i`. A child edit costs `T_(i+1)`, and prefix-total recourse gives
`O(R_i)` such edits per parent edit amortized over the local period.
The child is rebuilt once per `Theta(m_i/(k Delta_i))` parent edits. Using the
initialization estimate, its amortized rebuilding cost is

    O(k Delta_i/m_i) I_(i+1)
      <= O(k Delta_i/m_i) * O((m_i R_i/k) W)
      = O(Delta_i R_i W).

The **current** one-level routine also needs to be rebuilt at this
horizon. Using the deliberately loose bound `O(m_i W)` for its
initialization charges another `O(k Delta_i W)` per parent edit.
This term must not be omitted. It could be reduced using the sharper
source `m_i k^4` initialization bound, but doing so is unnecessary.
Thus, after also charging retirement of the old instance,

    T_i <= O((1+k Delta_i+Delta_i R_i) W)+R_i T_(i+1).

Multiplying through at most `D` levels yields

    T_0 <= O_D(k W max_i Delta_i product_i(1+R_i))
        = M^(11 eta+O(theta)+o(1)).

The fixed factor `2^D` in `product(1+R_i)` is an asymptotic constant.
The same bound covers a query, because only a constant number of
selected local candidate types and the recursive selected candidate
need to be compared at each level; each selected explicit candidate
has the size bounded in Section 6.

For example, the relaxed common bound

    initialization M^(1+20 eta+o(1)),
    amortized edit/query M^(20 eta+o(1))

is sufficient. The construction does not depend on the numerical value
20; any larger fixed absolute envelope can be absorbed by choosing
`eta` smaller.

## 5. Why the local polynomial envelope is legitimate

The source primitive costs, before candidate maintenance, are bounded
by

    O~(m k^4 + m Delta^2 + m gamma_l)

at initialization and

    O~(k^4 + Delta^2 A gamma_l^(O(K_sp^2)) k^2)

per update. Because `K_sp` is fixed,
`gamma_l^(O(K_sp^2))=M^o(1)`.

In DO26 Lemma 4.1, the maintained pivot set shatters balls and inverse
clusters into size at most `O~(k Delta^2)`. A local ball neighborhood
therefore has at most `O~(k Delta^3)` vertices and
`O~(k Delta^4)` edges. A changed endpoint belongs to at most
`O~(k Delta^3)` such neighborhoods, by summing the inverse clusters
of it and its neighbors. Rebuilding each affected neighborhood's
minimum-spanning-tree fundamental-cycle list, even writing every
cycle explicitly by a naive tree-path scan, takes at most
`O~(k^3 Delta^10)` time per endpoint edit.

The source's additional forest cuts and pivot insertions have
`R`-bounded recourse and can be charged similarly; any more economical
implementation only improves this bound. The one-level envelope
`k^10 (Delta A)^40 M^o(1)` dominates these costs without relying on
sharp exponents.

Fundamental forest-cycle candidates have explicitly bounded component
size, and the source forests are decremental between rebuilds. Their
keys need to be inserted or deleted only on the explicitly reported
edge/forest events. Spanner correction candidates have explicitly
maintained routes of cardinality `gamma_l^(O(K_sp))=M^o(1)`; their
route-change records are part of the primitive's reported work.
Processing every such record and decomposing a selected correction
into sign-compatible simple cycles adds only a fixed subpolynomial
factor.

The flat-forest lift creates separate copies for the retained child
vertex occurrences. Directly allowing `R^4` rather than the sharper
printed bound covers the number of copies, the parent forest cuts,
and the at-most-degree-many root merge edits. Stable physical vertex
maps avoid rescanning a whole component when its root metadata
changes. These additional factors are independent of `k` except for
the already allowed local primitive work.

Lift initialization and parent-forest cuts can also depend on the
**descendant** occurrence cap, not only the current `R_i`. Section 7
bounds that cap by `product_(j>i) R_j^4 M^o(1) <= M^(4theta+o(1))`.
This factor is included in the common `40theta` margin in `W`.
Forwarding one child-forest edit itself causes only a constant number
of parent projected-edge edits; the replicated parent cuts are charged
separately. Thus the descendant cap does not introduce a new `k`
factor at each recursive level.

## 6. Quality: the local extraction factor occurs once

At each level, the independently checked ASZ/forest dichotomy and
spanner dichotomy lose at most `40 alpha rho`, where

    alpha=M^o(1),
    rho=gamma_l^(O(K_sp))=M^o(1).

They say that either a useful cycle is present in a local neighborhood,
in a fundamental forest cycle, in an explicit spanner correction, or
in the next graph. The recursion follows the last case only until the
first useful local candidate appears or the base graph is reached.

A local ball neighborhood has at most `O~(k Delta_i^3)` vertices.
The minimum-spanning-tree fundamental-cycle lemma loses at most this
number. A final graph of size at most `4k Delta_i` loses at most
`4k Delta_i`, or can be solved exactly. This is bounded by the same
`O(k max_i Delta_i^3)` envelope. Forest cycles are already simple. A selected explicit
spanner correction can be coalesced and decomposed into sign-compatible
simple cycles; its best component is at least as good as its net score.

The full approximation loss is therefore at most

    (40 alpha rho)^D * O~(k max_i Delta_i^3)
       = M^(eta+3theta+o(1)).

There is **one** factor `k max_i Delta_i^3`, not one per hierarchy
level. Placing it inside the `D`-th power would erase the desired
small exponent and does not describe the dichotomy proof.

The selected abstract cycle has at most
`M^(eta+3theta+o(1))` explicitly listed edges. It is simplified before
lifting. Each hierarchy edge lifts using at most `2D+1` forest-path
or physical-edge pieces, so the same exponent bounds the final answer
piece count.

The raw-lift note proves that the physical literal traversal length is
at most the sum of the abstract stored edge charges. Complete-cycle
gradient is preserved. Thus these are raw-certified answers, not an
unsupported conversion of a large implicit net circulation.

## 7. Exact gauges, contractions, and stable callbacks

Use a frozen potential `p_i` for each decremental core forest. Internal
core edges have the frozen value

    g_i(e)=g(e)+p_i(u)-p_i(v).

Do not discard the resulting gauge gradients on zero star links.
Instead, after sparsification and before contracting aliases, correct
each retained positive edge with physical roots `a,b` to

    h_e=g_i(e)-p_i(a)+p_i(b).

This subtracts the potential `p_i(a)` on the alias `(a,i)`, and zero
on its star center. Every zero star link then has gradient zero.
Contraction preserves circulation gradients, and every positive child
edge has the literal parent root-leg gradient. The parent length
upper bound and spanner distances are unchanged.

The correction is `O(1)` per already-emitted retained edge lifetime.
Frozen potentials and persistent physical roots imply that it changes
only with root endpoint/provenance edits or instance rebuilds; those
edits are already included in `R_i`. There is no scan over the
unsparsified core's `O(k)` incidences. The recursive graph has strictly
positive lengths, exactly as required by the source distance primitive.

Keep edge-copy IDs, parent-edge IDs, core-copy indices, and root IDs.
Before cutting a representation or retiring its physical metadata,
flush both signed motion and accumulated absolute motion. Birth and
retirement callbacks are charged to the forest copy and edge recourse
above. The KMPG flat-lift construction keeps each physical vertex image
fixed for its lifetime.

Over at most `D` levels, occurrence multiplicity and occurrence edits
are bounded by fixed powers of `product R_i`, hence by
`M^(O(theta)+o(1))`. A few auxiliary copies of a level forest contribute
only another fixed-depth polylogarithmic factor.

More explicitly, let `C_i` be a cap on the number of retained vertex
occurrences having the same level-`i` image, counting isolated and
auxiliary copies as well as incident vertices. The copy construction
can use the conservative recurrence

    C_i <= R_i^4 (C_(i+1)+polylog M) M^o(1).

We pass this explicit vertex cap when allocating copy pools; we do not
infer it solely from edge congestion, which would overlook isolated
occurrences. For ordinary non-rebuilding edits, if `E_i` is the number
of flat-forest record edits per level-`i` input edit, a sufficient
recurrence is

    E_i <= R_i E_(i+1)+R_i^4 C_(i+1) M^o(1).

The first term forwards child edits. The second pays for replicated
parent forest cuts, root-identification edits, and isolated births.
At the terminal graph, candidates are returned as explicit edge lists;
their private spanning tree is not added to the maintained flat lift.
Thus `C_base,E_base=O(1)` for this representation recurrence. The
`O(k Delta)` candidate-list work is already included in `W` and in the
answer-piece bound. Solving gives
`C_i,E_i=M^(O(theta)+o(1))`. Complete rebuilds birth or
retire `O(m_i C_i)` records and are charged by the already included
`k Delta_i W` term. This makes explicit why no extra `k` factor is
multiplied at every level merely to maintain the flat representation.

## 8. Arithmetic and use in the matching construction

Each child length is at most the current vertex count times its parent
length upper bound. With constant `D`, polynomial root data remain
polynomially bounded with an exponent depending only on the fixed
parameters. The frozen potentials and corrected edge gradients are
sums of polynomially many such bounded entries. Exact rational or
scaled-integer arithmetic therefore uses `O_(a,D)(log M)` bits.
The large fixed `K_sp` affects constants, not the input bit exponent.

For example one may take `eta=1/(10^6 a)` and then fix `D,K_sp` as
above, enlarging the constant `10^6` if a chosen implementation uses a
larger absolute local-work envelope. The quality, piece, occurrence,
and edit factors then fit the OAI client's polynomial slack budgets
for every sufficiently large input at this fixed `a`. Its existing
guard/fallback mechanism handles finite exceptional sizes without
turning a suspension into LOW.

The additive numerical phase exponent can consequently be made
arbitrarily small at a fixed parameter. For the historical
`O~(m n^(1/3))` composition, choosing it below `1/6` suffices.
The current persistent-carrier construction instead has near-linear
structural work and uses this backend to obtain the fixed-branch
bound `N^(1+O(1/a)+o_a(1))`. The integration note composes those
branches with independent final matching verification to obtain
the proposed uniform bound `O(n+m)+(m_s+1)^(1+o(1))`.
The backend itself changes no structural matching operation.

## 9. Dependency statement

This route still uses the constructive local KMPG distance/sparsifier
algorithms, their explicit routes and forest-copy construction, and
the fixed-parameter OAI numerical client. The independent additions
are the raw-cycle normalization/lift argument, the retained-edge gauge
correction, and this conservative constant-depth accounting. It does
not assume that the reversed inequality printed in DO26 Lemma 5.4 is
correct, nor that its displayed local extraction factor is incurred
at every level, nor that its full-depth squared-degree recurrence is
subpolynomial.


Primary sources:

* <https://arxiv.org/abs/2311.06402v1>, especially Theorem 3.1,
  Lemma 3.5, Algorithms 2--5, Claims 3.17--3.18, and Lemma 3.21.
* <https://arxiv.org/abs/2609.23852v1>, especially Lemmas 3.23,
  4.1--4.3, Theorem 4.5 and its proof, and the hierarchy/lift discussion.
