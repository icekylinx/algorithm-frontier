# Unrelated-value allocation with an exact budget and a fractional comparator

## 1. Model and theorem

Let $`P`$ be an explicit set of $`q`$ players. For a normalized monotone
integral submodular rank $`f`$, write

```math
P(f)=\{x\in\mathbb R_{\ge0}^{P}:x(S)\le f(S)\text{ for every }S\subseteq P\}.
```

Resource type $`j`$ has rank $`f_j`$. Its integer allocation is a vector
$`x_j\in P(f_j)\cap\mathbb Z^P`$; unused units are allowed. Pair $`(p,j)`$
has nonnegative rational value $`v_{pj}`$ and cost $`a_{pj}`$. One budget is

```math
\sum_{p,j}a_{pj}x_j(p)\le C,\qquad C\ge0. \tag{U1}
```

Let $`\mathcal B`$ be a nonempty family of $`r`$-element player sets,
$`1\le r\le q`$. A paid polynomial-time restriction selector finds a
member contained in any specified $`Q\subseteq P`$, or correctly reports
that none exists. A matroid-basis family is the principal example. Put
$`c=q-r`$. All resource ranks, costs and values remain fixed when the
selector is restricted. Eligibility masks are incorporated before the
algorithm starts.

For fixed $`I\in\mathcal B`$, let $`\lambda_I`$ be the optimum common
utility with fractional resource counts, zero assignments outside $`I`$,
and budget (U1). Define

```math
\mathrm{FOPT}=\max_{I\in\mathcal B}\lambda_I,\qquad
 u_p=\max\bigl(\{v_{pj}:f_j(\{p\})\ge1\}\cup\{0\}\bigr),\qquad
 u=\max_pu_p. \tag{U2}
```

The selected set in FOPT is an actual member of $`\mathcal B`$; only the
resource counts are relaxed. Thus FOPT is at least the integer optimum
OPT. Put $`\Gamma(R)=R^R/(R-1)^{R-1}`$ for $`R>1`$.

**Theorem U.** For every rational $`0<\varepsilon<1`$, a deterministic
algorithm returns $`I\in\mathcal B`$ and an integer allocation obeying
(U1), such that

```math
\sum_jv_{pj}x_j(p)\ge
 \max\{0,(1-\varepsilon)\mathrm{FOPT}-u_p\}\qquad(p\in I). \tag{U3}
```

Its time is

```math
\Gamma(1/\varepsilon)^c\mathrm{poly}(H), \tag{U4}
```

and its workspace is polynomial in $`H`$. Here $`H`$ includes the full
binary input and accuracy, oracle-answer lengths, and the paid costs of
exact rank, submodular minimization, restriction selection, rational LP
and weighted polymatroid-intersection operations. These polynomial
bounds are uniform in $`c`$ and $`\varepsilon`$.

For fixed rational $`\varepsilon`$, the same guarantee also has time

```math
\left(2-\Gamma(1/\varepsilon)^{-1}\right)^q
 2^{O(q\log\log(q+2)/\log(q+2))}\mathrm{poly}(H). \tag{U5}
```

The unbudgeted theorem is the specialization $`a_{pj}=C=0`$. The guarantee
against OPT follows from FOPT $`\ge`$ OPT. Both comparators use the full
requested accuracy in the exponent.

## 2. Exact separation of one fixed service region

Define

```math
\mathcal X_C=\{(x_j)_j:x_j\in P(f_j),\
                              \sum_{p,j}a_{pj}x_j(p)\le C\},
 \qquad
 \mathcal U_C=\{z\ge0:\exists x\in\mathcal X_C,\
                           z_p\le\sum_jv_{pj}x_j(p)\ (p\in P)\}. \tag{U6}
```

These are compact rational polytopes; $`\mathcal U_C`$ contains zero and
is downward closed. Every resource coordinate is bounded by its singleton
rank. Resource separation minimizes $`f_j(S)-x_j(S)`$; the other rows
are explicit. Exact rational LP tests service membership and reconstructs
a fractional allocation in polynomial oracle time. A restriction query
has zero service outside $`Q`$ on the original ground. Resources are
neither contracted nor redefined.

**Lemma 1 (nonnegative separation).** A nonnegative query outside
$`\mathcal U_C`$ has an exactly computable polynomial-bit strict separator
$`a\cdot z\le h_C(a)`$, with $`a\ge0`$ and $`h_C(a)\ge0`$.

**Proof.** For $`a\ge0`$, optimize

```math
h_C(a)=\max_{x\in\mathcal X_C}\sum_{p,j}a_pv_{pj}x_j(p).
```

The support optimizer may be chosen at a vertex by lexicographic
refinement. All such vertices have uniform polynomial bit length:
resource rows have zero-one coefficients and encoded integral right
sides, the budget has original rational data, and a vertex uses at most
the ambient number of independent active rows.

Let $`V=\sum_j f_j(P)\max_pv_{pj}`$. For the query $`z`$, solve

```math
\max\left\{a\cdot z-h:\ a\ge0,\ a(P)=1,\ 0\le h\le V,\
 h\ge\sum_{p,j}a_pv_{pj}x_j(p)
                       \text{ for every vertex }x\text{ of }\mathcal X_C\right\}.
 \tag{U7}
```

The inner support problem separates the last row family with
polynomial-bit inequalities. At an optimum $`h=h_C(a)`$, so a positive
optimum supplies the required row. Conversely, strong separation of
$`z\ge0`$ from a compact downward region gives a nonnegative normal:
replace negative coordinates of a signed separator by zero. Downward
closure preserves the support value, while the queried scalar product
cannot decrease. Normalize its nonzero positive part to sum one.
Thus an external query has positive optimum in (U7); a nonpositive
optimum certifies membership. The argument covers zero budgets and
lower-dimensional service polytopes. $`\square`$

## 3. The fixed-target selection gap

Set $`\alpha=1-\varepsilon`$. Apply the
[weighted omission theorem](../whole-ground-allocation/selection.md)
with full service $`t=T>0`$ and relaxed service $`b=\alpha T`$. Its ratio
is $`t/(t-b)=1/\varepsilon`$. Lemma 1 supplies the separator and the
given restriction selector supplies the fixed-cardinality family.

The routine returns an actual $`I\in\mathcal B`$ with
$`\alpha T\mathbf1_I\in\mathcal U_C`$, or fails only when no permitted
set supports full target $`T`$. Its all-input time is (U4), including
failed restrictions. Indeed, a violated row at $`Q`$ and a protected
full-target set $`I^*\subseteq Q`$ satisfy

```math
T a(I^*)\le h<\alpha T a(Q),\qquad
                      a(Q\setminus I^*)>\varepsilon a(Q).
```

Ordering the nonnegative weights forces a first prefix whose omitted
density exceeds $`\varepsilon`$. Prefix-free certificate enumeration
has branch sum $`\sum_D\Gamma(1/\varepsilon)^{-|D|}\le1`$, and one deletion
preserves $`I^*`$. The cited theorem proves the complete enumeration
and polynomial-space bounds. A successful nominal $`T`$ need not itself
be fully feasible.

## 4. Exact reoptimization preserves the fractional comparator

For each permitted set the original, target-independent LP is

```math
\begin{aligned}
 \max\;&\lambda,\\
 x_j&\in P(f_j),\qquad x_j(p)=0\quad(p\notin I),\\
 \sum_jv_{pj}x_j(p)&\ge\lambda\quad(p\in I),\\
 \sum_{p,j}a_{pj}x_j(p)&\le C,\qquad 0\le\lambda\le V .
 \end{aligned} \tag{U8}
```

It is bounded, nonempty and exactly optimizable. Let $`n`$ bound its
dimension and let $`2^L`$ uniformly bound the numerator and denominator
magnitudes of its row data. Polynomial $`n,L`$ are computed from the
original data and full ranks. Clearing denominators row by row bounds
integer entries by $`W=2^{(n+2)L}`$. Cramer's rule gives the uniform
denominator bound $`D=n!W^n`$ for every $`\lambda_I`$; $`D`$ has polynomial
binary length. Boundedness ensures a vertex also on lower-dimensional
feasible faces. Since $`\mathcal B`$ is finite, FOPT is one of these optima.

Write $`\alpha=A/B`$ in lowest terms and use grid
$`\delta=1/(2BD^2)`$. Start at lower target zero with any permitted set,
and an external upper grid target above $`V`$. On a midpoint success
save the returned set and raise the lower endpoint; on failure lower
the upper endpoint. Every failed upper endpoint remains strictly above
FOPT. At adjacent endpoints the saved set obeys

```math
L>\mathrm{FOPT}-\delta,\qquad
                  \lambda_I\ge\alpha L. \tag{U9}
```

Reoptimize (U8) for this set. If $`\lambda_I<\alpha\mathrm{FOPT}`$,
their denominator bounds imply

```math
\alpha\mathrm{FOPT}-\lambda_I
                            \ge 1/(BD^2)=2\delta,
```

contradicting (U9). Therefore $`\lambda_I\ge\alpha\mathrm{FOPT}`$.
There are polynomially many target calls, of polynomial bit length,
without enumerating $`D`$. FOPT $`=0`$ is included. The
[rational optimization lemma](../whole-ground-allocation/rational-optimization.md)
gives the general form of this argument.

## 5. One integral rounding preserves every prefix and the cost

Restrict the fractional optimum to its fixed set $`I`$. For each resource
write $`f=f_j|I`$, $`n=f(I)`$, add a disposal coordinate $`0`$, and define

```math
\widehat f(S)=
 \begin{cases}f(S),&0\notin S,\\n,&0\in S.\end{cases} \tag{U10}
```

This is normalized, monotone, integral and submodular. Adding disposal
$`n-x_j(I)`$ completes the independent vector to a base without changing
any real assignment or cost. On the augmented ground $`E`$, put

```math
d_e=\widehat f(\{e\}),\qquad
 g(S)=\widehat f(E\setminus S)+d(S)-n.
```

The rank $`g`$ is integral and submodular. It is monotone because every
marginal of $`\widehat f`$ is at most the corresponding singleton
$`d_e`$. Base complementation gives the bijection

```math
y=d-\widehat x\in B(g)
             \quad\Longleftrightarrow\quad
                  \widehat x\in B(\widehat f). \tag{U11}
```

At each player order its type coordinates by nonincreasing value.
For each prefix $`S_h`$, including the full prefix, impose
$`y'(S_h)\le U_h=\lceil y(S_h)\rceil`$. These are the independence
inequalities of the integral chain polymatroid with rank
$`R(A)=\max\{U_h:e_h\in A\}`$ for nonempty $`A`$, and empty rank zero.
Give disposal coordinates their singleton caps. Take the direct sum
of these chains and disposal groups.

Intersect this side with the direct sum of the complement resources.
Its maximum-total face at $`\sum_jg_j(E_j)`$ contains the fractional
$`y`$ and is integral. Maximize the actual assignment coefficients
$`a_{pj}`$ on this face, giving disposal coefficient zero, and choose
an integral optimizer $`y'`$. Full total forces every resource
component to remain a base. Complement and discard disposal. The
result is a legal integer original allocation of no greater cost,
since $`a\cdot d`$ is constant and $`a\cdot y'\ge a\cdot y`$.

Every player prefix satisfies

```math
x'(S_h)\ge d(S_h)-\lceil d(S_h)-x(S_h)\rceil
                              =\lfloor x(S_h)\rfloor. \tag{U12}
```

For decreasing values $`v_1\ge\cdots\ge v_m\ge0`$, put $`v_{m+1}=0`$.
Summation by parts yields

```math
\sum_i v_i x'_i
 \ge\sum_h(v_h-v_{h+1})\lfloor x(S_h)\rfloor
 \ge\sum_i v_i x_i-v_1. \tag{U13}
```

Here $`v_1\le u_p`$. Combining (U9)--(U13) proves (U3), with its maximum
with zero following from nonnegative utility. This construction
optimizes one scalar cost on an integral face; it does not assume that
a budget halfspace preserves integrality. It adds one disposal coordinate
per resource, and every count stays binary encoded.

## 6. Time, global conversion and scope

The selection gap dominates the polynomial LP, target-search and
rounding work, proving (U4) and polynomial workspace. After forced
omissions $`Z`$, a full witness avoiding $`Z`$ still survives and the
remaining deficit is $`c-|Z|`$. The
[streamed global conversion](../whole-ground-allocation/global-conversion.md)
therefore gives (U5) for fixed rational accuracy. Target optimization
and rounding remain unchanged. For varying binary accuracy, the safe
rational upper bound $`A=3/\varepsilon>\Gamma(1/\varepsilon)`$ gives
the uniform global base $`2-\varepsilon/3`$.

The restriction family may comprise common bases of two matroids with
one fixed selection-cost threshold, when weighted matroid intersection
implements its selector. That selection threshold is distinct from
(U1). Several independent exact assignment budgets are not preserved
by the single rounding objective.

The guarantee remains additive. Without controlling $`u`$ relative to
the comparator it need not imply a positive multiplicative ratio.
Pairs with whole-unit cost larger than $`C>0`$ remain in the fractional
LP because fractional use can contribute to FOPT. When $`C=0`$, positive
cost coordinates can instead be masked out exactly.

Cost-preserving additive allocation rounding has public antecedents in
[Rohwedder, Rouhani and Wennmann, ICALP 2025](https://doi.org/10.4230/LIPIcs.ICALP.2025.127).
The proof above supplies its recipient-polymatroid, exact-budget,
selection and rational-comparator composition.

---

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
