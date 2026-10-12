"""Numerical proposal generation only; exact SELECTORS/A/B acceptance is separate.
Frozen tested dependencies: Python3.13.5, NumPy2.3.5, SciPy1.17.0.
"""
import hashlib,json,sys
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
from scipy.spatial import ConvexHull
sys.set_int_max_str_digits(0)
def main():
 source,out=map(Path,sys.argv[1:]);a=json.loads(source.read_text());raw=np.array([[float(Q(t)) for t in r] for r in a['raw_vertices']]);g=np.array([float(Q(t)) for t in a['raw_centroid']]);P=raw-g
 u,v=P[7],P[85];rho=np.linalg.norm(u);gamma=np.dot(u,v)/(rho*np.linalg.norm(v));phi=np.arccos(gamma);e=u/rho;f=(v/np.linalg.norm(v)-gamma*e)/np.sqrt(1-gamma**2);lam=(np.linalg.norm(v)/rho)**(1/5)
 chain=np.array([rho*lam**k*(np.cos(k*phi/5)*e+np.sin(k*phi/5)*f) for k in range(1,5)]);grid=10**12;ints=np.rint((chain+g)*grid).astype(np.int64)
 assert ints.tolist()==[[-652386830976,-278549019006,-59994875610],[-673052036488,-291747836672,247470117785],[-570437000458,-249889387058,566581053189],[-339758403441,-150071123912,838060234941]]
 X=np.r_[raw,ints/grid];hull=ConvexHull(X);T=hull.simplices.copy()
 for k,(i,j,l) in enumerate(T):
  if np.dot(np.cross(X[j]-X[i],X[l]-X[i]),hull.equations[k,:3])<0:T[k]=[i,l,j]
 det=np.linalg.det(X[T]);vol=det.sum()/6;cg=np.einsum('i,ij->j',det,X[T].sum(axis=1))/(4*det.sum());pol=[]
 for row in hull.equations:
  if not any(np.linalg.norm(row-q)<1e-8 for q in pol):pol.append(row)
 eq=np.array(pol);verts=X[hull.vertices]-cg;duals=eq[:,:3]/(-eq[:,3]-eq[:,:3]@cg)[:,None]
 def nmax(V):
  t=V@V.T-np.sum(V*V,axis=1)[:,None];np.fill_diagonal(t,-np.inf);return int((t.max(axis=1)<0).sum())
 U=nmax(verts);S=nmax(duals);V=len(hull.vertices);F=len(pol)
 report={'floating_VEF':[V,V+F-2,F],'floating_centroid':cg.tolist(),'floating_counts':[S,U,S+U-2],'floating_hull_triangles':T.tolist(),'floating_volume':float(vol),'grid':grid,'new_raw_points':ints.tolist(),'parent_audit_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
 out.write_text(json.dumps(report,sort_keys=True,separators=(',',':'))+'\n');print('CHAIN5_NUMERICAL_PROPOSAL',report['floating_VEF'],report['floating_counts'])
if __name__=='__main__':main()
