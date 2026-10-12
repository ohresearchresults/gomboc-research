"""New true material points near the current P interface; no integration relabeling.
All new hulls receive actual mass evaluation and unconstrained vertex continuation.
"""
import sys,json,numpy as np,hashlib
from pathlib import Path
from gmpy2 import mpq
from free_vertex_continuation import ROOT,run
from support_persistence import barcode
src=ROOT/'artifacts/canonical_atlas/VC47D_free39/exact_strict121_g14/audit.json';r=json.loads(src.read_text());c=np.array([float(mpq(v)) for v in r['raw_centroid']]);X=np.array([[float(mpq(v)) for v in p] for p in r['raw_vertices']])-c;edges=np.array(r['edges']);bp,bw,bb=barcode(X,np.ones(len(X)),edges);edge=bp[np.argmax(bb),1:];a,b=X[edge];e=b-a;t=np.clip(-a@e/(e@e),0,1);death=np.linalg.norm(a+t*e)**2;mean=(X[edges[:,0]]+X[edges[:,1]])/2;rr=np.sum(mean*mean,axis=1);angle=1-np.sum(X[edges[:,0]]*X[edges[:,1]],axis=1)/(np.linalg.norm(X[edges[:,0]],axis=1)*np.linalg.norm(X[edges[:,1]],axis=1));weights=angle/(.02+abs(rr-death));order=np.argsort(-weights)
base=ROOT/'artifacts/vc47d_refine39';base.mkdir(exist_ok=False)
for N,offset in [(64,1e-4),(84,1e-4),(84,.015)]:
 n=N-len(X);chosen=order[:n];P=np.vstack([X,mean[chosen]*(1+offset)]);name=f'n{N}_offset{offset}';f=base/(name+'.npy');np.save(f,P);(base/(name+'.json')).write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),principal_death=death,chosen_edges=edges[chosen].tolist(),outward_radial_factor=1+offset,nomination_only=True),indent=2)+'\n');run(f,base/name,927064+N,0.,3500)
