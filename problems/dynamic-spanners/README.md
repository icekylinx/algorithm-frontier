# Dynamic spanners with recourse tradeoffs

Two dynamic-spanner constructions are retained because their recourse contracts differ. Their stretch exponents should not be compared while dropping those assumptions.

| Field | Curated statement |
|---|---|
| **Guarantee** | Maintains a spanner of an arbitrary-degree undirected graph with the stated stretch, size, amortized work, and output-recourse guarantee. |
| **Objective and output** | Maintain a sparse spanner and report its current edge set after settled updates. |
| **Time** | Tracked-terminal row: total initialization/update work `(n+m0+I+D) exp(O(U^(4/5) h^(1/5)))`; full-horizon row: `(n+m0+I+D) exp(O(U^(5/6) h^(1/6)))`. |
| **Full-horizon row** | Stretch and work follow the five-sixths envelope. Output recourse is proportional to the fixed vertex count plus the number of deletions, with no dependence on the cumulative insertion count. |
| **Tracked-terminal row** | Stretch, work, and ordinary output recourse follow the four-fifths envelope. The recourse bound includes insertions and deletions in the declared history. |
| **Space** | The current spanner has the fixed vertex count multiplied by the row’s stretch factor in edges. The hierarchy pays actual initial edges and actual update history. |
| **Parameters** | **n** is the fixed vertex count; **m0** is the initial edge count; **I** and **D** count edge insertions and deletions; **N** is the declared polynomial history cap; **U** is log of N plus a constant; **h** is log of U plus a constant. **D** is also the deletion term in the full-horizon recourse row. |
| **Model and representation** | Unweighted undirected graphs, with distinct identifiers for parallel edge lifetimes and settled external updates. Both rows are amortized. Self-loops are discarded. |
| **Lower-bound scope** | This page records two upper-bound constructions and their incomparable recourse assumptions. It does not claim an optimality lower bound. |
| **Review status** | Internal proof, algorithm, and source review is tracked in the [headline review report](../../reviews/headline/dynamic-graph-frontier.md). Finite audit notes are evidence for the constructions; they are not formal verification. |
| **Source** | [Tracked-terminal construction](../../sources/checkpoint-o/tracked_terminal_flat_spanner_four_fifths.md) and [full-horizon construction](../../sources/checkpoint-o/fully_dynamic_spanner_five_sixths.md). |

Read the [proof map](proof.md), [source map](sources.md), and [complexity guide](../../docs/COMPLEXITY.md) for the exact envelopes and recourse accounting.


**Attribution.** Yilin Liu · GPT-6 Astra Pro
