# Second independent audit: workload scheduling and finite-rank private slack

**25 October 2026. Independent mathematical review.**

This note reviews both `many_small_sizes_workload_makespan_transfer.md` and `many_small_sizes_private_slack_deficiency.md`, together with the direct rounding proof in `many_small_sizes_workload_independent_audit.md`. Both derivations pass. The main guarantees concern an actual integral schedule in the original job-polymatroid model. They retain an explicit additive term u, the largest job size smaller than the largest size a.

The general workload result is

\[
 C_{\max}\le \left(2-\frac1{3+\eta}\right)\mathrm{OPT}+u,
\]

with the nonpolynomial running time depending on the number h of largest-size units. The private-slack result is

\[
 C_{\max}\le \beta(D)\max\{\mathrm{OPT},\Theta_{k,D}\}+u,
 \qquad \beta(D)=\max\{3/2,2-1/D\},
\]

where D>=3-2/k and the cap threshold is explicitly defined and computed. For D=3-2/k+eta the engineered exact quota supplies a uniform relative growth margin, including small original job counts.

## 1. Per-machine rounding is sufficiently strong

The needed rounding statement preserves a separate fractional load bound at each machine, up to +u. A uniform makespan theorem alone would not justify it. The direct proof in the first audit does justify it for arbitrary integral job polymatroids and binary multiplicities.

For sizes p_1>=...>=p_m, put an element (p,j) for every machine/type pair. The direct-sum rank A is the sum of the type ranks. For each machine define

\[
 C_{p,j}=\left\lceil\sum_{\ell\le j}x_\ell(p)\right\rceil.
\]

These capacities are nondecreasing. The rank B on that machine is the maximum C_{p,j} among the selected type indices, and B is summed over machines. A maximum of nonnegative weights is submodular. Its polymatroid inequalities are exactly the cumulative-prefix bounds, because an arbitrary subset is contained in the prefix ending at its largest index.

The original fractional type bases belong to both polymatroids and attain the full direct-sum rank. Integral polymatroid intersection therefore produces integer type bases with these prefix bounds. Telescoping by the nonnegative differences p_j-p_{j+1} bounds the load increase at each machine by p_1<=u. The argument does not require equal starting loads, uniform residual capacities, or explicit job copies. The ground set has q times m elements, and all cumulative capacities have polynomial bit length.

This also agrees with the per-machine calculation in the primary source, Bamas et al., [Theorem 23 and its proof](https://arxiv.org/html/2307.08453v1). The audit relies on the explicit construction above, so the stronger interface is not inferred merely from the theorem's uniform makespan wording.

## 2. Workload aggregation, capping, and decomposition are consistent

Choose a rational unit Delta dividing every original size, and set m_j=p_j/Delta for smaller jobs. The workload rank F=sum_j m_j f_j is an integral polymatroid. Its rank query is a binary weighted sum of original rank queries. No step expands m_j copies.

At a target T with c=T/Delta integral, capping the workload by c per machine gives an integral capped rank G. An original feasible schedule supplies an integer base of F within this cap, so a total-rank loss G(P)<F(P) is a sound infeasibility certificate. In the branch T<2a the largest class similarly requires a Boolean base of cardinality h; a rank loss under the unit box is also sound.

The complement rank

\[
                  f(S)=c|S|+G(P\setminus S)-G(P)
\]

is the usual integral polymatroid dual with respect to the box c. Extending a dual independent vector to an integer base and complementing gives an integer base of G. Because the cap retained total rank, this is also a base of F.

Integral decomposition into bases of m_j f_j is the correct reconstruction step. Dividing the jth component by m_j yields a fractional base of f_j; it need not yield an integer base. The workload identity sum_j p_j x_j(p)=Delta w_p is exact. Applying the per-machine rounding lemma only to these smaller jobs restores all original constraints and pays precisely +u. The largest assignment remains integral throughout. Same-size components can be recovered by a further ordinary integral decomposition.

## 3. The large workload quota is a valid promise

For any true target-T schedule in the hard branch, a largest-job recipient has workload at most (T-a)/Delta. Its complement therefore contains at least K=a/Delta units. The recipients form a basis of the Boolean largest-job matroid, so the allocation core has exactly the claimed K-unit promise at player rank h.

In the first workload note, Delta=g/ceil(18/eta), with g a common original size quantum. Consequently K>=18/eta>=2(3+eta)/eta for 0<eta<=1. This meets the previously proved large-quota condition. Taking b=ceil(K/(3+eta)) leaves load at most T+(1-1/(3+eta))a+u on a largest-job machine, bounded by (2-1/(3+eta))T+u because a<=T. Other machines have load at most T+u. The easy branch T>=2a has load at most T+a<=3T/2.

This refinement changes the divisible workload model used internally. It does not solve the original small indivisible-quota gate without loss: the +u rounding payment is still present in the final original schedule.

## 4. The private coordinate calculation is exact

For the capped workload rank,

\[
 G(\{p\})=\min\{c,F(\{p\})\}.
\]

Thus the private marginal of the complement rank is

\[
 \sigma_p=f(P)-f(P\setminus\{p\})
          =c-\min\{c,F(\{p\})\}.
\]

When b>=1, sigma_p>=b holds exactly when F({p})<=c-b. Multiplying by Delta gives the displayed private set

\[
        F_D(T)=\{p:W_p\le T-a/D\},
 \qquad W_p=\sum_{j:p_j<a}p_j f_j(\{p\}),
\]

provided b Delta=a/D. There is no missing floor or ceiling in this equivalence.

Choose a largest independent subset F_0 of this private set. Contract only the player matroid and restrict the recipient ground set. An originally feasible largest-job basis spans the contraction; some subset of its members outside F_0 is a contracted basis and retains the full K allocation. The residual problem therefore has rank delta=h-r_M(F_D(T)) and the full K-unit promise.

The private insertion lemma safely combines any residual feasible vector with b units on each member of F_0, since every context marginal at p is at least sigma_p. Resource contraction would be a different operation and is correctly absent. For residual rank zero, private insertion alone completes the construction.

## 5. Engineering an exact quota removes the numerical gate in this model

Write the desired rational divisor as D=A/B and let g divide every original size. Taking Delta=g/A gives

\[
             K=a/\Delta=A_0 A,
       \qquad b=K/D=A_0 B,
       \qquad a=A_0g.
\]

Both K and b are positive integers. All smaller weights p_j/Delta are integer and have polynomial encoding length. The denominator/numerator magnitudes are never enumerated. For D_k=3-2/k the unreduced numerator 3k-2 is equally valid for this purpose.

For actual residual rank 1<=r<=k, the unit-quota condition is

\[
                   (3-2/r)b<K+1+(r-1)/r.
\]

Since 3-2/r<=D_k<=D and Db=K, its left side is at most K; the condition is strictly satisfied. For D=D_k+eta, its exact slack Gamma obeys

\[
 \Gamma=(D-(3-2/r))b+1+(r-1)/r
                \ge\eta b+1+(r-1)/r.
\]

The cover coefficient is 2b-1, so Gamma/(2b-1)>eta/2. This directly supplies the uniform growth margin without requiring a separate lower bound on K. No arbitrary original integer quota has been rounded in this calculation; the artificial workload unit was chosen to make Db=K exact. This distinction is necessary for correctness.

## 6. The cap threshold and the target grid match exactly

Throughout a<=T<2a, the largest-job Boolean matroid is fixed. The set F_D(T) grows with T, so its rank deficiency is nonincreasing. If its total rank is h and k<h, define lambda_k as the first singleton-workload threshold at which rank h-k is reached. Sorting W_p and evaluating matroid rank computes this threshold in polynomial time. The first target passing the cap is

\[
       \Theta_{k,D}=\min\{2a,\max\{a,\lambda_k+a/D\}\}.
\]

If k>=h the threshold is a. If the Boolean rank is smaller than h, the threshold is 2a; in that case every original schedule already has makespan at least 2a, so this convention does not exclude any smaller feasible target.

Each W_p and each original schedule load belongs to the g-grid. Since a/D=b Delta and g=A Delta, the displayed threshold is attained on the Delta-grid. In particular, OPT and max{OPT,Theta} are on the same search grid. Every original rank, artificial workload rank, derived cap, and target has polynomial bit length, even if its numerical value is large.

A cap failure excludes capped feasible targets at most T; it is not an original infeasibility certificate. An original rank/core/LP failure excludes original feasible targets at most T. With a failed lower endpoint and a successful upper endpoint, adjacent-grid termination gives a successful trial target at most max{OPT,Theta}, even if successful outputs are not monotone. This is the correct one-sided search direction. An arbitrary feasible original assignment supplies a sufficient upper endpoint after also taking the maximum with 2a.

## 7. Coefficients, runtimes, and limits

On largest-job machines the reconstructed schedule has load at most

\[
       T+(1-1/D)a+u\le(2-1/D)T+u.
\]

The inequality uses D>=1. Combining it with the easy-branch 3T/2 gives beta(D)T+u. The finite-rank values are therefore correct: k=1 and k=2 give beta=3/2, k=3 gives 11/7, and k=4 gives 8/5. For k>=2 the exact expression is (5k-4)/(3k-2).

All nonpolynomial allocation work is on residual rank at most k, with ordinary 2^{O(k)} time at D_k and the previously established rank-quasipolynomial alternative at D_k+eta. Polynomial outer work includes the artificial scaling, paid rank/SFM operations, decomposition, rounding, and the number of target trials. The same statements with k=h need no additional private-slack assumption on originally feasible targets.

These are additive or conditional multiplicative guarantees. Removing +u, or asserting a uniform ratio below two without a size gap, would exceed this proof. The comparison with public polynomial two-approximation for arbitrary job polymatroids is the appropriate general-many-values comparison; a public two-value 7/4+epsilon theorem is not a many-values baseline.

No gap was found in the numerical scaling, rounding interface, core promise, rank parameter, or target optimization. This is an independent internal mathematical review, not an implementation, formal verification, external peer review, or exhaustive novelty determination.
