# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md).

## Mathematical evidence

- The quarter-threshold classification covers every normalized full-target load with the stated interval boundaries and small-load caps.
- A single cost-preserving integral-intersection recovery retains every original job total despite masks and shared resource types.
- All six load bounds, zero cases and one-sided target optimization are derived symbolically.

## Executable evidence

[verify_profile_certificates.py](../../../tools/verify_profile_certificates.py) checks the following finite claim:

All 915 nondecreasing positive integer load multisets of total at most 16, including the empty multiset, normalized by 16, fit at least one of the six profiles; the five nontrivial rounded-load sums equal <code class="math">3/2</code>. That scalar check covers profile geometry; the separate original-input reference below exercises resource and exact-budget recovery.

Run from the repository root:

```sh
python3 tools/verify_profile_certificates.py
```

The reusable `SixBackend` in the [scheduling reference](../../activated-machine-scheduling/reference/README.md)
implements all six profiles, full original-type LP constraints, joint
minimum-cost integral recovery and one-sided target optimization. Its
[realization proof](../../activated-machine-scheduling/reference-realization.md)
separates the direct six-profile client from the additional activation adapter.
The direct checker uses original scheduling inputs without activation or setup
transformations:

```sh
python3 -B problems/activated-machine-scheduling/verify/check_six_profiles.py
```

It checks 29 original instances, 145 targets, 29 optimizations, 4,176 fixed
profile vectors and 2,713 joint recoveries including 857 fractional witnesses.
Independent original-count enumeration checks all original ranks, mandatory
totals, costs and loads. Coverage includes 106 protected full-target profile
vectors, six examples each requiring a different unique profile, and 24
open-left/closed-right endpoint cases. Two malformed queries are rejected.

## Model and verification boundaries

The reference actually enumerates the six-profile product and realizes exact
budget recovery. Its complete rank tables, LP-vertex enumeration and numeric
count search have separately charged costs, including potentially exponential
vertex storage. It does not claim the fast polynomial fixed-profile oracle
implementation. Arbitrary-rational coverage, approximation and the fast
oracle-model bounds are mathematical proofs, distinct from finite execution.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** icekylinx and GPT-6 Astra Pro.
