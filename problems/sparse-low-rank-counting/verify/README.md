# Finite verification and its limits

[Statement](../README.md) · [Proof](../proof.md) · [Dependencies](../sources.md)

Run from the repository root with the Python standard library:

```sh
python3 -B problems/sparse-low-rank-counting/verify/check_core.py
python3 -B problems/sparse-low-rank-counting/verify/check_hypermatching.py
```

The deterministic 2 November 2026 runs pass **3,516 exact assertions**.
Reports are saved next to the checkers. The seeded input generation is a
reproducible finite test selection; the mathematical algorithms themselves
are deterministic and require no randomness.

`check_core.py` passes 2,148 assertions:

- 112 integer permanent identities, 560 modular identities and 224 prime-characteristic truncation identities.
- 120 integer hafnian/monomer identities and 600 modular identities.
- 381 two-state chain tensor identities, enumerating every incident bit pattern through degree six and all hidden states, for three signed/zero monomer values.
- 112 signed modular reconstructions.
- 15 rational permanent, 12 rational hafnian and 12 rational fixed-monomer modular lifts. Independent dense Fraction-valued outputs are compared with denominator clearing, factor-based output bounds, power-of-two evaluation and signed recovery.

Permanent dimensions range from zero to six with widths zero to three.
Hafnian sizes range over zero, two, four, six and eight. Modular tests use
2, 3, 4, 6 and 101; composite moduli exercise the absence of field-only
division. Zero width, empty instances, signed factors and arbitrary symmetric
cores are included.

`check_hypermatching.py` passes 1,368 assertions: 108 integer and 540 modular
symmetric-core identities, 90 integer and 450 modular partite identities,
and 180 prime-characteristic truncation identities. Symmetric uniformities
are two, three and four, through two blocks and width three. Partite cases
have two or three parts, sizes zero through four and widths zero through two.
Repeated color labels in a core are included.

These tests compare the moment reductions with independent permutation or
matching enumeration. The reference recurrences implement the finite
coefficient identities, using direct subset enumeration in place of the
fast contraction backend. They do not implement, benchmark or establish
the external quantitative recursion, its asymptotic exponent, the general
integral coefficient theorem, or historical priority. The complete local
mathematical arguments and source boundaries are in the proof companions.
No external peer review or proof-assistant verification is claimed.

**Attribution:** icekylinx and GPT-6 Astra Pro. Apache-2.0.
