"""Trace the introduced cap vertices through incidence quotients and retire them.
Each deletion makes a fresh literal convex hull. The complete own-centroid
class is then corrected and its new contacts continued. No ancestor mass or
equilibrium assertion is transferred to a child body.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,pathlib,json,itertools,time,contextlib
import numpy as np
from contact_forest import ContactModel
from make_contact_atlas import make
from stable_face_augmentation import halfspaces
from geometry import halfspace_mesh
from basin_scout import score
from contact_topology_continuation import run as continue_contacts

def trace(chart,root,root_input,cache):
    chart=pathlib.Path(chart).resolve();root=pathlib.Path(root).resolve()
    if str(chart) in cache:return cache[str(chart)]
    c=ContactModel(chart,1,2,'local',exempt_junior=True)
    if chart==root:
        X=np.load(root_input)['X'];A=c.A0[c.F:];dist=np.linalg.norm(A[:,None,:]-X[None,:,:],axis=2);ix=dist.argmin(1);assert np.max(dist[np.arange(len(ix)),ix])<1e-9 and len(set(ix.tolist()))==len(ix);labels=['main','compensation0','compensation1','compensation2'];tags=[([labels[int(i)-len(X)+4]] if i>=len(X)-4 else []) for i in ix]
    else:
        proposal=pathlib.Path(c.meta['source']);j=json.loads(proposal.read_text());parent=pathlib.Path(j['source']);prior=trace(parent,root,root_input,cache)
        if 'vertex_groups' in j:tags=[sorted(set(tag for i in group for tag in prior[i])) for group in j['vertex_groups']]
        else:
            pc=ContactModel(parent,1,2,'local',exempt_junior=True);old=pc.evaluate(np.load(j['input'])['z'],False)['X'];new=np.array(j['raw_vertices'],float);dist=np.linalg.norm(new[:,None,:]-old[None,:,:],axis=2);ix=dist.argmin(1);assert np.max(dist[np.arange(len(ix)),ix])<1e-9 and len(set(ix.tolist()))==len(ix);tags=[prior[int(i)] for i in ix]
    cache[str(chart)]=tags;return tags

def run(source,input,root,root_input,out):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);c=ContactModel(source,1,2,'local',exempt_junior=True);e=c.evaluate(np.load(input)['z'],False);cache={};tags=trace(source,root,root_input,cache);indices=[i for i,t in enumerate(tags) if any(s.startswith('compensation') for s in t)];(out/'lineage.json').write_text(json.dumps(dict(source=str(pathlib.Path(source).resolve()),input=str(pathlib.Path(input).resolve()),root=str(pathlib.Path(root).resolve()),root_input=str(pathlib.Path(root_input).resolve()),tags=tags,tagged_compensation_vertices=indices,all_charts=cache),indent=2));history=[];start=time.time();print('TAGGED_COMPENSATORS',[(i,tags[i]) for i in indices],flush=True)
    for size in range(len(indices),0,-1):
        for removed in itertools.combinations(indices,size):
            folder=out/('delete-'+'-'.join(map(str,removed)));folder.mkdir();X=np.delete(e['X'],removed,axis=0)
            try:
                Q=halfspaces(X);m=halfspace_mesh(Q);s=score(Q);row=dict(removed=list(removed),before=s)
                if not 17<=s['E']<249:raise ValueError('literal retirement outside edge budget')
                Y=Q[m['active']];proposal=dict(scope='Numerical complete hull after literal vertex retirement; exact audit required',source=str(pathlib.Path(source).resolve()),removed_vertices=list(removed),V=len(m['X']),E=len(m['edges']),F=len(Y),faces=m['faces'],edges=m['edges'].tolist(),active=list(range(len(Y))),raw_vertices=[[str(v) for v in p] for p in m['X']],raw_halfspaces=[[str(v) for v in p]+['1'] for p in Y]);(folder/'proposal.json').write_text(json.dumps(proposal,indent=2));make(folder/'proposal.json',folder/'chart',balanced=True);child=ContactModel(folder/'chart',1,2,'local',exempt_junior=True);ee=child.evaluate(child.initial,False);np.savez(folder/'realization.npz',z=child.initial,X=ee['X'],Q=ee['Y'])
                with (folder/'continuation.log').open('w') as log,contextlib.redirect_stdout(log):continue_contacts(folder/'chart',folder/'realization.npz',folder/'continuation',side='Q',rounds=12,tol=1e-7,strategy='balanced',flow_steps=100)
                if (folder/'continuation/POTENTIAL_OWN110.json').exists():
                    (out/'POTENTIAL_OWN110.json').write_bytes((folder/'continuation/POTENTIAL_OWN110.json').read_bytes());return
                h=folder/'continuation/history.json'
                if h.exists():row['after']=json.loads(h.read_text())[-1]
                row['seconds']=time.time()-start
            except (ValueError,AssertionError,RuntimeError,np.linalg.LinAlgError) as error:row=dict(removed=list(removed),error=repr(error),seconds=time.time()-start)
            history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('RETIRED_COMPENSATION_CAP',json.dumps(row),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--input',required=True);ap.add_argument('--root',required=True);ap.add_argument('--root-input',required=True);ap.add_argument('--out',required=True);a=ap.parse_args();run(a.source,a.input,a.root,a.root_input,a.out)
