# material-d96aa68c6318

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J91 numerical methods: finite actual hull, controller replacement and exact freezing

Read every complete source unit and checkpoint with J91_METHODS_CORE.md and the exact J90 source core in [internal-source-reference]. The J91 exact recovery is separate: [internal-source-reference] MUST be supplemented by [internal-source-reference], saved as J91_CAPFLOW_C452_G18_INPUT.json after extraction. The first bundle accidentally transcribed that body's face index68 as a duplicate old face; the complete correction has the exact certified input SHA04934ba469a529db6d285ad5b6ed6f9f4669533c3904a4273e84e82bbfb1b09c. The manifest rejects the transcription error; C434/C494 inputs and producing geometry are not altered.

Dependencies: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, PyTorch2.10.0+cpu, OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1. Exact freeze additionally uses Fraction and the J90 GMP auditor. All thresholds in this code are numerical nomination policies, never exact exclusion or weak-equilibrium tests. The four CHECKPOINT files preserve complete binary64 input arrays and frame shifts, omitting only historical reports. To use the original command names copy each *_CHECKPOINT.json to the same filename without _CHECKPOINT. Copy J91_CAPFLOW_CHECKPOINT before scout and J91_OUTER2_CHECKPOINT before rebalancing.

Commands and scope: `python envelope91.py greedy 20` is the finite diameter-ball negative control; `python outerflow91.py scout` is the175-evaluated two-apex scout. The original outer run requested50steps but was interrupted after30accepted steps by a container call boundary, not a convergence theorem. `python outerflow91.py J91_TWO_APEX_START.json 30 J91_OUTER2` reruns those nominal iterations in the recorded environment. `python rebalance91.py` tests20deterministically randomized moment-allocation costs with seed910227 and selects actual ownS2/U1/E<=249 candidates; case12 gives controllers6/43/63,C434. `python freeze_outer91.py J91_REBALANCED.json 18 J91_REBALANCED_C434_G18`, then `./vfaudit90 < J91_REBALANCED_C434_G18_VF.txt > J91_REBALANCED_C434_G18_AUDIT.json`, reconstructs and audits the selected literal rational body. Optimization-free recovery from its exact input/face cycles does not depend on reproducing this optimizer.

## File `envelope91.py`
```python
"""U-safe, old-point diameter-ball outer-envelope experiments.
Numerical nomination only: maximal-facet grouping uses a stated tolerance.
All physical volume and centroid values are reintegrated on each actual hull.
"""
from pathlib import Path
import json,sys
import numpy as np
from scipy.spatial import ConvexHull
from j90 import geometry,report,score
from masscaps90 import poly
ROOT=Path(__file__).resolve().parent

def hullpoly(points,tol=2e-8):
 x=np.asarray(points,float);h=ConvexHull(x)
 if np.max(h.equations[:,3])>=0:raise ValueError('origin not interior')
 par=np.arange(len(h.simplices))
 def root(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 for i,ns in enumerate(h.neighbors):
  for j in ns:
   if j>i and np.linalg.norm(h.equations[i]-h.equations[j])<tol:par[root(j)]=root(i)
 groups={}
 for i in range(len(par)):groups.setdefault(root(i),[]).append(i)
 faces=[]
 for ids in groups.values():
  es={}
  for k in ids:
   t=h.simplices[k]
   for a,b in zip(t,np.roll(t,-1)):
    e=tuple(sorted([int(a),int(b)]));es[e]=es.get(e,0)+1
  boundary=[e for e,v in es.items() if v==1];nb={}
  for a,b in boundary:nb.setdefault(a,[]).append(b);nb.setdefault(b,[]).append(a)
  if not all(len(v)==2 for v in nb.values()):raise ValueError('noncycle boundary')
  start=min(nb);cy=[start];prev=-1;cur=start
  while True:
   nxt=next(t for t in nb[cur] if t!=prev)
   if nxt==start:break
   cy.append(nxt);prev,cur=cur,nxt
   if len(cy)>len(nb):raise ValueError('cycle failure')
  if len(cy)!=len(nb):raise ValueError('disconnected face')
  n=h.equations[ids[0],:3]
  if np.cross(x[cy[1]]-x[cy[0]],x[cy[2]]-x[cy[0]])@n<0:cy.reverse()
  faces.append(cy)
 used=sorted(set(i for f in faces for i in f));mp={v:i for i,v in enumerate(used)}
 out=poly(x[used],[[mp[v] for v in f] for f in faces]);out['labels']=used
 return out

def ref(z):
 r=z.copy();r.update(p=z['x'],q=z['y'],g=np.zeros(3));return report(r)

def support_ball(old,n,slack=1e-4):
 n=np.array(n)/np.linalg.norm(n);r=np.linalg.norm(old,axis=1)
 vals=(old@n+r)/2;i=int(np.argmax(vals))
 w=old[i]/2+(1-slack)*r[i]*n/2
 return w,i,float(w@(old[i]-w)),float(vals[i])

def base():
 raw=np.loadtxt(ROOT/'J90_DETACHED_C390_G8.txt',skiprows=1)/1e8
 z=geometry(raw);return geometry(z['q']),z['g']

def main(mode='greedy',steps=20):
 z,g=base();old=z['x'].copy();points=old.copy();hist=[];best=None
 for k in range(steps):
  zz=hullpoly(points);rr=ref(zz);own=report(zz)
  print('STEP',k,'V/E/F',rr['V'],rr['E'],rr['F'],'referenceSU',len(rr['S']),len(rr['U']), 'Q', [b['depth'] for b in rr['Q']],'ownSU',len(own['S']),len(own['U']),'g',own['centroid'],flush=True)
  rec=dict(step=k,reference=rr,own=own)
  if len(rr['S'])==1:
   rec['note']='reference S1 only; physical centroid still must be repaired';hist.append(rec);break
  junior=rr['Q'][0]['root'];n=zz['y'][junior]
  if mode=='greedy':w,vi,guard,val=support_ball(old,n,1e-3)
  elif mode=='recursive':w,vi,guard,val=support_ball(points,n,1e-3)
  elif mode=='death':
   a,b=rr['Q'][0]['edge'];n=(zz['y'][a]+zz['y'][b])/2;w,vi,guard,val=support_ball(old,n,1e-3)
  else:raise ValueError('mode')
  if np.max(zz['y']@w)<1+1e-8:rec['note']='no strict outward support';hist.append(rec);break
  points=np.vstack([points,w]);rec.update(w=w.tolist(),witness=vi,guard=guard);hist.append(rec)
 (ROOT/f'J91_ENVELOPE_{mode}.json').write_text(json.dumps(dict(mode=mode,slack=.001,initial_shift=g.tolist(),points=points.tolist(),history=hist),indent=2)+'\n')
 print('J91_ENVELOPE_SCOUT_ONLY',mode,flush=True)
if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else 'greedy',int(sys.argv[2]) if len(sys.argv)>2 else 20)
```

## File `outerflow91.py`
```python
"""J91 full actual-hull finite outer growth with own-moment retraction.
Old rational-source vertices are fixed in the true old-centroid frame. New
points have positive chords to old points; this is a sufficient U1 condition
at exactly that centroid. Rebuilding the hull allows finite normal-fan changes.
All numeric outcomes require later exact rational reconstruction and census.
"""
from pathlib import Path
import sys,json
import numpy as np,torch
from scipy.optimize import linprog,minimize
from capflow91 import setup
from envelope91 import hullpoly,ref
from j90 import report,score
ROOT=Path(__file__).resolve().parent
torch.set_default_dtype(torch.float64);torch.set_num_threads(1)

def init():
 m=setup();W=np.array(json.loads((ROOT/'J91_CAPFLOW.json').read_text())['apexes']);return m,m['z']['x'],W

def chart(old,W):
 zz=hullpoly(np.vstack([old,W]));labs=zz['labels'];fs=[[labs[i] for i in f] for f in zz['faces'].values()];tri=[[f[0],f[j],f[j+1]] for f in fs for j in range(1,len(f)-1)]
 # A noncollinear supporting triple; selected by area, not arbitrary collinear prefix.
 ft=[];x=np.vstack([old,W])
 for f in fs:
  ts=np.array([[f[0],f[j],f[j+1]] for j in range(1,len(f)-1)]);a=x[ts];k=np.argmax(np.linalg.norm(np.cross(a[:,1]-a[:,0],a[:,2]-a[:,0]),axis=1));ft.append(ts[k])
 O=torch.tensor(old);T=torch.tensor(tri);FT=torch.tensor(np.array(ft))
 def fields(w):
  X=torch.cat([O,w]);a=X[FT];n=torch.linalg.cross(a[:,1]-a[:,0],a[:,2]-a[:,0]);h=(n*a[:,0]).sum(1);q=n/h[:,None]
  t=X[T];D=(t[:,0]*torch.linalg.cross(t[:,1],t[:,2])).sum(1);vol=D.sum()/6;M=(D[:,None]*t.sum(1)).sum(0)/24
  return q,M,vol
 return zz,fields

def retract(old,W,tol=2e-14,maxit=10):
 w=np.array(W,copy=True)
 for it in range(maxit):
  zz,fields=chart(old,w);a=torch.tensor(w);M=fields(a)[1].numpy()
  if np.max(abs(M))<=tol:return w,zz,True
  J=torch.func.jacrev(lambda v:fields(v)[1])(a).numpy().reshape(3,-1)
  if np.linalg.matrix_rank(J,tol=1e-12)<3:return w,zz,False
  d=np.linalg.lstsq(J,-M,rcond=None)[0].reshape(w.shape);prev=np.linalg.norm(M);accepted=False
  for bt in range(12):
   trial=w+d*2**-bt
   try:zt,ff=chart(old,trial);Mt=ff(torch.tensor(trial))[1].numpy()
   except Exception:continue
   if np.linalg.norm(Mt)<prev:
    w=trial;accepted=True;break
  if not accepted:return w,zz,False
 zz,_=chart(old,w);return w,zz,np.max(abs(zz['g']))<tol

def scout():
 m,old,W=init();z=hullpoly(np.vstack([old,W]));r=ref(z);vals=score(z['y']).max(1);nonroots=[i for i in np.argsort(vals) if i not in r['S']];chosen=nonroots[:4];table=[];best=None
 for fi in chosen:
  cy=z['faces'][fi];a=z['x'][cy];cf=a.mean(0);n=z['y'][fi]/np.linalg.norm(z['y'][fi]);height=1/np.linalg.norm(z['y'][fi]);foot=height*n
  for bias in [0.,.5,.85]:
   for corner in range(len(a)):
    v=(1-bias)*cf+bias*a[corner]
    for h in [1e-5,1e-4,5e-4,2e-3]:
     b=v+h*n
     if np.max(b@(old-b).T)<=1e-9:continue
     try:
      w,zz,ok=retract(old,np.vstack([W,b]));rr=report(zz)
     except Exception:continue
     guards=np.einsum('ij,ikj->ik',w,old[None]-w[:,None]).max(1)
     row=dict(face=int(fi),base_labels=[z['labels'][v] for v in cy],bias=bias,corner=corner,height=h,closed=ok,min_U_safe=float(guards.min()),report=rr)
     table.append(row)
     if not ok or min(guards)<=1e-9 or rr['E']>249 or len(rr['U'])!=1 or len(rr['S'])>2:continue
     key=(len(rr['S']),rr['Q'][0]['depth'] if rr['Q'] else 0.)
     if best is None or key<best[0]:
      best=(key,w,row);print('SCOUT_BEST',key,row,flush=True);(ROOT/'J91_TWO_APEX_START.json').write_text(json.dumps(dict(apexes=w.tolist(),cap_ids=m['ids']+[-1],frame_shift=m['g'].tolist(),nomination=row),indent=2)+'\n')
 (ROOT/'J91_TWO_APEX_SCOUT.json').write_text(json.dumps(table,indent=2)+'\n');print('J91_TWO_APEX_SCOUT_COMPLETED',len(table),bool(best),flush=True)

def run(source,steps=60,tag='J91_OUTERFLOW'):
 m,old,unused=init();W=np.array(json.loads(Path(source).read_text())['apexes']);hist=[];trust=.02;O=torch.tensor(old)
 for k in range(steps):
  zz,fields=chart(old,W);rr=report(zz);q=zz['y'];bars=rr['Q'];
  if not bars:print('NUMERICAL_OWN_S1_CANDIDATE',rr,flush=True);break
  peak=bars[0]['root'];a,b=bars[0]['edge'];elder=int(np.argmax((q*q).sum(1)));qi=np.array([i for i in range(len(q)) if i not in [peak,elder]]);qj=score(q).argmax(1)[qi];wi=np.argmax(np.einsum('ik,ijk->ij',W,old[None]-W[:,None]),axis=1)
  def fun(w):
   Q,M,V=fields(w);D=Q[qj]-Q[qi];qc=(Q[qi]*D).sum(1)/(torch.linalg.vector_norm(Q[qi],dim=1)*torch.linalg.vector_norm(D,dim=1));us=(w*(O[wi]-w)).sum(1)
   d=Q[b]-Q[a];t=torch.clamp(-(Q[a]*d).sum()/(d*d).sum(),0,1);f=Q[a]+t*d;loss=1-(f*f).sum()/(Q[peak]*Q[peak]).sum()
   return torch.cat([us,qc,M,loss[None]])
  wt=torch.tensor(W);v=fun(wt).numpy();J=torch.func.jacrev(fun,chunk_size=64)(wt).numpy().reshape(len(v),-1);nc=len(v)-4;G=J[:nc];MG=J[nc:nc+3];grad=J[-1]
  target=np.minimum(v[:nc],1e-8);target[:len(W)]=np.minimum(v[:len(W)],1e-7);nr=np.linalg.norm(G,axis=1);keep=nr>1e-9;scale=np.maximum(nr[keep],1e-8);GG=G[keep]/scale[:,None];rhs=(target-v[:nc])[keep]/scale;ms=np.maximum(np.linalg.norm(MG,axis=1),1e-6);EE=MG/ms[:,None];ee=-v[nc:nc+3]/ms
  op=linprog(grad,A_ub=-GG,b_ub=-rhs,A_eq=EE,b_eq=ee,bounds=[(-trust,trust)]*W.size,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9});rec=dict(k=k,old=float(v[-1]),trust=trust,lp=op.success,accepted=False)
  if op.success and grad@op.x<-1e-13:
   L=np.vstack([GG,-grad]);lb=np.r_[rhs,-.7*grad@op.x];fit=minimize(lambda d:(.5*d@d,d),op.x,jac=True,method='SLSQP',bounds=[(-trust,trust)]*W.size,constraints=[{'type':'ineq','fun':lambda d:L@d-lb,'jac':lambda d:L},{'type':'eq','fun':lambda d:EE@d-ee,'jac':lambda d:EE}],options={'maxiter':120,'ftol':1e-17});d=fit.x if min(L@fit.x-lb)>-1e-8 and max(abs(EE@fit.x-ee))<1e-9 else op.x;d=d.reshape(W.shape)
   for bt in range(17):
    try:w,zt,closed=retract(old,W+2**-bt*d,tol=2e-15,maxit=8);r=report(zt)
    except Exception:continue
    us=np.einsum('ik,ijk->ij',w,old[None]-w[:,None]).max(1);new=r['Q'][0]['depth'] if r['Q'] else 0.
    if not closed or min(us)<=1e-10 or r['E']>249 or len(r['U'])!=1 or len(r['S'])>2 or r['P'] or new>=rec['old']-1e-12:continue
    W=w;rec.update(accepted=True,alpha=2**-bt,new=new,report=r,min_U_safe=float(us.min()),min_Q_nonroot=float(np.sort(score(zt['q']).max(1))[2]));break
  hist.append(rec);print(tag,json.dumps(rec),flush=True)
  (ROOT/(tag+'.json')).write_text(json.dumps(dict(base='J90_DETACHED_C390_G8',frame_shift=m['g'].tolist(),apexes=W.tolist(),history=hist,report=report(chart(old,W)[0])),indent=2)+'\n')
  if rec['accepted']:
   if rec['alpha']>=.5:trust=min(.1,trust*1.25)
  else:trust*=.5
  if trust<1e-7:break
 print('J91_FULL_OUTER_FLOW_NUMERICAL_ONLY',flush=True)
if __name__=='__main__':
 if sys.argv[1]=='scout':scout()
 else:run(sys.argv[1],int(sys.argv[2]) if len(sys.argv)>2 else 60,sys.argv[3] if len(sys.argv)>3 else 'J91_OUTERFLOW')
```

## File `rebalance91.py`
```python
"""Replace expensive moment controllers without altering the two-apex Q patch.
Linear cap-volume allocation initializes the exact quadratic moment equations.
Candidate convexity, actual mass, U safety, and all root counts are rebuilt.
These are numeric nominations, not exact equilibrium claims.
"""
import json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import linprog,least_squares
from capflow91 import setup
from envelope91 import hullpoly
from j90 import report
from masscaps90 import face_data
ROOT=Path(__file__).resolve().parent

def main():
 m=setup();z=m['z'];old=z['x'];src=json.loads((ROOT/'J91_OUTER2.json').read_text());primary=np.array(src['apexes'])[7:9];prime=hullpoly(np.vstack([old,primary]));M=prime['vol']*prime['g'];print('PRIMARY_ONLY',report(prime),'M',M.tolist(),flush=True)
 U=report(z)['U'][0];stable=report(z)['S'];vis=set(np.where(np.max(z['y']@primary.T,axis=1)>1+1e-10)[0]);choices=[]
 for fi,cy in z['faces'].items():
  if fi in stable or fi in vis or U in cy:continue
  c,n,A=face_data(z,fi);sl=1-z['y']@c;dn=z['y']@n;ix=[j for j in range(len(dn)) if j!=fi and dn[j]>0];cap=.7*np.min(sl[ix]/dn[ix])
  gi=np.argmax(c@(old-c).T);r0=c@(old[gi]-c);b=n@(old[gi]-2*c)
  if r0<=0:continue
  safe=(b+np.sqrt(b*b+4*r0))/2;cap=min(cap,.7*safe)
  if cap<1e-9:continue
  choices.append((int(fi),c,n,A,float(cap),len(cy)))
 C=np.array([c for fi,c,n,A,cap,k in choices]).T;bounds=[(0,A*cap/3) for fi,c,n,A,cap,k in choices];table=[];best=None;rng=np.random.default_rng(910227)
 for case in range(20):
  cost=np.array([k for fi,c,n,A,cap,k in choices],float)
  if case:cost*=np.exp(rng.normal(0,.6,len(cost)))
  bb=bounds.copy()
  if case%3==0:
   for j,item in enumerate(choices):
    if item[0]==14:bb[j]=(0,0)
  op=linprog(cost,A_eq=C,b_eq=-M,bounds=bb,method='highs')
  if not op.success:table.append(dict(case=case,reason='moment-capacity-infeasible'));continue
  sel=np.where(op.x>1e-13)[0];initial=op.x[sel];scale=max(np.max(initial),np.linalg.norm(M))
  def eq(v):
   R=M.copy()
   for j,i in enumerate(sel):
    fi,c,n,A,cap,k=choices[i];R+=v[j]*(c+3*v[j]/A*n/4)
   return R
  upper=np.array([bb[i][1] for i in sel]);sol=least_squares(lambda v:eq(v*scale)/scale,initial/scale,bounds=(np.zeros(len(sel)),upper/scale),xtol=1e-13,gtol=1e-13,ftol=1e-13,max_nfev=500);vv=sol.x*scale
  if max(abs(eq(vv)))>1e-13:table.append(dict(case=case,reason='quadratic-moment-infeasible',residual=eq(vv).tolist()));continue
  caps=[];ids=[]
  for j,i in enumerate(sel):
   fi,c,n,A,cap,k=choices[i];caps.append(c+3*vv[j]/A*n);ids.append(fi)
  w=np.vstack([caps,primary]);guards=np.einsum('ik,ijk->ij',w,old[None]-w[:,None]).max(1)
  try:zz=hullpoly(np.vstack([old,w]));rr=report(zz)
  except Exception as e:table.append(dict(case=case,reason=str(e)));continue
  rec=dict(case=case,controller_faces=ids,report=rr,pyramid_residual=eq(vv).tolist(),min_U_safe=float(guards.min()));table.append(rec)
  if max(abs(zz['g']))>1e-12 or min(guards)<=1e-10 or len(rr['S'])!=2 or len(rr['U'])!=1 or rr['E']>249:continue
  key=(rr['E'],rr['Q'][0]['depth'])
  if best is None or key<best:
   best=key;print('REBALANCE_BEST',key,rec,flush=True);(ROOT/'J91_REBALANCED.json').write_text(json.dumps(dict(base='J90_DETACHED_C390_G8',frame_shift=m['g'].tolist(),apexes=w.tolist(),controller_faces=ids,primary_count=2,info=rec),indent=2)+'\n')
 (ROOT/'J91_REBALANCE_SCAN.json').write_text(json.dumps(dict(seed=910227,choices=[dict(face=i,centre=c.tolist(),normal=n.tolist(),area=A,height_cap=cap,cost=k) for i,c,n,A,cap,k in choices],primary=primary.tolist(),primary_moment=M.tolist(),results=table),indent=2)+'\n');print('J91_REBALANCE_NUMERICAL_FINISHED',best,flush=True)
if __name__=='__main__':main()
```

## File `freeze_outer91.py`
```python
"""Freeze a finite actual-hull nomination; exact supporting-plane grouping.
SciPy proposes triangles only. Every accepted plane and complete contact set
is tested with Fraction. The emitted VF complex is then certified independently
of SciPy's proposal tolerance by the complete GMP maximal-facet auditor.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import reduce
import math,json,sys
import numpy as np
from scipy.spatial import ConvexHull
ROOT=Path(__file__).resolve().parent
sys.set_int_max_str_digits(0)
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def plane(a,b,c):
 n=cross(sub(b,a),sub(c,a));h=dot(n,a)
 if h<0:n=tuple(-v for v in n);h=-h
 if h==0:return None
 row=(*n,h);d=math.lcm(*(t.denominator for t in row));z=[int(t*d) for t in row];gg=reduce(math.gcd,z);return tuple(t//gg for t in z)
def freeze(src,digits,name):
 inp=json.loads(Path(src).read_text());base=json.loads((ROOT/'J90_DETACHED_C390_G8_AUDIT.json').read_text());x=[tuple(map(F,p)) for p in base['vertices']];g=np.array(inp['frame_shift']);D=10**digits
 ap=[tuple(F(round(F(float(v))*D),D) for v in row) for row in (np.array(inp['apexes'])+g)]
 x+=ap;xf=np.array([[float(a) for a in p] for p in x]);hull=ConvexHull(xf);planes={};rejected=[]
 for t in hull.simplices:
  row=plane(*(x[k] for k in t))
  if row is None:continue
  sl=[row[3]-dot(row[:3],p) for p in x]
  if min(sl)<0:rejected.append([t.tolist(),float(min(sl))]);continue
  planes[row]=[i for i,s in enumerate(sl) if s==0]
 faces=[]
 for row,cy in sorted(planes.items()):
  n=np.array(row[:3],float);n/=np.linalg.norm(n);c=xf[cy].mean(0);p=xf[cy]-c;u=p[0]/np.linalg.norm(p[0]);v=np.cross(n,u);ang=np.arctan2(p@v,p@u);cy=[cy[k] for k in np.argsort(ang)]
  if dot(row[:3],cross(sub(x[cy[1]],x[cy[0]]),sub(x[cy[2]],x[cy[0]])))<0:cy.reverse()
  faces.append(cy)
 es={}
 for cy in faces:
  for a,b in zip(cy,cy[1:]+cy[:1]):e=tuple(sorted((a,b)));es[e]=es.get(e,0)+1
 print('PROPOSED_EXACT',name,'VEF',len(x),len(es),len(faces),'rejected',rejected,'edgecounts',sorted(set(es.values())),flush=True)
 assert all(v==2 for v in es.values()) and len(x)-len(es)+len(faces)==2
 out=dict(name=name,base='J90_DETACHED_C390_G8',grid=D,rounding='ties-to-even of each exact binary64 raw apex times 10**digits',apexes=[list(map(str,p)) for p in ap],faces=faces,source=Path(src).name)
 (ROOT/(name+'_INPUT.json')).write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
 with (ROOT/(name+'_VF.txt')).open('w') as f:
  f.write(f'{len(x)} {len(faces)}\n')
  for p in x:f.write(' '.join(map(str,p))+'\n')
  for cy in faces:f.write(' '.join(map(str,[len(cy),*cy]))+'\n')
 print('J91_LITERAL_VF_FROZEN_NOT_YET_AUDITED',name,flush=True)
if __name__=='__main__':freeze(sys.argv[1],int(sys.argv[2]),sys.argv[3])
```

## File `J91_CAPFLOW_CHECKPOINT.json`
```json
{"apexes":[[-0.765120395362036,0.15609394919460176,0.04257850661993697],[0.015045204244448992,-0.09622937759608974,-0.9857308190144409],[0.49666107409928784,-0.20108277355954238,-0.8284342794276913],[0.12893636937617153,-0.09599836635391909,-0.9817495083484233],[0.3258967062832201,-0.20612577635332321,-0.9024623870013734],[0.3772402587709779,-0.20309571783419988,-0.8914832750863172],[0.2946767290238554,-0.47024299288460203,0.2203491485314047],[-0.34214177258951217,0.4492984200237728,0.19528925776438588]],"base":"J90_DETACHED_C390_G8","cap_ids":[6,14,16,19,39,41,43,65],"frame_shift":[0.0014912244454172178,0.00019128633735983745,0.00040522044254412453]}
```

## File `J91_OUTER2_CHECKPOINT.json`
```json
{"apexes":[[-0.7651308953653412,0.15610618515237315,0.04258207245809395],[0.014988007986773293,-0.0964757932485166,-0.9859173615901763],[0.4967391619361583,-0.20108880060548764,-0.8285430050134643],[0.12900369088767294,-0.09588909820688363,-0.9819479765313255],[0.32606541206341555,-0.20683359898205636,-0.9034737854195092],[0.37733244649448716,-0.2032442727474062,-0.8917551979883941],[0.2947163770488274,-0.4703545313141186,0.22038978333208767],[-0.3351589130454221,0.4533955104568723,0.19851259991671794],[-0.36985730823321505,0.4431983950030348,0.16660691224784827]],"base":"J90_DETACHED_C390_G8","frame_shift":[0.0014912244454172178,0.00019128633735983745,0.00040522044254412453]}
```

## File `J91_TWO_APEX_START_CHECKPOINT.json`
```json
{"apexes":[[-0.7651203710934137,0.15609391990121624,0.04257849697254031],[0.015045189157460755,-0.09622943860280306,-0.985730862587142],[0.4966610924753839,-0.2010827754050212,-0.8284343051951315],[0.12893638398260876,-0.09599834264609762,-0.981749551406751],[0.325896740456731,-0.2061259235282669,-0.9024625963339576],[0.37724027216603284,-0.20309573502428985,-0.891483309423548],[0.29467672823977065,-0.4702429914045025,0.22034914713100712],[-0.3421414654620389,0.44929797778689745,0.195289053293035],[-0.3848032285615944,0.42769896174323124,0.17270007709717172]],"cap_ids":[6,14,16,19,39,41,43,65,-1],"frame_shift":[0.0014912244454172178,0.00019128633735983745,0.00040522044254412453]}
```

## File `J91_REBALANCED_CHECKPOINT.json`
```json
{"apexes":[[-0.7652356987947021,0.15623283416188807,0.04262392883994398],[0.2946964892725571,-0.470296015064762,0.2203714214811953],[0.5739123922548929,-0.3451132748338508,-0.7040719330906278],[-0.3351589130454221,0.4533955104568723,0.19851259991671794],[-0.36985730823321505,0.4431983950030348,0.16660691224784827]],"base":"J90_DETACHED_C390_G8","controller_faces":[6,43,63],"frame_shift":[0.0014912244454172178,0.00019128633735983745,0.00040522044254412453],"primary_count":2}
```

## File `J91_METHOD_MANIFEST.json`
```json
{"J91_CAPFLOW_CHECKPOINT.json":{"bytes":660,"sha256":"14d643e3f52df23d67679dabd1348339fc97a5ef0fb99381130ad061b0f02f59"},"J91_OUTER2_CHECKPOINT.json":{"bytes":686,"sha256":"fe187eb17e7f579cb8f2485bc5546c6577a796434db85f6844b90614860a6da0"},"J91_REBALANCED_CHECKPOINT.json":{"bytes":479,"sha256":"1bf0e84b1abf50b5b57093dc7432f57c1c961c7c79641d2f6185be1a7dcd2985"},"J91_TWO_APEX_START_CHECKPOINT.json":{"bytes":689,"sha256":"077211d81f30d9e87b507975fbffeca45f9185dfb39457a5b9aad3724e42e7e8"},"capflow91.py":{"bytes":6199,"sha256":"bc0c428c733ceec597c8c6b646c256a3cbfafd6d63c1d15cd79f2425f438a40a"},"envelope91.py":{"bytes":3634,"sha256":"8b34ee40f771f5edcda15b12ed9d01f9010422db3ac907786e285c87ad5dae92"},"freeze_outer91.py":{"bytes":2909,"sha256":"1369826e34e09f21364d1bc05ffbb57490ef1da98fe1e7c24253d0ddc5c6dcc2"},"j90.py":{"bytes":7723,"sha256":"87fafe401715d2206ec26c449c9e4714906e7531d7f84ed884b2567473c38c4d"},"masscaps90.py":{"bytes":5882,"sha256":"d6cb3a06f3107322ff4d33f1b19b69efe26a53849c6cd6b4ac7fea1a3312a1ac"},"outerflow91.py":{"bytes":6904,"sha256":"59e45190fa31c5efecd6e81ca51372df26324b169faa0508a4b5c185d3c5f5e4"},"rebalance91.py":{"bytes":3719,"sha256":"1f64dd751eb76de5772979e8861920370fbd52a6413e6441fa79b1c795ef3a7d"}}
```
