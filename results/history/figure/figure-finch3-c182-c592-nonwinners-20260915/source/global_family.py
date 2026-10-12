"""Whole C598 projective/affine geometry with newly integrated homogeneous mass.
Optional five movable chain points. Numerical proposals, never fixed reference centring.
"""
import sys,json,time,argparse
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.optimize import least_squares
from model import dot,cross,norm,divide,HERE
sys.set_int_max_str_digits(0)
class Global:
 def __init__(self,nodes=False):
  R=json.load(open(HERE/'seed/A.json'));self.P=np.array([[float(F(v)) for v in r] for r in R['raw_vertices']]);self.q=np.array([[float(F(v,d)) for v in n] for n,d in zip(R['normals'],R['offsets'])]);self.faces=R['faces'];self.E=np.array(R['edges']);self.root=82;self.stable=114;self.nodes=nodes;self.K=8+15*nodes
  self.tris=np.array([(cy[0],cy[k],cy[k+1]) for cy in self.faces for k in range(1,len(cy)-1)])
  self.ue=np.array([(a,b) for i,j in self.E for a,b in [(i,j),(j,i)]]);self.ui=[np.flatnonzero(self.ue[:,0]==i) for i in range(len(self.P))]
  efs={tuple(e):[] for e in self.E.tolist()}
  for fi,cy in enumerate(self.faces):
   for a,b in zip(cy,cy[1:]+cy[:1]):efs[tuple(sorted((a,b)))].append(fi)
  self.fe=np.array([(a,b) for fs in efs.values() for a,b in [fs,fs[::-1]]]);self.fi=[np.flatnonzero(self.fe[:,0]==i) for i in range(len(self.q))]
  meta=json.load(open(HERE/'META.json'));self.labels=np.array(meta['labels']);self.sel=meta['selectors'];self.newids=[int(np.flatnonzero(self.labels==i)[0]) for i in range(167,172)];self.last=None;self.reslast=None
 def evaluate(self,z):
  K=self.K;P=self.P.copy();DP=np.zeros((*P.shape,K));q=self.q.copy();DQ=np.zeros((*q.shape,K))
  if self.nodes:
   P[self.newids]+=z[8:].reshape(5,3);DP[self.newids,:,8:]=np.eye(15).reshape(5,3,15)
   new=[k for k,s in enumerate(self.sel) if 'tri' in s];ts=np.array([[int(np.flatnonzero(self.labels==j)[0]) for j in self.sel[k]['tri']] for k in new]);A=P[ts];DA=DP[ts];v=np.linalg.solve(A,np.ones((len(A),3,1)))[...,0];dv=np.linalg.solve(A,-np.einsum('niak,na->nik',DA,v));q[new]=v;DQ[new]=dv
  a=z[5:8];da=np.zeros((3,K));da[:,5:8]=np.eye(3);den=1+P@a;dden=np.einsum('nik,i->nk',DP,a)+P@da
  Y=P/den[:,None];DY=(DP-Y[:,:,None]*dden[:,None,:])/den[:,None,None];q=q+a;DQ=DQ+da
  L=np.array([[np.exp(z[0]),z[2],z[3]],[0.,np.exp(z[1]),z[4]],[0.,0.,np.exp(-z[0]-z[1])]]);DL=np.zeros((3,3,K));DL[0,0,0]=L[0,0];DL[1,1,1]=L[1,1];DL[2,2,0]=DL[2,2,1]=-L[2,2];DL[0,1,2]=DL[0,2,3]=DL[1,2,4]=1
  X=Y@L.T;DX=np.einsum('nik,ji->njk',DY,L)+np.einsum('ni,jik->njk',Y,DL)
  N=np.linalg.solve(L.T,q.T).T;DN=np.linalg.solve(L.T,(DQ-np.einsum('jik,nj->nik',DL,N)).transpose(1,0,2).reshape(3,-1)).reshape(3,len(N),K).transpose(1,0,2)
  T=X[self.tris];DT=DX[self.tris];cr,dcr=cross(T[:,1],T[:,2],DT[:,1],DT[:,2]);dt,ddt=dot(T[:,0],cr,DT[:,0],dcr);D=dt.sum();dD=ddt.sum(axis=0);B=np.einsum('n,ni->i',dt,T.sum(axis=1));dB=np.einsum('nk,ni->ik',ddt,T.sum(axis=1))+np.einsum('n,nik->ik',dt,DT.sum(axis=1));g=B/(4*D);dg=(dB-4*g[:,None]*dD)/(4*D);Z=X-g;DZ=DX-dg
  i,j=self.ue.T;v,dv=dot(Z[i],X[j]-X[i],DZ[i],DX[j]-DX[i]);ll,dll=norm(X[j]-X[i],DX[j]-DX[i]);rr,drr=norm(Z[i],DZ[i]);u,du=divide(v,ll*rr,dv,dll*rr[:,None]+drr*ll[:,None])
  h=1-N@g;dh=-np.einsum('nik,i->nk',DN,g)-N@dg;QQ=N/h[:,None];DQQ=(DN-QQ[:,:,None]*dh[:,None,:])/h[:,None,None]
  i,j=self.fe.T;e=QQ[j]-QQ[i];de=DQQ[j]-DQQ[i];v,dv=dot(QQ[i],e,DQQ[i],de);ll,dll=norm(e,de);rr,drr=norm(QQ[i],DQQ[i]);fv,df=divide(v,ll*rr,dv,dll*rr[:,None]+drr*ll[:,None])
  su=np.array([ix[np.argmax(u[ix])] for ix in self.ui]);sf=np.array([ix[np.argmax(fv[ix])] for ix in self.fi]);UU=np.arange(len(su))!=self.root;FF=np.arange(len(sf))!=self.stable
  vals=np.r_[1e-6-u[su[UU]],1e-6-fv[sf[FF]],1e-5+u[su[self.root]],1e-5+fv[sf[self.stable]],.08-den];J=np.vstack((-du[su[UU]],-df[sf[FF]],du[su[self.root]],df[sf[self.stable]],-dden));weights=np.r_[np.ones(np.sum(UU)+np.sum(FF)+2),np.full(len(den),10.)]
  if self.nodes:
   inc=np.ones((len(q),len(P)),bool)
   for f,cy in enumerate(self.faces):inc[f,cy]=False
   f,vv=np.where(inc);ss=1-np.einsum('ni,ni->n',q[f]-a,P[vv]);ds=-np.einsum('nik,ni->nk',DQ[f]-da,P[vv])-np.einsum('ni,nik->nk',q[f]-a,DP[vv]);vals=np.r_[vals,1e-10-ss];J=np.vstack((J,-ds));weights=np.r_[weights,np.full(len(ss),50.)]
  V=np.maximum(vals,0)*weights;Jac=J*(weights*(vals>0))[:,None]
  return V,Jac,{'S':np.flatnonzero(fv[sf]<0).tolist(),'U':np.flatnonzero(u[su]<0).tolist(),'g':g.tolist(),'volume':D/6,'min_den':float(den.min()),'max_hinge':float(V.max()),'cost':float(V@V),'node_geometry_valid':bool(not self.nodes or ss.min()>0)}
 def both(self,z):
  if self.last is None or not np.array_equal(z,self.last):self.reslast=self.evaluate(z);self.last=z.copy()
  return self.reslast
 def fun(self,z):return self.both(z)[0]
 def jac(self,z):return self.both(z)[1]

def run(tag,count,seed,maxeval,nodes,start):
 G=Global(nodes);rng=np.random.default_rng(seed);best=1e9;tr=[]
 for it in range(count):
  if it==0:z=np.zeros(G.K) if start is None else np.load(start)
  elif it%3==0:z=bestz+rng.normal(size=G.K)*.03
  else:z=np.r_[rng.normal(size=5)*.2,rng.normal(size=3)*.15,np.zeros(G.K-8)]
  lo=np.r_[[-1.2]*2,[-1.5]*3,[-.65]*3,[-.2]*(G.K-8)];hi=-lo;z=np.clip(z,lo+1e-5,hi-1e-5);t=time.time()
  r=least_squares(G.fun,z,jac=G.jac,bounds=(lo,hi),max_nfev=maxeval,ftol=1e-10,xtol=1e-10,gtol=1e-10,x_scale='jac');v,j,s=G.evaluate(r.x);row={'start':it,'nfev':r.nfev,'success':bool(r.success),'message':r.message,'x':r.x.tolist(),'seconds':time.time()-t,**s};tr.append(row)
  print(json.dumps(row),flush=True);(HERE/(tag+'.json')).write_text(json.dumps(tr,sort_keys=True,separators=(',',':')))
  if row['cost']<best:best=row['cost'];bestz=r.x.copy();np.save(HERE/(tag+'.npy'),bestz)
  if len(s['S'])==len(s['U'])==1 and s['node_geometry_valid']:break
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--tag',default='GLOBAL1');p.add_argument('--starts',type=int,default=12);p.add_argument('--seed',type=int,default=59831);p.add_argument('--maxeval',type=int,default=400);p.add_argument('--nodes',action='store_true');p.add_argument('--start');a=p.parse_args();run(a.tag,a.starts,a.seed,a.maxeval,a.nodes,a.start)
