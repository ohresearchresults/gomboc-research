"""Physical one-support coarsening of exact conditioned own110 benchmarks."""
import sys,json,numpy as np
from collections import defaultdict
from gmpy2 import mpq
from geometry import hull_from_supports,mass,angular_scores
from support_persistence import ROOT,barcode
sys.set_int_max_str_digits(0)
for name in ['CONDITIONED_C624','CONDITIONED_C626']:
 r=json.loads((ROOT/'artifacts'/name/'B_exact.json').read_text());c=np.array([float(mpq(v)) for v in r['raw_centroid']]);Y=np.array([[float(mpq(n,h)) for n in ns] for ns,h in zip(r['normals'],r['offsets'])]);Y=Y/(1-Y@c)[:,None];rows=[];out=ROOT/'artifacts/conditioned_deletions'/name;out.mkdir(exist_ok=True,parents=True)
 for removed in range(len(Y)):
  if removed in r['stable_face_ids']:continue
  YY=np.delete(Y,removed,axis=0);X,H,faces,tr,E,active=hull_from_supports(YY,tol=1e-9);v,c2=mass(X,tr);Z=X-c2;Q=H/(1-H@c2)[:,None];edge={}
  for f,vs in enumerate(faces):
   for i,j in zip(vs,vs[1:]+vs[:1]):edge.setdefault(tuple(sorted((i,j))),[]).append(f)
  eu=np.array(list(edge));es=np.array(list(edge.values()));s=angular_scores(Q).max(1);u=angular_scores(Z).max(1);depths=[]
  for A,ee in [(Z,eu),(Q,es)]:
   p,w,bb=barcode(A,np.ones(len(A)),ee);birth=np.sum(A[p[:,0]]**2,axis=1);depth=bb/birth;depths.append(depth)
  row=dict(removed=removed,V=len(X),E=E,F=len(H),S=int((s<0).sum()),U=int((u<0).sum()),Qmax=float(depths[1].max()),Pmax=float(depths[0].max()),loss=float(sum(np.sum(d*d) for d in depths)),centroid=c2.tolist(),volume=v);rows.append(row)
 rows.sort(key=lambda a:(a['loss'],a['E']));(out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n');print('CONDITIONED_DELETIONS',name,rows[:5],flush=True)
