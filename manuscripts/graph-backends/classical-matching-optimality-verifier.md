# A classical independent optimality verifier for general matching

The final matching check can use a pre-2026 algorithm independently
of the newer simplified implementation. The relevant primary source
is Harold N. Gabow,
[The Weighted Matching Approach to Maximum Cardinality Matching,
arXiv:1703.03998v1](https://arxiv.org/abs/1703.03998v1), 2017.
Figures 1–2 give the first search and its no-augmenting-path outcome;
Sections 3 and 5 provide its correctness and implementation. Section 5
uses the incremental-tree set-union algorithm of Gabow and Tarjan,
[A Linear-Time Algorithm for a Special Case of Disjoint Set Union](https://doi.org/10.1016/0022-0000(85)90014-5),
*Journal of Computer and System Sciences* 30 (1985), 209–221.

Only one search is needed. Neither the complete blocking-phase
algorithm nor a recomputation of maximum matching from the empty
matching is used by the verifier.

## 1. Starting from an arbitrary proposed matching

Given an undirected general graph $G$ and a proposed edge list
$M$, first check edge validity and distinctness of matched endpoints.
An invalid proposal is rejected. For a valid matching, initialize
the first search of Gabow's algorithm using
$$
w(e)=\begin{cases}2,&e\in M,\\0,&e\notin M,\end{cases}
 \qquad y(v)=1,
$$
with no nontrivial initial blossoms. These are legitimate initial
dual data for every matching: all edge inequalities hold, every
matched edge is tight, and all free vertices have equal dual value.
The search structures are constructed from the current free
vertices, without any augmentation history.

If the search finds an augmenting path, reject the proposal. If it
exhausts the search with no augmenting path, accept. The augmenting
path criterion proves that acceptance is equivalent to maximum
cardinality. The search forest may have roots in many connected
components; a perfect-matching or connectedness promise is not
required.

## 2. A conservative near-linear implementation

The source's Section 5 implements one search in $O(n+m)$ time
using the 1985 specialized set-union structure. For the present
application, the weaker bound
$$
O(n+m\,\alpha(n+2))                     \tag{1}
$$
is sufficient. It follows by using ordinary disjoint-set union for
the same $O(m)$ finds and $O(n)$ unions; keep the blossom's
base label separately from the representative chosen by union by
rank. The remaining adjacency scans, blossom bookkeeping and
integer buckets have linear total size.

There is a useful explicit termination convention for an unsuccessful
search. Let $\Delta$ be the accumulated dual adjustment, so a
free vertex has dual value $1-\Delta$. The source's Section 5
shows that the existence of any augmenting path implies
$\Delta\le n/2$. Therefore the bucket scan can stop and certify
absence as soon as no next event exists at an index at most $n/2$.
It never scans an unbounded interval while waiting for an event.
Finding a positive outcome only needs the search's boolean result;
the verifier need not expand the augmenting path.

One may instead use simple balanced set representations, paying
$O((n+m)\log(n+2))$ and retaining the same mathematical
acceptance test. This also fits every almost-linear envelope in
the matching construction.

## 3. Use after shared preprocessing

After the original input has been scanned and isolated vertices
removed, let the trusted compact graph have $r$ vertices and
$m_s$ distinct nonloop edges. Then $r\le2m_s$ unless the
graph is empty, which is decided directly. Formula (1) becomes
$O(m_s\alpha(m_s+2))$. Apply the verifier to this compact graph
or to an independently established exact kernel, and map accepted
edge IDs back to the original input once.

The verifier does not inspect any proposed numerical certificate,
LOW decision, dynamic-forest state, or approximation quality from
the fast branch. Conversely, passing it does not prove the fast
branch's running-time analysis. Its work is charged inside the
branch's instruction allowance, as in
[the uniformization construction](deterministic-uniformization-by-optimality-check.md).
