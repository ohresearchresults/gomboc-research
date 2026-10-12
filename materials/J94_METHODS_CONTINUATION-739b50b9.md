# material-739b50b98359

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J94 finite-cap continuation: complete runnable sources and literal states

Dependencies: complete J90/J91 bundles [internal-source-reference], [internal-source-reference], [internal-source-reference], [internal-source-reference], [internal-source-reference]. Extract all source blocks below with final newlines beside the J90/J91 sources and reconstructed J90_DETACHED_C390_G8_AUDIT.json. Exact selected bodies are independently recoverable from [internal-source-reference] plus the complete J90 core. This numerical producer is not an exact own110 claim. Environment executed: Python3.13.5, NumPy2.3.5, SciPy1.17.0, PyTorch2.10.0+cpu, OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1; g++14.2/GMP for exact audit.

Commands and actual scope: `python surgery94.py J94_SCOUT`147 attempts,103 recorded,67 accepted numerical mass-closed/U1/E249 candidates, allowing extra S. C440_START below was obtained by adding centroid of current junior triangle[33,133,39]+.001 outward unit normal then actual-mass retraction. `python flow94.py J94_SCOUT_BEST.json 60 J94_FLOW free` interrupted after about34 saved steps, not completed60. `python flow94.py J94_START.json 65 J94_CHAIN all all` completed65, numerical135/222/89 S4/U1,Q[.1598686535,.0021348043,.0006313607]. `python flow94.py J94_C440_START.json 65 J94_TWOFLOW two all` interrupted after64 saved accepted steps k0..63. Literal TWOFLOW state below is that executed endpoint, not optimizer convergence.

STATE files preserve complete computational variables, not the large original histories; they are distinct byte objects. Copy each required *_STATE.json to its unsuffixed *.json basename for the listed original commands. `python polish94.py` tests all ten listed interpolation parameters with actual nonlinear mass retraction. t=.9999 gives BACKOFF state below. `python freeze_outer91.py J94_BACKOFF_0_9999.json 8 J94_INTERIOR_C440_G8`, then `./vfaudit90 < J94_INTERIOR_C440_G8_VF.txt > J94_INTERIOR_C440_G8_AUDIT.json`, yields exact136/220/86 own211/weak000/primitivezero000,Q.16179081487085792. `python freeze_outer91.py J94_TWOFLOW.json 18 J94_TWO_CAND_G18` instead yields exact own312 with additional Q6.615379650992725e-29, missed by the floating S2 census. `python freeze94.py J94_FIXEDCHAIN_0_3.json 8 J94_CHAIN_C444_G8` allows retired input points and yields exact135/222/89 own312/weak000/primitivezero000. Its complete producing fixed-chain method is the companion chain-method source; the full selected state is here. Exact input/output hashes and replay commands are in [internal-source-reference].

## surgery94.py
3439B; SHA2569793cdc899e739b9ab6e9db43cdf2cca98a4efa9e4c94d49388c929084c98be7.
```python
"""Finite mass-balanced cap insertion on exact J91 C434 input.
Numerical nominations only. Requires complete J90/J91 CORE and OUTER sources.
All actual hulls are reintegrated, U and every positive P/Q bar recounted.
"""
import sys,json,itertools
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from envelope91 import hullpoly,support_ball
from outerflow91 import retract,chart
from j90 import report,score
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent

def initial():
 b=json.loads((ROOT/'J90_DETACHED_C390_G8_AUDIT.json').read_text())
 d=json.loads((ROOT/'J91_REBALANCED_C434_G18_INPUT.json').read_text())
 g=np.array([float(F(s)) for s in b['centroid']])
 old=np.array([[float(F(s)) for s in p] for p in b['vertices']])-g
 w=np.array([[float(F(s)) for s in p] for p in d['apexes']])-g
 return old,w,g

def save(name,old,w,g,extra):
 (ROOT/(name+'.json')).write_text(json.dumps(dict(base='J90_DETACHED_C390_G8',frame_shift=g.tolist(),apexes=w.tolist(),**extra),indent=2)+'\n')

def key(r):
 return (len(r['U'])!=1, bool(r['P']),sum(b['depth'] for b in r['Q']),len(r['Q']),r['E'])

def scout(tag='J94_SCOUT',source=None):
 old,W,g=initial()
 if source:W=np.array(json.loads(Path(source).read_text())['apexes'])
 z=hullpoly(np.vstack([old,W]));r=report(z)
 # Target the current near-born stable carrier plus current junior stable carrier.
 near=score(z['q']).max(1);elder=int(np.argmax((z['q']**2).sum(1)))
 fis=[i for i in np.argsort(near) if i!=elder][:3]
 table=[];best=None;good=[];ntrial=0
 for fi in fis:
  cy=z['faces'][fi];pts=z['x'][cy];cf=pts.mean(0);n=z['y'][fi]/np.linalg.norm(z['y'][fi]);labs=[z['labels'][i] for i in cy]
  candidates=[]
  for bias in [0.,.5,.85]:
   for corner in range(len(pts)):
    if bias==0 and corner:continue
    for height in [1e-5,1e-4,1e-3,5e-3,.02]:
     candidates.append((dict(bias=bias,corner=corner,height=height),(1-bias)*cf+bias*pts[corner]+height*n))
  for slack in [.5,.1,.01,.001]:
   b,vi,guard,val=support_ball(old,n,slack)
   candidates.append((dict(ball_slack=slack,old_witness=vi),b))
  for params,b in candidates:
   ntrial+=1
   if np.max(b@(old-b).T)<=1e-9:continue
   try:
    w,zz,ok=retract(old,np.vstack([W,b]),tol=2e-14,maxit=6)
    rr=report(zz)
   except Exception as e:
    table.append(dict(face=int(fi),labels=labs,parameters=params,error=str(e)));continue
   us=np.einsum('ij,ikj->ik',w,old[None]-w[:,None]).max(1)
   rec=dict(face=int(fi),labels=labs,parameters=params,closed=bool(ok),min_old_witness=float(us.min()),report=rr)
   table.append(rec)
   if not ok or us.min()<=1e-10 or rr['E']>249 or len(rr['U'])!=1 or rr['P']:continue
   good.append((key(rr),w.copy(),rec))
   if best is None or key(rr)<best[0]:
    best=(key(rr),w.copy(),rec);save(tag+'_BEST',old,w,g,dict(info=rec))
    print('BEST',ntrial,labs,params,'VEF',rr['V'],rr['E'],rr['F'],'SU',len(rr['S']),len(rr['U']),'Q', [b['depth'] for b in rr['Q']],flush=True)
  print('FACE_DONE',fi,labs,len(table),len(good),flush=True)
 good.sort(key=lambda q:q[0])
 for k,(kk,w,rec) in enumerate(good[:6]):save(tag+f'_TOP{k}',old,w,g,dict(info=rec))
 (ROOT/(tag+'_TABLE.json')).write_text(json.dumps(dict(start=r,attempted=ntrial,accepted=len(good),results=table),indent=2)+'\n')
 print('SCOUT_END',ntrial,len(table),len(good),flush=True)

if __name__=='__main__':scout(sys.argv[1] if len(sys.argv)>1 else 'J94_SCOUT',sys.argv[2] if len(sys.argv)>2 else None)
```

## flow94.py
4476B; SHA2561a7af6ddde1d845f19b19a5bcadc1e00a31f388a2d215be3e5e7c13e9d5e9a83.
```python
"""Actual-hull, fixed-host, finite-mass multi-bar continuation.
Unlike J91 outerflow, every current polar persistence root is allowed to die;
loss is the sum of all positive polar depths. No count/weak claim is exact.
Dependencies are the complete J90/J91 sources plus surgery94.py.
"""
import sys,json
from pathlib import Path
import numpy as np,torch
from scipy.optimize import linprog,minimize
from surgery94 import initial,save
from outerflow91 import chart,retract
from j90 import report,score
ROOT=Path(__file__).resolve().parent
torch.set_default_dtype(torch.float64);torch.set_num_threads(1)

def run(source,steps=60,tag='J94_FLOW',root_policy='all',witness_policy='old'):
 old,W,g=initial();W=np.array(json.loads(Path(source).read_text())['apexes'])
 hist=[];trust=.025;O=torch.tensor(old)
 for k in range(steps):
  zz,fields=chart(old,W);rr=report(zz);q=zz['y'];bars=rr['Q']
  if not bars:
   print('NUMERICAL_Q_NONE_NOT_EXACT',rr,flush=True);break
  elder=int(np.argmax((q*q).sum(1)));roots={elder,*[b['root'] for b in bars]}
  qi=np.array([i for i in range(len(q)) if i not in roots],int);qj=score(q).argmax(1)[qi]
  pool=np.vstack([old,W]) if witness_policy=='all' else old
  votes=np.einsum('ik,ijk->ij',W,pool[None]-W[:,None])
  if witness_policy=='all':votes[np.arange(len(W)),len(old)+np.arange(len(W))]=-np.inf
  wi=np.argmax(votes,axis=1)
  def fun(w):
   Q,M,V=fields(w);D=Q[qj]-Q[qi]
   qc=(Q[qi]*D).sum(1)/(torch.linalg.vector_norm(Q[qi],dim=1)*torch.linalg.vector_norm(D,dim=1))
   P=torch.cat([O,w]) if witness_policy=='all' else O
   us=(w*(P[wi]-w)).sum(1);ls=[]
   for bar in bars:
    a,b=bar['edge'];peak=bar['root'];d=Q[b]-Q[a]
    t=torch.clamp(-(Q[a]*d).sum()/(d*d).sum(),0,1);f=Q[a]+t*d
    ls.append(1-(f*f).sum()/(Q[peak]*Q[peak]).sum())
   loss=torch.stack(ls).sum()
   return torch.cat([us,qc,M,loss[None]])
  wt=torch.tensor(W);v=fun(wt).numpy();J=torch.func.jacrev(fun,chunk_size=64)(wt).numpy().reshape(len(v),-1)
  nc=len(v)-4;G=J[:nc];MG=J[nc:nc+3];grad=J[-1]
  target=np.minimum(v[:nc],1e-8);target[:len(W)]=np.minimum(v[:len(W)],1e-7)
  if root_policy=='free':
   # Sign changes of existing nonroot q witnesses are permitted. Actual sum and
   # every critical count is recomputed after the full nonlinear mass step.
   target[len(W):]=-1e3
  nr=np.linalg.norm(G,axis=1);keep=nr>1e-9;scale=np.maximum(nr[keep],1e-8)
  GG=G[keep]/scale[:,None];rhs=(target-v[:nc])[keep]/scale
  ms=np.maximum(np.linalg.norm(MG,axis=1),1e-6);EE=MG/ms[:,None];ee=-v[nc:nc+3]/ms
  op=linprog(grad,A_ub=-GG,b_ub=-rhs,A_eq=EE,b_eq=ee,bounds=[(-trust,trust)]*W.size,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
  rec=dict(k=k,old=float(v[-1]),trust=trust,lp=bool(op.success),accepted=False)
  if op.success and grad@op.x<-1e-13:
   L=np.vstack([GG,-grad]);lb=np.r_[rhs,-.7*grad@op.x]
   fit=minimize(lambda d:(.5*d@d,d),op.x,jac=True,method='SLSQP',bounds=[(-trust,trust)]*W.size,constraints=[{'type':'ineq','fun':lambda d:L@d-lb,'jac':lambda d:L},{'type':'eq','fun':lambda d:EE@d-ee,'jac':lambda d:EE}],options={'maxiter':120,'ftol':1e-17})
   d=fit.x if min(L@fit.x-lb)>-1e-8 and max(abs(EE@fit.x-ee))<1e-9 else op.x;d=d.reshape(W.shape)
   for bt in range(17):
    try:w,zt,closed=retract(old,W+2**-bt*d,tol=2e-15,maxit=8);r=report(zt)
    except Exception:continue
    pp=np.vstack([old,w]) if witness_policy=='all' else old
    us=np.einsum('ik,ijk->ij',w,pp[None]-w[:,None]).max(1)
    new=sum(b['depth'] for b in r['Q'])
    if root_policy=='two' and len(r['S'])>2:continue
    if not closed or min(us)<=1e-10 or r['E']>249 or len(r['U'])!=1 or r['P'] or new>=rec['old']-1e-12:continue
    W=w;rec.update(accepted=True,alpha=2**-bt,new=new,report=r,min_U_safe=float(us.min()));break
  hist.append(rec)
  print(tag,k,'loss',rec.get('new',rec['old']),'SU',len(report(chart(old,W)[0])['S']),len(report(chart(old,W)[0])['U']),'alpha',rec.get('alpha'), 'trust',trust,flush=True)
  save(tag,old,W,g,dict(source=str(source),policy=root_policy,witness_policy=witness_policy,history=hist,report=report(chart(old,W)[0])))
  if rec['accepted']:
   if rec['alpha']>=.5:trust=min(.1,trust*1.25)
  else:trust*=.5
  if trust<1e-7:break
 print('J94_MULTIBAR_FINITE_FLOW_NUMERICAL_ONLY',flush=True)
if __name__=='__main__':run(sys.argv[1],int(sys.argv[2]) if len(sys.argv)>2 else 60,sys.argv[3] if len(sys.argv)>3 else 'J94_FLOW',sys.argv[4] if len(sys.argv)>4 else 'all',sys.argv[5] if len(sys.argv)>5 else 'old')
```

## polish94.py
1195B; SHA256add92c56c201319c9a0036d5a89ab7d34ee8d73f60b4551e32f8e5a86c4222f1.
```python
"""Interior backoff from J94's floating-point stability boundary.
Each finite interpolation is retracted by actual hull volume integration.
Reports are numerical nominations until freeze_outer91 + vfaudit90 certify them.
"""
import json,sys
from pathlib import Path
import numpy as np
from surgery94 import initial,save
from outerflow91 import retract
from j90 import report
ROOT=Path(__file__).resolve().parent

def main():
 old,_,g=initial();start=np.array(json.loads((ROOT/'J94_C440_START.json').read_text())['apexes']);end=np.array(json.loads((ROOT/'J94_TWOFLOW.json').read_text())['apexes'])
 table=[]
 for t in [0,.25,.5,.75,.9,.99,.999,.9999,.99999,.999999]:
  w,z,closed=retract(old,(1-t)*start+t*end,tol=2e-15,maxit=10);r=report(z)
  rec=dict(t=t,closed=bool(closed),report=r)
  table.append(rec);tag='J94_BACKOFF_'+str(t).replace('.','_')
  save(tag,old,w,g,dict(source='J94_C440_START.json + J94_TWOFLOW.json',parameters=rec))
  print(t,closed,'VEF',r['V'],r['E'],r['F'],'SU',len(r['S']),len(r['U']),'Q',[b['depth'] for b in r['Q']],'guard',r['sortedQguards'][:5],flush=True)
 (ROOT/'J94_BACKOFF_TABLE.json').write_text(json.dumps(table,indent=2)+'\n')
if __name__=='__main__':main()
```

## freeze94.py
2998B; SHA256b3dece0d9343ea857db326e00f9304822ec35324b117ebf34237d28dafb9bcd3.
```python
"""Exact maximal-facet recovery allowing old or new points to retire.
SciPy proposes supporting triangles; every plane and contact is checked with
Fraction. Each planar contact set is replaced by its exact 2D convex boundary.
All original points satisfy all retained supports; the closed VF complex is
then audited by the existing complete GMP own-mass/global-equilibrium program.
"""
from pathlib import Path
from fractions import Fraction as F
import sys,json
import numpy as np
from scipy.spatial import ConvexHull
from freeze_outer91 import plane,sub,dot,cross
ROOT=Path(__file__).resolve().parent
sys.set_int_max_str_digits(0)

def boundary(ids,x,row):
 drop=max(range(3),key=lambda k:abs(row[k]));keep=[k for k in range(3) if k!=drop]
 def pt(i):return tuple(x[i][k] for k in keep)
 ids=sorted(ids,key=pt)
 def turn(i,j,k):
  a,b,c=pt(i),pt(j),pt(k)
  return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
 lo=[];hi=[]
 for i in ids:
  while len(lo)>=2 and turn(lo[-2],lo[-1],i)<=0:lo.pop()
  lo.append(i)
 for i in reversed(ids):
  while len(hi)>=2 and turn(hi[-2],hi[-1],i)<=0:hi.pop()
  hi.append(i)
 cy=lo[:-1]+hi[:-1]
 assert len(cy)>=3
 if dot(row[:3],cross(sub(x[cy[1]],x[cy[0]]),sub(x[cy[2]],x[cy[0]])))<0:cy.reverse()
 return cy

def freeze(src,digits,name):
 d=json.loads(Path(src).read_text());base=json.loads((ROOT/'J90_DETACHED_C390_G8_AUDIT.json').read_text());x=[tuple(map(F,p)) for p in base['vertices']];D=10**digits
 raw=np.array(d['apexes'])+np.array(d['frame_shift']);ap=[tuple(F(round(F(float(v))*D),D) for v in row) for row in raw];x+=ap
 hull=ConvexHull(np.array([[float(a) for a in p] for p in x]));planes={};rejected=0
 for t in hull.simplices:
  row=plane(*(x[k] for k in t))
  if row is None:continue
  sl=[row[3]-dot(row[:3],p) for p in x]
  if min(sl)<0:rejected+=1;continue
  planes[row]=[i for i,s in enumerate(sl) if s==0]
 faces=[boundary(ids,x,row) for row,ids in sorted(planes.items())];ret=sorted({i for f in faces for i in f});index={v:i for i,v in enumerate(ret)};faces=[[index[i] for i in f] for f in faces];edges={}
 for f in faces:
  for a,b in zip(f,f[1:]+f[:1]):e=tuple(sorted((a,b)));edges[e]=edges.get(e,0)+1
 assert set(edges.values())=={2} and len(ret)-len(edges)+len(faces)==2
 out=dict(name=name,base='J90_DETACHED_C390_G8',grid=D,rounding='ties-to-even of each exact binary64 raw apex times 10**digits',apexes=[list(map(str,p)) for p in ap],retained_input_indices=ret,faces=faces,source=Path(src).name)
 (ROOT/(name+'_INPUT.json')).write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
 with (ROOT/(name+'_VF.txt')).open('w') as f:
  f.write(f'{len(ret)} {len(faces)}\n')
  for i in ret:f.write(' '.join(map(str,x[i]))+'\n')
  for cy in faces:f.write(' '.join(map(str,[len(cy),*cy]))+'\n')
 print('J94_EXACT_VF_NOMINATION',name,'VEF',len(ret),len(edges),len(faces),'retired',sorted(set(range(len(x)))-set(ret)),'rejected_triangles',rejected,flush=True)
if __name__=='__main__':freeze(sys.argv[1],int(sys.argv[2]),sys.argv[3])
```

## J94_START_STATE.json
402B; SHA256ef07e9482529c47f0bb803bbc37fa273dc771b65b13d277f62930dd89fd3b321.
```json
{"apexes":[[-0.7652356987947021,0.15623283416188805,0.042623928839944],[0.294696489272557,-0.47029601506476204,0.22037142148119532],[0.5739123922548929,-0.34511327483385085,-0.7040719330906278],[-0.3351589130454222,0.45339551045687226,0.19851259991671796],[-0.36985730823321517,0.44319839500303476,0.1666069122478483]],"frame_shift":[0.0014912244454173174,0.0001912863373598814,0.0004052204425441016]}
```

## J94_C440_START_STATE.json
492B; SHA25645c63a9e2fdc0a565699feb6744b748107825a4a41253165ce72822a3bbfe452.
```json
{"apexes":[[-0.7652522597371922,0.15625261736279059,0.04263023822886418],[0.2947030644105892,-0.47031445114448567,0.22037825883978648],[0.5740376592667228,-0.34522334335472915,-0.7042450101266577],[-0.33504890105886576,0.4532372078423577,0.19843972536602061],[-0.3697618203939716,0.4430655263963641,0.166548064849945],[-0.24998771232774822,0.5181134291536372,0.184398687129287]],"base":"J90_DETACHED_C390_G8","frame_shift":[0.0014912244454173174,0.0001912863373598814,0.0004052204425441016]}
```

## J94_SCOUT_BEST_STATE.json
497B; SHA25611d075d4465283bc28858c96b437ac780f8fd996eb7dab27637bc63e04404925.
```json
{"apexes":[[-0.7653198358170415,0.15633314092070702,0.0426557206538446],[0.29474161280866296,-0.4704223312388975,0.22041847593842273],[0.5746585387483163,-0.3457689962351442,-0.7051030288823735],[-0.3351024195539677,0.45332022583524795,0.19847549013470728],[-0.36952044870712375,0.44276463963864454,0.16640803297913226],[-0.29328761272795273,0.48677912311898763,0.19193899487562108]],"base":"J90_DETACHED_C390_G8","frame_shift":[0.0014912244454173174,0.0001912863373598814,0.0004052204425441016]}
```

## J94_TWOFLOW_STATE.json
495B; SHA2560c02891f6254bad433ea2f17067cd0bd74985659a10e81ea99ce4d54db7e50bb.
```json
{"apexes":[[-0.7653200009846604,0.1563025970783196,0.04261400203381426],[0.29471314532247694,-0.4704473263538936,0.22030811953815305],[0.571211789907653,-0.34553222363278435,-0.7073792518104622],[-0.33238962348273343,0.4562539416853865,0.19672875431416392],[-0.3618397586679848,0.44907321233630737,0.16705272466994714],[-0.26430630480493955,0.5141933832666304,0.17392914865073061]],"base":"J90_DETACHED_C390_G8","frame_shift":[0.0014912244454173174,0.0001912863373598814,0.0004052204425441016]}
```

## J94_BACKOFF_0_9999_STATE.json
493B; SHA25635c816fe9b3ffe22c4aa35279090903178d5da03b7fba534d162a74cdf257e20.
```json
{"apexes":[[-0.7653199940194568,0.15630259185176476,0.04261400358413448],[0.29471314420207867,-0.47044731275566987,0.2203081264320817],[0.5712120716669431,-0.3455321920169935,-0.7073789372419825],[-0.33238988966651584,0.45625364037696553,0.19672892558831326],[-0.3618405516233799,0.44907261261108156,0.1670526746617478],[-0.264304873765887,0.5141937764883557,0.1739301961825409]],"base":"J90_DETACHED_C390_G8","frame_shift":[0.0014912244454173174,0.0001912863373598814,0.0004052204425441016]}
```

## J94_FIXEDCHAIN_0_3_STATE.json
558B; SHA256492553e7f0404d57a0a98b52f16e1a09705e1930dc32abb579682cb867c49045.
```json
{"apexes":[[-0.7654394403679359,0.1564761943337384,0.042701547414352975],[0.29483079070454893,-0.47066845385343214,0.2205140487900374],[0.5754031248900864,-0.34636907774071224,-0.7060063744081573],[-0.3351589130454222,0.45339551045687226,0.19851259991671796],[-0.36913775768781093,0.44228610535007146,0.16618609661694705],[-0.3066859413865535,0.46061210706560624,0.22564008929378565],[-0.3150440055193807,0.4885153834685591,0.1610064175062145]],"base":"J90_DETACHED_C390_G8","frame_shift":[0.0014912244454173174,0.0001912863373598814,0.0004052204425441016]}
```
