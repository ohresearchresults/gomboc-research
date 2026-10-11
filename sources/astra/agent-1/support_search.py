"""Own-mass support continuation with complete-graph escape forests.
Floating exploration only. The stored Q rows define physical halfspaces Q_i.x<=1.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,torch,json,pathlib,time,argparse
from scipy.optimize import least_squares
from geometry import halfspace_mesh,census,routes,arrows

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def repair(Q,out,steps=100,seed=0,goal=2e-6,apex=True,qroots=1):
 out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);rng=np.random.default_rng(seed)
 fixed=np.isclose(Q[:,2],1,atol=1e-12,rtol=0) if apex else np.zeros(len(Q),bool)
 mask=np.ones(Q.shape,bool);mask[fixed,2]=False
 flat=np.flatnonzero(mask.ravel());selector=torch.eye(Q.size)[flat].T
 hist=[];trust=.05;best=np.inf;t0=time.time()
 for it in range(steps):
  try:m=halfspace_mesh(Q)
  except (ValueError,np.linalg.LinAlgError) as e:print('STOP',e,flush=True);break
  X=m['X']-m['g'];R=Q/(1-Q@m['g'])[:,None]
  u=int(np.argmax(np.linalg.norm(X,axis=1)));s=int(np.argmax(np.linalg.norm(R,axis=1)))
  if qroots==2:
   from persistence_search import pairs,polar_edges
   epq=polar_edges(m);pairq,hq=pairs(R,epq,m['active']);rad=(R*R).sum(1)
   if len(pairq):
    depth=1-hq[pairq[:,1]]/rad[pairq[:,0]];s=[s,int(pairq[np.argmax(depth),0])]
  ip,jp=routes(X,u,power=1 if it%7==6 else 2);iq,jq=routes(R,s,power=1 if it%7==6 else 2)
  st=census(m);wp=arrows(X).max(1);wq=arrows(R).max(1);violation=float(np.linalg.norm(np.minimum(np.delete(wp,u)-goal,0))+np.linalg.norm(np.minimum(np.delete(wq,s)-goal,0)))
  row=dict(it=it,violation=violation,trust=trust,seconds=time.time()-t0,**st);hist.append(row)
  if it%5==0:print(json.dumps(row),flush=True)
  np.savez(out/'latest.npz',Q=Q);(out/'history.json').write_text(json.dumps(hist,indent=2))
  if violation<best:best=violation;np.savez(out/'best.npz',Q=Q);(out/'best.json').write_text(json.dumps(row,indent=2))
  if st['S']==qroots and st['U']==1 and st['min_primal_nonroot']>1e-9:
   np.savez(out/('NOMINATION_S'+str(qroots)+'_U1.npz'),Q=Q);print('NOMINATION_REQUIRES_EXACT_AUDIT',qroots,flush=True);return Q
  q0=torch.tensor(Q);ti=torch.tensor(m['triples']);tt=torch.tensor(m['triangles']);base=torch.zeros(len(flat))
  nonowner=(1-Q@m['X'].T)>1e-8
  ci,cj=np.where(nonowner & ((1-Q@m['X'].T)<.12))
  ci=torch.tensor(ci);cj=torch.tensor(cj)
  ip,jp,iq,jq=map(torch.tensor,(ip,jp,iq,jq))
  def calc(z):
   q=q0+(selector@z).reshape(q0.shape)
   x=torch.linalg.solve(q[ti],torch.ones((len(ti),3,1)))[:,:,0]
   v=torch.sum(x[tt[:,0]]*torch.linalg.cross(x[tt[:,1]],x[tt[:,2]]),dim=1)/6
   g=torch.sum(v[:,None]*x[tt].sum(1),dim=0)/(4*v.sum())
   p=x-g;r=q/(1-q@g)[:,None]
   def esc(p,i,j):
    d=p[j]-p[i]
    return (p[i]*d).sum(1)/(torch.linalg.vector_norm(p[i],dim=1)*torch.linalg.vector_norm(d,dim=1)).clamp(min=1e-15)
   ep=esc(p,ip,jp);eq=esc(r,iq,jq)
   sl=1-(q[ci]*x[cj]).sum(1)
   return torch.cat([torch.clamp(goal-ep,min=0),torch.clamp(goal-eq,min=0),10*torch.clamp(1e-8-sl,min=0),10*torch.clamp(1e-12-v,min=0),.001*z])
  cache={}
  def evaluate(z):
   if cache.get('z') is None or not np.array_equal(cache['z'],z):
    zz=torch.tensor(z);cache['z']=z.copy();cache['f']=calc(zz).detach().numpy();cache['j']=torch.func.jacrev(calc)(zz).detach().numpy()
   return cache['f'],cache['j']
  f0=evaluate(np.zeros(len(flat)))[0];loss0=np.linalg.norm(f0)
  res=least_squares(lambda z:evaluate(z)[0],np.zeros(len(flat)),jac=lambda z:evaluate(z)[1],bounds=(-trust,trust),max_nfev=9,ftol=None,xtol=1e-7,gtol=1e-9)
  dz=(selector@torch.tensor(res.x)).numpy().reshape(Q.shape)
  accepted=False
  for k in range(13):
   trial=Q+dz*2**-k
   try:
    mm=halfspace_mesh(trial);pp=mm['X']-mm['g'];rr=trial/(1-trial@mm['g'])[:,None]
    aa=arrows(pp).max(1);bb=arrows(rr).max(1)
    vp=np.delete(aa,np.argmax(np.linalg.norm(pp,axis=1)));vq=np.sort(bb)[qroots:]
    new=float(np.linalg.norm(np.minimum(vp-goal,0))+np.linalg.norm(np.minimum(vq-goal,0)))
   except Exception:continue
   # Actual rebuilt hull objective, independent of stale topology.
   if np.linalg.norm(calc(torch.tensor(res.x*2**-k)).detach().numpy()) < loss0*(1-1e-5*2**-k) and new<max(violation*1.5,violation+.03):
    Q=trial;accepted=True;trust=min(.12,trust*1.13);break
  row['accepted']=accepted;row['halvings']=k;row['step_norm']=float(np.linalg.norm(dz))
  if not accepted:
   trust*=.5
   if trust<1e-7:print('STALLED',flush=True);break
 return Q

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--seed',type=int,default=0);ap.add_argument('--steps',type=int,default=100);ap.add_argument('--count',type=int,default=85);ap.add_argument('--input');ap.add_argument('--out',required=True);ap.add_argument('--free-apex',action='store_true');ap.add_argument('--qroots',type=int,default=1);a=ap.parse_args()
 if a.input:Q=np.load(a.input)['Q']
 else:
  Q=np.load('artifacts/baseline/float.npz')['H'];rng=np.random.default_rng(a.seed)
  apex=np.flatnonzero(abs(Q[:,2]-1)<1e-12);keep=list(set(apex.tolist()+[3]));rest=list(set(range(len(Q)))-set(keep))
  # Retain the high-degree apex and spread the remaining supports geometrically.
  while len(keep)<a.count:
   norms=Q/np.linalg.norm(Q,axis=1)[:,None];scores=np.min(np.linalg.norm(norms[rest,None]-norms[None,keep],axis=2),axis=1)
   scores*=rng.uniform(.8,1.2,len(rest));j=rest.pop(int(np.argmax(scores)));keep.append(j)
  Q=Q[sorted(keep)]
  p=pathlib.Path(a.out);p.mkdir(parents=True,exist_ok=True);(p/'selected.json').write_text(json.dumps(sorted(keep)))
 repair(Q,a.out,a.steps,a.seed,apex=not a.free_apex,qroots=a.qroots)
if __name__=='__main__':main()
