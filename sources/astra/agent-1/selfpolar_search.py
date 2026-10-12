"""Negatively self-polar add-and-cut search with actual-centroid cone-section balance.
Jensen arXiv:1902.00784 Theorem7.4/Corollary7.5 supplies the add/cut identity.
The 4D orthogonal section balance and optimization here are agent1 calculations.
Numerical exploration only; every requested result requires rational body audit.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json,pathlib,time,argparse
from geometry import halfspace_mesh,arrows,census
from scipy.spatial import QhullError
from persistence_search import pairs

def mass(X,tris):
 a=X[tris];v=np.einsum('ij,ij->i',a[:,0],np.cross(a[:,1],a[:,2]))/6
 V=v.sum();S=a.sum(1);g=(v[:,None]*S).sum(0)/(4*V)
 second=(np.einsum('i,ij,ik->jk',v,S,S)+np.einsum('i,ilj,ilk->jk',v,a,a))/(20*V)
 return V,g,second

def transform(X,b):
 t=np.linalg.norm(b)
 if t<1e-30:return X.copy()
 u=b/t;d=X@u;den=np.cos(t)-np.sin(t)*d
 if den.min()<=0:raise ValueError('section outside cone')
 return (X+((np.cos(t)-1)*d+np.sin(t))[:,None]*u)/den[:,None]

def mesh_indexed(X):
 m=halfspace_mesh(-X);distance=np.linalg.norm(m['X'][:,None]-X[None],axis=2);mp=distance.argmin(1)
 if distance.min(1).max()>1e-7 or len(set(mp))!=len(X) or len(m['X'])!=len(X):raise ValueError('not negative selfpolar')
 return m,mp,m['triangles'].copy() if False else mp[m['triangles']],mp[m['edges']]

def balance(X):
 m,mp,tr,ed=mesh_indexed(X)
 for it in range(15):
  V,g,M=mass(X,tr)
  if np.linalg.norm(g)<1e-12:break
  b=np.linalg.solve(np.eye(3)+5*M-4*np.outer(g,g),-g)
  accepted=False
  for k in range(15):
   try:Y=transform(X,b*2**-k);_,gg,_=mass(Y,tr)
   except ValueError:continue
   if np.linalg.norm(gg)<np.linalg.norm(g):X=Y;accepted=True;break
  if not accepted:raise ValueError('section balance failed')
 if np.linalg.norm(mass(X,tr)[1])>1e-10:raise ValueError('section centroid unresolved')
 return X

def stats(X):
 m,mp,tr,edges=mesh_indexed(X);V,g,M=mass(X,tr);Z=X-g;pair,h=pairs(Z,edges);rr=(Z*Z).sum(1);depths=(1-h[pair[:,1]]/rr[pair[:,0]]) if len(pair) else np.array([])
 u=int(np.sum(arrows(Z).max(1)<-1e-10));st=census(m)
 return dict(V=len(X),E=len(m['edges']),F=len(m['faces']),C=2*len(m['edges']),S=st['S'],U=st['U'],g=g.tolist(),normg=float(np.linalg.norm(g)),P=depths.tolist(),score=float(np.log1p(depths/.005).sum()),maxdepth=float(depths.max()) if len(depths) else 0)

def addcut(X,f,w,height):
 m,mp,tr,edges=mesh_indexed(X);ci=list(m['active']).index(f);cy=mp[m['faces'][ci]];y=w@X[cy]
 # -X_f.y=1; outward scaling sees only this facet up to the finite visibility limit.
 values=-X@y;others=np.delete(values,f);bound=min(5.,1/max(others.max(),1e-30))
 if bound<=1+1e-8:raise ValueError('empty visibility interval')
 lam=1+height*(bound-1);x=lam*y
 if not(-X@x)[f]>1 or np.max(np.delete(-X@x,f))>=1:raise ValueError('visibility failed')
 js=set()
 for i,j in edges:
  if i==f:js.add(j)
  if j==f:js.add(i)
 new=[]
 for j in sorted(js):
  t=(-1-x@X[f])/(x@(X[j]-X[f]));assert 0<t<1
  new.append(X[f]+t*(X[j]-X[f]))
 Y=np.vstack([np.delete(X,f,axis=0),new,x]);return balance(Y)

def seed(family='pyramid'):
 if family=='tetra':
  X=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],dtype=float)
  # Deterministic construction only; no objective/census search below C34.
  for f in (0,0):
   m,mp,tr,edges=mesh_indexed(X);cy=m['faces'][list(m['active']).index(f)]
   X=addcut(X,f,np.full(len(cy),1/len(cy)),.12)
  assert len(X)>=10
  return X
 n=9;a=1/np.sqrt(3);r=np.sqrt((1+a*a)/np.cos(np.pi/n));ang=np.arange(n)*2*np.pi/n
 X=np.c_[r*np.cos(ang),r*np.sin(ang),np.full(n,-a)];return np.vstack([X,[0,0,1/a]])

def run(out,seednum=42,rounds=12,trials=100,family="pyramid"):
 out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);rng=np.random.default_rng(seednum);X=seed(family);hist=[];t0=time.time()
 for r in range(rounds):
  st=stats(X);st.update(round=r,seconds=time.time()-t0);hist.append(st);print(json.dumps(st),flush=True);np.savez(out/f'round{r}.npz',X=X,Q=-X);(out/'history.json').write_text(json.dumps(hist,indent=2))
  if st['S']==st['U']==1:np.savez(out/'NOMINATION110.npz',X=X,Q=-X);return X
  m,mp,tr,edges=mesh_indexed(X);best=None;bestkey=None
  for k in range(trials):
   f=int(rng.integers(len(X)));cy=mp[m['faces'][list(m['active']).index(f)]]
   if len(X)+len(cy)>83:continue
   w=rng.dirichlet(np.full(len(cy),rng.choice([.08,.2,1.,3.])))
   try:Y=addcut(X,f,w,float(rng.uniform(.05,.999)));s=stats(Y)
   except (ValueError,AssertionError,np.linalg.LinAlgError,QhullError):continue
   key=s['score']+rng.uniform(0,.001)
   if bestkey is None or key<bestkey:bestkey=key;best=(Y,s,f,w.tolist())
  if best is None:break
  X=best[0];(out/f'choice{r}.json').write_text(json.dumps({'facet':best[2],'weights':best[3],'stats':best[1]},indent=2))
 return X
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);ap.add_argument('--seed',type=int,default=42);ap.add_argument('--trials',type=int,default=100);ap.add_argument('--rounds',type=int,default=12);ap.add_argument('--family',default='pyramid');a=ap.parse_args();run(a.out,a.seed,a.rounds,a.trials,a.family)
