# Independent audit of the exact-two derived-corank gate

**25 October 2026. Full independent review of X1--X10.**

Reviewed manuscript: `general_value_exact_two_corank_gate.md`.
The three positive partial results and both recorded obstructions
pass. They leave the unrestricted fixed-parameter exact-two question
open. This review also checked their interfaces with the complete
dual-union adapter in `general_value_matroid_selection_near_two.md`
and with the independently reviewed additive workload theorem.

## 1. The parameter is attached to the correct threshold

The exact-two note defines its parameter at theta*=OPT/2, with
equality assigned to the heavy types. This is a different convention
from the near-two theorem's threshold OPT/(2+eta). The loop-deleted
derived corank need not be monotone as the threshold changes, so the
former hypothesis cannot be inferred merely from a bound on the
latter parameter. The manuscript keeps these statements separate.

At the exact threshold, the dual-union construction supplies a basis
I* of K=(M* vee N)* that is contained in the optimum's light-only
players. This follows by extending the U-independent set consisting
of the complement of the optimal M-basis together with its heavy
receivers. The complement of that extension is I*. Consequently
every member of I* retains the original optimum using light types
alone. Removing the loops of K does not remove any of its basis
elements or any of this witness's resource counts.

For an arbitrary output K-basis I, the completion lemma recovers an
original M-basis B containing I with B\I independent in the Boolean
heavy matroid. The containment is essential: it is supplied by
extending the M* component of a union-basis decomposition inside
P\I. Heavy and light resources are disjoint type collections, so
the one-heavy-unit completion cannot invalidate the allocation on I.

Rank-zero derived instances need no minimum over an empty light set.
They have a full original basis coverable by one heavy unit per
player and are handled directly. OPT=0 is a separate trivial case.

## 2. The exact workload optimization is fully implementable

At a fixed enumerated split, choose a common rational value quantum
g and form the integral light workload rank F=sum_j(v_j/g)f_j on
the fixed loop-deleted derived ground Q. Its coefficients and ranks
have polynomial binary length even when their numerical values are
large. Independent resource vectors, and hence their sum after
scaling, remain feasible when restricted to Q.

For a fixed candidate K-basis I, the predicate

\[
                         \ell\mathbf1_I\in P(F)
\]

is equivalent to nonnegativity of the minimum of
F(S)-ell|I intersection S|. It has an exact submodular-minimization
test. It is monotone in the integer ell, so ordinary binary search
finds the largest feasible ell using a polynomial number of tests.
Zero is feasible and F(Q)+1 is a valid failed upper endpoint when
I is nonempty. No gap oracle and no unknown-optimum parameter are
hidden in this step.

Complete the resulting integer workload vector to a base of F,
decompose that base into the scaled recipient polymatroids, and
divide by the scaling factors. The explicit compressed decomposition
from the additive manuscript produces fractional original resource
bases without expanding capacities into copies. The lower-rounding
lemma then loses at most u_L at each selected player. An allocation
of original integer value T gives T/g integer workload at every
selected player, so it implies ell>=T/g before this rounding loss.

Counts added during base completion cause no assignment-cost issue:
this note has no assignment budget or cross-type local constraint,
and unused counts can be discarded after rounding. This is exactly
the unbudgeted model required by the cited additive construction.

## 3. The XP algorithm does not guess OPT

The algorithm enumerates the finitely many splits between distinct
input value classes, including the empty heavy or light side.
Equality-heavy makes the split at OPT/2 one of these possibilities
even though OPT is unknown. It computes the derived matroid and its
loop-deleted corank independently for each split.

For a split with corank c<=k, every basis is the complement of a
c-element subset of Q. Enumerating those subsets and testing basis
status is therefore exhaustive. At the optimum split it includes
the promised I*. Its computed workload bound is at least OPT, and
its rounded light utility is at least OPT-u_L>OPT/2. Heavy completion
gives at least OPT/2 to each newly selected player, including the
boundary where a heavy unit has value exactly OPT/2.

There are at most binom(|Q|,c)<=(q+1)^k candidate omissions per
processed split, with polynomial work per candidate and polynomial
workspace for the subset iterator and oracle computations. The
algorithm compares the actual integer values of its completed
allocations. An unproductive split can return value zero without
affecting correctness. Skipping a split with c>k makes no assertion
of infeasibility; the public fallback supplies the stated
unconditional output when the parameter promise is absent.

When c=0, a loopless rank-|Q| matroid is free and has the unique basis
Q. Thus the same method is polynomial. This endpoint is substantive:
the numerical epsilon substitution discussed later is unnecessary
at zero corank, and exact factor two is already proved there.

## 4. The quantified light-value gap gives the stated FPT case

For a supplied rational sigma in (0,1/2], the condition
u_L<=(1/2-sigma)OPT at the half-optimum split combines with the
additive corank guarantee to give

\[
 (1-\sigma)\mathrm{OPT}-u_L\ge\mathrm{OPT}/2.
\]

The heavy completion meets the same bound. The additive algorithm
is run as a complete optimization routine for every processed split;
it is not supplied OPT. Its running time Gamma(1/sigma)^k poly(H)
and polynomial space therefore apply exactly as stated. The extreme
sigma=1/2 condition may force no positive light value at the good
split; the direct pure-heavy handling and zero-value branches already
cover the relevant endpoints.

The displayed OPT=2B, u_L=B-1 pattern correctly diagnoses the current
additive proof's limitation. It requires epsilon<=1/(2B), yielding
numerical dependence comparable to B^c. It is explicitly presented
as a numerical limitation, not as an instance family proving
hardness. In particular the XP algorithm is polynomial for fixed
c=1, so this failed parameter substitution cannot establish an
inherent exponential-in-bit-length barrier.

## 5. The proposed two-medium-unit cover is not a matroid

For the neighborhood-union rank in X9, the pair {a,b} has union
size four and admits two units per player. The triple {a,c,d} has
union size six; all its pairs have union size at least four and
its singletons have size four. These are all its subset inequalities
for the count vector that requests two units per member, so the
triple is feasible.

Neither c nor d augments {a,b}: either resulting triple has only
five neighboring resource units but asks for six. The downward
family of two-unit recipient sets therefore violates matroid
augmentation between a feasible pair and a feasible triple. This
is an explicit obstruction to treating that family as a Boolean
matroid in another dual-union adapter.

The private-player extension also checks. Each of e,f,g has three
private units, disjoint from all other resource neighborhoods. In
the U_(3,7) player matroid, their joint basis obtains value 9/4 at
unit value 3/4. Any basis containing a private player has minimum
at most 9/4 because that player's singleton count is at most three.
Any three-player basis chosen solely from a,b,c,d has total count
at most six, so its minimum utility is at most 3/2. Hence OPT=9/4
exactly, and all units lie in [OPT/4,OPT/2). The failed augmentation
on the original four players persists inside the enlarged resource.

This is a valid strong-promise example, but only an obstruction to
the proposed matroid interface. It is one-valued and remains within
the previously solved unit-quota framework. No complexity lower
bound follows from the augmentation failure.

## 6. The two oracle-boundary statements are compatible

Adding a positive modular private bonus delta to a hidden two-unit
instance gives the one-unit solution value v+delta, which is at
least half of the new optimum 2v+delta. Thus that particular bonus
cannot convert the strict-below-two oracle obstruction into an
exact-two obstruction. X10 is algebraically correct and makes no
broader impossibility claim.

For completeness, the existing refined-zero strict-below-two
examples also remain at parameter zero at the exact half-optimum
threshold. They have OPT=2 and a value-one resource admitting an
all-ones allocation. At OPT/2=1, equality-heavy includes that
resource, making the aggregate Boolean heavy matroid free. Thus
the same hidden-set argument excludes every factor strictly below
two at refined parameter zero even under this endpoint convention.
It does not exclude the polynomial exact-two result in Section 2.

The resulting status is precise: exact two is proved at derived
corank zero, in XP time for arbitrary bounded derived corank, and
in single-exponential FPT time with a quantified light-value gap.
The unrestricted F(k)poly(H) exact-two theorem at c(OPT/2)<=k remains
unproved by these methods; no aligned exact-two hardness result is
claimed.
