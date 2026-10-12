"""N40 complete numerical nomination units. Only N40_RECOVER certifies geometry.
Run phases in order: first q_a q_b q_c robust simplify_a simplify_b simplify_c.
Negative scans are optional; floating solver trajectories are not certificates.
Executed: Python3.13.5, NumPy2.3.5, SciPy1.17.0, torch2.10.0+cpu.
"""
import os,sys,types,argparse,json,hashlib
from pathlib import Path
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import N40_RECOVER as exact
import numpy as np
from fractions import Fraction as F
UNITS={}
UNITS['explore40'] = r'''"""Numerical nomination only: dynamic-hull live-centroid coupled hinge deformation."""
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import differential_evolution, minimize
import json,sys,time
import J75_REFERENCE110_CAP233 as g
P0=np.array(g.points(),float)

def geom(P):
    H=ConvexHull(P)
    T=P[H.simplices];o=P[H.vertices].mean(0)
    vol=np.abs(np.einsum('ij,ij->i',T[:,0]-o,np.cross(T[:,1]-o,T[:,2]-o)))/6
    V=vol.sum();c=(vol[:,None]*(T.sum(1)+o)/4).sum(0)/V
    # nomination merge only; exact auditor does not use this tolerance
    normals=H.equations[:,:3];hh=-H.equations[:,3]-normals@c
    polar=normals/hh[:,None]
    keys=np.round(polar,10)
    _,first,group=np.unique(keys,axis=0,return_index=True,return_inverse=True)
    Q=polar[first];edges=set();dual=set()
    for i in range(len(H.simplices)):
      for k,j in enumerate(H.neighbors[i]):
        if i>=j or group[i]==group[j]:continue
        a,b=sorted(set(H.simplices[i])&set(H.simplices[j]));edges.add((int(a),int(b)));dual.add(tuple(sorted((int(group[i]),int(group[j])))))
    ids=sorted(H.vertices);mp={a:i for i,a in enumerate(ids)}
    ep=np.array([(mp[a],mp[b]) for a,b in sorted(edges)],int)
    eq=np.array(sorted(dual),int)
    return P[ids]-c,Q,ep,eq,c,V,ids

def bars(X,E):
    r=np.einsum('ij,ij->i',X,X);u=X[E[:,0]];v=X[E[:,1]];d=v-u
    dd=(d*d).sum(1);a=(u*d).sum(1);t=np.clip(-a/dd,0,1)
    z=u+t[:,None]*d;w=(z*z).sum(1)
    par=np.arange(len(X));peak=par.copy();out=[]
    def root(i):
      while par[i]!=i:par[i]=par[par[i]];i=par[i]
      return i
    for k in np.argsort(-w,kind='stable'):
      i,j=E[k];a,b=root(i),root(j)
      if a==b:continue
      if r[peak[a]]<r[peak[b]]:a,b=b,a
      dep=max(0.,1-w[k]/r[peak[b]])
      if dep>0:out.append((dep,int(peak[b]),int(peak[a]),int(k)))
      par[b]=a
    return sorted(out,reverse=True)

def metrics(P,detail=False):
    try:X,Q,E,D,c,V,ids=geom(P)
    except Exception:return (100.,None) if detail else 100.
    pb=bars(X,E);qb=bars(Q,D)
    # All floating positive depths are retained in loss. Exactness is checked separately.
    ap=np.array([a[0] for a in pb]);aq=np.array([a[0] for a in qb])
    cost=ap.sum()+aq.sum()
    if detail:return cost,dict(P=pb,Q=qb,V=V,c=c,vef=(len(X),len(E),len(Q)),ids=ids)
    return cost

'''
UNITS['descent40'] = r'''"""All-vertex coupled numerical descent. Every evaluation re-hulls and integrates real mass.
Only rational replay, not these floating thresholds or solver termination, certifies an endpoint.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import numpy as np, torch, json,sys,time
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
from itertools import combinations
import J75_REFERENCE110_CAP233 as g
from explore40 import bars

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
P0=np.array(g.points(),float);PATCH=list(g.PATCH);REST=[i for i in range(75) if i not in PATCH]

def topology(P):
 H=ConvexHull(P);T=H.simplices.copy();N=H.equations[:,:3]
 wrong=np.einsum('ij,ij->i',np.cross(P[T[:,1]]-P[T[:,0]],P[T[:,2]]-P[T[:,0]]),N)<0
 T[wrong]=T[wrong][:,[0,2,1]]
 o=P[H.vertices].mean(0);tris=P[T]
 v=np.einsum('ij,ij->i',tris[:,0]-o,np.cross(tris[:,1]-o,tris[:,2]-o))/6
 c=(v[:,None]*(tris.sum(1)+o)/4).sum(0)/v.sum()
 q=N/(-H.equations[:,3]-N@c)[:,None]
 par=list(range(len(T)))
 def rt(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 for i in range(len(T)):
  for j in H.neighbors[i]:
   if i<j and np.linalg.norm(q[i]-q[j])<1e-8:par[rt(j)]=rt(i)
 group=np.array([rt(i) for i in range(len(T))]);_,group=np.unique(group,return_inverse=True)
 ftri=[];groups=[]
 for k in range(group.max()+1):
  a=np.where(group==k)[0];vid=sorted(set(T[a].flatten()));groups.append(vid)
  # Wide triple avoids ill-conditioned sliver normals.
  i=vid[0];j=max(vid,key=lambda j:np.linalg.norm(P[j]-P[i]));kk=max(vid,key=lambda k:np.linalg.norm(np.cross(P[j]-P[i],P[k]-P[i])))
  ft=[i,j,kk]
  if np.dot(np.cross(P[j]-P[i],P[kk]-P[i]),N[a[0]])<0:ft=[i,kk,j]
  ftri.append(ft)
 E=set();D=set()
 for i in range(len(T)):
  for j in H.neighbors[i]:
   if i<j and group[i]!=group[j]:
    E.add(tuple(sorted(set(T[i])&set(T[j]))));D.add(tuple(sorted((int(group[i]),int(group[j])))))
 E=np.array(sorted(E),int);D=np.array(sorted(D),int);ft=np.array(ftri,int)
 nx=np.cross(P[ft[:,1]]-P[ft[:,0]],P[ft[:,2]]-P[ft[:,0]])
 Q=nx/np.einsum('ij,ij->i',nx,P[ft[:,0]]-c)[:,None]
 return T,ft,E,D,c,Q,groups,H.vertices

def unpack(x,patch):
 if not patch:return x.reshape(75,3)
 if isinstance(x,torch.Tensor):P=torch.zeros((75,3),dtype=x.dtype);v=x[:36].reshape(18,2)
 else:P=np.zeros((75,3));v=x[:36].reshape(18,2)
 P[PATCH,0]=v[:,0];P[PATCH,2]=v[:,1];P[PATCH,1]=x[-3]*v[:,0]+x[-2]*v[:,1]+x[-1]
 P[REST]=x[36:-3].reshape(57,3)
 return P

def pack(P,patch):
 if not patch:return P.flatten()
 a=np.linalg.lstsq(np.c_[P[PATCH,0],P[PATCH,2],np.ones(18)],P[PATCH,1],rcond=None)[0]
 return np.r_[P[PATCH][:,[0,2]].flatten(),P[REST].flatten(),a]

def state(P):
 T,F,E,D,c,Q,groups,ids=topology(P);X=P-c
 bp=bars(X,E);bq=bars(Q,D)
 return bp,bq,(T,F,E,D,c,Q,groups,ids)

def tradius(X):return (X*X).sum(1)
def tgate(X,E):
 u=X[E[:,0]];d=X[E[:,1]]-u;dd=(d*d).sum(1);t=torch.clamp(-(u*d).sum(1)/dd,0.,1.);r=u+t[:,None]*d
 return (r*r).sum(1)

def widest(X,E):
 import heapq
 r=np.linalg.norm(X,axis=1);root=int(np.argmax(r));adj=[[] for _ in X]
 for i,j in E:
  d=X[j]-X[i];l=np.linalg.norm(d)
  adj[j].append((int(i),float(np.dot(X[i],d)/(r[i]*l))))
  adj[i].append((int(j),float(np.dot(X[j],-d)/(r[j]*l))))
 best=np.full(len(X),-np.inf);best[root]=np.inf;crit=[None]*len(X);heap=[(-np.inf,root)]
 while heap:
  neg,j=heapq.heappop(heap)
  if -neg<best[j]:continue
  for i,s in adj[j]:
   z=min(best[j],s)
   if z>best[i]:
    best[i]=z;crit[i]=(i,j) if s<best[j] else crit[j];heapq.heappush(heap,(-z,i))
 arcs=[crit[i] for i in range(len(X)) if i!=root and crit[i] is not None]
 return np.array(arcs,dtype=int),best,root

class Objective:
 def __init__(self,patch=True,power=1.,weights=(1.,1.),mode='bars',rootp=None,rootq=None):
  self.patch=patch;self.power=power;self.weights=weights;self.mode=mode;self.calls=0;self.best=1e9;self.saved=None;self.rootp=rootp;self.rootq=rootq
 def __call__(self,x):
  self.calls+=1
  P=unpack(x,self.patch)
  try:bp,bq,(T,F,E,D,c,Q,groups,ids)=state(P)
  except Exception:return 1e4,np.zeros_like(x)
  t=torch.tensor(x,requires_grad=True);Y=unpack(t,self.patch);a,b,d=Y[T[:,0]],Y[T[:,1]],Y[T[:,2]]
  o=Y.mean(0);v=((a-o)*torch.linalg.cross(b-o,d-o,dim=1)).sum(1)/6
  cc=(v[:,None]*(a+b+d+o)/4).sum(0)/v.sum()
  X=Y-cc;n=torch.linalg.cross(Y[F[:,1]]-Y[F[:,0]],Y[F[:,2]]-Y[F[:,0]],dim=1)
  QQ=n/(n*X[F[:,0]]).sum(1)[:,None]
  loss=t.sum()*0
  for coeff,vec,edges,bb in zip(self.weights,[X,QQ],[E,D],[bp,bq]):
   if self.mode=='widest':
    arcs,_,_=widest(vec.detach().numpy(),edges)
    if not len(arcs):continue
    u=vec[arcs[:,0]];d=vec[arcs[:,1]]-u
    score=(u*d).sum(1)/(torch.linalg.vector_norm(u,dim=1)*torch.linalg.vector_norm(d,dim=1))
    loss=loss+coeff*torch.relu(1e-5-score).pow(2*self.power).mean()
   else:
    if not len(bb):continue
    bb=[bar for bar in bb if bar[0]>1e-16]
    if not bb:continue
    ei=torch.tensor([bar[3] for bar in bb]);pk=torch.tensor([bar[1] for bar in bb]);birth=tradius(vec)[pk];death=tgate(vec,edges)[ei]
    dep=torch.clamp((birth-death)/birth,min=0.)
    loss=loss+coeff*((dep+1e-20)**self.power-1e-20**self.power).sum()
  # Remove scale/translation flatness with numerically harmless reference gauge.
  # No geometry or mass in objective is computed using an obsolete complex.
  val=float(loss.detach());loss.backward();grad=t.grad.numpy()
  if np.isfinite(val) and val<self.best:
   self.best=val;self.saved=x.copy()
  if self.calls%200==0:
   print('CALL',self.calls,'loss',val,'best',self.best,'PQ',sum(a[0] for a in bp),sum(a[0] for a in bq),'counts',sum(a[0]>1e-12 for a in bp)+1,sum(a[0]>1e-12 for a in bq)+1,flush=True)
  if not np.all(np.isfinite(grad)):return 1e4,np.zeros_like(x)
  return val,grad

'''
UNITS['poly40'] = r'''"""Coherent non-affine polynomial surface deformation; physical hull and mass are live."""
from descent40 import *
import argparse

def basis(P,degree=2):
 c=state(P)[2][4];x=P[:,0]-c[0];z=P[:,2]-c[2];w=P[:,1]+.272*P[:,0]+.409*P[:,2]+.68526367
 vec=[];names=[]
 for deg in range(2,degree+1):
  mons=[]
  for i in range(deg+1):
   for j in range(deg-i+1):
    k=deg-i-j;mons.append((x**i*z**j*w**k,(i,j,k)))
  for comp in [0,2]:
   for m,key in mons:
    b=np.zeros_like(P);b[:,comp]=m;b[:,1]=-(.272 if comp==0 else .409)*m
    vec.append(b);names.append((comp,key))
  for m,key in mons:
   if key[2]>0:
    b=np.zeros_like(P);b[:,1]=m;vec.append(b);names.append((1,key))
 B=np.stack(vec,axis=2);scale=np.max(np.abs(B),axis=(0,1));B/=scale
 return B,names,scale

def run(P=P0,degree=2,power=.5,weights=(1,1),steps=500,prefix='poly40',seed=0,bound=.4):
 B,names,scale=basis(P,degree);obj=Objective(False,power,weights);cnt=[0]
 def fg(x):
  pp=P+np.einsum('ijk,k->ij',B,x);f,grad=obj(pp.flatten());return f,np.einsum('ijk,ij->k',B,grad.reshape(75,3))
 x0=np.zeros(B.shape[2]) if seed==0 else np.random.default_rng(seed).uniform(-.02,.02,B.shape[2])
 r=minimize(fg,x0,jac=True,bounds=[(-bound,bound)]*len(x0),method='L-BFGS-B',options={'maxiter':steps,'ftol':1e-14,'gtol':1e-10,'maxls':40})
 # Objective.saved is the actual all-point geometry at best observed evaluation.
 Y=obj.saved.reshape(75,3);coef=np.linalg.lstsq(B.reshape(225,-1),(Y-P).flatten(),rcond=None)[0];np.save(prefix+'.npy',Y)
 bp,bq,data=state(Y);out={'power':power,'weights':weights,'degree':degree,'coefficients':coef.tolist(),'names':names,'scales':scale.tolist(),'nit':int(r.nit),'nfev':int(r.nfev),'message':str(r.message),'vef':[len(data[-1]),len(data[2]),len(data[1])],'P':[float(a[0]) for a in bp if a[0]>1e-13],'Q':[float(a[0]) for a in bq if a[0]>1e-13],'centroid':data[4].tolist(),'loss':obj.best}
 json.dump(out,open(prefix+'.json','w'));print(prefix,json.dumps({k:v for k,v in out.items() if k not in ['names','coefficients','scales']}),flush=True)
 return Y
'''
UNITS['retract40'] = r'''"""All-new-roots numerical repair using actual hull and own centroid at every evaluation."""
from descent40 import *
K0=g.hull(g.points());N0=[]
for f in [K0['faces'][27],K0['faces'][53]]:
 n=np.cross(P0[f[1]]-P0[f[0]],P0[f[2]]-P0[f[0]]);N0.append(n/np.linalg.norm(n))
N0=np.array(N0)

def best_arcs(V,E,roots):
 adj=[[] for _ in V]
 for i,j in E:adj[i].append(j);adj[j].append(i)
 arcs=[]
 for i,js in enumerate(adj):
  if i in roots or not js:continue
  j=max(js,key=lambda j:np.dot(V[i],V[j]-V[i])/np.linalg.norm(V[j]-V[i]))
  arcs.append((i,j))
 return np.array(arcs)

class Repair:
 def __init__(self,patch,margin,npr=2,nqr=2,weight=(1,1)):
  self.patch=patch;self.margin=margin;self.npr=npr;self.nqr=nqr;self.weight=weight;self.calls=0;self.best=1e99;self.bestx=None
 def __call__(self,x):
  self.calls+=1;P=unpack(x,self.patch)
  try:bp,bq,(T,F,E,D,c,Q,groups,ids)=state(P)
  except Exception:return 1e10,np.zeros_like(x)
  rootp=[6,62][:self.npr]
  rootq=[int(np.argmax((Q/np.linalg.norm(Q,axis=1)[:,None])@n)) for n in N0]
  if self.nqr==1:rootq=rootq[1:]
  Ap=best_arcs(P-c,E,rootp);Aq=best_arcs(Q,D,rootq)
  t=torch.tensor(x,requires_grad=True);Y=unpack(t,self.patch);a,b,d=Y[T[:,0]],Y[T[:,1]],Y[T[:,2]];o=Y.mean(0)
  vv=((a-o)*torch.linalg.cross(b-o,d-o,dim=1)).sum(1)/6
  cc=(vv[:,None]*(a+b+d+o)/4).sum(0)/vv.sum();X=Y-cc
  n=torch.linalg.cross(Y[F[:,1]]-Y[F[:,0]],Y[F[:,2]]-Y[F[:,0]],dim=1);QQ=n/(n*X[F[:,0]]).sum(1)[:,None]
  loss=t.sum()*0
  for coeff,V,A in [(self.weight[0],X,Ap),(self.weight[1],QQ,Aq)]:
   if len(A):
    u=V[A[:,0]];d=V[A[:,1]]-u
    z=(u*d).sum(1)/(torch.linalg.vector_norm(u,dim=1)*torch.linalg.vector_norm(d,dim=1))
    loss=loss+coeff*torch.relu(self.margin-z).square().sum()
  val=float(loss.detach());loss.backward();grad=t.grad.numpy()
  if val<self.best:self.best=val;self.bestx=x.copy()
  if self.calls%250==0:print('REPAIR',self.calls,val,'best',self.best,'counts',int(sum(a[0]>1e-12 for a in bp)+1),int(sum(a[0]>1e-12 for a in bq)+1),'PQ',max((a[0] for a in bp),default=0),max((a[0] for a in bq),default=0),flush=True)
  if not np.isfinite(val) or not np.all(np.isfinite(grad)):return 1e10,np.zeros_like(x)
  return val,grad

def repair(P,steps=1000,patch=True,margin=1e-5,npr=2,nqr=2,prefix='repair40',weight=(1,1),trust=None):
 obj=Repair(patch,margin,npr,nqr,weight);x0=pack(P,patch)
 r=minimize(obj,x0,jac=True,method='L-BFGS-B',bounds=None if trust is None else [(x-trust,x+trust) for x in x0],options={'maxiter':steps,'maxfun':steps*5,'maxls':40,'ftol':1e-16,'gtol':1e-13,'maxcor':20})
 P=unpack(obj.bestx,patch);np.save(prefix+'.npy',P);bp,bq,data=state(P)
 out={'loss':obj.best,'margin':margin,'npr':npr,'nqr':nqr,'nit':int(r.nit),'nfev':int(r.nfev),'message':str(r.message),'vef':[len(data[-1]),len(data[2]),len(data[1])],'P':[float(a[0]) for a in bp if a[0]>1e-13],'Q':[float(a[0]) for a in bq if a[0]>1e-13],'centroid':data[4].tolist()}
 print(prefix,json.dumps(out),flush=True);json.dump(out,open(prefix+'.json','w'));return P
'''
UNITS['positive40'] = r'''"""All-new-roots numerical repair using actual hull and own centroid at every evaluation."""
from descent40 import *
K0=g.hull(g.points());N0=[]
for f in [K0['faces'][27],K0['faces'][53]]:
 n=np.cross(P0[f[1]]-P0[f[0]],P0[f[2]]-P0[f[0]]);N0.append(n/np.linalg.norm(n))
N0=np.array(N0)

def best_arcs(V,E,roots):
 adj=[[] for _ in V]
 for i,j in E:adj[i].append(j);adj[j].append(i)
 arcs=[]
 for i,js in enumerate(adj):
  if i in roots or not js:continue
  j=max(js,key=lambda j:np.dot(V[i],V[j]-V[i])/np.linalg.norm(V[j]-V[i]))
  arcs.append((i,j))
 return np.array(arcs)

def pack_positive(P,patch):
 if not patch:return P.flatten()
 a=np.linalg.lstsq(np.c_[P[PATCH,0],P[PATCH,2],np.ones(18)],P[PATCH,1],rcond=None)[0]
 w=P[REST,1]-a[0]*P[REST,0]-a[1]*P[REST,2]-a[2]
 assert min(w)>0,(min(w),'nonpositive height')
 return np.r_[P[PATCH][:,[0,2]].flatten(),np.c_[P[REST,0],P[REST,2],np.log(w)].flatten(),a]

def unpack_positive(x,patch):
 if not patch:return x.reshape(75,3)
 if isinstance(x,torch.Tensor):P=torch.zeros((75,3),dtype=x.dtype);v=x[:36].reshape(18,2);w=torch.exp(x[36:-3].reshape(57,3)[:,2])
 else:P=np.zeros((75,3));v=x[:36].reshape(18,2);w=np.exp(x[36:-3].reshape(57,3)[:,2])
 P[PATCH,0]=v[:,0];P[PATCH,2]=v[:,1];P[PATCH,1]=x[-3]*v[:,0]+x[-2]*v[:,1]+x[-1]
 v=x[36:-3].reshape(57,3);P[REST,0]=v[:,0];P[REST,2]=v[:,1];P[REST,1]=x[-3]*v[:,0]+x[-2]*v[:,1]+x[-1]+w
 return P
pack=pack_positive
unpack=unpack_positive

class Repair:
 def __init__(self,patch,margin,npr=2,nqr=2,weight=(1,1)):
  self.patch=patch;self.margin=margin;self.npr=npr;self.nqr=nqr;self.weight=weight;self.calls=0;self.best=1e99;self.bestx=None
 def __call__(self,x):
  self.calls+=1;P=unpack(x,self.patch)
  try:bp,bq,(T,F,E,D,c,Q,groups,ids)=state(P)
  except Exception:return 1e10,np.zeros_like(x)
  rootp=[int(np.argmax(np.linalg.norm(P-c,axis=1)))]
  if self.npr==2 and bp:rootp.append(bp[0][1])
  rootq=[int(np.argmax(np.linalg.norm(Q,axis=1)))]
  if self.nqr==2 and bq:rootq.append(bq[0][1])
  Ap=best_arcs(P-c,E,rootp);Aq=best_arcs(Q,D,rootq)
  t=torch.tensor(x,requires_grad=True);Y=unpack(t,self.patch);a,b,d=Y[T[:,0]],Y[T[:,1]],Y[T[:,2]];o=Y.mean(0)
  vv=((a-o)*torch.linalg.cross(b-o,d-o,dim=1)).sum(1)/6
  cc=(vv[:,None]*(a+b+d+o)/4).sum(0)/vv.sum();X=Y-cc
  n=torch.linalg.cross(Y[F[:,1]]-Y[F[:,0]],Y[F[:,2]]-Y[F[:,0]],dim=1);QQ=n/(n*X[F[:,0]]).sum(1)[:,None]
  loss=t.sum()*0
  for coeff,V,A in [(self.weight[0],X,Ap),(self.weight[1],QQ,Aq)]:
   if len(A):
    u=V[A[:,0]];d=V[A[:,1]]-u
    z=(u*d).sum(1)/(torch.linalg.vector_norm(u,dim=1)*torch.linalg.vector_norm(d,dim=1))
    loss=loss+coeff*torch.relu(self.margin-z).square().sum()
  val=float(loss.detach());loss.backward();grad=t.grad.numpy()
  if val<self.best:self.best=val;self.bestx=x.copy()
  if self.calls%250==0:print('REPAIR',self.calls,val,'best',self.best,'counts',int(sum(a[0]>1e-12 for a in bp)+1),int(sum(a[0]>1e-12 for a in bq)+1),'PQ',max((a[0] for a in bp),default=0),max((a[0] for a in bq),default=0),flush=True)
  if not np.isfinite(val) or not np.all(np.isfinite(grad)):return 1e10,np.zeros_like(x)
  return val,grad

def repair(P,steps=1000,patch=True,margin=1e-5,npr=2,nqr=2,prefix='repair40',weight=(1,1),trust=None):
 obj=Repair(patch,margin,npr,nqr,weight);x0=pack(P,patch)
 r=minimize(obj,x0,jac=True,method='L-BFGS-B',bounds=None if trust is None else [(x-trust,x+trust) for x in x0],options={'maxiter':steps,'maxfun':steps*5,'maxls':40,'ftol':1e-16,'gtol':1e-13,'maxcor':20})
 P=unpack(obj.bestx,patch);np.save(prefix+'.npy',P);bp,bq,data=state(P)
 out={'loss':obj.best,'margin':margin,'npr':npr,'nqr':nqr,'nit':int(r.nit),'nfev':int(r.nfev),'message':str(r.message),'vef':[len(data[-1]),len(data[2]),len(data[1])],'P':[float(a[0]) for a in bp if a[0]>1e-13],'Q':[float(a[0]) for a in bq if a[0]>1e-13],'centroid':data[4].tolist()}
 print(prefix,json.dumps(out),flush=True);json.dump(out,open(prefix+'.json','w'));return P
'''
UNITS['qcontinue40'] = r'''from positive40 import *
from descent40 import tgate,tradius
class QContinue(Repair):
 def __call__(self,x):
  self.calls+=1;P=unpack(x,True)
  try:bp,bq,(T,F,E,D,c,Q,groups,ids)=state(P)
  except Exception:return 1e10,np.zeros_like(x)
  rootp=[int(np.argmax(np.linalg.norm(P-c,axis=1)))];Ap=best_arcs(P-c,E,rootp)
  t=torch.tensor(x,requires_grad=True);Y=unpack(t,True);a,b,d=Y[T[:,0]],Y[T[:,1]],Y[T[:,2]];o=Y.mean(0)
  vv=((a-o)*torch.linalg.cross(b-o,d-o,dim=1)).sum(1)/6;cc=(vv[:,None]*(a+b+d+o)/4).sum(0)/vv.sum();X=Y-cc
  n=torch.linalg.cross(Y[F[:,1]]-Y[F[:,0]],Y[F[:,2]]-Y[F[:,0]],dim=1);QQ=n/(n*X[F[:,0]]).sum(1)[:,None]
  u=X[Ap[:,0]];d=X[Ap[:,1]]-u;z=(u*d).sum(1)/(torch.linalg.vector_norm(u,dim=1)*torch.linalg.vector_norm(d,dim=1))
  loss=self.weight[0]*torch.relu(self.margin-z).square().sum()
  bb=[bar for bar in bq if bar[0]>1e-16]
  if bb:
   ei=torch.tensor([bar[3] for bar in bb]);pk=torch.tensor([bar[1] for bar in bb]);birth=tradius(QQ)[pk];death=tgate(QQ,D)[ei]
   dep=torch.clamp((birth-death)/birth,min=0.);loss=loss+dep.sum()
  val=float(loss.detach());loss.backward();grad=t.grad.numpy()
  if val<self.best:self.best=val;self.bestx=x.copy()
  if self.calls%250==0:print('QCONT',self.calls,val,'best',self.best,'PQ',sum(a[0] for a in bp),sum(a[0] for a in bq),flush=True)
  if not np.isfinite(val) or not np.all(np.isfinite(grad)):return 1e10,np.zeros_like(x)
  return val,grad

def go(P,steps,weight,trust,prefix):
 obj=QContinue(True,1e-5,1,2,(weight,1));x0=pack(P,True)
 r=minimize(obj,x0,jac=True,method='L-BFGS-B',bounds=[(x-trust,x+trust) for x in x0],options={'maxiter':steps,'maxfun':steps*5,'maxls':40,'ftol':1e-16,'gtol':1e-13,'maxcor':20})
 P=unpack(obj.bestx,True);np.save(prefix+'.npy',P);bp,bq,data=state(P)
 out={'loss':obj.best,'weight':weight,'nit':int(r.nit),'nfev':int(r.nfev),'message':str(r.message),'vef':[len(data[-1]),len(data[2]),len(data[1])],'P':[float(a[0]) for a in bp if a[0]>1e-13],'Q':[float(a[0]) for a in bq if a[0]>1e-13],'centroid':data[4].tolist()}
 print(prefix,json.dumps(out),flush=True);json.dump(out,open(prefix+'.json','w'));return P
'''
UNITS['simplify40'] = r'''"""Finite vertex removal plus live-hull two-landscape repair; numerical nomination only."""
import positive40 as r
import json
np=r.np

def simplify(P,steps=20,prefix='simp40',start=0):
 for k in range(start,start+steps):
  bp,bq,data=r.state(P);ids=set(data[-1]);oldn=len(ids);c=data[4];oldq=max((b[0] for b in bq),default=0);cap=P[r.PATCH].mean(0)
  # All inactive material rows become harmless interior representatives, not implicit support owners.
  for i in range(len(P)):
   if i not in ids:P[i]=cap if i in r.PATCH else c
  candidates=[]
  for i in sorted(ids):
   if i==6:continue
   Y=P.copy();Y[i]=cap if i in r.PATCH else c
   try:
    pb,qb,d=r.state(Y);main=max((a[0] for a in qb),default=0)
    loss=sum(a[0] for a in pb)+sum(a[0] for a in qb)-main+.03*main
    candidates.append((loss,i,Y,len(d[-1])))
   except Exception:continue
  won=False
  for loss,i,Y,n in sorted(candidates,key=lambda a:(a[0],a[1]))[:5]:
   if n>=oldn:continue
   name=prefix+'_'+str(k)+'_try'+str(i)
   Z=r.repair(Y,300,True,1e-4,1,2,name,(1,1),.08)
   meta=json.load(open(name+'.json'));nn=meta['vef'][0]
   if meta['loss']<1e-17 and nn<oldn:
    P=Z;np.save(prefix+'_'+str(k)+'.npy',P)
    meta['removed_material']=int(i);meta['old_vef']=[oldn,len(data[2]),len(data[1])];meta['old_Q']=oldq
    json.dump(meta,open(prefix+'_'+str(k)+'.json','w'));print('SIMPLIFIED',k,i,meta,flush=True);won=True;break
  if not won:print('NO_ACCEPTED_SIMPLIFICATION_AT',k,flush=True);break
 return P
'''
UNITS['audit_candidate40'] = r'''import numpy as np,json,sys
from fractions import Fraction as F
import J75_REFERENCE110_CAP233 as g
import masslift57 as m
from pathlib import Path

def audit(name,D=10**7,DP=10**8):
 P=np.load(name+'.npy');a=np.linalg.lstsq(np.c_[P[g.PATCH,0],P[g.PATCH,2],np.ones(18)],P[g.PATCH,1],rcond=None)[0]
 plane=[F(round(float(v)*DP),DP) for v in a];rows=[[round(float(x)*D) for x in row] for row in P]
 p=[tuple(F(x,D) for x in row) for row in rows]
 for i in g.PATCH:
  x,_,z=p[i];p[i]=(x,plane[0]*x+plane[1]*z+plane[2],z)
 K=g.hull(p);R=m.report(K)
 source={'D':D,'DP':DP,'rows':rows,'plane':plane,'patch':g.PATCH}
 g.dump(name+'_source.json',source);br=g.dump(name+'_body.json',{'density':1,'points':K['points']});rr=g.dump(name+'_audit.json',R)
 print('EXACT',name,'VEF',[R[x] for x in ['V','E','F']],'strict',R['strict'],'weak',R['additional_weak'],'zeros',R['primitive_zero'],'P',[float(x['depth']) for x in R['P_bars']],'Q',[float(x['depth']) for x in R['Q_bars']],'body',br,'audit',rr,flush=True)
 return R,source
'''
UNITS['bridge40'] = r'''"""Numerical reciprocal-surface chain cuts from the exact N40 211 checkpoint."""
import numpy as np,json
from scipy.spatial import HalfspaceIntersection,ConvexHull
from fractions import Fraction as F
from explore40 import metrics
R=json.load(open('pos40_0_audit.json'))
P=np.array([[float(F(x)) for x in p] for p in R['points']]);Q=np.array([[float(F(x)) for x in p] for p in R['Q_vectors']]);C=np.array([float(F(x)) for x in R['centroid']]);U=Q[R['Q_bars'][0]['peak']];Z=Q[R['Q_bars'][0]['elder']]

def chain(n,bend=0,rpower=1):
 ru=np.linalg.norm(U);rz=np.linalg.norm(Z);a=U/ru;b=Z/rz;theta=np.arccos(a@b);ort=np.cross(a,b);ort/=np.linalg.norm(ort)
 out=[]
 for j in range(1,n):
  t=j/n;v=(np.sin((1-t)*theta)*a+np.sin(t*theta)*b)/np.sin(theta)
  v+=bend*np.sin(np.pi*t)*ort;v/=np.linalg.norm(v)
  rad=ru*(rz/ru)**(t**rpower);out.append(rad*v)
 return np.array(out)

def evaluate(n,bend=0,rpower=1):
 new=chain(n,bend,rpower);allq=np.r_[Q,new]
 h=HalfspaceIntersection(np.c_[allq,-np.ones(len(allq))],np.zeros(3));p=h.intersections+C
 val,info=metrics(p,True)
 if info is None:raise ValueError('hull')
 return p,{'n':n,'bend':bend,'rpower':rpower,'vef':info['vef'],'P':[float(a[0]) for a in info['P'] if a[0]>1e-12],'Q':[float(a[0]) for a in info['Q'] if a[0]>1e-12],'centre':info['c'].tolist(),'volume':info['V'],'lambda':new.tolist()}
'''
UNITS['J75_CENTRE_MILP'] = r'''"""Nominate reference centres with one S and one U; exact-check every candidate.
MILP infeasibility is a numerical conclusion only, not an exact exclusion proof.
All selections include every non-root vertex/facet, not only the old two defects.
"""
import argparse,json,time
from fractions import Fraction as F
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix
import J75_REFERENCE110_CAP233 as g
inputs=g

def problem(K,fixed=None,epsilon=1e-6):
    # Variables c0,c1,c2,margin,distance; then negative-witness and optional root binaries.
    p=np.array(K['points'],dtype=float);lo=p.min(0);hi=p.max(0)
    V,M=g.mass(K);c0=np.array(g.mul(M,1/V),dtype=float)
    lb=list(lo)+[epsilon,0];ub=list(hi)+[epsilon,4.0];ints=[0]*5
    rows=[];lims=[];witness_info=[];allroots=[]
    def row(d,b):rows.append(d);lims.append(b)
    def binary():
        i=len(lb);lb.append(0);ub.append(1);ints.append(1);return i
    for j in range(3):
        row({j:1,4:-1},c0[j]);row({j:-1,4:-1},-c0[j])
    for f in K['faces']:
        a,b,c=[p[i] for i in f[:3]];n=np.cross(b-a,c-a);n/=np.linalg.norm(n)
        row({0:n[0],1:n[1],2:n[2],3:1},n@a)
    # S first; U second. Choosing a strict negative guard rules out weak as well as strict equilibrium.
    groups=g.affine_guards(K)[:2]
    for kind,group in enumerate(groups):
        rr=[]
        for k,gg in enumerate(group):
            if fixed is not None and k==fixed[kind]:
                for ar,br in gg:
                    a=np.array(ar,dtype=float);norm=np.linalg.norm(a);a/=norm;b=float(br)/norm
                    row({0:a[0],1:a[1],2:a[2],3:1},b)
                continue
            ww=[]
            if fixed is None:
                root=binary();rr.append(root);ww.append(root)
            for j,(ar,br) in enumerate(gg):
                a=np.array(ar,dtype=float);norm=np.linalg.norm(a);a/=norm;b=float(br)/norm
                if np.min(b-p@a)>=-1e-13:continue # no strict negative guard at any interior centre
                y=binary();ww.append(y);witness_info.append((kind,k,j,y))
                big=max(0,b-sum(a[t]*(lo[t] if a[t]>0 else hi[t]) for t in range(3))+epsilon)+1e-7
                row({0:-a[0],1:-a[1],2:-a[2],3:1,y:big},big-b)
            row({i:-1 for i in ww},-1)
        if fixed is None:
            row({i:1 for i in rr},1);row({i:-1 for i in rr},-1)
            allroots.append(rr)
    rowi=[];coli=[];val=[]
    for i,d in enumerate(rows):
        for j,x in d.items():rowi.append(i);coli.append(j);val.append(x)
    A=coo_matrix((val,(rowi,coli)),shape=(len(rows),len(lb))).tocsc()
    objective=np.zeros(len(lb));objective[4]=1
    return objective,np.array(ints),Bounds(lb,ub),LinearConstraint(A,-np.inf,lims),allroots

def run(out,fixed,epsilon,seconds):
    K=g.hull(inputs.points());obj,ints,bounds,const,roots=problem(K,fixed,epsilon)
    print('MODEL',len(obj),'variables',sum(ints),'integer',const.A.shape[0],'rows',flush=True)
    start=time.time();r=milp(obj,integrality=ints,bounds=bounds,constraints=const,
       options={'time_limit':seconds,'mip_rel_gap':1e-8,'presolve':True,'disp':False})
    result={'fixed':fixed,'epsilon':epsilon,'status':int(r.status),'message':str(r.message),'seconds':time.time()-start}
    print('MILP',result,flush=True)
    if r.x is not None:
        result['raw_centre']=list(map(float,r.x[:3]));result['distance']=float(r.x[4]);result['solver_objective']=float(r.fun)
        c=tuple(F(round(x*10**10),10**10) for x in r.x[:3]);result['exact_centre']=c
        result['exact_census']=g.census(K,c)
        result['interior']=all(g.dot(g.cross(g.sub(K['points'][f[1]],K['points'][f[0]]),g.sub(K['points'][f[2]],K['points'][f[0]])),g.sub(K['points'][f[0]],c))>0 for f in K['faces'])
        print('CANDIDATE',result,flush=True)
    g.dump(out,result)
'''
UNITS['gridfix40'] = r'''"""A finite integer one-coordinate screen; exact endpoint verification is separate."""
import numpy as np,json
from fractions import Fraction as F
import J75_REFERENCE110_CAP233 as g,masslift57 as m
from descent40 import state
S=json.load(open('robust40_0.005_G1000_source.json'));R=json.load(open('robust40_0.005_G1000_audit.json'));D=S['D'];plane=list(map(F,S['plane']))
def make(rows):
 pp=[tuple(F(v,D) for v in row) for row in rows]
 for i in S['patch']:
  x,_,z=pp[i];pp[i]=(x,plane[0]*x+plane[1]*z+plane[2],z)
 return pp
peak=next(i for i in R['U'] if R['material'][i]!=6);nb={peak}
for i,j in R['edges']:
 if i==peak:nb.add(j)
 if j==peak:nb.add(i)
choices=[]
for i in sorted(R['material'][j] for j in nb):
 for axis in range(3):
  if i in S['patch'] and axis==1:continue
  for step in [-1,1]:
   rows=[row.copy() for row in S['rows']];rows[i][axis]+=step;p=make(rows)
   bp,bq,data=state(np.array(p,float));key=(sum(b[0]>1e-12 for b in bp),sum(b[0]>1e-12 for b in bq),sum(b[0] for b in bp)+sum(b[0] for b in bq))
   choices.append((key,i,axis,step,rows))
for key,i,axis,step,rows in sorted(choices)[:12]:
 K=g.hull(make(rows));V,M=g.mass(K);c=g.mul(M,1/V);C=g.census(K,c)
 print('GRIDCHECK',i,axis,step,C['strict'],C['weak'],flush=True)
 if C['strict']==[2,1,1] and C['weak']==C['primitive_zero']==[0,0,0]:
  R=m.report(K);name='gridfix40_211';S['rows']=rows;S['integer_patch']=[i,axis,step];g.dump(name+'_source.json',S);br=g.dump(name+'_body.json',{'density':1,'points':K['points']});ar=g.dump(name+'_audit.json',R)
  print('GRIDFIX40_211_EXACT_PASS',[R[k] for k in ['V','E','F']],[float(b['depth']) for b in R['Q_bars']],br,ar);break
else:print('NO_211_IN_SCREENED_PREFIX')
'''

# These are the exact patches used to derive the dual-guard and free-surface runs.
UNITS['qcdual40']=UNITS['qcontinue40'].replace(
 'rootp=[int(np.argmax(np.linalg.norm(P-c,axis=1)))];Ap=best_arcs(P-c,E,rootp)',
 'rootp=[int(np.argmax(np.linalg.norm(P-c,axis=1)))];Ap=best_arcs(P-c,E,rootp)\n  rootq=[int(np.argmax(np.linalg.norm(Q,axis=1)))];\n  if bq:rootq.append(bq[0][1])\n  Aq=best_arcs(Q,D,rootq)').replace(
 'loss=self.weight[0]*torch.relu(self.margin-z).square().sum()',
 'loss=self.weight[0]*torch.relu(self.margin-z).square().sum()\n  u=QQ[Aq[:,0]];d=QQ[Aq[:,1]]-u;z=(u*d).sum(1)/(torch.linalg.vector_norm(u,dim=1)*torch.linalg.vector_norm(d,dim=1))\n  loss=loss+self.weight[0]*torch.relu(self.margin-z).square().sum()')
UNITS['qcfree40']=UNITS['qcdual40']
for a,b in [('unpack(x,True)','unpack(x,False)'),('unpack(t,True)','unpack(t,False)'),('pack(P,True)','pack(P,False)'),('unpack(obj.bestx,True)','unpack(obj.bestx,False)'),('QContinue(True,','QContinue(False,')]:
 UNITS['qcfree40']=UNITS['qcfree40'].replace(a,b)

sys.modules['J75_REFERENCE110_CAP233']=exact
sys.modules['masslift57']=exact
modules={}
def load(name):
 if name in modules:return modules[name]
 module=types.ModuleType(name);sys.modules[name]=module
 exec(compile(UNITS[name],name+'.py','exec'),module.__dict__);modules[name]=module
 return module
for name in ['explore40','descent40','poly40','retract40','positive40','qcontinue40','qcdual40','qcfree40','simplify40','audit_candidate40']:
 load(name)
p=modules['positive40'];audit=modules['audit_candidate40'].audit

def grid(stem,D,DP):
 name=stem+'_G'+str(D);np.save(name+'.npy',np.load(stem+'.npy'));return audit(name,D,DP)

def free_audit(stem,D=10**8):
 Y=np.load(stem+'.npy');rows=[[round(float(x)*D) for x in row] for row in Y]
 K=exact.hull([tuple(F(x,D) for x in row) for row in rows]);R=exact.report(K)
 exact.dump(stem+'_source.json',dict(D=D,DP=1,rows=rows,plane=[],patch=[]))
 exact.dump(stem+'_body.json',dict(density=1,points=K['points']));exact.dump(stem+'_audit.json',R)
 print('N40_FREE_NOMINEE',R['V'],R['E'],R['F'],R['census'],flush=True)

def expand_exact(name):
    pts,mat=exact.literal(name);K=exact.hull(pts);V,M=exact.mass(K);c=exact.mul(M,1/V)
    P=[c]*75
    if name!='PARENT' and exact.DATA[name]['plane']:
        cap=exact.DATA[name]['cap'];o=tuple(sum(pts[i][j] for i in cap)/len(cap) for j in range(3))
        for i in exact.PATCH:P[i]=o
    for point,i in zip(pts,mat):P[i]=point
    return P

def start_exact(name):
    return np.array(expand_exact(name),dtype=float)

def phase(which):
 if which=='first':
  P=modules['poly40'].run(degree=3,power=1.,weights=(1,.001),steps=1400,prefix='poly40_d3_w0.001',seed=0,bound=.8)
  P=modules['retract40'].repair(P,1500,True,1e-5,1,2,'r40_U1_patch',(1,0),.02)
  P=p.repair(P,1000,True,1e-5,1,2,'pos40_0',(1,1),.04)
  audit('r40_U1_patch');audit('pos40_0')
 elif which=='q_a':
  P=np.load('pos40_0.npy');q=modules['qcontinue40']
  P=q.go(P,150,1000,.15,'qc40_0');P=p.repair(P,400,True,1e-5,1,2,'pos40_qc0',(1,1),.06)
  P=q.go(P,200,1000,.2,'qc40_1');P=p.repair(P,400,True,1e-5,1,2,'pos40_qc1',(1,1),.06)
  for k in range(2,5):
   P=q.go(P,250,1000,.25,'qc40_'+str(k));P=p.repair(P,500,True,1e-5,1,2,'pos40_qc'+str(k),(1,1),.08)
 elif which=='q_b':
  P=np.load('pos40_qc4.npy');q=modules['qcdual40']
  for k in range(3):
   P=q.go(P,300,1000,.25,'qd40_'+str(k));P=p.repair(P,500,True,1e-5,1,2,'pos40_qd'+str(k),(1,1),.08)
  audit('pos40_qd2')
 elif which=='q_c':
  P=np.load('pos40_qd2.npy');P=p.repair(P,500,False,1e-5,1,2,'free40_start',(1,1),.02)
  q=modules['qcfree40']
  for k in range(3):
   P=q.go(P,300,1000,.3,'qfree40_'+str(k));P=p.repair(P,500,False,1e-5,1,2,'free40_'+str(k),(1,1),.08)
  free_audit('free40_2')
 elif which=='robust':
  P=np.load('pos40_qd2.npy')
  for mar in [1e-4,.0005,.001]:P=p.repair(P,600,True,mar,1,2,'robust40_'+str(mar),(1,1),.05)
  for stem in ['robust40_0.0005','robust40_0.001']:
   for D in [10000,100000]:grid(stem,D,D)
  P=np.load('robust40_0.0005.npy')
  for mar in [.002,.005,.01]:P=p.repair(P,700,True,mar,1,2,'robust40_'+str(mar),(1,1),.15)
  grid('robust40_0.005',1000,1000);grid('robust40_0.01',1000,1000);load('gridfix40')
 elif which.startswith('simplify_'):
  part=which[-1];stem={'a':'pos40_qd2','b':'simp40_9','c':'simp40_21'}[part]
  start={'a':0,'b':10,'c':22}[part];steps={'a':10,'b':12,'c':12}[part]
  modules['simplify40'].simplify(np.load(stem+'.npy'),steps,'simp40',start)
  names={'a':['simp40_9'],'b':['simp40_21'],'c':['simp40_22','simp40_23_try26','simp40_23_try72']}[part]
  for name in names:audit(name,10**8,10**9)
 elif which=='negative':
  P=np.load('pos40_0.npy')
  for k in range(12):P=p.repair(P,400,True,1e-5,1,1,'pos40_target_'+str(k),(1,1),.08)
  b=load('bridge40')
  for n in [9,10,12,16,20]:
   P,out=b.evaluate(n);np.save('bridge40_'+str(n)+'.npy',P);exact.dump('bridge40_'+str(n)+'.json',out);print('BRIDGE_NOMINATION_ONLY',out,flush=True)
 elif which=='compare':
  receipt={}
  for name,d in exact.DATA.items():
   raw=Path(d['origin']+'_body.json').read_bytes();sha=hashlib.sha256(raw).hexdigest();assert sha==d['sha'],name
   receipt[name]={'bytes':len(raw),'sha256':sha}
  exact.dump('N40_COLD_RECEIPT.json',receipt);print('N40_ALL_16_COLD_NOMINATED_BODY_HASHES_MATCH',flush=True)
 elif which=='references':
  t=load('J75_CENTRE_MILP')
  for name in ['V46_211_G7','V47_FREE211_G8']:
   pts,_=exact.literal(name);K=exact.hull(pts);obj,ints,bounds,const,roots=t.problem(K,None,1e-6)
   result=t.milp(obj,integrality=ints,bounds=bounds,constraints=const,options={'time_limit':15,'presolve':True,'mip_rel_gap':1e-8})
   print('REFERENCE_MILP_NOMINATION_ONLY',name,result.message,result.fun,flush=True)
   if result.x is not None:
    cc=tuple(F(round(float(x)*10**9),10**9) for x in result.x[:3]);print(cc,exact.census(K,cc),flush=True)
 else:raise ValueError(which)
 print('N40_NOMINATION_PHASE_FINISHED',which,flush=True)

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('phase',choices=['first','q_a','q_b','q_c','robust','simplify_a','simplify_b','simplify_c','negative','references','compare']);ap.add_argument('--work',default='N40_nomination');args=ap.parse_args()
 Path(args.work).mkdir(parents=True,exist_ok=True);os.chdir(args.work);phase(args.phase)
