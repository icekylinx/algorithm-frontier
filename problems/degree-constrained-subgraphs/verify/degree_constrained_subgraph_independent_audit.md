# Verification note

**Curated source path:** `sources/checkpoint-o/degree_constrained_subgraph_independent_audit.md`

The source audit follows.

# Independent audit of the degree-constrained subgraph reductions

**25 October 2026.** The reductions in `general_degree_constrained_subgraphs.md` pass the following independent checks. They are corollaries of the general matching backend and do not improve its exponent.

## Sparse selector

The recursive permutation network has distinct input and output positions at every nontrivial level. The size-one subnetwork may use one position for both roles; its incoming and outgoing arcs still meet different endpoints after splitting. Every split endpoint has its idle edge plus at most two transition edges. Only the top input endpoints receive port attachments, and only the top output endpoints receive sink attachments. Thus maximum degree three is preserved, including the size-one case.

Parallel original edges have different incidence ports and different cross-edge endpoint pairs. No identification of their edge records occurs. The resulting ordinary matching instance is simple even when the original host is a multigraph.

At an occupied split position, both endpoints must use non-idle edges. Summing occupied incoming and outgoing matches cancels every transition. Exactly the prescribed number of sink attachments therefore equals the number of local port attachments. All other ports use cross edges. Conversely, a partial bijection between the desired ports and the selected outputs extends to a full permutation; deleting the unneeded vertex-disjoint routes leaves the required matching paths, and unused positions use idle edges.

## Interval-degree hub

Let `X=sum_v(f(v)-deg_H(v))=F-2|E(H)|`. Every feasible original subgraph has `0<=X<=D` and parity `X==F mod 2`. For `A` the least integer at least `D` with parity `F`, the number `(A-X)/2` is an integer in `[0,floor(A/2)]`. When `A` is odd, `X` is odd and consequently at least one; this supplies the only endpoint check needed for the upper bound.

A triangle whose private vertices each require degree one chooses either their private edge or both hub edges. These choices contribute exactly zero or two to the hub degree. Distinct triangles and parallel dummy edges remain independent explicit records.

For `D=0`, even `F` gives an isolated hub requiring degree zero, which may be discarded. Odd `F` gives a hub requiring degree one with no available incident edge, correctly rejecting the impossible prescribed-degree instance. No hidden loop is used.

## Cardinality optimization

Before adding parity triangles, prescribing each original degree `f(v)` leaves hub degree exactly `F-2|E_original|`. The hub upper bound `F-2K` therefore expresses at least `K` original edges, and its lower bound expresses at most `K`. Intersecting with `[0,D]` and rejecting empty intervals handles all boundary cases. These inequality predicates are monotone even if feasible exact cardinalities have gaps.

Applying the interval reduction a second time is still linear in the original number of records. Only the first hub has a nonzero interval width, at most `D<=2m`; all original vertices have singleton prescribed intervals. The final selector graph is therefore `O(m log(m+2))`. Decoding through both reductions retains only original cross-edge identifiers.

## Necessary input normalization

Upper bounds may be clipped to the incident degree. A required lower bound above that clipped upper bound must instead cause rejection. In particular an exact prescribed degree above the incident degree must not be clipped to a smaller requirement. An isolated vertex with positive required degree is infeasible. This clarification was sent to the author during review.

If bounds are supplied using arbitrarily long binary encodings, reading their bit strings must be charged to input length; the graph-operation bound assumes bounded-word values or adds that reading cost. After comparisons and clipping, all nontrivial gadget degrees and numeric parameters are `O(m)`.

The zero-edge instance reduces to the empty factor exactly when all required lower degrees vanish. The promised verifier must certify a maximum matching before its failure to be perfect is used as a NO answer or a binary-search predicate. These checks introduce no new matching or weighted-optimization assumption.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
