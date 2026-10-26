# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md) and the following companion manuscripts:

- [Corank omission with a changing residual budget](../adaptive-selection.md)
- [A polynomial-space conversion from corank gaps to global exponential time](../global-conversion.md)
- [Faster global time for coarser integer-quota approximation](../integer-quotas.md)
- [Rational comparator recovery without splitting the approximation error](../rational-optimization.md)
- [Single-exponential corank time for weighted packing through first-violation prefixes](../selection.md)

## Mathematical evidence

- Forced omissions retain one full original witness, and local extension time includes failures and restriction-selector work.
- The deterministic block cover counts profiles and Cartesian-product choices while proving polynomial workspace.
- Weighted selection, adaptive budgets and rational optimization have separate manuscripts, retaining each application’s family, comparator and exact constraints.
- Scheduling keeps the physical ground in its dual, allocation retains heavy options after seeding, and integer quotas have separate one-unit endpoints.

## Executable evidence

[verify_profile_certificates.py](../../../tools/verify_profile_certificates.py) checks the following finite claim:

Integer-quota arithmetic: d=2,...,30 and every d<K<=399 (11,107 cases) satisfy K/(K-ceil(K/d)) <= (d+1)/(d-1); every 1<=K<=d satisfies the one-unit gate. Selection, budgets, rank oracles and rounding are not executed. Only the integer-quotas companion is covered; no global-conversion check is claimed.

Run from the repository root:

```sh
python3 tools/verify_profile_certificates.py
```

These programs do not implement the full algorithm or mechanically verify its oracle, approximation and running-time arguments.

## Model and verification boundaries

Finite quota tests support only the integer-tradeoff companion. They do not implement global covering families or establish their subexponential overhead. Approximation, rank-oracle, fixed-accuracy and bit-complexity claims retain the distinct models of each transfer.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
