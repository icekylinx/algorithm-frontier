# Selected algorithms from the SAT research checkpoint

The supplied checkpoint was screened for substantive, completed algorithms
on arbitrary inputs in their declared models. Rebuilding an existing theorem,
taking a direct corollary, or substituting a newer numerical matrix exponent
does not by itself qualify as a selected contribution. A fixed parameter is
not a defect; a missing general-input evaluator is.

## Retained constructions

| Algorithm | Strongest selected bound | Substantive construction and scope |
|---|---|---|
| [Integral ordered crossing circuits](../problems/noncommutative-crossing/) | <code class="math">O(N^{1.719516})</code> arithmetic gates | Normalization-one Schur crossing, unpaired integral character profiles, a full integer three-shape deduction, simultaneous ordered insertion and shared products. One circuit works over every associative unital ring. The exact integral tensor source premises are listed explicitly. |
| [Uniform ordered subset contraction](../problems/ordered-subset-contraction/) | <code class="math">2^{O_\epsilon(k)}(N/k)^{3k/8+1/2+\epsilon k}</code> | Growing row counts and balanced subset sizes, arbitrary input weights, division-free multiplication in its original order, and all input-table and parameter overhead charged. Works over associative rings, including nonunital rings; unequal sizes use the proved capacity envelope. |

The first result's known field curve and underlying crossing idea retain
their original attribution. Its selected content is the integral and ordered
composition. The second result's selected content is the uniform
growing-parameter algorithm, rather than the numerical square-exponent
substitution. Neither result asserts historical priority or global optimality.
The subset bound gives no smaller-base algorithm for the integer square
permanent when row count is comparable to universe size.

## Selection and cleanup

| Material | Disposition and reason |
|---|---|
| SAT theorem reconstruction and immediate counting consequences | Not added as separate research results: reconstruction and direct consequences fail the substantive-contribution filter. |
| Modular permanent reconstruction and elementary streaming derandomization | Not added as a separate result under the same filter. |
| General integer square-permanent target | Not added. The proposed routes still require unresolved evaluators or overlap corrections. No general algorithm is obtained merely by naming that dependency. |
| Structured-family permanent routes | Not added as a replacement for a general-input permanent result. |
| Older crossing exponents and growing-degree position-partition bound | Superseded branches omitted. Incomparable fixed-degree analyses remain internal proof context where needed. |
| Standalone numerical matrix-exponent substitutions and routine padding outputs | No independent catalogue entry. Only necessary supporting calculations remain. |
| Review archives, formal trees, build logs and historical PDFs | Not copied. Historical formal receipts are not represented as current verification. |

The shallow existing-repository pass also removed five auxiliary entries
from the independent supporting-results catalogue: augmenting-path recourse,
fractional path extraction, exact flow trimming, the subsumed laminar
reservation approximation interface, and a static slack reduction whose fast
dynamic provider was not realized. Useful proofs remain internal dependencies.
The obsolete unfinished colored-pool forest candidate was deleted; its valid
focused audits now refer to the accepted no-reset construction. These changes
do not assert that every remaining repository theorem has undergone a new
comprehensive review.

## Evidence and source identities

The two packages provide **18,124 exact finite assertions** in six focused
suites. They cover actual noncommutative identities, integer lattice and
capacity certificates, ordered substitutions and circuit interfaces. They do
not implement the asymptotic matrix engines or formally establish the cited
external theorems. The crossing TeX sources have closed local references;
no local PDF compilation is claimed.

The [import manifest](../provenance/imports/sat-research.json) identifies all
1,069 original members, the 22 selected source members and their 20 adapted
targets. Excluded payloads have metadata only. New reader guides, wrappers
and exact certificate adapters are current curation work, not purported
byte-identical source copies. Original ZIPs remain ignored.

```sh
python3 -B tools/verify_sat_import.py
```

This command checks selection metadata, retained targets and source hashes;
when the original archive is locally available it also replays its entire
member inventory. It does not validate mathematical correctness. Only
changed algorithms and affected documentation/metadata are checked for this
import; no full repository regression is claimed.

**Attribution:** icekylinx and GPT-6 Astra Pro. Apache-2.0 under the repository
[license](../LICENSE); cited external constructions retain their attribution.
