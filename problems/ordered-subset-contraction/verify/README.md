# Exact runnable verification

**Attribution:** icekylinx and GPT-6 Astra Pro. Apache-2.0.

From the repository root, with Python 3.10 or later and no third-party packages:

```sh
python3 problems/ordered-subset-contraction/verify/check_ordered_subset.py
python3 problems/ordered-subset-contraction/verify/check_integer_capacities.py
python3 problems/ordered-subset-contraction/verify/check_cyclic_compiler.py
```

The first check compares direct injective assignments, direct disjoint triples, the five-role identity, trimmed upper transforms, ordered block DP and actual matrix-profile contraction. It uses exact 2 by 2 matrices over the integers and modulo `2,4,6`, arbitrary unrelated subset weights, overfull row counts and the nonunital ring `2 M2(Z)`. Deliberately reversing the final factor produces counterexamples.

The second exhausts all `729` ordered capacity triples with coordinates `0..8`, including the input-table exponent. Exact rational maxima check the integer `U` formula, the characteristic-two formula, `g<=1` reduction and square-tiling envelopes at `omega=2,9/4,5/2,3`. This checks a stated finite cost certificate, not matrix or circuit optimality.

The third compiles shared arithmetic circuits and compares all cyclic derivatives with an independent exact ordered-word oracle. It tests repeated variable names and repeated operands, reductions modulo `2,4,6`, the selected-row rotation, conservative row-degree guards, malformed inputs, the linear arithmetic charge and an actual CLI serialization round trip. Its seeded generated cases are reproducible finite examples, not a probabilistic correctness argument.

The scripts write JSON reports beneath `results/`; timestamps and source hashes describe the current run. Their success checks finite identities. The mathematical proof supplies the uniform asymptotic bound in each stated matrix interface: universal rings for square tiling, scalar fields for the stronger full rectangular refinements. No fast matrix scheme, square-permanent advance, historical priority or external formal verification is certified by these scripts.

A reusable compiler CLI is also available:

```sh
python3 problems/ordered-subset-contraction/reference/cyclic_circuit_compiler.py \
  problems/ordered-subset-contraction/examples/cyclic_row_input.json \
  --rotate-row z --output /tmp/ordered-cyclic-output.json
```

The ordered subset prototype exposes `block_table`, `upper_zeta`, `direct_disjoint`, `marker_expansion`, `grouped_triangle` and exact matrix-ring arithmetic as importable functions. Its `main` is the first verification command above; its matrix products are deliberately naive.
