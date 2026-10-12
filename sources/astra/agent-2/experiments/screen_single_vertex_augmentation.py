"""Finite physical hull augmentation around the remaining stable basin.
Qhull/coplanarity are numerical nominations; exact rational re-hulling is required.
"""
import sys,json,time,hashlib,numpy as np
from pathlib import Path
from scipy.spatial import ConvexHull,QhullError
from gmpy2 import mpq
from geometry import mass,angular_scores
from support_persistence import ROOT,barcode
sys.set_int_max_str_digits(0)
def census(P):
 h=ConvexHull(P);tr=h.simplices.copy();n=np.cross(P[tr[:,1]]-P[tr[:,0]],P[tr[:,2]]-P[tr[:,0]]);rev=np.einsum('ij,ij->i',n,h.equations[:,:3])<0;tr[rev]=tr[rev][:,[0,2,1]];volume,c=mass(P,tr);Yraw=h.equations[:,:3]/(-h.equations[:,3,None]);Y=[];members=[]
 for i,y in enumerate(Yraw):
  d=np.linalg.norm(np.asarray(Y)-y,axis=1) if Y else np.array([])
  if len(d) and d.min()<1e-9*max(1,np.linalg.norm(y)):members[d.argmin()].update(map(int,tr[i]))
  else:Y.append(y);members.append(set(map(int,tr[i])))
 Y=np.array(Y);faces=[];edge={}
 for fi,vs in enumerate(members):
  ids=np.array(sorted(vs));n=Y[fi]/np.linalg.norm(Y[fi]);a=np.cross(n,np.eye(3)[np.argmin(abs(n))]);a/=np.linalg.norm(a);b=np.cross(n,a);v=ids[ConvexHull(P[ids]@np.array([a,b]).T).vertices].tolist();faces.append(v)
  for i,j in zip(v,v[1:]+v[:1]):edge.setdefault(tuple(sorted((i,j))),[]).append(fi)
 vv=sorted(set(v for f in faces for v in f));remap={v:i for i,v in enumerate(vv)};eu=np.array([[remap[i],remap[j]] for i,j in edge]);es=np.array(list(edge.values()));assert all(len(x)==2 for x in edge.values());assert len(vv)-len(edge)+len(faces)==2
 Z=P[vv]-c;Q=Y/(1-Y@c)[:,None];ss=angular_scores(Q).max(1);uu=angular_scores(Z).max(1);depth=[]
 for A,ee in [(Z,eu),(Q,es)]:
  bp,bw,bb=barcode(A,np.ones(len(A)),ee);depth.append(bb/np.sum(A[bp[:,0]]**2,axis=1))
 return dict(V=len(vv),E=len(edge),F=len(faces),S=int((ss<0).sum()),U=int((uu<0).sum()),Pmax=float(depth[0].max()),Qmax=float(depth[1].max()),loss=float(sum(np.sum(x*x) for x in depth)),volume=float(volume),centroid=c.tolist())
if __name__=='__main__':
 src=ROOT/'artifacts/projected_contact_retire/delete_4_35_94_99/audit.json';r=json.loads(src.read_text());X=np.array([[float(mpq(v)) for v in row] for row in r['raw_vertices']]);c=np.array([float(mpq(x)) for x in r['raw_centroid']]);X-=c;Y=np.array([[float(mpq(x,mpq(h))) for x in row] for row,h in zip(r['normals'],r['offsets'])]);Y=Y/(1-Y@c)[:,None];s=r['stable_face_ids'];f=min(s,key=lambda i:np.linalg.norm(Y[i]));foot=Y[f]/(Y[f]@Y[f]);normal=Y[f]/np.linalg.norm(Y[f]);radius=np.linalg.norm(foot);directions=[normal]
 for k in s:
  for t in np.linspace(0,1,13):
   z=(1-t)*normal+t*Y[k]/np.linalg.norm(Y[k]);directions.append(z/np.linalg.norm(z))
 rng=np.random.default_rng(321989);directions.extend([d/np.linalg.norm(d) for d in rng.normal(size=(300,3))]);points=[]
 for d in directions:
  rad=1/np.max(Y@d)
  for e in np.geomspace(1e-7,.5,16):points.append(rad*(1+e)*d)
 for v in r['faces'][f]:
  for t in np.linspace(-.5,1.5,21):
   for e in np.geomspace(1e-7,.25,16):points.append(foot+t*(X[v]-foot)+e*radius*normal)
 out=ROOT/'artifacts/single_vertex_augmentation_C490';out.mkdir(exist_ok=False,parents=True);(out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),seed=321989,main_stable_facet=f),indent=2));rows=[];best=np.inf;beg=time.time()
 for i,p in enumerate(points):
  if np.max(Y@p)<=1+1e-10:continue
  try:row=census(np.vstack([X,p]))
  except (QhullError,ValueError,AssertionError):continue
  if row['E']>248:continue
  row.update(point=p.tolist(),index=i);rows.append(row)
  if row['loss']<best:
   best=row['loss'];(out/'best.json').write_text(json.dumps(row,indent=2)+'\n');print('AUGMENT_BEST',i,row,'seconds',time.time()-beg,flush=True)
  if row['S']==row['U']==1:
   (out/f'NUMERICAL_NOMINATION_{i}.json').write_text(json.dumps(row,indent=2)+'\n');print('REQUIRES_EXACT',row,flush=True)
  if i%100==0:(out/'screen.json').write_text(json.dumps(sorted(rows,key=lambda x:x['loss']),indent=2)+'\n')
 (out/'screen.json').write_text(json.dumps(sorted(rows,key=lambda x:x['loss']),indent=2)+'\n');print('DONE',len(points),len(rows),'seconds',time.time()-beg,flush=True)
