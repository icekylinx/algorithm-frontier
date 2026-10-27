# Verification and scope

The [main proof](../proof.md) and [reference realization](../reference-realization.md)
supply separate mathematical and executable evidence.

## Mathematical review

Internal review covers the exact width-two one-unit gate, including
complete original singleton/pair conflict tests, forced omissions in the
dual player matroid, the matching terminal's independent representatives
and basis completion, degree branching and its full Fibonacci node bound.
Actual final scenario tests and minimal shrinking give sound all-input
success/failure/width-violation semantics. The streamed whole-ground
conversion and its fixed-quadratic exact comparisons have been checked
against that uniform extension interface. Boolean-resource exact
optimization follows because no count can exceed one.

Section 8's higher-quota factor tradeoffs retain their stated dependencies
but are outside this scoped review. General budgeted polymatroid unit tests
remain the paid interface proved in the bounded-certificate allocation
manuscript. The implementation supplies the polynomial matching
intersection algorithm, using the explicitly identified standard
augmenting-path theorem rather than assuming a missing terminal solver.

## Executable evidence

```sh
python3 problems/robust-width-two-allocation/verify/check_width_two.py
```

The [local gate](../reference/README.md) is checked against independently
enumerated original selected bases and common independent sets:

- 3,252 exhaustive simple-graph/uniform-matroid cases on up to four players,
  covering all ranks and every permitted forced-omission seed.
- 400 seeded binary-represented player matroids with singleton loops,
  pair conflicts and forced omissions; rank is computed by exact binary
  elimination, without constructing the dual matroid in the checker.
- 300 matroid-intersection outputs compared with exhaustive common-
  independent-set optima for two independently generated binary matroids.
- 15 minimal higher-width certificates, verified by original infeasibility
  and feasibility of every single deletion, plus a modular-budget guard.
- Explicit matching representative/exchange/completion cases, sound
  off-promise success and failure, five malformed input rejections,
  and Fibonacci node-count bounds for the graph tests.

Native conflict scenarios use one Boolean partition resource per scenario.
The budget guard has unit modular prices and a two-unit exact budget.
The exhaustive comparators do not call the dual-cover solver or the
matroid-intersection routine. They use the same supplied original rank
oracle and scenario predicates, as required by their common model.
Finite comparisons do not prove the general augmentation theorem or
validate arbitrary external oracle implementations.

## Model and implementation boundaries

The reference realizes the local Fibonacci gate with paid exact original
rank and scenario-unit callbacks. It returns actual callback witnesses,
but does not implement general weighted polymatroid allocation, higher-
quota recovery or the streamed whole-ground wrapper. Costs, binary
capacities and resource multiplicities are never expanded into unit
records. A width violation is a separate structural certificate and
never a failed extension.

The separate whole-ground rank-oracle obstruction does not determine
an optimal base for explicit instances. The [source map](../sources.md)
identifies the named mathematical dependencies. Repository checks validate
links, notation and generated surfaces, not mathematical correctness.
External peer review and proof-assistant verification are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
