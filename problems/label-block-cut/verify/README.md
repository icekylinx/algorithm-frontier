# Verification and scope

[Main proof](../proof.md) · [Source dependencies](../sources.md)

## Evidence status

The decoder and lower bounds are algebraic proofs. No dedicated executable currently checks the family-wide approximation or runtime statements. Enumerating a finite list of failure scenarios would not establish their universal quantifiers.

## Exact common-scalar decoder

For every original block column,
$$
CT_Fz_{e,j}=\gamma_F(S_e)a_{e,j}.
$$
The same scalar multiplies every column of that block, and its zero set is exactly the failed-label condition. Subspace membership therefore decodes independently of its nonzero magnitude.

The underlying polynomial identity is
$$
p_T(\theta(F))=\prod_{c\in T}q_F(\alpha_c),
$$
with the dummy-label factor equal to one. Ordinary monomial coefficients require no factorial division, so the identity holds in every characteristic.

Rank compression selects original rows and preserves their labels. It does not label an arbitrary linear combination of rows. The explicit finite-field extension preserves the original-field membership queries.

## Construction and failure models

The query class remains closed after each restriction. Conditional failure probabilities and approximation errors have summable budgets independent of the initial number of items. The feature-dimension gate returns the full input before constructing a lift that is too large.

Hyperedge failure deletes the whole incident item, and a partition objective counts a crossing item once. The quantum failure specialization requires globally commuting blocks and one common eigenbasis for every surviving instance. These are the stated models, not automatic consequences for arbitrary quantum deletions.

## Lower bounds

A block indexed by a $k$-subset of an $(h+k)$-label universe survives failure of its complement; every other indexed block contains a failed label. Thus each original block must separately satisfy the underlying cut lower bound.

That cut bound is proved directly from discrepancies, singleton degree inequalities, the $L_1$ Khintchine inequality, and Jensen's inequality. A spectral lower bound alone would not establish the claimed cut lower bound. The compact runtime follows from the dimension gate and explicit arithmetic interfaces, rather than an empirical timing experiment.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
