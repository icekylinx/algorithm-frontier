# Sequential fresh-cut matching without an initial-cut ambiguity

**Mathematical implementation lemma, 24 October 2026.** This note
supplies the matching/cut interface used by the reconstructed virtual
hierarchy. It uses the exact bounded-length packing and the complete
empty-initial-cut lemma proved in
[sequential_short_path_matching.md](sequential_short_path_matching.md),
Section 2.1. It does not import the general \(C_{\rm in}\) bookkeeping
in the abbreviated proof of Chang--Saranurak,
[arXiv:2007.14898](https://arxiv.org/pdf/2007.14898), Lemma D.12.

The changes are sequential implementations of the required structural
interfaces. No CONGEST round bound is converted to work without
accounting for its operations. The 5/6 matching construction is
independent of this additional hierarchy route.

## 1. The proved empty-cut one-round primitive

Let \(H\) have \(N\) vertices, \(m\) edge IDs, and maximum degree
\(\Delta\geq1\). Let \((S_i,T_i)_{i=1}^k\) be disjoint terminal
pairs, with \(0<|S_i|\leq|T_i|\). Let \(0<\eta\leq\Delta\),
\[
 d=\left\lceil c\Delta\eta^{-1}\log(N+2)\right\rceil,\qquad
 \zeta=\frac{\eta}{100\Delta(d+1)}.                       \tag{1}
\]
A sufficiently large fixed \(c\) gives this deterministic alternative:

* return at least \(\zeta\sum_i|S_i|\) vertex-disjoint
  same-color paths, each of length at most \(d\); or
* return an actual host cut \(C\), with \(|C|\leq N/2\)
  and \(\Psi_H(C)\leq\eta/2\), which either has
  \(|C|\geq N/3\), or satisfies
  \[
       |C\cap(S_i\cup T_i)|\geq |S_i| \quad\text{for all }i.
                                                               \tag{2}
  \]

The work is
\[
                 O(k(m+N)(d+2)),                            \tag{3}
\]
apart from fixed polynomial word costs. Path congestion is
literally one, independent of \(k\).

For completeness, the key cut accounting is as follows.
Greedily process colors with exact maximal short vertex-disjoint
path packing. If the number of paths is too small, their vertex
set \(W\) has \(\Delta|W|<\eta\sum_i|S_i|/100\).
Delete its incident edges but retain all vertex slots. Every
same-color terminal distance now exceeds \(d\). Repeated
distance-ball separators yield a cut of sparsity at most
\(\eta/4\) before the deleted edges are restored.

If that cut is unbalanced, (2) and disjointness imply
\(|C|\geq\sum_i|S_i|\). If it is balanced, then
\(\sum_i|S_i|\leq N/2\leq3|C|/2\).
Either inequality pays for all restored incident edges.
No terminal lies outside the stated host universe, and no
previous cut is silently deleted.

For one color, the returned cut separates all of its current
source terminals from all of its current sink terminals.
It can be oriented to put the sources on its designated side.
Sparsity is unchanged by this orientation, although that
designated side need not be the smaller side.

## 2. Match half of every pair, or certify failed pairs

Fix initial disjoint pairs \((S_i^0,T_i^0)\), with
\(|S_i^0|\leq|T_i^0|\), and put
\[
             b=\min_i |S_i^0|/N>0.
 \tag{4}
\]
Start with empty matchings. In each round, apply Section 1
to the still-unmatched terminal sets of the active pairs.
A pair becomes inactive once at least half of its original
sources have been matched. Previously used matching endpoints
are removed from their own terminal sets, but the physical
host \(H\) is unchanged.

If paths are returned, add them to the relevant matchings.
If a cut is returned, stop and publish that cut and all
previously found matching paths.

While pair \(i\) is active, its current source set satisfies
\[
                  |S_i|>|S_i^0|/2\geq bN/2.
 \tag{5}
\]
A successful round reduces the active unmatched source total
by a factor at most \(1-\zeta\); removing newly finished pairs
only helps. Initially this total is at most \(N/2\). Thus the
number of successful rounds before all pairs finish or a cut
occurs is
\[
 R=O\!\left(\zeta^{-1}\log(2/b)\right)
  =\operatorname{poly}(\Delta,\eta^{-1},\log(N+2),\log(2/b)).
                                                               \tag{6}
\]
The graph never accumulates removed path vertices between
different rounds. Only one round's temporary packing is
vertex-disjoint; the resulting total path congestion is at
most \(R\), and dilation is at most \(d\).

An unbalanced returned cut contains at least
\(|S_i|>|S_i^0|/2\) original terminals of every unfinished pair,
by (2). Finished pairs already have the required matching.
Consequently the exact output contract is:

* every pair has a matching of size at least half its original
  source set; or
* a balanced cut is returned; or
* a cut of sparsity at most \(\eta/2\) contains at least
  half the original source count in \(S_i^0\cup T_i^0\)
  for every pair that did not receive its required matching.

The work is
\[
             O(k(m+N)(d+2)(R+1)).                           \tag{7}
\]
The polynomial \(k\) factor is construction work only.
In the hierarchy \(b=\Omega(1/k)\), so its influence on path
congestion is only \(\log(2/b)=O(\log(k+2))\).
All constants are independent of the hierarchy depth.

No general nonempty-\(C_{\rm in}\) theorem was used.

## 3. Fresh cuts in the outer cut-matching games

In the simultaneous KKOV games on parts \(V_1,\ldots,V_k\),
let \(j=1,2,\ldots\) be the outer matching-round index.
Each active game asks for a matching between
\[
 |V_i|/4\leq|S_i^0|\leq|V_i|/2,\qquad T_i^0=V_i\setminus S_i^0.
                                                               \tag{8}
\]
Run Section 2 on the FULL current host graph with cutoff
\[
                            \eta_j=\psi/(16j^2).            \tag{9}
\]
An accumulated failure cut is used only for bookkeeping;
its vertices are not removed from this call. The embedded
paths are allowed to pass through that accumulated set.

If the new cut \(C_j\) is balanced, stop the weak hierarchy
routine and return a cut-only answer. Otherwise mark as failed
exactly those active games whose current matching request
received fewer than half of its original sources, and add
\(C_j\) to the accumulated union \(C_{\rm acc}\).
If every request received its half-matching, add no failure
cut and mark no game as failed. Such a failed block contributes at
least \(|V_i|/8\) of its vertices to the union, by (8) and
Section 2. Continue each other active game with its new
matching. Finished games retain their successful virtual
expander and embedding.

Stop the entire weak routine as soon as
\[
                      |C_{\rm acc}|\geq\beta N,
                  \qquad \beta=1/1000.                     \tag{10}
\]
Before the last addition the union has size below \(\beta N\);
each new cut has size at most \(N/2\). Therefore at the first
crossing its size is at most \((1/2+\beta)N\). If necessary
return its complement. Both choices have fixed positive
balance, and complementation loses less than a factor two
in boundary-to-side ratio.

For every prefix, even with overlapping cuts,
\[
 \begin{split}
 |\partial C_{\rm acc}|
 &\leq\sum_j|\partial C_j|
 \leq\sum_j(\eta_j/2)|C_j|\\
 &\leq\left(\sum_{j\geq1}\frac{\psi}{32j^2}\right)
                                      |C_{\rm acc}|
 <(\psi/8)|C_{\rm acc}|.
 \end{split}                                                \tag{11}
\]
Each \(C_j\) is a subset of its final union; this is why
overlap creates no problem. Thus the returned actual-host
cut has sparsity below \(\psi\), with substantial fixed slack.

Each recursive cut player on an ABSTRACT matching graph is
requested to return continuing cuts of sparsity at most \(1/8\).
The explicit proof in
[half_matching_entropy_progress.md](half_matching_entropy_progress.md)
then bounds the number of active matching rounds by
\(512\lceil\log_2(N+2)\rceil\). It uses the actual balanced
cuts and half-matchings, counting parallel occurrences separately.
This abstract cut-player threshold is distinct from the
actual embedding-host cutoff \(\eta_j\) in (9). A virtual-expander
success stops that game's execution and does not need to be
inserted into its unfinished matching graph. The source's
incorrect per-round entropy calculation at threshold \(1/2\)
is not used.

Consequently
\[
 \eta_j^{-1}\leq
           \operatorname{poly}(\log(N+2))\,\psi^{-1}
 \tag{12}
\]
throughout the actual execution. Path length, union congestion,
and work in (6)--(7) remain fixed polynomials in
\(\Delta,\psi^{-1},\log N\), apart from the explicit local
construction factor \(k\). Formula (9) is executable without
knowing the constant hidden in the \(O(\log N)\) round theorem.

This is the interface needed by the weak virtual hierarchy.
It avoids all clipping or source/sink balance questions created
by restricting an old terminal pair to \(V\setminus C_{\rm in}\).

## 4. Exact saturation on a proved expander

Suppose \(H\) has edge sparsity at least \(\sigma>0\), and
\(S,T\) are disjoint with \(|S|\leq|T|\). Apply Section 1 with
one color and \(\eta<\sigma\), always on the unchanged graph.
A returned cut would have sparsity at most \(\eta/2<\sigma\)
and is therefore impossible while any source remains.

Every round matches at least a \(\zeta\) fraction of the
remaining sources. Matching endpoints are removed only from
the source/sink sets. After
\[
                 O(\zeta^{-1}\log(N+2))                    \tag{13}
\]
rounds every source is matched. All paths are explicit,
have length \(O(\Delta\sigma^{-1}\log N)\), and total
vertex congestion
\(\operatorname{poly}(\Delta,\sigma^{-1},\log N)\).
Work is
\[
                  (m+N)\operatorname{poly}
                           (\Delta,\sigma^{-1},\log N).
                                                               \tag{14}
\]
No small-leftover parameter \(\beta=1/N\), exponential local
search, or distributed scheduling theorem is needed.
This supplies the matching player for the precomputed
shufflers on already certified virtual expanders.

## 5. The covering matching on an arbitrary host

The hierarchy also needs to enlarge disjoint good sets
\(U_i\) whose union \(T\) has cardinality above \(11N/20\).
Set \(S=V(H)\setminus T\). Use the same one-color iteration
as Section 4, with a requested cut threshold \(\eta\),
but do not assume the host is an expander.

It either saturates all of \(S\), or returns a cut separating
the still-unmatched \(S'\) from the still-unmatched \(T'\).
Orient the latter cut so \(S'\) lies on its designated side.
Since a matching removes the same number of vertices from
each terminal set,
\[
                   |T'|-|S'|=|T|-|S|>N/10.                 \tag{15}
\]
The complementary side contains \(T'\), so its cardinality
is always above \(N/10\). If the designated source side
also has size at least \(N/10\), return the smaller side as
a balanced cut-only answer. Otherwise it is a small cut
containing every uncovered source.

Assign each matched source vertex to the block \(U_i\)
containing its unique matched sink. This gives disjoint
\(U_i^*=U_i\cup U_i'\), an injective covering matching,
\(|U_i'|\leq|U_i|\), and
\[
                       V(H)\setminus\bigcup_iU_i^*
                              \subseteq C_1.                \tag{16}
\]
There is no small unmatched leftover set outside \(C_1\).
The path and work bounds are those of (13)--(14), with
\(\sigma\) replaced by the requested threshold \(\eta\).
This is a stronger sequential interface than the source's
allowed small-leftover alternative.

In particular, when the host itself is a certified expander
and the cutoff is below its true sparsity, the covering
matching saturates every outside vertex. This can simplify
root coverage, although a caller may retain a separately
proved covering wrapper for consistency.

## 6. Precision and preprocessing scope

Packing, distance balls, endpoint lists, and actual cuts use
only original graph IDs, counters, and exact integer comparisons.
The cutoff (9) is rational with an explicitly represented
\(j^2\) denominator. Its bit length is the input cutoff bit
length plus \(O(\log(j+2))\). The depth \(d\) is an integer
ceiling; one may use powers of two for conservative caps.

Exact spectral and moment routines elsewhere in the hierarchy
may have larger polynomial-\((k,\text{word size})\) temporary
integers. Those costs belong to the construction-work factor.
They do not change the geometric bounds proved here and
must not be hidden inside the numerical client's smaller
stored-label word cap.
