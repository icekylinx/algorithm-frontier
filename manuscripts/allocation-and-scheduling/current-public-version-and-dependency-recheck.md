# Current public versions and the allocation/scheduling proof dependencies

**25 October 2026. Independent primary-source recheck.**

This note rechecks the public comparison after noticing the revised
Davies--Rothvoss--Zhang manuscript. It supplements, rather than replaces,
[matroid-allocation-public-comparison-and-version-audit.md](matroid-allocation-public-comparison-and-version-audit.md). The latter
already records the correct version history and the separate unclosed
historical-exchange interface. No theorem below is certified merely by
an abstract or by the fact that another paper cites it.

## 1. The corrected numerical baseline

The official [DRZ submission history](https://arxiv.org/abs/1807.07189)
lists v2 on 7 May 2019, v3 on 27 July 2025, and v4 on 4 January 2026.
The distinction is **v2 versus v3/v4**, not v3 versus v4.

| Public statement | Version and exact scope |
|---|---|
| Integral value `(1/3-epsilon)T-u/3` from the compact player-basis relaxation `Q(T)`; resulting ordinary Santa Claus factor `4+epsilon` | [DRZ v2, Theorems 2--3](https://arxiv.org/pdf/1807.07189v2). Superseded numerical claim. |
| Integral value `(1/5-epsilon)T-u/5` from `Q(T)`; resulting ordinary Santa Claus factor `6+epsilon` | [DRZ v3](https://arxiv.org/html/1807.07189v3) and [v4, Theorems 2--3](https://arxiv.org/html/1807.07189v4). Current displayed theorem. |
| Polynomial `4+delta` for ordinary restricted Santa Claus, against its configuration LP | [Cheng--Mao, arXiv:1905.06084](https://arxiv.org/abs/1905.06084), and the [2022 Algorithmica publication](https://link.springer.com/article/10.1007/s00453-022-00942-y). This independent public result remains a baseline. |

Here `u` is the largest ordinary physical-item value. DRZ's player
matroid selects the recipients to serve; it does not impose an arbitrary
recipient polymatroid separately on every resource. Cheng--Mao's
ordinary problem likewise does not supply that broader resource model.
The phrase “the public Santa Claus baseline is six” would therefore be
incorrect without identifying the particular DRZ compact-LP route.

DRZ v4 Section 4 explicitly explains its correction: blocker growth
proved when a layer was created could fail after collapses. The revised
algorithm checks existing layers for newly available adding edges and
changes the relative edge sizes. This supports the stated revision;
it does not establish that every other local-search paper has the same
defect. The authors themselves point to Cheng--Mao's independent factor
four improvement.

## 2. BLMRS has one currently listed arXiv version

The [official history of arXiv:2307.08453](https://arxiv.org/abs/2307.08453)
currently lists only v1, dated 17 July 2023. In that manuscript,
[Theorem 4](https://arxiv.org/html/2307.08453v1) states polynomial
`8+epsilon` for arbitrary resource values and `4+epsilon` for two values
under integral recipient polymatroids. Corollary 5 gives `7/4+epsilon`
for two-size job-polymatroid makespan; Theorem 23 gives the general
largest-job additive rounding and hence factor two.

Its introduction's DRZ factor-four citation is historical. Its own
algorithm is separately specified and analyzed: Appendix F Lemmas
31--33 use the current blocking set, prove shrinkage after recursion,
and derive the current size inequality from rank. They are not a
black-box use of superseded DRZ Theorem 2. This dependency inspection
preserves BLMRS's displayed results; it is not a new complete proof
audit of every lemma in that public paper.

## 3. Internal factor four does not import the corrected invariant

The relevant proof chain in the research notes is explicit:

1. [general-resource-all-remaining-blockers.md](general-resource-all-remaining-blockers.md) establishes individual
   player eligibility, the separate already-matched-owner case,
   earliest-layer fundamental-circuit exchange, and the current
   reservation construction.
2. [recipient matroid configuration proof](../../problems/recipient-matroid-configuration/proof.md) maintains
   independence of every unmarked matching block after contraction of
   **every ordered center prefix**, including prefixes ending inside a
   layer. Appending a candidate marks every still-unmarked record at
   each used resource where the whole candidate is dependent.
3. Before a maximality/growth calculation, every retained center is
   scanned for a current strong-release condition. A passing center
   triggers one atomic earliest-layer exchange. Releasing its group
   alone is not an allowed mutation. This recheck applies even when
   the center's own designated group has not changed.
4. The retained-prefix proof is repeated for each atomic exchange.
   The rank charge is recomputed from the **current** reserved sets:
   `Phi <= max{u,2B+min(u,B)} |Y|`. The finite-rank and positive-slack
   running-time bounds use the separately proved signature argument.

Consequently the internal result does not use a birth-time size
inequality as though it survived every collapse. The stronger invariant
and normalization procedure are part of the new algorithm, and their
cost is paid. Its `2^{O(r)}` or rank-quasipolynomial running time is also
different from the superseded public polynomial-time assertion.

This is a dependency conclusion, not a claim that recognizing the DRZ
error automatically proves the new algorithm. The complete replacement invariant is proved in the [resource-matroid manuscript](../../problems/recipient-matroid-configuration/proof.md).

## 4. Natural-matroid compression is a separate algebraic step

For an integral polymatroid rank function `f`, the conceptual natural
matroid has copy-set rank

`r(C(z)) = min_{S subseteq P} [f(S)+z(P\S)]`.

This identity and submodular minimization give compressed rank queries
without enumerating binary-encoded units. The contraction-loss lemma
then preserves a subvector of a fixed integral optimal allocation,
losing at most the rank already reserved. Neither statement uses a
DRZ layer argument.

[recipient polymatroid proof](../../problems/recipient-polymatroid/proof.md) proves the
prefix invariants for whole copy blocks, including the exchange and
current release test. Its original comparator is integer optimum.
The later stronger residual-configuration comparator is proved via
valid residual cuts and truncation, in
[recipient-polymatroid-residual-configuration-relaxation.md](recipient-polymatroid-residual-configuration-relaxation.md); it is not
inferred from the weaker aggregate configuration LP, whose gap can
grow with rank. These comparator distinctions remain necessary after
the public version correction.

## 5. Scheduling imports are independently accounted for

The scheduling notes use the internal unit-quota theorem, not the
superseded DRZ unit-resource or one-third claim. Their other operations
are polymatroid aggregation, coordinate caps, complement duality,
integral decomposition, and rounding the fractional small jobs.

These operations have direct algebraic proofs in the notes. In
particular, [Arbitrary small sizes through workload aggregation and per-machine rounding](../../problems/many-size-scheduling/proof.md) supplies
a separate per-machine rounding proof: sorted prefix counts are
rounded through integral polymatroid intersection, and telescoping
their weighted sums increases each machine's small-job load by at
most the largest rounded small size. Thus the retained `+u` term does
not rely on DRZ's approximation ratio or runtime analysis.

The player-matroid contraction in the bottleneck theorem is likewise
independent. A fixed independent set is contracted only on the player
side; the optimal basis still contains a contracted basis retaining
the resource promise. Zero insertion on the committed coordinates
preserves resource independence. Singleton ranks bound the actual
loads on those coordinates after final integral decomposition and
rounding. This is the argument checked in
[Scheduling by bottleneck commitments and a reduced search rank](../../problems/commitment-scheduling/proof.md).

## 6. Checkpoint wording

The appropriate current comparison is:

* ordinary restricted Santa Claus: retain Cheng--Mao's public
  polynomial factor `4+epsilon`;
* the DRZ player-matroid compact-LP theorem: cite current v4 and its
  one-fifth guarantee, while labeling v2's one-third result historical;
* arbitrary recipient polymatroids: retain BLMRS's displayed general
  `8+epsilon` and two-value `4+epsilon`, with an explicit v1 date;
* the research factor four and scheduling transfers: describe them as
  internally reviewed theorems in a different parameter/time regime,
  with the precise comparator and additive terms stated.

No remaining dependency identified by this recheck requires reverting
the current internal factor-four or scheduling statements. This does
not settle the separately documented historical-exchange interface,
give external peer review to the research notes, or certify exhaustive
publication priority.

## 7. Bounded check of the current OpenAI mathematics index

The official [OpenAI mathematics manuscript map](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md)
was rechecked for the new allocation/corank direction. Its current
index contains no text match for “Santa”, “allocation”, or “matroid
parity”. The nearby result 114 concerns randomized approximate
counting of common integer polymatroid bases. The scheduling result
124 concerns unit-length jobs with precedence constraints on three
identical machines, a different model.

These index statements are not imported as theorems in the present
proof. In particular, quota selection asks for vectors K*1_I.
Those vectors are only some integer points of the scaled matroid
base polytope B(K r_M), which also allows intermediate coordinate
counts. A common-base counting statement therefore cannot simply
replace the quota-selection problem or bypass its hidden-subset
oracle obstruction.

This is a documented index-level comparison, not a proof that no
related argument appears anywhere in the repository. The existing
general-matching OAI audit remains the baseline for that separate
line of work; no attempt to change its 4/5 exponent is made here.
