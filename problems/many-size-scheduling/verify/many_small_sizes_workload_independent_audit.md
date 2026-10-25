# Verification note

**Curated source path:** `sources/checkpoint-o/many_small_sizes_workload_independent_audit.md`

The source audit follows.

# Independent audit of the many-small-sizes workload transfer

**25 October 2026. Independent internal mathematical review.**

This audit concerns `many_small_sizes_workload_makespan_transfer.md`.
The reviewed conclusion is an actual integral schedule of load at most
(2-1/(3+eta)) OPT+u, where all largest job units have one common size a,
u is the largest smaller size, and the nonlinear runtime depends on
the total number h of largest units. The smaller jobs may have
arbitrarily many sizes and arbitrary integral job-polymatroid constraints.

The proof passes. The additive u is essential to the argument: artificial
workload refinement produces fractional assignments of original smaller
jobs, and their final integral rounding pays this term. This audit gives
an independent construction of the per-machine rounding interface, as
well as checking scaling, decomposition, the target promise and search.

## 1. A direct proof of per-machine additive rounding

Let the smaller job types have sizes p_1>=...>=p_m>0 and integral
polymatroid ranks f_1,...,f_m. Let x_j be any fractional base of f_j.
Use the polynomial-size ground set of pairs E=P times {1,...,m}.
The first polymatroid is the direct sum of the job polymatroids:

\[
                    A(S)=\sum_{j=1}^m f_j(S_j),
 \qquad S_j=\{p:(p,j)\in S\}.
 \tag{A1}
\]

For each machine p, define integer cumulative capacities

\[
             C_{p,j}=\left\lceil\sum_{\ell=1}^j x_\ell(p)\right\rceil,
 \qquad C_{p,0}=0.
 \tag{A2}
\]

These capacities are nondecreasing in j. The second polymatroid has
rank

\[
                 B(S)=\sum_{p\in P}
                      \max\{C_{p,j}:(p,j)\in S\},
 \tag{A3}
\]

where an empty maximum is zero. A maximum of nonnegative element
weights is normalized, monotone and submodular; summing over machines
preserves these properties. Equivalently, P(B) is defined by the
nested per-machine constraints

\[
                      \sum_{\ell=1}^j y_\ell(p)\le C_{p,j}.
 \tag{A4}
\]

One implication follows by applying the rank inequality to each prefix.
For the other, any subset of one machine's types is contained in the
prefix ending at its largest index, whose capacity equals its rank in
(A3). Summing over machines gives every B-rank inequality.

The original fractional x belongs to both P(A) and P(B), with total
count R=sum_j f_j(P). Integral polymatroid intersection therefore
finds an integral common independent vector of count R. As A(E)=R,
its component y_j has y_j(P)=f_j(P) for every j, so every component
is an integer base of its original job polymatroid.

Set p_(m+1)=0. Telescoping at each individual machine gives

\[
 \begin{split}
 \sum_jp_jy_j(p)
   &=\sum_{j=1}^m(p_j-p_{j+1})
                        \sum_{\ell=1}^j y_\ell(p)\\
   &\le\sum_{j=1}^m(p_j-p_{j+1})C_{p,j}\\
   &\le\sum_jp_jx_j(p)+p_1.
 \end{split}
 \tag{A5}
\]

Thus the additive rounding guarantee holds separately for every
machine, for arbitrary unequal starting loads. All capacities are
binary encoded; the ground set has q*m pairs, with no job-copy
expansion. The construction pays the standard deterministic integral
polymatroid-intersection primitive.

This matches the checked per-machine Delta_i calculation in the proof
of Bamas et al., Theorem 23:
<https://arxiv.org/html/2307.08453v1>.
The displayed theorem's uniform makespan phrasing alone would not
justify arbitrary residual-load claims; the proof above supplies the
precise stronger interface used here.

## 2. Workload scaling is polynomial in binary input length

Take a rational g=1/Q dividing all original sizes, where Q can be the
product of their denominators. Its binary length is the sum of those
denominator lengths. With L=ceil(18/eta) and Delta=g/L, every
m_j=p_j/Delta is a positive integer of polynomial bit length.

The function F=sum_j m_j f_j is an integral polymatroid rank. Its
evaluation is a polynomial number of original rank queries and binary
arithmetic operations. Each weighted rank and total workload has
polynomial encoding length even if its numerical value is large.
The algebraic scaling does not require a list of m_j job copies.

For a target on the original g-grid, c=T/Delta is integral. This
is why the quota in the hard scheduling branch is exactly K=a/Delta;
there is no hidden floor error in that identity.

## 3. The integer target promise and large quota are valid

When T<2a, an original feasible schedule has at most one largest
unit per machine. Hence the unit-box cap of the largest-job polymatroid
must preserve its total rank h. A feasible schedule's aggregated
small workload is an integer base of F and obeys the coordinate cap c.
The cap must therefore preserve F(P) as well. Either rank loss is a
sound original infeasibility certificate.

Dualizing the capped workload gives rank
barG(S)=c|S|+G(P\\S)-G(P). The complement of the actual workload
base has at least a/Delta units on the largest-job recipient basis.
This basis has player rank h. Since a/g is a positive integer,

\[
                    K=a/\Delta\ge18/\eta
                                      \ge2(3+\eta)/\eta.
\]

The large-quota theorem therefore applies with b=ceil(K/(3+eta)),
including its Omega(eta) relative growth and stated rank-dependent
runtime. This only proves a unit-workload promise; the note correctly
does not identify such units with indivisible original jobs.

## 4. Base decomposition and final rounding preserve all original jobs

Extend the output dual allocation to an integral dual base, then
complement to a base w of the capped workload polymatroid. The full-rank
cap check makes w a base of F. Integral Minkowski decomposition gives
integer bases w^j of m_j f_j with sum w^j=w. Every x_j=w^j/m_j
is a fractional base of f_j, and

\[
                        \sum_j p_jx_j(p)=\Delta w_p.
\]

The decomposition step is allowed to return integer workload counts
not divisible by m_j. These give fractional original counts and are
exactly why the separate rounding step is needed.

Round these smaller-job bases by Section 1 while leaving the largest
allocation fixed. On a selected largest-job machine, the load is at
most T+a-a/(3+eta)+u. Since a<=T in the hard branch, this is at most
(2-1/(3+eta))T+u. Other machines have load at most T+u. Original
polymatroid constraints remain true for every type, and any same-size
aggregation can be decomposed again into original components.

## 5. Easy branch, optimization and model boundaries

For T>=2a, additive rounding all jobs gives T+a<=3T/2, within the
claimed target bound. The full original optimum is at least a when
the largest class has positive rank. The public additive algorithm
also supplies the independent upper guarantee 2 OPT; taking the
better of two explicit schedules justifies the stated minimum.

Every actual integral load lies on the original g-grid. Failures of
the target oracle are sound original infeasibility certificates,
while a success returns an explicit integral schedule. The finite
one-sided binary search therefore gives the stated optimized bound
without assuming monotonicity of successful targets. Its number of
trials is polynomial in the binary range of target indices.

The one-size and empty-type cases are explicitly separated. For
arbitrary-many-values scheduling, the comparison is to the public
general two-approximation. The public two-value 7/4+epsilon result
does not establish the same baseline for this larger model.

## 6. Review outcome

No gap was found in W1--W14 or in their runtime parameter. The proof
delivers an actual schedule against integer OPT, with explicit additive
u, and can use a deliberately fine conceptual workload unit because
the final per-machine rounding is separately paid. The private-slack
contraction from `two_size_makespan_private_slack_deficiency.md` also
applies to the dual workload polymatroid and can further reduce the
player rank; that extension should state its own cap threshold and
search grid.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
