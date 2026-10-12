"""Full-support own-mass flow inside an open strict211 region, numerical only.
Every proposed step rebuilds the actual hull and checks both complete chord landscapes.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,torch,json,pathlib,time,argparse
from scipy.optimize import linprog
from geometry import halfspace_mesh,census,arrows
from persistence_search import pairs,polar_edges

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
def state(Q):
 m=halfspace_mesh(Q);p=m['X']-m['g'];q=Q/(1-Q@m['g'])[:,None]
 Wp=arrows(p);Wq=arrows(q);U=np.flatnonzero(Wp.max(1)<0);S=np.flatnonzero(Wq.max(1)<0)
 pq,h=pairs(q,polar_edges(m),m['active'])
 if len(pq):
  dep=1-h[pq[:,1]]/(q[pq[:,0]]**2).sum(1);k=np.argmax(dep);depth=float(dep[k]);birth=int(pq[k,0]);edge=polar_edges(m)[pq[k,1]]
 else:depth=0;birth=0;edge=np.array([0,1])
 return m,p,q,Wp,Wq,U,S,depth,birth,edge

def flow(Q,out,steps=500,seed=0):
 out=pathlib.Path(out);out.mkdir(exist_ok=True,parents=True);hist=[];trust=.003;t0=time.time()
 for it in range(steps):
  m,p,q,wp,wq,U,S,depth,birth,edge=state(Q)
  row=dict(it=it,depth=depth,trust=trust,seconds=time.time()-t0,**census(m));hist.append(row)
  if it%5==0:print(json.dumps(row),flush=True)
  (out/'history.json').write_text(json.dumps(hist,indent=2));np.savez(out/'latest.npz',Q=Q)
  if len(U)==len(S)==1:np.savez(out/'NOMINATION110.npz',Q=Q);print('NUMERICAL110_REQUIRES_EXACT',flush=True);break
  if len(U)!=1 or len(S)!=2:raise ValueError(('not strict211 start',len(U),len(S)))
  ip=np.delete(np.arange(len(p)),U);jp=wp.argmax(1)[ip];iq=np.delete(np.arange(len(q)),S);jq=wq.argmax(1)[iq]
  ti=torch.tensor(m['triples']);tt=torch.tensor(m['triangles']);q0=torch.tensor(Q)
  ip,jp,iq,jq=map(torch.tensor,(ip,jp,iq,jq))
  def values(z):
   qt=z.reshape(Q.shape);x=torch.linalg.solve(qt[ti],torch.ones((len(ti),3,1)))[:,:,0]
   v=(x[tt[:,0]]*torch.linalg.cross(x[tt[:,1]],x[tt[:,2]])).sum(1)/6;g=(v[:,None]*x[tt].sum(1)).sum(0)/(4*v.sum())
   pp=x-g;qq=qt/(1-qt@g)[:,None]
   def esc(a,i,j):
    d=a[j]-a[i];return (a[i]*d).sum(1)/(torch.linalg.vector_norm(a[i],dim=1)*torch.linalg.vector_norm(d,dim=1)).clamp(min=1e-15)
   a=qq[edge[0]];d=qq[edge[1]]-a;t=(-(a*d).sum()/(d*d).sum()).clamp(0,1)
   dep=1-((a+t*d)**2).sum()/(qq[birth]**2).sum()
   return torch.cat([esc(pp,ip,jp),esc(qq,iq,jq),dep.reshape(1)])
  z=q0.flatten();vals=values(z).detach().numpy();J=torch.func.jacrev(values)(z).detach().numpy();v=vals[:-1];jac=J[:-1];c=J[-1]
  floor=np.minimum(1e-7,v*.2)
  result=linprog(c,A_ub=-jac,b_ub=v-floor,bounds=[(-trust,trust)]*Q.size,method='highs',options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
  if not result.success:
   row['LP']=result.message;trust*=.5
   if trust<1e-8:break
   continue
  predicted=float(c@result.x);row['predicted']=predicted
  accepted=False
  for k in range(30):
   qt=Q+result.x.reshape(Q.shape)*2**-k
   try:mm,pp,qq,wwp,wwq,uu,ss,d,bb,ee=state(qt)
   except Exception:continue
   if len(uu)==1 and len(ss)<=2 and d<depth-1e-12 and np.sort(wwp.max(1))[1]>1e-9 and np.sort(wwq.max(1))[len(ss)]>1e-9:
    Q=qt;accepted=True;trust=min(.02,max(1e-7,trust*(1.4 if k==0 else max(.1,2**(-k/2)))));break
  row['accepted']=accepted;row['halvings']=k
  if not accepted:
   trust*=.5
   if trust<1e-8:print('STRICT_REGION_STALLED',flush=True);break
 return Q
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--steps',type=int,default=500);a=ap.parse_args();flow(np.load(a.input)['Q'],a.out,a.steps)
