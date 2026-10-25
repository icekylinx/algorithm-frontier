# Second independent audit: shared player-setup and assignment budget

**25 October 2026. Fresh full read by the transfer-frontier researcher of
`unrelated_allocation_shared_setup_budget.md`, Sections 1--9 and SD1--SD15.
Internal mathematical audit, not formal verification or external review.**

The theorem passes. The persistent zero-utility dummy fixes the exact
point at which a naive setup-fee extension would fail: deleting an
unselected player's dummy during an omission step would remove a budget
credit. The manuscript retains all dummy counts on the protected path,
uses a bounded signed rounding objective, and converts the final integer
dummy support to an actual original basis before discarding anything.
Those choices close the budget, utility and selection interfaces.

## 1. Initial feasibility is exact for the original model

Every legal original solution pays the setup sum of an actual M-basis,
and all assignment costs are nonnegative. A minimum-setup basis therefore
decides whether even zero utility is legal. If its fee exceeds C, no
original solution exists. Otherwise that actual basis with zero counts
is a legal initialized output, including C=0 and positive fees on other
players. No feasibility claim about a particular later role family is
needed for this initialization.

Deleting original player loops is safe: no original basis contains them,
and discarding their original assignments cannot raise cost or reduce
selected utility. The setup sum used later must be over the retained
ground, as in the manuscript. Rank zero is correctly separated.

## 2. The signed dummy is an exact integer budget certificate

The dummy recipient rank is M*, so an integer dummy vector y has entries
zero or one and support D independent in M*. Dual rank gives

\[
                 r_M(P\setminus D)=r_M(P)=r.
\]

Thus an original M-basis B can be selected inside the dummy-free set,
even when D is smaller than a full dual basis. Its actual fee and real
assignment cost obey

\[
 \begin{aligned}
 \sigma(B)+c(x|_B)
 &\le\sigma(P\setminus D)+c(x)\\
 &=\sigma(P)-\sigma(D)+c(x).
 \end{aligned}
\]

The first inequality uses the stated nonnegativity of original fees and
costs. The second expression is precisely the affine budget enforced
before extraction. This proves original feasibility for every returned
integer point, without requiring full dummy rank or choosing a
minimum-fee basis at the final stage.

The auxiliary right side C-sigma(P) may be negative. That is harmless:
the dummy objective is bounded on a compact matroid polytope, and all
optimization problems are ordinary bounded rational LPs. This is not a
claim about arbitrary negative original assignment costs.

## 3. The persistent dummy preserves the full witness

For an original optimum on B*, use the canonical dummy basis P\B*.
Its affine setup expression equals sigma(B*) exactly. Choose I* to be
the originally selected players without a heavy real unit; keep their
original light allocations and one original heavy unit at every other
selected player.

At a node Q containing I*, retaining the entire canonical dummy while
dropping only real heavy allocations on Q\I* preserves all constraints.
Every player outside Q is either an originally heavy selected player
or an originally unselected dummy player. It still has total count one.
The allowed real pairs have the correct current masks, real resource
counts decrease, and the unchanged dummy means no setup credit is lost.
All removed costs are nonnegative original costs. The original full
service on I* therefore remains feasible in the current projection.

The more general benchmark witness can have dummy counts on its light
set as well. The same deletion operation remains valid: retain every
dummy count, keep real assignments on the protected light set and on
the currently forced complement, and discard only real assignments on
the other current light candidates. The heavy equalities on the forced
complement are unchanged. This verifies the full-role benchmark used in
the target search, not just the special integer-optimum witness.

Restricting the dummy to P\Q would invalidate this argument. The
manuscript explicitly retains it everywhere, which is the necessary
structural change from the positive-value dummy reduction.

## 4. Nonnegative service separation survives the signed affine row

For nonempty X_Q, the projected service region U_Q contains zero and
is downward: its coordinates are utility lower bounds dominated by
the same fractional witness. This statement does not require the
underlying x,y polytope to be coordinatewise downward in y. All real
and dummy resource polytopes are bounded, so U_Q is compact and convex.

The nonnegative-normal separation argument therefore applies exactly.
A signed separator of a nonnegative query can have its negative
coordinates set to zero without changing the support of a downward
region. Support maximization is a linear program over the original
joint masked ranks, the persistent dummy, forced equalities and the
one affine budget. The dummy's negative cost is internal to that LP;
it does not create a negative coefficient in the returned service row.

Empty X_Q must be tested separately and is correctly rejected. A
protected witness prevents this rejection on its surviving path.
Extreme-point support cuts have uniform polynomial bit length because
the dimension, original numerical data, dummy ranks and the sum
C-sigma(P) do. The normalized support LP accepts every nonpositive
optimum as membership, inherited from the explicitly correct J
interface. The support bound excludes dummy utility, which is zero.

## 5. One integer point preserves the affine cost and both kinds of service

The free-disposal construction turns each original independent vector,
including the dummy, into an extended base without changing real-player
coordinates or cost. On the bounded integral maximum-total intersection
face, minimizing any signed original linear cost is equivalent to
maximizing that same signed coefficient vector on the complement.
Since the fractional complement is feasible on the face, an integral
optimizer has no larger original signed cost. No nonnegative-objective
assumption is used in that inequality.

At a current light player the dummy is ordered with value zero, and
all allowed real values are at most u_L. Prefix telescoping consequently
preserves original light utility to within u_L, without charging a
large artificial dummy value as the loss. At a forced player, the
full-prefix floor preserves at least one total real-or-dummy unit.
Both properties hold at the same signed-cost-optimal integer point.

The dummy resource remains integer and M*-independent. After selecting
an M-basis in its dummy-free complement, every selected forced player
has at least one original heavy unit, and every selected light player
has the stated original light utility. Keeping extra heavy counts
causes no difficulty. Real allocations outside the recovered basis may
then be discarded by nonnegativity. The affine budget certificate in
Section 2 establishes the exact original setup-plus-assignment budget.

An arbitrary pre-extraction trim to one heavy-or-dummy unit would be
unsafe if it discarded a negative-cost dummy. The manuscript avoids
that operation. No hidden deletion of signed-cost coordinates is used.

## 6. Zero-adjoined benchmarks and the all-heavy gate are sound

For k<q there is at least one protected light coordinate, so every
full-role service target is at most V. If a role family is empty,
adjoining numerical zero makes its benchmark defined without asserting
a false feasible role witness. If the family is nonempty, its achievable
light service is downward and bounded; the largest original-grid value
exists by compactness and the finite number of possible light sets.

The initialized globally affordable zero-value original solution is
sufficient as the saved nominal-zero output. Its value is at least
the required nominal-zero lower bound, even if that particular role
family is empty. At positive queried targets, total gap failure excludes
the full benchmark target. Thus the external upper endpoint remains
strictly above the benchmark, and adjacent grid endpoints imply the
saved nominal lower target is at least that benchmark. No monotone
success or exact feasibility claim is made for weak successes.

At k=q there is no light target to optimize. The separate gate intersects
the joint original-heavy-plus-dummy resource product with one-unit
per-player caps and imposes maximum total q. This face is integral.
Minimizing the signed cost on it is polynomial and yields an integer
affine-budget certificate whenever the fractional optimum satisfies
the budget. The canonical optimum with all selected players heavy
provides such a witness. Dummy-free extraction then supplies an original
M-basis of heavy recipients and the claimed value.

## 7. Approximation, parameter and global time

At the true near-half threshold, the protected light set has size
r-|F*|, so its omitted complement has exactly c+|F*| elements. The
conditional support cap c+K includes that cardinality. The global
algorithm enumerates every exact cardinality below q and handles q
by the pure gate; the omission cover therefore has the correct exact
protected complement size. Early relaxed success with fewer forced
roles still recovers a legal original basis allocation.

At every protected node, the same nonnegative row inequality gives
the weighted first-crossing omission certificate. The complete branch
bound depends only on R and the remaining deficit, not on nesting
of the changing projections. It includes failed empty-region and
support LP calls on unpromised inputs. All those calls have uniform
polynomial encoding, so their costs fit the claimed factor.

The original integer optimum lies on the common original-value grid.
At its mask, the benchmark is at least that optimum or the all-heavy
gate applies. Light utility after rounding exceeds the threshold
because u_L is strictly smaller than it; selected heavy players reach
the threshold. OPT=0 uses the initialized feasible basis, without
evaluating a zero threshold. The fixed-rational accuracy and polynomial
workspace accounting are inherited from the reviewed gap and streamed
global-cover implementations.

The theorem's one combined budget, one original player matroid and
nonnegative original costs are respected throughout. The signed dummy
is a proved accounting device, not permission to generalize the model
to arbitrary signed costs, several setup objectives or multiple exact
integer budgets. No substantive mathematical gap was found.
