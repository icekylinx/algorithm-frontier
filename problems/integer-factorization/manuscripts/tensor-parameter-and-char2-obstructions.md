# Scoped limitations of direct contraction retuning

<!-- imported-source: checkpoint_13_general_factoring_increment_2026-10-28.zip; tensor_parameter_and_char2_obstructions_2026-10-28.txt; sha256=16f67fc7fc3141a0d19081b1be21fd41f14f02debadf1fe69338803c0d7ae455 -->

**Scope:** limitations of the specified contraction templates. See the [curated dependency and review map](../sources.md).

**Review scope clarification.** The working precision is `p_t = p + 8*h*D_t + 8*M*(a+1)`; its simplified tile term uses the specified cumulative schedule. The Cauchy-rank argument concerns its full half-grid submatrix. The linear mode count additionally assumes the stated number of full packets. It is a limitation of that direct template, not a claim about every factoring network.

Research checkpoint, 2026-10-28 (Asia/Singapore).

These are limitations of three specified proof/algorithm templates, not
lower bounds for integer factorization, tensor contraction, or arbitrary
future improvements. The October 25, 2026 contraction theorem is assumed.

## 1. Small root precision and small native degree do not by themselves
```text
   improve the logarithmic exponent in the current mode enumeration
```

In the current Cauchy/Hermite construction, a call with M Boolean edges
uses packet length L=2^a and a label-array size D_arr=64^(2a)=2^(12a).
Its packing condition includes M>=L D_arr. Consequently

```text
                      a <= (log_2 M)/13.
```


The retained valuation-level parameter u satisfies u<=a/2 in the stated
cumulative schedule. Thus u=O(log M) regardless of how small the native
maximum degree is. The second packing condition involving the maximum
degree can improve constants in this restriction, but not its order.

The deformation polynomial has degree approximately 2ML. The tapered
Hermite multiplicities have slope h=Theta(M/u). At a retained node whose
tile-size parameter is D, the precision needed for this interpolation
is of order MD/u, even if the incoming precision is only one bit. Thus
replacing P_0=Theta(M) by P_0=O(M/log M), or even P_0=1, does not remove
the term responsible for the first-call branching exponent.

The proof bounds the number of variables at each positive weight by
O(M/D), with budget O(MD/u). To test what can be obtained from these
bounds alone, consider the abstract budget model having Theta(M/D)
potential variables per weight and budget Theta(MD/u). This model is
consistent with those numerical upper bounds; it is not an assertion
that every actual network realizes all these independent nonzero modes.
Suppose, as in the parameter range used in the proof, D/sqrt(u) grows.
Take a small constant c>0 and choose all variables whose weights lie in
the interval

```text
                    1 <= j <= c D/sqrt(u).
```


There are Theta(M/sqrt(u)) such variables. Allow their exponents to be
independently zero or one. The total weighted budget of selecting all of
them is O(c^2 MD/u), so a sufficiently small fixed c makes every subset
budget-feasible. Their total unweighted degree is O(M/sqrt(u)), which
also lies below the M-affine-factor degree cap. Therefore this generic
enumeration includes

```text
                        2^{Omega(M/sqrt(u))}
```


tuples in this abstract model. Since u=O(log M), these numerical budget
estimates alone do not yield a better asymptotic denominator than
sqrt(log M). Improving the actual algorithm requires additional
structure beyond the current parameter bounds.

This statement is deliberately restricted. For a special tensor family,
many enumerated coefficients might vanish or admit joint computation.
A proof of such a property would escape this accounting obstruction.
The argument does not establish that every admissible tuple contributes
on a factoring instance, or that every actual network attains the
abstract model's potential-mode count.

## 2. Direct characteristic-two interpolation loses the low-rank modes
A natural proposal is to work directly in characteristic two, avoiding
the artificial two-adic precision increase. Let L=2^a, identify packet
positions with the finite field F_L, and replace the integer-grid
polynomial by

```text
                          C(T)=T^L-T.
```


Put W_xy(T)=C(T)/(T-(y-x)). Since C'(T)=-1=1, these are polynomials,
and W(0)=I. At a field element t, W_xy(t) is zero unless y-x=t, in which
case it equals one. Writing positions in an F_2 basis, translation by
nonzero t flips at least one coordinate. This is compatible with the
same orientation-based idea of choosing groups where the translated
matching is local. The interpolation nodes now have unit differences.

However, look at a cross-group entry and expand at T=t+z. If
d=t-y+x is nonzero, then

```text
 W_xy(t+z) = (z^L-z)/(d+z),
```


so its coefficient of z is 1/d in characteristic two. Choose a coordinate
where t has bit one, and choose row and column positions with the same
fixed value of that coordinate. Then the sets of field elements
{t+x} and {y} are disjoint affine half-grids, each of size L/2. The
matrix of first coefficients on this submatrix is

```text
                         (1/(t+x-y))_(x,y).
```


This is a Cauchy matrix over the finite field. Its determinant is a ratio
of products of pairwise differences within the two sets and differences
between them; every factor is nonzero. It therefore has rank L/2.

Accordingly a separated row/column representation of the first-order
cross interaction already needs at least L/2 scalar modes on this full
submatrix. Across Theta(M/L) full packets this gives Theta(M) modes of
weight one. With Hermite jet order Theta(M), the straightforward mode
enumeration is exponential in M. The gain from integer two-adic tiles
was their progressively low-rank approximation; distinct characteristic-
two field points do not preserve that property.

This rules out only the direct substitution of a finite-field grid into
the existing Cauchy interpolation and separated-mode scheme. A different
kernel, an algorithm that contracts these full-rank interactions without
enumerating modes, or additional arithmetic structure of the factoring
tensors could still improve the bound.

## 3. Why recursively contracting the mode sum does not automatically
```text
   supply a second logarithmic improvement
```

Consider the proposed composition in its optimistic form. A first
deformation has parameter u, and its retained mode tuples are represented
using E=Theta(M/sqrt(u)) bits, matching the abstract entropy scale above.
The coefficient of a tuple is a product of contributions from r groups.
One would like to contract this outer mode problem recursively, while
computing each group contribution by a smaller inner contraction.

Even granting a perfect encoding with O(E) wires and ignoring the cost
of expressing the global weighted-budget restriction, the group boundary
degrees average Omega(E/r). If one uses the literal theorem with outer
parameter s_outer=Theta(E), its maximum-degree requirement therefore
forces

```text
                            r=Omega(E^(1/10)).
```


For the original packing construction with r groups, the array has
D_arr=r^(2a) cells and the packet length is L=2^a. Its packing budget
M>=L D_arr gives

```text
                    a(1+2 log_2 r)<=log_2 M.
```


With a>=2u as in the cumulative schedule, this implies

```text
                         u log r=O(log M).
```


In the regime E=Theta(M/sqrt(u)), log E=Theta(log M). Thus the literal
outer maximum-degree condition makes log r=Omega(log M), which in turn
forces u=O(1). The first-stage mode encoding is then only E=Theta(M),
and the outer theorem supplies the original M/sqrt(log M) scale rather
than an additional logarithmic divisor.

There is also a useful way to see the same tradeoff in an idealized
degree-sensitive generalization. Suppose an outer contraction on E
wires and degree Delta could cost exp(O(E/sqrt(log(E/Delta)))). Taking
Delta on the average scale E/r would give the prospective exponent

```text
               E/sqrt(log r)=Theta(M/sqrt(u log r)).
```


The packing budget u log r=O(log M) prevents this accounting from
certifying a smaller scale than M/sqrt(log M). This paragraph is a
parameter calculation for a hypothetical generalized interface, not
an additional theorem being assumed or a lower bound on its algorithms.

If the group vertices are too large, exposing their internal factors
can reduce their individual degrees, but it also reintroduces the
Theta(M) internal wires that the composition sought to remove. Actual
mode sparsity, special algebraic cancellation, or a different packing
construction could avoid these premises. This argument does not rule
out such improvements; it rules out counting the same packing budget
twice to claim an automatic extra sqrt(log M) gain.

Reference for the template being analyzed:
https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-contraction.tex

**Attribution:** icekylinx and GPT-6 Astra Pro.
