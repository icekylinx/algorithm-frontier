# Weighted oracle summaries exceed the binomial bound from two failures onward

## 1. Statement and scope

The sharp rank-only bound
$r\binom{h+d}{d}$ does not extend to fixed-cost summaries of arbitrary
oracle matroids. It already fails for rank four, one label per item, and
two failed labels.

**Theorem 1.** There is a rank-four matroid on 13 original items, each
carrying one of four labels and a fixed positive integer cost, such that
every original-ground restriction preserving the minimum cost of a
surviving basis after every at-most-two-label failure must retain all 13
items. All six two-label queries have surviving rank four. In contrast,
$r\binom{h+d}{d}=4\binom31=12$.

Consequently 12 items cannot suffice even for preserving only the exact
minimum-cost value; preserving every cost prefix or the canonical optimum
is at least as demanding.

**Theorem 2.** For every integer $h\ge2$, there is a rank-four,
one-label-per-item example requiring

$$
4(h+1)+1
\tag{WO1}
$$

original items. Taking direct sums gives, for every rank $r$ divisible
by four, examples requiring $r(h+1)+r/4$. Thus the one-failure weighted
oracle theorem is a substantive endpoint. The represented-matroid theorem
is unaffected: the resource matroid used here is not representable over
any field, as verified directly in Section 6.

These are exact finite constructions with proofs. They do not assert an
optimal general weighted-oracle bound above the displayed obstruction.

## 2. The underlying eight-class matroid

Let the underlying class ground be $\{0,1,\ldots,7\}$. Declare every set
of at most three classes independent, and declare a four-class set a
basis except for the following five forbidden sets:

$$
\begin{aligned}
H_1&=\{0,1,2,3\}, & H_2&=\{0,1,4,5\},\\
H_3&=\{0,1,6,7\}, & H_4&=\{2,3,4,5\},\\
H_5&=\{2,3,6,7\}.&&
\end{aligned}
\tag{WO2}
$$

Sets larger than four are dependent. This is a relabeling of the classical
Vámos matroid. Its needed properties follow from the explicit definition;
no representation theorem is assumed.

**Lemma 2.1.** The declared bases define a rank-four matroid.

**Proof.** Different forbidden four-sets intersect in at most two
classes. Take two allowed bases $B,C$ and $e\in B\setminus C$. If
$|C\setminus B|=1$, its only replacement gives $C$ itself. Otherwise
the candidate sets $B-e+f$, for $f\in C\setminus B$, are distinct
four-sets sharing the three-set $B-e$. At most one can be forbidden, so
an allowed exchange exists. This is the basis-exchange axiom.

Every three-set has five possible fourth classes, and at most one of its
four-set extensions is forbidden. Thus every set of at most three
classes is contained in an allowed basis, as declared. There are
$\binom84-5=65$ bases, so the rank is four. $\square$

Replace some underlying classes by parallel copies. A set of copies is
independent exactly when it contains at most one copy of each class and
its class set is independent in WO2. This defines a matroid: heredity is
immediate, and augmentation follows by augmenting the smaller underlying
independent class set with a class from the larger one and then taking
its available copy. This explicit parallel-extension oracle is the entire
resource interface below.

It is an explicit, efficiently evaluable oracle: check duplicate classes,
the cardinality, and the five constant-size forbidden sets. The lower
bound concerns the retained original ground, not computational difficulty
hidden inside the oracle.

## 3. The 13 ordered, colored items

Give item $i$ cost $c_i=2^{i-1}$. All subset costs are distinct, so each
surviving optimum is unique. The cost order is the item order in this
table. The last column gives one failure query under which that item is
forced into the unique optimum.

| Item $i$ | Underlying class | Its only label | A necessity witness |
|---|---:|---|---|
| 1 | 5 | B | fail C,D |
| 2 | 2 | A | fail C,D |
| 3 | 3 | A | fail C,D |
| 4 | 1 | C | fail B,D |
| 5 | 7 | D | fail B,C |
| 6 | 4 | B | fail A,D |
| 7 | 0 | C | fail A,B |
| 8 | 6 | D | fail A,C |
| 9 | 2 | D | fail A,B |
| 10 | 1 | B | fail C,D |
| 11 | 5 | C | fail B,D |
| 12 | 4 | D | fail B,C |
| 13 | 2 | C | fail A,D |

Every underlying class has a copy, so the extension has rank four.
Failure of a label removes every item carrying that label. The six
two-label optima are as follows.

| Failed labels | Surviving labels | Unique minimum-cost basis | Cost |
|---|---|---|---:|
| A,B | C,D | $\{4,5,7,9\}$ | 344 |
| A,C | B,D | $\{1,5,6,8\}$ | 177 |
| A,D | B,C | $\{1,4,6,13\}$ | 4137 |
| B,C | A,D | $\{2,3,5,12\}$ | 2070 |
| B,D | A,C | $\{2,3,4,11\}$ | 1038 |
| C,D | A,B | $\{1,2,3,10\}$ | 519 |

**Lemma 3.1.** This table lists the canonical greedy basis and the unique
minimum-cost basis in every displayed restriction.

**Proof.** Greedy scans the surviving items in the given increasing cost
order. It rejects repeated underlying classes and the five forbidden
four-sets in WO2. The complete nontrivial rejection traces are short:

- With labels C,D surviving, greedy takes $4,5,7$, rejects item 8 because
  its classes would be $H_3$, and takes 9.
- With labels B,D surviving, it takes $1,5,6,8$. The four classes are
  $\{4,5,6,7\}$, the allowed union of the last two underlying pairs.
- With labels B,C surviving, it takes $1,4,6$, rejects item 7 by $H_2$,
  rejects 10 and 11 as parallel repetitions, and takes 13.
- With labels A,D surviving, it takes $2,3,5$, rejects 8 by $H_5$ and 9
  as a repetition, and takes 12.
- With labels A,C surviving, it takes $2,3,4$, rejects 7 by $H_1$, and
  takes 11.
- With labels A,B surviving, it takes $1,2,3$, rejects 6 by $H_4$, and
  takes 10.

All listed accepted four-sets are allowed bases. Matroid greedy minimizes
the fixed additive cost of a basis, and distinct powers of two make this
optimum unique. The numerical costs are the corresponding sums.
$\square$

**Proof of Theorem 1.** The union of the six displayed bases is all 13
items. If a restriction omits item $i$, use its necessity query from the
first table. The unique original optimum contains $i$, so the restricted
instance either has no rank-four basis or has strictly larger optimum
cost. Either outcome violates the prescribed guarantee. Thus every valid
restriction retains all 13 items. This also proves the prefix obstruction:
at the prefix ending in an accepted item, omitting that item loses the
greedy rank increase. $\square$

## 4. Amplification to every failure budget at least two

Fix $h\ge2$. Before the 13-item order, prepend $h-2$ blocks
$Q_1,\ldots,Q_{h-2}$. Each block consists of four new parallel copies
whose underlying classes are the allowed basis $\{1,2,3,5\}$. Give all
four copies in $Q_j$ a new single label $Z_j$; these labels are distinct
and do not belong to the original four-label alphabet. Assign costs as
successive powers of two in the complete new order.

Every item of $Q_j$ is forced by the query failing
$Z_1,\ldots,Z_{j-1}$. The remaining earlier blocks are absent, and
$Q_j$ is the first surviving block and a full basis. Greedy takes all of
it. This query uses at most $h-3$ failures whenever such a block exists.

Every one of the original 13 items is still forced: fail all $h-2$
new block labels, then use its two-label witness from Section 3. This
uses exactly $h$ failures and leaves the same ordered original instance.
There are $4(h-2)+13=4(h+1)+1$ forced items and the resource rank
remains four. This proves WO1.

In fact every allowed failure still leaves rank four. If a new block
survives, it is a full basis. If no new block survives, at least $h-2$
failures were spent on their labels, leaving at most two failures among
the four original labels. Section 3 then supplies a surviving basis.

For $t$ disjoint copies of the construction, take the direct sum of their
resource matroids and reuse the same label alphabet across copies. A
surviving basis is a union of bases of the separate components. Give all
items distinct power-of-two costs, keeping the prescribed local order
inside each component. The optimum is unique and componentwise optimal,
so the same witness still forces each copy of each item. The rank is
$r=4t$, and the necessary support is
$t(4(h+1)+1)=r(h+1)+r/4$. $\square$

## 5. Why this does not contradict the rank-only theorem

The nine-item restriction

$$
H_{\mathrm{rank}}=\{1,2,3,5,7,10,11,12,13\}
\tag{WO3}
$$

already preserves full rank after every allowed failure in the base
13-item example. For failures A,B; A,C; A,D; B,C; B,D; and C,D,
respectively, it contains the following surviving bases:

$$
\begin{gathered}
\{5,7,11,12\},\quad \{1,5,10,12\},\quad
\{1,7,10,13\},\\
\{2,3,5,12\},\quad \{2,3,7,11\},\quad
\{1,2,3,10\}.
\end{gathered}
$$

Their underlying class sets are all allowed by WO2. Every zero- or
one-label failure leaves a superset of one of these two-label surviving
instances, so it also retains rank four. Some of these bases are more
expensive than the true optimum, which is permitted by rank preservation.

Thus the sharp rank-only summary, the one-failure weighted oracle summary,
and the represented fixed-cost theorem have different valid scopes. The
obstruction rules out silently transferring the last theorem to all
independence-oracle matroids for $h\ge2$.

## 6. Nonrepresentability and source attribution

Here is a short independent check of the representation boundary. Group
the underlying classes into pairs
$P=\{0,1\}$, $Q=\{2,3\}$, $R=\{4,5\}$, and $S=\{6,7\}$.
Suppose vectors over a field represented WO2, and let the same letters
denote their two-dimensional spans. The five forbidden pair unions have
dimension three, whereas $R+S$ has dimension four. Also
$P+Q+R$ and $P+Q+S$ have dimension four.

Since $\dim(P+Q)=3$, let $L=P\cap Q$, a line. Both $R\cap P$ and
$R\cap Q$ are lines. If they were different, they would span $R$
inside $P+Q$, contradicting $\dim(P+Q+R)=4$. They must therefore be
the same line, namely $L$, so $L\subseteq R$. The identical argument
gives $L\subseteq S$. This forces $\dim(R+S)\le3$, contradicting
its required dimension four. No field representation exists. A parallel
extension containing every class cannot remove this obstruction.

The underlying matroid is classical; the 13-item coloring, order, failure
table, and amplification above are the concrete obstruction used here.
For primary background on the Vámos matroid, see Karn, Nasr, Proudfoot
and Vecchi, [*Equivariant Kazhdan--Lusztig theory of paving matroids*,
Section 5](https://pages.uoregon.edu/njp/eq-relax.pdf). None of its
representation or polynomial-invariant results is needed for the proof
above. No publication-priority claim is made for this failure-summary
application.

## 7. Reproducible exact certificate

Run

~~~sh
python3 -B problems/matroid-failure-summaries/verify/check_weighted_obstruction.py
~~~

The checker independently enumerates the 65 underlying bases, the 386
extended bases, and all 8,192 subsets of the 13-item ground. It verifies
basis exchange, constructs the complete rank table by exhaustive subset
recurrence, and compares greedy with literal minimum cost over all
surviving bases. It checks all zero-, one-, and two-label queries, every
item's optimum and prefix necessity witness, and the rank-only restriction
WO3. Small amplified instances are also checked directly; the proof in
Section 4 establishes the unbounded family.

The computational search used to discover the example is not part of
this certificate or a premise of the theorem. The committed checker is
deterministic and verifies only the fully specified construction.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
