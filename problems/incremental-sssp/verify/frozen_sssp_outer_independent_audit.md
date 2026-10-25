# Verification note

**Curated source path:** `sources/checkpoint-o/frozen_sssp_outer_independent_audit.md`

The source audit follows.

# Independent audit of the frozen-detector SSSP recursion

**25 October 2026.** This note independently checks the phase count, changing degree demands, child inventory, and explicit distance notifications in `frozen_detector_incremental_sssp.md`. It follows the separate single-detector audit in `frozen_barrier_detector_independent_audit.md`.

The audited recurrence supports

\[
 (n+m)\exp O\!\left(\log E(N)+
  \sqrt{\log N\,[\log\log N+\log(1/\varepsilon)]}\right)
\]

under the detector and raw-backend hypotheses. In particular, the oracle overhead is a factor in each owner's computation, not in the factor by which total graph inventory grows from one recursion depth to the next.

This audit does not replace the separate checks of scale normalization, recursive path witnesses, the raw backend, or the common arithmetic envelope. Its purpose is to isolate the accounting that could otherwise hide a factor of `E` per outer level.

## 1. Local objects and the accounting measure

An owner receives an incremental positive-length directed graph, possibly with parallel edges, source proxies, and vertex births. Its announced allowance `M` covers its complete lifetime inventory of logical input records. One fixed expansion constant pays per-detector stars, degree units, and port records. The `O(log N)` scale copies are charged in time, outside this allowance.

The raw representation can have `M E(N)^{O(1)}` flat occurrences. These are not additional demand units, parent graph edges, or terms in the coefficient of the detector's potential. They do not enter the child quota or the weighted-distance objective. This separation is indispensable.

Within one owner, every edge identity persists until that owner ends. A phase restart changes anchors and reinitializes its detectors, but does not delete parent graph records. When its parent phase ends, the entire owner ends; there is no attempted persistence of its unit identities into an unrelated new owner.

## 2. Degree units and old-vertex promotion

At target `v`, use one base unit and one unit for every incident parent edge record, with a consistent convention for the source and discarded self-loops. Thus the unit count is proportional to

\[
 1+\deg_{\rm in}(v)+\deg_{\rm out}(v).
\]

The relevant degree is the current degree in the parent graph, including records omitted from a particular normalized scale. A scale's detector reports a vertex only after all its current units are frozen. When the union of scale reports first promotes an old vertex, charge its degree volume to the scale that caused that first promotion. These charged units are distinct across vertices, even if another scale reports the same vertex later.

Consequently the summed degree volume at old-vertex promotions is

\[
 O(\alpha M U^3/\sigma),\qquad U=\log_2N.
\]

Scanning incoming and outgoing adjacency lists at a promotion is therefore paid. The outgoing scan matters: an edge whose head was promoted earlier must acquire its native child version when its tail enters the child later.

This bound deliberately excludes two categories: newly born vertices, which are immediately exceptional, and edges arriving after one or both endpoints were promoted. Both categories are paid by the external input stream, as formalized by the quota below.

## 3. Persistent deficit tokens prove the sound-stop phase count

Fix one normalized scale and one owner lifetime. Give each auxiliary unit a persistent identity through every phase reset. A unit's owner vertex has a true normalized distance in `[1,2]`, nonincreasing after that vertex and unit have been born.

Let the current number of units be `W`, and write

\[
 H=\sum_{j\text{ born}}d(v(j)),\qquad
 F=\sum_{j\text{ born}}a_j,\qquad D=F-H.
\]

Every anchor is an available-walk cost, so `D>=0`. A phase begins with exact anchors for all units then present, hence `D=0`. A later unit may inherit its old vertex's phase anchor or use the cost-two witness for a new vertex. Its birth contributes at most two to `D`; no exact distance computation at that birth is needed.

Between births, the only increase in `D` is a decrease in true distances. At any reset, all current anchors are replaced by current exact distances and `D` is discarded. A reset never creates positive deficit. Thus an individual unit's total contribution to deficit production over an interval is bounded by its birth contribution, if any, plus its true distance decrease during that interval. Resetting that unit repeatedly cannot replenish its distance decrease budget.

Partition time into maximal ranges where

\[
 2^j\leq W<2^{j+1}.
\]

There are `O(log M)` ranges, possibly with some skipped by a large atomic birth batch. During such a range there are at most `O(2^j)` units in total. Each unit initially present can contribute at most one further true distance decrease; each later birth contributes a bounded initial deficit and at most one further decrease. Total new deficit production is therefore `O(2^j)`.

A completed phase wholly within this range that ends in a sound stop discards at least

\[
 \alpha F/2\geq\alpha W/2\geq\alpha2^{j-1}
\]

deficit. Such discarded amounts are disjointly charged to the production budget. There are `O(1/alpha)` such phases. A phase crossing a doubling boundary is charged to that boundary; the total number of those phases is `O(log M)`, even when one batch crosses several boundaries.

Hence one scale causes at most `O(log M/alpha)` stops. Stops attributed to other scales, or quota resets, merely discard uncharged nonnegative deficit; they can only reduce the amount available to be charged here. There are `O(U)` scales, giving

\[
 P_{\rm stop}=O(U^2/\alpha)
\]

per owner. This argument requires only soundness when a detector stops. It does not require a detector to stop as soon as the weighted objective has decreased.

## 4. The child quota pays future incidence volume

Let `theta=2^-s`. Choose `alpha=theta/K_0`, where `K_0` is a fixed polynomial in `U` and `1/epsilon` large enough that all old-vertex promotions generate at most a small fixed fraction of `theta M` child inventory.

Define the quota using graph records and a fixed logical expansion constant `C_d`: the child may receive at most `theta M/C_d` graph records, ensuring that its announced full allowance is at most `theta M`. A source vertex and other constant initialization records can be absorbed because recursive owners are used only above a fixed multiple of `1/theta`; smaller owners are leaves.

Every parent edge creates only a constant number of child records in one phase: at most a source proxy and a native copy, together with at most one anchor per old promoted vertex. Retaining the old proxy after its tail is promoted is harmless and is included in this constant.

If the quota would be exceeded, either an old promotion or an external arrival would account for the new records. Old promotions together occupy only a small fraction of the quota. Therefore a quota restart requires `Omega(theta M)` actual external parent records since the phase began. These records are disjoint across consecutive phases, and the owner receives at most `M` records over its lifetime. The number of quota restarts is `O(1/theta)`.

This also handles one very large batch. Insert the whole batch in the parent's ordinary store, decide that its projected child would overflow, and rebuild the parent without partially creating an oversized child. Charge the restart to that batch's external volume. The newly computed exact phase anchors make all its vertices old in the next phase.

Combining quota restarts, sound stops, and initialization yields

\[
 P\leq K_1/\theta,\qquad
 \log K_1=O(\log U+\log(1/\varepsilon)).
\]

No raw-cycle quantity appears in `K_0` or `K_1`.

## 5. Derivation of the complete recursion bound

Let `A_b` be the sum of the announced allowances of all owners born at depth `b` over the root execution. One owner of allowance `M` creates at most one child per phase. Each such child has allowance at most `theta M`, so

\[
 \sum_{\text{children of this owner}}M_{\rm child}
 \leq P\theta M\leq K_1M.
\]

It follows inductively that

\[
 A_b\leq A_0 K_1^b,
 \qquad A_0=O(n+m).
\]

An owner's computation outside its descendants costs, over all its phases,

\[
 O\!\left(M E(N)^C\operatorname{poly}(U)K_1/\theta\right)
\]

for a fixed `C`. This includes detector construction and lifetime work, all scales, Dijkstra restarts, promotion scans, forwarding, and retirement of the old child. Retirement can visit only the actual records previously created; its cost is charged to their construction/lifetime budgets.

Stop recursing when `M<=C'/theta`. A leaf may recompute exact distances by Dijkstra after each complete external batch. There are at most `M` nonempty batches, so its cost is at most

\[
 M^2\operatorname{poly}(U)
 \leq O(M/\theta)\operatorname{poly}(U).
\]

Its explicit distance writes fit the same bound. The depth is `B<=U/s+O(1)`. Summing owner and leaf costs gives logarithmic overhead

\[
 O\!\left(\log E+s+(U/s+1)\log K_1\right).
\]

Choosing `s=Theta(sqrt(U(log U+log(1/epsilon))))` gives the claimed expression. The fixed polynomial powers of `E` merely change the absolute constant multiplying `log E`.

This derivation exposes the exact failure mode that freezing avoids. If the child reporting volume had included `E^c`, then `K_1` would include `E^c`, producing `B log E` in the exponent. With the proved frozen-unit bound, `K_1` contains only logarithmic and accuracy factors.

## 6. Explicit distance notifications do not create another recursion

An owner has one active child in a phase. Its stored estimate for a vertex outside the exceptional set is its frozen exact phase anchor; for an exceptional vertex it uses the child's current estimate, optionally taking the minimum with an available older upper estimate. All chosen values are costs of available walks.

A local Dijkstra rebuild or a leaf computation visits its own graph and can emit at most one current-value notification per vertex visited. This is paid by its local computation. A notification received from a child can change only the estimate for that same original vertex. It is passed along the unique active ancestor chain, of length at most `B`.

Thus one original notification induces at most `O(B)` ancestor writes, not an independently branching collection of updates. The root array is explicit and has constant-time lookup. Crucially, these estimate changes do not modify the parent's immutable phase anchors, its proxy lengths, or its normalized detector's edge costs. Treating them as such weight updates would both change the incremental model and break the accounting; the proposed construction does not do so.

When an owner restarts, its new exact Dijkstra values overwrite all estimates in that owner. Notifications from its retired child must be suppressed after retirement. This is ordinary settled lifetime bookkeeping and costs only the records already accounted for.

## 7. Master size and finite exceptions

Use global `U=log_2N` for every detector's precision, barrier exponent, and admissible parameters. A local owner of small `M` pays only for its actual records; it is not padded to the master size. The condition on the phase parameter is

\[
 \log_2(1/\alpha)=s+\log_2K_0+O(1)\leq U/100,
\]

not a condition in `log M`. Similarly the raw numerical progress parameter is compared with `N^-1/100`. This resolves the otherwise incorrect conclusion that small recursive owners cannot use the common phase parameter.

For constant or inverse-polylogarithmic `epsilon`, the optimized `s` is `Theta(sqrt(U log U))`, so the parameter condition eventually holds. The stated sufficiently small fixed upper bound on `log(1/epsilon)/U` also makes it hold. Finite exceptional master sizes may be handled by direct recomputation with a fixed enlarged asymptotic constant.

## 8. Small corrections and audit conclusion

During review, three harmless clarifications were sent to the author and incorporated:

* Exclude the source from old-vertex anchor edges, since `D(s)=0` would otherwise create a zero-length loop.
* Define the quota before constant-factor expansion into logical units and ports, so the advertised child allowance really is at most `theta M`.
* State that distance notifications follow a unique ancestor chain and do not update frozen anchors or proxy weights.

No substantive obstruction was found in the audited phase count, changing-demand treatment, quota, recurrence, or explicit-array maintenance. The final exponent claim is conditional on the single-detector and raw-backend hypotheses, as stated in the main note; verification of a returned distance array would not by itself establish that running-time claim.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
