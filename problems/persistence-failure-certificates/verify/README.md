# Verification and scope

[Main proof](../proof.md) · [Source dependencies](../sources.md)

## Evidence status

The exact incidence and persistence statements are established by symbolic identities and chain-complex arguments in the linked proof. No dedicated executable currently verifies all label failures and filtration states. Finite Betti-number comparisons would not establish the naturality required by the persistence-module statement.

## Incidence decoding

Independent original rows are selected before the lift, preserving their row-label meanings. Factoring the label polynomial for a column into its row-label and incidence-deficit factors makes the surviving column's scalar independent of the incident row. Projection onto the selected original rows is injective on the full column span and on every later column restriction.

For a top simplex and one of its facets, the label deficit is at most $`a+b`$. In the one-color specialization, the exterior kernel has dimension $`\binom{n-k}{p+1}`$; stacking the rescaled boundary blocks gives the other bound $`kr`$. Both bound the same lifted rank. The color-count convention assigns safe vertices a permanent, never-failing color.

## Homology and filtration scope

At every allowed state, the lower chain coordinates and lower boundary maps agree literally, and the surviving top-boundary image spaces agree. The induced homology identifications therefore commute with the filtration and inclusion maps. This gives persistence-module isomorphisms, rather than only equality of Betti numbers.

The full original lower skeleton is retained. The theorem depends on the chosen coefficient field and covers degrees at most $`p-1`$. A supplied filtration order and an independent cost order require separate constructions unless they coincide. The [separate spectral incidence theorem](../../correlated-spectral-regression/manuscripts/graded-incidence-and-simplicial-spectral-sparsification.md) does not add a spectral guarantee at every filtration threshold.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
