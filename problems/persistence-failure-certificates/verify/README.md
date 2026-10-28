# Verification and scope

[Main proof](../proof.md) · [Source dependencies](../sources.md)

## Evidence status

The exact incidence and persistence statements are established by symbolic
identities and chain-complex arguments in the linked proof. The
[feature-rank checker](check_feature_construction.py) now verifies all
allowed failures and order prefixes in its finite domains, comparing full
boundary spans. The naturality required by the persistence-module statement
is proved separately; finite Betti-number comparisons alone would not
establish it.

## Actual-rank construction and exact finite evidence

The [reference algorithm](../reference/feature_summary.py) constructs an
evaluation module by a breadth-first frontier of independent product rows.
The checker compares it to direct monomial enumeration on small inputs,
including exact pivot columns, row ranks, degree bounds and candidate
counts. Represented-matroid and simplicial cases then compare every
surviving original prefix span against the retained one. Original boundary
rows are selected by streaming sparse-generated columns; no dense boundary
or complete lifted feature matrix is required by the implementation.

```sh
python3 problems/persistence-failure-certificates/verify/check_feature_construction.py
python3 problems/persistence-failure-certificates/verify/check_feature_construction.py --full
```

The completed larger run covers 2,288 module comparisons, 240 represented
instances, 308 simplicial instances and 12,566 surviving-prefix states.
Rational and prime-field examples include vanishing features, shifted
rows, repeated label patterns, original face orientations and rank drops.
Two larger fixtures have 5,408,312 formal tensor rows but retain four
original columns, and 2,704,156 formal vertex features but actual feature
rank three, retaining 48 of 153 graph edges. These are exact fixtures,
not estimates of worst-case performance.

The executable supports rational and supplied prime fields. The full proof
separately constructs finite-field extensions and bounds rational bit
growth. No verification of integral torsion or top-degree homology is
claimed; those objects are outside the theorem.

## Incidence decoding

Independent original rows are selected before the lift, preserving their row-label meanings. Factoring the label polynomial for a column into its row-label and incidence-deficit factors makes the surviving column's scalar independent of the incident row. Projection onto the selected original rows is injective on the full column span and on every later column restriction.

For a top simplex and one of its facets, the label deficit is at most <code class="math">a+b</code>. In the one-color specialization, the exterior kernel has dimension <code class="math">\binom{n-k}{p+1}</code>; stacking the rescaled boundary blocks gives the other bound <code class="math">kr</code>. Both bound the same lifted rank. The color-count convention assigns safe vertices a permanent, never-failing color.

## Homology and filtration scope

At every allowed state, the lower chain coordinates and lower boundary maps agree literally, and the surviving top-boundary image spaces agree. The induced homology identifications therefore commute with the filtration and inclusion maps. This gives persistence-module isomorphisms, rather than only equality of Betti numbers.

The full original lower skeleton is retained. The theorem depends on the chosen coefficient field and covers degrees at most <code class="math">p-1</code>. A supplied filtration order and an independent cost order require separate constructions unless they coincide. The [separate spectral incidence theorem](../../correlated-spectral-regression/manuscripts/graded-incidence-and-simplicial-spectral-sparsification.md) does not add a spectral guarantee at every filtration threshold.


## General incidence and additional top labels

The [native backend](../reference/incidence.py) is justified by its
[realization proof](../incidence-realization.md).

```sh
python3 -B problems/persistence-failure-certificates/verify/check_incidence.py
```

An independently implemented original-matrix elimination checks 373 matrices
and 5,503 surviving ordered prefixes over the rationals and a supplied prime
field. Fifty random simplicial inputs include extra top labels; six labeled
cone fixtures check the exact rank formula and forced retention of every top
simplex. Tests also cover field-specific zero incidences, dependent original
rows with different labels, 70 shared labels with incidence increment one,
a 101-digit failure budget, empty matrices and six malformed requests.
These finite checks supplement the full incidence, naturality and lower-bound
proofs. The API assumes a supplied prime modulus; it implements neither field
extension construction nor top-dimensional homology.

**Attribution:** icekylinx and GPT-6 Astra Pro.
