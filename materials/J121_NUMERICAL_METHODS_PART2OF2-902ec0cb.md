# material-902ec0cb90c1

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J121 numerical producing methods — complete part 2 of 2

Requires complete part1 [internal-source-reference] (geometry121.py, coforest121.py, paired121.py), the original two literal J119_FREEH_G6 inputs in [internal-source-reference], and the Python/NumPy/SciPy/torch versions specified there. This part contains every additional helper and the exact old-version patch. A standalone reconstruction of the three certified rational endpoints instead needs only [internal-source-reference] and [internal-source-reference]; numerical rerunning is not an exact audit prerequisite.

## relays121.py — 5339 bytes, SHA f435ce77a56739b2b4aa717acca5ea64168c61718787cb6622e3712d6301873c
```python
"""J121 finite two-sided local relay capacity scouts, numerical only.
Insert a point on either the physical or actual-centred polar side. Retain
complete current hull, recompute actual homogeneous mass, and test all roots.
A new H chart is accepted only with <=85 active supports. Candidate capacity
means one LP's predicted common fractional bar decrease, not target proof.
Dependencies: geometry121.py, paired121.py and their stated numerical stack.
"""
import sys,json,time
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import linprog
from geometry121 import *
from paired121 import model

def from_points(v):
 h=ConvexHull(v);assert h.equations[:,3].max()<0
 nr=-h.equations[:,:3]/h.equations[:,3,None];keep=[]
 for x in nr:
  if not any(np.linalg.norm(x-y)<1e-8 for y in keep):keep.append(x)
 return np.array(keep)

def capacity(n,tau=1e-6,trust=.02):
 G,v,J,pol=model(n);guards=v[:-6];D=v[-6:-4];dim=n.size;sc=np.repeat(np.linalg.norm(n,axis=1),3)
 A=np.vstack([np.column_stack([-J[:-6]*sc,np.zeros(len(guards))]),np.column_stack([J[-6:-4]*sc,np.maximum(D,1e-9)])]);b=np.r_[guards-tau,0.,0.]
 eq=np.column_stack([J[-4:]*sc,np.zeros(4)])
 lp=linprog(np.r_[np.zeros(dim),-1],A_ub=A,b_ub=b,A_eq=eq,b_eq=np.zeros(4),bounds=[(-trust,trust)]*dim+[(0,.2)],method='highs')
 return dict(success=bool(lp.success),fraction=float(lp.x[-1]) if lp.success else None,min_guard=float(guards.min()),duals=(-lp.ineqlin.marginals).tolist() if lp.success else [],policy=pol)

def scout(inp,out,side='both',limit=12):
 n=normalize(read_h(inp));G=geometry(n);n=n[G['active']];G=geometry(n);baseline=describe(n);baseD=np.array([baseline[z][0]['depth'] if baseline[z] else 0. for z in ['P','Q']]);ledger=[];saved=[];start=time.time();count=0
 out=Path(out);out.mkdir(exist_ok=True,parents=True)
 rng=np.random.default_rng(121030)
 for tag,x,edges in [('P',G['p'],G['pe']),('Q',G['q'],G['qe'])]:
  if side!='both' and side!=tag:continue
  a,w,A=arrows(x);pr=int(np.argmax((x*x).sum(1)));bb=bars(x,edges);jr=bb[0]['root'] if bb else pr
  eligible=[int(i) for i in np.argsort(a) if i not in {pr,jr} and a[i]>0][:limit]
  for i in eligible:
   j=int(w[i]);u=x[i];z=x[j]
   for lam in [.1,.25,.5,.75,.9]:
    for fraction in [.03,.1,.3,.6]:
     eps=fraction*lam*(1-lam)*np.sum((z-u)**2)/(u@u);point=(1+eps)*u+lam*(z-u)
     if not(u@(point-u)>0 and point@(z-point)>0):continue
     recipe=dict(side=tag,source=i,target=j,lambda_=lam,fraction=fraction,epsilon=float(eps));count+=1
     try:
      if tag=='Q':nn=np.vstack([n,point/(1+point@G['g'])])
      else:nn=from_points(np.vstack([G['v'],point+G['g']]))
      gg=geometry(nn);nn=nn[gg['active']]
      if len(nn)>85:raise ValueError('free-H support budget')
      jitter=0.
      if not gg['simple']:
       # Fixed, saved finite perturbation releases nonsimple H incidences.
       noise=rng.normal(size=nn.shape);nn=nn+1e-7*noise;jitter=1e-7;gg=geometry(nn)
      s=describe(nn);D=np.array([s[z][0]['depth'] if s[z] else 0. for z in ['P','Q']]);mn=[]
      for xx,ed in [(gg['p'],gg['pe']),(gg['q'],gg['qe'])]:
       aa,ww,_=arrows(xx);b=bars(xx,ed);rr=int(np.argmax((xx*xx).sum(1)));jj=b[0]['root'] if b else rr;idx=[k for k in range(len(xx)) if k not in {rr,jj}];mn.append(float(aa[idx].min()))
      ok=min(mn)>1e-8 and len(s['S'])<=2 and len(s['U'])<=2 and len(s['P'])<=1 and len(s['Q'])<=1 and all(D<=baseD*1.02+1e-9)
      rec=dict(recipe=recipe,VEF=s['VEF'],S=len(s['S']),U=len(s['U']),D=D.tolist(),min_guard=mn,accepted=bool(ok),jitter=jitter)
      if ok:
       fn='candidate_'+str(len(saved))+'.json';item=dict(n=nn.tolist(),recipe=recipe,stats=s,initial_hash_input=inp,jitter=jitter);(out/fn).write_text(json.dumps(item,indent=2)+'\n');rec['file']=fn;saved.append((float(np.sum(D/baseD)),fn))
      ledger.append(rec)
     except (ValueError,AssertionError,QhullError,np.linalg.LinAlgError) as ex:ledger.append(dict(recipe=recipe,error=str(ex)))
 print('RELAY121_FINITE_SCOUT',count,'admitted',len(saved),flush=True)
 ranked=[]
 # Capacity sampling is explicitly bounded: the best 12 by full bar sum plus
 # the 12 with greatest margin, at most 24 complete feasible bodies.
 order=[fn for _,fn in sorted(saved)[:12]]
 bymargin=sorted([r for r in ledger if r.get('accepted')],key=lambda r:-min(r['min_guard']))
 order+= [r['file'] for r in bymargin[:12] if r['file'] not in order]
 for fn in order:
  rr=json.loads((out/fn).read_text());nn=normalize(np.array(rr['n']))
  try:c=capacity(nn)
  except (ValueError,AssertionError,QhullError,np.linalg.LinAlgError) as ex:c=dict(success=False,error=str(ex))
  ranked.append(dict(file=fn,capacity=c,recipe=rr['recipe'],D=[rr['stats'][k][0]['depth'] if rr['stats'][k] else 0. for k in ['P','Q']]))
 ranked.sort(key=lambda r:-(r['capacity'].get('fraction') or -1));summary=dict(input=inp,side=side,limit=limit,baseline=baseline,base_capacity=capacity(n),ranked=ranked,count=count,admitted=len(saved),ledger=ledger,seconds=time.time()-start)
 (out/'scout.json').write_text(json.dumps(summary,indent=2)+'\n')
 print('RELAY121_DONE',side,'best',[(r['recipe'],r['D'],r['capacity'].get('fraction')) for r in ranked[:4]],flush=True)
 return summary
if __name__=='__main__':scout(sys.argv[1],sys.argv[2],sys.argv[3] if len(sys.argv)>3 else 'both',int(sys.argv[4]) if len(sys.argv)>4 else 12)
```

## nonlinear121.py — 4146 bytes, SHA 1e8ce1bfb930db5be173b70e36ad7931c92305396204f17ecacf26e974a7fdb7
```python
"""Direct nonlinear all-witness constrained continuation. Numerical only.
The complete actual H hull, uniform centroid and P/Q persistence are rebuilt
at every evaluation. Constraints use sorted outgoing maxima, excluding only
the global farthest vertex and the largest-persistence root on each side.
Padding to the Euler maximum keeps dimension fixed through fan retirement.
Every current nonroot remains constrained; this is not a sampled guard set.
Requires geometry121.py, paired121.py and their recorded numerical versions.
"""
import sys,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from geometry121 import read_h,normalize,describe
from paired121 import model

class Evaluation:
 def __init__(self,n,tau,prefix):
  self.n=n;self.scale=np.repeat(np.linalg.norm(n,axis=1),3);self.tau=tau;self.prefix=prefix
  self.dim=n.size;self.cap=[2*len(n)-6,len(n)-2];self.ng=sum(self.cap)
  self.G,self.v,self.J,self.pol=model(n);self.D=self.v[-6:-4].copy();self.start=time.time()
  self.last=None;self.records=[];self.best=None;self.best_t=-1e99
 def get(self,z):
  if self.last is not None and np.array_equal(z,self.last[0]):return self.last[1:]
  n=self.n+(z[:-1]*self.scale).reshape(self.n.shape)
  try:
   G,v,J,pol=model(n);size=[len(p['idx']) for p in pol];off=0;vv=[];jj=[]
   for k,num in enumerate(size):
    if num>self.cap[k]:raise ValueError('Euler padding overflow')
    order=np.argsort(v[off:off+num])+off
    vv.extend(v[order].tolist()+[1.]*(self.cap[k]-num))
    jj.extend(J[order].tolist()+[[0.]*self.dim]*(self.cap[k]-num));off+=num
   vv=np.array(vv);jj=np.array(jj)
   guards=(vv-self.tau)/.01
   depth=1-v[-6:-4]/self.D-z[-1]
   c=np.r_[guards,depth]
   dc=np.vstack([np.column_stack([jj*self.scale/.01,np.zeros(self.ng)]),np.column_stack([-J[-6:-4]*self.scale/self.D[:,None],-np.ones(2)])])
   eq=np.r_[v[-4:-1]/.1,v[-1]]
   deq=np.column_stack([J[-4:]*self.scale,np.zeros(4)]);deq[:3]/=.1
   feasible=float(min(guards))>=-1e-7 and float(min(depth))>=-1e-8 and max(abs(eq))<1e-7
   rec=dict(call=len(self.records),t=float(z[-1]),D=v[-6:-4].tolist(),min_guard=float(vv.min()),constraint_min=float(c.min()),eqmax=float(max(abs(eq))),feasible=bool(feasible),VEF=[len(G['v']),len(G['pe']),len(G['active'])])
   if feasible and z[-1]>self.best_t:
    self.best_t=float(z[-1]);self.best=dict(n=n.tolist(),stats=describe(n),t=self.best_t,record=rec)
    Path(self.prefix+'.best.json').write_text(json.dumps(self.best,indent=2)+'\n')
  except (ValueError,AssertionError,np.linalg.LinAlgError) as ex:
   c=np.full(self.ng+2,-1e3);dc=np.zeros((len(c),self.dim+1));eq=np.zeros(4);deq=np.zeros((4,self.dim+1));rec=dict(call=len(self.records),error=str(ex))
  self.records.append(rec);self.last=(z.copy(),c,dc,eq,deq)
  if len(self.records)%20==0:print('NONLINEAR121',len(self.records),rec,'best',self.best_t,flush=True)
  return c,dc,eq,deq

def run(inp,prefix,maxiter=120,trust=.04,tau=1e-6):
 n=normalize(read_h(inp));e=Evaluation(n,tau,prefix);z=np.zeros(n.size+1)
 def obj(z):return -z[-1]+1e-6*np.mean(z[:-1]**2),np.r_[2e-6*z[:-1]/n.size,-1.]
 res=minimize(obj,z,jac=True,method='SLSQP',bounds=[(-trust,trust)]*n.size+[(0,.2)],constraints=[dict(type='ineq',fun=lambda x:e.get(x)[0],jac=lambda x:e.get(x)[1]),dict(type='eq',fun=lambda x:e.get(x)[2],jac=lambda x:e.get(x)[3])],options=dict(maxiter=maxiter,ftol=1e-10))
 last=e.get(res.x);out=dict(input=inp,initial=n.tolist(),maxiter=maxiter,trust=trust,tau=tau,success=bool(res.success),status=int(res.status),message=str(res.message),iterations=int(res.nit),last_n=(n+(res.x[:-1]*e.scale).reshape(n.shape)).tolist(),last_t=float(res.x[-1]),last_constraint_min=float(min(last[0])),last_eqmax=float(max(abs(last[2]))),best=e.best,history=e.records,seconds=time.time()-e.start)
 Path(prefix+'.json').write_text(json.dumps(out,indent=2)+'\n');print('NONLINEAR121_DONE',res.success,res.message,'best',e.best_t,'last',res.x[-1],flush=True)
 return out
if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 120,float(sys.argv[4]) if len(sys.argv)>4 else .04,float(sys.argv[5]) if len(sys.argv)>5 else 1e-6)
```

## Complete exact patch recovering paired121_v1.py
The old version is a separate produced source, 5846 bytes, SHA fd98948b64933f77d49ea7733824866cab47a2d4584a6cdf8b45d6f5e5802cc9. Save and run the following Python script beside the complete current paired121.py from part1. No helper is omitted.
```python
from pathlib import Path
import hashlib
p=Path('paired121.py').read_bytes()
assert hashlib.sha256(p).hexdigest()=='903d5ca44c69f8f60b598c9a9b328b7b7748194d3ac88bf4a11e3202d86baa36'
s=p.decode()
a="  # Restore the fixed positive margin at each linear step; do not creep\n  # along the lower finite-admission boundary.\n  floor=np.full_like(guards,tau)"
b="  # Never ask a guard already below tau to jump instantly; do not weaken it.\n  floor=np.minimum(tau,guards)"
assert s.count(a)==1
s=s.replace(a,b)
a="  if it%10==0 or not good:print('PAIRED121',mode,it,accepted,D,'=>',[b['depth'] for b in rec.get('stats',{}).get('P',[])],[b['depth'] for b in rec.get('stats',{}).get('Q',[])],min(guards),delta,flush=True)"
b="  if it%10==0 or not good:print('PAIRED121',mode,it,accepted,D,'=>',rec.get('stats',{}).get('P',[{}])[0].get('depth'),rec.get('stats',{}).get('Q',[{}])[0].get('depth'),min(guards),delta,flush=True)"
assert s.count(a)==1
s=s.replace(a,b)
assert len(s.encode())==5846
assert hashlib.sha256(s.encode()).hexdigest()=='fd98948b64933f77d49ea7733824866cab47a2d4584a6cdf8b45d6f5e5802cc9'
Path('paired121_v1.py').write_text(s)
print('J121_OLD_SOURCE_EXACTLY_RECOVERED')
```

## Complete commands and observed finite limits
Each command below was actually executed with OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1. Floating solver histories include wall-clock seconds and are not byte-deterministic output certificates. Preserve frozen input arrays for direct continuation; do not replace a floating input by its rounded rational endpoint without declaring a new experiment.

1. `python coforest121.py J119_FREEH_P_G6.txt coforest_P 120 .01`: 31 accepted steps, terminal finite_policy_trust_stall. V88/E132/F46, numerical S30/U25, 24 P and29 Q above the display floor. Worst outgoing nonroot rho improved to -.02591217385798 but main P=.2150643344148797,Q=.3148963317505027. Thus max-min improvement can spread a deficit to many roots. This is a finite failed search, not an exact census or family exclusion.
2. `python paired121_v1.py J119_FREEH_P_G6.txt paired_P 120 .01 .000001`: completed120 accepted steps, iteration_limit, V92/E138/F48,numerical2/2,P=.18126127622156474,Q=.24005699333945485. The old floor could creep along the finite admission boundary; the current source restores the fixed positive tau at each LP.
3. `python paired121.py J119_FREEH_Q_G6.txt paired_Q_qp 80 .02 .00001 qp`: completed80 accepted steps, iteration_limit, V88/E132/F46,numerical2/2,P=.2492945423813251,Q=.20764983978906115. This exact floating .last.json array is the input for items5,8,9. Its rounded G8 exact body is distinct and in [internal-source-reference].
4. `python paired121.py J119_FREEH_P_G6.txt paired_P_qp 80 .02 .00001 qp`: execution ended at the enclosing tool time limit after20 accepted steps. Only a .last.json checkpoint, not a terminal80-step result, was observed: V92/E138/F48,numerical2/2,P=.180898394472935,Q=.23958384032478053. A complete bounded replay may run20 iterations; do not reproduce a timeout as a scientific stopping criterion.
5. `python relays121.py paired_Q_qp.last.json relay_Q both 12`: complete480 proposals,196 finite admitted bodies, explicitly at most24 full LP capacity samples. Capacity is one LP's predicted fractional paired-depth improvement, not a cancellation proof. Baseline fraction .008980204627204304. Candidate32 (P68->86,lambda=.1,fraction=.03,epsilon=.00006823439059157263) predicts .03640094912682933. Candidate116 (Q13->11,lambda=.5,fraction=.03,epsilon=.0005492790044595085) predicts .03580442664518819. The P continuation below uses candidate16 instead, P83->82,lambda=.25,fraction=.1,epsilon=.00038380544161564583. All labels are the scout's floating order; they are not exact-auditor labels. Random seed121030 and every finite test are literal above. The raw scout count and admitted count must not be replaced by an older compacted narrative's incorrect123.
6. `python paired121.py relay_Q/candidate_16.json paired_relayP 60 .02 .000001 qp`: completed60 accepted steps,iteration_limit,V96/E144/F50,numerical2/2,P=.24767722771736123,Q=.20630398503512715. Rounded G8 exact body has strict222/weak000/primitive000 with sole P/Q, not110.
7. `python paired121.py relay_Q/candidate_116.json paired_relayQ 60 .02 .000001 qp`: completed60 accepted steps,iteration_limit,V90/E135/F47,numerical2/2,P=.24535746695470784,Q=.20436877430820333. This uses only one additional physical H support. Its G8 exact body is strict222/weak000/primitive000, sole P/Q; it is not a one-sided cancellation.
8. `python nonlinear121.py paired_Q_qp.last.json nonlinear_Q 90 .04 .000001`: terminated unsuccessful with 'More than 3*n iterations in LSQ subproblem'. No feasible improved endpoint, best t=0 (the start). Last t=.006733685164773057; lower depths at infeasible iterates came with negative unwanted guards and nonzero normalization constraints. No general nonlinear-chart exclusion follows.
9. `python nonlinear121.py paired_Q_qp.last.json nonlinear_Q_small 65 .01 .000001`: same explicit unsuccessful termination, no feasible improvement, best t=0; last t=.0031995293165453633. This narrower trust box did not resolve the simultaneous finite guard/fan difficulty.

Observed producer markers are COFOREST121_DONE, PAIRED121_DONE, RELAY121_DONE and NONLINEAR121_DONE with the stated success/limit values. Item4 has no final marker. The numerical G8 freezes use nint=np.rint(n*10**8).astype(np.int64) and integer H input 'm 100000000', not coordinate rounding of the physical vertices. All three exact terminal markers and exact output hashes are in [internal-source-reference]. No method here proves own110 or promotes a new canonical construction.
