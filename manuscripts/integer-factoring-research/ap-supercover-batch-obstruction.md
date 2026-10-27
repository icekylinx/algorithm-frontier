# AP supercovers and shared q-factorial batches for thickened quadratics

<!-- imported-source: checkpoint_10_general_factoring_theory_2026-10-27.zip; ap_supercover_batch_obstruction_2026-10-27.txt; sha256=40850536bd743e1900fbeaa7cc92b3ce0ef2899588ac70e0d9179f9bf513c021 -->

**Scope:** retained separate research branch; not part of the selected conditional theorem review. See the [curated dependency and review map](../../problems/integer-factorization/sources.md).

Status: proved restrictions on specified representation/cost templates.
These are not lower bounds for arbitrary algorithms or arithmetic circuits.

## 1. Independent AP products: a general separated-interval theorem

Fix positive constants c,C. Let S be the union of T integer intervals
of H consecutive integers. Assume their left endpoints are separated
by at least cT, all intervals lie in a span of at most CT^2, and
1<=H<=cT/2. For every finite integer AP P of n distinct terms,

```text
  |P intersect S| = O_(c,C)((H+sqrt(T)) sqrt(n)).
```


Consequently, every AP supercover S subset union_r P_r, with lengths
n_r, satisfies

```text
  sum_r sqrt(n_r) = Omega_(c,C)(T H/(H+sqrt(T))).
```


At H comparable to sqrt(T), this is Omega(T). One AP containing the
whole span has square-root charge O(T), so the optimum supercover
budget in this particular model is Theta(T).

Proof. Intersect P with the containing interval of S. The intersection
is an AP segment of m<=n terms and step D>=1. If D>H, each of the T
intervals contains at most one AP term. Thus

```text
  |P intersect S| <= min(m,T) <= sqrt(Tm).
```


If D<=H, the span of these m terms meets O_c(1+mD/T) intervals of S.
Each interval contains at most 1+(H-1)/D<=2H/D terms. Therefore

```text
  |P intersect S| <= O_c(H/D+mH/T).
```


Since D>=1 and m<=CT^2+1, this is O_(c,C)(H sqrt(m)). The single-AP
bound follows. Summing it over a cover and using |S|=TH proves the
budget lower bound.

This includes all signed indicator decompositions, regardless of the
sizes of their integer coefficients: if 1_S=sum_r c_r 1_(P_r), then
S is contained in the union of APs with nonzero coefficients. It also
includes strict AP supersets used only for collision detection. No
restriction that an AP stay inside S is imposed.

Interpretation. An AP a,a+D,...,a+(n-1)D contributes
prod_(j<n)(1-q^(a+jD)), an ordinary geometric q-factorial. A strategy
whose certified cost is the sum of independent soft-O(sqrt(n_r))
q-factorial calls cannot obtain an o(T) budget by choosing a better AP
supercover at H comparable to sqrt(T). This says nothing about a
different algorithm for evaluating those AP products jointly.


## 2. Shared common-step batches: a divisor-energy obstruction

Let T>=64, 1<=H<=T/8, and

```text
  S(T,H)={t^2-i : T<=t<2T, 0<=i<H}.
```


Write Delta(T)=max_(1<=v<=3T^2) tau(v), where tau counts positive
divisors. The elementary maximal-divisor bound gives Delta(T)=T^o(1).

A common-step batch consists of K integer APs, all with the same
positive step D and each with at most n terms; their starting points
are arbitrary. Let B=K+sqrt(Kn). Such a batch covers at most

```text
  O(H sqrt(Delta(T)) B)
```


points of S(T,H). Therefore any collection of these batches whose
union covers S(T,H), even using different D and n in different batches,
has total budget

```text
  sum_batches (K+sqrt(Kn)) = Omega(T/sqrt(Delta(T))) = T^(1-o(1)).
```


In particular, this cost template cannot certify a fixed-power saving
over T. Supersets, signed cancellation, and large integer coefficients
do not evade the conclusion, since it uses only the cover property.

Proof for D>H. Let I be the number of S-points covered by one batch.
Assign each covered point to one AP containing it, obtaining disjoint
sets of sizes v_1,...,v_K, with sum v_r=I. Any unordered pair assigned
to the same AP has positive difference mD for some 1<=m<n.
Write its two elements as t^2-i > s^2-j. Since D>H, necessarily t>s,
and

```text
  (t-s)(t+s) = mD+(i-j) > 0.
```


The integer on the right is at most 3T^2. For fixed m and delta=i-j,
there are at most Delta(T) possible pairs (t,s), because a factor pair
(t-s,t+s) determines them uniquely. The number of offset pairs (i,j)
with this delta is H-|delta|, and the sum of these counts over all
delta is H^2. Thus the total number of S-pairs with positive difference
in {D,2D,...,(n-1)D} is at most n H^2 Delta(T). Consequently,

```text
  (I^2/K-I)/2 <= sum_r binom(v_r,2) <= n H^2 Delta(T),
```


and hence

```text
  I <= K + H sqrt(2Kn Delta(T)).
```


The assignment is important: it prevents overlap between the APs from
counting one pair repeatedly.

Proof for D<=H. The intervals [t^2-H+1,t^2] have separation at least
a constant times T. As in part 1, a single n-term AP meets at most
O(H+nH/T) points of S. Hence

```text
  I <= min(TH, O(HK+HKn/T)).
```


If Kn<=T^2, use Kn/T<=sqrt(Kn); if Kn>T^2, use TH<Hsqrt(Kn).
In both cases I=O(H(K+sqrt(Kn))). Combining the two step-size cases
proves the batch bound. Sum over batches, use |S|=TH, and divide.

Why this is the relevant shared budget. For K AP starts a_r and common
step D, construct explicitly

```text
  f(X)=prod_(r<K)(1-q^(a_r)X), deg(f)=K.
```


The product of all AP factors is prod_(j<n) f((q^D)^j). Root generation
and polynomial construction cost soft-O(K), and the known geometric
q-factorial algorithm gives soft-O(K+sqrt(Kn)), including the input
degree when K>n. The theorem is a lower bound on this explicitly
charged common-step batching template, not a claim that all possible
ways of exploiting those same APs require that cost.

Remaining escapes include more implicit input polynomials, sharing
work across batches rather than charging the displayed sum, norms or
resultants outside this AP template, arbitrary non-monomial constants
in the factors, and modular identities or useful period/factor
discoveries. The statement makes no assumption about ord(q) and uses
no factorization of the coefficient modulus.


## 3. Exact contained APs: an optional stronger count bound

For S(T,H) above, every AP wholly contained in S(T,H) has
O(H+sqrt(T)) terms. Hence an exact nonnegative AP cover requires
Omega(TH/(H+sqrt(T))) APs, independently of their square-root budgets.

Proof. Write an AP as x_j=x_0+jD=t_j^2-e_j, with 0<=e_j<H.
If D<=H, it cannot jump between square intervals, so it has at most H
terms. If D>T^(3/2), total span O(T^2) gives O(sqrt(T)) terms.
Otherwise H<D<=T^(3/2), and the t_j strictly increase. Put
d_j=t_(j+1)-t_j. Then

```text
  1<=d_j<=(D+H)/(2T)<=sqrt(T)/2+1/16,
```


and at each interior j,

```text
  2t_j(d_j-d_(j-1))+d_j^2+d_(j-1)^2
       =e_(j+1)-2e_j+e_(j-1).
```


The right side has absolute value <=2(H-1)<=T/4, while
d_j^2+d_(j-1)^2<T. Any nonzero integer d_j-d_(j-1) makes the left
side have absolute value >T. Thus all d_j equal some d>=1. Now e_j
is quadratic in j, with leading coefficient d^2. For 2m+1 terms,

```text
  e_0+e_(2m)-2e_m=2d^2m^2<=2(H-1),
```


so the AP has at most 2sqrt(H)+2=O(sqrt(T)) terms in this case.

Translating all exponents changes none of these arguments, so known
integer zero exponents can be avoided by an overall shift. The
modular scalar may still admit special shortcuts, which these
representation statements do not attempt to exclude.


## 4. Extension of the shared-batch obstruction to general quadratics

Let p(t)=At^2+Bt+C with integer A!=0, 0<=t<L, and H comparable to
sqrt(L). For sufficiently large L, there is a subinterval of
T=floor(L/4) consecutive rows on which p is monotone and successive
values differ in absolute value by at least |A|L/2. To see this, write
p(t+1)-p(t)=2A(t-v), where v=-(A+B)/(2A). If v<=L/2 choose the last
quarter of rows; otherwise choose the first quarter. These H-wide
exponent intervals are disjoint and have gaps Omega(T).

Set V=1+|A|L^2+|B|L and Delta_V=max_(1<=v<=V) tau(v). For D>H, the
pair-count proof changes only to

```text
  (t-s)(A(t+s)+B)=mD+(i-j).
```


Each nonzero right side has at most 2tau(|mD+i-j|) possible pairs
(t,s), since the signed factor pair determines t-s and t+s uniquely
when A!=0. Its absolute value is at most V. For D<=H, the same gap
count gives O(H+nH/T) intersections per AP; a bound on the total
exponent span is not needed for this batched argument.

Thus any AP supercover of all the original quadratic-band exponents,
partitioned into explicit common-step q-factorial batches, has total
budget at least Omega(L/sqrt(Delta_V)). If |A|+|B|<=L^O(1), then
Delta_V=L^o(1), so the budget is L^(1-o(1)). The constant C is an
irrelevant translation and may be arbitrarily large.

The divisor quantity is used only in the mathematical analysis; this
claim does not ask an algorithm to compute any factorization. For
completeness, tau(v)=v^o(1) follows elementarily: for any epsilon>0,
large primes p satisfy a+1<=2^a<=p^(epsilon*a/2), while the finitely
many smaller primes contribute at most a fixed power of log(v), which
is eventually <=v^(epsilon/2).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
