"""Own-centroid radial-persistence optimization of physical support bodies.
Exact endpoints require audit_exact.py; floating persistence has no proof status.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,torch,json,pathlib,time,argparse
from scipy.optimize import minimize
from geometry import halfspace_mesh,census

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def pairs(X,edges,active=None):
 active=range(len(X)) if active is None else active
 r=(X*X).sum(1);edges=np.array(edges,dtype=int)
 a=X[edges[:,0]];d=X[edges[:,1]]-a;dd=(d*d).sum(1)
 t=np.clip(-(a*d).sum(1)/np.maximum(dd,1e-300),0,1)
 h=np.sum((a+t[:,None]*d)**2,axis=1)
 h=np.minimum(h,np.minimum(r[edges[:,0]],r[edges[:,1]]))
 parent=np.arange(len(X));elder=np.arange(len(X));out=[]
 def root(i):
  while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
  return i
 # At each edge's lower endpoint or interior minimum its components merge.
 for k in np.argsort(-h,kind='stable'):
  i,j=map(int,edges[k]);u,v=root(i),root(j)
  if u==v:continue
  if r[elder[u]]<r[elder[v]]:u,v=v,u
  b=int(elder[v]);parent[v]=u
  if r[b]-h[k]>1e-15:out.append((b,int(k)))
 return np.array(out,dtype=int).reshape(-1,2),h

def polar_edges(m):
 incident={}
 for f,cy in zip(m['active'],m['faces']):
  for i,j in zip(cy,cy[1:]+cy[:1]):incident.setdefault(tuple(sorted((i,j))),[]).append(int(f))
 assert all(len(v)==2 for v in incident.values())
 return np.array(sorted(set(tuple(sorted(v)) for v in incident.values())),dtype=int)

def search(Q,out,iters=500,apex=True,kind='linear',seed=0,eta=.001):
 out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);rng=np.random.default_rng(seed)
 fixed=np.isclose(Q[:,2],1,atol=1e-12,rtol=0) if apex else np.zeros(len(Q),bool)
 mask=np.ones(Q.shape,bool);mask[fixed,2]=False;flat=np.flatnonzero(mask.ravel())
 base=Q.copy();p0=Q.ravel()[flat];best=np.inf;hist=[];t0=time.time();calls=0
 def evaluate(z):
  nonlocal calls,best
  calls+=1;q=base.copy();q.ravel()[flat]=z
  try:m=halfspace_mesh(q)
  except Exception as e:raise RuntimeError('invalid physical support body during search') from e
  ep=m['edges'];eq=polar_edges(m);pn=m['X']-m['g'];qn=q/(1-q@m['g'])[:,None]
  pp,hp=pairs(pn,ep);pq,hq=pairs(qn,eq,m['active'])
  zz=torch.tensor(z,requires_grad=True);qt=torch.tensor(base).flatten().scatter(0,torch.tensor(flat),zz).reshape(base.shape)
  ti=torch.tensor(m['triples']);tt=torch.tensor(m['triangles']);x=torch.linalg.solve(qt[ti],torch.ones((len(ti),3,1)))[:,:,0]
  v=(x[tt[:,0]]*torch.linalg.cross(x[tt[:,1]],x[tt[:,2]])).sum(1)/6
  g=(v[:,None]*x[tt].sum(1)).sum(0)/(4*v.sum());p=x-g;r=qt/(1-qt@g)[:,None]
  def barloss(x,edges,pair):
   if len(pair)==0:return x.sum()*0,[]
   bi=torch.tensor(pair[:,0]);ee=torch.tensor(edges[pair[:,1]]);a=x[ee[:,0]];d=x[ee[:,1]]-a
   t=(-(a*d).sum(1)/(d*d).sum(1).clamp(min=1e-30)).clamp(0,1);dead=((a+t[:,None]*d)**2).sum(1);born=(x[bi]**2).sum(1)
   bars=(1-dead/born).clamp(min=0)
   if kind=='linear':loss=bars.sum()
   elif kind=='square':loss=(bars**2).sum()
   elif kind=='log':loss=torch.log1p(bars/eta).sum()*eta
   elif kind=='sqrt':loss=(torch.sqrt(bars+1e-9)-np.sqrt(1e-9)).sum()
   return loss,bars.detach().numpy().tolist()
  lp,bp=barloss(p,ep,pp);lq,bq=barloss(r,eq,pq);loss=lp+lq
  grad=torch.autograd.grad(loss,zz)[0].detach().numpy();val=float(loss.detach())
  row={'eval':calls,'loss':val,'P':len(bp),'Q':len(bq),'Pmax':max(bp,default=0),'Qmax':max(bq,default=0),'seconds':time.time()-t0,**census(m)}
  if calls%20==1:print(json.dumps(row),flush=True)
  if val<best:
   best=val;np.savez(out/'best.npz',Q=q);(out/'best.json').write_text(json.dumps(row,indent=2))
  if calls%10==0:hist.append(row);(out/'history.json').write_text(json.dumps(hist,indent=2))
  if row['S']==row['U']==1 and row['min_primal_nonroot']>1e-10 and row['min_polar_nonroot']>1e-10:
   np.savez(out/'NOMINATION.npz',Q=q);print('NOMINATION_REQUIRES_EXACT',flush=True)
  return val,grad
 result=minimize(evaluate,p0,jac=True,method='L-BFGS-B',bounds=[(x-.8,x+.8) for x in p0],options={'maxiter':iters,'ftol':1e-14,'gtol':1e-10,'maxls':30,'maxcor':20})
 final=base.copy();final.ravel()[flat]=result.x;np.savez(out/'final.npz',Q=final);(out/'result.json').write_text(json.dumps({'message':str(result.message),'nfev':result.nfev,'nit':result.nit,'fun':float(result.fun)}));print('END',result.message,result.fun,flush=True)
 return final

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--iters',type=int,default=500);ap.add_argument('--kind',default='linear');ap.add_argument('--free-apex',action='store_true');a=ap.parse_args();q=np.load(a.input)['Q'];search(q,a.out,a.iters,not a.free_apex,a.kind)
