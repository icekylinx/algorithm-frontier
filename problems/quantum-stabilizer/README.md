# Positive Pauli Hamiltonians and whole stabilizer blocks

The output retains whole original positive clauses or blocks and approximates every quantum state's energy in Loewner order. The ordinary sparse-support theorems and the stabilizer-witness approximation address different outputs.

## Results

All support bounds are capped by the original number of items $m$. Let $\rho=\log_2(2D)$, where $D$ is the total Hilbert-space dimension.

| Problem | Guarantee or retained support | Construction | Proof |
|---|---|---|---|
| Arbitrary-locality positive Pauli Hamiltonian on $n$ qubits | Existence $O((n+1)/\varepsilon^2)$; compact $O\!\left(\frac{(n+1)\log((n+2)/\varepsilon)}{\varepsilon^2}\right)$; optional exact total coefficient | Sharp-support construction is polynomial in $2^n$; compact construction is randomized polynomial in the binary input and $\varepsilon^{-1}$ | [Theorem 1](manuscripts/arbitrary-locality-pauli-sparsification.md) |
| Whole blocks of commuting checks on prime-dimensional $p$-level qudits, with arbitrary noncommutation between blocks | Existence $O\!\left(\frac{(n+1)\log p}{\varepsilon^2}\right)$; compact $O\!\left(\frac{(n+1)[\log p+\log((n+2)/\varepsilon)]}{\varepsilon^2}\right)$ | Compact randomized polynomial time; sharp-support construction uses an explicit character table; individual checks are included | [Theorem SB](manuscripts/arbitrary-locality-stabilizer-block-sparsification.md), [single-check corollary](manuscripts/arbitrary-locality-prime-qudit-checks.md) |
| Whole stabilizer blocks in arbitrary heterogeneous local dimensions $q_1,\ldots,q_n$ | Existence $O(\rho/\varepsilon^2)$; compact $O\!\left(\frac{\rho\log(2\rho/\varepsilon)}{\varepsilon^2}\right)$ | Compact randomized polynomial bit time without factoring; sharp-support construction polynomial in $D$; individual Weyl checks are included | [Theorems 1–2](manuscripts/arbitrary-dimension-whole-stabilizer-blocks.md), [single-check corollary](manuscripts/arbitrary-dimension-weyl-checks.md) |
| Positive Pauli ground-energy surrogate and stabilizer witness | Factor $2+\sqrt2$ relative to the actual ground energy; identical original/surrogate energy on every state of the constructed basis | Deterministic polynomial-time reduction; exact minimization by $2^d\operatorname{poly}(L)$ enumeration and polynomial space, $d\le n$ | [Theorem 1](manuscripts/commuting-surrogates-and-stabilizer-energy-witnesses.md) |
| Prime-dimensional individual-check ground-energy surrogate | Factor $2(1+p^{-1/2})$ and a compact stabilizer witness | Deterministic compact polynomial-time reduction; $p^n\operatorname{poly}(L)$ enumeration and polynomial space | [Corollary 2](manuscripts/commuting-surrogates-and-stabilizer-energy-witnesses.md) |
| Positive Pauli clauses after all $h$ correlated label deletions, at most $a$ labels per clause | Explicit-dimension support $O\!\left(\frac{\Gamma(h,a)(n+1)[n+\log(2Q/\delta)]}{\varepsilon^2}\right)$; compact support bound has an additional factor $\log(2m)$ | Randomized preprocessing, one common event of probability at least $1-\delta$, fixed coefficients for all failures | [Section 7](manuscripts/arbitrary-locality-pauli-sparsification.md) |
| Globally commuting prime-dimensional whole blocks after all label failures | $O\!\left(\frac{R\log(2R/\varepsilon)}{\varepsilon^2}\right)$, $R=(n+1)\binom{h+a}{a}$ | Compact randomized polynomial time; all checks must commute across all blocks | [Block-failure theorem](../label-block-cut/manuscripts/exact-label-whole-blocks-and-hyperedges.md) |

For correlated failures, $Q=\sum_{j=0}^h\binom{L}{j}$ and $\Gamma(h,a)=\frac{(h+a)^{h+a}}{h^h a^a}$, with value one if either parameter is zero; $L$ is the number of occurring labels. These failures delete specified clauses or blocks.

## Contract

| Field | Statement |
|---|---|
| **Objective and output** | All-state relative energy approximation of positive Pauli or Weyl acceptance-projector penalties, with whole-item output; alternatively, the stated classical stabilizer-witness approximation. |
| **Time** | Compact sparsifier constructions are randomized polynomial in their full binary input length and inverse accuracy, with the stated success probability. Optimal-support constructions may be exponential in compact dimension. Surrogate construction is polynomial; its stated exact objective optimization is exponential. |
| **Space** | Support counts retained input objects. The witness-enumeration algorithms use polynomial workspace and output a polynomial-size tableau. No independent workspace bound is inferred for other constructions. |
| **Parameters** | $n$ is qudit count; $p$ is prime local dimension; $q_j$ are arbitrary local dimensions; $D=\prod_{j=1}^n q_j$; $m$ counts original whole blocks; $\varepsilon$ is relative error. |
| **Model and representation** | Each block's checks commute internally. Ordinary block theorems permit arbitrary cross-block noncommutation and locality. Constant penalties and inconsistent internal targets are allowed. All phases and displacement labels have compact modular descriptions. |
| **Lower-bound scope** | Classical cut instances require $\Omega(n/\varepsilon^2)$ terms in the stated prime-dimensional regime. Multilevel checks for $q=2^k$ require $\Omega(n\log q/\varepsilon^2)$ when $\varepsilon\le1/4$ and $n\ge2\left\lceil(2\varepsilon)^{-2}\right\rceil$. |
| **Review status** | The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed. |
| **Source** | [Proofs](proof.md), [manuscript and reference map](sources.md), [operator and algebra review](verify/README.md), [finite evidence](verify/README.md). |

Prime-dimensional and general-dimensional compact bounds are both retained because their parameter dependences differ. The positive identity shifts are part of the supplied Hamiltonian, and the witness factors apply to that objective.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
