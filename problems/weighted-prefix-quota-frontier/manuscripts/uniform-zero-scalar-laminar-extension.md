# Uniform scalar coefficients on optional zero-weight coordinates

**25 October 2026. Complete incremental extension of [laminar-common-weight-root-cap-fpt.md](laminar-common-weight-root-cap-fpt.md); full internal mathematical reviews completed for checkpoint T. The stronger nonuniform-cost companion is [laminar-valuated-zero-completion-fpt.md](laminar-valuated-zero-completion-fpt.md).**

The LM theorem already permits an arbitrary common scalar coefficient on zero-weight coordinates of a mandatory base. This note proves the analogous extension for an optional independent vector. The added point is that an optional optimum need not have full original resource rank: its best zero completion is expressed by a contraction rank that replacements preserve monotonically.

## 1. Statement and the easy sign

Use the global integral polymatroid, common-weight laminar rows, root cap $B$, and exact rational scalar objective of LM. The resource here is optional: $x\in P(F)\cap\mathbb Z^E$. Write $P=\{e:w_e>0\}$, $Z=\{e:w_e=0\}$, and suppose

$$
c_z=\gamma\in\mathbb Q
                               \quad(z\in Z).
\tag{UZ1}
$$

Positive-weight coordinates may have arbitrary signed rational scalar coefficients. Then exact feasibility and scalar optimization still have deterministic running time

$$
2^{O(B^2\log(B+1))}\mathrm{poly}(H)
\tag{UZ2}
$$

and uniform polynomial binary space, independent of the number of laminar nodes in the exponent.

If minimizing with $\gamma\ge0$, or maximizing with $\gamma\le0$, omit all zero-weight units. Downward closure preserves feasibility and cannot worsen the scalar. This is the positive-coordinate LM problem, with the original positive coefficients $c_e$. Thus only minimization with $\gamma<0$, or maximization with $\gamma>0$, requires a new argument. Call these the favorable signs.

## 2. The exact optional completion value

For a resource-feasible positive vector $x$, use the same residual rank as LM:

$$
h_x(A)=\min_{C\subseteq P}\bigl(F(A\cup C)-x(C)\bigr),
                              \qquad A\subseteq Z.
\tag{UZ3}
$$

It is a normalized integral polymatroid rank, and $P(h_x)$ is exactly the set of zero completions compatible with $x$. Let

$$
g(C)=F(C\cup Z)-F(Z),
 \qquad
 q(S)=\min_{C\subseteq P}\bigl(g(C)+x_S(P\setminus C)\bigr)
\tag{UZ4}
$$

be the natural contraction-matroid rank on positive copies. For a set $S$ representing $x$,

$$
h_x(Z)=F(Z)+q(S)-|S|.
\tag{UZ5}
$$

For either favorable sign, a best zero completion has the maximum possible total $h_x(Z)$. An integral greedy base of $h_x$ constructs one with binary counts. Therefore the best true scalar attainable from $S$ is

$$
\Phi(S)=\gamma F(Z)
           +\sum_{e\in P}(c_e-\gamma)x_S(e)
           +\gamma q(S).
\tag{UZ6}
$$

This expression does not require $S$ to span the contraction matroid. Its full rank $F(E)-F(Z)$ may be larger than $B$. In particular, the mandatory rejection rule $F(E)-F(Z)>B$ is **not** applied in this optional extension.

The rank in UZ4 is evaluated by submodular minimization on the original coordinate ground. For every currently selected set, $q(S)\le |S|\le B$, regardless of that matroid's full rank.

## 3. Preserving current contraction rank under replacement

Use the same candidate classes as LM: common positive weight, common lower-row membership, and common loop/nonloop status in the contraction matroid $Q$. Give a copy the adjusted coefficient $c_e-\gamma$, negated for a minimization representative score and unchanged for maximization.

Fix a feasible positive set $S$ and a selected copy $e$, and put $S^-=S-e$, $\rho=q(S)$. Resource independence and the disjoint maximal upper-blocker tests are exactly as in LM. Only the meaning of the $Q$-test changes.

If $e$ is a $Q$-loop, deletion does not change $\rho$, and a same-class replacement is also a loop. Omit the $Q$-test.

If $e$ is a nonloop and $q(S^-)=\rho$, use the empty $Q$-test. The target passes it because it is a nonloop, and adding any replacement cannot reduce the already attained rank $\rho$.

If $q(S^-)<\rho$, the one-element rank change implies $q(S^-)=\rho-1$. Choose a $Q$-basis $D\subseteq S^-$ as the test. Its size is at most $|S|-1\le B-1$, and $e\notin\mathrm{cl}_Q(D)$. A replacement outside that closure restores rank $\rho$.

Thus the same separate-test representative lemma returns a no-worse adjusted-score replacement with

$$
q(S-e+f)\ge q(S).
\tag{UZ7}
$$

The total independent-test rank remains at most $3B-3$: at most $B-1$ for resource independence, at most $B-1$ for the disjoint upper blockers, and at most $B-1$ for this optional contraction test. No bound on the global rank of $Q$ was used.

For favorable minimization, the adjusted linear term does not increase and $\gamma<0$, so UZ7 cannot increase the final rank term either. For favorable maximization, the adjusted linear term does not decrease and $\gamma>0$, so UZ7 cannot decrease the rank term. Hence

$$
\Phi(S-e+f)\le\Phi(S)\quad\text{for minimization},
 \qquad
 \Phi(S-e+f)\ge\Phi(S)\quad\text{for maximization}.
\tag{UZ8}
$$

Every numeric row remains feasible as before. Repeatedly replacing selected copies outside the representative union yields a solution entirely in that union with no worse **true** scalar value. Current contraction rank may increase during this process; this is permitted and helps the comparison.

## 4. Exact optimization, reconstruction, and space

Enumerate at most $B$ emitted candidates exactly as in LM. Test resource independence and all laminar rows. There is no full-span test. Evaluate UZ6 and keep the exact best value. Once the best positive vector is known, construct a greedy base of UZ3 on $Z$. This produces the best zero completion and attains the saved scalar value.

The representative count and enumeration exponent are unchanged. The binary-space implementation is also unchanged. With $n=|P|$, if $B\ge n$, stream all count vectors $0\le x_e\le\lfloor B/w_e\rfloor$ using $n$ binary counters and evaluate UZ6. Otherwise, $B<n$, so the positive copy ground and recursion depth are polynomial in explicit input size, and representative positions are regenerated from their branching words. Neither branch expands zero capacities.

When $B=0$ or no positive coordinate survives, first reject any positive lower requirement. At a favorable sign, output a maximum-total zero vector, with scalar $\gamma F(Z)$. At an unfavorable sign, output the zero vector, with scalar zero. These cases are polynomial.

## 5. Precise combined scope

Together LM and this note cover both optional and mandatory resources when all zero-weight coordinates share an arbitrary rational scalar coefficient. For mandatory bases the scalar reduction is the fixed affine expression in LM14; for optional resources the favorable case additionally uses the current contraction rank in UZ6. They are different arguments, and neither silently forces an optional vector to attain the original rank.

The nonuniform-zero example in LM remains a counterexample to its naive positive-only scalar comparison. This note removes only the optional **uniform**-coefficient restriction. It neither proves hardness for nonuniform coefficients nor claims that the present rank-monotonic argument already handles them.

This is a separate new increment. The reviewed LM manuscript remains unchanged, and its primary-source comparison and representative-lemma attribution continue to apply.
