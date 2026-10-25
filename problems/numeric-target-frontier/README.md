# Numeric-target and support-sensitive frontier

| Item | Result |
|---|---|
| **Priority** | Tier A headline record: the newest incremental family and the main place to read the target/support tradeoff. |
| **Guarantee** | Exact target decision and exact scalar optimization for one globally coupled integral polymatroid, plus deterministic approximation and support-sensitive refinements. |
| **Objective** | Upper, equality, or covering target rows with one signed scalar MIN/MAX; approximation records state direction separately. |
| **Time** | Arbitrary rows: `2^(O((T + 1) log(T + 2)) * poly(H))`. Fixed `d` rows: `exp(O_d((T + 1)^(d / (d + 1))) * poly(H))`. Support-sensitive S bound: `2^(O(T log(2 + Q/T)) * poly(H))` for `T > 0` after preprocessing. |
| **Space** | Polynomial binary workspace in the stated oracle or readable-program model; no unit expansion of binary counts. |
| **Parameters** | `T` is the numeric target sum, `Q` is the number of distinct nonempty eligible-column support patterns, `d` is fixed row dimension, and `H` includes binary input and paid polynomial primitive work. |
| **Representation** | R and S cover independent regions or original-total bases of one arbitrary integral polymatroid. Mandatory totals, exact budgets, and representation boundaries are stated per source. |
| **Lower bound** | R gives matching-order rank-oracle boundaries. S adds a two-parameter query classification and separate deterministic-ETH consequences for readable rank programs/circuits. These are not lower bounds for every explicit matroid class or ordinary graph matching. |
| **Status** | Internal full mathematical review is recorded in the checkpoints; no formal verification or external peer review is claimed. |

The central distinction is between the numeric budget `T` and the support geometry `Q`. S removes an arity restriction: a column may meet many rows while its support pattern is counted once. The budget envelope and geometry-sensitive refinements are therefore displayed separately.

See the [complexity guide](../../docs/COMPLEXITY.md), [complete index](../../CONTENTS.md), [proof map](proof.md), and [source map](sources.md).

**Sources.** [`sources/checkpoint-r/CHECKPOINT_R_INCREMENT.md`](../../sources/checkpoint-r/CHECKPOINT_R_INCREMENT.md) and [`sources/checkpoint-s/CHECKPOINT_S_INCREMENT.md`](../../sources/checkpoint-s/CHECKPOINT_S_INCREMENT.md).

**Attribution.** Yilin Liu · GPT-6 Astra Pro
