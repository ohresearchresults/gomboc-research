"""Physical polar/halfspace chart: at most 85 supporting planes gives E<=249.
The parameter origin is an interior reference only. The OWN filled centroid is
reintegrated at every trial, and the centered polar is q/(1-q.g).
Nomination, never an exact acceptance certificate.
"""
from pathlib import Path
from itertools import combinations
import os,json,sys,argparse,time
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import numpy as np,torch as T
from scipy.spatial import ConvexHull,HalfspaceIntersection
from scipy.optimize import minimize
from search93 import mesh,angular,bars,edges
T.set_default_dtype(T.float64);T.set_num_threads(1)

def chart(q):
 hs=HalfspaceIntersection(np.c_[q,-np.ones(len(q))],np.zeros(3));p=hs.intersections
 tri=[]
 for ls in hs.dual_facets:
  abc=max(combinations(ls,3),key=lambda t:abs(np.linalg.det(q[list(t)])))
  tri.append(abc)
 ids,f=mesh(p);assert len(ids)==len(p)
 return np.array(tri,int),f,np.array(sorted(set(i for ls in hs.dual_facets for i in ls)),int),p

def geometry(q,tr,f,active):
 p=T.linalg.solve(q[tr],T.ones((len(tr),3,1))).squeeze(2)
 r=p.mean(0);a=p[f]-r;v=(a[:,0]*T.linalg.cross(a[:,1],a[:,2])).sum(1)
 V=v.sum()/6;g=r+(v[:,None]*a.sum(1)).sum(0)/(4*v.sum());P=p-g;Q=q[active]/(1-(q[active]*g).sum(1))[:,None]
 return P,Q,g,V,p

def state(q,graphs=False):
 tr,f,active,p=chart(q);P,Q,g,V,_=geometry(T.tensor(q),tr,f,active);P=P.numpy();Q=Q.numpy();g=g.numpy()
 root=[]
 for X in(P,Q):
  scores=X@X.T-(X*X).sum(1)[:,None];np.fill_diagonal(scores,-np.inf);root.append(np.where(scores.max(1)<0)[0].tolist())
 # Physical edges come from shared pairs of active supports, not triangulation diagonals.
 hs=HalfspaceIntersection(np.c_[q,-np.ones(len(q))],np.zeros(3));inc=list(map(set,hs.dual_facets));pe=[];qe=[];mp={int(k):i for i,k in enumerate(active)}
 for i,j in combinations(range(len(p)),2):
  common=inc[i]&inc[j]
  if len(common)>=2:
   ls=sorted(common);pe.append([i,j]);qe.append([mp[ls[0]],mp[ls[1]]])
 pe=np.array(pe,int);qe=np.array(qe,int);pb=bars(P,pe);qb=bars(Q,qe)
 result=(dict(V=len(p),E=len(pe),F=len(active),S=len(root[1]),U=len(root[0]),P=pb,Q=qb,g=g.tolist(),vol=float(V),Uids=root[0],Sids=[int(active[i])for i in root[1]]), (tr,f,active), (P,Q))
 return (*result,(pe,qe)) if graphs else result

def freeze(q,out,name='NOMINEE'):
 out=Path(out);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(q.tolist(),separators=(',',':'))+'\n')

def scan(source,out):
 Q=np.array(json.loads(Path(source).read_text()),float);out=Path(out);out.mkdir(parents=True,exist_ok=True);records=[]
 for i in range(len(Q)):
  q=np.delete(Q,i,axis=0)
  try:s,_,_=state(q)
  except Exception as e:records.append(dict(drop=i,error=repr(e)));continue
  records.append(dict(drop=i,**s));freeze(q,out/f'DROP{i}.json')
  if s['S']<=2 and s['U']<=2:print('DROP',i,s,flush=True)
 (out/'SCAN.json').write_text(json.dumps(records,separators=(',',':'))+'\n')
 print('DROP_SCAN_DONE',len(records),flush=True)

def optimize(source,out,steps=500,bound=.3,wp=1.,wq=1.,margin=1e-4,mode='offset',pquota=1,qquota=1,barweight=0.,seed=0):
 q0=np.array(json.loads(Path(source).read_text()),float);out=Path(out);out.mkdir(parents=True,exist_ok=True);n=0;best=(999,999.);best121=999.;best211=999.;ledger=[];t0=time.monotonic()
 x0=np.zeros(len(q0)) if mode=='offset' else q0.ravel()
 def toq(x):return T.tensor(q0)*T.exp(x[:,None]) if mode=='offset' else x.reshape(q0.shape)
 def fun(xx):
  nonlocal n,best,best121,best211
  x=T.tensor(xx,requires_grad=True);q=toq(x);qnp=q.detach().numpy();tr,f,active,_=chart(qnp);P,Q,g,V,p=geometry(q,tr,f,active);loss=x.sum()*0;counts=[]
  for X,w,quota in [(P,wp,pquota),(Q,wq,qquota)]:
   sc=angular(X);r=(X*X).sum(1);allow=[int(T.argmax(r).detach())]
   candidates=bars(P.detach().numpy(),edges(f)[0]) if X is P else []
   for k in range(quota-1):
    if k<len(candidates):allow.append(int(candidates[k][1]))
    else:
     m=sc.detach().clone();m[allow]=1e6;allow.append(int(T.argmin(m)))
   keep=T.ones(len(X),dtype=T.bool);keep[allow]=False;loss+=w*(T.clamp(margin-sc[keep],min=0)**2).sum();counts.append(int((sc.detach()<0).sum()))
  if barweight:
   pe,_=edges(f)
   for dep,root,k in bars(P.detach().numpy(),pe):
    i,j=pe[k];d=P[j]-P[i];t=T.clamp(-(P[i]*d).sum()/(d*d).sum(),0,1);lr=T.log((P[root]**2).sum()/((P[i]+t*d)**2).sum());loss+=barweight*T.clamp(lr,min=0)**.5
  if not T.isfinite(loss):raise FloatingPointError('loss')
  loss.backward();n+=1
  if (counts[0]<=2 and counts[1]<=2) or n%30==1:
   s,_,_=state(qnp);score=(s['U']+s['S'],sum(v[0]for v in s['P']+s['Q']));save=[]
   if score<best:best=score;save.append('BEST')
   if s['S']==1 and s['U']<=2:
    dd=sum(v[0]for v in s['P'])
    if dd<best121:best121=dd;save.append('BEST121')
   if s['U']==1 and s['S']<=2:
    dd=sum(v[0]for v in s['Q'])
    if dd<best211:best211=dd;save.append('BEST211')
   if save:
    for label in save:freeze(qnp,out/(label+'.json'))
    rec=dict(calls=n,loss=float(loss.detach()),labels=save,seconds=time.monotonic()-t0,**s);ledger.append(rec);(out/'LEDGER.json').write_text(json.dumps(ledger,separators=(',',':'))+'\n');print('H_BEST',out.name,json.dumps(rec),flush=True)
  return float(loss.detach()),x.grad.numpy()
 r=minimize(fun,x0,jac=True,method='L-BFGS-B',bounds=list(zip(x0-bound,x0+bound)),options={'maxiter':steps,'ftol':1e-14,'gtol':1e-10,'maxls':30,'maxcor':25})
 q=toq(T.tensor(r.x)).numpy();freeze(q,out/'FINAL.json');s,_,_=state(q)
 rec=dict(status=int(r.status),message=str(r.message),iterations=int(r.nit),calls=n,parameters=dict(source=source,steps=steps,bound=bound,wp=wp,wq=wq,margin=margin,mode=mode,pquota=pquota,qquota=qquota,barweight=barweight,seed=seed),**s);(out/'RUN.json').write_text(json.dumps(rec,separators=(',',':'))+'\n');print('H_DONE',out.name,rec,flush=True)
 return q
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('source');a.add_argument('out');a.add_argument('--scan',action='store_true');a.add_argument('--steps',type=int,default=500);a.add_argument('--bound',type=float,default=.3);a.add_argument('--wp',type=float,default=1.);a.add_argument('--wq',type=float,default=1.);a.add_argument('--margin',type=float,default=1e-4);a.add_argument('--mode',default='offset');a.add_argument('--pquota',type=int,default=1);a.add_argument('--qquota',type=int,default=1);a.add_argument('--barweight',type=float,default=0.);a.add_argument('--seed',type=int,default=0);p=a.parse_args()
 if p.scan:scan(p.source,p.out)
 else:optimize(**{k:v for k,v in vars(p).items()if k!='scan'})
