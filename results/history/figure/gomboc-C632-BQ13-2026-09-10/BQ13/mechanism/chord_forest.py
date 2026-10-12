"""Whole-root-forest non-affine contact deformation with squared-chord normalization.
Numerical discovery only: an exact independent census is required for promotion.
"""
import sys,json,time,argparse
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'parent_sources'))
from atlas_opt import Atlas
from numeric import mechanics

def etas(z):
 diff=z[None,:,:]-z[:,None,:];ell=np.einsum('ijk,ijk->ij',diff,diff);uv=np.einsum('ic,ijc->ij',z,diff)
 out=np.divide(uv,ell,out=np.full_like(uv,-np.inf),where=ell>1e-20);np.fill_diagonal(out,-np.inf);return out

def eta_d(z,dz,ii,jj):
 a=z[ii];d=z[jj]-a;ell=np.einsum('ic,ic->i',d,d);uv=np.einsum('ic,ic->i',a,d);v=uv/ell
 if dz is None:return v
 da=dz[ii];dd=dz[jj]-da
 J=(np.einsum('icp,ic->ip',da,d)+np.einsum('ic,icp->ip',a,dd)-2*v[:,None]*np.einsum('ic,icp->ip',d,dd))/ell[:,None]
 return v,J

def prove_forest(p,root):
 for i in range(len(p)):
  j=i;seen=set()
  while j!=root:
   if j in seen:return False
   seen.add(j);j=p[j]
 return True

class Model:
 def __init__(self,g,fs,rootu=98,bad=105,outlet=111):
  self.m=Atlas(g,fs,stable=3,unstable=rootu);m=self.m;s=m.state(m.u0,False)
  self.sp=etas(s['n']).argmax(1);self.sp[3]=3
  self.up=etas(s['x']).argmax(1);self.up[rootu]=rootu;self.up[bad]=outlet
  assert prove_forest(self.sp,3) and prove_forest(self.up,rootu)
  self.bad=bad;self.target=len(m.si)+np.flatnonzero(m.ui==bad)[0]
  self.sourcec=s['c'];self.gbase=s['gaps'];self.eg=np.array(sorted(m.ef));d=s['P'][self.eg[:,1]]-s['P'][self.eg[:,0]];self.ell0=np.einsum('ij,ij->i',d,d)
 def state(self,u,jac=True):
  m=self.m;s=m.state(u,jac)
  if jac:
   h=s['h'];q=s['q'];dh=-np.einsum('icp,c->ip',s['dq'],s['c'])-q@s['dc'];dn=s['dq']/h[:,None,None]-q[:,:,None]*dh[:,None,:]/h[:,None,None]**2;dx=s['dP']-s['dc'][None,:,:]
   a,JA=eta_d(s['n'],dn,m.si,self.sp[m.si]);b,JB=eta_d(s['x'],dx,m.ui,self.up[m.ui]);s['etaJ']=np.vstack([JA,JB])
  else:a=eta_d(s['n'],None,m.si,self.sp[m.si]);b=eta_d(s['x'],None,m.ui,self.up[m.ui])
  s['eta']=np.r_[a,b];return s
 def basis(self,s):
  # Full primal and dual physical motions, not arbitrary chart-coordinate magnitudes.
  A=np.concatenate([s['dq'].reshape(-1,self.m.np)/2,s['dP'].reshape(-1,self.m.np)])
  U,d,Vt=svd(A,full_matrices=False,check_finite=False);assert d[-1]>1e-12
  return Vt.T/d
 def rows(self,s,W,floor,keepcent=False):
  m=self.m;vi,qi=np.where((~m.inc)&(s['gaps']<.08));G=m.gap_jac(s,vi,qi)
  # Exact geometry is checked at the endpoint; these floors are proposal guards.
  gf=np.maximum(1e-9,np.minimum(1e-6,self.gbase[vi,qi]*.01))
  mat=np.vstack([s['etaJ'],G]);val=np.r_[s['eta']-floor,s['gaps'][vi,qi]-gf]
  return mat@W,val
 def valid(self,s,floor,targmin=-np.inf):
  other=np.ones(len(floor),bool);other[self.target]=False
  if not(np.isfinite(s['eta']).all() and s['eta'][other].min()>0):return False
  if s['eta'][self.target]<targmin:return False
  if (s['eta']-floor)[other].min()<-1e-10:return False
  if s['gaps'][~self.m.inc].min()<1e-10 or s['det'].min()<=0 or s['h'].min()<=0:return False
  d=s['P'][self.eg[:,1]]-s['P'][self.eg[:,0]];ell=np.einsum('ij,ij->i',d,d)
  return np.min(ell/self.ell0)>1e-6
 def save(self,u,out):return self.m.save(u,out)

def linear(c,A,b,trust,aux=False):
 # A step <= b form supplied by caller.
 n=len(c);norm=np.maximum(np.linalg.norm(A,axis=1),1e-6)
 return linprog(c,A_ub=A/norm[:,None],b_ub=b/norm,bounds=[(-trust,trust)]*n,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9,'time_limit':4.})

def run(gen,faces,out,steps=150,trust=.002,keepcent=False,phase='death'):
 out=Path(out);out.mkdir(exist_ok=True,parents=True);mod=Model(gen,faces);m=mod.m;u=m.u0.copy();s=mod.state(u);e0=s['eta'];floor=np.minimum(2e-5,e0*.1);floor[mod.target]=-1e3
 target=mod.target;history=[];start=time.time()
 for it in range(steps):
  s=mod.state(u);value=s['eta'][target];history.append([it,float(value),float(np.min(np.delete(s['eta'],target))),float(s['gaps'][~m.inc].min()),float(trust)])
  mod.save(u,out/'LATEST.json');(out/'faces.json').write_text(json.dumps(faces,separators=(',',':')));(out/'parents.json').write_text(json.dumps({'uparent':mod.up.tolist(),'sparent':mod.sp.tolist()}));(out/'history.json').write_text(json.dumps(history));np.savez(out/'LATEST.npz',u=u,P=s['P'],q=s['q'],c=s['c'],X=s['X'])
  if it%5==0:print('FOREST',it,'sec',round(time.time()-start,2),'eta',value,'other',np.min(np.delete(s['eta'],target)),'gap',s['gaps'][~m.inc].min(),'trust',trust,flush=True)
  if value>2e-6:
   print('NUMERICAL_POSITIVE_FOREST',mechanics(s['q'],faces,tol=1e-12),flush=True);return mod,u,s,history
  W=mod.basis(s);J,v=mod.rows(s,W,floor);obj=-J[target];r=linear(obj,-J,v,trust)
  if not r.success:trust*=.5;print('LPFAIL',r.message,flush=True);continue
  direction=W@r.x;pred=-r.fun;accepted=False
  for ls in range(14):
   lam=2.**(-ls);un=u+lam*direction
   try:new=mod.state(un,False)
   except Exception:continue
   if new['eta'][target]<=value+1e-10:continue
   # Correct feasibility of the complete chosen forest and the current geometry.
   if not mod.valid(new,floor,value) and new['gaps'].min()>-.05:
    for rep in range(5):
     try:ss=mod.state(un);WW=mod.basis(ss);JJ,vv=mod.rows(ss,WW,floor*1.02)
     except Exception:break
     vv[target]=ss['eta'][target]-(value+max(1e-10,.05*lam*pred));n=m.np
     AA=np.vstack([np.column_stack([-JJ,np.zeros(len(vv))]),np.column_stack([np.eye(n),-np.ones(n)]),np.column_stack([-np.eye(n),-np.ones(n)])]);bb=np.r_[vv,np.zeros(2*n)]
     norms=np.maximum(np.linalg.norm(AA,axis=1),1e-6);rad=trust*lam*.7
     rr=linprog(np.r_[np.zeros(n),1],A_ub=AA/norms[:,None],b_ub=bb/norms,bounds=[(-rad,rad)]*n+[(0,rad)],method='highs',options={'primal_feasibility_tolerance':1e-9,'time_limit':3.})
     if not rr.success:break
     un+=WW@rr.x[:n]
     try:new=mod.state(un,False)
     except Exception:break
     if mod.valid(new,floor,value+1e-10):break
   if mod.valid(new,floor,value+max(1e-10,.0001*lam*pred)):
    u=un;accepted=True;trust=min(.03,trust*(1.4 if ls<2 else .6));break
  if not accepted:trust*=.4
  if trust<1e-9:break
 s=mod.state(u,False);mod.save(u,out/'LATEST.json');print('FOREST_END',s['eta'][target],mechanics(s['q'],faces,tol=1e-12),flush=True)
 return mod,u,s,history
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--out',default='forest');ap.add_argument('--steps',type=int,default=100);ap.add_argument('--trust',type=float,default=.002);ar=ap.parse_args()
 gen=json.loads((R/'C630_COORD_NONWINNER_OWN121.json').read_text());fs=json.loads((R/'start630/faces.json').read_text());run(gen,fs,R/ar.out,ar.steps,ar.trust)
