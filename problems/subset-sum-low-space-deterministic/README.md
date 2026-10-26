# Deterministic Subset Sum: writable-space bound

**Objective and output**

Exact YES/NO decision and the selected input indices for arbitrary signed binary integers, including zeros and repeated weights.

**Randomness**

Deterministic exact algorithm in the uniform bit model, including indexed-witness recovery; the writable-space and restricted-range variants have no probability of error.

**Time**

$`\mathrm{poly}(n,L)2^{n/2}`$ bit operations.

**Space**

$`\mathrm{poly}(n,L)2^{E_Sn}`$ writable bits, where $`E_S=18261635770550353/10^{17}=0.18261635770550353`$. Read-only input storage is excluded.

**Parameters**

$`n`$ is the number of weights. $`L`$ includes every input bit, including the target, signs and delimiters. Polynomial degrees are fixed.

**Model and representation**

Uniform deterministic bit model, bounded-storage generation and indexed witness recovery.

**Lower-bound scope**

No lower bound is claimed.

**Review status**

**Ready for review in the stated scope.** The two-short-range theorem, including signed-input normalization, nested residue streams, indexed witnesses, and the self-contained exact Boolean convolution lemma. The general low-space ledger now explicitly charges the one-bit deficiency-proxy loss.

**Conditions and remaining work.** The stronger n/6 space exponent requires the supplied three-block partition and its two short normalized ranges. The general 0.18261635770550353-space theorem is a separate algorithm; finite range tests do not verify its full storage schedule.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Theorem and complete proof](proof.md), [source and verification index](sources.md), [import notice](NOTICE.md).

The resource certificate is [check_resources.py](verify/check_resources.py). Its exact rational and integer comparisons accompany the proof's analytic reductions. The [structural check](verify/check_structural.py) covers the finite ownership and layout identities stated in its documentation.

This algorithm has its own construction. Its writable-space guarantee is not attached to the separate [faster-time theorem](../subset-sum-fast-deterministic/).

The [dependency map](sources.md) identifies where the required extraction,
cover, projection, stream and bit-cost statements are proved internally.

## Two short normalized ranges

For a supplied partition into three blocks of size at most $`m`$, put $`N=2^m`$. Suppose two blocks have normalized sum ranges $`W_A,W_B`$, at arbitrary positive lattice scales. For $`C^2\ge\max\{N,W_A+1,W_B+1\}`$, the [range theorem](range-branch.md) gives

```math
T=O^*(NC+C^3),\qquad S=O^*(C+\sqrt N).
```

Thus $`W_A,W_B\le O^*(2^m)`$ and $`n=3m+O(1)`$ give $`O^*(2^{n/2})`$ time and $`O^*(2^{n/6})`$ writable space. The third block and the ratio of lattice scales are unrestricted. The $`O^*`$ notation hides fixed polynomial factors in the full binary input; this is a detectable restricted-input result, separate from the general theorem.

The range theorem's [convolution lemma](convolution.md) proves its required
bit-time and space bounds using elementary deterministic arithmetic.
A [complete finite reference check](verify/check_range_solver.py)
compares both scale regimes and original indexed witnesses with exhaustive
search.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
