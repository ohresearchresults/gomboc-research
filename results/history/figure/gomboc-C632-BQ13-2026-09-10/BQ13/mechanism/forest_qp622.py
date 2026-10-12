"""Minimum-material-motion continuation of the complete C630 drainage forest."""
import sys,json,time,argparse
from pathlib import Path
import numpy as np
from scipy.optimize import linprog,minimize,LinearConstraint,Bounds
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R));from chord_forest import Model
sys.path.insert(0,str(R/'parent_sources'));from numeric import mechanics

def qp(A,b,eq,rhs,rad,seed=None):
 # inequalities A*d >= b, equality eq*d=rhs; physical tangent coordinates
 norm=np.maximum(np.linalg.norm(A,axis=1),1e-12);AA=A/norm[:,None];bb=b/norm
 en=np.maximum(np.linalg.norm(eq,axis=1),1e-12);EE=eq/en[:,None];rr=rhs/en
 n=A.shape[1]
 res=minimize(lambda x:.5*x@x,np.zeros(n),jac=lambda x:x,method='SLSQP',constraints=[LinearConstraint(AA,bb,np.inf),LinearConstraint(EE,rr,rr)],bounds=Bounds(-rad,rad),options={'ftol':1e-12,'maxiter':12,'disp':False})
 x=res.x
 if np.min(AA@x-bb)<-2e-8 or np.max(abs(EE@x-rr))>2e-8:return None,'QP-inexact:'+str(res.message)
 return x,'QP:'+str(res.success)

class Controlled(Model):
 def eqrows(self,s,W):return s['dc']@W,self.sourcec-s['c']
 def constraints(self,s,W,floors,progress):
  J,val=super().rows(s,W,floors)
  val[self.target]=s['eta'][self.target]-progress
  a,b=self.eg.T;d=s['P'][b]-s['P'][a];dd=s['dP'][b]-s['dP'][a];ell=np.einsum('ic,ic->i',d,d);dl=2*np.einsum('ic,icp->ip',d,dd)
  J=np.vstack([J,dl@W]);val=np.r_[val,ell-.002*self.ell0]
  return J,-val
 def feasible(self,s,floors):
  a,b=self.eg.T;d=s['P'][b]-s['P'][a];ell=np.einsum('ic,ic->i',d,d)
  return self.valid(s,floors) and (ell-.002*self.ell0).min()>-1e-12

def run(out,steps=80,initial=None):
 out=Path(out);out.mkdir(exist_ok=True,parents=True);g=json.loads((R/'C622_chart/supports.json').read_text());fs=json.loads((R/'C622_chart/faces.json').read_text());mod=Controlled(g,fs,rootu=98,bad=103,outlet=114);m=mod.m;u=m.u0.copy();s=mod.state(u);floors=np.minimum(1e-4,s['eta']*.2);floors[mod.target]=-100
 
 if initial is not None:
  gg=json.loads(Path(initial).read_text());xx=np.array(gg['controls'],float)/gg['grid'];u=xx[m.free[:,0],m.free[:,1]]/m.scale
 history=[];start=time.time();delta=.005;rad=.006
 for it in range(steps):
  if time.time()-start>155:break
  s=mod.state(u);value=s['eta'][mod.target];history.append(dict(it=it,eta=float(value),other=float(np.min(np.delete(s['eta'],mod.target))),gap=float(s['gaps'][~m.inc].min()),centerr=float(np.linalg.norm(s['c']-mod.sourcec)),delta=delta,sec=time.time()-start));print('QPFOREST',history[-1],flush=True)
  mod.save(u,out/'LATEST.json');(out/'faces.json').write_text(json.dumps(fs,separators=(',',':')));(out/'parents.json').write_text(json.dumps(dict(up=mod.up.tolist(),sp=mod.sp.tolist())));(out/'history.json').write_text(json.dumps(history,indent=2));np.savez(out/'LATEST.npz',u=u,P=s['P'],q=s['q'],c=s['c'],X=s['X'])
  if value>1e-6:print('CANDIDATE',mechanics(s['q'],fs,tol=1e-12),flush=True);break
  W=mod.basis(s);goal=min(1e-3,value+delta);AA,bb=mod.constraints(s,W,floors*1.05,goal);eq,rhs=mod.eqrows(s,W);d,why=qp(AA,bb,eq,rhs,rad)
  if d is None:delta*=.5;print('STEP_FAIL',why,flush=True);continue
  accepted=False
  for ls in range(4):
   lam=2.**-ls;un=u+lam*(W@d);tgoal=value+.25*lam*(goal-value)
   try:new=mod.state(un,False)
   except Exception:continue
   if new['gaps'].min()<-.03:continue
   for rep in range(2):
    if mod.feasible(new,floors) and new['eta'][mod.target]>tgoal and np.linalg.norm(new['c']-mod.sourcec)<1e-11:break
    try:
     ss=mod.state(un);WW=mod.basis(ss);AAA,bbb=mod.constraints(ss,WW,floors*1.03,tgoal);e,r=mod.eqrows(ss,WW);cc,why=qp(AAA,bbb,e,r,rad*.4*lam)
     if cc is None:break
     un+=WW@cc;new=mod.state(un,False)
    except Exception:break
   if mod.feasible(new,floors) and new['eta'][mod.target]>tgoal and np.linalg.norm(new['c']-mod.sourcec)<1e-9:
    u=un;accepted=True;delta=min(.015,delta*(1.10 if ls==0 else .7));break
  if not accepted:delta*=.4
  if delta<1e-7:print('STOP_DELTA',flush=True);break
 s=mod.state(u,False);mod.save(u,out/'LATEST.json');np.savez(out/'END.npz',u=u,P=s['P'],q=s['q'],c=s['c'],X=s['X']);print('END',float(s['eta'][mod.target]),mechanics(s['q'],fs,tol=1e-12),flush=True);return mod,u
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--steps',type=int,default=80);a.add_argument('--out',default='qpforest');a.add_argument('--initial');p=a.parse_args();run(R/p.out,p.steps,p.initial)
