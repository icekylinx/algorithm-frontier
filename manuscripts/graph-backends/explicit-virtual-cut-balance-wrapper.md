# An explicit balance wrapper for virtual-expander success

**Correctness refinement, 24 October 2026.** This note supplies the
complete balance interface used by the sequential virtual hierarchy.
Every weak success, including a spectral leaf reached after earlier
cuts, must cover at least a $`1-\beta`$ fraction of its CURRENT
input host. The fixed choice is $`\beta=1/1000`$.

This replaces reliance on a leftover bound not stated by the former
three-quarter-coverage weak leaf. The correction changes only fixed
thresholds and a fixed number of calls. It changes neither the
quantitative routing tradeoff nor the $`4/5`$ composition's exponent.
Previously delivered checkpoints are not overwritten.

## 1. Required weak interface

For every actual induced host $`F`$ on $`N\geq1`$ vertices, and a
requested cut threshold $`\psi_{\rm w}>0`$, the weak procedure returns
one of the following:

* a nonempty cut $`S`$ with
  ```math
  \beta N\leq |S|\leq N/2,\qquad
          |\partial_F S|\leq\psi_{\rm w}|S|;
     \tag{1}
  ```
* a terminal set $`X\subseteq V(F)`$, with
  ```math
  |X|\geq(1-\beta)N,
     \tag{2}
  ```
  an explicit virtual expander with vertex set exactly $`X`$, and
  its explicit embedding into $`F`$.

A returned cut may first be complemented inside $`F`$ to make it
the smaller side. Its balance and boundary certificate must refer
to this CURRENT host, rather than an earlier host before deletions.
For a singleton the success alternative is allowed with its
vacuous expansion convention.

The expander's quantitative guarantee depends on the current host
degree and requested threshold exactly as in the hierarchy's weak
construction. The wrapper below never composes two success
embeddings.

## 2. The spectral weak leaf has this interface

Start with an actual leaf host of $`N`$ vertices. Give each vertex
mass one, and set $`\Delta=\max\{1,\max_v\deg_F(v)\}`$.
Apply the exact spectral cut-or-certificate primitive of
[virtual-expander-hierarchy-reconstruction.md](virtual-expander-hierarchy-reconstruction.md),
Section 1, with a fixed parameter
```math
\eta\leq\psi_{\rm w}/4.
 \tag{3}
```
As before, a returned cut has at most half of the current remaining
mass and boundary at most $`\eta`$ times its mass. Remove it and
repeat, but stop as soon as the removed union $`C`$ has
```math
|C|\geq\beta N,
 \tag{4}
```
rather than waiting for $`N/4`$.

The boundary of $`C`$ in the ORIGINAL leaf host is at most
$`\eta|C|`$. To see this, sum the cut boundaries in the successive
induced hosts. An edge joining two removed pieces may be counted
earlier, but no such edge remains in the final boundary. Every
edge of the final boundary is counted at the removal of its endpoint.

Immediately before the last removal, $`|C|<\beta N`$. The last
piece has at most half of the remaining host, so at the first
crossing of (4),
```math
\beta N\leq |C|<
                       \frac{1+\beta}{2}N.
 \tag{5}
```
If necessary, return its complement. Since $`\beta<1/3`$, the
smaller side still has at least $`\beta N`$ vertices. Complementing
increases boundary divided by side size by at most
```math
\frac{1+\beta}{1-\beta}<2.
 \tag{6}
```
Together with (3), this proves the weak cut alternative (1), with
fixed slack.

If the spectral procedure certifies the remaining graph first,
then $`|C|<\beta N`$. The remaining induced graph therefore
supplies (2) with its identity embedding. Its sparsity is at least
$`\eta^2/(16\Delta)`$, with the same positive maximum-degree bound
$`\Delta`$ as the spectral lemma. The change from stopping mass
$`N/4`$ to $`\beta N`$ does not change this certificate.

At most $`N-1`$ nonempty removals occur. Each spectral test has
fixed polynomial arithmetic and bit work in the actual leaf size,
so the leaf remains within the declared polynomial
$`k_{\rm route},\log n,\log\psi_{\rm w}^{-1}`$ preprocessing bound.
It is never padded to its leaf threshold.

## 3. Internal weak successes already have the same coverage

Use the PRIMARY exact covering routine in the virtual hierarchy.
Before the coarse merge, every uncovered vertex is in its actual
small cut $`C_1`$. After removing the coarse blocks in $`C_2`$,
the final terminal set is their retained union $`X`$. Therefore
```math
V(F)\setminus X
                                     \subseteq C_1\cup C_2.
 \tag{7}
```
The weak routine returns a cut-only answer whenever
$`|C_1\cup C_2|\geq\beta N`$. Every successful internal call thus
has
```math
|V(F)\setminus X|<\beta N,
 \tag{8}
```
which proves (2). It is harmless if $`C_1`$ overlaps $`X`$;
only the containment (7) is used.

The already proved actual-boundary sum pays for a returned union.
If that union is larger than $`N/2`$, its complementary side remains
of fixed positive size and the fixed threshold slack pays for
complementation. Thus both internal calls and the corrected
spectral leaves meet the SAME weak interface.

The optional historical variant with a tiny leftover $`B`$ is
unnecessary here. This wrapper uses only the exact-covering
construction, so no separate bound on such a $`B`$ is assumed.

## 4. Strong balance with one retained success

Let the original host be $`G`$ on $`N_0`$ vertices, with requested
cut threshold $`\psi>0`$. Set
```math
\psi_{\rm w}=\psi/2.
 \tag{9}
```
Initialize $`C=\varnothing`$. While $`|C|<N_0/4`$, run the weak
routine on the ACTUAL induced host
```math
F=G[V(G)\setminus C].
 \tag{10}
```

If it returns a weak cut $`S`$, add $`S`$ to $`C`$ and discard
every candidate success hierarchy from that call. If it returns
a success, retain only this ONE successful hierarchy and return
that virtual graph and its embedding into $`G`$. The embedding
already lies in (10), which is a subgraph of $`G`$; no geometric
composition is needed.

### A cut exit is balanced

Consider the first time $`|C|\geq N_0/4`$. Before the final
addition write $`c=|C_{\rm old}|<N_0/4`$. By (1) the added
piece has at most $`(N_0-c)/2`$ vertices. Hence
```math
N_0/4\leq |C|
                  \leq c+(N_0-c)/2
                  <5N_0/8.
 \tag{11}
```
If $`C`$ exceeds half of $`G`$, complement it. The returned
smaller side then has cardinality in
```math
[N_0/4,N_0/2].
 \tag{12}
```

The pieces added to $`C`$ are disjoint. Summing their boundaries
in the CURRENT induced hosts yields
```math
|\partial_G C|
                          \leq\psi_{\rm w}|C|.
 \tag{13}
```
This argument does not require their boundaries in the original
host to be small individually. Edges to previously removed pieces
are already internal to the growing union and cause no additional
final boundary.

If complementation is needed, (11) gives
```math
\frac{|C|}{N_0-|C|}<\frac53.
 \tag{14}
```
Equations (9), (13), and (14) show that the returned balanced cut
has sparsity at most $`5\psi/6<\psi`$.

### A success exit covers at least two thirds

Before a success, the remaining host has
```math
|V(F)|>3N_0/4.
```
By the SAME weak coverage guarantee (2), valid at leaves as well
as internal nodes,
```math
|X|\geq(1-\beta)|V(F)|
               >(1-\beta)\frac{3N_0}{4}
               >\frac{2N_0}{3}.
 \tag{15}
```
Thus every strong call returns either the balanced cut (12) or a
virtual expander on at least $`2N_0/3`$ vertices, exactly as
required by the continuing cut-matching game.

### The number of weak calls is fixed

Before a cut exit, the active host has more than $`3N_0/4`$
vertices, so every added weak cut has size at least
$`3\beta N_0/4`$. Therefore at most $`O(1/\beta)`$ calls occur.
Since $`\beta=1/1000`$ is a fixed constant, this changes only a
fixed factor in work. It does not add a factor depending on
$`p`$, $`k_{\rm route}`$, or the hierarchy depth to any geometric
embedding. Failed candidate hierarchies are not retained.

If the original graph is a promised expander and $`\psi`$ is
strictly below its sparsity, the primary hierarchy's actual-cut
arguments force the first weak call to have no nonempty removed
cut and to cover the entire original host. The exact-root-coverage
claim is therefore preserved as well.

### Exact coverage at a promised-expander root

Here is the complete argument for the last assertion; it does not
infer exact coverage merely from the weak success guarantee (2).
Suppose the ORIGINAL root host $`G`$ satisfies
$`\Psi(G)\geq\sigma>0`$, and every actual-host cutoff in its weak
construction is strictly below $`\sigma`$. The spectral parameter
$`\eta`$, covering cutoff, and fresh matching cutoffs are fixed
smaller multiples of the requested root threshold, so this condition
is explicit.

First consider a root that is a spectral leaf. Its FIRST proposed
removed set is a nonempty cut of $`G`$ with sparsity at most
$`\eta<\sigma`$, which is impossible. The primitive therefore
certifies the whole original root host. Later residual-host tests
are never reached, and the output is $`X=V(G)`$.

At an internal root, every matching request is made on the FULL,
unchanged root host. The exact short-path packing lemma restores
all temporarily removed path-incident edges before publishing its
cut certificate; their boundary contribution has already been
paid by the terminal-count inequality in that lemma. Thus even
an arbitrarily small failure cut has its OWN true-host sparsity
certificate below $`\sigma`$, with no additive error term.
No such failure cut exists, so no root block fails and the
accumulated root failure cut is empty. Recursive cuts inside a
block's ABSTRACT matching graph may still occur. They are not
cuts of $`G`$ and are not removed root vertices.

The successful good sets cover at least two thirds of the root
vertices. Run the exact covering matching on the FULL $`G`$, as
specified in the fresh-cut adapter. Its possible failure cut also
has its own true-host sparsity certificate below $`\sigma`$.
It is therefore impossible, and every vertex outside the good
sets receives a distinct partner inside them. Consequently the
enlarged blocks $`U_i^*`$ partition $`V(G)`$ exactly:
```math
V'=V(G),\qquad C_1=\varnothing.
 \tag{16}
```
This uses the PRIMARY exact covering routine; no optional
leftover set $`B`$ is permitted in this argument.

Now inspect the FIRST proposed coarse removal. Before it, no
coarse block has been removed, and (16) is a full partition.
For every coarse subset $`\mathcal I`$, its mass is
$`\left|\bigcup_{i\in\mathcal I}U_i^*\right|`$, and its coarse
boundary is EXACTLY the boundary of this same vertex set in
$`G`$. Internal edges of a block do not cross either cut.
Hence the coarse graph has mass sparsity at least $`\sigma`$.
A returned smaller-side coarse cut of mass sparsity at most
$`\eta<\sigma`$ is impossible. There is no first coarse
removal, and therefore
```math
C_2=\varnothing.
 \tag{17}
```
The terms involving $`\partial C_1`$ and optional
$`\Delta|B|`$ in the general coarse-to-host accounting are
both zero here. One need not claim that an arbitrary coarse
cut AFTER earlier removals has its own sparse cut in $`G`$;
the first-removal argument prevents reaching that situation.

The first weak call therefore succeeds on ALL original root
vertices. The strong wrapper performs no later induced-host
call, retains this single hierarchy, and returns $`X=V(G)`$.
This proves exact root coverage while allowing ordinary subset
successes and genuine cuts at nonroot abstract calls.

## 5. Interaction with the entropy and work lemmas

For an abstract matching-graph cut player, choose $`\psi\leq1/8`$.
The strong wrapper returns an actual cut of sparsity below that
threshold and balance in (12), or a successful virtual graph.
The corrected half-matching entropy lemma applies unchanged.
Each matching occurrence keeps its separate native edge ID.

The smaller weak threshold in (9) and the smaller leaf stopping
mass in (4) are absolute constant changes. The spectral
certificate, the nonroot inverse-expansion recurrence, the single
root embedding, the actual-size leaf test, and the full query
router retain their stated asymptotic bounds.

This note is a proof-level correction to a success-interface
boundary. It is not an implementation test or an external
verification claim.
