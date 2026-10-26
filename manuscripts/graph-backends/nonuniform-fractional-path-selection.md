# Sparse deterministic selection from nonuniform fractional routes

**Separate constructive lemma, 24 October 2026.** This extends the
uniform-candidate selection used by the current 4/5 construction to
arbitrary positive rational candidate masses. It is intended to support
a future compressed-flow route. It does not change the current matching
exponent or assume that a particular flow oracle exposes these records.

## 1. Input and conclusion

For every group g, let J_g be a nonempty list of choices. A choice j has
a nonnegative integer occurrence count a_{gjx} at each resource x.
Only nonzero incidences are stored, or equivalently explicit occurrence
lists are given. Let w_g>=0 be its rational group weight and
alpha_{gj}>=0 its rational candidate mass, with A_g=sum_j alpha_{gj}>0.
Zero-mass candidates may be discarded. Define probabilities only
MATHEMATICALLY by p_{gj}=alpha_{gj}/A_g. The implementation need not
materialize the normalized rational numbers or a common denominator.

Let S>=2 include all group/choice/resource headers and all supplied
occurrences, and let b bound the bit size of each input scalar,
including rational weights/masses/B and encoded integer counts.
Let B>0 be any rational upper bound on every w_g a_{gjx}. Define
```math
\mu_x=\sum_g\sum_j p_{gj}w_g a_{gjx}.        \tag{1}
```
There is a deterministic algorithm choosing one j(g) per group with
```math
\sum_g w_g a_{g,j(g),x}
          \leq 2\mu_x+B\log(8(|X|+1))
                          \quad\hbox{for every }x.           \tag{2}
```
Its work is S times a fixed polynomial in log(S+2) and b, charging
ordinary multiword arithmetic. Only the supplied sparse incidences
are scanned. Zero-weight groups can choose an arbitrary positive-mass
candidate immediately. If there are no nonzero weighted incidences,
the result is trivial.

## 2. Exact positive potential

Put u_{gjx}=w_ga_{gjx}/B, so 0<=u_{gjx}<=1, and
```math
E_{gx}=\sum_jp_{gj}\exp(u_{gjx}),\qquad
 z_x=\mu_x/B .
```
For a partial choice define
```math
W_x=\exp\!\left(\sum_{g\ {\rm fixed}}u_{g,j(g),x}-2z_x\right)
                    \prod_{g\ {\rm unfixed}}E_{gx}.           \tag{3}
```
Since exp(u)<=1+(e-1)u for 0<=u<=1,
```math
\prod_gE_{gx}\leq\exp((e-1)z_x),\qquad
                         W_x^{\rm initial}\leq1.             \tag{4}
```
Thus the initial sum of (3) is at most |X|.

When fixing g, a candidate j gives
```math
W_x^{\rm new}=W_x E_{gx}^{-1}\exp(u_{gjx}).
```
The terms independent of j are a common baseline. Compare only the
nonnegative sparse scores
```math
T_j=\sum_{x:a_{gjx}>0}(W_x/E_{gx})(\exp(u_{gjx})-1).          \tag{5}
```
Their p-weighted average satisfies
```math
\sum_jp_{gj}T_j
       =\sum_x W_x(1-E_{gx}^{-1})\leq\sum_xW_x.              \tag{6}
```
An exact minimum score cannot increase sum_x W_x. After all choices,
W_x=exp((chosen load at x-2mu_x)/B), so even the bound
B log(|X|) would follow under exact real arithmetic. The slack in
(2) supplies a finite deterministic implementation.

For each group, form E_{gx} only on resources appearing in at least
one of its candidates. Outside that union E_{gx}=1 and there is no
change. After selecting j, update every resource in this union,
including those absent from the selected candidate. Their total
count over groups is at most S. This is necessary: absent selected
incidences still require division by E_{gx}.

## 3. Avoid exact rational normalization

Compute
```math
E_{gx}=1+
   \frac{\sum_j\alpha_{gj}(\exp(u_{gjx})-1)}
        {\sum_j\alpha_{gj}},\qquad
 z_x=\sum_g
   \frac{\sum_j\alpha_{gj}u_{gjx}}{\sum_j\alpha_{gj}}.         \tag{7}
```
All numerators and denominators in (7) are positive sums, without
cancellation. A group total can be approximated by floating addition
of its input masses; no exact sum with a product of unrelated
denominators is constructed. Conditional averaging in the proof
uses the true ratios, while the algorithm approximates (7) with
explicit relative or absolute error as appropriate.

For u>0 evaluate exp(u)-1 as the positive series
```math
u(1+u/2!+u^2/3!+\cdots).
```
Because u<=1, O(log(S+2)) terms with guarded rounding suffice for
relative error S^{-c}, with a fixed sufficiently large c.
This remains true when u or an alpha is tiny: their binary exponents
are stored explicitly and the leading u is not subtracted from one.

Use mantissas with O(log(S+2)) guard bits and signed binary exponent
fields of O(log(S+b+2)) bits. Input rational-to-floating conversion
costs polynomial(b+log S) bit work. A product w_ga/B can have an
exponent of magnitude O(b+log S); products in (3) have exponents of
magnitude O(S). These bounds follow from u<=1, z_x<=number of groups,
and 1<=E_{gx}<=e.

Small positive summands may be rounded away only when their aggregate
relative contribution is inside the declared error. Positive sums
and products have standard elementary relative-error accumulation
bounds. There are O(S polylog S) scalar operations on the sparse
records. Choose c to dominate that count. The maintained W_x and
candidate scores then approximate their exact versions within one
common relative factor 1+epsilon, with epsilon<=1/(100(S+1)).
For the initial exponent -2z_x, the same precision gives absolute
error O(S times S^{-c}), and hence the required relative error after
exponentiation.
For that initial exponential, scale the nonnegative magnitude into
[0,1], use its positive Taylor series, take a reciprocal, and square
O(log(S+2)) times. Guard precision S^{-c} absorbs this amplification;
no unit-cost transcendental operation is assumed.

Selecting the minimum approximate score yields an exact score at
most (1+O(epsilon)) times the exact minimum, and therefore at most
(1+O(epsilon)) times the p-weighted average. By (6), potential grows
by at most a factor 1+O(epsilon) at each group. Initial rounding and
all group choices keep total potential below 8(|X|+1), proving (2).

Every score has only nonnegative terms. A candidate's tiny sparse
score is not recovered by subtracting two nearly equal global
potentials. This is why relative control suffices without an
exponentially precise mantissa.

## 4. Consequence for fractional path records

Suppose a represented fractional route family assigns each commodity
g total mass one, with path probabilities p_{gj}. Give commodity g
weight w_g. If its weighted expected resource loads are bounded by
mu_x and every individual weighted candidate occurrence is at most B,
the lemma returns one actual route for every commodity satisfying (2).

For ambient paths, first normalize every immediate input edge image.
If every candidate host path has at most H edges and the input
images are simple, then a candidate visits an ambient vertex at most
O(H+1) times. If w_g<=Delta, one can take
B=O((Delta+1)(H+1)). This is the same length-free ambient principle
as in [deterministic-weighted-path-selection.md](deterministic-weighted-path-selection.md),
now with nonuniform probabilities and no token-copy expansion.

Suppose a flow on a remaining commodity set has total weighted path
length at most H times its total mass and a shared path representation.
[compressed-fractional-path-extraction.md](compressed-fractional-path-extraction.md)
gives a short inventory for many commodities in its stated unit-demand
case. Renormalized candidate masses can be passed as the ORIGINAL
retained alpha values: (7) performs their normalization implicitly.
Their weighted expected loads increase by the explicitly proved
renormalization factor, not by the number of candidates.

For weighted commodities, a weighted-total-length bound alone
guarantees a fraction of TOTAL WEIGHT, not necessarily a fraction of
the NUMBER of commodities. A logarithmic-round termination argument
must specify which progress measure is used and the input weight
range. The unit-token version avoids that distinction.

## 5. Scope of the extension

The lemma supplies deterministic sparse rounding once candidate masses,
their path representation, and a fractional-load certificate are
available. It does not create such a fractional flow, establish a
low-step source's epsilon dependence, or prove its compressed
representation size. Those are separate provider obligations.

The current 4/5 matching construction continues to use its reviewed
uniform-token selection. This extension is a separate mathematical
tool for investigating a stronger provider.
