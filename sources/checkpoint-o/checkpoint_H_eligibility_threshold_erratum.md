# Checkpoint H erratum: eligibility in the old-root preparation

**25 October 2026. Corrected in the live notes and checkpoint I.**

The immutable checkpoint H ZIP contains a localized error in Section 2
of `root_only_sp_tree_epoch_counterexample.md` and the corresponding
root audit. That preparation raised a new contact to actual slack 3C
and then expanded it. The established matching client instead triggers
expansion when its cached slack is at least 4C. Its approximation
guarantee implies that an eligible bin has actual slack at least 3C;
this is a necessary lower bound and does not authorize the earlier
trigger. The original preparation as written did not establish a
legal history.

The source contract is explicit in
`current_checkpoint/deterministic_phase_cost_and_guards.md` and
`current_checkpoint/algorithm_outline_and_proof_map.md`.

## Repair

Maintain exact structural-eligibility slack caches during this
preparation. Exact caches satisfy the allowed approximation guarantee.
A numerical path changes only its two endpoint slacks, so maintaining
these particular exact entries requires constant additional work.
This does not reset or change the persistent allocation-price registers.

Raise each contact to its first crossing of 4C, then expand the next
matched pair. Before that crossing the contact-to-free-root offer is
greater than .186/C, since all donors are at least .99L. An exact
winning source therefore has pre-step slack below 4.033C and post-step
slack below 4.1C. Expanding leaves the former contact between 3C-1
and 3.1C-1. Later harmless increases keep every old noncontact below
4.1C, and telescoping parent allocations are bounded by 6(t+1)C.
The chosen L=10000CN still makes every required donor at least .99L.

At the final bridge expansion, the right contact w has slack below
3.1C and therefore exact cache below 4C. The left contact a still
has slack between two and three. These are the only contacts to the
paired remainder, so neither is eligible. All other source-dominance,
linear-tree-size, logarithmic-progress, price-variation, semantic-excess
and surviving-comparison conclusions use the unchanged coarser bound
that old internal slacks are below 5C. They continue to follow.

The corrected construction and root audit contain these constants
explicitly. This is a repair of a claimed reachable history, not a
claim that the uncorrected history was legal.

## Scope

The correction concerns this illustrative old-root-only obstruction.
The fixed-tree path interface, the independent-transversal theorem,
the earlier transfer exponents, and the accepted general-graph
maximum-matching exponent 4/5 do not use this preparation. The
obstruction still does not give a matching running-time lower bound
or imply that a global shortest-path rebuild is necessary.

The later non-tight-receiver example was separately checked against
the same 4C rule before inclusion in checkpoint I. Its preparation
uses an additional legal numerical transfer after expansion; its
proof does not reuse the erroneous 3C trigger.
