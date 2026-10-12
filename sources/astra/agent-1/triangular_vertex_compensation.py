"""One old all-triangular vertex compensates the mass of one new point.

Scientific source exchange: peer agent-3 vertex_mass_compensation.py, pinned in
sources/. This independent adaptation preserves every nonincident maximal
polygon facet in a nonsimple parent by selecting only all-triangular old stars.
Every Newton step checks the actual hull and reference S<=2,U=1. Final claims
require a literal rational whole-body audit at its new own centroid.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,pathlib,json,time,hashlib
from fractions import Fraction
import numpy as np
from scipy.spatial import QhullError
from balanced_flower_caps import parent_data
from balanced_cap_optimize import mass
from stable_face_augmentation import halfspaces
from geometry import halfspace_mesh,arrows
from basin_scout import score

def classify_reference(X):
    Q=halfspaces(X);U=int(np.sum(arrows(X).max(1)<0));S=int(np.sum(arrows(Q).max(1)<0));m=halfspace_mesh(Q);return S,U,Q,m

def eligible_stars(X,old_count,Q,m):
    dist=np.linalg.norm(m['X'][:,None,:]-X[None,:,:],axis=2);mapping=dist.argmin(1)
    if np.max(dist[np.arange(len(mapping)),mapping])>1e-8 or len(set(mapping.tolist()))!=len(mapping):raise ValueError('ambiguous literal input-to-hull vertex mapping')
    faces=[[int(mapping[i]) for i in cy] for cy in m['faces']];stars={i:[cy for cy in faces if i in cy] for i in mapping if i<old_count};return [int(i) for i,cy in stars.items() if cy and all(len(f)==3 for f in cy)]

def run(scout,out,cases=25):
    scout=pathlib.Path(scout);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);candidates=[];seen=set()
    for file in scout.glob('candidate*/summary-numerical.json'):
        row=json.loads(file.read_text())
        if row['S']!=2 or row['U']!=1:continue
        folder=file.parent;v=np.load(folder/'body.npz')['added_points'][0];key=tuple(v)
        if key in seen:continue
        seen.add(key);candidates.append((max(row['Q'],default=0),folder,v))
    candidates.sort(key=lambda r:r[0]);p=None;history=[];start=time.time();best=1.
    for case,(_,source,v) in enumerate(candidates[:cases]):
        r=json.loads((source/'construction.json').read_text());parent=pathlib.Path(r['parent_audit']).parent
        if p is None:
            p=parent_data(parent);P=p['P'];a=p['audit'];raw=np.array([[float(Fraction(s)) for s in row] for row in a['raw_vertices']]);centred=raw-p['centroid'];dmap=np.linalg.norm(P[:,None,:]-centred[None,:,:],axis=2);to_exact=dmap.argmin(1);assert len(set(to_exact.tolist()))==len(P) and np.max(dmap[np.arange(len(P)),to_exact])<1e-8;radius=float(np.max(np.linalg.norm(P,axis=1)))
        base=np.r_[P,v[None]];S,U,Q,m=classify_reference(base);folder=out/f'case{case:03d}';folder.mkdir();np.savez(folder/'base.npz',X=base,Q=Q);(folder/'source.json').write_text(json.dumps(dict(source=str(source.resolve()),parent=str(parent.resolve()),referenceS=S,referenceU=U),indent=2))
        if U!=1 or not 1<=S<=2:continue
        eligible=eligible_stars(base,len(P),Q,m);results=[]
        for index in eligible:
            X=base.copy();closed=False
            for it in range(18):
                V,M,J=mass(X,[index]*3,np.eye(3));norm=float(np.linalg.norm(M)/V)
                if norm<1e-13:closed=True;break
                try:delta=np.linalg.solve(J,-M)
                except np.linalg.LinAlgError:break
                accepted=False
                for level in range(14):
                    Y=X.copy();Y[index]+=delta*2**-level
                    if np.linalg.norm(Y[index]-base[index])>.08*radius:continue
                    try:
                        ss,uu,qq,mm=classify_reference(Y)
                        if uu!=1 or not 1<=ss<=2 or not 17<=len(mm['edges'])<249:continue
                        VV,MM,_=mass(Y,[index]*3,np.eye(3))
                    except (ValueError,QhullError,np.linalg.LinAlgError):continue
                    if VV>m['volume']*.5 and np.linalg.norm(MM)/VV<norm-max(1e-15,norm*1e-5):X=Y;accepted=True;break
                if not accepted:break
            rec=dict(compensator=index,exact_parent_vertex=int(to_exact[index]),iterations=it,closed=closed,mass_norm=float(np.linalg.norm(mass(X,[index]*3,np.eye(3))[1])/mass(X,[index]*3,np.eye(3))[0]),displacement=float(np.linalg.norm(X[index]-base[index])))
            if closed:
                ss,uu,qq,mm=classify_reference(X);s=score(qq);rec.update(s);value=max(s['Q'],default=0);target=folder/f'vertex{index:03d}';target.mkdir();np.savez(target/'body.npz',X=X,Q=qq,added_points=X[-1:]);recipe=dict(parent_audit=str((parent/'audit.json').resolve()),parent_audit_sha256=hashlib.sha256((parent/'audit.json').read_bytes()).hexdigest(),parent_frame='raw',parent_translation='None; all unchanged exact raw parent vertices are retained',replace_vertices=[dict(index=int(to_exact[index]),point=[str(x) for x in X[index]+p['centroid']])],added_points=[[str(x) for x in X[-1]+p['centroid']]],scope='New literal rational convex hull: exact parent with one vertex replaced and one point added. The full own-centroid exact audit remains mandatory.');(target/'construction.json').write_text(json.dumps(recipe,indent=2));(target/'summary-numerical.json').write_text(json.dumps(rec,indent=2));rec['folder']=str(target.resolve())
                if s['S']==s['U']==1 and 17<=s['E']<249:
                    (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(construction=str((target/'construction.json').resolve())),indent=2));return
                if s['S']==2 and s['U']==1 and value<best:
                    best=value;(out/'best-strict211.json').write_text(json.dumps(rec,indent=2));print('TRIANGULAR_COMPENSATION_BEST',json.dumps(rec),flush=True)
            results.append(rec);(folder/'trials.json').write_text(json.dumps(results,indent=2))
        row=dict(case=case,source=str(source.resolve()),eligible_vertices=eligible,successful=sum(r['closed'] for r in results),best_Q=best,seconds=time.time()-start);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('TRIANGULAR_COMPENSATION_CASE',json.dumps(row),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--scout',required=True);ap.add_argument('--out',required=True);ap.add_argument('--cases',type=int,default=25);a=ap.parse_args();run(a.scout,a.out,a.cases)
