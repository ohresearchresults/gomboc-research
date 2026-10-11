"""Eight-parameter physical projective/affine orbit of literal J91 C434.
A is upper triangular with determinant one; y=A x/(1+b.x). Mass is recomputed.
No independently chosen reference centre or inconsistent dual metric is used.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,torch,pathlib,json,time,argparse
from scipy.optimize import minimize
from audit_exact import R
from geometry import halfspace_mesh,census
from persistence_search import pairs,polar_edges

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
def run(out,tries=100,seed=701):
 out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);rng=np.random.default_rng(seed)
 Q=np.load('artifacts/j91-c434/seed.npz')['Q'];m=halfspace_mesh(Q);X=m['X'];ep=m['edges'];eq=polar_edges(m);tt=torch.tensor(m['triangles']);xt=torch.tensor(X);qt=torch.tensor(Q)
 best=float('inf');rows=[];t0=time.time()
 def geo(z):
  zero=z[0]*0;A=torch.stack([torch.stack([z[0].exp(),z[2],z[3]]),torch.stack([zero,z[1].exp(),z[4]]),torch.stack([zero,zero,(-z[0]-z[1]).exp()])]);b=z[5:];den=1+xt@b
  Y=(xt@A.T)/den[:,None];qn=torch.linalg.solve(A.T,(qt+b).T).T
  a=Y[tt];v=(a[:,0]*torch.linalg.cross(a[:,1],a[:,2])).sum(1)/6;g=(v[:,None]*a.sum(1)).sum(0)/(4*v.sum())
  return Y-g,qn/(1-qn@g)[:,None],den,qn,A,b,g
 def loss(z,eps):
  zz=torch.tensor(z,requires_grad=True);den=1+xt@zz[5:]
  if float(den.min().detach())<.15:
   f=10+((.15-den).clamp(min=0)**2).sum()*100;grad=torch.autograd.grad(f,zz)[0].detach().numpy();return float(f.detach()),grad
  p,q,den,qn,A,b,g=geo(zz);value=zz.sum()*0
  for y,edges in [(p,ep),(q,eq)]:
   pp,_=pairs(y.detach().numpy(),edges)
   if not len(pp):continue
   bi=torch.tensor(pp[:,0]);ee=torch.tensor(edges[pp[:,1]]);a=y[ee[:,0]];d=y[ee[:,1]]-a;t=(-(a*d).sum(1)/(d*d).sum(1)).clamp(0,1);dep=(1-((a+t[:,None]*d)**2).sum(1)/(y[bi]**2).sum(1)).clamp(min=0)
   value=value+torch.log1p(dep/eps).sum()*eps
  grad=torch.autograd.grad(value,zz)[0].detach().numpy();return float(value.detach()),grad
 for it in range(tries):
  if it==0:z=np.zeros(8)
  elif it%4==0:z=bestz+rng.normal(0,.01,8)
  else:z=np.r_[rng.normal(0,.12,5),rng.normal(0,.035,3)]
  eps=[.01,.001,.0001,.03][it%4]
  res=minimize(lambda z:loss(z,eps),z,jac=True,method='L-BFGS-B',bounds=[(-1.2,1.2)]*5+[(-.4,.4)]*3,options={'maxiter':300,'gtol':1e-10,'ftol':1e-13,'maxls':25})
  try:
   p,q,den,qn,A,b,g=geo(torch.tensor(res.x));qh=qn.detach().numpy();mm=halfspace_mesh(qh);st=census(mm)
   bars=[]
   for yy,edges in [(p.detach().numpy(),ep),(q.detach().numpy(),eq)]:
    pp,h=pairs(yy,edges);rr=(yy*yy).sum(1);bars.append((1-h[pp[:,1]]/rr[pp[:,0]]).tolist())
   score=sum(np.log1p(np.array(v)/.001).sum() for v in bars)*.001
   row=dict(trial=it,eps=eps,score=float(score),seconds=time.time()-t0,P=bars[0],Q=bars[1],**st);rows.append(row)
   if score<best:
    best=score;bestz=res.x.copy();np.savez(out/'best.npz',Q=qh,z=bestz,A=A.detach().numpy(),b=b.detach().numpy());(out/'best.json').write_text(json.dumps(row,indent=2));print('BEST',json.dumps(row),flush=True)
   if st['S']==st['U']==1:np.savez(out/'NOMINATION110.npz',Q=qh,z=res.x,A=A.detach().numpy(),b=b.detach().numpy());print('NOMINATION110_REQUIRES_EXACT',flush=True);break
  except Exception as e:rows.append(dict(trial=it,error=str(e)))
  if it%10==0:print('TRIAL',it,'best',best,'elapsed',time.time()-t0,flush=True)
  (out/'history.json').write_text(json.dumps(rows,indent=2))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);ap.add_argument('--tries',type=int,default=100);a=ap.parse_args();run(a.out,a.tries)
