# Independent audit of the corank-sensitive global time curve

**25 October 2026. Full independent read of P1--P13 in
`global_gap_corank_profile_bound.md`.**

The refinement passes. It bounds the same streamed block algorithm by
E(q)*Psi_A(q,c)*poly(H), keeps polynomial space, and correctly combines
that guarantee with the original corank gap and complete-omission
enumeration. The proof does not assume an exact fixed-selected-set
optimizer, nor a favorable answer on unpromised extension calls.

## 1. The new local averaging identity is exact

For fixed n,p and any x>=0, the weights
binom(p,k)*x^k/(1+x)^p are nonnegative and sum to one. At x=0 their
meaning is the point mass on k=0. Multiplying by the original local
extension cost gives

\[
 w_k(x)T_{n,p}(k)
 =\left(\frac A{1+x}\right)^p
       \binom nk\left(\frac xA\right)^k.
\]

The truncated sum is bounded above by the complete nonnegative
binomial expansion. Hence the selected local minimum satisfies P5 for
every finite nonnegative x. This holds also at p=0 and p=n, with no
division by a zero binomial coefficient.

The algorithm still chooses the exact minimizer of T, independently of
x. It does not tune its choices using an unknown witness profile or an
analytical optimizer. A single minimum is at most every weighted average,
so all these inequalities apply to the same implemented local table.

## 2. The common x works for all profiles and all product choices

For a fixed profile, the complete Cartesian extension cost is the
product of its local cover sizes times A raised to the remaining
deficit. Applying the new local bound with one common x gives exactly

\[
 (\ell+2)^m
 \left(\frac A{1+x}\right)^{\sum_i p_i}
 \left(1+\frac xA\right)^{\sum_i n_i}
 =
 (\ell+2)^m
 \left(\frac A{1+x}\right)^c
 \left(1+\frac xA\right)^q.
\]

All profiles have the same totals c and q. Thus summing their already
bounded number preserves a common bound for every x. Taking the
infimum afterward is legitimate: the actual algorithm and its running
time have not changed. There is no interchange of an unknown profile
with an algorithmic minimization.

This accounting includes every Cartesian seed and every extension call,
including failed selectors and calls with no full-target witness.
Local precomputation and iterator overhead have the same bounds as in
the accepted global theorem. The refinement changes no stored object,
so its polynomial-space proof is unchanged.

## 3. The optimizer and closed form are correct at every stated endpoint

Taking a natural logarithm of the objective yields

\[
 L'(x)=-\frac c{1+x}+\frac q{A+x}.
\]

Its sign is the sign of (q-Ac)+(q-c)x. Because the theorem assumes
c<q, this affine numerator is increasing. If Ac<=q, the objective
is nondecreasing on x>=0 and its minimum is the x=0 value A^c.
If Ac>q, its unique minimum occurs at
x*=(Ac-q)/(q-c)>0.

At that point,

\[
 1+x^*=\frac{c(A-1)}{q-c},\qquad
 1+\frac{x^*}{A}=\frac{q(A-1)}{A(q-c)}.
\]

Substitution gives the second expression in P10:

\[
 \frac{q^q}{c^c(q-c)^{q-c}}
           \left(1-\frac1A\right)^{q-c}.
\]

At Ac=q this equals A^c, so the branches join without an extra factor.
At c=0, only the first branch is needed and its value is one. The
unforced extension then has zero deficit and is polynomial without
paying E(q). The excluded c=q case would concern an empty selected set
and is properly delegated to the application's separate convention;
P9 is not evaluated with a zero denominator.

For rational A, Ac<=q and x* have exact polynomial-bit comparisons.
Every exponent in the displayed rational closed form is at most q, so
the encoded integers have polynomial bit length. No numerical loop
proportional to A is introduced. In fact x and the closed form need
not be evaluated by the block algorithm at all.

## 4. The entropy curve and its maximum check

Writing rho=c/q transforms P10 into P11 exactly. This is an algebraic
expression for the real bound, not a Stirling replacement of an actual
binomial coefficient. On the nonlinear branch its derivative is

\[
 \log_2\frac{1-\rho}{\rho}
 -\log_2\left(1-\frac1A\right).
\]

At rho=1/A this equals log_2 A, matching the derivative of the linear
branch. The nonlinear branch is strictly concave. Its derivative is
zero at rho*=A/(2A-1), which lies strictly above 1/A for A>1. Evaluating
there gives log_2(2-1/A). Thus the stated whole-ground base is exactly
the maximum of this continuous corank bound.

For A=27/4, the transition 4/27, maximum point 27/50, and base 50/27
are correct. For A=4 the corresponding values are 1/4, 4/7, and 7/4.
The limit as rho approaches one is also consistent: the nonlinear
exponent approaches zero, while applications still exclude an actual
empty selected set or handle it separately.

## 5. Complete-omission enumeration needs only the given gap interface

Enumerate every c-element seed Z and invoke the original extension on
Q=P\Z. Its remaining deficit is exactly zero, so the stipulated
all-input bound is polynomial, including when no original full-target
witness exists on Q.

Every successful call returns a valid original relaxed solution. If a
full witness I* exists, its complement Z=P\I* appears in the enumeration
and the corresponding extension cannot fail. Hence total failure is
a sound full-target rejection. There are exactly binom(q,c) calls,
which can be generated with polynomial-space counters.

This does not require computing an exact optimum on a prescribed
selected set. In particular, the zero-deficit routine can still be a
genuine two-target gap with its original completion or routing witness.
P13 correctly explains this point instead of assuming a stronger
fixed-set primitive.

## 6. Combining the bounds preserves semantics and storage

The original corank routine, streamed block routine, and full-omission
enumeration all have the same valid gap output contract. Deterministic
dovetailing may stop when any one finishes, including with a sound
failure. A failure need not agree with another algorithm that could
find a relaxed solution above the full-target feasibility threshold;
both are permitted answers in that situation.

A constant number of polynomial workspaces is still polynomial. The
uniform polynomial overhead of interleaving computations changes no
displayed exponential term. Therefore the minimum of the three bounds
in P13 is justified without needing to evaluate hidden constants in
their polynomial factors or the entropy curve.

For fixed A, the usual whole-ground shorthand follows. For varying A,
the explicit E(q) bound remains the correct uniform statement. The
original requirements for representing the local comparisons continue
to apply: a supplied rational A, or the accepted exact comparisons for
fixed rational accuracy, suffices. This refinement creates no new
real-number oracle assumption.

## 7. Conclusion

All P1--P13 claims pass. The refinement is a sharper analysis of the
same polynomial-space block implementation. Its endpoints, all-input
costs, and zero-deficit fallback are correct, and its combination with
the original corank runtime avoids an unnecessary block overhead for
small corank. It changes neither the approximation guarantee nor the
original protected-witness interface.
