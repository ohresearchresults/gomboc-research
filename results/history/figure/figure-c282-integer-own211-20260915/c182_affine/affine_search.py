"""Bounded whole-affine-orbit exploration of the exact Finch C182 body.
The actual filled-volume centroid transforms affinely; it is never fitted.
Floating-point proposals only. Run exact audits before accepting a body.
"""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.optimize import minimize

def load(audit,raw):
 b=Path(audit).read_bytes();assert hashlib.sha256(b).hexdigest()=='caf78ccee9abec82174d346227b2da7d99a13b823c88a4ef405e3e8cb9d1967d';A=json.loads(b)
 b=Path(raw).read_bytes();assert hashlib.sha256(b).hexdigest()=='3a3d80e75979c004f995115dd4bfb491560af0f661af0840c6868f3b5f046d86';H=np.array(json.loads(b)['H'],float)
 g=np.array([float(F(v)) for v in A['raw_centroid']]);P=np.array([[float(F(v)) for v in p] for p in A['raw_vertices']])-g
 Q=H[A['active_input_indices'],:3];offset=H[A['active_input_indices'],3]-Q@g;Q=Q/offset[:,None]
 ep=[set() for _ in P];eq=[set() for _ in Q];edgefaces={}
 for i,j in A['edges']:ep[i].add(j);ep[j].add(i)
 for f,cy in enumerate(A['faces']):
  for i,j in zip(cy,cy[1:]+cy[:1]):edgefaces.setdefault(tuple(sorted((i,j))),[]).append(f)
 for pair in edgefaces.values():
  assert len(pair)==2;i,j=pair;eq[i].add(j);eq[j].add(i)
 w,V=np.linalg.eigh(P.T@P/len(P));W=np.diag(w**-.5)@V.T
 if np.linalg.det(W)<0:W[0]*=-1
 W/=np.linalg.det(W)**(1/3)
 return P,Q,ep,eq,W

class Escape:
 def __init__(self,X,adj):
  self.X=X;self.nei=np.array([sorted(a)+[i]*(max(map(len,adj))-len(a)) for i,a in enumerate(adj)]);self.mask=np.array([[True]*len(a)+[False]*(max(map(len,adj))-len(a)) for a in adj]);self.D=X[self.nei]-X[:,None,:]
 def evaluate(self,G,tau):
  X,D=self.X,self.D;xx=np.einsum('ni,ij,nj->n',X,G,X);dd=np.einsum('nki,ij,nkj->nk',D,G,D);xd=np.einsum('ni,ij,nkj->nk',X,G,D)
  den=np.sqrt(np.maximum(xx[:,None]*dd,1e-300));v=np.where(self.mask,xd/den,-np.inf);j=np.argmax(v,axis=1);ii=np.arange(len(X));scores=v[ii,j];root=int(np.argmin(scores));deficit=np.maximum(tau-scores,0.);deficit[root]=0
  d=D[ii,j];dd=dd[ii,j];den=den[ii,j];outer=lambda a,b:np.einsum('ni,nj->nij',a,b)
  grad=(outer(X,d)+outer(d,X))/(2*den[:,None,None])-scores[:,None,None]/2*(outer(X,X)/xx[:,None,None]+outer(d,d)/dd[:,None,None])
  return float(deficit@deficit),np.einsum('n,nij->ij',-2*deficit,grad),scores,root

def matrices(x):
 a,b=np.exp(x[0]),np.exp(x[1]);c=np.exp(-x[0]-x[1]);L=np.array([[a,x[2],x[3]],[0,b,x[4]],[0,0,c]])
 dL=np.zeros((5,3,3));dL[0,0,0]=a;dL[0,2,2]=-c;dL[1,1,1]=b;dL[1,2,2]=-c;dL[2,0,1]=1;dL[3,0,2]=1;dL[4,1,2]=1
 G=L.T@L;K=np.linalg.inv(G);dG=np.array([d.T@L+L.T@d for d in dL]);return L,G,K,dG

def main():
 p=argparse.ArgumentParser();p.add_argument('--audit',required=True);p.add_argument('--raw',required=True);p.add_argument('--out',required=True);p.add_argument('--starts',type=int,default=32);p.add_argument('--seed',type=int,default=182443);p.add_argument('--maxiter',type=int,default=250);p.add_argument('--tau',type=float,default=1e-5);a=p.parse_args()
 P,Q,ep,eq,W=load(a.audit,a.raw);pr=Escape(P@W.T,ep);du=Escape(Q@np.linalg.inv(W),eq)
 def evaluate(x,full=False):
  L,G,K,dG=matrices(x);up,ug,us,ur=pr.evaluate(G,a.tau);sp,sk,ss,sr=du.evaluate(K,a.tau);gradient=ug-K@sk@K;grad=np.einsum('ij,kij->k',gradient,dG)
  if full:return {'x':x.tolist(),'transform':(L@W).tolist(),'objective':up+sp,'S':int(sum(ss<0)),'U':int(sum(us<0)),'stable_ids':np.where(ss<0)[0].tolist(),'unstable_ids':np.where(us<0)[0].tolist(),'min_nonroot_S':float(np.min(np.delete(ss,sr))),'min_nonroot_U':float(np.min(np.delete(us,ur))),'condition':float(np.linalg.cond(L@W))}
  return up+sp,grad
 rng=np.random.default_rng(a.seed);x=np.array([.3,-.2,.1,.2,-.1]);f,grad=evaluate(x);eps=1e-6;num=np.array([(evaluate(x+eps*np.eye(5)[i])[0]-evaluate(x-eps*np.eye(5)[i])[0])/(2*eps) for i in range(5)]);assert np.max(np.abs(grad-num))<2e-6
 print('GRADIENT_CHECK',np.max(np.abs(grad-num)),flush=True)
 out=Path(a.out);out.mkdir(exist_ok=False,parents=True);rows=[];best=None
 for k in range(a.starts):
  x0=np.zeros(5) if k==0 else rng.normal(size=5)*np.array([.85,.85,1.3,1.3,1.3])
  r=minimize(evaluate,x0,jac=True,method='L-BFGS-B',bounds=[(-4,4),(-4,4),(-5,5),(-5,5),(-5,5)],options={'maxiter':a.maxiter,'maxls':60,'ftol':1e-14,'gtol':1e-9})
  t=evaluate(r.x,True);t.update(start=k,status=int(r.status),evaluations=int(r.nfev),initial=x0.tolist());rows.append(t)
  rank=(t['S']+t['U'],t['objective'])
  if best is None or rank<best[0]:best=(rank,t);(out/'BEST.json').write_text(json.dumps(t,sort_keys=True,separators=(',',':')));print('BEST',k,t['S'],t['U'],t['objective'],t['condition'],flush=True)
  (out/'SEARCH.json').write_text(json.dumps({'parameters':vars(a),'whitener':W.tolist(),'rows':rows},sort_keys=True,separators=(',',':')))
 print('C182_BOUNDED_AFFINE_SEARCH_ENDED',len(rows),'best',best[0],flush=True)
if __name__=='__main__':main()
