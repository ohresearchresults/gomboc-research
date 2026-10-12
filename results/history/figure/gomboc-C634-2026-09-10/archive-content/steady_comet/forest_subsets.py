"""Root-closed original-vertex subsets, retaining the entire stable 21-gon.
All sets of <=91 vertices satisfy E<=249, independently of new facet incidence.
The fixed old-centroid unstable certificate is only a necessary screen: each
candidate is integrated anew at its own FILLED centroid before scoring.
Floating discovery only; exact plane reconstruction/audits are mandatory later.
"""
from pathlib import Path
from fractions import Fraction as F
import json,time,sys,numpy as np
sys.set_int_max_str_digits(0)
from scipy.spatial import ConvexHull
R=Path(__file__).parent;A=json.loads((R/'parent650/C650/A.json').read_text());extra=json.loads((R/'parent650/C650/EXTRA.json').read_text());P0=np.array([[float(F(z)) for z in p] for p in A['raw_vertices']]);cent0=np.array(list(map(lambda z:float(F(z)),A['raw_centroid'])));pa=extra['primal_parent'];root=101;stable=set(A['faces'][3]);owner=[set() for _ in P0]
for i,cy in enumerate(A['faces']):
 for v in cy:owner[v].add(i)
H0=json.loads((R/'parent650/C650/RAW.json').read_text())['H'];Q0=np.array([[float(F(v,h[3])) for v in h[:3]] for h in H0]);core=stable|{root}
def close(S):
 S=set(S)
 while True:
  q={pa[v] for v in S if pa[v]>=0}-S
  if not q:return S
  S|=q
core=close(core);paths=[close({i}) for i in range(len(P0))];print('CORE',len(core),sorted(core),flush=True)

def audit(ids,details=False):
 ids=sorted(ids);P=P0[ids];origin=P.mean(0);P=P-origin;hull=ConvexHull(P);groups={}
 for tri,eq in zip(hull.simplices,hull.equations):
  common=set.intersection(*(owner[ids[v]] for v in tri));key=('old',min(common)) if common else ('new',*tuple(sorted(map(int,tri))))
  if key not in groups:groups[key]=dict(vertices=set(),tris=[],n=eq[:3],h=-eq[3])
  groups[key]['vertices'].update(map(int,tri));groups[key]['tris'].append(tuple(map(int,tri)))
 faces=[];q=[];original=[];V=0.;M=np.zeros(3)
 for key,data in groups.items():
  n=data['n'];hh=data['h'];vs=sorted(data['vertices']);p=P[vs];cc=p.mean(0);axis=p[0]-cc;axis/=np.linalg.norm(axis);other=np.cross(n,axis);ang=np.arctan2((p-cc)@other,(p-cc)@axis);cy=[vs[j] for j in np.argsort(ang)];faces.append(cy);q.append(n/hh);original.append(key[1] if key[0]=='old' else -1)
  aa=P[cy[0]]
  for k in range(1,len(cy)-1):
   bb=P[cy[k]];cc=P[cy[k+1]];dv=aa@np.cross(bb,cc)/6;V+=dv;M+=dv*(aa+bb+cc)/4
 q=np.array(q);c=M/V;X=P-c;n=q/(1-q@c)[:,None];ef={}
 for i,cy in enumerate(faces):
  for a,b in zip(cy,cy[1:]+cy[:1]):ef.setdefault(tuple(sorted((a,b))),[]).append(i)
 if any(len(f)!=2 for f in ef.values()) or len(ids)-len(ef)+len(faces)!=2:raise ValueError('floating hull coplanarity grouping incomplete')
 ss=np.sum(n*n,axis=1)[None,:]-n@n.T # column j is ||n_j||^2 - n_i.n_j
 scos=np.einsum('ik,ijk->ij',n,n[None,:,:]-n[:,None,:])/(np.linalg.norm(n,axis=1)[:,None]*np.maximum(np.linalg.norm(n[None,:,:]-n[:,None,:],axis=2),1e-100));np.fill_diagonal(scos,-np.inf)
 ucos=np.einsum('ik,ijk->ij',X,X[None,:,:]-X[:,None,:])/(np.linalg.norm(X,axis=1)[:,None]*np.maximum(np.linalg.norm(X[None,:,:]-X[:,None,:],axis=2),1e-100));np.fill_diagonal(ucos,-np.inf)
 S=np.where(scos.max(1)<-1e-10)[0];U=np.where(ucos.max(1)<-1e-10)[0];HH=[]
 for (a,b),(i,j) in ef.items():
  d=X[b]-X[a];w=-X[a]@d;z=X[b]@d
  if min(w,z,n[i]@(n[i]-n[j]),n[j]@(n[j]-n[i]))>1e-12:HH.append([a,b])
 sr=original.index(3);ur=ids.index(root);esc=np.r_[np.delete(scos.max(1),sr),np.delete(ucos.max(1),ur)];bad=(esc<0).sum();score=np.maximum(0,-esc).sum()
 out=dict(V=len(ids),E=len(ef),F=len(faces),counts=[len(S),len(U),len(HH)],S=S.tolist(),Uoriginal=[ids[j] for j in U],stable_original=[original[j] for j in S],volume=float(V),centroid=(origin+c).tolist(),centre_shift=float(np.linalg.norm(origin+c-cent0)),bad=int(bad),score=float(score),minimum=float(esc.min()),stable_face_size=len(faces[sr]),ids=ids)
 if details:out.update(faces=faces,original_faces=original,q=q.tolist(),origin=origin.tolist(),P=P.tolist())
 return out

def run(samples=3000,seed=7189,N=91):
 rng=np.random.default_rng(seed);out=R/'forest_subset_records';out.mkdir(exist_ok=True);best=None;ledger=[];t0=time.time()
 for it in range(samples):
  S=core.copy();weights=rng.exponential(1,len(P0));bias=rng.normal(size=3);bias/=np.linalg.norm(bias);weights*=np.exp((P0-cent0)@bias*rng.uniform(0,5))
  if it%3==0:
   vv=int(np.argmin(P0[:,0]));S|=paths[vv]
  if it%3==1:
   vv=int(np.argmax((P0-cent0)@bias));S|=paths[vv]
  if len(S)>N:continue
  while len(S)<N:
   possible=[i for i in range(len(P0)) if i not in S and len(S|paths[i])<=N]
   if not possible:break
   d=np.min(np.linalg.norm(P0[:,None,:]-P0[sorted(S)][None,:,:],axis=2),axis=1)
   scores=[weights[i]*d[i]**rng.uniform(.5,2)/len(paths[i]-S)**rng.uniform(.0,.8) for i in possible];v=possible[int(np.argmax(scores))];S|=paths[v]
  try:rr=audit(S)
  except Exception as e:
   if it<10:print('FOREST_ERROR',it,repr(e),flush=True)
   continue
  assert rr['V']<=91 and rr['E']<=249
  key=(sum(rr['counts'][:2]),rr['score'])
  if best is None or key<best:
   best=key;full=audit(S,True);tag=f'FOREST_{it}_V{rr["V"]}_E{rr["E"]}_S{rr["counts"][0]}_U{rr["counts"][1]}';(out/(tag+'.json')).write_text(json.dumps(full,sort_keys=True,separators=(',',':')));(out/'BEST.json').write_text(json.dumps(full,sort_keys=True,separators=(',',':')));ledger.append(dict(iteration=it,**rr));(out/'LEDGER.json').write_text(json.dumps(ledger,indent=2));print('FOREST_BEST',it,{k:v for k,v in rr.items() if k!='ids'},'sec',round(time.time()-t0,2),flush=True)
  if rr['counts']==[1,1,0]:print('FOREST_NUMERIC_WINNER',flush=True);return
  if it%100==0:print('FOREST_ITER',it,'sec',round(time.time()-t0,2),flush=True)
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--samples',type=int,default=3000);p.add_argument('--N',type=int,default=91);a=p.parse_args();run(samples=a.samples,N=a.N)
