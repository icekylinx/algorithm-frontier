# Quantum, Pauli, qudit, and stabilizer blocks — checkpoint X draft

**Status: Draft checkpoint X.** Family-level review handle; not promoted.

| Field | Candidate statement |
|---|---|
| **Guarantee** | Drafts cover arbitrary-locality positive Pauli Hamiltonians, prime-qudit checks, whole stabilizer blocks, arbitrary-dimension Weyl checks, commuting surrogates, and heterogeneous local dimensions. |
| **Objective and output** | Preserve positive Hamiltonian energy or accepting-projector penalties for every stated state/character query while retaining whole original terms or blocks. |
| **Time** | Displayed support orders include `O(n/epsilon^2)` existential Pauli support, compact randomized `O((n+1) log((n+2)/epsilon)/epsilon^2)`, explicit prime-qudit `log p` terms, and arbitrary-dimension whole blocks with `O(log(2D)/epsilon^2)` existential support plus an extra compact-construction logarithm. |
| **Space** | Local dimension, Hilbert dimension `D`, stabilizer rank, and compact block descriptions are separate. Exact optimal-support constructions may be exponential in compact input. |
| **Parameters** | `n` is site/qudit count; `p` is prime dimension; `q` is general local dimension; `D` is total Hilbert dimension; `epsilon` is error; locality and internal block rank are explicit. |
| **Model and representation** | Positive Pauli/Weyl terms, commuting stabilizer blocks, or affine finite-field projectors exactly as stated. Whole blocks remain atomic. |
| **Lower-bound scope** | Cut-code and block lower families apply only in their stated commuting or homogeneous regimes; no general quantum complexity lower bound is asserted. |
| **Review status** | Proof, algorithm, and source review are pending; formal verification is not claimed. |
| **Source** | Payloads `21`, `22`, `23`, `24`, `25`, and `34` in the checkpoint-X source tree. |

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
