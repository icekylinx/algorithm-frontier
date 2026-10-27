#!/usr/bin/env python3
"""Independent original Pauli operator and energy checks.
Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro. Apache-2.0.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from dataclasses import replace
import random
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'reference'))
import pauli_witness as backend
from verify_witness import verify_witness,energy_of_tableau


def dense(p,n):
    # Direct computational-basis action, independent of symplectic reduction.
    size=1<<n
    out=[[0j]*size for _ in range(size)]
    letters={(0,0):((1,0),(0,1)),(1,0):((0,1),(1,0)),
             (0,1):((1,0),(0,-1)),(1,1):((0,-1j),(1j,0))}
    for x in range(size):
        for y in range(size):
            z=(-1)**p.sign
            for j in range(n):z*=letters[(p.x>>j&1,p.z>>j&1)][y>>j&1][x>>j&1]
            out[y][x]=z
    return out


def multiply(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(a))) for j in range(len(a))] for i in range(len(a))]


def dense_energy(n,clauses,gs):
    size=1<<n
    state=[[int(i==j)/size for j in range(size)] for i in range(size)]
    for g in gs:
        a=dense(g,n)
        for i in range(size):a[i][i]+=1
        state=multiply(state,a)
    assert sum(state[i][i] for i in range(size))==1
    answer=F(0)
    for weight,p in clauses:
        a=dense(p,n)
        expectation=sum(a[i][j]*state[j][i] for i in range(size) for j in range(size))
        assert expectation.imag==0 and expectation.real in (-1,0,1)
        answer+=weight*(1-int(expectation.real))
    return answer


rng=random.Random(6119)
counts={'instances':0,'basis_states':0,'dense_states':0,'pairs':0,'forged':0,'invalid':0}
fixtures=[]
for n in range(4):
    for trial in range(35):
        clauses=tuple((F(rng.randrange(1,8),rng.randrange(1,6)),backend.Pauli(rng.randrange(1<<n),rng.randrange(1<<n),rng.randrange(2))) for _ in range(rng.randrange(9)))
        fixtures.append((n,clauses))
fixtures.extend([(1,((F(1),backend.Pauli(1,0)),(F(1),backend.Pauli(1,1)),(F(1,10**100),backend.Pauli(0,1)))),
                 (2,((F(1),backend.Pauli(3,0)),(F(2),backend.Pauli(0,3)),(F(3),backend.Pauli(3,3)))),
                 (0,((F(10**100),backend.Pauli(0,0,1)),))])
for n,clauses in fixtures:
    result=backend.reduce_hamiltonian(n,clauses)
    remaining=list(result.residual)
    for i,j,amount in result.pairs:
        assert not backend.commutes(clauses[i][1],clauses[j][1]) and amount>0
        remaining[i]+=amount;remaining[j]+=amount;counts['pairs']+=1
    assert remaining==[w for w,p in clauses]
    active=[p for a,(w,p) in zip(result.residual,clauses) if a]
    assert all(backend.commutes(p,q) for p in active for q in active)
    energies=[]
    for assignment in range(1<<n):
        gs=tuple(replace(p,sign=p.sign^(assignment>>j&1)) for j,p in enumerate(result.generators))
        actual=energy_of_tableau(n,clauses,gs)
        assert actual==result.energy(assignment)
        if n<=2 or counts['instances']%7==0:
            assert dense_energy(n,clauses,gs)==actual;counts['dense_states']+=1
        energies.append(actual);counts['basis_states']+=1
    witness=backend.minimize(result)
    assert witness.energy==min(energies) and verify_witness(n,clauses,witness)
    assert not verify_witness(n,clauses,replace(witness,energy=witness.energy+1))
    counts['forged']+=1;counts['instances']+=1
# Large qubit count but effective parity rank one: no Hilbert-space enumeration.
clauses=((F(7,13),backend.Pauli(0,1)),(F(2,13),backend.Pauli(0,1,1)))
large=backend.reduce_hamiltonian(80,clauses)
witness=backend.minimize(large)
assert witness.parity_rank==1 and witness.energy==F(4,13)
assert verify_witness(80,clauses,witness)
# Producer-disabled verification requires only original input and a tableau.
saved=backend.reduce_hamiltonian,backend.minimize,backend.coordinates,backend.product
backend.reduce_hamiltonian=backend.minimize=backend.coordinates=backend.product=lambda *a,**k:(_ for _ in ()).throw(AssertionError('producer disabled'))
assert verify_witness(80,clauses,witness)
backend.reduce_hamiltonian,backend.minimize,backend.coordinates,backend.product=saved
bad=replace(witness,generators=witness.generators[:-1])
assert not verify_witness(80,clauses,bad)
# Hostile tableaus must fail independently of claimed energy.
for gs in [(backend.Pauli(1,0),backend.Pauli(0,1)),
           (backend.Pauli(1,0),backend.Pauli(1,0)),
           (backend.Pauli(4,0),backend.Pauli(0,2)),
           (backend.Pauli(1,0,2),backend.Pauli(0,2))]:
    assert not verify_witness(2,(),backend.Witness(gs,F(0),0))
    counts['forged']+=1
assert not verify_witness(80,clauses,replace(witness,energy=float(witness.energy)))
counts['forged']+=1
for n,clauses in [(-1,()),(1,((0,backend.Pauli(1,0)),)),(1,((1.0,backend.Pauli(1,0)),)),(1,((1,backend.Pauli(2,0)),)),(1,((1,backend.Pauli(0,0,2)),)),(True,())]:
    try:backend.reduce_hamiltonian(n,clauses)
    except ValueError:counts['invalid']+=1
    else:raise AssertionError('invalid input accepted')
print('PASS compact Pauli witnesses:',counts,'; phase-aware dependencies, 80-qubit rank-one search, disabled producer')
