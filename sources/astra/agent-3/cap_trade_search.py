"""Replace a stable carrier with one/two literal exterior cap points.

Explore both balanced persistence and an explicit S1-favouring objective to
permit trading the remaining stable-saddle pair for a smaller unstable-saddle
pair. All original mass and newly added convex cap volume are included.
"""
import argparse,json,time,hashlib
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution,minimize
from vertex_geometry import geometry
from persistence_birth import evaluate
from support_geometry import escape

def run(source,out,seed,count,qweight,iters):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);g=geometry(np.load(source),False);X=g['Z'][g['vertices']];X/=np.max(np.linalg.norm(X,axis=1));assert len(X)+count<=84;g=geometry(X,False);s=np.flatnonzero(escape(g['H'])[0]<0);assert len(s)==2;f=int(s[np.argmin(np.sum(g['H'][s]**2,axis=1))]);h=g['H'][f];foot=h/(h@h);n=foot/np.linalg.norm(foot);a=np.eye(3)[np.argmin(abs(n))];a-=n*(a@n);a/=np.linalg.norm(a);B=np.column_stack((a,np.cross(n,a),foot));np.save(out/'source_vertices.npy',X);np.save(out/'basis.npy',B);np.save(out/'foot.npy',foot);(out/'definition.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),source_sha256=hashlib.sha256(Path(source).read_bytes()).hexdigest(),seed=seed,cap_points=count,qweight=qweight,old_stable_facet=f,old_stable_vertices=g['T'][f].tolist(),formula='convex_hull(source_vertices union {foot + basis @ coefficient_i}); uniform density1'),indent=2));start=time.time();calls=0;best=np.inf;best121=np.inf;best211=np.inf;eta=.01
 def fun(t,gradient=False):
  nonlocal calls,best,best121,best211
  calls+=1;Y=np.vstack((X,foot+t.reshape(count,3)@B.T));v,G,info=evaluate(Y,eta)
  if qweight!=1:v+=(qweight-1)*info['Qloss']
  if qweight!=1 and gradient:
   from persistence_birth import bars_loss
   gg=geometry(Y);owners={}
   for f,tri in enumerate(gg['T']):
    for i,j in zip(tri,np.roll(tri,-1)):owners.setdefault(tuple(sorted((i,j))),[]).append(f)
   qe=np.array(list(owners.values()));lq,GQ,_=bars_loss(gg['H'],qe,eta);G+=(qweight-1)*np.einsum('fc,fcp->p',GQ,gg['DH']).reshape(Y.shape)
  if v<best:
   best=v;np.save(out/'best.npy',Y);np.save(out/'best_coefficients.npy',t);info.update(weighted_loss=float(v),calls=calls,seconds=time.time()-start);(out/'best.json').write_text(json.dumps(info,indent=2))
  if info['Qmax']<1e-12 and info['Pmax']<best121:
   best121=info['Pmax'];np.save(out/'best_S1.npy',Y);(out/'best_S1.json').write_text(json.dumps(info,indent=2))
  if info['Pmax']<1e-12 and info['Qmax']<best211:
   best211=info['Qmax'];np.save(out/'best_U1.npy',Y);(out/'best_U1.json').write_text(json.dumps(info,indent=2))
  if max(info['Pmax'],info['Qmax'])<1e-12:
   np.save(out/f'potential{calls}.npy',Y);print('CAP_TRADE_POTENTIAL_REQUIRES_EXACT',out,info,flush=True)
  if calls%5000==0:print('CAP_TRADE',out,calls,best,best121,best211,flush=True)
  return (v,(G[-count:]@B).ravel()) if gradient else v
 rng=np.random.default_rng(seed);bounds=[(-1.2,1.2),(-1.2,1.2),(1e-5,3.)]*count;pop=np.empty((72,3*count))
 for k in range(count):pop[:,3*k:3*k+2]=rng.normal(size=(72,2))*.15;pop[:,3*k+2]=np.exp(rng.uniform(np.log(.001),np.log(2.),72))
 de=differential_evolution(fun,bounds,init=pop,seed=seed,maxiter=iters,tol=1e-8,polish=False,recombination=.75,mutation=(.4,1.1));r=minimize(lambda t:fun(t,True),np.load(out/'best_coefficients.npy'),jac=True,method='L-BFGS-B',bounds=bounds,options=dict(maxiter=3000,maxls=50,ftol=1e-15,gtol=1e-10));(out/'termination.json').write_text(json.dumps(dict(global_message=de.message,local_message=r.message,calls=calls,seconds=time.time()-start),indent=2));print('CAP_TRADE_DONE',out,best,best121,best211,flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--seed',type=int,default=74500);p.add_argument('--count',type=int,choices=[1,2],default=2);p.add_argument('--qweight',type=float,default=1.);p.add_argument('--iterations',type=int,default=700);a=p.parse_args();run(a.input,a.out,a.seed,a.count,a.qweight,a.iterations)
