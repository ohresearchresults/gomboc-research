"""Explicit primal or polar edge events in actual-centroid contact search.
Only numerically admitted bodies continue. Topology proposals do not establish
exact hull counts; each claimed physical result needs a rational audit.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,argparse,time
import numpy as np
from contact_forest import ContactModel
from contact_persistence_flow import run as descend
from merge_contact_facets import run as merge_facets
from merge_contact_vertices import run as merge_vertices

def run(source,input,out,side='P',rounds=30,tol=1e-7):
    source=pathlib.Path(source);input=pathlib.Path(input);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);start=time.time();history=[]
    nU,nS=(2,1) if side=='P' else (1,2)
    for k in range(rounds):
        c=ContactModel(source,nU,nS,'local',exempt_junior=True);e=c.evaluate(np.load(input)['z'],False)
        lengths=[]
        for A,edges in [(e['X'],c.eu),(e['Y'],c.es)]:
            lengths.append(float(np.min(np.linalg.norm(A[edges[:,0]]-A[edges[:,1]],axis=1))/np.sqrt(np.mean(A*A))))
        kind='vertices' if lengths[0]<lengths[1] else 'facets'
        folder=out/f'event{k:03d}-{kind}';folder.mkdir(parents=True,exist_ok=False)
        if min(lengths)>tol:
            (folder/'STOP_NO_VANISHING_EDGE.json').write_text(json.dumps(dict(primal_relative=lengths[0],polar_relative=lengths[1],threshold=tol,source=str(source),input=str(input)),indent=2));print('NO_ADMISSIBLE_EDGE_EVENT',lengths,flush=True);break
        producer=merge_vertices if kind=='vertices' else merge_facets
        try:summary=producer(source,input,folder/'body',tol,nU,nS,'quality')
        except (ValueError,AssertionError,RuntimeError,np.linalg.LinAlgError) as error:
            (folder/'UNADMITTED.json').write_text(json.dumps(dict(source=str(source),input=str(input),kind=kind,error=repr(error)),indent=2));print('PROPOSAL_UNADMITTED',k,repr(error),flush=True);break
        source=folder/'body/chart';input=folder/'body/realization.npz'
        if summary['S']==summary['U']==1:
            (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(source.resolve()),input=str(input.resolve()),scope='Numerical physical body requires exact audit'),indent=2));return
        if summary['S']>nS or summary['U']>nU:
            print('EVENT_ADMITTED_BUT_EXTRA_EQUILIBRIA',summary,flush=True);break
        descend(source,folder/'flow',side=side,steps=200)
        if (folder/'flow/POTENTIAL_OWN110.npz').exists():
            (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(source.resolve()),input=str((folder/'flow/POTENTIAL_OWN110.npz').resolve()),scope='Numerical physical body requires exact audit'),indent=2));return
        input=folder/'flow/latest.npz';c=ContactModel(source,nU,nS,'local',exempt_junior=True);e=c.evaluate(np.load(input)['z'],False)
        row=dict(event=k,kind=kind,scope='Numerical contact body; rational audit pending',V=len(e['X']),E=c.meta['E'],F=c.F,S=e['S'],U=e['U'],objective=max([b['relative'] for b in e['bars'][0 if side=='P' else 1]],default=0),minimum=float(e['mechanical'].min()),minimum_gap=e['minimum_gap'],chart=str(source.resolve()),input=str(input.resolve()),seconds=time.time()-start);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('CONTACT_EVENT_END',row,flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--side',choices=['P','Q'],default='P');ap.add_argument('--rounds',type=int,default=30);a=ap.parse_args();run(a.source,a.input,a.out,a.side,a.rounds)
