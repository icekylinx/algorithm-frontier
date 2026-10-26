# Rational comparator recovery without splitting the approximation error

This manuscript improves the fractional-comparator time base in the
unrelated-value allocation and selected-flow applications. A known
polynomial-bit denominator bound on each fixed selected-set LP
optimum permits using the full requested gap epsilon in the
selection routine. Exact reoptimization of the returned selected
set then removes the tiny search error. The selected family must
be fixed during the search.

The resulting fractional-comparator time is
`Gamma(1/epsilon)^c poly(H)`, using the full requested error parameter in the selection gap. No improvement of an integer rounding loss is claimed.
This is a rational optimization lemma, not a first-publication claim.

## 1. Abstract fixed-family interface

Let F be a finite nonempty family of permitted sets. For each
I in F, let lambda_I be a finite nonnegative optimum of a fixed-set
optimization problem, and let

```math
\Lambda=\max_{I\in\mathcal F}\lambda_I.
\tag{RG1}
```

Assume the following interfaces, all with polynomial binary
complexity in H.

1. A permitted set can be found, or an empty family can be detected,
   before the search.
2. Every lambda_I can be optimized exactly, with a witness, in
   polynomial time once I is specified.
3. A known positive integer D, with polynomial bit length, bounds
   the denominator of every lambda_I in lowest terms. A known
   rational V bounds Lambda from above.
4. For a requested rational alpha in (0,1) and positive target T,
   a deterministic gap routine either returns a permitted I with
   `lambda_I>=alpha*T`, or fails. Failure is allowed only when
   `Lambda<T`. Its time is `G(alpha,c) poly(H,bitlength(T))` and
   its space is polynomial for the targets below.

No success-monotonicity is assumed. In particular, success need
not imply `Lambda>=T`. Both the family F and the fixed-set objective
lambda_I are independent of T. A selector whose membership changes
with T needs a separate argument and is not covered automatically.

## 2. Search on a sufficiently fine rational grid

Write alpha=A/B in lowest terms, with positive integers A<B, and
set

```math
\delta=\frac{1}{2BD^2}.
\tag{RG2}
```

Use integer indices for the delta-grid. Initialize L=0 with any
permitted set and an external upper endpoint

```math
U=\big(\lceil V/\delta\rceil+1\big)\delta.
\tag{RG3}
```

Thus U>V>=Lambda. Query grid midpoints until the upper and lower
indices differ by one. On success, save the returned set and set
L=T. On failure, set U=T. Every such failed upper endpoint is
strictly larger than Lambda by the gap guarantee. Hence at the
end,

```math
L>\Lambda-\delta.
\tag{RG4}
```

If no positive target succeeded, the saved initial set still has
lambda_I>=alpha*L=0. In every case the saved I satisfies

```math
\lambda_I\ge\alpha L
                           >\alpha\Lambda-\alpha\delta.
\tag{RG5}
```

The number of calls is logarithmic in `V/delta+2`. Its bit length
is polynomial in H, log D and the encoding of alpha. A numerically
large D is never used as a loop count.

## 3. Reoptimize the saved set and use rational separation

Optimize the original fixed-I problem exactly, returning its
actual optimum lambda_I and witness. This step is necessary:
an arbitrary fractional witness from a target LP can have a
denominator depending on the artificially fine target grid. The
denominator bound used here is for the optimum of the original
fixed-set problem, whose description does not contain T.

Because F is finite, Lambda equals lambda_J for some J, and both
lambda_I and Lambda have denominator at most D. If
`lambda_I<alpha*Lambda`, write them in lowest terms as p/d and
z/e, where d,e<=D. The positive difference satisfies

```math
\alpha\Lambda-\lambda_I
   =\frac{Azd-Bpe}{Bed}
   \ge\frac1{BD^2}=2\delta.
\tag{RG6}
```

But RG5 gives this difference smaller than alpha*delta<delta,
a contradiction. Therefore the returned exact fixed-set optimum
obeys

```math
\lambda_I\ge\alpha\Lambda.
\tag{RG7}
```

This includes Lambda=0. If all fixed-set values are zero, the
initial zero witness is enough; if Lambda>0, RG4 and the denominator
bound ensure that the search cannot be trapped at a zero lower
endpoint by insufficient precision.

The complete optimization time is `G(alpha,c) poly(H,log D,log B)`
with the original polynomial space. No second allocation of the
approximation error to the search is required.

## 4. A uniform denominator bound for implicit rational LPs

For completeness, suppose every fixed-I optimum is realized by
a bounded nonempty rational LP with at most n variables. Pad a
smaller formulation by zero-fixed coordinates so n is the common
ambient dimension. All
constraint coefficients and right sides have numerator and
denominator of absolute value at most `2^L`, uniformly in I.
The number of constraints can be exponential, provided exact
polynomial separation and the stated encoding bound are available.

Clear denominators in each individual row. There are at most
n+1 entries, including the right side, so all resulting integer
entries have magnitude at most

```math
W=2^{(n+2)L}.
\tag{RG8}
```

At an optimum vertex, choose n linearly independent active rows,
including equalities represented in the usual way if necessary.
Boundedness guarantees vertices even when the feasible polytope
has lower affine dimension. Cramer's rule and the determinant
bound give a denominator for each coordinate of at most

```math
D=n!W^n.
\tag{RG9}
```

If the objective is a coordinate lambda, RG9 is directly the
required bound. General rational linear objectives can be handled
by adding that objective as one extra coordinate, preserving a
polynomial encoding bound. The length of D is
`O(n log n+n(n+2)L)`. Computing D or a power-of-two upper bound
therefore takes polynomial bit complexity. No enumeration of
the implicit constraints is needed to compute this bound.

The deliberately loose rowwise denominator bound avoids assuming
that all exponentially many rank rows share an explicitly listed
common denominator. Uniform coefficient bounds suffice.

## 5. Application to unrelated-value allocation, with or without budget

Fix one genuine permitted player set I. Its fractional common
service optimum lambda_I is the optimum of the LP

```math
\begin{aligned}
  \max\;&\lambda,\\
  x_j&\in P(f_j),\\
  \sum_j v_{pj}x_{jp}&\ge\lambda &&(p\in I),\\
  \lambda&\ge0,
 \end{aligned}
\tag{RG10}
```

with the original assignment-cost row added in the budgeted model.
A redundant upper bound lambda<=V makes boundedness explicit.
All counts are bounded by resource singleton ranks. Each resource
row has zero-one coefficients and an integer right side at most
f_j(P). The only other coefficients are original rational values,
costs, the budget and the explicit lambda bounds. Their uniform
encoding bound is known from the original instance and rank queries
on P. Thus RG8--RG9 apply with polynomial n and L.

The family is the fixed set of permitted player bases, optionally
with a fixed polynomially implementable selection condition. The
budget in RG10 is an assignment budget and does not change with T.
The weighted corank gap already established in U and B has
alpha=1-epsilon and time `Gamma(1/epsilon)^c poly(H)`.

Apply RG2--RG7, reconstruct the exact optimum allocation of the
saved basis, and then use the accepted lower rounding. This gives

```math
v_p\ge\max\{0,(1-\varepsilon)\mathrm{FOPT}-u_p\}
       \quad\text{for every selected }p,
\tag{RG11}
```

in `Gamma(1/epsilon)^c poly(H)` time and polynomial space. With
one nonnegative assignment budget, use the disposal and maximum-total
dual-cost rounding from B; the budget remains exact. FOPT still
selects one actual basis and relaxes only the resource counts.

The earlier relative-search proof and its explicit positive scale
remain correct. RG11 improves its exponential base through stronger
use of the rational LP description; it does not change its comparator,
the loss u_p, or its permitted assignment model.

## 6. Application to selected splittable multicommodity flow

For a fixed permitted commodity set, its maximum concurrent rate
is the optimum of an explicit rational flow LP. Capacities are finite,
demands are positive and source differs from sink; the manuscript's
known finite rate bound can be imposed explicitly. Nonnegative
routing costs and one fixed budget add only original rational rows.
Therefore a uniform D follows directly from RG8--RG9.

Once the direct nonnegative flow separator and the weighted selection
gap have been independently verified, RG7 yields a schedule of
selected flows with concurrent rate at least `(1-epsilon)OPT` in
`Gamma(1/epsilon)^c poly(H)` time, exact edge capacities and exact
routing budget. There is no integral assignment rounding in this
application, so no largest-unit additive loss appears.

This conclusion is for splittable fractional flow. It does not
provide unsplittable routing, edge-disjoint paths or integer flows
for the multicommodity problem. It is also unrelated to selecting
active machines that must support all job bases; that model lacks
the required downward service interface.

## 7. Scope of the lemma

The proof uses only a known rational denominator bound, exact
fixed-set reoptimization and the already stated one-sided gap
properties. It does not assume that successful gap answers are
monotone or exactly feasible at their nominal target. It does
not infer exact combinatorial optimization from an approximate
gap routine.

Target-dependent selected-set families are outside RG1 unless a separate fixed benchmark is supplied. The uniform denominator bound belongs to the original fixed-set optimum, not to an arbitrary target-dependent witness.

---

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
