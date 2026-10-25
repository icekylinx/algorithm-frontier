# Exact degree reduction and an optimum-gap driver for general matching

**Mathematical component of the deterministic general-matching candidate.**
The degree reduction and decoding below are elementary and exact. The
phase implementation imports the specified OAI deterministic matching
state and logarithmic-progress analysis, with the structural and
numerical replacements described in the current checkpoint. No
perfect-matching promise is used.

## 1. Clean input and exact size parameters

Read an undirected graph with n vertices and m listed edge records.
Discard loops, coalesce parallel copies while retaining an original
edge ID, and remove isolated vertices. Integer sorting and compact
relabeling cost O(n+m) in the stated word-RAM input representation.
Let r and m_s be the surviving vertex and edge counts. If m_s=0,
return the empty matching. Otherwise r<=2m_s.

For a vertex v of degree d_v, create a path on 2d_v-1 vertices. Its odd
positions are ports, one per original incidence. Replace each original
edge by an edge joining its two designated ports. The resulting graph
J is subcubic. Put

    A = sum_v(d_v-1) = 2m_s-r,
    N = sum_v(2d_v-1) = 4m_s-r.

Its order may be odd. This causes no difficulty for maximum matching.

## 2. Lifting any original matching

For an original vertex matched through its port at position 2j-1,
match the even-length path on each side of that port internally. This
uses d_v-1 internal edges. For an unmatched original vertex, leave its
first port unmatched and match the remaining even-length path, again
using d_v-1 internal edges.

Consequently any original matching M lifts in linear time to a matching
Q with exactly A+|M| edges. This proves nu(J)>=A+nu(G).

## 3. Decoding every gadget matching

Let Q be ANY matching of J, and let F be its external edges viewed as
an edge subset of G. Write t_v=deg_F(v), and let V(F) contain the
vertices incident to at least one edge of F.

If t_v=0, at most d_v-1 internal edges of v's path can be matched.
If t_v=t>=1, let the occupied odd-port indices be j_1<...<j_t.
The remaining path segments have total maximum matching size

    (j_1-1) + sum_(i=1)^(t-1)(j_(i+1)-j_i-1) + (d_v-j_t)
       = d_v-t.

Thus

    |Q| <= |F| + sum_v(d_v-max{1,t_v})
         = A + |V(F)|-|F|.

For a nonempty connected component C of F, |V(C)|-|E(C)| is one
when C is a tree and at most zero otherwise. Choose one original edge
from every tree component. These edges form a matching, because the
components are vertex-disjoint, and its cardinality is at least
|V(F)|-|F|>=|Q|-A. Connected components and chosen original edge IDs
can be obtained in linear time.

Applying this to a maximum Q proves

    nu(J) = A+nu(G).

It also proves that a maximum Q decodes to an original maximum matching.
No canonical local form of Q is assumed. In particular, a gadget may
use several external ports; the counting argument already covers that
case. Partial Q also decodes to an original matching of size at least
|Q|-A, although the driver need only decode its final answer.

## 4. The gap-target phase

Let J be any subcubic graph of order N. Start a phase with an explicit
or valid implicitly represented matching Q_0 of size q_0. The nontrivial
phase contract uses an integer target 1<=K<=N. Before initialization,
if K>floor(N/2)-q_0, return LOW with i=0 and the unchanged matching:
the cardinality bound nu(J)<=floor(N/2)<q_0+K proves this conclusion
directly. Thus every initialized phase has K<=floor(N/2)-q_0<=N.
Fix the source parameter a and put
C=a+1. Choose

    L = ceil(10000 C N/K),
    g_* = max{1, floor(K/(100 C))}.

Initialize the source row/bin state from Q_0: unmatched vertices are
singleton bins, matched pairs are the paired remainder, and there are
no initial rows or blockers. Use the deterministic local pair routine,
persistent actual integral carriers and one complete deterministic raw
numerical backend.

The phase ends with one of three distinguished outcomes:

* SUCCESS: g_* gains, yielding size q_0+g_*.
* LOW after i<g_* gains: size q_0+i and the conclusion
  nu(J)<q_0+K.
* SUSPENDED: a checked prerequisite or finite guard fails. This is
  never used as an optimum or LOW certificate.

The proof below establishes the new interpretation of LOW. It imports
the deterministic source state invariants, blocker/debt bound and
priced progress lemma. Their source is the September 24, 2026 OAI
manuscript, Sections 3--5:

<https://github.com/openai/math/tree/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026>.

## 5. No false LOW when the target improvement exists

Suppose a comparison matching has size at least q_0+K. After i gains,
its symmetric difference with the current matching contains at least
K-i vertex-disjoint augmenting paths for that current matching. The
source debt accounting bounds the number of blockers by
2C(g_*-1). Discard paths meeting a blocker.

At a settled state with no distinct-bin edge, orient each remaining
augmenting path from an unmatched endpoint. Its first bin is free and
entered at its exposed base. A free bin has no crossing matching edge.
If the path exits to a row by a nonmatching edge, the next matching
edge is that row's assigned edge, entering another bin at its exposed
base. This assigned bin's unique crossing matching edge was just used,
so a simple path must next leave by a nonmatching edge.

The path must reach the paired remainder: it avoids blockers, cannot
end inside an assigned bin, and cannot enter another free bin through
an assigned row edge. Every bin entry uses its unique physical base.
Vertex-disjointness of the original augmenting paths therefore makes
these prefixes disjoint in both bins and rows. Reassign each prefix
row to its preceding bin. This simultaneous injection leaves at least

    r_0 >= K-i-2C(g_*-1) >= K/2

bins with paired-remainder contacts free. This is an existence argument
about the current represented matching, not a request to materialize
or reroute it during every pricing step.

Scale this conceptual assignment by L. The desired top column
capacities are L+p_d^0-Cw_d. Clip overloaded columns; at most CN mass
is removed because an assigned column loses at most Cw_d and the
total bin weight is at most N. The current feasible top allocation
proves that the clipped partial flow can be completed under these
capacities. Residual source-to-sink augmentation does not decrease
column sink flows, and only the removed mass must be restored.
Hence the specified initially empty contact columns receive at most
CN additional mass.

If Z is the set of bins with paired-remainder contacts, the resulting
feasible alternative top slack satisfies

    s'(Z) >= L r_0 - 2CN.

At a stall the source's cache and eligibility conditions give s_d<=5C
on Z. The difference between the alternative and current top vectors
is a circulation. Each negative logarithmic directional contribution
has magnitude at most one, because the alternative coordinates are
nonnegative. There are at most 4N such coordinates. The positive
contribution is at least

    (L r_0-2CN)/(5C) - N > 12N.

Its directional derivative divided by the sum of absolute logarithmic
derivatives is therefore greater than one half. The deterministic
priced-step interface cannot return a valid LOW in this situation.
The bounded objective range and positive progress per priced step also
preclude endless pricing without a structural action. Thus LOW implies
nu(J)<q_0+K as claimed.

The sole role of a perfect matching in the original source proof was
to supply sufficiently many augmenting paths. The comparison matching
here supplies them directly. Permanently unmatched vertices, odd order
and disconnected components do not invalidate this argument.

## 6. Phase accounting does not require K to be the deficiency

Before its terminal gain, the source accounting gives

    total peeled weight <= 2L(g_*-1) + a negligible positive remainder,
    number of blockers <= 2C(g_*-1),
    expansions + sum of contraction arities = O(N+L g_*).

If K<100C then g_*=1 and L=O_a(N). Otherwise

    L g_* <= (10000CN/K+1) K/(100C) = O(N).

Hence all these totals, and the source tick count, are O_a(N).
The number of initial free bins can exceed 2K; it is still at most N,
which is the bound actually used in the cost analysis.

Persistent carriers and successful pair actions add only near-linear
structural work: each successful pair costs O(L polylog N), and tight
searches charge their output arity. The sparse projection accounting
and either numerical route give the eventual fixed-parameter phase
bound N^(1+O(1/a)+o_a(1)), as stated in
`persistent_carrier_general_matching.md`. All guard suspensions remain
separate from LOW.

## 7. A direct maximum-matching driver

Start from any original matching M, for example a greedy matching, and
its exact gadget lift Q. Initialize

    U = floor(r/2)-|M|.

The identity N=2A+r gives U=floor(N/2)-|Q|, and the optimum-offset
identity implies U>=nu(J)-|Q|. Maintain the integer invariants

    nu(J)-|Q| <= U <= floor(N/2)-|Q|.

While U>0, take K=ceil(U/2) and run a gap phase starting from current Q.
In particular its target satisfies K<=U<=floor(N/2)-q_0, where
q_0=|Q| is that phase's starting cardinality.

On SUCCESS, replace U by U-g_* and keep its gained matching.
On LOW after i gains, replace U by K-1-i and keep that matching.
The second update is valid because integral cardinalities turn
nu(J)<q_0+K into nu(J)<=q_0+K-1. A suspended branch proposes no answer.
The upper physical-cardinality invariant is preserved as well:
success subtracts the same gain from U and floor(N/2)-|Q|, while
LOW gives K-1-i<=U_old-i<=floor(N/2)-(q_0+i).

For U above a constant multiple of C, success decreases U by a fixed
fraction depending only on a; LOW approximately halves it. For smaller
U, a success gains at least one and LOW strictly reduces the bound.
There are O_a(1+log(r+1)) phases.

When U=0, Q is maximum by the maintained invariant. Materialize it
and apply the decoder. The complete fixed-parameter time is

    O(n+m) + (m_s+1)^(1+O(1/a)+o_a(1)).

This driver does not use a perfect-matching decision search, a threshold
network, a warm-start approximation, or a restricted graph family.
The uniform verified wrapper is a separate argument in
`uniform_general_maximum_matching.md`; it protects accepted output
correctness even for exceptional finite branch behavior, but does not
replace the fast-branch proof above.
