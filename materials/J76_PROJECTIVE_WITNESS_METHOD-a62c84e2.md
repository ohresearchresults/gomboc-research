# material-a62c84e29f36

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J76 — directly optimizing one-root witnesses in the eight-parameter projective orbit

## Method and significance
This is a complete executed nomination method, not a new exact body and not an infeasibility proof. It uses the analytic centering derivatives from [internal-source-reference] rather than simply reducing persistence depths. The geometric input is literal R22-B7 via J75 source.

For a centered primal vertex u and true incident edge e, use the normalized outgoing score s=u^T G e/sqrt((u^T G u)*(e^T G e)). A non-root vertex needs at least one strictly positive score; its maximum over neighbors is therefore constrained. Apply the same condition to the centered polar vertices with G^-1 for the stable landscape. All vertices/facets are included. If every vertex except one has a strictly positive outgoing witness, squared G-radius strictly increases along those witnesses. A finite graph cannot have a directed cycle, and its unique terminal root must itself be a strict local maximum: a zero outgoing root guard would lead to a neighbor of strictly greater squared radius, which cannot have a positive-witness path back to that root. Thus exact strict positivity of all non-root maxima on both graphs would give the desired two one-root landscapes; final S/U/H and additional weak census would still be checked directly.

The source minimizes the sum of squared positive parts of tau minus those non-root maximum scores, with tau=1e-6. A positive objective is not success, however small. In particular, the designated roots are not assumed to exist in a partial solution. Actual roots of each numerical image are retained in the report. The metric is G=L L^T with five free Cholesky parameters and last diagonal fixed1, covering positive metrics up to uniform scale. Reference c supplies the other three projective parameters. The normalized support distances are constrained at least1e-4. Log-diagonal parameters are bounded[-3,3], other Cholesky entries[-4,4]. These are finite search restrictions, not necessary geometric conditions.

Analytic derivatives include both the inverse-metric derivative and the canonical projective mass-centering Jacobian. Residual own centroid from the numerical Newton solve is subtracted for score values; derivatives use the exact centered-section formulas. One specified regular test point checked the full eight-dimensional objective derivative against central differences of step1e-6, relative error1.4020783853617953e-9. This is a numerical consistency check at that point, not a global differentiability claim across changes of active neighbor.

## Executed finite results
Eight SLSQP starts with seed760426 and maxiter250 completed. The first four start from the old own centroid and identity metric, taking desired U/S roots(6,53),(62,53),(6,27),(62,27). Four randomized starts use the exact seeded choices in the source. Observed tuples(run,best loss,numerical S count,U count,score calls,status) were:
(0,.00936820062784396,22,19,30,0);
(1,.000046947294021549786,3,3,430,9);
(2,.00018606359548680183,4,7,237,0);
(3,.0028168746173190254,10,4,172,0);
(4,.00006851511742748788,3,4,408,9);
(5,.0007185094797391092,7,5,333,0);
(6,.014897397852456853,7,7,73,0);
(7,.00025205217175198693,4,4,281,0).
Status0 means only the optimizer's termination criterion, not110. Status9 is its iteration limit. No start yielded even a numerical S1 or U1. The best run1 had negative non-root scores approximately-.004310475733532155 and-.002298920393343217. Its metric eigenvalues approximately(.0361345424,1.00049814,403.897883) show substantial anisotropy and its first log-diagonal hit the bound3. Reduced loss did not mean real cancellation; continuing toward near-degenerate metrics is not a certified body.

Complete best numerical continuation checkpoint (not an exact body claim): desired roots U62,S53; z=(c_x,c_y,c_z,log L11,log L22,L21,L31,L32)=(-.07747610965234217,-.1908713942965784,-.4610979718020658,3.,-1.65942296207708,-.6279960800213287,-.27293702162590655,-.02557971085862086). The centering solve gave b approximately(-.06261154184209874,.34493810166803013,.5885285273291903), residual centroid around(4.94e-15,5.36e-15,-6.09e-15). Actual numerical U labels2,3,62 and S53,98,103. Neither H nor exact weak status is promoted for this working point. This finite failure is not a root-free projective exclusion and does not apply to h90's changed one-sided bodies.

## Dependencies and reconstruction
Supply this material, [internal-source-reference] for complete projective76.py, and [internal-source-reference] for J75_REFERENCE110_CAP233.py with its exact75 input rows. The mathematical derivative derivation is in [internal-source-reference]; its separate source programs are not imported by this method. No FULL76, old optimizer workspace or previous nomination output is needed.
Save the following complete code fences with one final LF. Executed Python3.13.5,NumPy2.3.5,SciPy1.17.0,OPENBLAS_NUM_THREADS=1.
projective76_witness.py4805B SHA18ce35b244e89f6e1b99508fd9dda52c98d979d5193a46b96765f90c297a433b. Run OPENBLAS_NUM_THREADS=1 python projective76_witness.py 8. Observed summary projective76_witness.json6346B SHA7b21e023b364d75873f0f21c3205e21ebd5ba53514dfb17d369ec1ab89b24165; terminal J76_PROJECTIVE_WITNESS_SEARCH_DONE 8. Per-start best files are also emitted, named projective76_witness_00.json through _07.json. Floating optimizer paths and their serialized hashes can be platform-sensitive; they are not exact geometry certificates.
witness_gradient76.py923B SHA207a56274fd7dae8bd2465fceaad783ef0e4dc8ccb1fd549e6d602fbabfb5bff. Run OPENBLAS_NUM_THREADS=1 python witness_gradient76.py. Observed report witness_gradient76.json540B SHA608fd4670d7d005d14a74a69211975cb25c76a16c57c0b33b1cb00f67d604058; marker J76_WITNESS_GRADIENT_NUMERICAL_CHECK_PASS.

## projective76_witness.py
```python
"""Eight-parameter projective/affine witness search with analytic mass-centering Jacobian.
Finite numerical nomination only; no proof of infeasibility from a failed search.
Dependencies: projective76.py and J75_REFERENCE110_CAP233.py, NumPy/SciPy.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from pathlib import Path
import json,sys
import numpy as np
from scipy.optimize import minimize,LinearConstraint,Bounds
from projective76 import setup,solve

K,p,g,tri,ns=setup()
unit=ns/np.linalg.norm(ns,axis=1)[:,None]
height=np.einsum('ij,ij->i',unit,p[[f[0] for f in K['faces']]])

def directed(edges,n):
 nb=[[] for _ in range(n)]
 for i,j in edges:nb[i].append(j);nb[j].append(i)
 i=[];j=[];starts=[]
 for a,l in enumerate(nb):
  starts.append(len(i));i.extend([a]*len(l));j.extend(sorted(l))
 return np.array(i),np.array(j),starts
IP,JP,SP=directed(K['edges'],len(p));IQ,JQ,SQ=directed(K['edge_faces'],len(ns))

def metric(z):
 L=np.array([[np.exp(z[0]),0,0],[z[2],np.exp(z[1]),0],[z[3],z[4],1.]])
 dL=np.zeros((3,3,5));dL[0,0,0]=L[0,0];dL[1,1,1]=L[1,1];dL[1,0,2]=1;dL[2,0,3]=1;dL[2,1,4]=1
 G=L@L.T;dG=np.einsum('ikp,jk->ijp',dL,L)+np.einsum('ik,jkp->ijp',L,dL)
 return G,dG

def score(x,dx,M,dM,I,J,starts):
 u=x[I];e=x[J]-u;du=dx[I];de=dx[J]-du
 um=u@M;em=e@M
 a=np.einsum('ij,ij->i',um,u);b=np.einsum('ij,ij->i',em,e);v=np.einsum('ij,ij->i',um,e)
 den=np.sqrt(a*b);s=v/den
 dv=np.einsum('ijp,ij->ip',du,em)+np.einsum('ij,ijp->ip',um,de)+np.einsum('ij,jkp,ik->ip',u,dM,e)
 da=2*np.einsum('ijp,ij->ip',du,um)+np.einsum('ij,jkp,ik->ip',u,dM,u)
 db=2*np.einsum('ijp,ij->ip',de,em)+np.einsum('ij,jkp,ik->ip',e,dM,e)
 ds=dv/den[:,None]-.5*s[:,None]*(da/a[:,None]+db/b[:,None])
 ends=starts[1:]+[len(s)];active=[a+int(np.argmax(s[a:b])) for a,b in zip(starts,ends)]
 return s[active],ds[active]

class Problem:
 def __init__(self,r,s,path,tau=1e-6):self.r=r;self.s=s;self.path=Path(path);self.tau=tau;self.best=np.inf;self.calls=0
 def evaluate(self,z):
  c=z[:3];slack=height-unit@c
  if min(slack)<=0:
   bad=np.minimum(slack-1e-8,0);return 10.+bad@bad,np.r_[-2*bad@unit,np.zeros(5)]
  try:
   b,J,it=solve(p,c,tri);V,grad,H,y,gp,dm=J
   Hi=np.linalg.inv(H);db=-4*V*Hi-np.outer(b,b)
   dy=-(1-y@b)[:,None,None]*np.eye(3)+np.einsum('ia,b->iab',y,b)+4*V*np.einsum('ia,ib,bc->iac',y,y,Hi)
   rr=unit/slack[:,None];q0=rr+b
   dq=np.einsum('ia,ib->iab',rr,rr)+db
   # Residual subtraction affects values; derivatives use the exact centered section.
   x=y-gp;q=q0/(1-q0@gp)[:,None]
   G,D=metric(z[3:]);Gi=np.linalg.inv(G)
   dG=np.zeros((3,3,8));dG[:,:,3:]=D;dGi=-np.einsum('ij,jkp,kl->ilp',Gi,dG,Gi)
   dx=np.zeros((len(x),3,8));dx[:,:,:3]=dy;dqq=np.zeros((len(q),3,8));dqq[:,:,:3]=dq
   up,dup=score(x,dx,G,dG,IP,JP,SP);sp,dsp=score(q,dqq,Gi,dGi,IQ,JQ,SQ)
   rp=np.maximum(self.tau-up,0);rs=np.maximum(self.tau-sp,0);rp[self.r]=0;rs[self.s]=0
   value=rp@rp+rs@rs;jac=-2*(rp@dup+rs@dsp)
  except (np.linalg.LinAlgError,ValueError,FloatingPointError):return 1000.+z@z,2*z
  self.calls+=1
  if value<self.best:
   self.best=float(value);out={'value':self.best,'tau':self.tau,'U_root':self.r,'S_root':self.s,'z':z.tolist(),'b':b.tolist(),'G':G.tolist(),'own_centroid_residual':gp.tolist(),'U':np.where(up<0)[0].tolist(),'S':np.where(sp<0)[0].tolist(),'worst_nonroot_P':float(min(np.delete(up,self.r))),'worst_nonroot_Q':float(min(np.delete(sp,self.s))),'calls':self.calls}
   self.path.write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
  return float(value),jac

def main(runs=8):
 rng=np.random.default_rng(760426);rows=[]
 A=np.zeros((len(unit),8));A[:,:3]=unit
 constraint=LinearConstraint(A,-np.inf,height-1e-4)
 bounds=Bounds(np.r_[p.min(0),[-3,-3,-4,-4,-4]],np.r_[p.max(0),[3,3,4,4,4]])
 for k in range(runs):
  r=[6,62,6,62][k%4];s=[53,53,27,27][k%4]
  z=np.r_[g,np.zeros(5)]
  if k>=4:
   target=p[int(rng.integers(len(p)))];z[:3]=.8*g+.2*target;z[3:]=rng.normal(size=5)*.15
  prob=Problem(r,s,f'projective76_witness_{k:02d}.json')
  result=minimize(prob.evaluate,z,jac=True,method='SLSQP',constraints=constraint,bounds=bounds,options={'maxiter':250,'ftol':1e-15,'disp':False})
  best=json.loads(prob.path.read_text());best.update({'run':k,'status':int(result.status),'message':str(result.message),'total_calls':prob.calls})
  rows.append(best);Path('projective76_witness.json').write_text(json.dumps(rows,sort_keys=True,separators=(',',':'))+'\n')
  print('WITNESS_RUN',k,prob.best,'SU',len(best['S']),len(best['U']),'guards',best['worst_nonroot_P'],best['worst_nonroot_Q'],'calls',prob.calls,'status',result.status,flush=True)
  if len(best['S'])==len(best['U'])==1:print('NUMERICAL_110_NOMINEE',json.dumps(best),flush=True)
 print('J76_PROJECTIVE_WITNESS_SEARCH_DONE',len(rows),flush=True)
if __name__=='__main__':main(int(sys.argv[1]) if len(sys.argv)>1 else 8)
```

## witness_gradient76.py
```python
"""One finite-difference check at a specified regular witness-search point."""
from pathlib import Path
import json,hashlib
import numpy as np
from projective76_witness import Problem,g

def main():
 z=np.r_[g+np.array([.013,-.017,.011]),[.11,-.12,.05,-.04,.03]]
 prob=Problem(6,53,'witness_gradient76_probe.json');f,jac=prob.evaluate(z)
 h=1e-6;fd=np.zeros(8)
 for k in range(8):
  e=np.eye(8)[k]*h;fd[k]=(prob.evaluate(z+e)[0]-prob.evaluate(z-e)[0])/(2*h)
 error=float(np.linalg.norm(jac-fd)/max(1e-12,np.linalg.norm(fd)))
 out={'z':z.tolist(),'h':h,'value':f,'analytic_gradient':jac.tolist(),'central_difference':fd.tolist(),'relative_error':error}
 raw=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode();Path('witness_gradient76.json').write_bytes(raw)
 assert error<1e-5
 print('J76_WITNESS_GRADIENT_NUMERICAL_CHECK_PASS',error,len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':main()
```
