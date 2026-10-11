# material-3c21f31328b2

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Incidence-adaptive rooted escape search V3–V7: complete new source units

## Status
Numerical proposal methods only; no new own110 is claimed. Every trial rebuilds the actual hull and filled-solid centroid. The numerical E=V+F-2 diagnostic uses tolerance-merged supports and is not an exact edge certificate. No H/weak audit is made by this search. The two rational V6 descendants independently audited as C366 own211/weak000 are preserved in full in [internal-source-reference]; the accepted own110 remains C622. Frozen numerical output preservation is separate from this source unit. The exact rational pair is recoverable independently of numerical optimisation replay.

V3 selects rooted paths by SUM of squared deficits plus a tiny positive cost, while its LP largely targets the WORST deficit. At the unchanged C372/C378 inputs its worst selected arcs are about-0.1594406/-0.1187947, versus the exact optimum root-reaching bottlenecks-0.09086810349921773/-0.07828908477931579 certified in [internal-source-reference]. V4 corrects that objective mismatch by maximum-bottleneck rooted paths and a max-deficit merit. Unprotected V3/V4 progress creates many unwanted U. V5 hard-protects physical root reach, but creates a third S. V6 additionally protects current positive local polar escapes and accepts only S<=2. V7 relaxes the physical guard from1e-6 to1e-8 and tightens LP feasibility from1e-9 to1e-10; it makes only modest further polar progress while spending another roughly hundredfold factor of positive primal margin. None of the twenty finite V3–V7 runs establishes own110. These observations are not continuous-family exclusions.

## Exact dependencies, versions and commands
Python3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, binary64, one thread, no GPU, assertions enabled. OPENBLAS/OMP/MKL threads1 are set before imports. All numerical constants, LP and line-search settings are literal below.

V3–V6 exact input reports come from the full immutable NC57 result figure-0398,73935 bytes,SHA256 b6c84be62ea56d1c11575d4d6309563f525d734f79b0ad2a299f0b7abd2ccdd3. Parent was read0->eof. Its full decoder reconstructs:
- proof/C372_ALT_FULL_G4/REPORT.json,14190 bytes,SHA256639b7dd56caf48ee99f1175e20b1f305100dc0fb3f75440dd20aba8df57b4cb5.
- proof/C378_ALT_POLY_G6/REPORT.json,18534 bytes,SHA256fc46fb08252486d5c2474d70c6834b2f4849f8de25bcf18ccb059a7aa9ced661.
V7 inputs are the exact G7/G8 reports regenerated from [internal-source-reference]:
G7 REPORT19442 bytes,2e79def1fe584c45b20cbf703903e45ba6e7d91891815c24620571cdd1c12596;
G8 REPORT21373 bytes,c352866aa2eee361c941c064073494ff15560fdc06e959d5b1ae3e4d59eabf41.

CLI:
 python -B HULL_LP_Vv.py INPUT_REPORT.json NEW_OUTPUT_DIRECTORY STEPS GAMMA SEED PERTURB INITIAL_TRUST
For v3..6 and n372/378,k0/1: gamma=[0.001,0.0001][k],seed=100*n+10*v+1+k,perturb0,initialtrust0.005. Steps300 for V3,150 for V4–V6. Four independent cases per version were run as separate CPU processes.
For V7: g7/8,k0/1, input exact Gg report,steps200,gamma0.0001,seed=7370+10*g+k,perturb0,initialtrust=[0.02,0.1][k].

Observed terminal SUMMARY values (diagnostic V/E/F;S/U, no H assertion):
V3_372_0:50 iterations,63/183/122;3/17,merit0.041709148718154856.
V3_372_1:58,63/183/122;3/16,0.039862559516361064.
V3_378_0:62,63/183/122;5/17,0.03524714621240012.
V3_378_1:75,63/183/122;5/16,0.03469302278950974.
V4_372_0:38,51/147/98;4/15,0.0409747104528996.
V4_372_1:38,51/147/98;4/15,0.040074710452894714.
V4_378_0:147,51/147/98;9/13,0.0184545157739906.
V4_378_1:149,51/147/98;9/13,0.01755443860732573.
V5_372_0:150,63/183/122;3/1,0.04232223780810322.
V5_372_1:150,63/183/122;3/1,0.041422237808109295.
V5_378_0:150,64/186/124;3/1,0.049374297256260816.
V5_378_1:150,64/186/124;3/1,0.04847429725626879.
V6_372_0:76,63/183/122;2/1,0.050471961159442566,primal9.968741561623277e-7.
V6_372_1:79,63/183/122;2/1,0.0495722650665204,primal9.965402043997672e-7.
V6_378_0:150,65/189/126;2/1,0.04974379381695935,primal5.304859131362062e-7.
V6_378_1:150,65/189/126;2/1,0.04884379381695991,primal5.3048591312377e-7.
V7_G7_0:94,63/183/122;2/1,0.0472680090416634,primal8.031933860794965e-9.
V7_G7_1:114,63/183/122;2/1,0.0474128096839885,primal7.719513403542923e-9.
V7_G8_0:85,63/183/122;2/1,0.04729452985307344,primal8.314410296495564e-9.
V7_G8_1:88,63/182/121;2/1,0.04712427883495114,primal9.68599209766959e-9. Its numerical182-edge estimate especially must NOT be promoted without exact maximal-support reconstruction.

Each source writes INPUT_REPORT.json,OPTIONS.json,BEST.json,CURRENT.json,FINAL.json,SUMMARY.json,TRACE.json and a NUMERICAL_WINNER.json only if its numerical gate is met. Terminal COORD_HULL_LP_FINISHED means completion, NOT success. BEST is lexicographic(S+U,merit), not necessarily FINAL. Floating gate survivors require rational freezing and independent full audits.

## Source recovery and hashes
Historical complete V3 chain, all read in full this turn:
V1 [internal-source-reference] -> HULL_LP.py6471 bytes SHA256ff8e633486cd8117106117a64c81c31a66aadac7489ee82054ae61e916420185.
V2 [internal-source-reference] -> HULL_LP_V2.py6379 bytes SHA2565afffaec9998a27a7b76165098d6d4346b127f3a796c432ea83721b3780890da.
V3 [internal-source-reference] -> HULL_LP_V3.py7153 bytes SHA256d049cd5a5cb87a97c0a9276139d6576931bf71fb49427974753be1d15ff1a98a.
CORRECTION: V3 prose's nonexistent V2 material [internal-source-reference] must be [internal-source-reference]. The original literal code/hash was correct.

Complete patches below:
BOTTLENECK_PATCH.py1518 bytes SHA256373ec4ed88de8d0dd3583407c41f62b7b717faa6410810d49d30b0e5bea740f5 -> V4.py7060 bytes SHA25630c8d008641fe258079c1024513649f316d9e2dcbf2339cbcd6e9e86042c2a9c.
PROTECTED_U_PATCH.py1723 bytes SHA256ef97d24b04de4f1e06d9e75d625079096eb080d9cff5d843a5b229e0b1c5196f -> V5.py7487 bytes SHA2565979a4cc18fb547dd80cf89121d8951253343d23cc4ba7d75b1f7e44b9cc6b4a.
PROTECTED_SU_PATCH.py1519 bytes SHA256fead020913c3a5fcd30900496f623c77c44d1847727a5a9d25d5fad422d29f67 -> V6.py7739 bytes SHA256561fac0b1615743db8cabcbee7be7c4b3843caf42f584ccae40ca40656a81582.
LOOSE_GUARD_PATCH.py775 bytes SHA256a28ea974ba603a37cb45cfdb7c4c46ccbdc788573df18516d353b47248ee1cd0 -> V7.py7743 bytes SHA256ce7a50b0e6835d0cd1a9b7670431d6b39c2caf7e7fb86d71760da278e1a88b4f.
Commands python -B -S PATCH.py INPUT.py OUTPUT.py assert the exact input hash. The standalone V6 below removes the need for V1–V5 dependencies when continuing V6/V7. Preserve exactly one newline at each code block's end and compare file hashes. Intermediate nonproduction V4 hash885ed... must not be used.

## Complete BOTTLENECK_PATCH.py
```python
#!/usr/bin/env python3
"""Replace sum-cost rooted targets by maximum-bottleneck rooted targets."""
from pathlib import Path
import hashlib,sys
raw=Path(sys.argv[1]).read_bytes()
assert hashlib.sha256(raw).hexdigest()=='d049cd5a5cb87a97c0a9276139d6576931bf71fb49427974753be1d15ff1a98a'
s=raw.decode();start=s.index('def rooted_targets(');end=s.index('def state(',start)
helper='''def rooted_targets(A,root,gamma):
 # Maximum bottleneck paths toward root. Parents always settle earlier.
 n=len(A);capacity=np.full(n,-np.inf);capacity[root]=np.inf
 done=np.zeros(n,dtype=bool);parent=np.full(n,-1,dtype=int)
 for _ in range(n):
  k=int(np.argmax(np.where(done,-np.inf,capacity)));done[k]=True
  cand=np.minimum(A[:,k],capacity[k]);better=(~done)&(cand>capacity)
  capacity[better]=cand[better];parent[better]=k
 ids=np.array([i for i in range(n) if i!=root]);assert np.all(parent[ids]>=0)
 return ids,parent[ids]

'''
s=s[:start]+helper+s[end:]
a="version='COORD_HULL_LP_V3_RADIAL_ROOTED',tree_cost='max(gamma-escape,0)^2+(gamma^2+1e-24)*1e-6',tree_refresh='every_trial'"
b="version='COORD_HULL_LP_V4_BOTTLENECK_MINIMAX',tree_cost='maximum minimum radial escape on root-reaching path',tree_refresh='every_trial'"
assert s.count(a)==1;s=s.replace(a,b)
s=s.replace('merit=float(d.max()+.2*d.mean())','merit=float(d.max())').replace('mp=float(pred.max()+.2*pred.mean())','mp=float(pred.max())')
Path(sys.argv[2]).write_text(s)
print('COORD_HULL_LP_BOTTLENECK_PATCHED',len(s.encode()),hashlib.sha256(s.encode()).hexdigest())
```

## Complete PROTECTED_U_PATCH.py
```python
#!/usr/bin/env python3
"""Exact patch V4 -> V5. Hard primal root reach; minimise polar root deficit."""
import sys,hashlib
from pathlib import Path
p=Path(sys.argv[1]);s=p.read_text()
assert hashlib.sha256(p.read_bytes()).hexdigest()=='30c8d008641fe258079c1024513649f316d9e2dcbf2339cbcd6e9e86042c2a9c'
s=s.replace("torch.set_num_threads(1);torch.set_default_dtype(torch.float64)","torch.set_num_threads(1);torch.set_default_dtype(torch.float64)\nPRIMAL_GUARD=1e-6")
s=s.replace("loss=float(d@d),merit=float(d.max()),worst=float(d.max()),", "loss=float(d@d),merit=float(d[len(ui):].max()),worst=float(d.max()),\n         primal_tree_margin=float(e[:len(ui)].min()),polar_tree_margin=float(e[len(ui):].min()),")
s=s.replace("version='COORD_HULL_LP_V4_BOTTLENECK_MINIMAX'", "version='COORD_HULL_LP_V5_PROTECTED_U',primal_guard=PRIMAL_GUARD,accept_primal_guard=PRIMAL_GUARD/2")
s=s.replace("if r['S']==r['U']==1 and r['margin']>gamma*.1:","if r['S']==r['U']==1 and r['primal_tree_margin']>PRIMAL_GUARD/2 and r['polar_tree_margin']>gamma*.1:")
s=s.replace("A=vstack([hstack([-csr_matrix(J),csr_matrix((m,D)),-np.ones((m,1))]),", "zcoeff=np.r_[np.zeros(len(ui)),np.ones(len(si))][:,None]\n  required=np.r_[np.full(len(ui),PRIMAL_GUARD),np.full(len(si),gamma)]\n  A=vstack([hstack([-csr_matrix(J),csr_matrix((m,D)),-zcoeff]),")
s=s.replace("b=np.r_[e-gamma,np.zeros(2*D)]", "b=np.r_[e-required,np.zeros(2*D)]")
s=s.replace("mp=float(pred.max())", "mp=float(pred[len(ui):].max())")
s=s.replace("if sr['merit']<r['merit']-", "if sr['U']==1 and sr['primal_tree_margin']>PRIMAL_GUARD/2 and sr['merit']<r['merit']-")
assert s!=p.read_text()
Path(sys.argv[2]).write_text(s)
print(len(s.encode()),hashlib.sha256(s.encode()).hexdigest())
```

## Complete PROTECTED_SU_PATCH.py
```python
#!/usr/bin/env python3
"""Exact V5 -> V6 patch: protect local positive polar escapes as well as U."""
import sys,hashlib
from pathlib import Path
p=Path(sys.argv[1]);s=p.read_text()
assert hashlib.sha256(p.read_bytes()).hexdigest()=='5979a4cc18fb547dd80cf89121d8951253343d23cc4ba7d75b1f7e44b9cc6b4a'
s=s.replace("return P,F,reps,(ui,ut,si,st),sm", "li=np.where(s>0)[0];lt=np.argmax(aS[li],axis=1);lg=np.minimum(1e-6,s[li]/2)\n return P,F,reps,(ui,ut,si,st,li,lt,lg),sm")
s=s.replace("ui,ut,si,st=targets;D=P.size", "ui,ut,si,st,li,lt,lg=targets;D=P.size")
s=s.replace("version='COORD_HULL_LP_V5_PROTECTED_U'", "version='COORD_HULL_LP_V6_PROTECTED_SU',polar_local_guard='min(1e-6,current_positive_local_escape/2)',maximum_accepted_S=2")
s=s.replace("torch.cat((arrows(X,ui,ut),arrows(Q[reps],si,st)))", "torch.cat((arrows(X,ui,ut),arrows(Q[reps],si,st),arrows(Q[reps],li,lt)))")
s=s.replace("zcoeff=np.r_[np.zeros(len(ui)),np.ones(len(si))][:,None]", "zcoeff=np.r_[np.zeros(len(ui)),np.ones(len(si)),np.zeros(len(li))][:,None]")
s=s.replace("required=np.r_[np.full(len(ui),PRIMAL_GUARD),np.full(len(si),gamma)]", "required=np.r_[np.full(len(ui),PRIMAL_GUARD),np.full(len(si),gamma),lg]")
s=s.replace("mp=float(pred[len(ui):].max())", "mp=float(pred[len(ui):len(ui)+len(si)].max())")
s=s.replace("if sr['U']==1 and sr['primal_tree_margin']", "if sr['S']<=2 and sr['U']==1 and sr['primal_tree_margin']")
assert s!=p.read_text()
Path(sys.argv[2]).write_text(s)
print(len(s.encode()),hashlib.sha256(s.encode()).hexdigest())
```

## Complete standalone HULL_LP_V6.py
```python
#!/usr/bin/env python3
"""Incidence-adaptive own-mass escape LP. Numerical proposals only.
Usage: HULL_LP.py REPORT.json OUT steps gamma seed perturb trust
Every trial rebuilds actual hull/own centroid; no frozen-triangle convexity wall.
CPython3.13.5 numpy2.3.5 scipy1.17.0 torch2.10.0+cpu; binary64, threads1.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import sys,json,hashlib,platform
from pathlib import Path
from fractions import Fraction
import numpy as np
import scipy
import torch
from scipy.optimize import linprog
from scipy.spatial import ConvexHull,QhullError
from scipy.sparse import csr_matrix,hstack,vstack,eye
assert __debug__
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
PRIMAL_GUARD=1e-6
def enc(v):return json.dumps(v,sort_keys=True,separators=(',',':'))+'\n'
def hx(P):return [[float(x).hex() for x in p] for p in P]
def geometry(z,F):
 T=z[F];a,b,c=T[:,0],T[:,1],T[:,2];w=(a*torch.linalg.cross(b,c)).sum(1)/6
 v=w.sum();g=(w[:,None]*(a+b+c)).sum(0)/(4*v);X=z-g
 n=torch.linalg.cross(b-a,c-a);q=n/(n*X[F[:,0]]).sum(1)[:,None]
 return X,q,g,v

def arrows(W,i,j):
 a=W[i];d=W[j]-a
 return (a*d).sum(1)/(a*a).sum(1)

def all_escape(W):
 D=W[None,:,:]-W[:,None,:];r=np.linalg.norm(W,axis=1);dn=np.linalg.norm(D,axis=2)
 # Coincident numerical facet normals represent the same support, not a new root.
 bad=dn<1e-12*np.maximum(1,r[:,None]);dn[bad]=1
 a=np.einsum('ik,ijk->ij',W,D)/(r[:,None]**2);a[bad]=-np.inf
 return a

def rooted_targets(A,root,gamma):
 # Maximum bottleneck paths toward root. Parents always settle earlier.
 n=len(A);capacity=np.full(n,-np.inf);capacity[root]=np.inf
 done=np.zeros(n,dtype=bool);parent=np.full(n,-1,dtype=int)
 for _ in range(n):
  k=int(np.argmax(np.where(done,-np.inf,capacity)));done[k]=True
  cand=np.minimum(A[:,k],capacity[k]);better=(~done)&(cand>capacity)
  capacity[better]=cand[better];parent[better]=k
 ids=np.array([i for i in range(n) if i!=root]);assert np.all(parent[ids]>=0)
 return ids,parent[ids]

def state(P,gamma):
 H=ConvexHull(P);idx=np.sort(H.vertices);P=P[idx];H=ConvexHull(P)
 F=H.simplices.copy();T=P[F];n=np.cross(T[:,1]-T[:,0],T[:,2]-T[:,0]);flip=np.einsum('ij,ij->i',n,H.equations[:,:3])<0;F[flip]=F[flip][:,[0,2,1]]
 with torch.no_grad():X,Q,g,v=geometry(torch.tensor(P),F)
 x=X.numpy();q=Q.numpy();g=g.numpy();v=float(v)
 assert v>1e-12 and np.isfinite(q).all()
 # Select one representative of numerically coplanar maximal supports.
 reps=[]
 for i in range(len(q)):
  if not any(np.linalg.norm(q[i]-q[j])<1e-11*max(1,np.linalg.norm(q[i]),np.linalg.norm(q[j])) for j in reps):reps.append(i)
 reps=np.array(reps,dtype=int);q1=q[reps]
 aU=all_escape(x);aS=all_escape(q1);u=aU.max(1);s=aS.max(1)
 ru=int(np.argmax((x*x).sum(1)));rs=int(np.argmax((q1*q1).sum(1)))
 ui=np.array([i for i in range(len(x)) if i!=ru]);si=np.array([i for i in range(len(q1)) if i!=rs])
 ui,ut=rooted_targets(aU,ru,gamma);si,st=rooted_targets(aS,rs,gamma);e=np.r_[aU[ui,ut],aS[si,st]];d=np.maximum(gamma-e,0)
 cov=x.T@x/len(x);ev=np.linalg.eigvalsh(cov)
 assert ev[0]>1e-10*ev[-1]
 sm=dict(V=len(P),F=len(q1),E=len(P)+len(q1)-2,S=int((s<0).sum()),U=int((u<0).sum()),
         margin=float(e.min()),local_escape_margin=float(np.r_[u[ui],s[si]].min()),loss=float(d@d),merit=float(d[len(ui):].max()),worst=float(d.max()),
         primal_tree_margin=float(e[:len(ui)].min()),polar_tree_margin=float(e[len(ui):].min()),
         volume=v,centroid=g.tolist(),root_u=ru,root_s=rs,stable=np.where(s<0)[0].tolist(),unstable=np.where(u<0)[0].tolist(),
         stable_owners=[sorted(F[reps[i]].tolist()) for i in np.where(s<0)[0]],
         root_s_owners=sorted(F[reps[rs]].tolist()),covariance_ratio=float(ev[0]/ev[-1]))
 li=np.where(s>0)[0];lt=np.argmax(aS[li],axis=1);lg=np.minimum(1e-6,s[li]/2)
 return P,F,reps,(ui,ut,si,st,li,lt,lg),sm

def main(src,out,steps,gamma,seed,perturb,initial_trust):
 raw=Path(src).read_bytes();ob=json.loads(raw);P=np.array([[float(Fraction(v)) for v in p] for p in ob['points']])
 rng=np.random.default_rng(seed);P=P+perturb*rng.normal(size=P.shape)
 P,F,reps,targets,r=state(P,gamma);P-=np.array(r['centroid']);P/=np.sqrt((P*P).sum(1).mean())
 out=Path(out);out.mkdir(parents=True,exist_ok=False);(out/'INPUT_REPORT.json').write_bytes(raw)
 options=dict(steps=steps,gamma=gamma,seed=seed,perturb=perturb,initial_trust=initial_trust,max_trust=.12,
              line_search=16,lp_feasibility=1e-9,L1weight=1e-5,facetmerge=1e-11,coincidentnormals=1e-12,
              volume_floor=1e-12,covariance_ratio_floor=1e-10,stop_margin=gamma*.1,version='COORD_HULL_LP_V6_PROTECTED_SU',polar_local_guard='min(1e-6,current_positive_local_escape/2)',maximum_accepted_S=2,primal_guard=PRIMAL_GUARD,accept_primal_guard=PRIMAL_GUARD/2,tree_cost='maximum minimum radial escape on root-reaching path',tree_refresh='every_trial',
              input_sha256=hashlib.sha256(raw).hexdigest(),python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,torch=torch.__version__)
 (out/'OPTIONS.json').write_text(enc(options));trace=[];best=None;trust=initial_trust
 def keep(label,P,r): (out/(label+'.json')).write_text(enc(dict(points_hex=hx(P),record=r,options=options)))
 for it in range(steps):
  P,F,reps,targets,r=state(P,gamma);ui,ut,si,st,li,lt,lg=targets;D=P.size
  key=(r['S']+r['U'],r['merit'])
  if best is None or key<best:best=key;keep('BEST',P,r);print('HULL_LP_BEST',it,r,flush=True)
  keep('CURRENT',P,r)
  if r['S']==r['U']==1 and r['primal_tree_margin']>PRIMAL_GUARD/2 and r['polar_tree_margin']>gamma*.1:keep('NUMERICAL_WINNER',P,r);break
  def fun(z):
   X,Q,g,v=geometry(z.reshape((-1,3)),F)
   return torch.cat((arrows(X,ui,ut),arrows(Q[reps],si,st),arrows(Q[reps],li,lt)))
  z=torch.tensor(P.ravel(),requires_grad=True);e=fun(z).detach().numpy();J=torch.autograd.functional.jacobian(fun,z,vectorize=True).numpy();m=len(e)
  zcoeff=np.r_[np.zeros(len(ui)),np.ones(len(si)),np.zeros(len(li))][:,None]
  required=np.r_[np.full(len(ui),PRIMAL_GUARD),np.full(len(si),gamma),lg]
  A=vstack([hstack([-csr_matrix(J),csr_matrix((m,D)),-zcoeff]),
            hstack([eye(D),-eye(D),csr_matrix((D,1))]),hstack([-eye(D),-eye(D),csr_matrix((D,1))])],format='csr')
  b=np.r_[e-required,np.zeros(2*D)];obj=np.r_[np.zeros(D),np.full(D,1e-5/D),1.]
  lp=linprog(obj,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*D+[(0,trust)]*D+[(0,None)],method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
  rec=dict(iteration=it,before=r,trust=trust,lp_status=int(lp.status),accepted=False)
  if lp.success:
   delta=lp.x[:D].reshape(P.shape);pred=np.maximum(gamma-e-J@delta.ravel(),0);mp=float(pred[len(ui):len(ui)+len(si)].max());rec['predicted_merit']=mp
   for ls in range(16):
    alpha=2.**(-ls)
    try:
     trial,tf,tr,tt,sr=state(P+alpha*delta,gamma)
     if sr['S']<=2 and sr['U']==1 and sr['primal_tree_margin']>PRIMAL_GUARD/2 and sr['merit']<r['merit']-1e-5*alpha*max(r['merit']-mp,1e-12):
      P=trial
      rec.update(accepted=True,alpha=alpha,after=sr);trust=min(.12,trust*(1.3 if alpha==1 else .8));break
    except (QhullError,AssertionError,ValueError,np.linalg.LinAlgError):pass
  if not rec['accepted']:trust*=.5
  trace.append(rec);(out/'TRACE.json').write_text(enc(trace));print('HULL_LP_STEP',it,rec['accepted'],trust,rec.get('after',r)['merit'],flush=True)
  if trust<1e-8:break
 P,F,reps,targets,r=state(P,gamma);keep('FINAL',P,r);(out/'SUMMARY.json').write_text(enc(dict(final=r,best_key=best,iterations=len(trace),options=options)))
 print('COORD_HULL_LP_FINISHED',r,flush=True)
if __name__=='__main__':main(sys.argv[1],sys.argv[2],int(sys.argv[3]),float(sys.argv[4]),int(sys.argv[5]),float(sys.argv[6]),float(sys.argv[7]))
```

## Complete LOOSE_GUARD_PATCH.py
```python
#!/usr/bin/env python3
"""Exact V6 -> V7 patch; relax the primal guard, tighten LP feasibility."""
import sys,hashlib
from pathlib import Path
p=Path(sys.argv[1]);s=p.read_text()
assert hashlib.sha256(p.read_bytes()).hexdigest()=='561fac0b1615743db8cabcbee7be7c4b3843caf42f584ccae40ca40656a81582'
s=s.replace('PRIMAL_GUARD=1e-6','PRIMAL_GUARD=1e-8').replace("version='COORD_HULL_LP_V6_PROTECTED_SU'","version='COORD_HULL_LP_V7_LOOSE_U_GUARD'")
s=s.replace('lp_feasibility=1e-9','lp_feasibility=1e-10').replace("'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9","'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10")
assert s!=p.read_text();Path(sys.argv[2]).write_text(s)
print(len(s.encode()),hashlib.sha256(s.encode()).hexdigest())
```

## Complete ROUND_AND_AUDIT.py
```python
#!/usr/bin/env python3
"""Frozen binary64 endpoint -> rational grid, independent NC57 A/B plus third mass."""
import sys,json,hashlib,subprocess
from pathlib import Path
from fractions import Fraction as Q

def main(nc57,endpoint,out,k):
 endpoint=Path(endpoint);out=Path(out);out.mkdir(parents=True,exist_ok=False);k=int(k);N=10**k
 raw=endpoint.read_bytes();x=json.loads(raw)
 d=dict(identity=f'COORD_HULL_V6_C372_FINAL_G{k}',grid=N,rows=[[round(Q(float.fromhex(t))*N)for t in p]for p in x['points_hex']],endpoint_sha256=hashlib.sha256(raw).hexdigest(),rounding='Exact Fraction(binary64 fromhex) times integer grid, nearest ties-to-even')
 cp=out/'CHECKPOINT.json';cp.write_text(json.dumps(d,sort_keys=True,separators=(',',':'))+'\n')
 subprocess.run([sys.executable,'-B','-S',str(Path(nc57)/'EXACT_NEW.py'),'points',str(cp),str(out/'proof')],check=True)
 subprocess.run([sys.executable,'-B','-S',str(Path(nc57)/'INDEPENDENT_TRIPLES.py'),str(out/'proof/REPORT.json'),str(out/'TRIPLES.json')],check=True)
 print('COORD_FROZEN_V6_RATIONAL_AB_MASS_TRIPLES_PASS',k,flush=True)
if __name__=='__main__':main(*sys.argv[1:])
```
ROUND_AND_AUDIT.py1119 bytes,SHA256c08bcec09ae9047da2d23d426b534e148ff962eeb12573b0064e6dc77270daa7. This identity convention is specific to V6_372_1 FINAL; it must be changed explicitly for unrelated frozen points. Exact G7/G8 literal checkpoints and their complete audit receipts remain authoritative in [internal-source-reference].
