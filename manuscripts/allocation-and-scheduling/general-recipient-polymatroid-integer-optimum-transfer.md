# Arbitrary integral recipient polymatroids: a direct rank-dependent allocation algorithm

**Reading order and supersession.** This note supplies the compressed
natural-matroid implementation, binary count bookkeeping, integer-optimum
contraction-loss lemma and fat reduction. Its displayed factor-five
bound is superseded by the factor-four refinement in
[recipient polymatroid proof](../../problems/recipient-polymatroid/proof.md), which imports
these prerequisites. Read that refinement for the current best result.
The recipient-matroid reservation algorithm extends to arbitrary integral
recipient polymatroids, with binary counts and value-oracle access, when
the comparator is **integer optimum**. The available capacity must be a
natural-matroid contraction rank, and its value certificate must be proved
against a fixed integral optimal basis. The aggregate count-configuration
LP is not a valid constant-factor comparator: see
[configuration-gaps.md](../../problems/allocation-lower-bounds/configuration-gaps.md).

The theorem below does not require a supplied matroid decomposition,
a bounded recipient rank, or expansion of numerical capacities. It uses
deterministic submodular minimization as a paid polynomial oracle operation.
The player-side local search, earliest exchanges and signature are the
already audited ones in [general-resource-all-remaining-blockers.md](general-resource-all-remaining-blockers.md).
All changes needed on the resource side are proved here.

## 1. Model and statement

There are q explicit players and a player-selection matroid M of rank r.
For each resource type j, a normalized, monotone, integer-valued submodular
function

$$
f_j:2^P\longrightarrow\mathbb Z_{\ge0}
$$

is supplied by a value oracle. A nonnegative integral recipient-count
vector n_.j is legal if

$$
n_.j(S)\le f_j(S)\quad\text{for every }S\subseteq P.
 \tag{P1}
$$

Each unit of type j has common rational intrinsic value v_j>=0. The
output selects a basis I of M and gives its players legal count vectors,
maximizing their minimum additive value. Unused resource capacity is
allowed. All counts and oracle values are binary encoded.

Optionally, each player has a type-symmetric downward-closed family

$$
\mathcal F_p\subseteq\prod_j\{0,\ldots,f_j(\{p\})\}.
 \tag{P2}
$$

For any integer availability vector A in this box, a paid deterministic
oracle returns n in F_p, n<=A, with value at least lambda times the best
feasible value in that box, where 0<lambda<=1 is a supplied rational
certified guarantee (or any supplied rational certified lower bound on
the oracle's guarantee). No such oracle is assumed
free or universally efficient. Without local restrictions, the exact
oracle simply returns A. Put tau=1/lambda and rho=(r-1)/r.

For r>=1, define d=tau+4rho. There is a deterministic algorithm with
integer-optimum approximation factor

$$
\boxed{d\quad\text{in }2^{O(r)}\mathrm{poly}(H),}
 \tag{P3}
$$

or, for a positive rational accuracy parameter eta, factor d+eta in

$$
\boxed{\mathrm{poly}(H)
 \min\{2^{O(r)},(r+1)^{O((1+\eta^{-1})\log(r+1))}\}.}
 \tag{P4}
$$

H includes the explicit player/type input, all numerical bit lengths,
recipient value-oracle and submodular-minimization work, player-matroid
work, and available-bundle oracle work. The wrapper has polynomial
space in H, in addition to supplied oracle workspace. In particular,
there is no factor proportional to sum_j f_j(P), or to the number of
conceptual service copies. With exact unrestricted availability this
gives d=5-4/r. Rank zero is the empty allocation. Rank one is exact with
the unrestricted exact oracle, but no exactness assertion is made for an
approximate local oracle.

## 2. A conceptual natural matroid with a binary rank oracle

Fix a resource j and write f=f_j. For each player p, imagine a block
E_p of F_p=f({p}) distinct service copies. A subset is independent when
its vector of block counts belongs to P(f). This is a matroid: downward
closure is immediate, and integer-polymatroid augmentation supplies an
owner block with an unused element when augmenting one independent set
by a larger one. This conceptual matroid is never explicitly constructed.

For a set W with block counts z_p, its rank is

$$
R(z)=\min_{S\subseteq P}\{f(S)+z(P\setminus S)\}.
 \tag{P5}
$$

One proof uses box restriction of an integral polymatroid: the largest
sum of a vector h in P(f), 0<=h<=z, is the right side of (P5).
The box-restricted rank function is

$$
f_z(A)=\min_{S\subseteq A}\{f(S)+z(A\setminus S)\},
$$

which is normalized, monotone, integral and submodular, and satisfies
P(f_z)=P(f) intersect [0,z]. These facts and their uncrossing proof are
also recorded in [type-symmetric-downward-closed-binary-allocation.md](type-symmetric-downward-closed-binary-allocation.md).
Thus a greedy base of f_z attains f_z(P), proving (P5).

Expression (P5) is a submodular-minimization query, plus a modular
constant. Its bit cost is polynomial in the original oracle bounds and
the bit lengths of z. The full block union E_S has rank f(S).

## 3. State and numerical availability

Maintain the same current matching records, selected centers, disjoint
designated groups D(c), layers and owner matroid as in the accepted
recipient-matroid algorithm. Matching owners are distinct; selected
owners may repeat in different layers. Every record stores an integer
count vector and is minimal above B>0. Let Y be the union of designated
matching groups and X the selected records.

For resource j, define the reserved multiplicity vector

$$
z^j_p=\sum_{c\in X:p(c)=p}n^c_j
             +\sum_{b\in Y:p(b)=p}n^b_j.
 \tag{P6}
$$

For a candidate owner p, replace coordinate p of z^j by f_j({p}),
obtaining z^(j,p). Its available count of type j is

$$
A_{pj}=R_j(z^{(j,p)})-R_j(z^j).
 \tag{P7}
$$

This is a nonnegative integer. It is at most f_j({p})-z^j_p.
Conceptually, it is r(W_j union E_pj)-r(W_j): the rank of the player's
remaining service copies after contracting the entire reserved set.

All unused copies in a player block are symmetric. Consequently, for
any 0<=a<=A_pj, an arbitrary a-element subset C of E_pj outside W_j
satisfies

$$
r(W_j\cup C)=r(W_j)+a.
 \tag{P8}
$$

For completeness, in (P5) partition the minimizers into those containing
p and those not containing p. Increasing z_p by a changes their two
candidate minima from (U,V) to (U,V+a). The rank increase is therefore
min(a,A_pj) until all unused p copies have been added. This proves (P8)
without inspecting individual copies.

At the current last layer, scan players outside
cl_M(I\owners(Y_<i)), compute their entire availability vectors (P7),
and invoke the available-bundle oracle. A returned value at least B
is pruned to a minimal B-bundle. If every returned value is below B,
the scan is completed at that unchanged state.

Pruning is numerical: for each positive-value type j, remove in one
batch the smaller of its count and floor((current value-B)/v_j).
After one pass, every remaining individual unit is essential. No loop
depends on a numerical multiplicity. Zero-value units can be removed
by downward closure, so they need not be stored.

## 4. Distinct service identities and compressed storage

The following conceptual bookkeeping invariant suffices:
for every player p and resource j, all service copies assigned to its
current matching record and all its selected records are distinct.
Their total count is at most f_j({p}).

Initially this is empty. If an eligible candidate owner p is currently
matched, its old matching record must lie in the earlier blocker prefix;
otherwise p belongs to the eligibility base and cannot be outside its
span. Thus that whole old record is included in (P6). Every old selected
record is included as well. Bound (P7) consequently supplies enough
unused p copies for the new candidate. If p is not matched, there is
no other matching record owned by p. This proves the invariant at every
new center or fresh free candidate.

Exchanges delete an old record, move the incoming center's own copies
to its new matching record, and retire or discard selected records.
These operations preserve distinctness. A stored incoming center's
counts must be saved or installed before its selected record is retired.
Repeated owner names never cause records or their numerical bundles to
be identified.

The algorithm need not store actual copy IDs. For each of at most 2r
record labels it stores one count vector, together with owner and layer
flags. The disjoint-copy execution just proved witnesses all numerical
operations in one fixed conceptual universe. Alternatively, all ranks
and reservations depend only on the counts. A lower layer's unchanged
record vectors give exactly the same rank and availability queries.

## 5. Universal reservations and completion

For every subset Z of selected records and each resource j, maintain

$$
Q_j(Z)=\sum_{b\in\mathcal M\setminus D(Z)}n^b_j e_{p(b)}
                 +\sum_{c\in Z}n^c_j e_{p(c)}\in P(f_j).
 \tag{P9}
$$

This is an invariant for every actual subset Z. The algorithm never
enumerates or tests those subsets.

For a new candidate c, designate as D(c) all current matching records
outside Y. Equivalently, one may use only such records that have a
positive count in some resource type used by c. The latter rule keeps
the same proof and restores the shared-resource sharp coefficient.

Fix an old subset Z and a resource j used by c. After deleting D(c),
all remaining matching copies at j belong to marked records. Together
with the old selected copies from Z they form an independent subset
H of the reserved W_j. The candidate contributes n^c_j copies of its
owner p, and n^c_j<=A_pj. By (P8), these copies are independent over W_j,
so they are independent over H. The new reservation is feasible.
At a resource not used by c, only old elements are deleted. This proves
every new reservation in (P9), while old subsets are unchanged.

The same argument works for relevant-only completion: at every used
resource it deletes all unmarked matching copies at that resource.
It does not matter that a recipient may own many units of a resource.

## 6. Free exchanges and old-prefix preservation

An empty designated group certifies a candidate jointly feasible with
every subset of the other selected records, by (P9). For a fresh empty
group, Section 5 gives the same assertion. Use the existing earliest
player-circuit rule to augment, or remove one earlier matching record
and install the incoming bundle.

For any retained selected subset, the new reservation is a deletion
from its old reservation plus the incoming bundle. Joint feasibility
was just established. If the deleted matching record had already been
excluded by its designated group, removing both the record and that
group membership does not reintroduce any service. The new matching
record receives a new identity and no old blocker flag.

Only one designated group can become empty after deleting one record;
process its center immediately. Truncation releases higher groups but
does not delete their matching allocations. Each cascade proceeds to
an earlier layer exactly as in the original proof.

Below the earliest player-exchange layer, the selected and designated
matching records remain literally the same records with the same count
vectors. Hence (P6)--(P7) are unchanged. The existing earliest-circuit
lemma preserves their player eligibility flats. Their completed failed
scans remain valid. Only the last retained layer requires refresh.
No assertion about current actual recipient circuits is used.

## 7. The crucial integer-optimum cover lemma

Let J be the current eligibility base and w=r-r_M(J)>0. Suppose a
completed scan finds no available bundle of value B. Define

$$
\Phi=\sum_j v_j R_j(z^j).
 \tag{P10}
$$

Assume an integer target allocation of value at least T exists on a
basis I* of M. Let E=I*\cl_M(J). Then |E|>=w. Restrict that allocation
to E, writing n*_.j for its count vector at resource j.

For each resource, contract the conceptual reserved set W_j and group
the remaining service copies by player. The resulting integral
polymatroid rank function is

$$
g_j(S)=r_j(W_j\cup E_{S,j})-r_j(W_j).
 \tag{P11}
$$

It satisfies g_j({p})=A_pj and

$$
g_j(S)\ge f_j(S)-R_j(z^j),
 \tag{P12}
$$

since r_j(W_j union E_S,j)>=r_j(E_S,j)=f_j(S).

Box restriction of g_j by the integral vector n*_.j gives an integral
vector h_.j<=n*_.j, h_.j in P(g_j), with

$$
\begin{split}
 h_.j(P)
 &=\min_{S\subseteq P}\{g_j(S)+n*_.j(P\setminus S)\}\\
 &\ge n*_.j(P)-R_j(z^j).
 \end{split}
 \tag{P13}
$$

The last inequality uses n*_.j(S)<=f_j(S). Thus at most R_j(z^j)
units of that resource have been removed. This vector is needed only
for the proof; the algorithm neither knows I* nor computes h.

For each p in E, the vector h_p is coordinatewise at most its old
feasible n*_p, so it remains in F_p. It also satisfies h_pj<=A_pj.
By the failed approximate-oracle scan, its value is strictly below
tau B. The original value was at least T. Summing the lost value,
and using (P13), proves

$$
\Phi>(T-\tau B)|E|\ge(T-\tau B)w
       \qquad\text{when }\tau B\le T.
 \tag{P14}
$$

This is the required strict lower cover inequality. It uses an integer
optimal basis, not fractional player masses. Replacing this proof by
a per-player fractional restriction argument would be incorrect in
general; the separate gap note gives a rank-sized counterexample.

## 8. Current upper cover and progress

Matroid rank is at most the number of reserved service copies. Every
minimal B-bundle has value below B+u, where u is the maximum positive
unit value. Stable designated groups are disjoint and nonempty, so
|X|<=|Y|. Therefore

$$
\Phi\le 2(B+u)|Y|.
 \tag{P15}
$$

For relevant-only completion, each designated blocker shares a used
type, hence a common unit value, with its center. The existing singleton
and nonsingleton star argument gives the sharper coefficient

$$
C_R(B,u)=\max\{2u,\,2B+2\min(u,B)\},\qquad
                         \Phi\le C_R(B,u)|Y|.
 \tag{P16}
$$

A center consisting of one unit of value at least B has only one-unit
minimal blockers. Otherwise every unit in it is below B; any sharing
minimal blocker also has no unit of value at least B. Counts greater
than one do not change this argument.

For a phase with k<r matched players and s earlier blockers,
w=r-k+s and s/w<=rho. Consequently an empty completed new layer is a
valid certificate of nonexistence of an integer target-T allocation if

$$
\tau B+\rho C_R(B,u)\le T,
 \tag{P17}
$$

or if its coarse counterpart using 2(B+u) holds. For a positive gap
Delta=T-tau B-rho C_R, use growth

$$
|Y_i|>\gamma(r-k+|Y_{<i}|),\qquad
 \gamma=\min\{1/2,\Delta/(2C_R)\}.
$$

The old micro-signature (-|X_1|,|Y_1|,...,infinity) strictly decreases
at every charged action. Completion, one-record earliest exchanges,
immediate empty-group cascades, and completed fresh scans have exactly
the interfaces required by that proof. The number of states is
2^{O(r)} at the boundary, or
(r+1)^{O(gamma^(-1) log(r+1))} with positive growth. There are at most
r augmentation phases.

## 9. Fat units and the integer dual-union reduction

Set d=tau+4rho and B0=T/d. A resource type is fat if its unit value
is at least B0. For each fat type j, cap its recipient polymatroid
coordinatewise by one. This is a matroid N_j with rank

$$
r_{N_j}(S)=\min_{A\subseteq S}\{f_j(A)+|S\setminus A|\}.
 \tag{P18}
$$

Restrict its ground set to players for whom one unit of type j is
locally feasible. Testing a positive-factor feasible oracle on e_j
decides that singleton condition exactly whenever f_j({p})>=1.
Take N to be the union of these fat matroids, and U=M* vee N.
Independence queries in (P18) use deterministic submodular minimization;
ordinary matroid union, duality and decomposition have polynomial cost.

If a target-T integer allocation exists, split its selected basis into
players with at least one fat unit and players with only small units.
Choose one fat unit for each of the former. Their set is independent
in N, by restriction of the legal integral recipient counts. Together
with the complement of the selected basis it gives an independent set
of U. Extend it to a U-basis. Its complement is a U*-basis contained
in the original all-small players, so their original small allocations
supply an integer target-T promise for the derived player matroid U*.
Its rank r' is at most r.

Run the small-resource algorithm on U*. On success, decompose the
complementary U-basis into an M*-independent part and an N-independent
part. Extend the former to an M*-basis, discard any allocated players
thereby removed, and give one fat unit to each surviving N-part player.
The remaining selected set is a basis of M. The small and fat resource
types are disjoint, and deleting recipients preserves (P1) and local
downward-closed feasibility. If r'=0, only this reconstruction is needed.

At B=B0 and u<B0, the coarse condition holds because

$$
\tau B0+2\rho_{r'}(B0+u)\le(\tau+4\rho)B0=T.
$$

For eta>0 retain the same fat threshold and put B=T/(d+eta). With
Cbar=2(B+B0),

$$
T-\tau B-\rho Cbar=(\tau+2\rho)(B0-B).
$$

Since tau+2rho>=d/2, the same uniform choice
gamma=min(eta,1)/64 as in the recipient-matroid proof is valid. This
proves (P3)--(P4) against integer optimum.

## 10. Paid operations and finite bit complexity

Every rank or residual query in (P5)--(P7) minimizes an integer
submodular function on q explicit elements, with a modular term whose
bit length is polynomial in H. Each stored count is at most its
singleton bound; summing at most 2r records adds only O(log(r+1)) bits.
Whole-state scans use polynomially many such queries. Batched pruning,
group changes, record moves and dual/union operations all have polynomial
bit cost and oracle work. No call enumerates capacities, service copies,
selected subsets, or rank-function values over all subsets.

The common rational value denominator gives a finite utility grid. Total
delivered value is at most V=sum_j v_j f_j(P), with polynomial encoding
length. Target zero is feasible by choosing any player basis and giving
empty bundles. A grid target above (d+eta)V cannot be returned as a
success, so supplies an initial failed upper endpoint. The one-sided
target search uses only sound integer infeasibility of failed targets;
it does not assume the algorithm's successful-target set is monotone.
Polynomially many grid-binary trials give the stated approximation to
the integer optimum. The exact-d version uses its corresponding bound.

## 11. Equal-unit core, with its integer rounding made explicit

If all units have value one and the search quota is an integer b>=1,
every minimal bundle has exactly b units. Thus the coarse current cover
improves to Phi<=2b|Y|. The direct sufficient condition is

$$
(1+2\rho)b\le T.
 \tag{P19}
$$

With the exact available oracle and an integral target t, every failed
available residual value is at most b-1. The proof of (P14) then gives
Phi>=(t-b+1)w. A sufficient strict contradiction is

$$
(1+2\rho)b<t+1.
 \tag{P20}
$$

These are quota guarantees. They do not automatically assert a uniform
3-2/r multiplicative approximation after rounding b to an integer. For
example, when r is large, t=4 does not make quota b=2 satisfy (P20).
Any two-value or makespan transfer must retain this arithmetic issue
or prove a separate repair. Positive fractional quota slack still gives
the same rank-quasipolynomial signature bound.

## 12. Comparison and remaining distinctions

The public Bamas--Lindermayr--Megow--Rohwedder--Schloeter theorem gives
polynomial 8+epsilon for general recipient matroid/polymatroid allocation
and 4+epsilon for the two-value compulsory-player case; see
[arXiv:2307.08453v1](https://arxiv.org/html/2307.08453v1), Theorem 4.
The dummy dual-resource adapter supplies its integer guarantee for
arbitrary player selection. The present construction changes the
quality/time tradeoff and also permits the explicit local-oracle
interface. It does not claim that the public polynomial runtime is
preserved, or that its two-value factor is improved without another
argument.

Natural-matroid representations of integral polymatroids are classical;
see Bonin, Chun and Fife,
[*The natural matroid of an integer polymatroid*, arXiv:2209.03786](https://arxiv.org/abs/2209.03786).
The new ingredient here is their compressed contraction-availability
use inside the universal reservation search and the integer-optimum
loss certificate (P13)--(P14). No priority claim beyond the checked
comparison is asserted. The complete proof has passed root and
independent mathematical review; it has not received external peer review
or formal verification.
