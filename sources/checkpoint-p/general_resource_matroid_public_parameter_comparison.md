# Public comparison for general recipient-matroid allocation

**25 October 2026. Primary-source and parameter audit.**

This note compares the current general-resource reservation candidates with
named public results. It distinguishes the rank r of an arbitrary
player-selection matroid from the total number q of potential players.
The new proof status is recorded in its separate manuscripts and audits;
this file is not itself a promotion of a candidate.

## 1. Correct public model and the existing constant approximation

Bamas, Lindermayr, Megow, Rohwedder and Schloeter,
[*Santa Claus meets Makespan and Matroids: Algorithms and Reductions*,
arXiv:2307.08453v1](https://arxiv.org/abs/2307.08453v1), Theorem 4,
give polynomial approximation factors 8+epsilon for general intrinsic
resource values and 4+epsilon for two values. Their resource-specific
matroid constrains the set of recipients of a resource. Integral
polymatroids are included. All players in their displayed model are
compulsory. Section 4 and Appendix F prove the central covering algorithm;
Appendix E, Theorem 21 and Lemma 22 provide the rounding and value reduction.
The arXiv record checked on the date above still lists only v1.

This is the same direction of resource constraint as the present general
recipient-matroid problem. It is not the player-local item matroid of DRZ
or of the earlier exact available-bundle extension.

### Arbitrary player selection already follows publicly

For an arbitrary player matroid M of positive rank, add one resource of
value H>sum_j v_j and recipient matroid M*. Make all q players compulsory.
Given an original basis I of M, give the new resource to its complement
and extend each original independent recipient set to a basis. Conversely,
the recipients D of the new resource form a dual basis, and I=P\D is an
M basis whose values use only the original resources. Restricting their
receiving sets preserves independence. These two operations prove equality
of the two integer optimum values.

H has polynomial encoding length; the dual oracle is a polynomial matroid
operation. Thus the public polynomial 8+epsilon guarantee already covers
arbitrary player selection and arbitrary recipient matroids in the base
common-value model. A new factor near five is a quality/time and parameter
tradeoff, not the first constant approximation for this model.

For unit-valued original resources, the dummy instance has only the two
positive values 1 and H. The public 4+epsilon theorem already applies.
The same conclusion follows directly from the Section 4 covering core.
For two arbitrary original values, the dummy resource can introduce a
third value; the printed two-value guarantee should not automatically be
transferred to that selection model.

The public displayed comparator is integer optimum. This source does not
state the particular coupled player-basis/configuration relaxation in the
new notes. A configuration-LP comparator needs its own proof. Additional
heterogeneous player-local bundle constraints are also not encoded merely
by the dual dummy resource.

## 2. Why slowing down the printed recursion is not enough

I read Section 4 and Appendix F, including Definition 34 and Lemmas
31--37, to check whether simply allowing quasipolynomial time improves
the displayed ratio. In that proof the leading four is a certificate
coefficient, not just the price of its polynomial batch count.

The source reserves 2b per addable element A but serves b per current
polymatroid element. Lemma 33 then compares the blocker count |B| with
approximately |A|. The infeasibility certificate has a rank deficit
approximately one half of |Z2|. In Lemma 35 its value inequality bounds
the fraction of Z2 assigned to the polymatroid by approximately
1/(alpha-2). To fit the rank deficit, this charged proof needs

\[
                         \frac{1}{\alpha-2}\le\frac12,
\]

so alpha>=4 in the zero-error limit. Sending its progress parameter to
zero, or paying for more recursive calls, does not change this inequality.

There is also a useful check on the obvious overprovisioning retuning.
Suppose the same positive certificate accounting is generalized from 2b
to ab, a>1. Its natural blocker comparison becomes
|B|>=(a-1)|A| up to vanishing error, and its corresponding certified
rank-deficit fraction is at most (a-1)/a. The value calculation uses
1/(alpha-a). Therefore this accounting would require

\[
 \alpha\ge a+\frac{a}{a-1}
           =4+\frac{(a-2)^2}{a-1}\ge4.
\]

This is a limitation of this specific positive certificate envelope.
It is not a lower bound for the public algorithm under every possible
analysis, nor a lower bound for the allocation problem. It does show why
merely replacing the time label in the printed proof by “quasipolynomial”
does not establish a stronger factor.

Lemma 22's general-value reduction then balances a fat-resource threshold
t with the small-resource guarantee T/alpha-t after its additive-largest-
resource rounding. This gives t=T/(2alpha). Within that named wrapper,
the leading eight similarly survives a pure runtime retuning. A ratio
near five would need another certificate, another reduction, or another
algorithmic ingredient. The present direct reservation certificate is
such an additional proposed ingredient; it should not be described as a
theorem already printed in BLMRS.

## 3. A stronger public parameterized result in an important subcase

Jansen and Maack,
[*An EPTAS for Scheduling on Unrelated Machines of Few Different Types*,
arXiv:1701.03263v2](https://arxiv.org/abs/1701.03263v2), also treat
ordinary additive Santa Claus. Their few-type scheme has displayed time

\[
 2^{O(K\log K\,\epsilon^{-1}\log^4\epsilon^{-1})}
       +\operatorname{poly}(|I|)
\]

for approximation 1+epsilon, with K the number of player valuation types.
In particular K<=q. The source explicitly includes the Santa Claus
variant, and [Dagstuhl Report 23291, Section 5.3](https://drops.dagstuhl.de/storage/04dagstuhl-reports/volume13/issue07/23291/DagRep.13.7.96/DagRep.13.7.96.pdf)
notes its parameterized-approximation interpretation with the number of
children as parameter. This is already a much stronger quality guarantee
than a constant factor for that ordinary compulsory-player subcase.

It does not supply the present arbitrary player-selection or arbitrary
recipient-matroid interfaces. Setting K<=q does not give a bound in
r when r<<q. Enumerating all possible size-r player bases would introduce
q to an r-dependent power, which is different from the new proposed
poly(input) times a function of r. Conversely, when M is the free matroid
on all players and resources are ordinary private-capacity-one items,
the public parameterized scheme must be acknowledged; a first-FPT-
constant claim in that subcase would be false.

## 4. Other checks and exact limits of the search

The 2026 paper by Kumar and Narayanaswamy,
[*Parameterized Hardness Results for the Restricted Santa Claus Problem*](https://link.springer.com/chapter/10.1007/978-3-032-17156-6_22),
studies incidence-graph structural parameters and the target utility.
Its stated hardness parameters are not the served-selection rank r of
an arbitrary player matroid. It does not resolve this comparison.

The corrected latest DRZ manuscript,
[arXiv:1807.07189v4](https://arxiv.org/html/1807.07189v4), concerns
a player-selection matroid with ordinary physical resources. Its current
coefficient and historical versions are recorded separately in
`matroid_allocation_public_comparison_and_version_audit.md`. Neither its
old third coefficient nor its current fifth coefficient can be applied
to arbitrary recipient matroids without a new resource adapter.

The explicit-transversal-slot adapter and the public all-player PS
available-bundle reconstruction are documented in
`item_matroid_allocation_public_scope_audit.md`. They cover important
structured classes, and can be stronger than near five there. They do
not identify arbitrary oracle recipient matroids with transversal slots.

No directly matching public general-recipient quasipolynomial factor-five
theorem was verified in this search, and no displayed theorem located
here gives the proposed r-only bound with arbitrary selection, general
recipient matroids, and the same configuration comparator. This is a
report of checked sources, not an exhaustive priority claim. The safe
comparison is against the named BLMRS pipeline and the stronger named
special cases above.

## 5. Comparison ledger

| Domain | Named public consequence | What remains different in the reservation proposal |
|---|---|---|
| Arbitrary recipient matroids, arbitrary selection M, general values | Polynomial 8+epsilon via BLMRS plus a dual dummy resource | Near-five quality with explicit rank-dependent search; coupled configuration comparator |
| Same recipient model, all players compulsory, two values | Polynomial 4+epsilon in BLMRS | A near-five statement does not improve this special case |
| Unit values and arbitrary M | Polynomial 4+epsilon by the same dual dummy construction | The direct near-five factor is not the best named special-case guarantee |
| Ordinary physical items, all players compulsory | Jansen--Maack parameterized scheme in player-type count K<=q | Arbitrary selection rank r can be much smaller than q; general recipient constraints are absent publicly here |
| Explicit transversal recipient slots | Public PS/DRZ reconstructions with their stated player-side imports | General oracle matroids need a proved joint resource invariant |
| Optional heterogeneous player-local families as well as recipient matroids | No automatic extension from the printed BLMRS theorem claimed | Both row-perspective and recipient-column constraints must be maintained |

Any final claim should name its time model, comparator, matroid access
model, and which of r, q, resource rank, and local-oracle parameters enter
the exponent. These are mathematical distinctions, not optional caveats.
