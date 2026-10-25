# Independent audit of the layer-lifetime branching bound

**25 October 2026. Status: passes.** This note independently checks the
stronger call-count argument for the fixed-certificate, no-superposition
algorithm in `certified_no_superpose_haxell_path_routing.md`, and its
application to explicitly listed bipartite hypergraphs. The argument uses
the proved layer growth and the fact that each selected set is fixed for
its lifetime. It does not assume termination in order to bound termination.

The final, stronger result of this audit is the rank-independent weighted
count in Sections 7--8:

\[
                 \#\mathrm{builds}
                  \le \exp O\!\left(\frac{U\log(2+s)}s\right),
                  \qquad s=\log\Delta.
\]

Sections 1--6 retain the preceding unweighted branching derivation as a
valid intermediate bound. The current explicit theorem is
`explicit_hypergraph_matching_branching_improvement.md` and also returns
a checkable strong-Haxell violation certificate when the promise fails.

**Public-baseline correction.** Section 9 independently checks that the
same final weighted bound follows from the already public BHHS algorithm,
because each layer has only a constant number of successful superposition
epochs. The explicit time bound is a new analysis of the public algorithm
as well as a bound for the fixed-certificate implementation. It is not a
separation from every consequence of the public framework.

## 1. Notation and the three required invariants

Let \(q\) be the number of demand/left vertices and \(R\ge1\) an upper
bound on the rank of every selected or matched hyperedge. Let
\(\Delta\ge4\) be the per-demand degree cap. At a main-loop boundary,
the algorithm has a stack of noncollapsible positive-index layers and the
root unmatched set \(Y_0\). Its already proved properties are:

\[
\begin{aligned}
 |X_i|&>\frac{\Delta}{10}|Y_{<i}|,\\
 |Y_i|&\ge\frac9{10}|X_i|,\\
 |X_i|&\le\Delta |A(Y_{i-1})|,\qquad
 |Y_i|\le R|X_i|.
\end{aligned}
\tag{B1}
\]

The first is the strong-hitting growth lemma. The second holds for every
surviving noncollapsible layer because nonfree selected hyperedges have
disjoint blocker sets. The third uses the input degree cap and the fact
that one rank-\(R\) selected hyperedge intersects at most \(R\) matching
hyperedges. The matching is disjoint on right vertices.

For the lifetime of a layer \(i\), its selected set \(X_i\) and prefix
through \(i-1\) are fixed. Its blocker set \(Y_i\) may shrink. A
collapse at level \(i+1\) changes \(Y_i\); a collapse changing the lower
prefix first discards layer \(i\). The full proof of this lifetime
property is essential to the new count.

## 2. A nonroot layer has few direct children

Fix one particular lifetime of layer \(i\ge1\). Put

\[
                   W=|Y_{<i}|>0,
                   \qquad z=W+|Y_i|.
\tag{B2}
\]

The value \(W\) remains fixed for that lifetime. It is positive because
the algorithm operates only while \(Y_0\ne\varnothing\). At the birth
of the layer, (B1) gives

\[
        |Y_i|\le R\Delta |A(Y_{i-1})|
                   \le R\Delta W,
        \qquad z\le(1+R\Delta)W.
\tag{B3}
\]

When a direct child layer \(i+1\) collapses, more than
\(|X_{i+1}|/10\) of its selected hyperedges are free. Their demand
identities occupy at least \(|X_{i+1}|/(10\Delta)\) different active
vertices. The swap removes the corresponding different matched edges from
\(Y_i\). The child growth inequality therefore gives a decrease greater
than

\[
       \frac{|X_{i+1}|}{10\Delta}
             >\frac{W+|Y_i|}{100}=\frac z{100}.
\tag{B4}
\]

Thus every direct-child collapse multiplies \(z\) by at most \(0.99\).
Throughout the lifetime, including after a child collapse, \(z\ge W\).
There can consequently be only

\[
              O\bigl(\log(1+R\Delta)\bigr)
\tag{B5}
\]

direct-child collapses. At most one direct child is still alive in a finite
execution prefix. Every earlier direct child ended by its own collapse:
the algorithm only discards the top layer, and a parent cannot be popped
while a child is still on the stack. Hence the number of direct-child
births is at most the bound in (B5) plus one.

Descendant activity does not invalidate (B4). A collapse strictly deeper
than \(i+1\) changes only a deeper blocker set. It cannot restore a
removed blocker to \(Y_i\), add a new one, or change \(W\).

## 3. Root children and depth

For the root, each layer-one collapse reduces \(|Y_0|\) by more than
\(|Y_0|/100\). Until the last such collapse the unmatched count is a
positive integer, initially at most \(q\). It has at most
\(O(1+\log q)\) collapses, including the final one that may reach zero,
and at most one additional currently live child in any finite prefix.

The surviving depth is bounded using (B1):

\[
       |Y_i|>\frac{9\Delta}{100}|Y_{<i}|,
       \qquad
       |Y_{\le i}|>
             (1+9\Delta/100)|Y_{<i}|.
\tag{B6}
\]

The blocker/unmatched sets have disjoint left identities, and their total
size is at most \(q\). Therefore the surviving stack has depth

\[
                    D=O(\log(q+2)/\log\Delta).
\tag{B7}
\]

A newly built, immediately collapsible layer can add one temporary level.
For a nonempty feasible instance, the strong-hitting condition
\(\Psi\ge\Delta R^2\) and the trivial singleton hitting bound imply
\(\Delta\le |B_{\rm active}|\), so \(\log\Delta\le U\) for a
master input logarithm \(U\). The extra one is absorbed by \(O(U/s)\)
when \(s=\log\Delta\).

## 4. Count every finite execution prefix first

Associate a rooted tree to the layer births: the parent of a new layer is
the then-current top layer; the permanent root is \(Y_0\). A layer's
children are its successive direct-child lifetimes. For every finite
execution prefix this tree has:

* \(O(1+\log q)\) children at the root;
* \(O(1+\log(1+R\Delta))\) children at every other node;
* depth \(O(U/s)\).

These bounds do not depend on the length of the execution prefix.
Consequently the total number of births in any such prefix is at most

\[
 (1+\log q)\,
 \bigl(C(2+\log R+s)\bigr)^{O(U/s)}.
\tag{B8}
\]

Equivalently, its logarithm is

\[
        O\!\left(\log U+
             \frac U{s}\log(2+\log R+s)\right).
\tag{B9}
\]

An infinite execution would have arbitrarily many builds, since every
individual build and collapse is a finite computation. That contradicts
the uniform finite-prefix bound. Once termination is established, the
algorithm can only have terminated with \(Y_0\) empty: strong hitting
guarantees a new nonempty layer whenever an unmatched identity remains.
This proves termination and (B8) without a circular assumption.

The independent signature/partition argument remains valid for the same
algorithm. Its \(\exp O(U/\sqrt{s})\) bound can be combined with (B9)
by taking the smaller exponent. The branching bound need not be stronger
for small \(s\), and the statement should retain that minimum.

## 5. Explicit hypergraphs supply the required certificates directly

Let \(H=(A,B,E)\) be an explicitly listed bipartite hypergraph: every
hyperedge contains one left vertex and between one and \(r\) right
vertices. Let \(p=\sum_{e\in E}|e|\), and suppose

\[
        \tau(E_S)\ge\Psi|S|\quad(S\subseteq A),
        \qquad \Psi\ge\Delta r^2,
        \qquad \Delta\ge4.
\tag{B10}
\]

In each valid outer state, scan the hyperedges in a fixed deterministic
order. Accept an edge if its left vertex is active and below the degree
cap, and its right vertices are disjoint from the current forbidden set.
Upon acceptance, forbid its right vertices and all right vertices of every
matched hyperedge it intersects. Each matched hyperedge is processed at
most once during the build.

The matching-edge exclusion is automatic in these valid states: at the
first layer active left vertices are unmatched; at later layers their own
matched hyperedges are in the forbidden prefix. One may explicitly skip
matching identities as well.

The added forbidden-right-vertex set \(C\) satisfies

\[
               B(X\cup Y)\subseteq C,
               \qquad |C|\le r^2|X|.
\tag{B11}
\]

For every unsaturated active vertex, all its incident hyperedges have been
scanned. They either contributed their right vertices to \(C\) when
accepted or were already blocked by the monotonically growing forbidden
set. Thus the forbidden prefix together with \(C\) hits every incident
hyperedge. This is exactly the fixed certificate used by the outer proof,
with \(R=r\). No approximate numerical oracle is needed.

A full scan costs \(O(p)\). Building the ownership table for the matching
and scanning all newly blocked matching hyperedges also costs \(O(p)\).
Certificate materialization touches at most \(|B_{\rm active}|\) actual
right vertices, regardless of the symbolic upper bound \(r^2|X|\).
All selected hyperedges of the surviving layers have disjoint right
supports, and the matching does as well; direct collapse scans remain
within \(O(p)\) per collapse. Hence the complete algorithm costs

\[
 p\exp O\!\left(\min\left\{
          \frac U{\sqrt{s}},\quad
          \log U+\frac U{s}\log(2+\log r+s)
                         \right\}\right),
\tag{B12}
\]

after linear input preprocessing, with \(U=\log(p+4)\) and
\(s=\log\Delta\). If the input separately lists isolated right
vertices, reading and removing them adds \(O(|A|+|B|+p)\) preprocessing.
The strong promise excludes an isolated left vertex. This avoids measuring
a long separately supplied vertex list as if it had zero input cost.

## 6. Quantitative consequences and comparison

The nonempty promise gives \(\Delta r^2\le\Psi\le
|B_{\rm active}|\le p\), so all counters have logarithmic bit length and
\(\log r+s=O(U)\). For a fixed \(0<\beta<1\), if
\(\Delta\ge\exp(\Theta(U^\beta))\), the branching term gives

\[
                        p\exp O(U^{1-\beta}\log U).
\tag{B13}
\]

If \(\Delta\ge p^\epsilon\) for fixed \(\epsilon>0\), it gives

\[
                          p(\log p)^{O(1/\epsilon)}.
\tag{B14}
\]

These are consequences of an explicit expansion promise, not a general
hypergraph matching algorithm and not a general-graph matching theorem.
The algorithm does not need to recognize the promise efficiently.

The directly checked public comparison is BHHS,
[*Disjoint Paths in Expanders in Deterministic Almost-Linear Time via
Hypergraph Perfect Matching*](https://arxiv.org/html/2511.02214v1),
Theorem 1.5 and Lemma 3.3, whose stated overhead uses
\(\sqrt{\log d}\). The fixed-certificate implementation obtains the
new displayed bound by removing superposition and counting layer
lifetimes. Section 9 shows that bounded superposition epochs also permit
the same final count for the original public algorithm.
A search of current primary paper, conference, and author records on
25 October 2026 did not locate a stronger published version of this
particular branching tradeoff. That search is not an exhaustive optimization
of every public hypergraph matching framework.

## 7. A rank-independent weighted count

The crude branching bound used an upper bound on the parent's initial
blocker count. The sharper argument does not. For each layer lifetime
\(i\), retain only its fixed positive prefix size
\(W_i=|Y_{<i}|\), which is an integer in \([1,q]\). Every time that
layer creates a child it is noncollapsible. Equations (B1) give

\[
             W_{\rm child}=W_i+|Y_i|
                    \ge\kappa W_i,
             \qquad \kappa=1+9\Delta/100.
\tag{B15}
\]

The birth sizes \(z_1,z_2,\ldots\) of its successive direct children
satisfy \(z_{j+1}\le\rho z_j\), with \(\rho=0.99\), by (B4).
This is true for any finite prefix of those children. The previous child
must have collapsed before the next is born. A still-live final child is
allowed and does not affect the geometric bound.

Put \(s=\log_2\Delta\ge2\) and choose

\[
                    \lambda=100\frac{\log_2(2+s)}s.
\tag{B16}
\]

Give a node weight \(w_i=W_i^{-\lambda}\). The children have increasing
weights as their prefix sizes decrease. Sum them backwards from the last
child. Equation (B15) and the geometric separation give

\[
 \sum_{\text{children }j}w_j
       \le\frac{\kappa^{-\lambda}}{1-\rho^\lambda}w_i
       \le\frac12 w_i.
\tag{B17}
\]

The last inequality holds uniformly, including small strength parameters.
For an explicit numerical check, \(\kappa\ge\Delta^{1/5}\).
Indeed the first three terms of its fifth power give

\[
 (1+9\Delta/100)^5
       \ge 1+9\Delta/20+81\Delta^2/1000\ge\Delta;
\]

the final positive quadratic has negative discriminant after subtracting
\(\Delta\). Hence
\(\kappa^{-\lambda}\le(2+s)^{-20}\). Also

\[
        1-0.99^\lambda
             \ge\min\{1/100,\lambda/200\}.
\]

If \(\lambda\ge1\), the ratio in (B17) is at most
\(100/(2+s)^{20}<1/2\). If \(\lambda<1\), it is at most
\(2s/[\log_2(2+s)(2+s)^{20}]<1/2\). No unstated restriction
on \(r\) or \(R\) is used here.

At the root, the birth sizes are the successive positive unmatched
counts. They are at least one and obey the same geometric decrease. Their
weights consequently sum to at most \(1/(1-\rho^\lambda)\).

For the layer-instance forest in any finite execution prefix, every node
other than a root child appears in the child sum of exactly one parent.
Summing (B17) therefore shows that the total node weight is at most
\(2/(1-\rho^\lambda)\). Every node has weight at least
\(q^{-\lambda}\). Thus

\[
             \#\mathrm{builds}
               \le \frac{2q^\lambda}{1-\rho^\lambda}
               =\exp O\!\left(\frac{U\log(2+s)}s\right).
\tag{B18}
\]

The prefactor causes no extra rank or master-logarithm term. Its logarithm
is \(O(\log(2+s))\), and \(s\le U\) in every nontrivial execution.
It is absorbed by the exponent displayed in (B18). The uniform finite-prefix
bound rules out infinite execution exactly as in Section 4; depth need not
be assumed in this weighted proof.

This also covers a newest node whose growth test has not yet passed, or
which is about to return a failure certificate. Its parent has already
passed the growth test and is noncollapsible, so (B15) holds for its birth.
A node that fails the test never creates a child. For any two successive
siblings, the earlier sibling necessarily passed and collapsed before the
later one was born. Both inequalities needed for (B17) therefore remain
valid in a certifying implementation.

### Consequences of the sharper count

For explicit hypergraphs the final work bound is

\[
       O(|A|+|B|)+
       p\exp O\!\left(\frac{U\log(2+\log\Delta)}{\log\Delta}\right).
\tag{B19}
\]

There is no additional rank dependence in this exponent. The rank still
enters the hypothesis \(\Psi\ge\Delta r^2\). The bounds (B13)--(B14)
remain valid, while for \(\Delta\ge U^c\), fixed \(c>0\), the new
overhead is \(\exp O(U\log\log U/\log U)\) for every feasible rank.
As \(s\to\infty\), \(\log(2+s)/s=o(1/\sqrt{s})\), so the checked
parameter dependence improves uniformly on the displayed BHHS bound.

## 8. Audit of the certifying alternative on arbitrary explicit inputs

I independently read the complete current
`explicit_hypergraph_matching_branching_improvement.md`. The certifying
implementation is valid without assuming the strong Haxell condition.

The input prechecks handle an isolated left vertex by returning that vertex
and the empty hitting set. If \(\Delta r^2>|B_{\rm used}|\), they return
a singleton left set together with \(B_{\rm used}\), which is a strict
violation certificate. In the remaining execution,
\(\Delta r^2\le|B_{\rm used}|\le p\), so \(s\le U\), counters fit
in input-size words, and the weighted count applies.

After each build, test
\(|X_{\ell+1}|>\Delta|Y_{\le\ell}|/10\). If it fails, the growth
proof constructs

\[
 S=A(Y_{\le\ell})\setminus\bigcup_i F_i,
 \qquad C=\bigcup_i C_i.
\]

The old layers are noncollapsible and have passed their growth tests. The
same fixed-certificate argument proves that \(S\ne\varnothing\), that
\(C\) hits every input hyperedge incident to \(S\), and that

\[
                           |C|<\Delta r^2|S|.
\]

Those assertions follow from the constructed sets, independently of any
promise. If the test passes, the node may be used as a parent later; if it
fails, the algorithm terminates immediately with the certificate. Section 7
therefore bounds every execution, not only promised ones.

The explicit output can be checked by scanning the incidence list once:
verify nonemptiness and cardinalities, mark \(S,C\), and test intersection
with \(C\) for every hyperedge whose left endpoint belongs to \(S\).
Reference counts over the current certificate sets permit their union to
be materialized in \(O(p)\) time, without an additional depth factor at
termination. A perfect matching is likewise checked by scanning its left
and right incidences. Both alternatives have linear verification work in
the full explicit input size.

A violation certificate rejects the sufficient strong-Haxell promise. It
does not assert that no perfect matching exists. This distinction is
explicit in the main theorem and must remain in its interpretation.

## 9. Independent check of bounded resets in the public BHHS algorithm

The primary source is BHHS,
[*Disjoint Paths in Expanders in Deterministic Almost-Linear Time via
Hypergraph Perfect Matching*](https://arxiv.org/html/2511.02214v1),
Algorithms 2--3, Proposition 5.6, and Lemma 5.8. The full derived-public
argument is in `public_hypergraph_algorithm_weighted_reanalysis.md`.
This check uses its maximal-layer algorithm, not the new physical
certificate oracle.

During the entire lifetime of a positive-index layer \(i\), its lower
prefix and therefore \(W_i=|Y_{<i}|\) are fixed. Algorithm 3 modifies
\(Y_i\) only after the current direct child has collapsed and has been
discarded. It may then increase \(X_i\) in a successful superpose-build.
It never discards a live child for a superposition or rebuild. A change
to the lower prefix requires layer \(i\) itself to collapse and disappear.

Lemma 5.8 gives the initial bound \(|X_i|>\Delta W_i/10\). The per-left
degree cap always gives \(|X_i|\le\Delta|Y_{i-1}|\le\Delta W_i\).
Every accepted superposition multiplies \(|X_i|\) by at least \(1.1\),
and selected edges are never removed from a surviving layer. Hence at most
25 successful superpositions occur during a layer lifetime; at most 26
epochs have a fixed selected set. These generous integer constants avoid
rounding conventions at equality.

Within one epoch, each child collapse reduces its next sibling's birth
prefix \(z=W_i+|Y_i|\) by a factor at most \(0.99\), exactly as in
(B4). At every birth the parent is noncollapsible, so
\(z\ge\kappa W_i\), where \(\kappa=1+0.09\Delta\). Across epochs
\(z\) may increase. Summing the backward geometric series separately
within the at most 26 epochs gives

\[
 \sum_{\text{all children }j}W_j^{-\lambda}
  \le 26\frac{\kappa^{-\lambda}}{1-0.99^\lambda}W_i^{-\lambda}
  \le\tfrac12W_i^{-\lambda},\qquad
 \lambda=100\frac{\log_2(2+s)}s.
\]

The explicit estimates after (B17) absorb the extra factor 26. Root layers
have no superposition, so their weight sum is unchanged. The finite-prefix
proof of (B18) applies. Each superpose-build call follows a child collapse,
including unsuccessful superpose-builds; their total number is at most
the number of collapsed layer instances. Counting those calls changes the
work by only a constant factor.

For an explicit incidence list, public greedy BuildLayer takes \(O(p)\)
time even from a nonempty selected set: mark its existing forbidden
resources and degrees, then scan all input edges once. The public algorithm
therefore has the derived bound

\[
 p\exp O\!\left(\frac{U\log(2+\log\Delta)}{\log\Delta}\right)
\]

under its original \(\Delta r^2\)-strong Haxell condition. This is a
derived public baseline, not the bound printed in BHHS Theorem 1.5.
Neither the new destructive-support path oracle nor fixed physical
certificates are needed for this explicit-hypergraph bound.

There is a similar caution about certification. BHHS Lemma 5.8 constructs
an actual left set and a right hitting set from the current layers and
their hypothetical maximal extensions. If a growth guard fails, those
extensions can be recomputed and the proof's sets returned as a
strong-Haxell violation certificate. This costs at most one input scan per
live layer at final failure, within the same asymptotic envelope. The
fixed-certificate implementation has a simpler persistent certificate and
avoids those extra scans, but certification itself should not be described
as absent from all white-box uses of the public algorithm.
