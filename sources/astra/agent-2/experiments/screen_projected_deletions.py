"""Numerical literal support-removal screen; records full actual-mass bar census.
No source geometry changed and no numerical result constitutes acceptance.
"""
import sys,json,numpy as np,hashlib
from pathlib import Path
from canonical_atlas import ROOT,Chart
from geometry import hull_from_supports,mass,angular_scores
from support_persistence import barcode
from io import BytesIO
folder=ROOT/sys.argv[1];source=folder/sys.argv[2];out=folder/sys.argv[3];out.mkdir(parents=True,exist_ok=False)
b=source.read_bytes();(out/'source_q.npy').write_bytes(b);c=Chart(folder);q=np.load(BytesIO(b));g=c.graph(q);Y=g['Q'];rows=[]
for removed in range(c.F):
 if angular_scores(Y).max(1)[removed]<0:continue
 try:
  X,H,faces,tr,E,active=hull_from_supports(np.delete(Y,removed,axis=0),tol=1e-10);vol,cent=mass(X,tr);Z=X-cent;Q=H/(1-H@cent)[:,None];edge={}
  for f,vs in enumerate(faces):
   for i,j in zip(vs,vs[1:]+vs[:1]):edge.setdefault(tuple(sorted((i,j))),[]).append(f)
  assert all(len(v)==2 for v in edge.values());eu=np.array(list(edge));es=np.array(list(edge.values()));a=angular_scores(Z).max(1);d=angular_scores(Q).max(1);loss=[];counts=[]
  for A,ee in [(Z,eu),(Q,es)]:
   p,w,bb=barcode(A,np.ones(len(A)),ee);depth=bb/np.sum(A[p[:,0]]**2,axis=1);loss.append(float(np.sum(depth*depth)));counts.append(float(depth.max()))
  row=dict(removed=removed,V=len(X),E=E,F=len(H),S=int((d<0).sum()),U=int((a<0).sum()),Pmax=counts[0],Qmax=counts[1],loss=sum(loss),centroid=cent.tolist(),min_nonroot=min(np.sort(a)[1],np.sort(d)[1]));rows.append(row)
  if row['S']==row['U']==1:print('NUMERICAL_DELETION110',row,flush=True)
 except Exception as e:rows.append(dict(removed=removed,error=str(e)))
rows.sort(key=lambda a:(a.get('loss',1e100),a.get('E',10000)));(out/'screen.json').write_text(json.dumps(dict(source=str(source),sha256=hashlib.sha256(b).hexdigest(),rows=rows),indent=2)+'\n');print('BEST',rows[:8],flush=True)
