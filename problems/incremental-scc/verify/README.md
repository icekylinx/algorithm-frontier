# Verification and proof scope

## Ready for review: historical labels

The small-to-large representation and Corollary 9.1 have complete proofs
independent of the raw backend, once the exact merge sequence is given.
Historical equality costs $`O(1+\log\log(n+2))`$; first coalescence costs
$`O(1+\log\log(n+2))`$ and binary-searches the common suffix of the two label histories.

Run from the repository root:

```bash
python3 -B problems/incremental-scc/verify/check_label_history.py
```

The checker enumerates 2,419 merge/batching histories through five
vertices, checking 193,340 historical equalities and 59,214 first
coalescence answers against explicit partition snapshots. It includes
multiple internal merges in one settled external update. This finite
evidence concerns the representation, not the numerical SCC solver.

## Conditional: fast SCC maintenance

The proof gives the SCC contraction and component-label composition with
logarithmic-barrier accounting. Its numerical envelope retains the stated
graph hierarchy and raw-backend conditions. The output contract is exact
component labels, not a topological ordering or a path witness.

Transpose access and topological ordering require additional interfaces;
they are not inferred from the component-label theorem. The current graph,
initialization and retirement work are charged in the proof. No executable
end-to-end SCC data structure is supplied.

Read the [main proof](../proof.md) with its [source map](../sources.md). Repository checks validate links, mathematical syntax and catalogue coverage; they do not certify the asymptotic theorem. No proof-assistant verification or external peer review is claimed.
