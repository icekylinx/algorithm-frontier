# Verification and proof scope

The proof gives the sparse-selector and interval-degree reductions,
including parity, original-edge recovery and cardinality optimization. Its
fast running-time corollary inherits the matching backend and its explicitly
stated Contract R condition. The reduction does not independently establish
that backend.

Cap normalization, loop/parallel-edge conventions and actual output length
must be read with the theorem. A matching optimality verifier can validate the
auxiliary solution without establishing the claimed backend running time.
There is no end-to-end implementation of these reductions in this repository.

Read the [main proof](../proof.md) with its [source map](../sources.md). Repository checks validate links, mathematical syntax and catalogue coverage; they do not certify the asymptotic theorem. No proof-assistant verification or external peer review is claimed.
