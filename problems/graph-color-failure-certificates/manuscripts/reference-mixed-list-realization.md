# Exact mixed and list-color realization with compressed features

The [native reference](../reference/list_colors.py) extends the existing
single-vertex-color backend to overlapping vertex lists, additional edge
lists, the symmetric-cubic single-color refinement, and completed-batch
single-failure difference reports. This note proves its original-input
interfaces and audits Sections 6–9 of the
[canonical manuscript](colored-graph-and-vertex-failure-certificates.md).
Its exact reference MSF updates are separate from the published fast
dynamic-MSF data structure.

## 1. Original records, failures and exact queries

`build(vertex_colors,edges,failures,modulus=None)` accepts a list of distinct
nonnegative original color IDs at each vertex and on each canonical
`Edge(u,v,weight,colors)` record. An edge's permanent ID is its original
input position. Weights are signed integers or `Fraction` objects. Loops
are validated and ignored; parallel edges remain different original items.
The input failure allowance is a nonnegative binary integer.

The output stores original vertex lists and retained original edge records
in their fixed weight/ID order. `forest(failed_colors,threshold=None)` uses
only those records. A threshold is an exact weight/original-ID pair.
Unknown nonnegative failure IDs have no effect but count toward the
allowance. Repeated IDs and over-budget queries are rejected. The query
does no feature construction or optimization on discarded edges.

Default arithmetic is rational. The optional field API has the canonical
declared-prime contract: the supplied modulus must be prime, and each
nontrivial component needs more field elements than its occurring labels.
Primality testing and finite-field extension are not implemented. The
mathematical deterministic construction can instead use the rational
branch, or choose a sufficiently large polynomial-sized prime. Sorting
and original scalar costs never use field residues.

## 2. Actual feature spans without a formal monomial universe

**Lemma 1.** `component_features` computes a polynomial-size exact
representation of the full coefficient-monomial activation matrix, with
the same ordered column dependencies.

**Proof.** Give component labels distinct nonzero field points; zero is a
never-failed dummy point. Pad each vertex root polynomial to the maximum
vertex-list size actually present. In the mixed case, pad edge polynomials
separately and multiply the two monic polynomials. Their coefficient bit
lengths and degrees are polynomial in the explicit label input.

With no edge labels, evaluation positions are the original component
vertices. Otherwise the positions are the two endpoint incidences of
every original component edge, carrying the polynomial of that endpoint
times the edge polynomial. The scalar coordinate functions are the
nonleading coefficients at those positions. Start from the all-ones row
and use the canonical [evaluation module](../../persistence-failure-certificates/reference/feature_summary.py)
to span all products of coordinate functions through the effective
failure degree.

The routine multiplies only accepted independent rows, in nondecreasing
degree. A dependent product is a combination of rows of no higher degree;
its subsequent coordinate products are combinations of their subsequent
products. Consequently discarding dependent candidates loses no final
row span. Once a degree stops growing, that span is invariant under every
coordinate multiplication. Since rank is bounded by the number of
evaluation positions, degree can be capped at that number. A huge binary
failure budget therefore creates no numerical-length iteration or array.
Only colors occurring in the component can matter, so the failure degree
is also clipped by that explicit label count.

Each retained module row is an actual monomial evaluation row, and every
formal monomial evaluation row is its linear combination on every
position. Thus the reduced feature matrix is a row projection of the
formal feature matrix, while the latter is recovered by one fixed linear
map from the former. Apply those same maps at every vertex block of the
activation matrix. Both full and reduced edge matrices recover one
another linearly, so their column dependencies agree exactly, including
on every ordered prefix. No generic-position assumption or independent
query-order choice is made. This proves the lemma.

The native component metadata gives the actual feature rank and the formal
binomial dimension, but the latter is only an integer, never an allocated
feature array. Vertex-only positions number the original component
vertices; mixed positions number twice its original nonloop edges.
`Component.feature_rank` is this component's position-evaluation rank.
In cubic mode it is an endpoint/edge feature rank; the separate vertex
Vandermonde rank used in G16 is computed as the minimum of its Vandermonde
dimension and its number of occurring vertex colors. No sum of component
feature ranks is substituted for the canonical global vertex-rank parameter.

## 3. Activation, rank savings and fixed-order forests

**Theorem 2.** The retained records preserve every original surviving
ordered-prefix connectivity partition and canonical forest. They satisfy
the stated vertex-list, general mixed-list and symmetric-cubic envelopes.

**Proof.** In the vertex-list case, a query evaluates the product of each
vertex polynomial at the failed label points. This is a linear functional
of its formal monomial features, nonzero exactly at surviving vertices.
Lemma 1 supplies the same functional on reduced features. Multiplying a
vertex block by its own survival factor sends an oriented edge column
to its ordinary incidence column times the product of endpoint factors.

In the mixed case, the common evaluation functional on endpoint/edge
positions gives the product of that endpoint's and edge's factors.
Multiplying a vertex block by its own factor again gives one identical
nonzero scalar at both ends exactly when the whole edge survives. Shared
labels simply repeat factors and do not alter their zero sets. A label
outside the component is ignored by this query map.

The fixed-order greedy column basis spans every original matrix prefix.
Apply the appropriate query map to those predecessor relations. A failed
edge maps to zero, while a surviving edge maps to a nonzero incidence
multiple. Thus the original and retained surviving incidence-prefix
spaces agree. Their connectivity partitions agree, and every original
canonical Kruskal edge must be retained. Query Kruskal returns literally
the same permanent IDs, with signed weights and ties handled by the
unchanged order.

For vertex-only lists, the reduced vertex vectors span their actual
coordinate dimension. Every symmetric matrix gives the annihilating row
from Section 2 of the canonical manuscript. The dependency map is
injective on that symmetric-matrix space. Its dimension is the symmetric
matrix term in the exact actual-rank envelope G21. The native code
computes this rank even when the formal dimension is enormous; it does
not replace actual rank by an uncomputed parameter envelope.

General mixed lists use the formal block dimension from G23. Lemma 1
preserves its activation-matrix rank; taking the minimum with the original
edge count is safe. For one color at each vertex and edge, the formal
features are symmetric bivariate polynomials of individual degree at most
the failure allowance. Powers of the sum and product form a basis: their
leading symmetric monomials give a triangular change of basis with
diagonal entries one. This argument requires no division, including in
characteristic two.

Every symmetric trilinear form yields a row dependency by evaluating its
first argument on each vertex color vector. The edge contributions cancel
by symmetry. Its kernel consists exactly of forms descending to the
quotient by the vertex-vector span, because annihilation in the first
argument implies the same in all three arguments. Subtracting that kernel
dimension gives G16 and hence the full and partial vertex-rank cubic
savings G17. Lemma 1 transfers that bound to the compressed native matrix.
The code checks the resulting component bound after construction. Sparse
graphs can have further dependencies; no exact generic rank is asserted.
Summing component bounds proves the theorem.

The ordinary singleton vertex specialization still has its previously
proved sharp componentwise bound. Empty components contribute zero, and
isolated vertices remain in the stored original list.

## 4. Completed-batch one-failure exchange wrapper

**Lemma 3.** `single_failure` returns the exact union of canonical forests
for no failure and for each individual color failure. Its replacement
lists satisfy the canonical incidence and baseline-loss bounds.

**Proof.** Let the baseline be the original canonical forest. Each baseline
edge increased original prefix rank. Deleting other edges cannot connect
its endpoints earlier, so every surviving baseline edge is still accepted.
The failed forest is therefore the surviving baseline plus its nonbaseline
replacement set. Deletion cannot increase graphic rank, so replacements
number at most destroyed baseline edges. Summing this loss over colors
gives G27, with each edge/color incidence counted once across the union
of its endpoint and edge lists.

The wrapper builds those incidence lists directly. Colors destroying no
baseline edge have unchanged canonical forest and cost, so they get a
default report. For every other color, delete its edge batch, collect the
current nonbaseline forest, then restore that exact batch. A dense
original-ID linked list tracks additions and removals using only reported
global forest exchanges. Intermediate deletion and restoration forests
are never copied into the certificate. At a completed batch the list is
exactly the replacement set just proved; restoration empties it.

Replacement IDs are sorted in the permanent original order before storing
their difference record. The exact cost subtracts destroyed original
baseline costs and adds the original replacement costs. All returned
records are from the baseline or a completed failure forest, so their
union is precisely the family claimed. Its size inherits every applicable
activation bound, because any activation certificate already contains
every one of these canonical forests. This proves the lemma.

`indexed(index)` returns the stored difference and value at a compact
palette index. Original-ID lookup uses a separately charged binary search;
an absent original color has the baseline value. `forest(color)` scans the
stored retained union to emit canonical IDs. The compact difference object
and the full forest report have distinct output and lookup costs.

## 5. Realizing the published dynamic interface

The fast mathematical bound uses Holm–de Lichtenberg–Thorup,
[*Poly-Logarithmic Deterministic Fully-Dynamic Algorithms*, JACM 48(4),
2001, Theorem 8 and Section 5.1](https://u.cs.biu.ac.il/~liamr/p723-holm.pdf).
The problem definition on page 724 explicitly requires responding to an
edge update with the corresponding updates of the maintained minimum
forest. Section 5.1's global insertion changes that forest by adding an
edge or replacing the heaviest path edge; deletion removes its tree edge
and adds its identified lightest replacement when available. Recording
those named original edge IDs takes constant extra work at the existing
global forest changes. Internal rebuilding of auxiliary local structures
does not require scanning or reporting their forests.

Use positive order ranks of the original weight/ID keys as dynamic
comparison weights. They give exactly the same canonical forests, while
actual cost reporting keeps the original signed rationals. A parallel-pair
priority queue exposes the cheapest active original edge per endpoint
pair. A change takes at most two simple-graph dynamic updates; their
constant-many reported global events can be composed to the final net
exchange. The input-incidence batches and linked-list collection then
have exactly the operation count G28. This closes the stated
exchange-reporting interface through the named published construction;
it is not an assumption that any arbitrary dynamic-MSForest library
exposes that interface.

The shipped `ReferenceMSF` is a separate exact implementation of the
interface. It scans all active original records in their fixed order and
recomputes canonical Kruskal after every individual insertion or deletion.
One update's net forest difference has at most one entering and one
leaving edge, by the ordinary single-edge minimum-forest exchange rule.
It reports those exact IDs. It does not implement HDT or claim its update
time.

## 6. Lower bounds and comparison scope

The list lower bound labels one apex per fixed-size palette subset and
gives the remaining base vertices empty lists. Failing the complementary
palette isolates exactly that apex's star; all its edges are necessary.
Splitting each apex's labels between its vertex and incident edges gives
the mixed-list simple-graph construction without changing this argument.

The single-color mixed multigraph lower example also forces its core
clique edges: when exactly two core colors remain, the surviving outer
edges attach to only one of those cores. Their core clique edge is then
the unique connection to the other core. Thus both the outer parallel
edges and every core edge are compulsory, giving G18's full count.
These are retained-subgraph support statements in their stated regimes,
not lower bounds for arbitrary encoded data structures or faster query
algorithms. The ordinary sharp vertex-failure example remains credited
to Sorkin–Steger–Zenklusen.

The journal-version color-list model is confirmed by the authors'
[institutional publication record](https://weizmann.elsevierpure.com/en/publications/color-fault-tolerant-spanners-2/).
No parameter comparison with an unseen journal full text, metric-spanner
claim, fastest-known assertion or exhaustive priority determination is
added by this review. The ITCS 2024 weighted earlier-path argument remains
its identified antecedent, rather than a new weighted-MSF observation.

## 7. Actual arithmetic, storage and sorting costs

Let `w` be a component's evaluation-position count, `d` its actual maximum
coefficient degree, and `t` its generated feature rank. The canonical module
accepts at most `w` rows and tries at most one initial row plus `d*w`
coordinate products; a conservative bound is `O((d+1)*w**3)` field
operations. Its storage is `O(w**2+d*w)`. Here `w=n_C` for vertex lists
and `w=2*m_C` for mixed lists. Root-polynomial construction, original
component organization and explicit list coefficients are additional
polynomial costs.

The activation column dimension is `R=n_C*t`. Greedy elimination uses
`O(m_C*R**2)` field operations and `O(R**2)` field elements, separately
from retained edge count. The formal binomial feature count has
polynomial bit length after clipping the failure budget to the explicit
component label universe; it is never enumerated. Coordinate products
use degree at most `w`, and rational elimination uses bounded-bit minors,
so rational bit work is polynomial in the complete explicit input.
Prime-field work has the corresponding encoded-modulus arithmetic cost.

Sorting the original records and final retained records by exact signed
weight/ID keys is charged. The single-failure wrapper initializes with one
update per original nonloop edge and uses at most twice the full
edge/color incidence count more updates. Its default reference update
performs an original-record scan, union-find work and forest-difference
work, with separately charged integer hash/set operations; total reference
time is polynomial and does not equal G28.

Each completed extra list is sorted. For the fast mathematical wrapper,
the sum of these costs is at most the replacement count times the log of
original forest size, which is absorbed by the incidence/update term in
G28 because each replacement can be charged to a destroyed baseline edge.
Sorting the retained union is likewise absorbed by the original-record
sorting/update ledger. The native code also pays these actual sorts.
Linked-list event handling itself is constant indexed work; enumerating
completed extras is proportional to their total length. Palette sorting,
long original color IDs, rational costs, compact-index lookup, raw-label
binary search and writing/printing output bits are all separate costs.

The certificate queries need only original vertex lists and retained
records. The difference summary keeps its palette, baseline, exact
differences and their original retained union. It stores no discarded
edge weights. These implementation and finite-check claims do not assert
external peer review or proof-assistant verification.

**Attribution:** Yilin Liu and GPT-6 Astra Pro. **License:** Apache-2.0.
