# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md) and the following companion manuscripts:

- [Compressed large-job slots and corank scheduling with arbitrary smaller sizes](../slot-surplus.md)

## Mathematical evidence

- Exact rational bin endpoints cover full-target schedules, and the profile count includes actual enumeration work and accuracy encoding.
- Upper-prefix recovery on the pair ground preserves every mandatory original type base and one assignment-cost budget, including zero-time coordinates.
- The slot-surplus companion proves its own protected target search, compressed weighted-sum decomposition and polynomial workspace for a binary-encoded slot budget.
- The [reference realization proof](../reference-realization.md) connects the
  occupied-profile iterator and shared joint recovery to the primary theorem
  with the reference LP/count costs charged separately.

## Executable evidence

[check_profiles.py](check_profiles.py) compares the
[profile client](../reference/profiles.py) with independent enumeration of all
original count schedules. The suite checks 25 instances, 250 targets and 50
optimized outputs, plus 558 fixed plans and 581 joint recoveries including 221
fractional witnesses. Original rank inequalities, mandatory totals, budget and
actual load are checked independently. It constructs 158 protected profiles from
full-target schedules and checks their joint LPs.

Separate rectangular enumeration compares 345 occupied-bin profile families
and all 2,154 emitted vectors, including both count and lower-load pruning.
Forty bin-boundary checks cover open-left/closed-right conventions. Five
binary-accuracy checks use an 81-bit accuracy denominator, a formal bin universe
larger than a 150-bit power of two, a numerically huge count budget and one
actually occupied bin, including a completed target/optimization solve.
Four further checks traverse 1,100 occupied coordinates under zero/one count
budgets and 1,100 physical-machine iterators, including a completed target solve.
Both traversal levels use explicit bounded stacks, so these valid inputs exceed
ordinary language recursion depth without failure.

```sh
python3 problems/arbitrary-processing-scheduling/verify/check_profiles.py
```

These checks exercise the complete-table reference and its actual streamed
iterator. The inherited LP solver enumerates vertices and integer count vectors;
it does not implement the theorem's polynomial oracle primitives or establish
overall polynomial workspace by execution. The slot-surplus client is not
implemented, and its mathematical guarantee remains separately proved.

## Model and verification boundaries

The main theorem permits arbitrary machine-type times and one assignment budget. The slot-surplus companion instead uses common type sizes, no assignment budget, an additive largest-smaller-job loss, and its stated parameter promise at <code class="math">\mathrm{OPT}</code>.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
