# Algorithm Frontier

Algorithms and proofs in combinatorial optimization, dynamic graphs, and sparsification. Each problem page gives the theorem, complexity, randomness, dependencies, and verification evidence.

[![Repository checks](https://github.com/icekylinx/algorithm-frontier/actions/workflows/curation.yml/badge.svg)](https://github.com/icekylinx/algorithm-frontier/actions/workflows/curation.yml) [![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

**53 problem families · 18 supporting results** · [Proof index](CONTENTS.md) · [Review and verification](reviews/README.md) · [Citation](CITATION.cff)

## Selected results

Three deterministic constructions. The linked problem pages give the full statements, proof dependencies, executable coverage and review status.

### [Deterministic general-graph maximum matching](problems/general-matching/)

Deterministic exact maximum matching in general graphs.

<!-- math-display: 959b4822078bcdb0b44c8061
O(n+m)+(m_s+1)\exp(O((\log(m_s+2))^{4/5}(\log\log(m_s+4))^{1/5}))
-->
![Formula](assets/math/959b4822078bcdb0b44c8061.svg)

Here m_s counts distinct nonloop edge pairs. The proof supplies the uniform cycle-search construction and names its published prerequisites. A separate executable solver returns independently verifiable optimality certificates.

### [Faster deterministic Subset Sum](problems/subset-sum-fast-deterministic/)

Exact decision and indexed witness.

<!-- math-display: 45dc56e8c77bc161431d075b
C+\mathrm{poly}(n,L)2^{0.495748n}
-->
![Formula](assets/math/45dc56e8c77bc161431d075b.svg)

Exact rational exponent on the card.

For n integers of total bit length L, including an indexed witness. The finite startup constant C is input-independent. The complete compiler proof and exact continuous certificates support the improved third-lookup exponent.

### [Matroid and submodular failure summaries](problems/matroid-failure-summaries/)

Sharp represented and rank summaries; exact two-failure rank-four oracle maximum.

Represented prefixes and oracle rank: <code class="math">r\binom{h+d}{d}</code>.

Two failed labels and one label per item: sharp <code class="math">3r</code> through rank three, exactly 13 at rank four.

Rank is r, failed-label budget is h, and each item has at most d labels. Represented preprocessing is uniform polynomial; arbitrary-oracle prefix construction uses a deterministic canonical-basis tree. The 13-item nonrepresentable example is minimal in rank, label count and ground size for exceeding 3r under two failures.

## Results

Browse by problem. Each link opens its statement, proof and dependencies. [Computational models](docs/COMPLEXITY.md) and [randomness contracts](docs/RANDOMNESS.md) explain how to compare bounds.

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
