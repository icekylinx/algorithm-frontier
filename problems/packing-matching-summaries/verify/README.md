# Verification and scope

[Main proof](../proof.md) · [Source dependencies](../sources.md)

## Evidence status

The support and replacement claims are proved through exterior algebra and the original resource representation. The [exact rational backend](../reference/README.md) now implements the product-feature construction, with a [realization proof](../manuscripts/reference-product-realization.md) covering input normalization, the dimension gate, private padding, row compression and bit accounting.

```sh
python3 problems/packing-matching-summaries/verify/check_product_summary.py
```

The independent checker passes 279 instances, including 85 nontrivial positive-feature constructions and 128 identity-gate cases. It checks 1,044 failure queries, 1,256 fixed-background contexts, 3,093 prescribed-cardinality optimum comparisons and 23,841 protected-item replacements. Eleven malformed-input cases are rejected. The remaining constructed cases are valid empty or rank-zero endpoints. A separate huge-budget fixture disables determinant computation to check that the identity gate performs no exterior work.

The comparator directly enumerates original item subsets and uses a separate rank routine on original resource and background columns. Fixtures include signed rational ties, empty supports, parallel matching edges, two independent label systems, loops in the resource matroid and rank-deficient ambient representations. Backgrounds may occupy extra dimensions or interact with the original positive flat. They are represented finite examples; the proof, rather than enumeration, establishes the guarantee for arbitrary later extensions, including nonrepresented extensions.

The implementation is rational only. The main manuscript's explicit finite-field construction remains a mathematical result, not an implemented field-extension API. The checker does not optimize a general later extension or establish historical priority.

## Feature dimension and bit complexity

At most <code class="math">p(K-1)+h_v</code> context coordinates must coexist with the <code class="math">p</code> coordinates of a protected item. Hence a Vandermonde ambient dimension of <code class="math">pK+h_v</code> is sufficient. Private never-failing padding keeps originally empty items distinct and prevents duplicate use. An oversized encoded upper bound <code class="math">p</code> is normalized to the actual maximum item size before padding.

For a padded universe <code class="math">U'</code>, a rational <code class="math">p</code>-minor has the conservative bit bound
<!-- math-display: 6d925f4c941a1f30eb05200f
O\!\left(p(pK+h_v)\log(|U'|+2)+p\log(p+2)\right)
-->
![Formula](../../../assets/math/6d925f4c941a1f30eb05200f.svg)
before the resource and label factors are included. The Vandermonde degree is part of this accounting. The retained-item dimension and the bit length of its entries are separate bounds.

## Original resource and later extensions

For an independent extension context <code class="math">T</code> and protected item <code class="math">e</code>, the set
<!-- math-display: 9c26d2158caed979c3c77590
A=E\cap\mathrm{cl}_{M^+}(T-e)
-->
![Formula](../../../assets/math/9c26d2158caed979c3c77590.svg)
is a flat of the original matroid and excludes <code class="math">e</code>. The supplied original linear representation yields a functional vanishing on that flat and nonzero on <code class="math">e</code>. Combining it with the packing and failure functionals yields a retained replacement outside the context closure.

The proof retains the full original resource rank and performs no context-dependent truncation. A later extension need not be represented, but its restriction to <code class="math">E</code> must equal the supplied resource matroid. Costs and their tie-breaking order are fixed at preprocessing. Original item or edge identities are retained whenever individual-identity failures are allowed.

**Attribution:** icekylinx and GPT-6 Astra Pro.
