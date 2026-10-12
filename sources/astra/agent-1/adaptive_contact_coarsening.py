"""Finite own121 descent with explicit facet-union events and re-admission.
Every intermediate is labelled numerical. A potential own110 body is preserved
immediately and terminates this experiment for an independent rational audit.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,pathlib,time
import numpy as np
from contact_forest import ContactModel
from contact_persistence_flow import run as descend
from merge_contact_facets import run as merge

def run(source,input,out,rounds=15):
    source=pathlib.Path(source);input=pathlib.Path(input);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);history=[];start=time.time()
    for k in range(rounds):
        folder=out/f'round{k:03d}';folder.mkdir(parents=True,exist_ok=True)
        try:summary=merge(source,input,folder/'union',tol=1e-9,nU=2,nS=1,strategy='quality')
        except (ValueError,AssertionError,RuntimeError,np.linalg.LinAlgError) as error:
            (folder/'UNADMITTED_PROPOSAL.json').write_text(json.dumps(dict(error=repr(error),source=str(source),input=str(input)),indent=2));print('CONTACT_UNION_NOT_ADMITTED',k,repr(error),flush=True);break
        source=folder/'union/chart';input=folder/'union/realization.npz'
        if summary['S']==summary['U']==1:
            (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(source.resolve()),input=str(input.resolve()),scope='Numerical physical body, exact audit required'),indent=2));return
        if summary['S']!=1 or summary['U']!=2 or summary['minimum']<=0:
            print('CONTACT_UNION_LOST_OWN121',summary,flush=True);break
        print('NUMERICAL_CONTACT_PHASE',k,summary,flush=True)
        descend(source,folder/'flow',side='P',steps=160)
        input=folder/'flow/latest.npz'
        if (folder/'flow/POTENTIAL_OWN110.npz').exists():
            (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(source.resolve()),input=str((folder/'flow/POTENTIAL_OWN110.npz').resolve()),scope='Numerical physical body, exact audit required'),indent=2));return
        c=ContactModel(source,2,1,'local');e=c.evaluate(np.load(input)['z'],False)
        row=dict(round=k,scope='Numerical contact body, not exact census claim',V=len(e['X']),E=c.meta['E'],F=c.F,S=e['S'],U=e['U'],P=max([b['relative'] for b in e['bars'][0]],default=0),minimum=float(e['mechanical'].min()),minimum_gap=e['minimum_gap'],chart=str(source.resolve()),input=str(input.resolve()),seconds=time.time()-start);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('NUMERICAL_CONTACT_PHASE_END',row,flush=True)
        if e['S']!=1 or e['U']!=2:break

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--rounds',type=int,default=15);a=ap.parse_args();run(a.source,a.input,a.out,a.rounds)
