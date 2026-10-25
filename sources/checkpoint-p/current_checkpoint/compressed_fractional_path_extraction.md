# Extracting short path inventories from a shared representation

This is an elementary conditional interface lemma. It does not claim
that an aggregate multicommodity-flow oracle exposes the required data.

## 1. Representation

Let `G` be a graph with positive integral edge lengths. A representation
consists of an acyclic directed dependency graph with `Z` arcs and nodes.
Each leaf is one oriented genuine edge ID or an empty walk. Each
internal node is the ordered concatenation of its children, with the
usual endpoint compatibility. Reversed references can be implemented by
an orientation bit and reversed traversal order. A root record therefore
denotes an actual finite walk in `G`.

There are `P` flow records. Record `a` specifies a commodity `i`, a root
node, and a nonnegative rational mass `f_a`. For each of `M` unit
commodities, the total mass is exactly one. Suppose the total weighted
walk length is at most `M H` and total edge-occurrence flow is bounded
by some capacity vector `c`. All rational arithmetic below is charged
at its actual bit complexity.

## 2. Short-inventory extraction

In `O(Z+P)` arithmetic operations, determine the records of walk length
at most `4H` and their total mass `b_i` for each commodity. At least
`M/2` commodities have `b_i >= 1/2`.

Indeed, if more than half the commodities had short mass below one half,
their long records alone would contribute more than

    (M/2) * (1/2) * 4H = M H

to total length. The weak conclusion with at least half is enough;
endpoint equality at `4H` can be assigned consistently to the short
side.

For every such good commodity, retain only short records and divide
their masses by `b_i`. The resulting records route that commodity's
entire unit. Their aggregate edge-occurrence flow is at most `2c`,
because every retained record is scaled by at most two and all other
records are discarded.

## 3. Output work without expanding long walks

Compute all represented lengths bottom-up, saturating at a threshold
larger than `4H` if only the short/long test is needed. Empty or
zero-length dependency subexpressions can be bypassed. A traversal of
a short record visits at most `O(4H)` genuine edge occurrences after
standard binary concatenation and unary-node suppression. Hence all
retained records can be expanded in

    O(Z + P + P H)

work, independent of the expansion lengths of discarded records.
Cycle erasure in the immediate native graph then produces simple paths
without increasing lengths or edge/vertex loads. A real self-loop is
handled as a genuine edge occurrence before erasure; an empty reference
is never confused with a physical loop.

The conclusion is an explicit fractional candidate-path inventory for
at least half the commodities, with path length at most `4H` and at most
twice the original fractional edge loads. Repeating a suitable flow
construction on the remaining commodities takes at most logarithmically
many rounds, provided its guarantees apply to every restricted demand.

This lemma alone is not an integral routing theorem. A deterministic
selection/rounding procedure must still bound the integral congestion,
its work, and any ambient composition. In particular, it must account
for arbitrary record probabilities, weighted demands, and the maximum
contribution of one selected path.

## 4. Relation to low-step emulators

[Haeupler et al., arXiv:2406.14384v1](https://arxiv.org/html/2406.14384v1)
explicitly use stacked path embeddings (Section 5) and sparse splitting
and concatenation records (Lemmas 7.6--7.7). These are candidate building
blocks for the representation above. Their final Definition 9.1 only
promises an aggregate edge-flow oracle, so the representation size,
construction work, exact masses, and orientation-preserving path
expansion must be verified separately before using this lemma with that
algorithm.

The filtering argument explains why a flow-path decomposition barrier
for all paths need not prohibit extracting a short candidate inventory.
It does not resolve that source's quantitative epsilon dependencies or
establish an improved matching exponent.
