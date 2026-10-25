# Independent audit of the fat-cover deficit parameter

**25 October 2026. Review of `fat_deficiency_parameter_allocation.md`.**

This review checks the parameter identity, conditional target algorithm,
the computable cap, and one-sided optimization search. It finds no
unresolved mathematical gap in those claims, subject to the already
reviewed allocation and comparator interfaces imported in that note.
It is an internal mathematical review, not formal or external verification.

## 1. The rank identity is exact

Write U=M* union N, with q ground elements and player rank r. A common
independent set F of M and N extends to an M-basis I, and P-I is a
disjoint dual basis. Therefore r(U)>=q-r+|F|.

Conversely, decompose a U-basis into disjoint D union F with D dual
independent and F independent in N. Extending D to a dual basis D'
can delete at most q-r-|D| elements from F. The surviving F-D' is
contained in an M-basis and remains N-independent, so its size is at
least r(U)-(q-r). Thus

\[
                    r(U^*)=r-\nu(M,N).
\]

The argument is constructive using the same paid union decomposition
and dual extension operations as the allocation wrapper. It does not
require an additional unimplemented oracle.

## 2. All nonlinear state counts use the residual rank

For threshold theta, the inner player matroid is exactly U_theta*.
Once its rank delta is at most k, every inner partial matching,
selected-center count, blocker count, phase count, and signature bound
is bounded by k. The original rank r and ground size q remain in
polynomial oracle and reconstruction costs only.

At d_k=tau+3-3/k, theta=T/d_k, and B=T/(d_k+eta0), one has
B>=theta/2. The small unit maximum is below theta, so the reviewed
sharp cover is at most 3B. The gap calculation using delta<=k is
therefore at least eta0 B. The claimed rank-quasipolynomial exponent
and exact-boundary rank-exponential alternative follow with k as the
parameter. The delta=0 case requires no inner search.

## 3. The cap has the stated threshold semantics

The fat matroid only changes when theta crosses a supplied unit value.
Because fat membership uses value>=theta, every positive finite
supremum beta_k is attained. The union-rank identity proves that
delta(T/d_k)<=k is equivalent to T<=d_k beta_k, with the stated
zero and infinity conventions.

This is a maximum common-independent fat cover. It is not a guess
about which players an optimal multiunit allocation supplies by fat
units, and no such guess is needed.

## 4. The finite-grid search remains sound for fractional comparators

Integer allocation optima lie on the common rational unit-value grid.
The configuration-LP threshold optimum also lies on that grid, even
though its configuration masses can be fractional: feasible target
sets change only when the threshold crosses a value of an individual
configuration. There are finitely many configurations because all
counts are bounded by finite binary capacities. The same reasoning
applies to the separately retained component-configuration comparator.

Refining this grid by the denominator of the rational d_k places both
OPT and d_k beta_k on one grid of polynomial encoding length. Hence
their minimum is on that grid as claimed. The number of configurations
or numerical units need not be enumerated for this observation.

A cap failure only excludes the current target from the capped feasible
set; it is not labeled original allocation infeasibility. An inner
failure excludes original comparator feasibility. Both exclude all
larger capped-feasible targets. Algorithmic successes need not be
monotone, and the proof does not rely on them being monotone.

At adjacent successful and failed grid endpoints L<U, soundness of
failure puts the capped optimum strictly below U and hence at most L.
The saved allocation has value at least L/(d_k+eta0), proving the
stated optimization guarantee.

For an infinite cap, a failed upper target can be chosen explicitly
above (d_k+eta0)V, where V is the total available value bound; on
the exact branch choose above d_k V. This is stronger than merely
choosing above V, since an approximation procedure may legitimately
succeed at a target above OPT. The manuscript's reference to the
previous target-search bound should be read with this factor included.

## 5. Endpoint and interpretation checks

Rank zero and a zero capped optimum allow an empty allocation to a
chosen basis under downward closure. The k=0 pure-fat endpoint is a
separate bottleneck common-basis computation and never uses 1/k.
For k=1 with exact availability, the rank-zero or rank-one inner problem
is polynomial and exact under the cap condition. Larger k examples
are conditional structural guarantees, not universal statements about
all instances of the original rank.

The important distinction is retained throughout: the number of
exceptions to a one-fat-unit cover can be far smaller than either
the compulsory selection rank or the number of candidate players.
No q^k exception-set enumeration is used.
