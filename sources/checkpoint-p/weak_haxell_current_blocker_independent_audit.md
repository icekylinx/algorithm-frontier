# Independent audit of current blocker growth in weak Haxell

**25 October 2026. Targeted mathematical audit passed.**

Audited notes: `weak_haxell_current_blocker_growth.md` and its historical
certificate and birth-growth prerequisite,
`weak_haxell_uniform_lifetime_analysis.md`, Sections 2--4.
The public operation sequence was checked against Annamalai,
[Finding Perfect Matchings in Bipartite Hypergraphs, arXiv:1509.07007v2](https://arxiv.org/html/1509.07007v2),
Sections 2--4. This is a quantitative reanalysis of that public algorithm,
with explicit certificate bookkeeping; it is not a new general-graph
matching algorithm or an improvement to the Haxell sufficient condition.

## 1. Persistence is about physical certificates

For a live layer j, its lower prefix is fixed. A swap strictly above
its direct child removes a matching edge from a higher blocker layer
and inserts a higher selected edge. Both have right support disjoint
from the current layer and all lower support. Thus such a swap changes
neither X_j nor the matching blockers Y_j of X_j.

A collapse of the direct child can remove blockers from Y_j, but is
immediately followed by an actual extension attempt. The retained
candidate is refreshed then, whether the extension is adopted or
rejected. Therefore the latest actual candidate contains the current
layer's physical support at every main-loop boundary. Extra resources
are retained as physical ghosts, not as claims that their old matching
edges are still members of the current matching.

Greedy maximality of that actual attempt says that every edge incident
to a non-full active left identity hits either the fixed lower prefix
or its candidate support. This remains true when unrelated matching
edges later change. The active identity's own matching edge is already
in the lower prefix; the dummy root is unmatched. Hence the certificate
covers every incident input edge, including matching edges.

As the notes explicitly require, extending layer j uses the prefix
strictly below j and initializes the candidate with (X_j,Y_j). The
source's displayed superposition calls abbreviate this indexing; the
stated convention is the one consistent with its active set and layer
invariant. It must not be replaced by a literal call that incorrectly
takes A(Y_j) as the active set.

## 2. Current blocker count pays for historical extras

Write mu=epsilon^2/(10r^2), Q=ceil(1/mu), and a=2r-3.
Current noncollapsibility gives X_j <= Y_j/(1-mu). Rejected
candidate extras number fewer than mu X_j. Since every matching
blocker meets exactly one selected edge,

    |B(X_j union Y_j)| <= (r-1) X_j + (r-2) Y_j.

An extra selected edge and its then-blockers use at most (r-1)^2
resources. Thus the current historical certificate satisfies

    |C_j| <= (a+eta) Y_j,
    eta = mu r(r-1)/(1-mu).

The count of full active identities is at most f Y_j, where
f=mu(1+mu)/(1-mu). Both charges use the current blocker count;
neither silently substitutes the blocker's larger birth value.

## 3. Prefix contradiction and constants

For a target layer i, let W=|Y_<i| include the dummy root, and
Y=|Y_i|. The active left identities through this prefix number W.
Their own matching edges are distinct; the dummy root contributes
no right support. Removing candidate-full identities and uniting
candidate supports therefore gives

    |C| <= (a+eta)(W-1+Y),
    |S| >= W-f(W-1+Y),

and C hits every incident edge of S.

For r>=2 and 0<epsilon<1,

    eta <= 4 epsilon^2/39,
    (a+epsilon) f <= 41 epsilon^2/780.

Their sum is 121 epsilon^2/780 < epsilon/5. If W>=2 and
Y <= epsilon W/(10r), then Y/(W-1) <= epsilon/(5r).
The resulting upper coefficient is at most a+31 epsilon/50,
strictly below a+epsilon. This gives the claimed explicit violation
|C| < (a+epsilon)(|S|-1). The full-identity removal is less than
0.028W, so S is nonempty (indeed at least two when W>=2).

When W=1, the existing birth-X growth gives X_i>=1, and
noncollapsibility forces Y_i>=1. This is more than epsilon W/(10r).
Thus the first positive layer is covered without an invalid dummy
matching-edge contribution.

## 4. The two growth bounds have different jobs

At a child birth, the parent is a surviving noncollapsible layer.
The new current-Y result gives

    W_child >= (1+epsilon/(10r)) W_parent.

The collapsing child may never have survived a main-loop boundary.
Its collapse charge must instead use the old birth-X inequality,
which persists because selected sets only grow. With the degree cap Q,
this gives the stated shrink rate tau >= epsilon^5/(1000r^6).
The draft keeps these two arguments separate correctly.

Adopted extensions split each parent's children into only polynomially
many epochs in r/epsilon. Within an epoch selected parent edges are
fixed, so successful child collapses only decrease its blockers.
Successive child prefix sizes shrink by 1-tau. Weighted summation with

    lambda = O((r/epsilon) log(2+r/epsilon))

then contracts total child weight by a fixed constant after increasing
the absolute coefficient. The logarithms of the epoch count and inverse
tau are only O(log(2+r/epsilon)). The finite-prefix argument includes
the final living child and does not presuppose termination.

## 5. Certifying implementation and scope

Only the last surviving layer affected by a collapse cascade can have
changed; lower surviving layers retain their earlier certificates and
current-Y bounds. Checking that last survivor, or a newly surviving
last layer, therefore maintains the invariant for the entire stack.
A failed check yields the explicit S,C just described. Initialization,
candidate replacement and certificate materialization can be charged to
the already allowed explicit input scans.

No counterexample was found. The rank-linear uniform exponent follows
under the stated conventions. This audit does not assert optimality
among all public algorithms or polynomial dependence on 1/epsilon.

