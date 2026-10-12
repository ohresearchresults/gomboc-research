"""Finite physical deformations localized by the dying POLAR radial component.

This moves literal primal vertices, with a frozen partition derived from the
source body's complete polar edge graph. All mass and equilibria are recomputed
on the resulting convex hull. Neither the old component nor its old carriers
are required to persist. The parameter family includes a global affine map and
an independently weighted affine displacement of the junior stable basin.
"""
import argparse,json,time,hashlib
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution,minimize
from vertex_geometry import geometry
from persistence_birth import evaluate

def partition(X,smoothing):
 g=geometry(X,False);A=g['H'];T=g['T'];owners={}
 for f,t in enumerate(T):
  for i,j in zip(t,np.roll(t,-1)):owners.setdefault(tuple(sorted((int(i),int(j)))),[]).append(f)
 ed=np.array(list(owners.values()));i,j=ed.T;e=A[j]-A[i];ee=np.sum(e*e,axis=1);tt=np.clip(-np.sum(A[i]*e,axis=1)/np.where(ee>0,ee,1),0,1);feet=A[i]+tt[:,None]*e;death=np.sum(feet*feet,axis=1);aa=np.sum(A*A,axis=1);par=np.arange(len(A));sets=[{k} for k in range(len(A))];best=(-1,None,None,None,None)
 def find(k):
  while k!=par[k]:par[k]=par[par[k]];k=par[k]
  return k
 for k in np.argsort(death)[::-1]:
  u,v=find(i[k]),find(j[k])
  if u==v:continue
  if (aa[u],u)>(aa[v],v):u,v=v,u
  dep=1-death[k]/aa[u]
  if dep>best[0]:best=(float(dep),int(u),int(v),sets[u].copy(),int(k))
  par[u]=v;sets[v]|=sets[u]
 dep,root,elder,B,k=best;assert dep>0 and root in B and elder not in B
 weights=np.zeros(len(X));degree=np.zeros(len(X));neigh=[set() for _ in X]
 for f,t in enumerate(T):
  degree[t]+=1
  if f in B:weights[t]+=1
  for a,b in zip(t,np.roll(t,-1)):neigh[a].add(int(b));neigh[b].add(int(a))
 assert np.all(degree>0)
 weights/=degree
 for _ in range(smoothing):weights=.5*weights+.5*np.array([np.mean(weights[list(ns)]) for ns in neigh])
 weights=(weights-weights.min())/(weights.max()-weights.min())
 return weights,dict(relative_Q=dep,root=root,elder=elder,dual_component=sorted(B),dual_saddle=ed[k].tolist(),weights=weights.tolist(),smoothing=smoothing)

def run(source,out,seed,iterations,eta,smoothing):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);g=geometry(np.load(source),False);X=g['Z'][g['vertices']];assert len(X)<=84;X/=np.max(np.linalg.norm(X,axis=1));w,meta=partition(X,smoothing);center=np.average(X,axis=0,weights=w);F=np.column_stack((X,w[:,None]*(X-center),w));F-=F.mean(0)
 # Orthogonal coordinates span the same physical family and balance its modes.
 u,s,v=np.linalg.svd(F,full_matrices=False);assert min(s)>1e-10;F=u*np.sqrt(len(X));meta.update(source=str(Path(source).resolve()),source_sha256=hashlib.sha256(Path(source).read_bytes()).hexdigest(),seed=seed,eta=eta,formula='convex_hull(source_vertices + basis @ coefficients); uniform density1',basis_span='global affine plus weighted junior-basin affine displacement',singular_values=s.tolist());np.save(out/'source_vertices.npy',X);np.save(out/'basis.npy',F);(out/'definition.json').write_text(json.dumps(meta,indent=2));d=F.shape[1]*3;calls=0;best=np.inf;start=time.time()
 def fun(t,gradient=False):
  nonlocal best,calls
  calls+=1;Y=X+F@t.reshape(-1,3);v,G,info=evaluate(Y,eta)
  if v<best:
   best=v;np.save(out/'best.npy',Y);np.save(out/'best_coefficients.npy',t);info.update(calls=calls,seconds=time.time()-start);(out/'best.json').write_text(json.dumps(info,indent=2))
  if max(info['Pmax'],info['Qmax'])<1e-12:
   np.save(out/f'potential{calls}.npy',Y);print('POLAR_BASIN_POTENTIAL_REQUIRES_EXACT',out,info,flush=True)
  if calls%10000==0:print('POLAR_BASIN',out,calls,best,info['Pmax'],info['Qmax'],flush=True)
  return (v,(F.T@G).ravel()) if gradient else v
 rng=np.random.default_rng(seed);pop=rng.normal(size=(128,d))*.025;pop[0]=0;bounds=[(-.35,.35)]*d
 de=differential_evolution(fun,bounds,init=pop,seed=seed,maxiter=iterations,polish=False,tol=1e-9,mutation=(.4,1.),recombination=.7,updating='immediate');r=minimize(lambda t:fun(t,True),np.load(out/'best_coefficients.npy'),jac=True,method='L-BFGS-B',bounds=bounds,options=dict(maxiter=6000,maxls=50,maxcor=25,ftol=1e-15,gtol=1e-10));(out/'termination.json').write_text(json.dumps(dict(global_message=de.message,local_message=r.message,calls=calls,seconds=time.time()-start),indent=2));print('POLAR_BASIN_DONE',out,json.loads((out/'best.json').read_text()),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--seed',type=int,default=74100);p.add_argument('--iterations',type=int,default=1000);p.add_argument('--eta',type=float,default=.03);p.add_argument('--smoothing',type=int,default=1);a=p.parse_args();run(a.input,a.out,a.seed,a.iterations,a.eta,a.smoothing)
