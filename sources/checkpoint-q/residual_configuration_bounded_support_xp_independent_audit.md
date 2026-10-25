# Independent audit: the bounded-support residual-configuration XP solver

**25 October 2026. Full independent mathematical review of X1--X20.**

The derivation in `residual_configuration_bounded_support_xp_solver.md` passes. It gives a fractional weak optimizer polynomial in the number m of explicitly retained residual cuts, the input bit length H, and epsilon^{-1}, while keeping all aggregate player-base and recipient-polymatroid constraints implicit. For all subset cuts of support at most s, its time is (q+1)^{O(s+1)} poly(H,epsilon^{-1}); at s=2(r-1) this is XP in r.

The proof does not supply an integer approximation scheme, a rank-FPT LP optimizer, or pricing for arbitrary local downward-closed families. It relies materially on coordinate-box configurations and nonnegative unit values. The internally derived allocation theorem uses this LP as a comparator and retains its separate approximation ratio and runtime.

## 1. The relaxation retains the necessary aggregate constraints

The compact representation uses

\[
               K=B(M)\times\prod_j P(f_j).
\]

For positive player rank r, this is a nonempty compact integral polytope. The player component of every vertex is a basis indicator and has coordinate sum r. Resource components have integral nonnegative coordinates bounded by f_j(P).

Arbitrary signed linear optimization over K is valid with the stated greedy oracles. Matroid-basis greedy must retain negative weights when necessary to complete the basis, as the note says. For a resource polymatroid, greedily fill only the strictly positive weight prefix and set other coordinates to zero. A deterministic tie rule yields an integral maximizing vertex. The support oracle returns that actual vertex, which is needed later for primal extraction.

The aggregate resource constraints are included through K even when the listed residual cut family is small. Thus the support-s comparator is exactly the stated residual-cut relaxation, not a relaxation that accidentally omits resource feasibility. The prior reserve-to-subset equivalence can be applied to it without changing the aggregate model.

## 2. The finite mixed Farkas system has the correct signs

For finite configuration columns C and aggregate vertices V, the primal is

\[
 E_C\mu=V\lambda,\qquad H_C\mu\le b,\qquad
                 \mathbf1^T\lambda=1,\qquad\mu,\lambda\ge0.
\]

Assign a free multiplier alpha to the linking equality, a nonnegative multiplier zeta to the residual inequalities, and a free multiplier omega to the convex-combination normalization. Farkas' lemma gives the column conditions

\[
      \alpha\cdot e(c)+\zeta\cdot h(c)\ge0,
      \qquad \omega\ge\alpha\cdot v,
\]

with zeta dot b+omega<0. Scale this last quantity to at most -1. Eliminating omega gives precisely

\[
 \alpha\cdot e(c)+\zeta\cdot h(c)\ge0\ (c\in C),
 \qquad
 \alpha\cdot v+\zeta\cdot b\le-1\ (v\in V).
\]

Conversely, if V is nonempty and these inequalities hold, take omega=max_{v in V} alpha dot v; this restores the normalized Farkas witness. If V is empty, the finite primal is infeasible because its normalization cannot hold. The displayed dual has no vertex inequalities and is nonempty; choose omega sufficiently negative in the unsimplified system. This boundary case is consistent.

For the full K vertex set, maximizing alpha dot v separates all vertex inequalities exactly. When all those inequalities and all hard-target configuration inequalities hold, the resulting witness proves original target infeasibility. It need not satisfy every weak-target configuration inequality for that early stopping claim.

## 3. Signed convex pricing remains an exact-budget approximation

The configuration cost has arbitrary signed linear coefficients and nonnegative convex hinge coefficients. Its marginal unit costs in each type are therefore nondecreasing. Select the entire nonpositive-cost prefix of each type, including zero-cost units. Every feasible count vector can be augmented to contain these units without increasing cost or decreasing value: the local family is a coordinate box and all unit values are nonnegative.

The cost G0 of this prefix vector is a global minimum over the box. For an exact cost budget C, there is no feasible vector if C<G0. Otherwise, subtract G0 from the budget and solve the remaining positive-cost bounded knapsack. Prefix compression remains valid within each type, and binary chunking has polynomial size in the number of hinge breakpoints and binary quotas. Profit scaling approximates only value; the residual cost budget is exact. Adding the forced prefix preserves the same multiplicative value ratio.

This argument also covers types with zero value, negative total prefix cost, all-free configurations, or no remaining positive-value chunk. Forced zero-value negative-cost units can only help the cost constraint and consume no quota outside their own coordinate.

For a rational threshold w of either sign, the largest cost-grid point below it is

\[
             C=(\lceil D_{\rm cost}w\rceil-1)/D_{\rm cost}.
\]

This budget may be negative and is handled by the exact G0 comparison. The old nonnegative-cost shortcut for w<=0 would be wrong here and is correctly absent. If a target-T violating column exists, it fits this strict grid budget and forces the approximate maximum value to reach (1-epsilon)T. Thus the oracle returns a true weak-target violation or certifies the absence of every hard-target violation. Equality with w is never treated as a violation.

## 4. Uniform certificate bounds survive split free variables

Split alpha into alpha^+-alpha^- and put beta=(alpha^+,alpha^-,zeta)>=0 in dimension D=2d+m. The normal vectors are

\[
           a_c=(e(c),-e(c),h(c)),\qquad b_v=(v,-v,b).
\]

Every entry is an integer of absolute value at most B>=max{1,r,max_j f_j(P)}. This includes every possible column and every integral K vertex, not just generated objects.

For every infeasible finite mixed primal, the split dual is a nonempty polyhedron in the nonnegative orthant. It has no line and hence has a vertex. The positive cancellation rays introduced by splitting do not invalidate pointedness: their negative directions eventually leave the orthant. At a vertex, D independent active equations have integer coefficients bounded by B and right sides zero or -1. Cramer's rule gives

\[
                  0\le\beta_{0i}\le U_0=(DB+1)^{D+1}.
\]

This bound is uniform in both finite families C and V, in the target, and in the capacities' numerical magnitudes beyond their bit lengths. If V is empty, beta0=0 is a possible basic witness and causes no difficulty in the next step.

## 5. The positive direction gives an explicit ball for every finite pair

Let theta be one in every split coordinate, except that the positive copy of each player coordinate is two. Positive and negative copies of count coordinates cancel, as do the unit parts of the signed player coordinates. Hence

\[
      \theta\cdot a_c=1+\sum_i h_i(c)\ge1,
      \qquad
      \theta\cdot b_v=r+\sum_i b_i\le(D+1)B.
\]

Both identities are exact and depend on the model's structure. They would not hold automatically in an arbitrary compact linking LP.

With gamma=1/[4(D+1)B], delta=gamma/(2DB), and beta*=2 beta0+gamma theta, every configuration inequality has slack at least gamma. Every generated vertex inequality has slack at least 3/4. Every lower coordinate bound has slack at least gamma, and every upper bound 4U0 has slack at least U0. The Euclidean norm of any normal is at most B sqrt(D)<=DB. Therefore the entire radius-delta ball about beta* satisfies the box and every inequality for the finite pair (C,V).

In particular, if the finite primal on any generated C,V is infeasible, its bounded dual has this explicit interior ball. This remains true for an empty generated vertex family or an empty generated configuration family. The property is proved from the finite primal's infeasibility; no general full-dimensionality assumption is being made.

## 6. Recording both configurations and vertices closes extraction

The ellipsoid starts in a ball containing [0,4U0]^D. It first separates explicit bounds, then maximizes over K and returns any violated vertex inequality, and only then invokes signed weak configuration pricing. Every continuation cut is a genuine inequality of the weaker-target Farkas system. The early stopping case instead gives a valid hard-target infeasibility witness.

If the procedure reaches volume smaller than a radius-delta ball without this early outcome, retain both families C and V encountered. The maintained ellipsoid contains their finite dual region: the initial ball contains the box, and each update preserves the intersection of the corresponding original cuts. If the finite mixed primal were infeasible, Section 5 would place a radius-delta ball inside this region, contradicting the volume bound. Thus the finite mixed primal is feasible.

Solving that explicit LP returns configuration weights and convex-combination weights on genuine K vertices. Their aggregate vector therefore belongs to K and satisfies all player-base and recipient-resource inequalities, including those never queried. All m listed residual rows are included in the explicit primal. Every generated configuration has weak-target value. Consequently the extracted point satisfies the entire specified weak-target relaxation.

Keeping only the configuration columns would leave an implicit K membership problem in the final primal. Recording the vertices supplies exactly the missing finite representation. The proof therefore does not rely on an unproved generic exact oracle-LP extraction theorem.

## 7. Bit complexity, target search, and XP scope

The dimension D is polynomial in H and m. The logarithms of U0, the initial radius, and delta^{-1} are polynomial in D and log B. Standard polynomial-precision rational ellipsoid updates keep the query prices polynomially encoded. Signed prefix costs, strict-grid denominators, binary chunks, dynamic programming, greedy support vertices, and the final finite LP all have polynomial bit length and operation counts in H,m,epsilon^{-1}.

For positive r, aggregate expected value gives rT<=sum_j v_j f_j(P) at every feasible target. The weaker displayed total-value upper bound is therefore safe. The zero target has a basis point with empty configurations. An upper grid trial above that total-value bound divided by (1-epsilon) cannot have a feasible weak target.

Every failed trial is a sound hard-target infeasibility certificate and hence is strictly above OPT_LP. A successful trial need not be hard-target feasible. At adjacent value-grid endpoints, the successful lower trial is at least OPT_LP because the failed upper trial is strictly above it and the optimum itself is a grid point. Its saved point has value at least (1-epsilon)OPT_LP. This is the correct orientation for max-min target search and does not require monotone success choices.

For all supports of size at most s, m=t sum_{i<=min{s,q}} binom(q,i), giving the stated (q+1)^{O(s+1)} bound. At s=2(r-1), this is an XP computation of the support-restricted comparator. It must not be called the full residual LP unless all cuts are included. The full family also yields the singly exponential q bound. Output size and working storage are polynomial in the explicitly retained-cut input size; this does not claim polynomial space in H alone when m is exponentially large.

## 8. Review outcome

The subsequent fractional-only extension X21 to arbitrary nonnegative player-specific unit values v_pj also passes. For a fixed player, these remain nonnegative constant profits within each type, so forcing nonpositive-cost prefixes, prefix compression, binary chunks, and profit scaling are unchanged. The common target grid uses all v_pj, and sum_j f_j(P) max_p v_pj is a valid expected-total-value upper bound. The aggregate constraints, Farkas system, and interior-ball proof do not depend on unit values. This proves only the stated fractional weak optimizer; the common-intrinsic-value allocation guarantee does not follow for player-specific values.

No gap was found in X1--X20. The compact dual, signed-prefix pricing, universal finite-pair witness bound, structural positive direction, two-object extraction, and final optimization are mutually consistent. The result closes the earlier gap between explicit-point cut checking and actually computing a fractional comparator for coordinate-box players.

The generic primitives remain classical; the reviewed contribution is their model-specific composition. This is an independent internal mathematical audit, not implementation, formal verification, external peer review, or exhaustive publication-priority determination.
