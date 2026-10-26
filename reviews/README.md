# Verification evidence

Every result family has one evidence note linked below. The machine-readable
[registry](registry.json) records the exact executable coverage for each family.
A manuscript proof, a finite computation and a proof-assistant derivation are
different forms of evidence. No proof-assistant verification or external peer
review is claimed.

## Run the checks

```sh
python3 tools/check_repository.py
```

The default command checks all canonical paths, source mappings, result-card
fields, mathematical delimiters and generated indexes. It then runs the
exact mathematical checks, validates the full-contact receipt's source/menu
binding, and freshly recomputes the rho=1.7 and direct contact branches.
It uses the Python standard library and modifies no files.

To recompute all 44 continuous contact branches:

```sh
python3 tools/check_repository.py --full-contacts --jobs 4
```

The full replay is substantially more expensive than the default run.
Receipt binding validates provenance and coverage metadata; only recomputation
establishes the inequalities again. The acceptance kernel's coverage argument
is in the [Subset Sum evidence note](../problems/subset-sum-fast-deterministic/verify/README.md).
The same full mode is available through the repository-check workflow's
manual dispatch. Pushes and pull requests use the default suite.

## Executable evidence

| Program | Checked mathematical component |
|---|---|
| [Continuous contacts](../tools/verify_subset_sum_contacts.py) | Exact interval coverage and acceptance for all 44 refined Subset Sum branches |
| [Scalar composition](../tools/verify_subset_sum_scalars.py) | Entropy enclosures, reflected contact profile and outer exponent ledger |
| [Energy tensors](../problems/subset-sum-fast-deterministic/verify/check_energy.py) | 132 finite cases and 1,056 independently enumerated outputs |
| [Space resources](../problems/subset-sum-low-space-deterministic/verify/check_resources.py) | Exact rational low-space resource envelope |
| [Structural identities](../problems/subset-sum-low-space-deterministic/verify/check_structural.py) | Finite ownership, covers, completions and layouts |
| [Range identities](../problems/subset-sum-low-space-deterministic/verify/check_range_identities.py) | Residues, batches and exact packed convolution |
| [Profiles and quotas](../tools/verify_profile_certificates.py) | 11,107 quota cases, 91 bucket identities and 915 load multisets |
| [Two-scenario reduction](../tools/verify_finite_reductions.py) | 26,568,384 exact target comparisons on the declared small integer domain |
| [Sensitivity mechanisms](../tools/verify_sensitivity_certificates.py) | Signed interval catalogue and exact exchange repairs on partition-matroid instances |
| [Quotient rounding](../problems/group-metric-constraints/verify/check_quotient_rounding.py) | 64 subsets and 4,096 ordered pairs over six blocks in the stated finite group |
| [Non-Fano obstruction](../tools/verify_non_fano.py) | 13 supports and all 128 sign vectors of the explicit counterexample |

These checks certify their stated identities or domains. They do not implement
every algorithm in the catalogue, discharge unnamed oracle contracts, or turn
support-size theorems into construction-time bounds.

## Evidence by result

### Subset Sum

| Result and evidence note | Executable coverage |
|---|---|
| [Faster deterministic Subset Sum](../problems/subset-sum-fast-deterministic/verify/README.md) | [verify_subset_sum_contacts](../tools/verify_subset_sum_contacts.py), [verify_subset_sum_scalars](../tools/verify_subset_sum_scalars.py), [check_energy](../problems/subset-sum-fast-deterministic/verify/check_energy.py) |
| [Low-space deterministic Subset Sum](../problems/subset-sum-low-space-deterministic/verify/README.md) | [check_resources](../problems/subset-sum-low-space-deterministic/verify/check_resources.py), [check_structural](../problems/subset-sum-low-space-deterministic/verify/check_structural.py), [check_range_identities](../problems/subset-sum-low-space-deterministic/verify/check_range_identities.py) |

### Numeric targets and quota geometry

| Result and evidence note | Executable coverage |
|---|---|
| [Numeric targets and support patterns](../problems/numeric-target-frontier/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Prefix, laminar and sparse quotas](../problems/weighted-prefix-quota-frontier/verify/README.md) | Manuscript arguments; no dedicated executable certificate |

### Graph algorithms

| Result and evidence note | Executable coverage |
|---|---|
| [Maximum-cardinality matching](../problems/general-matching/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Degree-constrained subgraphs](../problems/degree-constrained-subgraphs/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Static and threshold min-cost flow](../problems/min-cost-flow/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Incremental strongly connected components](../problems/incremental-scc/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Incremental directed SSSP](../problems/incremental-sssp/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Fully dynamic APSP](../problems/apsp-frontier/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Dynamic spanners](../problems/dynamic-spanners/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Dynamic minimum spanning forest](../problems/dynamic-msf/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Strong forests and Gomory–Hu trees](../problems/decremental-strong-forest/verify/README.md) | Manuscript arguments; no dedicated executable certificate |

### Exact failures, persistence and compilation

| Result and evidence note | Executable coverage |
|---|---|
| [Single-failure optimum preservers](../problems/exact-failure-preservers/verify/README.md) | [verify_sensitivity_certificates](../tools/verify_sensitivity_certificates.py) |
| [Flow, matching and price sensitivity](../problems/exact-flow-sensitivity/verify/README.md) | [verify_sensitivity_certificates](../tools/verify_sensitivity_certificates.py) |
| [Matroid and submodular failure summaries](../problems/matroid-failure-summaries/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Colored and vertex-failure graph certificates](../problems/graph-color-failure-certificates/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Resource-constrained packing summaries](../problems/packing-matching-summaries/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Persistent-homology failure certificates](../problems/persistence-failure-certificates/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Boolean linear optimization compiler](../problems/boolean-linear-compiler/verify/README.md) | [verify_sensitivity_certificates](../tools/verify_sensitivity_certificates.py) |

### Spectral, group and quantum sparsification

| Result and evidence note | Executable coverage |
|---|---|
| [Correlated spectral, regression and seminorm summaries](../problems/correlated-spectral-regression/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Label and whole-block cut sparsification](../problems/label-block-cut/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Finite groups, affine constraints and metrics](../problems/group-metric-constraints/verify/README.md) | [check_quotient_rounding](../problems/group-metric-constraints/verify/check_quotient_rounding.py) |
| [Pauli, qudit and stabilizer blocks](../problems/quantum-stabilizer/verify/README.md) | [check_quotient_rounding](../problems/group-metric-constraints/verify/check_quotient_rounding.py) |
| [Exact-separation and non-Fano boundaries](../problems/obstruction-boundaries/verify/README.md) | [verify_non_fano](../tools/verify_non_fano.py) |

### Allocation and resource matroids

| Result and evidence note | Executable coverage |
|---|---|
| [Arbitrary-value allocation scheme](../problems/arbitrary-value-allocation-scheme/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Recipient polymatroids](../problems/recipient-polymatroid/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Recipient-matroid configuration](../problems/recipient-matroid-configuration/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Explicit-item matroid union](../problems/item-matroid-union/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [One-value allocation](../problems/one-value-exact-two/verify/README.md) | [verify_profile_certificates](../tools/verify_profile_certificates.py) |
| [Intrinsic two-value allocation](../problems/two-value-exact-two/verify/README.md) | [verify_profile_certificates](../tools/verify_profile_certificates.py) |
| [Intrinsic values near factor two](../problems/intrinsic-values-near-two/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Unrelated-value additive allocation](../problems/unrelated-values-additive/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Unrelated values with a joint role](../problems/unrelated-values-joint-role/verify/README.md) | [verify_profile_certificates](../tools/verify_profile_certificates.py) |
| [Whole-ground selection and transfers](../problems/whole-ground-allocation/verify/README.md) | [verify_profile_certificates](../tools/verify_profile_certificates.py) |

### Selected flow and robust allocation

| Result and evidence note | Executable coverage |
|---|---|
| [Selected concurrent flow](../problems/selected-flow/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Flow with shared setup budget](../problems/shared-setup-flow/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Robust selected flow](../problems/robust-scenario-flow/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Robust unrelated allocation](../problems/robust-unrelated-allocation/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Robust bounded-width certificates](../problems/robust-bounded-certificates/verify/README.md) | [verify_profile_certificates](../tools/verify_profile_certificates.py) |
| [Width-two robust unit allocation](../problems/robust-width-two-allocation/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Two-scenario hardness](../problems/robust-two-scenario-hardness/verify/README.md) | [verify_finite_reductions](../tools/verify_finite_reductions.py) |

### Scheduling

| Result and evidence note | Executable coverage |
|---|---|
| [Arbitrary-processing scheme](../problems/arbitrary-processing-scheduling/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Activated-machine scheduling](../problems/activated-machine-scheduling/verify/README.md) | [verify_profile_certificates](../tools/verify_profile_certificates.py) |
| [Six-profile scheduling](../problems/six-profile-three-halves/verify/README.md) | [verify_profile_certificates](../tools/verify_profile_certificates.py) |
| [Processing-bucket tradeoff](../problems/processing-bucket-tradeoff/verify/README.md) | [verify_profile_certificates](../tools/verify_profile_certificates.py) |
| [Two-size scheduling](../problems/two-size-scheduling/verify/README.md) | [verify_profile_certificates](../tools/verify_profile_certificates.py) |
| [Per-machine two-time scheduling](../problems/two-time-scheduling/verify/README.md) | [verify_profile_certificates](../tools/verify_profile_certificates.py) |
| [Many-size workload scheduling](../problems/many-size-scheduling/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Commitment scheduling](../problems/commitment-scheduling/verify/README.md) | Manuscript arguments; no dedicated executable certificate |

### Matching certificates and oracle barriers

| Result and evidence note | Executable coverage |
|---|---|
| [Hypergraph matching and expander routing](../problems/strong-haxell-matching/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Independent transversals](../problems/independent-transversal/verify/README.md) | Manuscript arguments; no dedicated executable certificate |
| [Allocation and scheduling barriers](../problems/allocation-lower-bounds/verify/README.md) | Manuscript arguments; no dedicated executable certificate |

## Maintaining evidence

When changing a theorem, update its evidence note and registry scope as well
as its statement and proof. Preserve the distinction between a shared finite
component and a check of the whole result. See [Contributing](../CONTRIBUTING.md)
and [import provenance](../provenance/README.md).
