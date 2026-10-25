# A strong two-incidence step can force long forestification motion

**25 October 2026. Local accounting obstruction; independent review pending.**

This note strengthens the accounting boundary in
allocation_forestification_and_pivot_accounting.md. The large neutral
motion here is not an arbitrarily chosen circulation at an unrelated
state: it is forced by every margin-preserving forestification after
one valid strong numerical step in an explicitly given unicyclic
ordinary graph.

It does not prove a superlinear lower bound on every pivot policy.
The initial O(m log S) register budget can pay for one such episode.
A history-wide amortization remains possible but requires an
additional theorem.

## 1. The unicyclic ledger

Let k>=2. A component has bins v_0,...,v_k, a, f and rows
r_1,...,r_k, e, p. Its ordinary incidences are

r_i--v_(i-1), r_i--v_i       (1<=i<=k),

e--v_0, e--a, e--v_k,

p--a, p--f.

All row degrees are at most three. Choose C>=1 integral and a
finite dyadic floor 0<epsilon<C/100. Use L=10000 C N, where the
physical realization below has N=4k+12.

Every bin has weight one, capacity L-C and zero debt. Set

x_(e,a)=5L/8,
x_(e,v_0)=3L/8-epsilon,
x_(e,v_k)=epsilon,

x_(r_i,v_(i-1))=5L/8-2iC+epsilon,
x_(r_i,v_i)=3L/8+2iC-epsilon,

x_(p,a)=L/4,
x_(p,f)=3L/4.                                             (1)

Each row sum is L. The slacks are

s_(v_i)=C                 (0<=i<k),

s_(v_k)=5L/8-(2k+1)C,

s_a=L/8-C,

s_f=L/4-C.                                               (2)

For example, the epsilon terms in the load of v_0 cancel.
At v_k, the epsilon receiver cancels the negative epsilon
in the last chain incidence. Thus every displayed slack is
strictly positive.

The incidences of value strictly above epsilon form a tree.
The sole off-basis incidence is e--v_k. Adding it creates exactly
one ordinary cycle, with 2k+2 edges. The two edges at p and the
edge e--a are bridges outside that cycle.

At this scale, all old cycle coordinates are between 0.374 L
and 0.626 L. The constants are deliberately loose.

## 2. An accepted two-incidence path

Consider the numerical path

a -> e -> v_k.

It donates only on e--a and receives on the epsilon incidence.
Its true one-sided gain and charge are

G=1/s_a-1/s_(v_k),

V=1/s_a+1/s_(v_k)+1/x_(e,a).

Using C/L<=1/(10000N) and k/N<1/4 gives

1/s_a>=8/L,
1/s_(v_k)<1.601/L,
1/x_(e,a)=1.6/L.

Consequently G/V>0.57, in particular it is strictly above one half.
The same path therefore passes the conservative quarter-threshold
test with ample rounding margin.

For an explicit finite-grid step, initialize the relevant donor
register to ell_(e,a)=3x_(e,a)/4, and choose H sufficiently large
that 1/H<=1/(10000L). Its conservative donor price satisfies

bar c_(e,a)/H = 8/(15L) + O(1/H).

The usual upper charge obeys

11.7/L < V_up < 11.8/L.

Take eta=L/4096, a finite dyadic amount. Then

1/512 < eta V_up < 1/256.

This is a standard permitted numerical step. It has constant
positive slack-objective progress and only O(1) one-sided negative
allocation-log motion.

After the step,

x_(e,a)=5L/8-eta,
x_(e,v_k)=epsilon+eta,

s_a'=s_a+eta,
s_(v_k)'=s_(v_k)-eta.                                    (3)

All other coordinates and slacks are unchanged. Every positivity
guard has ample margin. The bridge e--a changed during the numerical
step, but it cannot change in a subsequent circulation that preserves
all these new row and bin margins.

## 3. Every forestification has only two possible outcomes

The ordinary graph has cycle rank one. Hence any difference between
two allocations with the same row and bin margins is a scalar
circulation on its unique cycle; all bridge coordinates are fixed.

Parameterize that correction by lambda, decreasing e--v_k by lambda.
It increases e--v_0 and every right chain coordinate
x_(r_i,v_i) by lambda, and decreases every left chain coordinate
x_(r_i,v_(i-1)) by lambda.

The feasible interval with all coordinates at least epsilon is

-(3L/8-2epsilon) <= lambda <= eta.                        (4)

The upper endpoint is where the newly used receiving edge returns
to epsilon. At the lower endpoint, e--v_0 is the first old edge to
reach epsilon. All other old right coordinates remain
2iC+epsilon>epsilon there.

A forest allocation with this fixed physical support and these
fixed margins must put at least one cycle coordinate at epsilon.
Since the only feasible boundary values in (4) are its two
endpoints, every such forestification has one of the following
two net outcomes. Taking many intermediate pivots does not enlarge
the set of possible final outcomes.

### Outcome A: remove the new receiving incidence from active support

Here lambda=eta. Every left chain incidence decreases by eta.
Since its value before the correction is at most 5L/8,

sum_(i=1)^k log(
 x_(r_i,v_(i-1)) /
 [x_(r_i,v_(i-1))-eta])
 >= k eta/(5L/8)
 = k/2560.                                               (5)

Thus even this smaller-motion choice has Omega(k) extra negative
allocation-log variation. The preceding numerical path had only
one donor, so its corresponding variation was O(1).

The old coordinates may not cross fresh hysteresis anchors in
this one episode. Formula (5) is an obstruction to importing the
old per-step negative-variation estimate, not a claim of k price
notifications in this branch. A dynamic tree can apply the common
path motion lazily.

### Outcome B: retain the new receiver and remove an old incidence

Here lambda=-(3L/8-2epsilon). Every right chain coordinate drops
from approximately 3L/8 to

2iC+epsilon.

For registers initially ell=3x/4, all k of these old coordinates
cross their lower hysteresis boundary. Their negative log variation
is at least

k log((3L/8)/(2kC+epsilon)) = Omega(k).                   (6)

The value ratio is uniformly large at the stated phase scale.
A maintained priced structure must process these old records, or
charge a separate reconstruction batch that materializes them.

Only one old active-support edge is removed, namely e--v_0.
Thus neither the number of basis-edge changes nor the length of the
accepted path accounts for the large motion in this branch.

## 4. Slack progress cannot charge the correction

Both outcomes preserve every new bin margin in (3). The correction
has exactly zero change in Phi=sum_d log s_d.

The numerical path has constant positive Phi change and O(1)
one-sided negative variation. Every subsequent forestification
nevertheless has the additional Omega(k) variation in (5) or (6).

This rules out the assertion that one may append an arbitrary
margin-preserving forestification to each accepted step while
retaining the original O(1) negative-variation charge per step.
It also rules out charging Outcome B's price work to its single
removed basis edge.

It does not rule out paying for one episode from initialization,
amortizing a specified sequence of pivots against another potential,
or choosing a representation that supports a large neutral batch
without notifying every intermediate price change.

## 5. Integral floors and a physical matching gap

All integral lower ledgers can use (1) with epsilon replaced by
zero. L is divisible by eight at the declared phase scale. The
row sums remain L and the bin loads are identical to the original
top loads. All residuals in (2) plus C are at least C, so every
integral floor c_0<=C is satisfied with zero debt.

For a physical realization, take two disjoint copies of the
component. In each copy match r_i to v_i, e to a, and p to f.
The free bins are v_0 and v_0' respectively. Add a matched
remainder pair u,v and the unmatched edges v_0--u and v--v_0'.

The physical graph is connected and subcubic. It has

N=4k+12

vertices. The displayed current matching has 2k+5 edges, and

v_0, u, v, v_0'

is an augmenting path. Augmenting produces a perfect matching
of 2k+6 edges. Hence the current matching gap is exactly one,
consistent with the phase estimate K=1.

The only paired-remainder contacts are at v_0 and v_0', whose
actual and exactly cached top slacks are C<4C. Thus no expansion
is eligible. There are no physical bin-to-bin edges. The example
does not insert its numerical step in front of an already eligible
structural operation.

This construction is already a valid subclass of general graphs.
The claim is not that every raw-client choice or prescribed
preparation visits these exact top coordinates. It is a literal
finite feasible-ledger example with an actual remaining
augmentation and a move admitted by the strong-direction numerical
contract. In particular it does not assert that every exact
maximum-score path selector chooses this particular passing path.

## 6. The remaining research target

A potentially useful policy must pay either the cumulative
short neutral reroutings of Outcome A, or the occasional large
basis replacement of Outcome B. The example does not decide
which choice is preferable over an entire run.

A successful theorem must also retain discovery through every
off-basis receiving incidence. Treating a coordinate at epsilon
as permanently unavailable would invalidate the very strong
path used in Section 2.

