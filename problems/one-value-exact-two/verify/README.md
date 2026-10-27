# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md) and the following companion manuscripts:

- [One-value optional allocation with a shared setup and assignment budget](../setup-tradeoffs.md)

## Main theorem review scope

The bounded audit of 2026-10-27 reconstructs the main exact factor-two theorem
with arbitrary nonnegative assignment costs and one exact budget. It checks
loop deletion, the fixed downward service projection and nonnegative separator,
the weighted first-violation branch count including rejected calls, exact
minimum-cost quota recovery, the separate one-unit gate and the nonmonotone
one-sided integer search. It also checks the fixed-basis polynomial endpoint
and the inherited strict-below-two value-oracle threshold.

The [direct gate note](../one-unit-gate.md) supplies Boolean-cap augmentation
and the exact pair correspondence. Submodular minimization, exact rational LP,
and weighted matroid/polymatroid intersection remain paid mathematical
primitives with explicit local inputs. This scoped review does not certify
the separate shared-setup, general integer-factor or whole-ground conversion
extensions. No executable full allocator, external peer review or
proof-assistant verification is claimed.

## Mathematical evidence

- The budgeted count projection has an exact nonnegative support separator, and one actual selected-basis witness survives omissions.
- An exact one-unit gate handles small quotas; higher quotas use integral recovery with minimum actual assignment cost.
- The setup companion retains an attaining cheapest basis and a protected combined-budget witness. Rational reoptimization removes target-search error.

## Executable evidence

The [one-unit gate checker](check_one_unit_gate.py) verifies 69 resource ranks,
2,495 Boolean-cap augmentation pairs and 285 gate instances. It compares
14,901 original unit-assignment candidates with an independent enumeration
of 32,728 pair subsets, followed by 1,602 exact rational budget comparisons.
The families include uniform and weighted-coverage polymatroids, zero ranks,
resource loops, uniform and partition player matroids, zero costs and budgets,
and infeasible gates. This is finite structural evidence, not a general
weighted matroid-intersection implementation.

```sh
python3 -B problems/one-value-exact-two/verify/check_one_unit_gate.py
```

[verify_profile_certificates.py](../../../tools/verify_profile_certificates.py) checks the following finite claim:

Integer-quota arithmetic: <code class="math">d=2,\ldots,30</code> and every <code class="math">d&lt;K\le399</code> (11,107 cases) satisfy <code class="math">K/(K-\lceil K/d\rceil)\le(d+1)/(d-1)</code>; every <code class="math">1\le K\le d</code> satisfies the one-unit gate. Selection, budgets, rank oracles and rounding are not executed.

Run from the repository root:

```sh
python3 tools/verify_profile_certificates.py
```

These programs do not implement the full algorithm or mechanically verify its oracle, approximation and running-time arguments.

## Model and verification boundaries

The finite quota test checks arithmetic in the fixed-integer tradeoff. Actual basis selection, shared setup and assignment cost, arbitrary recipient ranks and the corank time bound remain symbolic obligations in the manuscripts.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
