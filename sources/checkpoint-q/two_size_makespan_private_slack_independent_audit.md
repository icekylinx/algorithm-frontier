# Independent audit of the private-slack rank-deficit scheduling refinement

**25 October 2026. Full review of D1--D23 passed, with the cap qualification stated below.**

This audit reviews
`two_size_makespan_private_slack_deficiency.md`. It accepts the displayed
private-coordinate reduction, capped target search, finite-rank quotas,
and fine-small-job consequences. These are internal mathematical reviews,
not external peer review or formal verification.

## 1. Private minimum marginals can be inserted without resource contraction

For sigma_p=f(P)-f(P minus {p}), diminishing returns gives every marginal
of adding p at least sigma_p. Thus f minus this modular vector remains
normalized, monotone, integral and submodular. For any set F_0, any
recipient vector y feasible on its complement, and any z on F_0 bounded
by sigma, adding F_0 coordinates one by one gives

\[
 f(S)\ge f(S\setminus F_0)+\sum_{p\in S\cap F_0}\sigma_p
                              \ge y(S\setminus F_0)+z(S\cap F_0).
\]

Hence y+z is feasible. This is a special property of minimum marginals;
it would not hold for arbitrary currently available units. The manuscript
uses precisely this property and does not assert free contraction for
arbitrary preassignments.

## 2. The full target promise survives contraction of only the player matroid

Take a maximum player-independent F_0 among machines with at least b
private units. Its size is r_M(F), so M/F_0 has rank delta=h-r_M(F).
Any unknown optimal player basis I* spans M and hence its image spans
the contraction. A contracted basis J can therefore be chosen from
I* minus F_0. Restricting the original K-unit allocation to J preserves
both its resource feasibility and its full K-unit quota.

The residual recipient object is only the restriction to P minus F_0.
The previous section permits adding b private units at every member of
F_0 after the residual algorithm. Thus F_0 need not belong to the
unknown optimal basis, and it need not have K private units. It only
needs the smaller output quota. Delta zero is handled by this insertion
alone, with no nonexistent rank-zero core search.

## 3. The scheduling parameter is explicit and monotone

For the small-job dual, direct evaluation gives

\[
 \sigma_p=c-g_s(\{p\})=c-\min\{c,f_s(\{p\})\}.
\]

Since b>=1, sigma_p>=b is exactly f_s({p})<=c-b. For
b=ceil((c-d)/3), elementary integer algebra gives
c-b=floor((2c+d)/3). Both c=floor(T/u) and d=floor((T-a)/u)
are nondecreasing in T. Thus F expands and delta decreases through
the hard interval, where the large Boolean matroid is fixed.

The rank-cap condition is correctly separate from original feasibility.
If its Boolean rank is below h, every target below 2a is genuinely
infeasible anyway, and the cap first holds at 2a. Accordingly, for
k>=h the cap places no additional restriction on **originally feasible**
targets. Taken literally without that qualification, the phrase
"no restriction beyond T>=a" would omit this Boolean-rank test.

## 4. Reconstruction and capped optimization are sound

A feasible target-T schedule gives K=c-floor((T-a)/u) dual units on
every large-job recipient. The private-coordinate reduction preserves
that K-unit promise on a player matroid of rank delta. Its output plus
the committed private units gives quota b to a full large-recipient
basis. Extending to a dual base and complementing preserves the original
small and large total ranks, hence gives an integral schedule.

Its hard-branch load is at most T+t-bu<=T+2t/3<=5T/3. The easy branch
has load at most 3T/2. A cap failure is only a failure of the requested
runtime parameter, while a rank or unit-core failure is a genuine
target infeasibility certificate.

The cap is upward closed and has an attained grid threshold Theta_k.
Its intersection with the originally feasible targets begins at
T*=max(OPT,Theta_k). Every rejected target is below T*: either it is
originally infeasible or it fails the monotone cap. Every success has
a returned schedule bounded by 5T/3. Thus the failed-lower/successful-
upper grid search proves 5T*/3 without requiring monotone algorithmic
success. All breakpoint and search arithmetic has polynomial bit length.

## 5. The finite-rank quota formulas are exact

The strict integer quota condition is
(3r-2)b<rK+2r-1. Its largest integer solution is exactly

\[
                 b_r(K)=\left\lfloor
                    \frac{rK+2r-2}{3r-2}\right\rfloor.
\]

A quota valid for rank k is also valid for the actual delta<=k,
because the coefficient rho is nondecreasing in the rank. The identity

\[
 c-b_k(c-d)=\left\lceil
       \frac{(2k-2)c+kd-2k+2}{3k-2}\right\rceil
\]

is correct, and its nonnegative coefficients preserve cap monotonicity.
The stronger quota needs its own threshold, as explicitly stated.

For k=1 the output quota is K; for k=2 it is ceil(K/2). The latter
gives the stated capped polynomial-time 3/2 scheduling guarantee.
For k>=3, K=3 still yields quota one; the example T=a=3u makes the
displayed bound reach 5T/3. This limits that certificate and does not
establish a lower bound against other algorithms.

The large-K estimate b_k(K)>(K-1)/(3-2/k) is also correct. Its derived
load contains the stated additive u/(3-2/k), which cannot be dropped
at small quotas.

## 6. Fine-small-job dependence uses the correct cap and rank

Under u<=eta T/18, the target K meets the existing large-quota threshold.
For b=ceil(K/(3+eta)), the identity
c-b=floor(((2+eta)c+d)/(3+eta)) makes the parameter cap monotone.
The core uses rank delta<=k and has relative growth Omega(eta), giving
the claimed minimum of the exponential and rank-quasipolynomial bounds.

Restricting optimization targets to T>=18u/eta is legitimate under the
stated promise on OPT; the initial preceding grid point remains below
the capped feasible threshold. The finite-k quota with denominator
3-2/k+eta has the same monotonicity because this denominator is at
least one. Its hard-branch ratio is combined with the unchanged easy
3/2 bound using a maximum, as required.

The result is a parameter and promise refinement. It does not solve
the unpromised critical small-quota time gate or imply a polynomial
5/3 approximation for arbitrary job-polymatroid instances.
