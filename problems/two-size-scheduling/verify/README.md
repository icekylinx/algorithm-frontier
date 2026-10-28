# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md) and the following companion manuscripts:

- [Two-size polymatroid scheduling parameterized by the number of large units](../rank-parameter.md)

## Mathematical evidence

- The full physical-machine workload dual is formed before restricting candidate large recipients. Feasible targets supply exact small-unit promises.
- Deficient-set branching counts necessary omissions, includes its large-witness guard and handles one-unit exceptions.
- Zero extension, base completion and decomposition preserve all mandatory original jobs; target search uses sound failures without monotone success.
- The separate rank companion counts large units and proves its five-thirds regime, distinct from surplus-position corank.
- The [reference realization proof](../reference-realization.md) connects the
  shipped corank client to the actual hard-target batch algorithm and charges
  its complete-rank-table work and inherited high-target enumeration separately.

## Executable evidence

[check_corank.py](check_corank.py) compares the
[complete-table client](../reference/corank.py) with independent enumeration
of original small and large bases. It checks 408 finite instances, 3,789 targets
and 422 optimized outputs, including all target branches. Separate checks cover
400 box-rank support values, 2,390 full-ground dual-complement vectors and 295
binary base completions. The reached search has 599 augmented batch nodes and
18 candidate branches, including 78 omission guards and one rank-rejected child;
each target's count satisfies the exact algebraic batch bound. Six further
target/optimization checks use an 81-bit forced small count while replacing the
inherited high-target routine by an exception. This directly exercises binary
hard-path counts without constructing service copies or entering a numeric
count enumerator.

[verify_profile_certificates.py](../../../tools/verify_profile_certificates.py) checks the following finite claim:

The <code class="math">d=2</code> quota subcheck covers <code class="math">K=1,\ldots,399</code>: the exact one-unit gate for <code class="math">K\le2</code> and <code class="math">K/(K-\lceil K/2\rceil)\le3</code> for <code class="math">K&gt;2</code>. This is arithmetic evidence only; it does not execute support selection, branching or recovery. It does not test the separate five-thirds rank algorithm.

Run from the repository root:

```sh
python3 problems/two-size-scheduling/verify/check_corank.py
python3 tools/verify_profile_certificates.py
```

The new client executes the hard-target corank construction on complete rank
tables and reuses the canonical two-time LP baseline above the high-target
cutoff. Its table scans and inherited enumeration costs are stated in the
realization proof. It does not implement the fast whole-ground wrapper or the
separate large-unit-rank local search, nor mechanically verify their general
oracle approximation and running-time proofs.

## Model and verification boundaries

The profile arithmetic test supports only quota arithmetic. The independent
corank checker exercises full-ground duality, batch selection and binary base
completion on finite explicit tables; the inherited high-target solver has
its separately charged vertex and numeric count enumeration. The five-thirds
large-unit-rank algorithm and its fine-small-job/private-slack variants retain
their mathematical proofs rather than an executable local-search claim.
This family uses two common positive sizes and no assignment-cost budget.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** icekylinx and GPT-6 Astra Pro.
