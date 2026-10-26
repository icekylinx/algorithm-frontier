# Current-blocker allocation with binary resource supplies

**25 October 2026. New compressed implementation; independent audit requested.**

This note removes dependence on the number of explicitly expanded copies
of an identical resource type. Supplies, and optional per-player type
quotas, may be encoded in binary. The current-blocker algorithm retains
its rank-sensitive number of steps. Each step is implemented using
integer counts, without enumerating the resource copies.

The mathematical imports are the audited current-blocker exchange and
signature proofs, the sharp rank-quality lemma, and the matroid-union
fat-resource wrapper. This note proves the additional finite
representation and available-value facts needed to apply them.

## 1. Input, output, and the two capacity interpretations

There are $q$ players with a player-selection matroid $M$ of
rank $r$, and $t$ resource types. Type $j$ has a positive
intrinsic unit value $v_j$ and an integer supply $c_j\ge0$.
Supply counts are binary integers. A liking incidence $(p,j)$
may also have a binary quota $a_{pj}$, meaning that player $p$
may receive at most $a_{pj}$ copies of type $j$. Replace
$a_{pj}$ by $\min(a_{pj},c_j)$, and use zero for an absent
incidence. An omitted quota means $a_{pj}=c_j$.

An allocation is represented by integer counts $n_{pj}$ with

$$
0\le n_{pj}\le a_{pj},\qquad
    \sum_p n_{pj}\le c_j.
 \tag{C1}
$$

Only selected basis players require positive target value. Their value
is $\sum_jv_jn_{pj}$. This is an output of polynomial bit length;
printing a separate record for every copy is not part of the model.

Two important cases must be distinguished:

* $a_{pj}=c_j$: ordinary identical item copies, where one player
  may receive many units of one type;
* $a_{pj}\in\{0,1\}$: a capacity-limited service that can be
  provided at most once to any player. This includes a uniform
  resource matroid on its eligible receiving players.

The second case does not silently count the same service repeatedly.
Neither case represents an arbitrary resource-specific matroid.

Let $\mathcal P$ be the number of players, types and explicit
liking/quota incidences, plus a constant. Let $b$ be the total
numeric bit length of all supplies, quotas, values and numerical
parameters.
The largest item parameter remains the largest **unit** value
$u=\max_{j:c_j>0}v_j$, or zero if no unit exists, not the value
$c_jv_j$ of an entire type. Rank zero is the trivial empty
allocation; approximation formulas containing $1/r$ assume
$r\ge1$.

## 2. The aggregate compact relaxation is sufficient

The appropriate perspective relaxation is

$$
\begin{split}
 &x\in P_{\mathcal B(M)},\\
 &\sum_jv_jy_{pj}\ge T x_p,\\
 &0\le y_{pj}\le a_{pj}x_p,\\
 &\sum_p y_{pj}\le c_j.
 \end{split}
 \tag{C2}
$$

It is a relaxation of every integral allocation (C1). It can be
related to a conceptual universe of $c_j$ distinct copies of
each type. Given a feasible point of (C2), assign the same fractional
amount $y_{pj}/c_j$ to each conceptual copy, for $c_j>0$.
Each copy has total fractional usage at most one, and each player's
copy variable is at most $x_p$, since $a_{pj}\le c_j$.

This conceptual lift is used only in the proof. No copy variables or
copy vertices are constructed by the algorithm.

### Lemma 1: the available-value bound with type quotas

Let a physical forbidden set contain $c_j-A_j$ of the conceptual
copies of type $j$. Player $p$'s maximum available value is

$$
V_p(A)=\sum_jv_j\min(a_{pj},A_j).
 \tag{C3}
$$

The uniform fractional lift gives it at most

$$
\sum_jv_j\frac{A_jy_{pj}}{c_j}
 \le x_p\sum_jv_j\min(a_{pj},A_j)=x_pV_p(A)
 \tag{C4}
$$

value outside the forbidden set. The inequality follows from both
$A_j a_{pj}/c_j\le a_{pj}$ and
$A_j a_{pj}/c_j\le A_j$. Types with zero supply contribute zero.

Thus a completed scan with $V_p(A)<B$ for every eligible player
gives the same strict fractional outside-value inequality as before.
The matroid rank-mass and current star-cover proofs remain valid.
The per-player quota does not obstruct deleting an item from a bundle,
so all inclusion-minimality estimates, including the sharper singleton
star bound, are unchanged.

## 3. The finite intersection-cell state

Maintain active labels for current matching bundles and selected
candidate bundles. A matching bundle has one player owner. Different
selected bundles may have the same player owner. During a phase there
are at most $r$ matching labels and at most $r$ selected labels,
including the conservative allowance for a temporary free cascade.

For each resource type $j$, store integer cell counts

$$
z_j[a,b],
 \tag{C5}
$$

where $a$ is a matching-bundle label or zero, and $b$ is a
selected-bundle label or zero. The count is the number of copies that
belong to exactly that matching bundle and exactly that selected
bundle. Zero means that the copy has no owner of that kind. Since
matching bundles are pairwise disjoint and selected bundles are
pairwise disjoint, these cells partition all copies of type $j$:

$$
z_j[a,b]\ge0,\qquad
                       \sum_{a,b}z_j[a,b]=c_j.
 \tag{C6}
$$

The full representation has $O(t(r+1)^2)$ cells. Each count uses
$O(\log(c_j+1))$ bits. It is initialized by putting $c_j$
in the cell $(0,0)$. Label slots are reused only after their old
bundle has been retired and all corresponding row or column counts
have been moved.

The matching layer flags identify which matching labels belong to
the current blocker prefix $Y$. The copies outside the current
forbidden set $R(X\cup Y)$ are exactly

$$
A_j=\sum_{a=0\text{ or }a\notin Y} z_j[a,0].
 \tag{C7}
$$

Undiscovered matching bundles are included in (C7). Excluding all
nonzero matching rows would wrongly prevent the construction of
blocked candidates.

## 4. Finding and pruning a candidate in batches

For an eligible player, compute (C3) by scanning its liking list.
If that value is at least $B$, build a provisional candidate in
fixed type order. If its current value is $V<B$, take

$$
\min\!\left\{a_{pj},A_j,
                       \left\lceil\frac{B-V}{v_j}\right\rceil\right\}
 \tag{C8}
$$

copies of the next type. Distribute that integer count across the
at most $r+1$ available cells of that type in a fixed matching-
label order. Store the provisional counts by type and old matching
row. There is no one-copy loop.

Once the target is reached, prune in one pass over the represented
types. If the candidate contains $n_j$ copies of type $j$,
remove

$$
d_j=\min\!\left\{n_j,
                       \left\lfloor\frac{V-B}{v_j}\right\rfloor\right\}
 \tag{C9}
$$

copies, updating $V$, and remove those counts from the provisional
cells in a fixed order. If any copy of a processed type remains,
deleting one more would reduce the value below $B$. Later pruning
only decreases the value, so that property persists. The final
candidate is inclusion-minimal above $B$, respects all quotas,
and uses only available copies.

All ceilings and floors are exact rational operations on binary
integers. Products of input denominators have polynomial bit length;
large supplies increase count bit lengths, not the number of loop
iterations.

## 5. Blockers, exchanges and truncations are cell operations

The candidate's matching blockers are precisely the distinct nonzero
matching labels with positive provisional count. They are outside
the old $Y$, by (C7). If any blocker exists, insert a new selected
column, splitting its chosen counts from the old zero-selected
column. Mark those matching rows as blockers of the new center.
The usual invariant ensures that a newly discovered matching bundle
does not intersect an older selected bundle; otherwise it would
already have been in $Y$.

If no blocker exists, all provisional copies have matching label zero.
The free-candidate rule applies unchanged. Replacing matching bundle
$a$ first moves every cell $(a,b)$ to $(0,b)$, and then
assigns the candidate's copies to the new matching label. For a stored
free candidate its selected column already identifies those copies;
for a fresh candidate the provisional cell counts do. The new
matching label has no retained blocker-layer flag.

For a stored free center, write its column into the new matching row
before retiring that selected column during truncation. Equivalently,
save its provisional cell counts first. This transaction order prevents
losing the candidate's unit identities when its old layer is discarded.

Only the selected owner of the deleted matching blocker can become
newly free. A blocker-label list and its selected-owner pointer track
this event without checking individual copies. Truncating a selected
layer moves each retired column $(a,b)$ into $(a,0)$. Retiring
a blocker-layer flag does not delete its matching bundle; it makes
its remaining copies available again as prescribed by (C7).

All of these operations can conservatively scan the full cell table.
They therefore cost $\mathcal P\operatorname{poly}(r)$ integer
operations per charged microstate. No event is multiplied by a supply
count. Reusing a row or column slot is preceded by clearing its old
counts and owner metadata, so historical labels do not accumulate.

## 6. Why fixed resource identities and old maximality remain sound

The cell representation is an exact quotient of a conceptual finite
copy execution. At initialization choose a fixed universe of
$c_j$ copies for every type. Whenever a cell is split, choose any
subset of that cell's conceptual copies of the requested cardinality.
Moving a cell changes only its matching or selected owner tag; it
does not change the copies' values, liking sets or identity.

This inductively realizes every stored cell table by actual bundles
in one fixed conceptual universe. The implementation need not name
those units individually. In particular, it need not perform a global
permutation that could obscure the meaning of an earlier maximality
claim.

After an earliest-layer exchange, the selected sets and blocker sets
of each strictly lower retained layer remain the same conceptual
resource sets, exactly as in the uncompressed proof. Removing a
matching row outside such a lower blocker prefix does not remove a
resource from that lower forbidden set. The new matching bundle
avoids retained selected resources and is not placed in an earlier
blocker prefix. Hence lower availability and maximality are literally
preserved, not merely preserved up to a numerical total.

At output, only aggregate type counts per matching player are needed.
Their capacity constraints follow from (C6). If desired, each type's
copies can be assigned contiguous integer ID intervals to the output
players; listing the intervals still takes polynomial space.

## 7. Runtime, certificates and numerical input size

An eligibility scan uses the same player-matroid oracle tests as
before. Available values use (C3); blocker discovery and all updates
use cell counts. A completed failed growth test outputs the
independent player set, its closure predicate, and forbidden counts
$c_j-A_j$. Verifying the available-value conditions and the cover
value

$$
v(F)=\sum_jv_j(c_j-A_j)
$$

is polynomial in $\mathcal P,r,b$. Lemma 1 proves that these
compressed facts certify infeasibility of (C2).

The original rank-only micro-signature count is independent of the
number of item copies. Consequently every proved positive-slack
sharp-rank guarantee is implementable in

$$
\mathcal P\operatorname{poly}(r,b)\,
 \min\!\left\{2^{O(r)},
       (r+1)^{O(\varepsilon^{-1}\log(r+1))}\right\}
 \tag{C10}
$$

time and original-matroid oracle calls, with polynomial space. The
exact boundary uses the first exponential term. Polynomial factors
in $r$ may be absorbed into either displayed rank dependence.
The numerical encoding includes supplies and quotas; the claim is
not pseudopolynomial in $\sum_jc_j$.

## 8. Fat matching without expanding capacities

For the arbitrary-size wrapper, a fat type has unit value at least
the chosen threshold. A player can receive a fat unit of type $j$
only when $a_{pj}\ge1$. The fat transversal matroid is implemented
by a bipartite capacitated matching graph: each player has capacity
one and each fat type has capacity $c_j$. The latter may be
truncated to $\min(c_j,q)$ for this oracle, because at most
one fat unit per player is used. Ordinary deterministic integral flow
or bipartite matching implements its independence and rank queries
without creating $c_j$ vertices.

Every original optimum allocation supplies the same forward promise
as before by choosing one fat unit for each fat-supplied player.
The reverse union decomposition supplies either a compressed small
bundle respecting all quotas or one fat unit; those player sets are
disjoint. Deleting players during dual-basis extension preserves
capacities and quotas. Thus the exact $4-3/r$ and positive-error
$4-3/r+\eta$ integer-optimum guarantees also have a compressed
implementation, with a polynomial full-input multiplier for the
derived matroid oracles.

For a configuration-LP comparator, configurations are quota-feasible
count vectors. Their per-type capacity constraints are $c_j$,
and the same fat fractional-capacitated-matching split supplies the
derived small relaxation. The number of conceptual configurations
need not be finite polynomial, nor need any of them be enumerated.

Finally, put $V=\sum_jc_jv_j$ and use the common value denominator.
If a successful target $T$ returns value at least $aT$, choose
a grid upper target $U_0>V/a$; it must fail, since a positive-rank
allocation cannot give one player more than $V$. The value $V$
itself is not assumed to be a failed target. The upper target and grid
have polynomial bit length in the declared binary input. The
nonmonotone-success binary-search argument therefore requires only
polynomially many target trials, even when the total supply is
exponentially large.
