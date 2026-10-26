# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md) and the following companion manuscripts:

- [The exact-factor-two endpoint for arbitrary unrelated allocation](../exact-two.md)
- [Unrelated-value allocation with one shared setup and assignment budget](../setup-budget.md)
- [Integer-quota time tradeoffs for compulsory unrelated two-value allocation](../two-value-tradeoffs.md)

## Mathematical evidence

- One masked polymatroid represents each original resource across light and heavy roles, preserving shared capacity.
- The changing role LP retains a protected original full allocation with uniform rational descriptions.
- The setup companion keeps one combined original budget on an actual selected basis; enumeration proves exact two in 2^q polynomial time.
- J2 and the discrete factor-d companion prove their exact quota recovery for compulsory player-specific values in {0,u,a}.

## Executable evidence

[verify_profile_certificates.py](../../../tools/verify_profile_certificates.py) checks the following finite claim:

Integer-quota arithmetic: d=2,...,30 and every d<K<=399 (11,107 cases) satisfy K/(K-ceil(K/d)) <= (d+1)/(d-1); every 1<=K<=d satisfies the one-unit gate. Selection, budgets, rank oracles and rounding are not executed. This applies only to the compulsory J2 and factor-d quota arithmetic, not shared-resource or setup coupling.

Run from the repository root:

```sh
python3 tools/verify_profile_certificates.py
```

These programs do not implement the full algorithm or mechanically verify its oracle, approximation and running-time arguments.

## Model and verification boundaries

Near-two and the 2^q exact-two endpoint allow optional player bases. The faster J2 and discrete pair-value tradeoffs require compulsory players. Adding a dummy value does not preserve the two-value premise; finite quota tests do not check shared-resource or setup constructions.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
