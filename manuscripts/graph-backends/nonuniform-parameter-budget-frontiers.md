# Nonuniform parameter budgets for the current hierarchy

**Internal optimization analysis, 25 October 2026.** This note explains
what can and cannot be gained by choosing different parameters at
different levels of the current distance hierarchy. It proves lower
bounds on a specified positive accounting envelope, not lower bounds on
algorithms, matching, distance oracles, or Gomory--Hu trees. A new
construction that removes one of these charged terms is outside the
model. The result therefore identifies a concrete research bottleneck
rather than ruling out further algorithmic progress.

Let `U` be the logarithm of the nominal initial size and let
`h = log(U+4)`. Multiplicative absolute constants are suppressed.
The discussion is asymptotic; finite small instances use the exact base
case. A budget denotes the logarithm of a multiplicative overhead.

**Checkpoint E update.** Section 5 records the earlier strong-forest
$`7/8`$ budget, whose copy charge has now been changed by the
uncontracted compressed-core construction. Section 7 proves the
corresponding $`6/7`$ boundary for the new budget. The matching
$`4/5`$ statement in Section 4 is unchanged. None is an algorithmic
lower bound.

## 1. The model and the part of the hierarchy that matters

Consider the initial part of a worst-case nominal size ledger whose
local logarithmic sizes `u_i` remain between `U/2` and `U`. A size
reduction parameter `x_i` decreases this ledger by at most `O(x_i)`.
Consequently, traversing this part of the hierarchy requires

```math
\sum_i x_i \ge cU.                     \tag{1}
```

This is a statement about the full worst-case size allowance that the
analysis promises to handle. Some particular graphs can have much
smaller children or terminate immediately; (1) is not asserted for
such an input's actual recursion tree.

At each of these levels use a routing parameter `p_i`, repair depth
`K_i`, and size-reduction parameter `x_i`. The following positive terms
are present in the current certified envelopes:

```math
\begin{array}{ll}
\text{local work:} & x_i,\quad u_i/p_i,\quad K_i p_i h,\\
\text{cumulative recourse/copies:} &
          c_{\rm in}\ \ge c_0\sum_i u_i/K_i,\\
\text{cumulative metric log-stretch:} &
          a\ \ge c_0 h\sum_i K_i p_i.
\end{array}                                                \tag{2}
```

The symbols in (2) denote the *charged positive envelopes*, not
necessary losses incurred by every execution. These ledgers are defined as fixed positive sums of the displayed
terms. An asymptotic upper bound such as `g = O(p h)` alone does not
imply a matching lower bound on a true quality loss or running time.
Other existing terms, such as the decomposition parameter and its
construction work, have been dropped. Dropping positive terms can only weaken an obstruction
for this envelope.

If the hierarchy work budget is `B`, the model requires

```math
x_i\le C B,\quad u_i/p_i\le C B,\quad
 K_i p_i h\le C B,\quad
 \sum_i u_i/K_i\le C B.                                    \tag{3}
```

The first two conditions and (1) imply, for the number `d` of levels in
this interval,

```math
d=\Omega(U/B),\qquad p_i=\Omega(U/B).
                                                               \tag{4}
```

If an implementation switches directly to an exact base inside this
interval, its nominal dense exact-base cost is `exp Omega(u_i)` and
must be charged to `B`. Thus this shortcut does not avoid the argument
for the sublinear budgets `B = o(U)` considered here.

All logarithms of the local sizes in this interval are within fixed
constant factors of `h`. Using local rather than master logarithms
therefore does not change the inequalities below.

## 2. A metric-versus-work inequality

By Cauchy--Schwarz,

```math
\left(\sum_i\sqrt{u_i}\right)^2
 \le \left(\sum_i u_i/K_i\right)\left(\sum_i K_i\right).
```

Since `u_i >= U/2`, equations (3)--(4) give

```math
\sum_i K_i=\Omega(d^2 U/B).
```

The metric envelope in (2) consequently satisfies

```math
a\ge\Omega\left((Uh/B)\sum_i K_i\right)
    =\Omega(d^2U^2h/B^2)
    =\boxed{\Omega(U^4h/B^4)}.                              \tag{5}
```

Thus, for a prescribed metric log-stretch allowance `Q`, the current
model needs

```math
B=\Omega((U^4h/Q)^{1/4}).               \tag{6}
```

This remains true when the routing, repair, and reduction parameters
vary arbitrarily from one level to another, subject to (1)--(3).

At `Q = Theta(U^(6/7) h)`, equation (6) becomes
`B = Omega(U^(11/14))`. The uniform choice in
[apsp frontier proof](../../problems/apsp-frontier/proof.md) attains this envelope up to absolute
constant factors. The `11/14` point is therefore optimal within the
specified positive-budget model, not only among uniform parameter
choices.

## 3. Why the work-only boundary is three quarters

The local repair-work term in (3), together with `p_i = Omega(U/B)`,
gives

```math
K_i=O(B^2/(Uh)).
```

Hence

```math
\sum_i u_i/K_i
       =\Omega(d U^2h/B^2)
       =\Omega(U^3h/B^3).
```

Its required upper bound `O(B)` yields

```math
B^4=\Omega(U^3h).                  \tag{7}
```

If the metric stretch is required to be subpolynomial, its certified
logarithm must be `a = o(U)`. Equation (5) then strengthens (7) to

```math
B/(U^{3/4}h^{1/4})\longrightarrow\infty.     \tag{8}
```

The slowly growing retreat

```math
B=O(U^{3/4}h^{1/4}\omega(U)),\qquad
 a=O(U/\omega(U)^4),\qquad \omega(U)\longrightarrow\infty
```

in the companion note approaches exactly this boundary. Choosing
`omega(U) = h^(1/4)` gives the cleaner explicit time
`exp O(U^(3/4) h^(1/2))` and stretch `exp O(U/h)`.
A claim of the boundary time `exp O(U^(3/4) h^(1/4))` together with
subpolynomial stretch is not supplied by these envelopes.

## 4. The matching quality charge returns four fifths

The raw-cycle and exact matching clients must also include the full
metric/cycle-quality envelope in their overhead budget. In this model
that adds `a = O(B)`. Substitution into (5) gives

```math
B^5=\Omega(U^4h),\qquad
                        B=\Omega(U^{4/5}h^{1/5}).          \tag{9}
```

The current matching parameter choice attains (9). Merely choosing
nonuniform levels therefore cannot turn the APSP `3/4` time point into
a matching result. One must improve a charged interface, such as the
full accumulated correction-and-lift quality, rather than omit it.
This is not a matching lower bound.

## 5. The strong-forest outer composition returns seven eighths

For this section the hierarchy work has budget `B`, while its charged
copy/congestion envelope is `c_in`. The outer strong-forest budget is
`Z`. Its current covering and flattening formula includes

```math
B\le CZ,\qquad U/\Lambda\le CZ,\qquad
 \Lambda U/K_{\rm cov}\le CZ,\qquad
 \Lambda c_{\rm in}\le CZ,                                \tag{10}
```

and its scale condition requires

```math
K_{\rm cov}\Lambda a\le CU.       \tag{11}
```

First obtain a relation that does not replace `c_in` by `B`.
Weighted Cauchy--Schwarz gives

```math
\left(h\sum_i K_i p_i\right)
       \left(\sum_i u_i/K_i\right)
 \ge h\left(\sum_i\sqrt{u_i p_i}\right)^2.
```

The local work condition `p_i >= c u_i/B`, together with (1) and
`x_i <= CB`, now gives

```math
a c_{\rm in}
                    =\Omega(U^4h/B^3)
                    \ge\Omega(U^4h/Z^3).                 \tag{12}
```

On the other hand, (10)--(11) imply

```math
a\le O(Z/\Lambda^2),\qquad
 c_{\rm in}\le O(Z/\Lambda),\qquad
 \Lambda\ge\Omega(U/Z).
```

Consequently,

```math
a c_{\rm in}\le O(Z^5/U^3).            \tag{13}
```

Combining (12) and (13),

```math
Z^8=\Omega(U^7h),\qquad
                       Z=\Omega(U^{7/8}h^{1/8}).          \tag{14}
```

The currently assembled strong forest attains this budget. Thus its
`7/8` balance also survives arbitrary per-level parameter choices in
the stated model. Improving the Gomory--Hu result through this route
requires changing the inner stretch/copy tradeoff, the covering scale
condition, the flattening copy charge, or replacing this strong-forest
client altogether.

## 6. What would count as further progress

The equations identify concrete ways a new idea could escape the
accounting model. They do not prove that any such idea exists:

* A repair construction with smaller selected-child recourse than the
  present `exp O(u_i/K_i)` term would change (2).
* A router or local repair whose complete work no longer contains the
  charged `K_i p_i h` term would change (3).
* A cycle comparison with less accumulated raw-quality loss would
  remove the identification `a = O(B)` in the matching client.
* A path-forest construction that avoids the present outer scale or
  copy amplification would change (10)--(11).

These are interface questions. The proofs above justify spending
further research effort on those questions rather than repeatedly
retuning the same positive terms.

## 7. The new pool construction reaches the six-sevenths budget

The no-recursive-reset construction in
[decremental strong forest proof](../../problems/decremental-strong-forest/proof.md) removes
$`\sum_i u_i/K_i`$ from the simultaneous forest-copy envelope.
That positive sum remains in the work budget $`B`$. Therefore
Sections 1--2 still give
```math
a\ge\Omega(U^4h/B^4).             \tag{15}
```
There is no remaining justification for substituting the old
$`c_{\rm in}\ge\Omega(\sum_i u_i/K_i)`$ in Section 5.
The new occurrence analysis is a genuine change of the charged
interface, and hence lies outside that old $`7/8`$ obstruction.

Let $`Z`$ bound the new outer logarithmic work. The unchanged
positive outer terms and scale constraint imply
```math
B\le O(Z),\qquad U/\Lambda\le O(Z),\qquad
 \Lambda U/K_{\rm cov}\le O(Z),\qquad
 K_{\rm cov}\Lambda a\le O(U).
```
The middle conditions give
```math
\Lambda\ge\Omega(U/Z),\qquad
 K_{\rm cov}\ge\Omega(\Lambda U/Z).
```
Combining with the scale constraint,
```math
a\le O(Z/\Lambda^2)\le O(Z^3/U^2).
                                                               \tag{16}
```
Equations (15)--(16), with $`B\le O(Z)`$, yield
```math
Z^7=\Omega(U^6h),\qquad
                     Z=\Omega(U^{6/7}h^{1/7}).             \tag{17}
```

This derivation permits arbitrary per-level routing, repair, and
shrink parameters under the nominal-size and positive-charge
assumptions of Sections 1--2. It does not rely on any positive
lower charge for the new simultaneous occurrence $`c`$.
Consequently simply improving $`c`$ further would not improve
this specified balance.

The new uniform construction attains (17): with $`U=t^7h`$,
$`p=r=d=\Lambda=t`$, $`K=K_{\rm cov}=t^2`$, and
$`x=\Theta(U/t)`$, it has $`B=O(t^6h)`$, $`a=O(t^4h)`$,
and $`c=O(t^2h)`$. The remaining outer work fits $`O(t^6h)`$.

Further progress through this framework therefore needs a better
inner metric/work tradeoff, a different outer scale relation, or
a different client. Equation (17) constrains the stated accounting
model; it does not rule out any of those changes or prove a lower
bound for strong SSSP, Gomory--Hu, or matching algorithms.
