"""Exact resource certificate for deterministic space exponent .18261635770550353.

Standard library only. Analytic boundary reductions are recorded in
problems/subset-sum-low-space-deterministic/proof.md; finite comparisons use rational and integer arithmetic.
"""

from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from decimal import Decimal, localcontext
import json
import argparse

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output", type=Path, help="write the full deterministic receipt to this path")
args = parser.parse_args()

if not __debug__:
    raise SystemExit("Run with assertions enabled.")

P, ALPHA = F(23,26), F(52,75)
Q, X, T, B = F(137,250), F(17,2000), F(27,200), F(203,1000)
ERROR = F(2,10**10)
QGRID = 10**12
NROOT = 10**12
LMIN=2*sum((F(1,(2*j+1)*3**(2*j+1)) for j in range(24)),F(0))
LPLUS=LMIN+F(2,49*3**49)*F(9,8)

@lru_cache(None)
def entropy(p):
    z=abs(1-2*p)
    ss=sum((z**(2*j)/((2*j)*(2*j-1)) for j in range(1,129)),F(0))
    tail=z**258/(258*257*(1-z*z))
    return 1-(ss+tail)/LMIN,1-ss/LPLUS

def eh(p,lower=None,upper=None):
    lo,hi=entropy(p)
    if lower is not None:assert lo>lower,(p,'lower',float(lo),float(lower))
    if upper is not None:assert hi<upper,(p,'upper',float(hi),float(upper))
    return {'argument':str(p),'lower_decimal':float(lo),'upper_decimal':float(hi)}

def sign(x,s,t):
    base=P*s-x*t
    assert base>0
    return t**52*(P-x)**75-base**75

@lru_cache(None)
def roots(x,s):
    assert 0<=x<=F(1,5) and 0<s<=1
    lo,hi=0,NROOT
    while hi-lo>1:
        j=(hi+lo)//2
        if sign(x,s,F(j,NROOT))<0:lo=j
        else:hi=j
    assert sign(x,s,F(lo,NROOT))<0<=sign(x,s,F(hi,NROOT))
    return F(lo,NROOT),F(hi,NROOT)

def clip(poly,a,b,c):
    if not poly:return []
    out=[]
    for i,t in enumerate(poly):
        s=poly[i-1];fs=a*s[0]+b*s[1]-c;ft=a*t[0]+b*t[1]-c
        if (fs<=0)!=(ft<=0):
            r=fs/(fs-ft)
            out.append((s[0]+r*(t[0]-s[0]),s[1]+r*(t[1]-s[1])))
        if ft<=0:out.append(t)
    answer=[]
    for t in out:
        if not answer or t!=answer[-1]:answer.append(t)
    if len(answer)>1 and answer[0]==answer[-1]:answer.pop()
    return answer

def qmax(a,b,c,l,r):
    pts=[l,r]
    if a<0 and l<=-b/(2*a)<=r:pts.append(-b/(2*a))
    return max((a*t*t+b*t+c,t) for t in pts)

entropy_receipts=[]
hpL,hpU=F(28639695711,10**11),F(28639695712,10**11)
HO,TO=F(76919282902,10**11),F(722554602,10**11)
entropy_receipts.extend([eh(F(1,20),lower=hpL,upper=hpU),eh(F(9,40),upper=HO),eh(F(9,20),lower=1-TO)])
H0,TAU0=F(741482739932,10**12),F(18546104967,10**12)
H,TAU,HQ=F(769192829014,10**12),F(7225546013,10**12),F(811278124460,10**12)
entropy_receipts.extend([eh(F(21,100),upper=H0),eh(F(21,50),lower=1-TAU0),eh(F(9,40),upper=H),eh(F(9,20),lower=1-TAU),eh(F(1,4),upper=HQ)])

# Dense ownership mode: rho and its design capacity are fixed.
RHO=F(9,10);PD=F(1,20)
DO,AO,FU=(hpL-PD)/2,(hpL-3*PD)/4,(hpU+PD)/8
VO,EO,RO=HO-F(1,2),2*HO-1-F(9,20)+TO,F(9,20)+F(1,2)-HO-TO
CO=F(3,4)-Q+(DO-AO)*RHO
def osigma(x):return min(F(1),(CO-x)/VO)
tl,tu=roots(X,RHO)
assert tl==F(859560838307,NROOT)
bt=X*tu
assert F(99998,10**5)<osigma(X)<1
assert osigma(T)>F(53006,10**5)>F(53,100)
assert CO-VO==F(849648632975,10**14)<X
owner_tiny_r=-DO*RHO+EO+bt+F(371,1000)*X
owner_tiny_q0=F(3,4)-AO*RHO-RO*osigma(X)
owner_tiny_qx=owner_tiny_q0+bt-(1-F(371,1000))*X
assert owner_tiny_r<-F(30765,10**8)<-F(3,10000)
assert owner_tiny_q0<F(54573133,10**8)
assert owner_tiny_qx<F(54769110,10**8)<Q-F(3,10000)
# Short ownership certificate: proportional local deficiency gives one
# concave rational quadratic per gain interval; only the top needs a root.
owner_quadratics=[]
for lo,hi,phi in [(X,F(3,100),F(371,1000)),(F(3,100),F(1,20),F(3,8)),(F(1,20),T,F(31,80))]:
    qa=-phi/VO
    qb=(phi*CO-EO)/VO
    qc=-DO*RHO+bt+EO*CO/VO
    value,where=qmax(qa,qb,qc,lo,hi)
    assert value<-F(3,10000)
    owner_quadratics.append({'left':str(lo),'right':str(hi),'phi':str(phi),'maximum_location':str(where),'maximum_upper':str(value),'maximum_upper_decimal':float(value)})
assert tu-(1-F(371,1000))>0
assert F(owner_quadratics[0]['maximum_location'])==F(29646127739029,2968000000000000)
assert F(owner_quadratics[0]['maximum_upper'])==F(-1955191732793963624585813319,6391714532250880000000000000000)
owner_leaf=max(1-osigma(T),F(3,8)+FU*RHO+VO/2)
assert owner_leaf==F(547441072186,10**12)<Q-F(55,10**5)
hhalf=F(374,461);uhalf=1-hhalf;vhalf=hhalf-F(1,2)
assert 3**1383>2**2192
owner_half_r=-DO*RHO+(2*hhalf-F(3,2))/2+bt
owner_half_q=F(3,4)-AO*RHO-uhalf/2-T+bt
owner_half_f=max(F(1,2),F(3,8)+FU*RHO+vhalf/4)
assert owner_half_r==F(-8711179803779801,230500000000000000)<-F(3779,10**5)
assert owner_half_q==F(57308853692168787,115250000000000000)<F(49726,10**5)
assert owner_half_f==F(1,2)
rt=F(18,25);aold=F(5,4)-F(3,2)*hhalf
tail_r=-uhalf*rt+(2*hhalf-F(3,2))/2+rt*B/2
tail_q=F(3,4)-aold*rt-uhalf/2-T+rt*T/2
tail_f=max(F(1,2),F(3,8)+vhalf*rt/4+vhalf/4)
assert tail_r<-F(15,10000)
assert tail_q==F(628599,1152500)<F(54543,10**5)<Q
assert tail_f==F(11729,23050)<F(50886,10**5)<Q
assert 1-HQ-B/2>0
assert F(19,100)*rt<F(1,5)
assert F(7,10)*F(19,100)*rt**2<1-rt

# Biased middle: exact quadratic boundary reductions.
S=F(21,50);DL=F(1,2)+S-H0-TAU0
AA=F(3,4)+S-F(3,2)*H0-TAU0
CC=DL-AA;FF=H0/4-F(1,8)
VV,EE,RR=H-F(1,2),2*H-1-F(9,20)+TAU,F(9,20)+F(1,2)-H-TAU
R0,Z=F(121,200),F(49,600)
bb=F(3,4)-Q;BB=bb+CC*R0;KK=3*CC;CAP=BB-VV;ZCAP=CAP/(1-KK)
assert EE+RR==VV and FF==CC/2
assert BB==F(27504852882943,10**14)
assert ZCAP==F(585569981543,63777589010200)
assert T<17*P/92 and F(17,20)<F(19,20)**3
assert F(1,100)<11*P/161 and F(16,25)**2<F(21,25)**5
def rho(a):return min(R0+3*a,F(17,20))
def ss(a,x):return min(F(1),(bb+CC*rho(a)-x)/VV)
def rbar(a,x,p0,ph):
    return -DL*rho(a)+(EE+ph*x)*ss(a,x)+F(19,20)*p0*a*rho(a)
topranges=[(X,F(1,20),F(69,200)),(F(1,20),Z,F(143,400))]
localranges=[(X,F(3,100),F(371,1000)),(F(3,100),F(1,20),F(3,8)),(F(1,20),T,F(31,80))]
source_upper={(0,0):F(-1771431,10**10),(0,1):F(-6064236,10**10),(0,2):F(-16602729,10**10),(1,1):F(-46558153,10**10),(1,2):F(-40912578,10**10)}
polygons=[];diagcoef=[]
for i,(a0,a1,p0) in enumerate(topranges):
    for j,(xlo,xhi,ph) in enumerate(localranges):
        poly=[(a0,xlo),(a1,xlo),(a1,xhi),(a0,xhi)]
        poly=clip(poly,F(1),F(-1),F(0))
        poly=clip(poly,KK,F(-1),-CAP)
        if not poly:
            assert (i,j) not in source_upper
            continue
        assert (i,j) in source_upper
        assert 3*F(19,20)*p0>0
        dc=3*F(19,20)*p0+ph*(KK-1)/VV
        diagcoef.append(dc);assert dc>0
        candidates=[(rbar(a,x,p0,ph),a,x) for a,x in poly]
        for z in [a0,a1]:
            lo=max(z,xlo,CAP+KK*z);hi=xhi
            if lo<=hi:
                critical=(bb+CC*rho(z)-EE/ph)/2
                xx=min(max(critical,lo),hi)
                candidates.append((rbar(z,xx,p0,ph),z,xx))
        value,za,zx=max(candidates)
        assert value<source_upper[i,j]<-F(1,6000)
        polygons.append({'top_case':i,'local_case':j,'phi_top':str(p0),'phi_local':str(ph),'vertices':[[str(a),str(x)] for a,x in poly],'maximum_location':[str(za),str(zx)],'maximum_upper':str(value),'maximum_upper_decimal':float(value),'published_upper':str(source_upper[i,j])})
assert len(polygons)==5
assert min(diagcoef)==F(35091383426981,538385658028000)>0
assert F(polygons[0]['maximum_location'][1])==F(7574073885281873,742000000000000000)
prho=F(17,20);p0=F(143,400);ph=F(31,80)
pcrit=(ph*(bb+CC*prho)-EE+F(19,20)*p0*prho*VV)/(2*ph)
assert pcrit==F(8011512564987923,62000000000000000) and Z<=pcrit<=T
plateau_r=rbar(pcrit,pcrit,p0,ph)
assert plateau_r<F(-37421981,10**10)<-F(1,6000)
assert X<ZCAP<F(1,100)
cap_r=[];cap_q=[]
for a in [X,ZCAP]:
    ro=rho(a)
    cap_r.append(-DL*ro+EE+F(21,25)*F(69,200)*a*ro+F(371,1000)*(CAP+KK*a))
    cap_q.append(F(3,4)-AA*ro-RR+(F(371,1000)-1)*a+F(21,25)*F(69,200)*a*ro)
assert max(cap_r)<F(-3827602,10**10)<-F(1,6000)
# The actual top root gives the tight cap restart maximum at X.
cap_l,cap_u=roots(X,rho(X))
assert cap_l==F(515456646931,NROOT)
beta_prime_upper=F(635,1000)+F(1,100)*(1+3*P)/(ALPHA*(P-F(1,100)))
assert beta_prime_upper<F(7,10)
assert -3*AA+(F(371,1000)-1)+F(69,200)*F(7,10)<0
critical=F(3,4)-AA*rho(X)-RR+(F(371,1000)-1)*X+F(69,200)*X*cap_u
assert critical==F(54784907211651059,10**17)
actual_q=critical+F(1,10**9)
fallback=F(3,4)-actual_q
assert actual_q==F(54784907311651059,10**17)<Q
assert fallback<B and actual_q+fallback==F(3,4)
cap_q=[critical]
biased_leaf=F(3,8)+FF*rho(ZCAP)+VV/2
assert biased_leaf<F(5477835481,10**10)<Q-F(1,5000)
sigma_min=(bb+CC*rho(X)-T)/VV
assert sigma_min==F(143127433763563,269192829014000)>F(53,100)
inc=[];half_r=[];half_q=[];half_f=[]
for a,p0 in [(X,F(69,200)),(F(1,20),F(69,200)),(F(1,20),F(143,400)),(Z,F(143,400)),(T,F(143,400))]:
    ro=rho(a);top=F(19,20)*p0*a*ro
    inc.append(TAU0*ro/2+top-a)
    half_r.append(-DL*ro+(2*HQ-F(3,2))/2+top)
    half_q.append(F(3,4)-AA*ro-(1-HQ)/2-T+top)
    half_f.append(max(F(1,2),F(3,8)+FF*ro+(HQ-F(1,2))/4))
assert max(inc)<F(-8968462,10**10)<-F(1,1250)
assert max(half_r)<F(-357253886,10**10)<-F(1,50)
assert max(half_q)<F(5262657137,10**10)<Q-F(1,50)
assert max(half_f)<F(5041346134,10**10)<Q-F(1,25)

# Complete uniform auxiliary envelopes, in units of m.
e05=entropy(F(1,20));e225=entropy(F(9,40));e21=entropy(F(21,100));e45=entropy(F(9,20))
assert e05[0]>F(28639,10**5) and e05[1]<F(28640,10**5)
assert e225[0]>F(76919,10**5) and e225[1]<F(76920,10**5)
assert e21[0]>F(74148,10**5) and e21[1]<F(74149,10**5)
assert TAU0<F(1855,10**5) and TAU<F(723,10**5)
assert HQ<F(81128,10**5)
dbin_lo,dbin_hi=1-entropy(F(14,25))[1],1-entropy(F(14,25))[0]
assert dbin_lo>F(27,2600)>X and dbin_hi<F(11,1000)
assert RHO*F(2,15)*(1-e05[0]-PD)<F(8,100)<1-RHO
assert RHO*(F(2,15)*(1-PD)-PD)==F(69,1000)<1-RHO
owner_beta=RHO*X
owner_cover=F(3,2)*RHO+2*owner_beta
owner_top_covers=(1+2*e05[1])*RHO+owner_beta
owner_top_primes=(1+e05[1])*RHO+owner_beta+F(45,100)/16
assert owner_cover==F(13653,10000)
assert owner_top_covers<F(142317,10**5)
owner_table=RHO*(e05[1]+F(3,4)*dbin_hi)
assert owner_table<F(265185,10**6)
maxownerregion=RHO*(F(1,2)+F(1,15))
container_prep=3*maxownerregion/4;container_state=maxownerregion/4
assert container_prep==F(3825,10000) and container_state==F(1275,10000)
outer_rate=F(85,100)*(F(1855,10**5)+F(143,400)*T)
assert outer_rate==F(56790625,10**9)<F(57,1000)
top_code=F(142,100)*F(85,100)+F(143,400)*F(85,100)*T
assert top_code<F(1249,1000)
top_translate=F(142,100)*F(85,100)+outer_rate
assert top_translate<F(1264,1000)
# Projection cap and useful-layer movable entropy, using actual ceilings.
dbase_hi=F(92,100)-e21[0]
assert F(28,25)*dbase_hi*F(85,100)**2<F(145,1000)<F(15,100)
assert F(1855,10**5)+F(143,400)*T<F(67,1000)
entropy_receipts.extend([eh(F(1,10),lower=F(4,10)),eh(F(1,5),lower=F(7,10))])
cstar=F(202,1000)+(F(74149,10**5)-F(1,2))*F(85,100)/2
vmin=F(26919,10**5);xstar=cstar-vmin
local_code=F(145,100)+F(31,80)*xstar
assert cstar==F(30463325,10**8) and xstar==F(3544325,10**8)
assert F(31,80)*cstar<F(145,100) and local_code<F(1464,1000)
local_prime=1+F(45,100)+F(45,100)/16
assert local_prime==F(473,320)<F(3,2)
cache=F(723,10**5)+F(31,80)*T
assert cache==F(595425,10**7)
own_local_cover=F(145,100)+owner_beta
middle_local_cover=F(145,100)+F(635,1000)*(F(1855,10**5)+F(143,400)*F(1,100))
assert middle_local_cover==F(1464049375,10**9)<F(1465,1000)
# Diagonal sigma leaves its cap before .01; then scan+outer-rate decreases.
assert ZCAP<F(1,100) and (3*CC-1)/VV<-F(23,10)
assert 3*(F(1855,10**5)+F(143,400)*Z)+F(17,20)*F(143,400)<F(448,1000)
histograms=F(57,1000)+cache+F(9,10)
assert histograms<F(1017,1000)
full_histograms=1+F(57,1000)
beta_bar=F(3,4)+(F(74149,10**5)/2-F(1,4))*F(85,100)+(F(76920,10**5)-F(1,2))
assert beta_bar<F(1122,1000)
ell_strict=(F(45,100)-F(31,80)*T)*F(53,100)
ell_half=F(1,4)-B/4
assert min(ell_strict,ell_half)>F(195,1000)
single_child_scan=F(1122,1000)-F(195,1000)
lift=F(45,100)+single_child_scan+F(5955,10**5)+F(57,1000)
assert lift==F(149355,10**5)<F(3,2)
restart_init=F(3,4)-(F(45,100)+F(1,2)-e225[0])
leaf_init_gap=F(3,8)-(F(45,100)+F(1,4)-e225[0]/2)
assert restart_init>F(56919,10**5)>Q and leaf_init_gap>F(5959,10**5)
child_low_strict=(F(3,2)-F(723,10**5)-T)/2
child_low_half=(F(3,2)-B)/2
assert min(child_low_strict,child_low_half)>F(64,100)
assert actual_q+fallback==F(3,4)
prep={'owner_cover':owner_cover,'owner_top_weighted_covers':owner_top_covers,'owner_top_prime_scans':owner_top_primes,'tensorized_container_preparation':container_prep,'biased_top_code':top_code,'biased_top_translate_covers':top_translate,'shared_local_code':local_code,'shared_local_prime':local_prime,'biased_top_prime_scans':top_translate+F(45,100)/16,'owner_local_weighted_covers':own_local_cover,'biased_local_weighted_covers':middle_local_cover,'signing_histograms':histograms,'full_support_histogram_replay':full_histograms,'pure_lift_scans_and_starts':lift,'ordinary_high_tail_separators':F(108,100),'full_support_counting':F(1),'cached_elementary_local_layouts':F(145,100),'cached_ordinary_top_layouts':F(72,100)*F(317,200),'cached_biased_top_layouts':F(85,100)*F(317,200)}
assert 3**200<2**317
for key,val in prep.items():assert val+ERROR<F(3,2),(key,float(val))
states={'support_counting':F(1,2),'owner_canonical_trace':RHO/2,'residues':F(45,100),'owner_assignment_tuples':owner_table,'biased_top_tuples':S*F(85,100),'high_tail_tuples':rt/2,'local_seed_cache':cache,'outer_top_labels':outer_rate,'complementary_support':F(1,2),'tensor_preparation':container_state}
for key,val in states.items():assert val+ERROR<actual_q,(key,float(val))
assert max(owner_tiny_r,max(F(r['maximum_upper']) for r in owner_quadratics))+ERROR<0
assert max(owner_tiny_q0,owner_tiny_qx,Q-F(3,10000))+ERROR<actual_q
assert max(owner_leaf,owner_half_f,tail_f,biased_leaf,max(half_f))+ERROR<actual_q
assert max(max(F(p['maximum_upper']) for p in polygons),plateau_r,max(cap_r))+ERROR<0
assert max(cap_q)+ERROR<actual_q and tail_q+ERROR<actual_q
assert Q+max(max(F(p['maximum_upper']) for p in polygons),plateau_r)+ERROR<actual_q
assert max(owner_half_q,max(half_q))+ERROR<actual_q
assert max(inc)+ERROR<0

active_integer_certificates={
 'top_support_forces_quarter_layer':3**9>2**14,
 'entropy_one_tenth_greater_45_over_100':10**20>2**9*9**18,
 'entropy_one_fifth_greater_7_over_10':5**10>2**23,
 'local_contrast_less_39_over_80':20**80<2**75*7**28*13**52,
 'entropy_one_ninth_greater_one_half':9**6>2**19,
}
assert all(active_integer_certificates.values())
assert F(143,400)*T<S/8
assert F(31,80)*T<F(9,20)/8
assert F(9,20)/4>F(1,9)
assert F(7,16)<F(47,100) and F(53,100)>F(1,2)
assert F(23,40)>F(1,2) and F(39,80)<F(1,2)

def exact_decimal(x):
    with localcontext() as ctx:
        ctx.prec=60
        return str(Decimal(x.numerator)/Decimal(x.denominator))

previous=F(412842547079759,2250000000000000)
result={'status':'PASS','time_exponent':'1/2','design_capacity':str(Q),'capacity':str(actual_q),'capacity_decimal_exact':exact_decimal(actual_q),'space_exponent':str(actual_q/3),'space_exponent_decimal':exact_decimal(actual_q/3),'implied_checkpoint_space_exponent':str(Q/3),'critical_restart_upper':str(critical),'critical_restart_location':[str(X),str(X)],'finite_grid':QGRID,'previous_refined_space_exponent':str(previous),'improvement':str(previous-actual_q/3),'improvement_decimal':exact_decimal(previous-actual_q/3),'finite_linear_error_allowance':str(ERROR),'fixed_high_deficiency_cutoff':str(fallback),'certified_high_tail_domain_upper':str(B),'fallback_identity':str(actual_q+fallback),'entropy_checks':entropy_receipts,'active_retained_layer_integer_certificates':active_integer_certificates,'owner':{'top_root_lower_numerator':int(tl*NROOT),'top_deficiency_upper':str(bt),'tiny_raw_upper':str(owner_tiny_r),'tiny_restart_upper':str(max(owner_tiny_q0,owner_tiny_qx)),'local_quadratics':owner_quadratics,'leaf_upper':str(owner_leaf),'half_raw_upper':str(owner_half_r),'half_restart_upper':str(owner_half_q),'half_leaf_upper':str(owner_half_f)},'biased':{'rising_polygons':polygons,'plateau_maximum':str(plateau_r),'plateau_critical':str(pcrit),'cap_raw_maximum':str(max(cap_r)),'cap_restart_maximum':str(max(cap_q)),'cap_top_root_lower_numerator':int(cap_l*NROOT),'cap_beta_derivative_upper':str(beta_prime_upper),'leaf_maximum':str(biased_leaf),'incidence_maximum':str(max(inc)),'half_raw_maximum':str(max(half_r)),'half_restart_maximum':str(max(half_q)),'half_leaf_maximum':str(max(half_f)),'strict_minimum_core_fraction':str(sigma_min)},'high_tail':{'raw_upper':str(tail_r),'restart_upper':str(tail_q),'leaf_upper':str(tail_f)},'preparation':{k:{'rational':str(v),'decimal':float(v)} for k,v in prep.items()},'state':{k:{'rational':str(v),'decimal':float(v)} for k,v in states.items()},'initialization':{'uncompressed_filtered_budget_lower':str(restart_init),'leaf_minus_shell_gap_lower':str(leaf_init_gap),'strict_image_scale_lower':str(ell_strict),'half_image_scale_lower':str(ell_half),'lift_loop_upper':str(lift)}}
if args.output:
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k:result[k] for k in ['status','capacity','space_exponent','space_exponent_decimal','improvement','improvement_decimal','finite_linear_error_allowance','time_exponent']},indent=2))
