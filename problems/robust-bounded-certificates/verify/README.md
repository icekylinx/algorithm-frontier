# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md).

## Mathematical evidence

- The width promise concerns minimal failures of the aggregate budget-feasible one-unit family, at least on player-independent sets.
- A scan returns an original minimal failure. Branches preserve a feasible common basis, prove a sound failure, or expose a failure wider than the supplied bound.
- Higher quotas share one selected basis while each scenario receives its own integral recovery under its exact budget.

## Executable evidence

[verify_profile_certificates.py](../../../tools/verify_profile_certificates.py) checks the following finite claim:

Integer-quota arithmetic: d=2,...,30 and every d<K<=399 (11,107 cases) satisfy K/(K-ceil(K/d)) <= (d+1)/(d-1); every 1<=K<=d satisfies the one-unit gate. Selection, budgets, rank oracles and rounding are not executed. Failure width and scenario feasibility are also outside the check.

Run from the repository root:

```sh
python3 tools/verify_profile_certificates.py
```

These programs do not implement the full algorithm or mechanically verify its oracle, approximation and running-time arguments.

## Model and verification boundaries

The width promise is substantive. The finite quota test does not verify width detection, scenario feasibility, common-basis reconstruction or the Fibonacci specialization. The unrestricted two-scenario obstruction is separate.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
