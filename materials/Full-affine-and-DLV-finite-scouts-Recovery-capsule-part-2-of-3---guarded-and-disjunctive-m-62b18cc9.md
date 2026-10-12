# material-62b18cc9d724

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Recovery capsule part 2/3 — FULL_AFFINE_DLV_FINITE_SCOUTS

Requires part1 [internal-source-reference] for literal c2_inputs.py and complete scout_affine.py. Part3 supplies DLV code, exact observed finite ledger and reconstruction receipts. These are NUMERICAL finite searches, not exact mechanics certificates or an affine exclusion. No new110 body was found. Root/edge choices are fixed only in the first method; the second permits maximizing-edge and root changes; the MILP pilot samples root-dependent disjunctive cells with floating PSD separation.

Save each complete block UTF-8/LF with final newline. Observed actual local files, not transient context synopsis hashes: guard_affine.py2566bytes SHA316d56cf7decf5442853a37fd449d9da0d8bec668ba748e63f285d0813b14880; mobile_guard_affine.py2151bytes SHAcfc8b0ab8af74ca09f2116034637f7f10bee47c5118a523a3bccd8605ea7742c; disjunctive_affine.py5455bytes SHAf76736bbb4b9773622a7664824c7d784be4144553177e76e52a0ae8301a92e62. The named v1 local duplicate was identical to this final disjunctive file and is not an extra method.

Environment CPython3.13.5,NumPy2.3.5,SciPy1.17.0,binary64, OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1. Run python -B guard_affine.py; python -B mobile_guard_affine.py. Observed terminal markers FULL_SPD_FIXED_U1_GUARD_SCOUT_FINISHED 32 and FULL_SPD_MOBILE_U1_GUARD_SCOUT_FINISHED 64. Source-enforced SLSQP feasibility is checked separately from census; reject numerical rows with feasible_slack<-1e-9. Floating feasibility at this tolerance is not exact acceptance.

The full disjunctive main is reusable, but its executed pilot was stopped after FOUR published rows, not a completed main campaign. All four had HiGHS time-limit/no-primal returns: S3_G6 root68 trial0 after11cuts, root68 trial1 after16cuts, root26 trial0 after13cuts, root63 trial0 after3cuts. No SPD metric or exact infeasibility certificate was obtained. No FULL_SPD_DISJUNCTIVE_U1_SCOUT_FINISHED marker was observed. The literal4-row ledger is in part3. Running the unmodified full main now is a NEW campaign, not an exact replay of a user-interrupted wall-clock pilot.

## guard_affine.py
```python
"""Finite full-SPD U1-cell continuation on literal C2 parents; numerical, not exclusion."""
import numpy as np, json, sys
from scipy.optimize import minimize, LinearConstraint
from scout_affine import Body
from c2_inputs import points
BAS=np.array([[[1.,0,0],[0,0,0],[0,0,0]],[[0.,0,0],[0,1,0],[0,0,0]],[[0.,0,0],[0,0,0],[0,0,1]],[[0.,1,0],[1,0,0],[0,0,0]],[[0.,0,1],[0,0,0],[1,0,0]],[[0.,0,0],[0,0,1],[0,1,0]]])
def mat(v):return np.einsum('i,ijk->jk',v,BAS)
def vals(M):return np.array([M[0,0],M[1,1],M[2,2],M[0,1],M[0,2],M[1,2]])
def main():
 rng=np.random.default_rng(2026092302); out=[]
 for name in ['S3_G6','CHAIN_G5','PAIRDELETE_G6','MASS_G8']:
  body=Body(points(name)); x=body.x; pairs=body.pairs
  raw=np.einsum('ij,ij->i',body.fx,body.dx); chosen=[];root=int(np.argmax(x[:,1]))
  for i in range(len(x)):
   if i==root:continue
   ix=np.flatnonzero(pairs[:,0]==i);chosen.append(ix[np.argmax(raw[ix])])
  a=np.einsum('ij,ljk,ik->il',body.fx[chosen],BAS,body.dx[chosen])
  # Positive escape along one original true edge for every nonroot, hence U1; root all negative.
  rix=np.flatnonzero(pairs[:,0]==root)
  a=np.r_[a,-np.einsum('ij,ljk,ik->il',body.fx[rix],BAS,body.dx[rix])]
  a/=np.linalg.norm(a,axis=1)[:,None]
  cons=[LinearConstraint(a,1e-8,np.inf),LinearConstraint([[1,1,1,0,0,0]],3,3),{'type':'ineq','fun':lambda v:np.linalg.eigvalsh(mat(v))-.02}]
  def loss(v):
   try:u,s=body.escapes(mat(v))
   except np.linalg.LinAlgError:return 1e10
   if not np.all(np.isfinite(s)):return 1e10
   d=np.minimum(np.sort(s)[1:]-1e-5,0)
   return d@d
  v=np.array([1.,1,1,0,0,0]);best=(loss(v),v.copy())
  print('START',name,body.census(mat(v)),flush=True)
  for k in range(8):
   if k==0: start=v
   else:
    # Generate a feasible point of this fixed U1 cell by a random linear objective.
    obj=rng.normal(size=6)
    seed=minimize(lambda t:obj@t,best[1],method='SLSQP',constraints=cons,options={'maxiter':400,'ftol':1e-10})
    start=seed.x
   z=minimize(loss,start,method='SLSQP',constraints=cons,options={'maxiter':1200,'ftol':1e-13})
   m=mat(z.x);c=body.census(m);feas=float(min((a@z.x).min()-1e-8,np.linalg.eigvalsh(m).min()-.02))
   row={'name':name,'trial':k,'loss':float(z.fun),'feasible_slack':feas,'M':m.tolist(),'census':c,'message':z.message}
   out.append(row)
   print('GUARD',name,k,row,flush=True)
   if feas>-1e-9 and z.fun<best[0]:best=(z.fun,z.x.copy())
   with open('guard_affine.json','w') as f:json.dump(out,f,sort_keys=True,indent=2)
 print('FULL_SPD_FIXED_U1_GUARD_SCOUT_FINISHED',len(out),flush=True)
if __name__=='__main__':main()
```

## mobile_guard_affine.py
```python
"""Finite numerical full-SPD U1 continuation with free roots and edge choices.
Unlike guard_affine.py, the maximizing escape edge is recomputed at every step.
Dropping the smallest vertex maximum permits root turnover; no individual tree is pinned.
Not an exact affine exclusion. All candidates are rechecked numerically.
"""
import json, numpy as np
from scipy.optimize import minimize, LinearConstraint
from scipy.stats import qmc
from scout_affine import Body
from c2_inputs import points
from guard_affine import BAS, mat, vals
FLOOR=.005
EPS=1e-8

def main():
 rng=np.random.default_rng(2026092304);out=[]
 for name in ['S3_G6','CHAIN_G5','PAIRDELETE_G6','MASS_G8']:
  b=Body(points(name));a=np.einsum('ij,ljk,ik->il',b.fx,BAS,b.dx)
  a/=np.linalg.norm(a,axis=1)[:,None]
  def escapes(v):
   r=np.full(len(b.x),-np.inf);np.maximum.at(r,b.pairs[:,0],a@v)
   return np.sort(r)[1:]-EPS
  cons=[LinearConstraint([[1,1,1,0,0,0]],3,3),{'type':'ineq','fun':escapes},
        {'type':'ineq','fun':lambda v:np.linalg.eigvalsh(mat(v))-FLOOR}]
  def loss(v):
   M=mat(v)
   if np.linalg.eigvalsh(M)[0]<=0:return 1000.
   _,s=b.escapes(M);d=np.minimum(np.sort(s)[1:]-1e-5,0)
   return float(d@d)
  one=np.array([1.,1,1,0,0,0]);best=one.copy();bestloss=loss(one)
  for trial in range(16):
   if trial==0:start=one.copy()
   else:
    c=rng.normal(size=6)
    seed=minimize(lambda v:c@v,best if trial%2 else one,method='SLSQP',constraints=cons,
                  options={'maxiter':600,'ftol':1e-11})
    start=seed.x
   f=minimize(loss,start,method='SLSQP',constraints=cons,options={'maxiter':1500,'ftol':1e-13})
   M=mat(f.x);margin=float(min(escapes(f.x).min(),np.linalg.eigvalsh(M).min()-FLOOR))
   row={'name':name,'trial':trial,'M':M.tolist(),'loss':float(f.fun),'feasible_slack':margin,
        'census':b.census(M),'message':f.message}
   out.append(row);print('MOBILE',name,trial,row,flush=True)
   if margin>=-1e-9 and f.fun<bestloss:best=f.x;bestloss=f.fun
   with open('mobile_guard_affine.json','w') as g:json.dump(out,g,sort_keys=True,indent=2)
 print('FULL_SPD_MOBILE_U1_GUARD_SCOUT_FINISHED',len(out),flush=True)
if __name__=='__main__':main()
```

## disjunctive_affine.py
```python
"""Numerical full-SPD disjunctive U1 cells; no mathematical exclusion claim.
True incidence and volume centroid come from the fixed-input numerical Body scout.
Every nonroot gets a freely chosen actual edge escape. A free root is allowed.
A root is necessarily the unique global norm maximum; redundant norm constraints
strengthen the MILP. SPD is handled by eigenvector separation and checked afterward.
"""
import json, sys, numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint, minimize
from scipy.sparse import lil_matrix, vstack, csr_array
from scout_affine import Body
from c2_inputs import points
from guard_affine import BAS, mat, vals

EPS=1e-7
FLOOR=.02

def root_candidate(body, root, objective, maxcuts=35):
    """MILP with one fixed candidate root, but all nonroot edge choices free."""
    x=body.x
    take=np.flatnonzero(body.pairs[:,0]!=root)
    p=body.pairs[take]
    a=np.einsum('ij,ljk,ik->il',body.fx[take],BAS,body.dx[take])
    a/=np.linalg.norm(a,axis=1)[:,None]
    lo=np.array([FLOOR]*3+[-1.5]*3)
    hi=np.array([3-2*FLOOR]*3+[1.5]*3)
    rowmin=np.minimum(a*lo,a*hi).sum(axis=1)
    big=EPS-rowmin
    n=6+len(a)
    rows=lil_matrix((len(a)+len(x)+1,n));lb=[];ub=[]
    rows[:len(a),:6]=a
    for j,b in enumerate(big):rows[j,6+j]=-b
    lb.extend((EPS-big).tolist());ub.extend([np.inf]*len(a))
    k=len(a)
    for i in range(len(x)):
        if i==root:continue
        rows[k,6+np.flatnonzero(p[:,0]==i)]=1
        lb.append(1);ub.append(np.inf);k+=1
    rows[k,:3]=1;lb.append(3);ub.append(3);k+=1
    rows=rows[:k].tocsr()
    norms=np.einsum('ij,ljk,ik->il',x,BAS,x)
    nr=np.delete(norms[root]-norms,root,axis=0)
    nr/=np.linalg.norm(nr,axis=1)[:,None]
    tail=np.zeros((len(nr),n));tail[:,:6]=nr
    rows=vstack([rows,csr_array(tail)],format='csr');lb.extend([0.]*len(nr));ub.extend([np.inf]*len(nr))
    dirs=[]
    for a0 in [-1,0,1]:
      for a1 in [-1,0,1]:
       for a2 in [-1,0,1]:
        w=np.array([a0,a1,a2],float)
        if np.any(w) and next(t for t in w if t)!=-1:dirs.append(w/np.linalg.norm(w))
    def addcuts(ws):
        nonlocal rows
        zz=np.zeros((len(ws),n));zz[:,:6]=np.einsum('wi,kij,wj->wk',np.array(ws),BAS,np.array(ws))
        rows=vstack([rows,csr_array(zz)],format='csr');lb.extend([FLOOR]*len(ws));ub.extend([np.inf]*len(ws))
    addcuts(dirs)
    c=np.r_[objective,np.zeros(n-6)]
    bounds=Bounds(np.r_[lo,np.zeros(n-6)],np.r_[hi,np.ones(n-6)])
    for it in range(maxcuts):
        fit=milp(c,integrality=np.r_[np.zeros(6),np.ones(n-6)],bounds=bounds,
                 constraints=LinearConstraint(rows,np.array(lb),np.array(ub)),
                 options={'time_limit':8,'mip_rel_gap':1e-7,'node_limit':100000})
        if fit.x is None:return {'root':root,'status':int(fit.status),'message':fit.message,'cuts':it}
        m=mat(fit.x[:6]);ev,vec=np.linalg.eigh(m)
        if ev[0]>=FLOOR-1e-8:
            census=body.census(m)
            chosen=np.flatnonzero(fit.x[6:]>.5)
            margin=float(np.min(a[chosen]@fit.x[:6]))
            return {'root':root,'status':int(fit.status),'cuts':it,'M':m.tolist(),
                    'census':census,'selected_margin':margin,'eigenvalues':ev.tolist(),
                    'chosen_pairs':p[chosen].tolist()}
        addcuts([vec[:,j] for j in range(3) if ev[j]<FLOOR-1e-8])
    return {'root':root,'status':-1,'message':'PSD separation limit; not a mathematical exclusion','cuts':maxcuts}

def improve(body, row):
    """A local descent in the newly discovered U1 guard cell; other cells remain open."""
    m=np.array(row['M']);v=vals(m);p=np.array(row['chosen_pairs']);x=body.x
    a=np.einsum('ij,ljk,ik->il',x[p[:,0]],BAS,x[p[:,1]]-x[p[:,0]])
    a/=np.linalg.norm(a,axis=1)[:,None]
    cons=[LinearConstraint(a,EPS*.5,np.inf),LinearConstraint([[1,1,1,0,0,0]],3,3),
          {'type':'ineq','fun':lambda t:np.linalg.eigvalsh(mat(t))-FLOOR}]
    def loss(t):
        M=mat(t)
        if np.linalg.eigvalsh(M)[0]<=0:return 1e4
        _,s=body.escapes(M);d=np.minimum(np.sort(s)[1:]-1e-5,0);return float(d@d)
    f=minimize(loss,v,method='SLSQP',constraints=cons,options={'maxiter':1200,'ftol':1e-13})
    M=mat(f.x);slack=float(min((a@f.x).min()-EPS*.5,np.linalg.eigvalsh(M).min()-FLOOR))
    return {'loss':float(f.fun),'M':M.tolist(),'census':body.census(M),'feasible_slack':slack,'message':f.message}

def main():
    rng=np.random.default_rng(2026092303);out=[]
    for name in ['S3_G6','CHAIN_G5','PAIRDELETE_G6','MASS_G8']:
        body=Body(points(name));top=int(np.argmax(body.x[:,1]))
        roots=[top]
        for i in range(200):
            a=rng.normal(size=(3,3));M=a@a.T+.05*np.eye(3)
            r=int(np.argmax(np.einsum('ij,jk,ik->i',body.x,M,body.x)))
            if r not in roots:roots.append(r)
            if len(roots)==8:break
        for root in roots:
            for trial in range(2 if root==top else 1):
                row=root_candidate(body,root,rng.normal(size=6));row.update(name=name,trial=trial)
                if 'M' in row:row['descent']=improve(body,row)
                out.append(row)
                print('DISJ',name,root,trial,{k:v for k,v in row.items() if k not in ('M','chosen_pairs','descent')},row.get('descent',{}).get('census'),flush=True)
                with open('disjunctive_affine.json','w') as f:json.dump(out,f,sort_keys=True,indent=2)
    print('FULL_SPD_DISJUNCTIVE_U1_SCOUT_FINISHED',len(out),flush=True)
if __name__=='__main__':main()
```
