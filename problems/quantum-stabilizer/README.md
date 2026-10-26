# Positive Pauli Hamiltonians and whole stabilizer blocks

The output retains whole original positive clauses or blocks and approximates every quantum state's energy in Loewner order. The ordinary sparse-support theorems and the stabilizer-witness approximation address different outputs.

## Results

All support bounds are capped by the original number of items <code class="math">m</code>. Let <code class="math">\rho=\log_2(2D)</code>, where <code class="math">D</code> is the total Hilbert-space dimension.

**Arbitrary-locality positive Pauli Hamiltonian on <code class="math">n</code> qubits**

**Guarantee or retained support.** Existence <code class="math">O((n+1)/\varepsilon^2)</code>; compact <code class="math">O\!\left(\frac{(n+1)\log((n+2)/\varepsilon)}{\varepsilon^2}\right)</code>; optional exact total coefficient

**Construction.** Sharp support is existential, with a Monte Carlo construction polynomial in <code class="math">2^n</code>, success at least <code class="math">2/3</code>; compact construction is Monte Carlo polynomial in binary input and <code class="math">\varepsilon^{-1}</code>, success at least <code class="math">2/3</code>

**Proof.** [Theorem 1](manuscripts/arbitrary-locality-pauli-sparsification.md)

**Whole blocks of commuting checks on prime-dimensional <code class="math">p</code>-level qudits, with arbitrary noncommutation between blocks**

**Guarantee or retained support.** Existence <code class="math">O\!\left(\frac{(n+1)\log p}{\varepsilon^2}\right)</code>; compact <code class="math">O\!\left(\frac{(n+1)[\log p+\log((n+2)/\varepsilon)]}{\varepsilon^2}\right)</code>

**Construction.** Compact Monte Carlo polynomial time, success at least <code class="math">2/3</code>; sharp support has a Monte Carlo explicit-character-table construction, success at least <code class="math">2/3</code>; individual checks are included

**Proof.** [Theorem SB](manuscripts/arbitrary-locality-stabilizer-block-sparsification.md), [single-check corollary](manuscripts/arbitrary-locality-prime-qudit-checks.md)

**Whole stabilizer blocks in arbitrary heterogeneous local dimensions <code class="math">q_1,\ldots,q_n</code>**

**Guarantee or retained support.** Existence <code class="math">O(\rho/\varepsilon^2)</code>; compact <code class="math">O\!\left(\frac{\rho\log(2\rho/\varepsilon)}{\varepsilon^2}\right)</code>

**Construction.** Compact Monte Carlo polynomial bit time without factoring, success at least <code class="math">2/3</code>; sharp support has a Monte Carlo construction polynomial in <code class="math">D</code>, success at least <code class="math">2/3</code>; individual Weyl checks are included

**Proof.** [Theorems 1–2](manuscripts/arbitrary-dimension-whole-stabilizer-blocks.md), [single-check corollary](manuscripts/arbitrary-dimension-weyl-checks.md)

**Positive Pauli ground-energy surrogate and stabilizer witness**

**Guarantee or retained support.** Factor <code class="math">2+\sqrt2</code> relative to the actual ground energy; identical original/surrogate energy on every state of the constructed basis

**Construction.** Deterministic polynomial-time reduction; exact minimization by <code class="math">2^d\mathrm{poly}(L)</code> enumeration and polynomial space, <code class="math">d\le n</code>

**Proof.** [Theorem 1](manuscripts/commuting-surrogates-and-stabilizer-energy-witnesses.md)

**Prime-dimensional individual-check ground-energy surrogate**

**Guarantee or retained support.** Factor <code class="math">2(1+p^{-1/2})</code> and a compact stabilizer witness

**Construction.** Deterministic compact polynomial-time reduction; <code class="math">p^n\mathrm{poly}(L)</code> enumeration and polynomial space

**Proof.** [Corollary 2](manuscripts/commuting-surrogates-and-stabilizer-energy-witnesses.md)

**Positive Pauli clauses after all <code class="math">h</code> correlated label deletions, at most <code class="math">a</code> labels per clause**

**Guarantee or retained support.** Explicit-dimension support <code class="math">O\!\left(\frac{\Gamma(h,a)(n+1)[n+\log(2Q/\delta)]}{\varepsilon^2}\right)</code>; compact support bound has an additional factor <code class="math">\log(2m)</code>

**Construction.** Monte Carlo preprocessing; one common event of probability at least <code class="math">1-\delta</code> covers all failures and all states with fixed coefficients

**Proof.** [Section 7](manuscripts/arbitrary-locality-pauli-sparsification.md)

**Globally commuting prime-dimensional whole blocks after all label failures**

**Guarantee or retained support.** <code class="math">O\!\left(\frac{R\log(2R/\varepsilon)}{\varepsilon^2}\right)</code>, <code class="math">R=(n+1)\binom{h+a}{a}</code>

**Construction.** Compact Monte Carlo polynomial time, success at least <code class="math">2/3</code> on one all-query/all-failure event; all checks must commute across all blocks

**Proof.** [Block-failure theorem](../label-block-cut/manuscripts/exact-label-whole-blocks-and-hyperedges.md)

For correlated failures, <code class="math">Q=\sum_{j=0}^h\binom{L}{j}</code> and <code class="math">\Gamma(h,a)=\frac{(h+a)^{h+a}}{h^h a^a}</code>, with value one if either parameter is zero; <code class="math">L</code> is the number of occurring labels. These failures delete specified clauses or blocks.

## Contract

**Objective and output**

All-state relative energy approximation of positive Pauli or Weyl acceptance-projector penalties, with whole-item output; alternatively, the stated classical stabilizer-witness approximation.

**Randomness**

Mixed. Compact and explicit-dimension whole-block sparsification are Monte Carlo with success at least <code class="math">2/3</code>; correlated Pauli preprocessing succeeds with probability at least <code class="math">1-\delta</code> simultaneously for all allowed failures. Sharp support is existential in the compact-input model. Stabilizer-basis surrogate construction and the stated exponential exact witness enumeration are deterministic. All sampling is classical preprocessing randomness.

**Time**

Compact sparsifier constructions are Monte Carlo polynomial in their full binary input length and inverse accuracy, with the stated success probability. Optimal-support constructions may be exponential in compact dimension. The randomness is classical preprocessing sampling, with no quantum sampling oracle. Surrogate construction and its stated exponential exact objective enumeration are deterministic.

**Space**

Support counts retained input objects. The witness-enumeration algorithms use polynomial workspace and output a polynomial-size tableau. No independent workspace bound is inferred for other constructions.

**Parameters**

<code class="math">n</code> is qudit count; <code class="math">p</code> is prime local dimension; <code class="math">q_j</code> are arbitrary local dimensions; <code class="math">D=\prod_{j=1}^n q_j</code>; <code class="math">m</code> counts original whole blocks; <code class="math">\varepsilon</code> is relative error.

**Model and representation**

Each block's checks commute internally. Ordinary block theorems permit arbitrary cross-block noncommutation and locality. Constant penalties and inconsistent internal targets are allowed. All phases and displacement labels have compact modular descriptions.

**Lower-bound scope**

Classical cut instances require <code class="math">\Omega(n/\varepsilon^2)</code> terms in the stated prime-dimensional regime. Multilevel checks for <code class="math">q=2^k</code> require <code class="math">\Omega(n\log q/\varepsilon^2)</code> when <code class="math">\varepsilon\le1/4</code> and <code class="math">n\ge2\left\lceil(2\varepsilon)^{-2}\right\rceil</code>.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Proofs](proof.md), [manuscript and reference map](sources.md), [operator and algebra review](verify/README.md), [finite evidence](verify/README.md).

Prime-dimensional and general-dimensional compact bounds are both retained because their parameter dependences differ. The positive identity shifts are part of the supplied Hamiltonian, and the witness factors apply to that objective.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
