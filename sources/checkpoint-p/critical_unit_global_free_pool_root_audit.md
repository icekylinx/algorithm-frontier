# Root audit of the critical-quota global free pool

**25 October 2026. Structural result accepted; runtime gate remains open.**

The root reviewer read F1--F5 and the exchange discussion in
`critical_unit_quota_global_free_pool.md`. The structural inequalities
and the paid acceleration pass. They do not establish polynomial or
rank-quasipolynomial time for the four-unit to two-unit promise.

Prefix rank additivity for the complete ordered prefix says the
unmarked matching copies are independent after contracting X union Y.
Thus their exact additional rank is b times the number of unmarked
records. Combining this identity with the current unit cover
`Phi <= (2b-1)|Y|` gives

\[
 \Psi\le(2b-1)k-(b-1)u_0,
\]

where k is the current matching size and u0 its unmarked record count.

Any promised optimum player that is not globally b-free retains at
most b-1 units after the full current reserve is contracted. With
t target units it loses at least d=t-b+1. The contraction-loss bound
pays all such losses by Psi. An optimum player basis consequently
has at most floor(Psi/d) members outside the free set, proving the
rank lower bound F3. The support bound for the residual-LP version
also holds: current matching and selected records use at most 2k
owners, with k<=r-1.

At t=3b-2, d=2b-1 and the free owners have rank at least r-k.
If all were in the span of the unmarked owners, an optimum basis
could have at most u0 free members. Comparing the resulting lower
loss `d(r-u0)` with the displayed upper bound gives a contradiction
precisely when `u0 < (2-1/b)(r-k)`, as in F5.

A globally strongly free owner outside that unmarked span either
augments immediately or has a fundamental player circuit containing
a marked record. Processing it after the whole stack and applying
the ordinary earliest marked exchange preserves the existing resource
and player invariants. It decreases the established signature and
adds only a polynomial player scan per state.

If all free owners lie in the unmarked span, their exchanges can
preserve resource feasibility but leave every signature count fixed.
The note correctly leaves this case unresolved. Marking an incoming
record would change old eligibility and require a new maximality
repair proof; retaining historical resource copies would require a
new rank charge. Neither operation is treated as free progress.

The structural result is therefore accepted as an acceleration and
a more precise obstruction statement. It does not alter the existing
rank-exponential upper bound, and generic exact parity hardness is
not used as a lower bound for the four-to-two promise.
