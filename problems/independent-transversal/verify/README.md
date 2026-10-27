# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md).

## Mathematical evidence

- The output includes the full domination and constellation certificate as well as the successful transversal alternative.
- Candidates are rebuilt against the current matching. The induced-star invariant, retained prefixes and total domination survive exchanges.
- The linked input-linear scans and elementary exponential fallback support the uniform signature count, including rational accuracy encoding.

## Executable evidence

The [elementary fallback](../reference/elementary.py) returns either an
independent transversal or an exact total-domination constellation. Its
[search-free verifier](../reference/transversal_certificates.py) reads the
original graph and imports no constructor. The
[realization proof](../reference-realization.md) establishes the cascade,
positive-signature termination and separate exponential resource bound.

```sh
python3 -B problems/independent-transversal/verify/check_elementary.py
```

The checker covers 4,773 graph/partition instances and 21,401 stable states,
checking every current blocker set, induced-star invariant and strict
signature descent. It returns 2,197 transversals and 2,576 constellations;
independent enumeration finds an existing transversal in 558 of the latter
cases, directly exercising the fact that this outcome is not a nonexistence
certificate. Four multiswap stable transitions exercise zero-blocker
cascades. Adding all within-class edges preserves 4,372 outputs, and 23
malformed cases are rejected. Verification also runs in a fresh interpreter
with the constructor import disabled.

Exhaustive graphs on the named small partitions and seeded larger instances
support the implementation. The written composition and invariant proofs
supply the arbitrary-size guarantee; the fast current-blocker layer
construction has not been implemented by this reference.

## Model and verification boundaries

The graph and partition are explicit and the class-neighbour independence parameter is stated. Within-class edges are removed for the induced constellation. A returned obstruction refutes the theorem’s promise, but need not exclude every independent transversal. The executable search realizes the elementary fallback; the independent validator checks that exact alternative.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
