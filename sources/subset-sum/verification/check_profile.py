#!/usr/bin/env python3
"""Finite profile audit. Default: cached-contact integrity and fresh scalar checks.
--full reconstructs all continuous contacts with exact rational acceptance.
A cached count/margin receipt alone is not an independent replay of its leaves.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json, time
from profile_core import certify, CONTACTS
from profile_summary import summary
if not __debug__:raise RuntimeError('Run with assertions enabled.')
BASE=Path(__file__).resolve().parent
SOURCES=['profile_core.py','profile_direct.py','profile_summary.py','check_profile.py']
def digests():return {n:hashlib.sha256((BASE/n).read_bytes()).hexdigest() for n in SOURCES}
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full',action='store_true',help='Reconstruct every continuous-domain contact; several minutes.')
    parser.add_argument('--receipt',type=Path,default=BASE/'profile_receipt.json')
    args=parser.parse_args();start=time.time()
    if args.full:
        first=[];new=[]
        for rr,gg,x,u,y,v in [('1.3','.47','.24','.12004','.40','.16082'),('1.7','.47','.40','.15966','.45','.17177')]:
            for tt,bb in ((x,u),(y,v)):first.append(certify(F(rr),F(gg),F(tt),F(bb),'first'))
        for rr,gg,x,u,y,v in CONTACTS:
            for tt,bb in ((x,u),(y,v)):
                for mode in ['push','recursive']:new.append(certify(F(rr),F(gg),F(tt),F(bb),mode))
        scalars=summary(True)
        result=dict(status='PASS',mode='full exact rational reconstruction',sources=digests(),first_contacts=first,new_contact_branches=new,profile_summary=scalars,seconds=time.time()-start)
        args.receipt.write_text(json.dumps(result,indent=2)+'\n')
    else:
        result=json.loads(args.receipt.read_text())
        assert result['status']=='PASS' and result['sources']==digests(),'Receipt/source mismatch; run --full.'
        new=result['new_contact_branches'];first=result['first_contacts']
        assert len(new)==24 and len(first)==4
        assert sum(r['leaves'] for r in new)==204538
        assert all(F(r['minimum_slack'])>0 for r in new+first)
        scalars=json.loads(json.dumps(summary(False)))
        for name in ['D_interval','quadratic_maximum','quadratic_margin','comparisons','energy_counterexample']:
            assert scalars[name]==result['profile_summary'][name],name
    print(json.dumps(dict(status='PASS',mode='full reconstruction' if args.full else 'cached contact/source integrity; fresh 76 scalar comparisons and energy recurrence',new_contact_leaves=sum(r['leaves'] for r in result['new_contact_branches']),trace_corrected_leaves=sum(r['corrected'] for r in result['new_contact_branches']),quadratic_maximum=result['profile_summary']['quadratic_maximum'],seconds=time.time()-start),indent=2))
if __name__=='__main__':main()
