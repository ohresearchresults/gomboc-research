"""Finite physical cuts from current polar positive-chord balls.
A reference positive chord is a nomination filter only; every trial recomputes
actual uniform mass and full P/Q. Convex combination of supports is never a cut.
"""
import sys,json,numpy as np,hashlib,time
from pathlib import Path
from io import BytesIO
from geometry import hull_from_supports,mass,angular_scores
from canonical_atlas import ROOT,Chart
from support_persistence import barcode
folder=ROOT/sys.argv[1];inputfile=folder/sys.argv[2];out=folder/sys.argv[3];out.mkdir(exist_ok=False);raw=inputfile.read_bytes();(out/'source_q.npy').write_bytes(raw);c=Chart(folder);g=c.graph(np.load(BytesIO(raw)));Y=g['Q'];X=g['Z'];up,uw,ub=barcode(X,np.ones(len(X)),c.eu);root=int(up[np.argmax(ub),0]);dirs=[];Z=X[root]/np.linalg.norm(X[root]);dirs.append(Z)
# Perturb around each actual unstable root and the current persistence saddle foot.
for i in np.flatnonzero(angular_scores(X).max(1)<0):dirs.append(X[i]/np.linalg.norm(X[i]))
for edge in up[np.argsort(-ub)[:2],1:]:
 a,b=X[edge];d=b-a;t=np.clip(-a@d/(d@d),0,1);p=a+t*d;dirs.append(p/np.linalg.norm(p))
rng=np.random.default_rng(912449)
for scale in [.1,.3,.7]:
 for _ in range(8):d=Z+scale*rng.normal(size=3);dirs.append(d/np.linalg.norm(d))
rows=[];start=time.time();best=1e99
for f,y in enumerate(Y):
 for di,d in enumerate(dirs):
  q=(y+np.linalg.norm(y)*(1-2e-5)*d)/2
  if np.max(X@q)<=1+1e-10:continue
  # The first value is the first cut event along q itself. Increasing it stays
  # inside the one-parent diameter ball only while its explicit guard is positive.
  radial=1/np.max(X@q)
  for frac in [.03,.1,.3,.6,1.]:
   z=q*(radial+frac*(1-radial));guard=float(z@(y-z)/(np.linalg.norm(z)*np.linalg.norm(y-z)))
   if guard<=1e-7:continue
   try:
    XX,H,faces,tr,E,active=hull_from_supports(np.vstack([Y,z]),tol=1e-10);v,cent=mass(XX,tr);A=XX-cent;B=H/(1-H@cent)[:,None];ss=angular_scores(B).max(1);uu=angular_scores(A).max(1);ef={}
    for fi,face in enumerate(faces):
     for i,j in zip(face,face[1:]+face[:1]):ef.setdefault(tuple(sorted((i,j))),[]).append(fi)
    assert all(len(v)==2 for v in ef.values());eu=np.array(list(ef));es=np.array(list(ef.values()));dd=[]
    for AA,ee in [(A,eu),(B,es)]:
     pp,ww,bb=barcode(AA,np.ones(len(AA)),ee);dd.append(bb/np.sum(AA[pp[:,0]]**2,axis=1))
    row=dict(parent=f,direction=di,fraction=frac,normal=z.tolist(),reference_guard=guard,V=len(A),E=E,F=len(B),S=int((ss<0).sum()),U=int((uu<0).sum()),Pmax=float(dd[0].max()),Qmax=float(dd[1].max()),loss=float(sum(np.sum(x*x) for x in dd)),centroid=cent.tolist());rows.append(row)
    if row['loss']<best:best=row['loss'];print('CUT_BEST',row,flush=True)
   except (ValueError,AssertionError,np.linalg.LinAlgError):continue
 rows.sort(key=lambda a:(a['loss'],a['S']+a['U']));(out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n')
(out/'provenance.json').write_text(json.dumps(dict(source=str(inputfile),source_sha256=hashlib.sha256(raw).hexdigest(),canonical_chart=str(folder/'chart.json'),rng_seed=912449),indent=2)+'\n');print('CUT_DONE',len(rows),'seconds',time.time()-start,flush=True)
