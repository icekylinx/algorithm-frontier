#!/usr/bin/env python3
"""Recompute the fast Subset Sum scalar profile and operation ledger exactly.

This checks entropy enclosures, all breakpoints of the lower envelope of the
stated contact chords, its reflected quadratic bound, and every outer cost.
The continuous contact inequalities and circuit construction are explicit
mathematical premises, not claims established by this scalar certificate.
Only Python standard-library integer and rational arithmetic accepts a bound.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from functools import lru_cache
import json
from pathlib import Path

CONTACTS = [
    ('1.3', '.47', [('.24','.14310'),('.40','.19000')]),
    ('1.7', '.47', [('.40','.18545'),('.44','.19560')]),
    ('2.2', '.50', [('.43','.19229'),('.46','.19877')]),
    ('2.6', '.54', [('.45','.19669'),('.48','.20234')]),
    ('2.8', '.58', [('.47','.20032'),('.49','.20396')]),
    ('3', '.60', [('.48','.20214'),('.49','.20384'),('.50','.20556'),('.51','.20730')]),
    ('3.4', '.62', [('.50','.20561'),('.51','.20706'),('.54','.21148'),('.58','.21758')]),
    ('4', '.65', [('.55','.21218'),('.60','.21801'),('.65','.22429')]),
    ('4', 'direct', [('.60','.21873'),('.76','.22760')]),
]


def ln_enclosure(x: F) -> tuple[F, F]:
    if not 1 <= x <= 2:
        raise ValueError('logarithm series requires 1 <= x <= 2')
    z = (x-1)/(x+1)
    z2 = z*z
    power = z
    value = F(0)
    for j in range(32):
        value += 2*power/(2*j+1)
        power *= z2
    return value, value+2*power/(65*(1-z2))


LN2 = ln_enclosure(F(2))


@lru_cache(maxsize=None)
def log2_enclosure(x: F) -> tuple[F, F]:
    if x <= 0:
        raise ValueError('logarithm argument must be positive')
    k = x.numerator.bit_length()-x.denominator.bit_length()
    v = x/(F(2)**k)
    while v < 1:
        v *= 2
        k -= 1
    while v >= 2:
        v /= 2
        k += 1
    lo, hi = ln_enclosure(v)
    return F(k)+lo/LN2[1], F(k)+hi/LN2[0]


def add(*intervals: tuple[F, F]) -> tuple[F, F]:
    return sum((x[0] for x in intervals),F(0)), sum((x[1] for x in intervals),F(0))


def scale(c: F, interval: tuple[F, F]) -> tuple[F, F]:
    a,b = interval
    return (c*a,c*b) if c >= 0 else (c*b,c*a)


def H(c: F, y: F) -> tuple[F, F]:
    if not 0 <= y <= c:
        raise ValueError('entropy outside its domain')
    terms = [scale(sign*x, log2_enclosure(x)) for x,sign in ((c,1),(y,-1),(c-y,-1)) if x]
    return add(*terms)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def line_value(line: tuple[F, F, F, F], x: F) -> F:
    return line[2]*x+line[3]


def envelope():
    push,pull = F('.58414212731239'), F('.85319345691908')
    lines = [(F(0),F(1),push,F(0)), (F(0),F(1),-pull,pull)]
    for _,_,raw in CONTACTS:
        points = [(F(x),F(y)) for x,y in raw]
        for (x,y),(z,w) in zip(points,points[1:]):
            a = (w-y)/(z-x)
            lines.append((x,z,a,y-a*x))
    cuts = {F(0),F(1)}
    for left,right,_,_ in lines:
        cuts.update((left,right))
    for i,first in enumerate(lines):
        for second in lines[:i]:
            if first[2] == second[2]:
                continue
            x = (second[3]-first[3])/(first[2]-second[2])
            if max(first[0],second[0]) < x < min(first[1],second[1]):
                cuts.add(x)
    raw_segments=[]
    cuts=sorted(cuts)
    for left,right in zip(cuts,cuts[1:]):
        mid=(left+right)/2
        eligible=[z for z in lines if z[0] <= mid <= z[1]]
        selected=min(eligible,key=lambda z:line_value(z,mid))
        if raw_segments and raw_segments[-1][2:] == selected[2:]:
            raw_segments[-1]=(raw_segments[-1][0],right,*selected[2:])
        else:
            raw_segments.append((left,right,*selected[2:]))
    return raw_segments


def scalar_profile():
    s,t,a,b=F('0.14'),F('0.45'),F('0.065'),F('0.075')
    row=H(F(1),t)
    hs=H(F(1),s)
    query=add(hs,H(s,a))
    dc=add(row,scale(F(-1),query))
    D=(F('.26905132960667'),F('.26905132960673'))
    require(D[0] <= dc[0] and dc[1] <= D[1], 'D_c entropy enclosure')
    require(add(H(t,a),H(1-t,b))[1] <= F('.58414212731239'),'push endpoint')
    require(H(1-s,t-a)[1] <= F('.85319345691908'),'pull endpoint')
    require(LN2[1] < F('0.7'),'entropy curvature')
    segments=envelope()
    expected=[F(x) for x in ['0','2425000000000/9700570910413','2/5','43/100','3759/8300','47/100','12/25','49/100','1/2','291/580','51/100','27/50','11/20','3/5','5709/9355','16693148922977/22715773922977','1']]
    actual=[segments[0][0]]+[s[1] for s in segments]
    require(actual==expected,'full lower-envelope breakpoint list')
    cuts=sorted(set(actual+[1-x for x in actual]))
    candidates=[]
    K=F(875,2592)
    for left,right in zip(cuts,cuts[1:]):
        mid=(left+right)/2
        forward=next(z for z in segments if z[0] < mid < z[1])
        reflected=next(z for z in segments if z[0] < 1-mid < z[1])
        for x in (left,right):
            u=line_value(forward,x)
            v=line_value(reflected,1-x)
            require(0 <= u < F(1,4) and 0 <= v < F(1,4),'profile value below one quarter')
            for d in D:
                theta=(2*x-1)*d+u-v
                require(abs(theta)<F('.52'),'monotonicity range')
                candidates.append((u+v+K*theta*theta,x,d))
    maximum=max(z[0] for z in candidates)
    expected_max=F(7169585626176460495449293952290503,17438976000000000000000000000000000)
    require(maximum==expected_max,'reflected quadratic maximum')
    require(len(candidates)==104,'complete one-sided comparison count')
    require(maximum < F('.41113'),'quadratic contact budget')
    return {'comparisons':len(candidates),'breakpoints':[str(x) for x in actual],
            'quadratic_maximum':str(maximum),'margin':str(F('.41113')-maximum),
            'maximizers':sorted({str(x) for value,x,_ in candidates if value==maximum})}


def ledger():
    s,t,a,b=F('.14'),F('.45'),F('.065'),F('.075')
    S,zeta,d0=F('.41113'),F(1,10**6),F(1,50)
    u=t-a+b
    typed=add(H(1-u,a),H(u,b))
    eta=add((F(1),F(1)),scale(F(-1),H(F(1),u)))
    alpha=add((1-s,1-s),H(F(1),s))
    gain=add((F(-1,2)-S/2-zeta,F(-1,2)-S/2-zeta),
             scale(F(1,2),H(F(1),s)),scale(F(1,2),H(s,a)),
             H(1-s,t-a),scale(F(-1,2),H(F(1),t)))
    D_U=F(58153814247997,10**14)
    alpha_U=F(144423881164287,10**14)
    eta_U=F(231078058989,5*10**13)
    g_L=F(131017921157,10**13)
    for condition,name in [(typed[1]<=D_U,'typed width'),(alpha[1]<=alpha_U,'energy transform'),
                           (eta[1]<=eta_U,'rounding loss'),(gain[0]>=g_L,'gain')]:
        require(condition,name+' entropy bound')
    mu=1/(2*(1+D_U+g_L))
    E=F(158153814247997,318927986919134)
    require(mu==F(50000000000000,159463993459567),'dictionary fraction')
    require(mu*(1+D_U)==F(1,2)-mu*g_L==E,'balanced exact exponent')
    require(3*mu<1 and g_L<d0,'dictionary fitting and deficiency threshold')
    require(H(F(1),F(1,5))[1]<1-d0,'canonical layer density gate')
    rates={
        'circuit_incidences_and_witnesses':F(1,2)-mu*g_L,
        'canonical_output_and_full_residue_cover':mu*(1+D_U),
        'modulus_energy':mu*(d0+eta_U+alpha_U+D_U/64),
        'selector_and_shared_witness_preprocessing':mu*(1+d0+eta_U),
        'repeated_prefix_lookups':mu*(1+2*(d0+eta_U)),
        'repeated_outside_lookups':(1-mu)/2+mu*(d0+2*eta_U),
        'cyclic_convolution_and_shifts':mu*(d0+eta_U+2*D_U),
        'high_deficiency_fallback':F(1,2)-d0*mu,
        'dictionary_preparation':mu,
    }
    require(all(x<=E for x in rates.values()),'complete outer cost domination')
    require(E<F(149809813343531,301754962128739),'strict time improvement')
    return {'exponent':str(E),'dictionary_fraction':str(mu),
            'operation_rates':{key:str(value) for key,value in rates.items()}}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result={'status':'PASS','scope':'Exact entropy bounds, 104 reflected-profile comparisons, and all outer rates; continuous contacts and circuit construction are separate premises.',
            'profile':scalar_profile(),'ledger':ledger()}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: exact entropy enclosures, 104 reflected-profile comparisons, and complete operation ledger')


if __name__=='__main__':
    main()
