# Shared path records for low-step flow emulators

This note reconstructs a representation adapter for
[Haeupler--Hershkowitz--Li--Roeyskoe--Saranurak, arXiv:2406.14384v1](https://arxiv.org/html/2406.14384v1).
It proves the adapter's combinatorial accounting and identifies its
arithmetic and quantitative premises separately. It does not import a
new matching exponent from the source's unspecified polynomials.

## 1. A path-valued refinement of an embedding

Suppose an edge e=uv of capacity c_e and length ell_e has a unit-flow
embedding into an earlier graph, with paths P_ej and nonnegative
fractions p_ej summing to one. Replace e by parallel edge IDs e_j,
each with endpoints u,v, length ell_e and capacity c_e p_ej. Give
e_j the single path image P_ej. Zero-capacity copies are discarded.

This transformation preserves all flow possibilities, path step
bounds and lengths in the abstract graph: every original usage of e
can be split among its parallel copies, and every copied-graph flow
can be aggregated back to e. It also preserves the embedding's
positive edge-occurrence load, since the capacity-weighted path
inventory is unchanged. Its edge count is the embedding's path
count, not the sum of fully unfolded path lengths.

This is a refinement of the actual graph used in subsequent calls,
not a post hoc choice of one embedding path for an unsplit edge.
The latter would generally destroy the congestion bound.

Apply this refinement after EVERY local emulator construction in
Section 5. Theorem 5.1 already bounds both the original emulator
edge count and its local embedding path count by the same
alpha-times-input-size envelope. Thus replacing an edge count by
the path count preserves its stated size recurrence, after a fixed
constant adjustment if necessary.

## 2. The concatenation DAG

Assign a unique immutable ID to every actual or auxiliary edge.
An original oriented edge is a leaf. A refined auxiliary edge
points to an ordered concatenation of older oriented edge IDs.
Every reference contains its orientation; reversing a reference
reverses the child order and orientations. Empty walks retain their
endpoint ID and are distinct from genuine self-loops.

Edges in one bootstrapping level map only to original edges or
edges in a previous level. The dependency relation is acyclic.
Binarize every local path list and suppress unary nodes. If Q is
the total number of local path-list occurrences produced throughout
the construction, the resulting DAG has O(Q) arcs and nodes.
No original-graph walk is unfolded merely to create its root.

In the notation of Theorem 5.1, put

    B_loc=(2st+3s)h.

The local embedding of level i has at most
(2alpha)^(i+1)m paths, each with at most B_loc edges. Therefore the
stack of levels 0,...,d admits the explicit bound

    Q <= O((d+1) m (2alpha)^(d+1) B_loc).

This is a bound on the representation actually constructed. It
does not charge the potentially much larger lengths of walks after
all levels are unfolded. The source's Lemma 5.2 scans these same
local embedding lists when mapping aggregate edge flows; retaining
their immutable ordered lists adds only constant structural work
per local occurrence.

For several scale stacks, sum this bound over the stacks. Shared
original leaves can be reused, but the accounting does not require
such reuse.

## 3. Sparse splitting and concatenation really preserve records

A flow record stores an ordered source and destination, a DAG root,
and a nonnegative mass. Records with identical roots need not be
merged. This avoids any need to compare fully expanded paths.

The following accounting applies directly to the implementations
in Lemmas 7.6 and 7.7.

**Splitting.** At one source vertex, put its a requested source
masses and b outgoing path masses in any deterministic order.
Pair overlapping intervals of their cumulative mass partitions.
There are at most a+b-1 nonzero overlaps. Each output record keeps
the old path root and stores the overlap mass. No path is copied.
The records partition both the original flow masses and the
requested source masses exactly.

**Concatenation.** At a joining vertex, perform the same overlap
operation on incoming and outgoing path masses. For each overlap,
make one binary concatenation node and one record of that mass.
There are at most a+b-1 such records. The total mass using each old
path is exactly its previous mass. Ordered endpoints and commodity
labels are preserved.

Consequently, if T is the total number of record births and local
record scans in these operations, their structural work and added
DAG size are O(T), apart from sorting/grouping by vertex. Sorting
by finite vertex and commodity IDs costs a polylogarithmic factor.
The bound is on ALL record births over the execution, not just the
final support size.

Algorithm 3, step 2(a)(iii), already creates a separate child edge
for every matching-flow path and stores its path embedding. Its
recursive graph therefore has exactly the immutable path-valued
edge interface above. Step 4 maps recursive paths through those
fixed edge records, splits tails, and concatenates them with their
matching prefixes. Keeping pointers implements these operations
without expanding their original-graph walks.

## 4. Positive flow, not net cancellation

These records denote walks until final cycle erasure. If a walk
uses a genuine edge twice, both occurrences are counted. Splitting
preserves occurrence loads; concatenation adds them. Replacing an
edge by its fixed path image is a nonnegative linear operation on
the oriented occurrence vector.

This matches the source's edge representation in Section 3, which
stores two nonnegative directed quantities for an undirected edge
and sums them for its load. It is not a signed flow representation.
The proofs of Lemma 5.2 and Lemma 7.10 bound precisely this positive
embedding and concatenation load. Their domination inequalities
therefore remain available before cycle erasure.

The local capacity-weighted embedding bound gives the parent load
bound even when several abstract edges have the same parent image.
At the bootstrapping levels, the disjoint original-length bands in
Theorem 5.1 account for fresh original edges; one must retain that
property when invoking its congestion-one conclusion.

For any subset of final commodities, put their root masses on the
DAG and propagate them in reverse topological order. At a binary
concatenation node the full incoming mass goes to EACH child.
Accumulate at genuine oriented leaves. This computes their gross
edge-occurrence flow in O(Q+T) arithmetic operations. It is exactly
the represented flow's aggregate map, with no commodity/path
enumeration beyond the stored records.

## 5. Mass precision: what the adapter proves and does not prove

All overlap operations use addition, subtraction, comparison and
minimum. If their incoming masses lie on one common lattice
(1/Q0)Z, their outgoing masses lie on the same lattice. If all
values have magnitude at most M0, their numerators use
O(log Q0+log M0) bits. There is no per-concatenation denominator
growth. A common scaling by a rational with b bits increases that
bound by O(b).

This proves finite bit work for the adapter under a declared
common-lattice contract for the primitive flow calls. It also
proves a useful weaker statement without such a contract: if K
unrelated b-bit denominators enter the execution, a conceptual
product of them is a common denominator with at most Kb bits.
That gives polynomial bit complexity, but is NOT enough by itself
for nearly linear bit work. We do not hide that distinction.

The source's Assumption 3.1 asserts polynomially bounded reciprocal
grids for internal capacities and lengths. Its Algorithm 5 also
claims a 1/n^2-fractional flow, and Algorithm 6 has at most one
final budget-truncation scalar before it returns. Those are useful
arithmetic hooks, but a fully independent quantitative audit still
has to establish the relevant grids for all embedded-flow atoms
and the multiplicative-weight price implementation. This note
does not infer that proof from a unit-cost real-arithmetic model.

In the boosting stage there is no need to materialize a giant
normalized denominator just for path selection. Suppose its
unboosted oracle flows F_i all route the complete unit demand,
and its final flow is the convex combination

    F=(sum_i z_i F_i)/(sum_i z_i).

Retain records with unnormalized masses z_i f_ia. The common
normalizer is identical for every commodity. The algorithm in
[nonuniform_fractional_path_selection.md](nonuniform_fractional_path_selection.md)
accepts these original rational masses and implements the required
ratios by positive finite-precision sums. This removes a FINAL
normalization obstacle, while leaving the generation of the z_i
and f_ia themselves explicitly charged.

## 6. Extracting routes, conditional on a complete provider

Assume the execution supplies a complete flow for M unit
commodities with this DAG, total original length at most MH, and
gross edge load at most c. Compute root lengths bottom-up,
saturating beyond 4H. Then
[compressed_fractional_path_extraction.md](compressed_fractional_path_extraction.md)
retains short candidate records for at least half the commodities,
with full mass restored using a factor at most two and expected
edge load at most 2c. Expanding only those short roots costs
O(Q+T+PH), where P is the number of retained records.

Immediate-native cycle erasure removes repeats before ambient
selection. Apply the nonuniform sparse selection lemma to the
remaining candidates. Repeating on the unserved commodities gives
logarithmic progress if the same provider applies to every
restricted demand. No long discarded walk is ever expanded.

For this purpose the boosted min-cost concurrent theorem is the
useful source interface. Set tau=|D| in Theorem 10.2. A partially
routed demand of value at least |D| is necessarily the entire
demand. If a reference full flow is feasible with the declared
capacity and cost budget, lambda*>=1. Its approximation factor
then bounds BOTH the congestion and the total length of the
normalized complete flow. The large unboosted congestion parameter
need not survive into the router's output quality.

This conditional construction is stronger than treating
Definition 9.1 as an opaque aggregate-flow oracle. It still depends
on the low-step construction, its arithmetic, and its quantitative
parameter choices.

## 7. The conditional quantitative target

To make the missing quantitative information explicit, suppose a
provider were proved uniformly to have work factor

    exp(O(U epsilon^a + epsilon^(-b)))

and a boosted routing loss exp(O(epsilon^(-b))), for specified
positive constants a,b and an admissible inverse-logarithmic
epsilon range. Then the adapter above retains those factors,
apart from fixed powers and logarithms.

Ignoring other decomposition losses for this calculation, the
current dynamic composition would require its logarithmic
overhead A to dominate

    x,  U epsilon^a,  U^2/(xK),
    (U/x) K epsilon^(-b).

Writing epsilon=U^(-lambda) and A=U^z, the resulting balanced
candidate is

    z=(3a+b)/(4a+b),   lambda=1/(4a+b),

provided the stated epsilon range includes it. It is below 4/5
only when a>b. These formulas are a CONDITIONAL target, not an
interpretation of the source's unexpanded polynomial notation.

Moreover, retaining our current classical expander decomposition
still contributes the independent U/r work versus r log U output
tradeoff. That channel alone retains the present 4/5 balance.
An improved flow router by itself does not remove it.

The quantitative breakpoint is therefore precise: one needs an
audited tunable source algorithm, its allowed epsilon range and
finite-word work, as well as a compatible improved decomposition
channel. The literal HHT spiral issues are recorded in
[hht_literal_sequence_and_parameter_boundary.md](hht_literal_sequence_and_parameter_boundary.md).
The current accepted 4/5 construction is independent of this
unresolved route.

## 8. What can be reconstructed from the actual parameter choices

### 8.1 The router-recursion index has a conditional repair

The proof of Theorem 7.1 takes recursion fanout n^epsilon and depth
d=ceil(1/epsilon), then prints an inner parameter
eta=epsilon^(1/c') while asking a per-level N^(poly eta) factor to
remain N^(poly epsilon) after d levels. A transparent sufficient
choice goes in the other direction.

Assume an audited local cut-strategy factor is at most

    polylog(N) N^(c eta^a),

for fixed a,c>0. Choose an integer C with Ca>=2 and set
eta=epsilon^C. Then

    d eta^a = O(epsilon^(Ca-1)) = O(epsilon),

and the product of those local factors is

    exp(O(U epsilon + epsilon^(-1) log U)).

The second term is at most O(U epsilon) when
U epsilon^2 dominates log U. The local work's fanout-squared
factor is n^(2epsilon), also within that envelope. The explicit
length recurrence in Lemma 7.10 gives

    log(length inflation)
        <= O((1/epsilon) log(1/eta))
         = O(C log(1/epsilon)/epsilon),

apart from the input router length. The range must additionally
ensure eta^(-1)<=log N for the invoked cut-strategy theorem, and
must meet that strategy's own admissible parameter range.

This is a valid conditional correction of THIS index choice. It
does not repair the decomposition/epoch issues in HHT or supply
the missing local constants a,c from an unaudited primitive.

### 8.2 The advertised stacking envelope retains a 4/5 barrier

Even with a repaired primitive, the actual Section 6 stacking
introduces an independent output/work tradeoff. To see it without
guessing hidden polynomial degrees, first suppose the local
primitive has

    log alpha=O(U epsilon^a0),
    log t=O(epsilon^(-b0)),

with length slack bounded by a fixed power of t. Choose the
stacking scale h=N^(epsilon^c), where 0<c<a0. Its depth is
Theta(epsilon^(-c)). The source's proved work expression contains
both poly(h) and alpha to that depth. Its resulting envelope has

    a_out=min(c,a0-c),
    b_out=b0+c

for the work exponent U epsilon^a_out and the output length
exponent epsilon^(-b_out). Thus b_out>a_out when b0>0; even if
the primitive's length were constant, a_out<=b_out. These are
exact consequences of the charged expressions, not identified
values for the unspecified source polynomials.

There is a more general version not restricted to power choices.
Put v=log h. Covering a polynomial original-length range uses
d=Omega(U/v) stack levels. The reported local work charges a
positive fixed power of h, so its logarithmic work budget charges
v. Theorem 5.1's length comparison multiplies a factor at least
2t+3>=5 per level, even for an ideal primitive. The proved output
logarithmic loss therefore charges at least d in this model.
Consequently the model retains

    local log-work >= c v,
    output log-loss >= c' U/v.

Combining these positive charges with the current dynamic
composition, if its total logarithmic budget is A and log k=x,
then x<=O(A), v<=O(A), and

    A >= Omega(U^2/(xK)),
    A >= Omega((U/x) K (U/v)).

The first gives K>=Omega(U^2/A^2); substituting this in the second
gives A^5>=Omega(U^4). Thus the same 4/5 power remains in the
advertised-expression optimization, even before charging the
actual primitive's losses or the separate decomposition channel.

For nonuniform scale factors, sum log h_i to cover the original
range. Bounding each log h_i by O(A) still requires
Omega(U/A) levels, and the same counting applies.

This is NOT a lower bound on the runtime of all emulator-based
algorithms. Source upper bounds need not be tight, and a new
direct representation or flow argument might avoid the repeated
length inflation. It does show that repairing the literal HHT
proof and exposing the DAG would not alone justify a better
matching exponent through the current stacked guarantee. That
is a concrete breakpoint for this particular follow-up route.
