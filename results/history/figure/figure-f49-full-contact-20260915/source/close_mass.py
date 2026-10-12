"""Reference-chamber-first filled-volume moment closure on a rational contact chart.
Numerical proposal only: never a mechanical or geometric certificate.
Preserves positive escapes about a variable reference g while closing c(u)=g.
No int64 casts are used when saving exact rational inputs.
"""
import argparse,json,sys,time,copy
from pathlib import Path
import numpy as np
from scipy.linalg import svd
P=argparse.ArgumentParser();P.add_argument('source',type=Path);P.add_argument('seed',type=Path);P.add_argument('out',type=Path);P.add_argument('--steps',type=int,default=40);P.add_argument('--fixed-g',action='store_true');P.add_argument('--goal',type=float,default=1e-8);P.add_argument('--trust',type=float,default=.03);P.add_argument('--qp-seconds',type=float,default=12);a=P.parse_args()
sys.path[:0]=[str(a.source/'parent/mechanism'),str(a.source/'parent/mechanism/parent_sources')]
from atlas_opt import Atlas
from numeric import mechanics
from minnorm_qp import solve
D=json.loads((a.seed/'GENERATOR.json').read_text());fs=json.loads((a.seed/'faces.json').read_text());m=Atlas(D,fs)
g0=np.array([-0.012533688566502676,0.006279895492828624,-0.008889061183282553]);N=m.np+(0 if a.fixed_g else 3)
a.out.mkdir(parents=True,exist_ok=False)
(a.out/'CONFIG.json').write_text(json.dumps(dict(steps=a.steps,fixed_g=a.fixed_g,goal=a.goal,trust=a.trust,qp_seconds=a.qp_seconds,initial_g=g0.tolist(),svd_relative_cut=1e-11,gap_floor=1e-6,tetra_floor=1e-9,grid=10**14),indent=2))
(a.out/'faces.json').write_bytes((a.seed/'faces.json').read_bytes())

def state(y,jac=True):
 u=y[:m.np];g=g0 if a.fixed_g else y[-3:];s=m.state(u,jac);q=s['q'];P=s['P'];x=P-g;h=1-q@g;n=q/h[:,None]
 def cosine(z):
  diff=z[None,:,:]-z[:,None,:];den=np.linalg.norm(z,axis=1)[:,None]*np.linalg.norm(diff,axis=2)
  v=np.einsum('ic,ijc->ij',z,diff)
  ans=np.divide(v,den,out=np.full_like(v,-np.inf),where=den>1e-14);np.fill_diagonal(ans,-np.inf);return ans
 cu,cs=cosine(x),cosine(n);uw=cu[m.ui].argmax(1);sw=cs[m.si].argmax(1)
 vals=np.r_[cs[m.si,sw],cu[m.ui,uw]]
 s.update(g=g,refvals=vals,refh=h,refx=x,refn=n,r=s['c']-g)
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
for it in range(a.steps):
 s=state(y);norm=float(np.linalg.norm(s['r']));rec=dict(it=it,centre_distance=norm,min_reference_exit=float(s['refvals'].min()),min_gap=float(s['gaps'][~m.inc].min()),min_tetra=float(s['det'].min()),seconds=time.monotonic()-t0);hist.append(rec);print(rec,flush=True);save(y)
 (a.out/'HISTORY.json').write_text(json.dumps(hist,indent=2))
 if norm<1e-12 and s['refvals'].min()>a.goal:print('MASS_CLOSED_NUMERICAL_ONLY',flush=True);break
 _,dd,Vt=svd(s['precondition'],full_matrices=False,check_finite=False);good=dd>dd[0]*1e-11;W=Vt[good].T/dd[good];rec['chart_rank']=int(good.sum())
 vi,qi=np.where((~m.inc)&(s['gaps']<.05))
 G=np.zeros((len(vi),N));G[:,:m.np]=m.gap_jac(s,vi,qi);T=np.zeros((len(s['det']),N));T[:,:m.np]=s['ddet']
 AA=np.r_[s['refJ'],G,T]@W;bb=np.r_[1.1*a.goal-s['refvals'],1e-6-s['gaps'][vi,qi],1e-9-s['det']];E=s['dcg']@W
 accepted=False
 for k in range(8):
  alpha=2.**-k;delta,why=solve(AA,bb,E=E,r=-alpha*s['r'],bound=a.trust,tol=2e-12,seconds=a.qp_seconds,maxsteps=20000)
  print('QP',it,alpha,why,flush=True);rec.setdefault('qp',[]).append(dict(alpha=alpha,**why))
  if delta is None:continue
  for ls in range(20):
   h=2.**-ls;yn=y+h*W@delta
   try:sn=state(yn,False)
   except (ValueError,np.linalg.LinAlgError,FloatingPointError):continue
   if np.isfinite(sn['refvals']).all() and sn['refvals'].min()>a.goal and sn['gaps'][~m.inc].min()>1e-6 and sn['det'].min()>1e-9 and sn['refh'].min()>.2 and np.linalg.norm(sn['r'])<norm*(1-1e-4*h*alpha):
    y=yn;accepted=True;rec['accepted']=dict(alpha=alpha,backtracks=ls);print('ACCEPT',rec['accepted'],flush=True);break
  if accepted:break
 if not accepted:print('NO_ACCEPTED_FINITE_STEP',flush=True);break
save(y);s=state(y,False);rep=mechanics(s['q'],fs,P=s['P'],tol=1e-13);rep.update(reference=s['g'].tolist(),reference_exit=float(s['refvals'].min()),centre_distance=float(np.linalg.norm(s['r'])))
(a.out/'NUMERICAL.json').write_text(json.dumps(rep,indent=2));(a.out/'HISTORY.json').write_text(json.dumps(hist,indent=2));print('FINAL',rep,flush=True)
