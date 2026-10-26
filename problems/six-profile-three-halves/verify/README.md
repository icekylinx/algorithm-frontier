# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md).

## Mathematical evidence

- The quarter-threshold classification covers every normalized full-target load with the stated interval boundaries and small-load caps.
- A single cost-preserving integral-intersection recovery retains every original job total despite masks and shared resource types.
- All six load bounds, zero cases and one-sided target optimization are derived symbolically.

## Executable evidence

[verify_profile_certificates.py](../../../tools/verify_profile_certificates.py) checks the following finite claim:

All 915 nondecreasing positive integer load multisets of total at most 16, including the empty multiset, normalized by 16, fit at least one of the six profiles; the five nontrivial rounded-load sums equal 3/2. General rational coverage, resource feasibility and exact-budget recovery remain symbolic.

Run from the repository root:

```sh
python3 tools/verify_profile_certificates.py
```

These programs do not implement the full algorithm or mechanically verify its oracle, approximation and running-time arguments.

## Model and verification boundaries

The grid check supports profile geometry. It does not replace the arbitrary-rational coverage proof, or implement rank queries, LP separation, exact-budget recovery or the 6^q profile enumeration.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
