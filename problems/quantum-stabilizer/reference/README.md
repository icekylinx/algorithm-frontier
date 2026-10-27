# Compact Pauli witness backend

[Native proof](../reference-realization.md) · [Constructor](pauli_witness.py) · [Independent verifier](verify_witness.py)

```python
from fractions import Fraction
from pauli_witness import Pauli, reduce_hamiltonian, minimize
from verify_witness import verify_witness

clauses = ((Fraction(1), Pauli(1, 0)),
           (Fraction(1), Pauli(0, 1)))
surrogate = reduce_hamiltonian(1, clauses)
witness = minimize(surrogate)
assert witness.energy == 1
assert verify_witness(1, clauses, witness)
```

`Pauli(x, z, sign=0)` uses binary X and Z masks; overlapping bits represent Y.
The sign is a bit, with one denoting a negative operator. Each original
`(weight, Pauli)` clause means its positive rational weight times identity
minus that signed Pauli. Identity shifts remain part of the original input.
Floats, nonpositive weights and masks outside the qubit count are rejected.

`reduce_hamiltonian` returns a complete commuting generator basis, original
scalar and weighted parity terms, and balanced-pair decomposition records.
Its `energy(assignment)` evaluates one generator eigenvalue assignment.
`minimize` enumerates only the effective rank of the parity rows and returns
a signed complete tableau with exact rational energy. This search may be
exponential. It optimizes the constructed basis, not every stabilizer basis.

`energy_of_tableau` in the verifier computes an arbitrary valid complete
tableau's original energy; `verify_witness` returns whether the claimed energy
is exact. Neither imports the reduction or optimizer. No Hilbert-space
matrices or state vectors are allocated by either reference module.
Prime-dimensional Weyl witnesses and sparsification are not implemented here.

```sh
python3 -B problems/quantum-stabilizer/verify/check_witness.py
```

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
