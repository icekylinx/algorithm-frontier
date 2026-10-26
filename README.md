# Algorithm Frontier

Algorithms and proofs in combinatorial optimization, dynamic graphs, and sparsification. Each problem page gives the theorem, complexity, randomness, dependencies, and verification evidence.

[![Repository checks](https://github.com/icekylinx/algorithm-frontier/actions/workflows/curation.yml/badge.svg)](https://github.com/icekylinx/algorithm-frontier/actions/workflows/curation.yml) [![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

**53 problem families · 18 supporting results** · [Proof index](CONTENTS.md) · [Review and verification](reviews/README.md) · [Citation](CITATION.cff)

## Selected results

Three entry points into the manuscripts. Full parameter ranges and the current review status are on the linked problem pages.

### [Deterministic general-graph maximum matching](problems/general-matching/)

Exact matching with original edge identifiers.

**Randomness.** Deterministic conditional composition, requiring deterministic external primitives and a deterministic implementation of Contract R.

**Quantitative result.**

```math
O(n+m)+(m_s+1)\exp(O((\log(m_s+2))^{4/5}(\log\log(m_s+4))^{1/5}))
```

Optional $`m_H=O(\nu(G)^2)`$ kernel.

**Model and scope.** Conditional on raw-backend Contract R and the named deterministic primitives; m_s counts distinct nonloop edges. The preprocessing kernel and its componentwise refinement are unconditional.

### [Faster deterministic Subset Sum](problems/subset-sum-fast-deterministic/)

Exact decision and indexed witness.

**Randomness.** Deterministic exact algorithm in the uniform bit model, including indexed-witness recovery and input-independent deterministic circuit construction; no probability of error.

**Quantitative result.**

```math
C+\mathrm{poly}(n,L)2^{0.495890734n}
```

Exact rational exponent on the card.

**Model and scope.** Exact rational certification of all 44 continuous contact branches; C is finite input-independent circuit precomputation; combinatorial compiler and bit-cost proofs are in the manuscript.

### [Matroid and submodular failure summaries](problems/matroid-failure-summaries/)

Sharp represented cost-prefix and oracle-rank summaries; weighted oracle endpoint and obstruction.

**Randomness.** Deterministic exact constructions. Random permutations and Bernoulli failures appear only in output-size proofs; no query sampling or probability of error.

**Quantitative result.**

Represented prefixes and oracle rank: $`r\binom{h+d}{d}`$.

Integral range $`R`$: $`R\binom{h+d}{d}`$.

Sharp one-failure weighted oracle size $`(d+1)r`$.

**Model and scope.** Uniform polynomial represented construction; explicit oracle FPT construction with linear input dependence for fixed parameters. General weighted oracle prefixes have the larger W–LF bound; a 13-item nonrepresentable example rules out the sharp binomial bound from two failures onward.

## Results

Browse by problem. Each link opens its statement and proof; conditional algorithms retain their named backend assumptions. [Computational models](docs/COMPLEXITY.md) and [randomness contracts](docs/RANDOMNESS.md) explain how to compare bounds.

### Subset Sum

- [Faster deterministic Subset Sum](problems/subset-sum-fast-deterministic/)
- [Low-space deterministic Subset Sum](problems/subset-sum-low-space-deterministic/)

### Numeric targets and quota geometry

- [Numeric targets and support patterns](problems/numeric-target-frontier/)
- [Prefix, laminar and sparse quotas](problems/weighted-prefix-quota-frontier/)

### Graph algorithms

- [Deterministic general-graph maximum matching](problems/general-matching/)
- [Degree-constrained subgraphs](problems/degree-constrained-subgraphs/)
- [Static and threshold min-cost flow](problems/min-cost-flow/)
- [Incremental strongly connected components](problems/incremental-scc/)
- [Incremental directed SSSP](problems/incremental-sssp/)
- [Fully dynamic APSP](problems/apsp-frontier/)
- [Dynamic spanners](problems/dynamic-spanners/)
- [Dynamic minimum spanning forest](problems/dynamic-msf/)
- [Strong forests and Gomory–Hu trees](problems/decremental-strong-forest/)

### Exact failures, persistence and compilation

- [Single-failure optimum preservers](problems/exact-failure-preservers/)
- [Flow, matching and price sensitivity](problems/exact-flow-sensitivity/)
- [Matroid and submodular failure summaries](problems/matroid-failure-summaries/)
- [Colored and vertex-failure graph certificates](problems/graph-color-failure-certificates/)
- [Resource-constrained packing summaries](problems/packing-matching-summaries/)
- [Persistent-homology failure certificates](problems/persistence-failure-certificates/)
- [Boolean linear optimization compiler](problems/boolean-linear-compiler/)

### Spectral, group and quantum sparsification

- [Correlated spectral, regression and seminorm summaries](problems/correlated-spectral-regression/)
- [Label and whole-block cut sparsification](problems/label-block-cut/)
- [Finite groups, affine constraints and metrics](problems/group-metric-constraints/)
- [Pauli, qudit and stabilizer blocks](problems/quantum-stabilizer/)
- [Exact-separation and non-Fano boundaries](problems/obstruction-boundaries/)

### Allocation and resource matroids

- [Arbitrary-value allocation scheme](problems/arbitrary-value-allocation-scheme/)
- [Recipient polymatroids](problems/recipient-polymatroid/)
- [Recipient-matroid configuration](problems/recipient-matroid-configuration/)
- [Explicit-item matroid union](problems/item-matroid-union/)
- [One-value allocation](problems/one-value-exact-two/)
- [Intrinsic two-value allocation](problems/two-value-exact-two/)
- [Intrinsic values near factor two](problems/intrinsic-values-near-two/)
- [Unrelated-value additive allocation](problems/unrelated-values-additive/)
- [Unrelated values with a joint role](problems/unrelated-values-joint-role/)
- [Whole-ground selection and transfers](problems/whole-ground-allocation/)

### Selected flow and robust allocation

- [Selected concurrent flow](problems/selected-flow/)
- [Flow with shared setup budget](problems/shared-setup-flow/)
- [Robust selected flow](problems/robust-scenario-flow/)
- [Robust unrelated allocation](problems/robust-unrelated-allocation/)
- [Robust bounded-width certificates](problems/robust-bounded-certificates/)
- [Width-two robust unit allocation](problems/robust-width-two-allocation/)
- [Two-scenario hardness](problems/robust-two-scenario-hardness/)

### Scheduling

- [Arbitrary-processing scheme](problems/arbitrary-processing-scheduling/)
- [Activated-machine scheduling](problems/activated-machine-scheduling/)
- [Six-profile scheduling](problems/six-profile-three-halves/)
- [Processing-bucket tradeoff](problems/processing-bucket-tradeoff/)
- [Two-size scheduling](problems/two-size-scheduling/)
- [Per-machine two-time scheduling](problems/two-time-scheduling/)
- [Many-size workload scheduling](problems/many-size-scheduling/)
- [Commitment scheduling](problems/commitment-scheduling/)

### Matching certificates and oracle barriers

- [Hypergraph matching and expander routing](problems/strong-haxell-matching/)
- [Independent transversals](problems/independent-transversal/)
- [Allocation and scheduling barriers](problems/allocation-lower-bounds/)

### Supporting results

The [complete index](CONTENTS.md#supporting-results) also lists 18 supporting algorithms, structural theorems, and scoped lower bounds. [Shared manuscripts](CONTENTS.md#shared-manuscripts) collect reusable proofs and backend interfaces.

## Reading and verification

Within each problem: `README.md` → `proof.md` → `sources.md` → `verify/README.md`. The [review registry](reviews/README.md) distinguishes manuscript review from executable checks and identifies their exact scope.

```sh
python3 tools/check_repository.py
```

See [Contributing](CONTRIBUTING.md) for the full verification mode and maintenance conventions. No external peer review or proof-assistant verification is claimed.

Yilin Liu and GPT-6 Astra Pro. *Algorithm Frontier* (2026). Cite the relevant problem path and commit; the [citation protocol](PROTOCOL.md) and [import provenance](provenance/README.md) retain the applicable licenses and notices.
