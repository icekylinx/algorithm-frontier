# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Robust unit allocation with bounded minimal infeasibility certificates](proof.md)

## Mathematical dependencies

- [Two exact scenario budgets already obstruct corank-FPT unit selection](../robust-two-scenario-hardness/proof.md)
- [A Fibonacci-base exact gate for width-two robust unit feasibility](../robust-width-two-allocation/proof.md)
- [A polynomial-space conversion from corank gaps to global exponential time](../whole-ground-allocation/global-conversion.md)
- [Faster global time for coarser integer-quota approximation](../whole-ground-allocation/integer-quotas.md)
- [Single-exponential corank time for weighted packing through first-violation prefixes](../whole-ground-allocation/selection.md)

## Executable evidence

- [verify_profile_certificates.py](../../tools/verify_profile_certificates.py): Integer-quota arithmetic: d=2,...,30 and every d<K<=399 (11,107 cases) satisfy K/(K-ceil(K/d)) <= (d+1)/(d-1); every 1<=K<=d satisfies the one-unit gate. Selection, budgets, rank oracles and rounding are not executed. Failure width and scenario feasibility are also outside the check.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
