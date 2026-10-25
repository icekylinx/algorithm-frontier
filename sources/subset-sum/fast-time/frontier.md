# Local research record: batch joins, coded centers, and total wires

Author: Yilin Liu. Research assistance: OpenAI Codex, including GPT-6 Astra.
Date: 23 October 2026.

These notes belong to local research, not to the paper's account of its
proved results. They curate the new batch-and-code checkpoint without
promoting a local lemma, diagnostic numerical value, or conditional cost
formula into a general running-time theorem. The accepted general bound
remains `149809813343531/301754962128739 < .4964618056`.

## 1. Actual-key batch contraction

**Exact local algorithm; notes 89 and 92.** Deduplicate outside sums while
retaining witnesses, then deduplicate complete prefix labels within an
exact-key bucket. This leaves actual source and opposing sets
`F_z ⊆ U_1 × U_2`, `B_z ⊆ V_1 × V_2`, of sizes `f_z,b_z`.
It does not merge distinct prefix labels merely because their numerical
contributions coincide. Let `p_i,r_i` be the respective core-projection
sizes. The source incidence matrix `A`, and restricted compatibility
matrices `L,R`, give

$$
Z=LAR,
\qquad
Z_{y_1,y_2}=\#\{x\in F_z:C_1(x_1,y_1)C_2(x_2,y_2)=1\}.
$$

Inspect only positions requested by actual records of `B_z`. A positive
requested entry permits one source scan to recover a valid original
witness. Positive unrequested positions do not solve the original call.

Writing `ω=log_2 7` and
`M(a,b,c)=O(abc/min(a,b,c)^(3−ω))`, the paid cost includes

$$
f_z+b_z+p_1r_1+p_2r_2+
\min\left\{
\begin{array}{l}
M(r_1,p_1,p_2)+M(r_1,p_2,r_2),\\
M(p_1,p_2,r_2)+M(r_1,p_1,r_2),\\
f_zr_1+M(r_1,p_2,r_2),\\
f_zr_2+M(r_1,p_1,r_2)
\end{array}\right\},
$$

up to polynomial bit factors. This pays restricted input matrices,
intermediates, outputs and witness recovery. If `f_z=b_z=t` and all four
projection sizes are `O(sqrt(t))`, the cost is `t^(ω/2) poly(n,L)`.
Universal half-compatibility tables can be prepared below exponent `.415n`
in the current reduction; constructing key-dependent restrictions remains
charged.

**Missing general transfer.** Sum the minimum of this cost, direct pairing,
the current incidence cost, and eligible boundary solvers over every
retained key and every cover call. Existing cardinality and copy bounds
permit matching-like medium buckets without projection compression, so
they do not force a strict saving in this sum. Repeated core labels at
different keys do not imply equal restricted problems. A sharper nonlinear
bucket score also needs a paid shift-selection method, or a guarantee for
the buckets chosen by the existing selector.

## 2. Boundary memoization and static-source frontiers

**Exact local algorithms; notes 54, 86, 88.** For observed transition
tables `T_v`, evaluate an internal node once per distinct pair of child
reachable-subset IDs. If `d_v` counts these pairs and there are `p` tree
nodes, a batch of `b` queries on `f` source records costs

$$
[fp+bp+\sum_v d_v|T_v|]\operatorname{poly}(p,L,\log(f+b+1)).
$$

Distinct child pairs can produce the same output mask yet require
different witnesses. Store predecessor selectors by the actual child-ID
pair and leaf restriction class, not solely by the interned output mask.
Static unrestricted subtrees may be processed once; their joins to active
subtrees remain charged.

A positive source index pays `P=f D_L poly(n,L)` once and
`Q=D_R poly(n,L)` per query. On a paid source-partition tree, a safe
frontier recurrence is

$$
W_v(b)=\min\{\min_a(P_{v,a}+bQ_{v,a}),\sum_w W_w(b)\}.
$$

Without a separately proved router, the same `b` is charged at every
child. Eligibility tests, cost estimation, all source copies and query
copies must be paid before claiming the frontier's cost.

**Scoped obstruction; note 90.** There are near-injective unrestricted
binary dictionaries and entire weight-`.45N` fibers of size at least
`2^(.06N)` whose every balanced physical cut has at least `|F|/2^40`
observed numerical states. The obstruction persists for the stated
full observed-table ledger under source partitions, fixed-coordinate
deletion and separate trees. It does not exclude memoization, query
routing, implicit states, unrestricted-subtree caching or other leaf
solvers. It is not a general time lower bound.

## 3. Actual fibers do not force projection sharing

**Local realizability and an explicit escape; note 94.** The construction
has three individually injective `M`-item dictionaries and an allowed
mixed raw call with complete bucket sizes between `2^(.181M)` and
`2^(.181M+1)`. Every core projection has multiplicity at most `2^20`.
Thus blockwise injectivity does not itself force the projection
compression used by the favorable `LAR` case.

This does not prove that the adaptive selector chooses the constructed
call or that such calls carry the worst-case aggregate mass. Private
radix digits expose disjoint triples from which a solution must select
one or two items. Their three local choices admit a polynomially
recognized meet-in-the-middle escape of cost
`O*(3^ceil(M/2))`, below `O*(2^(.264161n))` for `n=3M`.
Original scalar target testing enforces the remaining checks. The needed
general alternative may therefore be “sharing or a paid original-input
solver,” rather than sharing alone.

The separate private-query construction makes every source row necessary
when preserving **each individual query answer**. It does not make every
row necessary when deciding only the OR of one known batch: one found
compatible pair suffices. This distinction must survive future routing
or representative-set arguments.

## 4. Positive thin joins and signed exactness

**Local Boolean result; notes 48, 56, 81–86.** At the specified thin
containment types, a deterministic positive cover gives per-endpoint
incidence cap `2^(.0558N)` and a keyed decision-and-witness join. The
cover's multiplicity need not equal one. Substituting its support directly
into an exact signed arithmetic identity invalidates cancellation.
The examined inclusion–exclusion closure of the independent cover
has expensive second-order terms; its obstruction is specific to that
cover distribution and its charged closure, not to all positive covers.

The alternative is to reach actual positive decision nodes with a valid
original witness lift. Common-pin and exact-negative-mask realizations
pay `(h f+r b) poly(n,L)` for their filtering and copies; the local thin
types require substantial common-one structure. No universal paid
aggregate decomposition is established. Determinant and affine-boundary
solvers remain conditional alternatives; low dictionary deficiency alone
does not bound their determinants or boundary tables. The supplied
large-determinant examples can themselves split into easier components,
so they do not exclude all recursive decompositions.

## 5. Exact coded centers and their residual

**Exact identity; note 93.** For `Q⊆R`, let `D=R\Q`, `d=|D|`, and let
`B` be a full-row-rank binary matrix with `c` rows. Retain middle subsets
with zero syndrome. Over `F_2`,

$$
2^{c-d}\#\{S:Q\subseteq S\subseteq R,\ B1_S=0\}
=2^{c-\operatorname{rank}(B_D)}
 1[B1_Q\in\operatorname{im}(B_D)].
$$

The expression equals one at full rank. Its exact correction is supported
precisely on compatible pairs with rank-deficient slack. Shared residual
factorization is therefore the relevant target; separately emitting every
dual character is not required by the identity.

The supplied query-star repair gives the local profile

$$
\max\{M(\tau)-\gamma,
       \tau[H(T,A)+\gamma-(T-A)]\},
\quad
M(\tau)=\max_{A\le x\le T}
[\tau H(T,x)+(1-\tau)H(1-A,x-A)],
$$

with `γ=c/N`, before its explicitly allocated compilation allowance.
The reported `.06041124417` evaluation at the active inner state exceeds
the previous `.06013010463` benchmark. Neither number is a new certified
outer profile. Multi-width and finite-difference identities are exact,
but still need a favorable complete incidence bound. The examined dense
vector channels, Fourier-band/star-repair cost comparison, and
larger-alphabet construction do not close the stated gap; their failures
do not prohibit all asymmetric codes or residual circuits.

**Scoped modular obstruction; note 91.** For scalar normalization on one
fixed middle width, under `q≤k≤r` and `q+k≥r`, omitting any center while
computing containment modulo `m` forces `m | lcm(1,…,r−q)`.
This limits precision in that architecture, not in all modular or
vector-valued circuits.

## 6. Endpoint-weighted shifts and the completed compiler interface

**Paid selector; note 95.** Let cheaply computable endpoint-local work
weights have prefix totals `W_U,W_V`. For `R` local residue choices modulo
`q`, exact weighted residue histograms select a common shift with retained
work at most

$$
(R/q)(|O_U|W_U+|O_V|W_V).
$$

All prefix weight computations, residue convolutions and outside scans
remain paid. Fixed-template degrees can be computed as sums of products
of stored local degrees; cache nonempty description pointers so retained
copies do not repeat expensive rejection scans. This applies to local
endpoint weights, not to an unevaluated nonlinear exact-key-bucket cost.

Raw total-wire expectations may retain negative *normalized mean-degree*
rates for rare colors. This is legitimate arithmetic averaging, not a
negative incidence count or an uncharged endpoint scan. Full-path
expectations followed by Markov bounds can coexist with all required
cover events at a fixed finite seed.

**Compiler gap closed under explicit hypotheses; note 97.** For a typed
exact seed whose automorphisms are transitive separately on both endpoint
domains, write `a_c=W_L,c/|R_N|`, `b_c=W_R,c/|Q_N|` and
`V_N(τ)=Σ_c a_c^τ b_c^(1−τ)`. Dead colors are removed. Color potentials
and Jensen's inequality bound mean logarithmic degree polynomials by
`log_2 V_N(τ)`. Tensor concentration gives good endpoint sets; finitely
many coordinate-permuted copies cover every endpoint pair. The signed
first-good-copy identity restores exact matrix values while retaining
good-set degree bounds. Separate endpoint transitivity suffices; pair
transitivity is unnecessary.

The repaired tensor object is a circuit for `T_N^(⊗b)`, not for the full
typed matrix `T_Nb`. First choose a sufficiently large original admissible
seed `N=k²+500k`, then a fixed amplification depth, then apply grouping
and padding. Arbitrarily small total allowance requires arbitrarily large
seeds with a common asymptotic profile bound. Tensoring one fixed small
seed cannot erase its original grouping/padding loss.

**Status correction:** note 97 supersedes the older statements in notes
07, 87 and 95 that leave this compiler conversion open. The remaining
problem is a strictly better complete total-wire profile over all
required contacts and branches, followed by the complete outer ledger.
Removing zero floors from old formulas is not such a proof; the saved
binding state already has a positive raw left-degree rate.

## 7. Next proof interfaces, without starting another campaign

A new general theorem needs at least one complete route:

1. An actual-key aggregate theorem: all retained calls have enough paid
   projection sharing/reuse, or the complementary cases have a faster
   original-input solver, with a computable selector and witness costs.
2. A better exact coded residual: full incidence bounds for the shared
   rank-defect correction, then certified whole-domain outer contacts.
3. A better total-wire family: explicit exact seeds at sufficiently large
   admissible sizes, strict improvement of the complete colored profile,
   application of note 97 with its grouping quantifiers, and the full
   general reduction's cost balance.

External partial-match/OV alternatives mentioned by the checkpoint were
not independently re-audited in this quick review. Their cited
upper-bound comparisons are not lower bounds on those algorithms.
No route above is presently complete enough to change the accepted
exponent, and no unsuccessful route should be added to the paper merely
to document this research history.
