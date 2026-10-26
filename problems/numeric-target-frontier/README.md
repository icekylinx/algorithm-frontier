# Numeric targets and support-sensitive optimization

Exact feasibility and signed-scalar optimization under one global integral polymatroid, with bounds that retain target size and support geometry.

| Field | Result |
|---|---|
| **Objective and output** | Decide nonnegative integer upper, equality and covering targets; return an attaining integer vector for the exact minimum or maximum of one rational scalar. Approximation variants specify their own direction. |
| **Time** | For total target $T>0$ and $Q>0$ distinct original nonempty eligible-column supports: $2^{O(T\log(2+\min\{Q/T,T\}))}\operatorname{poly}(H)$. Cases $T=0$ or $Q=0$ are polynomial. The table below gives distinct refinements. |
| **Space** | Uniform polynomial binary workspace, including infeasible instances. |
| **Parameters** | $T=\sum_jT_j$; $Q$ counts distinct supports, not coefficient values; $d$ is row dimension; $H$ includes the full binary input and charged polynomial oracle work; $H_\epsilon$ also includes the rational accuracy. |
| **Model and representation** | One normalized monotone integral polymatroid, with exact rank access or a readable implementation of that rank. Counts and capacities are binary encoded. Each row states optional-vector or original-total-base feasibility. The scalar may be signed. |
| **Lower-bound scope** | For every budget pair $t\ge512,q\ge1$, a rank-oracle family with $T\le t,Q\le q$ requires at least $2^{t\log_2(2+\min\{q/t,t\})/256}$ queries, including bounded-error randomized decision. Separate ETH results use readable rank programs; they are not hardness claims for every explicit matroid class. |
| **Review status** | The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed. |
| **Source** | [Main theorem and proof](proof.md), [all companion manuscripts and primary sources](sources.md). |

## Results

Each time bound includes $\operatorname{poly}(H)$ unless another input size is shown.

| Structure or objective | Guarantee and time |
|---|---|
| Arbitrary row count and support | $2^{O(T\log(2+\min\{Q/T,T\}))}$; matching worst-case rank-query order under parameter budgets. |
| Fixed dimension $d$ | $\exp(O_d((T+1)^{d/(d+1)}))$; matching exponent on balanced-target oracle families. |
| Unequal positive auxiliary caps $U_j$ | $\exp((d+2(2^d-1))K(U))$, where $K(U)=\max_{\varnothing\ne S}(\prod_{j\in S}U_j)^{1/(|S|+1)}$. For two caps: $\max\{\sqrt{U_1},\sqrt{U_2},(U_1U_2)^{1/3}\}$. |
| Single integer objective, one exact scalar side condition | Target decision in $2^{O(\sqrt{T+1})}$; exact optimization in $2^{O(\sqrt{\mathrm{OPT}+1})}$. |
| Seven single-resource approximation variants | A $(1-\epsilon)$ maximum or $(1+\epsilon)$ minimum, with exact side constraint, in $\epsilon^{-1}\exp(141/(50\epsilon)+7)\operatorname{poly}(H_\epsilon)$. |
| At most one target row per column | $\exp(3\sum_j\sqrt{U_j})\le e^{3T}$, where upper/equality rows use $U_j=T_j$ and covering rows use $U_j=2T_j-1$. |
| At most two target rows per column | $\exp(O(T\log(2+m/T)))$ for $m$ distinct interacting row pairs. Dense instances give the $T\log T$ oracle boundary. |
| Disconnected support geometry | Product of the component partition bounds; the resource recovery remains one global problem. |
| Unequal targets and actual support family $\mathcal S$ | Profile count at most $\exp(\inf_{t>0}\Phi_U(t))$, with $\Phi_U(t)=\sum_jU_jt_j+2\sum_{A\in\mathcal S}\prod_{j\in A}(e^{t_j}-1)^{-1}$. Any required cover-lift preparation is charged separately. |
| Connected star, $k$ unit leaves and center target $B$ | $\exp(O(k\log(2+B/k)))$ when every nonzero column touches a leaf. Matching-order oracle and encoded-ETH families are provided. |
| Selected disjoint objective blocks | $\binom qr\exp(O(r\sqrt{T+1}))$ for an actual rank-$r$ selected basis; the integer grid is part of the parameter. |
| Global allocation and scheduling | Allocation $\binom qr\exp(O(r/\epsilon))$; mandatory scheduling $\exp(O(q/\epsilon))$; six-profile $3/2$ endpoint $6^q$. Exact shared budgets and original totals are retained. |
| Mandatory fair allocation and adaptive scenarios | Charged active/passive copies retain all units and costs; a common selection is combined with separate scenario assignments. |
| Compressed nonlinear utility, cost and load | Polynomially many binary-length marginal bands preserve the corresponding linear profile bounds. |
| Aligned nonlinear numeric rows | Convex upper rows, concave covering rows and linear equalities inherit the linear exact bound; overlap is measured on the refined band columns. |

Zero-coefficient coordinates retain their actual costs and resource contributions. Optional disposal is added only to an originally optional problem. The numeric parameter is the integer target, not its encoding length or approximation accuracy.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
