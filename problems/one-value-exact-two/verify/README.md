# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md) and the following companion manuscripts:

- [One-value optional allocation with a shared setup and assignment budget](../setup-tradeoffs.md)

## Mathematical evidence

- The budgeted count projection has an exact nonnegative support separator, and one actual selected-basis witness survives omissions.
- An exact one-unit gate handles small quotas; higher quotas use integral recovery with minimum actual assignment cost.
- The setup companion retains an attaining cheapest basis and a protected combined-budget witness. Rational reoptimization removes target-search error.

## Executable evidence

[verify_profile_certificates.py](../../../tools/verify_profile_certificates.py) checks the following finite claim:

Integer-quota arithmetic: d=2,...,30 and every d<K<=399 (11,107 cases) satisfy K/(K-ceil(K/d)) <= (d+1)/(d-1); every 1<=K<=d satisfies the one-unit gate. Selection, budgets, rank oracles and rounding are not executed.

Run from the repository root:

```sh
python3 tools/verify_profile_certificates.py
```

These programs do not implement the full algorithm or mechanically verify its oracle, approximation and running-time arguments.

## Model and verification boundaries

The finite quota test checks arithmetic in the fixed-integer tradeoff. Actual basis selection, shared setup and assignment cost, arbitrary recipient ranks and the corank time bound remain symbolic obligations in the manuscripts.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
