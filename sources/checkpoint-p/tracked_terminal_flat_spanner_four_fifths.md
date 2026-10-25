# A direct dynamic spanner from tracked terminal forests

**Research proof assembly, 25 October 2026. Root and independent
mathematical audits completed.**

This note constructs a deterministic fully dynamic spanner with explicit
four-fifths overhead, by using the already maintained flat witness
forests of the numerical APSP hierarchy. Its output recourse depends
on insertions as well as deletions. It therefore complements, rather
than supersedes, the five-sixths low-recourse construction in
`fully_dynamic_spanner_five_sixths.md`.

The bound, for an arbitrary-degree unweighted undirected
graph on `n` fixed vertices, is

\[
 \begin{array}{ll}
 \text{stretch}&\exp O(U^{4/5}h^{1/5}),\\
 \text{current output edges}&n\exp O(U^{4/5}h^{1/5}),\\
 \text{initialization and total update work}
   &(n+m_0+I+D)\exp O(U^{4/5}h^{1/5}),\\
 \text{safe total output-recourse bound}
   &(n+m_0+I+D)\exp O(U^{4/5}h^{1/5}).
 \end{array}                                                \tag{T1}
\]

Here `m_0` is actual initial input size, `I,D` are insertions/deletions
over a polynomially bounded history, `N` is its declared master cap,
`U=log(N+4)`, and `h=log(U+4)`. Distinct edge lifetimes and parallel
edges have distinct identifiers. Self-loops can be ignored. Queries
and the output see settled external updates. No worst-case update
claim or recourse bound independent of `I` is made.

The construction does not union every edge in every allocated flat
forest. Such a union can depend on the `Theta(m)` native port vertices
in an arbitrary-degree input. Instead it marks only the at most `n`
original query traces at each level and outputs short compressed
paths between their marks.

## 1. Retained hierarchy and forest family

Use the already audited normalized positive-port numerical hierarchy
from `apsp_time_stretch_tradeoff.md`. With parameter `t`, it has

\[
 \begin{aligned}
 p=r&=\Theta(t),\quad K_{\rm repair}=\Theta(t^2),\quad
 k=2^x,\quad x=\Theta(U/t),\quad d=O(t),\\
 B&=O(U/t+t^3h),\qquad
 \log\gamma_{\rm native}=O(t^4h).
 \end{aligned}                                             \tag{T2}
\]

Its arbitrary-degree root adapter is a current-incidence balanced
binary tree for each original vertex. Connectors have length one;
an original unweighted edge has native length `H=poly(U)`, a fixed
power of two. Only the original `n` vertices have permanent query
handles `q_v`. For original endpoints,

\[
 d_G(u,v)\le H^{-1}d_{G_0}(q_u,q_v)\le2d_G(u,v).       \tag{T3}
\]

The root native graph can contain `Theta(m+n)` port vertices. That
inventory is paid by initialization and the actual update history,
but it is not used as the spanner's terminal count.

At each level `i`, retain the following native forest families:

1. the exact nearest-pivot forest `N_i`;
2. a shortest-path tree rooted at every native vertex on its strict
   pivot ball, including the root;
3. at an actual-size base, one exact shortest-path forest per source;
4. the exact local shortest-path trees used to answer queries within
   an initially small untouched component.

The last family is explicit even where an untouched component is
answered by a local exact table instead of the ordinary strict-ball
termination. Such a component has fewer than `k` edges, so these
trees cost only another fixed polynomial in `k` locally.

Lift each family from the level where it is born through its ancestors
to the root native graph `G_0`. Keep all typed null edges; do not
contract away different input-vertex handles at an intermediate or
final forest. Each native forest node `y` has a stable current handle
`eta_i(y)` in its flat root forest. The flat forest's other nodes may
include full unused pools and historical isolates. They are all paid
for in working storage and maintenance.

The explicit proof of these families, their pointwise occurrence,
and their full maintenance is
`destructive_apsp_path_support_extractor.md`, Sections 2--2.2, with
`destructive_apsp_independent_audit.md`. The extra local exact family
in item 4 has the same `k^{O(1)} poly(U)` bound. Its generic lift
recurrence is `G_parent <= P(G_child+1)`, and each local family is
lifted once from its birth level. The factor `k^{O(1)}` is not
multiplied once per hierarchy depth. Total work and explicit flat
forest edits, including initial credit and all unused pools, fit

\[
                     (n+m_0+I+D)\exp O(B).              \tag{T4}
\]

The weights on a flat forest are the lengths of its real `G_0` edge
copies and zero on its typed nulls. They are exact integers. If a
native forest path is born at level `i`, the length of the path
between its lifted endpoint handles is at most its native length
divided by the cumulative inter-level port scale `sigma_i`.
This is the arbitrary-forest metric inequality in
`separated_metric_forest_and_strong_sssp.md`, Section 5.

## 2. Track only original-query pivot images

Set

\[
                         S_0=\{q_v:v\in V(G)\}.        \tag{T5}
\]

This contains `n` handles, not all root port vertices. For a level
whose nearest-pivot component is active and exposes its pivot in the
child, propagate a tracked native vertex `w` to the child query
handle of `p_i(w)`. Let `S_{i+1}` be the **set** of these propagated
handles. Duplicate images count once. Thus

\[
                            |S_i|\le n                 \tag{T6}
\]

for every level. This is only a query-tracking set. Adding its marks
does not promote new centers, modify native graph edges, or rebuild
the numerical hierarchy.

An initially small untouched component may have a private common
pivot `r_C` with no recursive child handle. Do not propagate it.
Queries involving this component terminate in the appropriate local
exact trees, or return infinity to a different untouched component.
Its first real activation, including a forced activation if used by
the native interface, exposes the old pivot before ordinary updates
and then enables propagation. This is the same small-component rule
as the audited component wrapper, not an assumption that private
handles already exist in the child.

### 2.1 Boolean component aggregates

Maintain a mark at each member of `S_i` in the native nearest-pivot
forest `N_i`. Each component stores the number of such marked
vertices, its designated pivot, and whether the pivot has an exposed
child query handle. Its output contributes exactly one Boolean mark
to `S_{i+1}` when that count is positive and the handle exists.

A single membership insertion/deletion in `S_i` changes only its
component's count. It causes at most one next-level membership event.
A native forest cut, link, root change, singleton birth/death, or
exposure-state change affects only constantly many components and
causes only constantly many next-level events. Ordinary dynamic-tree
component aggregates perform these operations in polynomial-logarithmic
time. Retain handle reference counts if an implementation exposes
coincident aliases; then a contribution changes set membership only
on a zero-to-one or one-to-zero transition.

If `b_i` counts changes to `S_i` and `l_i` is the complete native
nearest-pivot/root/exposure transcript at level `i`, the safe total
propagation bound is

\[
                       b_{i+1}\le b_i+O(l_i).           \tag{T7}
\]

The coefficient on the propagated membership events is one: a set
mark changes only one component count and can toggle only that
component's one output. There is no `k b_i` term. Summing (T7)
over depth loses at most a factor `O(d)`. The native transcripts are
already charged in (T4). A period replacement removes old traces
and initializes new ones from its actual forest inventory, also
charged there. Initial small isolates do not allocate absent child
handles just to propagate a mark.

A native update transcript need not have exactly one pivot in every
intermediate component. For its observer, store both the component's
`S_i` mark count and its minimum currently eligible exposed-pivot ID.
Temporarily use that minimum as the component's one output, or no
output if there is none. Cuts, links and eligibility/root flags change
only constantly many component contributions. A mark toggle still
changes at most one output, since the pivot choice is independent of
that count. At a settled state the nearest-pivot component has its
unique actual pivot, so this temporary rule agrees with the intended
trace. The number of contributing components never exceeds the number
of `S_i` marks, preserving (T6) even during observer processing.

Enable an exposure flag only after the child's query handle and its
observer node exist, and disable it before that handle retires. Local
ball/base source trees may be created later in the same transaction;
their node-birth handler reads the current active-source flag and adds
the corresponding marks then. These are observation events only and
do not feed temporary pivots back into the native algorithm.

## 3. Marks in the flat witness forests

Use the stable handle of each selected native forest node in its own
flat root forest. The active marks are as follows.

* In the lifted nearest-pivot forest born at level `i`, mark every
  vertex of `S_i` and each of their nearest pivots. This has at most
  `2n` distinct marked handles.
* In the strict-ball tree rooted at `w`, activate that tree exactly
  when `w` belongs to `S_i`. If active, mark **all** of its native
  tree vertices at their lifted handles.
* Apply the same rule to a source's exact base tree or exact untouched-
  component tree when that local termination is available.

No distance threshold is used to decide which source is active or
which of its tree vertices is marked. In particular, changing a root
distance does not trigger a bulk search for vertices whose path has
just become short. The length test will be applied to compressed
forest edges instead.

Each strict ball and each local exact component has `k^{O(1)} poly(U)`
vertices. The actual-size base has the same bound. Thus the total
number `Q_mark` of active marked handles, over the disjoint forest
family at all levels, obeys

\[
                   Q_{\rm mark}\le n k^{O(1)}
                                        \operatorname{poly}(U). \tag{T8}
\]

The bound counts marks separately when they occur in different flat
forest copies, even if their physical images agree. Root native ports
that are not on a tracked tree need not be marked. All unused pool
vertices remain allocated and charged as working records; (T8) makes
no assertion that their number is small in terms of `n` alone.

### 3.1 Mark-update work and stable lifted handles

A change of membership in `S_i` activates or deactivates at most
`k^{O(1)} poly(U)` current tree nodes. Iterate the actual tree nodes,
not a padded `k`-sized table. The local forest family is already
maintained for every native source; changing an active source does
not construct an additional recursive hierarchy or alter a native
pivot set. A native tree-node birth/retirement creates/removes one
active mark if its source is active. Ordinary tree-edge changes are
handled by the flat-forest transcript and do not require enumerating
all marked vertices in a component.

The generic forest lift supplies one distinguished root handle for
each living input node. Carry that node's owner tag along this
distinguished handle, not to every auxiliary pool copy. A forest-
period replacement retires old handles and creates new ones through
explicit node records. Remove marks on retiring handles before their
isolated-node retirement; after the current native traces are settled,
insert the required marks at the new current handles. No live marked
node silently changes its image or identity.

Observe **canonical-owner claim and release events** as well as physical
flat-node births and deaths. Releasing an input node's pool index may
leave that pool root allocated as an unused ghost. Its old owner's
mark is removed at release, even though the physical forest-node
record survives. Reusing the index installs the new owner only after
the old mark and tag have been removed. These are constant-size events
already supplied by the input-node lifetime and pool-assignment logs;
they do not require scanning the full pool. Current distinguished
handle lookup through the hierarchy takes `poly(U)` time.

Combining (T7), the native family transcript, and this local cost,
the total active-mark transcript and bookkeeping fit

\[
                       (n+m_0+I+D)\exp O(B).             \tag{T9}
\]

Multiplication by a fixed polynomial in `k` only increases the fixed
coefficient of `x` already in `B`. Propagation depth contributes a
polynomial in `U`. There is no repeated `k` factor for a single mark
at every level. The marks are observers of the maintained numerical
and forest structures, so no feedback loop turns this observer work
into additional native updates.

## 4. Maintain marked Steiner subtrees and expose only short edges

For every flat root forest `T`, maintain the minimal subtree spanning
the active marks in each of its components. Remove unmarked branches
and suppress unmarked degree-two vertices. A compressed edge represents
the full forest path between its retained endpoints. Store its exact
root-native path length.

The local construction and proof are
`dynamic_marked_forest_short_path_union.md`. They apply to arbitrary
forest cuts, links, mark changes and nonnegative length changes, not
only decremental forests. Each such operation changes `O(1)` compressed
records in polynomial-logarithmic structural work. In particular:

* inserting a mark uses the first previously assigned virtual-edge
  ID on its path to any old mark to locate the attachment point;
* a cut affects at most one old compressed path and its endpoints;
* a link between two marked components is handled by temporarily
  marking its endpoints, linking them, and removing those temporary
  marks; if one side has no marks the old marked subtree is unchanged.

These operations use lazy path IDs and path sums, not traversal of
long unused paths. Zero-length typed-null edges cause no difficulty
for the topological compression. Path enumeration has a separate
physical-edge aggregate and skips all nulls and root port connectors.

Set

\[
 \Gamma=2\gamma_{\rm native},\qquad
                         R=\lceil H\Gamma\rceil.       \tag{T10}
\]

Expose exactly those compressed edges whose root-native length is at
most `R`. Their output lists contain only original physical edge IDs,
not native port connectors. A physical original-edge occurrence has
root-native length `H`, so such a list has at most `R/H` occurrences;
the weaker bound `R` will suffice. Repeated IDs are allowed in a list
and are charged with multiplicity. Typed nulls and port connectors
are skipped without individually enumerating them.

A short record caches its full physical list. Retire that cache using
old metadata before its path disappears or changes. A long record
has no expanded cache. A record crossing the threshold has its old
cache retired and/or its new short path enumerated. Global reference
counts over these lists maintain a literal subgraph `H_out` of the
original graph. Only zero-to-positive and positive-to-zero reference
changes alter the published edge set.

The root forest replica and its compression consume the chronological
flat edge/node logs. They can retain the pre-update state needed to
retire a cache even if the provider has already computed the new
state. No query or output publication occurs midway through that
transaction. Native exposed paths use only currently living physical
edges at the settled state, so `H_out` is then a subgraph of `G`.

## 5. Why every original edge is represented

Fix a living original unweighted edge `uv`. By (T3), the numerical
query on its two root handles has estimate at most

\[
 \widehat d_{G_0}(q_u,q_v)
       \le\gamma_{\rm native} d_{G_0}(q_u,q_v)
       \le2H\gamma_{\rm native}\le R.                  \tag{T11}
\]

Its witness is a concatenation of native nearest-pivot legs and one
terminal strict-ball, base, or untouched-component exact path. The
appropriate cumulative port scale divides each native leg length.
All contributions are nonnegative. Each constituent's root-flat
path therefore has length at most the total estimate in (T11).

The two endpoints of every constituent are marked:

* every visited pivot-chain vertex is in the corresponding `S_i`;
  its nearest-pivot leg has both endpoints marked in the lifted `N_i`;
* the terminal exact source belongs to `S_i`, and every native node
  of its relevant local tree is marked, including the target.

An untouched-component termination is covered by the explicit local
exact family; no missing child pivot handle is required. Disconnected
pairs are irrelevant to (T11), since `uv` itself is living.

In a forest, the path between two marked vertices lies in their
minimal marked subtree and is a concatenation of whole compressed
edges. Each compressed edge on this path has nonnegative length at
most the entire path length, hence at most `R`. Every one is exposed
by Section 4. Consequently `H_out` contains every original physical
edge in the projected constituent paths.

The constituent root paths have compatible physical endpoints even
when their forest copies use distinct auxiliary handles. Concatenate
their physical projections, delete null/connector steps, and obtain
a `u`-to-`v` walk in `H_out`. Its original length is at most
`R/H`, or at most `Gamma` by using the unrounded bound (T11).
Loop erasure cannot increase this length. Replacing each edge on an
original shortest path proves that `H_out` is a `Gamma`-spanner.

This proof does not require maintaining the actual query answer for
every input edge. It is an existence argument using all marked short
compressed paths, and it works for every current original edge at
the same time.

## 6. Size, actual work, and ordinary recourse

A forest with `q` marks has `O(q)` compressed vertices and edges,
summed over its marked components. Components with no marks contribute
nothing; a component with one mark contributes an isolated vertex.
By (T8), the number of candidate compressed paths is at most
`n k^{O(1)} poly(U)`. Every exposed path contributes at most `R`
physical occurrences before deduplication. Hence

\[
                    |E(H_{\rm out})|
                      \le n k^{O(1)}R\operatorname{poly}(U).
                                                               \tag{T12}
\]

This is where the number `n` rather than the root native port count
enters. Long compressed paths and full unused forest branches are not
expanded into the output. They remain working records whose actual
maintenance was paid in (T4).

Initialize the compression by a linear scan of each actual allocated
flat forest, followed by enumeration of its short compressed paths.
The flat inventory has its already charged `exp O(B)` allowance.
Thereafter each flat-forest or mark operation changes constantly many
compressed records. Updating a short record costs
`(R+1) poly(U)` for cached retirement and current physical enumeration;
updating a long record uses only polynomial-logarithmic structural
work. A change of length has the same bound. Equations (T4) and (T9)
therefore give total work

\[
             (n+m_0+I+D)\exp O(B+\log R).               \tag{T13}
\]

The same expression safely bounds total output recourse, since every
actual edge insertion/deletion in the output is charged to a reference
operation already paid in that work. An initial published output has
only the `n`-based size (T12), but the provider's initial selected
credit may cause forest changes later. Without another amortization
argument, `m_0` must not be removed from the safe total recourse bound.
For an initially empty graph it becomes `(n+I+D) exp O(B+log R)`.

When an entire numerical or forest period is replaced, retire its old
marked handles and cached short records through their old metadata,
then initialize the new actual inventory. Old and new private objects
can be processed sequentially before publication. This replacement is
part of the actual forest/mark transcript; it is not an uncharged
global sweep of every original vertex after each input update.

All labels are exact root-native integer path lengths or zero.
Dynamic-tree path sums use polynomially many bits in `U`, as do all
hierarchy length labels. `R` may be rounded upward to a concrete
integer or power-of-two bound; constants in the approximation absorb
that rounding. Only a physical original-edge occurrence of positive
length contributes to a path cache. Thus no zero-length chain or large
numerical original edge weight creates an uncharged enumeration.

The root degree adapter emits polynomially many elementary changes
per original update. The total generated hierarchy inventory and
transcript are the actual input history times a subpolynomial factor.
A fixed polynomial increase of the master cap covers them; it changes
`U` only by a constant factor. No absent local instance is padded to
the global cap.

## 7. Explicit parameter points

For the family (T2), `log R=O(t^4h+h)` and
`log k=Theta(U/t)`. Both size and work in (T12)--(T13) have
logarithmic overhead

\[
                     Z=O(U/t+t^4h),                    \tag{T14}
\]

while the logarithmic stretch is `O(t^4h)`. Taking

\[
                         t=\Theta((U/h)^{1/5})         \tag{T15}
\]

gives `Z=O(U^{4/5}h^{1/5})` and proves (T1).
The source shrink guard has slack: `x=Theta(t^4h)` dominates
`log P=O(t^3h)` for these choices. Its local construction and positive
port parameters are exactly within the previously audited normalized
APSP range. The observer adds only fixed powers of `k`, so it does
not require a deeper or differently parameterized numerical hierarchy.

There is also a finer-stretch point. Put

\[
 A_0=U^{5/7}h^{2/7},\qquad
                  t=\Theta((U/h)^{5/28}).
\]

Then logarithmic stretch is `O(A_0)`, and logarithmic time and
output-density overhead are

\[
                         O(U^{23/28}h^{5/28}).          \tag{T16}
\]

The permitted density is larger than just `n exp O(A_0)`: tracking
all local tree vertices pays `k^{O(1)}`, whose logarithm is
`Theta(U/t)`. That factor must not be hidden when comparing this
direct construction with the deletion-bounded or low-recourse spanner.

## 8. Scope and comparisons

The five-sixths construction has the stronger total recourse bound
`(n+D) exp O(U^{5/6}h^{1/6})`. The present direct construction may
change output edges after an insertion, and claims only the ordinary
total recourse in (T1). It offers a lower balanced time/stretch/density
exponent, with a different recourse contract.

For a fair provider comparison, the same elementary tracked-terminal
and short-compression observer can be applied to the reconstructed
public APSP hierarchy, using its original full-forest copy lift and
the positive inter-level adapters. Its local ball/base families have
the same `k^{O(1)}` occurrence bound. The work recurrence substitutes
the public local repair factor and retains the initial child credit,
giving

\[
                  B_{\rm pub}=O(U/t+t^6h),\qquad
                  A_{\rm pub}=O(t^5h).                 \tag{T17}
\]

The original KMG arbitrary-forest copy construction supplies a handle
for every input forest-node occurrence, including auxiliary nodes;
its contraction proof preserves their paths. The argument does not
need all those occurrences to be distinct designated original
terminals. Copies and degree-reset aliases are fully counted in the
`P`-per-level lift bound. This comparison does not use the new
uncontracted colored-pool construction to improve public work.

The inter-level port conversion uses an explicitly named **plain-copy
zero-link extension of public Algorithm 5**. Assign every incoming
forest-node occurrence its own `T_v` copy, even when several current
port aliases project to the same native root `v`. A real incoming
edge uses the original physical endpoint attachments. A port connector
or immediate true-null edge becomes a zero-length link between the
two assigned roots. Contracting all assigned trees recovers the
incoming forest exactly, so the result is a forest with the required
path domination. A child edge log changes only `O(1)` connecting
records; a native stable-forest edit is the separate charge of
`P(G+1)` copied records. Releasing an incoming owner promptly frees
its assignment slot and observer mark, even if the unused physical
pool remains allocated. Historical retired aliases are not counted
as new current owners. This is an elementary common observer adapter
spelled out in the present reconstruction, not a claim that the printed
Lemma 3.21 already states the expanded typed-null contract.
The focused completed check is
`tracked_terminal_spanner_public_flat_comparator_audit.md`.

The public observer's safe overhead is `O(B_pub+A_pub+x)`, which
is minimized at `t=Theta((U/h)^{1/7})`. It yields logarithmic
time and output-density overhead `O(U^{6/7}h^{1/7})`, at
logarithmic stretch `O(A_0)`. At that same stretch scale, (T16)
has the smaller `23/28` time and density envelope. At the looser
balanced four-fifths stretch cap, the public six-sevenths point
also qualifies, although its actual stretch guarantee is finer.
These are derived compositions with the same observer, not printed
spanner theorems or a claim of an optimized public frontier.

The elementary alternative `H_out=G` is already superior whenever
the entire living graph fits the allowed output-size cap. The new
construction is significant in denser regimes, for example a graph
that may contain `n^{1+epsilon}` edges for fixed `epsilon>0`, while
the output is constrained to `n exp O(U^{4/5}h^{1/5})`. The current
primary-source baseline checks are in
`dynamic_spanner_public_baseline_audit.md`; exact stretch, density,
randomness, and update model must remain visible in comparisons.

Positive polynomial-range weighted graphs follow by independent
unweighted dyadic length classes, adding polynomial logarithmic
factors and a factor two in stretch. Clipped root caps and caches
refer to each unweighted class, not to the numerical magnitude of
its original edge weights.

## 9. Proof dependencies and completed audits

The numerical hierarchy, normalized static provider, local source
families, and arbitrary-forest lift are retained research imports.
The new ingredients assembled here are the original-terminal trace
observer, its root mark inventory, and the short compressed-path
union. The local compression proof is separately written in
`dynamic_marked_forest_short_path_union.md`.

The full tracking, canonical-handle, source-family, and update-count
interfaces have passed the independent audit in
`tracked_terminal_flat_spanner_independent_audit.md` and the root
audit in `tracked_terminal_flat_spanner_root_audit.md`. The separate
public-provider comparison is checked in the focused audit named
above. These are internal mathematical reviews of a research proof
assembly, not formal verification, external review, or performance
measurements. No claim about exact matching or insertion-independent
recourse follows from the four-fifths spanner point.
