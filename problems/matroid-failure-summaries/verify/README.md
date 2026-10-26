# Verification and scope

[Main proof](../proof.md) · [Source dependencies](../sources.md)

## Evidence status

The family is supported by the written algebraic and combinatorial proofs. No dedicated executable currently checks its universal failure guarantees, arbitrary-matroid oracle construction, or asymptotic size bounds. Repository syntax and link checks do not establish those mathematical claims.

## Represented fixed-cost theorem

For an item with at most $d$ labels, the coefficient feature consists of all monomials of total degree at most $h$ in its degree-$d$ label-polynomial coefficients. Its dimension is $\binom{h+d}{d}$. The query functional vanishes exactly on failed items.

The greedy relation uses earlier retained columns. Applying the query functional to that relation preserves every surviving prefix span, hence the canonical minimum-cost basis for the fixed order, including signed costs and rank drops. It is the prefix relation, rather than rank equality at only the final prefix, that supplies the cost guarantee.

The dimension gate is applied before feature enumeration. Small finite fields use an explicit field extension; rank over the original field is unchanged by extension. Later matroid extensions are handled using original-matroid closure. They need not be represented, but must restrict to the original resource matroid.

## Arbitrary-matroid and submodular boundaries

The sharp arbitrary-matroid bound uses a coloop witness in the entire surviving restriction. A cheaper-prefix nonclosure witness would not justify the circuit-blocking permutation proof. Consequently, the final deletion step preserves rank and feasibility; it does not inherit the represented theorem's arbitrary fixed-cost-prefix guarantee.

Separating pools preserve every query closure. Rebuilding their hash family after a reduction is valid because labels absent from the current ground set have no effect. The fixed-parameter bounds depend on $r+h+d$, or on $R+h+d$ for integral-submodular values. Here $R$ is the numerical value range, not its binary encoding length.

The real-valued marginal and entropy results require no integrality. They are inequalities and do not assert a small exact cardinality summary in those models.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
