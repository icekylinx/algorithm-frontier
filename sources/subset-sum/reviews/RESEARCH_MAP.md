# Research map and dependency boundaries

The current research continuation is [the structural Part II theorem](../research/part-II/structural/THEOREM.md), with space exponent $E_S<0.1826163578$ and uniform time exponent 1/2; its exact rational value is in the proof. The combined manuscript now integrates this same bound. New proofs, measured branches and simplifications are indexed in [research/part-II/](../research/part-II/README.md).


The current [manuscript](../proof.md), **A deterministic Subset Sum bound**, combines two separate general-input deterministic algorithms. One proves time exponent less than $0.4964618056$ with a finite input-independent circuit startup cost. The other proves time exponent $1/2$ with space exponent $E_S=18261635770550353/10^{17}<0.1826163578$. Both use polynomial factors in the full binary input length and permit witness recovery. Their resource guarantees are not combined in one execution.

## Current faster-time chain

| Component | Role in the complete theorem |
|---|---|
| Exact signed matching circuits and affine rebalancing | Realize matching by integer factorizations and enumerate their actual incidences |
| Recursive containment and pooled trace coefficients | Aggregate coefficients before emitting shared remaining incidences |
| Full-domain profile certificate | Supplies a uniform bound, including tails and reflected ranges |
| Joint balancing over unequal cores | Uses support entropy deficit to pay the imbalance cost |
| Canonical-witness covers and implicit energy | Construct deterministic modular filters without enumerating unsupported pair tables |
| Exact keys and signed counting | Preserve integer equality and support witness recovery |
| Complete resource balance | Gives $E=149809813343531/301754962128739<0.4964618056$ |

The fixed circuit searches are finite and independent of the instance. Their termination proves uniformity; obtaining usable stored circuits and a useful startup bound remains an implementation problem. The exact coefficients, full-domain profile, and enumeration costs are all necessary. A local contact improvement does not by itself improve the general theorem.

## Current low-space chain

| Component | Role in the complete theorem |
|---|---|
| Exact full support counts and high-deficiency fallback | Exhaustively classify arbitrary full blocks |
| Canonical cube edges and nonlinear potential | Choose strict cores before useful layers with fixed-power certificates |
| Fixed-layer trace mass and dyadic support classes | Supply joint support/signing credit and pay the actual code size |
| Elementary restricted-color layout covers | Construct fine balanced cells with a complete factorial conditional-expectation proof |
| Exact-distance ownership and grouped XOR covers | Handle small least-deficiency inputs with the same quota in support and checking |
| Leaf-conserving radius and variable containers | Control both sided incidences while preserving the stored-leaf budget |
| Ordinary-top layer-preserving projection | Adapt useful layers with a fixed nominal base density and exact inherited scale |
| Atomic whole complements and oriented halves | Store genuine distinct supports and preserve witness semantics |
| Common prime paths and shared weighted covers | Cover the two fixed local images and global top image with paid preprocessing |
| Independent original-key signing unions | Keep one bounded dictionary per side and add their restart costs |
| Full mixed-density scalar certificates | Prove the ordinary and ownership regions and their handoff |

The ordinary top uses the canonical affine-biased separator. Its common degree bound preserves exact incidence cancellation after actual product balance. Local images and child roles are fixed before top fine-profile selection; only ancestor factors move between children. The original full-local ambient support bounds the entire local-signing union, while raw occurrences retain their labels. Atomic support arrays remain indivisible.

The exact capacity includes fixed granularity and finite-coordinate errors. Uniform bit time remains $\operatorname{poly}(n,L)2^{n/2}$.

## Verification and historical material

The current finite checks are in [rounds/20261023-joint/](../rounds/20261023-joint/) and [rounds/20261024-structural/](../rounds/20261024-structural/); run them with `make verify-current`. The complete proof remains in the manuscript. There is no complete executable solver or full Lean formalization of either theorem.

The earlier [rounds/20261023-r2/](../rounds/20261023-r2/) schedule, [rounds/20261023-r1/](../rounds/20261023-r1/) circuit evidence, [tools/verify_proof.py](../tools/verify_proof.py), and [formal/](../formal/) stored comparisons are historical. Their original data and receipts remain useful evidence for those earlier results. Their commands do not certify the newer joint manuscript.

The independent local density-$0.116$ circuit remains valid, although the newer complete scheme has a smaller general time exponent. Some older mechanisms persist in occurrence aggregation, deterministic residue selection, cached lists, and exact signed counting. No global domination result over all earlier time-space or preprocessing tradeoffs has been established.

## Separate research interfaces

[rounds/20261023-time-space/](../rounds/20261023-time-space/) concerns a randomized simultaneous time-space candidate. [rounds/20261023-deterministic-space/](../rounds/20261023-deterministic-space/) records the earlier deterministic-space investigation. The new low-space theorem uses its own complete construction; it does not automatically close every interface in either earlier investigation.

The retained phase and checksum work has distinct contracts. A small phase alphabet, entropy bound, or shortened random tape does not deterministically select a successful global tape. General phase selection and paid evaluation of its conditional objective remain separate questions.

Special-input structural solvers require their stated pairing or additive-block promises. Scoped circuit, rectangle, trace, and support-energy obstructions apply only to their specified models. They are not lower bounds for general Subset Sum. In particular, the sharp support-energy inequality refuted by the newer counterexample must not be used as a premise.

Growing-block coefficient extraction is an independent exactification lemma. It remains available for a suitable common-kernel factorization but is not needed by the present theorems. Further local contacts and deeper trace identities are archived research results rather than additional certified general exponents.

## Archives

Superseded originals and received checkpoint packages are moved into verified local archives. They are not left as duplicate active sources, and they remain recoverable. See [ARCHIVES.md](ARCHIVES.md). Archive history records provenance; the current theorem must be readable and checkable without private archive access.


## Latest Part I continuation

The [local frontier record](../research/part-I/FRONTIER.md) curates the 99-file batch-and-code checkpoint. The accepted exponent is unchanged. It records actual-key matrix contraction, memoized boundary batches, exact coded residuals, degree-weighted shift selection, scoped counterexamples, and the precise aggregate-cost obligations. Note 97 closes the colored total-wire compiler interface when exact seeds exist at arbitrarily large admissible sizes and endpoint transitivity holds. A smaller complete profile and its outer resource ledger remain the next mathematical obligations. The article presents the established algorithms and proofs; this continuation is kept in research records.

## Latest Part II continuation

The [Part II frontier](../research/part-II/FRONTIER.md) distinguishes established structural advances from scoped limits of trace gains, separate top-signing branches, local separator/light-bucket composition, and third-level conservation. The ordinary stored-leaf requirement currently determines the tightest capacity certificate. A smaller complete bound requires another full mixed-profile argument; individual favorable contacts remain local research evidence.

The new research has its own complete resource proof and `make verify-research` target. `make verify-all` runs both the manuscript and research checks. The ordinary and ownership size policies retain design anchor .548 while actual dictionary capacity and the full-block fallback are tightened together.
