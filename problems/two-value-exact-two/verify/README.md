# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md).

## Mathematical evidence

- The affordable heavy-support parameter is defined by an actual compatible assignment, which the completion oracle returns with its true cost.
- A protected full allocation survives the changing heavy set and residual budget. Exact small-unit quotas incur no additive loss.
- The half-quota promise, pure-heavy and one-unit endpoints, loops, coloops and target search are covered separately.

## Executable evidence

[verify_profile_certificates.py](../../../tools/verify_profile_certificates.py) checks the following finite claim:

The <code class="math">d=2</code> quota subcheck covers <code class="math">K=1,\ldots,399</code>: the exact one-unit gate for <code class="math">K\le2</code> and <code class="math">K/(K-\lceil K/2\rceil)\le3</code> for <code class="math">K&gt;2</code>. This is arithmetic evidence only; it does not execute support selection, branching or recovery.

Run from the repository root:

```sh
python3 tools/verify_profile_certificates.py
```

These programs do not implement the full algorithm or mechanically verify its oracle, approximation and running-time arguments.

## Model and verification boundaries

Players are compulsory and each resource has a common intrinsic value from the two-value set. Player-dependent pair values with shared roles belong to the separate J2 theorem. Optional selection does not follow by adding a third-valued dummy.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** icekylinx and GPT-6 Astra Pro.
