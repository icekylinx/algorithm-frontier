# Exact compact-body reduction and violation certificates

[Implementation](compact_body.py) · [Realization proof](../manuscripts/reference-compact-membership.md) · [Independent checker](../verify/check_compact_body.py)

The constructor turns a nonnegative integer weighted Max-Cut instance into
the compact binary-check body from the exact-membership theorem. A supplied
threshold is an upper bound: the constructed point belongs to the body if
and only if every cut has weight at most that threshold.

```python
from compact_body import reduce_maxcut, separate, verify_violation, recover_cut

edges = ((0, 1, 3), (1, 2, 4), (0, 2, 2))
body = reduce_maxcut(3, edges, threshold=5)
witness = separate(body)
assert verify_violation(body, witness)
cut = recover_cut(3, edges, 5, witness)
assert sum(w for u, v, w in edges if (u in cut) != (v in cut)) > 5
```

Vertices are original IDs from zero through the vertex count minus one.
Edges are loopless undirected `(u, v, weight)` records with nonnegative exact
integer weights; parallel records remain separate. Thresholds are exact
integers. Zero coefficients are omitted, and empty/all-zero graphs are
handled directly by the same algebraic identities. Binary magnitudes are
never expanded into repeated unit-weight records.

`Body` also accepts generic homogeneous binary checks, positive rational
weights, a rational point and an accuracy parameter. Check rows list distinct
variable IDs. `QueryViolation` supplies a dense original binary assignment;
`SparseQueryViolation` supplies only original IDs assigned one, with omitted
coordinates zero. `CubeViolation` supplies an out-of-range cube coordinate. The search-free
verifier tests the claimed strict violation using exact arithmetic.

`separate` checks cube constraints, then streams binary assignments on the
coordinates actually used by the rows, returning a sparse violated query. `None` means membership after completing that
search. It is exponential in the number of used coordinates and retains polynomial workspace;
it is a reference exact oracle, not a polynomial-time compact separation
algorithm. Unused coordinates are never expanded, even when the declared dimension is
a huge binary integer. If all check rows are empty, the query inequalities
are vacuous and no assignment space is materialized. General negative point coordinates
can violate the lower query inequality; the special Max-Cut construction
always has nonnegative point coordinates.

For a valid constructed query witness, `recover_cut` returns original vertex
IDs forming a cut strictly above the supplied threshold. It rebuilds and
checks the reduction before decoding. A witness for an arbitrary unrelated
body is not a Max-Cut certificate.

No third-party implementation is included. The classical hardness source
and its precise threshold convention are recorded in the realization proof.

**Attribution:** Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
