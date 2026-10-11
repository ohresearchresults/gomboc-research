"""SVD physical-coordinate-conditioned escape-forest feasibility search."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,torch,json,pathlib,time,argparse
from scipy.linalg import svd
from scipy.optimize import linprog,minimize,LinearConstraint,Bounds
from geometry import halfspace_mesh,census,arrows,routes
from persistence_search import pairs,polar_edges

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
def choose(m,Q,nP,nQ):
 p=m['X']-m['g'];q=Q/(1-Q@m['g'])[:,None];roots=[]
 for a,ed,n in [(p,m['edges'],nP),(q,polar_edges(m),nQ)]:
  rs=[int(np.argmax((a*a).sum(1)))];pp,h=pairs(a,ed)
  if n>1 and len(pp):
   dep=1-h[pp[:,1]]/(a[pp[:,0]]**2).sum(1);rs.extend(int(pp[i,0]) for i in np.argsort(-dep)[:n-1])
  roots.append(rs)
 return p,q,roots

def polish(Q,out,nP=1,nQ=2,steps=120):
 out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);hist=[];trust=.03;target=2e-7;t0=time.time()
 for it in range(steps):
  m=halfspace_mesh(Q);p,q,roots=choose(m,Q,nP,nQ);rp,rq=roots;ip,jp=routes(p,rp);iq,jq=routes(q,rq)
  wp=arrows(p).max(1);wq=arrows(q).max(1);badp=np.minimum(np.delete(wp,rp)-target,0);badq=np.minimum(np.delete(wq,rq)-target,0);actual=float(np.linalg.norm(np.r_[badp,badq]));st=census(m)
  row=dict(it=it,defect=actual,trust=trust,seconds=time.time()-t0,**st);hist.append(row);print(json.dumps({k:row[k] for k in ['it','defect','trust','S','U','E','seconds']}),flush=True)
  np.savez(out/'latest.npz',Q=Q);(out/'history.json').write_text(json.dumps(hist,indent=2))
  if actual<1e-12 and st['U']==nP and st['S']==nQ:
   np.savez(out/'NOMINATION.npz',Q=Q);print('STRICT_NUMERIC_NOMINATION_REQUIRES_EXACT',nQ,nP,flush=True);return Q
  ti=torch.tensor(m['triples']);tt=torch.tensor(m['triangles']);ip,jp,iq,jq=map(torch.tensor,(ip,jp,iq,jq));q0=torch.tensor(Q)
  sl=1-Q@m['X'].T;ci,cj=np.where((sl>1e-8)&(sl<.05));ci,cj=map(torch.tensor,(ci,cj));nmech=len(ip)+len(iq)
  def calc(z):
   y=z.reshape(Q.shape);x=torch.linalg.solve(y[ti],torch.ones((len(ti),3,1)))[:,:,0];a=x[tt];v=(a[:,0]*torch.linalg.cross(a[:,1],a[:,2])).sum(1)/6;g=(v[:,None]*a.sum(1)).sum(0)/(4*v.sum());P=x-g;R=y/(1-y@g)[:,None]
   def esc(x,i,j):
    d=x[j]-x[i];return (x[i]*d).sum(1)/(torch.linalg.vector_norm(x[i],dim=1)*torch.linalg.vector_norm(d,dim=1)).clamp(min=1e-15)
   vals=torch.cat([esc(P,ip,jp),esc(R,iq,jq),1-(y[ci]*x[cj]).sum(1)])
   return torch.cat([vals,x.flatten()])
  z=q0.flatten();val=calc(z).detach().numpy();jac=torch.func.jacrev(calc)(z).detach().numpy();nv=nmech+len(ci);J=jac[:nv];v=val[:nv]
  scaleX=np.sqrt(np.mean(p*p));scaleQ=np.sqrt(np.mean(q*q));metric=np.vstack([jac[nv:]/scaleX,np.eye(Q.size)/scaleQ]);_,d,Vt=svd(metric,full_matrices=False,check_finite=False);W=Vt.T/d
  A=J@W;b=np.r_[np.full(nmech,target),np.full(len(ci),1e-9)]-v;norm=np.linalg.norm(A,axis=1);keep=norm>1e-14;A=A[keep]/norm[keep,None];b=b[keep]/norm[keep]
  bound=trust/np.sqrt(Q.size)
  lp=linprog(np.zeros(Q.size),A_ub=-A,b_ub=-b,bounds=[(-bound,bound)]*Q.size,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
  if not lp.success:
   row['LP']=lp.message;trust*=1.7
   if trust>.5:print('POLICY_INFEASIBLE_WITHIN_TESTED_TRUST',flush=True);break
   continue
  qp=minimize(lambda x:(.5*x@x,x),lp.x,jac=True,method='SLSQP',constraints=[LinearConstraint(A,b,np.inf)],bounds=Bounds(-bound,bound),options={'ftol':1e-14,'maxiter':120})
  if np.min(A@qp.x-b)<-1e-8:print('QP_RESIDUAL_REJECTED',flush=True);break
  direction=(W@qp.x).reshape(Q.shape);accepted=False
  for k in range(20):
   qt=Q+direction*2**-k
   try:
    mt=halfspace_mesh(qt);pt,rt,rr=choose(mt,qt,nP,nQ);vv=np.r_[np.minimum(np.delete(arrows(pt).max(1),rr[0])-target,0),np.minimum(np.delete(arrows(rt).max(1),rr[1])-target,0)];merit=float(np.linalg.norm(vv))
   except Exception:continue
   if merit<actual*(1-1e-4*2**-k):Q=qt;accepted=True;break
  row['accepted']=accepted;row['halvings']=k
  if not accepted:
   trust*=.4
   if trust<1e-7:print('GEOMETRIC_POLISH_STALLED',flush=True);break
 return Q
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--nP',type=int,default=1);ap.add_argument('--nQ',type=int,default=2);ap.add_argument('--steps',type=int,default=120);a=ap.parse_args();polish(np.load(a.input)['Q'],a.out,a.nP,a.nQ,a.steps)
