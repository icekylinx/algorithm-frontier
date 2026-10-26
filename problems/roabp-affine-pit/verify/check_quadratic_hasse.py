"""Independent exact checks of the original-field quadratic obstruction.

No author verifier is imported. Uses integer polynomial coefficient bases,
fraction-free Bareiss elimination, and prime-field elimination.
"""
from pathlib import Path
import argparse
from math import comb, factorial, prod, isqrt
from fractions import Fraction
import hashlib
import json


def bareiss(matrix):
    A = [list(row) for row in matrix]
    n = len(A)
    previous, sign = 1, 1
    for k in range(n-1):
        pivot = next((i for i in range(k,n) if A[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            A[k], A[pivot] = A[pivot], A[k]
            sign = -sign
        value = A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator = value*A[i][j] - A[i][k]*A[k][j]
                assert numerator % previous == 0
                A[i][j] = numerator // previous
            A[i][k] = 0
        previous = value
    return sign*A[-1][-1]


def det_mod(matrix,p):
    A = [[v % p for v in row] for row in matrix]
    result = 1
    for j in range(len(A)):
        pivot = next((i for i in range(j,len(A)) if A[i][j]),None)
        if pivot is None:
            return 0
        if pivot != j:
            A[j],A[pivot] = A[pivot],A[j]
            result = -result
        value = A[j][j]
        result = result*value % p
        inverse = pow(value,-1,p)
        for i in range(j+1,len(A)):
            factor = A[i][j]*inverse % p
            for k in range(j,len(A)):
                A[i][k] = (A[i][k]-factor*A[j][k]) % p
    return result % p


def multiply_linear(poly,constant,linear):
    out = [0]*(len(poly)+1)
    for i,a in enumerate(poly):
        out[i] += constant*a
        out[i+1] += linear*a
    return out


def evaluate(poly,x):
    value = 0
    for a in reversed(poly):
        value = value*x+a
    return value


def primes_after(bound,count=3):
    out=[]
    p=bound+1
    while len(out)<count:
        if p>=2 and all(p%d for d in range(2,isqrt(p)+1)):
            out.append(p)
        p+=1
    return out


def check(w):
    N=w*w-1
    ps=[]
    for i in range(w):
        polynomial=[1]
        for a in range(i+1,w):
            polynomial=multiply_linear(polynomial,a,1)
        for b in range(i):
            polynomial=multiply_linear(polynomial,N-b,-1)
        assert len(polynomial)==w
        ps.append(polynomial)
    evaluation=[[evaluate(ps[i],N-s) for s in range(w)] for i in range(w)]
    for i in range(w):
        for s in range(i):
            assert evaluation[i][s]==0
        diagonal=Fraction(factorial(i)*factorial(N+w-1-i),factorial(N))
        assert evaluation[i][i]==diagonal
    coefficient_det=bareiss(ps)
    predicted_coefficient_det=Fraction(
        (-1)**(w*(w-1)//2)*prod(factorial(N+s) for s in range(w)),
        factorial(N)**w)
    assert coefficient_det==predicted_coefficient_det

    ks=[w*j for j in range(w)]
    B=[[comb(N,i+ks[j]) for j in range(w)] for i in range(w)]
    actual=bareiss(B)
    for i in range(w):
        for j in range(w):
            column=Fraction(factorial(N),factorial(ks[j]+w-1)*factorial(N-ks[j]))
            assert column*evaluate(ps[i],ks[j])==B[i][j]
    vandermonde=prod(ks[b]-ks[a] for a in range(w) for b in range(a+1,w))
    formula=Fraction(
        (-1)**(w*(w-1)//2)*prod(factorial(N+s) for s in range(w))*vandermonde,
        prod(factorial(ks[j]+w-1)*factorial(N-ks[j]) for j in range(w)))
    assert actual==formula and actual!=0

    # Construct the middle-only residual polynomial term by term from A_ij.
    # Key is (Y_T exponent, C exponent). No precomputed binomial identity.
    residual={}
    for i in range(w):
        for j in range(w):
            degree=N-i-w*j
            coefficient=(-1)**degree*B[i][j]
            for a in range(degree+1):
                key=(a,i+w*j+degree-a)
                residual[key]=residual.get(key,0)+coefficient*comb(degree,a)
    residual={e:c for e,c in residual.items() if c}
    assert residual=={(N,0):(-1)**N}
    E=w*(w*w-1)//2
    assert 2*E==w*(w*w-1)
    signed=[[(-1)**(N-i-w*j)*B[i][j] for j in range(w)] for i in range(w)]
    assert bareiss(signed)==(-1)**E*actual
    finite=[]
    for p in primes_after(N+w-1):
        assert det_mod(B,p)==actual%p!=0
        assert det_mod(signed,p)!=0
        assert all(comb(N,m)%p for m in range(N+1))
        assert all(0<=i+w*j<=N for i in range(w) for j in range(w))
        assert p>N and len({1,w,p})==3
        degrees=[N+i*(p-1)+j*(p-w) for i in range(w) for j in range(w)]
        assert max(degrees)==2*p*(w-1) and degrees.count(max(degrees))==1
        finite.append({"p":p,"determinant_mod_p":det_mod(signed,p),
                       "scalar_total_degree":max(degrees),
                       "all_nonconstant_endpoint_residual_orders_at_least":p})
    return {"w":w,"N":N,"binomial_determinant":str(actual),
            "coefficient_basis_determinant":str(coefficient_det),
            "middle_determinant_T_exponent":E,
            "middle_only_residual":f"(-Y_T)^{N}",
            "prime_checks":finite,"all_assertions_pass":True}


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    source=Path(__file__).resolve().parent.parent/"manuscripts/quadratic-hasse-obstruction.md"
    output={
      "source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
      "verifier_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      "method":"integer coefficient bases, Bareiss determinants, prime-field elimination; no author code imported",
      "scope":"finite corroboration of a separately reconstructed general proof",
      "cases":[check(w) for w in range(2,11)]}
    destination=args.output
    if destination:
        destination.write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps({"all_assertions_pass":True,"widths":[2,10],
                      "source_sha256":output["source_sha256"],
                      "output":str(destination) if destination else None},indent=2))
