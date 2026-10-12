"""Literal halfspace deletion at a nominated nearly coincident facet pair.
This defines fresh convex bodies and reconstructs their complete true contact
graphs. It is distinct from asserting that the original planes are coplanar.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,pathlib,json,time,contextlib
import numpy as np
from contact_forest import ContactModel,correct
from make_contact_atlas import make
from geometry import halfspace_mesh,census
from basin_scout import score
from contact_topology_continuation import run as continue_contacts

def run(source,input,out,tol=1e-5,limit=8):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);c=ContactModel(source,1,2,'local',exempt_junior=True);e=c.evaluate(np.load(input)['z'],False);Y=e['Y'];length=np.linalg.norm(Y[c.es[:,0]]-Y[c.es[:,1]],axis=1)/np.sqrt(np.mean(Y*Y));ids=sorted(set(c.es[length<tol].ravel().tolist()));history=[];start=time.time();candidates=[]
    (out/'definition.json').write_text(json.dumps(dict(source=str(pathlib.Path(source).resolve()),input=str(pathlib.Path(input).resolve()),threshold=tol,nominated_facets=ids,scope='Literal deletion of individual supporting inequalities; each resulting body re-integrated'),indent=2))
    for f in ids:
        q=np.delete(Y,f,axis=0);folder=out/f'delete{f:03d}';folder.mkdir();np.savez(folder/'literal-supports.npz',Q=q)
        try:
            m=halfspace_mesh(q);s=score(q)
            row=dict(deleted=f,**s)
            if 17<=s['E']<249:
                Q=q[m['active']];proposal=dict(scope='Numerical true hull after literal halfspace deletion; exact audit pending',V=len(m['X']),E=len(m['edges']),F=len(Q),faces=m['faces'],edges=m['edges'].tolist(),active=list(range(len(Q))),raw_vertices=[[str(x) for x in v] for v in m['X']],raw_halfspaces=[[str(x) for x in v]+['1'] for v in Q]);(folder/'proposal.json').write_text(json.dumps(proposal,indent=2));make(folder/'proposal.json',folder/'chart',balanced=True)
                child=ContactModel(folder/'chart',1,2,'local',exempt_junior=True);ee=child.evaluate(child.initial,False);np.savez(folder/'realization.npz',z=child.initial,X=ee['X'],Q=ee['Y']);candidates.append((s['score'],f,folder))
                row['reconstructed_census']=[ee['S'],ee['U']];row['minimum']=float(ee['mechanical'].min())
                if ee['S']==ee['U']==1:
                    (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str((folder/'chart').resolve()),input=str((folder/'realization.npz').resolve())),indent=2));history.append(row);(out/'screen.json').write_text(json.dumps(history,indent=2));return
        except (ValueError,AssertionError,RuntimeError,np.linalg.LinAlgError) as err:row=dict(deleted=f,error=repr(err))
        history.append(row);(out/'screen.json').write_text(json.dumps(history,indent=2));print('LITERAL_NEAR_FACET_RETIREMENT',json.dumps(row),flush=True)
    for rank,(_,f,folder) in enumerate(sorted(candidates)[:limit]):
        with (folder/'continuation.log').open('w') as log,contextlib.redirect_stdout(log):
            continue_contacts(folder/'chart',folder/'realization.npz',folder/'continuation',side='Q',rounds=12,tol=1e-7,strategy='balanced',flow_steps=120)
        if (folder/'continuation/POTENTIAL_OWN110.json').exists():
            (out/'POTENTIAL_OWN110.json').write_bytes((folder/'continuation/POTENTIAL_OWN110.json').read_bytes());return
        print('RETIRED_BODY_CONTINUATION_FINISHED',f,time.time()-start,flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--tolerance',type=float,default=1e-5);ap.add_argument('--limit',type=int,default=8);a=ap.parse_args();run(a.source,a.input,a.out,a.tolerance,a.limit)
