# Public quantitative frontier for explicit strong-Haxell hypergraph matching

**Audit date: 25 October 2026.** This note distinguishes a
published displayed theorem from the stronger bound that this
research round proves for an already public operation sequence.
Only primary mathematical sources support the comparisons below.

## 1. Common normalization

The input is an explicitly listed bipartite hypergraph
`H=(A,B,E)`, with one left vertex and at most `r` right
vertices per edge. Its volume is `p=sum_e |e|`. The promise
under comparison is

\[
          \tau(E_S)\ge\Delta r^2 |S|
          \quad\text{for every }S\subseteq A,
          \qquad\Delta\ge4.
 \tag{1}
\]

Here the hitting set uses right vertices. All times below
include reading the edge list; separately listed unused vertices
cost their input-list length once. A matching covers the entire
left side. It is not required to cover every right vertex.

## 2. Primary sources and their exact scopes

### Annamalai: a near-threshold polynomial-time algorithm

Primary text:
[*Finding Perfect Matchings in Bipartite Hypergraphs*,
arXiv:1509.07007v2](https://arxiv.org/html/1509.07007v2).
The arXiv history lists v1 on 23 September 2015 and v2 on
5 December 2016. The work appeared at SODA 2016 and in
Combinatorica in 2018.

Theorem 1.3 fixes both the uniformity and a positive slack and
then guarantees polynomial time under a strengthened
near-threshold Haxell condition. That source's uniformity `R`
counts the whole hyperedge. For its uniform setting, writing
our right-side rank as `r=R-1` turns its condition into

\[
           \tau(E_S)>(2r-1+\epsilon)(|S|-1).
\]

The implementation analysis in Section 2 explicitly takes
`0<epsilon<1` and sets its parameters for that range. It
remarks that substantially larger slack could permit more
aggressive parameters, but does not state a uniform
`p^(1+O(log log Delta/log Delta))` running time. Thus the
shorthand polynomial dependence on fixed rank and slack must
not be extrapolated by substituting `epsilon=Delta r^2`
into formulas whose algorithm parameters were chosen for
small slack.

Theorem 5.4 already provides a qualitative certifying
alternative: a perfect matching or a subset violating that
near-threshold condition. Therefore a matching-or-violation
outcome is not new in itself. The research notes attach it
to a sharper strong-Haxell time bound and give an explicit
right-resource set that is linearly checkable.

### BHHS: the same rank-squared strong promise

Primary text:
[*Disjoint Paths in Expanders in Deterministic Almost-Linear
Time via Hypergraph Perfect Matching*,
arXiv:2511.02214v1](https://arxiv.org/html/2511.02214v1),
SODA 2026. The current
[arXiv version history](https://arxiv.org/abs/2511.02214)
lists only v1, submitted 4 November 2025.

Theorem 1.5 uses the right-side rank convention of (1), allows
bounded rather than necessarily uniform rank, and displays

\[
         p\exp O\!\left(\frac{\log(p+4)}{
                                      \sqrt{\log\Delta}}\right)
 \tag{2}
\]

under exactly (1). Lemma 3.3 supplies the maximal-half-layer
reduction; Algorithms 1--3 give the actual operations. Sections
5.4--5.5 count signature vectors via partitions to obtain (2).
This is the strongest directly displayed, same-promise
quantitative theorem located in this audit.

The approximate-half-layer result is a different interface.
Lemma 3.5 uses an additional approximation factor and a
stronger promise; the present explicit comparison does not
substitute that theorem for the exact maximal-layer statement.

## 3. Stronger bound derived in this round for the public algorithm

The audit of the actual BHHS operations gives a stronger rate
than (2), without changing those operations:

\[
         p\exp O\!\left(
             \frac{\log(p+4)\log(2+\log\Delta)}{\log\Delta}
                          \right).
 \tag{3}
\]

The complete argument is in
`public_hypergraph_algorithm_weighted_reanalysis.md`, with
independent audits in
`public_haxell_weighted_reanalysis_audit.md` and the companion
flow audit. Its two relevant additions to the displayed source
analysis are:

1. Preserve the physical hitting interpretation of the latest
   actual superposition attempt, rather than requiring a
   hypothetical rerun to retain its old cardinality after the
   outside matching changes. This proves layer growth from
   the historical candidate's saturated vertices and resource
   union.
2. Every layer starts above `Delta W/10` and is capped by
   `Delta W`. An adopted superposition multiplies its size by
   at least `1.1`, so there are at most constantly many reset
   epochs. Within each epoch, child prefix sizes decrease
   geometrically. A contracting weight on the tree of layer
   instances gives (3).

This is a new derivation in this round, not a claim that the
public source already prints (3). However, it is a valid
derived-public baseline when comparing algorithms. The new
no-superposition implementation reaches the same rate and is
useful for its simpler persistent certificates and destructive
path-support interface; it does not have an exclusive speed
advantage over the reanalyzed public explicit algorithm.

The subsequent rank-sensitive refinement also applies to both operation
sequences. A positive-index parent's children can only be born while
their fixed prefixes lie between
`(1+.09 Delta) W` and `(1+r Delta) W`. Their geometric decrease
therefore gives `O(log(r+2))` children per epoch, independently of
`Delta`. Put

\[
 a=\min\{\log(2+\log\Delta),\log(2+\log(r+2))\}.
\]

The precise layer-build bound, including the separate root factor, is

\[
 O\!\left(\min\{\log(|A|+1),1+\log\Delta/a\}\right)
 \exp O\!\left(\frac{a\log(|A|+1)}{\log\Delta}\right).
\]

See `rank_sensitive_layer_count.md` for the finite-prefix proof and
the distinction between this counting bound and implementation lower
examples. For constant rank and `Delta>=p^epsilon`, it gives the
layer time `p log(p+4) exp O(1/epsilon)`, plus input-list reading.
This too is a derived-public reanalysis, not an exclusive speed
separation from the original BHHS operation sequence.

## 4. Concrete regimes, with the same promise throughout

Let `U=log(p+4)`.

| Regime of `Delta` | Published BHHS displayed overhead | Derived-public and no-superposition overhead |
|---|---:|---:|
| `Delta>=p^epsilon`, fixed `0<epsilon<1` | `exp O(sqrt(U/epsilon))` | `(log p)^{O(1/epsilon)}` |
| `Delta>=exp(U^beta)`, fixed `0<beta<1` | `exp O(U^(1-beta/2))` | `exp O(U^(1-beta) log U)` |
| `Delta>=U^c`, fixed `c>0` | `exp O(U/sqrt(log U))` | `exp O(U log log U/log U)` |

The rank `r` is unrestricted apart from the feasibility of
(1); no extra polynomial-rank or constant-rank hypothesis
enters (3). The total running time is the displayed overhead
times `p`, plus the initial vertex-list cost.

All such comparisons must also include an elementary baseline. If
`|A|<=Delta r`, sequential greedy matching takes linear time under
(1): at any failed step the already used resources would be fewer
than the singleton hitting requirement. Without the promise those
resources certify the failed singleton. Checking the all-left
certificate first makes `Delta^2 r^3>=|B_used|` a sufficient
input condition for this linear-time endpoint. In particular
`Delta>=sqrt(p)` is already elementary, so no polylogarithmic
improvement is claimed over elementary matching in that range.
More generally maximal greedy leaves at most
`|A|/(Delta r+1)` uncovered left vertices under (1); resolving
their interaction with the existing matching remains necessary.

Right-side rank one is another elementary boundary. The promise becomes
`|N(S)|>=Delta |S|`. Alternating BFS grows its reached left set by a
factor `Delta` until it finds a free right endpoint; hence every
nonperfect matching has an augmenting path of length
`O(1+log(|A|+1)/log Delta)`. The classical
[Hopcroft--Karp phases](https://doi.org/10.1137/0202019) therefore give
`O(p(1+log(|A|+1)/log Delta))`, plus input-list reading. This beats
the layer bound in that graph case. The rank-sensitive comparison of
interest is rank at least two and outside the preceding greedy endpoint.

## 5. What the freshness check does and does not establish

The search checked the exact titles, the phrases strong Haxell
and near-linear hypergraph perfect matching, current arXiv
version records, and the current publication pages of the
BHHS authors. No later primary statement with the same
explicit-input, left-perfect, rank-squared promise and the
rate in (3) was located. Recent dense-degree threshold or
almost-perfect hypergraph results use different assumptions
or outputs and cannot silently replace this comparison.

The refreshed search also checked
[*Efficient Parallel Algorithms for Hypergraph Matching*,
arXiv:2602.22976](https://arxiv.org/abs/2602.22976).
Its stated target is maximal matching with high-probability parallel
work/depth guarantees. It is not deterministic left-perfect matching
under (1), so it does not supply a replacement rate for this table.

This is a scoped literature audit, not an exhaustive
nonexistence proof for every unpublished or differently
formulated algorithm. The strongest affirmative comparison
is already supplied in Section 3: the existing public
operation sequence admits (3) by the analysis developed in
this round. Accordingly all checkpoint claims should say
that the published quantitative analysis is strengthened,
and should not describe (3) as a separation from all
algorithms already present in public papers.
