"""Refined physical halfspace search with <=84 submitted supports.

Four fixed source supports positively span R3, keeping every trial bounded.
All other supports are free. Every evaluation integrates the actual filled
intersection and both COMPLETE finite barcodes on its genuine primal/dual
edge graphs. Density is uniform, and no reference-centre test is promoted.
"""
import argparse,json,time,itertools
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
from support_geometry import geometry,escape
from persistence_birth import bars_loss

def evaluate(Q,eta):
 g=geometry(Q);owners={}
 for f,cy in enumerate(g['faces']):
  for i,j in zip(cy,cy[1:]+cy[:1]):owners.setdefault(tuple(sorted((i,j))),[]).append(f)
 pe=np.array(list(owners));qe=np.array(list(owners.values()));lp,GP,P=bars_loss(g['Z'],pe,eta);lq,GQ,R=bars_loss(g['H'],qe,eta);J=np.einsum('ic,icp->p',GP,g['DZ'])+np.einsum('ic,icp->p',GQ,g['DH']);info=dict(V=g['nv'],E=g['ne'],F=g['nf'],C_2E=2*g['ne'],VplusEplusF=g['nv']+g['ne']+g['nf'],Pmax=max(P,default=0.),Qmax=max(R,default=0.),P_count=len(P),Q_count=len(R),S=int(np.sum(escape(g['H'])[0]<0)),U=int(np.sum(escape(g['Z'])[0]<0)),mass=g['g'].tolist(),volume=float(g['V']),loss=lp+lq);return lp+lq,J.reshape(Q.shape),info

def refine(Q,n,seed):
 rng=np.random.default_rng(seed);moves=[]
 while len(Q)<n:
  h=ConvexHull(Q);T=h.simplices;X=-h.equations[:,:3]/h.equations[:,3,None];radius=np.linalg.norm(X,axis=1);weights=(radius/radius.max())**4+0.1;f=int(rng.choice(len(T),p=weights/weights.sum()));alpha=rng.dirichlet(np.full(3,2.));push=float(rng.uniform(.001,.025));p=(alpha@Q[T[f]])*(1+push);moves.append(dict(face=T[f].tolist(),barycentric=alpha.tolist(),radial_push=push));Q=np.vstack((Q,p))
 return Q,moves

def run(source,out,count,seed,steps):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);Q=np.load(source);g=geometry(Q,False);Q=g['H'];Q/=np.max(np.linalg.norm(Q,axis=1));score=-np.inf;fixed=None
 for ids in itertools.combinations(range(len(Q)),4):
  A=np.vstack((Q[list(ids)].T,np.ones(4)))
  try:w=np.linalg.solve(A,[0.,0.,0.,1.])
  except np.linalg.LinAlgError:continue
  if w.min()>score:score=float(w.min());fixed=ids
 assert score>.001;Q,moves=refine(Q,count,seed);assert len(Q)<=84;fixed=list(fixed);free=np.array([i for i in range(len(Q)) if i not in fixed]);np.save(out/'initial_Q.npy',Q);(out/'definition.json').write_text(json.dumps(dict(source=source,count=count,seed=seed,fixed_support_indices=fixed,positive_barycentric_minimum=score,refinement=moves,inequality='Q_i dot x <= 1; uniform density1',scope='optimizer nominations only'),indent=2));start=time.time();records=[]
 for stage,eta in enumerate([.3,.03,.003,.0003,.00003]):
  d=out/f'stage{stage}';d.mkdir();best=np.inf;calls=0;base=Q.copy()
  def fun(t):
   nonlocal best,calls
   calls+=1;Y=base.copy();Y[free]=t.reshape(-1,3);v,G,info=evaluate(Y,eta)
   if v<best:
    best=v;np.save(d/'best_Q.npy',Y);info.update(calls=calls,seconds=time.time()-start);(d/'best.json').write_text(json.dumps(info,indent=2))
   if info['S']==info['U']==1:
    np.save(d/f'potential_Q_{calls}.npy',Y);print('SUPPORT_PERSISTENCE_POTENTIAL_REQUIRES_EXACT',d,info,flush=True)
   if calls%1000==0:print('SUPPORT_PERSISTENCE',out,stage,calls,info['Pmax'],info['Qmax'],info['S'],info['U'],flush=True)
   return v,G[free].ravel()
  r=minimize(fun,Q[free].ravel(),jac=True,method='L-BFGS-B',options=dict(maxiter=steps,maxfun=10*steps,maxls=50,maxcor=30,ftol=1e-15,gtol=1e-10));Q=np.load(d/'best_Q.npy');inf=evaluate(Q,eta)[2];row=dict(stage=stage,eta=eta,message=r.message,nit=r.nit,calls=calls,**inf);records.append(row);(out/'stages.json').write_text(json.dumps(records,indent=2));print('SUPPORT_PERSISTENCE_STAGE',out,row,flush=True)
 np.save(out/'final_Q.npy',Q)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--count',type=int,default=84);p.add_argument('--seed',type=int,default=79501);p.add_argument('--steps',type=int,default=4000);p.add_argument('--check',action='store_true');a=p.parse_args()
 if a.check:
  Q=np.load(a.source);d=np.random.default_rng(9923).normal(size=Q.shape);d/=np.linalg.norm(d);v,J,inf=evaluate(Q,.03);rows=[]
  for h in [1e-6,1e-7,1e-8]:rows.append(dict(h=h,fd=(evaluate(Q+h*d,.03)[0]-evaluate(Q-h*d,.03)[0])/(2*h),analytic=float(np.sum(J*d))))
  Path(a.out).write_text(json.dumps(rows,indent=2));print(rows)
 else:run(a.source,a.out,a.count,a.seed,a.steps)
