# Elementary certifying independent transversal backend

[Construction](elementary.py) · [Search-free verifier](transversal_certificates.py) · [Proof and scope](../reference-realization.md)

This implements the elementary single-vertex Graf--Haxell fallback, with
zero-blocker cascades and a bound based on positive blocker-count
compositions. It returns either one independent original vertex per class
or an induced constellation totally dominating its active classes. The
second outcome is an explicit domination witness; a transversal may still
exist elsewhere. It must not be interpreted as an infeasibility certificate.

```python
from elementary import solve
from transversal_certificates import Constellation, verify

classes = ((0, 1), (2, 3))
edges = ((0, 2), (0, 3), (1, 2), (1, 3))
answer = solve(classes, edges)
assert isinstance(answer, Constellation)
assert verify(classes, edges, answer)
```

Classes are nonempty explicit vertex lists partitioning the integers from
zero through the original vertex count minus one. An empty graph with an
empty partition returns the empty transversal. Edges are loopless undirected
pairs; repeated records are harmless. Within-class edges are removed, which
preserves transversals and is exactly the source's constellation convention.
Vertex and class IDs are retained. The routine requires no claw promise,
slack parameter, or precomputed solution.

`Transversal.vertices` lists the chosen original vertices. A
`Constellation` gives original class IDs and pairs of a center with its
nonempty leaf tuple. Its vertex set totally dominates every vertex of those
classes in the interclass graph, including its own vertices. The leaves
represent all but one of those classes. All stars are induced together, so
extra edges between stars are forbidden. The independent verifier checks
these properties directly and imports no constructor.

An optional `observe(root, matching, stars)` callback receives immutable
stable-state snapshots. Callback work and retained snapshots are additional
user costs. The solver itself retains only its current graph and state; it
does not save an exponential execution trace.

The reference has an exponential-in-class-count bound, with explicit
arithmetic/hash and bit accounting in the realization note. It does not
implement the faster current-blocker layer construction. The algorithm is
credited to Graf and Haxell; all source code here is a new local implementation
under Apache-2.0, with no third-party code copied.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
