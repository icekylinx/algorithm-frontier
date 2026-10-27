# Verification and proof scope

## Ready for review: historical labels

The small-to-large representation and Corollary 9.1 have complete proofs
independent of the raw backend, once the exact merge sequence is given.
Historical equality costs

<!-- math-display: f11830ebe3dac2ffab24edf4
O(1+\log\log(n+2))
-->
![Formula](../../../assets/math/f11830ebe3dac2ffab24edf4.svg)
; first coalescence costs
<!-- math-display: f11830ebe3dac2ffab24edf4
O(1+\log\log(n+2))
-->
![Formula](../../../assets/math/f11830ebe3dac2ffab24edf4.svg)
 and binary-searches the common suffix of the two label histories.

Run from the repository root:

```bash
python3 -B problems/incremental-scc/verify/check_label_history.py
```

The checker enumerates 2,419 merge/batching histories through five
vertices, checking 193,340 historical equalities and 59,214 first
coalescence answers against explicit partition snapshots. It includes
multiple internal merges in one settled external update. This finite
evidence concerns the representation, not the numerical SCC solver.

## Ready for review: fast SCC maintenance

The proof gives the SCC contraction and component-label composition with
logarithmic-barrier accounting. Section 1 instantiates the generic client
with the [quantitative raw backend](../../../manuscripts/graph-backends/quantitative-matching-4-5-composition.md),
the [exact base and retirement bridge](../../../manuscripts/graph-backends/raw-cycle-to-frozen-detector-bridge.md)
and the [lifetime construction](../../../manuscripts/graph-backends/numerical-backend-lifetime-and-loops.md).
These local proofs and their named deterministic public inputs establish
the stated numerical envelope. The output contract is exact component
labels; the history checker above tests a separate representation layer.

Transpose access and topological ordering require additional interfaces;
they are not inferred from the component-label theorem. The current graph,
initialization and retirement work are charged in the proof. No executable
end-to-end SCC data structure is supplied.

Read the [main proof](../proof.md) with its [source map](../sources.md). Repository checks validate links, mathematical syntax and catalogue coverage; they do not certify the asymptotic theorem. No proof-assistant verification or external peer review is claimed.
