# Approximate available-bundle oracles in current-blocker allocation

**25 October 2026. Oracle and value-time extension; internal root and
independent audits completed.**

This note relaxes the exact available-bundle oracle in
[player-local-downward-closed-allocation-extension.md](player-local-downward-closed-allocation-extension.md). It keeps
physical item ownership, common intrinsic values, the player-selection
matroid, and all current-blocker exchanges. The oracle may lose a
specified multiplicative factor. The loss enters the value certificate
explicitly; it does not require assuming that approximate oracle
outputs are monotone under deletion of available items.

The algorithmic imports are the audited current-blocker exchange and
integer-signature lemmas, the sharp star coefficient, and the
matroid-union fat-resource reduction. The new proof is the oracle
certificate and its parameter accounting.

## 1. Model and oracle contract

Let $`M`$ be a player-selection matroid of rank $`r`$ on the
explicit player set. Physical items have common nonnegative intrinsic
values $`v_e`$. Each player $`p`$ has a nonempty downward-closed
family $`\mathcal F_p`$ of permitted bundles. Different selected
players must receive disjoint physical items. Rank zero is the empty
allocation; ratios below assume $`r\ge1`$.

For every available set $`A`$, a deterministic oracle returns a
feasible bundle $`W_p(A)\subseteq A`$, with the guarantee

```math
v(W_p(A))\ge\lambda\,
 \max\{v(C):C\subseteq A,\ C\in\mathcal F_p\},
 \qquad 0<\lambda\le1.
 \tag{A1}
```

The factor $`\lambda`$ is common to the calls and known. An oracle
with different certified factors can use their minimum. Oracle work,
its numerical parameters and the bit length of $`\lambda`$ are
paid. This is a guarantee relative to (A1), not a claim that any
feasible bundle returned by a heuristic certifies an upper bound.

Use the same perspective relaxation $`L(T)`$ as the exact-oracle
note:

```math
\begin{split}
 &x\in P_{\mathcal B(M)},\qquad
 y_p\in x_p\mathrm{conv}
                  \{\mathbf1_C:C\in\mathcal F_p\},\\
 &\sum_p y_{pe}\le1,\qquad
 \sum_e v_e y_{pe}\ge T x_p.
 \end{split}
 \tag{A2}
```

At $`x_p=0`$ the perspective variable is zero. No feasible point
or configuration LP is required as input.

## 2. Fresh scans replace exact maximality

At a search state with forbidden physical union $`F`$, call (A1)
on $`E\setminus F`$ for each eligible player. If the returned
value is at least the chosen bundle threshold $`B>0`$, delete
items until the bundle is inclusion-minimal above $`B`$, and run
the original blocked-insertion or free-cascade microstep.

A completed scan is a sequence of calls made at one unchanged state.
If every return has value below $`B`$, then

```math
\max\{v(C):C\subseteq E\setminus F,\ C\in\mathcal F_p\}
                          <B/\lambda
       \quad(p\text{ eligible}).
 \tag{A3}
```

After a microstep the implementation may restart the scan. It does
not permanently cache a failed approximate call. A deterministic
approximation algorithm can return different-quality witnesses on
nested available sets, even when the actual optima are monotone.
Restarting costs at most one full player scan per charged state.

Previously completed lower layers retain their mathematical
inequalities (A3): the earliest-circuit exchange preserves both their
eligible player sets and their forbidden physical sets literally.
No relation between different approximate outputs is needed. The
last-layer refresh and immediate old-free-center cascades are unchanged.

## 3. The strict certificate and general quality condition

For an eligible player with $`x_p>0`$, decompose
$`y_p/x_p`$ into feasible-bundle indicators and restrict each
bundle to $`E\setminus F`$. Downward closure and (A3) imply

```math
\sum_{e\notin F}v_e y_{pe}
                                  <(B/\lambda)x_p.
 \tag{A4}
```

Let the current matching size be $`k<r`$, let
$`s=|Y_{<i}|`$, and put

```math
J_0=I\setminus\mathrm{owners}(Y_{<i}),\qquad
 w=r-|J_0|=r-k+s\ge1.
```

The eligible mass is at least $`w`$. Provided $`B\le\lambda T`$,
a feasible point of (A2) therefore requires

```math
v(F)>(T-B/\lambda)w.
 \tag{A5}
```

Strictness holds also at $`B=\lambda T`$: positive eligible
mass exists and the available-value bound is strict for every positive
player coordinate.

Thus (A3), an independent $`J_0`$, and

```math
v(F)\le(T-B/\lambda)(r-|J_0|)
 \tag{A6}
```

are a valid oracle-relative certificate of infeasibility. A verifier
can rerun a complete scan and check the returned values, in addition
to the matroid and resource counts. The soundness of that verification
uses the proved guarantee of the available-bundle algorithm (A1).

All stored bundles remain minimal above $`B`$. Physical ownership
is unchanged, so the sharp star bound remains

```math
v(F)\le C(B,u)|Y|,
 \qquad C(B,u)=\max\{u,\ 2B+\min(u,B)\},
 \quad u=\max_e v_e
 \tag{A7}
```

Here $`u=0`$ if the item set is empty.

Put $`\rho_r=(r-1)/r`$. Since $`s/w\le\rho_r`$, an
empty final blocker layer gives (A6) whenever

```math
\boxed{\quad B/\lambda+\rho_r C(B,u)\le T.\quad}
 \tag{A8}
```

The exact-boundary search therefore terminates with a valid result in
$`2^{O(r)}`$ times a polynomial input and oracle multiplier. Each
successful layer has at least one distinct matching blocker, and the
same rank-bounded integer-composition count pays every microstep.

## 4. Positive slack and the general value curve

If

```math
\Delta=T-B/\lambda-\rho_r C(B,u)>0,
       \qquad
       \gamma=\min\{1/2,\Delta/(2C(B,u))\},
 \tag{A9}
```

test a completed layer for $`|Y_i|>\gamma w`$. Failure implies

```math
v(F)\le C(B,u)(\rho_r+\gamma)w
                 <(T-B/\lambda)w,
```

so it is certified infeasible. Passing layers have multiplicative
current growth, and their depth is
$`O(\gamma^{-1}\log(r+1))`$. The number of charged states is

```math
\min\left\{2^{O(r)},
        (r+1)^{O(\gamma^{-1}\log(r+1))}\right\}.
 \tag{A10}
```

For completeness the equality solution of (A8) has an explicit form.
Write $`\tau=1/\lambda`$, $`d=\tau+3\rho_r`$. For
$`r\ge2`$, a positive solution exists exactly when
$`u<T/\rho_r`$, and its largest value is

```math
B^*_{r,\lambda}(T,u)=
 \begin{cases}
 (T-\rho_r u)/(\tau+2\rho_r),&u\le T/d,\\
 T/d,&T/d\le u\le3T/d,\\
 \lambda(T-\rho_r u),&3T/d\le u<T/\rho_r.
 \end{cases}
 \tag{A11}
```

The formulas agree at the boundaries. For rank one use
$`B^*_{1,\lambda}=\lambda T`$ for arbitrary $`u`$. This is
also obtained by choosing the best approximate bundle among nonloop
players; exact optimization is not being claimed for an inexact oracle.

## 5. Arbitrary item sizes and the matroid-union wrapper

Let

```math
d_{r,\lambda}=\lambda^{-1}+3-3/r,
                 \qquad B_0=T/d_{r,\lambda}.
 \tag{A12}
```

An item is fat when $`v_e\ge B_0`$. Keep a player-fat incidence
only when $`\{e\}\in\mathcal F_p`$. This singleton test is
implementable by (A1): for positive $`v_e`$, an admissible singleton
has positive optimum on $`\{e\}`$, and any $`\lambda>0`$
guarantee forces that singleton to be returned. An inadmissible
singleton cannot be returned by a feasible oracle.

Construct the fat transversal matroid $`N`$, set
$`U=M^*\vee N`$, and run the small-item algorithm on $`U^*`$.
Its rank $`r'`$ is at most $`r`$. The existing integral-optimum
and configuration-LP promises remain valid because they only use
feasible singletons, downward closure and convex combinations of
feasible all-small configurations. They do not use exact available
optimization.

For the exact target $`B=B_0`$, small items have $`u<B_0`$,
and $`C(B,u)\le3B_0`$. Since
$`\rho_{r'}\le\rho_r`$, condition (A8) follows from

```math
B_0/\lambda+3\rho_r B_0=T.
```

When $`r'=0`$, no inner algorithm is needed. The existing union
decomposition and extension of its dual part return a basis of the
original matroid, each player supplied by either a small feasible
bundle or one fat feasible singleton. This proves ratio
$`d_{r,\lambda}`$ in rank-exponential time.

The comparison may be taken against the player-matroid configuration
LP with configurations in $`\mathcal F_p`$. It is not a claim
against the original unrestricted-size perspective relaxation alone.
All polynomial union, dual and fat-matching oracle costs are paid as
in the established wrapper.

## 6. Uniform positive-error time: no additional inverse-lambda exponent

Fix $`\eta>0`$. Keep the fat threshold $`B_0=T/d`$, where
$`d=d_{r,\lambda}`$, and use the smaller inner bundle target

```math
B=T/(d+\eta),\qquad
 \varepsilon=(B_0-B)/T=\frac{\eta}{d(d+\eta)}.
 \tag{A13}
```

The coarse coefficient $`\overline C=2B+B_0`$ bounds the sharp
coefficient because $`u<B_0`$. It satisfies
$`\overline C\le3T/d`$. Even using the original rank $`r`$,
the gap is

```math
\begin{split}
 T-B/\lambda-\rho_r\overline C
  &=(\tau+2\rho_r)(B_0-B)\\
  &=(\tau+2\rho_r)\varepsilon T.
 \end{split}
 \tag{A14}
```

Here $`\tau\ge1\ge\rho_r`$, so
$`\tau+2\rho_r\ge3d/4`$. Hence the gap divided by
$`\overline C`$ is at least

```math
\frac{\eta(\tau+2\rho_r)}{3(d+\eta)}
       \ge\frac{\eta d}{4(d+\eta)}
       \ge\frac18\min\{\eta,1\}.
 \tag{A15}
```

The last step uses $`d\ge1`$, separately for $`\eta\le1`$
and $`\eta\ge1`$. Therefore the uniform choice

```math
\gamma=\frac1{16}\min\{\eta,1\}
 \tag{A16}
```

validates the same growth certificate. In particular ratio
$`d_{r,\lambda}+\eta`$ is obtained in

```math
\mathrm{poly}(\text{input bits, oracle work})\,
 \min\left\{2^{O(r)},
       (r+1)^{O((1+\eta^{-1})\log(r+1))}\right\}.
 \tag{A17}
```

The hidden constant in the rank exponent does not grow with
$`\lambda^{-1}`$. The oracle's own complexity and numerical bit
length may, and are explicitly outside that assertion. The allocation
wrapper uses polynomial space in the full explicit input, in addition
to the supplied oracle's workspace. The same common-grid,
nonmonotone-success target search
applies; use an upper target exceeding
$`(d+\eta)\sum_e v_e`$, which has polynomial encoding length.

## 7. A self-contained knapsack oracle specialization

Suppose player $`p`$ has nonnegative item costs $`a_{pe}`$ and
budget $`b_p`$, with
$`\mathcal F_p=\{C:\sum_{e\in C}a_{pe}\le b_p\}`$.
Costs may depend on the player; the utility of item $`e`$ is still
the common intrinsic value $`v_e`$. The family is downward closed.

A deterministic fully polynomial approximate available oracle is
enough; exact knapsack optimization is unnecessary. Here is a simple
implementation, included to make its numerical guarantee explicit.
Discard unavailable items and singleton-infeasible items. If their
maximum positive value is $`V_{\max}`$, let
$`K=\kappa V_{\max}/m`$, where $`m`$ is the number of retained
items, and round each profit down to $`\lfloor v_e/K\rfloor`$.
Every rounded profit is at most $`m/\kappa`$. A standard dynamic
program stores the minimum cost attaining each integer rounded
profit, and returns a maximum-profit state of cost at most $`b_p`$.
If there is no positive feasible item, return the empty bundle.

The rounded profit range is $`O(m^2/\kappa)`$, giving a
conservative $`O(m^3/\kappa)`$ arithmetic implementation. Every
optimal feasible bundle loses less than $`mK`$ under rounding.
Since $`V_{\max}\le\mathrm{OPT}_{\rm available}`$, the returned
true value is at least
$`(1-\kappa)\mathrm{OPT}_{\rm available}`$. Costs, comparisons
and reconstruction use polynomial-bit rationals. Thus (A1) holds with
$`\lambda=1-\kappa`$, deterministically. This is the classical
profit-scaling FPTAS principle; see, for example, Lawler,
*Fast Approximation Algorithms for Knapsack Problems*,
[Mathematics of Operations Research 4(4), 1979](https://doi.org/10.1287/moor.4.4.339).
No claim of a new knapsack oracle or best FPTAS running time is made.

For a requested allocation ratio $`4-3/r+\zeta`$, choose

```math
\kappa=\min\{1/2,\zeta/(2+\zeta)\},\qquad \eta=\zeta/2.
```

Then $`\lambda^{-1}-1=\kappa/(1-\kappa)\le\zeta/2`$,
so (A17) gives the requested ratio. Oracle cost and workspace are polynomial in
input size and $`1+\zeta^{-1}`$, and the rank-quasipolynomial
exponent uses $`1+\zeta^{-1}`$. In particular rank-one exact
knapsack is not being solved: any guarantee approaching one here
uses a positive approximation error and the FPTAS cost. If $`\zeta`$
is encoded by a very small rational, the FPTAS workspace is not being
claimed polynomial in its encoding length alone.

## 8. Comparison scope

This is an explicit oracle/value bridge for the present rank-sensitive
player-matroid method. It is not by itself a first-approximation claim
for budgeted allocation, an all-player result, or arbitrary
resource-side matroids. The all-player exact-oracle comparison already
has a public Polacek--Svensson extension, documented in
[item-matroid-allocation-public-scope-audit.md](item-matroid-allocation-public-scope-audit.md).

In particular, an all-player knapsack quasipolynomial factor
$`4+\zeta`$ also follows from that public exact-oracle framework.
At target $`T`$, cap intrinsic item values at $`T`$, then round
them down on the common grid $`K=\kappa T/m`$, where $`m`$ is
the item count. Every original target configuration retains value at
least $`(1-\kappa)T`$; the total integer profit is
$`O(m^2/\kappa)`$, so each player's available knapsack optimum
can be computed exactly for these fixed rounded values. This supplies
the public algorithm's exact search interface. Taking its error
$`\zeta/2`$ and $`\kappa=\zeta/[2(4+\zeta)]`$ gives
$`(4+\zeta/2)/(1-\kappa)=4+\zeta`$. Thus the knapsack example
is not an exclusive all-player consequence of the new oracle bridge.

That fixed common-rounding argument is specific to a discretizable
family such as knapsack. An arbitrary $`\lambda`$-only oracle
does not automatically supply the exact nearest-layer search used in
the public algorithm. Any broader same-model record claim requires a
separate source comparison that preserves player selection, common
values, local feasibility, oracle access and the comparator.
