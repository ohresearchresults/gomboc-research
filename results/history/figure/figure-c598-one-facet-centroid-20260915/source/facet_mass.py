"""Finite one-facet centroid continuation of the exact journaled C598 body.
Numerical discovery only. All unchanged supports are the literal exact C598 input.
"""
import sys,json,hashlib,platform
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import scipy
from scipy.spatial import HalfspaceIntersection,ConvexHull,QhullError
from scipy.optimize import least_squares
sys.set_int_max_str_digits(0)
ROOT=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent

def load():
 a=json.loads((ROOT/'C598_A.json').read_text());parent=json.loads((ROOT/'C602_A.json').read_text())
 N=np.array([[float(F(z,d)) for z in row] for row,d in zip(a['normals'],a['offsets'])]);norm=np.linalg.norm(N,axis=1);h=1/norm;N/=norm[:,None]
 g0=np.array([float(F(z)) for z in parent['raw_centroid']]);g=np.array([float(F(z)) for z in a['raw_centroid']]);f=114;n=N[f].copy();t=np.eye(3)[np.argmin(np.abs(n))];t-=n*t.dot(n);t/=np.linalg.norm(t);u=np.cross(n,t)
 return a,N,h,g0,g,f,t,u

a,N,h,g0,g,f,t,u=load()

def evaluate(p,details=False):
 nn=N.copy();hh=h.copy();nn[f]+=p[1]*t+p[2]*u;hh[f]+=p[0]
 if hh[f]<=0:raise ValueError('origin not interior')
 X=HalfspaceIntersection(np.column_stack((nn,-hh)),np.zeros(3)).intersections
 # Canonical enough for numerical discovery; exact auditing is separate.
 X=np.unique(np.round(X,12),axis=0);hull=ConvexHull(X);X0=X[hull.simplices];base=np.mean(X[hull.vertices],axis=0)
 T=X0-base;v=np.abs(np.einsum('ij,ij->i',T[:,0],np.cross(T[:,1],T[:,2])))/6
 V=v.sum();c=(v[:,None]*(X0.sum(axis=1)+base)/4).sum(axis=0)/V
 if not details:return c
 active=[];faces=[];edges=set();stable=[];unstable=[];saddles=[]
 for fi,(n,d) in enumerate(zip(nn,hh)):
  ids=np.flatnonzero(np.abs(X@n-d)<2e-8*np.linalg.norm(n))
  if len(ids)<3:continue
  v1=X[ids]-np.mean(X[ids],axis=0);e=np.eye(3)[np.argmin(np.abs(n))];e-=n*e.dot(n)/n.dot(n);e/=np.linalg.norm(e);e2=np.cross(n,e);e2/=np.linalg.norm(e2)
  if np.linalg.matrix_rank(v1,tol=2e-8)<2:continue
  ch=ConvexHull(np.column_stack((v1@e,v1@e2))).vertices;cy=ids[ch];faces.append((fi,cy));active.append(fi)
  vals=[]
  for i,j in zip(cy,np.roll(cy,-1)):
   edges.add(tuple(sorted((int(i),int(j)))));vals.append(n@np.cross(X[i]-c,X[j]-X[i]))
  if min(vals)>1e-10:stable.append(fi)
 for i in hull.vertices:
  ds=(X-X[i])@(X[i]-c);ds[i]=-np.inf
  if np.max(ds)<-1e-10:unstable.append(int(i))
 # Count only S and U; H=S+U-2 here is a diagnostic, not a complete census.
 return dict(centre=c.tolist(),volume=float(V),V=len(hull.vertices),E=len(edges),F=len(faces),S=stable,U=unstable,C=2*len(edges),param=list(map(float,p)),plane=list(map(float,np.r_[nn[f],hh[f]])),hull_volume=float(hull.volume))

def run():
 report={'status':'NUMERICAL_DISCOVERY_NOT_EXACT','warning':'The rounded-vertex face-graph routine overcounts true edges even at the exact starting body. V/E/F/S/U are provisional diagnostics only; see exact checkpoint A/B audits. The moment continuation, not these counts, is used for the theorem.','input_sha256':hashlib.sha256((ROOT/'C598_raw.json').read_bytes()).hexdigest(),'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'fixed_facet':f,'basis':[t.tolist(),u.tolist()],'target':g0.tolist(),'start':g.tolist(),'bounds':[[-h[f]+1e-5,-6,-6],[4,6,6]],'steps':[]}
 p=np.zeros(3)
 for lam in np.linspace(0,1,21):
  target=(1-lam)*g+lam*g0
  def fun(p):return evaluate(p)-target
  r=least_squares(fun,p,bounds=report['bounds'],xtol=1e-12,ftol=1e-12,gtol=1e-12,max_nfev=300,diff_step=1e-5)
  p=r.x;d=evaluate(p,True);d.update(lam=float(lam),target=target.tolist(),residual=float(np.linalg.norm(r.fun)),success=bool(r.success),nfev=r.nfev,message=r.message)
  report['steps'].append(d);print(json.dumps(d),flush=True)
 (ROOT/'FACET_MASS_NUMERICAL.json').write_text(json.dumps(report,sort_keys=True,separators=(',',':')))
if __name__=='__main__':run()
