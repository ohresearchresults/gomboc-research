"""Release one physical section vertex while retaining every nonincident plane.
The four incident quads may split, allowing C<=496 from the C488 rectangle.
Numerical counts are nominations; exact quad-preserving source audit is required.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from rectangular_sections import RectFamily
from vertex_geometry import geometry
from persistence_birth import evaluate

class Search:
 def __init__(self,f,q,index,out,eta):
  self.f=f;self.q=q;self.index=index;self.out=Path(out);self.out.mkdir(parents=True,exist_ok=False);self.eta=eta;self.last=None;self.calls=0;self.best=np.inf;self.start=time.time();self.history=[];self.keep=np.array([i for i,face in enumerate(f.faces) if index not in face]);(self.out/'source.json').write_text(json.dumps(dict(layers=f.L,index=index,kept_faces=self.keep.tolist(),source='literal base_params.npy plus released vertex offset'),indent=2));np.save(self.out/'base_params.npy',q)
 def calc(self,w):
  if self.last is not None and np.array_equal(w,self.last[0]):return self.last[1]
  q=w[:-3];offset=w[-3:];base=self.f.physical(q);Y=base['X'].copy();Y[self.index]+=offset;v,G,info=evaluate(Y,self.eta);DY=np.zeros((len(Y),3,len(w)));DY[:,:,:-3]=base['DX'];DY[self.index,:,-3:]=np.eye(3);J=np.einsum('ic,icp->p',G,DY)
  H=base['H'][self.keep];Z=Y[self.index]-base['g'];ineq=1-H@Z;dZ=DY[self.index].copy();dZ[:,:-3]-=base['Dg'];DI=-H@dZ;DI[:,:-3]-=np.einsum('fcp,c->fp',base['DH'][self.keep],Z);assert np.isfinite(v) and np.isfinite(J).all();data=(v,J,ineq,DI,Y,info,base);self.last=(w.copy(),data);self.calls+=1
  if min(ineq)>-1e-10 and v<self.best:
   self.best=v;np.save(self.out/'best_params.npy',w);np.save(self.out/'best_vertices.npy',Y);np.savez(self.out/'best_construction.npz',**base['construction'],released_vertex=self.index,released_offset=offset);info.update(min_unaffected_slack=float(min(ineq)),calls=self.calls,seconds=time.time()-self.start);(self.out/'best.json').write_text(json.dumps(info,indent=2))
  if max(info['Pmax'],info['Qmax'])<1e-12 and min(ineq)>-1e-10:
   np.savez(self.out/f'potential_construction_{self.calls}.npz',**base['construction'],released_vertex=self.index,released_offset=offset);print('HYBRID_POTENTIAL_REQUIRES_EXACT',self.index,info,flush=True)
  if self.calls%500==0:print('HYBRID',self.index,self.calls,info['Pmax'],info['Qmax'],min(ineq),flush=True)
  return data
 def run(self,iters):
  L=self.f.L;w=np.r_[self.q,np.zeros(3)];bounds=[(-4.,4.)]*L+[(-14.,6.)]*(4*L)+[(-3.,3.)]*2+[(-1.5,1.5),(-2.,2.)]+[(-1.,1.)]*3;cons=[dict(type='ineq',fun=lambda w:self.calc(w)[2],jac=lambda w:self.calc(w)[3])];r=minimize(lambda w:self.calc(w)[:2],w,jac=True,method='SLSQP',bounds=bounds,constraints=cons,options=dict(maxiter=iters,ftol=1e-11));(self.out/'termination.json').write_text(json.dumps(dict(message=r.message,nit=r.nit,success=bool(r.success)),indent=2));print('HYBRID_DONE',self.index,r.message,flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--index',type=int,required=True);p.add_argument('--layers',type=int,default=30);p.add_argument('--eta',type=float,default=.02);p.add_argument('--iterations',type=int,default=3500);p.add_argument('--check',action='store_true');a=p.parse_args();f=RectFamily(a.layers);q=np.load(a.input);s=Search(f,q,a.index,a.out,a.eta)
 if a.check:
  rng=np.random.default_rng(6152);w=np.r_[q,[1e-5,-2e-5,1e-5]];d=rng.normal(size=w.shape);d/=np.linalg.norm(d);f,J,c,DC,*_=s.calc(w)
  for h in [1e-5,1e-6,1e-7]:
   p1=s.calc(w+h*d);p2=s.calc(w-h*d);print('GRAD',h,(p1[0]-p2[0])/(2*h),J@d,'constraints',np.max(abs((p1[2]-p2[2])/(2*h)-DC@d)))
 else:s.run(a.iterations)
