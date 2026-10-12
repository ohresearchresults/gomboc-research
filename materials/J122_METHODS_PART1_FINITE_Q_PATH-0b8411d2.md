# material-0b8411d2967e

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J122 numerical methods — Recovery capsule part 1/4: finite whole-Q paths

This part preserves the complete materially successful finite-Q producing method, its original versions and the directed widest-path helper. Numerical continuation is not a strict/weak certificate. The resulting NEW exact own121 body is separately reconstructible from [internal-source-reference]; it is NOT own110. Its exact audit has V90/E135/F47, one P~.637419005758565, Q[], additionalweak000/primitivezero000, both U disjoint from its sole S.

Complete inherited dependency geometry121.py is in [internal-source-reference] (J121_NUMERICAL_METHODS_PART1OF2.md), source5112B/SHA b64da8c4140fba3954b28323d603be3813b0643ed6aca18b195a2b62f2c44bf2c44bf2. CORRECTION: the exact source SHA is b64da8c4140fba3954b28323d603be3813b0643ed6aca18b195a2b62f2c44bf2; the preceding longer string is not an identity. The literal starting H input J121_PAIRED_RELAYQ_G8.txt is1417B/SHA4f31b3ee611dd5af8c30f559372abf0e5d46ec80725a3aa73ec59b7b04fab828, fully in [internal-source-reference]. No C622 or worker sandbox is a dependency. Select those two exact materials when the computation needs them. Part4 preserves the literal consumed intermediate fields; named files alone do not supply them.

Observed numerical environment Python3.13.5,NumPy2.3.5,SciPy1.17.0,Torch2.10.0+cpu,float64, one BLAS/OMP/Torch thread. The imported geometry121 sets Torch defaults. Numerical hull grouping uses explicit tolerances and is not exact incidence. Its describe() displays P/Q above1e-12 and S/U below-1e-10, while all_positive_float_P/Q retain every positive floating bar. No filtered display is evidence of cancellation. The exact auditor, not these diagnostics, proved the G8 endpoint.

## Mechanism
For distinct centred points x,y, x.(y-x)>0 implies |y|²>|x|². Thus positive directed cycles are impossible. Widest paths toward the largest-radius elder optimize the least angular arrow on a COMPLETE directed path. A reverse settled-set construction gives an acyclic parent policy even with negative scores. All resulting nonelder levels strictly positive would exclude all other radial maxima. The theorem applies to physical vertices for U and actual centred polar points for S. The numerical method changes the full deficient-root path, including its old positive return, while protecting other individual outgoing witnesses and recomputing actual homogeneous mass on each finite trial. It is not a global-convergence theorem, a proof of a clean intermediate equilibrium homotopy, or equivalent to reducing only a root's local maximum guard.

## forest122.py — complete1862B
SHA c1fcebfa7bbe62a5045ec2fa8ddc472ef42f8064d5d497d268bef474bb04ea4c.
```python
"""Exact-path combinatorics on floating radial scores, J122 discovery only.
Widest paths are rooted trees, never the cyclic local argmax policy.
Finite hulls use actual uniform-volume mass through geometry121.
"""
import numpy as np
from geometry121 import arrows

def widest(a,elder):
    m=len(a);levels=np.full(m,-np.inf);levels[elder]=np.inf
    parent=np.full(m,-1,int);done=np.zeros(m,bool);order=[]
    for _ in range(m):
        choices=np.where(~done)[0];u=int(choices[np.argmax(levels[choices])])
        done[u]=True;order.append(u)
        for i in np.where(~done)[0]:
            v=min(float(a[i,u]),float(levels[u]))
            if v>levels[i]:levels[i]=v;parent[i]=u
    assert np.all(np.isfinite(levels[np.arange(m)!=elder]))
    return levels,parent,order

def path(parent,u):
    p=[]
    while u>=0:
        assert u not in p
        p.append(int(u));u=int(parent[u])
    return p

def report(x):
    best,w,a=arrows(x);elder=int(np.argmax((x*x).sum(1)))
    level,parent,order=widest(a,elder);juniors=np.where((best<0)&(np.arange(len(x))!=elder))[0]
    records=[]
    for jr in juniors:
        pp=path(parent,jr);records.append(dict(root=int(jr),best=float(best[jr]),target=int(w[jr]),width=float(level[jr]),path=pp,scores=[float(a[i,j]) for i,j in zip(pp[:-1],pp[1:])]))
    edges=[(i,int(parent[i])) for i in range(len(x)) if i!=elder]
    return dict(elder=elder,roots=records,reachable=int(np.sum(level>0)),unreachable=int(np.sum(level<=0)),tree_negative=[(i,j,float(a[i,j])) for i,j in edges if a[i,j]<=0],tree_min=float(min(a[i,j] for i,j in edges)),parents=parent.tolist(),levels=[float(v) if np.isfinite(v) else None for v in level])

if __name__=='__main__':
    import sys,json
    from geometry121 import read_h,geometry
    G=geometry(read_h(sys.argv[1]));r={s:report(G[s]) for s in ['p','q']}
    print(json.dumps(r,indent=2))
```

## finite122.py — complete v4,6140B
SHA433245eb05bb8fdd4f3c18a6ca4269d7635662b13386356e9a58440400d7c0cb. Protects all except TWO current primal worst guards. A future ownU1 continuation must consciously change this quota; this source is not a hidden U1-constrained producer.
```python
"""Finite nonlinear retraction of a whole Q return path (J122, numerical).
Dynamic actual hull/centroid at every evaluation, free H normals. Individual
nonpath polar guards and all but two primal outgoing guards are constrained.
No area weights, fixed reference centre, or hard positive-bar cutoff is used
in optimization. Endpoint claims still require the separate exact auditor.
"""
import sys,json,time,argparse
from pathlib import Path
import numpy as np,torch
from scipy.optimize import minimize
from geometry121 import geometry,tensors,read_h,arrows,describe,normalize
from forest122 import widest,path

class Model:
 def __init__(self,n,tau,retain=.5):
  self.n=n.copy();self.tau=tau;self.scale=np.repeat(np.linalg.norm(n,axis=1),3);self.last=None;self.calls=0
  G=geometry(n);q=n/(1-n@G['g'])[:,None];a,w,A=arrows(q);elder=int(np.argmax((q*q).sum(1)));lev,par,_=widest(A,elder)
  juniors=np.where((a<0)&(np.arange(len(n))!=elder))[0];chosen={};self.paths=[]
  for u in juniors:
   pp=path(par,u);self.paths.append(pp)
   for i,j in zip(pp[:-1],pp[1:]):chosen[i]=j
  self.idx=np.array(sorted(chosen),int);self.dst=np.array([chosen[i] for i in self.idx],int)
  self.base=np.array([A[i,j] for i,j in zip(self.idx,self.dst)])
  self.coeff=np.where(self.base<0,tau-self.base,0);self.target=np.where(self.base<0,self.base,tau)
  self.off=np.array([i for i in range(len(n)) if i!=elder and i not in chosen],int)
  self.elder=elder;self.width=float(np.delete(lev,elder).min());self.pmax=2*len(n)-4
  self.qfloors=np.maximum(tau,np.minimum(.001,retain*a[self.off]))
  self.meta=dict(paths=self.paths,elder=elder,idx=self.idx.tolist(),dst=self.dst.tolist(),base=self.base.tolist(),off=self.off.tolist(),qfloors=self.qfloors.tolist(),width=self.width)
 def calc(self,z):
  if self.last is not None and np.array_equal(z,self.last):return self.val,self.jac
  nn=self.n+(z[:-1]*self.scale).reshape(self.n.shape);G=geometry(nn)
  if not G['simple']:raise ValueError('nonsimple derivative fan')
  pa,pw,_=arrows(G['p']);order=np.argsort(pa)[2:]
  qnow=nn/(1-nn@G['g'])[:,None];qa,qw,_=arrows(qnow)
  missing=self.pmax-2-len(order);assert missing>=0
  def fn(zz):
   n=torch.tensor(self.n)+(zz[:-1]*torch.tensor(self.scale)).reshape(nn.shape);p,_,g,V=tensors(n,G);q=n/(1-n@g)[:,None]
   xp=p[order];dp=p[pw[order]]-xp
   pg=(xp*dp).sum(1)/torch.sqrt((xp*xp).sum(1)*(dp*dp).sum(1))-self.tau
   x=q[self.off];d=q[qw[self.off]]-x
   qg=(x*d).sum(1)/torch.sqrt((x*x).sum(1)*(d*d).sum(1))-torch.tensor(self.qfloors)
   x=q[self.idx];d=q[self.dst]-x
   eg=(x*d).sum(1)/torch.sqrt((x*x).sum(1)*(d*d).sum(1))-torch.tensor(self.target)-torch.tensor(self.coeff)*zz[-1]
   return torch.cat([pg,torch.ones(missing),qg,eg,g,torch.log(V)[None]])
  t=torch.tensor(z);self.val=fn(t).detach().numpy();self.jac=torch.autograd.functional.jacobian(fn,t,vectorize=True).detach().numpy()
  self.last=z.copy();self.calls+=1
  return self.val,self.jac

def run(inp,prefix,outer=5,maxiter=50,trust=.03,tau=1e-7,retain=.5,initial_t=.0,gaincap=.5):
 n=normalize(read_h(inp));initial=n.copy();hist=[];start=time.time();reason='outer_iteration_limit';accepted=0
 for it in range(outer):
  M=Model(n,tau,retain);z=np.zeros(n.size+1);z[-1]=initial_t
  try:
   res=minimize(lambda z:(-z[-1]+1e-5*(z[:-1]@z[:-1]),np.r_[2e-5*z[:-1],-1.]),z,jac=True,method='SLSQP',bounds=[(-trust,trust)]*n.size+[(0,gaincap)],constraints=[dict(type='ineq',fun=lambda z:M.calc(z)[0][:-4],jac=lambda z:M.calc(z)[1][:-4]),dict(type='eq',fun=lambda z:M.calc(z)[0][-4:],jac=lambda z:M.calc(z)[1][-4:])],options=dict(maxiter=maxiter,ftol=1e-12,disp=False))
   v,_=M.calc(res.x);nn=n+(res.x[:-1]*M.scale).reshape(n.shape);D=describe(nn)
   # Admit by actual finite inequalities, independently of optimizer status.
   # A positive guard may use at most 90% of its requested safety margin;
   # every negative path arrow must achieve at least half the proposed gain.
   npg=M.pmax-2;nqg=len(M.off);eg=v[npg+nqg:-4]+M.target+M.coeff*res.x[-1]
   target=np.where(M.base<0,M.base+.5*res.x[-1]*(tau-M.base),tau*.1)
   pg=v[:npg]+tau;qg=v[npg:npg+nqg]+M.qfloors
   good=pg.min()>=tau*.1 and (len(qg)==0 or qg.min()>=tau*.1) and (eg-target).min()>=-1e-12 and res.x[-1]>1e-7 and D['VEF'][1]<=249
   rec=dict(iteration=it,success=bool(res.success),status=int(res.status),message=res.message,nit=int(res.nit),t=float(res.x[-1]),min_constraint=float(v[:-4].min()),gauge=float(abs(v[-4:]).max()),calls=M.calls,policy=M.meta,accepted=bool(good),stats=D,n=nn.tolist(),step=res.x.tolist())
  except Exception as ex:
   rec=dict(iteration=it,error=repr(ex),calls=M.calls,policy=M.meta,accepted=False);good=False
  hist.append(rec)
  print('FINITE122',it,{k:rec.get(k) for k in ['success','t','min_constraint','gauge','calls','accepted','error']},'P/Q',len(rec.get('stats',{}).get('P',[])),len(rec.get('stats',{}).get('Q',[])),flush=True)
  if good:
   n=normalize(nn);accepted+=1
   Path(prefix+'.last.json').write_text(json.dumps(dict(n=n.tolist(),stats=describe(n),accepted=accepted),indent=2)+'\n')
   if len(D['S'])==1:reason='NUMERICAL_Q_CANCELLATION_NEEDS_EXACT';break
  else:reason='no_finite_accepted_retraction';break
  Path(prefix+'.history.json').write_text(json.dumps(hist,indent=2)+'\n')
 out=dict(n=n.tolist(),initial=initial.tolist(),history=hist,stats=describe(n),accepted=accepted,outer=outer,maxiter=maxiter,trust=trust,tau=tau,retain=retain,initial_t=initial_t,gaincap=gaincap,seconds=time.time()-start,reason=reason)
 Path(prefix+'.json').write_text(json.dumps(out,indent=2)+'\n');print('FINITE122_DONE',reason,accepted,out['stats'],flush=True);return out

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('prefix');p.add_argument('--outer',type=int,default=5);p.add_argument('--maxiter',type=int,default=50);p.add_argument('--trust',type=float,default=.03);p.add_argument('--tau',type=float,default=1e-7);p.add_argument('--retain',type=float,default=.5);p.add_argument('--initial-t',type=float,default=0.);p.add_argument('--gaincap',type=float,default=.5)
 a=p.parse_args();run(a.input,a.prefix,a.outer,a.maxiter,a.trust,a.tau,a.retain,a.initial_t,a.gaincap)
```

## recover_versions122.py — complete1737B
SHAc01f5a40ad2f74185aa1c06406804c20a1f04534e8e34cf4849d46918848360b. This exact executable patch-generator restores ALL original finite versions, rather than attributing early runs to later admission rules. It was executed and matched each original byte. Terminal J122_FINITE_PRODUCER_VERSIONS_EXACT_PASS.
```python
"""Restore original complete finite122 source versions from the preserved v4.
Run in the directory containing finite122.py. No numerical run is performed.
"""
from pathlib import Path
import hashlib
v4=Path('finite122.py').read_text()
assert hashlib.sha256(v4.encode()).hexdigest()=='433245eb05bb8fdd4f3c18a6ca4269d7635662b13386356e9a58440400d7c0cb'
v3=v4.replace('initial_t=.0,gaincap=.5):','initial_t=.0):').replace('[(0,gaincap)]','[(0,.5)]').replace('initial_t=initial_t,gaincap=gaincap,seconds','initial_t=initial_t,seconds').replace(";p.add_argument('--gaincap',type=float,default=.5)",'').replace('a.initial_t,a.gaincap)','a.initial_t)')
v2=v3.replace('self.coeff=np.where(self.base<0,tau-self.base,0);self.target=np.where(self.base<0,self.base,tau)','self.coeff=np.maximum(tau-self.base,0);self.target=np.where(self.base<tau,self.base,tau)').replace('target=np.where(M.base<0,','target=np.where(M.base<tau,')
v1=v2.replace('n=normalize(read_h(inp));initial=n.copy();','n=read_h(inp);n=n[geometry(n)[\'active\']];n=normalize(n);initial=n.copy();')
a=v1.index('   # Admit by actual finite inequalities')
b=v1.index('   rec=dict(iteration=it,success=',a)
v1=v1[:a]+"   good=float(v[:-4].min())>=-1e-9 and float(abs(v[-4:]).max())<=1e-8 and res.x[-1]>1e-7 and D['VEF'][1]<=249\n"+v1[b:]
for i,s,h in [(1,v1,'2722c9a2378c8b521b055d003f035662758b8566fb2df5e0880530c731ba5167'),(2,v2,'0fd207b855a2313253ae1e5f6d0e044758047074095470e2d04b73068ec50c66'),(3,v3,'fca0a424cc8ae6d657b1d18c392b0f8481af90837b168e312d3e0ab75fd5d10a')]:
 assert hashlib.sha256(s.encode()).hexdigest()==h,i
 p=Path(f'finite122_v{i}.py')
 if p.exists():assert p.read_bytes()==s.encode()
 p.write_bytes(s.encode())
print('J122_FINITE_PRODUCER_VERSIONS_EXACT_PASS')
```

## Executed finite-Q sequence and actual limits

All commands run with OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1; retain=.5 and initial-t=0 throughout. Original source versions below are distinct and recoverable. Start entries and intermediate exact binary64 normal fields are preserved in part4; numerical optimizer trajectories themselves are not claimed bit-portable. Read_h accepts the JSON n field.

Columns: output prefix, source, consumed input, outer/maxiter/trust/tau/gaincap, observed outcome.
- FINITEQ122: v1,J121_PAIRED_RELAYQ_G8.txt,1/30/.01/1e-7/.5: rejected,t~.09737,minconstraint~-3.36e-7.
- FINITEQ122_160: v1,same input,1/160/.01/1e-7/.5: one admitted iteration-limit endpoint, t~.097370221. Actual84/126/44,S7/U2,P~.2866258584, sixQ(max~.167100455),whole-Q width~-.192468915.
- FINITEQ122_NEXT: v1,_160.last,3/140/.02/1e-7/.5: no admitted step; v1 strips inactive H rows. First failure stops the requested three rounds.
- FINITEQ122_B2: v2,_160.last,3/140/.02/1e-7/.5: no admitted step; positive base slightly below tau was incorrectly assigned the negative-edge progress target.
- FINITEQ122_C: v3,_160.last,3/110/.02/1e-7/.5: TWO admitted steps before external45-second execution cutoff, not three completed. Actual82/123/43,S7/U2,P~.4053887888; sixQ .03691280205,.01008142547,.00945229976,.00923893232,.00911404280,.00906561835. Width~-.130665237.
- FINITEQ122_D: v4,C.last,2/70/.02/1e-7/.12: first candidate rejected; new polar22 guard~-3.179e-8 and S8. Tiny birth is not ignored.
- FINITEQ122_E: v4,C.last,2/80/.02/1e-5/.12: two admitted steps,88/132/46,S7/U2,P~.4570195971,sixQ(max~.010238389),width~-.101184925.
- FINITEQ122_F: v4,E.last,2/90/.04/1e-5/.35: two admitted steps,90/135/47,S7/U2,P~.57403595,sixQ .001827289584,.001824468733,.001672739877,.001453200900,.001240877921,.000988686205,width~-.0427468079.
- FINITEQ122_G: v4,F.last,2/85/.04/1e-5/.5: two admitted steps,90/135/47,S7/U2,P~.6240473604,sixQ(max~.000114045744),width~-.0106792202.
- FINITEQ122_H: v4,G.last,1/130/.04/1e-5/1: one admitted numerical S1/U2 endpoint,Q[],minnonelderpolarangular~9.994422e-6; exact G8 freeze gave the independently integrated actual-centred audit in [internal-source-reference]. This is wholeQ cancellation on ONE body, not a merger of one-sided findings.

Example of the last executed command:
```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python finite122.py FINITEQ122_G.last.json FINITEQ122_H --outer 1 --maxiter 130 --trust .04 --tau 1e-5 --gaincap 1
```

V1 was more stringent about finite solver residual/gauge; v2 changed admission to actual guards and retained inactive input normals; v3 corrected the sign boundary from base<tau to base<0; v4 exposes gaincap. These are actual methodological changes, not proofs of impossibility for rejected candidates. The method's numerical S1 stopping flag by itself is deliberately labelled NEEDS_EXACT. The new exact own121 is complete, but a homogeneous own110 at E249 is still missing.
