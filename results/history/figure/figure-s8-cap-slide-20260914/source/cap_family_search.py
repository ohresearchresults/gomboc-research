"""Finite numerical search in piecewise-projective cap families; not a proof."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1'); os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse,json,time,sys,itertools
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.optimize import least_squares

class CapFamily:
 def __init__(self,report):
  self.data=json.loads(Path(report).read_text());self.P0=np.array([[float(Fraction(x)) for x in row] for row in self.data['raw_vertices']]);self.faces=self.data['faces'];self.n=len(self.P0);self.nf=len(self.faces)
  self.edges=np.array(self.data['edges']);self.ef={}
  for f,cy in enumerate(self.faces):
   for a,b in zip(cy,cy[1:]+cy[:1]):self.ef.setdefault(tuple(sorted((a,b))),[]).append(f)
  self.ep=np.array(list(self.ef));self.ed=np.array(list(self.ef.values()));assert self.ep.shape==self.ed.shape
  self.src=np.r_[self.ep[:,0],self.ep[:,1]];self.dst=np.r_[self.ep[:,1],self.ep[:,0]];self.fs=np.r_[self.ed[:,0],self.ed[:,1]];self.fd=np.r_[self.ed[:,1],self.ed[:,0]]
  self.trip=np.array([[cy[0],cy[k],cy[k+1]] for cy in self.faces for k in range(1,len(cy)-1)]);self.ft=np.array([cy[:3] for cy in self.faces]);self.inc=np.zeros((self.nf,self.n),bool)
  for f,cy in enumerate(self.faces):self.inc[f,cy]=True
  adj=[set() for _ in range(self.n)]
  for a,b in self.edges:adj[a].add(int(b));adj[b].add(int(a))
  sets=set()
  for a in range(self.n):
   for c in range(a+1,self.n):
    for b,d in itertools.combinations(adj[a]&adj[c],2):sets.add(tuple(sorted((a,b,c,d))))
  caps=[]
  for sep in sorted(sets):
   un=set(range(self.n))-set(sep);cc=[]
   while un:
    stack=[un.pop()];comp=[]
    while stack:
     a=stack.pop();comp.append(a);new=adj[a]&un;un-=new;stack.extend(new)
    cc.append(sorted(comp))
   if len(cc)>1:
    cap=min(cc,key=len);rest=set(range(self.n))-set(cap)-set(sep)
    mixed=[f for f,cy in enumerate(self.faces) if set(cy)&set(cap) and set(cy)&rest]
    B=np.c_[self.P0[list(sep)],np.ones(4)].T
    if not mixed and abs(np.linalg.det(B))>1e-8:caps.append(dict(sep=list(sep),cap=cap))
  # Keep two disjoint pockets and the largest pocket; avoid redundant inner charts.
  self.caps=[z for z in caps if len(z['cap'])<=2 or len(z['cap'])==max(len(x['cap']) for x in caps)]
  self.nshape=3*len(self.caps);self.dim=self.nshape+8;self.calls=0;self.bestkey=None
  self.last=None
 def points(self,z):
  P=self.P0.copy();denmins=[]
  for k,cap in enumerate(self.caps):
   B=np.c_[P[cap['sep']],np.ones(4)].T;M=(B*np.exp(np.r_[z[3*k:3*k+3],0]))@np.linalg.inv(B)
   U=np.c_[P[cap['cap']],np.ones(len(cap['cap']))]@M.T;dd=U[:,3];denmins.append(float(dd.min()));dd=np.maximum(dd,1e-8);P[cap['cap']]=U[:,:3]/dd[:,None]
  t=z[self.nshape:self.nshape+3];dd=1+P@t;denmins.append(float(dd.min()));P=P/np.maximum(dd,1e-8)[:,None]
  a,b,s01,s02,s12=z[self.nshape+3:];A=np.array([[np.exp(a),s01,s02],[0,np.exp(b),s12],[0,0,np.exp(-a-b)]]);return P@A.T,denmins
 def evaluate(self,z):
  self.calls+=1;P,dens=self.points(z);tri=P[self.trip];D=np.einsum('ij,ij->i',tri[:,0],np.cross(tri[:,1],tri[:,2]));total=D.sum();c=np.einsum('i,ij->j',D,tri.sum(axis=1))/(4*total);P=P-c
  ftri=P[self.ft];N=np.cross(ftri[:,1]-ftri[:,0],ftri[:,2]-ftri[:,0]);N=N/np.linalg.norm(N,axis=1)[:,None];off=np.einsum('ij,ij->i',N,ftri[:,0]);Y=N/np.maximum(off,1e-8)[:,None]
  gaps=off[:,None]-N@P.T;gaps[self.inc]=np.inf;ming=gaps.min(axis=1)
  roots=[];top=[]
  for X,src,dst in [(P,self.src,self.dst),(Y,self.fs,self.fd)]:
   e=X[dst]-X[src];cos=np.einsum('ij,ij->i',X[src],e)/(np.linalg.norm(X[src],axis=1)*np.linalg.norm(e,axis=1));tt=np.full(len(X),-np.inf);np.maximum.at(tt,src,cos);root=int(np.argmax(np.sum(X*X,axis=1)));roots.append(root);tt[root]=1;top.append(tt)
  v=np.r_[top[0],top[1]];res=np.r_[np.minimum(v-1e-7,0),30*np.minimum(ming-1e-9,0),30*np.minimum(off-1e-7,0),30*np.minimum(np.array(dens)-1e-5,0)]
  st=dict(P=P,c=c,N=N,off=off,Y=Y,ming=ming,dens=dens,top=top,roots=roots,volume=total/6,res=res)
  return st
 def residual(self,z):
  try:
   st=self.evaluate(z);r=st['res'];return np.nan_to_num(r,nan=1e6,posinf=1e6,neginf=-1e6)
  except (ValueError,ZeroDivisionError,np.linalg.LinAlgError):return np.full(self.n+3*self.nf+len(self.caps)+1,1e6)
 def report(self,z):
  s=self.evaluate(z);P=s['P'];H=[]
  for (i,j),(f,h) in zip(self.ep,self.ed):
   e=P[j]-P[i];u=-P[i]@e/(e@e);foot=P[i]+u*e;n,nn=s['N'][[f,h]];k=np.cross(n,nn);kk=k@k
   if min(u,1-u,np.cross(foot,nn)@k/kk,np.cross(n,foot)@k/kk)>1e-10:H.append([int(i),int(j)])
  U=np.where(s['top'][0]<0)[0].tolist()+[s['roots'][0]];S=np.where(s['top'][1]<0)[0].tolist()+[s['roots'][1]]
  return dict(counts=[len(S),len(U),len(H)],S=sorted(S),U=sorted(U),H=H,roots=s['roots'],loss=float(np.linalg.norm(s['res'])),min_escape=float(min(x.min() for x in s['top'])),min_gap=float(s['ming'].min()),min_off=float(s['off'].min()),min_den=float(min(s['dens'])),centroid=s['c'].tolist(),volume=float(s['volume']),z=np.array(z).tolist(),caps=self.caps)

def main():
 p=argparse.ArgumentParser();p.add_argument('report');p.add_argument('out');p.add_argument('--starts',type=int,default=50);p.add_argument('--evals',type=int,default=200);p.add_argument('--seed',type=int,default=140926);a=p.parse_args();out=Path(a.out);out.mkdir(exist_ok=False);m=CapFamily(a.report);rng=np.random.default_rng(a.seed);zero=np.zeros(m.dim);base=m.report(zero);print('BASE',json.dumps(base),flush=True);(out/'BASE.json').write_text(json.dumps(base,sort_keys=True));best=(base['loss'],zero.copy());allr=[];clock=time.monotonic()
 low=np.r_[np.full(m.nshape,-1.),np.full(3,-1.2),[-.8,-.8,-1.5,-1.5,-1.5]];high=-low
 for k in range(a.starts):
  z=zero.copy() if k==0 else best[1]+rng.normal(size=m.dim)*10**rng.uniform(-3,-.5)
  z=np.clip(z,low+1e-6,high-1e-6)
  sol=least_squares(m.residual,z,bounds=(low,high),loss='linear',max_nfev=a.evals,ftol=1e-9,xtol=1e-10,gtol=1e-10)
  r=m.report(sol.x);r.update(start=k,nfev=sol.nfev);allr.append(r)
  with (out/'ALL.jsonl').open('a') as f:f.write(json.dumps(r,sort_keys=True)+'\n')
  good=r['min_gap']>1e-10 and r['min_off']>0 and r['min_den']>0
  if good and r['loss']<best[0]:best=(r['loss'],sol.x.copy());(out/'BEST.json').write_text(json.dumps(r,sort_keys=True));print('BEST',k,r['counts'],r['loss'],r['min_gap'],flush=True)
  if good and r['counts']==[1,1,0] and r['min_escape']>1e-8:(out/'NUMERICAL_110.json').write_text(json.dumps(r,sort_keys=True));print('NUMERICAL_110_REQUIRES_EXACT_VERIFICATION',flush=True);break
  print('END',k,r['counts'],r['loss'],r['min_gap'],'seconds',time.monotonic()-clock,flush=True)
 (out/'CONFIG.json').write_text(json.dumps(vars(a),sort_keys=True));print('FINITE_CAP_SEARCH_COMPLETE',len(allr),m.calls,flush=True)
if __name__=='__main__':main()
