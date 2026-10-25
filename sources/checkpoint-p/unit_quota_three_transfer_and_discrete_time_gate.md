# Unit quotas, a factor-three transfer, and the discrete time boundary

**25 October 2026. New derived research theorem and scope audit.**

This note uses the normalized prefix construction proved in
`general_resource_prefix_additivity_four_candidate.md` and, for integer
recipient polymatroids, its block version in
`general_recipient_polymatroid_prefix_four_transfer.md`.
It records the exact integer calculation rather than treating a
quota-gap decision oracle as an automatically lossless approximation
wrapper.

The useful new guarantee is rank-sensitive: the player ground set may
contain q candidates while the required basis has rank r much smaller
than q. The exponential branch below is in r. It is not asserted to
improve the best all-player approximation available in time exponential
in q; Section 7 explains a stronger elementary baseline in that regime.

## 1. Equal small units sharpen the normalized cover

Consider the small-resource problem on a player matroid of rank r>=1.
Every service unit has the same positive rational value u. Recipient
constraints may be arbitrary integral polymatroids with binary-encoded
rank values. The initial proof in that full model uses integer optimum.
Section 4.1 proves the stronger comparison with the separately defined
residual-capacity configuration relaxation.
For ordinary one-service recipient matroids, the corresponding compact
or configuration-LP arguments remain available as specified in their
own notes.

Choose an integer quota b>=1 and bundle target B=b u. Every minimal
bundle contains exactly b service units. A fully normalized center
with its t designated blockers has the following current rank charge.

* For b=1, every bundle is a singleton unit. Current dependency saves
  the center's one rank increment, so the charge is at most t units.
* For b>=2 and t=1, current dependency saves at least one unit from
  the separate count of both bundles, giving at most 2b-1 units.
* For b>=2 and t>=2, counting all units gives at most (t+1)b units.
  Since (t-1)b>=t, this is at most t(2b-1).

Telescoping over ordered prefixes therefore gives

\[
                 \Phi\le (2b-1)u\,|Y|.
 \tag{U1}
\]

This saving uses the current normalized dependence. It is not a birth
charge carried through shrinking blocker groups.

## 2. The exact integer target condition

Suppose the integer optimum can supply a player basis with at least
k units each, where k>=1 is an integer. A complete failed available
scan at quota b has maximum available value at most (b-1)u for each
eligible player. The recipient-polymatroid contraction-loss lemma then
gives

\[
                 \Phi\ge(k-b+1)u\,w,
 \qquad w=r-|I\setminus\operatorname{owners}(Y_{<i})|.
 \tag{U2}
\]

The same non-strict lower bound follows directly from the fractional
cover proof in the one-service recipient-matroid model. Write
rho=(r-1)/r. At an empty last blocker layer, (U1) is at most
rho(2b-1)u w. Consequently the sufficient exact condition is

\[
 \boxed{\quad k-b+1>\rho(2b-1),\quad}
 \qquad\text{equivalently}\qquad
 (3-2/r)b<k+1+\rho.
 \tag{U3}
\]

The inequality is strict because (U2) is non-strict. It must not be
replaced by a non-strict inequality at this exact integer boundary.
Since multiplication by r makes both sides integral, the largest
certified integer quota is

\[
             b_r(k)=\left\lfloor
                       \frac{rk+2r-2}{3r-2}
                     \right\rfloor.
 \tag{U3a}
\]

Indeed, the strict condition is (3r-2)b<rk+2r-1, equivalent to
(3r-2)b<=rk+2r-2. This refinement is used in the finite-rank scheduling
curves in `two_size_makespan_private_slack_deficiency.md`.
Under (U3), the existing signature algorithm returns a b-unit basis,
or correctly certifies that no k-unit basis exists, in

\[
                       2^{O(r)}\operatorname{poly}(H).
 \tag{U4}
\]

All submodular minimization, numerical work, and binary count operations
are included in H. No number of expanded service units occurs in the
runtime.

## 3. An exact-boundary uniform factor three

Set b=ceil(k/3). Then (U3) holds for every finite r.
To check the only potentially tight residue, write k=3a+1. Then
b=a+1 and

\[
 (k-b+1)-\rho(2b-1)
       =(2a+1)(1-\rho)>0.
 \tag{U5}
\]

For k=3a and k=3a+2, the gap is larger. Thus the small-unit problem
has a deterministic factor-three algorithm in (U4). Its output is
the integer quantity ceil(k/3), not floor(k/3). Rank one is exact
with an exact available optimizer. The same condition gives factor
two at rank two by choosing b=ceil(k/2).

This is a genuinely discrete strengthening of a coarse condition
such as 3b<=k. It is precisely what is needed to avoid losing a full
unit when the optimum quota is small.

## 4. A fat-resource transfer with arbitrary player selection

Suppose resources have two positive intrinsic values u<=a, and consider
a target T>0. Recipient constraints may be arbitrary integral
polymatroids. Choose a basis of an arbitrary player matroid M, of
rank r, and compare against an integer allocation supplying value T.

Treat every a-valued resource as fat. The players that can receive
one permitted fat unit form a matroid N: for each resource restrict
its polymatroid to the unit box, then take their matroid union. Apply
the accepted dual-union reduction U=M* union N and solve on U*.
Its rank r' is at most r. The r'=0 case needs only the fat decomposition.

Every optimum player not supplied by a fat resource has an all-small
bundle with at least

\[
                         k=\lceil T/u\rceil
 \tag{U6}
\]

units. Therefore the derived small instance has the k-unit integer
promise. Run Section 3 and give its selected players b=ceil(k/3)
small units. Reverse the dual-union construction and keep the required
original player basis.

The small-supplied players obtain b u>=T/3. Fat-supplied players obtain
a. Hence, whenever

\[
                              T\le3a,
 \tag{U7}
\]

the result supplies at least T/3 to every output player, in
2^{O(r')}poly(H) time. The inner value b u is allowed to exceed a:
the final guarantee is min(a,b u), and (U7) is sufficient for that
minimum to be at least T/3.

The same target theorem holds when fat resources have different values
but all are at least T/3, and every remaining positive unit has common
value u. Local downward-closed count constraints can be retained if
the stated exact available optimizer and singleton tests are supplied.

For one-service recipient matroids, feasible all-small configurations
contain at least k units, so the accepted configuration-LP fat reduction
also supplies the integer-threshold fractional promise needed in (U2).
For general recipient polymatroids this argument first establishes
the integer comparison. The following corollary gives a stronger,
explicitly different LP comparator.

### 4.1 Residual-capacity configuration-LP corollary

Use the strengthened relaxation defined in
`recipient_polymatroid_residual_configuration_relaxation.md`, with
its valid residual-capacity cuts (L4). This is not the weaker aggregate
count-configuration LP, whose constant-factor gap claim is false.

At an actual algorithm reservation W_j, the basis-count construction
in that note gives a feasible reserved vector z^j whose residual
capacities equal the actual available counts A_pj and whose total
count is r_j(W_j). The corresponding residual cut bounds the expected
number of lost units of type j by r_j(W_j).

For exact available optimization at quota b, truncate each original
integer count configuration coordinatewise to its available counts.
Its surviving value is an integer multiple of u and is strictly below
b u, hence at most (b-1)u. Mixing configurations of player p gives
retained expected value at most (b-1)u x_p. If all configurations
have at least k units, summing their lost values over eligible players
and applying the residual cuts proves

\[
                     \Phi\ge(k-b+1)u\,x(E)
                               \ge(k-b+1)u\,w.
 \tag{U2R}
\]

This is exactly (U2), so the strict integer quota condition (U3),
the factor-three rank-exponential result, and the large-quota
rank-quasipolynomial results all hold against this strengthened LP.
Fat splitting preserves these cuts because it only deletes
configurations or decreases their nonnegative masses. An all-small
target-T configuration has at least ceil(T/u) units, so the rounded
target (U6) also retains the strengthened LP promise.

The same statement follows for supplied scaled-matroid components
from their component configuration relaxation, since those constraints
imply the residual cuts, as proved in the residual-relaxation note.
No polynomial separation or solution algorithm for all residual cuts
is asserted or used. The discrete small-quota time boundary in Section
6 is unchanged by this stronger comparator.

## 5. When the factor approaches three in rank-quasipolynomial time

Let 0<eta<=1, d=3-2/r, and select

\[
                       b=\left\lceil\frac{k}{d+\eta}\right\rceil.
 \tag{U8}
\]

The normalized cover coefficient is C=2b-1 units. Its slack is

\[
 \begin{split}
 \Delta&=k-b+1-\rho(2b-1)\\
       &=k+1+\rho-db\\
       &\ge\frac{k\eta}{d+\eta}-\rho.
 \end{split}
 \tag{U9}
\]

If

\[
                           k\ge\frac{2(d+\eta)}{\eta},
 \tag{U10}
\]

then Delta>=k eta/[2(d+eta)] and C<=3k/(d+eta), giving
Delta/C>=eta/6. The usual growth test may use gamma=eta/24.
This proves factor d+eta in

\[
 \operatorname{poly}(H)
 \min\{2^{O(r)},(r+1)^{O((1+\eta^{-1})\log(r+1))}\}
 \tag{U11}
\]

under the large-quota condition (U10). For the fat-resource transfer,
replace r by the derived rank r' and additionally require
a>=T/(d+eta).

For the simpler factor 3+eta corollary, use the explicitly different
quota b=ceil(k/(3+eta)). Since d<=3, its gap is at least
k eta/(3+eta)-rho, and the same argument gives growth Omega(eta)
whenever k>=2(3+eta)/eta. The resulting small-unit value is at least
T/(3+eta); thus the fat requirement is only a>=T/(3+eta).
A simple sufficient small-unit condition is u<=eta T/8, because
0<eta<=1 implies 2(3+eta)/eta<=8/eta. This is the quota used in
the fine-small-job scheduling transfer; it does not silently use the
stronger fat requirement belonging to d+eta.

This is a value-scale promise, not a hidden restriction on recipient
matroid rank, the number of players, or the number of resources.
It remains meaningful for arbitrary recipient polymatroids.

## 6. Why positive ratio error does not remove every small-quota case

At k=4 and required output b=2, the limiting coefficient in both
(U1) and (U2) is three units. The actual slack is

\[
                              \Delta=3/r.
 \tag{U12}
\]

For every eta<1, a factor 3+eta still requires two units when the
optimum has four. Thus this case cannot be rounded down to one unit,
and the existing growth proof provides only an O(1/r) growth parameter.
The exact-boundary signature proof still terminates in 2^{O(r)} time.

No uniform rank-quasipolynomial factor 3+eta follows from Sections
1--3 alone. In particular, replacing an integer quota oracle by the
informal phrase "find b or reject 3b" would hide a material rounding
and runtime issue. A separate algorithm for the critical small quotas,
or a new progress argument, is needed for that stronger claim.

## 7. All-player two-value wrappers and a stronger elementary baseline

If all q players are compulsory and there are no additional local
bundle constraints, Section 4 combines with a public rounding theorem
to give a uniform factor-three algorithm in 2^{O(q)}poly(H). For
T>3a, solve the ordinary assignment relaxation and apply Theorem 21
of Bamas, Lindermayr, Megow, Rohwedder and Schloeter: its integral
output has value at least T-a>T/3. An infeasible relaxation is a
sound failure certificate. The target-dependent branch T<=3a is
Section 4. Finite rational-grid search gives the optimization result.

However, **this all-player exponential-time corollary is not the main
improvement**. The same source's aggregation and rounding primitives
give the following stronger derived baseline. Fix 0<epsilon<1 and a
target T. Aggregate resources of each value into two integral
polymatroids P_small and P_big.

If a<=epsilon T, assignment-LP rounding yields value at least
(1-epsilon)T. Otherwise, trim any feasible target-T allocation so
each player's number of big units is at most ceil(T/a), which is at
most ceil(1/epsilon). Enumerate the vector z of these big counts.
There are at most (1+ceil(1/epsilon))^q choices. For each z, test

\[
 z\in P_{\rm big},\qquad
 \ell(z)\in P_{\rm small},\qquad
 \ell_p(z)=\max\left\{0,
          \left\lceil\frac{T-a z_p}{u}\right\rceil\right\}.
 \tag{U13}
\]

These are polynomial-time polymatroid membership tests by submodular
minimization. The tests are necessary and sufficient for the enumerated
big vector to admit a target-T allocation, because unused capacity is
permitted. Integral aggregate decompositions recover the original
resource allocations. This gives a (1-epsilon) value guarantee in

\[
                   (1+\epsilon^{-1})^{O(q)}\operatorname{poly}(H).
 \tag{U14}
\]

This baseline is a derivation here, not a theorem claimed to be printed
in that paper. It explains why a factor-three algorithm exponential
in the number of compulsory players should not be advertised as a
new approximation-quality breakthrough in that time regime.

By contrast, (U4) and (U11) depend on the **required player rank** r
or derived rank r', while q may be arbitrarily larger. Also, (U11)
has quasipolynomial rather than exponential rank dependence under its
explicit large-quota promise. Those distinctions are preserved in
the claims of this note.

## 8. Makespan implication and its proper scope

The public two-value polymatroid-duality reduction turns a genuine
factor-three all-player resource algorithm into a factor 5/3
job-matroid makespan algorithm with the corresponding runtime.
For a makespan target T and sizes p_1,p_2, cap each type's load count
by k_j=floor(T/p_j), check that this preserves its total rank, and
dualize with respect to k_j times the all-ones vector. If the original
target is feasible, the dual resource instance has minimum value at
least t=k_1 p_1+k_2 p_2-T. A resource value t/3 leaves load at most
T+2t/3<=5T/3. This is the argument of their Lemma 15 with alpha=3.

The unrestricted exponential-time corollary is again dominated by a
simple fixed-accuracy enumeration baseline. If the largest job size
a<=epsilon T, the public assignment rounding theorem gives makespan
at most (1+epsilon)T. Otherwise enumerate each machine's big-job
count in 0,...,floor(T/a). Test whether the vector is a big-job
polymatroid basis, and whether the small-job polymatroid has a basis
under the residual capacity bounds floor((T-a z_p)/u). Each test
uses polynomial submodular minimization and decomposition. This yields
(1+epsilon) in (1+epsilon^-1)^{O(q)}poly(H).

A rank-quasipolynomial 5/3-type transfer requires checking that every
dual resource target used by the reduction satisfies the explicit
large-quota and fat-value conditions from Section 5. It is not an
unconditional theorem for all two-value makespan inputs in this note.

## 9. Primary source and comparison

The public source used for the external primitives is:

* E. Bamas, A. Lindermayr, N. Megow, L. Rohwedder and J. Schloeter,
  *Santa Claus meets Makespan and Matroids: Algorithms and Reductions*,
  arXiv:2307.08453v1, 17 July 2023; SODA 2024.
  <https://arxiv.org/html/2307.08453v1>
  Proposition 9 gives aggregation by value; Theorem 21 gives additive
  loss at most the largest resource value; Theorem 23 gives the
  corresponding makespan rounding; Lemma 15 and Theorem 3 give the
  duality reduction. Theorem 4 states polynomial 8+epsilon for general
  values and polynomial 4+epsilon for two values.

The normalized prefix and unit-quota improvements above are separate
research derivations. No exhaustive novelty or publication-priority
claim is made. The rank-exponential and large-quota rank-quasipolynomial
branches must not be conflated, and the full recipient-polymatroid
result must retain its integer-optimum comparator.
