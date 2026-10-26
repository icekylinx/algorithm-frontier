# Profile schemes under one global integral polymatroid

**25 October 2026. Complete theorem and proof; root and
transfer_frontier have independently passed the full manuscript.
The separate review is global_polymatroid_profile_transfer_audit.md.**

The allocation and scheduling profile schemes do not require a direct
sum of independent resource types. They extend to one arbitrary
integral polymatroid on the entire assignment-coordinate ground.
Resource dependencies can therefore cross type and recipient blocks.
The objectives must still use a partition of the coordinates into
player or machine blocks.

Allocation permits an independent resource vector, an arbitrary
selected player-matroid basis, unrelated nonnegative values, and one
exact shared setup-plus-assignment budget. Scheduling requires one
base of the global polymatroid and preserves one exact assignment
budget. Their approximation and time bounds are unchanged:

    Allocation: (1-epsilon)OPT,
      binomial(q,r) exp(O(r/epsilon)) poly(H_epsilon).

    Scheduling: (1+epsilon)OPT,
      exp(O(q/epsilon)) poly(H_epsilon).                         (GP1)

Both algorithms use polynomial binary space. The six-profile
factor-three-halves scheduling endpoint also transfers, with time
6^q poly(H). Here q counts the objective blocks, and r is the
selected player rank in the allocation model.

For a single block and a matroid resource, GP1 gives
2^{O(1/epsilon)}-time approximation schemes for budgeted matroid
independent set and constrained minimum-weight matroid basis, with
polynomial dependence on the full encoded instance. Section 10
compares this accuracy dependence with a directly checked 2026
primary baseline. No publication-priority or fastest-known claim
is made.

## 1. Global ground, masks, and the two distinct resource models

Let E be an explicitly listed coordinate ground, partitioned into
disjoint blocks

    E=disjoint_union_(p in P) E_p,       |P|=q.                  (GP2)

A coordinate can be an eligible item-recipient pair, an aggregate
assignment type, or an element with a predetermined group. Its
integer multiplicity may be binary-large. Let

    F:2^E -> Z_nonnegative

be normalized, monotone and submodular, supplied by an exact rank
oracle. Write

    P(F)={x>=0: x(S)<=F(S) for every S subset E},
    R=F(E),
    B(F)={x in P(F):x(E)=R}.                                   (GP3)

The oracle values are bounded by R, whose binary encoding is part
of the numerical complexity. H includes the coordinate list, block
partition, numerical data and the paid polynomial rank/SFM/LP work.
Set H_epsilon=H+size(epsilon), with the full rational accuracy
encoding.

A mask A subset E fixes coordinates outside A to zero. On A, the
rank is the restriction F_A(S)=F(S). Its independent polytope is
exactly the masked part of P(F). This follows because, for every
S subset E,

    x(S)=x(S intersect A)<=F(S intersect A)<=F(S).

There are two different total conventions:

- **Allocation:** x is any integer vector of P(F). Restricting the
  ground and leaving resource units unused are legitimate.
- **Mandatory global-base scheduling:** x must be an integer vector
  of B(F). After every mask, the original total R remains required.
  If F(A)<R, that mask is infeasible. The total is never replaced
  by the smaller masked rank.

In particular, the allocation proof may complete unused units into
an auxiliary disposal coordinate, whereas the scheduling output
must retain all of its original global base total.

## 2. Global upper-prefix recovery for a mandatory base

Suppose a masked fractional x in P(F_A) has total R, and suppose
an integral polymatroid K on A contains x. Then

    P(F_A) intersect P(K) intersect {y(A)=R}                    (GP4)

is nonempty and integral. Indeed, intersection of two integral
polymatroids is integral. Its total is at most F(A)<=F(E)=R,
so the displayed equality specifies a maximum-total face. A
nonempty face of an integral polytope is integral.

Minimize the one actual assignment-cost vector c on this face.
An integral minimizer y has c*y<=c*x. Thus the same point is a
valid original global base, respects K, and preserves any budget
met by x. There is no assertion that adding an arbitrary budget
inequality preserves integrality; cost is optimized on an integral
face.

The machine polymatroids used below have a simple form. For a
group ordered by decreasing nonnegative processing times
v_1,...,v_m, define U_h=ceil(sum_(i<=h)x_i). The prefix caps

    y({1,...,h})<=U_h

have rank k(S)=max_{h in S}U_h, with empty rank zero. This rank is
integral, monotone and submodular. The rank inequalities and prefix
caps are equivalent: for a nonempty set S, use the prefix ending
at its largest index. Summation by parts gives

    sum_i v_i y_i <= sum_i v_i x_i + v_1.                       (GP5)

A disjoint group with integer count cap h has rank h on each
nonempty subset. Taking the direct sum of these *machine-side*
groups gives K. Nothing in GP4 requires the *resource-side* F to
decompose across blocks or types.

Exact polynomial optimization can be implemented by separation
over the two polymatroids and the displayed face. If needed, a
lexicographic sequence of coordinate optimizations on the optimal
cost face selects an integral vertex, using only polynomially many
exact LP calls. No expansion into individual resource units is
required.

## 3. Global lower-prefix recovery for independent allocations

Fix any masked real ground A and fractional x in P(F_A). Let
n=F(A). Add one global disposal coordinate 0 and set

    Fhat(S)=F(S) if 0 is not in S;
    Fhat(S)=n    if 0 is in S.                                 (GP6)

Here the first case uses S subset A. This is a normalized monotone
integral submodular rank. Submodularity for two sets both excluding
0 is inherited from F; for two containing 0 it is equality; for
one containing 0 it reduces to monotonicity of F on the other set
and their intersection.

Assign n-x(A) to disposal. The resulting xhat is a base of Fhat.
Conversely, deleting disposal from any such base leaves an
independent vector in the real restricted resource. This completion
does not make unused original units mandatory in the output.

On D=A union {0}, let d_e=Fhat({e}) and define

    G(S)=Fhat(D minus S)+d(S)-n.                                (GP7)

The rank G is normalized, integral, monotone and submodular. A
marginal of G equals d_e minus a marginal of Fhat, which lies
between zero and d_e. Complementation gives the exact bijection

    y=d-xhat in B(G)  iff  xhat in B(Fhat).                     (GP8)

For example, the forward inequality is
y(S)=d(S)-n+xhat(D minus S)<=G(S). In the reverse direction,
y_e<=G({e})<=d_e gives xhat>=0, and the inequality on D minus S
gives xhat(S)<=Fhat(S). The total on either side supplies the base
equality.

Choose one coordinate order in each real block E_p intersect A.
Impose ceiling-prefix caps ceil(y(S)) in that order, and give the
disposal coordinate its cap d_0. Their direct sum is an integral
polymatroid K containing y. Intersect P(G) with P(K) at total
G(D). This is a nonempty integral maximum-total face.

Maximize the actual real assignment coefficients c on y, giving
disposal coefficient zero. For an integral maximizer y', let
xhat'=d-y' and delete disposal. Since c*d is constant,

    c*x' = c*d-c*y' <= c*d-c*y = c*x.                           (GP9)

Every real prefix S simultaneously satisfies

    x'(S)>=d(S)-ceil(y(S))=floor(x(S)).                         (GP10)

Thus one integer x' in P(F_A) preserves every prescribed lower
prefix floor and does not increase actual assignment cost. There
is exactly one global resource complement and one global disposal
coordinate; no type independence is used anywhere.

## 4. Global-resource allocation theorem

Let M be an arbitrary original player matroid of rank r>=1 on
the q nonloop blocks. A solution chooses an actual M-basis B and
an integer x in P(F), supported on union_(p in B)E_p and the given
eligibility mask. Coordinate e has nonnegative value v_e and
nonnegative assignment cost c_e. Player p has nonnegative setup
fee sigma_p. The exact budget is

    sigma(B)+sum_e c_e x_e<=C.                                 (GP11)

The objective is min_(p in B) sum_(e in E_p) v_e x_e. Let OPT_A
be its integer optimum. If no M-basis has setup fee at most C,
there is no legal zero-utility solution. Otherwise zero counts on
a minimum-setup basis initialize a legal output.

**Theorem GA.** For rational 0<epsilon<=1, there is a deterministic
algorithm returning at least (1-epsilon)OPT_A under GP11 in

    binomial(q,r) exp(O(r/epsilon)) poly(H_epsilon)               (GP12)

time and polynomial space. More explicitly, with

    delta=epsilon/3, J=floor(1/delta), K=ceil(1/delta),
    b=ceil((1-delta)/delta^2),

the two simultaneous time bounds are

    binomial(q,r) binomial(b+K,K)^r poly(H_epsilon),
    binomial(q,r) exp(4r(J+1)) poly(H_epsilon).                   (GP13)

### 4.1 Fixed-basis target routine

At positive target T, enumerate actual M-bases B with affordable
setup. Mask outside coordinates to zero and remove zero-value
coordinates. Restrict the one global F to this real ground.
Set w_e=min(v_e,T). Full *integer* target feasibility is preserved:
one assigned unit originally worth at least T still supplies T;
otherwise capping changes nothing at that player.

Small coordinates have w_e<=delta*T. Partition big normalized
values into the intervals

    (lambda_i,mu_i],
    lambda_i=delta+i*delta^2,
    mu_i=min(1,delta+(i+1)*delta^2),   0<=i<b.                   (GP14)

Store only occupied bins at each player. For each selected block
enumerate integer counts h_i>=0 satisfying

    sum_i h_i<=K,       L=sum_i lambda_i h_i<=2,
    U=sum_i mu_i h_i.                                          (GP15)

For the fixed profiles, solve one LP inside the restricted P(F).
Require each big-bin total to equal its h_i, small true utility
at each player to be at least max(0,1-U)T, and assignment cost
at most C-sigma(B).

### 4.2 Full-target witness and global coupling

Consider an integer full-T allocation on B*. After capping, if a
player's big utility reaches T, retain the first prefix of any
unit order that reaches T and delete all its other units. This
big total is below 2T and its count is at most ceil(1/delta).
If big utility is below T, keep every big unit and its original
small units; the big count is again at most K.

All these operations are coordinatewise deletions. Although F may
couple arbitrary different players and types, P(F) is downward
closed, so the simultaneous retained global vector remains feasible.
Nonnegative assignment cost does not increase. The big counts obey
GP15, and the retained small utility meets the fixed-profile LP
requirement because U bounds actual big utility from above.
Therefore an original full target supplies one enumerated feasible
profile LP without needing resource separability.

### 4.3 Recovery and utility

Give every big coordinate in bin i surrogate value lambda_i*T;
keep small true values. Order each player's big bins by decreasing
surrogate, followed by its small coordinates in decreasing value
order, putting big coordinates first at ties. Apply GP10 and GP9
to these orders with the single global F.

In summation by parts, the loss at a prefix boundary is its value
difference times the fractional part of the fractional prefix
count. Inside a big bin the value difference is zero. At the end
of each big bin, the fractional prefix count is a sum of the
integer h_i and has zero fractional part. This includes the final
big/small boundary. Only small-group differences contribute, and
their total is at most delta*T.

The fractional surrogate utility is at least
[L+max(0,1-U)]T, while

    U-L<=K*delta^2.

Hence integer actual utility is at least

    (1-delta-K*delta^2)T >=(1-epsilon)T.                        (GP16)

The last inequality follows from K<=1/delta+1 and
2delta+delta^2<=7epsilon/9<=epsilon. Actual values dominate
surrogates. The actual selected basis does not change, and GP9
does not increase assignment cost. GP11 is therefore exact.

The output does not need to preserve every bin count equality.
The lower prefix floors and the vanishing fractional big-boundary
errors already prove GP16.

## 5. Global-base scheduling theorem

The q blocks are now fixed available machines or load classes.
The required vector is an integer x in B(F), with the original
total R=F(E). It must respect eligibility and

    sum_e c_e x_e<=C,                                          (GP17)

where c_e>=0. Coordinate e in E_p has processing time ell_e>=0.
The objective is min max_p sum_(e in E_p) ell_e x_e, with
integer optimum OPT_S when the original budget-feasible family
is nonempty.

**Theorem GS.** For rational 0<epsilon<=1, a deterministic algorithm
detects global budget infeasibility or returns an original base
of load at most (1+epsilon)OPT_S in

    exp(O(q/epsilon)) poly(H_epsilon)                           (GP18)

time and polynomial space. With delta=epsilon/2,
K=floor(1/delta), and b=ceil((1-delta)/delta^2), its time is
simultaneously bounded by

    binomial(b+K,K)^q poly(H_epsilon),
    exp(3q(K+1)) poly(H_epsilon).                               (GP19)

### 5.1 Target profiles and recovery

At T>0, forbid times above T and keep the original total R.
If the allowed rank falls below R, the target is infeasible.
Small times are at most delta*T. Bin the other times by GP14
with the scheduling delta. Per machine enumerate integer counts

    sum_i h_i<=K,       L=sum_i lambda_i h_i<=1.                 (GP20)

The fixed-profile LP lies in the masked P(F), has total R, obeys
GP17, caps each big-bin count by h_i, and caps each machine's
fractional small load by (1-L)T.

Every original integer full-T base supplies such profiles through
its actual big counts: each big unit is strictly above delta*T,
so there are at most K; its lower big load is at most its actual
load; and the remaining small load is at most (1-L)T. The entire
original vector is used unchanged, so every cross-block resource
dependence remains satisfied.

On each machine use the integer big-bin caps and a small upper-
prefix chain. Their direct sum is one machine polymatroid K_mach.
Apply GP4 with the single masked F. The recovered integer point
is an original resource base of no greater cost. Its big load is
at most LT+K*delta^2*T<=LT+delta*T. By GP5 its small load is at
most (1-L)T+delta*T. Its total load is at most (1+epsilon)T.

Thus fixed-profile success is legal, and exhaustive failure
certifies OPT_S>T. Resource separability is absent from both
directions of this argument.

### 5.2 The exact three-halves endpoint

The six-profile table in
[six profile three halves proof](../../six-profile-three-halves/proof.md) uses only
disjoint big count-one groups and one small prefix chain on each
machine. The full-target case classification uses only machine
loads. Its recovery therefore uses GP4 verbatim with one global F.
It gives an original base of makespan at most (3/2)OPT_S in

    6^q poly(H) time and poly(H) space.                         (GP21)

The same conclusion holds without any bound on the number of
distinct processing times.

## 6. Original totals, zero cases, and exact target optimization

For scheduling, let A_0 be the original eligibility mask. If
F(A_0)<R, no original base exists on eligible coordinates. Otherwise
minimize actual assignment cost on the total-R base face. Excessive
minimum cost certifies global budget infeasibility; an integral
minimizer gives an initial actual schedule. If R=0, the zero vector
is optimal. For R>0, separately test load zero by keeping only
zero-time eligible coordinates while retaining total R and the
same exact budget.

For allocation, an affordable minimum-setup basis with zero real
counts is the initializer. No resource-rank condition is needed
for zero utility because the independent zero vector is feasible.

Choose a positive rational grid dividing every positive original
coordinate value or time, as appropriate. All integer objective
values lie on it. A common denominator and integer gcd have
polynomial encoding. A global allocation upper bound is

    V_A=R*max_(e in E) v_e,                                    (GP22)

since every independent vector has total at most R. If R=0 or all
eligible values are zero, output value zero. Otherwise start the
maximization search with saved nominal target zero and external
upper target V_A+g. Complete target failure implies T>OPT_A;
success stores at least (1-epsilon)T. At adjacent endpoints,
the upper endpoint is strictly above OPT_A and grid integrality
gives a saved lower target at least OPT_A.

For scheduling, an actual initial schedule has load at most
R*max_e ell_e. After the exact zero test fails, start the failed
lower target at zero and the weak upper output at that actual
schedule. A complete target failure implies T<OPT_S. Success
stores a schedule of load at most (1+epsilon)T, or 3T/2 for GP21.
At adjacent endpoints, grid integrality gives a saved upper target
at most OPT_S.

Neither search assumes that weak successes are monotone. There
are polynomially many target calls in the original binary data.
No extra multiplicative accuracy loss or fractional-comparator
rational-gap argument is used.

## 7. Profile counts, all-input time, and binary space

The profile enumerators prune partial vectors at both their count
bound and their lower-load bound. A generated partial vector always
has an all-zero completion, so at a fixed recursion depth distinct
partial vectors have distinct complete profiles. Traversal overhead
is polynomial per emitted profile, including all bad profiles and
failed LPs. Cartesian products across selected players or fixed
machines are streamed with the same property.

For allocation, lambda_i>=delta^2(J+i) with J=floor(1/delta).
Profiles with L<=2 inject into integer partitions of total at most
floor(2/delta^2)<2(J+1)^2, using h_i parts of size J+i. The
cumulative partition generating product at t=1/(J+1) has logarithm
at most

    t*floor(2/delta^2)+2/t <4(J+1).

This gives exp(4(J+1)) profiles per selected player. For scheduling,
L<=1 and J=K give the analogous bound exp(3(K+1)). The estimate
uses exp(y)-1>=y and sum_(l>=1)1/l^2<=2. It is an analysis-only
bound, not a computed partition table. Ignoring lower load gives
the simultaneous finite binomial count bounds.

Only occupied input bins are stored. Their number is at most |E|,
and their binary IDs, counts, endpoints and partial sums have
polynomial bit length in H_epsilon. The global disposal extension
adds one coordinate, not R coordinates. Its complement rank is
at most |E|R, so its numerical encoding remains polynomial.

For an arbitrary real candidate x, resource separation minimizes
F_A(S)-x(S), a submodular function, on the explicit ground A.
Complement rank evaluation uses one original rank evaluation plus
the known modular term; the machine ranks are explicit. All LPs
and integral-face optimizations therefore retain polynomial paid
oracle work on a polynomial coordinate dimension. The larger
global F does not introduce an enumeration of its subsets.

These observations prove GP12–GP21 on all inputs with polynomial
workspace and no unit expansion.

## 8. Concrete applications that introduce cross-type dependence

### 8.1 Fair assignment of a globally matroid-independent item set

Let G be a matroid on original items J. An allocated item set must
be independent in G, and each selected item may be assigned to
only one eligible recipient. Values and costs depend arbitrarily
on the assignment. The selected recipients may themselves form
an arbitrary basis of M, with nonnegative setup fees.

Create coordinate (p,j) for a potential assignment and let pi(S)
be the items represented by coordinates in S. The parallel-copy
rank

    F(S)=rank_G(pi(S))                                         (GP23)

is a matroid rank on the assignment ground. For a direct check,
pi(A union B)=pi(A) union pi(B) and pi(A intersect B) is contained
in pi(A) intersect pi(B); rank submodularity and monotonicity give
submodularity of F. Singletons have rank at most one.

An integer independent vector of F selects at most one copy of
each item, and its underlying selected item set is G-independent.
Conversely, assigning an independent item set to eligible recipients
gives an independent vector of F. Thus Theorem GA applies with
arbitrary cross-item matroid dependence. It is not necessary for
item types to be independent resource components.

This is a global constraint on the union of allocated items. It
is not the different requirement that every recipient separately
obtain a G-independent set while their union may contain several
bases of G. Adding that latter family simultaneously would require
a separate proof.

### 8.2 Minimum-congestion bases with disjoint weighted classes

Let G be a matroid whose elements are partitioned into q classes.
Element e has nonnegative load ell_e within its own class and
nonnegative acquisition cost c_e. Choose a G-basis of cost at most
C while minimizing the maximum weighted class load. Taking
F=rank_G and E_p to be the class gives Theorem GS and GP21.

For a connected graph and its graphic matroid, this chooses a
spanning tree under an exact total acquisition budget, minimizing
the largest weighted load of any one edge color class. The classes
are disjoint. This does not claim a degree-bound theorem in which
one edge simultaneously contributes to both endpoint rows.

Alternatively, apply GP23 to assigning a selected G-basis of items
to machines. Retain the original rank of G even if eligibility
or target masks remove copies; rank loss means no such basis can
be assigned. The result chooses and assigns a global basis. It
does not require every original item to be scheduled.

### 8.3 Two important single-block specializations

With q=r=1, no setup fee, and F a matroid rank, allocation becomes
budgeted maximum-weight matroid independent set. GP12 gives

    value >=(1-epsilon)OPT, exact budget,
    2^{O(1/epsilon)} poly(H_epsilon) time, polynomial space.     (GP24)

With q=1, scheduling becomes minimum-weight matroid basis under
one exact upper budget on another weight vector. GP18 gives

    objective <=(1+epsilon)OPT, exact budget,
    2^{O(1/epsilon)} poly(H_epsilon) time, polynomial space.     (GP25)

Both also hold for an arbitrary integral polymatroid with binary
multiplicities, in the independent-vector and base-vector versions
respectively. GP24–GP25 are the two variants proved here; this
note does not silently assert all budget/cover/objective-direction
variants of single-matroid optimization.

## 9. Scope boundaries and required encodings

**A global base does not automatically impose named job totals.**
The condition x(E)=F(E) enforces the rank constraints of F and its
one total. If F is a direct sum of type ranks, the old per-type
base totals follow, as in the original scheduling theorem. For an
arbitrary F, they need not. For example, a rank-two uniform matroid
on {a_1,a_2,b_1,b_2} has base {a_1,a_2}; total two does not enforce
one a-type and one b-type item. A model requiring such equalities
must encode them in the supplied resource rank or establish a
different integral intersection theorem. Intersecting an arbitrary
F with additional type quotas need not leave one polymatroid.

**The load/utility supports must form blocks.** Each coordinate
belongs to exactly one objective block. Arbitrarily overlapping
weighted row supports do not yield the disjoint chain/partition
polymatroid used for recovery. Copying a coordinate into several
rows while forcing simultaneous equal counts is an additional
constraint, not a valid use of GP23.

**One global resource is essential to this proof.** An intersection
of two unrelated resource polymatroids is not assumed to be a
polymatroid. Adding the machine or player prefix side would then
produce a different intersection problem, with no integrality
guarantee supplied here.

**One scalar budget is preserved per recovered point.** The cost
objective can certify one budget exactly. This construction does
not preserve several independent cost rows on the same integer
vector. Scenario-adaptive recoveries with a separately fixed common
basis are a distinct composition, not a multi-budget rounding
claim for one vector.

The comparator in allocation remains integer OPT. Capping large
values at the target is justified by individual assigned units and
does not preserve every fractional full-target witness.

## 10. Bounded primary-source comparison

### 10.1 Existing one-budget matroid schemes and the displayed accuracy bound

Doron-Arad, Kulik and Shachnai already obtained an EPTAS for budgeted
matroid independent set; see their
[SOSA-era primary preprint](https://arxiv.org/abs/2209.04654).
The [2026 journal version](https://link.springer.com/article/10.1007/s10107-026-02397-3)
also covers budgeted matching and matroid intersection through
representative sets. Thus GP24 is not a first EPTAS claim.

Doron-Arad, Shachnai and Shmerler,
[*Tight Approximation Results for Matroid Optimization with a Linear Constraint*, APPROX/RANDOM 2026](https://drops.dagstuhl.de/storage/00lipics/lipics-vol392-approx-random2026/LIPIcs.APPROX-RANDOM.2026.18/LIPIcs.APPROX-RANDOM.2026.18.pdf),
state a unified EPTAS with displayed dependence
(1/epsilon^2)^{O(1/epsilon)} for the nontrivial single-matroid
variants. Their Section 2.1, Lemma 3 counts unweighted bucket-count
compositions. In the two variants proved independently above,
the weighted lower-load pruning and partition bound replace that
displayed accuracy dependence by 2^{O(1/epsilon)}. This is a
comparison of proved bounds, not an exhaustive fastest-known claim.
The same public paper discusses why no FPTAS is available for the
general family; our exponential accuracy dependence is consistent
with that boundary. No unreviewed extension to its other variants
is imported here.

### 10.2 Fair matroid selection and discrepancy are established subjects

Gourves, Monnot and Tlilane,
[*A Matroid Approach to the Worst Case Allocation of Indivisible Goods*, IJCAI 2013](https://www.ijcai.org/Proceedings/13/Papers/030.pdf),
study a common matroid basis evaluated by several agents, and give
constructive guarantees in terms of normalized single-element
values. This is direct precedent for matroid-based fairness. Our
block-supported integer-OPT scheme with one exact budget has a
different guarantee and parameterized running time; it does not
cover arbitrary overlapping agent evaluations of a common element.

Kiralý, Lau and Singh,
[*Degree Bounded Matroids and Submodular Flows*](https://www.microsoft.com/en-us/research/publication/degree-bounded-matroids-submodular-flows/),
give cost-preserving additive bounds for matroid bases with
hyperedge cardinality restrictions, measured by maximum incidence
degree. In particular, the disjoint unweighted degree special case
already has exact integral structure. The present weighted-block
schemes should not be advertised as a new solution to that simpler
count-only case.

Berczi, Liu, Reis and Tarnawski,
[*Weighted Equitability and Matroid-Constrained Discrepancy*, August 2026](https://arxiv.org/html/2608.13983v1),
prove weighted equitability and cost-preserving discrepancy bounds
for fractional matroid bases. Their identical-machine partition
application and weighted sparse-row rounding are relevant nearby
results. The present resource model has one global independent
set or basis and disjoint weighted objective blocks; its claims
are the explicit multiplicative schemes, oracle-polymatroid and
binary-count scope, and exact single-budget recovery. This bounded
comparison does not establish publication priority.

## 11. Dependencies and status

The local profile tables and counting arguments are developed in
[arbitrary value allocation scheme proof](../../arbitrary-value-allocation-scheme/proof.md),
[arbitrary processing scheduling proof](../../arbitrary-processing-scheduling/proof.md), and
[six profile three halves proof](../../six-profile-three-halves/proof.md). Sections 2–5
above prove the new global-resource interface directly, rather
than assuming that per-type separability survives automatically.

The full global theorem, including the one-block comparisons, has
passed root and transfer_frontier's complete independent reads.
The detailed independent audit is
`global_polymatroid_profile_transfer_audit.md`. No formal verification
claim is attached.
