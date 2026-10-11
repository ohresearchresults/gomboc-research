# J130 prescribed volume exchange, full mass equations and local gates — complete methods

Dependencies: att_e24d68f17ea7f7e16750_01 supplies exact130.py and the literal DETACHED_G6.txt; att_7454012a94b751afe3ba_01 supplies the CURRENT star130.py, not its initial or fixed-margin historical variants. This material adds all five complete source units below. No optimizer archive, C622 source or missing worker sandbox is needed. Exact proof of the six local gates is gates130.py in the primary material; these numerical sources explain and reproduce their nomination and the finite constructive tests.

Environment: Python3.13.5, NumPy2.3.5, SciPy1.17.0, OPENBLAS_NUM_THREADS=1. Numerical SLSQP and HiGHS outputs are not exact body classifications or general infeasibility certificates. star130.stats uses a1e-13 persistence display threshold; it is never the final census. Every positive depth counts in the primary exact engine. The local LP results were rationalized through a separate exact3x3 dual identity and positive gap, not by trusting a floating infeasible status.

## Finite formulas and interpretation

Use the independent stars and K_i,D_i defined in the primary. Under prescribed star-volume changes tau_i, exact endpoint mass closure is affine:
K_i.d_i=6 tau_i; sum tau_i=0; sum[(D_i+6 tau_i I)d_i+6 tau_i p_i]=0.
The ENTIRE interpolation additionally needs sum tau_i d_i=0. Without it, endpoint closure does not imply constant intermediate first moment. exchange130.py supports that extra segment constraint, but the executed12 pilots used segment=False. The quadratic guards are inner-majorized by their PSD positive parts. Positive phase-I slack is a finite inner-chart optimizer failure, NOT a proof that a general volume exchange cannot work.

free130.py instead keeps only total-volume closure linear and uses genuine nonlinear moment equations sum[D_i d_i+(K_i.d_i)(p_i+d_i)]/24=0 together with the TRUE quadratic guard matrices. It is a nonconvex numerical method, not a convex chart theorem. It retains selected physical outgoing witnesses and nonroot stable-facet escapes. New routes/carriers and centre changes are not globally excluded by it.

## Executed trials

Run `OPENBLAS_NUM_THREADS=1 python exchange130.py 45 0 .6`. Explicit tau45 values are -.0005,-.001,-.003,+.0005,+.001,+.003. Compensators either share the opposite change in proportion to |K_i| or put it entirely on the largest-|K_i| selected star. Both phases use at most70 iterations; phaseI ftol1e-10, phaseII1e-11, trust.6. All12 phase-I slacks were positive. Ordered distributed/largest pairs were:
-.0005: .01783939845/.01259680102;
-.001: .08944684665/.05169759431;
-.003: 1.09448568445/.67945119479;
+.0005: .002174174914/.002872515496;
+.001: .09599309709/.03427139848;
+.003: 1.4165888445/.70350258635.
No selected endpoint from those trials was promoted as an exact construction.

Run `OPENBLAS_NUM_THREADS=1 python free130.py DRIVER SEED` for pairs(45,0),(5,0),(38,0),(45,8),(45,11),(5,1),(5,7). All seven returned floating211 with no target-edge sign crossing. The respective main Q values were approximately.4622962763942099,.46210107570636116,.4600183629478286,.4616741220078586,.46266658040923025,.4621010757057237,.4621010748754204. The driver45 seeds8/11 include moving controller1; driver5 seeds1/7 release3/36 respectively, so these trials do change named non-neighbor carrier data relative to some local gates. They still do not constitute exclusions of those enlarged families. maxiter160,ftol1e-11,trust.6 and regularizer1e-7 are literal. Floating mass residuals near1e-16 are not exact certificates.

### Corrected outer-relaxation interpretation

lp130.py is preserved as a FAILED INTERPRETATION, not a proof. Its leading docstring calls it an outer relaxation, but it selected rows using the stored Q_+ matrix. A negative-semidefinite nonzero rawQ can have Q_+=0; the resulting affine inner constraint is NOT a necessary affine condition on the original geometry. Its24 driver/seed trials therefore cannot be used to exclude finite geometry. The inline correction and this paragraph override the erroneous heading. No scientific conclusion relies on those purported outer bounds.

outer130.py replaces that selection with genuinely affine raw hull inequalities and exact tangent necessary inequalities for convex physical guards. It builds coefficients rationally from literal coordinates and only then passes them to a floating LP. Its main three-driver run reported raw lower bounds approximately .00319612526548,.01426762062798,.0001305421819477 with the chosen global mass constraints. An initial JSON serialization failure after those calculations was corrected by e.convert; a second full main run is not claimed.

`OPENBLAS_NUM_THREADS=1 python localpilot130.py` was executed after preserving that correction. It recovers the six local nominations using only rows supported on the driver's three coordinates, with/without that local star-volume equality. All six numerical policy sets agree with the exact frozen gates. Lower bounds with fixed star volume are approximately.003196125265480047,.012922971020866675,.0001305421819477199 for drivers5,38,45; without ANY volume/moment constraint they are.001013916215515083,.011499358683598233,.00009812774817841326. The exact rational values, actual fixed centroid, necessary fixed labels and multipliers are in J130_GATES_REPORT.json generated by primary gates130.py. These are only opposite-edge, specified-neighbor/witness gates, NOT whole-Q or own110 impossibility theorems.

## Manifest and commands

exchange130.py6019B SHAd6594953576f973a606ab93c130e2bda3eec224ec7a19c69f05f42ac4c7df5c8
free130.py2537B SHAc4a9ef45d21d052ddd9d419704fa70556af92e16fc29b52ad2fdc11b01c59531
outer130.py3526B SHAb4d1432902591375dbed35606fed0be2246e051add3c478b75b4e987650a7732
lp130.py1153B SHA1f1f088d7aa4183824fa093abfe4c50ee7a28f120fdb278be44b08df45a30441
localpilot130.py1645B SHA86344f28ee976278417e853aa061f91ee45af25bd8a8f1c4eb7361b52819096e

Save exact text with one terminal newline. Commands above use only literal primary input and explicit driver/seed/policy settings; no sampled checkpoint is hidden. Output prefixes EXCHANGE_,FREE130_,OUTER130_PILOT,LOCAL130_PILOT and terminal J130_LOCAL_NOMINATION_FINISHED_NOT_EXACT identify numerical runs. Reports with elapsed times do not have deterministic hash claims. For exact verification run `OPENBLAS_NUM_THREADS=1 python gates130.py`; expected J130_GATES_PASS,15413-byte report SHAac1fbd153943bf061922c5bc218c1ab2920a548c7ba6ab534a04d72c16aeed88.

## File: exchange130.py
```python
#!/usr/bin/env python3
"""J130 prescribed star-volume exchange: endpoint volume and first moment close.
Unlike zero-star-volume cells, this convex affine slice need not preserve mass
at intermediate t. Full rational endpoint reconstruction is a separate step.
Uses all true quadratic hull guards and selected physical/polar guards.
"""
import json,sys,time
import numpy as np
from scipy.linalg import null_space
from scipy.optimize import minimize,linprog
import star130 as s

def prepare(X,driver,seed,trust=.3):
 # Reuse only the independent-set and witness selections of a zero-volume cell.
 nc=s.make_cell(X,driver,seed,trust);d=nc['d'];X=d['X'];ids=nc['selected'];F=d['F'];k=len(ids);m=3*k;where={v:i for i,v in enumerate(ids)}
 K=[];Ds=[]
 for i in ids:
  KK=np.zeros(3);DD=np.zeros((3,3));dd=0
  for t in F[np.any(F==i,axis=1)]:
   j=t.tolist().index(i);a,b=X[t[(j+1)%3]],X[t[(j+2)%3]];cr=np.cross(a,b);KK+=cr;dd+=X[i]@cr;DD+=np.outer(a+b,cr)
  K.append(KK);Ds.append(DD+dd*np.eye(3))
 return dict(nc=nc,X=X,ids=ids,F=F,K=np.array(K),Ds=np.array(Ds),where=where,driver=driver,seed=seed,trust=trust)

def affine_map(pre,tau,segment=False):
 ids,X,K,Ds=pre['ids'],pre['X'],pre['K'],pre['Ds'];k=len(ids);m=3*k;A=np.zeros((k+3+(3 if segment else 0),m));b=np.zeros(len(A))
 assert abs(sum(tau))<1e-12
 for j,i in enumerate(ids):
  A[j,3*j:3*j+3]=K[j];b[j]=6*tau[j]
  A[k:k+3,3*j:3*j+3]=Ds[j]+6*tau[j]*np.eye(3)
  b[k:k+3]-=6*tau[j]*X[i]
  if segment:A[k+3:,3*j:3*j+3]=tau[j]*np.eye(3)
 scales=np.linalg.norm(A,axis=1);nz=scales>1e-15;A=A[nz]/scales[nz,None];b=b[nz]/scales[nz]
 u=np.linalg.lstsq(A,b,rcond=None)[0];Z=null_space(A)
 assert np.linalg.norm(A@u-b)<1e-9
 base=X.copy();P=np.zeros((len(X),3,Z.shape[1]))
 for j,i in enumerate(ids):base[i]+=u[3*j:3*j+3];P[i]=Z[3*j:3*j+3]
 return base,P,u,Z

def make_constraints(pre,tau,segment=False):
 base,P,u,Z=affine_map(pre,tau,segment);d=pre['nc']['d'];ids=pre['ids'];X=base;F=pre['F'];root=pre['nc']['root'];sr=pre['nc']['sr'];target=pre['nc']['target'];driver=pre['driver'];p=P.shape[2]
 c0s=[];gs=[];Qs=[];kinds=[];targets=[]
 def put(c,g,Q,kind,margin):c0s.append(c+margin);gs.append(g);Qs.append(s.positive(Q));kinds.append(kind)
 for i,j in pre['nc']['parents'].items():
  a,b=X[i],X[j];A,B=P[i],P[j];rr=d['X'][i]@d['X'][i]
  c=a@(a-b)/rr;g=(A.T@(2*a-b)-B.T@a)/rr;Q=A.T@(A-B)/rr
  put(c,g,Q,'U',1e-7)
 for fi,t in enumerate(F):
  a,b,c=X[t];A,B,C=P[t];n=np.cross(b-a,c-a);D=np.cross((B-A).T,c-a).T+np.cross(b-a,(C-A).T).T
  h=n@a;hg=D.T@a+A.T@n;oldn=d['n'][fi];nn=oldn@oldn;norm=np.sqrt(nn)
  for j in range(len(X)):
   if j in t:continue
   c0=(n@X[j]-h)/norm;g=(D.T@X[j]+P[j].T@n-hg)/norm;Q=D.T@P[j]/norm
   put(c0,g,Q,'hull',1e-9)
  edges=[]
  for l in range(3):
   i,j=t[l],t[(l+1)%3];aa,bb=X[i],X[j];AA,BB=P[i],P[j];cr=np.cross(aa,bb);L=np.cross(AA.T,bb).T+np.cross(aa,BB.T).T
   edges.append((n@cr/nn,(D.T@cr+L.T@n)/nn,D.T@L/nn,i,j))
  if fi==target:
   targetdata=next(e for e in edges if driver not in e[-2:]);assert np.linalg.norm(targetdata[2])<1e-9
  elif fi==sr:
   for c,g,Q,_,_ in edges:put(-c,-g,-Q,'Sroot',1e-7)
  else:
   # The original body's witness is selected before changing volume, not from
   # an affine base which may be outside the feasible geometry.
   j=int(np.argmin(d['sg'][fi]));c,g,Q,_,_=edges[j];put(c,g,Q,'S',1e-7)
 return dict(base=base,P=P,u=u,Z=Z,f0=np.array(c0s),G=np.array(gs),M=np.array(Qs),kinds=kinds,target=targetdata,trust=pre['trust'],tau=tau,segment=segment)

def run(pre,tau,segment=False,maxiter=90):
 cc=make_constraints(pre,tau,segment);c,G,M=cc['f0'],cc['G'],cc['M'];n=G.shape[1];o,og=cc['target'][:2]
 def vals(z):return c+G@z+np.einsum('i,kij,j->k',z,M,z,optimize=True)
 def jac(z):return G+2*np.einsum('kij,j->ki',M,z,optimize=True)
 # Phase I convex slack problem; z=0 is not assumed feasible after volume exchange.
 def f1(y):return y[-1]+1e-8*(y[:-1]@y[:-1])
 def j1(y):return np.r_[2e-8*y[:-1],1.]
 def vc(y):return y[-1]-vals(y[:-1])
 def jc(y):return np.c_[-jac(y[:-1]),np.ones(len(c))]
 start=np.r_[np.zeros(n),max(0.,float(c.max()))+1e-5];bounds=[(-pre['trust'],pre['trust'])]*n+[(0.,None)]
 p1=minimize(f1,start,jac=j1,constraints=[dict(type='ineq',fun=vc,jac=jc)],bounds=bounds,method='SLSQP',options=dict(maxiter=maxiter,ftol=1e-10))
 if p1.x[-1]>1e-7:return None,dict(phase1=float(p1.x[-1]),success=False,iterations=int(p1.nit),tau=list(tau),selected=pre['ids'],driver=pre['driver'],seed=pre['seed'],segment=segment)
 p2=minimize(lambda z:o+og@z+1e-7*(z@z),p1.x[:-1],jac=lambda z:og+2e-7*z,constraints=[dict(type='ineq',fun=lambda z:-vals(z),jac=lambda z:-jac(z))],bounds=bounds[:-1],method='SLSQP',options=dict(maxiter=maxiter,ftol=1e-11))
 XX=cc['base']+np.einsum('ijk,k->ij',cc['P'],p2.x)
 report=dict(phase1=float(p1.x[-1]),success=bool(p2.success),iterations=int(p2.nit),max_inequality=float(vals(p2.x).max()),objective=float(o+og@p2.x),tau=list(tau),selected=pre['ids'],driver=pre['driver'],seed=pre['seed'],segment=segment,stats=s.stats(XX))
 return XX,report

def main():
 driver=int(sys.argv[1])if len(sys.argv)>1 else 45;seed=int(sys.argv[2])if len(sys.argv)>2 else 0;trust=float(sys.argv[3])if len(sys.argv)>3 else.6
 pre=prepare(s.load(),driver,seed,trust);allout=[]
 # Explicit prescribed-volume policies; positive controllers share the opposite
 # driver's volume in proportion to |K_i|, or one selected controller absorbs it.
 for tv in [-.0005,-.001,-.003,.0005,.001,.003]:
  for policy in ['distributed','largest']:
   tau=np.zeros(len(pre['ids']));tau[0]=tv;weights=np.linalg.norm(pre['K'][1:],axis=1)
   if policy=='distributed':tau[1:]=-tv*weights/weights.sum()
   else:tau[1+int(np.argmax(weights))]=-tv
   XX,r=run(pre,tau,maxiter=70);r['policy']=policy;r['nominal_tau']=tv;allout.append(r)
   name=f'EXCHANGE_{driver}_{seed}_{tv}_{policy}'.replace('.','p')
   if XX is not None:np.save(s.ROOT/(name+'.npy'),XX)
   print(name,json.dumps(r),flush=True)
 (s.ROOT/f'EXCHANGE_{driver}_{seed}.json').write_text(json.dumps(allout,indent=2)+'\n')
if __name__=='__main__':main()
```

## File: free130.py
```python
#!/usr/bin/env python3
"""J130 full independent-star motion: global volume and exact quadratic moments.
This is NONCONVEX numerical research, not a certified convex sector. No critical
point is ignored; the selected whole U forest and non-root S witnesses remain.
"""
import sys,json,time
import numpy as np
from scipy.linalg import null_space
from scipy.optimize import minimize
import star130 as s,exchange130 as ex

def run(driver,seed,trust=.6):
 pre=ex.prepare(s.load(),driver,seed,trust);ids,X,K,Ds=pre['ids'],pre['X'],pre['K'],pre['Ds'];k=len(ids)
 Z=null_space(K.reshape(1,3*k));P=np.zeros((len(X),3,Z.shape[1]))
 for j,i in enumerate(ids):P[i]=Z[3*j:3*j+3]
 # Pass the complete global-volume-null displacement map; moment closure is
 # imposed by the genuine quadratic equalities below, not by this map.
 old=ex.affine_map;pos=s.positive
 try:
  ex.affine_map=lambda pre,tau,segment:(X,P,np.zeros(3*k),Z)
  s.positive=lambda Q:(Q+Q.T)/2
  cc=ex.make_constraints(pre,np.zeros(k))
 finally:ex.affine_map=old;s.positive=pos
 c,G,M=cc['f0'],cc['G'],cc['M'];p=G.shape[1];o,og=cc['target'][:2]
 def vals(z):return c+G@z+np.einsum('i,kij,j->k',z,M,z,optimize=True)
 def jac(z):return G+2*np.einsum('kij,j->ki',M,z,optimize=True)
 def moment(z):
  D=(Z@z).reshape(k,3);kd=np.einsum('ij,ij->i',K,D)
  return (np.einsum('ijk,ik->j',Ds,D)+np.einsum('i,ij->j',kd,X[ids]+D))/24
 def mjac(z):
  D=(Z@z).reshape(k,3);kd=np.einsum('ij,ij->i',K,D);blocks=Ds+np.einsum('ij,ik->ijk',X[ids]+D,K)+kd[:,None,None]*np.eye(3)
  return np.concatenate(list(blocks),axis=1)@Z/24
 start=time.monotonic();r=minimize(lambda z:o+og@z+1e-7*(z@z),np.zeros(p),jac=lambda z:og+2e-7*z,constraints=[dict(type='ineq',fun=lambda z:-vals(z),jac=lambda z:-jac(z)),dict(type='eq',fun=moment,jac=mjac)],bounds=[(-trust,trust)]*p,method='SLSQP',options=dict(maxiter=160,ftol=1e-11))
 Y=X+np.einsum('ijk,k->ij',P,r.x);report=dict(driver=driver,seed=seed,trust=trust,selected=ids,success=bool(r.success),message=r.message,iterations=int(r.nit),max_inequality=float(vals(r.x).max()),moment_residual=moment(r.x).tolist(),tau=(np.einsum('ij,ij->i',K,(Z@r.x).reshape(k,3))/6).tolist(),objective=float(o+og@r.x),seconds=time.monotonic()-start,stats=s.stats(Y));return Y,report

def main():
 driver=int(sys.argv[1]);seed=int(sys.argv[2])if len(sys.argv)>2 else 0;Y,r=run(driver,seed);name=f'FREE130_{driver}_{seed}';np.save(s.ROOT/(name+'.npy'),Y);(s.ROOT/(name+'.json')).write_text(json.dumps(r,indent=2)+'\n');print(name,json.dumps(r),flush=True)
if __name__=='__main__':main()
```

## File: outer130.py
```python
#!/usr/bin/env python3
"""J130 true linear outer relaxation for finite independent-star motion.
Contains only linear hull guards (face and test point not both moving),
linear opposite-edge facet escapes, and tangent necessary guards for the
convex physical witness inequalities. No Q_+ matrix is used. Numerical only.
"""
from fractions import Fraction as F
import numpy as np,json
from scipy.optimize import linprog
from scipy.linalg import null_space
import star130 as s,exact130 as e

def build(driver,seed):
 xf=s.load();nc=s.make_cell(xf,driver,seed,.3);ids=nc['selected'];m=3*len(ids)
 w=list(map(int,(e.R/'DETACHED_G6.txt').read_bytes().split()));N,D=w[:2];X=[tuple(F(t,D)for t in w[2+3*i:5+3*i])for i in range(N)]
 fs,hs,es,vs=e.hull(X);V,M,g=e.mass(X,fs);X=[e.sub(x,g)for x in X];C=e.constraints(X,fs,ids);where={v:k for k,v in enumerate(ids)}
 A=[];b=[];meta=[]
 def affine(fn,used,sign,info):
  v0=fn(X);row=[F(0)]*m
  for i in used:
   if i not in where:continue
   for j in range(3):
    Y=X[:];p=list(X[i]);p[j]+=1;Y[i]=tuple(p);row[3*where[i]+j]=sign*(fn(Y)-v0)
  if not any(row):assert sign*v0<=0;return
  A.append(row);b.append(-sign*v0);meta.append(info)
 for fi,t in enumerate(fs):
  moving=set(t)&set(ids)
  for j in range(N):
   if j in t or (moving and j in where):continue
   def fn(Y,t=t,j=j):
    a,bb,c=[Y[k]for k in t];return e.dot(e.cross(e.sub(bb,a),e.sub(c,a)),e.sub(Y[j],a))
   affine(fn,set(t)|{j},1,['hull',list(t),j])
 # A selected outgoing radial witness f=(p_i).(p_i-p_j)<=0 is convex under
 # independent-star motion. Its exact tangent at the original body is necessary.
 for i in range(N):
  if i==nc['root']:continue
  neigh=nc['d']['neigh'][i];j=max(neigh,key=lambda j:e.dot(X[i],e.sub(X[j],X[i])))
  c=e.dot(X[i],e.sub(X[i],X[j]));assert c<0;row=[F(0)]*m
  if i in where:
   for k in range(3):row[3*where[i]+k]=2*X[i][k]-X[j][k]
  if j in where:
   for k in range(3):row[3*where[j]+k]=-X[i][k]
  if any(row):A.append(row);b.append(-c);meta.append(['U_tangent',i,j])
 # Objective: junior facet edge OPPOSITE driver, necessarily affine.
 tj=next(t for t in fs if set(t)==set(nc['d']['F'][nc['target']]));edge=next((tj[k],tj[(k+1)%3])for k in range(3)if driver not in(tj[k],tj[(k+1)%3]))
 def obj(Y):
  a,bb,c=[Y[k]for k in tj];return e.dot(e.cross(e.sub(bb,a),e.sub(c,a)),e.cross(Y[edge[0]],Y[edge[1]]))
 c0=obj(X);o=[F(0)]*m
 for k in range(3):
  Y=X[:];p=list(Y[driver]);p[k]+=1;Y[driver]=tuple(p);o[3*where[driver]+k]=obj(Y)-c0
 return ids,C,A,b,meta,c0,o,tj,edge

def main():
 allout=[]
 for driver in [5,38,45]:
  ids,C,A,b,meta,c0,o,tj,edge=build(driver,0)
  AA=np.array([[float(x)for x in row]for row in A]);bb=np.array(list(map(float,b)));norm=np.linalg.norm(AA,axis=1);AA/=norm[:,None];bb/=norm
  CC=np.array([[float(x)for x in row]for row in C]);CC/=np.linalg.norm(CC,axis=1)[:,None];oo=np.array(list(map(float,o)));on=np.linalg.norm(oo);oo/=on
  res=linprog(oo,A_ub=AA,b_ub=bb,A_eq=CC,b_eq=np.zeros(len(CC)),bounds=[(None,None)]*len(o),method='highs')
  out=dict(driver=driver,selected=ids,status=res.status,objective=float(c0)+res.fun*on if res.success else None)
  if res.success:
   active=np.flatnonzero(np.abs(res.ineqlin.marginals)>1e-7);out['dual_constraints']=[meta[i]for i in active];out['dual_indices']=list(map(int,active));out['min_slack']=float(res.ineqlin.residual.min())
   out['point']=res.x.tolist()
  print(out,flush=True);allout.append(out)
 (e.R/'OUTER130_PILOT.json').write_text(json.dumps(e.convert(allout),indent=2)+'\n')
if __name__=='__main__':main()
```

## File: lp130.py
```python
#!/usr/bin/env python3
"""Necessary LINEAR outer relaxation of a selected independent-star cell.
Only true affine inequalities are included; omitting quadratic guards yields
an outer region, not a valid constructed hull. LP results are nomination only.
"""
import numpy as np,json,sys
from scipy.optimize import linprog
import star130 as s
X=s.load();out=[]
for driver in [5,38,45]:
 for seed in range(8):
  c=s.make_cell(X,driver,seed,.3);sel=[i for i,Q in enumerate(c['M'])if np.linalg.norm(Q)<1e-14 and c['types'][i]in ['hull','U','S','Sroot']]
  # The stored M is Q_+, so negative-semidefinite nonzero Q could be mistaken
  # for affine. Only this pilot intentionally treats them as INNER relaxations;
  # exact raw coefficients must select truly affine constraints before a proof.
  res=linprog(c['objg'],A_ub=c['G'][sel],b_ub=-c['f0'][sel],bounds=[(None,None)]*len(c['objg']),method='highs')
  v=c['obj0']+res.fun if res.success else None
  out.append(dict(driver=driver,seed=seed,dimension=len(c['objg']),count=len(sel),status=res.status,value=v))
  print(out[-1],flush=True)
(s.ROOT/'LP130_PILOT.json').write_text(json.dumps(out,indent=2)+'\n')
```

## File: localpilot130.py
```python
#!/usr/bin/env python3
"""Executable recovery of the six local LP nominations, not their exact proof.
Only inequalities involving the driver's three coordinates survive. Omit every
other coordinate and every global moment equality. Optionally retain just the
local star-volume plane. gates130.py checks the frozen rational certificates.
"""
import numpy as np,json
from scipy.optimize import linprog
import outer130 as outer,exact130 as e

def main():
 out=[]
 for driver in [5,38,45]:
  ids,C,A,b,meta,c0,o,tj,edge=outer.build(driver,0)
  k=ids.index(driver);cols=list(range(3*k,3*k+3));outside=[j for j in range(len(o))if j not in cols]
  keep=[i for i,row in enumerate(A)if any(row[j]for j in cols)and not any(row[j]for j in outside)]
  AA=np.array([[float(A[i][j])for j in cols]for i in keep]);bb=np.array([float(b[i])for i in keep]);sc=np.linalg.norm(AA,axis=1);AA/=sc[:,None];bb/=sc
  obj=np.array([float(o[j])for j in cols]);KK=np.array([[float(C[k][j])for j in cols]]);KK/=np.linalg.norm(KK)
  for kind in ['zero_star_volume','free_volume']:
   eq=dict(A_eq=KK,b_eq=np.zeros(1))if kind=='zero_star_volume' else {}
   r=linprog(obj,A_ub=AA,b_ub=bb,bounds=[(None,None)]*3,method='highs',**eq)
   item=dict(driver=driver,kind=kind,status=r.status)
   if r.success:
    active=np.flatnonzero(abs(r.ineqlin.marginals)>1e-9)
    item.update(lower_bound=float(c0)+float(r.fun),policies=[meta[keep[i]]for i in active],point=r.x.tolist())
   print(item,flush=True);out.append(item)
 (e.R/'LOCAL130_PILOT.json').write_text(json.dumps(e.convert(out),indent=2)+'\n')
 print('J130_LOCAL_NOMINATION_FINISHED_NOT_EXACT')
if __name__=='__main__':main()
```
