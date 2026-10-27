# Verification and scoped internal review

[Statement](../README.md) · [Complete proof](../proof.md) · [Dependencies](../sources.md)

## What is ready for review

The conditional reduction, its three-transform root verifier, signed-moment
separation, complete prime-power extraction, Sidon second moments and packed
square-zero recovery have passed independent internal review. Reviewers also
read the actual external tensor theorem and checked its literal coefficient
ring, Boolean edge count, degree, succinct-entry, precision and space interface.
Correctness of that theorem remains the accepted premise. Its proof and
implementation are not certified by these local programs.

The direct one-fifth-exponent branch is preserved separately and is not a
prerequisite of this selected theorem. No publication-wide priority,
external peer review or proof-assistant verification is claimed.

## Original roots, moments, carries and transforms

```sh
python3 -B problems/integer-factorization/verify/check_root_moments.py
```

The checker enumerates roots and prime powers directly on 407 odd inputs,
including every odd integer from 3 through 801 and seven larger repeated-factor
or many-factor fixtures. It checks 1,620 digit-parameter cases, 605 prime-power
cases and 2,838 ordered prime-pair separations. Its streaming scans cover
965,207 saturated gcd candidates; 363 nonempty rough residuals also exercise
preprocessing and the residual prime-factor-count bound.

There are 27 literal first-moment ring evaluations, nine Sidon second-moment
evaluations across 21 root polynomials, and 50 independently checked Sidon
exponent sets. Twenty-one signed-carry and direct/grouped finite-field-transform
cases include perturbed-carry rejection. Another 592 exhaustive tiny input/quotient
assignments compare carry acceptance with the original root equation.
These tests use elementary original-input enumeration as their oracle, not the
external contraction algorithm or the asymptotic reduction's output.

## Square-zero algebra, packing and characteristic-two recovery

```sh
python3 -B problems/integer-factorization/verify/check_packed_recovery.py
```

Exact arithmetic in a small explicit field checks 256 square-zero identities,
512 binary regular-representation columns and 87 monotone integer-path cases.
All 2,517 distinct-root subsets of the 16-element field with at most four roots
are covered, including empty sets, zero roots and even cardinalities.
There are 22,653 guarded packing round trips and 2,516 nonempty Hankel/polynomial/
trace-splitting recoveries. An explicit one-bit unguarded packing fails because
of carries; the guarded construction succeeds. Thirty-two characteristic-two
Cauchy half-grid matrices each have rank eight. That last test concerns the
full-grid template only and implies no general factoring lower bound.

The field is deliberately tiny and the checker does not construct the general
linear-edge network, a large field tower or the external fast contraction
backend. Finite identities supplement the symbolic parameter and recovery
proofs; they do not establish asymptotic complexity by experiment.

## Source import identities and language

```sh
python3 -B problems/integer-factorization/verify/check_import.py
```

The [import record](../../../provenance/imports/integer-factorization.json) maps
all 31 members of the two supplied archives: 19 retained members map to
18 canonical English targets, while 12 excluded members have no retained text.
When the original local ZIPs are present, the checker replays their bytes,
archive hashes, exact member inventories and member hashes. CI checks metadata,
target existence, source-identity headers, attribution and language without
requiring the ignored binary archives. Current proofs may be edited; source
hashes are provenance and do not freeze current text or validate mathematics.
The Chinese summary is integrated in the English research overview.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
