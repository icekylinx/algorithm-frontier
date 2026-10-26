# A global free-pool lemma at the critical unit quota

**25 October 2026. New structural lemma and a paid acceleration; the small-quota time gate remains open.**

This note studies the unresolved promise problem: a player basis can
receive four unit-value services each; construct a basis receiving two
each in rank-quasipolynomial or polynomial time. It does not attempt to
change the general-graph maximum-matching exponent.

The existing normalized prefix algorithm already solves that promise
in 2^{O(r)}poly(H). The results below show that a completed normalized
state always has a substantial pool of globally resource-free owners.
The remaining obstacle is the player-side eligibility and the cost of
exchanging with an unmarked player record.

## 1. The exact full-reservation rank identity

Use equal unit values, an integer output quota b>=1, an exact available
optimizer, and a rank-r player matroid. Every current matching and
selected record has exactly b units. Let k<r be the current matching
size, X the selected records, and Y their disjoint designated groups.
Consider a fully normalized state of the prefix algorithm.

For each resource j, let W_j=X_j union Y_j be its reserved copy set,
and U_j=M_j minus Y_j the unmarked matching copies. Define

```math
\Phi=\sum_j r_j(W_j),\qquad
 \Psi=\sum_j r_j(M_j\cup X_j).
```

Prefix rank additivity for the full selected prefix gives

```math
\Psi=\Phi+\sum_j|U_j|
                     =\Phi+b(k-|Y|).
 \tag{F1}
```

The equal-unit current cover is Phi<=(2b-1)|Y|. Hence

```math
\boxed{\Psi\le bk+(b-1)|Y|\le(2b-1)k.}
 \tag{F2}
```

This is stronger than merely counting all b(k+|X|) service units of
M union X. It uses the current prefix invariant, not a birth charge.

## 2. A large rank of globally strongly free owners

Compute availability after contracting the full M_j union X_j at every
resource. A player is globally strongly free if its exact local
available optimizer can produce b units under these residual caps.
Let F be the set of these players. A produced bundle is independent
over the actual matching and every selected record simultaneously.
All capacities and tests remain compressed natural-matroid rank queries.

Suppose an integral target basis I* can receive at least t units each,
and write d=t-b+1>0. Apply the contraction-loss lemma to the resource
sets M_j union X_j and the allocation of the players in I* minus F.
Every such player has available optimum at most b-1, so it loses at
least d units when restricted to these capacities. At most Psi units
can be lost in total. Therefore

```math
|I^*\setminus F|\le\left\lfloor\frac\Psi d\right\rfloor,
 \qquad
 r_M(F)\ge r-\left\lfloor\frac\Psi d\right\rfloor.
 \tag{F3}
```

The same rank conclusion holds against the residual-capacity
configuration relaxation: its cuts applied to bases of M_j union X_j
give d x(P minus F)<=Psi, and x(F)<=r_M(F). Those reserve bases have
at most 2(r-1) owners, so the already sufficient bounded-support cuts
cover this application too.

At the critical integer target t=3b-2, one has d=2b-1. Combining
(F2)--(F3) yields

```math
r_M(F)\ge r-k.
 \tag{F4}
```

In particular, for t=4 and b=2 there is always a globally strongly
free candidate while k<r. Its owner need not lie outside the current
matching's player span, which is the important qualification.

## 3. A global free candidate can safely accelerate some exchanges

Let U be the set of owners of unmarked matching records, with
u_0=|U|=k-|Y|. Suppose a globally strongly free owner p lies outside
cl_M(U). If p lies outside cl_M(I), augment immediately. Otherwise,
its fundamental player circuit meets Y. If p is already matched, its
own record belongs to Y, since an unmarked owner would lie in cl_M(U).

In either case, view the free candidate as found in a virtual layer
after the entire current stack. Choose the usual earliest marked
exchange layer. Every retained center precedes the candidate, and the
whole incoming bundle is already independent over the old M plus all
X. Thus all resource reservations, prefix additivity, record identities
and old eligibility/maximality arguments apply without change.

The operation is an ordinary strict micro-signature decrease: X is
unchanged in the earliest retained layer, one Y record is removed,
and higher layers are truncated. There is no need to append or
complete the virtual layer, since no selected record is stored there.
Scanning all players for such global candidates between other charged
actions costs polynomial work per state and is safe. An actual
augmentation ends the phase. This is a paid deterministic acceleration,
not yet an improved global asymptotic bound.

## 4. A quantitative condition forces an eligible global free owner

If F were contained in cl_M(U), an optimal basis would have at most
u_0 members in F. Hence at least r-u_0 optimal players would each lose
d units. This implies Psi>=d(r-u_0).

At the critical target, (F2) can be rewritten as

```math
\Psi\le(2b-1)k-(b-1)u_0.
```

Writing delta=r-k>0, these inequalities contradict each other whenever

```math
u_0<(2-1/b)\,\delta.
 \tag{F5}
```

Thus (F5) guarantees either augmentation or the safe marked exchange
in Section 3. For b=2 and delta=1, zero or one unmarked matching
record is enough to force such an exchange. If k<r/2, (F4) also
implies that F cannot be contained in cl_M(I), so direct augmentation
is available in that early part of a phase sequence.

These are structural consequences of the actual target promise. They
are not used to issue a false infeasibility certificate when the
promise does not hold.

## 5. Why arbitrary unmarked exchanges do not yet close the gate

The remaining possibility is that the globally free pool lies inside
cl_M(U). A free bundle can then replace a matching owner in its
fundamental circuit among unmarked records. Such an exchange can
preserve actual resource feasibility, every old reserved set, and
the old player eligibility flats. However, it removes no Y record
and changes no X count. The existing signature does not decrease.
No bound on the number of these exchanges has been proved.

Marking the incoming record in an old designated group is not a free
fix. Strong resource freedom would preserve the resource rank
invariants, but the corresponding player eligibility base loses a
previously unmarked direction. Newly eligible players must be scanned,
so earlier maximality can no longer be inherited literally. A new
repair/progress argument would be needed.

Keeping all released old resource copies as historical reservations
would create a different problem: their ranks must be charged in the
cover and the integer target-loss inequality. The current proof pays
only current matching and selected records. It does not give free
storage or free rank budget to an accumulating history.

Generic exact matroid-parity oracle hardness is also not a proof that
the four-to-two promise is hard. Exact quota-two instances can have
singleton capacity two and no four-unit basis at all. Adding free
units or scaling capacities can make the demanded two-unit output
trivial. The separate below-two oracle barrier in the checkpoint is
therefore explicitly not used to close this promise problem.

## 6. Current research conclusion

The global resource side is not empty at a stalled critical state:
its strongly free owners have rank at least the current player-rank
deficit. The algorithm can exploit all members outside the unmarked
player span through an immediately paid exchange. The unsolved step
is to handle a free pool contained in that span with a new global
progress measure or a rigorously bounded simultaneous repair.

The existing rank-exponential two-unit construction remains valid,
and the large-quota near-three rank-quasipolynomial theorem remains
unchanged. No uniform improvement of the critical small-quota
runtime is claimed by this structural note.
