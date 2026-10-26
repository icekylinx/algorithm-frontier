# Audit of the public-provider flat-forest spanner comparison

**25 October 2026. Passed with the explicit common adapter below.**

This audits Section 8 of [dynamic spanners proof](../../problems/dynamic-spanners/proof.md).
The comparison is a reconstructed public APSP provider **plus the same
tracked-terminal/short-path observer and an explicit elementary extension
of the public forest-copy construction**. It is not a printed spanner
theorem, and a numerical distance oracle alone does not imply the needed
flat forest interface.

The primary source is [KMG, *A Dynamic Shortest Paths Toolbox*,
arXiv:2311.06402v1](https://arxiv.org/pdf/2311.06402v1): Theorem 3.2,
Claim 3.9, Lemma 3.10, and Lemma 3.21 / Definition 3.22 / Algorithm 5.
The Algorithm 5 proof is on source pages 30--32. The provider's quantitative work and recourse are derived in the [public APSP reconstruction](public-apsp-joint-retuning-audit.md).

## 1. Local witness families are source-supported

The public center construction controls both strict balls and their
inverse clusters. The exact local path inventory, not merely a numerical
distance label, is maintained by Lemma 3.10. A physical native vertex
therefore belongs to only `k^{O(1)} poly(U)` strict-ball shortest-path
trees. Positive shortest paths to vertices inside a strict ball stay in
that ball. The nearest-pivot forest contributes one additional native
copy. An actual-size exact base contributes `k^{O(1)} poly(U)`
source trees.

The small disconnected-component completion must explicitly retain its
local exact trees as well as its distance table. Until activation those
trees answer the local queries; no nonexistent recursive pivot handle is
assumed. This has the same fixed-polynomial `k` allowance.

Each family is born at one level and lifted through its ancestors. Its
`k^{O(1)}` local occurrence is not multiplied anew at every ancestor.
The static local-path inventory and all actual native edits are paid
in the public provider's work bound.

## 2. What Algorithm 5 really supplies

Algorithm 5 allocates copies `T_(v,j)` of a direct sum of native core
trees rooted at `v`. It assigns a separate slot to **every** input
forest node at `v`, not just to designated original terminals. A real
input edge is represented by its core provenance's literal native
edge between the corresponding assigned tree copies. Contracting each
assigned copy to its root recovers the input forest. Thus the actual
construction represents paths between any two assigned input-node
roots.

Its printed slot count is obtained by converting edge congestion to
node congestion using degree. A direct bound on the number of input
node occurrences is sufficient instead, as proved in
[public-forest-direct-vertex-inventory.md](public-forest-direct-vertex-inventory.md). Isolated input nodes must
be included explicitly; their bound cannot be inferred from edges.

The distinguished root is available for each live node occurrence.
An observer can attach its owner tag there without marking all pool
copies of the same physical vertex. The source's constant maps and
slot assignment, with the core-cut bookkeeping in
[public-strong-forest-marks-anchor-focused-audit.md](public-strong-forest-marks-anchor-focused-audit.md), give the required
current handles.

## 3. Required positive-port adapter: use independent roots and zero links

The numerical public hierarchy applies positive binary-tree degree
reduction at recursive boundaries. Its connector edges project to a
single vertex of the selected graph `H`. The printed flat-embedding
contract of Lemma 3.21 does not itself represent such a projected
connector. The following elementary extension is therefore an explicit
dependency of the comparison.

For each incoming forest node `y`, first project its native port image
to the corresponding selected vertex `v` of `H`, and give `y` its
own assigned copy `T_(v,j)`, with distinguished root `eta(y)`.
Process incoming edges as follows:

* a real selected edge uses its original Algorithm 5 projected native
  edge between its two assigned copies;
* a port connector, or an already-null incoming edge, becomes a
  zero-length link between `eta(y)` and `eta(z)`.

The latter endpoints have the same physical parent image. They are
distinct allocated forest nodes, since the two incoming nodes have
distinct assigned copies. The link therefore records a null physical
step without identifying their owners.

Contracting the independent assigned tree copies recovers the complete
incoming forest, including its connector edges. The output is a forest.
Real-edge routes have the public core-edge metric upper bound; zero
links have zero length, no larger than their incoming nonnegative
connector length divided by the positive inter-level scale. This
proves the arbitrary-path metric inequality needed by the observer.

This extension uses the public full-tree-copy mechanism. It does not
use the new uncontracted colored pool, a compressed selected core, or
the normalized repair algorithm. It should nevertheless be identified
as an added elementary adapter, rather than attributed verbatim to
Lemma 3.21's printed flat-edge contract.

### Why quotienting incoming connector components is not enough for time

A tempting alternative is to contract those components before invoking
the original lemma. A single incoming connector cut can then split a
quotient vertex with `Theta(PG)` incident owner records. Explicitly
retargeting them for every child forest edit can introduce an unwanted
`G` multiplier into recursive work. The present comparison does not
use that argument.

With independent assigned roots, an incoming forest edge insertion or
deletion changes only one projected edge or zero link. Its cost is
`poly(U)`, independently of the full occurrence budget `G`.
Only changes of the native core forests are replicated through all
assigned copies.

## 4. Live slots, retirement, and the linear occurrence recurrence

The selected degree before a recursive port expansion is bounded by
`P^{O(1)}`. If the incoming forest has at most `G` occurrences at
each current native port, its current node population above any
selected vertex of `H` is at most `P^{O(1)}G`. The full-copy slot
capacity and direct vertex inventory consequently give

$$
G_{parent}\le P^{O(1)}(G_{child}+1).
$$

This is a bound on live owners, including full currently allocated
unused pools. It is not a bound on the number of port names ever born.
After a temporary input node becomes isolated and permanently retires,
remove its observer tags, release its slot, and remove its input owner
record. The unused assigned pool copy can remain available for reuse.
Likewise, copies of a permanently retired native port are isolated;
retire those exported forest-node records instead of forwarding them
forever as additional owners at an ancestor.

These operations do not invalidate any surviving input-node path.
They are isolated-node retirement and free-slot bookkeeping. Original
query handles that remain live are never released. Retiring a native
port may touch its `G` actual copied occurrences, which is a native
update charge; each resulting child forest log is still processed
once by the ancestor interface. Keeping every retired alias as a new
owned full-tree copy would invalidate the displayed recurrence and is
not permitted.

For a native core edit, the full copies cost
`P^{O(1)}(G+1)` actual forest edits and work. For an incoming forest
edit, the work is only `poly(U)` per explicit log. A native primitive
is computed once and its result is copied; its construction factor
`F` is not recomputed separately inside every forest copy. Together
with the initial child-credit term, this is the separation needed to
charge

$$
B_{public}=O(x+f+K^2g+d\log P+h).
$$

It does not introduce `d^2 log P`, `k^d`, or one additional copy of
`F` per hierarchy depth.

## 5. Tracked marks and the quantitative comparison

The tracked native sets contain at most the original `n` query traces
per level. A source's local tree has `k^{O(1)} poly(U)` vertices.
Marking its distinguished input-node handles therefore gives
`n k^{O(1)} poly(U)` active marks over all lifted local families,
independently of the number of unmarked pool vertices.

The same marked-Steiner compression and short-edge exposure observer
can now be applied. It adds only its stated local mark work and one
factor equal to the exposed path-length cap. For the public family,

$$
B_{public}=O(U/t+t^6h),\qquad
 A_{public}=O(t^5h),\qquad x=\Theta(U/t).
$$

The logarithmic time and output-density allowance is
`O(B_public+A_public+x)`. At `t=Theta((U/h)^(1/7))` it is
`O(U^(6/7)h^(1/7))`, with logarithmic stretch
`O(U^(5/7)h^(2/7))`. At the same stretch scale, the research
provider with the same observer has the smaller `23/28` time and
density point. At the looser balanced `4/5` stretch cap, this public
`6/7` point also qualifies and should be included in the comparison.

These conclusions compare two named provider constructions under the
same explicitly described observer and elementary zero-link adapter.
They are not a lower bound on public algorithms or a claim of a
globally fastest dynamic spanner. The elementary alternative of
retaining the whole input graph must also be used whenever it fits
the permitted output size.
