# Verification note

**Curated source path:** `sources/checkpoint-o/general_value_matroid_selection_near_two_independent_audit.md`

The source audit follows.

# Independent audit: near-two general-value allocation with an arbitrary player matroid

**25 October 2026. Full review of J1--J17 passed after three presentation clarifications.**

Reviewed manuscript:
`general_value_matroid_selection_near_two.md`.
The additive workload theorem used by this adapter was independently
reviewed in `corank_arbitrary_value_additive_independent_audit.md`.
This note checks the different structural issue in the adapter:
preserving a prescribed light-player basis while completing it with
heavy resource units inside the original player matroid.

## 1. The claimed parameter is the correct one

The theorem uses K_theta=(M* vee N_theta)*, where N_theta is the
Boolean cap of the aggregate heavy resource. Its nonlinear
parameter is the corank of K_theta after deleting K_theta-loops.
It is not generally the corank of M alone. The manuscript states
this distinction both at the start and in the theorem's scope.

The rank identity

\[
                 r(K_\theta)=r(M)-\nu(M,N_\theta)
\]

is valid. A common independent F extends to an M-basis, whose
complement together with F is union independent, proving one
inequality. In the reverse direction, decompose a union basis as
C disjoint-union D, extend C to an M*-basis C', and retain D\C'.
At most r(M*)-|C| elements of D are lost. The retained set is
N-independent and contained in the M-basis P\C', giving the
opposite inequality. This proof does not assume that the original
union decomposition already gives a full M* component.

Consequently the upper parameter bounds by original corank plus
nu(M,N), and then by original corank plus rank(N), are sound.
For free M, K=N*, and removing the dual loops gives precisely
rank(N) minus the number of N-coloops. The note does not require
the refined parameter to be monotone in the threshold.

## 2. The union-basis spanning step is complete

Let S be a basis of U=M* vee N and S=C disjoint-union D a union
decomposition. If S did not span M*, choose e outside the M*-closure
of S. Necessarily e lies outside S and also outside the closure of
C. Then C+e is M*-independent, so S+e is union independent with
components C+e and D. This contradicts maximality of S.

Therefore S spans M*. Matroid augmentation extends C to an M*-basis
C' using only S. For I=P\S, the complement B=P\C' is an M-basis
containing I, while

\[
                         B\setminus I=S\setminus C'\subseteq D
\]

is N-independent. The containment C' subseteq S is essential, and
the proof supplies it. An unrestricted extension in P would not
have established this preservation property.

The same construction handles rank(K)=0 with I empty and S=P.
It gives a full original M-basis covered by heavy units, rather
than calling a positive-rank light algorithm on an empty basis.

## 3. The original optimum supplies the right light promise

In any original target-T allocation on an M-basis B*, let R be its
selected players receiving at least one heavy unit. Keeping one
such unit at each player proves that R is N-independent. Its
light-only players L=B*\R have complement

\[
                          P\setminus L=(P\setminus B^*)\dot\cup R,
\]

which is U-independent. Extending that complement to a U-basis
produces a K-basis I* contained in L. Every player in I* retains
the original target value using only light resources. Restricting
light resources to the nonloop ground of K preserves that witness.

This proves the required light optimum comparison without assuming
that all light-only players themselves form a basis, and without
guessing the original optimum's heavy allocation.

## 4. Split enumeration, reconstruction and the constant

All distinct heavy/light splits are enumerated by value classes,
including empty sides. The split at the existential optimum
threshold is therefore among them, with equality on the heavy
side. Splits exceeding the budget are skipped without an
infeasibility assertion. Pure-heavy rank-zero splits are handled
in polynomial time.

For every processed positive-rank split, the additive algorithm
returns a K-basis I of light value at least
(1-epsilon)OPT_L-u_L. The union-basis completion produces an
original M-basis containing I and a heavy-independent complement.
Integral aggregate decomposition assigns exactly one heavy unit to
each member of that complement. Since the heavy and light types
are disjoint and there are no cross-type local constraints, the two
allocations combine without disturbing either guarantee.

At theta*=(1-epsilon)OPT/2, the light promise gives OPT_L>=OPT
and the strict split gives u_L<theta*. The light output therefore
exceeds theta*, while every heavy unit is worth at least theta*.
This proves the factor 2/(1-epsilon), equivalently 2+eta after
epsilon=eta/(2+eta). The correct parameter condition is exactly
c(OPT/(2+eta))<=k.

The no-heavy case reduces to the original player matroid and only
uses the light output. The no-light positive-rank case can return a
legal zero-value candidate. Neither causes an invalid positive
guarantee. For OPT=0, nonnegativity already proves the approximation
claim and no parameter at the undefined positive threshold zero is
needed; this clarification has been inserted in the manuscript.

## 5. The fallback for arbitrary original player selection

The dummy-resource construction correctly transfers the public
compulsory-player constant to the original-M model. Its value V+g
is larger than the total original resource value and hence larger
than the original optimum. Its recipient matroid is M*.

For the witness direction, first extend every original independent
resource vector to a full base on the original fixed ground. This
preserves every selected player's utility and fits the public
base-assignment model. Then assign one dummy unit to each player
outside the optimum M-basis. All players have value at least OPT.
The manuscript now makes this base-extension step explicit.

In any returned compulsory allocation, dummy recipients form an
M*-independent set D. Extend D to an M*-basis D', and take
B=P\D'. Every player in B received no dummy unit and keeps its
full guaranteed value from original resources alone. Removing
dummy units and discarding counts outside B is therefore safe.
The resulting fallback value is at least OPT/(8+zeta) for fixed
zeta>0. The primary public statement used here is Bamas et al.,
arXiv:2307.08453v1, Theorem 4, checked directly:
<https://arxiv.org/html/2307.08453v1>.

Both fallback and new split outputs are explicit feasible
allocations. Comparing their actual values preserves every
applicable guarantee. A skipped split is never misreported as an
original infeasibility certificate.

## 6. Runtime, numerical details, and limits

Boolean caps, matroid duals and unions, union decomposition and
within-S extension all have paid polynomial oracle implementations.
The inner workload multipliers and targets are integral after
exact rational scaling, and the ratio t/(t-b)=1/epsilon is fixed
for the entire split. No numerical supply expansion is needed.
The number of splits and one-sided target trials is polynomial.
Each processed corank is at most k, proving the stated
Gamma(1/epsilon)^k poly(H) time and polynomial workspace.

The proof retains arbitrary original player matroids and arbitrary
recipient polymatroids. It requires common intrinsic values and
independent resource-type feasibility constraints. It does not
prove a general-value result at eta=0, does not use original corank
alone as the parameter, and does not assert a configuration-LP
comparator. These limitations are correctly stated.

The final lower-bound discussion now says **strictly below** factor
two, resolving a potentially misleading earlier phrase about an
"exact factor two" lower bound. A separate alignment is required
for any lower bound in this threshold-derived parameter; it is not
inferred from the older unit-corank construction by terminology.

With the three clarifications above incorporated, no mathematical
gap remains in J1--J17 from this independent review.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
