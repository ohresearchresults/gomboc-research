"""Actual-mass correction/descent across explicitly rebuilt hull complexes.
Incidence changes are proposals, followed by complete convex-domain admission.
This search never certifies an edge count by a small-distance threshold.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,pathlib,json,time
import numpy as np
from contact_forest import ContactModel,correct
from contact_persistence_flow import run as descend
from merge_contact_facets import run as merge_facets
from merge_contact_vertices import run as merge_vertices
from repair_contact_domain import run as domain_admit

def run(source,input,out,side='Q',rounds=20,tol=1e-7,strategy='balanced',flow_steps=180,epsilon=1e-7,objective_mode='bar',hold_unique_only=False,primal_weight=1.):
    source=pathlib.Path(source);input=pathlib.Path(input);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);nU,nS=(1,2) if side=='Q' else (2,1);history=[];start=time.time()
    (out/'definition.json').write_text(json.dumps(dict(source=str(source.resolve()),input=str(input.resolve()),side=side,rounds=rounds,threshold=tol,strategy=strategy,flow_steps=flow_steps,epsilon=epsilon,objective_mode=objective_mode,hold_unique_only=hold_unique_only,primal_weight=primal_weight,scope='Numerical actual-centroid contact continuation; all incidence claims need an exact audit'),indent=2))
    for k in range(rounds):
        folder=out/f'stage{k:03d}';folder.mkdir()
        if objective_mode=='joint-tree':
            if hold_unique_only:raise ValueError('Joint-tree mode has no unique-opposite-class restriction')
            from contact_multibasin_flow import EssentialMaxima
            c=EssentialMaxima(source);nU,nS=c.root_counts
        elif hold_unique_only:
            from contact_multibasin_flow import UniqueUnstable,UniqueStable
            c=(UniqueUnstable if side=='Q' else UniqueStable)(source);nU,nS=c.root_counts
        else:c=ContactModel(source,nU,nS,'local',exempt_junior=True)
        z=np.load(input)['z'];e=c.evaluate(z,False)
        ok=bool(e['S']<=nS and e['U']<=nU and e['mechanical'].min()>.8*epsilon)
        if not ok:
            z,e,ok=correct(c,z,folder/'class-correction',steps=90,eps=epsilon,trust=.002,verbose=False,polish_margin=True,physical_retraction=True)
            np.savez(folder/'corrected.npz',z=z,X=e['X'],Q=e['Y']);input=folder/'corrected.npz'
        if e['S']==e['U']==1:
            (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(source.resolve()),input=str(input.resolve())),indent=2));return
        if ok:
            descend(source,folder/'flow',side=side,input=input,steps=flow_steps,eps=epsilon,edge_event_tolerance=tol,objective_mode=objective_mode,hold_unique_only=hold_unique_only,primal_weight=primal_weight)
            if (folder/'flow/POTENTIAL_OWN110.npz').exists():
                (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(source.resolve()),input=str((folder/'flow/POTENTIAL_OWN110.npz').resolve())),indent=2));return
            input=folder/'flow/latest.npz';e=c.evaluate(np.load(input)['z'],False)
        lengths=[float(np.min(np.linalg.norm(A[ed[:,0]]-A[ed[:,1]],axis=1))/np.sqrt(np.mean(A*A))) for A,ed in [(e['X'],c.eu),(e['Y'],c.es)]]
        row=dict(stage=k,V=len(e['X']),E=c.meta['E'],F=c.F,S=e['S'],U=e['U'],minimum=float(e['mechanical'].min()),Pmax=max((b['relative'] for b in e['bars'][0]),default=0),Qmax=max((b['relative'] for b in e['bars'][1]),default=0),lengths=lengths,source=str(source.resolve()),input=str(input.resolve()),strict_class=bool(ok),held_unique_only=hold_unique_only,seconds=time.time()-start);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('CONTACT_TOPOLOGY_STAGE',json.dumps(row),flush=True)
        if min(lengths)>=tol:
            (folder/'NO_EVENT.json').write_text(json.dumps(row,indent=2));return
        kind='vertices' if lengths[0]<lengths[1] else 'facets';producer=merge_vertices if kind=='vertices' else merge_facets;body=folder/f'merge-{kind}'
        try:producer(source,input,body,tol,nU,nS,strategy)
        except (ValueError,AssertionError,RuntimeError,np.linalg.LinAlgError) as err:
            (folder/'UNADMITTED_INITIAL_PROPOSAL.json').write_text(json.dumps(dict(kind=kind,error=repr(err)),indent=2))
            if not (body/'chart/chart.json').exists():return
            try:domain_admit(body/'chart',body/'domain-admission',nU=nU,nS=nS,eps=1e-9,steps=80)
            except (ValueError,AssertionError,RuntimeError,np.linalg.LinAlgError) as error:
                (folder/'DOMAIN_ADMISSION_FAILED.json').write_text(json.dumps(dict(error=repr(error)),indent=2));return
            if not (body/'domain-admission/ADMITTED.npz').exists():return
            input=body/'domain-admission/ADMITTED.npz'
        else:input=body/'realization.npz'
        source=body/'chart';child=ContactModel(source,nU,nS,'local',exempt_junior=True);ee=child.evaluate(np.load(input)['z'],False)
        if not 17<=child.meta['E']<249:raise ValueError('new body exceeds the intended edge budget')
        (out/'latest-admitted.json').write_text(json.dumps(dict(chart=str(source.resolve()),input=str(input.resolve()),V=len(ee['X']),E=child.meta['E'],F=child.F,S=ee['S'],U=ee['U'],scope='Admitted numerical physical body, equilibrium correction and rational audit may remain'),indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--side',choices=['P','Q'],default='Q');ap.add_argument('--rounds',type=int,default=20);ap.add_argument('--tolerance',type=float,default=1e-7);ap.add_argument('--strategy',choices=['balanced','quality','greedy'],default='balanced');ap.add_argument('--flow-steps',type=int,default=180);ap.add_argument('--epsilon',type=float,default=1e-7);ap.add_argument('--objective-mode',choices=['bar','capacity','capacity-tree','joint-tree'],default='bar');ap.add_argument('--hold-unique-only',action='store_true');ap.add_argument('--primal-weight',type=float,default=1.);a=ap.parse_args();run(a.source,a.input,a.out,a.side,a.rounds,a.tolerance,a.strategy,a.flow_steps,a.epsilon,a.objective_mode,a.hold_unique_only,a.primal_weight)
