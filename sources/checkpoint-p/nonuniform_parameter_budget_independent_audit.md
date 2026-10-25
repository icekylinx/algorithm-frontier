# Independent audit of the nonuniform parameter-budget obstruction

**25 October 2026.** This checks
`nonuniform_parameter_budget_frontiers.md` as an optimization statement
about its declared positive certificate ledger. It does not interpret
any displayed asymptotic upper bound as an algorithmic lower bound.

## Verdict

The algebra is correct. The fixed-stretch `11/14`, subpolynomial-stretch
`3/4` boundary with a growing retreat, quality-charged `4/5`, and strong
forest `7/8` balances survive arbitrary parameter choices at different
levels **within the stated ledger model**. The corresponding uniform
choices attain the displayed balances, so the obstruction is not an
artifact of imposing uniform parameters.

The word "ledger" is essential: a statement such as
`log Gamma = O(p h)` alone does not imply a lower bound of order `p h`
on the actual distortion or on the best possible certificate. Here the
model fixes positive nominal charges proportional to these expressions,
and asks how small a budget can cover those charges. Improving the
analysis so that one of these charges disappears or becomes smaller
changes the model, just as a new data structure does.

## 1. Interior hierarchy calculation

On the nominal interval `U/2 <= u_i <= U`, assume

\[
 \sum_i x_i\ge cU,\qquad
 x_i\le CB,\quad u_i/p_i\le CB,\quad
 K_i p_i h\le CB,\quad \sum_i u_i/K_i\le CB.
\]

Then `d >= c' U/B` and every `p_i >= c' U/B`.
Cauchy--Schwarz yields

\[
 \sum_i K_i\ge
 \frac{(\sum_i\sqrt{u_i})^2}{\sum_i u_i/K_i}
 \ge c' d^2U/B.
\]

Consequently the metric ledger satisfies

\[
 a\ge c' h\sum_i K_i p_i
   \ge c' d^2 U^2h/B^2
   \ge c' U^4h/B^4.
\]

No equality of the `p_i`, `K_i`, or `x_i` is used. In particular,
requiring `a <= C U^(6/7) h` forces `B >= c U^(11/14)`;
requiring `a = o(U)` forces
`B/(U^(3/4) h^(1/4)) -> infinity`; and requiring `a <= C B`
forces `B >= c U^(4/5) h^(1/5)`.

Independently, the local repair charge implies
`K_i <= C' B^2/(U h)`. Substitution into the cumulative charge gives
`B^4 >= c U^3 h`. This agrees with, but is weaker than, the
subpolynomial-metric consequence above.

## 2. Strong forest calculation

Retain the congestion ledger `c_in` separately. Weighted
Cauchy--Schwarz gives

\[
 a c_{\rm in}
 \ge c h\left(\sum_i\sqrt{u_i p_i}\right)^2
 \ge c d^2U^2h/B
 \ge c U^4h/B^3.
\]

The declared outer terms require

\[
 B\le CZ,\quad \Lambda\ge cU/Z,\quad
 K_{\rm cov}\ge c\Lambda U/Z,\quad
 c_{\rm in}\le CZ/\Lambda,\quad
 K_{\rm cov}\Lambda a\le CU.
\]

Thus `a <= C' Z/Lambda^2` and

\[
 a c_{\rm in}\le C'Z^2/\Lambda^3\le C''Z^5/U^3.
\]

Combining this with the lower bound and `B <= CZ` gives
`Z^8 >= c U^7 h`. All inequality directions are correct.

## 3. Nominal-ledger assumptions that must remain visible

1. The interval requires a complete worst-case nominal size allowance
   to pass from log-size `U` to `U/2`. A particular graph may shrink
   faster; this proof says nothing about that execution. Replacing an
   upper-bound child-size allowance by an actual lower bound would be
   invalid and is not used here.
2. A direct exact base while nominal log-size is still at least `U/2`
   has a positive log-work charge of order `U` for the base algorithms
   under discussion. It is therefore outside a proposed `B=o(U)`
   budget. This closes the apparent option of terminating the nominal
   chain before the interval has been traversed.
3. The cumulative recourse and metric charges refer to the same
   nominal hierarchy path. They cannot be independently taken from
   incompatible executions and then called an execution lower bound.
   They are simultaneous terms in the current worst-case certificate.
4. The outer scale restriction must use the same certified metric
   ledger `a`. A future outer proof using finer local metric information
   is a legitimate escape from the present model.

With these interpretations, no substantive correction is needed.
