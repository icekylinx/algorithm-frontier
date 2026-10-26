# Sources and proof dependencies

## Canonical manuscripts

- [A direct dynamic spanner from tracked terminal forests](proof.md)

## Linked mathematical dependencies

These manuscripts contain the interfaces, auxiliary arguments or source
comparisons referenced by this result. Their stated hypotheses remain
part of each use; an interface analysis does not supply an omitted backend.

| Layer | Required contract | Scope of the local argument |
|---|---|---|
| Numerical hierarchy | Deterministic adaptive histories, actual-size initialization, upper estimates and polynomial-bit lengths | The APSP factor is a premise, with its own local-provider dependencies. |
| Tracked-terminal construction | Explicit nearest-pivot and local source forests, fixed owner handles, typed nulls and chronological physical-edge logs | Proves an observer and short-path union with ordinary recourse proportional to the complete input history. A distance-only oracle is insufficient. |
| Clipped reporting | Reports at most the threshold number of physical edge occurrences, skipping null and connector chains | Charges actual reported length and route retirement; no output charge is hidden in numerical query time. |
| Full-horizon construction | Single-instance assignment accounting (F2) and work (F3) | Proves nested deletion clocks, actual seeding costs and recourse depending on $`n+D`$. Dense graphs are not rebuilt after every $`n`$ deletions at every layer. |
| Nonnegative integer lengths | One unweighted zero-edge class plus the positive dyadic classes | Preserves zero-cost connectivity by current output paths and sums all class work and recourse. |

All conclusions concern settled updates. The providers must support the
same adaptive deterministic history as the enclosing construction.
An explicit current edge set supports full enumeration only at the
additional cost of writing that set; recourse measures changes to it.

- [Clipped walk reporting and a deterministic dynamic-spanner transfer](../../manuscripts/graph-backends/clipped-walk-queries-and-dynamic-spanner.md)
- [Destructive path-support extraction from the APSP hierarchy](../../manuscripts/graph-backends/destructive-apsp-path-support-extractor.md)
- [Dynamic marked-forest compression and short-path unions](../../manuscripts/graph-backends/dynamic-marked-forest-short-path-union.md)
- [Deterministic dynamic spanners: current public baselines and admissible comparisons](../../manuscripts/graph-backends/dynamic-spanner-public-baseline-audit.md)
- [Nonuniform parameter budgets for the current hierarchy](../../manuscripts/graph-backends/nonuniform-parameter-budget-frontiers.md)
- [Joint retuning of the public deterministic APSP construction](../../manuscripts/graph-backends/public-apsp-joint-retuning-audit.md)
- [A stronger public APSP comparison at exactly the same stretch scale](../../manuscripts/graph-backends/same-stretch-apsp-comparison-and-root-audit.md)
- [Separating metric stretch, forest congestion, and work](../../manuscripts/graph-backends/separated-metric-forest-and-strong-sssp.md)
- [Audit of the public-provider flat-forest spanner comparison](../../manuscripts/graph-backends/tracked-terminal-spanner-public-flat-comparator-audit.md)
- [Fully dynamic all-pairs distances: a time–stretch theorem](../apsp-frontier/proof.md)
- [Strong forests from uncontracted Steiner cores, without recursive degree resets](../decremental-strong-forest/proof.md)
- [Zero-length edges in integer distance and spanner interfaces](../../manuscripts/graph-backends/nonnegative-integer-distance-adapters.md)

## Primary references

The manuscripts identify the theorem and version used at each import.
Direct external references appearing in this reading path are:

- <https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.111/LIPIcs.ICALP.2025.111.html>

The full-horizon batching source is **Section 5 of the published
ICALP 2025 version** of Kyng–Meierhans–Zöcklein, *A Simple Dynamic
Spanner via APSP*. The older arXiv version is not interchangeable
with that section. The numerical constants and explicit overhead
substitution in this repository remain separate from the public
batching theorem.

## Evidence and provenance

The [verification note](verify/README.md) states the scope of executable
evidence and the remaining mathematical dependencies. The
[import record](../../provenance/README.md) preserves source revisions,
canonical paths, attribution and applicable licenses.

**Attribution:** Yilin Liu · GPT-6 Astra Pro.
