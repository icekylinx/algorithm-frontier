# Rational whole-block decoder realization and quotient composition audit

This note connects the
[exact rational implementation](../reference/whole_blocks.py) to
[Theorem B1](exact-label-whole-blocks-and-hyperedges.md), and audits its
composition with the ordinary quotient backend and the
[adaptive ledger](adaptive-quotient-resparsification.md).
The executable component is the deterministic compiler/decoder and exact
whole-item rank/query interface. A quotient sampler is not implemented.

## Input and realization proposition

The input is an explicit tuple of original items, each given by rational
column vectors in one original ambient space. Every column of an item has
the item's same original label set. Original rows have their own label
sets. Weights are nonnegative rationals, failures are original label IDs,
and the supplied failure budget is a nonnegative binary integer. Nonzero
incidences must contain the row labels in the item labels and meet any
supplied deficit bound. The compiler verifies these conditions on **all
original rows**, before selecting independent rows.

**Proposition.** In `LIFT` mode, `decoder(F)` is exactly the map `C T_F`
of Theorem B1, and `decode(F)` equals the original columns multiplied by
one common item scalar. That scalar is zero precisely for items whose
original labels meet the failure set. In `FULL_INPUT` mode the compiler
returns the original input before constructing the lift; its direct query
method evaluates the same original objective exactly. In `ZERO` mode all
block-subspace-complement objectives are zero. Every mode has polynomial
bit complexity in its explicit rational input and query representation.

**Proof.** The canonical feature module supplies exact row selection by
original coordinate pivots. Let `P A` be those original rows. The backend
selects an invertible column minor of `P A` and solves each original row
against that minor. Its `compression` is the exact matrix `C` satisfying
`A=C(P A)`. The selected original row IDs keep their actual original
labels; elimination rows receive no artificial labels.

Used original label IDs are mapped injectively to positive integer points.
The dummy has point zero and never appears in a genuine failure set. The
backend multiplies ordinary homogeneous linear forms, padding the actual
label difference by powers of the dummy form. Its dictionary keys are
monomial exponent tuples. There are no divided powers, factorial
normalizations, floating point coefficients, or random evaluations.

For any allowed failure query it forms the normalized univariate product
whose factors are `1-t/alpha_f`; unused failed label IDs are omitted after
checking the original failure budget. This polynomial has value one at
the dummy and zero exactly at the failed used points. Its coefficient
vector is substituted into the homogeneous monomials. Multiplying a
selected row block by the product of these values on that row's original
labels gives the full product on the item's labels: on every nonzero
incidence the row labels and their item-label difference are disjoint and
cover exactly the item labels. Zero incidences contribute zero.

This proves the common-scalar identity of Theorem B1, Equation B4, before
and after reconstruction by `C`. Every column of a whole item has the
same scalar, regardless of its own zeros or its position among the item's
columns. Subspace membership is unchanged by a nonzero scalar, and zero
lies in every linear subspace. Thus the preimage of any original subspace
has exactly the survivor/outside predicate of Equation B5. `value` checks
that predicate for an entire block and charges its weight once. An empty
or zero-dimensional block is always contained; it is never charged.

The effective failure degree is bounded by the used-label count, and the
deficit is replaced by its maximum actual value, also at most that count.
Consequently the formal binomial dimension has polynomial bit length in
the explicit label representation. If rank is positive and formal lift
dimension is at least item count, `FULL_INPUT` is returned before calling
either feature enumeration or polynomial multiplication. Otherwise the
materialized dimension is below item count. The number of original block
columns is itself explicit input. Every coefficient is a product/sum of
polynomially many integer powers of polynomial-bit label points. Rank
compression, queried subspace elimination, normalized failure products and
decoder evaluation use polynomial-size rational matrices and have the
usual rational determinant bit bounds. Rank zero uses no feature matrix.
The decoder need not be precomputed for all failure sets. QED.

## Exact interface to ordinary quotient sparsification

`rank_on` takes original item IDs and returns the dimension of the sum of
their **whole lifted blocks**. This is a normalized, monotone, integer
submodular rank with total rank bounded by the formal lift dimension and
every positive marginal at least one. A lifted subspace's contained-item
set is closed: the span of its contained blocks is still inside that
subspace, so every zero-marginal block is already contained.

Quanrud, *Quotient sparsification for submodular functions*, SODA 2024,
[Theorem 1.1 and Lemma 2.1](https://kentq.s3.amazonaws.com/submodular-sparsification.pdf),
therefore apply to this exact original-item rank oracle. The theorem
preserves every quotient with one nonnegative reweighting on original IDs.
It does not split an item's weight across columns. Its all-quotient event
includes every preimage subspace of every original failure/subspace query.
This establishes one event uniform over those queries, including queries
chosen after the output, with no union bound over failure scenarios.
Failure-dependent decoding never changes the summary coefficients.

This is a completed mathematical composition through an identified
published algorithm. The lack of a sampler in the reference does not turn
that mathematical construction into an unproved conditional statement.
It does delimit the software: `Compilation` retains the original input
and, in `LIFT` mode, its entire compiled representation.

## Adaptive restriction, error and probability ledger

The quotient restriction argument in QB2 is exact for every retained
original-ID support. A closed original set intersected with a retained
support remains closed for the restricted rank, by diminishing returns.
Its complement is the corresponding restricted quotient. All later
backend calls therefore approximate every original query's current weight,
not a different or externally enumerated query family.

The constants in QB2–QB6 imply that every nonterminated preliminary call
halves the logarithm of current support size. Reading the stages backward,
their requested relative errors have the geometric envelope in QB7.
Their sum is less than `0.054 epsilon`; the final error adds
`epsilon/4`, so the total is less than `0.304 epsilon`. The product of
lower factors is at least one minus the sum. The product of upper factors
is at most its exponential, which is below `1+epsilon` for
`0<epsilon<1`. This proves simultaneous multiplicative composition,
including zero-valued quotients.

Every call uses fresh randomness conditional on the current support and
weights. Quanrud's Lemma 3.3 and its constant-amplification footnote allow
any fixed polynomial confidence exponent by decreasing the threshold
constant. Lemma 3.4 unions the strength levels, and the concluding Chernoff
argument also bounds support. Thus the quantified confidence used in QB1
is available with an absolute sampling constant. Size-cap violations
terminate with a failure flag. The accepted size caps enforce geometric
shrinkage even on a path with a silently false quotient guarantee. The
backward pathwise bound on conditional failure budgets in QB9 consequently
also bounds their expected sum. The final call's fixed confidence budget
and exact treatment of tiny supports yield the stated constant success
probability, without a support penalty for the number of stages.

## Integer-rank bit ledger and bounded random bits

Quanrud's Section 3 computes an exact strength decomposition by submodular
minimization and fractional optimization. The threshold for a strength
layer is a common parameter times a ratio of a difference of current
rational weights to a positive difference of rank values. In this client
that rank difference is an integer between one and the original lifted
rank bound. Replacing the logarithmic parameter factor by a dyadic
rational within a fixed constant factor preserves the analysis after an
absolute constant adjustment.

With one current common weight denominator, one pass adds only the
denominator factors of its at most current-item-count many integer rank
gaps and the common dyadic parameter. This is additive polynomial bit
growth, as QB4 states. Rounded weights are integer multiples of their
layer threshold. A threshold is bounded by a constant times the current
total weight; hence total-weight bit length grows by at most a logarithm
of current item count per pass. There are only logarithmically many
logarithmic-size-halving stages. All exact rank queries remain polynomial
bit computations on subsets of the fixed compiled original items.

For completeness, a fixed-time random-bit implementation can avoid
unbounded rejection loops for rational Bernoulli probabilities. There
are at most `2m^2` individual rounding draws over all calls on an initial
support of size `m>=2`: each call has at most `m` draws and even the crude
stage bound `m+1` suffices. Round each exact Bernoulli probability downward
to a multiple of `2^(-b)`, where `b=ceil(log2(600m^2))`, and use exactly
`b` fair bits per draw. Couple this draw to the ideal rational draw.
Conditional on every past history their mismatch probability is less
than `2^(-b)`. A union bound gives total mismatch probability at most
`1/300`, including adaptive histories and stopping. Increasing the fixed
confidence constants leaves success at least `2/3`. Output weights remain
the exact rational rounded-layer values; only their selection
probabilities are discretized. This supplies a strict polynomial random-bit
account instead of silently claiming a worst-case bound for rejection
sampling. The reference module itself uses no random bits.

## Review scope

The audited mathematical scope is rational whole-block decoding and its
composition with the published ordinary quotient theorem and the
integer-rank adaptive resparsification ledger. The executable scope is the
compiler, exact original-item rank oracle, common-scalar maps and query
evaluation, including the full-input dimension gate. Finite tests compare
independent polynomial expansion, original subspace ranks, graph cuts and
atomic hyperedge partition objectives.

Finite-field extension software, the rational subgroup-rank client,
quantum stabilizer algebra and the support lower-bound reductions are
outside this review. Their existing mathematical statements and primary
dependencies remain separately recorded. No external peer review or
proof-assistant verification is claimed.

**Attribution:** icekylinx and GPT-6 Astra Pro.
