# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md).

## Mathematical evidence

- The bucket endpoints and their open/closed intervals cover every normalized full-target load.
- Upper-prefix ceilings define an integral machine polymatroid; its intersection with the masked resource direct sum retains all mandatory totals and a single exact-cost recovery point.
- Every successful label LP produces the stated load, while full-target failures are sound. Zero times and the polynomial endpoint have explicit branches.
- The [reference realization proof](../reference-realization.md) identifies the
  bucket client's exact masks and one shared original-total plan solver, with
  its actual finite solver costs.

## Executable evidence

[check_buckets.py](check_buckets.py) exercises the
[complete-table bucket client](../reference/buckets.py) against the independent
original-pair schedule oracle shared by the profile checker. It covers 24 finite
instances, 360 target calls, 72 optimizations, 1,400 fixed label LPs and 1,208 joint
recoveries including 383 fractional witnesses. Actual original type ranks,
mandatory totals, costs and loads are checked without using backend constraints.
It also constructs 267 protected label vectors from full-target schedules and
checks their LPs, and checks 63 open-left/closed-right endpoint cases.

[verify_profile_certificates.py](../../../tools/verify_profile_certificates.py) checks the following finite claim:

The <code class="math">k=0</code> factor-two endpoint, ordered bucket intervals for <code class="math">k=1,\ldots,13</code>, and all 91 exact bucket load identities <code class="math">b_i+2(1-b_{i-1})=\gamma_k</code>. Arbitrary depths and exact-cost LP recovery remain symbolic.

Run from the repository root:

```sh
python3 problems/processing-bucket-tradeoff/verify/check_buckets.py
python3 tools/verify_profile_certificates.py
```

The client implements the semantic bucket/rounding construction using the
explicit-table LP/count baseline. Its vertex and numeric count enumeration costs
are charged separately from the theorem's paid polynomial primitives; finite
checks do not mechanically verify the general oracle proof.

## Model and verification boundaries

The profile arithmetic checker verifies bucket identities. The new independent
schedule checker exercises resource feasibility and exact-budget recovery on its
finite complete-table inputs. The reference solver may store exponentially many
vertices and enumerate numeric counts, so its implementation does not attain
the theorem's per-label time or workspace. The theorem retains arbitrary
nonnegative machine-type times, binary multiplicities and the
<code class="math">(k+1)^q</code> enumeration factor.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
