# Exact persistence certificates under correlated failures

A retained set of original top simplices preserves lower-dimensional persistence modules for one supplied filtration, after every allowed correlated failure.

[Proof](proof.md) · [Sources](sources.md)

| Field | Statement |
|---|---|
| **Guarantee** | At most $\min\left\{N,r\binom{h+a+b}{a+b}\right\}$ top simplices preserve every surviving boundary space at every filtration threshold, hence persistence modules in degrees at most $p-1$. |
| **Objective and output** | An original-top-simplex restriction plus the full original lower skeleton. A separate cost-ordered construction contains the canonical minimum-cost surviving boundary basis. |
| **Time** | Uniform deterministic polynomial preprocessing in the explicit complex and chosen field representation. With $C=\binom{h+a+b}{a+b}$ and $rC<N$, a direct lifted elimination uses $O(N(rC)^2)$ field operations plus original row selection and feature generation. |
| **Space** | The bound counts retained top simplices, not all lower faces, total encoded bits, or elimination workspace. |
| **Parameters** | $N$ counts $p$-simplices; $r$ is top-boundary rank; $a$ is vertex-label degree; $b$ is additional top-simplex label degree; $h$ is failure budget; $n$ is vertex count; $\ell$ is color count. |
| **Model and representation** | Fixed rational or explicit finite-field coefficients and one fixed supplied filtration. Field extensions used for construction preserve the original-field ranks. Filtration and independent cost orders require separate constructions. |
| **Lower-bound scope** | The one-color complete-universe envelope is exact. The general binomial coefficient is asymptotically necessary. No preservation of top-degree homology, integral torsion, or homotopy type is claimed. |
| **Review status** | The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed. |
| **Source** | [Complete proof](proof.md) and [canonical manuscript map](sources.md). |

## Results

| Result | Retained top-simplex bound / guarantee |
|---|---|
| General vertex and top labels | $\min\left\{N,r\binom{h+a+b}{a+b}\right\}$ |
| One color per vertex, no extra top labels | $\min\left\{N,kr,\binom{n}{p+1}-\binom{n-k}{p+1}\right\}$, $k=\min\{h+1,\ell\}$ |
| Overlapping vertex labels, no extra top labels | $\min\left\{N,sr,\binom{n}{p+1}-\binom{n-s}{p+1}\right\}$, $s=$ rank of vertex coefficient features |
| Failure of labeled $s$-faces and all cofaces | $\min\left\{N,r\binom{h+\binom{p}{s}}{\binom{p}{s}}\right\}$ |
| Compatible relative homology and zigzag sequences of allowed states | Same retained set; natural coordinate identifications commute with all supplied inclusions |
| Fixed signed cost order | Canonical minimum-cost basis for every surviving boundary matroid, including rank drops |

Safe vertices are represented by an extra never-failing color when using the one-color envelope. This exact prefix theorem is separate from the fixed-weight real spectral theorem in the [spectral family](../correlated-spectral-regression/).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
