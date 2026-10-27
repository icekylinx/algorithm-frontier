# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md).

## Mathematical evidence

- An actual activation basis is fixed before profiling and rounding; profiles are counted on its <code class="math">r</code> active machines.
- Every original job-type total survives the inactive-machine masks. One maximum-total integral-intersection recovery preserves the combined setup and assignment cost.
- The feasibility gate tests resource feasibility as well as affordable activation, including empty jobs and zero processing times.
- The [reference realization proof](../reference-realization.md) proves the
  original-total active-coordinate restriction, binary greedy cost gate and
  actual joint profile adapter, with inherited finite solver costs separated.

## Executable evidence

[check_activation.py](check_activation.py) compares the
[reference adapter](../reference/activation.py) with independent enumeration of
original activation bases and original physical job schedules. It checks 72
finite instances, 216 exact feasibility results, 216 optimized outputs and 1,080
targets across all three methods. It checks 483 actual solver calls operate
on the activated rank of machines. Nine additional tests use an 81-bit job
count while disabling positive-target solver creation; exact feasibility,
zero load and optimization then execute the binary greedy gate alone.

The cases include cheap setups without mandatory capacity, expensive assignment
on a cheap setup, independently affordable pieces exceeding the combined budget,
rank-zero and nonuniform activation matroids, activation loops, empty jobs,
zero times and rational data.

[check_six_profiles.py](check_six_profiles.py) tests the direct original six-profile
model without activation: 29 instances, 145 targets, 29 optimizations, 4,176 fixed
profiles and 2,713 joint recoveries including 857 fractional witnesses. It checks
106 protected full-target profile vectors, six fixtures each fitting precisely
one intended profile and 24 open-left/closed-right endpoint cases. Original
rank constraints, counts, budgets and actual loads are checked independently.

[verify_profile_certificates.py](../../../tools/verify_profile_certificates.py) checks the following finite claim:

All 915 nondecreasing positive integer load multisets of total at most 16, including the empty multiset, normalized by 16, fit at least one of the six profiles; the five nontrivial rounded-load sums equal <code class="math">3/2</code>. The <code class="math">k=0</code> factor-two endpoint, ordered bucket intervals for <code class="math">k=1,\ldots,13</code>, and all 91 exact bucket load identities <code class="math">b_i+2(1-b_{i-1})=\gamma_k</code>. Activation and shared-cost recovery are outside this check.

Run from the repository root:

```sh
python3 problems/activated-machine-scheduling/verify/check_activation.py
python3 problems/activated-machine-scheduling/verify/check_six_profiles.py
python3 tools/verify_profile_certificates.py
```

The reference implements the actual semantic adapter and six-profile client
using the canonical complete-table LP/count solver. Its inherited enumeration
and vertex-storage costs remain charged separately from the theorem's paid
polynomial oracle primitives. Finite tests do not mechanically verify the
general oracle approximation and running-time proof.

## Model and verification boundaries

The arithmetic profile test concerns formulas within a fixed active set. The
new activation checker exercises actual basis enumeration, original-total
restriction and combined-cost recovery; the direct SX checker exercises
six-profile LPs and joint integer recovery. Profile-count/binary-accuracy tests
are supplied by the canonical arbitrary-processing checker. Positive-target
reference recovery still uses explicit vertex and numeric count enumeration,
so it does not attain the general theorem's per-profile time or workspace.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
