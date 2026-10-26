# Verification and proof scope

## Ready for review: the reduction theorem

Theorem 1.1 is an unconditional deterministic reduction to exact general
matching. It includes exact or ranged cardinality with one feasibility
call; optimization uses a logarithmic number of calls. The selector is
built explicitly by the recursive permutation network, so it needs no
unimplemented sparse-selector oracle.

Run from the repository root:

```bash
python3 -B problems/degree-constrained-subgraphs/verify/check_reductions.py
```

The standard-library checker independently solves local bipartite
selector instances and exhaustively enumerates degree states on the
actual augmented multigraphs. It checks 2,580 selector cases, 634
interval-degree instances and 5,260 exact/ranged cardinality reductions.
The latter include all simple graphs through three vertices with all
valid degree intervals, plus explicit parallel-edge cases. Both sides
are compared with enumerated original edge subsets. These are finite
checks of the specified gadgets, not a substitute for the general proof.

## Conditional: the fast running-time corollary

The proof gives the sparse-selector and interval-degree reductions,
including parity, original-edge recovery and cardinality optimization. Its
fast running-time corollary inherits the matching backend and its explicitly
stated Contract R condition. The reduction does not independently establish
that backend.

Cap normalization, loop/parallel-edge conventions and actual output length
must be read with the theorem. A matching optimality verifier can validate the
auxiliary solution without establishing the claimed backend running time.
The finite checker does not implement the complete fast matching solver.

Read the [main proof](../proof.md) with its [source map](../sources.md). Repository checks validate links, mathematical syntax and catalogue coverage; they do not certify the asymptotic theorem. No proof-assistant verification or external peer review is claimed.
