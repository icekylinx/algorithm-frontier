# Independent audit of robust unit allocation with an additive low-quota boundary

**25 October 2026. Full independent read of RU1--RU8 and all eight sections: passes.**

This is the allocation-four audit of
`robust_unit_allocation_additive_and_promised_two.md`. The proof gives an
unconditional floor(K*/2) bound, the stronger ceil(K*/2) when K*>=2, and
an exact-factor-two guarantee for all compatible instances when an actual
feasible one-unit robust witness is supplied. These qualifications are
essential and correctly retained.

## 1. The common basis and adaptive allocations are distinguished

Each scenario has its own fractional count region, original resources,
costs and one assignment budget. All regions are downward and contain
zero. Checking every explicit scenario gives polynomial separation for
their intersection: a violated row from any one scenario is valid for
the intersection. Scenario count is part of the input size H.

The same selected M-basis is used in every scenario. Membership supplies
different allocation witnesses, as the model permits. Neither common
resource use nor a common assignment vector is inferred. Resource ranks
remain fixed when candidate players are omitted; only the queried service
vector changes.

## 2. Positive gaps and per-scenario integer recovery

For every integer K>=2, the weak quota b=ceil(K/2) is an integer and
K/(K-b)<=3. A robust full-K basis supplies the same protected selected
set for every possible separating scenario. Thus a changing supplier
of the violated row causes no difficulty: all rows belong to the fixed
intersection and preserve the same promised basis. The accepted
prefix-free proof gives the complete (27/4)^c bound, including failed
calls on unpromised targets.

After a success, fix the actual returned basis I. In each scenario
separately, reconstruct b-service, drop outside counts, and trim selected
totals to b. The integral maximum-total face of that scenario's resource
direct sum and partition quota polymatroid has total br. A minimum-cost
integer point costs no more than its fractional witness and supplies
exactly b units to every member of I.

The recovery does not change I between scenarios and loses no units.
Different cost budgets are safe because they apply to different adaptive
allocations. This is not a simultaneous multi-budget rounding claim for
one common integer vector.

## 3. The nominal-one branch and search are logically complete

At K=1, the algorithm returns an actual basis with zero allocation in
every scenario and declares a weak success, not a full-feasibility claim
and not a failure. Zero is legal under all nonnegative assignment costs
and budgets. This is the precise place where the theorem allows its
unconditional guarantee to vanish.

Every real search failure therefore occurs at K>=2 and excludes a robust
integer full target. The external upper endpoint U_0+1, with U_0 the
minimum scenario total-rank bound divided by r, stays strictly above K*.
At adjacent integer endpoints, the saved nominal L satisfies L>=K*.
If K*>=2, the saved success necessarily came from a positive-gap call
and guarantees ceil(L/2)>=ceil(K*/2). If K*<=1, its possibly zero output
is exactly the stated weaker guarantee.

This argument does not require monotonicity of successful gap calls or
a positive starting service. If U_0=0, the initialized zero solution
already suffices. Grid search has polynomially many calls even for
binary-sized resource ranks.

## 4. The supplied one-unit certificate fills only the missing case

An actual common basis with legal one-unit allocations in all scenarios
can be verified by matroid membership, resource separation, integer
count checks and budget evaluation. Retaining it as an additional output
candidate gives value one when K*=1. For K*>=2, the search output already
has the stronger ceiling guarantee. Thus taking the better actual
candidate proves exact factor two for all instances compatible with the
certificate.

The proof does not assume a polynomial or corank-FPT algorithm to find
that certificate. Invalid certificate data establish no stronger
guarantee. This distinction avoids the Hitting Set obstruction.

## 5. Global time, space and the negative companion

Under forced omissions Z, all original scenario data stay fixed and a
full basis avoiding Z remains a witness. The uniform extension time is
(27/4)^(c-|Z|) poly(H), so the accepted block wrapper gives base50/27
with the explicit subexponential overhead. The nominal-one zero-success
convention is unchanged by this replacement. Counts and allocations
remain binary encoded, and storing the explicit scenario witnesses uses
polynomial space.

The negative companion has integer optimum exactly one or zero. RU
allows output zero at both, so it does not decide those Hitting Set
instances. The high-quota promise removes the difficult positive
instances from the promised regime; an external unit certificate
instead supplies their missing feasibility information. There is no
unrestricted finite multiplicative corank theorem or whole-q lower
bound hidden in this composition.

**Disposition:** RU1--RU8 pass without substantive correction. The
positive theorem and the explicit robust-unit obstruction have
compatible scopes, and together isolate the exact one-unit selection
gate that cannot be imported from the single-scenario algorithm.
