# Exact binomial fault summaries for arbitrary matroids

**Abstract.** A circuit-blocking set-pair inequality gives the sharp binomial bound for rank-preserving summaries of arbitrary oracle matroids under correlated label failures. A separating-family reduction yields fixed-parameter preprocessing. The same argument extends to integer-valued monotone submodular functions and to sharp real-valued marginal and entropy inequalities. Cost-prefix preservation requires the separate represented-matroid construction.

## 1. Model and result

Let M be a matroid on a finite explicitly listed ground set E, with rank r. Each element e has a set Lambda(e) of at most d labels. A query F consists of at most h labels and deletes every element whose label set intersects F. Write

$$
X_F=\{e\in X: \Lambda(e)\cap F=\varnothing\}
$$

for X contained in E. We seek a single restriction H contained in E such that

$$
r_M(H_F)=r_M(E_F)\qquad\text{for every }|F|\le h. \tag{1}
$$

**Theorem 1 (sharp size).** Every inclusion-minimal H satisfying (1) obeys

$$
\boxed{|H|\le r\binom{h+d}{d}.} \tag{2}
$$

This bound is best possible, even for a direct sum of rank-one represented matroids. In particular, for one label per element, an exact (h+1)r bound holds for arbitrary matroids, not just represented ones.

**Theorem 2 (constructivity).** Given an independence oracle, a restriction satisfying (1) and (2) can be found deterministically in

$$
f(r,h,d)\,|E|^{O(1)}
$$

oracle time for a computable function f. A direct reverse-deletion implementation instead uses |E|^{O(h)} oracle time. The FPT statement includes r in the parameter; it is not a uniform polynomial-time construction when r,h,d are unrestricted inputs.

The combinatorial size proof is short and independent of the construction. The FPT construction uses an elementary separating family followed by repeated reduction and a bounded final search. Its parameter dependence is intentionally not optimized here.

Before construction, one may clip `h` to the number `L` of distinct labels and `d` to the largest actual label-set size; rank is always at most `|E|`. The oracle statement treats one independence-oracle call as one unit of cost. It does not assume a linear representation, a field, or a bit-level encoding for oracle answers. Label relabeling, palette enumeration, and bookkeeping use `f(r,h,d)*|E|^{O(1)}` ordinary word operations, with label and pool indices stored in `O(log(|E|+L+dh*log(L+2)))` bits. Thus the theorem gives an FPT oracle-query/time bound, not a polynomial-space bit-kernel claim.

## 2. A circuit-blocking set-pair lemma

For every e in a matroid ground set H, let A_e and B_e be disjoint subsets of some auxiliary label universe. Suppose

$$
e\notin\operatorname{cl}_M\bigl(\{f\in H-e:A_f\cap B_e=\varnothing\}\bigr). \tag{3}
$$

Equivalently, deleting all elements whose A-set meets B_e makes e a coloop. Then

$$
\boxed{\sum_{e\in H}\binom{|A_e|+|B_e|}{|A_e|}^{-1}\le r_M(H).} \tag{4}
$$

**Proof.** Order the finite auxiliary label universe uniformly at random. Select e if every label in A_e occurs before every label in B_e. The probability of this event is exactly

$$
\binom{|A_e|+|B_e|}{|A_e|}^{-1};
$$

the event is automatic when either set is empty, agreeing with this formula.

Let J be the selected set. We show that J is independent. Suppose a circuit C were contained in J. Condition (3) says that, for every e in C, at least one f in C-e has A_f meeting B_e: otherwise C-e would survive B_e, contradicting (3). Consequently, C cannot have all its A-sets empty.

Choose e in C whose last A_e-label in the random order is as late as possible, treating the last label of the empty set as earlier than every real label. Choose f in C-e and a label lambda in A_f intersect B_e as guaranteed above. Its position is at most the position of the last A_f-label, which is at most the position of the last A_e-label. But e was selected, so every B_e-label, including lambda, occurs strictly after every A_e-label. This is a contradiction. Thus |J| is at most r_M(H); taking expectations proves (4). QED.

For rank one, (3) gives the ordinary strong cross-intersection condition between distinct set pairs, so (4) specializes to the classical Bollobas set-pairs inequality. The new use here is that circuit blocking replaces pairwise cross-intersection and the right-hand side becomes matroid rank.

## 3. Proof of the size theorem

Start with an inclusion-minimal H satisfying (1); existence is immediate because E itself satisfies (1). For each e in H, minimality gives a failure set F_e of at most h labels such that H-e does not satisfy (1). Since H does satisfy it, this says

$$
r_M((H-e)_{F_e})<r_M(H_{F_e}). \tag{5}
$$

Necessarily Lambda(e) is disjoint from F_e, and (5) says that e is a coloop of M restricted to H_{F_e}. Apply (4) with A_e=Lambda(e) and B_e=F_e. Since |A_e| is at most d and |B_e| is at most h,

$$
\binom{|A_e|+|B_e|}{|A_e|}\le\binom{d+h}{d}.
$$

Therefore

$$
\frac{|H|}{\binom{h+d}{d}}
\le\sum_{e\in H}\binom{|A_e|+|B_e|}{|A_e|}^{-1}
\le r_M(H)\le r.
$$

This proves (2). The nonuniform inequality (4) can also retain information about the actual element label degrees and witness sizes instead of replacing both by worst-case bounds.

### Tightness

Use h+d labels. In each of r rank-one direct-sum classes, create one element e_A for every d-element subset A of the labels, and give e_A label set A. To force a particular e_A, fail the h-element complement of A. In each class, e_A is then its only surviving element. Hence every rank-preserving restriction must contain all r times binomial(h+d,d) elements. The construction also works when h=0 or d=0, with the usual conventions.

### Extension interpretation

Because H_F is contained in E_F, rank equality implies equality of their original-matroid closures. This closure relation persists in any later matroid extension whose restriction to E is M. Thus the summary preserves the maximum number of surviving original elements that can extend any fixed independent background set in such an extension. Repeated exchange can retain that background exactly. This is an unweighted feasibility/cardinality consequence; no arbitrary-cost claim follows from it.

## 4. Direct XP construction

List the L labels actually occurring in E. Repeatedly remove e whenever

$$
r_M((H-e)_F)=r_M(H_F)
$$

for every F contained in this label universe with |F| at most h. Each rank computation uses at most |E| independence queries by greedy augmentation. A single pass through the elements suffices: if e has a witness making it a coloop when tested, later deletions that keep e cannot destroy that coloop property. A safe implementation can also repeat to a fixed point.

The resulting H is inclusion-minimal and therefore satisfies (2). This straightforward method uses at most

$$
O\!\left(|E|^2\sum_{i=0}^{h}\binom{L}{i}\right)
$$

independence queries, up to bookkeeping and with h clipped at L. It is polynomial for each fixed h, but this expression alone is not an FPT bound in h.

## 5. An elementary separating reduction

Assume h,d are positive; if either is zero, an ordinary basis solves the problem. Let the current ground set X have s elements, and relabel its L at most ds occurring labels as the integers 0 through L-1. If L=0, again an ordinary basis suffices.

Choose a prime

$$
q>dh\lceil\log_2(L+1)\rceil,
\qquad
q=O\bigl(dh\log(L+1)+1\bigr).
$$

This can be done deterministically by trial division; Bertrand's postulate supplies the displayed size bound. Encode each label lambda by its base-q digits as a polynomial P_lambda(T) over the prime field F_q, of degree at most ceil(log_q(L+1))-1. Distinct labels give distinct polynomials.

For each t in F_q, let chi_t(lambda)=P_lambda(t). If A,B are disjoint label sets with |A| at most d and |B| at most h, the nonzero polynomial

$$
\prod_{a\in A,\,b\in B}(P_a(T)-P_b(T))
$$

has degree less than q. Thus some t has chi_t(A) disjoint from chi_t(B). If A or B is empty, separation is automatic.

For every t and every palette P contained in F_q with |P| at most d, form

$$
X_{t,P}=\{e\in X: \chi_t(\Lambda(e))\subseteq P\}
$$

and retain any greedy basis of M restricted to X_{t,P}. Let R be their union. Then

$$
|R|\le r q\sum_{i=0}^{\min(d,q)}\binom qi
\le r q(q+1)^d. \tag{6}
$$

For an allowed failure set F and a surviving e in X_F, choose t separating Lambda(e) from F intersect the current label universe, and choose P=chi_t(Lambda(e)). This pool contains e and contains no failed elements. Its retained basis therefore spans e using elements of R_F. It follows that

$$
\operatorname{cl}_M(R_F)=\operatorname{cl}_M(X_F) \tag{7}
$$

for every query F. Importantly, the failure labels outside the current instance do nothing, so (7) composes through repeated restrictions even when the hash maps are rebuilt between rounds.

If every pool basis is computed in the same fixed cost order, the same argument proves equality of all surviving cost-prefix spans. Thus this preliminary reduction can preserve costs. Only the final inclusion-minimal rank-preserving deletion step is unweighted.

## 6. Removing the input-size dependence and proving FPT construction

There is a computable A=A(h,d) such that the q in the preceding reduction is at most A log_2(s+2). With k=d+1 and B=r(2A)^k, (6) gives

$$
|R|\le B\,[\log_2(s+2)]^k. \tag{8}
$$

Choose a computable threshold T=T(r,h,d) such that

$$
B[\log_2(s+2)]^k\le s/2 \qquad\text{for every }s>T. \tag{9}
$$

For fixed B,k such a threshold exists because a fixed power of log(s) is o(s). It is effective: after the function s/[log_2(s+2)]^k becomes increasing, double s until (9) first holds. One can replace this by an unnecessarily large explicit elementary bound if desired.

Repeatedly apply the separating reduction whenever s>T. Each application halves s and preserves every failure rank profile, so there are at most O(log |E|) rounds. Each round scans s elements for at most q(q+1)^d pools. Since every fixed power of log(s+2) is at most g(d) times s for a computable g, the total number of oracle calls over all rounds is at most

$$
f_1(h,d)\,|E|^2,
$$

up to polynomial bookkeeping. The resulting X has at most T elements and at most dT occurring labels. Run the direct reverse-deletion procedure only on this bounded instance, enumerating at most

$$
\sum_{i=0}^{h}\binom{dT}{i}
$$

failure sets. Its entire cost is a function of r,h,d. Transitivity of (7) makes the resulting rank profile identical to that of the original instance, and Theorem 1 gives the exact final bound r binomial(h+d,d). This proves Theorem 2.

No minimum-cardinality optimization is claimed: the final summary is inclusion-minimal and has the sharp worst-case upper bound, but it need not be globally smallest for its particular input.

**Query interface after preprocessing.** For a rank query F, scan the retained H and run greedy augmentation on `H_F`; this returns a surviving basis of size `r_M(E_F)` using at most `|H|` independence-oracle calls and `O(|H|)` stored element IDs. For the submodular extension, evaluate `f(H_F)` directly with the value oracle; a greedy scan can also return a value-increasing certificate using at most `|H|` value queries. These are query costs on the retained summary and do not turn the construction into a uniform-polynomial bit algorithm.

## 7. Boundaries and open algorithmic question

The argument establishing (4) uses that e is a coloop of the **entire surviving restriction**. Under the weighted, cost-ordered LF rule, one only knows that e lies outside the span of cheaper surviving elements. In a selected circuit, the element with the last own-label in the random order need not be the most expensive element. Consequently, that weaker witness is insufficient for the proof in Section 2. Extending the exact binomial bound to arbitrary-oracle fixed-cost prefix summaries remains open in this note.

For explicitly represented matroids, the companion polynomial-feature lift already constructs a fixed-cost summary of size r binomial(h+d,d) in uniform polynomial time. Here the exact rank-only size is generalized to all matroids, while the construction is only FPT when r+h+d is the parameter, or XP in h by direct enumeration. A uniform polynomial construction attaining (2) for arbitrary independence-oracle matroids, already for d=1, is not established here.

The known W[2]-hardness of a generic colored failure-witness problem is not used as a lower bound on constructing an arbitrary valid summary.

## 8. Antecedents and comparison to public results

* The permutation event and its reciprocal-binomial probability are the classical Bollobas set-pairs method. A useful primary modern account, including the strong and skew versions and the distinction between them, is Gabor Hegedus and Peter Frankl, *Variations on the Bollobas set-pair theorem*: https://arxiv.org/html/2307.14704v1 . The circuit-blocking rank inequality (4) should be checked against matroidal extensions of set-pair inequalities before any priority claim.

* Matthias Bentert, Fedor V. Fomin, Petr A. Golovach, and Laure Morelle, *Fault-Tolerant Matroid Bases*, ESA 2025, DOI 10.4230/LIPIcs.ESA.2025.83: https://drops.dagstuhl.de/storage/00lipics/lipics-vol351-esa2025/html/LIPIcs.ESA.2025.83/LIPIcs.ESA.2025.83.html . Their main algorithm finds a **minimum-cardinality** set retaining the original full rank after a bounded number of **individual element failures**, with parameter rank plus fault budget. Our task uses arbitrary correlated label failures, permits the surviving input rank to drop, and only attains the exact universal worst-case size bound. These are different optimization requirements; this note does not claim to improve their minimum-cardinality algorithm.

* Dipan Dey and Telikepalli Kavitha, *Low-Cost Arborescence Under Edge Faults*, May 2026, Section 4: https://arxiv.org/html/2605.13800v1 . They explicitly construct a union of k+1 successive minimum-cost bases for at most k individual item faults in an arbitrary matroid. This gives the familiar (k+1)r weighted individual-fault bound, not a correlated-label result. Their v1 abstract and theorem print kr despite the k+1 bases in the algorithm/proof; the stated kr bound cannot hold under their at-most-k-failures definition, as a rank-one class of k+1 parallel elements shows. Use the actual construction and distinguish the parameter convention rather than quoting that displayed constant unchecked.

* Relative to Checkpoint W's LF rank summary, (2) replaces r (h+d)^(h+d)/(h^h d^d) by the sharp r binomial(h+d,d), but only the unweighted/rank part is upgraded for arbitrary matroids. The represented companion retains fixed-cost preservation. No unrestricted weighted-oracle improvement is asserted.

## 9. Monotone submodular functions

The permutation proof has a more general form that does not use matroid exchange or circuits.

**Theorem 3 (submodular set-pair inequality).** Let f be a finite real-valued monotone submodular function on a finite ground set H. Give each e disjoint auxiliary label sets A_e and B_e, and write

$$
H_e=\{x\in H:A_x\cap B_e=\varnothing\},
\qquad
\delta_e=f(H_e)-f(H_e-e).
$$

Then

$$
\boxed{
\sum_{e\in H}
\frac{\delta_e}{\binom{|A_e|+|B_e|}{|A_e|}}
\le f(H)-f(\varnothing).
} \tag{10}
$$

Here disjointness ensures e belongs to H_e. All delta_e are nonnegative by monotonicity. The matroidal inequality (4) is the special case f=r_M and delta_e=1.

**Proof.** Randomly order the labels and select e when all A_e-labels precede all B_e-labels, exactly as before. Order the selected elements by the position of their last A-label, in nondecreasing order, with the empty A-set first. Fix a selected e. Every label of every earlier selected element has position at most the last A_e-label, while every B_e-label has a strictly larger position. Thus all earlier selected elements lie in H_e-e. Diminishing returns gives

$$
f(J_{<e}+e)-f(J_{<e})\ge f(H_e)-f(H_e-e)=\delta_e.
$$

Summing over selected elements yields sum_{e in J} delta_e at most f(J)-f(emptyset), hence at most f(H)-f(emptyset). Taking expectations proves (10). Empty A-sets and empty B-sets obey the same argument with the stated ordering convention. QED.

**Corollary 4 (exact integral-submodular failure-value summary).** Let f be integer-valued and monotone submodular on E, and let R=f(E)-f(emptyset). Under the same at-most-d-labels-per-element and at-most-h-failures model, there is a restriction H with

$$
f(H_F)=f(E_F)\quad\text{for all }|F|\le h,
\qquad
|H|\le R\binom{h+d}{d}. \tag{11}
$$

Every inclusion-minimal exact summary satisfies this size bound. Given a value oracle, the elementary separating reduction and final bounded search construct one in deterministic f_2(R,h,d)|E|^{O(1)} oracle time. The parameter includes the numerical range R, not only its bit length.

To prove the size statement, choose an inclusion-minimal H and for each e a failure witness F_e where deleting e strictly reduces value. Integrality gives delta_e at least 1, so (10) proves (11). For the constructive statement, replace each pool's matroid basis by the subset obtained by scanning the pool and keeping an element precisely when it increases the current f-value. Zero marginal gains remain zero as the retained set grows; the final subset has the full pool value, and every retained item increases it by at least one. Hence each pool retains at most R elements. All separator, halving, and bounded-search arguments continue unchanged.

The bound is already tight for coverage functions: use one feature for each of R classes in the lower-bound construction, and let an element cover exactly its class feature. The function counts covered features. Conversely, integrality or a positive marginal-gap assumption is needed for a cardinality consequence: a modular function giving each of N items weight 1/N has total value 1, but its value-preserving restriction must contain all N items even with no failures.

There is also a universal-context interpretation. If g is any monotone submodular extension of f to additional elements B, then

$$
g(H_F\cup B)=g(E_F\cup B)
$$

for every context B. Indeed, the zero marginal gain from adjoining E_F to H_F cannot increase after adjoining B, by submodularity. Thus (11) simultaneously preserves the exact value after correlated failures and arbitrary later augmentation, provided the later function restricts to the original f.

This extension concerns exact saturation/value preservation. It does not claim a smaller general-purpose coreset for constrained submodular maximization or minimum-cost submodular cover, and does not close the arbitrary-matroid weighted-prefix gap in Section 7. Priority of (10) and its precise fault-summary application should be checked separately; the proof is self-contained.

### A sharp real-valued total-sensitivity consequence

For any real-valued monotone submodular f, define the maximum final marginal of e after allowed failures by

$$
\sigma_e=\max_{\substack{|F|\le h\\\Lambda(e)\cap F=\varnothing}}
\bigl[f(E_F)-f(E_F-e)\bigr].
$$

There is no minimum-marginal or integrality assumption in the following sharp inequality:

$$
\boxed{\sum_{e\in E}\sigma_e\le
\binom{h+d}{d}\,[f(E)-f(\varnothing)].} \tag{12}
$$

Indeed, choose a maximizing failure witness separately for each e and apply (10), followed by the worst-case reciprocal-binomial bound. This controls the sum of the individual worst marginal losses, even though different items may attain their maxima under different correlated failure queries.

For a concrete information-theoretic specialization, let X_e be jointly distributed discrete random variables with finite joint Shannon entropy, and put f(S)=H(X_S). Then

$$
\boxed{
\sum_{e\in E}
\max_{\substack{|F|\le h\\\Lambda(e)\cap F=\varnothing}}
H\bigl(X_e\mid X_{E_F-e}\bigr)
\le\binom{h+d}{d}\,H(X_E).
} \tag{13}
$$

Thus the aggregate of the worst residual uncertainties of individual surviving variables under correlated erasures is bounded by the exact binomial multiplier of the original joint entropy. These are conditional entropies given **all other surviving variables**, not cost/time-prefix conditionings.

Equality is possible. Take independent variables Y_1,...,Y_r. For each i create C=binomial(h+d,d) identical copies of Y_i, indexed by the d-subsets A of an (h+d)-label universe, assigning label set A to its copy. Failing the complement of A leaves exactly that copy in each class. Its conditional entropy given the other surviving classes is H(Y_i). Hence the left side of (13) equals C sum_i H(Y_i)=C H(X_E). This also proves exact tightness of (12) for weighted coverage functions. No priority claim for this entropy formulation is made without further literature comparison.
