"""Reference-chamber-first filled-volume moment closure on a rational contact chart.
Numerical proposal only: never a mechanical or geometric certificate.
Preserves positive escapes about a variable reference g while closing c(u)=g.
No int64 casts are used when saving exact rational inputs.
"""
import argparse,json,sys,time,copy
from pathlib import Path
import numpy as np
from scipy.linalg import svd
P=argparse.ArgumentParser();P.add_argument('source',type=Path);P.add_argument('seed',type=Path);P.add_argument('out',type=Path);P.add_argument('--steps',type=int,default=40);P.add_argument('--fixed-g',action='store_true');P.add_argument('--goal',type=float,default=1e-8);P.add_argument('--trust',type=float,default=.03);P.add_argument('--qp-seconds',type=float,default=12);P.add_argument('--inner',type=int,default=100);P.add_argument('--equality',action='store_true');P.add_argument('--reg',type=float,default=1e-6);a=P.parse_args()
sys.path[:0]=[str(a.source/'parent/mechanism'),str(a.source/'parent/mechanism/parent_sources')]
from atlas_opt import Atlas
from numeric import mechanics
from minnorm_qp import solve
D=json.loads((a.seed/'GENERATOR.json').read_text());fs=json.loads((a.seed/'faces.json').read_text());m=Atlas(D,fs)
g0=np.array([-0.012533688566502676,0.006279895492828624,-0.008889061183282553]);
if (a.seed/'REFERENCE.json').exists():
 rr=json.loads((a.seed/'REFERENCE.json').read_text());g0=np.array(rr['numerators'],float)/rr['denominator']
N=m.np+(0 if a.fixed_g else 3)
a.out.mkdir(parents=True,exist_ok=False)
(a.out/'CONFIG.json').write_text(json.dumps(dict(steps=a.steps,fixed_g=a.fixed_g,goal=a.goal,trust=a.trust,qp_seconds=a.qp_seconds,initial_g=g0.tolist(),svd_relative_cut=1e-11,gap_floor=1e-6,tetra_floor=1e-9,grid=10**14),indent=2))
(a.out/'faces.json').write_bytes((a.seed/'faces.json').read_bytes())

def state(y,jac=True,witnesses=None):
 u=y[:m.np];g=g0 if a.fixed_g else y[-3:];s=m.state(u,jac);q=s['q'];P=s['P'];x=P-g;h=1-q@g;n=q/h[:,None]
 def cosine(z):
  diff=z[None,:,:]-z[:,None,:];den=np.linalg.norm(z,axis=1)[:,None]*np.linalg.norm(diff,axis=2)
  v=np.einsum('ic,ijc->ij',z,diff)
  ans=np.divide(v,den,out=np.full_like(v,-np.inf),where=den>1e-14);np.fill_diagonal(ans,-np.inf);return ans
 cu,cs=cosine(x),cosine(n);uw=cu[m.ui].argmax(1);sw=cs[m.si].argmax(1)
 if witnesses is not None:sw,uw=witnesses
 vals=np.r_[cs[m.si,sw],cu[m.ui,uw]]
 s.update(witnesses=(sw,uw),g=g,refvals=vals,refh=h,refx=x,refn=n,r=s['c']-g)
 if jac:
  dq=np.zeros((len(q),3,N));dq[:,:,:m.np]=s['dq'];dp=np.zeros((len(P),3,N));dp[:,:,:m.np]=s['dP'];dg=np.zeros((3,N))
  if not a.fixed_g:dg[:,-3:]=np.eye(3)
  dh=-np.einsum('icp,c->ip',dq,g)-q@dg;dn=dq/h[:,None,None]-q[:,:,None]*dh[:,None,:]/h[:,None,None]**2;dx=dp-dg
  def derivative(z,dz,ii,jj):
   aa=z[ii];bb=z[jj]-aa;da=dz[ii];db=dz[jj]-da;aa2=np.einsum('ic,ic->i',aa,aa);bb2=np.einsum('ic,ic->i',bb,bb);den=np.sqrt(aa2*bb2);uv=np.einsum('ic,ic->i',aa,bb)
   duv=np.einsum('icp,ic->ip',da,bb)+np.einsum('icp,ic->ip',db,aa)
   return duv/den[:,None]-(uv/den)[:,None]*(np.einsum('icp,ic->ip',da,aa)/aa2[:,None]+np.einsum('icp,ic->ip',db,bb)/bb2[:,None])
  J=np.r_[derivative(n,dn,m.si,sw),derivative(x,dx,m.ui,uw)];dc=np.zeros((3,N));dc[:,:m.np]=s['dc'];dc-=dg
  s.update(refJ=J,dcg=dc,precondition=np.r_[dq.reshape(-1,N)/2,dp.reshape(-1,N),np.sqrt(len(P))*dg])
 return s

def save(y,prefix=''):
 z=copy.deepcopy(D);X=m.chart(y[:m.np],False);z['grid']=10**14
 # Dependent coordinates are immaterial inputs; use zero to keep exact source small.
 z['controls']=[[0,0,0] for _ in range(len(X))];z['controls'][m.n]=[0,0,z['grid']]
 for i,k in m.free:z['controls'][int(i)][int(k)]=int(round(float(X[i,k])*z['grid']))
 (a.out/(prefix+'GENERATOR.json')).write_text(json.dumps(z,sort_keys=True,separators=(',',':')))
 (a.out/(prefix+'REFERENCE.json')).write_text(json.dumps(dict(numerators=[int(round(float(t)*10**16)) for t in (g0 if a.fixed_g else y[-3:])],denominator=10**16),sort_keys=True,separators=(',',':')))
 (a.out/(prefix+'CONTROLS_FLOAT.json')).write_text(json.dumps(y.tolist(),separators=(',',':')))

y=m.u0.copy() if a.fixed_g else np.r_[m.u0,g0];hist=[];t0=time.monotonic()
# Finite difference check of analytic reference and mass derivatives at the first point.
s=state(y);rng=np.random.default_rng(481950);direction=rng.standard_normal(N);direction/=np.linalg.norm(direction);eps=1e-7
sp=state(y+eps*direction,False);sm=state(y-eps*direction,False)
# Witness switches can invalidate a max derivative check: mass derivative always smooth.
fd=(sp['r']-sm['r'])/(2*eps);err=np.linalg.norm(fd-s['dcg']@direction);assert err<1e-7,err
print('MASS_JACOBIAN_CHECK',err,flush=True)

def linear(s):
 _,dd,Vt=svd(s['precondition'],full_matrices=False,check_finite=False);good=dd>dd[0]*1e-11;W=Vt[good].T/dd[good]
 vi,qi=np.where((~m.inc)&(s['gaps']<.05));G=np.zeros((len(vi),N));G[:,:m.np]=m.gap_jac(s,vi,qi);T=np.zeros((len(s['det']),N));T[:,:m.np]=s['ddet']
 AA=np.r_[s['refJ'],G,T]@W;bb=np.r_[2*a.goal-s['refvals'],1e-6-s['gaps'][vi,qi],1e-9-s['det']]
 return W,AA,bb,s['dcg']@W

def violation(s,target):
 v=np.minimum(s['refvals']-1.5*a.goal,0);g=np.minimum(s['gaps'][~m.inc]-1e-6,0);t=np.minimum(s['det']-1e-9,0)
 return float(np.linalg.norm(np.r_[v,g,t,100*(s['r']-target)]))


from scipy.optimize import minimize
for it in range(a.steps):
 s=state(y);r0=float(np.linalg.norm(s['r']));wit=s['witnesses'];W,_,_,_=linear(s);K=W.shape[1];last={};best={'y':y.copy(),'r':r0};vi,qi=np.where((~m.inc)&(s['gaps']<.002));kk=np.flatnonzero(s['refvals']<.01);tt=np.flatnonzero(s['det']<.0001);rowScale=1/np.maximum(np.linalg.norm(np.r_[s['refJ'][kk]@W,m.gap_jac(s,vi,qi)@W[:m.np],s['ddet'][tt]@W[:m.np]],axis=1),1e-3)
 print('SLSQP_OUTER',it,'distance',r0,'dimension',K,'geometry_rows',len(vi),'initial_exit',s['refvals'].min(),flush=True)
 ybase=y.copy()
 def calc(z):
  if 'z' not in last or not np.array_equal(z,last['z']):
   st=state(ybase+W@z,True,wit);last.clear();last.update(z=z.copy(),s=st)
  return last['s']
 def obj(z):
  st=calc(z);r=st['r']/r0;J=st['dcg']@W/r0
  if a.equality:return .5*float(z@z),z
  return .0005*float(r@r)+a.reg/2*float(z@z),.001*r@J+a.reg*z
 def fun(z):
  st=calc(z);return rowScale*np.r_[st['refvals'][kk]-2*a.goal,st['gaps'][vi,qi]-1e-6,st['det'][tt]-1e-9]
 def jac(z):
  st=calc(z);return rowScale[:,None]*np.r_[st['refJ'][kk]@W,m.gap_jac(st,vi,qi)@W[:m.np],st['ddet'][tt]@W[:m.np]]
 def eq(z):return calc(z)['r']/r0
 def eqjac(z):return calc(z)['dcg']@W/r0
 counter=[0]
 def callback(z):
  st=calc(z);rr=float(np.linalg.norm(st['r']));gap=float(st['gaps'][~m.inc].min());ex=float(st['refvals'].min());dt=float(st['det'].min());counter[0]+=1
  if rr<best['r'] and ex>a.goal and gap>1e-6 and dt>1e-9 and st['refh'].min()>.2:
   best.update(y=ybase+W@z,r=rr);save(best['y'],'BEST_')
  if counter[0]%5==0:print('SLSQP_INNER',it,counter[0],rr,ex,gap,'best',best['r'],flush=True)
 con=[dict(type='ineq',fun=fun,jac=jac)]
 if a.equality:con.append(dict(type='eq',fun=eq,jac=eqjac))
 res=minimize(obj,np.zeros(K),jac=True,method='SLSQP',constraints=con,bounds=[(-a.trust,a.trust)]*K,callback=callback,options=dict(maxiter=a.inner,ftol=1e-13,disp=False))
 callback(res.x);hist.append(dict(outer=it,success=bool(res.success),message=str(res.message),iterations=int(res.nit),fun=float(res.fun),r_initial=r0,r_best=best['r'],inner=a.inner,regularization=a.reg,equality=a.equality));print('SLSQP_RESULT',hist[-1],flush=True)
 y=best['y'];save(y);(a.out/'HISTORY.json').write_text(json.dumps(hist,indent=2))
 if best['r']>=r0*.999999 or best['r']<1e-12:break
save(y);s=state(y,False);rep=mechanics(s['q'],fs,P=s['P'],tol=1e-13);rep.update(reference=s['g'].tolist(),reference_exit=float(s['refvals'].min()),centre_distance=float(np.linalg.norm(s['r'])))
(a.out/'NUMERICAL.json').write_text(json.dumps(rep,indent=2));print('FINAL',{k:rep[k] for k in ['V','E','F','counts','min_gap','reference_exit','centre_distance']},flush=True)
