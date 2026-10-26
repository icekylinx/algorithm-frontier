# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md).

## Mathematical evidence

- The bucket endpoints and their open/closed intervals cover every normalized full-target load.
- Upper-prefix ceilings define an integral machine polymatroid; its intersection with the masked resource direct sum retains all mandatory totals and a single exact-cost recovery point.
- Every successful label LP produces the stated load, while full-target failures are sound. Zero times and the polynomial endpoint have explicit branches.

## Executable evidence

[verify_profile_certificates.py](../../../tools/verify_profile_certificates.py) checks the following finite claim:

The k=0 factor-two endpoint, ordered bucket intervals for k=1,...,13, and all 91 exact bucket load identities b_i+2(1-b_(i-1))=gamma_k. Arbitrary depths and exact-cost LP recovery remain symbolic.

Run from the repository root:

```sh
python3 tools/verify_profile_certificates.py
```

These programs do not implement the full algorithm or mechanically verify its oracle, approximation and running-time arguments.

## Model and verification boundaries

The finite checker verifies bucket identities, not general polymatroid feasibility or exact-budget rounding. The theorem retains arbitrary nonnegative machine-type times, binary multiplicities and the (k+1)^q enumeration factor.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
