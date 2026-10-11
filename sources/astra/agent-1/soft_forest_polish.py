"""Own-mass support retraction with bottleneck forests and explicit L1 residuals.
Bottleneck/L1 formulation informed by agent3/polish_121.py (shared source).
SVD support-to-physical-coordinate conditioning and H-body geometry are agent1.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,torch,json,pathlib,time,argparse
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from geometry import halfspace_mesh,census,arrows
from geometric_polish import choose

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
def forest(A,roots):
 w=arrows(A);cap=np.full(len(A),-np.inf);cap[roots]=np.inf;used=np.zeros(len(A),bool);parent=np.full(len(A),-1,int)
 for _ in range(len(A)):
  j=int(np.argmax(np.where(used,-np.inf,cap)));used[j]=True;new=np.minimum(cap[j],w[:,j]);take=(new>cap)&(~used);cap[take]=new[take];parent[take]=j
 for j in roots:parent[j]=int(np.argmax(w[j]))
 assert np.all(parent>=0)
 return parent

def guards(Q,nP,nQ):
 m=halfspace_mesh(Q);p,q,rr=choose(m,Q,nP,nQ);vectors=[];parents=[];signs=[]
 for x,roots in zip([p,q],rr):
  pa=forest(x,roots);sg=np.ones(len(x));sg[roots]=-1;w=arrows(x);vectors.append(sg*w[np.arange(len(x)),pa]);parents.append(pa);signs.append(sg)
 return m,np.r_[tuple(vectors)],parents,signs

def run(Q,out,nP=1,nQ=2,steps=250,apex=False):
 out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);trust=.02;eps=5e-7;hist=[];t0=time.time()
 fixed=np.isclose(Q[:,2],1,atol=1e-12,rtol=0) if apex else np.zeros(len(Q),bool);mask=np.ones(Q.shape,bool);mask[fixed,2]=False;flat=np.flatnonzero(mask.ravel());d=len(flat)
 for it in range(steps):
  m,v,pa,sg=guards(Q,nP,nQ);merit=float(np.maximum(eps-v,0).sum());st=census(m);row=dict(it=it,merit=merit,minimum=float(v.min()),trust=trust,seconds=time.time()-t0,**st);hist.append(row)
  print(json.dumps({k:row[k] for k in ['it','merit','minimum','S','U','E','trust','seconds']}),flush=True)
  np.savez(out/'latest.npz',Q=Q);(out/'history.json').write_text(json.dumps(hist,indent=2))
  exact_sign_numeric=census(m,0)
  if exact_sign_numeric['S']==exact_sign_numeric['U']==1 and min(exact_sign_numeric['min_primal_nonroot'],exact_sign_numeric['min_polar_nonroot'])>1e-9:
   np.savez(out/'POTENTIAL_OWN110.npz',Q=Q);print('POTENTIAL_OWN110_REQUIRES_COMPLETE_EXACT',flush=True);break
  if v.min()>eps*.8 and st['S']==nQ and st['U']==nP:
   np.savez(out/'NOMINATION.npz',Q=Q);print('STRICT_NUMERICAL_NOMINATION_REQUIRES_EXACT',nQ,nP,flush=True);break
  ti=torch.tensor(m['triples']);tt=torch.tensor(m['triangles']);parents=list(map(torch.tensor,pa));signs=list(map(torch.tensor,sg))
  def calc(z):
   q=z.reshape(Q.shape);x=torch.linalg.solve(q[ti],torch.ones((len(ti),3,1)))[:,:,0];a=x[tt];vol=(a[:,0]*torch.linalg.cross(a[:,1],a[:,2])).sum(1)/6;g=(vol[:,None]*a.sum(1)).sum(0)/(4*vol.sum());P=x-g;R=q/(1-q@g)[:,None];vs=[]
   for A,pa,sg in zip([P,R],parents,signs):
    d=A[pa]-A;vs.append(sg*(A*d).sum(1)/(torch.linalg.vector_norm(A,dim=1)*torch.linalg.vector_norm(d,dim=1)).clamp(min=1e-15))
   return torch.cat([*vs,x.flatten()])
  z=torch.tensor(Q.ravel());J=torch.func.jacrev(calc)(z).detach().numpy()[:,flat];nm=len(v);scaleX=np.sqrt(np.mean((m['X']-m['g'])**2));scaleQ=np.sqrt(np.mean(Q**2));metric=np.vstack([J[nm:]/scaleX,np.eye(d)/scaleQ]);_,dd,Vt=svd(metric,full_matrices=False,check_finite=False);W=Vt.T/dd;A=J[:nm]@W;I=eye(d);O=csr_matrix((d,nm));mat=vstack([hstack([-csr_matrix(A),-eye(nm),csr_matrix((nm,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');rhs=np.r_[v-eps,np.zeros(2*d)];objective=np.r_[np.zeros(d),np.ones(nm),np.full(d,1e-7)];bound=trust/np.sqrt(d)
  if apex:
   zcols=[int(np.where(flat==3*i+2)[0][0]) for i in np.flatnonzero(~fixed)];extra=hstack([csr_matrix(W[zcols]),csr_matrix((len(zcols),nm+d))]);mat=vstack([mat,extra],format='csr');rhs=np.r_[rhs,1-1e-9-Q[~fixed,2]]
  lp=linprog(objective,A_ub=mat,b_ub=rhs,bounds=[(-bound,bound)]*d+[(0,None)]*(nm+d),method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
  if not lp.success:row['LP']=lp.message;trust*=.5;continue
  direction=np.zeros(Q.size);direction[flat]=W@lp.x[:d];direction=direction.reshape(Q.shape);accepted=False
  for k in range(12):
   qt=Q+direction*2**-k
   try:mt,vv,_,_=guards(qt,nP,nQ);mm=float(np.maximum(eps-vv,0).sum())
   except Exception:continue
   if mm<merit*(1-1e-5):Q=qt;accepted=True;row['alpha']=2**-k;break
  if accepted and k==0:trust=min(.15,trust*1.2)
  if not accepted:trust*=.4
  if trust<1e-9:print('SOFT_FOREST_STALLED',flush=True);break
 return Q
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--nP',type=int,default=1);ap.add_argument('--nQ',type=int,default=2);ap.add_argument('--steps',type=int,default=250);ap.add_argument('--apex',action='store_true');a=ap.parse_args();run(np.load(a.input)['Q'],a.out,a.nP,a.nQ,a.steps,a.apex)
