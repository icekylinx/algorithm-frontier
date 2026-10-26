# Decremental strong forest and Gomory-Hu transfer

This is a conditional dynamic-graph transfer record, presented separately
from the fully dynamic APSP and spanner frontiers.

**Guarantee**

A strong decremental forest construction substituted into an exact deterministic Gomory-Hu reduction under the source's metric, forest, and fixed-parameter contracts.

**Objective and output**

Maintain the decremental strong-forest interface and use it to output the exact Gomory-Hu cut-tree representation named by the reduction.

**Randomness**

Deterministic conditional composition; the strong forest and exact Gomory-Hu transfer require the named deterministic hierarchy, flow, skeleton and guide-tree interfaces.

**Time**

The native decremental forest has total work $`(n+m)E_{6/7}`$. The separately preprocessed exact Gomory–Hu application has total work $`O(n+m)+(m+1)E_{6/7}`$ under its additional interfaces, where $`E_{6/7}=\exp(O(U^{6/7}h^{1/7}))`$.

**Space**

Polynomial in the maintained graph, forest certificates, and reduction state; no independent space exponent is claimed.

**Parameters**

$`n`$ is the vertex count; $`m`$ is the lifetime edge inventory; $`k`$ is the fixed reduction parameter; $`U`$ is the master logarithmic scale; $`h`$ is the iterated logarithmic scale used by the forest envelope.

**Model and representation**

The forest uses a fixed bounded-degree native graph, now allowing nonnegative polynomial-range integer lengths by the fixed perturbation in Section 14.1. Its flat projection may repeat physical edges. The Gomory–Hu application accepts arbitrary-degree undirected multigraphs with nonnegative polynomial-range integer capacities; zero-capacity edges and loops are removed in one scan. It retains the fixed-parameter reduction and named forest/flow interfaces.

**Lower-bound scope**

No lower bound is claimed. The page does not claim an independently implemented near-linear Gomory-Hu data structure.

**Review status**

**Ready for review in the stated scope.** The nonnegative-integer flat-forest adapter and zero-capacity Gomory–Hu preprocessing, with native-forest and cut-tree input costs stated separately.

**Conditions and remaining work.** The faster forest and exact-flow constructions retain the data-structure assumptions in sources.md. The local reductions do not supply those implementations or an additional simple-path reporting interface.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Complete theorem and proof](proof.md), [dependencies and primary sources](sources.md).

## Exact cut-tree output

The returned tree uses the original vertices. For every pair, the minimum edge weight along its tree path equals the exact minimum-cut value. Disconnected component trees are joined by zero-weight edges; graph loops do not affect cuts.

The reduction charges actual-size degree expansion, finite-precision multiplicative weights, the skeleton, fixed-$`k`$ guide families, contractions, and all flow calls. Their $`5/6`$ and $`4/5`$ overhead scales are absorbed by the stated $`6/7`$ factor. This is an application of the complete strong-forest contract, including occurrence and retirement accounting.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
