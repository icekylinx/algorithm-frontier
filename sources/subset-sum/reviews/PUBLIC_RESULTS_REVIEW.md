# Public-result comparison for the combined manuscript

Review date: 23 October 2026. This record compares stated guarantees from primary sources. It does not establish priority, external peer review, or a practical runtime crossover.

The title remains **A deterministic Subset Sum bound**, by Yilin Liu. The manuscript contains two separate deterministic algorithms on arbitrary signed binary integers:

| Result | Time | Space | Correctness |
|---|---|---|---|
| Theorem 1 | $C+\operatorname{poly}(n,L)2^{En}$, $E=149809813343531/301754962128739<0.4964618056$ | — | Exact, with binary witness recovery |
| Theorem 2 | $\operatorname{poly}(n,L)2^{n/2}$ | $\operatorname{poly}(n,L)2^{E_Sn}$ bits, $E_S<0.1826163578$ | Exact, with binary witness recovery |

The exact low-space exponent is $E_S=18261635770550353/10^{17}$, giving the ten-place upper bound $E_S<0.1826163578$. The two rows describe separate algorithms.

## Time comparison

The relevant deterministic baseline is Jain's public Stage 5b preprint, pinned at commit `1daaf519f567dd7a65a00692b08b4ff54b252d24`. Its Theorem 5b-F gives $\operatorname{poly}(n,L)2^{(0.4986298176+\epsilon)n}$ for every fixed $\epsilon>0$. In the common regime $L=2^{o(n)}$, the new fixed exponent is smaller. Even the rounded new bound gives the exact difference

$$
0.4986298176-0.4964618056=0.0021680120.
$$

This compares certified upper bounds within the inherited representation-and-circuit framework. It does not prove that no better parameters exist in the earlier construction. Jain's source is a public preprint. [Pinned theorem](https://github.com/Swapnil-jain/subsetsum-derand/blob/1daaf519f567dd7a65a00692b08b4ff54b252d24/proofs/stage5b.md).

OpenAI's October 4 preprint gives a randomized $O(2^{.49n})$ word-time algorithm under each fixed polynomial input-bit-length bound. Its resource cap holds on every execution and its error is one-sided. Theorem 1 does not improve that randomized time exponent. [Official introduction](https://github.com/openai/math/blob/main/preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/build/sections/introduction.tex).

Ye and Li's partial-match algorithm is also randomized. It supplies the foundational matching representation, rather than a deterministic competing guarantee. Alman and Li supply the circuit framework. Their attribution remains at the relevant points in the manuscript. [Ye–Li](https://arxiv.org/abs/2610.10446v1), [Alman–Li](https://arxiv.org/abs/2509.14489v1).

## Space comparison

Schroeppel and Shamir give the classical deterministic half-exponential-time, quarter-exponential-space algorithm. Theorem 2 has a smaller stated space exponent at the same time exponent, with polynomial factors in the full encoding length retained. [Original publication](https://epubs.siam.org/doi/abs/10.1137/0210033).

OpenAI's September 26 low-space preprint gives a **randomized** algorithm with time $\operatorname{poly}(n)2^{n/2}$ and space $\operatorname{poly}(n+b)2^{.199n}$ writable words. Under each fixed polynomial-bit convention, the latter implies ordinary $O(2^{.2n})$ word space. It always rejects NO instances and accepts each YES instance with probability at least $2/3$; both resource bounds hold on every run. Theorem 2 is deterministic and states the smaller exponent $E_S<.1826163578$ with polynomial bit factors, so the correctness guarantees and word/bit conventions must remain explicit in comparisons. The source preprint does not already establish the deterministic theorem. [Official theorem and model](https://github.com/openai/math/blob/main/preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/build/introduction.tex).

The new proof credits that source's representation layout, pair-stream viewpoint, and biased-separator calculation. It proves nonlinear extraction, fixed-layer trace bounds, support-dependent signings, exact-distance ownership, deterministic filters, atomic generators, independent streams, and the complete mixed-density resource inequalities. The final rational balance refines the received $367/2000$ checkpoint without changing the uniform time exponent $1/2$. No exhaustive survey of every possible deterministic or randomized space tradeoff is claimed.

## References and evidence

The newly added bibliography metadata were checked against the primary publisher/proceedings records: Schroeppel–Shamir, *SIAM Journal on Computing* 10(3):456–464 (1981), DOI `10.1137/0210033`; Jin–Park–Saha–Xu, *ICALP 2026*, LIPIcs 374, 119:1–119:23, DOI `10.4230/LIPIcs.ICALP.2026.119`; and Madiman–Marcus–Tetali, *Random Structures & Algorithms* 40(4):399–424 (2012), DOI `10.1002/rsa.20385`. [SIAM](https://epubs.siam.org/doi/abs/10.1137/0210033), [ICALP proceedings](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.119), [Wiley](https://onlinelibrary.wiley.com/doi/10.1002/rsa.20385).

Greedy multi-prime selection through an implicit counting oracle is attributed to Jin, Park, Saha, and Xu, Section 4.3 and Lemmas 22–26. The manuscript supplies its problem-specific energy oracle rather than claiming that general selection principle as a new standalone result. [Primary full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.119/LIPIcs.ICALP.2026.119.html).

The earlier public-result review and its detailed metadata audit were moved into the joint integration archive before replacement. Existing pinned source receipts remain unchanged. The current [mathematical review](PROOF_REVIEW.md) records the distinct internal proof and finite-certificate checks; public availability of an antecedent is not evidence for the new theorem's correctness.

The manuscript and submission materials were synchronized on 24 October 2026 to the exact structural space exponent $18261635770550353/10^{17}$, displayed with the ten-place upper bound $0.1826163578$. The complete fixed-policy capacity audit tightens the supplied 137/750 checkpoint; the general time exponent remains 1/2.
