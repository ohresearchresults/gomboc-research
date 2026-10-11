"""Sparse LP with EXACT FIRST-ORDER own-volume centroid coupling.
The three centroid increments are auxiliary variables, NOT a movable reference:
delta_g = Jg delta_q is enforced as three equalities in every LP. Every actual
trial is then re-integrated and fully reclassified at its true volume centroid.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import time,numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from coarsen2 import geom,load,checkpoint,ERR,data
from forest_search import widest

def sparse_data(G,root,der=False):
 u=G['source'].index(('root',));ui=np.array([i for i in range(G['V']) if i!=u]);si=G['active'][G['active']!=root]
 pu,_=widest(G['A_U'],u);ps,_=widest(G['A_S'],root,G['active']);v=np.r_[G['A_U'][ui,pu[ui]],G['A_S'][si,ps[si]]]
 if not der:return v,None,None
 n=G['q'].size;Q=np.zeros((len(v),n));C=np.zeros((len(v),3));q=G['q'];g=G['g'];h=G['h']
 for row,i in enumerate(ui):
  j=pu[i];a=G['Y'][i];b=G['Y'][j];nn=a@a;ga=b/nn-2*a*(a@b)/nn**2;gb=a/nn
  Q[row]=ga@G['JX'][i]+gb@G['JX'][j];C[row]=-ga-gb
 for row0,i in enumerate(si):
  row=len(ui)+row0;j=ps[i];a=G['Z'][i];b=G['Z'][j];nn=a@a;ga=b/nn-2*a*(a@b)/nn**2;gb=a/nn
  Q[row,3*i:3*i+3]+=ga@(np.eye(3)/h[i]+np.outer(q[i],g)/h[i]**2)
  Q[row,3*j:3*j+3]+=gb@(np.eye(3)/h[j]+np.outer(q[j],g)/h[j]**2)
  C[row]=ga@np.outer(q[i],q[i])/h[i]**2+gb@np.outer(q[j],q[j])/h[j]**2
 return v,csr_matrix(Q),C

def repair(q,root=3,steps=50,rho=2e-6,trust=.001,verbose=False,out=None,labels=None,link=None,links=None,pins=None):
 q=q.copy();n=q.size;m=n+3;rm=q[:,2]==1.;E=eye(n,format='csr');hist=[];start=time.time();links=([link] if link is not None else links) or [];pins=pins or {};opts={'time_limit':3.,'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9}
 for it in range(steps):
  G=geom(q,True);v,A,C=sparse_data(G,root,True);f=float(v.min());cc=[len(G[k]) for k in ('S','U','H')];hist.append(dict(iteration=it,minimum=f,counts=cc,VEF=[G[k] for k in ('V','E','F')],elapsed=time.time()-start,trust=trust))
  if verbose and it%5==0:print('FAST_REPAIR',hist[-1],flush=True)
  if f>=.99*rho and cc==[1,1,0]:break
  sc=np.repeat(np.maximum(np.linalg.norm(q,axis=1),.5)*trust,3);mat=hstack([A.multiply(sc),csr_matrix(C*trust)],format='csr')
  bounds=[(-1,1)]*n
  for i in range(len(q)):
   if rm[i] or i in pins:bounds[3*i+2]=(0,0)
   else:bounds[3*i+2]=(-1,min(1,(1-1e-9-q[i,2])/sc[3*i+2]))
  bounds+=[(None,None)]*3
  eqs=[np.c_[-G['Jg']*sc/trust,np.eye(3)]]
  for ix,js,w,lam,anchor in links:
   H=np.zeros((3,m))
   for ax in range(3):
    H[ax,3*ix+ax]=sc[3*ix+ax]/trust
    for j,ww in zip(js,w):H[ax,3*j+ax]-=lam*ww*sc[3*j+ax]/trust
   eqs.append(H)
  eq=csr_matrix(np.vstack(eqs));rhs=np.zeros(eq.shape[0])
  lp=linprog(np.r_[np.zeros(m),-1.],A_ub=hstack([-mat,np.ones((len(v),1))],format='csr'),b_ub=v,A_eq=hstack([eq,csr_matrix((eq.shape[0],1))],format='csr'),b_eq=rhs,bounds=bounds+[(None,rho)],method='highs',options=opts)
  if not lp.success:
   trust*=.5
   if trust<1e-8:break
   continue
  t=lp.x[-1];dq=lp.x[:n];target=f+.8*(t-f)
  plus=hstack([E,csr_matrix((n,3)),-E],format='csr');minus=hstack([-E,csr_matrix((n,3)),-E],format='csr');M=vstack([hstack([-mat,csr_matrix((len(v),n))]),plus,minus],format='csr')
  lp2=linprog(np.r_[np.zeros(m),np.ones(n)],A_ub=M,b_ub=np.r_[v-target,np.zeros(2*n)],A_eq=hstack([eq,csr_matrix((eq.shape[0],n))],format='csr'),b_eq=rhs,bounds=bounds+[(0,None)]*n,method='highs-ipm',options=opts)
  if lp2.success:dq=lp2.x[:n]
  dq=(dq*sc).reshape(q.shape);found=False
  for k in range(14):
   fac=2.**(-k);z=q+fac*dq;z[rm,2]=1
   for i,targ in pins.items():z[i,2]=targ
   for ix,js,w,lam,anchor in links:z[ix]=(1-lam)*anchor+lam*w@z[js]
   z[rm,2]=1
   try:
    H=geom(z);ff=float(sparse_data(H,root)[0].min())
   except ERR:continue
   if ff>f+max(1e-13,1e-5*fac*max(t-f,0)):
    q=z;found=True
    if k==0:trust=min(.025,trust*1.25)
    elif k>4:trust=max(1e-8,trust*.65)
    break
  if not found:
   trust*=.3
   if trust<1e-9:break
 G=geom(q);return q,float(sparse_data(G,root)[0].min()),hist
