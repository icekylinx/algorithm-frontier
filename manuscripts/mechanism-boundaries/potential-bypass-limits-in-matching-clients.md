# Potential-gradient shortcuts and their limits in the actual matching clients

**Separate mathematical analysis, 24 October 2026.** An ordinary
gradient that is close to a vertex potential permits a useful
shortest-return-cycle shortcut. The two actual matching clients
do not satisfy that condition automatically. This note gives
explicit legal states, including the literal zero-flow
initialization of an exchange projection, and states the
additional algorithmic interface that would be needed.

No change to the current matching theorem or exponent is claimed.

## 1. The precise shortest-return-cycle shortcut

Let an oriented graph have positive lengths, ordinary edges, and
one distinguished return edge $t\to s$. Suppose a supplied
potential $p$ satisfies
$$
|g_{uv}-(p(v)-p(u))|\le \epsilon\ell_{uv}
                    \quad\text{on ordinary edges}.
 \tag{1}
$$
Ordinary paths may use either reference orientation, with the
corresponding signed gradient. Let
$$
d=\operatorname{dist}_{\ell,{\rm ordinary}}(s,t),\qquad
 \kappa=g_{\rm ret}+p(t)-p(s).
$$
If $s,t$ are connected, a shortest ordinary path plus the
return edge has ratio within additive $2\epsilon$ of the
global maximum absolute circulation ratio.

Indeed, for any circulation $c$, an ordinary shortest-path
Lipschitz potential gives
$$
\|\ell c_{\rm ordinary}\|_1\ge d|c_{\rm ret}|.
$$
Hence
$$
|g^{\mathsf T}c|
 \le|\kappa|\,|c_{\rm ret}|
       +\epsilon\|\ell c_{\rm ordinary}\|_1.
$$
The optimum is at most
$|\kappa|/(\ell_{\rm ret}+d)+\epsilon$; the stated candidate
has ratio at least that fraction minus $\epsilon$.
Circulations omitting the return edge have ratio at most
$\epsilon$, so they are included. At $\epsilon=0$ the
shortest-return-cycle formula is exact.

This is a STATIC implication from a supplied potential. Checking
it and computing a shortest path costs a full graph scan plus
ordinary shortest-path work. It does not give the subpolynomial
amortized update/query interface required by the numerical client.
The detailed proof also appears in
[the logarithmic-state obstruction](logarithmic-client-quality-obstruction.md),
Section 7.1.

## 2. A legal top-ledger state with large potential defect

Let $C\ge3$, let $w\ge2$ be an integer, and set
$$
L=3Cw,\qquad \sigma=8\delta.
 \tag{2}
$$
Use three bins $d_1,d_2,d_3$, each of weight $w$, and two
rows $r_1,r_2$, each adjacent to all three bins. For every
integral level use the allocation
$$
X^{\rm int}=
 \begin{pmatrix}
 0&2L/3&L/3\\
 2L/3&0&L/3
 \end{pmatrix}.
 \tag{3}
$$
Its four positive incidences form a tree. Thus the actual
integral allocation already has an acyclic carrier. Each row
sums to $L$, each bin load is $2L/3$, and each residual is
$L/3=Cw$. Zero integral debts satisfy every required floor
$c_jw$ with $c_j\le C$.

At the top instead use
$$
X^0=
 \begin{pmatrix}
 1&2L/3-1&L/3\\
 2L/3-1&1&L/3
 \end{pmatrix},
 \qquad
 p^0_d=\sigma,\qquad s_d=\sigma.
 \tag{4}
$$
The column loads are unchanged, so the top equations
$$
s_d=L-\operatorname{load}(d)+p^0_d-Cw
 \tag{5}
$$
hold exactly. The allocation entries are positive integers
when $L>3$. Slacks and debts are exact grid values, and
the total top debt $3\sigma=24\delta$ is below the phase's
tiny-debt allowance. Exact cached values $\sigma=8\delta$
are already above the positivity-service trigger. There is
no hidden need to repair these slacks before a pricing call.

Strict Hall holds: no proper subset of the three bins contains
a captive row, whereas the full set has two captive rows and
deficiency one. Bottom weights obey $3w=L/C\le L$.
The carrier's canonical injection supplies one free bin.

This has an actual subcubic physical realization. Realize
each bin by an odd cycle of length $2w-1$, using distinct
cycle vertices as the two row contacts. Each row has its
three prescribed contacts; every physical degree is at most
three. All bins are constructively factor-critical. There
are no distinct-bin edges and no paired-remainder contacts.

For compatibility with a nontrivial legal phase target WITHOUT
adding original isolated vertices, retain this $6w-1$-vertex
core and add $2w-1$ disjoint triangle bins, each of weight
two, together with two disjoint matched edges in the paired
remainder. There are no edges between these components. The
total number of physical vertices is
$$
N=(6w-1)+3(2w-1)+4=12w.
$$
Every vertex has positive degree, the maximum degree is three,
and no bin has a remainder contact. The additional bins have
zero debts and top slacks $L-2C>0$; they contribute only
slack leaves to the numerical graph.

Choose $K=40000$, for sufficiently large integer $w$.
Then the prescribed threshold is exactly
$$
\left\lceil10000CN/K\right\rceil=3Cw=L.
 \tag{6}
$$
The represented matching has size
$(3w-1)+(2w-1)+2=5w$, so its physical cardinality
deficit is $w$. Taking $w\ge80000$ makes both the
phase target and the upper gain bound
$U_{\rm gain}=80000$ compatible with the direct driver's
invariant; the latter produces this target.
This confirms the algebraic/physical phase
scope; it is not a claim that a particular earlier sequence
of the implemented algorithm reaches exactly (4).

## 3. No potential fits this top gradient accurately

For the top objective, $g_e=\lambda_e=1/x_e$ on allocations
and $g_d=\lambda_d=1/s_d$ on slack arcs. Let
$$
A=2L/3-1.
$$
The row-only four-cycle that increases $x_{11},x_{22}$
and decreases $x_{12},x_{21}$ has ratio
$$
\frac{2-2/A}{2+2/A}
                     =\frac{A-1}{A+1}=1-O(1/L).
 \tag{7}
$$
Every vertex potential vanishes on this exact circulation.
Consequently any potential approximation on the allocation
graph satisfies
$$
\max_e\frac{|g_e-(p(v_e)-p(u_e))|}{\lambda_e}
                     \ge\frac{A-1}{A+1}.
 \tag{8}
$$
In particular, the error cannot be a small constant, let
alone the numerical accuracy parameter.

The same conclusion survives removing ANY ONE incidence
as a putative distinguished return edge. Removing an edge
in one column leaves the four-cycle on the other two
columns. Its ratio is either (7) or
$$
\frac{1-1/A}{1+1/A+6/L}=1-O(1/L).
 \tag{9}
$$
Removing a slack arc leaves all the allocation cycles.

The slack source does not cure this problem. Every elementary
cycle using one row, two bin contacts, and their two slack
arcs has canceling slack gradients because all $s_d=\sigma$.
Its numerator is at most one in absolute value and its
length is at least $2/\sigma$, so its ratio is at most
$\sigma/2$. Thus checking only these short slack-source
cycles misses the strong row-only direction (7).

The official integer pricing and degree-three port paths
do not remove the obstruction. Gradient errors telescope
against native circulations, real prices are multiplied by
the common large price scale, and the additional zero-gradient
port-path length is negligible compared with those real
prices. All parallel and connector identities remain literal.

## 4. It need not be an isolated off-center iterate

Consider the top client starting from (4), with no structural
action available. Let $\eta$ bound the TOTAL core debt,
including the initial $3\sigma$ and all later positivity
increments. On the guarded prefixes this remains below a
negligible $\eta<S^{-800}$. Total core row mass stays $2L$.
The other two columns each have upper load $2L/3+p_d$,
so column capacities imply
$$
\operatorname{load}(d_1)
                               \ge 2L/3-\eta.
 \tag{10}
$$
As long as $x_{11}\le L/100$, it follows that
$x_{21}\ge 0.65L$, for the guarded sizes. One of the other
two entries in row one, say $x_{1j}$, is at least
$(L-x_{11})/2\ge0.495L$.

The four-cycle increasing $x_{11},x_{2j}$ has positive
derivative sum at least $1/x_{11}$; its negative sum is
at most
$$
1/x_{21}+1/x_{1j}<4/L.
 \tag{11}
$$
Its ratio is consequently at least
$$
\frac{1-4x_{11}/L}{1+4x_{11}/L}
                         \ge\frac{12}{13}>\frac9{10}.
 \tag{12}
$$
Thus every potential still has normalized error above $9/10$,
and a valid LOW is impossible.

An accepted numerical step changes each coordinate by at most
a $q/100$ fraction of its present value. Explicit positivity
repairs contribute at most the tiny total $\eta$; while
$x_{11}\le L/100$, it cannot be the large donor of its row.
Starting at $x_{11}=1$, reaching $L/100$ therefore takes
$$
\Omega(q^{-1}\log L)
 \tag{13}
$$
accepted steps. If it never reaches that value, (12) continues
to hold instead. This is a trajectory statement FROM the
displayed valid state, not a proof of its reachability from
the phase's prescribed initial partition.

Accordingly, feasibility, positive slacks and exact conservation
do not imply that all but a constant number of priced queries
have nearly conservative gradients. Proving a stronger
reachable-state property would be a new theorem.

## 5. Projection gradients fail conservativity already at initialization

The obstruction is more immediate in the ACTUAL exchange network.
Every positive INTEGRAL parent allocation $x_e>0$, on an incidence
$(r,d)$, creates two DISTINCT ordinary arc IDs:
$$
d\longrightarrow r\quad[\operatorname{cap}=x_e],
       \qquad
        r\longrightarrow d\quad[\operatorname{cap}=L+1].
 \tag{14}
$$
Both have lower bound zero. In a threshold test their upper
capacities are multiplied by 16, both initial flows are zero,
and both lower/upper pads equal $\zeta=4\delta$.

For either arc with scaled upper $U_e\ge16$, the initial
exact gradient and absolute price are
$$
g_e=\frac1\zeta-\frac1{U_e+\zeta},\qquad
       \lambda_e=\frac1\zeta+\frac1{U_e+\zeta}.
 \tag{15}
$$
Their genuine directed two-edge cycle has ratio
$$
\frac{2/\zeta-\sum_{e=1}^2 1/(U_e+\zeta)}
      {2/\zeta+\sum_{e=1}^2 1/(U_e+\zeta)}
                         =1-O(\delta).
 \tag{16}
$$
It uses no numerical return arc. Every vertex potential
vanishes on it, so the best normalized potential error on
the ordinary graph is at least (16).

This is the literal zero-flow initialized state of the local
or all-expanded projection, whenever a positive incidence is
represented. No speculative reachability or choice of later
steps is involved. It also survives exact integer rounding:
the leading lower-pad reciprocal is common, and the two
positive rounded labels cannot become conservative around
their directed two-edge cycle.

These are not the forward and reverse representations of the
SAME undirected edge. They are two different ordinary flow
variables with different capacity descriptors. A positive
circulation on both changes the barrier variables while
leaving the induced allocation
$x'_e=x_e-F_{d,r}+F_{r,d}$ unchanged. The current objective
legitimately includes that degree of freedom.

One could design a different signed-coordinate formulation
that combines the two directions and removes such redundant
exchange circulations. It would require a new barrier,
local boundary/lock proof, exact recovery interface, and
numerical update analysis. It is not an allowed loop erasure
of the current objective, and it would not by itself eliminate
the top-state obstruction (7).

## 6. What a useful stronger theorem would have to supply

The positive shortcut in Section 1 would need two separate
ingredients for a worst-case time improvement:

1. A proved centrality or gradient-decomposition invariant
   giving sufficiently small residual $\epsilon$ on a
   suitably defined ordinary graph for the queries being
   replaced, together with a charged treatment of all
   exceptional queries.
2. A deterministic dynamic shortest-path/potential interface
   handling the clients' signed gradient changes, positive
   length changes, topology edits, and representation
   retirement, with actual-size initialization and
   subpolynomial amortized work. Recomputing a static
   shortest path at every numerical query does not have
   that bound.

An approximate potential found only by solving the general
weighted cycle-ratio dual is not a simplification: that is
another formulation of the same optimization obligation.
For the ordinary graph with incidence matrix $B$, finite
linear-programming duality gives the exact identity
$$
\min_p\max_e\frac{|g_e-(B^{\mathsf T}p)_e|}{\ell_e}
 =
 \max_{\substack{Bc=0\\ \|\ell c\|_1\le1}}g^{\mathsf T}c.
 \tag{17}
$$
The two inequalities defining each absolute residual produce
signed dual variables, whose vertex constraints are $Bc=0$
and whose total weighted absolute value is at most one.
Thus (17) requires the same circulation optimization unless
additional structure makes the potential available cheaply.
Likewise, conservation alone supplies no centrality:
(4) obeys all ledger equations and (16) occurs at exact
projection initialization.

These examples leave open an algorithm that deliberately
maintains centrality, optimizes combinations of correction
circulations, or changes the projection barrier. They rule
out obtaining the desired worst-case improvement solely
from the present logarithmic objective, matching feasibility,
or exact-conservation invariants.
