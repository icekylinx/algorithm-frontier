# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md) and the following companion manuscripts:

- [One-value optional allocation with a shared setup and assignment budget](../setup-tradeoffs.md)

## Complete proof review scope

The audit of 2026-10-27 reconstructs the main exact factor-two theorem
with arbitrary nonnegative assignment costs and one exact budget. It checks
loop deletion, the fixed downward service projection and nonnegative separator,
the weighted first-violation branch count including rejected calls, exact
minimum-cost quota recovery, the separate one-unit gate and the nonmonotone
one-sided integer search. It also checks the fixed-basis polynomial endpoint
and the inherited strict-below-two value-oracle threshold.

The [direct gate note](../one-unit-gate.md) supplies Boolean-cap augmentation
and the exact pair correspondence. Submodular minimization, exact rational LP,
and weighted matroid/polymatroid intersection remain paid mathematical
primitives with explicit local inputs. The extended audit also covers the
shared-setup companion, the general fixed-integer small-target and quota-ratio
arguments, and the streamed whole-ground conversion. It follows the same
protected original full basis through changing attained setup minima and
residual assignment budgets. The
[native realization](../reference-realization.md) proves a direct capped-service
dual separator, exact scalar minimum-cost quota recovery and both original
target-search contracts. No external peer review or proof-assistant
verification is claimed.

## Mathematical evidence

- The budgeted count projection has an exact nonnegative support separator, and one actual selected-basis witness survives omissions.
- An exact one-unit gate handles small quotas; higher quotas use integral recovery with minimum actual assignment cost.
- The setup companion retains an attaining cheapest basis and a protected combined-budget witness. Integer quota search introduces no rational utility approximation error.

## Executable evidence

The [full native checker](check_one_value.py) uses independent original
recipient count vectors and original player bases, without calling a derived
LP or gate as its optimum oracle. It checks 35 original-input instances,
1,072 target calls, 210 optional optimizations, 60 prescribed-basis exact
optima and 300 exact fixed-quota tests against 471 affordable original
allocations. It tests 140 direct service queries and checks all 286 packing
rows produced by omission nodes against independent original count allocations
under their current assignment budget. In 292 protected nodes it checks that
the attained setup minimum preserves the original full witness. Its 536
whole-ground calls include the actual four-player logarithmic-block wrapper.

The fixtures include zero rank, empty resources, unaffordable zero service,
zero budget, resource and player loops, weighted-coverage polymatroids,
nonuniform rational assignment and setup costs, uniform and partition player
matroids, a changing minimum-setup basis, and forced omissions that preserve
original resource ranks. An explicit fractional half-unit remains available
even when its whole unit is unaffordable. Four
binary-size fixtures run actual fixed and optional optimization, native LP
separation and varying-integer-factor coverage with more than 330-bit supplies
or quotas; no numerical unit enumeration is used on those inputs. Thirteen
malformed inputs are rejected.

```sh
python3 -B problems/one-value-exact-two/verify/check_one_value.py
```

The native allocator calls canonical exact weighted matroid intersection,
weighted first-crossing omission and streamed rational covers. Its concrete
Bland-simplex LP has a separate potentially exponential finite basis bound,
while retaining polynomial complete-table/binary workspace. Factor-two and
factor-three rational covers attain the sharp endpoints; other integer
factors use the documented certified rational envelope. The sharper
fixed-factor algebraic cover theorem is a distinct proved construction.

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

The full native checker executes the reference allocator. The older gate and
profile programs check their named finite subclaims. None mechanically proves
the unbounded oracle, approximation or running-time arguments.

## Model and verification boundaries

The finite quota test checks arithmetic in the fixed-integer tradeoff; the
native checker additionally exercises actual original-basis selection,
recipient ranks, shared setup and assignment budgets, no-loss recovery and
both target paths. The complete corank and whole-ground bounds rely on their
manuscript proofs and paid primitives, rather than on this finite evidence.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** icekylinx and GPT-6 Astra Pro.
