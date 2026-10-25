# Second independent audit: one shared commodity setup and routing budget

**25 October 2026. Independent full mathematical read by the transfer-frontier
researcher. This is an internal audit, not external peer review or formal
verification.**

Reviewed the entire manuscript
`shared_setup_routing_budget_corank_flow.md`, Sections 1--10 and SF1--SF15,
against the weighted prefix-free omission interface and the exact rational
comparator lemma. The result passes. No substantive correction is requested.
This review is separate from the earlier audit with the shorter filename.

## 1. The model supports the claimed residual region

The setup fee is incurred by selecting a commodity. It changes the available
routing budget but does not change the physical graph, edge capacities,
terminal pairs or other routing rows. Once a selected set I is specified,
its setup charge s(I) is a fixed rational constant. The remaining rate
optimization is consequently an ordinary bounded rational flow LP with
routing budget C-s(I).

Nonnegative routing costs and capacity coefficients are essential. Scaling
down one commodity's entire flow reduces every shared load and every
routing charge. This proves downward closure of the normalized service
region, including disconnected terminals, zero budget rows, and zero
capacities. For an undirected edge the combined bidirectional capacity row
in Section 1 is the correct physical constraint.

The theorem properly requires an exact minimum-setup restriction optimizer,
not just some permitted set contained in Q. Minimum-weight matroid basis
or two-matroid cardinality-r intersection supplies this optimizer. A second
unrelated hard selection objective is explicitly excluded unless another
oracle is supplied. This distinction prevents an unjustified constrained
optimization claim.

## 2. The adaptive target proof uses one unchanged witness

Fix a full-target permitted set I* and its original full-T routing. At
every node Q containing I*, the exact setup minimum obeys

\[
                 h(Q)\le s(I^*),\qquad
                 C-h(Q)\ge C-s(I^*).
\]

Thus that same routing remains feasible in the current service region.
This statement holds again after any deletion avoiding I*. It does not
assume one fixed region across the recursion, nor does it try to compare
independently minimizing sets for two objectives.

For alpha=1-epsilon and a violated nonnegative row `a*z<=U`, feasibility
of T*1_(I*) and violation by alpha*T*1_Q imply

\[
           T a(I^*)\le U<\alpha T a(Q),\qquad
              a(Q\setminus I^*)>\epsilon a(Q).
\]

The original first-density-crossing argument therefore finds an enumerated
omission word lying wholly inside Q\I*. One surviving child preserves the
full witness. If the remaining deficit is zero, Q=I*; downward closure
then makes the weak query feasible. This verifies completeness and sound
full-target failure, including all changing setup minima.

At a successful node, keeping the attaining set I_Q is necessary and
sufficient. The reconstructed flows serve all of Q with routing cost at
most C-h(Q). Restricting to I_Q reduces every nonnegative routing load and
charge, while the setup charge is exactly h(Q). Their actual combined cost
is therefore at most C. Choosing an arbitrary different permitted subset
of Q could lose this inequality; the manuscript correctly does not do so.

## 3. The separator remains exact and has nonnegative coefficients

The displayed potential/length system is the dual Farkas system of the
explicit bounded primal routing LP. If one commodity's terminal potential
gap is negative, setting all of its potentials to zero preserves every
arc inequality because its right side is nonnegative. At a nonnegative
query this operation cannot reduce the separating objective. A strict
certificate may therefore be chosen with nonnegative commodity
coefficients.

Splitting potentials into positive and negative variables and applying the
one-norm normalization gives a finite bounded LP. Its zero certificate is
feasible, so a positive optimum is exactly the infeasible-query case; a
zero optimum means membership. This is distinct from a simplex-normalized
support LP whose optimum can be negative in the feasible case. The
manuscript uses the correct formulation.

The changing right side C-h(Q) has uniform polynomial bit length because
h(Q) is an actual sum of at most q original setup fees. Exact primal and
dual flow LPs consequently retain polynomial encoding at every node.
Additional explicitly listed routing-only rows affect only this LP size.

## 4. The target-time and workspace accounting survive adaptivity

The row returned at a node depends on Q, but the weighted prefix-free
enumeration bound uses only the ratio R=1/epsilon and the remaining
omission count d=|Q|-r. Its probability-mass inequality is insensitive to
the origin of the nonnegative row. The per-node invariant above is the
only promised-witness fact needed for completeness.

Every minimum-setup call, failed selector, LP separation and reconstructed
flow has polynomial cost on unpromised inputs as well. The complete target
bound is therefore Gamma(1/epsilon)^(q-r) times a polynomial, not merely a
bound on one successful path. A depth-first implementation stores at most
q recursive grounds and current polynomial-size certificate/LP data.
There is no enumeration by numerical budget, flow value or denominator.

The same reasoning holds after any forced omitted set Z: the selected
family is merely restricted to P\Z, the protected full set still survives
if it avoids Z, and the remaining exponent is q-r-|Z|. This justifies the
global inclusion-cover application in the separate global-transfer note.

## 5. Exact reoptimization recovers the full requested accuracy

The setup-feasible family B_C is independent of every queried target. For
each I in that family, the exact maximum normalized rate lambda_I is an
attained optimum of a bounded rational LP. Its coefficients and the
right side C-s(I) have a common polynomial bit bound. Clearing row
denominators and applying Cramer's rule gives the displayed denominator
bound D; lower-dimensional feasible faces do not obstruct choosing a
full-rank active subsystem at a vertex.

With alpha=A/B and grid delta=1/(2BD^2), the one-sided search maintains an
external upper endpoint above the true maximum Lambda. Total target
failure is the only fact used to update that upper endpoint. A weak
success need not certify its nominal full target and need not be monotone.
At adjacency the saved target L satisfies L>Lambda-delta, and its actual
set I has lambda_I>=alpha*L.

Exactly reoptimizing that saved set uses the original fixed-set LP. If its
optimum were below alpha*Lambda, the denominators of lambda_I and Lambda
would force a gap at least 1/(BD^2), whereas the previous inequality allows
less than alpha*delta. This is impossible. The returned rate is therefore
at least alpha*Lambda with the original epsilon, not with an unmentioned
extra loss. Reoptimizing the saved actual set, rather than merely rounding
its artificial-grid witness, is the important precision step.

## 6. Initial feasibility, zero cases, and scope

The initial h(P) test is necessary because selected commodities pay their
setup charges even at rate zero. If h(P)>C or the family is empty, no legal
selected set exists. Otherwise the attaining affordable set with zero
routing is a valid initialized output. Positive rates are not needed to
start the rational search; a zero optimum is handled correctly. Rank-zero
selection is separated from the finite-rate statement.

The illustrative two-commodity example correctly shows why the routing
budget must be recomputed after a deletion. It is not used as proof of
optimality or as a hardness claim.

The conclusion concerns splittable routing and an explicit candidate
commodity ground. It preserves one combined setup/routing budget and any
fixed additional nonnegative routing-only rows. It makes no unsupported
claim for several independently minimized setup vectors, a second exact
selection cost, unsplittable routing, or selecting paid edges that changes
network availability. The bounded source discussion is not an exhaustive
novelty audit. These qualifications match the actual proof interfaces.
