# Results overview

This page is the entry point for the current curated frontier. Read the
problem README before reading a proof: the README fixes the model, comparator,
parameter, and status. A headline is kept only when it is the strongest
supported bound in that exact scope; incomparable parameterizations remain
separate.

## Current modules

Checkpoint Q adds arbitrary-accuracy schemes and robust unit gates; these are
listed below as separate, parameter-sensitive modules.

| Problem | Current result | Main limitation or status |
|---|---|---|
| [Whole-ground allocation](problems/whole-ground-allocation/) | Exact factor 2 for one-value and compulsory two-value rows; fixed-R intrinsic-value tradeoff; base 50/27 in the q+o(q) sense | Exponential-time whole-ground conversion; exact model matters |
| [One-value exact two](problems/one-value-exact-two/) | Exact factor 2 in (27/4)^c poly(H) | Corank-parameterized scope |
| [Two-value exact two](problems/two-value-exact-two/) | Exact factor 2 for compulsory two-value allocation | Large-cover/corank parameter; one exact budget |
| [Intrinsic values near two](problems/intrinsic-values-near-two/) | Factor 2+eta under derived-corank conditions; exact boundary cases separately proved | No uniform exact-two sub-two-base claim |
| [Unrelated values](problems/unrelated-values-additive/) | Additive (1-epsilon)OPT-u_p guarantee; one-budget extension | No unsupported multiplicative general-value claim |
| [Unrelated joint role](problems/unrelated-values-joint-role/) | P-specific near-two route with joint setup/assignment budget | Keep the selector and budget assumptions visible |
| [Recipient polymatroids](problems/recipient-polymatroid/) | Factor 4-3/r versus integer OPT | Different comparator from recipient-matroid configuration result |
| [Recipient-matroid configuration](problems/recipient-matroid-configuration/) | Factor 4-3/r versus coupled configuration LP | Recipient-matroid scope only |
| [Explicit-item matroid union](problems/item-matroid-union/) | Factor 4-3/r versus integer OPT and stated configuration addendum | Explicit-item model |
| [Selected flow](problems/selected-flow/) | Rate (1-epsilon)OPT in Gamma(1/epsilon)^c poly(H) | Exact selection and routing interfaces |
| [Robust scenario flow](problems/robust-scenario-flow/) | Same rate in each explicit scenario | Exact full-rate admission hardness is separate |
| [Shared setup flow](problems/shared-setup-flow/) | Same rate with exact shared setup/routing budget | Requires attaining minimum-setup selector |
| [Arbitrary-value allocation scheme](problems/arbitrary-value-allocation-scheme/) | Value at least (1-epsilon)OPT with one shared setup/assignment budget | Q scheme; binom(q,r) exp(O(r/epsilon)) time |
| [Arbitrary processing-time scheduling](problems/arbitrary-processing-scheduling/) | Makespan at most (1+epsilon)OPT with mandatory jobs and one exact budget | Q scheme; 2^{O(q/epsilon)} time |
| [Activated-machine scheduling](problems/activated-machine-scheduling/) | Makespan at most (1+epsilon)OPT with an activated machine basis | Q scheme; mandatory totals retained |
| [Six-profile 3/2 scheduling](problems/six-profile-three-halves/) | Exact 3/2 endpoint in 6^q poly(H) for the arbitrary processing profile endpoint | Six-profile endpoint; base not claimed optimal |
| [Robust width-two allocation](problems/robust-width-two-allocation/) | Fibonacci-base phi^c exact positivity gate | Width-two obstruction promise; explicit violation returned outside promise |
| [Robust unrelated allocation](problems/robust-unrelated-allocation/) | Additive robust (1-epsilon)FOPT-u guarantee with exact scenario budgets | Additive result; may return zero on unit obstruction |
| [Processing-bucket tradeoff](problems/processing-bucket-tradeoff/) | gamma_k curve: 5/3, 11/7, and approach to 3/2 | Parameterized profile frontier |
| [Robust bounded certificates](problems/robust-bounded-certificates/) | ceil(K*/d) under width-w aggregate certificate promise | Exact scenario budgets; promise is explicit |
| [Two-scenario robust hardness](problems/robust-two-scenario-hardness/) | W[1]-hardness for exact admission via k-SUM | Negative result with corank c=k |
| [Allocation lower bounds](problems/allocation-lower-bounds/) | Oracle barriers below 2 and below 3/2; configuration gaps | Negative results; no explicit-input hardness inferred |

Graph, matching, scheduling, dynamic data-structure, and hypergraph modules are
being added in later commits. Their source notes are already preserved in the
O/P snapshots, but they are not treated as curated current results until their
own README, proof, and verify sets exist.

## Source precedence

- `sources/checkpoint-p/` governs allocation-specific claims.
- `sources/checkpoint-o/` is the cumulative source for flow, scheduling, and
  graph-transfer claims.
- `sources/matching-manuscript/` is the separate general-matching manuscript
  package.
- `provenance/archive-manifest.json` records every original archive hash,
  including the newly added P archive.

## Review status

The source audits are internal mathematical audits. They are not peer review,
formal proof checking, or an implementation certificate. Conditional claims
retain the exact external primitive or internal contract on which their runtime
depends.
