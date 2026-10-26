# Quantitative deterministic general matching with preserved length aspect

**Conditional mathematical construction, 24 October 2026.** This note
composes the length-preserving numerical hierarchy with the exact
general-matching phase. It gives a new quantitative candidate while
leaving the `209/210` and `335/336` constructions unchanged. Output
verification and an exact fallback ensure correctness on every input;
the improved time additionally requires the component proofs below.

## 1. The conditional general-graph bound

Read an arbitrary undirected graph with `n` vertices and `m` listed
edges. Remove loops, merge parallel copies while retaining original
edge witnesses, and remove isolated vertices in deterministic
`O(n+m)` time under the integer-label word-RAM input convention.
Let `m_s` be the number of remaining distinct nonloop edges. If it
is zero, return the empty matching.

Subject to the stated numerical and structural constructions, a single
computable deterministic algorithm returns an exact maximum-cardinality
matching in time

$$
\boxed{\quad
 O(n+m)+(m_s+1)\exp\!\left(
 O\left((\log(m_s+2))^{167/168}
          (\log\log(m_s+4))^2\right)\right).
 \quad}                                                     \tag{1}
$$

The implied constant is absolute. There is no bipartiteness,
connectedness, density, parity or perfect-matching promise.

The required mathematical components are:

* [Preservation of the master length aspect](local-length-aspect-preservation.md),
  including its immediate-null quotient and cheap stored HRG metric.
* [The local metric-growth lemma](local-metric-growth-without-root-pools.md),
  which proves the length recurrence without presuming a root forest.
* The explicit geometric, alias, path-pool, sparse-cover and spanner
  constructions referenced in those notes, with their complete
  [numerical lifetime contract](numerical-backend-lifetime-and-loops.md).
* [Priced logarithmic steps](priced-logarithmic-steps-from-raw-cycles.md),
  [local exact projection](local-exact-projection-from-priced-steps.md),
  [ledger algebra](ledger-algebra-and-phase-budget.md), and
  [persistent integral carriers](persistent-integral-ledger-carrier.md).
* [The exact degree reduction and general optimum-gap driver](general-graph-gap-reduction.md),
  together with its factor-critical matching-state proof.
* [The quantitative deterministic exact-flow primitive](quantitative-exact-flow-dependency.md).

The [209/210 composition](quantitative-matching-209-210-composition.md)
provides a full outer template. The following argument verifies each
changed parameter and reproduces its necessary quantitative counts;
it does not substitute into a fixed-parameter little-oh statement.

## 2. The metric variant used by this hierarchy

For the subcubic matching graph, choose `S=2^s` with `N<=S<2N` and
keep it fixed through all phases. The numerical backend uses master

$$
U=2s,\qquad S_b=2^U=S^2.           \tag{2}
$$

At one recursive general-cycle input, an SNC export is a flat forest
over that **immediate** input. Contract only forest edges explicitly
classified as true null in this map. Retain every genuine input-edge
occurrence, its orientation and its edge lifetime. A genuine edge
with zero gradient, a genuine loop, or an edge null only under an
earlier root projection is not eligible for this contraction.

Each true-null component lies over one input vertex and has at most
the declared occurrence bound. Contracting it preserves the forest
and the images of its marked vertices. The local quotient wrapper
reconstructs affected fibers with a fixed polynomial in the local
occurrence bound, emitting complete replacement lifetimes and
deletion-first callbacks. These explicit logs are part of the
assumed maintained construction.

Give every surviving real cover edge its original current integer
input length. This is at most the scaled rounded metric used by the
private cover, so marked-tree diameter does not increase. True-null
edges have been contracted. There is consequently no tiny positive
exported null length and no need to multiply the entire HRG by `m^4`
to clear denominators. The private cover itself retains its polynomial
integer metric and finite heavy-backbone wrapper unchanged.

In the stored HRG, linking edges have length one and paired edges
have length two, both with gradient zero. Their immediate physical
projections are null. Original graph edges and real cover edges
retain their input lengths and gradients. The routing and monotone
decomposition proof uses a separate analytical metric with linking
lengths `gamma_HRG D_i` and paired lengths `2 gamma_HRG D_i`.
It produces a fundamental cycle in the same maintained family.
Replacing those analytical auxiliary lengths by smaller stored
lengths does not worsen that cycle's ratio. Its numerator is
unchanged and its physical raw traversal remains bounded by its
stored denominator.

This is the metric variant proved in the length-preservation note.
It is not a direct invocation of a source theorem after silently
changing that theorem's prescribed edge lengths.

## 3. New port capacity, small common scale, and length recurrence

Set

$$
p=41/42,\quad \alpha=167/168,\quad
 t=1/84,\quad \beta=83/84,\quad
 L_U=\lceil\log_2(U+4)\rceil.
$$

At every recursive level use the same master parameters

$$
\begin{split}
 k&=2^{\lceil U^\alpha L_U\rceil},\\
 \Gamma&=2^{\lceil U^p\rceil L_U^2},\\
 \kappa&=\max\{3,\lceil U^t/L_U\rceil\},\\
 C_{\rm port}&=2^{\lceil U^\beta\rceil},\\
 A&=2^{\lceil U^\beta\rceil L_U^2}.
 \end{split}                                                \tag{3}
$$

Finite integer-root and division routines compute equivalent rounded
parameters. The geometric graph degree is bounded by a fixed
polynomial in `kappa,Gamma`; more precisely the existing degree
lemma gives at most
`4 kappa(gamma_HRG+1)+2 gamma_HRG+3` with `gamma_HRG=2Gamma`.
Its logarithm is `O(U^(41/42)L_U^2)=o(U^(83/84))`, so the port
capacity in (3) suffices eventually. Fixed powers of that capacity
fit the local envelope `A`.

The old port exponents `104/105` and `167/168` are not retained in
any subsidiary expansion. Likewise the old common multiplier
`M^10` or `S_b^10` is not used. Instead, with

$$
h=\lceil\log_2 C_{\rm port}\rceil,\qquad
 H_{\rm port}=2^{\lceil\log_2(4(h+1))\rceil},              \tag{4}
$$

we have `4(h+1)<=H_port<8(h+1)`. Multiply both length and gradient
of each nonfiber geometric edge by `H_port`, and give every binary
fiber connector length one and gradient zero. At a geometric vertex,
a passage between two ports uses at most `2h` connectors. Since
geometric lengths are at least one, the port lift increases a
circulation's length by at most another copy of its scaled original
length. Its quality loss is at most two. On lifting back, divide
both numerator and certified denominator by `H_port`.

Every compressed Steiner edge has no permanent portal in its interior.
Its initial-tree interior therefore lies in one `O(k)`-vertex-volume
piece. Edited initial edges and newly inserted tree edges are direct
between promoted terminals. A geometric tree edge consequently sums
at most `c_K k` parent edges for an absolute `c_K`. Central edges
retain their original off-tree length, not an old spanner-alias price.
If `L_i` is the largest input length at outer numerical level `i`,

$$
L_{i+1}\le c_K k H_{\rm port}\max\{L_i,2\}.              \tag{5}
$$

With root lengths of `O(U)` bits and depth `O(U/log k)`, (5) gives

$$
B_{\rm len}=O(U),\qquad
 B_{\rm grad}=O(U\cdot\mathrm{depth})=O(U^{169/168}).       \tag{6}
$$

For the first bound, sum `log k+O(log U)` per level. For the second,
retain the existing frozen gauges: a potential or path sum adds only
`O(U)` gradient bits per level. New tree edges keep their actual
frozen-gauge residual. Gradient magnitudes are not inserted as metric
lengths. Covers, routing radii and the spanner aspect use `B_len`;
exact gradient arithmetic has a fixed polynomial cost in `B_grad`.

This proof does not assume that deep input edges already have root
canonical pool paths. A computable depth guard may be imposed first;
(5) holds throughout the guarded prefix, and the size reduction below
then proves that the guard is not reached eventually.

For example use `d_guard=ceil(8U/log_2 k)+10`, declared allowed
length bits `b_star=(c0+100)U`, and gradient bits
`(c0+100 d_guard)U`. Fix each local instance's analytical radii
from `b_star`, rather than its currently observed maximum length.
The bound `log(c_K k H_port)<=2 log k` eventually proves the
declared length allowance throughout the guarded prefix. An allowed
edge insertion therefore does not cause an uncharged global change
of all cover radii or analytical labels. A period/size restart can
choose its new local scale data with the already charged restart.

## 4. The common numerical interface

The parameter identities are

$$
p+t=\beta,\qquad 1-t=\beta,\qquad
 \beta+1-\alpha=\alpha.                                  \tag{7}
$$

The HRG tree-family logarithm is `O(kappa log Gamma)=O(U^beta L_U)`.
By (6), the aspect-dependent routing logarithm is
`O(U/kappa)=O(U^beta L_U)`. Both fit the computable
`log A=Theta(U^beta L_U^2)` with slack for fixed coefficients.
The immediate-null quotient costs only another fixed local power
of `Gamma`.

The extra `L_U` in `log k` balances the base and recursive work.
The established geometric/pool recurrences have total child nominal
size at most `m A/k` and total child input recourse `A` per parent
edit in the amortized prefix sense. A child forest occurrence log
only changes attachments to already allocated input-lifetime path
pools; it does not incur an extra `k` factor. Since `log A=o(log k)`,
size shrinks geometrically and depth is `O(U^(1/168)/L_U)`.
Both `log(k^10)` and `depth log A` are `O(U^(167/168)L_U)`,
using the last identity in (7). The same absolute recurrences
therefore give common factor

$$
E(s)=\exp\bigl(O(s^{167/168}\log(s+4))\bigr).              \tag{8}
$$

The imported interface is the full raw one: actual nominal size `M`
initializes in `M E(s)` time, while edit/query work, complete logs,
inverse raw quality, occurrences and returned unit-piece count have
factor `E(s)`. It includes dormant signed and absolute counters,
stable edge provenance, real-loop/null distinctions, and complete
old-to-final transactions. It supports polynomial master lifetimes
through charged local restarts. No local instance initializes an
`S`-sized structure merely because it uses master `U=2s`.

Root lengths and gradients have an absolute `O(s)`-bit bound, within
a fixed range such as `S^1200`. Equations (2) and (6) supply the
required backend precision. Internal arithmetic is performed on
charged digit arrays; fixed polynomials in `s^(169/168)` are absorbed
by (8). Final original-input numerators are exact integers; a raw
certificate can be rounded upward to an `O(s)`-bit denominator with
at most a factor-two quality loss.

## 5. Outer parameters and exact local cost

Compute

$$
T_s=\lceil\log_2(s+4)\rceil,\qquad
 a=\left\lfloor\frac{\lfloor s^{1/168}\rfloor}{T_s^2}\right\rfloor.
$$

Suspend the fast branch unless `a>=1000`. Let

$$
C=a+1,\quad v=\lceil s/a\rceil,\quad B=2^v,\quad
 q=B^{-100},\quad D_*=B^{10},                              \tag{9}
$$

and retain `delta=S^-1000`, `epsilon=S^-3000`, `H_price=S^100`.
The matching floor `C`, numerical port capacity `C_port`, port scale
`H_port`, and price scale `H_price` are distinct quantities.

Now

$$
v=\Theta(s^{167/168}(\log s)^2),\quad
 a^2=o(v),\quad v=o(s),\quad \log E(s)=o(v).                \tag{10}
$$

The computable master cap `D_*` thus dominates all required backend
factors with fixed slack, and `(4D_*)^-1>2q` supplies the strong-
direction acceptance margin. The insufficient local cap `M^(10/a)`
is not used.

The periods `b_j=B^(a-j)` satisfy `S<=b_0<2^aS`. Rounding
`16(R+B)` to exponent divisible by `2a^2` costs a factor less than
`2^(2a^2)`. Top lifetime `R_top=SB` contains its actual
`O(aS log S)` births and retargetings. At a local reset `j>1`,

$$
P\le(C+2)b_{j-1}<(a+3)2^aS/B.
$$

Therefore local `R=8192(P+1)` fits `R+B<=S` eventually, and both
top and local rounded sizes have `M<=S^2`. This meets the backend
root-size contract with master `U=2s`. All factors `2^a`,
`2^(2a^2)` and fixed polynomials in `a,s` are absorbed by (10).

For `Q` externally requested engine operations and `J` accepted
steps, internal refreshes number `O(D_*J)`. Their complete sweeps
cost `O(D_*^2J)`. The exact priced-client categories give

$$
T_{\rm price}\le(M+Q)D_*^2\operatorname{poly}(s).           \tag{11}
$$

Here `Q` excludes internal refresh/repricing transactions. Responses
to genuine numerical-motion notifications are external requests;
acknowledgments of explicit client settings are handled once and
do not recursively become new reports. This separation avoids a
circular operation bound.

A local threshold test has `O(P+1)` records, objective range and
structural loss `O((P+1)s)`, and `Omega(q^2)` progress per step.
Thus `J_loc=O((P+1)B^200 s)` and
`Q_loc<=(P+1+D_*J_loc)poly(s)`. Equation (11) gives
`(P+B)2^(2a^2)B^230 poly(s)` numerical work.

For its exact static-flow checks, the fixed deterministic primitive
has factor `exp(O(s^(17/18)log s))` after the capacity-digit reduction.
The exact gap is

$$
\frac{167}{168}-\frac{17}{18}=\frac{25}{504}>0.             \tag{12}
$$

This factor and its bit costs are at most `B` eventually. Small
graphs are charged their size plus `B`, not `S`. Including `O(s)`
threshold tests and exact union-flow recovery, a full projection
costs at most

$$
T_{\rm proj}\le(P+B)B^{250}.      \tag{13}
$$

Its exact changed support is still `O(P)`. The frozen parent,
optimistic boundary, permanent locks and complete residual peel
arguments are unaffected by the new backend metric.

## 6. Phase and complete candidate time

For any target gain `1<=K<=N`, take
`L=ceil(10000 C N/K)` and `g_*=max(1,floor(K/(100C)))`.
The explicit inequality `Lg_*<=10001 C N` gives tick count
`tau=O(aS)`, total physical structural volume `O(aS)`, and
`a^2 S poly(s)` work for bookkeeping across the integral levels.
The top objective loses at most `O(aSs^2)` to structural changes,
so it has `O(aS B^200 s^2)` accepted numerical steps. Full refresh
response and sweep costs in (11) place the top client within
`SB^240` eventually.

For local resets, including large gain jumps,

$$
\sum_{j=2}^{a}\frac{\tau}{b_j}
       [(C+2)b_{j-1}+B]
 \le\tau[(a-1)(C+2)B+2B]=O(a^3SB).                        \tag{14}
$$

This is an additive sum, not a product down the hierarchy. Sparse
projection support and persistent carrier normalization are paid
by that sum and (13). At level one there are at most `O(aB)`
global exact exchange flows, with total cost at most `SB^3`
eventually. Initialization and final materialization fit the same
budgets. Hence one phase costs at most `SB^300`.

The general optimum-gap driver takes `O(a(1+log(N+1)))` phases:
LOW halves its remaining-improvement upper bound, while a successful
phase gains a `Theta(1/a)` fraction above the small integer range.
The smaller range takes `O(a)` further successful gains. It uses
the same `S,a` throughout. Consequently

$$
T_{\rm candidate}\le SB^{320}
   =S\exp(O(s^{167/168}(\log s)^2)).                        \tag{15}
$$

This phase proof uses comparison matchings and does not assume that
the starting deficiency equals its target `K`. It applies on arbitrary
general graphs, including no-instances for that target.

## 7. Finite guards and the common machine model

Keep the explicit checks `a>=1000`, `S>=2^100`,
`100000C<=S^(1/20)`, `B<=S^(1/20)`, `q>=S^-1`, and
`D_*<=S^2`. They hold eventually by (10). A failed check suspends;
it is never interpreted as LOW.

The first-failure proof initially uses only the loose caps `S^20`
on main actions/threshold iterations and `S^100` on engine external
operations. They imply total positivity debt and local padding
violation below `S^-800`, because each setting is only a constant
times `S^-1000`. The local `O(P)` region argument and structural
debt bounds then apply before their first attempted overflow.

Root numerical quantities retain their absolute polynomial envelopes:
integral debts are `O(a^2S)`, `L<=10001(a+1)S`, and logarithmic
arguments lie on the `S^-3000` grid. A raw list has at most
`O(M D_*^2)=S^{2+o(1)}` traversals. The existing bounds
`V/H_price<=S^1044`, `mu>=S^-1045/400` and
`theta>=S^-1030` keep every exact dyadic choice above the grid.
The `S^220` cumulative-motion estimate gives absolute `O(s)`-bit
signed bases, live and dormant counters and buckets.

Backend lengths have `O(s)` bits and its possibly longer gauged
gradients have `O(s^(169/168))` bits. Both are handled by the
charged arithmetic model. Polynomially many internal repricings
and complete logs fit the backend's master `S_b^200=S^400`
lifespan. The sharp counts are `SB^O(1)=S^{1+o(1)}` and
eventually fall strictly below the loose caps. This establishes
the eventual guards without assuming successful completion.

The backend's own guarded null quotient, degree/size checks and
uniform primitive hypotheses are still necessary. Finite mechanical
checks do not establish raw-cycle approximation quality on an
exceptional size.

## 8. One computable program with exact output

After shared cleanup, execute two private instruction-level
coroutines with a fixed one-to-one share of elementary physical
instructions. The first is the candidate defined above; the second
is one fixed deterministic polynomial-time classical general matching
algorithm. Include decoding and final verification in each one's
instruction allowance. Long arithmetic, allocation and graph routines
are charged incrementally; neither coroutine can block the other by
treating an entire routine as one step.

Check a proposal's edge IDs and disjoint endpoints. For a valid
matching, perform one exact deterministic augmenting-path search
to exhaustion and accept only if none exists. Berge's criterion
then proves optimality. The required one-search implementation and its
near-linear cost are supplied by
[classical matching verification](classical-matching-optimality-verifier.md),
using [Gabow, arXiv:1703.03998, Sections 3 and 5](https://arxiv.org/abs/1703.03998).
The independent 2026 exposition is retained in
[the alternate verifier note](deterministic-maximum-matching-verifier.md).
A failed proposal or suspended candidate is retired. Shared input
and original witness data remain read-only.

The classical coroutine ensures termination and exact output on
every input. For every sufficiently large cleaned size, the
candidate's conditional proof applies uniformly over the graphs
of that size, so a constant multiple of (15), plus its verification
cost, suffices. Finite exceptional cleaned sizes are covered by
enlarging one absolute analysis constant using the classical
polynomial bound. The program does not know or encode the
eventual cutoff. It computes only the explicit parameters in
(2)--(4) and (9); it does not search for a favorable parameter
branch or pay an exponential portfolio weight.

Choose one physical word-size constant for the polynomial number
of actual instructions and allocations possible before the fixed
classical computation completes. Larger logical integers use
charged digit arrays and logical memory is allocated only when
touched. Thus the construction has one finite machine model even
on an exceptional size with unfavorable numerical parameters.

The exact path-port reduction has `N=4m_s-r=O(m_s)` vertices,
a known optimum offset, and a decoder valid for every auxiliary
matching. Verify the decoded matching on the cleaned original
graph and map its retained witnesses back once. Substitution
`S=Theta(m_s+1)` in (15), together with shared `O(n+m)` cleanup,
gives (1) subject to the candidate's eventual-performance proofs.

The distinction is essential: exact verification and the classical
fallback prove output correctness and termination. The improved
running time additionally depends on the complete immediate-null,
cheap-metric, geometric-lift, raw-cycle, projection and structural
arguments. A failure of one of those components would leave the
output protected but would not establish the faster time.
