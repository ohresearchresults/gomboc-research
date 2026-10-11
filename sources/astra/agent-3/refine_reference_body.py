"""Add physical facet controls while retaining numerical reference110 at zero.
No centroid translation is performed: the current reference is kept fixed.
The actual homogeneous centroid is reported and remains a separate constraint.
"""
import argparse,json
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from vertex_geometry import geometry
from support_geometry import escape

def ref_geometry(X):
 g=geometry(X,False);h=ConvexHull(X);H=-h.equations[:,:3]/h.equations[:,3,None];return g,H,h.simplices
def run(source,out,target,seed):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);X=X[ConvexHull(X).vertices];rng=np.random.default_rng(seed);hist=[];np.save(out/'initial.npy',X)
 for step in range(target-len(X)):
  g,H,T=ref_geometry(X);vh=escape(H)[0];S=np.flatnonzero(vh<0);U=np.flatnonzero(escape(X)[0]<0);assert len(S)==len(U)==1;area=np.linalg.norm(np.cross(X[T[:,1]]-X[T[:,0]],X[T[:,2]]-X[T[:,0]]),axis=1);order=np.argsort(-area*rng.uniform(.5,1.5,len(area)));ok=False
  for f in order:
   if f in S:continue
   bary=rng.dirichlet([2,2,2]);base=bary@X[T[f]];n=H[f]/np.linalg.norm(H[f]);scale=np.linalg.norm(base)
   for eps in [1e-5,1e-6,1e-7,1e-8,1e-9]:
    p=base+eps*scale*n;Y=np.vstack((X,p));gg,HH,TT=ref_geometry(Y);ss=int(np.sum(escape(HH)[0]<0));uu=int(np.sum(escape(Y)[0]<0))
    if ss==uu==1 and len(gg['vertices'])==len(Y):X=Y;ok=True;hist.append(dict(step=step,face=T[f].tolist(),barycentric=bary.tolist(),relative_height=eps));break
   if ok:break
  if not ok:raise ValueError('no strict reference110 preserving facet addition found')
 np.save(out/'vertices.npy',X);(out/'construction.json').write_text(json.dumps(dict(source=source,seed=seed,target=target,additions=hist,actual_centroid=geometry(X,False)['g'].tolist(),reference='zero; NOT declared own centroid'),indent=2));print('REFERENCE_REFINEMENT',len(X),'actual_centroid',geometry(X,False)['g'],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--target',type=int,default=70);p.add_argument('--seed',type=int,default=7732);a=p.parse_args();run(a.input,a.out,a.target,a.seed)
