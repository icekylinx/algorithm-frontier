#!/usr/bin/env python3
"""Recompute the fast Subset Sum scalar profile and operation ledger exactly.

This checks entropy enclosures, all breakpoints of the lower envelope of the
stated contact chords and finite-volume cones, their continuous reflected
quadratic bound, and every outer cost.
The continuous contact inequalities and circuit construction are explicit
mathematical premises, not claims established by this scalar certificate.
Only Python standard-library integer and rational arithmetic accepts a bound.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from functools import lru_cache
import json
import hashlib
from pathlib import Path

CONTACTS = [
    ('1.3', '.47', '.5', [('.24','.14310'),('.40','.19000')]),
    ('1.7', '.47', '.5', [('.40','.18545'),('.44','.19560')]),
    ('2.2', '.50', '.5', [('.43','.19229'),('.46','.19877')]),
    ('2.6', '.54', '.5', [('.45','.19669'),('.48','.20234')]),
    ('2.8', '.58', '.5', [('.47','.20032'),('.49','.20396')]),
    ('3', '.60', '.5', [('.48','.20214'),('.49','.20384'),('.50','.20556'),('.51','.20730')]),
    ('3.15', '.664', '.56', [('.48','.20200'),('.49','.20371'),('.50','.20544')]),
    ('3.29', '.664', '.56', [('.49','.20377'),('.50','.20538'),('.51','.20700')]),
    ('3.4', '.62', '.5', [('.50','.20561'),('.51','.20706'),('.54','.21148'),('.58','.21758')]),
    ('3.43', '.664', '.56', [('.50','.20545'),('.51','.20695'),('.52','.20846')]),
    ('4', '.65', '.5', [('.55','.21218'),('.60','.21801'),('.65','.22429')]),
    ('4', 'direct', 'direct', [('.60','.21873'),('.76','.22760')]),
]


THIRD_MENU_PATH = Path(__file__).resolve().parents[1] / "problems/subset-sum-fast-deterministic/verify/third_contacts.json"


@lru_cache(maxsize=1)
def third_contact_data():
    """Load the extension only when requested; the E_2 replay is independent."""
    data = THIRD_MENU_PATH.read_bytes()
    menu = json.loads(data)
    require({key:F(value) for key,value in menu["types"].items()} == {
            'a':F('.065'),'b':F('.075'),'s':F('.14'),'t':F('.45')},
            'third-contact menu uses the refined matching types')
    contacts = [tuple(family[key] for key in ('rho','gamma','gamma2','gamma3'))
                + (family['contacts'],) for family in menu['families']]
    return contacts, hashlib.sha256(data).hexdigest()


def all_contact_points(include_third=True):
    extension = third_contact_data()[0] if include_third else []
    return [row[-1] for row in CONTACTS]+[row[-1] for row in extension]


PROFILE_CASES = {
    False: {
        'budget':F('.41077126'),
        'comparisons':160,
        'maximum':F(10515744200139750970543135213463,25600000000000000000000000000000),
        'breakpoints':['0','2425000000000/9700570910413','5672/14453','2/5',
            '288877/673855','43/100','3759/8300','2114877/4502050','47/100',
            '177893/370800','12/25','49/100','99/200','1/2','607/1200','51/100',
            '13/25','257244/494425','27/50','308143/561610','11/20','3/5',
            '5709/9355','16693148922977/22715773922977','1'],
        'gain_lower':F(132821521157,10**13),
        'dictionary_fraction':F(50000000000000,159482029459567),
        'exponent':F(158153814247997,318964058919134),
        'previous_exponent':F(158153814247997,318963914919134),
        'displayed_exponent':F('.495836'),
        'nonbinding_caps':['.463358446','.321234175','.328953402','.352410683',
                           '.372361028','.493729702','.313514947'],
    },
    True: {
        'budget':F('.41020007'),
        'comparisons':112,
        'maximum':F(212647711284991364849543952290503,518400000000000000000000000000000),
        'breakpoints':['0','2425000000000/9700570910413','5672/14453','2/5',
            '288877/673855','43/100','1643/3725','12/25','49/100','1/2',
            '372241/716425','13/25','303886/552835','11/20','3/5','5709/9355',
            '16693148922977/22715773922977','1'],
        'gain_lower':F(135677471157,10**13),
        'dictionary_fraction':F(50000000000000,159510588959567),
        'exponent':F(158153814247997,319021177919134),
        'previous_exponent':F(158153814247997,318964058919134),
        'displayed_exponent':F('.495748'),
        'nonbinding_caps':['.463275485','.321176660','.328894505','.352437108',
                           '.372294358','.493730824','.313458814'],
    },
}


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


def envelope(include_third=True):
    push,pull = F('.58414212731239'), F('.85319345691908')
    lines = [(F(0),F(1),push,F(0)), (F(0),F(1),-pull,pull)]
    for raw in all_contact_points(include_third):
        points = [(F(x),F(y)) for x,y in raw]
        for (x,y),(z,w) in zip(points,points[1:]):
            a = (w-y)/(z-x)
            lines.append((x,z,a,y-a*x))
        # Positive integer color degrees imply the finite volume inequality
        # Upsilon(tau) <= Upsilon(alpha)**max(tau/alpha,(1-tau)/(1-alpha)).
        # Each contact therefore supplies two globally valid cone pieces.
        for alpha,value in points:
            require(0<alpha<1 and value>=0,'valid contact cone')
            lines.extend([(F(0),alpha,-value/(1-alpha),value/(1-alpha)),
                          (alpha,F(1),value/alpha,F(0))])
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
    for left,right in zip(raw_segments,raw_segments[1:]):
        require(left[1]==right[0] and line_value(left,left[1])==line_value(right,right[0]),
                'continuity of the contact/chord/cone envelope')
    return raw_segments


def scalar_profile(include_third=True):
    case=PROFILE_CASES[include_third]
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
    segments=envelope(include_third)
    expected=[F(x) for x in case['breakpoints']]
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
    expected_max=case['maximum']
    require(maximum==expected_max,'reflected quadratic maximum')
    require(len(candidates)==case['comparisons'],'complete endpoint comparison count')
    require(maximum < case['budget'],'quadratic contact budget')
    return {'comparisons':len(candidates),'continuous_envelope':True,'breakpoints':[str(x) for x in actual],
            'quadratic_maximum':str(maximum),'margin':str(case['budget']-maximum),
            'maximizers':sorted({str(x) for value,x,_ in candidates if value==maximum})}


def retyping_contract(include_third=True):
    """Check the finite obligations changed by the refined circuit types.

    The input difference tensor is indexed by at most 2sM nonzero symbols.
    Its exponent need not be below one; it only needs to fit the alpha
    exponent of the subsequent pruned contractions.  This distinction
    matters at s=.14, unlike the older s=.11 parameter setting.
    """
    s,t,a,b=F('.14'),F('.45'),F('.065'),F('.075')
    require(a+b==s and 0<a<t and 0<b<1-t,'valid refined matching types')
    require(s<F(1,5) and s<F(1,3) and 2*s<F(2,3),
            'core fitting and pruned-tensor entropy domains')
    require(add(H(F(1),s),H(s,a))[1]<1,'raw query universe below the binary cube')
    initial=add(H(F(1),2*s),(2*s,2*s))
    alpha=add(H(F(1),s),(1-s,1-s))
    require(initial[1]<alpha[0],'initial difference table fits the energy-transform budget')
    require(initial[1]<F('1.135451') and alpha[0]>F('1.444238'),
            'displayed initial-table and transform bounds')
    for rho,gamma,gamma2,_ in CONTACTS:
        beta=a+F(rho)*(s-a)
        require(beta<min(t,1-t),'outer lookup fits both row symbols')
        if gamma!='direct':
            require(0<F(gamma2)<1,'second lookup is a legal positive-query width')
            require(beta-s<=F(gamma)*beta,'first inner lookup contains every query')
    third_contacts=third_contact_data()[0] if include_third else []
    for rho,gamma,gamma2,gamma3,points in third_contacts:
        rho,gamma,gamma2,gamma3=map(F,(rho,gamma,gamma2,gamma3))
        require(rho>1 and all(0<value<1 for value in (gamma,gamma2,gamma3)),
                'legal third-lookup family fractions')
        beta=a+rho*(s-a)
        require(beta<min(t,1-t,1-s),'third-family outer and trace domains')
        for m in (a,s):
            beta_m=a+rho*(m-a)
            require(gamma*beta_m>=beta_m-m,'third-family complete first-query containment')
        weights=[F(point[0]) for point in points]
        require(weights==sorted(set(weights)) and all(0<value<1 for value in weights),
                'ordered distinct third-family contact weights')
        require(all(F(point[1])>0 for point in points),'positive third-contact targets')
    padding=1000
    require(a*padding>=12 and b*padding>=12 and
            (t-a)*padding>=24 and (1-t-b)*padding>=24,
            'three-count dummy padding')
    amplification=max(max(1/F(tau),1/(1-F(tau)))
                      for points in all_contact_points(include_third) for tau,_ in points)
    require(amplification==F(25,6),'uniform contact-cone seed amplification')
    require(amplification*F(3,10**10)+F(1,800000000)==F(1,400000000),
            'strict seed and depth errors fit the template allowance')
    grid=10000
    interpolation=F(1296,875)/(4*grid*grid)
    require(interpolation<F(5,10**9),'refined compiler interpolation allowance')
    result={'initial_difference_table_upper':'1.135451',
            'energy_transform_lower':'1.444238',
            'core_fraction_grid':grid,'compiler_allowance':'1/100000000',
            'max_contact_cone_amplification':str(amplification),
            'pre_cone_seed_error_cap':'3/10000000000',
            'second_lookup_fractions':[str(value) for value in sorted({F(row[2]) for row in CONTACTS if row[1]!='direct'}|{F(row[2]) for row in third_contacts})],
            'quadratic_interpolation_loss':str(interpolation)}
    if include_third:
        result['third_lookup_fractions']=[str(value) for value in sorted({F(row[3]) for row in third_contacts})]
    return result


def ledger(include_third=True):
    case=PROFILE_CASES[include_third]
    s,t,a,b=F('.14'),F('.45'),F('.065'),F('.075')
    S,zeta,d0=case['budget'],F(1,10**8),F(1,50)
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
    g_L=case['gain_lower']
    for condition,name in [(typed[1]<=D_U,'typed width'),(alpha[1]<=alpha_U,'energy transform'),
                           (eta[1]<=eta_U,'rounding loss'),(gain[0]>=g_L,'gain')]:
        require(condition,name+' entropy bound')
    mu=1/(2*(1+D_U+g_L))
    E=case['exponent']
    require(mu==case['dictionary_fraction'],'dictionary fraction')
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
    require(E<case['previous_exponent'],'strict improvement over the preceding ledger')
    require(E<case['displayed_exponent'],'displayed rounded exponent')
    cap_names=('modulus_energy','selector_and_shared_witness_preprocessing',
               'repeated_prefix_lookups','repeated_outside_lookups',
               'cyclic_convolution_and_shifts','high_deficiency_fallback',
               'dictionary_preparation')
    displayed_caps=dict(zip(cap_names,map(F,case['nonbinding_caps'])))
    require(all(rates[key]<cap for key,cap in displayed_caps.items()),
            'strict displayed nonbinding rate caps')
    return {'exponent':str(E),'dictionary_fraction':str(mu),
            'operation_rates':{key:str(value) for key,value in rates.items()}}


def main():
    if not __debug__:
        raise SystemExit('Run mathematical verification without python -O.')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--base-two-level',action='store_true',
                        help='replay the preserved Part II E_2 ledger without loading the third-level menu')
    args=parser.parse_args()
    include_third=not args.base_two_level
    count=PROFILE_CASES[include_third]['comparisons']
    result={'status':'PASS',
            'scope':f'Exact entropy bounds, {count} reflected-profile comparisons, and all outer rates; continuous contacts and circuit construction are separate premises.',
            'theorem':'F3' if include_third else 'F2',
            'profile':scalar_profile(include_third),
            'retyping':retyping_contract(include_third),'ledger':ledger(include_third)}
    if include_third:
        digest=third_contact_data()[1]
        result['third_menu_sha256']=digest
        require(hashlib.sha256(THIRD_MENU_PATH.read_bytes()).hexdigest()==digest,
                'third-contact menu unchanged during scalar verification')
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS: {result["theorem"]}, exact entropy enclosures, {count} reflected-profile comparisons, and complete operation ledger')


if __name__=='__main__':
    main()
