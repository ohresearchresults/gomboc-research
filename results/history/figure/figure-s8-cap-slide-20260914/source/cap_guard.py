"""Finite guarded cap continuation. All accepted records are numerical endpoints."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from cap_family_search import CapFamily
class Guard:
 def __init__(self,m,factor=.1):
  self.m=m;self.last=None;z=np.zeros(m.dim);s=m.evaluate(z);self.which=[];vals=[]
  for X,src,dst,root in [(s['P'],m.src,m.dst,s['roots'][0]),(s['Y'],m.fs,m.fd,s['roots'][1])]:
   e=X[dst]-X[src];cc=np.einsum('ij,ij->i',X[src],e)/(np.linalg.norm(X[src],axis=1)*np.linalg.norm(e,axis=1));ids=[int(np.where(src==i)[0][np.argmax(cc[src==i])]) for i in range(len(X)) if i!=root];self.which.append(ids);vals.extend(cc[ids])
  vals=np.array(vals);self.good=vals>0;self.bad=np.where(~self.good)[0];assert len(self.bad)==1
  self.floors=np.maximum(1e-8,np.minimum(factor*vals,1e-4));self.scale=np.maximum(1e-5,np.minimum(abs(vals),1e-2));self.initial=vals
 def state(self,z):
  if self.last is not None and np.array_equal(z,self.last[0]):return self.last[1]
  s=self.m.evaluate(z);vals=[]
  for X,src,dst,idx in [(s['P'],self.m.src,self.m.dst,self.which[0]),(s['Y'],self.m.fs,self.m.fd,self.which[1])]:
   a=src[idx];b=dst[idx];e=X[b]-X[a];vals.extend(np.einsum('ij,ij->i',X[a],e)/(np.linalg.norm(X[a],axis=1)*np.linalg.norm(e,axis=1)))
  vals=np.array(vals);ret=(s,vals);self.last=(z.copy(),ret);return ret
 def objective(self,z):return -100*self.state(z)[1][self.bad[0]]
 def constraints(self,z):
  s,v=self.state(z);return np.r_[(v[self.good]-self.floors[self.good])/self.scale[self.good],(s['ming']-1e-7)*100,(s['off']-.02),np.array(s['dens'])-.02]

def main():
 p=argparse.ArgumentParser();p.add_argument('report');p.add_argument('out');p.add_argument('--iterations',type=int,default=300);p.add_argument('--factor',type=float,default=.1);a=p.parse_args();out=Path(a.out);out.mkdir(exist_ok=False);m=CapFamily(a.report);g=Guard(m,a.factor);z=np.zeros(m.dim);hist=[];best=[g.objective(z),z.copy()];clock=time.monotonic()
 def callback(z):
  s,v=g.state(z);c=g.constraints(z);rec=dict(objective=g.objective(z),min_guard=float(c.min()),bad=float(v[g.bad[0]]),z=z.tolist());hist.append(rec)
  if c.min()>-1e-7 and rec['objective']<best[0]:best[:]=[rec['objective'],z.copy()];(out/'BEST.json').write_text(json.dumps(m.report(z),sort_keys=True));print('FEASIBLE',len(hist),rec['bad'],rec['min_guard'],flush=True)
  if len(hist)%20==0:print('STEP',len(hist),rec['bad'],rec['min_guard'],time.monotonic()-clock,flush=True)
 bounds=[(-1.,1.)]*m.nshape+[(-1.2,1.2)]*3+[(-.8,.8),(-.8,.8),(-1.5,1.5),(-1.5,1.5),(-1.5,1.5)]
 sol=minimize(g.objective,z,method='SLSQP',constraints={'type':'ineq','fun':g.constraints},bounds=bounds,callback=callback,options={'maxiter':a.iterations,'ftol':1e-11,'eps':2e-7,'disp':True})
 (out/'HISTORY.json').write_text(json.dumps(hist,sort_keys=True));r=m.report(best[1]);r['optimizer_success']=bool(sol.success);r['optimizer_message']=str(sol.message);r['which']=g.which;r['floors']=g.floors.tolist();(out/'ENDPOINT.json').write_text(json.dumps(r,sort_keys=True));(out/'CONFIG.json').write_text(json.dumps(vars(a),sort_keys=True));print('GUARDED_FINITE_CAP_ENDPOINT',r['counts'],r['min_escape'],r['min_gap'],flush=True)
if __name__=='__main__':main()
