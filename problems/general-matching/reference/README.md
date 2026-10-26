# Executable exact maximum matching

[matching.py](matching.py) is a deterministic maximum-cardinality matching
solver for arbitrary undirected graphs. It requires Python 3.10 or later and
only the standard library. It returns original edge identifiers, handles
loops, parallel input records and isolated vertices, and optionally supplies
an optimality certificate checked by a [separate verifier](verify_certificate.py).

This implementation uses the classical Edmonds blossom algorithm with the
proved componentwise matching kernel. Its ordinary polynomial running time
is stated below. The faster conditional [research theorem](../proof.md)
requires additional deterministic cycle-search machinery and is a separate
result; that machinery is not part of this executable.

## Run the example

From the repository root:

```bash
python3 -B problems/general-matching/reference/matching.py \
  problems/general-matching/reference/example.json --certificate \
  > /tmp/matching-result.json

python3 -B problems/general-matching/reference/verify_certificate.py \
  problems/general-matching/reference/example.json /tmp/matching-result.json
```

The example has a star, an odd cycle, parallel records, loops and an isolated
vertex. Its optimum has two edges. The verifier returns
`"optimality_verified": true` after checking the actual input, matching and
certificate. It does not import or call the blossom solver.

Both normal mode and `--certificate` have the same cubic time bound.
Use `--no-kernel` to solve
the full normalized components. Input `-`, or no filename, reads JSON from
standard input. A result without a certificate can be checked with
`--feasibility-only`; that check establishes edge validity and disjoint
endpoints, and does not establish maximum cardinality.

## Input and output

The input is a JSON object with `n`, `edges`, and optional `edge_ids`:

```json
{"n": 4, "edges": [[1, 0], [0, 1], [1, 2], [2, 3]],
 "edge_ids": ["first", "parallel", "middle", "last"]}
```

Vertices are the integers from zero through `n-1`. Every edge is a pair of
vertices. Edge IDs are distinct integers or strings; integers and strings
are different types, so `1` and `"1"` are different IDs. Booleans are not
accepted as vertices or IDs. If IDs are omitted, zero-based input record
indices are used. All arithmetic governing matching and certification is
integral and exact.

Each returned matching entry contains `input_index`, `id`, `u`, and `v`.
The endpoints preserve the orientation of that original input record, even
though the graph is undirected. For a parallel pair the earliest input
record is retained. A loop is never selected. Output is ordered by input
record index. Empty graphs return an empty matching.

The callable interface is
`maximum_matching(n, edges, edge_ids=None, *, use_kernel=True, certificate=False)`.
The separate `verify_result` function raises `ValueError` on a rejected
certificate and returns the verified scope on acceptance. Its
`require_certificate=False` option only checks feasibility. Informational
statistics supplied by the solver never serve as certificate evidence.

## Running time and storage

Let $`n`$ be the number of named vertices and $`m`$ the number of input edge
records. For each nonempty connected component of the normalized simple
graph, let $`H_i`$ be the retained kernel and put $`k_i=|V(H_i)|`$. The
implemented bounds are

```math
T_{\mathrm{normal}},\ T_{\mathrm{certificate}}
 = O\!\left(n+m\log(m+2)+\sum_i k_i^3\right).
```

Once a maximum matching has been found, certificate extraction adds only
$`O(\sum_i k_i^2)`$ work. It uses one simultaneous failed alternating
forest per kernel requiring a nonempty barrier, without recomputing
matchings after vertex deletions. The
[complete extraction proof](certificate-proof.md) is self-contained.

Working storage is $`O(n+m)`$. The output certificate also has
$`O(n+m)`$ records. These are word-operation bounds with vertex indices and
record indices occupying $`O(\log(n+m+2))`$ bits. Arbitrarily long ID strings
or integers incur their actual comparison, storage and JSON input/output
costs. The solver uses comparison sorting for deterministic normalization
and ID uniqueness checks; it does not assume worst-case constant-time
hashing or claim the manuscript's linear radix-sort preprocessing bound.

The independent certificate verifier uses comparison sorting and graph
scans in $`O(n+m\log(m+2))`$ word operations and $`O(n+m)`$ storage, plus
the actual label and certificate encoding costs. It performs no matching
search. On invalid input, processing is also charged to the supplied
certificate's size.

The kernel keeps all edges inside a vertex cover $`C_i`$ formed by a greedy
maximal matching, and at most $`c_i=|C_i|`$ distinct outside neighbors per
cover vertex. Therefore

```math
|E(H_i)|\leq
\min\!\left\{m_i,\binom{c_i}{2}+c_i^2\right\},
\qquad
k_i\leq c_i+c_i^2,
\qquad
c_i\leq 2\nu(G_i).
```

The code computes these quantities from the graph; the optimum is not an
input parameter. With `--no-kernel`, $`H_i`$ is the full normalized
component. A large star, for example, becomes a four-vertex, three-edge
kernel with this greedy cover. Processing many separate components does
not allocate a full $`n`$-vertex array for each one.

## Why the returned matching is maximum

**Normalization and the kernel.** Removing loops preserves matching
cardinality. Selecting one original record for each unordered nonloop pair
preserves every possible matched pair. Components can be solved separately.
The endpoints of a greedy maximal matching form a vertex cover $`C`$.
If a maximum matching uses an omitted edge $`uv`$, where $`u\in C`$ and
$`v\notin C`$, remove that edge temporarily. The remaining matching has at
most $`c-1`$ matched vertices outside the cover. Of the $`c`$ neighbors
retained at $`u`$, one is therefore free. Substituting this retained edge
preserves cardinality and decreases the number of omitted matching edges.
Repeated substitution puts a maximum matching inside the kernel. This is
the [main proof's Lemma 3.1](../proof.md#31-cleanup-and-an-optional-quadratic-edge-kernel).

**Blossom search.** The code initializes a greedy matching and searches
from each still-free vertex. An alternating tree labels unmatched and
matched steps. An edge joining two outer vertices contracts the odd cycle
through their least common tree ancestor. The `base` array represents the
contraction; rewritten `parent` links retain the alternating route needed
when an augmenting path is found. This is the classical blossom
contraction/expansion search of
[Edmonds, *Paths, Trees, and Flowers* (1965), Section 4](https://doi.org/10.4153/CJM-1965-045-4).
It applies to nonbipartite and disconnected graphs, without a perfect
matching promise.

The augmenting-path criterion follows by taking the symmetric difference
with any larger matching: one component would be an augmenting path.
Each successful search increases the cardinality by one and leaves all
previously matched vertices matched. A failed free root needs no later
restart. If a later augmentation from that root were possible, comparing
the resulting matching with the matching at the failed search would yield
an augmenting path from that root already then. Exhausting the searches
therefore leaves a maximum matching.

Within one search, every vertex becomes outer at most once and its
adjacency is scanned once. Each nontrivial contraction merges current
bases, so there are at most $`k_i`$ contractions. Ancestor/branch walks
and a contraction scan each cost $`O(k_i)`$. A search costs
$`O(k_i^2)`$, and at most $`k_i`$ root searches give the stated cubic
bound. The implementation is iterative; it does not require a recursion
depth proportional to the graph size.

## A certificate whose verification needs no blossom algorithm

For each original nonempty component the certificate lists its cover,
retained native input indices, and a set $`A\subseteq V(H)`$. The verifier
reconstructs the normalized input independently. It checks that the cover
meets every edge, every cover-cover edge is retained, and each cover vertex
keeps at least $`\min\{c,|N(u)\setminus C|\}`$ distinct outside neighbors.
These conditions certify exact preservation by the preceding exchange
proof. The verifier also checks every selected native ID and endpoint.

Let $`o(H-A)`$ count the odd connected components after removing $`A`$,
including isolated retained vertices. The final acceptance test is

```math
2|M|=|V(H)|-o(H-A)+|A|.
```

**Self-contained upper-bound proof.** An odd component of $`H-A`$ that
has no matching edge to $`A`$ contains an unmatched vertex. At most
$`|A|`$ such components can use matching edges to $`A`$, because those
edges have distinct endpoints in $`A`$. Thus every matching leaves at
least $`o(H-A)-|A|`$ vertices unmatched and has size at most the displayed
right-hand side divided by two. A feasible matching attaining that upper
bound is maximum. No claim about the search's internal state is used.

**How a certificate is found.** First try $`A=\varnothing`$; this already
works whenever each retained component has a perfect or nearly perfect
matching. Otherwise run one complete alternating forest from all exposed
vertices, with the maximum matching fixed. Every original member of a
contracted outer blossom is included in the outer set $`O`$. Let $`I`$
be the remaining inner vertices and return $`A=I`$.

At exhaustion there are $`|I|+f`$ odd outer blocks, where $`f`$ is the
number of exposed roots. There are no edges between different outer
blocks or from the outer set to unreached vertices. The unreached part
has a perfect matching. Hence $`o(H-I)=|I|+f`$, proving the required
equality directly. The [full proof](certificate-proof.md) establishes the
contraction, lifting and counting invariants, the quadratic extraction
bound, and the identification $`O=\{v:\nu(H-v)=\nu(H)\}`$. This is
the classical Gallai–Edmonds exposable set, with the required facts proved
locally. The code checks the equality before returning its certificate.

The certificate itself is sufficient even if its producer is untrusted:
its verifier uses only the elementary kernel exchange and odd-component
upper bound, and never assumes that the producer correctly identified
the exposable set or correctly contracted a blossom.

## Executable evidence and scope

```bash
python3 -B problems/general-matching/verify/check_reference.py
python3 -B problems/general-matching/verify/check_certificate_search.py
```

The first check compares all 33,868 simple graphs through six vertices
with an independent subset dynamic program in both kernel and full-graph
modes: 67,736 certified solves. It also checks 152 native-record instances,
260 seeded or explicit larger instances, 29 invalid-input/certificate
cases, and three scale/CLI cases. Every oracle comparison includes
independent certificate verification. The larger cases include odd cycles,
touching blossoms, the Petersen graph, dense graphs, stars and paths.

The second check tests the actual certificate search on all 33,868 simple
graphs through six vertices and 500 seeded graphs on seven through thirteen
vertices. Independent subset dynamic programming identifies the exact
exposable set; explicit even alternating paths and terminal block
invariants are checked separately. The checker also rejects two valid but
nonmaximum input matchings through explicit production exceptions.

The seed selects test graphs only; the solver has no randomized step.
The mathematical checkers explicitly refuse optimized Python execution
that disables assertions. The production solver and verifier acceptance
logic use explicit conditions rather than assertions. Finite evidence
supports code review and does not constitute a proof-assistant
formalization or verification of the separate fast research construction.
