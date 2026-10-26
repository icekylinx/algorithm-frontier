# Exact correlated-failure cuts and whole-block quotients

A polynomial label decoder turns every permitted failure and query into an ordinary quotient query. One nonnegative coefficient per original item then works simultaneously for all queries, including those chosen after the summary is revealed.

## Results

Write

```math
S(D,\varepsilon)=O\!\left(\min\left\{m,\frac{D\log(2D/\varepsilon)}{\varepsilon^2}\right\}\right).
```

All constructions below are Monte Carlo randomized polynomial time in the explicit compact matrix/graph input and inverse accuracy. One event of probability at least $`2/3`$ covers every allowed failure and the entire query family, including queries selected after the output. The exact polynomial decoder and field-extension steps are deterministic; a failed sampling event can silently violate an approximation guarantee.

**Ordinary normalized monotone submodular quotients of rank $`r`$, positive marginals at least one**

**Lifted rank parameter $`D`$.** $`r`$

**Retained support and output.** $`S(r,\varepsilon)`$ original items; $`O(\log\log(2m))`$ backend calls

**Proof.** [Adaptive resparsification theorem](manuscripts/adaptive-quotient-resparsification.md)

**Represented columns or whole represented subspaces with incidence label deficit at most $`k`$**

**Lifted rank parameter $`D`$.** $`r\binom{h+k}{k}`$

**Retained support and output.** $`S(D,\varepsilon)`$ original columns or whole blocks, preserving all subspace-complement queries

**Proof.** [Column theorem](manuscripts/exact-label-cut-and-matroid-quotient-sparsification.md), [Theorem B1](manuscripts/exact-label-whole-blocks-and-hyperedges.md)

**Undirected graph: at most $`a`$ labels per vertex and $`b`$ additional labels per edge**

**Lifted rank parameter $`D`$.** $`(n-c)\binom{h+a+b}{a+b}`$

**Retained support and output.** $`S(D,\varepsilon)`$ edges, preserving every cut after every allowed failure

**Proof.** [Equation EC1](manuscripts/exact-label-cut-and-matroid-quotient-sparsification.md)

**One vertex color per graph vertex, no additional edge labels**

**Lifted rank parameter $`D`$.** $`(n-c)(h+1)`$

**Retained support and output.** $`S(D,\varepsilon)`$ edges with one fixed coefficient each

**Proof.** [Equation EC2](manuscripts/exact-label-cut-and-matroid-quotient-sparsification.md)

**Hyperedges of size at most $`t`$, with at most $`a`$ vertex labels and $`b`$ additional item labels**

**Lifted rank parameter $`D`$.** $`(n-c)\binom{h+a(t-1)+b}{a(t-1)+b}`$

**Retained support and output.** $`S(D,\varepsilon)`$ whole hyperedges; cuts and partition-crossing objectives

**Proof.** [Equation B6](manuscripts/exact-label-whole-blocks-and-hyperedges.md)

**Whole hedges, with at most $`d`$ labels per hedge**

**Lifted rank parameter $`D`$.** At most $`(n-c)\binom{h+d}{d}`$

**Retained support and output.** $`S(D,\varepsilon)`$ whole hedges; no factor for the number of constituent edges

**Proof.** [Equation B9](manuscripts/exact-label-whole-blocks-and-hyperedges.md)

**Globally commuting prime-dimensional stabilizer blocks, at most $`d`$ labels per block**

**Lifted rank parameter $`D`$.** $`(n+1)\binom{h+d}{d}`$

**Retained support and output.** $`S(D,\varepsilon)`$ whole blocks; simultaneous all-state energy and kernel preservation

**Proof.** [Equations B10–B11](manuscripts/exact-label-whole-blocks-and-hyperedges.md)

## Contract

**Objective and output**

One original-item reweighting preserving every stated cut, partition, represented quotient, or commuting-block energy after all sets of at most $`h`$ failed labels.

**Randomness**

Monte Carlo randomized preprocessing, with success probability at least $`2/3`$ for one event covering every allowed failure and quotient/cut query. Queries and failed labels may be chosen after the summary is revealed. The exact label decoder and field-extension arithmetic are deterministic.

**Time**

Polynomial in explicit compact input length and $`\varepsilon^{-1}`$; the construction returns the whole input before materializing a lift whose dimension exceeds the item count. No failure set is enumerated.

**Space**

Lifted rank bounds and retained support are separate from workspace. Only the polynomial-sized capped lift is materialized; no independent optimized space bound is claimed.

**Parameters**

$`m`$ counts original items, $`r`$ is original concatenated-column rank, $`c`$ counts positive-input components including isolated vertices, $`h`$ is the failure budget, and $`k`$ bounds item labels absent from an incident row.

**Model and representation**

Explicit rational or finite-field matrices and rational item weights. A failed vertex deletes every incident hyperedge as a whole. A partition charges a crossing hyperedge once. Stabilizer failure results require global commutation.

**Lower-bound scope**

Simple unweighted graph and hypergraph families require $`\Omega\!\left(\frac{n\binom{h+k}{k}}{\varepsilon^2}\right)`$ original items in the stated large-$`n`$ regimes. Repeated labeled commuting-check families require $`\Omega\!\left(\frac{n\binom{h+d}{d}}{\varepsilon^2}\right)`$ when $`n\ge2\left\lceil\varepsilon^{-2}\right\rceil`$. These are support lower bounds allowing arbitrary nonnegative output weights.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Proofs](proof.md), [manuscript and reference map](sources.md), [decoder review](verify/README.md), [finite evidence](verify/README.md).

The graph theorem concerns cuts; [spectral and seminorm summaries](../correlated-spectral-regression/) have separate guarantees and parameter bounds.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
