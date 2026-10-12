"""Finite, homogeneous, own-centroid edge-slide experiments."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
from fractions import Fraction
from pathlib import Path
import itertools,json,sys
import numpy as np
sys.set_int_max_str_digits(0)
class Slide:
 def __init__(self,report,u,w):
  self.d=json.loads(Path(report).read_text());self.P0=np.array([[float(Fraction(x)) for x in row] for row in self.d['raw_vertices']]);self.u=u;self.w=w;faces=[cy.copy() for cy in self.d['faces']];adj={j if i==u else i for i,j in self.d['edges'] if u in (i,j)};assert len(adj)==3 and w in adj;ab=sorted(adj-{w});self.ab=ab;missing=[i for i,cy in enumerate(faces) if u in cy and w not in cy];assert len(missing)==1;self.cut=missing[0];assert len(faces[self.cut])>=4;faces[self.cut].remove(u);tri=[ab[0],ab[1],u]
  # Outward direction of the new cap points toward the removed old vertex.
  P=self.P0.copy();P[u]=(P[u]+P[w])/2
  if np.cross(P[tri[1]]-P[tri[0]],P[tri[2]]-P[tri[0]])@(self.P0[u]-P[tri[0]])<0:tri=tri[::-1]
  faces.append(tri);self.faces=faces;self.tri=np.array([[cy[0],cy[i],cy[i+1]] for cy in faces for i in range(1,len(cy)-1)]);self.ft=np.array([cy[:3] for cy in faces]);self.ef={};self.inc=np.zeros((len(faces),len(P)),bool)
  for f,cy in enumerate(faces):
   self.inc[f,cy]=True
   for i,j in zip(cy,cy[1:]+cy[:1]):self.ef.setdefault(tuple(sorted((i,j))),[]).append(f)
  assert all(len(x)==2 for x in self.ef.values());self.ep=np.array(list(self.ef));self.ed=np.array(list(self.ef.values()));self.src=np.r_[self.ep[:,0],self.ep[:,1]];self.dst=np.r_[self.ep[:,1],self.ep[:,0]];self.fs=np.r_[self.ed[:,0],self.ed[:,1]];self.fd=np.r_[self.ed[:,1],self.ed[:,0]]
 def state(self,s):
  P=self.P0.copy();P[self.u]=(1-s)*P[self.u]+s*P[self.w];tri=P[self.tri];D=np.einsum('ij,ij->i',tri[:,0],np.cross(tri[:,1],tri[:,2]));total=D.sum();c=np.einsum('i,ij->j',D,tri.sum(axis=1))/(4*total);P=P-c;tt=P[self.ft];N=np.cross(tt[:,1]-tt[:,0],tt[:,2]-tt[:,0]);N/=np.linalg.norm(N,axis=1)[:,None];h=np.einsum('ij,ij->i',N,tt[:,0]);Y=N/h[:,None];gaps=h[:,None]-N@P.T;planarity=float(abs(gaps[self.inc]).max());gaps[self.inc]=np.inf
  tops=[];roots=[]
  for X,src,dst in [(P,self.src,self.dst),(Y,self.fs,self.fd)]:
   e=X[dst]-X[src];v=np.einsum('ij,ij->i',X[src],e)/(np.linalg.norm(X[src],axis=1)*np.linalg.norm(e,axis=1));top=np.full(len(X),-np.inf);np.maximum.at(top,src,v);tops.append(top);roots.append(np.where(top<0)[0].tolist())
  e=P[self.ep[:,1]]-P[self.ep[:,0]];u=-np.einsum('ij,ij->i',P[self.ep[:,0]],e)/np.einsum('ij,ij->i',e,e);foot=P[self.ep[:,0]]+u[:,None]*e;n,nn=N[self.ed[:,0]],N[self.ed[:,1]];k=np.cross(n,nn);kk=np.einsum('ij,ij->i',k,k);alpha=np.einsum('ij,ij->i',np.cross(foot,nn),k)/kk;beta=np.einsum('ij,ij->i',np.cross(n,foot),k)/kk;H=self.ep[(u>1e-10)&(u<1-1e-10)&(alpha>1e-10)&(beta>1e-10)].tolist()
  r=dict(s=float(s),V=len(P),E=len(self.ep),F=len(self.faces),counts=[len(roots[1]),len(roots[0]),len(H)],S=roots[1],U=roots[0],H=H,min_gap=float(gaps.min()),planarity=planarity,centroid=c.tolist(),volume=float(total/6),old_exit=float(tops[0][self.u]),max_S_violation=float(np.min(tops[1])))
  return r
if __name__=='__main__':
 report,out=sys.argv[1:];d=json.loads(Path(report).read_text());rows=[]
 for u in d['unstable_vertices']:
  adj=sorted({j if i==u else i for i,j in d['edges'] if u in (i,j)})
  if len(adj)!=3:continue
  for w in adj:
   m=Slide(report,u,w);old=None
   for s in np.unique(np.r_[np.linspace(.000001,.999999,501),np.logspace(-8,-3,20),1-np.logspace(-8,-3,20)]):
    r=m.state(float(s));r.update(u=u,w=w,cut=m.cut,ab=m.ab);rows.append(r)
    key=(r['counts'],r['S'],r['U'],r['H'])
    if key!=old:print('REGIME',u,w,s,r['counts'],r['S'],r['U'],r['H'],'gap',r['min_gap'],flush=True);old=key
    if r['counts']==[1,1,0] and r['min_gap']>1e-10:print('NUMERICAL_110_REQUIRES_EXACT_VERIFICATION',r,flush=True)
 Path(out).write_text(json.dumps(rows,sort_keys=True,separators=(',',':')))
