# Second audit: rank reduction, target caps and deficit-parameter guarantees

**25 October 2026. Separate review by the recipient-polymatroid analysis
agent. This note records its own derivation, not a duplicate of the first
independent audit. The mathematical claim passes.**

The object checked is `fat_deficiency_parameter_allocation.md`, with
special attention to whether a large original player matroid can really
be removed from the nonlinear runtime, and whether the target cap can
be searched without falsely certifying infeasibility.

## 1. Why the derived rank is the correct exception count

Write U=M* vee N for the union with the current fat matroid. The largest
fat-covered set extendible to an original M-basis is a common independent
set F of M and N. Extending F to an M-basis gives a disjoint union of
F with a dual basis, so r(U)>=q-r+|F|.

In the other direction, let a U-basis decompose into D disjoint-union F,
with D independent in M* and F independent in N. Extending D to a full
dual basis consumes at most q-r-|D| elements of F. All remaining F
elements belong to the complementary M-basis. Hence a common independent
set has size at least r(U)-(q-r). This proves exactly

\[
              r(U^*)=q-r(U)=r-\nu(M,N).
\]

Thus the parameter is an intrinsic maximum-cover deficit, not a guessed
exception set or an input promise with an unimplemented recognition task.
The existing polynomial union/decomposition operations compute it.

## 2. Where the original rank still enters

The original M and its dual still occur in rank queries, fat unions and
the final reconstruction. Those operations are charged to the polynomial
input factor. The small search uses U*, whose rank is delta. Every
current small matching has fewer than delta records, every blocker group
uses one of those records, and every selected center is charged to a
nonempty group after normalization. Consequently all signature counts
and augmentation phases are controlled by delta, not by r.

This distinguishes the claimed parameter dependence from an algorithm
that guesses k exceptional players among q potential players. The proof
does not enumerate those q^k sets.

## 3. Rechecking the threshold arithmetic

For budget k>=1, put d_k=tau+3-3/k and theta=T/d_k. If delta<=k,
then rho_delta<=1-1/k. At B=theta, the small-unit upper coefficient is
at most 3theta, so tau B+rho_delta C<=T.

For eta0=min(eta,1), B=T/(d_k+eta0). Since d_k>=1, B>=theta/2.
Small units have u<theta, and

\[
 \max\{u,2B+\min(u,B)\}\le3B.
\]

The residual cover gap is at least eta0 B. Therefore the same constant
times eta0 growth threshold used in the main factor-four theorem applies
uniformly in the original rank. At delta=0 the fat reconstruction already
covers a complete basis and supplies value theta; no formula involving
rho_delta or an empty small search is required.

## 4. Why the bottleneck endpoint is included

As theta increases, the fat services only disappear. Thus the common
independent-set size is nonincreasing and delta is nondecreasing.
The list of possible changes is the finite list of positive unit values.
Because a unit of value exactly theta is still declared fat, the largest
admissible positive threshold beta_k is attained when k<r.

It follows that delta(T/d_k)<=k is equivalent to T<=d_k beta_k, including
equality. The zero convention when no positive threshold qualifies and
the infinite convention for k=r are both consistent with this statement.

## 5. The cap cannot be treated as an allocation failure

An intermediate target above d_k beta_k may be feasible in the original
allocation problem. The algorithm is only declining to spend more than
the selected deficit budget. Its failure is sound for the intersection
of original feasible targets with the cap, and not necessarily for the
uncapped comparator.

The promised optimization target is therefore precisely
min(OPT,d_k beta_k). Both of its defining conditions are monotone.
Keeping a successful lower target and a failed upper target is valid
for this capped set even if the search algorithm sometimes succeeds at
targets exceeding the true comparator optimum. Such extra successes
only give a stronger actual allocation than the lower-bound guarantee
requires.

The original target grid is refined by the denominator of d_k. This
places the finite cap on the same rational grid as the comparator
optimum. When final endpoints are adjacent, a sound failed upper
endpoint must be strictly above the capped optimum, so the successful
lower one is at least that optimum. The stored output then has value
at least min(OPT,d_k beta_k)/(d_k+eta), as claimed.

## 6. Stronger polymatroid LP compatibility

The new residual-capacity configuration relaxation can replace integer
optimum in the arbitrary-polymatroid case. Its fat reduction discards
fat-containing configurations and scales the all-small configurations
by player-dependent factors at most one. Every new residual cut has
nonnegative configuration coefficients, so those operations preserve
all cuts. The derived rank is still delta, and its lower cover has the
same coefficient as in the integer proof.

The equivalent subset-cut formulation can even use only subsets of
size at most 2(k-1) on the capped domain: every completed inner state
has that owner-support bound when delta<=k. This is a valid optional
comparator refinement; it does not remove the cap or establish a
faster separation routine.

## 7. Conditional examples and audit conclusion

At k=1 with exact availability, d_1=1. The derived problem is rank zero
or one, so the exact branch really is exact when OPT<=beta_1. The claim
does not say arbitrary instances meet that condition. The displayed
k=2 and k=3 factors follow from the same expression and retain the
same structural cap.

The complete refinement is sound: the nonlinear time depends on k,
all large-ground-set matroid work remains paid, and the cap-aware target
search returns the stated value. This review is internal mathematical
validation, not a polynomial-time general solver, a publication-priority
claim, external peer review or formal verification.
