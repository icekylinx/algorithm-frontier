# Deterministic token routing by edge thresholds and expander pruning

**Mathematical construction, 24 October 2026.** This note turns the
deterministic decremental expander-path primitive reconstructed in
[separated-static-sparsifier-parameters.md](separated-static-sparsifier-parameters.md)
into an explicit simultaneous token router. It uses that primitive's
path length and expander-pruning bounds. It does not use the CHS
distributed hierarchy, a distributed-round-to-work simulation, or a
random routing procedure.

The primary dependencies are Chuzhoy--Saranurak,
[arXiv:2009.08479v1](https://arxiv.org/pdf/2009.08479), Theorem 3.7
and Section 3.2, together with the finite-word, small-instance, and
loopless-multigraph adapters proved in the linked note. The construction
below is separate from those source algorithms.

## 1. Input and the precise decremental interface

Let $H=(V,E)$ be a fixed loopless multigraph with $m\geq1$
edges and no isolated vertices. Parallel edges retain distinct IDs.
Assume $H$ has conductance at least $\phi$, where
$0<\phi\leq1$. Every degree and volume in this note is measured
in this ORIGINAL fixed graph:

$$
d(v)=\deg_H(v),\qquad
 \mathrm{vol}(P)=\sum_{v\in P}d(v).
 \tag{1}
$$

There are $M$ explicitly listed ordered token pairs. At most
$D d(v)$ tokens start at $v$, and at most $D d(v)$
tokens end at $v$, for a known $D\geq1$. The two bounds are
separate, so the number of token endpoints in a set $P$ is at
most $2D\mathrm{vol}(P)$. Multiplicities and opposite
orientations are allowed. A pair with identical endpoints is returned
immediately with its empty path; this cannot increase any load.

We use a deterministic decremental oracle with the following interface.
For a fresh copy of $H$, it starts with a pruned set $P=\varnothing$,
accepts explicit edge deletions, and only enlarges $P$. For an
absolute constant $c_0$, after $t$ explicit deletions, within
its permitted deletion budget,

$$
\mathrm{vol}(P)\leq c_0t/\phi.
 \tag{2}
$$

For any two vertices outside $P$, it returns an explicit path
in the surviving graph, of at most $\Lambda$ edges. We erase any
repeated vertices before using a returned walk as a path. The interface
remains valid with larger $\Lambda$. Initialization and all allowed
updates in one oracle generation cost $mF\mathrm{poly}(U)$;
explicit path output costs $\Lambda\mathrm{poly}(U)$ per
query. This is the interface supplied by the linked reconstruction;
in particular $F$ is construction work, not a path-length bound.

Here $U$ bounds record sizes and logarithms of the explicit input
and parameter ranges. If no such master parameter is fixed, all
$\mathrm{poly}(U)$ factors below may instead include the
relevant input-word bit costs and $\log(M+m+2)$.

### 1.1 Extending the interface through deletion-quota exhaustion

Suppose the permitted number of explicit deletions is
$\lfloor\phi m/c_q\rfloor$, for an absolute constant $c_q$.
If the next threshold-deletion request exceeds this quota, count that
request as the next explicit deletion and declare **all** vertices
pruned. Do not send the excessive request to the source oracle and do
not query that oracle again. If $t$ includes this first excessive
request, then $t>\phi m/c_q$, and therefore

$$
\mathrm{vol}(V)=2m<2c_qt/\phi.
 \tag{3}
$$

Thus, with $c=\max\{c_0,2c_q\}$, the augmented interface always
satisfies

$$
\mathrm{vol}(P)\leq ct/\phi.
 \tag{4}
$$

This convention covers quotas below one: the first actual request pays
for declaring the whole host pruned. The internal edges removed because
an endpoint is pruned are not additional explicit deletions in $t$.
They are already covered by the original-volume guarantee (4).

## 2. The routing algorithm

Fix an integer threshold

$$
\tau\geq\max\{2,\lceil8cD\Lambda/\phi\rceil\}.
 \tag{5}
$$

Maintain a global integer load $\ell_e$, initially zero, for every
original edge ID $e$. The load counts previously returned paths,
including paths whose edges an earlier oracle generation subsequently
deleted. Such paths remain valid paths in the ORIGINAL static host.

In round $j=1,2,\ldots$:

1. Initialize a fresh decremental oracle on the full original graph
   $H$, with $P=\varnothing$. Retain all global loads.
2. Scan the still-unassigned token pairs in a fixed order. If either
   endpoint is already pruned, leave the token for the next round.
   Otherwise query a path between the endpoints, save its explicit
   original-edge-ID list as that token's final route, and increment
   $\ell_e$ by one on each edge of that simple path.
3. For every edge whose load has now reached $j\tau$, request its
   deletion if it is still present in the current oracle. A previous
   request in this same transaction may already have removed it through
   pruning; skip such an absent edge instead of issuing an illegal
   duplicate deletion. Apply the live-edge requests and all resulting pruning before
   issuing another query. If the deletion quota is exceeded, use
   Section 1.1 and stop querying in this round. All remaining unassigned
   tokens then have pruned endpoints.
4. Discard this oracle generation, and start the next round only if
   tokens remain.

All changes caused by a path are a single no-query transaction. Its
saved route is valid in the static host even if one of those changes
immediately prunes its endpoints. If several edges reach the threshold
on the last route, it is enough to count the requests actually examined
up to the first excessive request; no later request is needed to
justify (3). All edge loads nevertheless include the whole saved path.

No source operation is reversed. Fresh rounds are separate oracle
generations. Global load counters and already returned paths belong to
the router, not to a decremental oracle generation.

## 3. Progress and congestion

Immediately before round $j$, every edge satisfies

$$
\ell_e\leq(j-1)\tau.
 \tag{6}
$$

This is true initially. Within the round, an edge is deleted as soon as
its load reaches $j\tau$, so no later path in that round can use
it. A simple queried path increases its load by at most one. Thus the
load never exceeds $j\tau$, including when a whole-host abort
ends the round, and (6) follows inductively.

Let $B_j$ be the number of tokens routed in this round, and let
$t_j$ be the number of examined threshold-deletion requests,
counting only still-live edges and including the first excessive request
if any. A newly thresholded edge skipped because pruning already removed
it is unavailable for every later query in this round, so it cannot
violate (6). Every counted edge required
at least $\tau$ NEW path traversals during this round, by (6).
Every newly assigned path uses at most $\Lambda$ edges. Hence

$$
t_j\tau\leq\Lambda B_j.
 \tag{7}
$$

The weaker $t_j\tau/2\leq\Lambda B_j$ would suffice if an
implementation uses harmless integer-threshold slack. We retain (7)
for the literal algorithm above.

At the end of the scan, every remaining token has an endpoint in the
final pruned set $P_j$. Indeed, a scanned token with two surviving
endpoints was routed, and pruning is monotone during a round. Let
$R_j$ be the number of remaining tokens. The original endpoint-load
bound applies to this subset of the original demand list, so (4), (5),
and (7) give

$$
\begin{aligned}
 R_j
 &\leq2D\mathrm{vol}(P_j)
 \leq 2Dc\,t_j/\phi\\
 &\leq \frac{2Dc\Lambda}{\phi\tau}B_j
 \leq B_j/4.
 \end{aligned}
 \tag{8}
$$

In particular $R_j\leq B_j/2$, even under the weaker version of
(7). If $N_j$ tokens enter a round, $N_j=B_j+R_j$ and thus
$R_j\leq N_j/3$ with this conservative constant. A nonempty
round must route at least one token: otherwise it makes no explicit
deletion, prunes nothing, and could not leave a token unassigned.

There are therefore $O(\log(M+2))$ rounds, and all tokens are
routed. Every output route has at most $\Lambda$ edges, while
(6) bounds the final edge congestion by

$$
\boxed{
  O\!\left(\frac{D\Lambda}{\phi}\log(M+2)\right).
 }
 \tag{9}
$$

The ceil in (5) adds only a constant factor because
$D\geq1$, $\Lambda\geq1$, and $\phi\leq1$.
Both orientations of a physical undirected edge contribute to the
same load. Distinct parallel edges have distinct loads.

## 4. Work, explicit outputs, and finite numbers

The still-unassigned lists shrink geometrically. Scanning them costs
$O(M)$ total. Exactly one successful path is saved per nontrivial
token, so path extraction, loop erasure if needed, and edge-load
increments cost

$$
O(M\Lambda)\mathrm{poly}(U).
$$

An edge reaches the current threshold at most once in a round. The
source's update work, including its own pruning metadata, fits its
generation bound. Initialization and updates across all generations
cost

$$
O(mF\log(M+2))\mathrm{poly}(U).
$$

Resetting the oracle and initializing its original edge IDs is charged
to this actual $m$-sized setup. No array is padded to a larger
master universe. The router's edge-load array is initialized only once.
Tracking whether an endpoint is pruned takes the oracle's explicit
membership query or a Boolean mark updated through its pruning log.
The total original-volume log in a generation is at most $2m$.

Consequently the total work is

$$
\boxed{
  O\bigl(mF\log(M+2)+M\Lambda\bigr)
       \mathrm{poly}(U).
 }
 \tag{10}
$$

There is ONE aggregate demand list and one oracle generation per round.
In particular, initialization is **not multiplied by $D$**. The
algorithm does not require coloring the token demands into $D$
matchings. The only dependence on $D$ outside the unavoidable
explicit token count is in the congestion threshold and its word size.

All thresholds can be conservatively rounded upward from the supplied
rational or dyadic parameters. Loads and token counters use
$O(\log(M+\tau+2))$ bits. The number of rounds is discovered
by the remaining-list test; no real logarithm or noncomputable cutoff
is used. If desired, an explicit geometric bound on the number of
rounds is a checked guard.

## 5. The parameterized router obtained from the reconstructed oracle

Let $h=\lceil\log_2(U+2)\rceil$, let $q\geq2$,
$r\geq1$, and assume $q,r\leq U$ and $qrh\leq U$.
The reconstructed oracle supplies, on the expander pieces used by the
static sparsifier,

$$
\phi^{-1}=\exp O(rh),\qquad
 \Lambda=\exp O(qrh),\qquad
 F=\exp O(U/q+U/r+r^2h+qrh).
 \tag{11}
$$

The graph and its entire token list must be explicit and have at most
$2^{O(U)}$ records. The same actual-size clipping and small-graph
base cases as in the oracle note apply. Enlarging a fixed constant in
the output factor gives

$$
\Gamma=\exp O(qrh)
 \tag{12}
$$

such that the token paths have length at most $\Gamma$, edge
congestion at most $D\Gamma$, and total work

$$
\bigl(mF+M\Gamma\bigr)\mathrm{poly}(U).
 \tag{13}
$$

The factor $\log(M+2)$ is absorbed by the displayed polynomial
and $\Gamma$. The construction-work factor $F$ does not
enter (12), nor the degree-proportional congestion factor $D\Gamma$.

For the weighted-witness application, the resulting token paths are
fed to
[deterministic-weighted-path-selection.md](deterministic-weighted-path-selection.md).
That separate lemma first simplifies each individual ambient input
image and then selects one candidate per witness edge. It is the
selection lemma, not the threshold router alone, that removes the
ambient input-path-length factor from composed congestion. Physical
ambient list expansion still costs its actual output size.

## 6. Scope

The theorem applies to arbitrary explicit token pairs in the fixed
expander host under the stated degree-proportional endpoint bound. It
does not assume demands form a matching, a permutation, or a simple
graph. It provides routes in the original host, so the temporary
deletions made by different generations have no effect on the final
validity of any output route.

This is an auxiliary routing theorem. A general-graph matching time
bound additionally requires the separately proved static ambient
sparsifier, touched-set maintenance, recursive raw-cycle backend, and
matching-driver interfaces. No new matching exponent follows merely
from (9).
