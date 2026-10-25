# Part II: general bound and structural continuation

Author: Yilin Liu. Assistance: OpenAI Codex, including GPT-6 Astra.

## Current general theorem

The new general research chain gives deterministic integer Subset Sum
with

$$
T=\operatorname{poly}(n,L)2^{n/2},\qquad
S=\operatorname{poly}(n,L)2^{E_Sn}.
$$

The exact exponent is $E_S=18261635770550353/10^{17}=.18261635770550353$. The received $137/750$ bound is also implied. The argument covers arbitrary
signed binary weights, repeated and zero values, exact YES/NO decisions,
and indexed witnesses. Its ownership, biased-top, scalar and preparation
proofs are curated in [structural/](structural/THEOREM.md).
Review status is recorded in [CURRENT_REVIEW.md](CURRENT_REVIEW.md).

The [manuscript](../../proof.md) now integrates the same exact bound
and complete proof. Part I's theorem and research record are unchanged.
Later structural branches and failed routes remain research records.

The later structural branches below have additional premises. They
do not strengthen the general theorem by themselves; the tighter exponent
above comes from the complete capacity audit. The branches supply the
following algorithms, certificates, and limits of proposed arguments.

## Proved structural branches and paid certificates

| Result | Guarantee and scope |
|---|---|
| Two individual normalized ranges | If two m-blocks have ranges $W_A,W_B=O^*(2^m)$, unrelated integer scales are allowed and the third block is arbitrary. Time remains $O^*(2^{3m/2})$, with $O^*(2^{m/2})$ state. |
| Affine and signature triggers | Short support-four relations, cardinality-balanced relations, and bounded annihilator signatures give detectable range certificates under their stated rank conditions. |
| Full ternary-relation span | A block's actual Boolean-collision relation span is computed in $O^*(3^{m/2})$ time and $O^*(3^{m/4})$ state. Exact linear algebra then gives support-product components and pivot-core certificates. |
| Paid core optimization | All coordinate cores can be inspected within $(1+\sqrt3)^m<2^{3m/2}$ time. Selected relation and actual-complement certificates are optimized exactly; successful certificates still require an existence theorem. |
| Positive uniform-slice coupling | A largest-fiber coupling proves a slice Renyi bound. The aggregate cross-layer low-noise inequality remains a separate question. |
| Measured owner and energy certificates | Exact relation data can certify quota-image density for a particular input and permit a fixed owner. Their predicates are explicit; they are not universal deficiency estimates. |

See [STRUCTURAL_BRANCHES.md](STRUCTURAL_BRANCHES.md) for the algorithms
and their measured premises. A common-scale clustered-support branch
remains useful when supports have gaps and a small interval cover;
it is not discarded merely because the individual-range branch has
arbitrary scales.

For the range branch, with $N=2^m$, the general cost is

$$
C^2\ge\max\{N,W_A+1,W_B+1\},
\qquad T=O^*(NC+C^3),\qquad S=O^*(C+2^{m/2}).
$$

Thus the detectable range case has space exponent $1/6$ when
$n=3m+O(1)$. It is distinct from the arbitrary-input $137/750$ theorem.
Supplied signature matrices may have many directions if the actual
attained-value counts are paid: the refined time bound is
$O^*(K_AK_BN\sqrt W)$ with $O^*(\sqrt N)$ state.
The product $K_AK_B\sqrt W$ must fit the available time allowance.

## The remaining general existence interface

For every $t\le m/6$, actual complement deficiency can already be
optimized over all t-coordinate complements in time

$$
O^*\!\left(2^{[h(1/6)+5/6]m}\right)<O^*(2^{3m/2}),
\qquad S=O^*(2^{m/2}).
$$

The unproved low-density target is that a block with
$d(B)\le m/100$ has a complement of size $m/6$ satisfying

$$
d(B\setminus T)-d(T)\le\frac23d(B)+O(\log m).
$$

The search cost is settled; uniform existence is not. A fixed positive
linear error changes the exponent, and an unspecified $o(m)$ error
does not automatically become an $O^*$ factor.

Support-product factorization reduces part of the problem. For true
independent factors $B_i$, a prescribed-size split satisfies

$$
d(B\setminus T)-d(T)
\le(1-2t/m)d(B)+\max_i d(B_i).
$$

Hence fixed small independent gadgets do not force a linear gap.
The residual case concerns larger support-indecomposable factors and
their measured relation structure. No theorem yet forces either a
useful joint split or two short-range blocks for every input.

## Exact limits of proposed proof routes

- A fixed canonical transversal can have inadequate projection loss
  even when actual restricted sumsets behave better. This limits that
  transversal argument, not the joint-deficiency theorem.
- Low deficiency and high relation rank do not force bounded integer
  annihilator signatures. A separate vanishing-deficiency family also
  excludes a near-full injective core as a universal substitute.
- The global low-noise target $N(w)Z_w(1/4)\le2^m$ remains open.
  Actual integer counterexamples refute stronger per-fiber,
  normalized-overlap and append-step assertions. They do not refute
  this aggregate target.
- Scalar slice constraints, monotonicities and the positive Renyi
  coupling alone do not imply the target: a formal graded partition
  violates it while failing additive relation closure. This is a
  non-additive obstruction, not an integer counterexample.
- Coordinate-stretch and thinning results are proved conditional
  transfers. Their initial universal low-noise premise remains explicit.
- Expanding compatibility gates into outer generation batches conserves
  the corresponding raw-work and restart cost in the stated interface.
  A shared internal generation method would require a new paid theorem.

Earlier scoped limits remain relevant: the support-only trace gain .08
fails on the stated [.44,.46] by .03 rectangle; abstract one-step cube
edges do not settle multistep integer extraction; and global image
density does not survive arbitrary separator conditioning.

The old ordinary-top separator comparison also has a precise scope.
An unbiased half-size separator has sided degree exponents
$1-H_L,1-H_R$; balancing actual parent domains leaves a
$\pm(H_R-H_L)a/2$ incidence term. The current manuscript proves the biased checker's all-layer
incidence calculation and uses exact actual-product balance.

These counterexamples and conservation identities concern their
specified models. They are not optimality statements for Subset Sum
or lower bounds against all algorithms.

## Curation and provenance

The received packet contains 163 Markdown files: 88 foundation files,
38 post-v1 files, 36 structural-continuation files, and one root guide.
All 88 foundation files are byte-identical to the previous received
v1 source. Their full originals stay in the verified external archive;
the active research text links to the complete manuscript instead of
duplicating that foundation.

The same archive preserves all conditional notes and counterexamples.
The active repository keeps concise mathematical contracts, a dependency
map, source hashes, and separately scoped finite checks. Historical
tradeoffs, source licenses, and original baseline bytes are preserved.

## Tight capacity and simplification tradeoff

The actual dictionary exponent is .54784907311651059 in m-block
units. The core policies keep design anchor .548; the full-block
fallback threshold is adjusted so their sum is exactly .75.
The critical restart envelope is evaluated with an outward top-root
certificate and retains a declared 10^-9 reserve. All finite losses
are at most 2*10^-10 in block units.

A uniform weaker top coefficient gives a valid three-region proof,
but raises the binding capacity estimate. The tight certificate keeps
the two coefficients and five rational regions. The accepted proof
shortenings are the common retained-quarter lemma, one owner root
with three quadratics, a decreasing tiny-cap estimate, active-only
containers, and elementary cyclic tensor layouts. Their proofs are in
[SIMPLIFICATIONS.md](structural/SIMPLIFICATIONS.md).
