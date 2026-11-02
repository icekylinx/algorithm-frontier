# Sources and exact-counting dependency boundary

Attribution: **icekylinx and GPT-6 Astra Pro**. Apache-2.0 under the
repository [license](../../LICENSE). External mathematical sources retain
their attribution. The selected construction is the exact-counting extension,
not a rediscovery of its source decision algorithm or an independently
advertised numerical substitution.

## Pinned primary source

OpenAI, *Subset Sum in Time `O(2^(0.49n))`* (4 October 2026), source snapshot
`openai/math` commit `4eaee87548250b2682affda7d05d947c05554bae`. The six
sections below were fetched at that exact commit on 2 November 2026.
Their SHA-256 identities are recorded in the checkpoint import manifest.

| Primary source section | Mathematical interface retained |
|---|---|
| [Filtering](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/build/sections/filtering.tex) | `prop:filtering-moments` and `lemma:finite-filtering`; smooth positive finite-circle scores and their moment bounds. |
| [Setup](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/build/sections/setup.tex) | Deficiency, random half restrictions, capped preliminary search and prime-collision estimates. |
| [Aliases](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/build/sections/aliases.tex) | `thm:aliases` for every fixed transformed input and fixed tags, original indexed aliases, exact-integer exclusion and capped list/pair work. |
| [Checksum](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/build/sections/checksum.tex) | The full construction behind `thm:checksum`, including conditional coverage, one-side sizes, joint match count, multiplicity correction and variance. The phase law is modified locally; its original theorem statement alone is not applied. |
| [Implementation](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/build/sections/implementation.tex) | `eq:finite-evaluation-error`, `eq:residual-accuracy` and `eq:all-history-time`; guarded bit work, finite sampling and high-precision arithmetic. |
| [Numerical bounds](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/build/sections/numerical.tex) | Analytic trapezoid, inner errors, score errors and strip estimates. The unchanged strip inputs are cited premises; the changed outer exponents and parameter ledger are checked exactly here. |

The local proof establishes the polynomial-prime phase law, shifted-grid
first-derivative controls, trace reconstruction, nonisolating tag bins,
reuse of indexed aliases, the original all-sparse-support coverage argument
at the selected parameters, and the complete cap ledger.
This is more than applying a decision procedure to a counting problem.
The original mathematical source lemmas remain named external dependencies;
their full software implementation or formal certification is not imported.

## Selected checkpoint members

Source: the supplied `tcs_research_checkpoint.zip`, revision 2 November 2026.
The [repository import record](../../provenance/imports/tcs-research-20261102.json)
identifies every original member and the retained adaptations.

| Checkpoint member | Current target |
|---|---|
| `manuscripts/exact_counting.md` | [Main proof](proof.md), including the complete changed-phase construction and internal interval/activity reductions. |
| `manuscripts/exact_counting_refinement.md` | [Parameter certificate](parameter-certificate.md), retaining only the strongest certified parameter set as the selected bound. |
| `verification/counting/check_trace_and_threshold.py` | [Trace and interval checks](verify/check_trace_and_threshold.py). |
| `verification/counting/check_activity_lifting.py` | [Product-activity checks](verify/check_activity_lifting.py). |
| `verification/counting/check_improved_filter_certificate.py` | [Exact rational certificate](verify/check_improved_filter_certificate.py). |
| `verification/counting/check_weighted_trace.py` | [Weighted trace checks](verify/check_weighted_trace.py); unrelated positive-moment optimization certificate removed. |

No copied external source tree, original ZIP, historical report or raw review
archive is a publication artifact. Older numerical parameters remain only
where the baseline derivation needs them. Routine threshold/activity
consequences are internal proof tools, not separate selected results.
