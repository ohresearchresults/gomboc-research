"""Selected original rational benchmark vertices; finite reference-center guide.
No selected-point or reference-root nomination is an own-centroid certificate.
Numerical coplanar grouping is used only for screening; exact audit is mandatory.
"""
import sys,json,time
import numpy as np
from scipy.spatial import ConvexHull
from support_persistence import ROOT,barcode
from geometry import angular_scores,mass
X=np.load(ROOT/'artifacts/closed_subset/X_centered.npy');meta=json.loads((ROOT/'artifacts/closed_subset/minimum_closure.json').read_text());root=meta['root'];allowed=angular_scores(X)>1e-11

def evaluate(ids):
 P=X[ids];h=ConvexHull(P);tri=h.simplices.copy();n=np.cross(P[tri[:,1]]-P[tri[:,0]],P[tri[:,2]]-P[tri[:,0]]);flip=np.einsum('ij,ij->i',n,h.equations[:,:3])<0;tri[flip]=tri[flip][:,[0,2,1]];vol,c=mass(P,tri);Yraw=h.equations[:,:3]/(-h.equations[:,3,None]);keep=[]
 for y in Yraw:
  if not keep or min(np.linalg.norm(np.asarray(keep)-y,axis=1))>1e-7:keep.append(y)
 Y=np.asarray(keep);E=len(P)+len(Y)-2;ph=ConvexHull(Y);edges=set()
 for f in ph.simplices:
  for i,j in zip(f,np.roll(f,-1)):edges.add(tuple(sorted((int(i),int(j)))))
 bp,w,bars=barcode(Y,np.ones(len(Y)),np.array(list(edges)));a=Y[bp[:,1]];d=Y[bp[:,2]]-a;tt=np.clip(-np.sum(a*d,axis=1)/np.sum(d*d,axis=1),0,1);birth=np.sum(Y[bp[:,0]]**2,axis=1);rel=np.maximum(birth-np.sum((a+tt[:,None]*d)**2,axis=1),0)*w/birth
 sr=angular_scores(Y).max(1);ur=angular_scores(P).max(1);Z=P-c;Q=Y/(1-Y@c)[:,None];s=angular_scores(Q).max(1);u=angular_scores(Z).max(1)
 return dict(selected=list(map(int,ids)),V=len(P),E=E,F=len(Y),C=2*E,refS=int((sr<0).sum()),refU=int((ur<0).sum()),refQ2=float(np.sum(rel**2)),refQmax=float(rel.max()),S=int((s<0).sum()),U=int((u<0).sum()),volume=float(vol),centroid=c.tolist(),centroid_norm=float(np.linalg.norm(c)))

def close(ids,j):
 selected=set(ids)|{j}
 # Reachability from the retained set through positive outward edges; add a
 # shortest finite witness chain if the nominated point does not reach it yet.
 dist=np.full(len(X),np.inf);dist[list(selected-{j})]=0;parent=np.full(len(X),-1);used=np.zeros(len(X),bool)
 for _ in range(len(X)):
  k=int(np.argmin(np.where(~used,dist,np.inf)))
  if not np.isfinite(dist[k]):break
  used[k]=True
  for i in np.flatnonzero(allowed[:,k]&(~used)):
   if dist[k]+1<dist[i]:dist[i]=dist[k]+1;parent[i]=k
  if k==j:break
 if not np.isfinite(dist[j]):return None
 while j not in ids:
  selected.add(int(j));j=int(parent[j])
  if j<0:raise ValueError('missing witness')
 return sorted(selected)

if __name__=='__main__':
 out=ROOT/'artifacts/grow_closed_subset';out.mkdir(exist_ok=True);ids=meta['selected'];history=[];seen=set();start=time.time()
 for it in range(40):
  cur=evaluate(ids);history.append(cur);print('GROW',it,{k:v for k,v in cur.items() if k!='selected'},flush=True);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n');np.save(out/f'iteration{it}_points.npy',X[ids]);(out/f'iteration{it}.json').write_text(json.dumps(cur,indent=2)+'\n')
  candidates=[]
  for j in range(len(X)):
   if j in ids:continue
   trial=close(ids,j)
   if trial is None or tuple(trial) in seen:continue
   seen.add(tuple(trial));r=evaluate(trial)
   if r['E']>249:continue
   if r['S']==r['U']==1:(out/f'OWN_NUMERICAL_NOMINATION_{it}_{j}.json').write_text(json.dumps(r,indent=2)+'\n')
   candidates.append(r)
  (out/f'candidates{it}.json').write_text(json.dumps(candidates,indent=2)+'\n')
  if not candidates:break
  # Scientific guide: remove reference finite stable basins, then mass mismatch.
  candidates.sort(key=lambda r:(r['refQ2'],r['centroid_norm'],r['E']));best=candidates[0]
  if best['refQ2']>=cur['refQ2'] and best['centroid_norm']>=cur['centroid_norm']:break
  ids=best['selected']
 print('GROW_DONE',len(seen),time.time()-start,flush=True)
