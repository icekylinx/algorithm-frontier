# Compressed nonlinear utility, cost, and load transfers under a global polymatroid

**25 October 2026. Complete incremental theorem and proof; accepted
after a full root review and an independent full review in
`compressed_nonlinear_transfer_audit.md`.** This manuscript adds a nonlinear
input model to the previously reviewed global-polymatroid profile
schemes. It does not change the original matching exponent.

Nondecreasing separable concave utilities and nondecreasing separable
convex assignment costs can be represented by a polynomial number of
binary-length marginal bands. The bands share the original resource
capacity. An arbitrary integral band allocation can be repacked into
prefix order without decreasing utility or increasing actual cost.
This gives an exact reduction of the integer optimum, including a
mandatory resource base, an actual selected player-matroid basis,
and one exact shared setup-plus-assignment budget.

The corresponding scheduling reduction works for nondecreasing
separable convex processing loads and convex assignment costs.
Prefix repacking decreases both load and cost. No capacity is expanded
into individually represented units.

The resulting guarantees are

    Fair allocation: (1-epsilon)OPT in
      binomial(q,r) exp(O(r/epsilon)) poly(H_epsilon).

    Mandatory scheduling: (1+epsilon)OPT in
      exp(O(q/epsilon)) poly(H_epsilon).                         (NB1)

Both use polynomial binary workspace and preserve the original real
cost budget exactly. Here q counts the original objective blocks,
r is the selected player rank, and H includes the complete marginal-
band descriptions. The number of bands enters only the polynomial
input factor. One-block refinements and exact numeric-target
consequences are stated separately below.

## 1. Original resource model and explicit function domains

Let E be an explicit coordinate ground, partitioned into disjoint
recipient or machine blocks

    E=disjoint_union_(p in P) E_p,      |P|=q.

Let F:2^E -> Z_nonnegative be normalized, monotone and submodular,
given by an exact rank oracle. Write

    P(F)={x>=0: x(S)<=F(S) for every S subset E},
    R=F(E),   B(F)={x in P(F):x(E)=R}.                           (NB2)

All x coordinates are integers. There may also be an original
eligibility mask A_0. A coordinate e has an explicit finite integer
domain 0<=x_e<=d_e. The domain endpoint is binary encoded. It may
be taken to be F({e}); if a larger endpoint is supplied, truncate its
unused tail to F({e}). A smaller endpoint is a genuine hard domain
constraint, not permission to reduce a mandatory resource total.

The two resource conventions are:

- **Optional resource:** x is in P(F), obeys the domains and the
  eligibility mask, and may leave resource rank unused.
- **Mandatory resource:** x is in B(F), obeys the same restrictions,
  and must still have the ORIGINAL total R from NB2.

Rank loss under a domain, eligibility, or selected-block restriction
can make the mandatory model infeasible. Its required total is never
silently replaced by a smaller restricted rank.

Every coordinate function is defined on the whole integer interval
{0,...,d_e}. A list that stops earlier does not implicitly extend by
its last marginal: its endpoint must instead be declared as the hard
domain. For d_e=0 the coordinate is forced to zero and needs no bands.

In allocation, e has utility U_e and assignment cost C_e satisfying

    U_e(0)=C_e(0)=0,
    U_e(k)-U_e(k-1) >= U_e(k+1)-U_e(k) >=0,
    0<=C_e(k)-C_e(k-1) <= C_e(k+1)-C_e(k).                      (NB3)

Thus utility is nondecreasing and discretely concave; cost is
nondecreasing and discretely convex. These properties are per
coordinate. The total utility of player p is sum_(e in E_p) U_e(x_e).
No arbitrary interaction between distinct coordinates is allowed.

For scheduling, replace U_e by a processing-load function P_e with

    P_e(0)=0,
    0<=P_e(k)-P_e(k-1) <= P_e(k+1)-P_e(k),                      (NB4)

and retain the convex cost condition. The load of machine p is
sum_(e in E_p) P_e(x_e). This is a count-dependent load model;
it does not introduce a separate sequencing or precedence problem.

## 2. Binary marginal bands and common refinement

Functions are supplied by explicit constant-marginal intervals with
integer endpoints and nonnegative rational slopes. After merging
the endpoints of the utility/load and cost descriptions, write

    0=b_(e,0)<b_(e,1)<...<b_(e,m_e)=d_e,
    ell_(e,i)=b_(e,i)-b_(e,i-1)>0.                              (NB5)

On the integer steps b_(e,i-1)+1,...,b_(e,i), the utility marginal is
u_(e,i), the processing marginal is p_(e,i) when scheduling, and
the cost marginal is c_(e,i). The common refinement has at most
the sum of the original lists' sizes. It does not enumerate the
integer points between endpoints.

For a count k, define its canonical prefix-band vector by

    z^*_(e,i)(k)=min{ell_(e,i), max{0,k-b_(e,i-1)}}.             (NB6)

The original function values are exactly

    U_e(k)=sum_i u_(e,i) z^*_(e,i)(k),
    P_e(k)=sum_i p_(e,i) z^*_(e,i)(k),
    C_e(k)=sum_i c_(e,i) z^*_(e,i)(k).                         (NB7)

The utility slopes are nonincreasing; load and cost slopes are
nondecreasing. Equal and zero slopes are permitted. Zero-utility
bands with positive cost are retained when needed by a mandatory
base. Zero-load bands are also retained. An algorithm cannot simply
delete such coordinates before checking the original total.

Let N=sum_e m_e be the number of refined bands. H includes E, its
block partition, all N bands, their binary lengths and rational
slopes, the original rank encoding, and the cost/setup data. It also
accounts for polynomial exact rank, SFM, LP, and polymatroid-
intersection work. As usual,

    H_epsilon=H+size(epsilon),  0<epsilon<=1,                    (NB8)

includes the full rational accuracy numerator and denominator.

## 3. A shared-capacity rank on the band coordinates

Let D={(e,i):1<=i<=m_e} be the band ground, and let pi map each band
to its original coordinate. Each band belongs to the same objective
block as e. Define a preliminary rank

    H_0(S)=F(pi(S)),       S subset D.                          (NB9)

This is an integral polymatroid rank. Normalization and monotonicity
are immediate. For submodularity, pi(A union B)=pi(A) union pi(B),
while pi(A intersect B) is contained in pi(A) intersect pi(B).
Submodularity of F followed by its monotonicity gives the claim.

For z>=0 on D, aggregate its counts by

    x_e=sum_i z_(e,i).                                        (NB10)

Then

    z in P(H_0)   if and only if   x in P(F),                  (NB11)

where coordinates without a band have aggregate zero. To prove the
forward direction, test the full band inverse image of every
original subset A. Its band sum is x(A), and its H_0 rank is at most
F(A). For the reverse direction, for any S subset D,

    z(S)<=x(pi(S))<=F(pi(S))=H_0(S).

Thus the construction shares the original capacity across all bands;
it does not make m_e independent resource copies of coordinate e.

## 4. Band capacities preserve one polymatroid

Let ell be the modular vector of positive integer band lengths.
Define

    G(S)=min_(T subset S) {H_0(T)+ell(S minus T)}.              (NB12)

Then G is a normalized monotone integral submodular rank, and

    P(G)=P(H_0) intersect {0<=z<=ell}.                         (NB13)

Here is a complete proof. Normalization and integrality follow
directly. For monotonicity, let A subset B and let T minimize NB12
for B. The candidate T intersect A for A has no larger H_0 rank
and no larger remaining modular cost, proving G(A)<=G(B).

For submodularity choose minimizing T_A subset A and T_B subset B.
Submodularity of H_0, together with modularity of ell, gives

    H_0(T_A)+ell(A minus T_A)+H_0(T_B)+ell(B minus T_B)
      >=H_0(T_A union T_B)
          +ell((A union B) minus (T_A union T_B))
        +H_0(T_A intersect T_B)
          +ell((A intersect B) minus (T_A intersect T_B)).

The right-hand candidates bound G(A union B)+G(A intersect B)
from above. This proves the required submodular inequality.

If z is in P(H_0) and z<=ell, every decomposition of S into T and
S minus T gives z(S)<=H_0(T)+ell(S minus T), so z is in P(G).
Conversely G(S)<=H_0(S), and G({a})<=ell_a by choosing T empty.
These imply P(G) subset P(H_0) and the coordinate box, proving NB13.

The rank can be evaluated by exact SFM on the ORIGINAL coordinate
ground. In a minimizer of NB12, once any band of a coordinate is
included in T, including all its bands present in S leaves H_0
unchanged and cannot increase the modular remainder. Consequently

    G(S)=min_(A subset E)
          {F(A)+sum_(e notin A) ell(S intersect pi^(-1)(e))}.
                                                                  (NB14)

Coordinates outside pi(S) may be removed from A by monotonicity.
The minimized function is F plus a known modular function. Its
rank values and modular coefficients have polynomial bit length.
No unit-capacity expansion is required to implement this oracle.

Combining NB11 and NB13 proves the exact projection identity

    {aggregate(z): z in P(G)}
       =P(F) intersect {0<=x_e<=d_e for every e}.              (NB15)

The reverse inclusion uses the canonical vector NB6, which has the
desired aggregate and obeys every band capacity. This identity holds
for real as well as integer vectors. In particular, integer x has
an integer canonical lift and integer z has an integer aggregate.

## 5. Original full ranks, domains, and masks

Totals agree under aggregation: z(D)=x(E). Also G(D)<=F(E)=R.
Hence an original mandatory-domain base exists if and only if
G(D)=R. In that case, for a band vector satisfying 0<=z<=ell,

    z in B(G)  if and only if
    aggregate(z) in B(F) with all original domains.            (NB16)

More generally one can always require z(D)=R explicitly; if the
current rank is lower, that face is empty. This remains the rule
after every eligibility or selected-block mask.

If d_e=F({e}) for every original coordinate, the unmasked rank is
automatically R. Indeed F(A)+sum_(e notin A)F({e})>=F(E) by
submodularity, and NB14 has equality at A=E. Shorter hard domains
can decrease the available rank, and that decrease must be tested.

A mask A on original coordinates permits exactly the full fibers
D_A=pi^(-1)(A). Restrict G to D_A. By NB15 its independent vectors
project exactly to the original masked, domain-bounded independent
vectors. For mandatory resources require G(D_A)=R and retain that
same R in every subsequent LP and integral recovery.

Target routines may internally mask only some band coordinates.
Their outputs still lie in P(G) and can be decoded by NB15. The
later canonical repacking is allowed to use a different band of
the SAME original coordinate: these internal band masks are proof
devices, not new original eligibility requirements. No count moves
to a forbidden original coordinate or a different objective block.

## 6. Canonical prefix repacking gives simultaneous domination

Fix an original coordinate e and an arbitrary feasible band vector
z_(e,1),...,z_(e,m_e), with total k. Write Z_h for its cumulative
count through band h and Z_h^* for the canonical cumulative count.
Then

    Z_h<=min{k,b_(e,h)}=Z_h^*,   and Z_(m_e)=Z^*_(m_e)=k.       (NB17)

For any slopes a_1,...,a_m, summation by parts gives

    sum_i a_i(z_i^*-z_i)
      =sum_(h<m) (a_h-a_(h+1))(Z_h^*-Z_h),                    (NB18)

because the total difference is zero. Thus prefix repacking

- weakly INCREASES a nonincreasing marginal utility sum;
- weakly DECREASES a nondecreasing marginal cost sum;
- weakly DECREASES a nondecreasing marginal processing-load sum.

The same canonical vector simultaneously has all three relevant
properties. It keeps x_e unchanged, so NB15 keeps the entire global
resource vector feasible. Its total is unchanged, including when
the original resource base is mandatory.

In particular every band allocation z has an original aggregate x
with

    sum_(e in E_p) U_e(x_e)
       >=sum_((e,i) in D_p) u_(e,i)z_(e,i),

    sum_e C_e(x_e)<=sum_(e,i)c_(e,i)z_(e,i),                    (NB19)

and, for scheduling,

    sum_(e in E_p) P_e(x_e)
       <=sum_((e,i) in D_p)p_(e,i)z_(e,i).                     (NB20)

The inequalities are valid with ties, zero slopes, and binary-large
counts. Canonical reconstruction is performed directly using NB6
in O(N) arithmetic operations on binary data. The argument does
not execute one exchange for every individual unit.

There is deliberately no explicit prefix-order constraint in the
lifted optimization problem. Band capacities and the shared rank
give one integral polymatroid. Prefix order is imposed afterward
by domination, avoiding an extra resource intersection.

## 7. Exact integer optimum correspondence, including setup fees

For allocation, let M be an original player matroid of rank r>=1
on P. The selected recipients must form an ACTUAL basis B of M.
Counts are supported on

    A_B=A_0 intersect union_(p in B) E_p.

Each selected player p has a nonnegative rational setup fee sigma_p.
The original budget and max-min objective are

    sigma(B)+sum_e C_e(x_e)<=C,
    min_(p in B) sum_(e in E_p) U_e(x_e),     C>=0.             (NB21)

For fixed B, use G on its allowed bands, the linear utility slopes
u, linear cost slopes c, the same setup fee, and the same optional
or mandatory total convention. Then the original nonlinear and
lifted linear INTEGER optimal max-min values are exactly equal.

To prove one direction, canonically lift any original feasible x.
Every utility and cost is identical by NB7, so it is an equally
good feasible lifted allocation. For the other direction, aggregate
any lifted feasible z. NB19 increases each selected utility and
does not increase assignment cost; B and its setup cost stay fixed.
The aggregate remains feasible by NB15 or NB16. The two opposite
optimal-value inequalities give equality. Feasibility itself is
equivalent by the same two maps.

Taking the maximum over actual M-bases preserves this equality.
It does not use a fractional or randomized selected basis. Setup
charges are not reassigned between selected sets.

For mandatory scheduling with all q fixed machine blocks, the
original budget is sum_e C_e(x_e)<=C and the objective is

    max_(p in P) sum_(e in E_p) P_e(x_e).                      (NB22)

The minimum nonlinear objective equals the minimum lifted linear
objective. A canonical original witness gives one inequality;
NB20 and the cost inequality give the reverse one. The original
full resource total R is retained in both directions.

These equalities concern the integer optimization problems. The
profile guarantees used below retain their original integer
comparators; no stronger fractional approximation statement is
inferred merely from the real projection identity NB15.

## 8. Approximation schemes and exact initialization

Apply the already proved global linear profile interfaces to G:

- global_polymatroid_profile_transfers.md for optional-resource
  allocation and mandatory scheduling;
- mandatory_base_fair_allocation_passive_lift.md for mandatory-
  resource allocation;
- arbitrary_processing_six_profile_three_halves.md and its global
  transfer for the fixed factor-three-halves endpoint.

The nonlinear reduction has just established every required resource,
mask, cost, and comparator interface. Therefore it gives:

**Theorem NB-A.** Under NB2–NB3 and NB21, either resource convention
admits an actual feasible (B,x) with utility at least
(1-epsilon)OPT in

    binomial(q,r) exp(O(r/epsilon)) poly(H_epsilon)              (NB23)

time and polynomial binary space, or the algorithm detects original
infeasibility. Its real budget is at most C exactly.

**Theorem NB-S.** Under NB2, NB4 and NB22, mandatory scheduling
admits makespan at most (1+epsilon)OPT in

    exp(O(q/epsilon)) poly(H_epsilon)                          (NB24)

time and polynomial binary space, with the original cost budget
exact. A factor 3/2 output also follows in 6^q poly(H) time and
polynomial space. These guarantees apply to the count-dependent
load functions themselves after canonical reconstruction.

For optional-resource allocation, zero counts incur zero assignment
cost and zero utility. Thus an affordable actual setup basis gives
the initial feasible zero-target output; minimum-setup matroid basis
optimization decides whether such a basis exists.

Mandatory allocation has a different initializer. Enumerate actual
r-element player bases. For each B first check sigma(B)<=C, then
G(D_(A_B))=R, and finally minimize linear band cost on the total-R
base face. Its minimum equals the minimum original nonlinear cost
by the canonical correspondence. A successful candidate gives an
actual integer feasible original base. All candidates failing proves
original infeasibility. No exponentially large feasible-basis list
is retained.

For fixed-machine mandatory scheduling, perform the same rank and
minimum-cost test on the original allowed band ground. The zero-
makespan test masks positive processing slopes and retains R. It is
exact: a zero original-load witness canonically uses only zero-load
bands, and a zero-load lifted witness decodes to nonnegative original
loads that are no larger, hence also zero.

If R=0, every mandatory allocation is zero. For r=0 the selected
set is empty; take its objective convention to be zero, with an
optional zero resource vector, or a mandatory zero vector only
when R=0. All-zero utility, load, or cost descriptions are permitted.
The profile search can keep any actual feasible initializer at a
zero utility target; it does not need a positive-OPT promise.

The underlying profile schemes use exact rational target grids.
Every nonlinear utility or load at integer counts is a sum of the
listed marginal slopes with integer multiplicities. Thus a rational
grid dividing these slopes also divides every original objective.
The existing target-search proofs apply with polynomial bit length.

## 9. One-block nonlinear versions of the seven scalar problems

There is a useful one-block extension beyond the upper-budget model.
For a separable objective V(x)=sum_e V_e(x_e), use nonnegative
nonincreasing marginals when MAXIMIZING and nonnegative nondecreasing
marginals when MINIMIZING. For the one separable side function W,
use the curvature in this table:

| Desired direction | Marginal order for canonical domination |
| --- | --- |
| Maximize V | nonincreasing objective marginals |
| Minimize V | nondecreasing objective marginals |
| W(x)<=L | nondecreasing side marginals |
| W(x)>=L | nonincreasing side marginals |

Normalize every coordinate function to zero at zero and refine the
objective and side breakpoints jointly. NB18 shows that canonical
prefix repacking improves the objective in the chosen direction and
preserves the side inequality in its chosen direction. Original
canonical witnesses preserve both quantities exactly. Hence the
nonlinear one-block optimum equals that of the lifted linear instance
for every descriptor. This is still only ONE side condition.

The seven-variant theorem and its reviewed explicit refinement now
give the respective (1+epsilon) MIN or (1-epsilon) MAX guarantees in

    epsilon^(-1) exp(141/(50epsilon)+7) poly(H_epsilon)          (NB25)

time and polynomial binary space. Optional independent vectors and
mandatory bases are both supported. Minimum independent objective
under an upper side threshold remains the trivial zero solution.

The exact side-feasibility initializer is also inherited correctly:
minimize lifted side weight for an upper condition and maximize it
for a lower condition. The canonical correspondence proves that
these extrema decide the original nonlinear condition exactly.
No lower covering constraint is combined with a second hard budget
on the same recovered vector.

## 10. Integer marginal objectives and exact numeric targets

Suppose the objective marginals in the one-block model are all
nonnegative integers. The side marginals may remain nonnegative
rationals, as allowed by the exact linear target interface. In
particular the following applies when every supplied marginal slope
is a nonnegative integer.

Apply exact_numeric_target_single_matroid_scheme.md to the lifted
instance. For a nonlinear target T in Z_nonnegative,

- MAX asks whether an original legal x has V(x)>=T;
- MIN asks whether an original legal x has V(x)<=T.

Canonical original witnesses lift with equality, while arbitrary
lifted outputs decode in the correct one-sided direction. Thus
the target answers are exact, including returned original witnesses,
in

    2^{O(sqrt(T+1))} poly(H+size(T))                           (NB26)

time and polynomial binary space. Exact optimization follows in
2^{O(sqrt(OPT+1))} poly(H). The MAX charged active/passive step of
that theorem operates on the already capacity-bounded band rank G;
after merging those copies, NB19 performs the final nonlinear
decoding. All genuine side costs remain present throughout.

For rational marginal objectives, choose an explicit positive grid
g dividing them and scale the objective by 1/g. The numerical
parameter is then T/g on grid targets, or OPT/g in optimization:

    2^{O(sqrt(OPT/g+1))} poly(H).                              (NB27)

A general rational target uses ceil(T/g) for MAX and floor(T/g)
for MIN. A denominator-clearing scale can be binary-large; the
exponent depends on that SCALE and is not a bound only in the
unscaled displayed value of OPT.

Exact objective EQUALITY does not follow from this reduction.
Canonical repacking can strictly improve a lifted objective, so it
need not preserve an equality to T. For example, one optional
coordinate of capacity two with utility marginals 2,1 has original
utilities 0,2,3, while the nonprefix lifted vector using only the
second band has linear utility one. The one-sided targets and
optimum correspondence above do not make that equality feasible.

### 10.1 Exact numeric targets for several original objective blocks

The fully reviewed block interface in
block_global_exact_numeric_target_schemes.md gives a stronger
consequence when all UTILITY marginals in NB21, or all PROCESSING
marginals in NB22, are nonnegative integers. Assignment-cost
marginals and setup fees may remain nonnegative rationals.

For an actual selected rank-r block basis and an integer target
T>=0, the following questions are decided exactly, with an actual
original integer witness on success:

- allocation, with either resource convention: every selected
  player has nonlinear utility at least T;
- mandatory scheduling: every selected machine has nonlinear
  processing load at most T.

The time is

    binomial(q,r) exp(O(r sqrt(T+1)))
       poly(H+log(T+1)),                                      (NB28)

with polynomial binary workspace and the original exact shared
setup-plus-assignment budget. Fixed compulsory blocks use r=q
and no binomial factor. For T>=1 the explicit profile factors are
exp(3r sqrt(2T-1)) for fairness and exp(3r sqrt(T)) for scheduling.

The lifted theorem groups exact positive marginal values separately
inside each selected block. Optional allocation retains only its
prescribed useful-unit total. Mandatory allocation marks surplus
units passive and uses one GLOBAL zero/passive group to fill the
original total R. Scheduling likewise fills R with one global
zero-time group. This is compatible with G even when F couples
all original blocks.

Completeness follows by canonically lifting an original nonlinear
target witness. Soundness follows by NB19 or NB20 when decoding
the exact lifted output. The internal optional deletion or
mandatory passive marking is performed on the band instance; it
does not bypass the true original cost or mandatory total.

For rational utility or processing marginals, use one explicit
common grid g and scale all relevant slopes to integers. Exact
optimization then takes

    binomial(q,r) exp(O(r sqrt(OPT/g+1))) poly(H)                (NB29)

time and polynomial space. Doubling followed by exact integer
binary search uses only targets O(OPT/g+1); no large external
upper target enters the exponential factor. At zero optimum the
original feasible initializer and exact zero gates apply.

This exact block consequence also composes over explicit adaptive
scenarios after fixing the same selected basis. Scenario searches
add; their profile families are not multiplied. Use a grid common
to all scenario marginals. A valid numerical upper bound for the
number of target calls is the maximum, over scenarios, of
R_s times its largest normalized marginal slope. The exact real
cost budget is retained separately by each scenario's own output.

NB28–NB29 remain numeric-target statements. They imply neither
a square-root dependence on approximation accuracy nor exact
nonlinear objective equalities.

## 11. Scenario-adaptive robust composition

The same reduction may be applied independently in every explicitly
listed scenario. Each scenario may have its own global rank, hard
domains, marginal descriptions, setup fees and one exact cost
budget. A common actual selected player basis B is fixed first.
Assignments and band repacking may then depend on the scenario.

For fixed B, each scenario's projection and domination proof is
independent. The robust target is feasible exactly when every
scenario's original target is feasible on that SAME B. Therefore
the previously proved robust profile composition applies: process
the scenarios sequentially at a target, rather than taking a
Cartesian product of their profile families.

Robust max-min allocation keeps NB23 with polynomial dependence
on the complete scenario input. Fixed-ground robust scheduling
keeps NB24; if active machines must themselves form a common
r-element matroid basis, enumerate those actual bases and use
binomial(q,r) exp(O(r/epsilon)) poly(H_epsilon). Every scenario
retains its own original mandatory resource rank where required,
and its own true setup-plus-assignment budget remains exact.

The initial feasibility tests are recomputed for the chosen B in
every scenario. They do not assume that a basis affordable or
resource-feasible in one scenario works in another. Sequential
solver work and the explicitly many output vectors have polynomial
total storage. This corollary is for adaptive scenario allocations,
not one shared integer assignment satisfying several cost rows.

## 12. Complete complexity and input boundaries

The lifted dimension is N, the number of supplied common-refinement
bands. It is polynomial in H. Band lengths may be enormous but only
their binary encodings are stored. No algorithm in this reduction
performs d_e individual unit operations.

Each G rank query is one SFM instance of NB14 on the original
coordinate ground. Its values have polynomial bit length. Standard
resource feasibility can also be separated directly through NB13:
check each band cap, aggregate z, and separate P(F) on the aggregate.
The associated complement ranks used in profile recovery use only
polynomially many such exact operations. A polynomial composition
of these oracle procedures remains polynomial in H.

After truncating d_e to F({e}), the sum of all band capacities is
at most |E|R, while G itself has rank at most R. Their encodings,
the band coefficient descriptions, and the transformed LP bit
bounds are polynomial. The approximation exponent therefore depends
on the ORIGINAL number of blocks and accuracy, not on a numerical
capacity or a count of conceptual units. The transformed input size
appears in a fixed-degree polynomial factor.

The representation assumption is substantive. An arbitrary value
oracle for a concave function can hide exponentially many distinct
marginal segments. This theorem requires the explicit compressed
band lists, or another representation that provably supplies such
a list in polynomial time. It does not infer that property from
concavity alone.

The order assumptions are also substantive. With one optional
coordinate of capacity two, utility marginals 1,1 and cost marginals
2,0, the nonprefix band vector (0,1) has utility one and cost zero,
whereas every nonzero original count costs at least two. Thus an
upper budget cannot be recovered by the present argument when its
cost marginals decrease. Theorem NB-A requires convex costs.

Fixed positive activation charges per coordinate are not hidden in
a zero-normalized convex function. The explicitly permitted setup
fees are attached to the actual selected player set, whose identity
does not change during repacking. Other activation models need a
separate proof.

Finally, blocks are a partition. General overlapping utility rows,
intersections of arbitrary global resource polymatroids, and
multiple exact hard cost rows on one integer vector are not added
by the band reduction. A global mandatory base encodes only the
constraints of F and its original total; per-job or per-type totals
must already be implied by F when the application requires them.

## 13. Public antecedents and bounded comparison

Groenevelt's [Two algorithms for maximizing a separable concave
function over a polymatroid feasible region, EJOR 54(2), 227–236
(1991)](https://www.sciencedirect.com/science/article/pii/037722179190300K)
studies both discrete and continuous separable concave polymatroid
optimization. Separable concavity on a polymatroid and marginal
allocation methods are established subjects. The present claims
concern the additional exact cost budget, block max-min or maximum-
load objectives, mandatory totals, and explicit binary-band
implementation of the stated profile guarantees.

Shioura's [Polynomial-Time Approximation Schemes for Maximizing Gross
Substitutes Utility Under Budget Constraints, MOR 40(1), 192–225
(2015; published online 2014)](https://pubsonline.informs.org/doi/abs/10.1287/moor.2014.0668)
gives PTASs for gross-substitutes and M-natural-concave utilities,
including a sum-of-two-functions variant under a budget. Its
nonlinear function classes are broader than explicit separable
marginal bands. This is a direct approximation-scheme antecedent;
the present result is not a first scheme for nonlinear utility
under budgets. The publisher statement and the author's indexed
manuscript were checked, but full direct PDF retrieval was blocked
by a timeout, so this note assigns no unverified precise runtime
to that paper. Author manuscript:
<https://www.dais.is.tohoku.ac.jp/~shioura/papers/MOR2014.pdf>.

The exact linear seven-variant and fixed-block comparisons are
recorded in the separately reviewed profile and baseline notes.
This manuscript contributes a fully specified optimum-preserving
compressed reduction and its consequences. No exhaustive priority,
fastest-known, general nonlinear-oracle, or fractional-comparator
claim is made.

## 14. Dependencies and review status

The new mathematical interface consists of NB9–NB20: shared projected
rank, band-box rank, explicit SFM evaluation, exact original-domain
projection, fixed mandatory total, and simultaneous canonical
domination. NB21–NB29 prove that the previous linear guarantees
transfer with the original nonlinear integer comparator and budget.

The imported complete linear results are in

- global_polymatroid_profile_transfers.md;
- mandatory_base_fair_allocation_passive_lift.md;
- global_robust_profile_composition.md;
- seven_variant_single_matroid_profile_scheme.md;
- refined_single_matroid_accuracy_constants.md;
- exact_numeric_target_single_matroid_scheme.md;
- block_global_exact_numeric_target_schemes.md.

This new nonlinear manuscript is an incremental candidate awaiting
independent full review. It does not modify any frozen checkpoint
file or presume that the imported linear proofs handle nonlinear
functions without the explicit reduction given here.
