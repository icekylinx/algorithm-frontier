# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Prefix rank additivity and eager release for resource matroids](proof.md)
- [Exact realization of ordered resource reservations](resource-backend.md)

## Mathematical dependencies

- [Current blocker growth for matroid max-min allocation](../../manuscripts/allocation-and-scheduling/matroid-allocation-current-blocker-quasipolynomial.md)
- [Configuration-LP comparison for the player-matroid union reduction](../item-matroid-union/configuration-comparator.md)

## Executable evidence

The [ordered-reservation backend](reference/README.md) executes the resource
transitions. Its [independent checker](verify/check_reservations.py) enumerates
universal reservations, ordered prefixes, strong freedom and normalized rank
covers on finite represented inputs. It does not execute the complete allocator.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** icekylinx and GPT-6 Astra Pro.
