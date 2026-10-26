# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md).

## Mathematical evidence

- The reduction uses two explicit scenarios, the common basis rank q-k, free Boolean resources and nonnegative assignment costs.
- Both budgets hold exactly when the omitted k-set has the prescribed sum. Positive common service is the encoded decision event.
- The proof imports the identified parameterized k-SUM hardness result and retains c=k; the whole-ground rank-oracle obstruction has a different representation and conclusion.

## Executable evidence

[verify_finite_reductions.py](../../../tools/verify_finite_reductions.py) checks the following finite claim:

Exhaustive reduction identity for q=2,...,7, every vector in {0,1,2,3}^q, all 1<=k<q, every omitted k-subset and every integer target from zero through the total sum. It checks equivalence of the two budget inequalities and the target subset sum, not W[1]-hardness itself.

Run from the repository root:

```sh
python3 tools/verify_finite_reductions.py
```

These programs do not implement the full algorithm or mechanically verify its oracle, approximation and running-time arguments.

## Model and verification boundaries

Exhaustive small instances test the exact reduction identity, not W[1]-hardness itself. The complexity conclusion depends on the cited source problem and parameter-preserving proof. No ETH bound or optimal whole-ground base follows from this finite check.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
