# Independent audit of the one-sided logarithmic SCC client

**25 October 2026.** This note independently checks
`log_barrier_incremental_scc.md`. The high-flow contraction principle is
credited there to CKLMP24. The new proof removes the objective-gap and
upper-capacity terms and uses explicitly charged endpoint retargeting.
No blocking mathematical defect was found in the stated client under the
complete raw-cycle and retirement interface.

## 1. The contraction certificate needs only the negative-flow budget

For any signed circulation with `f_e>=-delta_e`, contract the true SCCs
conceptually. On the resulting DAG, every cross-component edge `e=(C,D)`
crosses some topological prefix containing `C` and excluding `D`.
All crossing edges point outwards. Their signed flow sums to zero,
so `f_e<=sum_a delta_a`. This proves that an edge with flow above the
global negative-flow budget cannot cross true SCCs.

There is no hidden upper-capacity assumption. In particular the proof
does not need an upper bound on the positive flows of other edges on the
cut. Its only positive conclusion is that the chosen edge is internal to
one true SCC; the two blocks being merged need not already induce a
strongly connected subgraph by themselves. This is sufficient: contracting
any subsets contained in true SCCs cannot create connections between
different true SCCs.

## 2. Contraction preserves the relevant circulation

The quotient's flow is a circulation before a merge. Sum its divergence
equations over the vertices being identified. Newly internal edges cancel
from the sum. Deleting those edges and retaining every external edge's
exact value therefore gives a circulation on the new quotient.

An internal edge may carry nonzero flow when removed. That does not create
a demand error at the merged vertex. For a surviving retargeted edge, its
flow, slack offset, and barrier term are unchanged. The implementation
must finish all signed and absolute transfers before the old occurrence
metadata is invalidated.

The temporary graph during a sequence of backend endpoint replacements
need not itself conserve flow. Queries, steps, and externally visible
component answers occur only after the entire structural transaction has
finished. This is the same transaction discipline already required by
the raw numerical client.

## 3. LOW certifies completion of all SCC merges

The potential gradient is exactly `g=-w`, with positive
`w_e=1/(f_e+delta_e)`. The nonnegative incidence vector of any directed
cycle has ratio exactly `-1`. Hence a sound certificate excluding every
circulation of ratio at most `-1/4` excludes every directed quotient
cycle.

If a true original SCC still contained more than one quotient block,
paths within that original SCC would project to a directed closed walk
visiting multiple blocks and therefore to a quotient cycle. This
contradicts LOW. Together with the soundness of every earlier merge,
LOW proves that the maintained partition is exactly the SCC partition.

This argument uses the **sound** threshold implication of the raw oracle.
A small returned ratio without the specified approximation guarantee, an
unfinished refresh, or a failed resource guard would not be a completion
certificate.

## 4. The potential budget is independent of contraction history

At every queried state all active flows are below a constant multiple of
the contraction threshold `theta=Theta(1/(m+1))`. Weighted drift control
and the raw per-step motion bound also preserve this upper envelope during
the next numerical transaction. The tiny offsets ensure that every slack
remains strictly less than one. Thus every individual term
`-log(f_e+delta_e)` is nonnegative.

Accepted steps decrease the potential by `Omega(beta^2)`. An original
edge birth injects `O(log N)`. Moving a slack boundary outward decreases
the potential. A contraction deletes nonnegative barrier terms and does
not alter any surviving term. These statements give

\[
 T=O(m\log N/\beta^2)
\]

without charging a positive amount for a contraction and without any
global objective-gap variation argument.

Endpoint replacement is not an independent barrier birth. Counting it
as a new term while retaining the old term, resetting its value to zero,
or resetting its negative-flow allowance would invalidate this account.
The algorithm explicitly does none of those operations.

## 5. Notification and endpoint costs are actual operation costs

The weighted coordinate-drift invariant bounds the discrepancy between a
current value and its last exact anchor. If the last read was below
`theta`, that discrepancy cannot conceal a value as large as `2 theta`.
One accepted step changes each slack by only a small fixed relative
amount. Thus every flow threshold crossing is discovered and processed
before the upper slack envelope used in Section 4 could fail.

Small-to-large merging by the number of original vertices pays every
member scan, component-label write, and incident-record examination at
most logarithmically many times. This remains valid for an edge inserted
late in the sequence: each subsequent move of either endpoint to a
larger block doubles the block size it belongs to. Dead historical
incidence entries can be scanned under the same charge, provided they
cannot trigger duplicate physical updates.

The resulting `O(m log(n+2))` endpoint lifetimes are input to the raw
backend. Their expanded copies and callbacks cost a fixed power of its
envelope. They are not new logical barrier terms. Since every numerical
step is paid by the potential and each raw update pays its complete
lifetime transcript, the stated total time follows.

## 6. Arithmetic, empty graphs, and restarts

Rearmed positive slacks lie within fixed polynomial bounds. One common
integer scale therefore prices `w` and `g` to the required relative
accuracy. Because `g=-w`, it is also possible to use opposite integer
labels `gamma=-ell` with a harmless rounding margin. The common-grid
dyadic steps from the raw bridge then preserve conservation exactly.

An empty quotient needs no numerical iteration. An original self-loop
is already internal to a singleton component and can be ignored for SCC
maintenance. An insertion internal to a previously certified block
cannot change the partition. The direct small-instance solver is valid
for this potential as well as for the distance detector.

For an unknown final insertion count, an exhausted geometric guess can
restart the numerical state on the current quotient at zero flow while
retaining the certified partition. The sums of actual graph sizes and
initial potential budgets over such restarts are geometric. The partition
is never refined back into old singleton blocks, so the small-to-large
endpoint bound persists across these numerical restarts.

## 7. A cycle-detection consequence, and what is not supplied

The SCC structure also gives incremental directed cycle detection with
the same total bound. A directed cycle exists exactly when a nontrivial
SCC exists or a self-loop has appeared. If an explicit first cycle is
requested, one ordinary DFS after the first YES answer costs `O(n+m)`
once and returns a witness. This does not provide repeated fast path
queries inside arbitrary SCCs.

The existence of a dual topological potential at LOW is insufficient
to maintain a topological ordering efficiently. The current raw interface
does not return that potential or support its transpose-routing queries.
No topological-sort theorem, fully dynamic SCC theorem, or path-reporting
SCC theorem is inferred here.

## 8. Attribution and status

The public comparison is CKLMP24 Theorem 1.8 and Section 8.3, with the
later public raw-cycle backend included when making an exponent
comparison. The current contribution is the simpler potential and its
fully paid integration with the four-fifths candidate. This independent
audit is a mathematical check within the research process, not an
external certification or a substitute for the named backend proofs.

Primary source: <https://arxiv.org/html/2311.18295v1>.
