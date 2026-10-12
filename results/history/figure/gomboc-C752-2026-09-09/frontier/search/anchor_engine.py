"""One genuine nonroot high-degree physical vertex, plus the protected apex.
Anchor and all contact rows are explicit; noncontact supporting inequalities are
retained. Floating discovery only. Exact general-purpose audit is separate.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import json,time,numpy as np
from pathlib import Path
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from geometry_anchor import geom,brief,escape_grad
from forest_search import widest
from coarsen2 import load,ERR

def data(G,root,der=False):
 u=G['source'].index(('root',));ui=np.array([j for j in range(G['V']) if j!=u]);si=G['active'][G['active']!=root]
 pu,_=widest(G['A_U'],u);ps,_=widest(G['A_S'],root,G['active']);v=np.r_[G['A_U'][ui,pu[ui]],G['A_S'][si,ps[si]]]
 J=np.vstack([escape_grad(G['Y'],G['JY'],pu,ui),escape_grad(G['Z'],G['JZ'],ps,si)]) if der else None
 return v,J

def project(q,anchor,pin=None):
 q=q.copy();a=np.array(anchor['point']);rm=q[:,2]==1;targets={i:1. for i in anchor['rows']}
 if pin is not None:targets[pin[0]]=pin[1]
 for i,t in targets.items():
  ax=int(np.argmax(np.abs(a[:2] if rm[i] else a)));q[i,ax]+=(t-q[i]@a)/a[ax]
 q[rm,2]=1;return q

def checkpoint(q,labels,anchor,path,**kw):
 G=geom(q,anchor=anchor);b=brief(G);b.update(q_hex=[[float(x).hex() for x in row] for row in q],original_rows=list(map(int,labels)),anchor={'point_hex':[float(x).hex() for x in anchor['point']],'rows':list(map(int,anchor['rows']))},minimum=float(data(G,labels.index(3))[0].min()),**kw);Path(path).write_text(json.dumps(b,separators=(',',':'),default=lambda x:x.item() if hasattr(x,'item') else list(x)))

def repair(q,root,anchor,steps=55,rho=2e-6,trust=.001,pin=None):
 q=project(q,anchor,pin);rm=q[:,2]==1.;n=q.size;E=eye(n,format='csr');aa=np.array(anchor['point']);history=[];eqids=anchor['rows']+([] if pin is None else [pin[0]]);targets={i:1. for i in anchor['rows']}
 if pin is not None:targets[pin[0]]=pin[1]
 guards=[i for i in range(len(q)) if i not in eqids];opts={'time_limit':3.,'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9}
 for it in range(steps):
  G=geom(q,True,anchor);v,A=data(G,root,True);f=float(v.min());cc=[len(G[k]) for k in ('S','U','H')];history.append(dict(iteration=it,minimum=f,counts=cc,VEF=[G[k] for k in ('V','E','F')]))
  if f>=.99*rho and cc==[1,1,0]:break
  sc=np.repeat(np.maximum(np.linalg.norm(q,axis=1),.5)*trust,3);mat=csr_matrix(A*sc);bounds=[(-1,1)]*n
  for i in range(len(q)):
   bounds[3*i+2]=(0,0) if rm[i] else (-1,min(1,(1-1e-9-q[i,2])/sc[3*i+2]))
  C=np.zeros((len(eqids),n));rhs=[]
  for j,i in enumerate(eqids):C[j,3*i:3*i+3]=aa*sc[3*i:3*i+3];rhs.append(targets[i]-aa@q[i])
  H=np.zeros((len(guards),n));hb=[]
  for j,i in enumerate(guards):H[j,3*i:3*i+3]=aa*sc[3*i:3*i+3];hb.append(1-1e-10-aa@q[i])
  eq=csr_matrix(np.c_[C,np.zeros(len(C))]);ineq=vstack([hstack([-mat,np.ones((len(v),1))]),hstack([csr_matrix(H),csr_matrix((len(H),1))])],format='csr')
  lp=linprog(np.r_[np.zeros(n),-1.],A_ub=ineq,b_ub=np.r_[v,hb],A_eq=eq,b_eq=rhs,bounds=bounds+[(None,rho)],method='highs',options=opts)
  if not lp.success:
   trust*=.5
   if trust<1e-9:break
   continue
  t=lp.x[-1];d=lp.x[:n];target=f+.8*(t-f)
  M=vstack([hstack([-mat,csr_matrix((len(v),n))]),hstack([csr_matrix(H),csr_matrix((len(H),n))]),hstack([E,-E]),hstack([-E,-E])],format='csr');ee=hstack([csr_matrix(C),csr_matrix((len(C),n))],format='csr')
  lp2=linprog(np.r_[np.zeros(n),np.ones(n)],A_ub=M,b_ub=np.r_[v-target,hb,np.zeros(2*n)],A_eq=ee,b_eq=rhs,bounds=bounds+[(0,None)]*n,method='highs-ipm',options=opts)
  if lp2.success:d=lp2.x[:n]
  d=(d*sc).reshape(q.shape);found=False
  for k in range(14):
   fac=2.**(-k);z=q+fac*d;z[rm,2]=1;z=project(z,anchor,pin)
   try:
    G2=geom(z,anchor=anchor);ff=data(G2,root)[0].min()
    if max(z@aa-1)>1e-8:continue
   except ERR:continue
   if ff>f+max(1e-13,1e-5*fac*max(t-f,0)):
    q=z;found=True;trust=min(.025,trust*1.25) if k==0 else (max(1e-8,trust*.65) if k>4 else trust);break
  if not found:
   trust*=.3
   if trust<1e-9:break
 G=geom(q,anchor=anchor);return q,float(data(G,root)[0].min()),history
