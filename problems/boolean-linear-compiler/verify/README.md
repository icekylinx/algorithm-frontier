# Verification and scope

[Main proof](../proof.md) · [Source dependencies](../sources.md)

## Support-sized interval refinement and complete compilation

Run from the repository root:

~~~sh
python3 -B problems/boolean-linear-compiler/verify/check_interval_compiler.py
~~~

The checker uses only Python's standard library and exact integer arithmetic. Its seeded samples are deterministic, it writes no files, and it refuses optimized Python execution with `-O`.

| Finite domain | Checked quantity |
|---|---:|
| Coefficient vectors in <code class="math">\{-4,\ldots,4\}^n</code>, for <code class="math">0\le n\le3</code>, including zero vectors | 820 |
| Additional edge and seeded four-variable fixtures | 408 |
| Row/interval instances | 60,588 |
| Original Boolean assignment/interval comparisons | 469,589 |
| Local halving frames / signed-rounding comparisons | 53,080 / 423,742 |
| Empty recursive intervals / overlapping boundary pairs | 1,296 / 1,054 |
| All-even frames, with both boundary intervals empty | 11,953 |
| Maximum checked halving depth on large binary integers | 513 |
| Slack widths from zero through 1,024 / independently enumerated slack assignments | 1,025 / 701,099 |
| Complete signed linear systems / slack-budget profiles | 307 / 732 |
| Packed Subset Sum instances / packed-assignment comparisons | 5,413 / 115,796 |
| Original-system assignment comparisons / signed objective optimum comparisons | 6,781 / 732 |

For each exhaustive coefficient vector, the interval endpoints range from two below its elementary minimum sum to two above its elementary maximum sum. Every interval in that range is checked. The additional fixtures include zero rows, reversed intervals, negative odd coefficients, an empty recursive interval with overlapping boundaries, all-even rows, and coefficients of more than 500 bits. The test compares the complete catalogue disjunction with direct evaluation on every Boolean assignment; it also checks the local rounding identity, width cap, catalogue count, and recursion-depth bound.

The integration suite varies signed interval rows, signed equalities, all valid per-row slack budgets, infeasible systems, zero-variable systems, and signed objectives. For every branch, it independently enumerates every assignment to the packed signed Subset Sum instance, checks equivalence with the branch equations, and projects its solutions onto the original variable indices. The union of those projected sets must equal the complete feasible set obtained by directly evaluating the original system. Its minimum objective must also agree. Thus the integration check covers both existence and every original indexed witness; it does not rely only on a feasible example.

## Cardinality and common-coefficient refinement

Run from the repository root:

~~~sh
python3 -B problems/boolean-linear-compiler/verify/check_cardinality_compiler.py
~~~

This integrated checker uses the original Boolean system as its independent reference. It checks local conditional rounding on the same tested frames, then enumerates complete packed assignments and their original-variable projections. It reuses only elementary helpers from the unconditioned checker, uses exact standard-library arithmetic, writes no files and refuses `-O`.

| Finite domain | Checked quantity |
|---|---:|
| Exhaustive vectors in <code class="math">\{-2,\ldots,2\}^n</code>, <code class="math">0\le n\le4</code> / additional fixtures | 781 / 255 |
| Extra raw parity-layer fixtures without modal normalization | 24 |
| Layer intervals / original assignment comparisons | 126,629 / 394,214 |
| Local guarded-disjunction comparisons | 418,103 |
| Negative common-coefficient shifts / constant-row cases | 52,936 / 2,308 |
| Constant remainder frames / empty children | 18,598 / 11,319 |
| Full systems / nontrivial layers / slack-budget profiles | 306 / 726 / 846 |
| Packed instances / packed-assignment comparisons | 4,120 / 117,684 |
| Layers with a strict total slack reduction / constant-row rejections | 172 / 309 |
| Exact rational exponent comparisons, with all <code class="math">0\le Q_k,B\le\bar Q\le64</code> | 468,325 |

The budget comparison includes a uniform budget larger than a layer's own available slack count and time exponents zero, one-third, one-half, one and three-halves. Large binary common coefficients of either sign, zero/one-variable systems, original equalities, constant rows and every cardinality are included. Every packed branch retains the cardinality equality on the original indices; the complete solution union must agree with direct original-system evaluation. The [full companion](../manuscripts/cardinality-and-modal-interval-compilation.md) proves the bounds and the objective transfer independently of these finite examples.

## Earlier interval baseline

The [shared signed-interval and exchange checker](../../../tools/verify_sensitivity_certificates.py) retains the earlier <code class="math">5s+1</code>-value interval rule:

~~~sh
python3 -B tools/verify_sensitivity_certificates.py
~~~

Its signed-interval section covers 342 nonzero three-variable rows with coefficients from <code class="math">\{-3,\ldots,3\}</code>, 79,002 row/interval pairs with endpoints in <code class="math">[-10,10]</code>, 632,016 Boolean comparisons, and 1,025 slack widths. This is evidence for the previous baseline, not the new support-sized rule. Its separate matching-exchange section belongs to another family.

## Proof obligations and backend composition

The complete proof uses signed Euclidean floor: <code class="math">a_j-2\lfloor a_j/2\rfloor\in\{0,1\}</code> even for negative <code class="math">a_j</code>. The number of odd coefficients gives the actual rounding-error bound. Clipped boundary tests cover every assignment whose rounded sum lies outside the safe recursive interval, including when that interval is empty. At most two boundaries are emitted at each scale; overlaps are permitted and counted literally. Zero rows are handled before logarithmic parameters are defined. The finite evidence supplements this inductive proof and does not establish the asymptotic theorem by enumeration.

Every packed branch has at most <code class="math">n+B</code> variables and polynomial binary encoding length. Signed radix packing uses reduction of signed differences modulo the radix. Sequential enumeration keeps only one backend workspace live. Fully enumerating the objective-threshold row costs an additional polynomial factor and introduces no extra exponential slack parameter.

The primary theorem is stated in symbolic backend exponents <code class="math">\alpha</code> and <code class="math">\sigma</code>. A time-only backend supplies no simultaneous space bound. Numerical instantiations inherit the selected backend's constructive interface and every stated analytic premise, as recorded in the [fast Subset Sum proof](../../subset-sum-fast-deterministic/proof.md). The executable does not run an exponential-time Subset Sum backend, verify its exponent, or certify continuous inequalities.

**Attribution:** icekylinx and GPT-6 Astra Pro.
