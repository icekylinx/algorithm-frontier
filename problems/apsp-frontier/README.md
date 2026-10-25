# Fully dynamic APSP tradeoff frontier

This is a Tier A record of incomparable fully dynamic all-pairs shortest-path tradeoffs. The rows are deliberately shown as a frontier rather than collapsed into one “best” point.

| Field | Curated statement |
|---|---|
| **Guarantee** | Maintains approximate all-pairs distances under fully dynamic updates with the stretch stated by each row. |
| **Objective and output** | Trade update work against distance stretch; answer distance queries in polylogarithmic time under the audited hierarchy interface. |
| **Tradeoff A** | Amortized update factor with leading exponent eleven-fourteenths in the master logarithm, paired with stretch whose leading exponent is six-sevenths times the hierarchy parameter **h**. |
| **Tradeoff B** | Amortized update factor with leading exponent three-fourths and a square-root dependence on **h**, paired with stretch of order the master parameter divided by **h**. |
| **Space** | Actual-size hierarchy storage and query structures, charged to the graph inventory and update history; no master-cap padding is materialized. |
| **Parameters** | **n** is the fixed vertex count; **m** is the current edge count; **N** is the declared polynomial history cap; **U** is log of N plus a constant; **h** is log of U plus a constant. Local depth and branching parameters are rounded as specified in the source. |
| **Model and representation** | Fully dynamic weighted-graph distance oracle with the source’s update encoding, positive polynomial-range lengths, and amortized maintenance. |
| **Lower-bound scope** | The record is an upper-bound frontier and comparison map. It does not assert that either point is globally optimal. |
| **Review status** | Internal proof, algorithm, and source review is tracked in the [headline review report](../../reviews/headline/dynamic-graph-frontier.md). Finite audit notes are evidence for the listed tradeoffs; they are not formal verification. |

Read the [proof map](proof.md), [source map](sources.md), and [complexity guide](../../docs/COMPLEXITY.md) for the exact symbolic forms and comparison points.

**Source.** [APSP time/stretch curve](../../sources/checkpoint-o/fully_dynamic_apsp_time_stretch_curve.md).

**Attribution.** Yilin Liu · GPT-6 Astra Pro
