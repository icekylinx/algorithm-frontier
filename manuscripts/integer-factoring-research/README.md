# Integer factorization research branches

[Selected conditional theorem](../../problems/integer-factorization/) · [Full conditional proof](../../problems/integer-factorization/proof.md) · [Import record](../../provenance/imports/integer-factorization.json)

This English overview integrates the retained parts of the two supplied source summaries. The later archive contains increments only; no missing intermediate stages are inferred. Material outside the current collection scope is excluded, with only original source identities retained in import metadata.

<!-- integrated-source: checkpoint_10_README_zh.txt; sha256=8a90af74a0973b47e5768c6cfba04145d986e8256f68352ebae19ba921793f40 -->
<!-- integrated-source: checkpoint_13_README_en.txt; sha256=73d1fdffa19122986d5d37a4530ea23ef7b22f1bb419024bc70f2f6007f94d2e -->

## Selected deterministic conclusion

Assuming the explicitly cited Boolean tensor-contraction theorem, the reviewed reduction completely factors every positive integer in deterministic subpolynomial time in its numerical value and polynomial space in its bit length. The later increment obtains complete recovery from at most one contraction and improves precision/recovery tradeoffs. It preserves the original leading exponent. The result card and proof display the exact bounds.

The selected theorem has no semiprime balance or squarefree-input promise. Its external theorem is accepted as a premise and is not proved by local finite tests.

## Separate direct deterministic branch

The retained source package also develops the unconditional candidate

```text
O(N^(1/5) * (log N)^(13/5) / (log log N)^(9/10)).
```

The power remains one fifth. Its content-sensitive hyperbola cover, CRT sign tries, output-sensitive preprocessing, geometric batches and amortized short-period recovery are preserved below. This import does not newly certify that entire independent proof chain or its publication priority. The numerical bound is retained as a candidate branch, not substituted for the stronger conditional theorem.

## Canonical retained manuscripts

Original mathematics is retained with indentation converted into copyable code blocks, section headings and current attribution. The selected proof presents its main formulas as bound SVGs. The table maps source topics to semantic canonical paths.

| Source topic | Canonical text | Review role |
|---|---|---|
| CONTENT-SENSITIVE HYPERBOLA COVER FOR GENERAL DETERMINISTIC FACTORING | [Manuscript](content-hyperbola-sieve.md) | Retained direct branch; outside selected-theorem review |
| CRT SIGN TRIES IN THE HARVEY--HITTMEIR FACTORING SEARCH | [Manuscript](crt-trie-hh-log-saving.md) | Retained direct branch; outside selected-theorem review |
| DETERMINISTIC RECOVERY FROM ONE PERIOD: AMORTIZED VERSION | [Manuscript](deterministic-period-recovery-amortized.md) | Retained direct branch; outside selected-theorem review |
| CRT SIGN-CUBE PREPROCESSING AND ZERO-FREE AUDIT | [Manuscript](crt-preprocessing-audit.md) | Retained direct branch; outside selected-theorem review |
| AGGREGATED GEOMETRIC COLLISIONS IN THE HARVEY--HITTMEIR SEARCH | [Manuscript](aggregated-hh-log-saving.md) | Retained direct branch; outside selected-theorem review |
| Saturation of the current small-modulus content-cover count | [Manuscript](content-sieve-saturation-addendum.md) | Retained direct branch; outside selected-theorem review |
| Large two-power modulus: a globally uncentered coefficient cover | [Manuscript](large-two-power-uncentered-cover.md) | Retained direct branch; outside selected-theorem review |
| An explicit power-saving gate for the uncentered conic cover | [Manuscript](implicit-conic-kernel-gate.md) | Retained direct branch; outside selected-theorem review |
| FACTORING OR SHORTENING A PERIOD WITH A KNOWN FACTORED COFACTOR | [Manuscript](factored-period-cofactor.md) | Retained direct branch; outside selected-theorem review |
| RAGGED GEOMETRIC PREFIX PRODUCTS | [Manuscript](ragged-geometric-products.md) | Retained direct branch; outside selected-theorem review |
| CONDITIONAL GENERAL FACTORING FROM A SUCCINCT BOOLEAN TENSOR THEOREM | [Manuscript](../../problems/integer-factorization/manuscripts/conditional-tensor-fft-factoring.md) | Reviewed conditional interface or extraction |
| AP supercovers and shared q-factorial batches for thickened quadratics | [Manuscript](ap-supercover-batch-obstruction.md) | Retained direct branch; outside selected-theorem review |
| Stable finite algebra carriers for the quadratic phase | [Manuscript](implicit-norm-carrier-obstruction.md) | Retained direct branch; outside selected-theorem review |
| ONE CONTRACTION FOR COMPLETE DETERMINISTIC INTEGER FACTORIZATION | [Manuscript](../../problems/integer-factorization/manuscripts/one-contraction-complete-factoring.md) | Reviewed conditional interface or extraction |
| ONE LITERAL-RING CONTRACTION AT SQUARE-ROOT PRECISION | [Manuscript](../../problems/integer-factorization/manuscripts/sidon-second-moment-factoring.md) | Reviewed conditional interface or extraction |
| ONE LITERAL-RING CONTRACTION WITH SUBPOLYNOMIAL PRECISION | [Manuscript](../../problems/integer-factorization/manuscripts/packed-square-zero-prony-factoring.md) | Reviewed conditional interface or extraction |
| THREE LIMITS OF DIRECT TENSOR-CONTRACTION RETUNING | [Manuscript](../../problems/integer-factorization/manuscripts/tensor-parameter-and-char2-obstructions.md) | Reviewed limitations of named templates |

**Attribution:** icekylinx and GPT-6 Astra Pro.
