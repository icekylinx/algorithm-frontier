# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md).

## Mathematical evidence

- An actual activation basis is fixed before profiling and rounding; profiles are counted on its <code class="math">r</code> active machines.
- Every original job-type total survives the inactive-machine masks. One maximum-total integral-intersection recovery preserves the combined setup and assignment cost.
- The feasibility gate tests resource feasibility as well as affordable activation, including empty jobs and zero processing times.

## Executable evidence

[verify_profile_certificates.py](../../../tools/verify_profile_certificates.py) checks the following finite claim:

All 915 nondecreasing positive integer load multisets of total at most 16, including the empty multiset, normalized by 16, fit at least one of the six profiles; the five nontrivial rounded-load sums equal <code class="math">3/2</code>. The <code class="math">k=0</code> factor-two endpoint, ordered bucket intervals for <code class="math">k=1,\ldots,13</code>, and all 91 exact bucket load identities <code class="math">b_i+2(1-b_{i-1})=\gamma_k</code>. Activation and shared-cost recovery are outside this check.

Run from the repository root:

```sh
python3 tools/verify_profile_certificates.py
```

These programs do not implement the full algorithm or mechanically verify its oracle, approximation and running-time arguments.

## Model and verification boundaries

The finite evidence concerns the six-profile and bucket formulas within a fixed active set. It does not enumerate activation bases, test the approximation-scheme profile count, or implement exact-cost recovery.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
