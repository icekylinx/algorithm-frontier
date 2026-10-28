# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Current blocker growth for independent transversals](proof.md)

## Mathematical dependencies

- [An elementary exponential fallback for the full transversal certificate](../../manuscripts/matching-and-routing/independent-transversal-elementary-exponential-fallback.md)
- [Input-linear scans for the independent-transversal layer primitives](../../manuscripts/matching-and-routing/independent-transversal-input-linear-iteration-implementation.md)

## Primary references

- [Graf--Haxell, *Finding Independent Transversals Efficiently*, arXiv:1811.02687v2](https://arxiv.org/html/1811.02687v2)

## Executable evidence

The [local realization proof](reference-realization.md) and
[reference API](reference/README.md) implement the elementary fallback with
positive blocker signatures. The code is a new local implementation of the
credited Graf--Haxell procedure; no third-party source code is included.
Its independent witness checker and finite execution audit are registered
separately from the full layer theorem.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** icekylinx and GPT-6 Astra Pro.
