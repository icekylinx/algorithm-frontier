# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md).

## Mathematical evidence

- Masks preserve each original mandatory amount and machine classes inherit a full-target witness.
- Exact small-quota gates and scaled support coordinates supply the heterogeneous omission inequality.
- All machine classes share one maximum-total integral recovery and assignment-cost objective. A disjoint modular zero-time block and a zero-target gate handle zero processing times.
- The [explicit-table realization proof](../reference-realization.md) discharges
  exact bounded LP, normalized support, integer recovery and target-search
  contracts with their actual enumeration costs.

## Executable evidence

[check_scheduling.py](check_scheduling.py) exercises the
[complete-table backend](../reference/scheduling.py) against an independent oracle
that enumerates original integer pair counts and checks every rank inequality,
mandatory type total, cost and load. Target failures must exclude all original
target schedules; successes and optimized outputs must satisfy the approximation
and exact budget. It also checks weak LP vertices' joint recovery, normalized
service rows, unequal-quota scaling, protected omission inequalities, zero-time
costs, target masks and every machine class. The fixed suite covers 64 instances,
1,728 target checks, 192 optimization checks, 1,478 joint recoveries (including
402 fractional witnesses), four strict support rows and 1,029 protected nodes.
Tests include one-, two- and three-machine instances. These finite checks support the
explicit-table baseline, whose enumeration costs differ from Theorem HT.

[verify_profile_certificates.py](../../../tools/verify_profile_certificates.py) checks the following finite claim:

Integer-quota arithmetic: <code class="math">d=2,\ldots,30</code> and every <code class="math">d&lt;K\le399</code> (11,107 cases) satisfy <code class="math">K/(K-\lceil K/d\rceil)\le(d+1)/(d-1)</code>; every <code class="math">1\le K\le d</code> satisfies the one-unit gate. Selection, budgets, rank oracles and rounding are not executed. Target-dependent masks and zero-time feasibility are not tested.

Run from the repository root:

```sh
python3 problems/two-time-scheduling/verify/check_scheduling.py
python3 tools/verify_profile_certificates.py
```

The reference backend implements the semantic interfaces with explicit-table
enumeration. It does not implement the fast omission/global-cover algorithm or
mechanically verify the general-oracle approximation and running-time proof.

## Model and verification boundaries

Each machine has at most two positive eligible times; the pair may differ across machines and zero times are allowed. The tradeoff parameter <code class="math">d</code> is a fixed integer at least two.
The profile arithmetic test does not verify masks, zero-time feasibility or cost
recovery; the independent scheduling checker exercises those operations on its
finite inputs. Complete-table enumeration does not provide the fast theorem's
binary-input or polynomial-workspace implementation.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** icekylinx and GPT-6 Astra Pro.
