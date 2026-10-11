"""Finite rebuilt-hull, own-uniform-mass angular-witness/material search.
Numerical nomination only. Rational frozen bodies require exact93.py.
"""
from pathlib import Path
import os,sys,json,time,argparse
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import numpy as np,torch as T
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
T.set_default_dtype(T.float64);T.set_num_threads(1)

def mesh(z):
 h=ConvexHull(z);ids=np.sort(h.vertices);inv=np.full(len(z),-1);inv[ids]=np.arange(len(ids));f=h.simplices.copy()
 t=z[f];flip=np.einsum('ij,ij->i',np.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]),h.equations[:,:3])<0
 f[flip]=f[flip][:,[0,2,1]];return ids,inv[f]

def geom(z,ids,f):
 p=z[ids];r=p.mean(0);t=p[f]-r;v=(t[:,0]*T.linalg.cross(t[:,1],t[:,2])).sum(1)
 vol=v.sum()/6;g=r+(v[:,None]*t.sum(1)).sum(0)/(4*v.sum());P=p-g
 t=p[f];n=T.linalg.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]);Q=n/(n*(t[:,0]-g)).sum(1)[:,None]
 return P,Q,g,vol

def angular(X):
 d=X[None,:,:]-X[:,None,:];l=T.linalg.vector_norm(d,dim=2);r=T.linalg.vector_norm(X,dim=1)
 val=(X[:,None,:]*d).sum(2)/(r[:,None]*T.clamp(l,min=1e-12));val=val.masked_fill(T.eye(len(X),dtype=T.bool),-1e6)
 return val.max(1).values

def edges(f):
 e={}
 for k,face in enumerate(f):
  for i,j in zip(face,np.roll(face,-1)):e.setdefault(tuple(sorted((int(i),int(j)))),[]).append(k)
 return np.array(sorted(e),int),np.array([e[k]for k in sorted(e)],int)

def bars(X,ed):
 R=(X*X).sum(1);a=X[ed[:,0]];d=X[ed[:,1]]-a;tt=np.clip(-np.einsum('ij,ij->i',a,d)/np.einsum('ij,ij->i',d,d),0,1)
 H=((a+tt[:,None]*d)**2).sum(1);order=np.lexsort((ed[:,1],ed[:,0],-H));pa=list(range(len(X)));peak=pa[:];out=[]
 def root(i):
  while pa[i]!=i:pa[i]=pa[pa[i]];i=pa[i]
  return i
 for k in order:
  i,j=map(int,ed[k]);u,v=root(i),root(j)
  if u==v:continue
  if (R[peak[u]],peak[u])<(R[peak[v]],peak[v]):u,v=v,u
  depth=float((R[peak[v]]-H[k])/R[peak[v]])
  if depth>1e-14:out.append((depth,int(peak[v]),int(k)))
  pa[v]=u
 return sorted(out,reverse=True)

def stat(z):
 ids,f=mesh(z);P,Q,g,V=geom(T.tensor(z),ids,f);P=P.numpy();Q=Q.numpy();pe,qe=edges(f)
 m=[];roots=[]
 for X in(P,Q):
  v=X@X.T-(X*X).sum(1)[:,None];np.fill_diagonal(v,-np.inf);roots.append(np.where(v.max(1)<0)[0].tolist());m.append(v.max(1))
 pb,qb=bars(P,pe),bars(Q,qe)
 return dict(V=len(ids),E=len(pe),F=len(f),S=len(roots[1]),U=len(roots[0]),P=pb,Q=qb,g=g.numpy().tolist(),vol=float(V),Uids=[int(ids[i])for i in roots[0]],Sfaces=[ids[f[i]].tolist()for i in roots[1]]),ids,f,P,Q

def optimize(z,bound,margin,wp,wq,nit,out,mode='angular',pquota=1,qquota=1,seed=0,regularization=0.):
 out=Path(out);out.mkdir(parents=True,exist_ok=True);z0=z.copy();n=0;best=(999,999.);best121=1e9;best211=1e9;ledger=[];start=time.monotonic()
 def fun(x):
  nonlocal n,best,best121,best211
  zz=x.reshape(z.shape);ids,f=mesh(zz);v=T.tensor(zz,requires_grad=True);P,Q,g,V=geom(v,ids,f);loss=v.sum()*0;counts=[]
  for X,weight,quota in [(P,wp,pquota),(Q,wq,qquota)]:
   sc=angular(X);rr=(X*X).sum(1);allow=T.topk(rr,quota).indices if quota>0 else T.tensor([],dtype=T.int64)
   # For quota two exempt actual radial maximum and worst remaining angular root.
   if quota>1:
    al=[int(T.argmax(rr))]
    for _ in range(quota-1):
     sc2=sc.detach().clone();sc2[al]=1e6;al.append(int(T.argmin(sc2)))
    allow=T.tensor(al)
   keep=T.ones(len(X),dtype=T.bool);keep[allow]=False
   viol=T.clamp(margin-sc[keep],min=0);loss=loss+weight*(viol*viol).sum()
   counts.append(int((sc.detach()<0).sum()))
  if mode=='Pbar':
   pe,qe=edges(f);Pnp=P.detach().numpy();pb=bars(Pnp,pe)
   for dep,root,k in pb:
    i,j=pe[k];d=P[j]-P[i];t=T.clamp(-(P[i]*d).sum()/(d*d).sum(),0,1)
    lr=T.log((P[root]**2).sum()/((P[i]+t*d)**2).sum());loss+=T.clamp(lr,min=0)**.5
  loss+=regularization*((v-T.tensor(z0))**2).sum()
  if not T.isfinite(loss):raise FloatingPointError('loss')
  loss.backward();n+=1
  if n%20==1 or (counts[0]<=2 and counts[1]<=2):
   inf,*_=stat(zz);score=(counts[0]+counts[1],sum(b[0]for b in inf['P']+inf['Q']));save=[]
   if score<best:best=score;save.append('BEST')
   if inf['S']==1 and inf['U']<=2:
    dep=sum(b[0]for b in inf['P'])
    if dep<best121:best121=dep;save.append('BEST121')
   if inf['U']==1 and inf['S']<=2:
    dep=sum(b[0]for b in inf['Q'])
    if dep<best211:best211=dep;save.append('BEST211')
   if save:
    for label in save:(out/(label+'.json')).write_text(json.dumps(zz.tolist(),separators=(',',':'))+'\n')
    rec=dict(calls=n,loss=float(loss.detach()),seconds=time.monotonic()-start,labels=save,**inf);ledger.append(rec);print(out.name,json.dumps(rec),flush=True);(out/'LEDGER.json').write_text(json.dumps(ledger,separators=(',',':'))+'\n')
  return float(loss.detach()),v.grad.numpy().ravel()
 r=minimize(fun,z.ravel(),jac=True,method='L-BFGS-B',bounds=list(zip((z0-bound).ravel(),(z0+bound).ravel())),options={'maxiter':nit,'ftol':1e-14,'gtol':1e-10,'maxls':30,'maxcor':20})
 zz=r.x.reshape(z.shape);(out/'FINAL.json').write_text(json.dumps(zz.tolist(),separators=(',',':'))+'\n');inf=stat(zz)[0]
 rec=dict(status=int(r.status),message=str(r.message),iterations=int(r.nit),calls=n,parameters=dict(bound=bound,margin=margin,wp=wp,wq=wq,nit=nit,mode=mode,pquota=pquota,qquota=qquota,seed=seed,regularization=regularization),**inf);(out/'RUN.json').write_text(json.dumps(rec,separators=(',',':'))+'\n');print('RUN_DONE',out,rec,flush=True);return zz

def main():
 a=argparse.ArgumentParser();a.add_argument('input');a.add_argument('out');a.add_argument('--bound',type=float,default=.4);a.add_argument('--margin',type=float,default=1e-4);a.add_argument('--wp',type=float,default=1.);a.add_argument('--wq',type=float,default=1.);a.add_argument('--nit',type=int,default=300);a.add_argument('--mode',default='angular');a.add_argument('--pquota',type=int,default=1);a.add_argument('--qquota',type=int,default=1);a.add_argument('--seed',type=int,default=0);a.add_argument('--regularization',type=float,default=0.);args=a.parse_args();z=np.array(json.loads(Path(args.input).read_text()),float);optimize(z,**{k:v for k,v in vars(args).items()if k!='input'})
if __name__=='__main__':main()
