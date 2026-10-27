# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md) and the following companion manuscripts:

- [Two integrality gaps for recipient-polymatroid configuration relaxations](../configuration-gaps.md)
- [The factor-two oracle obstruction persists at refined parameter zero](../refined-parameter-barrier.md)

## Mathematical evidence

- The hidden-set rank functions are proved normalized, monotone, integral and submodular; their oracle transcript distinguishes the unique hidden basis.
- Allocation below factor two and scheduling below three halves have separate constructions. The scheduling dual is verified as an independent rank function.
- The configuration companions distinguish the aggregate gap approaching <code class="math">r</code> from the full residual gap exactly two. The refined-parameter companion specifies the threshold at which its parameter is zero.

An internal manuscript audit on 2026-10-27 reconstructed all three
canonical proofs, including rank and corank quantifiers, the complementary
small-job base, and the distinction between a free heavy Boolean cap and
the loop-deleted dual ground. It also replaced the residual-cut lemma's
conceptual natural-matroid step by a direct tight-support inequality and
supplied its greedy vertex argument. This closes that proof dependency
without a resource-unit expansion. Both component-merging comparisons
also have direct integer decompositions, rather than relying on a general
polymatroid decomposition interface. The family is ready for manuscript
review in these stated models; this is internal mathematical review, not
external peer review or proof-assistant verification.

## Executable evidence

Run the independent exact-arithmetic checker from the repository root:

```sh
python3 problems/allocation-lower-bounds/verify/check_barriers.py
```

Its finite scope is:

- All 240 hidden ranks with `2 <= q <= 7` and `1 <= r < q`: normalization, integrality, monotonicity and every local two-element submodular inequality. All 4,692 selected-basis comparisons test the one-unit and unique two-unit allocation against every subset row. The only changed rank answer is the hidden set.
- All 213 scheduling duals in that range satisfying `q >= r+2`: the same rank axioms, singleton capacity two, and the complementary hidden schedule's base inequalities and total. The 28 balanced hidden ranks test the all-ones feasible base giving a free Boolean cap in the refined-zero construction.
- The aggregate gap for `2 <= r <= 7` and `D = r, 2r, ..., 6r`: 2,919 exact rational subset-size inequalities, plus attaining integer quotas and the next-quota obstruction.
- The full residual gap for `3 <= r <= 30`: all 952 subset-size cuts. Independently at `r=3`, all 415 feasible reserves in `{0,1,2}^6` satisfy their actual minimum-slack reserve cut, without invoking the subset-equivalence lemma. These are all integral reserves because singleton capacity is two. Their direct decomposition into the two uniform components is also checked, as is the free-plus-two-rank-one decomposition on all 256 vectors in `{0,1,2,3}^4`.
- All 1,957 orders on subsets of the six-player residual-gap instance: feasibility of each greedy reserve and 11,742 comparisons of its directly minimized residual capacity with the rank marginal of its support.

These finite checks do not execute an adaptive lower-bound adversary,
enumerate unbounded ranks, or prove the asymptotic query bound. The
convexity argument covers all real reserves mathematically; the direct
reserve enumeration covers its named finite integral instance.

## Model and verification boundaries

These are deterministic rank-query lower bounds and explicitly defined
relaxation gaps. They do not assert the same query bound for randomized
algorithms, explicit-input NP-hardness, ETH bounds, or optimal
approximation-algorithm exponential bases. The refined-zero threshold is
fixed at `OPT/(2+eta)` for positive `eta`; the compulsory example has
unrefined heavy-cover rank equal to the ground size. The lower bounds do
not solve the separate four-unit/two-unit promise problem. The scheduling
construction uses arbitrary small-job polymatroid value oracles, rather
than explicit allowed-machine lists.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
