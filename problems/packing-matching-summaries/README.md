# Universal packing and matching summaries

Failure-tolerant packing restrictions with exact fixed-cost replacement in the original context.

[Proof](proof.md) · [Sources](sources.md)

**Guarantee**

Retain at most $`\min\{N,D\}`$ items, where $`D=r\binom{pK+h_v}{p}\prod_j\binom{h_j+d_j}{d_j}`$. Omit $`r`$ without an extra resource matroid.

**Objective and output**

Preserve feasibility, prescribed positive cardinality up to $`K`$, and minimum fixed positive cost for every allowed failure and every fixed quota-free background in a later extension.

**Randomness**

Deterministic uniformly polynomial construction over the supplied rational or finite-field representation; no randomized representation, hashing or isolation step is assumed.

**Time**

Uniform deterministic polynomial preprocessing, gated before feature enumeration. Gaussian elimination uses $`O(ND^2)`$ field operations; padding, determinant features, label features, and rank compression are additional polynomial work.

**Space**

At most $`\min\{N,D\}`$ original item IDs. Tensor/exterior features and elimination workspace are separate. No solver runtime for an unspecified later extension is claimed.

**Parameters**

$`p`$ is actual item-support bound after normalization; $`K`$ is positive cardinality; $`h_v`$ is failed universe count; $`h_j,d_j`$ are label budgets/degrees; $`r`$ is the full represented resource rank.

**Model and representation**

Explicit packing sets, signed rational costs, and optional rational or finite-field represented resource columns. Later extensions may be arbitrary but must restrict to the original positive resource.

**Lower-bound scope**

Comparison with arbitrary-oracle packing bounds uses the stronger represented-resource input model. This is a size/replacement theorem, not a faster unrestricted matching algorithm.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Complete proof](proof.md) and [canonical manuscript map](sources.md).

## Results

**Packing with represented resource**

$`\min\left\{N,r\binom{pK+h_v}{p}\prod_j\binom{h_j+d_j}{d_j}\right\}`$

**Packing without resource constraint**

$`\min\left\{N,\binom{pK+h_v}{p}\prod_j\binom{h_j+d_j}{d_j}\right\}`$

**General multigraph matching, $`h_v`$ vertex and $`h_e`$ edge-ID failures**

$`\min\left\{m,(h_e+1)\binom{2K+h_v}{2}\right\}`$

**Matching with an additional represented resource**

Multiply the preceding bound by $`r`$, capped by $`m`$

**Matching with $`h_c`$ additional single-color risk groups**

$`\min\left\{m,r(h_e+1)(h_c+1)\binom{2K+h_v}{2}\right\}`$; omit $`r`$ when absent

Private dummy padding keeps empty packing sets distinct. Original edge IDs remain distinct when individual failures are allowed. Rational bit accounting includes the Vandermonde ambient degree $`pK+h_v`$.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
