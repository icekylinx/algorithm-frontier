# Finite exact reference reductions

[Proof](../proof.md) · [Verification](../verify/README.md)

`reductions.py` computes the sparse matching polynomial by subset/matching
recurrences, then applies the permanent factorial or hafnian core moment
functional. `hypermatching.py` supplies the symmetric-core and partite
analogues with independent direct enumeration routines. All computations use
Python integers; optional moduli in the matrix routines include composite
rings. The code accepts explicit factor arrays, including zero width.

These routines implement the finite algebraic reductions for general finite
inputs. They use exponential enumeration in the matrix dimension and do not
implement or benchmark the cited subexponential contraction backend. The
asymptotic algorithm is the source recursion composed with the proved finite
coefficient representation. Reading small-instance timings as that algorithm's
performance would be incorrect.

No third-party dependencies are needed. Empty outputs follow the convention
that the empty permanent, hafnian and hypermatching sum are one.

**Attribution:** icekylinx and GPT-6 Astra Pro. Apache-2.0.
