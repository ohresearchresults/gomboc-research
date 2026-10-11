"""Local physical realization chart preserving all selected-hull incidences.
The vertex/facet incidence graph is planar bipartite, hence3-degenerate. Peeling
nodes of degree<=3 and reversing gives linear contact reconstructions n.x=1.
Only free coordinate controls vary; each dependent coordinate is solved anew.
Strict nonincidence, bounded realization and exact final reconstruction matter.
"""
import sys,json,itertools,time
from pathlib import Path
from functools import partial
import numpy as np
from scipy.optimize import minimize
import jax
import jax.numpy as jnp
from gmpy2 import mpq
from support_persistence import ROOT,barcode
from selected_projective import load
from geometry import angular_scores
sys.set_int_max_str_digits(0)

def make(path,out,quality_floor=1e-3):
 X,Y,tri,eu,es,r=load(path);F=len(Y)
 center=np.array([float(mpq(v)) for v in r['raw_centroid']]);X=X-center;Y=Y/(1-Y@center)[:,None];u=int(np.argmax(np.sum(X*X,axis=1)));f=int(np.argmax(np.sum(Y*Y,axis=1)));radius=np.linalg.norm(X[u]);ez=X[u]/radius;ex=Y[f]-(Y[f]@ez)*ez;ex/=np.linalg.norm(ex);ey=np.cross(ez,ex);R=np.column_stack([ex,ey,ez]);X=X@R/radius;Y=Y@R*radius;X[u]=[0.,0.,1.];Y[f,1]=0.;A=np.r_[Y,X];N=len(A);pinned={F+u,f};adj=[set() for _ in range(N)]
 for fi,vs in enumerate(r['faces']):
  for v in vs:adj[fi].add(F+v);adj[F+v].add(fi)
 rem=set(range(N));peel=[]
 while rem:
  poss=[i for i in rem if i not in pinned and len(adj[i]&rem)<=3] if len(rem)>2 else ([f] if f in rem else [F+u]);assert poss,'not3degenerate'
  # Prefer a well-conditioned local minor among equal degree candidates.
  options=[]
  for i in poss:
   deps=sorted(adj[i]&rem);degree=len(deps);quality=1. if not deps else np.linalg.svd(A[deps],compute_uv=False)[-1]/max(np.linalg.norm(A[deps]),1e-30);options.append((quality<quality_floor,-degree,-quality,i,deps))
  _,_,_,i,deps=min(options);peel.append((i,deps));rem.remove(i)
 plan=[];free=[];layers={};depth={}
 for i,deps in reversed(peel):
  d=len(deps)
  if d:
   axes=max(itertools.combinations(range(3),d),key=lambda a:abs(np.linalg.det(A[np.ix_(deps,a)])));quality=abs(np.linalg.det(A[np.ix_(deps,axes)]));assert quality>1e-14
  else:axes=()
  fixed={0:0,1:0,2:1} if i==F+u else ({1:0} if i==f else {});assert not set(fixed)&set(axes);rest=[k for k in range(3) if k not in axes and k not in fixed];indices=list(range(len(free),len(free)+len(rest)));free.extend((i,k) for k in rest);lev=0 if not deps else 1+max(depth[j] for j in deps);depth[i]=lev;layers.setdefault((lev,d,len(rest),tuple(sorted(fixed.items()))),[]).append((i,deps,list(axes),rest,indices));plan.append(dict(node=i,deps=deps,axes=list(axes),free_axes=rest,free_indices=indices,fixed={str(k):v for k,v in fixed.items()}))
 levels=[]
 for key,group in sorted(layers.items()):
  level,degree,nfree,fixed=key;levels.append(dict(level=level,degree=degree,free_count=nfree,fixed=list(fixed),nodes=[g[0] for g in group],deps=[g[1] for g in group],axes=[g[2] for g in group],rest=[g[3] for g in group],indices=[g[4] for g in group]))
 incidence=np.zeros((F,len(X)),bool)
 for fi,vs in enumerate(r['faces']):incidence[fi,vs]=True
 meta=dict(source=str(path),quality_floor=quality_floor,peeling_policy='degree-with-explicit-minor-quality-floor',canonical_transform=dict(center=center.tolist(),R=R.tolist(),scale=1/radius,root_vertex=u,azimuth_facet=f),V=len(X),F=F,E=r['E'],nodes=N,free_coordinates=len(free),max_depth=max(depth.values()),plan=plan,levels=levels,faces=r['faces'])
 out.mkdir(exist_ok=True,parents=True);(out/'chart.json').write_text(json.dumps(meta,indent=2)+'\n');q=np.array([A[i,k] for i,k in free]);np.savez(out/'data.npz',q=q,A=A,tri=tri,eu=eu,es=es,incidence=incidence);print('CONTACT_CHART',dict(V=len(X),F=F,E=r['E'],nodes=N,free=len(free),depth=max(depth.values()),levels=len(levels)),flush=True)
 return meta,q,A,tri,eu,es,incidence

class Chart:
 def __init__(self,folder):
  self.folder=folder;self.meta=json.loads((folder/'chart.json').read_text());d=np.load(folder/'data.npz');self.q=d['q'];self.A=d['A'];self.tri=d['tri'];self.eu=d['eu'];self.es=d['es'];self.incidence=d['incidence'];self.F=self.meta['F'];F=self.F;N=self.meta['nodes'];tri=jnp.array(self.tri);groups=[]
  for g in self.meta['levels']:groups.append({k:jnp.array(v,dtype=int) if k not in ['level','degree','free_count','fixed'] else v for k,v in g.items()})
  def reconstruct(q):
   A=jnp.zeros((N,3),dtype=jnp.float64)
   for g in groups:
    ids=g['nodes'];d=g['degree'];rest=g['rest'];axes=g['axes'];vs=jnp.zeros((len(ids),3),dtype=jnp.float64)
    for axis,value in g['fixed']:vs=vs.at[:,axis].set(value)
    if g['free_count']>0:vs=vs.at[jnp.arange(len(ids))[:,None],rest].set(q[g['indices']])
    if d:
     dep=A[g['deps']];mat=jnp.take_along_axis(dep,axes[:,None,:],axis=2);rhs=1-jnp.sum(dep*vs[:,None,:],axis=2);sol=jnp.linalg.solve(mat,rhs[...,None]).squeeze(-1);vs=vs.at[jnp.arange(len(ids))[:,None],axes].set(sol)
    A=A.at[ids].set(vs)
   return A
  def physical(q):
   A=reconstruct(q);Y=A[:F];X=A[F:];a,b,c=X[tri[:,0]],X[tri[:,1]],X[tri[:,2]];six=jnp.sum(a*jnp.cross(b,c),axis=1);g=jnp.sum(six[:,None]*(a+b+c),axis=0)/(4*six.sum());Z=X-g;Q=Y/(1-Y@g)[:,None];gaps=1-Y@X.T
   return X,Y,Z,Q,g,six.sum()/6,gaps
  inc=jnp.array(self.incidence)
  def loss(q,bp,bw,bq,qw,tau,mu):
   X,Y,Z,Q,g,vol,gaps=physical(q)
   def bars(A,p,w):
    root,a,b=A[p[:,0]],A[p[:,1]],A[p[:,2]];d=b-a;t=jnp.clip(-jnp.sum(a*d,axis=1)/jnp.sum(d*d,axis=1),0,1);birth=jnp.sum(root*root,axis=1);depth=jnp.maximum(birth-jnp.sum((a+t[:,None]*d)**2,axis=1),0)*w/birth
    return jnp.where(tau<0,jnp.sum(depth*depth),jnp.log1p(depth/jnp.maximum(tau,1e-12)).sum())
   safe=jnp.where(inc,1,gaps);barrier=jnp.sum(jnp.where(inc,0,jnp.log1p(.01/safe)))/(F*self.meta['V']-int(self.incidence.sum()))
   return bars(Z,bp,bw)+bars(Q,bq,qw)+mu*barrier
  self.reconstruct=jax.jit(reconstruct);self.physical=jax.jit(physical);self.lossgrad=jax.jit(jax.value_and_grad(loss))
 def graph(self,q):
  X,Y,Z,Q,c,v,gaps=map(np.asarray,self.physical(q));minimum=float(gaps[~self.incidence].min());contact_error=float(np.max(abs(gaps[self.incidence])))
  if minimum<=0 or contact_error>1e-7 or v<=0 or not np.isfinite(X).all():raise ValueError('invalid physical contact realization')
  # Every integration fan triangle must retain the outward cyclic orientation.
  for f,face in enumerate(self.meta['faces']):
   a=X[face[0]]
   for k in range(1,len(face)-1):
    if np.cross(X[face[k]]-a,X[face[k+1]]-a)@Y[f]<=0:raise ValueError('degenerate or reversed true facet')
  bp,bw,p=barcode(Z,np.ones(len(Z)),self.eu);bq,qw,pq=barcode(Q,np.ones(len(Q)),self.es)
  return dict(X=X,Y=Y,Z=Z,Q=Q,c=c,v=float(v),minimum=minimum,contact_error=contact_error,bp=bp,bw=bw,bq=bq,qw=qw)
class Search:
 def __init__(self,chart,out,tau=-1,mu=1e-4):
  self.chart=chart;self.out=out;out.mkdir(exist_ok=True,parents=True);self.tau=tau;self.mu=mu;self.best=np.inf;self.calls=0;self.bestcount=1000;self.hist=[];self.target=False
 def eval(self,q):
  try:g=self.chart.graph(q)
  except (ValueError,np.linalg.LinAlgError):return 1e6,np.zeros_like(q)
  val,grad=self.chart.lossgrad(q,g['bp'],g['bw'],g['bq'],g['qw'],self.tau,self.mu);val=float(val);grad=np.asarray(grad)
  if not np.isfinite(val) or not np.isfinite(grad).all():return 1e6,np.zeros_like(q)
  self.calls+=1;u=angular_scores(g['Z']).max(1);s=angular_scores(g['Q']).max(1);row=dict(S=int((s<0).sum()),U=int((u<0).sum()),loss=val,minimum_noncontact=g['minimum'],contact_error=g['contact_error'],floor=float(min(np.sort(u)[1],np.sort(s)[1])),calls=self.calls,tau=self.tau,mu=self.mu)
  if val<self.best:self.best=val;np.save(self.out/'best_q.npy',q);(self.out/'best.json').write_text(json.dumps(row,indent=2)+'\n')
  if row['S']+row['U']<self.bestcount or self.calls%500==0:
   self.bestcount=min(self.bestcount,row['S']+row['U']);self.hist.append(row);(self.out/'history.json').write_text(json.dumps(self.hist,indent=2)+'\n');print('ATLAS',self.out,row,flush=True)
  if row['S']==row['U']==1 and row['floor']>1e-9:
   self.target=True;np.save(self.out/'NUMERICAL_NOMINATION_q.npy',q);(self.out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n')
  return val,grad
 def run(self,q,iters=1500):
  span=.1*np.maximum(abs(q),.2);bounds=list(zip(q-span,q+span));opt=minimize(self.eval,q,jac=True,method='L-BFGS-B',bounds=bounds,options={'maxiter':iters,'maxls':50,'maxcor':25,'gtol':1e-10,'ftol':1e-14});np.save(self.out/'final_q.npy',opt.x);print('ATLAS_DONE',self.out,opt.fun,opt.nit,opt.message,flush=True);return np.load(self.out/'best_q.npy')
