# Correctness and certificates for the executable degree solver

**Ready for review: unconditional local construction and ordinary
polynomial-time implementation.** The code uses the complete sparse
reduction in [Theorem 1.1 and Sections 2–5](../proof.md), followed by the
repository's [exact matching solver](../../general-matching/reference/README.md).
No numerical cycle-search or randomized primitive is used. This note
identifies the implemented decisions, the exact certificate meaning and
the runtime charged to them.

## 1. Native records and normalization

Every input edge has two distinct vertices and a stable input index.
Parallel records receive separate incidences and remain independently
selectable. Loops are rejected because the stated degree reduction is
for loopless graphs; a loop must not silently disappear from a degree
request. Supplied IDs are distinct integers or strings and remain passive
labels during solving.

For every vertex, scan its incident degree `d(v)`, keep the lower bound
`g(v)` unchanged and replace its upper bound by `f(v)=min(f(v),d(v))`.
If `g(v)>f(v)`, the request is infeasible. Intersect the requested
cardinality interval with `[0,m]`; an empty intersection is infeasible.
All these conclusions are directly rechecked by the verifier.

After this scan, discard degree-zero vertices from every nontrivial
reduction. A discarded vertex has lower bound zero, or the request has
already been rejected. The active vertex count is at most `2m`. The
original vertex universe is retained only for the native input and
final degree vector. Optimization never rescans all isolates on each
matching query.

## 2. From a cardinality interval to a prescribed factor

For a query interval `[L,U]`, the first hub is exactly the one in Section 5
of the main proof. Put `F=sum_v f(v)` and `D=sum_v(f(v)-g(v))`.
Add `f(v)-g(v)` distinct edges from vertex `v` to a new hub, prescribe
degree `f(v)` at every old vertex, and give the hub the degree interval
`[max(0,F-2U), min(D,F-2L)]`.

The key identity is `degree(hub)=F-2|X|`, where `X` is the selected
original subset. Thus the new hub interval is equivalent to the requested
cardinality condition. Its emptiness is another exact local NO. For the
unconstrained interval `[0,m]`, this first augmentation is omitted.

Convert the remaining interval-degree instance to a prescribed-degree
instance by Section 4: add one second hub, the required dummy incidences,
and private triangles whose contributions to the hub are zero or two.
Choose the hub target to have the same parity as the prescribed degree
sum. This realizes every permitted total deficiency and only those
deficiencies. When all degree intervals are already singletons, this
second augmentation is omitted. An odd prescribed degree sum, or a
prescribed degree larger than the available incident degree in the
augmented graph, is an immediate NO.

All added edges are explicitly represented. Their count is linear in the
original `m`, because every retained original upper bound is at most its
incident degree. The construction never expands an arbitrarily large
numeric input bound into that many records.

## 3. Sparse selectors and native decoding

For each augmented edge create two incidence ports and one cross edge
between them. For an augmented vertex of degree `d` and prescribed
degree `f`, exactly `d-f` ports must be matched locally.

The code builds the recursive permutation network proved in Section 3
of the main proof, splits every network position into an in/out pair,
and attaches exactly `d-f` output sinks. The count of matched in and out
endpoints cancels every internal transition. In a perfect matching,
exactly the number of ports corresponding to those sinks uses local
attachments. Therefore exactly `f` incidence ports use cross edges.
Conversely, a prescribed factor determines a partial input-output
permutation; the network routes it, and unused positions use idle edges.
This proves both directions for the actual constructed graph.

One implemented simplification omits a selector when `d-f=0`. The same
count identity forces all its ports to use cross edges. Its unused
network positions could all use idle edges, so deleting that selector
preserves both extension and decoding. This also handles degree-zero
vertices without constructing a network of width zero.

Distinct native records always have distinct port pairs. The reduced
graph is therefore simple even when the input has parallel edges, and
every reduced vertex has degree at most three. Network input and output
positions have no incoming and outgoing transitions, respectively, so
their external attachments respect that degree bound.

Each cross edge carries either its original native index or a dummy
marker. Decoding retains only matched cross edges with a native index;
all hub, triangle, selector and other auxiliary edges are discarded.
The original ID and endpoint orientation are then restored from that
index. An independent native scan checks all vertex degrees and the
selected cardinality before any `YES` leaves the solver.

## 4. Exact feasibility and independently checked NO results

Let the constructed matching graph have `N` vertices. The exact matcher
returns a matching and its independent optimality certificate. The
solver checks that certificate even when it is about to return a NO.

If the checked cardinality is `N/2`, the matching is perfect and the
preceding equivalence supplies a feasible native subset. If twice its
cardinality is smaller than `N`, the certificate proves that no perfect
matching exists. The equivalence then proves infeasibility of the native
request. An unsuccessful matching attempt without an optimality
certificate would not establish this conclusion.

The independent matching verifier uses a native matching lower bound and
a tight odd-component upper bound, as proved in the
[matching certificate note](../../general-matching/reference/certificate-proof.md).
The degree verifier reconstructs the same reduction and invokes that
checker. It imports no matching search. It shares the deterministic
reduction builder and normalization code, so its independence is from
search, not from every line of construction code.

Two easy successful cases bypass the matching call: an empty native
subset when every lower degree is zero and the interval contains zero;
and the whole native graph when every upper degree permits it and the
interval contains `m`. Both witnesses still receive the independent
native degree/cardinality check.

## 5. Optimization and one-interval certificates

First solve the full permitted interval `[K_min,K_max]`. If that query
is infeasible, report its checked NO.

For maximization, the predicate “some feasible subset has size in
`[K,K_max]`” is monotone in `K`. Binary search retains one successful
native witness and one final failed interval. At termination the best
size `k` is supported by the witness. Unless `k=K_max`, the retained
failed query is exactly `[k+1,K_max]`; its certificate excludes every
better permitted cardinality.

For minimization, use the monotone predicate for `[K_min,K]`. The final
witness has size `k`; unless `k=K_min`, the failed interval is exactly
`[K_min,k-1]`. The production code explicitly rejects any disagreement
between the returned native size and the binary-search boundary.

The external verifier checks just the final native witness and that one
excluded interval, or the relevant endpoint equality. It need not replay
the binary search. No assertion about intervals of feasible **exact**
cardinalities is used.

## 6. Ordinary polynomial cost

Set `H=1+m log(m+2)`. Both hub augmentations use `O(m+1)` records.
A power-of-two network of width `s` has `s(2 log_2(s)+1)` positions;
each chosen width is less than twice its positive incident degree.
Summing over all augmented vertices gives `O(H)` matching vertices and
edges, constructible in `O(H)` work after the initial native scan.

The existing exact matcher, including its certificate extraction, costs
at most `O(H^3)` on this graph. Its comparison sorting and independent
certificate check fit that bound. Therefore a feasibility request costs
`O(n+H^3)`. Optimization makes at most an initial query and a logarithmic
number of binary-search queries, giving `O(n+H^3 log(m+2))`. Failed
interval certificates and current witnesses occupy `O(H)` space; the
full native input/output occupies `O(n+m)`. Total storage is `O(n+H)`.

The external verifier reconstructs at most one reduced graph and uses
comparison sorting plus graph scans, so it costs
`O(n+H log(H+2))` time and `O(n+H)` space. It does not call the cubic
matcher. Actual reading, numeric arithmetic and label-comparison costs
must also be charged for representations longer than input words.

These bounds are ordinary polynomial guarantees of the shipped code.
They do not discharge or reuse the faster theorem's unimplemented
cycle-search requirements.

## 7. Finite implementation evidence

[check_reference.py](../verify/check_reference.py) enumerates original
edge subsets independently of the reduction and matcher. Its default
suite checks 8,292 feasibility/optimization requests, including every
valid degree interval on all simple graphs through three vertices and
two parallel-record graphs, all cardinality ranges there, all simple
four-vertex graphs with additional degree requests, and 120 seeded
native cases. It invokes the matcher 5,341 times and checks 3,364 actual
reduced graphs for simplicity and maximum degree three.

The suite additionally rejects 15 malformed requests and 15 corrupted
certificates, checks an isolated vertex universe and long numeric/ID
representations, and exercises both production command-line programs
with Python assertions disabled. Production acceptance conditions are
explicit checks; the mathematical test script itself refuses optimized
execution. These finite results support the implementation review and
do not replace the proofs above.

**Attribution:** Yilin Liu · GPT-6 Astra Pro.
