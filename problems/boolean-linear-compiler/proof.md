# Exact Boolean optimization by interval and slack compilation

## 1. Compiler theorem

The input has $n$ Boolean variables, signed binary integer equalities, and interval rows $\ell_i\le a_i^\top x\le u_i$. Let $L$ be its binary length, $s_i=|\operatorname{supp}(a_i)|$, and $W_i=u_i-\ell_i$. Normalize one-sided rows against their attainable ranges and handle empty intervals and zero rows directly. Put
$$
\kappa_i=\min\{W_i+1,5s_i+1\},\quad q_i=\lceil\log_2\kappa_i\rceil,\quad Q=\sum_iq_i.
$$
Assume a deterministic Subset Sum backend returns indexed witnesses in time $\operatorname{poly}(L')2^{\alpha N}$, and, if supplied, writable space $\operatorname{poly}(L')2^{\sigma N}$. For any integer $0\le B\le Q$, the compiler gives
$$
T_B\le\operatorname{poly}(L)\left(\prod_i p_i\right)
2^{\alpha n+Q-(1-\alpha)B},\qquad
S_B\le\operatorname{poly}(L)2^{\sigma(n+B)},
$$
where $p_i\le4\lceil\log_2(W_i+1)\rceil+1$, and $p_i=1$ if $W_i\le5s_i$. Exact equalities contribute no slack parameter. Feasibility, indexed witnesses, linear optimization, and explicitly listed polynomial-size lexicographic optimization are supported.

## 2. Signed interval lemma

For one row, stop when the interval width is at most $5s$. Otherwise peel odd endpoints as singleton tests until both endpoints are even. Emit $[\ell,\ell+3s]$ and $[u-2s,u]$, then recurse with $a'_j=\lfloor a_j/2\rfloor$ on
$$
[(\ell+2s)/2,(u-2s)/2].
$$
For every Boolean assignment, even with signed coefficients,
$$
0\le a^\top x-2(a')^\top x\le s.
$$
This makes every recursive acceptance parent-feasible. A parent-feasible sum outside the two emitted boundaries has its rounded sum in the recursive interval. Induction proves exact disjunction assignment by assignment. At most two singleton endpoints and two boundary intervals occur per halving, proving the catalogue-size bound. Each emitted interval contains at most $\kappa_i$ integer values.

## 3. Slack and branch count

Choose $0\le b_i\le q_i$ summing to $B$. Split each catalogue interval into chunks of at most $2^{b_i}$ values. There are at most $2^{q_i-b_i}$ chunks, so the number of branch tuples is at most
$$
\left(\prod_i p_i\right)2^{Q-B}.
$$
For a positive-width chunk $[l,u]$, put $w=u-l$, $q=\lceil\log_2(w+1)\rceil\le b_i$. The $q$ weights
$$
1,2,\ldots,2^{q-2},\quad w-(2^{q-1}-1)
$$
have subset sums exactly $0,\ldots,w$. For $q=1$, the initial list is empty. The powers cover the initial interval; the final shift overlaps or abuts it and ends at $w$. Thus the chunk becomes one equality with at most $b_i$ Boolean slack variables. Different rows use different variables; width zero needs none. This is a witness reduction, not a parsimonious counting reduction.

## 4. Signed radix packing

For a branch with equations $c_j^\top y=t_j$ on $N\le n+B$ variables, use
$$
R=1+\max_j\left(\sum_k|c_{jk}|+|t_j|\right),\qquad
A_k=\sum_jc_{jk}R^j,\qquad T=\sum_jt_jR^j.
$$
Handle the all-zero system directly; otherwise $R\ge2$. The packed equation $\sum_kA_ky_k=T$ is equivalent to all branch equations. Indeed $d_j=c_j^\top y-t_j$ satisfies $|d_j|<R$. Reducing $\sum_jd_jR^j=0$ modulo $R$ forces $d_0=0$; divide and repeat. This proof permits signed digits.

The packed bit length is polynomial in $L$. Multiplying the branch bound by the backend cost at $n+B$ proves the time formula. Branches run sequentially with one backend workspace, proving the space formula. A witness is restricted to its original $n$ coordinates.

## 5. Optimization and backend conditions

Binary search over the polynomial-bit objective range uses polynomially many feasibility queries. Completely enumerate the short-target catalogue for the one added threshold row; its cost is polynomial and it adds no slack variables. Fix an optimum as an exact equality before treating the next lexicographic objective.

For a fixed number of interval rows, $Q=O(\log n)$ and $\prod_i p_i$ is polynomial in $L$, so the backend's separate time and space interfaces transfer up to polynomial factors. A time-only backend supplies no new simultaneous space bound. The refined numerical exponent additionally inherits its full-domain analytic contact premises; scalar exponent verification alone does not prove those premises.

## Complete proof

[Interval compiler, numerical instantiations, and primary source comparison](manuscripts/boolean-linear-optimization-compiler.md). Signed interval rounding is inherited from Nederlof–van Leeuwen–van der Zwaan and Bansal–Garg–Nederlof–Vyas; the theorem isolates the short-interval/slack interpolation.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
