# Root audit of the old-root-only epoch obstruction

**25 October 2026. Mathematical audit completed.**

This audit checks the construction in
[root-only-sp-tree-epoch-counterexample.md](../mechanism-boundaries/root-only-sp-tree-epoch-counterexample.md). Its conclusion is an
obstruction to a particular per-epoch amortization: exhaustion of an
old exact shortest-path tree, when starts are restricted to its old
artificial-source children, need not earn linear objective or price-
variation credit. It is not a lower bound on matching time, on all
epoch rules, or on a local repair algorithm.

## 1. The physical graph and comparison are genuine

There are two alternating chains with t matched pairs each, a matched
pair r,b attached to their far contacts a,w, and an unexpanded matched
pair p,q joining a to w. The graph has 4t+6 vertices, maximum degree
three, and the odd cycle a-r-w-q-p-a. Its two free chain roots are
connected by an explicit augmenting path through p,q. The matching
gap is exactly one. Thus the example does not rely on a bipartite-only
promise, a false gap parameter, or an arbitrary allocation instance
unrelated to a physical general graph.

With phase K=1, L=10000 C N, and zero ordinary debt, the top ledger
has row sums L and bin equations load+s=L-C. All nonzero top values
can lie on the existing guarded dyadic grid. At every lower integral
floor c<=C, the displayed allocation gives residual c at a nonroot
chain bin, 2c at b, and L-(t+1)c at a free root, where residual here
means L minus integral load. These values satisfy the floor capacities.
They are not claimed to equal the top slack, whose capacity subtracts
C. No prohibited equality between different floor allocations is used.

## 2. Exact-source reachability closes with explicit constants

The preparation maintains exact structural-eligibility slack caches,
an allowed special case of the approximate caches in the client. Each
path changes only two slack entries, so doing so costs constant extra
work. The actual trigger is cached slack at least 4C. The guarantee
that an eligible bin has actual slack at least 3C does not replace that
trigger. This corrects the preparation in the immutable H checkpoint.

The latest contact of an unfinished chain begins with slack one.
Until it reaches 4C, the unique ordinary path toward its free root
has all donors at least .99L. Its source offer at that endpoint is
greater than .186/C. Any source winning the exact endpoint query
therefore has slack below 4.033C. The normalized step overshoots by
at most a 1/256 fraction, giving post-step slack below 4.1C.

After expanding the next pair, the former contact has slack between
3C-1 and 3.1C-1. Further exact-source steps only increase a nonfree
source or decrease the free terminal. Thus old noncontacts retain
their lower bound and remain below 4.1C. This proves the preparation
inductively. Telescoping the bin equations gives each small parent
allocation as a sum of at most t+1 terms bounded by 6C, so the .99L
donor bound used in the induction is justified by the declared L.

If the newest contact never became eligible, it would supply a
constant-ratio direction forever. Each normalized step would increase
the bounded slack objective by a fixed positive constant, a
contradiction. Thus the preparation reaches its required threshold in
finite legal numerical work. Its cost is not claimed to be fast.

The final left contact can be stopped on first crossing slack two,
well below three. It then strictly dominates every older nonfree
source in that chain. Processing the right chain independently is
legitimate because their ordinary allocation components are still
disjoint. At the first right eligibility, expanding r,b before p,q
is an allowed structural choice. Padding the additional r,a incidence
by a tiny positive dyadic amount leaves a below three, w below 3.1C,
and b at slack 1+epsilon. The only remaining physical contacts a,w
have exact eligibility caches below 4C and are then ineligible.
There is no physical bin/bin edge or ordinary
debt that forces another structural action at the start of the epoch.

## 3. The old exact tree and its limited progress

At the constructed state, b offers nearly .75, whereas every other
bin offers at most .375 plus a negligible perturbation. Paths from b
to both chains have total donor cost O(t/L). Hence b is the unique
source child of the exact threshold tree, and all rows and bins are
represented in this linear-size tree. Its receiving arcs are tight
in the old potential.

If starts are restricted to that old source child, only b's slack
increases. Every other slack stays unchanged or decreases. Once
s_b exceeds a constant times C, all nonfree terminals fail the
threshold. A path to a free root has t+1 donors. Before the relevant
stopping scale these donors and the free slack remain a constant
fraction of L. Their total donor charge is Theta(t/L), so full tree
exhaustion occurs at s_b=Theta(L/t)=Theta(C), with constants allowed
to depend on the fixed factor 10000.

The normalized step gives a fixed positive multiplicative increase
in s_b whenever an old-root path is accepted. There are therefore
only O(log C) accepted steps. Its total slack-objective gain is also
O(log C), since only b contributes a positive slack-log change.

No unaccounted guard event is needed in this epoch for sufficiently
large t. Donors remain a constant fraction of L; receiving values only
increase. An accepted nonfree terminal has slack greater than 5s_b/3
before its small step and stays bounded away from zero afterward.
The contacts never become structurally eligible because their slack
does not increase.

## 4. Price credit and the LOW screen are insufficient

Each large donor decreases by at most O(L/t), so their aggregate
negative log variation is O(1). A chain receiving allocation at
distance j from its far endpoint is Omega(Cj), by the same telescoping
bin equations. Its increase is O(C), and summing log(1+O(1)/j)
gives O(log(t+1)). The tiny padded r,a incidence contributes at most
O(log S). Slack variation is O(log C), also bounded directly by the
number of normalized steps. Thus the example has only logarithmic
coordinate-price credit, despite its linear-size old tree.

All old bin potentials pi=A-D are at least one half. The fixed total
slack is 2L-C(2t+3). Consequently the semantic excess is Omega(L),
far above either the real 7N or conservative finite-word 6N LOW
threshold. The semantic certificate cannot avoid the obstruction by
declaring that the genuine matching gap is already absent.

There is also an explicit surviving comparison: increase contact a's
slack by L/10 and decrease its own free-root slack by L/10 along its
chain. The donor and terminal values after this transfer remain at
least .8L for sufficiently large t. The earlier .9L sentence has
been corrected to this conservative constant, since the initial
values are slightly below L. Because s_a<=3, the normalized positive
slack mass is at least L/30>12N. This is a feasible actual comparison,
not merely a directed path that happens to pass a local threshold.

Finite-word rounding loses only O(N/H) along a simple path. The
existing polynomial scale makes that smaller than all constant
source-dominance and threshold margins. The argument is not dependent
on exact-real cancellations.

## 5. What remains possible

The example admits an immediate escape if a fresh source arc may start
at an intermediate bin: the path from a along its own chain to the
free root still uses old tight receiving arcs and has a strong ratio.
This is exactly why the any-ancestor-source interface is useful.
The example neither proves that a whole-tree refresh is necessary nor
bounds how often such a refresh could occur in a better algorithm.
Its role is to rule out the specific claim that every exhausted
literal old-root epoch has already paid for a linear-size rebuild.
