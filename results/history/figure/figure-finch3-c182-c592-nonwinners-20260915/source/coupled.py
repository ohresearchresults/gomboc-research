"""Minimum-motion SQP with simultaneous chart/centroid variables.
Full S/U classes are numerical proposals only; fixed individual floors and all topology guards.
"""
import os,time,json,argparse
from pathlib import Path
import numpy as np
from scipy.optimize import minimize,linprog
from scipy.linalg import cholesky,solve_triangular
from model import Model,HERE

class Phase:
 def __init__(self,M,z):
  self.M=M;R=M.evaluate(z);self.ui,self.fi=M.choices(R)
  self.uv=np.array([i for i in range(len(M.labels)) if i!=M.root]);self.ff=np.array([i for i in range(len(M.F)) if i not in [9,104,M.stable]])
  self.um=np.maximum(1e-9,.1*R['u'][self.ui[self.uv]]);self.fm=np.maximum(1e-9,.1*R['f'][self.fi[self.ff]])
  self.rm=np.maximum(1e-7,.1*(-R['u'][M.u_indices[M.root]]));self.sm=np.maximum(1e-7,.1*(-R['f'][M.f_indices[M.stable]]))
  self.gm=np.maximum(1e-11,.05*R['s']);self.dm=np.maximum(1e-13,.05*R['det'])
 def constraints(self,R,allgeom=False):
  M=self.M;U=self.ui[self.uv];F=self.fi[self.ff]
  # Return sufficient selected strict witnesses and all small nonincidences.
  ix=np.flatnonzero((R['s']<.02)|(R['s']<5*self.gm)) if not allgeom else np.arange(len(R['s']))
  # side convexity and origin-based orientation are guarded by positive tetrahedral determinant.
  g=np.r_[R['u'][U]-self.um,R['f'][F]-self.fm,-R['u'][M.u_indices[M.root]]-self.rm,-R['f'][M.f_indices[M.stable]]-self.sm,R['s'][ix]-self.gm[ix],R['det']-self.dm]
  J=np.vstack((R['du'][U],R['df'][F],-R['du'][M.u_indices[M.root]],-R['df'][M.f_indices[M.stable]],R['ds'][ix],R['ddet']))
  return g,J
 def as_dict(self):
  return {k:getattr(self,k).tolist() for k in ['ui','fi','uv','ff','um','fm','rm','sm','gm','dm']}

def optimize(tag,steps=25,start=None,trust=.02):
 M=Model();z=np.r_[M.z0,M.m] if start is None else np.load(start);phase=Phase(M,np.r_[M.z0,M.m]);trace=[]
 if start is not None:
  old=Path(start).with_suffix('.phase.json')
  if old.exists():
   for k,v in json.load(open(old)).items():setattr(phase,k,np.array(v))
 R=M.evaluate(z);c,J=phase.constraints(R);print('INITIAL',M.summary(R),'gap',R['gap'],flush=True)
 for it in range(steps):
  t0=time.time();c,J=phase.constraints(R)
  W=R['dP'].reshape(-1,len(z)).T@R['dP'].reshape(-1,len(z))+.02*R['dq'].reshape(-1,len(z)).T@R['dq'].reshape(-1,len(z))+.00001*np.eye(len(z));W[-3:,-3:]+=np.eye(3)
  T=solve_triangular(cholesky(W,lower=True).T,np.eye(len(z)),lower=False);A=J@T;B=R['dgap']@T;gap=R['gap'];row=np.maximum(np.linalg.norm(A,axis=1),1e-5);An=A/row[:,None];cn=c/row
  # Solve convex quadratic model. Mechanical floors retain their initial identities.
  mu=.02
  H=B.T@B+mu*np.eye(len(z));grad=B.T@gap
  def fun(u):return .5*u@H@u+grad@u
  r=minimize(fun,np.zeros(len(z)),jac=lambda u:H@u+grad,method='SLSQP',constraints=[{'type':'ineq','fun':lambda u:cn+An@u,'jac':lambda u:An}],bounds=[(-trust,trust)]*len(z),options={'maxiter':120,'ftol':1e-13})
  dz=T@r.x;alpha=1.;accepted=False;oldmer=np.linalg.norm(gap)**2+1000*np.sum(np.minimum(c,0)**2)
  for ls in range(16):
   try:
    Q=M.evaluate(z+alpha*dz);cc,_=phase.constraints(Q,True);newmer=np.linalg.norm(Q['gap'])**2+1000*np.sum(np.minimum(cc,0)**2)
    # Permit small violations only during corrector, do not call this no-birth.
    if newmer<oldmer-1e-16 and cc.min()>-1e-6 and np.isfinite(newmer):accepted=True;break
   except (np.linalg.LinAlgError,ValueError,FloatingPointError):pass
   alpha*=.5
  data={'iteration':it,'accepted':accepted,'qp_success':bool(r.success),'qp_message':str(r.message),'qp_nit':int(r.nit),'alpha':alpha,'trust':trust,'gap':float(np.linalg.norm(R['gap'])),'guard_min':float(c.min()),'seconds':time.time()-t0}
  if accepted:
   z=z+alpha*dz;R=Q;data.update(after_gap=float(np.linalg.norm(R['gap'])),after_guard=float(cc.min()));np.save(HERE/(tag+'.npy'),z)
   if alpha>.9:trust=min(.1,trust*1.2)
  else:trust*=.4
  trace.append(data);print(json.dumps(data),flush=True)
  (HERE/(tag+'.trace.json')).write_text(json.dumps(trace,sort_keys=True));(HERE/(tag+'.phase.json')).write_text(json.dumps(phase.as_dict(),sort_keys=True))
  if trust<1e-7 or np.linalg.norm(R['gap'])<1e-8:break
 print('FINAL',M.summary(R),'gap',R['gap'],'own',M.summary(M.evaluate(z[:M.D])),flush=True)
 np.save(HERE/(tag+'.npy'),z)
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--tag',default='MASS1');a.add_argument('--steps',type=int,default=25);a.add_argument('--start');a.add_argument('--trust',type=float,default=.02);v=a.parse_args();optimize(v.tag,v.steps,v.start,v.trust)
