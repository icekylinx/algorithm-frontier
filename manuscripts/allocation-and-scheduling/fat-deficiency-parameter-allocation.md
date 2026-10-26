# Allocation parameterized by the deficit of a fat-resource cover

The factor-four allocation theorem can be parameterized by the number
of selected players that cannot be covered by one sufficiently valuable
resource unit each. The exponential or quasipolynomial part need not
depend on the full player-selection rank r. This note makes the adaptive
parameter, the optimization guarantee, and the sound target search
explicit. It does not assume the desired target or its deficit is known.

The theorem imports the reviewed algorithms in
[recipient matroid configuration proof](../../problems/recipient-matroid-configuration/proof.md),
[recipient polymatroid proof](../../problems/recipient-polymatroid/proof.md), and, for its
stronger component comparator,
[scaled-recipient-matroids-binary-configuration-transfer.md](scaled-recipient-matroids-binary-configuration-transfer.md).

## 1. Model and the appropriate comparator

Use one of the following already reviewed allocation models, with an
arbitrary player matroid M of rank r on q explicit potential players:

* arbitrary recipient matroids, compared to their coupled configuration
  optimum;
* supplied scaled matroid types f_j=c_j r_Rj, compared to their separate
  component count-configuration optimum;
* arbitrary integral recipient polymatroids, compared to integer optimum
  or the residual-capacity configuration optimum proved separately in
  [recipient-polymatroid-residual-configuration-relaxation.md](recipient-polymatroid-residual-configuration-relaxation.md).

Call the selected comparator optimum OPT. Unit values are common
nonnegative rationals. Optional player-local type-symmetric downward-
closed families use a paid certified rational lambda available oracle,
with tau=1/lambda. Exact unrestricted availability has tau=1. A stronger
comparator for arbitrary polymatroids can be substituted only after its
fat-complement and lower-cover interfaces are separately proved.

All original and derived oracles, submodular minimization where needed,
numerical encodings, target search and reconstruction are paid in H.
Resource copies or numerical capacities are not expanded.

## 2. The fat-player matroid and its deficit

For a positive threshold theta, call a unit fat when its value is at
least theta. The players that can each receive one locally feasible
fat unit form a matroid N_theta:

* for ordinary recipient matroids, union their singleton-feasible
  restrictions over the fat resources;
* for integral recipient polymatroids, first take each fat resource's
  Boolean cap P(f_j) intersect [0,1]^P, then restrict and union;
* for supplied scaled matroids, use their Boolean c_j-fold union,
  clipping c_j to q for this one-service operation.

These are the same paid fat matroids as in the accepted wrappers. Let

```math
U_\theta=M^*\vee N_\theta,
 \qquad
 \delta(\theta)=r(U_\theta^*).
 \tag{D1}
```

This delta is exactly the rank of the derived small-player problem.
It is computable in polynomial oracle time and is nondecreasing in
theta, since raising the threshold only removes possible fat services.

### Lemma 1: delta is the maximum-cover deficit

Let nu(M,N) be the largest cardinality of a common independent set of
M and N. Then

```math
\boxed{\delta(\theta)=r-\nu(M,N_\theta).}
 \tag{D2}
```

**Proof.** If F is common independent, extend it to an M-basis I.
Its complement D is an M*-basis disjoint from F. Thus D union F is
independent in M* vee N, giving r(U)>=q-r+|F|.

Conversely, decompose a U-basis as disjoint D union F, with D independent
in M* and F independent in N. Extend D to an M*-basis D'. The set
F'=F minus D' is contained in the M-basis P minus D', hence is common
independent. At most q-r-|D| members of F have been removed, so

```math
|F'|\ge r(U)-(q-r).
```

Both bounds prove r(U)=q-r+nu, and (D2) follows. This proof also uses
exactly the decomposition and extension operations already available
in the algorithm. No unimplemented intersection oracle is required.
$`\square`$

Thus r-delta players can be selected independently in M and each covered
by one theta-valued fat unit. The remaining delta is a structural
deficit, not the total number of potential or compulsory players.

## 3. A fixed exception budget k

Fix an integer 1<=k<=r. Put

```math
d_k=\tau+3-3/k,\qquad \eta_0=\min\{\eta,1\}.
 \tag{D3}
```

For a positive target T, set theta=T/d_k and compute delta(theta).

If delta>k, return the explicit response **fat deficit exceeds k**.
This is not a certificate that the original target is infeasible.

If delta<=k, run the reviewed small-resource algorithm on U_theta*,
with small units of value less than theta, and use

```math
B=T/(d_k+\eta_0)
 \tag{D4}
```

for the positive-error branch, or B=theta for the exact branch. If
delta=0 no small search is needed. On success use the existing union
decomposition to reconstruct a full basis of the original M.

### Lemma 2: conditional target correctness and time

If the chosen target comparator is feasible at T and delta(T/d_k)<=k,
the algorithm succeeds with minimum value at least B. Its time is

```math
\mathrm{poly}(H)
 \min\{2^{O(k)},(k+1)^{O((1+\eta^{-1})\log(k+1))}\},
 \tag{D5}
```

or 2^{O(k)} poly(H) at the exact boundary. Wrapper space is polynomial.

**Proof.** The fat-complement argument gives a feasible derived target
on the matroid U_theta*, whose rank delta is at most k. All current
record counts, augmentation phases and signatures in the inner search
are bounded by delta, not by r. The original large-r matroid only
enters polynomial union, duality, rank and reconstruction work.

Let rho_delta=(delta-1)/delta when delta>0. At B=theta, the sharp cover
is at most 3theta and

```math
\tau\theta+3\rho_\delta\theta
                \le d_k\theta=T.
```

For positive error, B>=theta/2 and the small-unit bound u<theta implies
C(B,u)<=3B. Since rho_delta<=1-1/k,

```math
T-\tau B-\rho_\delta C(B,u)\ge\eta_0 B.
```

The same gamma=eta0/16 supplies uniform current-layer growth and the
signature count (D5). If delta=0, the fat reconstruction gives at
least theta>=B directly. No small-record state is needed.
$`\square`$

## 4. A computable bottleneck value beta_k

For k<r, define

```math
\beta_k=\sup\{\theta>0:\nu(M,N_\theta)\ge r-k\},
 \tag{D6}
```

with beta_k=0 if no positive threshold works. If k=r, set beta_k=infinity.
For k<r and beta_k>0 the supremum is attained at a positive resource
unit value, because fat units use the weak inequality v_j>=theta and
there are only finitely many supplied values. The matroid N changes
only at those values. Testing them, or binary searching their sorted
list, computes beta_k in polynomial oracle time.

Equivalently, beta_k is the best minimum value of a one-unit allocation
to r-k players whose owners are independent in M. Formula (D2) gives

```math
\delta(T/d_k)\le k
             \quad\Longleftrightarrow\quad T\le d_k\beta_k
 \tag{D7}
```

for positive T, with the stated zero/infinity conventions.

Define the capped target

```math
T_k^*=\min\{\mathrm{OPT},d_k\beta_k\}.
 \tag{D8}
```

It is a structural target with an exact meaning; the cap is not an
unproven assertion about which players an optimum uses for small units.

## 5. Optimizing without knowing OPT or its deficit

The algorithm has the following explicit approximation guarantee:

```math
\boxed{\quad
 \text{output value}\ \ge
       \frac{\min\{\mathrm{OPT},d_k\beta_k\}}{d_k+\eta}
       \quad\text{in time (D5).}\quad}
 \tag{D9}
```

The exact branch gives T_k^*/d_k in 2^{O(k)} poly(H) time.
In particular, whenever

```math
\delta(\mathrm{OPT}/d_k)\le k,
 \tag{D10}
```

the full OPT/(d_k+eta) guarantee holds, even if the original selection
rank r and number q of potential players are large.

To implement target search, refine the common rational unit-value grid
by the denominator of d_k. Every configuration/integer optimum lies on
the original grid, and finite d_k beta_k lies on the refined grid.
Thus T_k^* is on a grid of polynomial encoding length. Start with zero
and a failed upper grid target: when beta_k is finite, any grid point
strictly above d_k beta_k fails the deficit cap; when k=r, let V be the
usual total delivered-value bound and use a grid target strictly above
(d_k+eta0)V, or above d_k V in the exact branch. Then the demanded
output value exceeds V and success is impossible. A target merely
above V is not sufficient for that conclusion, since an approximate
algorithm can succeed at a target above the original optimum.

At an intermediate grid target, either the cap fails, an inner failure
certifies infeasibility of the chosen comparator at T, or a basis
allocation of value at least T/(d_k+eta0) is returned. A failure excludes
T and all larger members of the **capped feasible target set**, because
both target feasibility and the deficit condition are monotone in T.
The successful targets of the algorithm need not be monotone.

Keep a successful lower endpoint and failed upper endpoint. At adjacent
grid points, soundness of failure implies the lower endpoint is at
least T_k^*. The saved output at that endpoint proves (D9). The number
of trials is polynomial in the numerical encoding, not in the value
range or the capacity count. When T_k^*=0, an arbitrary player basis
with empty bundles suffices.

This search never labels a mere failure of the deficit cap as original
allocation infeasibility. That distinction is essential for correctness.

## 6. Examples of the parameter interpretation

If all but at most k independent selected players can be covered by
one sufficiently valuable unit at threshold OPT/d_k, the nonlinear
runtime depends on k. The algorithm need not know which players are
the exceptions and does not enumerate q^k possible exception sets.

For k=1 and exact availability, d_1=1. The derived small matroid has
rank zero or one, so the procedure is polynomial and exact whenever
OPT<=beta_1. For k=2, d_2=5/2; for k=3, d_3=3. These are structural
guarantees under (D10), not claims that every rank-r instance has such
a small fat deficit.

The k=0 endpoint can be handled separately: maximize the bottleneck
value of a common M,N_theta basis. If one exists, a pure one-fat-unit
allocation is obtained in polynomial time. No formula containing 1/k
is used at zero.

A portfolio for k=1,...,K, together with the pure-fat endpoint, may
return the best output. Its time is at most an additional polynomial
factor times the k=K bound. This is optional; the theorem for a chosen
k already has the explicit guarantee (D9).

## 7. Scope of the refinement

This is a parameter and guarantee refinement of the reviewed factor-four
algorithm. It is not a faster general-graph matching algorithm, a claim
that every large-r allocation instance has small deficit, or an exact
solver for a general recipient-polymatroid target.

The ordinary Santa Claus parameterized scheme of
[Jansen and Maack, arXiv:1701.03263v2](https://arxiv.org/abs/1701.03263)
uses the number of valuation types, at most the number of players; it
does not by itself give (D5) with k much smaller than q for the resource
polymatroid model. Conversely, no exhaustive novelty claim for fat-deficit parameterization
is made here. The model, supplied oracles, comparator, and cap condition
must all be retained in comparisons.
