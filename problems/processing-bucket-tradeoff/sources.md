# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Arbitrary unrelated processing times: a bucket-label scheduling tradeoff](proof.md)
- [Exact complete-table bucket realization](reference-realization.md)

## Mathematical dependencies

The model-specific reductions and inequalities are proved in the canonical manuscripts. Standard rank-oracle, linear-programming and integral-intersection interfaces are stated where they are used; an internal review label is not an additional mathematical premise.

The shipped client imports the
[shared general-processing joint plan realization](../arbitrary-processing-scheduling/reference-realization.md),
which reuses the canonical two-time exact-table LP and count primitives.

## Primary references

- [Shmoys and Tardos, An approximation algorithm for the generalized assignment problem (1993)](https://link.springer.com/article/10.1007/BF01585178)

## Executable evidence

- [Bucket client](reference/buckets.py) and
  [independent original-schedule checker](verify/check_buckets.py): 24 finite
  instances, 360 targets, 72 optimizations, 1,400 fixed labels, 1,208 joint
  recoveries including 383 fractional witnesses, 267 protected full-target
  labels and 63 interval endpoint cases. Actual original ranks, type totals,
  costs and loads are checked independently of the LP implementation.

- [verify_profile_certificates.py](../../tools/verify_profile_certificates.py): The <code class="math">k=0</code> factor-two endpoint, ordered bucket intervals for <code class="math">k=1,\ldots,13</code>, and all 91 exact bucket load identities <code class="math">b_i+2(1-b_{i-1})=\gamma_k</code>. Arbitrary depths and exact-cost LP recovery remain symbolic.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** icekylinx and GPT-6 Astra Pro.
