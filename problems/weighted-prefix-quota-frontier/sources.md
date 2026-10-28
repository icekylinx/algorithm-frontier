# Sources and proof dependencies

## Canonical manuscripts

- [Exact prefix, laminar and sparse quotas](proof.md)
- [Native one-order prefix profiles and exact signed recovery](reference-prefix-realization.md)
- [Native two-order and variable-family prefix recovery](reference-orders-families-realization.md)
- [Exact sparse numeric quotas with a root cap and arbitrary completion costs](manuscripts/bounded-frequency-root-cap-valuated-fpt.md)
- [Deterministic sunflower kernels for several coverable matroids](manuscripts/deterministic-coverable-matroid-sunflower-kernel.md)
- [Deterministic sparse packing kernels with an oracle matroid](manuscripts/deterministic-sparse-packing-oracle-kernel.md)
- [Sharp sparse-packing restrictions with deterministic FPT preprocessing](manuscripts/sharp-sparse-packing-fpt-restrictions.md)
- [Deterministic kernels with explicitly represented transversal matroids](manuscripts/deterministic-transversal-matroid-kernel-transfer.md)
- [Sharp root-target lower bounds with disjoint weighted quota rows](manuscripts/disjoint-row-root-target-sharp-lower.md)
- [Exact weighted prefix quotas parameterized by the largest target](manuscripts/exact-weighted-prefix-quotas-max-target.md)
- [Exact prefix quotas with a bounded number of weight families](manuscripts/few-weight-families-prefix-target-scheme.md)
- [Joint lower bounds for prefix targets and weight-family count](manuscripts/few-weight-prefix-joint-lower-bounds.md)
- [New primary-source comparisons for checkpoint T](manuscripts/incremental-primary-baselines-T.md)
- [Primary baselines and method credits for increment U](manuscripts/incremental-primary-baselines-U.md)
- [Exact common-weight laminar quotas under a root cap](manuscripts/laminar-common-weight-root-cap-fpt.md)
- [Exact laminar quotas with arbitrary zero-weight completion costs](manuscripts/laminar-valuated-zero-completion-fpt.md)
- [Faster exact recovery for laminar quotas by fixing the uncommon weights](manuscripts/laminar-dominant-weight-recovery.md)
- [Two positive weights already force exponential laminar oracle complexity](manuscripts/two-positive-weight-laminar-boundary.md)
- [Exact quotas on compatible cuts](manuscripts/compatible-cut-quota-extension.md)
- [Row-dependent weights defeat the largest-prefix-target parameter](manuscripts/row-dependent-full-prefix-target-boundary.md)
- [A direct hash-and-profile algorithm for sparse exact root-bounded quotas](manuscripts/sparse-root-quota-hash-profile-algorithm.md)
- [Two weighted coordinate orders: a sharp largest-target classification](manuscripts/two-order-weighted-prefix-target-classification.md)
- [Uniform scalar coefficients on optional zero-weight coordinates](manuscripts/uniform-zero-scalar-laminar-extension.md)
- [Labeled sunflower kernels for sparse numeric quotas and valuated completion](manuscripts/valuated-sparse-quota-sunflower-kernel.md)
- [Sharp support-budget tradeoffs for one and two weighted-prefix orders](manuscripts/weighted-prefix-support-budget-tradeoffs.md)

## Linked mathematical dependencies

These manuscripts contain the interfaces, auxiliary arguments or source
comparisons referenced by this result. Their stated hypotheses remain
part of each use; an interface analysis does not supply an omitted backend.

- [A sharp column-support dichotomy for exact numeric targets](../numeric-target-frontier/manuscripts/column-support-numeric-target-dichotomy.md)
- [A total-target ETH lower bound for explicitly encoded rank matroids](../numeric-target-frontier/manuscripts/conditional-lower-bound-encoded-target-matroids.md)
- [An encoded ETH tradeoff across row-overlap densities](../numeric-target-frontier/manuscripts/encoded-overlap-density-eth-lower-bound.md)
- [Covering-row chain compression for exact mixed numeric targets](../numeric-target-frontier/manuscripts/mixed-target-cover-chain-compression.md)
- [Sharp arbitrary-matroid failure summaries](../matroid-failure-summaries/proof.md): exact binomial rank summaries, deterministic deletion-witness search, and the one-label fixed-cost-prefix endpoint used by the sharp packing transfer.
- [Deterministic weighted oracle prefix construction](../matroid-failure-summaries/manuscripts/weighted-oracle-prefix-fpt-construction.md): the Bernoulli and original-basis support bounds, with the faster deterministic ordered basis tree and a one-pass retained-prefix alternative; supplies the arbitrary-profit <code class="math">O_\delta(k^{\delta+1})</code> packing restriction.
- [Sources, attribution and canonical paths](../../provenance/README.md)

## Primary references

The manuscripts identify the theorem and version used at each import.
Direct external references appearing in this reading path are:

- Grötschel, Lovász and Schrijver (1981), [*The ellipsoid method and its consequences in combinatorial optimization*](https://ir.cwi.nl/pub/10046/10046D.pdf), Sections 3–5; page 183 explicitly includes polymatroid intersection. This supplies exact weighted optimization with polynomial binary rank access.
- Schrijver (2000), [*A combinatorial algorithm minimizing submodular functions in strongly polynomial time*](https://homepages.cwi.nl/~lex/files/minsubm6.pdf). This supplies paid value-oracle minimization for the compressed resource rank and separation.

- <https://arxiv.org/abs/2304.13984>
- <https://arxiv.org/html/1806.11527v4>
- <https://arxiv.org/html/2307.07773v2>
- <https://arxiv.org/html/2412.02217v2>
- <https://arxiv.org/html/2603.17345v1>
- <https://courses.cs.washington.edu/courses/cse599i/24sp/papers/ImpagliazzoPaturiZane_2001_jcss.pdf>
- <https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2017.55>
- <https://drops.dagstuhl.de/storage/00lipics/lipics-vol294-swat2024/LIPIcs.SWAT.2024.22/LIPIcs.SWAT.2024.22.pdf>
- <https://theoretics.episciences.org/14792/pdf>
- <https://www.cs.tau.ac.il/~nogaa/PDFS/aghp4.pdf>
- <https://www.di.ens.fr/~cchuang/work/matchoid.pdf>
- Naor, Schulman and Srinivasan, [*Splitters and near-optimal derandomization*](https://www.wisdom.weizmann.ac.il/~naor/PAPERS/splitters.pdf), Theorem 7 and the local-evaluation definition in Section 1.3. This indexed construction supplies the stronger laminar coefficient <code class="math">5/9+o(1)</code> with polynomial space. The elementary coloring proof gives coefficient <code class="math">10/9</code> without this import.

## Evidence and provenance

The [one-order reference](reference/README.md) implements actual original-input
mixed prefix optimization with mandatory original totals or optional disposal.
Its [independent checker](verify/check_prefix.py) compares 956 signed min/max
solves on 478 mode/eligibility instances, 718 original feasible vectors and
1,436 marked-profile recoveries. It charges 1,330 streamed profiles, including
814 failed row filters and 76 empty faces, and exercises six binary-large
fixtures, 11 malformed inputs and two forged outputs. The full one-order
companion is audited separately from the two-order, bounded-family and broader
ground-reduction chains. Native Bland pivot time remains separate from its
paid polynomial intersection theorem; counts, target parameters and signed
zero-coordinate costs retain their original binary scope.

The [two-order and family client](reference/orders_families.py) reuses that
original-subset recovery and implements actual simultaneous marks, streamed
covering-family chains and occupied vector profiles. The
[bounded realization](reference-orders-families-realization.md) audits the
full two-order and family companions, actual-support refinements and joint
target/family lower calibration. Its
[independent checker](verify/check_orders_families.py) compares original signed
optima and canonical marks, including tied stops, arbitrary zero family entries,
mandatory totals and binary-large data. Broader sparse-hash, kernel and
laminar-coloring scope remains separate.

The [verification note](verify/README.md) states the scope of executable
evidence and the remaining mathematical dependencies. The
[import record](../../provenance/README.md) preserves source revisions,
canonical paths, attribution and applicable licenses.

**Attribution:** icekylinx · GPT-6 Astra Pro.
