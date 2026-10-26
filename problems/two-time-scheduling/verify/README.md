# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md).

## Mathematical evidence

- Masks preserve each original mandatory amount and machine classes inherit a full-target witness.
- Exact small-quota gates and scaled support coordinates supply the heterogeneous omission inequality.
- All machine classes share one maximum-total integral recovery and assignment-cost objective. A disjoint modular zero-time block and a zero-target gate handle zero processing times.

## Executable evidence

[verify_profile_certificates.py](../../../tools/verify_profile_certificates.py) checks the following finite claim:

Integer-quota arithmetic: d=2,...,30 and every d<K<=399 (11,107 cases) satisfy K/(K-ceil(K/d)) <= (d+1)/(d-1); every 1<=K<=d satisfies the one-unit gate. Selection, budgets, rank oracles and rounding are not executed. Target-dependent masks and zero-time feasibility are not tested.

Run from the repository root:

```sh
python3 tools/verify_profile_certificates.py
```

These programs do not implement the full algorithm or mechanically verify its oracle, approximation and running-time arguments.

## Model and verification boundaries

Each machine has at most two positive eligible times; the pair may differ across machines and zero times are allowed. The tradeoff parameter d is a fixed integer at least two. The finite arithmetic test does not verify masks, zero-time feasibility or cost recovery.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
