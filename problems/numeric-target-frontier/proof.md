# Exact numeric targets and support-sensitive algorithms

Let $F$ be one normalized, monotone integral polymatroid rank on an explicit coordinate ground. Resource counts and ranks are binary encoded. Feasible vectors are integer points in $P(F)$, or in the original base face of total $F(E)$. Target rows have nonnegative integer coefficients; the separately optimized rational scalar may be signed.

The central theorem below proves the sharp two-parameter budget classification, including its constants and randomized rank-query lower bound. The following companion theorems give distinct refinements of the same exact resource-and-profile framework.

| Theorem | Bound, excluding polynomial work in the encoded input | Complete proof |
|---|---|---|
| Total target and original support patterns | $2^{O(T\log(2+\min\{Q/T,T\}))}$ | Sections 1–7 below |
| Fixed row dimension $d$ | $\exp(O_d((T+1)^{d/(d+1)}))$ | [Mixed targets](manuscripts/fixed-dimensional-mixed-numeric-targets.md) |
| Unequal positive auxiliary caps $U_j$ | $\exp((d+2(2^d-1))K(U))$, $K(U)=\max_{\varnothing\ne S}(\prod_{j\in S}U_j)^{1/(|S|+1)}$ | [Anisotropic bound, Section 9](manuscripts/fixed-dimensional-mixed-numeric-targets.md) |
| One integer objective and one scalar side constraint | $2^{O(\sqrt{T+1})}$; exact optimization uses $\mathrm{OPT}$ in place of $T$ | [Single objective](manuscripts/exact-numeric-target-single-matroid-scheme.md) |
| Seven single-resource approximation variants | $\epsilon^{-1}\exp(141/(50\epsilon)+7)$ | [Schemes](manuscripts/seven-variant-single-matroid-profile-scheme.md), [exact constant](manuscripts/refined-single-matroid-accuracy-constants.md) |
| Disjoint row supports | $\exp(3\sum_j\sqrt{U_j})\le \exp(3T)$ | [Support-one theorem](manuscripts/column-support-numeric-target-dichotomy.md) |
| At most two rows per column, $m$ interacting row pairs | $\exp(O(T\log(2+m/T)))$ | [Overlap density](manuscripts/row-overlap-density-numeric-target-refinement.md) |
| Component-sensitive and unequal-support counts | Product of component catalogue bounds; $\exp(\inf_{t>0}\Phi_U(t))$ for a prepared ground | [Components](manuscripts/component-sensitive-numeric-target-catalogues.md), [partition potential](manuscripts/support-sensitive-partition-potential-and-star-targets.md) |
| Connected star, $k$ unit-target leaves and center target $B$ | $\exp(O(k\log(2+B/k)))$ | [Star theorem](manuscripts/support-sensitive-partition-potential-and-star-targets.md) |
| Selected disjoint objective blocks | $\binom qr\exp(O(r\sqrt{T+1}))$ | [Block targets](manuscripts/block-global-exact-numeric-target-schemes.md) |
| Compressed nonlinear rows | The matching linear bound for convex upper rows, concave covers and linear equalities | [Aligned rows](manuscripts/aligned-nonlinear-mixed-numeric-targets.md), [overlap transfer](manuscripts/aligned-nonlinear-overlap-density-transfer.md) |
| Global allocation, scheduling and adaptive scenarios | Profile bounds with one shared resource in each scenario, exact budgets and original totals | [Global transfer](manuscripts/global-polymatroid-profile-transfers.md), [mandatory lift](manuscripts/mandatory-base-fair-allocation-passive-lift.md), [robust composition](manuscripts/global-robust-profile-composition.md) |

All algorithms use uniform polynomial binary workspace in the stated oracle or readable-program model. The fixed-dimensional and support-sensitive bounds are different analyses and retain their own parameters. In particular, the number of rows is not silently treated as constant in the two-parameter classification.

The recovery mechanism is shared: a streamed multiplicity profile fixes the totals of coefficient classes; one partition-count polymatroid enforces those totals, and its intersection with the one shared resource rank is integral. A mandatory base keeps its original total throughout masks and lifts. Optional disposal is added only for an originally optional problem. Real zero-coefficient coordinates retain their actual scalar costs.

## Main theorem: a sharp budget classification

This note combines the original-support upper bound with the total-target upper bound, and calibrates two different hidden-matroid families to every sufficiently large pair of parameter budgets. The result is a worst-case classification under upper bounds on the parameters. It does not assert a lower bound for every exactly prescribed pair of parameter values, or for every individual instance.

Throughout this note, logarithms have base two. For positive real numbers define

$$
f(t,q)=t\log_2\!\left(2+\min\{q/t,t\}\right).
 \tag{BC1}
$$

## 1. Model and the classification

Use the model of [unrestricted-support-pattern-numeric-targets.md](manuscripts/unrestricted-support-pattern-numeric-targets.md) (UP) and [variable-dimension-total-target-classification.md](manuscripts/variable-dimension-total-target-classification.md) (VT): one normalized monotone integral polymatroid on an explicit ground, integer points in its independent-set polytope or its original base polytope, explicit nonnegative integer rows with relations in $\{\le,=,\ge\}$, and one arbitrary rational scalar objective to minimize or maximize exactly. Resource counts and ranks are binary encoded. Scalar coefficients may have either sign. Original mandatory totals must be retained, and optional disposal is used only for an originally optional independent-set problem.

Let $T$ be the sum of the row targets. Following the exact zero-target and eligibility preparation in UP, let $Q$ count the distinct nonempty positive supports of the original eligible columns. Repeated supports count once even if their coefficient values differ. The scalar objective is not included in these supports. Let $H$ be the complete binary input size, with polynomially implemented rank, submodular minimization and weighted intersection operations charged.

There is a deterministic exact algorithm, including infeasibility detection, using

$$
2^{O(f(T,Q))}\mathrm{poly}(H)
 \tag{BC2}
$$

time and uniform polynomial binary workspace whenever $T,Q>0$. The cases $T=0$ or $Q=0$ are polynomial.

Conversely, for every pair of integers

$$
t\ge512,\qquad q\ge1,
 \tag{BC3}
$$

there is a family of rank-oracle instances whose actual parameters satisfy $T\le t$ and $Q\le q$, whose common explicit non-oracle data have size polynomial in $t$, and on which exact feasibility has worst-case rank-query complexity at least

$$
2^{f(t,q)/256}.
 \tag{BC4}
$$

This applies to any randomized algorithm with success probability at least $2/3$ on every instance and a bounded worst-case number of queries. It therefore also applies to deterministic exact algorithms. Ordinary matroid ranks, equality rows, scalar zero, and coefficients in $\{0,1,2\}$ suffice. The construction works separately for mandatory bases and optional independent sets.

Together BC2 and BC4 establish the exponential order $2^{\Theta(f(t,q))}$ in the worst case over the parameter-budget class, up to polynomial factors. The constants are uniform in the row count, the column arity, and the budgets.

## 2. Upper bound and monotonicity in the budgets

UP gives an exact algorithm with exponent $O(T\log_2(2+Q/T))$, uniformly in the row count and column arity. VT gives exponent $O(T\log_2(T+2))$ for positive integral $T$. Run the two algorithms by alternating simulation steps and stop when the first finishes. Both outputs are exact, so this costs at most twice the faster running time and stores two polynomial-space states. Consequently the exponent is

$$
\begin{aligned}
 &O\!\left(\min\{T\log_2(2+Q/T),\ T\log_2(T+2)\}\right)\\
 &\hspace{35mm}=O(f(T,Q)).
\end{aligned}
 \tag{BC5}
$$

No exponential expression needs to be computed or stored by the algorithm.

The function $f$ is nondecreasing in each coordinate. Monotonicity in $q$ is immediate. For fixed $a>0$, the derivative of $x\ln(2+a/x)$ is

$$
\ln(2+z)-\frac{z}{2+z}>0,
                    \qquad z=a/x\ge0.
 \tag{BC6}
$$

Indeed this expression is $\ln2$ at zero and has derivative $z/(2+z)^2\ge0$ in $z$. Also $x\ln(x+2)$ is increasing. The minimum of these two increasing functions is increasing. Thus $T\le t,Q\le q$ implies $f(T,Q)\le f(t,q)$, giving the claimed upper bound for the whole budget class.

For $T=0$, zero-target preprocessing leaves only masks and scalar optimization. If $Q=0$ and positive targets remain, every eligible column is zero in every row. A positive equality or covering target is then impossible; upper rows are automatic. Scalar optimization on the remaining resource is polynomial. These cases do not use the expression $Q/T$.

## 3. A common hidden-matroid lemma

Let $\mathcal H$ be a family of $r$-subsets of a finite ground such that no two different members differ by a single-element exchange. Assume some $r$-subset is outside $\mathcal H$. A reference matroid permits every set of size below $r$, and permits an $r$-subset as a base exactly when it is outside $\mathcal H$. For a chosen hidden $A\in\mathcal H$, also permit $A$.

These are matroids. Heredity is immediate. The only nontrivial augmentation case has an independent $(r-1)$-set and an independent $r$-set. If there is just one candidate added element, the resulting set is the given larger independent set. If there are at least two, the resulting $r$-subsets are pairwise single-exchange neighbors; at most one is forbidden. Thus an augmentation exists. The assumed outside set establishes rank $r$.

The hidden and reference rank oracles differ only on $A$. A smaller set has its cardinality as rank. A larger set contains two adjacent $r$-subsets, at least one of which is a base in every instance. At size $r$, only the status of $A$ changes.

Suppose the target equalities are infeasible in the reference instance and have unique feasible set $A$ in its hidden instance. Let $\mathcal G\subseteq\mathcal H$ contain $N$ possible hidden sets. Under the distribution giving probability one half to the reference and one half to a uniformly chosen hidden instance, a deterministic algorithm making at most $D$ queries succeeds with probability at most

$$
\frac12+\frac{D}{2N}.
 \tag{BC7}
$$

To see this, follow the reference transcript. Its queries name at most $D$ hidden candidates; all other hidden inputs give the same transcript. If the final answer is NO, only queried hidden inputs can contribute additional successes beyond the reference half. If it is YES, the total success is at most the hidden half plus any possible gain on the queried inputs, which is bounded by the same expression. Averaging over random coins proves the randomized bound. Success at least $2/3$ on every input therefore requires $D\ge N/3$.

The following two constructions use this lemma. Their rank queries have ordinary explicit subsets as inputs and polynomial-bit rank outputs. They do not provide an uncharged stronger oracle.

## 4. Low support-pattern budgets

Suppose $t\ge8$ and $q/t\le4$. Choose the largest integer $h\ge1$ such that

$$
r=2^h,\qquad T_h=r(3h+1)\le t.
 \tag{BC8}
$$

Use the one-support construction OS, recalled here to fix its parameter accounting. The ground is $E=\{1,2\}^{2h}$, with $|E|=r^2$. Each of the $2h$ label coordinates is an equality row with target $3r/2$. Add an all-ones cardinality equality with target $r$. Every column has the same full nonempty support, so $Q=1\le q$, and the total target is precisely $T_h$.

Let $\mathcal H$ contain all balanced $r$-subsets, meaning those with label sum $(3r/2,\ldots,3r/2)$. Distinct labels imply that two members cannot be single-exchange neighbors. There is an outside reference base: choose $r$ labels with first coordinate one, possible because $r^2/2\ge r$.

Pair each label $u$ with its complement $3-u$. Taking any $r/2$ of these $r^2/2$ pairs gives a balanced candidate, so use the candidate family of size

$$
N=\binom{r^2/2}{r/2},\qquad
       \log_2N\ge\frac{rh}{2}\ge\frac{T_h}{8}.
 \tag{BC9}
$$

The binomial lower bound follows from $\binom{M}{k}\ge(M/k)^k$. The cardinality equality forces full rank even for the optional independent-set problem. Hence the reference is infeasible and the hidden instance has exactly its restored candidate as a feasible set.

The consecutive target sizes satisfy

$$
\frac{T_{h+1}}{T_h}
       =2\frac{3h+4}{3h+1}
       \le\frac72.
 \tag{BC10}
$$

Maximality in BC8 yields $T_h>2t/7$, and thus $\log_2N>t/28$. In this regime
$f(t,q)\le t\log_2 6<3t$, giving

$$
\log_2N>f(t,q)/84.
 \tag{BC11}
$$

The ground has at most $t^2$ elements and $O(\log t)$ rows. Every non-oracle datum has polynomial total size in $t$, independently of how large the stated budget $q$ is.

## 5. Higher support-pattern budgets

Suppose $q/t>4$ and $t\ge16$. Set

$$
\begin{split}
 b&=2\min\{\lfloor q/t\rfloor,\lfloor t/4\rfloor\},\\
 L&=\lfloor t/b\rfloor,\qquad t'=Lb.
 \end{split}
 \tag{BC12}
$$

These quantities can be formed with integer arithmetic. The integer $b$ is even and satisfies $8\le b\le t/2$. Also $t/2\le t'\le t$.

Take $L$ disjoint cliques on $b$ vertices. The ground consists of their edges. There is one equality row per vertex, with edge-incidence coefficients and target one. Its total target and support count are

$$
T=t',\qquad
 Q'=L\binom b2=\frac{t'(b-1)}2
                    \le\frac{tb}{2}\le q.
 \tag{BC13}
$$

Every edge has its own two-element positive support. Let the one global resource matroid have rank $r=t'/2$, and let $\mathcal H$ be all perfect matchings of this graph. Equalities force a perfect matching, including in the optional formulation. Distinct edge-incidence columns make $\mathcal H$ nonadjacent under one-element exchange. An outside $r$-set exists: from a perfect matching, replace one edge by an edge sharing an endpoint with a different retained matching edge inside its clique. The reference/hidden construction therefore applies with

$$
N=((b-1)!!)^{L}.
 \tag{BC14}
$$

This is a single hidden global matroid, not a direct sum of independently queried resource matroids.

For $b\ge8$, at least $\lfloor b/4\rfloor\ge b/8$ factors of $(b-1)!!$ are at least $b/2$, and $\log_2(b/2)\ge\tfrac12\log_2b$. Hence

$$
\log_2((b-1)!!)\ge\frac{b}{16}\log_2b.
 \tag{BC15}
$$

Write $x=q/t$, $z=\min\{x,t\}$, and $a=\min\{x,t/4\}$. Then $a\ge4$, $z\le4a$, and $b=2\lfloor a\rfloor\ge a$. It follows that $2+z\le4b+2\le5b\le b^2$, so
$\log_2b\ge\tfrac12\log_2(2+z)$. Combining this with BC12 and BC15 gives

$$
\log_2N
   \ge\frac{t'}{16}\log_2b
   \ge\frac{t}{32}\log_2b
   \ge\frac{f(t,q)}{64}.
 \tag{BC16}
$$

There are at most $t^2/4$ ground elements and at most $t$ rows, with binary coefficients. The full explicit matrix and all other non-oracle data are polynomial in $t$.

## 6. Uniform lower constant and precise scope

The two regimes give the convenient common bound

$$
N\ge2^{f(t,q)/128}.
 \tag{BC17}
$$

For $t\ge512$, one has $f(t,q)\ge t\ge512$. Thus $2^{f(t,q)/256}\ge4>3$, and BC7 implies

$$
D\ge N/3\ge2^{f(t,q)/256},
 \tag{BC18}
$$

as claimed. This also explains why a polynomial factor in the explicit input size cannot absorb the lower bound: all constructed non-oracle encodings have size polynomial in $t$, while $f(t,q)\ge t$.

The quantifiers are over a family with common explicit data and varying rank oracle. For each budget pair, any algorithm correct for the class has a hard instance in that family. The assertion is not that one fixed, publicly identified instance is hard for every algorithm.

The budgets need not be attained exactly. In particular the lower construction deliberately uses $Q=1$ throughout the low-budget regime, and uses whole even cliques in the high-budget regime. This is sufficient and necessary for the stated worst-case envelope; it is not an exact-pair classification. It also makes no instancewise hardness claim for easy subclasses such as modular resources.

This theorem is unconditional in the rank-oracle model. The separately proved encoded rank-program/circuit reductions in OS and [encoded-overlap-density-eth-lower-bound.md](manuscripts/encoded-overlap-density-eth-lower-bound.md) give ETH exclusions along their calibrated parameter families. They are not being promoted here to an encoded ETH assertion for every arbitrary numerical budget pair. Likewise, the result does not turn an oracle lower bound into hardness for a more restrictive explicit matroid representation.

## 7. Dependencies and contribution

The upper bound uses the complete UP and VT algorithms without changing their proofs, mandatory-total conventions, or polynomial-space guarantees. The lower families are the reviewed one-support construction OS and the reviewed disjoint-clique construction RD/ED. The new work is the all-budget calibration, the uniform constants, the monotonicity needed to pass from actual parameters to budgets, and the precise matching worst-case envelope.

The upper-bound algorithms and the two lower constructions are proved in the companion manuscripts. The calibration above establishes a worst-case classification under parameter budgets; it does not assert an exact-pair or representation-independent lower bound.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
