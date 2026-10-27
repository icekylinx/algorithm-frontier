"""Independent compact original-input Pauli energy verification.
Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro. Apache-2.0.
No producer or optimizer is imported. Local multiplication uses the Pauli table.
"""
from fractions import Fraction


def _pauli(n,p):
    x,z,sign=p.x,p.z,p.sign
    if any(type(v) is not int for v in (x,z,sign)) or x<0 or z<0 or sign not in (0,1) or max(x,z).bit_length()>n:
        raise ValueError('invalid original Pauli')
    return tuple(((x>>j)&1)+2*((z>>j)&1) for j in range(n)),sign


def energy_of_tableau(n,clauses,generators):
    if type(n) is not int or n<0 or len(generators)!=n:raise ValueError('complete tableau required')
    gs=[_pauli(n,g) for g in generators]
    for i,(a,_) in enumerate(gs):
        for b,_ in gs[:i]:
            if sum(u!=v and bool(u) and bool(v) for u,v in zip(a,b))%2:
                raise ValueError('noncommuting tableau')
    rows=[]
    for j,g in enumerate(generators):
        vector=g.x+(g.z<<n);mask=1<<j
        for pivot,row,combination in rows:
            if vector>>pivot&1:vector^=row;mask^=combination
        if not vector:raise ValueError('dependent tableau')
        rows.append((vector.bit_length()-1,vector,mask));rows.sort(reverse=True)
    # Codes: I=0, X=1, Z=2, Y=3. Entries are powers of i.
    phases={(1,3):1,(3,1):3,(1,2):3,(2,1):1,(3,2):1,(2,3):3}
    energy=Fraction(0)
    for weight,p in clauses:
        if type(weight) not in (int,Fraction) or weight<=0:raise ValueError('positive rational weights required')
        local,sign=_pauli(n,p)
        vector=p.x+(p.z<<n);mask=0
        for pivot,row,combination in rows:
            if vector>>pivot&1:vector^=row;mask^=combination
        expectation=0
        if not vector:
            accumulated=[0]*n;phase=0
            for j,(letters,gsign) in enumerate(gs):
                if mask>>j&1:
                    phase+=2*gsign
                    for k,v in enumerate(letters):
                        phase+=phases.get((accumulated[k],v),0)
                        accumulated[k]^=v
            if tuple(accumulated)!=local or phase%2:raise ValueError('invalid Hermitian product')
            expectation=1 if (phase-2*sign)%4==0 else -1
        energy+=weight*(1-expectation)
    return energy


def verify_witness(n,clauses,witness):
    try:
        if type(witness.energy) not in (int,Fraction):return False
        return energy_of_tableau(n,clauses,witness.generators)==witness.energy
    except (AttributeError,TypeError,ValueError):
        return False
