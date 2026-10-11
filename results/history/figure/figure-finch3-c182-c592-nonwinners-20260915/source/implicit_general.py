"""Full incidence-manifold own-mass optimization: no inherited hidden contacts.
Tangent corrections act jointly on every vertex and every support. Saved proposals
must be rationally reconstructed and exhaustively audited; iteration counts alone prove nothing.
"""
import os,json,time,argparse
import numpy as np
from scipy.linalg import qr,cho_solve,cho_factor
from model import dot,cross,norm,divide,HERE,Model
import radial
class Manifold:
 def __init__(self,P,q,faces):
  self.P0=P;self.q0=q;self.F=faces;self.V=len(P);self.n=len(q);self.K=3*(self.V+self.n);self.root=0;self.stable=114
  self.inc=np.array([(f,i) for f,cy in enumerate(faces) for i in cy]);mask=np.ones((len(q),len(P)),bool)
  for f,cy in enumerate(faces):mask[f,cy]=False
  self.non=np.array(np.where(mask)).T;E=sorted({tuple(sorted((i,j))) for cy in faces for i,j in zip(cy,cy[1:]+cy[:1])});self.E=np.array(E);self.ue=np.array([(a,b) for i,j in E for a,b in [(i,j),(j,i)]]);self.ui=[np.flatnonzero(self.ue[:,0]==i) for i in range(self.V)]
  self.side=np.array([(f,i,j) for f,cy in enumerate(faces) for i,j in zip(cy,cy[1:]+cy[:1])]);self.fi=[np.flatnonzero(self.side[:,0]==f) for f in range(self.n)];self.tris=np.array([(cy[0],cy[j],cy[j+1]) for cy in faces for j in range(1,len(cy)-1)])
 def con(self,z):
  P=z[:self.V*3].reshape(-1,3);q=z[self.V*3:].reshape(-1,3);f,i=self.inc.T;v=np.einsum('ni,ni->n',q[f],P[i])-1.;J=np.zeros((len(v)+3,self.K));rows=np.arange(len(v))
  for k in range(3):J[rows,3*i+k]=q[f,k];J[rows,3*self.V+3*f+k]=P[i,k]
  J[-3:,:3]=np.eye(3);return np.r_[v,P[0]-[0,0,1]],J
 def project(self,z,maxit=6):
  z=z.copy()
  for it in range(maxit):
   c,A=self.con(z)
   if np.max(abs(c))<1e-12:return z,True
   # Normal correction to the entire incidence system, including the anchor.
   try:d=A.T@cho_solve(cho_factor(A@A.T),-c)
   except np.linalg.LinAlgError:d=np.linalg.lstsq(A,-c,rcond=1e-12)[0]
   z+=d
  return z,np.max(abs(self.con(z)[0]))<1e-10
 def evaluate(self,z,T=None):
  P=z[:3*self.V].reshape(-1,3);q=z[3*self.V:].reshape(-1,3)
  if T is None:T=np.eye(self.K)
  K=T.shape[1];DP=T[:3*self.V].reshape(self.V,3,K);DQ=T[3*self.V:].reshape(self.n,3,K);X=P[self.tris];DX=DP[self.tris];v,dv=cross(X[:,1],X[:,2],DX[:,1],DX[:,2]);d,dd=dot(X[:,0],v,DX[:,0],dv);S=d.sum();DS=dd.sum(axis=0);B=np.einsum('n,ni->i',d,X.sum(axis=1));DB=np.einsum('nk,ni->ik',dd,X.sum(axis=1))+np.einsum('n,nik->ik',d,DX.sum(axis=1));g=B/(4*S);dg=(DB-4*g[:,None]*DS)/(4*S);Z=P-g;DZ=DP-dg
  i,j=self.ue.T;e=P[j]-P[i];de=DP[j]-DP[i];u,du=dot(Z[i],e,DZ[i],de);l,dl=norm(e,de);r,dr=norm(Z[i],DZ[i]);u,du=divide(u,l*r,du,dl*r[:,None]+dr*l[:,None]);f,i,j=self.side.T;e=P[j]-P[i];de=DP[j]-DP[i];v,dv=cross(Z[i],e,DZ[i],de);a,da=dot(q[f],v,DQ[f],dv);l,dl=norm(e,de);r,dr=norm(Z[i],DZ[i]);b,db=norm(q[f],DQ[f]);fs,dfs=divide(-a,l*r*b,-da,dl*(r*b)[:,None]+dr*(l*b)[:,None]+db*(l*r)[:,None]);f,i=self.non.T;s=1-np.einsum('ni,ni->n',q[f],P[i]);ds=-np.einsum('nik,ni->nk',DQ[f],P[i])-np.einsum('ni,nik->nk',q[f],DP[i]);return {'P':P,'q':q,'g':g,'volume':S/6,'u':u,'du':du,'f':fs,'df':dfs,'s':s,'ds':ds,'det':d,'ddet':dd}
 def res(self,R):
  ui=np.array([ix[np.argmax(R['u'][ix])] for ix in self.ui]);fi=np.array([ix[np.argmax(R['f'][ix])] for ix in self.fi]);U=ui[1:];F=fi[np.arange(self.n)!=self.stable];v=np.r_[1e-6-R['u'][U],1e-6-R['f'][F],1e-5+R['u'][ui[0]],1e-5+R['f'][fi[self.stable]]];J=np.vstack((-R['du'][U],-R['df'][F],R['du'][ui[0]],R['df'][fi[self.stable]]));sel=v>0;return v[sel],J[sel],{'S':np.flatnonzero(R['f'][fi]<0).tolist(),'U':np.flatnonzero(R['u'][ui]<0).tolist()}

def run(tag,start,steps,mu=1e-9,lam=.001):
 G=json.load(open(start));raw,P=radial.reconstruct(G);n=G['n_supports'];PP=np.array([[float(x) for x in r] for r in P]);qq=np.array([[float(__import__('fractions').Fraction(v,r[-1])) for v in r[:3]] for r in raw['H']]);M=Manifold(PP,qq,G['faces']);M.stable=G.get('stable_root',114);z=np.r_[PP.ravel(),qq.ravel()];R=M.evaluate(z,np.zeros((M.K,1)));sf=.02*R['s'];tf=.02*R['det'];trace=[]
 def objective(R):
  v,J,s=M.res(R)
  if (R['s']<=sf).any() or (R['det']<=tf).any():return np.inf
  return .5*v@v-mu*(np.log(R['s']-sf).sum()+np.log(R['det']-tf).sum())
 for it in range(steps):
  t=time.time();c,A=M.con(z);Q,RR=qr(A.T,mode='full');T=Q[:,len(c):];R=M.evaluate(z,T);v,J,stat=M.res(R);B=np.vstack((R['ds']/(R['s']-sf)[:,None],R['ddet']/(R['det']-tf)[:,None]));H=J.T@J+mu*B.T@B+lam*np.eye(T.shape[1]);b=-J.T@v+mu*B.sum(axis=0)
  try:u=cho_solve(cho_factor(H),b)
  except np.linalg.LinAlgError:u=np.linalg.lstsq(H,b,rcond=1e-12)[0]
  dz=T@u;a=min(1.,.2/max(np.linalg.norm(dz),1e-12));old=objective(R);ok=False
  for ls in range(24):
   zz,projected=M.project(z+a*dz)
   if projected:
    R2=M.evaluate(zz,np.zeros((M.K,1)));new=objective(R2)
    if np.isfinite(new) and new<old-1e-15:ok=True;break
   a*=.5
  row={'it':it,'accepted':ok,'alpha':a,'lambda':lam,'cost':float(old),'min_slack':float(R['s'].min()),'min_det':float(R['det'].min()),'max_contact':float(np.max(abs(c))),'class':stat,'seconds':time.time()-t}
  if ok:z=zz;lam=max(1e-9,lam*(.8 if a>.2 else 1.2))
  else:lam*=10
  trace.append(row);np.save(HERE/(tag+'.npy'),z);(HERE/(tag+'.trace.json')).write_text(json.dumps(trace,sort_keys=True,separators=(',',':')));print(json.dumps(row),flush=True)
  if lam>1e6:break
 PP=z[:M.V*3].reshape(-1,3);qq=z[M.V*3:].reshape(-1,3);out=radial.make(PP,qq,M.F,0,10**12,G.get('priority'));out['priority']=G.get('priority');out['parent_labels']=G.get('parent_labels');out['stable_root']=G.get('stable_root',114);(HERE/(tag+'_GENERATOR.json')).write_text(json.dumps(out,sort_keys=True,separators=(',',':')));print('END',M.res(M.evaluate(z,np.zeros((M.K,1))))[2],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--tag',default='IMP1');p.add_argument('--start',required=True);p.add_argument('--steps',type=int,default=60);p.add_argument('--mu',type=float,default=1e-9);p.add_argument('--lam',type=float,default=.001);a=p.parse_args();run(a.tag,a.start,a.steps,a.mu,a.lam)
