# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md) and the following companion manuscripts:

- [Two-size polymatroid scheduling parameterized by the number of large units](../rank-parameter.md)

## Mathematical evidence

- The full physical-machine workload dual is formed before restricting candidate large recipients. Feasible targets supply exact small-unit promises.
- Deficient-set branching counts necessary omissions, includes its large-witness guard and handles one-unit exceptions.
- Zero extension, base completion and decomposition preserve all mandatory original jobs; target search uses sound failures without monotone success.
- The separate rank companion counts large units and proves its five-thirds regime, distinct from surplus-position corank.

## Executable evidence

[verify_profile_certificates.py](../../../tools/verify_profile_certificates.py) checks the following finite claim:

The <code class="math">d=2</code> quota subcheck covers <code class="math">K=1,\ldots,399</code>: the exact one-unit gate for <code class="math">K\le2</code> and <code class="math">K/(K-\lceil K/2\rceil)\le3</code> for <code class="math">K&gt;2</code>. This is arithmetic evidence only; it does not execute support selection, branching or recovery. It does not test the separate five-thirds rank algorithm.

Run from the repository root:

```sh
python3 tools/verify_profile_certificates.py
```

These programs do not implement the full algorithm or mechanically verify its oracle, approximation and running-time arguments.

## Model and verification boundaries

The finite quota test supports only the half-quota arithmetic in the corank routine. It does not test the five-thirds rank algorithm, duality or oracle recovery. This family uses two common positive sizes and no assignment-cost budget.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
