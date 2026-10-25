# Fixed-dimensional numeric-target and accuracy lower bounds for encoded rank programs

**25 October 2026. Complete incremental theorem and proof; root and independent
full mathematical reviews passed.** These are conditional computational lower
bounds for explicitly encoded, polynomial-time rank programs. They
complement the unconditional rank-oracle lower bounds; they do not
assert hardness for graphical, linearly represented, or laminar
matroids.

For every fixed positive dimension d, ETH rules out exact nonnegative
numeric-target algorithms with running time

\[
               2^{o(T^{d/(d+1)})}\operatorname{poly}(H),
                  \qquad T=\sum_{j=1}^d T_j,
 \tag{FE1}
\]

already for d equality rows on ordinary matroid bases. All rank queries
in the constructed input family are answered in polynomial time by a
fixed decoder and the supplied instance data. Thus the lower bound
still holds if an algorithm is allowed to inspect that data and rank
program directly.

For each of the seven nontrivial single-matroid optimization variants
with one exact scalar side constraint, ETH also rules out approximation
schemes with running time

\[
            2^{o(\varepsilon^{-1/2})}
                         \operatorname{poly}(H_\varepsilon).
 \tag{FE2}
\]

The maximizing guarantee is (1-epsilon)OPT (or OPT/(1+epsilon)); the
minimizing guarantee is (1+epsilon)OPT. Side constraints remain exact.
FE2 is not an inverse-error-linear lower exponent and does not close
the gap to the current exp(O(1/epsilon)) upper bound.

The assumption in both displays is deterministic ETH, formulated here
as the nonexistence of a deterministic 2^{o(N)} poly(|phi|)-time
algorithm for 3-CNF satisfiability with N variables. Randomized
algorithms are excluded by the same reductions only under the
corresponding randomized ETH. No implication from deterministic ETH
to randomized ETH is used.

## 1. An explicit equal-vector-sum family

Fix d. Given a 3-CNF formula phi on N variables, choose an even integer
k and put

\[
       E=[k]^d,\qquad n=k^d,\qquad r=n/2.
 \tag{FE3}
\]

Every element is its distinct vector label u=(u_1,...,u_d). Order E
lexicographically as e_1,...,e_n. Since k is even, n and r are integers.

Among all r-subsets of E, choose a most populous class with the same
vector sum alpha:

\[
 \mathcal H_\alpha=
       \left\{S\subseteq E:|S|=r,\ \sum_{u\in S}u=\alpha\right\},
                    \qquad L=|\mathcal H_\alpha|.
 \tag{FE4}
\]

Each component sum is an integer between zero and rk. There are at
most (rk+1)^d possible sums. The central binomial coefficient satisfies
binomial(n,n/2)>=2^n/(n+1), and hence

\[
           L\ge \frac{2^n}{(n+1)(rk+1)^d}
                       =2^{n-O_d(\log n)}.
 \tag{FE5}
\]

Choose the smallest even k with k^d>=4N, after padding N to a fixed
constant depending only on d if necessary. Then n=Theta_d(N).
For all sufficiently large such n,
(n+1)(rk+1)^d<=2^{n/2}, so L>=2^{n/2}>=2^N.
The finite initial range can be handled directly, or by adding a
constant number of unused SAT variables. A fully mechanical compiler
can increase even k until the explicit lower bound in FE5 is at least
2^N; this also has n=Theta_d(N), and requires polynomially many
iterations for fixed d. No satisfying assignment is needed to select
k or alpha.

Two distinct sets in H_alpha cannot differ by a single element
exchange. Indeed, replacing u by v while preserving the vector sum
would require u=v. This property holds for every subfamily of H_alpha.

## 2. Polynomial counting and lexicographic ranking

The compiler can compute alpha without enumerating the r-subsets.
For i=1,...,n+1, cardinality h and a vector beta, define

\[
 D_i(h,\beta)=
   \#\left\{S\subseteq\{e_i,\ldots,e_n\}:
           |S|=h,\ \sum_{u\in S}u=\beta\right\}.
 \tag{FE6}
\]

Use h in {0,...,r} and every component of beta in {0,...,rk}.
Entries outside these ranges are zero. The recurrence is

\[
 D_i(h,\beta)=D_{i+1}(h,\beta)
                     +D_{i+1}(h-1,\beta-e_i),
 \quad D_{n+1}(0,0)=1,
 \tag{FE7}
\]

with every other final entry zero. The table contains at most
(n+1)(r+1)(rk+1)^d entries. For fixed d this is polynomial in n.
Every entry is at most 2^n and has at most n+1 bits. The compiler
chooses a maximum D_1(r,beta), with a fixed tie rule, as alpha and L.

Order the characteristic strings of H_alpha lexicographically with
0<1. A candidate S in H_alpha has a zero-based index

\[
                 \operatorname{idx}(S)\in\{0,\ldots,L-1\}.
 \tag{FE8}
\]

This index is computable using the same suffix table. Scan positions
i=1,...,n, maintaining the number h and vector sum beta already
chosen in earlier positions, initially both zero. If e_i is absent
from S, continue. If e_i is present, add

\[
                       D_{i+1}(r-h,\alpha-\beta)
 \tag{FE9}
\]

to the index, and then increment h and beta by 1 and e_i. FE9 counts
exactly the completions whose prefix agrees so far but puts 0 at i,
which precede this candidate's 1 at the first differing position.
Invalid remainder states contribute zero. This is the usual direct
lexicographic count; no unranking, subset enumeration, or exponential
storage is involved.

Each rank evaluation can recompute D if it was not retained. The
table, indices and arithmetic all have polynomial bit complexity
for fixed d. The encoded input may supply only k, alpha, N and phi
plus the fixed evaluation routine; a cached table is optional and
has polynomial size as well.

## 3. A polynomial-time assignment decoder

Interpret the integer

\[
                 a(S)=\operatorname{idx}(S)\bmod 2^N
 \tag{FE10}
\]

as an N-bit assignment, using a fixed bit order. This map from H_alpha
onto the Boolean assignments is surjective: L>=2^N, so every index
0,...,2^N-1 occurs. Computing the residue only needs the low N bits
of an O(n)-bit number.

Define the accepted subfamily

\[
           \mathcal A_\phi=
              \{S\in\mathcal H_\alpha:\phi(a(S))=\mathrm{true}\}.
 \tag{FE11}
\]

It is nonempty exactly when phi is satisfiable. Testing membership
in A_phi is polynomial-time: compute one candidate's index and
evaluate phi on that single assignment. It does not solve SAT inside
a rank query. Surjectivity establishes the existential equivalence;
the program does not search over the assignments.

## 4. The encoded matroid and its full rank evaluator

Let M_phi have the following independent sets:

\[
 \mathcal I_\phi=
    \{S:|S|<r\}\ \cup\
    \{S:|S|=r,\ S\notin\mathcal H_\alpha\}\ \cup\
                                     \mathcal A_\phi.
 \tag{FE12}
\]

No set larger than r is independent. This is a rank-r matroid for
every formula phi, including an unsatisfiable one.

Hereditary closure is immediate. For augmentation, only an independent
I of size r-1 and an independent J of size r need examination; smaller
I can accept any new element and remain below r. If J minus I has one
element, its addition gives J. Otherwise choose two distinct elements
u,v in J minus I. The two r-sets I+u and I+v have distinct vector sums,
so at least one is outside H_alpha and is independent regardless of
phi. This proves augmentation without making any assumption about
which members of H_alpha satisfy phi.

There is always a rank-r set outside H_alpha: any (r+1)-set contains
two r-subsets that differ by an exchange, and they cannot both lie
in H_alpha. Thus the rank does not depend on satisfiability.

The full rank of any query set S is

\[
 r_\phi(S)=
 \begin{cases}
 |S|,&|S|<r,\\
 r,&|S|>r,\\
 r,&|S|=r,\ \sum_{u\in S}u\ne\alpha,\\
 r,&|S|=r,\ \sum_{u\in S}u=\alpha,\ \phi(a(S))=\mathrm{true},\\
 r-1,&\text{otherwise}.
 \end{cases}
 \tag{FE13}
\]

For |S|>r, the preceding exchange-neighbor argument gives a contained
basis independently of phi. For a forbidden r-set every (r-1)-subset
is independent, so its rank is exactly r-1. FE13 is therefore a correct
rank program on all query sets, not just on prospective solutions.
It runs in poly_d(n+|phi|) bit operations. Independence queries are
also polynomial by comparing rank with cardinality.

This is an explicit promised representation: the decoder just proved
produces a valid matroid for every well-formed data record. Verifying
whether an arbitrary unknown program defines a matroid is not part
of the instance or the reduction. Algorithms may inspect the supplied
program and data, not merely make black-box calls.

## 5. The fixed-dimensional numeric-target reduction

Give element u coefficient a^j_u=u_j in row j and set T_j=alpha_j.
Ask for a basis of M_phi satisfying

\[
                         \sum_{u\in S}u_j=\alpha_j,
                           \qquad j=1,\ldots,d.
 \tag{FE14}
\]

Such a basis must belong to H_alpha and hence to A_phi. Conversely
every member of A_phi is a basis satisfying all these equalities.
By FE11, FE14 is feasible if and only if phi is satisfiable. Scalar
weights, if the solver expects an additional scalar objective, may
all be zero.

The parameter size is controlled in both directions. Each coordinate
label 1,...,k occurs k^{d-1} times. Among r=n/2 elements, the smallest
possible sum in a fixed coordinate is

\[
   k^{d-1}\sum_{i=1}^{k/2}i=\frac{n(k+2)}8\ge\frac{nk}8.
 \tag{FE15}
\]

The largest is at most rk=nk/2. Therefore

\[
          \frac{dnk}8\le T=\sum_j\alpha_j\le\frac{dnk}2,
 \qquad
 T=\Theta_d(n^{1+1/d})=\Theta_d(N^{1+1/d}),
 \quad T^{d/(d+1)}=\Theta_d(N).
 \tag{FE16}
\]

The explicit d-by-n coefficient matrix, targets, ground, formula data
and rank routine have total encoding H=poly_d(N+|phi|). Constructing
them, including the suffix counts and largest class, is polynomial
for fixed d. With repeated and tautological clauses removed, a 3-CNF
has at most O(N^3) distinct clauses; alternatively all statements can
retain the poly(|phi|) input factor directly.

If an algorithm with FE1 existed, this polynomial reduction followed
by that algorithm would decide phi in 2^{o(N)} poly(|phi|) time.
This contradicts ETH and proves the fixed-d lower bound. The proof
allows arbitrary inspection of the polynomial-time rank program.
It does not obtain its running-time bound by charging exponentially
hard work to a supposedly unit-cost oracle.

The target vector is balanced: every alpha_j=Theta_d(nk). Hence the
anisotropic expression K(U) from the upper-bound theorem is Theta_d(n)
on this family. This establishes a matching worst-case order for that
balanced family, not a lower bound for every prescribed unbalanced
target vector.

## 6. Related inequality-only formulations

Over bases, the equality construction also gives d pure covering rows together
with one exact nonnegative scalar cost budget. Give element u the
cost c_u=sum_j u_j and use budget T. Requiring every row sum at least
alpha_j forces total cost at least T; the budget forces equality
in every row. This is precisely the same satisfiability test.

For d pure upper rows on bases, set D=dk, let
c_u=D-sum_j u_j>=0, and use budget rD-T>=0. Every basis has cost
rD minus its total row sum. The upper targets and this budget
together again force all equalities. Exact minimum-cost optimization
can decide either budget variant by comparing its minimum to the
specified budget.

For independent sets, one additional scalar lower condition
|S|>=r forces a basis and preserves the equality reduction. These
observations do not assert the same row count for an independent
variant that omits this cardinality condition.

All coefficients in these constructions are nonnegative and binary
encoded. Their linear coordinate functions are subclasses of the
aligned nonlinear theorem. Thus allowing the latter's compressed
nonlinearity cannot remove this lower bound for its full model.

## 7. The one-dimensional accuracy consequence

Now take d=1. To avoid collision with the side threshold, continue
to write r=n/2. The ground labels are i=1,...,n, the largest size-r
equal-sum family has sum alpha, and the same assignment-ranking
compiler gives M_phi on n=Theta(N) elements.

Since L>=2^N>=2, alpha is strictly between the unique minimum and
maximum sums of an r-subset. In particular,

\[
     \frac{r(r+1)}2<\alpha<\frac{r(2n-r+1)}2,
 \tag{FE17}
\]

after the fixed small-input range is removed. Consequently the
minimum-sum and maximum-sum r-subsets are bases of every M_phi.
They provide feasible instances for either side-constraint direction,
even when phi is unsatisfiable.

Use w_i=i and the exact side threshold alpha. For each of the seven
nontrivial optimization variants use the following objective:

| Variant | Nonnegative integer objective v_i | Satisfiable optimum B |
|---|---:|---:|
| MAX independent set, w(S)<=alpha | i+1 | alpha+r |
| MAX independent set, w(S)>=alpha | n+1-i | r(n+1)-alpha |
| MIN independent set, w(S)>=alpha | i-1 | alpha-r |
| MAX basis, w(S)<=alpha | i | alpha |
| MAX basis, w(S)>=alpha | n+1-i | r(n+1)-alpha |
| MIN basis, w(S)<=alpha | n+1-i | r(n+1)-alpha |
| MIN basis, w(S)>=alpha | i | alpha |

The omitted eighth combination, MIN independent set with an upper
side budget and nonnegative objective, is solved by the empty set.
The allowed zero coefficient v_1=0 in the third row causes no issue.

For independent sets, the three bounds are respectively

\[
 w(S)+|S|\le\alpha+r,\qquad
 (n+1)|S|-w(S)\le r(n+1)-\alpha,\qquad
 w(S)-|S|\ge\alpha-r.
 \tag{FE18}
\]

Equality in each requires |S|=r and w(S)=alpha. For bases, cardinality
r is automatic and the remaining four bounds follow directly from
the corresponding side inequality. Thus in every row, attaining B
is equivalent to being a basis in H_alpha, which is equivalent to
decoding a satisfying assignment through FE10.

If phi is satisfiable, at least one such basis exists and OPT=B.
If phi is unsatisfiable, the instance remains feasible but every
feasible objective is at least one integer unit worse than B.
Unlike the single-hidden-basis oracle proof, uniqueness is unnecessary:
every basis attaining B certifies satisfiability.

All table values B are positive and Theta(n^2). For example,
alpha-r>=r(r-1)/2 and
r(n+1)-alpha>=r(r+1)/2, while the other bounds are immediate.
Choose the explicitly computable rational accuracy

\[
                         \varepsilon=\frac1{2B}.
 \tag{FE19}
\]

On a satisfiable MAX instance, a (1-epsilon) solution has integer
value at least B-1/2 and therefore exactly B. The convention
OPT/(1+epsilon) gives a strictly stronger bound than B-1/2 here.
On a satisfiable MIN instance, a (1+epsilon) solution has integer
value at most B+1/2 and therefore exactly B. On an unsatisfiable
instance, no legal solution has that value in either direction.

Run the approximation algorithm and compare its returned feasible
solution's exact objective with B. This decides phi. The numeric
data and the accuracy have polynomial encoding, and

\[
                    \varepsilon^{-1/2}=\sqrt{2B}
                              =\Theta(n)=\Theta(N).
 \tag{FE20}
\]

Thus FE2 would give a deterministic 2^{o(N)} poly(|phi|) SAT
algorithm, contradicting ETH. The same reduction applies to each
of the seven rows separately. It uses actual feasible output
solutions and exact side constraints; an algorithm allowed to
violate a budget or covering threshold is outside this claim.

## 8. Computational-model distinctions and limits

The unconditional companion lower bounds allow a hidden oracle and
therefore directly constrain even randomized query algorithms. The
present input instead supplies a polynomial-length rank program with
polynomial-time evaluation. Its full computation may be inspected,
so an information-theoretic query adversary alone would not prove
FE1 or FE2. SAT reduction and ETH provide the required computational
argument.

Every constructed instance is a valid matroid independently of the
formula's truth value. No difficult promise verification is delegated
to the optimization algorithm. The evaluator explicitly answers larger
query sets without finding a satisfying assignment.

This representation is not a matrix representation, graph, or laminar
family. The proof makes no lower claim for such more structured input
classes. Its fixed-d polynomial degree may depend on d; the separate
variable-d companion `conditional_lower_bound_encoded_target_matroids.md`
uses a different rankable family and proves its own target parameter
calibration.

The all-seven accuracy exponent remains a square root. In particular,
neither this conditional construction nor the unconditional hidden
family proves that exp(O(1/epsilon)) accuracy dependence is optimal.
The numeric target T and approximation accuracy 1/epsilon are linked
only by the specific unit-gap instances in Section 7.

## 9. Primary antecedents and bounded attribution

Doron-Arad, Kulik and Shachnai, *Lower Bounds for Matroid Optimization
Problems with a Linear Constraint*, ICALP 2024, full version
arXiv:2307.07773v2, Section 4, already constructs efficiently decoded
SAT-matroids. Definitions 4.4--4.5 and Lemma 4.6 put a SAT predicate
inside an equal-sum matroid while keeping membership polynomial.
Their polynomial enumeration of cardinality and sum parameters also
makes the one-dimensional numeric ETH parameter tracking natural.
The present proof is not the first encoded SAT-matroid construction.
Primary full text: <https://arxiv.org/html/2307.07773v2>.

Their Section 5 also announces an inverse-error quarter-power
exponential observation for the oracle approximation setting. The
square-root unit-gap table used here is proved explicitly in the
companion `single_matroid_accuracy_lower_bound_audit.md`; Section 7
above checks it again for the many-accepted-bases encoded construction.
The new quantitative statements are not attributed to the public
paper as displayed theorems.

Doron-Arad, Kulik and Shachnai, *You (Almost) Can't Beat Brute Force
for 3-Matroid Intersection*, arXiv:2412.02217v2, Section 3, gives
another public family parameterized by acceptable balanced subsets.
This reinforces the prior use of selected-subfamily paving
constructions; the present increment is the polynomial ranking of a
large fixed-dimensional equal-sum class and its explicit target and
accuracy calibration. Primary full text:
<https://arxiv.org/html/2412.02217v2>.

The ETH convention is that of the exponential-time work of Impagliazzo
and Paturi, *On the Complexity of k-SAT*, Journal of Computer and System
Sciences 62(2), 367--375, 2001. Primary publisher record:
<https://www.sciencedirect.com/science/article/pii/S0022000000917276>.
The variable-count subexponential framework is also discussed in
Impagliazzo, Paturi and Zane, *Which Problems Have Strongly Exponential
Complexity?*, JCSS 63, 512--530, 2001; the complete primary article
was checked at the institutional copy
<https://courses.cs.washington.edu/courses/cse599i/24sp/papers/ImpagliazzoPaturiZane_2001_jcss.pdf>.
The assumptions used in this note are explicitly stated before the
proof; no sparsification theorem is required by the reduction.

No publication-priority claim or extrapolation to particular explicit
matroid representations is made.
