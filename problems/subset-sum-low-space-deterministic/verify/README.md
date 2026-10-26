# Verification of the low-space Subset Sum construction

The [main proof](../proof.md) supplies the deterministic extraction, modular
streaming, shared covers, ownership, interval processing and resource analysis.
The [short-range companion](../range-branch.md) proves its own restricted
input theorem. The programs below check the indicated parts of these arguments
with exact arithmetic.

| Program | Scope | Saved run |
|---|---|---|
| [Resource certificate](check_resources.py) | Rational entropy bounds, resource envelopes, preparation and live-state costs yielding the stated space exponent and time exponent 1/2 | [Receipt](space_resources_receipt.json) |
| [Structural identities](check_structural.py) | Finite ownership, association, image, cover, completion and layout identities, plus rational parameter checks | [Receipt](structural_receipt.json) |
| [Range identities](check_range_identities.py) | Exact quotient/residue identities, target-batch incidence and packed convolutions | [Receipt](range_identities_receipt.json) |

Run these commands from the repository root:

```sh
python3 problems/subset-sum-low-space-deterministic/verify/check_resources.py
python3 problems/subset-sum-low-space-deterministic/verify/check_structural.py
python3 problems/subset-sum-low-space-deterministic/verify/check_range_identities.py
```

The scripts use the Python standard library, require assertions, and do not
modify files unless `--output PATH</BT> is supplied. The committed receipts are
recorded outputs; rerunning the programs recomputes the claims they check.

The structural run checks 4,032 association cases, 19,456 image cases,
186 owner-cover cases, 369 owner-pair cases, 32,512 prefix completions,
354 cover doublings, 255 subset tests, 8,122 layouts and 17 rational
comparisons. The range run checks 592 configurations, 34,808 quotient
identities, 23,566 batch bounds and 340 convolutions.

These programs are not a full resource-bounded Subset Sum solver. Finite
identity checks do not establish arbitrary-input correctness, witness recovery
or bit complexity on their own. Those obligations remain mathematical proofs
in the manuscripts. The short-range improvement requires its two normalized
range assumptions; the third block and scale ratio remain unrestricted only
within that theorem's stated decomposition.

No proof-assistant verification or external peer review is claimed.
