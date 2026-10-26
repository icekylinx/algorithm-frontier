# Proof of barrier-parameter cone sparsification

Yilin Liu and GPT-6 Astra Pro — research manuscript reading map, 2026-10-26.

The complete typeset mathematical argument is the canonical [editable TeX manuscript](manuscripts/self_concordant_sparsification.tex). This page explains the proof chain and the precise scope of each external input without replacing the derivations in the manuscript. The argument proves an existence bound and supplies an oracle-randomized realization under additional computational assumptions.

## 1. Setup and directional inequality

Let K be a proper cone in a finite-dimensional real vector space of positive dimension, with a standard logarithmically homogeneous self-concordant barrier phi having parameter nu. The cone order x <=_K y means y-x belongs to K. Every v_i belongs to K, and e is their sum; e need not be interior. The radial restriction of self-concordance implies nu >= 1, although nu need not be integral.

For x in the interior of K and u in K, the barrier satisfies the directional bound

`-D phi(x)[u] >= sqrt(D^2 phi(x)[u,u])`.

This is a standard barrier fact; the manuscript proves it by combining logarithmic homogeneity and convexity to show D phi(x)[u] <= 0, then integrating the one-dimensional self-concordance bound on the ray x + t u. This step does not assume pairwise-self-concordance. Boundary directions u are handled by continuity.

## 2. The new potential

Set H(x)=exp(-phi(x)) on the interior of K and H(x)=0 elsewhere. The barrier blow-up and positive homogeneity imply that H is continuous and nonnegative on the whole ambient space and positively homogeneous of degree nu.

For u in K and interior x, differentiate twice in direction u. The formula

`D^2 H(x)[u,u] = H(x) ( (D phi(x)[u])^2 - D^2 phi(x)[u,u] )`

is nonnegative by the directional barrier inequality. The first derivative is also nonnegative. Along an affine line in a cone direction, the interior interval is upward closed. At any finite left endpoint H tends to zero, so extending the increasing convex restriction by zero keeps it convex. Therefore H is convex on every line whose direction lies in K.

Consequently the function f(t)=H(sum_i t_i v_i) is separately convex in the coefficients. This is the bridge between the barrier and the separate-convexity tools.

## 3. Uniform positivity, including boundary sums

Reis and Rothvoss, Lemma 18, lower-bounds the fraction of Boolean signs at which a nonnegative nonzero separately convex homogeneous function is positive: at least exp(-2nu) in the present setting. The original statement has integer degree; its hypercontractive proof depends algebraically on the degree and works for every positive real value. The manuscript spells out this extension.

If e belongs to the interior, f is nonzero at the all-positive vertex, so the imported lemma immediately gives the positivity estimate for a random sign sum. If e is on the boundary, replace each v_i by v_i + eta a for one fixed interior a. Apply the bound for eta > 0, then use the fact that K is closed and there are only finitely many sign configurations. The limiting event is membership in the closed cone, not necessarily the interior; this distinction is essential. Conditioning independent symmetric real coefficients on their magnitudes reduces the general distribution to the sign case. No moment assumption is needed.

Thus for every sublist and for arbitrary independent symmetric coefficients X_i, the probability that sum_i X_i v_i is in K is at least exp(-2nu).

## 4. Coordinate-section volume and symmetrization

Fix delta in (0,1/2]. Consider the coefficient body A consisting of x in [-1,1]^m such that delta e + sum_i x_i v_i belongs to K. The whole cube [-delta,delta]^m lies in A because it gives a nonnegative combination of v_i. In particular A has full coefficient-space dimension even if e or its summands are on a proper face of K.

For every coordinate subset S, the uniform positivity theorem applied only to S, followed by adding delta e in K, gives a section-volume fraction at least exp(-2nu). Reis and Rothvoss, Theorem 22, then guarantees the absolute volume lower bound 2^(-5m) for the symmetric body A intersect (-A), whenever m is at least (2nu / log 2)/delta^2.

The symmetric body is exactly the set of coefficient vectors producing an additive cone-order error between -delta e and +delta e. Reis and Rothvoss, Theorem 7, supplies a partial coloring in a constant dilation of this body, saturating at least half the coordinates. One of the coloring and its negation sets at least a quarter of all coordinates to -1, while retaining the same two-sided error bound.

## 5. Multiplicative iteration and support

Start with all weights equal to one. At a stage with m_t active terms, choose delta_t proportional to sqrt(nu/m_t), and apply the preceding partial coloring to the currently weighted vectors. Update each nonnegative weight by multiplication with 1+x_i, where x_i is the signed coloring coordinate. At least one quarter of the currently nonzero weights becomes zero, so m_(t+1) <= 3m_t/4.

The new vector sum lies in cone order between (1-s delta_t) and (1+s delta_t) times the previous sum, for an absolute constant s from partial coloring. Stop at C nu/epsilon^2 active terms. The chosen constant C ensures delta_t <= 1/2 and makes the stage errors, read backwards, form a geometrically decaying sequence with total at most epsilon/2. Since each lower multiplicative factor is positive, the cone-order sandwiches compose. Elementary product estimates give the final factors 1-epsilon and 1+epsilon. There is no need to move boundary sums into the interior at any stage.

This is a complete structural proof relative to the three imported geometric results; it does not claim that the partial-coloring theorem or a generic barrier oracle was developed here.

## 6. Corollaries, algorithms and limits

Dualizing the standard barrier preserves the parameter nu and gives the same support for K*. This yields a linear-in-degree result for duals of degree-d hyperbolicity cones. The standard (k+1)-parameter barrier on the spectral-norm epigraph transfers by duality to the nuclear-norm epigraph. Face and lift results follow by preserving cone order under the corresponding linear maps; the proof treats the correct face order and does not require the lift to intersect the cone interior.

The mathematical assertion is existential. A randomized construction follows only if the symmetric coefficient body has an ideal strong separation oracle and a valid parameter upper bound is supplied. In particular, existence of an abstract small barrier does not automatically furnish a polynomial-bit oracle implementation for any representation of K. The literature comparison is with Saunderson's general quadratic parameter bound, not with his stronger numerical constant under pairwise-self-concordance. No universal historical novelty, publication or formal verification is asserted.

For detailed hypotheses, constants and the full arguments for every corollary, read the [source TeX](manuscripts/self_concordant_sparsification.tex). For bibliographic attribution read [sources.md](sources.md) and for the limits of the supplied checks read [verify/README.md](verify/README.md).
