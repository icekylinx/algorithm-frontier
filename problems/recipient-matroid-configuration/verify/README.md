# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md).

## Mathematical evidence

- The proof defines the coupled configuration comparator with separate recipient-matroid columns and proves the fractional lower-cover lemma.
- Current-prefix additivity is restored after every retained-prefix exchange; eager release and all-center normalization preserve the current rank charge.
- The heavy-resource adapter preserves the compact small-resource promise without enumerating configurations, and approximate availability requires the stated local certification.

## Executable evidence

Run the independent resource-state check:

```sh
python3 problems/recipient-matroid-configuration/verify/check_reservations.py
```

It checks 7,381 states, 37,525 universal reservations, 35,081 internal-prefix
identities, 5,779 completions, 4,532 exchanges, 145 nonempty-group releases and
7,161 normalized sharp covers; 430 explicit invalid operations are rejected
without mutation. Exact rational minimal bundles occur in the seeded traces.
The checker enumerates binary spans independently of its Gaussian rank oracles.

The [backend proof](../resource-backend.md) establishes the general invariant;
the [API](../reference/README.md) states the caller's player-side obligations.
This is a resource-state implementation, not a complete allocator, local
availability optimizer or matroid-union engine.

## Model and verification boundaries

Each player-resource pair supplies at most one service; values are common. Additional local families are downward closed with a paid availability interface. Arbitrary aggregate recipient polymatroids do not automatically inherit this configuration comparator.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
