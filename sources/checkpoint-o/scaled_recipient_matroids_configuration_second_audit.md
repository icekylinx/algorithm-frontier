# Second independent audit of the binary scaled-matroid configuration transfer

**25 October 2026. Complete mathematical review passed.**

The reviewed manuscript is
`scaled_recipient_matroids_binary_configuration_transfer.md`, including
S1--S14. This audit checks the stronger configuration comparator and the
absence of copy-pattern or capacity-expansion costs. It relies on the
separately audited full-polymatroid algorithm for the actual search and
its sharp approximation factor. This is an internal mathematical review,
not formal verification or external peer review.

## 1. Integer counts correctly represent identical matroid copies

For one type with c identical recipient matroids R, a feasible compressed
count vector satisfies n(S)<=c r_R(S). Conversely, replace each player's
n_p services by conceptual parallel occurrences in R. For every subset A
of occurrences,

\[
 |A|\le n(\operatorname{supp}A)
             \le c r_R(\operatorname{supp}A).
\]

The c-fold matroid-union criterion therefore partitions the occurrences
into c independent sets, one per resource copy. No part can contain two
parallel occurrences of the same player. Thus the aggregate count vector
is exactly a compressed legal allocation to copies.

This equivalence is a proof of existence, not a prescribed explicit
copy-by-copy output. The theorem clearly chooses binary counts as its
output representation; printing every copy could itself require time
proportional to an exponentially large binary multiplicity.

## 2. The fractional loss lemma has the correct normalization

For f=c r_R, an independent set I of R has c|I| independent natural-
matroid service copies in its full player blocks E_I. Let W be the
current reserved set, L=r(W), and a_p=r(W union E_p)-r(W).
Contracted-rank subadditivity yields

\[
 \sum_{p\in I}a_p\ge r(W\cup E_I)-r(W)
                              \ge c|I|-L.
\]

Hence sum_{p in I}(c-a_p)<=L for every R-independent I. Since y/c lies
in the independent-set polytope of R, expressing it as a convex
combination of such indicators gives exactly

\[
                    \sum_p(1-a_p/c)y_p\le L.
\]

The division by c is essential and is present. It is not an assertion
about an arbitrary polymatroid f. W need not be independent: contraction
by its span has the same displayed rank function. The argument uses no
representability, recipient-rank restriction, or explicit decomposition
of the fractional vector.

## 3. Local configuration restriction does not require shared copy IDs

For each player and type, a feasible count n<=c can be represented as a
uniform n-subset of c private proof slots. Intersecting with a fixed
a_p-subset retains expected count a_p n/c, while producing an actual
count at most both n and the algorithm's availability cap a_p.

Perform this conceptual construction for every type in a local count
configuration. Its resulting count vector is coordinatewise smaller,
so every supplied type-symmetric downward-closed local constraint is
preserved. Mixing the configurations preserves the corresponding
fractional retained value. No common slot assignment across different
players is claimed or required: the global loss budget is supplied by
the independent resource inequality in the previous section.

A complete failed factor-lambda available-oracle scan therefore makes
the retained expected value strictly below (B/lambda)x_p on every
positive eligible player coordinate. The proof does not require an LP
solution as input, and does not assume monotonicity of approximate
oracle outputs across different states.

## 4. The strict lower cover is restored against the stated relaxation

The player-base polytope gives at least w positive total mass outside
the eligibility flat. On those players, the original value is at least
T x_p and the restricted value is strictly below (B/lambda)x_p.
The loss coefficients 1-a_p/c are nonnegative, so the sum over eligible
players is bounded by the whole resource-column loss. Summing the
resource lemma gives

\[
                     \Phi>(T-B/\lambda)w
\]

when T>=B/lambda. Strictness is valid even at equality, because w>0
forces positive eligible fractional mass. This is exactly the lower-
cover interface used by prefix normalization and its rank signature.

The upper cover remains the independently proved current quantity
max{u,2B+min(u,B)}|Y|. Accordingly the full-polymatroid search obtains
its factor lambda^{-1}+3-3/r against the stronger relaxation in this
scaled-matroid resource class.

## 5. Fat types preserve the component configuration promise

Choosing one fat unit from each fat-containing configuration gives a
per-type selected marginal f^j bounded by its old y^j, while the total
selected marginal is bounded by x<=1. Thus f^j lies in c_j P(R_j)
and in the unit box. The intersection is the independent polytope of
the c_j-fold union matroid: the displayed union-rank inequalities follow
by bounding f^j(A) by c_j r_Rj(A) and the remaining coordinates by one.

The union of those fat matroids supports the total fat marginal. Its
sum with 1-x is a feasible independent vector of the dual-player/fat
union, bounded coordinatewise by one. Extend it to a union base and
complement. The resulting small-player base vector is dominated by the
all-small configuration mass. Scaling only those all-small rows preserves
every local perspective and every separate type column by down-closure.

The reverse decomposition uses one fat service per selected fat player
and the already constructed small count vectors. Deleting additional
players preserves all feasibility conditions. For Boolean fat service
assignments, c_j can be clipped to q; ordinary union and decomposition
therefore have polynomial oracle cost even for huge binary c_j.

## 6. No pattern table or expanded capacity is hidden in the runtime

The actual search uses the compressed natural-matroid rank

\[
       R(z)=\min_S\{c r_R(S)+z(P\setminus S)\},
\]

computed by deterministic submodular minimization on q explicit
players. State records contain only O(r) count vectors and their group
and layer flags. Candidate-block dependence and strong-release tests
use a polynomial number of such rank queries. Counts, sums, pruning,
and the finite target grid have polynomial bit length.

The slot randomization is only a proof of a local convex combination;
the algorithm is deterministic and does not sample it. The matroid-union
partition of all individual copies is also only a proof of compressed
output feasibility. Neither argument creates an uncharged loop or a
2^{O(r)} copy-pattern factor. The claimed polynomial wrapper space and
rank-quasipolynomial positive-error bound therefore pass this review.

## 7. Components with different recipient matroids must stay separate

The rank-gap construction f(S)=|S|+D min{1,|S|} is the sum of two scaled
matroid ranks, yet its single aggregate configuration relaxation has a
gap tending to the player-selection rank. Keeping the two supplied
types distinct preserves separate columns and rejects the gap point.
The theorem correctly uses that stronger component-level comparator.

Merging such components preserves the integer feasible count set when
the relevant integral decomposition exists, but it does not preserve
the component-level configuration relaxation. The full arbitrary-
polymatroid theorem remains valid against integer optimum after merging;
this separate stronger comparison is what requires visible components.
