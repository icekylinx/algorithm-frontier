# Quantitative deterministic general matching from the 209/210 hierarchy

**Conditional mathematical composition, 24 October 2026.** This note
combines the master-controlled `209/210` raw-cycle hierarchy with the
explicit priced-step, local-projection, persistent-carrier and general
matching phase constructions. It states the required numerical interface
and derives all outer parameter dependence. It also gives one computable
program with unconditional output verification and a classical fallback.
The faster running-time conclusion remains conditional on the named
mathematical components; final verification does not prove that speed.

## 1. Statement and component assumptions

Let an arbitrary undirected graph be given by `n` vertices and `m` edge
records. Deterministically discard loops, coalesce parallel copies while
retaining original edge witnesses, and remove isolated vertices. Let
`m_s` be the number of remaining edges. This shared preprocessing costs
`O(n+m)` in the integer-label word-RAM representation.
If `m_s=0`, return the empty matching immediately; below assume
`m_s>=1` so the subcubic-size parameters are defined.

Subject to the component constructions listed below, there is a single
computable deterministic maximum-matching algorithm with time

$$
\boxed{\quad
 O(n+m)+(m_s+1)\exp\!\left(
 O\left((\log(m_s+2))^{209/210}
          (\log\log(m_s+4))^3\right)\right).
 \quad}                                                     \tag{1}
$$

The hidden constant is absolute. The graph need not be connected,
bipartite, sparse relative to its original vertex count, or of even
order. The output is an exact maximum-cardinality matching.

The component proofs are:

* [The master-controlled 209/210 hierarchy](hierarchy-parameter-balances.md),
  including its parameterized HRG construction and its explicitly named
  sparse-cover, spanner and geometric-lift dependencies.
* [Priced logarithmic steps](priced-logarithmic-steps-from-raw-cycles.md)
  and [the full numerical lifetime interface](numerical-backend-lifetime-and-loops.md).
* [Local exact projection](local-exact-projection-from-priced-steps.md),
  [ledger algebra](ledger-algebra-and-phase-budget.md), and
  [persistent integral carriers](persistent-integral-ledger-carrier.md).
* [The exact degree reduction and optimum-gap driver](general-graph-gap-reduction.md)
  with its factor-critical matching-state construction.
* [The quantitative deterministic exact-flow primitive](quantitative-exact-flow-dependency.md).

Their elementary client inequalities are used below with growing
parameters. A fixed-parameter `O_a` theorem is not treated as a uniform
estimate. The frozen `335/336` construction remains a separate version.

## 2. The numerical hierarchy and the changed port capacity

For the subcubic matching graph, choose one `S=2^s` with `N<=S<2N`.
Use the same `S` in every phase. Invoke every numerical hierarchy with
master logarithmic parameter

$$
U=2s,\qquad S_b=2^U=S^2.
$$

All its recursive instances use this same master. Put

$$
p=41/42,\quad \alpha=209/210,\quad
 t=1/70,\quad \beta=104/105,\quad
 L_U=\lceil\log_2(U+4)\rceil.
$$

The hierarchy parameters are

$$
\begin{split}
 k&=2^{\lceil U^\alpha\rceil},\\
 \Gamma&=2^{\lceil U^p\rceil L_U^2},\\
 \kappa&=\max\{3,\lceil U^t/L_U\rceil\},\\
 C_{\rm port}&=2^{\lceil U^\beta\rceil},\\
 A&=2^{\lceil U^\beta\rceil L_U^2}.
 \end{split}                                                \tag{2}
$$

Integer roots and integer division give an equivalent executable
rounding of these formulas. The port parameter in (2) is used at
**every** recursive level. It replaces the old `167/168` port exponent;
the latter is not retained in a subsidiary geometric expansion.

This replacement preserves the degree requirement. The hierarchy's
degree lemma bounds the relevant tree-cycle degree by

$$
4\kappa(\gamma_{\rm HRG}+1)+2\gamma_{\rm HRG}+3,
 \qquad \gamma_{\rm HRG}=2\Gamma.
$$

Its logarithm is `O(U^(41/42)L_U^2+log U)=o(U^beta)`. Thus the
fixed-capacity binary port trees suffice eventually. Their creation,
retained null fibers and deletion cost contribute fixed powers of
`C_port`, each absorbed by `A`. No port tree needs an asymptotically
larger capacity. Conversely, keeping the old exponent would be invalid
for this balance: since

$$
\frac{167}{168}-\frac{104}{105}=\frac1{280},
$$

the old port logarithm exceeds `log A` by a factor of order
`U^(1/280)/L_U^2`, which tends to infinity.

The balancing identities

$$
p+t=\beta,\qquad 2-\alpha-t=\beta,\qquad
 \beta+1-\alpha=\alpha                                  \tag{3}
$$

control the three different effects. The explicit HRG family has
logarithm `O(U^beta L_U)`. The aspect-dependent routing loss has the
same logarithmic bound when the internal bit length is
`O(U^(211/210))`. Both are below `log A`, with logarithmic slack for
fixed hidden coefficients. Since `log A=o(log k)`, the outer numerical
depth is `O(U^(1/210))`.

The hierarchy proves, using its depth-independent input-lifetime pool
and child-recourse recurrences, the common factor

$$
E(s)=\exp\bigl(O(s^{209/210}(\log(s+4))^2)\bigr).          \tag{4}
$$

Precisely the following full interface is required here:

1. A numerical instance of actual nominal size `M<=S^2` initializes
   in `M E(s)` time. Updates, queries, complete forest logs, inverse
   raw quality, occurrence multiplicity and answer-piece count have
   factor at most `E(s)`. Initialization is not padded to `S`.
2. The raw denominator counts every mapped traversal before
   cancellation. Real loops, true null edges, stable edge provenance,
   dormant signed/absolute counters and old-to-final transactions have
   the full lifetime semantics in the numerical interface note.
3. The root accepts integer data of absolute `O(s)` bit length; fixed
   exponent `S^1200` suffices. Internal `O(s^(211/210))`-bit arithmetic
   is charged as a fixed polynomial in the bit length.
4. The implementation supports polynomial master lifetimes. Local
   cover/spanner instances restart on their own permitted horizons,
   and both initialization and retirement are charged. The backend's
   `S_b^200` master lifespan exceeds the guarded outer requirement.

The hierarchy's master size is larger than the actual root size only
to set numerical parameters. It does not require an `S_b`-sized array
in each local projection. The argument applies to arbitrary adaptive
client sequences meeting the stated deterministic interface.

## 3. Computable matching parameters and nominal sizes

Let

$$
T_s=\lceil\log_2(s+4)\rceil,\qquad
 a=\left\lfloor\frac{\lfloor s^{1/210}\rfloor}{T_s^3}\right\rfloor.
$$

Suspend the fast candidate before division by `a` unless `a>=1000`.
Define

$$
C=a+1,\quad v=\lceil s/a\rceil,\quad B=2^v,\quad
 q=B^{-100},\quad D_*=B^{10},                              \tag{5}
$$

and keep `delta=S^-1000`, `epsilon=S^-3000`, `H=S^100`.
The matching floor parameter `C` in (5) is distinct from the numerical
port capacity `C_port` in (2).

For sufficiently large `s`,

$$
v=\Theta(s^{209/210}(\log s)^3),\qquad
 a^2=o(v),\qquad a=o(v),\qquad v=o(s).                     \tag{6}
$$

The logarithm of (4) is `o(v)`. Therefore `D_*` eventually dominates
the backend factor, occurrence count and inverse quality with any
fixed constant slack. Also

$$
(4D_*)^{-1}>2q.                                          \tag{7}
$$

This is the acceptance margin needed by the raw priced-step client.
One must use this master cap; the local expression `M^(10/a)` is
not substituted into the growing-parameter proof.

Keep periods `b_j=B^(a-j)`, so `S<=b_0<2^aS`. Round
`16(R+B)` to `M=2^u` with `u` divisible by `2a^2`. Then

$$
16(R+B)\le M<16(R+B)2^{2a^2}.                             \tag{8}
$$

Neither `2^a` nor `2^(2a^2)` is treated as constant. Both fit the
allowance in (6).

The top lifetime bound is `R_top=SB`. Actual topology births and
retargetings are `O(aS log S)` and fit it eventually. At a reset
to integral level `j>1`, the parent-debt argument gives

$$
P\le(C+2)b_{j-1}\le(C+2)b_1
   <(a+3)2^a S/B.                                         \tag{9}
$$

The local proof uses `R=8192(P+1)` or an absolute larger constant.
Equation (9) implies `R+B<=S` eventually. Equation (8) therefore
gives `M<=S^2` for both local and top instances, since

$$
\log_2 M_{\rm top}\le s+v+2a^2+O(1)<2s.                  \tag{10}
$$

This proves the size hypothesis used with master `U=2s`. The actual
root prices have `O(s)` bits regardless of local `M`: all capacities,
debts and floors are polynomial in `S`, and derivatives are evaluated
exactly on the common epsilon grid. The fixed backend input-bit
constant can be chosen once, for example `c0=1200` with master `U`.

## 4. Priced steps and exact local projection

The priced-step proof's scalar inequalities depend on `q`, the copy
cap and fixed arithmetic guards, rather than a fixed value of `a`.
With `D_*`, it supplies exact epsilon-grid circulation steps with
objective increase `Omega(q^2)` and complete raw-motion control.
Its query-log/consume transaction prevents refreshes from invalidating
an unconsumed answer.

Let `Q` count requests from the owning matching or projection client,
and let `J<=Q` count accepted steps. Internal anchor refreshes and
their backend repricings are a separate category. They number
`O(D_*J)`, and their complete coordinate sweeps cost `O(D_*^2J)`.
The backend costs, returned-list raw sums including LOW answers,
point reads, retirement transfers and dynamic-tree operations give

$$
T_{\rm price}\le(M+Q)D_*^2\mathrm{poly}(s).
                                                               \tag{11}
$$

Every polynomial here has an absolute degree. Explicit client settings
are charged once; their acknowledgments are not recursively treated
as new numerical-motion reports. No-motion representation changes
cannot create new absolute-motion credit.

A local threshold test has `O(P+1)` represented records and objective
range and insertion/lock loss `O((P+1)s)`, with absolute constants.
Consequently

$$
J_{\rm loc}=O((P+1)B^{200}s),\qquad
 Q_{\rm loc}\le(P+1+D_*J_{\rm loc})\mathrm{poly}(s).
$$

Substitution into (8) and (11) gives numerical work

$$
(P+B)2^{2a^2}B^{230}\mathrm{poly}(s).                \tag{12}
$$

The local graph, optimistic boundary capacities, locked threshold
test, exact union-flow recovery and `O(P)` changed support remain
those of the local exact-projection proof. Its parent is frozen
through all tests and exact recovery.

For the exact static-flow checks, the fixed deterministic algorithm of
van den Brand et al.,
[arXiv:2309.16629v1](https://arxiv.org/abs/2309.16629v1), has the
proof-level rate derived in the quantitative flow note:

$$
Z\exp(O((\log Z)^{17/18}\log\log(Z+4)))
       \mathrm{poly}(\text{input bits}).
$$

Capacity-digit reduction handles `O(s)`-bit capacities on a small
graph without changing the inner flow algorithm. Charge size `Z+B`,
not `S`. The crucial exponent gap is exactly

$$
\frac{209}{210}-\frac{17}{18}=\frac{16}{315}>0.
                                                               \tag{13}
$$

Thus the static factor is at most `B` eventually, including the
polynomial arithmetic and scaling overhead. There are `O(s)`
threshold tests. By (6), (12) and (13), the entire exact local
projection has the conservative bound

$$
T_{\rm proj}\le(P+B)B^{250}.                              \tag{14}
$$

## 5. Phase and driver costs

For target gain `1<=K<=N`, take

$$
L=\lceil10000 C N/K\rceil,\qquad
 g_*=\max\{1,\lfloor K/(100C)\rfloor\}.
$$

If `K>=100C`, then `Lg_*<=101N`; otherwise `g_*=1` and
`L<=10001CN`. Thus `Lg_*=O(aN)` with an absolute constant.
The exact preserving-deletion debt identity pays all peel weight.
Including the terminal gain, expansions, contraction arities and
ticks have total `O(aS)`. Largest-bin physical bookkeeping and
application to the integral levels cost
`a^2S poly(s)`. Sparse persistent projection changes are charged
to their actual support.

The top objective has `O(S)` coordinates, `O(s)` logarithmic width
per coordinate and total structural loss `O(aSs^2)`. Therefore

$$
J_{\rm top}=O(aS B^{200}s^2).
$$

The client performs constantly many local responses per genuine
notification. A bin residual is read as `y=s-p+Cw`, so no moving
high-degree allocation column is summed. Equations (8) and (11)
bound total top numerical work by `SB^240` eventually.

Let `tau=O(aS)` be total ticks. The level-`j>1` reset charge is

$$
\begin{split}
 \sum_{j=2}^{a}\frac{\tau}{b_j}
       [(C+2)b_{j-1}+B]
 &\le\tau[(a-1)(C+2)B+2B]\\
 &=O(a^3SB).
 \end{split}                                                \tag{15}
$$

The parent-debt bound (9) remains true for a large `L`-tick gain:
selecting level `j` means no coarser boundary was crossed. There
is no assumption of unit tick increments. Multiplying (15) by the
common local factor `B^250` pays all local projections. At level
one, at most `tau B/S=O(aB)` global exact exchange flows occur;
their total, including fresh carriers, is at most `SB^3` eventually.

Including initialization, final materialization and a first final
attempt, one phase therefore costs at most

$$
T_{\rm phase}\le SB^{300}.                                \tag{16}
$$

The optimum-gap driver needs `O(a(1+log(N+1)))` phases. With upper
bound `U_gap` on the remaining improvement, it takes
`K=ceil(U_gap/2)`. LOW approximately halves that bound. For
`U_gap>=400C`, success gains at least `U_gap/(400C)` edges; below
that range each success gains at least one. The same `a,S` are
used throughout. Hence

$$
T_{\rm fast}\le SB^{320}
   =S\exp(O(s^{209/210}(\log s)^3)).                        \tag{17}
$$

The no-stall proof uses a comparison matching with `K` additional
edges. It does not require a perfect matching or that the initial
free-vertex count equal `2K`. Thus (16)--(17) apply on arbitrary
general-graph inputs and on phases ending in a valid LOW.

## 6. Uniform finite guards

Use the same fixed guards

$$
S\ge2^{100},\quad 100000C\le S^{1/20},\quad
 B\le S^{1/20},\quad q\ge S^{-1},\quad D_*\le S^2.
$$

They all hold eventually by (6). Retain caps `S^20` on main actions
and threshold iterations and `S^100` on an engine's external requests.
A failed guard suspends and supplies no LOW certificate.

The first-failure argument begins with these loose caps. Top positivity
settings and local pad settings are polynomially many with absolute
exponents. Their total addition or bound violation is below `S^-800`
because each costs only a constant times `delta=S^-1000`. These
preliminary bounds establish the structural debt and local region
proofs before the sharper count is invoked.

Those proofs give integral debt `O(a^2S)`, `L<=10001(a+1)S`, and
the local nominal bound (9), even through a first attempted overflow.
The price calculations thus remain in the absolute polynomial range.
The represented raw list has at most `O(M D_*^2)=S^{2+o(1)}`
traversals, below `S^20`. The existing estimates

$$
V/H\le S^{1044},\qquad
 \mu\ge S^{-1045}/400,\qquad
 \theta\ge S^{-1030}
$$

remain valid and keep both exact dyadic choices above
`epsilon=S^-3000`. Signed bases, live and dormant copy increments,
absolute buckets and lazy offsets have absolute `O(s)`-bit fields
under the `S^220` cumulative-motion bound.

At the loose request cap, internal repricings and complete logs are
still polynomially many in `S`, well inside the hierarchy's master
`S_b^200=S^400` lifespan. Actual backend internal words have
`O(s^(211/210))` bits, whose fixed-polynomial simulation cost is
already included. Finally, all sharp client counts are
`SB^{O(1)}=S^{1+o(1)}`, strictly below the guards eventually.
This rules out a first guard failure in the eventual range without
using successful completion as a premise for earlier error bounds.

The hierarchy's own prerequisite proof remains necessary. Checking
finite degree, size and precision caps is not a finite certificate
of raw-cycle approximation quality.

## 7. A single computable program and exact output on every input

No unknown eventual size cutoff or favorable parameter index is given
to the program. After shared input cleanup, start two private
instruction-level computations:

* the growing-parameter candidate defined above, including its exact
  decoding and final verification;
* one fixed deterministic polynomial-time classical general matching
  algorithm, with its final verification.

Alternate one bounded physical instruction of each unfinished
computation. Integer multiplication, long loops and memory allocation
are decomposed into charged instructions; neither computation may
execute a whole graph routine as one uninterruptible step. They share
only read-only input and original edge-witness data.

Before accepting a proposal, check its edge identities and endpoint
disjointness, then perform one deterministic general-graph
augmenting-path search to exhaustion. Accept exactly when no augmenting
path exists. Berge's criterion proves exact optimality. Gabow's
[2017 primary algorithm, Figures 1--2 and Sections 3 and 5](https://arxiv.org/abs/1703.03998v1)
supplies the one-search interface from an arbitrary current matching.
The conservative `O(m_s alpha(m_s+2)+m_s)` implementation and the
independent 2026 exposition are described in
[classical-matching-optimality-verifier.md](classical-matching-optimality-verifier.md) and
[deterministic-maximum-matching-verifier.md](deterministic-maximum-matching-verifier.md). An invalid proposal or
suspended candidate is retired.

The classical computation ensures termination and a correct answer on
every input, including finite exceptional sizes where a numerical
prerequisite was not established. Each computation receives a fixed
positive share of all instructions. On every sufficiently large
cleaned size, the candidate's conditional proof applies to all graphs
of that size, and its verified answer arrives within a constant
multiple of (17), plus its near-linear verification cost.

For the finitely many exceptional cleaned sizes, the classical
polynomial bound is finite. Enlarging one absolute analysis constant
covers them all; the program need not compute or know that cutoff.
This composition has no `2^a` search-over-parameters penalty.

Choose a physical word-size constant once for the polynomial number
of actual instructions and allocations that can occur before the
fixed classical computation finishes. Longer logical integers and
addresses use charged digit arrays or touched-cell dictionaries.
Thus the interleaving has one finite machine model, not a new unit-cost
word model for each input-dependent parameter.

The exact path-port reduction has `N=4m_s-r=O(m_s)` vertices and
preserves optimum matching size up to a known offset. Its decoder
works for every auxiliary matching; the final check is on the cleaned
original graph. Mapping retained witnesses back costs linear time.
Substituting `S=Theta(m_s+1)` into (17), and adding shared cleanup,
proves (1) subject to the stated eventual-performance components.

The two conclusions must remain separate. The verification and
classical fallback establish output correctness and termination.
The improved bound (1) additionally requires the complete structural,
projection, raw-cycle and lifetime proofs. If one of those components
has a gap, verification would still protect the output but would not
establish the faster time.
