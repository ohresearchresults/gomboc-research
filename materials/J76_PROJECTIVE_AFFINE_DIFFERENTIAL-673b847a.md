# material-673b847a1525

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J76 — projective/affine factorization, differential identities, finite coupled scan

## Definitions and precise claim scope
Reuse the canonical projective centering of [internal-source-reference]. For an original convex K, reference c in its interior, x=p-c and d=1+b.x, let b(c) be the unique minimizer of Phi(c,b)=integral_K[1+b.(p-c)]^-4 dp. Let L_c=T_b(K-c), V(c)=Vol(L_c), and Sigma(c)=V^-1 integral_L yy^T dy. The own centroid of L_c is0, so Sigma is its positive-definite covariance. These are differential identities derived here for a known projective-centering mechanism, not a novelty claim for the general existence theorem. Numerical checks below are sanity checks of the explicit implementation, not substitutes for the derivation.

### Full projective orbit modulo output affine transformations
Every nonsingular projective image F(K) whose denominator has constant nonzero sign on K can be centered in the form A T_b(c)(K-c) for a unique preimage c=F^-1(centroid(FK)) and nonsingular A. Indeed, writing F(p)=(A0 p+a)/(l.p+d0) and subtracting g=centroid(FK), the numerator vanishes at c. Thus
F(c+x)-g=[(A0-g*l^T)/(l.c+d0)] x/[1+(l/(l.c+d0)).x].
The bracketed matrix is nonsingular. Since the image has centroid0, its pre-affine projective factor also has centroid0, forcing b=b(c) by the centering uniqueness. Hence the entire centered projective orbit is parameterized by c in interior(K), followed by a positive metric G=A^T A. Rotation and uniform scale do not change equilibrium counts; G has five essential normalized parameters. The c-only sweep previously performed was not the whole family: the remaining affine metric matters. This factorization is a research formulation, not an existence claim for110 within that orbit.

### Exact differential identities in dimension3
Use F(c,b)=integral x*d^-5 dp=0 at the minimizer and H=Hess_b Phi=20 integral xx^T*d^-6 dp. The change of variables y=x/d gives H=20 V Sigma. Also integral d^-5=V and integral x*d^-6=-(H/20)b, since d=1+b.x and F=0. Therefore
F_b=-H/4,
F_c=-V I-(H b b^T)/4,
Db/Dc=-(1/5) Sigma^-1-b b^T=-4V H^-1-b b^T.
This Jacobian is symmetric negative definite everywhere. The envelope identity is
D_c log V=4b,
Hess_c log V=-(4/5) Sigma^-1-4b b^T<0.
Thus optimized log projective volume is strictly concave on interior(K); its unique stationary point is the original homogeneous centroid, where b=0. This volume potential does not measure proximity to equilibrium class110.
For any fixed material point p and y=(p-c)/(1+b(c).(p-c)), the exact material velocity is
D_c y=-(1-b.y)I+y b^T+(1/5)y y^T Sigma^-1.
At the original centroid this is -I+(1/5)y y^T Sigma^-1. This gives the three mass-centered projective deformation directions explicitly; together with affine directions it avoids numerical differentiation through a mass-centering solver. It does not avoid checking changes in equilibrium witnesses or hull contacts for more general material deformations.

### Numerical differential check
The complete unit below evaluated central differences with step2e-7 at the original own centroid, halfway to REF_NEAR, and REF_ROBUST. Relative Jacobian errors were approximately2.42e-10,1.40e-10,1.22e-7; relative vertex-velocity errors3.29e-10,2.22e-10,1.24e-7. The log-volume gradient scaled errors were5.55e-10,1.27e-10,8.95e-11. The reference-robust Jacobian eigenvalues were approximately(-2228.20126836,-140.21387292,-81.2203311391), demonstrating the much greater sensitivity near the boundary. All numerical residuals, matrices and steps are in the generated report. No approximate residual is called exact centering.

## Finite coupled projective-plus-affine scan
The finite test used42 reference centres: original own centroid, REF_NEAR, REF_ROBUST, plus c=g+t*(p_i-g), for i=0,6,...,72 and t in(.3,.6,.85). Each was canonically projectively centered, with its actual residual centroid subtracted. Eight principal frames were chosen: identity plus seven normal-quaternion frames with seed760326. For each frame the floating polygon method from frames76.py examined the normalized positive scale simplex with eigenvalues at least1e-7, on both primal G and reciprocal polar G^-1. Representative points of nominated single-root regions were checked with every actual outgoing guard on both landscapes. No validated one-sided or110 candidate was found:42*8=336 frame/centre tests. This is NOT an exclusion of all c, all frames, all positive-definite G, or tiny cells below the floating area thresholds. The code inherits1e-18 polygon-area and1e-15 nomination thresholds, and all floating persistence depths inherit1e-12 filtering from projective76.py. These are search limits, not exact zero claims.

## Complete source dependencies and receipts
For projective76_differential.py, supply this material, [internal-source-reference] (projective76.py), and [internal-source-reference] (exact J75 source). The coupled scan additionally requires [internal-source-reference] (frames76.py and metric76.py). These are complete source dependencies; no raw old sandbox or FULL76 is needed.
Save each following code fence verbatim with one terminating LF. Executed Python3.13.5,NumPy2.3.5,SciPy1.17.0,Shapely2.1.2,OPENBLAS_NUM_THREADS=1.
projective_affine76.py2836B SHA111199a9748afb0a83e5611c3c33b968a644510e7baee23a45e0f6dcb3b3b82e. Command OPENBLAS_NUM_THREADS=1 python projective_affine76.py 8. Observed output projective_affine76.json39280B SHA8b8ec0e93958c664d85a73b1e0d06b85a096a8c06fcc29c55f50d53a17efd07b; terminal J76_PROJECTIVE_AFFINE_NOMINATION_DONE 42 8 hits 0.
projective76_differential.py1940B SHA88a42a22e8b6f671d5d16e2fa66aedbab6e75c6d3ca9e474b04510df599ebd53. Command OPENBLAS_NUM_THREADS=1 python projective76_differential.py. Observed output projective76_differential.json1854B SHA5072c50963d84b2355e1a0677cf5171b1905f79283ae14d22162fc4bd97853c9; terminal J76_PROJECTIVE_DIFFERENTIAL_NUMERICAL_CHECK_PASS. Floating output hashes may depend on the numerical platform; neither unit defines a new exact body.

## projective_affine76.py
```python
"""Full scale-simplex nominations after canonical projective centering.
Finite floating search, NOT an exclusion of the full projective/affine orbit.
Requires projective76.py, frames76.py, metric76.py and exact J75 source.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from pathlib import Path
import json,sys
import numpy as np
from scipy.spatial.transform import Rotation
from projective76 import setup,solve,root_data,depths
from frames76 import single_regions,pieces,lam
from metric76 import guards,counts
import J75_REFERENCE110_CAP233 as m

def main(nframes=8):
 K,p,g,tri,ns=setup();rng=np.random.default_rng(760326)
 frames=[np.eye(3)]+[Rotation.from_quat(rng.normal(size=4)).as_matrix() for _ in range(nframes-1)]
 centres=[('own',g),('near',np.array(m.REF_NEAR,float)),('robust',np.array(m.REF_ROBUST,float))]
 centres += [(f'vertex{i}_t{t}',g+t*(p[i]-g)) for i in range(0,75,6) for t in [.3,.6,.85]]
 rows=[];hits=[]
 for k,(name,c) in enumerate(centres):
  b,J,it=solve(p,c,tri);V,gr,H,y,gp,den=J;x=y-gp
  height=np.einsum('ij,ij->i',ns,p[[f[0] for f in K['faces']]]-c)
  q0=ns/height[:,None]+b;q=q0/(1-q0@gp)[:,None]
  CP,_,up=guards(x,K['edges']);CQ,_,sp=guards(q,K['edge_faces'])
  row={'centre_name':name,'c':c.tolist(),'b':b.tolist(),'centroid':gp.tolist(),'frames':[]}
  for j,frame in enumerate(frames):
   PR,pa,pn,pcov=single_regions(x,K['edges'],frame)
   SR,sa,sn,scov=single_regions(q,K['edge_faces'],frame)
   row['frames'].append({'frame':j,'P_single_area':pa,'S_single_area':sa,'P_roots':[i for i,r in PR],'S_roots':[i for i,r in SR]})
   for side,regions in [('P',PR),('S',SR)]:
    for root,region in regions:
     for poly in pieces(region):
      pt=poly.representative_point();l=lam((pt.x,pt.y));G=frame@np.diag(l)@frame.T
      if side=='S':G=np.linalg.inv(G);G/=np.trace(G)
      U=counts(G,CP,up);S=counts(np.linalg.inv(G),CQ,sp)
      if len(U)==1 or len(S)==1:
       h={'centre_name':name,'c':c.tolist(),'b':b.tolist(),'G':G.tolist(),'frame':j,'side':side,'U':U,'S':S}
       ev,Q=np.linalg.eigh(G);A=Q@np.diag(np.sqrt(ev))@Q.T
       h['P_depths']=depths(x@A,K['edges']);h['Q_depths']=depths(q@np.linalg.inv(A),K['edge_faces'])
       hits.append(h);print('ONE_SIDE',name,j,side,'SU',len(S),len(U),'PQ',h['P_depths'][:2],h['Q_depths'][:2],flush=True)
       if len(U)==len(S)==1:print('CANDIDATE110',json.dumps(h),flush=True)
  rows.append(row)
  out={'seed':760326,'nframes':nframes,'frames':[f.tolist() for f in frames],'rows':rows,'hits':hits}
  Path('projective_affine76.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
  print('CENTRE_DONE',k,name,'hits',len(hits),flush=True)
 print('J76_PROJECTIVE_AFFINE_NOMINATION_DONE',len(centres),nframes,'hits',len(hits),flush=True)
if __name__=='__main__':main(int(sys.argv[1]) if len(sys.argv)>1 else 8)
```

## projective76_differential.py
```python
"""Finite-difference sanity check of the analytically derived centering identities.
Numerical checks do not replace the proof; exact input comes from J75 source.
Requires projective76.py and J75_REFERENCE110_CAP233.py.
"""
from pathlib import Path
import json,hashlib
import numpy as np
from projective76 import setup,solve
import J75_REFERENCE110_CAP233 as m

def main():
 K,p,g,tri,ns=setup();near=np.array(m.REF_NEAR,float);robust=np.array(m.REF_ROBUST,float)
 out=[];h=2e-7
 for name,c in [('own',g),('half-near',(g+near)/2),('robust',robust)]:
  b,(V,grad,H,y,res,den),it=solve(p,c,tri)
  J=-4*V*np.linalg.inv(H)-np.outer(b,b)
  dy=-(1-y@b)[:,None,None]*np.eye(3)+np.einsum('ia,b->iab',y,b)+4*V*np.einsum('ia,ib,bc->iac',y,y,np.linalg.inv(H))
  fd=np.zeros((3,3));dv=np.zeros(3);fd_y=np.zeros_like(dy)
  for k in range(3):
   step=np.eye(3)[k]*h
   bp,P,_=solve(p,c+step,tri,b);bm,M,_=solve(p,c-step,tri,b)
   fd[:,k]=(bp-bm)/(2*h);dv[k]=(np.log(P[0])-np.log(M[0]))/(2*h)
   fd_y[:,:,k]=(P[3]-M[3])/(2*h)
  error=np.linalg.norm(fd-J)/np.linalg.norm(J)
  error_y=np.linalg.norm(fd_y-dy)/np.linalg.norm(dy)
  error_v=np.linalg.norm(dv-4*b)/max(1,np.linalg.norm(4*b))
  row={'reference':name,'b':b.tolist(),'own_centroid_residual':res.tolist(),'J':J.tolist(),'J_eigenvalues':np.linalg.eigvalsh(J).tolist(),'finite_difference_step':h,'relative_J_error':float(error),'relative_vertex_velocity_error':float(error_y),'scaled_log_volume_gradient_error':float(error_v)}
  print('DIFFERENTIAL',name,error,error_y,error_v,row['J_eigenvalues'],flush=True)
  assert max(error,error_y,error_v)<1e-4 and max(row['J_eigenvalues'])<0
  out.append(row)
 raw=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode();Path('projective76_differential.json').write_bytes(raw)
 print('RECEIPT',len(raw),hashlib.sha256(raw).hexdigest(),flush=True)
 print('J76_PROJECTIVE_DIFFERENTIAL_NUMERICAL_CHECK_PASS',flush=True)
if __name__=='__main__':main()
```
