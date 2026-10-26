# Factor two for two-value polymatroid allocation in the large-cover parameter

**25 October 2026. New research manuscript; independent audit requested.**

The corank gap algorithm yields a deterministic factor-two approximation
for the **compulsory-player**, two-value recipient-polymatroid Santa
Claus problem. Its nonlinear parameter is the largest number of players
that can each receive one large unit. The guarantee concerns all
instances of this model, with no size separation or small-unit error.

The public polynomial theorem for this model states factor four plus
an arbitrarily small constant. The present factor two uses a different
parameterized running time. A self-contained value-oracle lower bound
below two has the same parameter. This is not a claim of exhaustive
publication priority or of hardness for explicit ordinary assignment.

## 1. Model and theorem

There are q>=1 players, and every player must be served. Each resource
type j has a common positive unit value and an integral normalized
monotone submodular recipient rank f_j on the players. Allocation
counts must be integer and resource-independent. Requiring each
resource to be assigned to a full base is equivalent here: extra
nonnegative units can be allocated after the guarantee is achieved.

There are at most two positive unit values, 0<u<a. Aggregate all
large-valued types into f_b and all small-valued types into f_s.
Integer polymatroid sum decomposition recovers assignments to the
original components. Numerical capacities remain binary encoded.
There are no extra local bundle restrictions and no optional
player-selection matroid in the original problem.

Let N be the Boolean-cap matroid of the large recipient polymatroid:

$$
P(N)=P(f_b)\cap[0,1]^P,
              \qquad \nu=\mathrm{rank}(N).
 \tag{F1}
$$

Thus nu is the maximum number of distinct players that can each
receive one large unit. It is at most q and at most the total number
f_b(P) of large units, but it can be much smaller than either.

**Theorem F.** The integer max-min allocation optimum OPT has a
deterministic factor-two approximation in

$$
(27/4)^{\nu}\mathrm{poly}(\mathcal H)
                        =2^{O(\nu)}\mathrm{poly}(\mathcal H)
 \tag{F2}
$$

time and polynomial workspace. Here mathcal H pays all original
input bits, rank-value and independence queries, deterministic
submodular minimization, rational linear programming and integral
decomposition. A single positive value is solved exactly in
polynomial oracle time.

The refined parameter `nu minus the number of coloops of N` is
also valid when the nonempty unit-core branch is used; Section 5
explains this optional improvement. The headline bound (F2) does
not require introducing that refinement.

## 2. Empty and one-value instances

Discard resource types of zero rank or zero value. If no positive
type remains, the optimum is zero. If only one value v remains,
aggregate its recipient ranks into f. A target of k integer units
per player is feasible exactly when

$$
k\,\mathbf1_P\in P(f).
 \tag{F3}
$$

This is tested by minimizing f(S)-k|S|. Binary search over
0<=k<=floor(f(P)/q) finds the exact integer optimum. Extend the
resulting independent counts to a base if required, and decompose
to the original types. This handles a nominal two-class input
whose large or small class actually has total rank zero.

We henceforth assume both classes have positive rank and 0<u<a.
Then nu>=1. The case nu=q is still handled below; it does not
justify stopping optimization permanently at value a, since many
units per player could make OPT much larger than a.

## 3. A self-contained largest-unit additive rounding lemma

The public additive allocation theorem gives value at least T-a
from a fractional all-player allocation of value at least T.
For clarity, it also follows from the independently reviewed
per-machine **upper** rounding lemma used in the scheduling notes.

For each resource type, set z_j(p)=f_j({p}). The coordinate bound
z_j dominates every feasible recipient vector. Its complement dual
has rank

$$
g_j(S)=z_j(S)+f_j(P\setminus S)-f_j(P).
 \tag{F4}
$$

For a fractional original base x_j, y_j=z_j-x_j is a fractional
g_j-base. Apply upper rounding to these dual bases, using the
original intrinsic unit values as job sizes. At every player the
weighted dual count increases by at most the largest value a.
The integer dual bases y'_j satisfy 0<=y'_j<=z_j. Complementing
back gives integer original bases x'_j=z_j-y'_j, and at every
player their value is at least its fractional original value minus a.

Thus a fractional target T yields integer value at least T-a in
polynomial oracle time. Fractional resource bases and the all-player
value constraints have polynomial separation by submodular
minimization, so their feasibility can be tested by rational linear
programming. This argument does not use a DRZ local-search theorem.

For the public statement and model see Bamas et al.,
[arXiv:2307.08453v1, Theorem 21](https://arxiv.org/html/2307.08453v1).
The upper-rounding primitive has a separate proof in
[Arbitrary small sizes through workload aggregation and per-machine rounding](../../problems/many-size-scheduling/proof.md).

## 4. The small-only basis hidden inside any feasible target

Fix a target T with

$$
0<T\le2a,
                   \qquad K=\lceil T/u\rceil.
 \tag{F5}
$$

Suppose an integer all-player allocation attaining T exists. Let
R be the set of players receiving at least one large unit in that
allocation. Its aggregate large count vector dominates 1_R, so
1_R belongs to P(f_b) and R is independent in N. Extend R to an
N-basis F. Its complement

$$
I^*=P\setminus F
 \tag{F6}
$$

is a basis of the dual player matroid M=N*. Since F contains R,
every member of I* had no large unit in the fixed optimum. Its
small count is at least K. Downward closure therefore gives

$$
K\mathbf1_{I^*}\in P(f_s).
 \tag{F7}
$$

This is an integer promise on the same small recipient polymatroid.
It does not require solving a configuration LP. The player matroid
M has rank q-nu and corank nu.

The support argument is valid even when one original player
receives many large units: only one unit at each large recipient
is retained when proving R independent. Extending R to F can only
remove more players from the small-only basis; it cannot introduce
a player that depended on large value into I*.

## 5. The hard-target algorithm and its exact rounding

If nu=q, an N-basis covers every player. Give one large unit to
each, producing value a>=T/2 for every target in (F5). No unit-core
call is made on a rank-zero player matroid.

Otherwise M=N* has positive rank. Invoke the gap theorem in
[unit-quota-corank-gap-branching.md](unit-quota-corank-gap-branching.md) with target K and output

$$
b=\lceil K/2\rceil.
 \tag{F8}
$$

For K>=2 one has b<K and K/(K-b)<=3, so its time is
(27/4)^nu poly(mathcal H), using the batched deficient-set
branching theorem. The entropy branch base for ratio R=K/(K-b)
is R^R/(R-1)^(R-1), which is increasing for R>1 and is 27/4
at R=3. For K=1 use the exact
one-unit matroid-intersection routine. A failure proves that no
K-unit M-basis exists, and hence by (F7) that the original target T
is infeasible.

On success, give b small units to every member of the returned
M-basis I and one large unit to every member of its complementary
N-basis P\I. These count vectors are independently feasible in
f_s and f_b. Extend them to bases and decompose to original resource
types if required. The extra units do not decrease any value.
Every player receives value at least

$$
\min\{a,bu\}
          \ge\min\{T/2,Ku/2\}
          \ge T/2.
 \tag{F9}
$$

The large value need not be a multiple of u, and b u need not be
at most a. The displayed minimum handles both orders. There is
no additive small-unit loss or accuracy slack.

The core routine first deletes loops of M, which are precisely
coloops of N. If N has z coloops, its remaining player ground
has q-z elements and still has rank q-nu. Its corank is nu-z.
The resource f_s is restricted to this ground and later extended
by zero, not contracted. Thus nu-z can replace nu in the nonlinear
time. The pure-large rank-zero case remains the separate branch
above. These forced-large players are still served by P\I.

## 6. The large-target branch

For T>2a, test fractional all-player feasibility at value T.
Infeasibility proves that the integer target is infeasible. If it
is feasible, the additive rounding lemma gives integer value

$$
T-a>T/2.
 \tag{F10}
$$

At T=2a either branch is valid; we use the hard-target branch as
specified in (F5). Together, Sections 5--6 give a one-sided target
procedure: return an actual allocation of value at least T/2, or
soundly certify that integer OPT<T. It may succeed when T>OPT,
because success only guarantees half the target.

The easy branch uses all-player value constraints. It does not
establish an additive theorem for a general optional player matroid.
Consequently this transfer is explicitly for compulsory players;
the separate corank unit-core theorem has the broader selection
model, but that alone does not broaden this two-value statement.

## 7. Target optimization on an exact rational grid

Write a=A gamma and u=U gamma for positive integers A,U and a
positive rational gamma of polynomial bit length. Every integer
allocation value is a multiple of gamma, so OPT is too. Let

$$
V=a f_b(P)+u f_s(P).
 \tag{F11}
$$

The minimum player value is at most V; this deliberately loose
upper bound suffices. Start with lower target zero and any legal
allocation, and an upper grid target strictly exceeding 2V. No
allocation can attain half that upper target, so the target
procedure cannot return success there. Equivalently, that endpoint
is certified infeasible directly by the total-value bound.

Maintain a successful lower grid index and a soundly failed upper
index. At a midpoint save a returned half-target allocation as a
success, or use the sound original-target infeasibility outcome as
a failure. At termination the endpoints are adjacent. The failed
upper target is strictly larger than OPT, and both it and OPT are
on the grid. Hence the successful lower target is at least OPT.
Its recorded allocation has value at least OPT/2.

This search does not assume that success decisions are monotone or
that a successful target is itself integer-feasible. The explicit
upper endpoint above 2V avoids relying on either assumption. The
number of trials is polynomial in the input's numerical bit length.
All counts and quota K use binary arithmetic; the algorithm never
expands a large numerical supply into unit copies.

## 8. A matching strict-below-two oracle obstruction

Fix q>r>=1, put c=q-r, and let P have q players. Use small unit
value one with the hidden recipient rank

$$
f_A(S)=\min\{2|S|,2r\}
          -\mathbf1[|S|=r]+\mathbf1[S=A],
                      \qquad |A|=r.
 \tag{F12}
$$

Use large value two and the uniform recipient matroid U_(c,q).
Its Boolean large-cover parameter is nu=c, and it has no coloops
because c<q. The validity and hidden-set property of (F12) are
proved self-containedly in
[allocation lower bounds proof](../../problems/allocation-lower-bounds/proof.md).

The hidden allocation gives two small units to A and one large
unit to each member of P\A. It serves every player with value two.
Conversely, at most c players can receive large units, so at least
r players depend entirely on the small resource. Its total rank
is 2r. No allocation can give all those r players value greater
than two. Therefore the all-player optimum is exactly two.

An approximation factor strictly below two must give integer value
at least two to every player. Let I be the players receiving no
large unit. Then |I|>=r and each member needs at least two small
units. The total small rank forces |I|=r, and feasibility gives
f_A(I)>=2r. Among r-sets, this forces I=A. Thus the returned
allocation identifies the hidden set even if unused supply was
permitted by the formulation.

The small rank oracle differs from its symmetric reference at
exactly the one hidden query A. The usual deterministic transcript
argument therefore requires at least

$$
\binom qr-1=\binom q\nu-1
 \tag{F13}
$$

queries. For any proposed runtime F(nu) q^C with a fixed polynomial
degree C, fix an integer nu>C and let q grow. The rank values have
only O(log q) bits. This excludes every strictly smaller uniform
approximation factor in fixed-parameter oracle time for this model.

The obstruction matches the factor-two threshold in (F2), including
the coloop-deleted refinement. It does not prove optimal dependence
on nu in the exponent, ordinary NP-hardness, or hardness for
explicit allowed-recipient lists. The lower instance uses an
arbitrary value-oracle small polymatroid.

## 9. Public and elementary comparisons

Bamas, Lindermayr, Megow, Rohwedder and Schloeter,
[arXiv:2307.08453v1, Theorem 4](https://arxiv.org/html/2307.08453v1),
state polynomial factor 4+epsilon for the compulsory-player
two-value resource-polymatroid problem. Their separate additive
rounding is used in the large-target branch. The new factor two
improves approximation quality in a different time regime; it
does not assert polynomial-time domination for unbounded nu.

An elementary exact approach at a hard target can enumerate the
nu large receiving positions, solve the resulting small-count
requirements, and check the large one-cap constraints. This has
input-size exponent depending on nu. The present factor-two
algorithm keeps that polynomial degree independent of nu. The
oracle lower bound explains why exact enumeration is not merely
a harmless alternative fixed-parameter implementation.

The current-public-version audit is
[current-public-version-and-dependency-recheck.md](current-public-version-and-dependency-recheck.md). In particular,
the superseded DRZ polynomial factor-four claim is not used in
this proof or its public comparison. The positive theorem concerns
integer OPT, not an unspecified aggregate configuration LP.

Independent mathematical review is requested for the target-to-
small-only-basis promise, exact unit rounding, all-player easy
branch, one-sided maximization search, and the parameter-matched
oracle lower bound. No formal verification or external peer review
is claimed.
