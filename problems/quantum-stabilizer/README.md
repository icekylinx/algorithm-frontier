# Positive Pauli Hamiltonians and whole stabilizer blocks

The output retains whole original positive clauses or blocks and approximates every quantum state's energy in Loewner order. The ordinary sparse-support theorems and the stabilizer-witness approximation address different outputs.

## Results

All support bounds are capped by the original number of items $`m`$. Let $`\rho=\log_2(2D)`$, where $`D`$ is the total Hilbert-space dimension.

**Arbitrary-locality positive Pauli Hamiltonian on $`n`$ qubits**

**Guarantee or retained support.** Existence $`O((n+1)/\varepsilon^2)`$; compact $`O\!\left(\frac{(n+1)\log((n+2)/\varepsilon)}{\varepsilon^2}\right)`$; optional exact total coefficient

**Construction.** Sharp support is existential, with a Monte Carlo construction polynomial in $`2^n`$, success at least $`2/3`$; compact construction is Monte Carlo polynomial in binary input and $`\varepsilon^{-1}`$, success at least $`2/3`$

**Proof.** [Theorem 1](manuscripts/arbitrary-locality-pauli-sparsification.md)

**Whole blocks of commuting checks on prime-dimensional $`p`$-level qudits, with arbitrary noncommutation between blocks**

**Guarantee or retained support.** Existence $`O\!\left(\frac{(n+1)\log p}{\varepsilon^2}\right)`$; compact $`O\!\left(\frac{(n+1)[\log p+\log((n+2)/\varepsilon)]}{\varepsilon^2}\right)`$

**Construction.** Compact Monte Carlo polynomial time, success at least $`2/3`$; sharp support has a Monte Carlo explicit-character-table construction, success at least $`2/3`$; individual checks are included

**Proof.** [Theorem SB](manuscripts/arbitrary-locality-stabilizer-block-sparsification.md), [single-check corollary](manuscripts/arbitrary-locality-prime-qudit-checks.md)

**Whole stabilizer blocks in arbitrary heterogeneous local dimensions $`q_1,\ldots,q_n`$**

**Guarantee or retained support.** Existence $`O(\rho/\varepsilon^2)`$; compact $`O\!\left(\frac{\rho\log(2\rho/\varepsilon)}{\varepsilon^2}\right)`$

**Construction.** Compact Monte Carlo polynomial bit time without factoring, success at least $`2/3`$; sharp support has a Monte Carlo construction polynomial in $`D`$, success at least $`2/3`$; individual Weyl checks are included

**Proof.** [Theorems 1–2](manuscripts/arbitrary-dimension-whole-stabilizer-blocks.md), [single-check corollary](manuscripts/arbitrary-dimension-weyl-checks.md)

**Positive Pauli ground-energy surrogate and stabilizer witness**

**Guarantee or retained support.** Factor $`2+\sqrt2`$ relative to the actual ground energy; identical original/surrogate energy on every state of the constructed basis

**Construction.** Deterministic polynomial-time reduction; exact minimization by $`2^d\mathrm{poly}(L)`$ enumeration and polynomial space, $`d\le n`$

**Proof.** [Theorem 1](manuscripts/commuting-surrogates-and-stabilizer-energy-witnesses.md)

**Prime-dimensional individual-check ground-energy surrogate**

**Guarantee or retained support.** Factor $`2(1+p^{-1/2})`$ and a compact stabilizer witness

**Construction.** Deterministic compact polynomial-time reduction; $`p^n\mathrm{poly}(L)`$ enumeration and polynomial space

**Proof.** [Corollary 2](manuscripts/commuting-surrogates-and-stabilizer-energy-witnesses.md)

**Positive Pauli clauses after all $`h`$ correlated label deletions, at most $`a`$ labels per clause**

**Guarantee or retained support.** Explicit-dimension support $`O\!\left(\frac{\Gamma(h,a)(n+1)[n+\log(2Q/\delta)]}{\varepsilon^2}\right)`$; compact support bound has an additional factor $`\log(2m)`$

**Construction.** Monte Carlo preprocessing; one common event of probability at least $`1-\delta`$ covers all failures and all states with fixed coefficients

**Proof.** [Section 7](manuscripts/arbitrary-locality-pauli-sparsification.md)

**Globally commuting prime-dimensional whole blocks after all label failures**

**Guarantee or retained support.** $`O\!\left(\frac{R\log(2R/\varepsilon)}{\varepsilon^2}\right)`$, $`R=(n+1)\binom{h+a}{a}`$

**Construction.** Compact Monte Carlo polynomial time, success at least $`2/3`$ on one all-query/all-failure event; all checks must commute across all blocks

**Proof.** [Block-failure theorem](../label-block-cut/manuscripts/exact-label-whole-blocks-and-hyperedges.md)

For correlated failures, $`Q=\sum_{j=0}^h\binom{L}{j}`$ and $`\Gamma(h,a)=\frac{(h+a)^{h+a}}{h^h a^a}`$, with value one if either parameter is zero; $`L`$ is the number of occurring labels. These failures delete specified clauses or blocks.

## Contract

**Objective and output**

All-state relative energy approximation of positive Pauli or Weyl acceptance-projector penalties, with whole-item output; alternatively, the stated classical stabilizer-witness approximation.

**Randomness**

Mixed. Compact and explicit-dimension whole-block sparsification are Monte Carlo with success at least $`2/3`$; correlated Pauli preprocessing succeeds with probability at least $`1-\delta`$ simultaneously for all allowed failures. Sharp support is existential in the compact-input model. Stabilizer-basis surrogate construction and the stated exponential exact witness enumeration are deterministic. All sampling is classical preprocessing randomness.

**Time**

Compact sparsifier constructions are Monte Carlo polynomial in their full binary input length and inverse accuracy, with the stated success probability. Optimal-support constructions may be exponential in compact dimension. The randomness is classical preprocessing sampling, with no quantum sampling oracle. Surrogate construction and its stated exponential exact objective enumeration are deterministic.

**Space**

Support counts retained input objects. The witness-enumeration algorithms use polynomial workspace and output a polynomial-size tableau. No independent workspace bound is inferred for other constructions.

**Parameters**

$`n`$ is qudit count; $`p`$ is prime local dimension; $`q_j`$ are arbitrary local dimensions; $`D=\prod_{j=1}^n q_j`$; $`m`$ counts original whole blocks; $`\varepsilon`$ is relative error.

**Model and representation**

Each block's checks commute internally. Ordinary block theorems permit arbitrary cross-block noncommutation and locality. Constant penalties and inconsistent internal targets are allowed. All phases and displacement labels have compact modular descriptions.

**Lower-bound scope**

Classical cut instances require $`\Omega(n/\varepsilon^2)`$ terms in the stated prime-dimensional regime. Multilevel checks for $`q=2^k`$ require $`\Omega(n\log q/\varepsilon^2)`$ when $`\varepsilon\le1/4`$ and $`n\ge2\left\lceil(2\varepsilon)^{-2}\right\rceil`$.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Proofs](proof.md), [manuscript and reference map](sources.md), [operator and algebra review](verify/README.md), [finite evidence](verify/README.md).

Prime-dimensional and general-dimensional compact bounds are both retained because their parameter dependences differ. The positive identity shifts are part of the supplied Hamiltonian, and the witness factors apply to that objective.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
