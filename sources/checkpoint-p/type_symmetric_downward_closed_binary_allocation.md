# Binary supplies with type-symmetric local feasible families

**25 October 2026. General compressed-oracle extension; internal root
and independent audits completed.**

This note combines the binary intersection-cell representation with
the exact or approximate player-local feasible-bundle interface. Its
new scope includes a different integral polymatroid on resource types
for each player, and binary bounded-knapsack constraints, without
expanding identical unit supplies. The constraints are on each
player's own count vector. They are not arbitrary resource-side
polymatroids on the receiving players.

The imported proofs are
`binary_resource_capacities_compressed_current_blocker.md`,
`player_local_downward_closed_allocation_extension.md`, and
`approximate_available_bundle_oracle_allocation.md`. This note supplies
the missing symmetry lift, the finite interface and exact local
polymatroid optimization.

## 1. Count-vector model and available oracle

There are \(t\) resource types, binary supplies
\(c_j\in\mathbb Z_{\ge0}\), and positive common intrinsic unit
values \(v_j\). Player selection uses a matroid \(M\) of rank
\(r\) on the explicit player set. Rank zero is the empty allocation.
Zero-supply types are discarded first. In particular a fat-singleton
test is made only when its availability vector \(e_j\) satisfies
\(e_j\le c\).

For every player \(p\), let

\[
 \mathcal F_p\subseteq\prod_{j=1}^t\{0,\ldots,c_j\}
 \tag{S1}
\]

be a nonempty downward-closed family of integral count vectors.
Membership depends only on counts of each type, not on the identities
of unit copies within that type. An allocation gives a vector
\(n_p\in\mathcal F_p\) to each selected player, with
\(\sum_p n_{pj}\le c_j\), and value \(v\cdot n_p\).
Input, output and intermediate vectors use binary counts.
Zero-supply types can be deleted before all oracle calls and restored
as zero coordinates in the output. In particular a fat-singleton test
is never made at an availability vector exceeding a zero supply.

For every availability vector \(0\le A\le c\), assume a
deterministic oracle returning \(n\in\mathcal F_p\), \(n\le A\),
such that

\[
 v\cdot n\ge\lambda\,
         \max\{v\cdot z:z\in\mathcal F_p,\ z\le A\},
                 \qquad 0<\lambda\le1.
 \tag{S2}
\]

The exact version has \(\lambda=1\). Oracle runtime and
workspace are paid. There is no assumption that an arbitrary
implicitly described downward-closed family admits efficient
optimization. This is an explicit interface condition.

## 2. The aggregate perspective relaxation

Use

\[
 \begin{split}
 &x\in P_{\mathcal B(M)},\qquad
          y_p\in x_p\operatorname{conv}(\mathcal F_p),\\
 &\sum_p y_{pj}\le c_j,\qquad v\cdot y_p\ge T x_p.
 \end{split}
 \tag{S3}
\]

At \(x_p=0\), set \(y_p=0\). The individual quota formulation
in the binary-supply note is a special case. For general
\(\mathcal F_p\), separate coordinate upper bounds do not
replace the perspective condition in (S3).

### Lemma 1: a uniform copy lift respects the entire local family

For every feasible point of (S3), there is a conceptual physical-copy
lift with per-copy marginals \(y_{pj}/c_j\), and each player's
conditional distribution is supported on physical sets whose count
vectors belong to \(\mathcal F_p\).

**Proof.** For \(x_p>0\), express \(y_p/x_p\) as a convex
combination of integral vectors \(n\in\mathcal F_p\). Given
\(n\), choose uniformly an \(n_j\)-element subset of the
\(c_j\) conceptual copies of each type \(j\), independently
across types. This is only an existence construction. Every chosen
physical set has count vector \(n\), and each unit of type \(j\)
has conditional marginal \(n_j/c_j\). Mixing and multiplying
by \(x_p\) gives the claimed marginal. A type of zero supply
has zero marginal and needs no copies. Summing over players gives
per-copy usage at most one by the aggregate capacity constraint.
\(\square\)

For an arbitrary fixed forbidden set of physical copies, let \(A_j\)
be the number of available copies of type \(j\). Restrict each
physical set in the conceptual distribution to those available units.
Its new count vector is coordinatewise smaller, so remains in
\(\mathcal F_p\), and it is at most \(A\). Hence its value
is at most the true available optimum in (S2). The fractional value
outside that forbidden set is exactly

\[
                 \sum_{j:c_j>0}v_j A_j y_{pj}/c_j.
 \tag{S4}
\]

If a completed unchanged-state scan has oracle return below \(B\)
for every eligible player, (S2) and Lemma 1 show that (S4) is strictly
less than \((B/\lambda)x_p\) whenever \(x_p>0\). This is
the same strict outside-value bound as the explicit-item algorithm.
It holds for the actual retained forbidden set, not merely for an
average forbidden set.

## 3. No unit-copy allocation or relabeling is needed

Use the existing count cells

\[
                       z_j[a,b]
\]

indexed by resource type, current matching-bundle label or zero, and
selected-bundle label or zero. There are \(O(t(r+1)^2)\) cells.
Their sums are the supplies. Each label has an owner and a current
layer flag, but different selected labels may have the same player
owner.

The available count is still

\[
                   A_j=\sum_{a=0\text{ or }a\notin Y}z_j[a,0].
 \tag{S5}
\]

Undiscovered matching rows are included. Invoke (S2) on this vector.
If its returned count vector has value at least \(B\), select
those counts from the available cells in a fixed row order.
Type symmetry guarantees that this choice of unit identities is
feasible for the owner: only the returned counts matter.

Prune the candidate by removing, for each represented type \(j\),

\[
           \min\left\{n_j,
                  \left\lfloor\frac{v\cdot n-B}{v_j}\right\rfloor
               \right\}
\]

units in one batch. Downward closure preserves local feasibility.
After one type pass every remaining unit is individually essential
to the value threshold. There is no iteration proportional to a
supply or to a returned count.

Blocker discovery, row exchanges, column retirement and slot reuse
are exactly the audited cell operations. In particular a stored free
column is copied into the new matching row before its old column is
retired, or its provisional counts are first saved. Reuse clears
old owner and layer flags.

The cell operations admit an execution in one fixed conceptual unit
universe. A split chooses a subset of one old cell; a tag move does
not change unit identity. Thus old lower forbidden sets and their
maximality statements remain literally valid. No global permutation
of resource copies is used in the proof.

## 4. Quality, time and fat resources

Let \(u\) be the largest positive-supply unit value, or zero when
there is no such type. Since all
minimality and physical star proofs take place in the conceptual
unit universe, their sharp coefficient remains

\[
                 C(B,u)=\max\{u,2B+\min(u,B)\}.
\]

The sufficient compact-relaxation condition is therefore

\[
                       B/\lambda+\frac{r-1}{r}C(B,u)\le T,
 \tag{S6}
\]

with the same positive-gap refinement. Binary multiplicities enter
only the cell count bit lengths and available-oracle complexity.
The charged-state factor is the same minimum of rank-exponential
and rank-quasipolynomial terms proved in the approximate-oracle note.
Ordinary work per state is polynomial in the explicit player/type
input, rank, total numerical bit length and oracle runtime.

For arbitrary unit sizes, a fat type has \(v_j\) above the fat
threshold. Player \(p\) can receive one fat unit precisely when
the unit vector \(e_j\) belongs to \(\mathcal F_p\). Testing
(S2) at availability \(e_j\) decides this exactly for every
\(\lambda>0\). The fat-player matroid is a capacitated
transversal matroid on the type graph, with capacities
\(\min(c_j,q)\); it does not require \(c_j\) item vertices.

The forward/reverse fat union reduction, and the configuration-LP
split using quota-feasible count-vector configurations, are unchanged.
They give ratio

\[
                         d_{r,\lambda}=\lambda^{-1}+3-3/r
 \tag{S7}
\]

in rank-exponential time, or \(d_{r,\lambda}+\eta\) in

\[
 \operatorname{poly}(\text{explicit input bits, oracle work})
 \min\left\{2^{O(r)},
       (r+1)^{O((1+\eta^{-1})\log(r+1))}\right\}.
 \tag{S8}
\]

Here the rank exponent is uniform in \(\lambda\); oracle accuracy
costs are still paid. Wrapper space is polynomial in the explicit
binary input, in addition to oracle workspace. Target search uses
the common value denominator and an initially failed target greater
than \((d_{r,\lambda}+\eta)\sum_jc_jv_j\). Its number of
trials is polynomial in the numerical encoding, not in total supply.

## 5. Exact availability for a player's integral polymatroid

Suppose player \(p\) supplies a normalized, monotone, integer-valued
submodular function \(f_p\) on the type set, through a value oracle.
Its feasible count vectors satisfy

\[
                n(S)\le f_p(S)\quad(S\subseteq[t]),
                \qquad n\in\mathbb Z_{\ge0}^t.
 \tag{S9}
\]

The global supply bound, and the current availability \(n\le A\),
are imposed by the allocation interface. The returned function values
and the original supplies have paid bit lengths. Different players
may have entirely different polymatroids.

Define the box-restricted rank function

\[
           g_A(S)=\min_{Q\subseteq S}
                         \{f_p(Q)+A(S\setminus Q)\}.
 \tag{S10}
\]

It is normalized, monotone, integral and submodular. Submodularity
follows by taking minimizers for two sets and uncrossing them with
submodularity of \(f_p\); the two modular \(A\)-terms have
exactly the same union/intersection sum. Monotonicity follows by
restricting a minimizer for a larger set to the smaller set and using
monotonicity of \(f_p\) and nonnegativity of \(A\).

Moreover,

\[
                         P(g_A)=P(f_p)\cap[0,A].
 \tag{S11}
\]

For the forward inclusion from right to left, split \(n(S)\)
over \(Q\) and \(S\setminus Q\), using \(f_p(Q)\) and
\(A(S\setminus Q)\), and minimize. Conversely choosing
\(Q=S\) and \(Q=\varnothing\) proves respectively the
original rank inequalities and the singleton coordinate caps.

Order the types by nonincreasing \(v_j\). On the corresponding
prefixes \(S_i\), set

\[
                   n_{j_i}=g_A(S_i)-g_A(S_{i-1}).
 \tag{S12}
\]

The ordinary polymatroid greedy proof shows this vector belongs to
\(P(g_A)\) and maximizes the nonnegative weighted objective:
every prefix of any feasible vector is at most \(g_A(S_i)\),
whereas (S12) has equality; summation by parts finishes the proof.
Submodularity supplies feasibility of the greedy vector, and
integrality makes its coordinates integers. Thus it is an exact
available count vector.

Each prefix value in (S10) is one submodular minimization of
\(f_p(Q)-A(Q)\) restricted to that prefix, plus the constant
\(A(S_i)\). There are at most \(t\) such calls, and deterministic
submodular minimization is polynomial in the ground-set size and
oracle encoding. A primary source is Iwata, Fleischer and Fujishige,
*A Combinatorial, Strongly Polynomial-Time Algorithm for Minimizing
Submodular Functions*,
[arXiv:math/0004089](https://arxiv.org/abs/math/0004089);
see also Schrijver's
[original algorithm](https://homepages.cwi.nl/~lex/files/minsubm6.pdf).
Only the existence of a deterministic polynomial implementation is
used here, not a claim of a new or best submodular-minimization bound.

This implements \(\lambda=1\) with no dependence on expanded
capacity. In particular the result handles cross-type local rank
constraints; it is not merely the coordinate-quota case renamed.

## 6. Binary bounded knapsack as an approximate available oracle

Suppose a player's local constraint is
\(\sum_j a_{pj}n_j\le b_p\), possibly together with coordinate
quotas, where costs are nonnegative and the available counts are
binary integers. For each type, split its allowed available count
into binary chunks of sizes \(1,2,4,\ldots\) with a final
remainder. The chunks have total size exactly that bound and their
subset sums realize every integer count up to it. There are only
\(O(\sum_j\log(c_j+1))\) chunks.

A chunk of size \(h\) has profit \(h v_j\) and cost
\(h a_{pj}\). Apply the self-contained deterministic profit-scaling
FPTAS from the approximate-oracle note to this ordinary finite
knapsack. Discard singleton-infeasible chunks first. Every feasible
count vector has a chunk representation in which each chosen chunk
is individually feasible, so this discarding loses no feasible vector.
The FPTAS returns a \((1-\kappa)\)-approximate available value
in time and workspace polynomial in the binary input and
\(1/\kappa\).

Convert its chosen chunks back to counts before interacting with the
allocation state. The subsequent minimalization removes single units
in type batches and may split chunks; this is legal because the local
count family is downward closed. The allocation star parameter remains
the unit value \(u=\max_jv_j\), not a large chunk profit. Chunks
are only private to the available-oracle implementation.

Choosing \(\kappa\) and the outer positive error as in the
approximate-oracle note gives ratio \(4-3/r+\zeta\), with
polynomial cost in the binary input and \(1+\zeta^{-1}\) outside
the same rank-sensitive search term. No exact solution to binary
knapsack is being asserted at rank one.

## 7. Scope and comparison boundary

The symmetry assumption is essential to the cell implementation.
If copies of one nominal type have different liking or feasibility
status, a type-count oracle does not identify which physical units
may be selected from an available cell. Such units must be split
into genuine types or handled by a different representation.

The integral polymatroids in Section 5 belong to individual players
and constrain their own resource-type counts. They should not be
confused with the arbitrary resource polymatroids of Bamas et al.,
which constrain the receiving-player vector of a resource. The latter
direction has the separate reservation obstruction, and the proved
laminar-resource adapter addresses only its stated class.

This is a representation and interface extension of the rank-sensitive
allocation method. Public all-player consequences and any novelty
claim require the same-model comparison already being maintained in
`item_matroid_allocation_public_scope_audit.md`; numerical capacities
alone are not asserted to create a new approximation record.
