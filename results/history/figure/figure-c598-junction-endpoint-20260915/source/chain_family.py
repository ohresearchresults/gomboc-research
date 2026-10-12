"""Numerical exact-grid primal-chain family; exact maximal-facet audits are separate.
Python3.13.5/NumPy2.3.5/SciPy1.17.0. No random input.
"""
import sys,json,hashlib
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
from scipy.spatial import ConvexHull
sys.set_int_max_str_digits(0)
def unique(rows,tol=1e-8):
 out=[]
 for p in rows:
  if not any(np.linalg.norm(p-x)<tol for x in out):out.append(p)
 return np.array(out)
def roots(X):
 y=X@X.T-(X*X).sum(axis=1)[:,None];np.fill_diagonal(y,-np.inf);return np.flatnonzero(y.max(axis=1)<0).tolist()
def main():
 parent,out=map(Path,sys.argv[1:]);a=json.loads(parent.read_text());out.mkdir(parents=True,exist_ok=True);raw=np.array([[float(Q(t)) for t in row] for row in a['raw_vertices']]);c=np.array([float(Q(t)) for t in a['raw_centroid']]);P=raw-c;u=P[7];D=10**12;results=[]
 for target,n0 in [(85,5),(91,6)]:
  z=P[target];r=np.linalg.norm(u);R=np.linalg.norm(z)/r;e=u/r;gam=np.dot(u,z)/r/np.linalg.norm(z);phi=np.arccos(gam);f=(z/np.linalg.norm(z)-gam*e)/np.sqrt(1-gam**2)
  for n in range(n0,n0+6):
   lam=R**(1/n);new=np.array([r*lam**k*(np.cos(k*phi/n)*e+np.sin(k*phi/n)*f) for k in range(1,n)]);ints=np.rint((new+c)*D).astype(np.int64);X=np.r_[raw,ints/D];h=ConvexHull(X);eq=unique(h.equations);U=roots(X[h.vertices]-c);polar=eq[:,:3]/(-eq[:,3]-eq[:,:3]@c)[:,None];S=roots(polar);ref=[len(S),len(U),len(S)+len(U)-2];T=h.simplices.copy()
   for k,(i,j,l) in enumerate(T):
    if np.dot(np.cross(X[j]-X[i],X[l]-X[i]),h.equations[k,:3])<0:T[k]=[i,l,j]
   det=np.linalg.det(X[T]);g=np.einsum('i,ij->j',det,X[T].sum(axis=1))/(4*det.sum());ownS=roots(eq[:,:3]/(-eq[:,3]-eq[:,:3]@g)[:,None]);ownU=roots(X[h.vertices]-g);V=len(h.vertices);F=len(eq);E=V+F-2
   st=dict(target=target,links=n,grid=D,new_raw_points=ints.tolist(),VEF=[V,E,F],C=2*E,reference=ref,reference_U_input=h.vertices[U].tolist(),own=[len(ownS),len(ownU),len(ownS)+len(ownU)-2],centroid=g.tolist(),volume=float(det.sum()/6),hidden_parent_vertices=[i for i in range(167) if i not in h.vertices],floating_hull_triangles=T.tolist());results.append(st);print(target,n,st['C'],st['reference'],st['own'],flush=True)
 (out/'RESULTS.json').write_text(json.dumps(dict(parent_sha256=hashlib.sha256(parent.read_bytes()).hexdigest(),results=results),sort_keys=True,separators=(',',':'))+'\n');print('PRIMAL_CHAIN_FAMILY_FINISHED',len(results),flush=True)
if __name__=='__main__':main()
