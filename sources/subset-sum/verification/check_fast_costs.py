"""Exact scalar certificate for the pooled-trace fast-time reduction.

This checks scalar entropy and operation costs. The mixed circuit contact
certificate and uniformity proof are separate obligations.
"""

from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def scale(c, a):
    return (c * a[0], c * a[1]) if c >= 0 else (c * a[1], c * a[0])


def log_series(x):
    z = (x - 1) / (x + 1)
    assert 0 <= z <= F(1, 3)
    grid = 2**120
    lower = sum((F((grid * 2 * z**(2*j+1) / (2*j+1)).__floor__(), grid)
                 for j in range(32)), F(0))
    return lower, lower + F(32, grid) + 2 * z**65 / (65 * (1 - z*z))


LN2 = log_series(F(2))


@lru_cache(None)
def log2(x):
    assert x > 0
    k = 0
    while x < 1:
        x *= 2
        k -= 1
    while x >= 2:
        x /= 2
        k += 1
    lo, hi = log_series(x)
    return k + lo / LN2[1], k + hi / LN2[0]


def H(c, y):
    assert 0 <= y <= c
    result = (F(0), F(0))
    for x, sign in ((c, 1), (y, -1), (c-y, -1)):
        if x:
            result = add(result, scale(sign*x, log2(x)))
    return result


def enclosure(a, digits=14):
    scale = 10**digits
    lower = (a[0]*scale).__floor__()
    upper = (a[1]*scale).__ceil__()
    return F(lower, scale), F(upper, scale)


def show(a):
    if isinstance(a, tuple):
        return [show(x) for x in a]
    return {'rational': str(a), 'decimal': format(float(a), '.16f')}


s, t, a, b = F(11,100), F(9,20), F(13,250), F(29,500)
S, zeta, d0 = F(903,2500), F(1,10**6), F(1,50)
hs, R, Hsa, Hrest = H(F(1),s), H(F(1),t), H(s,a), H(1-s,t-a)
Q = add(hs,Hsa)
J = add((F(1),F(1)),scale(-1,add(Hsa,Hrest)))
gain = (F(-1,2)-S/2-zeta,F(-1,2)-S/2-zeta)
for weight,entropy in ((F(1,2),hs),(F(1,2),Hsa),(F(1),Hrest),(F(-1,2),R)):
    gain=add(gain,scale(weight,entropy))
u=t-a+b
typed=add(H(1-u,a),H(u,b))
eta=add((F(1),F(1)),scale(-1,H(F(1),u)))
alpha=add((1-s,1-s),hs)
g_lower=F(2135335441677,200000000000000)
D_upper=F(49809813343531,10**14)
alpha_upper=F(138991595816454,10**14)
eta_upper=F(559334743723,10**14)
assert gain[0]>=g_lower
assert typed[1]<=D_upper
assert alpha[1]<=alpha_upper
assert eta[1]<=eta_upper
assert LN2[1]<F(7,10)
assert H(F(1),F(1,5))[1]<1-d0
mu=1/(2*(1+D_upper+g_lower))
assert mu==F(100000000000000,301754962128739)
E=F(149809813343531,301754962128739)
assert E==mu*(1+D_upper)==F(1,2)-mu*g_lower<F('0.4964618056')
assert 3*mu<1
assert g_lower<d0
rates={
    'main_incidences':F(1,2)-mu*g_lower,
    'canonical_output_and_complete_cover':mu*(1+D_upper),
    'candidate_modulus_energy':mu*(alpha_upper+D_upper/64+d0+eta_upper),
    'selector_and_shared_trie':mu*(1+d0+eta_upper),
    'repeated_prefix_lookups':mu*(1+2*(d0+eta_upper)),
    'repeated_outside_lookups':(1-mu)/2+mu*(d0+2*eta_upper),
    'direct_cyclic_convolutions':mu*(d0+eta_upper+2*D_upper),
    'high_deficiency_fallback':F(1,2)-d0*mu,
    'dictionaries_and_layers':mu,
}
assert all(value<=E for value in rates.values())
assert all(value<E for name,value in rates.items() if name not in ('main_incidences','canonical_output_and_complete_cover'))
# Both entropy expansions describe the same joint type.
identity=add(add(H(F(1),u),typed),scale(-1,add((F(1),F(1)),add(hs,scale(-1,J)))))
assert identity[0]<=0<=identity[1]
result={
    'status':'PASS',
    'scope':'Exact scalar entropies and complete fast-time operation ledger; the circuit profile is a separate certificate.',
    'entropy_bounds':{name:show(enclosure(value)) for name,value in {
        'h_s':hs,'row_entropy':R,'query_entropy':Q,'flip_loss':J,
        'typed_width':typed,'round_loss':eta,'energy_transform':alpha,'gain':gain}.items()},
    'mu':show(mu),'theorem_exponent':show(E),
    'operation_upper_rates':{name:show(value) for name,value in rates.items()},
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: scalar entropies, exact balance, all auxiliary costs')
print('E =',E,'< 0.4964618056')
