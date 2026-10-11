"""Strict 1S/2U numerical retraction using rooted witness forests and own mass.
This is a nomination method, followed by exact rational hull audit when successful.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,argparse,time
from pathlib import Path
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from vertex_geometry import geometry
from support_geometry import escape

def persistent_root(g):
 X=g['Z'];aa=np.sum(X*X,axis=1);T=g['T'];edges=np.unique(np.sort(np.concatenate([T[:,[0,1]],T[:,[1,2]],T[:,[2,0]]]),axis=1),axis=0);i,j=edges.T;e=X[j]-X[i];ee=np.sum(e*e,axis=1);t=np.clip(-np.sum(X[i]*e,axis=1)/ee,0,1);h=np.sum((X[i]+t[:,None]*e)**2,axis=1);parent=np.arange(len(X));best=(-1,None)
 def find(k):
  while k!=parent[k]:parent[k]=parent[parent[k]];k=parent[k]
  return k
 for k in np.argsort(h)[::-1]:
  u,v=find(i[k]),find(j[k])
  if u==v:continue
  if (aa[u],u)>(aa[v],v):u,v=v,u
  parent[u]=v;b=aa[u]-h[k]
  if b>best[0]:best=(b,int(u))
 return [int(aa.argmax()),best[1]]

def forest(A,roots):
 aa=np.sum(A*A,axis=1);e=A[None]-A[:,None];ee=np.sum(e*e,axis=2);q=np.einsum('ic,ijc->ij',A,e)/np.sqrt(np.maximum(aa[:,None]*ee,1e-60));np.fill_diagonal(q,-np.inf)
 cap=np.full(len(A),-np.inf);cap[roots]=np.inf;used=np.zeros(len(A),bool);parent=np.full(len(A),-1,int)
 for _ in range(len(A)):
  u=int(np.argmax(np.where(used,-np.inf,cap)));used[u]=True;new=np.minimum(cap[u],q[:,u]);take=(new>cap)&(~used);cap[take]=new[take];parent[take]=u
 for u in roots:parent[u]=int(q[u].argmax())
 return parent

def guards(g,roots,derivative=True):
 # Exact-equal floating facet equations represent a single nominated maximal plane.
 _,idx=np.unique(g['H'],axis=0,return_index=True);idx=np.sort(idx);H=g['H'][idx];DH=g['DH'][idx] if derivative else None
 out=[];JJ=[];classes=[]
 for A,DA,rr in [(g['Z'],g.get('DZ'),roots),(H,DH,[int(np.argmax(np.sum(H*H,axis=1)))])]:
  pp=forest(A,rr);keep=np.ones(len(A));keep[rr]=-1
  if derivative:v,j,J=escape(A,DA,angular=True,chosen=pp);JJ.append(J*keep[:,None])
  else:v,j=escape(A,angular=True,chosen=pp)
  v=v*keep;out.append(v)
  maximum,_=escape(A);classes.append(int(np.sum(maximum<0)))
 return np.r_[tuple(out)],np.vstack(JJ) if derivative else None,classes

def run(path,out,steps,eps):
 X=np.load(path);out=Path(out);out.mkdir(exist_ok=False,parents=True);np.save(out/'initial.npy',X);roots=persistent_root(geometry(X,False));(out/'roots.json').write_text(json.dumps(roots));trust=.001;hist=[];start=time.time()
 for it in range(steps):
  g=geometry(X);v,J,cl=guards(g,roots);res=np.maximum(eps-v,0);merit=float(res.sum());row=dict(it=it,merit=merit,minimum=float(v.min()),roots=roots,U=cl[0],S=cl[1],trust=trust,elapsed=time.time()-start);hist.append(row);print('POLISH',row,flush=True);(out/'history.json').write_text(json.dumps(hist,indent=2));np.save(out/'latest.npy',X)
  if not np.all(np.isfinite(J)):raise ValueError('nonfinite angular derivative: no numerical promotion')
  if cl==[1,1]:
   from goal_nomination import preserve
   preserve(X,out/f'goal_nomination_it{it}','actual S1U1 before121quota repair')
  if min(v)>eps*.8:
   np.save(out/'potential.npy',X);(out/'potential.json').write_text(json.dumps(row,indent=2));print('POTENTIAL_STRICT121',out,flush=True);break
  d=X.size;m=len(v);I=eye(d);O=csr_matrix((d,m));A=vstack([hstack([-csr_matrix(J),-eye(m),csr_matrix((m,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[v-eps,np.zeros(2*d)];obj=np.r_[np.zeros(d),np.ones(m),np.full(d,1e-7)]
  sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*d+[(0,None)]*m+[(0,None)]*d,method='highs')
  if not sol.success:row['error']=sol.message;trust*=.5;continue
  dx=sol.x[:d].reshape(X.shape);accepted=False
  for alpha in [1.,.5,.25,.125,.0625,.03125,.015625,.0078125,.00390625]:
   xx=X+alpha*dx;gg=geometry(xx,False);vv,_,cc=guards(gg,roots,False);mm=np.maximum(eps-vv,0).sum()
   if cc==[1,1]:
    from goal_nomination import preserve
    preserve(xx,out/f'goal_nomination_it{it}_alpha{alpha:g}','actual S1U1 in121retraction line search')
   if np.isfinite(mm) and mm<merit*(1-1e-5):X=xx;accepted=True;row['alpha']=alpha;break
  if accepted and alpha>.99:trust=min(trust*1.2,.02)
  if not accepted:trust*=.4
  if trust<1e-11:break
 print('POLISH_END',out,hist[-1],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--steps',type=int,default=300);p.add_argument('--epsilon',type=float,default=1e-6);a=p.parse_args();run(a.input,a.output,a.steps,a.epsilon)
