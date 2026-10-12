# material-a37a9ae91b2d

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J75 numerical nomination methods and exact recovery manifest

REQUIRED EXACT DEPENDENCY: [internal-source-reference], J75_REFERENCE110_CAP233.py.txt, 11412 bytes, SHA256 e16788d0d477fef56c4a8ac979d2b201c9691d0f6ee302939f7699209a740b82. Save its literal bytes as J75_REFERENCE110_CAP233.py. This is a complete self-contained reconstruction and exact census source; it includes all75 rational input rows and the planar correction. No originating sandbox or older optimizer is required. Parent assignment figure-0566, SHA256 1dd2a815454fdcdf5442f539f13181506b8ecd85c884a433f8061ea92c9f08be, remains the literal scientific parent for successors.

The earlier references mat_ycIJwnsFqIFRydeVC_eTz1uO and [internal-source-reference] could not be retrieved from this run (not found / not owned). Do not use either as a required dependency. The primary dependency above and this complete methods material replace those unavailable references; their historical receipt claims are not accepted evidence.

## Exact findings and evidence boundary
The exact parent R22-B7 is V75/E204/F131,C408, own strict222, weak000. Two exact interior reference points have reference110, weak000, primitivezero000; neither is the uniform body's own centroid. The robust reference point is (463597809/1250000000,-4993524079/10000000000,-6706652071/10000000000). The exact cap defined in the primary source is a homogeneous V14/E25/F13,C50 body of own strict233, weak000, primitivezero000. It is a nonwinner, not a new canonical110.

Let c0 be a body's uniform centroid, and c the centroid of a remaining subset after removing relative volume v. The removed material has centroid r=c+(c0-c)/v in the original body. Every support n.x<=h with n.(c0-c)>0 gives v>=n.(c0-c)/(h-n.c). For the robust reference point, the maximum exact lower bound is 59025415830779399196860455609672891442360768001109/98513453130444726592326870922584689695803548320159, approximately0.5991609669049162. This is necessary for this target and cut-only alteration; it is not a global exclusion of all reference110 centres or addition of material.

The cap dual F(lambda)=integral_K max(0,1+lambda.(x-c)) dx is convex, with gradient M_cap-c*V_cap. An interior c makes F coercive: a ball about c inside K provides a positive directional lower bound growing linearly with |lambda|. Differentiation is valid because the cutting plane has zero3D measure; lambda=0 has positive integrand throughout. At an exact stationary minimizer the cap has centroid c. For every measurable A subset K with centroid c, volume(A)=integral_A(1+lambda.(x-c))<=F(lambda); a stationary cap attains equality. This is a conceptual maximum-volume formulation, not certification of numerical stationarity or of equilibrium class. Compare the earlier finite-one-cut theorem in figure-0552 before claiming novelty. The exact rationalized cap is not asserted to have centroid exactly equal to the nominated reference point.

## Recovery and observed output
Environment actually used: Python3.13.5, NumPy2.3.5, SciPy1.17.0. Save every source with LF endings and final newline. Exact reconstruction and verification command:

OPENBLAS_NUM_THREADS=1 python J75_REFERENCE110_CAP233.py

Observed terminal marker: J75_REFERENCE110_CAP233_EXACT_PASS.
J75_PARENT.json:4392 bytes; SHA256 bd11ca3c0700bccd1a99a4cc2171a725c8a5d8acae5f22992b265f1c2797fb59.
J75_CAP233.json:2213 bytes; SHA256 0fff649b93f148c88f6120a7ae0bb8d2873cd52bdd2c05196ccb785462a59d1d.
J75_EXACT_REPORT.json:4748 bytes; SHA256 63aee978096a8723d10d43a4d884f94b02a5d27e5d7671e2549ddc1dbd3740f5.
The coordinator executed this source and observed these hashes. Qhull is used only to nominate facet planes; all support checks, maximal facet polygons, oriented closed connected hull checks, S/U/H primitive signs and volume moments are rational/integer. Positive tetrahedra at the cap's interior own centroid give a second mass summation. This is the coordinator's own replay, not an independent verifier.

## Complete nomination source units
The three sources below are the methods that materially produced the nominations. They do not prove numerical solver optimality or infeasibility. Save them beside the primary source. Commands:

OPENBLAS_NUM_THREADS=1 python J75_CENTRE_MILP.py --out all_reference_milp.json --seconds 20
OPENBLAS_NUM_THREADS=1 python J75_CHAMBER_LP.py
OPENBLAS_NUM_THREADS=1 python J75_CENTROID_CAP.py

The MILP uses epsilon1e-6 normalized negative-witness margins and minimizes L-infinity centroid distance; --fixed 53 6 restricts roots. The LP expands a selected witness chamber, not the whole reference110 region. It expects its seed's only S/U to be53/6. The cap BFGS numerically minimizes the dual, rationalizes lambda at denominator10^8, and exact-checks the resulting body's OWN census. These scripts are preserved as research methods; they can raise an assertion when a different solver seed fails the assumed chamber. No bitwise solver-output claim is made. The fixed exact witnesses and cap are reconstructed without optimization by the primary source.

Source manifests:
J75_CENTRE_MILP.py:4149 bytes, SHA256 ed370475b5b971ee651910208238cc6d65a34f09a6b59b22ff32c72feae0c867.
J75_CHAMBER_LP.py:1611 bytes, SHA256 74e0bc1955fc0fa9a675e69149f4dee88f3d4a466834b06eb596af5a43e01913.
J75_CENTROID_CAP.py:2436 bytes, SHA256 6c6b6caa7b2f9a910a59ec26d03365854d6a40f1e2f5aa52958f5b5dc643fcf9.

### J75_CENTRE_MILP.py
```python
"""Nominate reference centres with one S and one U; exact-check every candidate.
MILP infeasibility is a numerical conclusion only, not an exact exclusion proof.
All selections include every non-root vertex/facet, not only the old two defects.
"""
import argparse,json,time
from fractions import Fraction as F
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix
import J75_REFERENCE110_CAP233 as g
inputs=g

def problem(K,fixed=None,epsilon=1e-6):
    # Variables c0,c1,c2,margin,distance; then negative-witness and optional root binaries.
    p=np.array(K['points'],dtype=float);lo=p.min(0);hi=p.max(0)
    V,M=g.mass(K);c0=np.array(g.mul(M,1/V),dtype=float)
    lb=list(lo)+[epsilon,0];ub=list(hi)+[epsilon,4.0];ints=[0]*5
    rows=[];lims=[];witness_info=[];allroots=[]
    def row(d,b):rows.append(d);lims.append(b)
    def binary():
        i=len(lb);lb.append(0);ub.append(1);ints.append(1);return i
    for j in range(3):
        row({j:1,4:-1},c0[j]);row({j:-1,4:-1},-c0[j])
    for f in K['faces']:
        a,b,c=[p[i] for i in f[:3]];n=np.cross(b-a,c-a);n/=np.linalg.norm(n)
        row({0:n[0],1:n[1],2:n[2],3:1},n@a)
    # S first; U second. Choosing a strict negative guard rules out weak as well as strict equilibrium.
    groups=g.affine_guards(K)[:2]
    for kind,group in enumerate(groups):
        rr=[]
        for k,gg in enumerate(group):
            if fixed is not None and k==fixed[kind]:
                for ar,br in gg:
                    a=np.array(ar,dtype=float);norm=np.linalg.norm(a);a/=norm;b=float(br)/norm
                    row({0:a[0],1:a[1],2:a[2],3:1},b)
                continue
            ww=[]
            if fixed is None:
                root=binary();rr.append(root);ww.append(root)
            for j,(ar,br) in enumerate(gg):
                a=np.array(ar,dtype=float);norm=np.linalg.norm(a);a/=norm;b=float(br)/norm
                if np.min(b-p@a)>=-1e-13:continue # no strict negative guard at any interior centre
                y=binary();ww.append(y);witness_info.append((kind,k,j,y))
                big=max(0,b-sum(a[t]*(lo[t] if a[t]>0 else hi[t]) for t in range(3))+epsilon)+1e-7
                row({0:-a[0],1:-a[1],2:-a[2],3:1,y:big},big-b)
            row({i:-1 for i in ww},-1)
        if fixed is None:
            row({i:1 for i in rr},1);row({i:-1 for i in rr},-1)
            allroots.append(rr)
    rowi=[];coli=[];val=[]
    for i,d in enumerate(rows):
        for j,x in d.items():rowi.append(i);coli.append(j);val.append(x)
    A=coo_matrix((val,(rowi,coli)),shape=(len(rows),len(lb))).tocsc()
    objective=np.zeros(len(lb));objective[4]=1
    return objective,np.array(ints),Bounds(lb,ub),LinearConstraint(A,-np.inf,lims),allroots

def run(out,fixed,epsilon,seconds):
    K=g.hull(inputs.points());obj,ints,bounds,const,roots=problem(K,fixed,epsilon)
    print('MODEL',len(obj),'variables',sum(ints),'integer',const.A.shape[0],'rows',flush=True)
    start=time.time();r=milp(obj,integrality=ints,bounds=bounds,constraints=const,
       options={'time_limit':seconds,'mip_rel_gap':1e-8,'presolve':True,'disp':False})
    result={'fixed':fixed,'epsilon':epsilon,'status':int(r.status),'message':str(r.message),'seconds':time.time()-start}
    print('MILP',result,flush=True)
    if r.x is not None:
        result['raw_centre']=list(map(float,r.x[:3]));result['distance']=float(r.x[4]);result['solver_objective']=float(r.fun)
        c=tuple(F(round(x*10**10),10**10) for x in r.x[:3]);result['exact_centre']=c
        result['exact_census']=g.census(K,c)
        result['interior']=all(g.dot(g.cross(g.sub(K['points'][f[1]],K['points'][f[0]]),g.sub(K['points'][f[2]],K['points'][f[0]])),g.sub(K['points'][f[0]],c))>0 for f in K['faces'])
        print('CANDIDATE',result,flush=True)
    g.dump(out,result)
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--out',default='centre_milp.json');a.add_argument('--fixed',nargs=2,type=int);a.add_argument('--epsilon',type=float,default=1e-6);a.add_argument('--seconds',type=float,default=20)
    v=a.parse_args();run(v.out,v.fixed,v.epsilon,v.seconds)
```

### J75_CHAMBER_LP.py
```python
"""A convex reference110 witness chamber through an exact seed centre.
Linear programming only nominates a centre. Rational exact signs certify the result.
"""
from fractions import Fraction as F
import json,numpy as np
from scipy.optimize import linprog
import J75_REFERENCE110_CAP233 as g
inputs=g
K=g.hull(inputs.points());seed=tuple(F(x) for x in json.load(open('all_reference_milp.json'))['exact_centre']);GG=g.affine_guards(K)
rows=[];rhs=[];selected=[]
for kind,grp in enumerate(GG[:2]):
 for k,gg in enumerate(grp):
  if k==[53,6][kind]: chosen=[(j,1) for j in range(len(gg))]
  else:
   j=min(range(len(gg)),key=lambda j:float(gg[j][1]-g.dot(gg[j][0],seed))/np.linalg.norm(np.array(gg[j][0],dtype=float)))
   assert gg[j][1]-g.dot(gg[j][0],seed)<0
   chosen=[(j,-1)];selected.append([kind,k,j])
  for j,sign in chosen:
   a,b=gg[j];a=np.array(a,dtype=float)*sign;b=float(b)*sign;n=np.linalg.norm(a)
   rows.append([*list(a/n),1]);rhs.append(b/n)
for f in K['faces']:
 a,b,c=[np.array(K['points'][i],dtype=float) for i in f[:3]];n=np.cross(b-a,c-a);n/=np.linalg.norm(n)
 rows.append([*n,1]);rhs.append(n@a)
r=linprog([0,0,0,-1],A_ub=rows,b_ub=rhs,bounds=[(None,None)]*3+[(0,None)],method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
print(r.message,r.fun,r.x)
result={'solver_message':str(r.message),'selected':selected}
if r.x is not None:
 c=tuple(F(round(x*10**10),10**10) for x in r.x[:3]);result.update(centre=c,margin=float(r.x[3]),census=g.census(K,c))
 print(result['centre'],result['margin'],result['census'])
g.dump('reference_chamber.json',result)
```

### J75_CENTROID_CAP.py
```python
"""Maximum-volume halfspace slice with nominated centroid; exact rational-plane census.
The numerical minimization nominates planes, not proofs of optimality.
"""
from fractions import Fraction as F
import json,sys
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
import J75_REFERENCE110_CAP233 as g
inputs=g
K=g.hull(inputs.points());P=np.array(K['points'],dtype=float);E=np.array(K['edges'],dtype=int)
V0,M0=g.mass(K);C0=np.array(g.mul(M0,1/V0),dtype=float)
def clip_float(lam,c):
 s=1+(P-c)@lam
 inside=P[s>=0];ei=E[(s[E[:,0]]*s[E[:,1]])<0]
 q=P[ei[:,0]]+(P[ei[:,1]]-P[ei[:,0]])*(-s[ei[:,0]]/(s[ei[:,1]]-s[ei[:,0]]))[:,None]
 return np.concatenate([inside,q])
def float_mass(p):
 hull=ConvexHull(p);o=p[hull.vertices].mean(axis=0);t=p[hull.simplices]
 vols=np.abs(np.einsum('ij,ij->i',t[:,0]-o,np.cross(t[:,1]-o,t[:,2]-o)))/6
 return vols.sum(),np.sum(vols[:,None]*(t.sum(axis=1)+o)/4,axis=0)
def val_grad(lam,c):
 p=clip_float(lam,c);v,m=float_mass(p);r=m-c*v
 return v+lam@r,r

def solve(c,initial=None):
 c=np.array(c,dtype=float)
 r=minimize(val_grad,np.zeros(3) if initial is None else initial,args=(c,),jac=True,method='BFGS',options={'gtol':1e-12,'maxiter':500})
 p=clip_float(r.x,c);v,m=float_mass(p)
 return r,{'lambda_float':r.x.tolist(),'target_float':c.tolist(),'numerical_centroid':(m/v).tolist(),'numerical_mass_residual':np.linalg.norm(m/v-c).item(),'volume_fraction_float':float(v/float(V0)),'success':bool(r.success),'message':str(r.message)}

def exact_clip(lam,c):
 # This plane is exact even when it does not place its own centroid exactly at c.
 s=[1+g.dot(g.sub(p,c),lam) for p in K['points']]
 p=[q for q,ss in zip(K['points'],s) if ss>=0]
 for i,j in K['edges']:
  if s[i]*s[j]<0:p.append(g.add(K['points'][i],g.mul(g.sub(K['points'][j],K['points'][i]),-s[i]/(s[j]-s[i]))))
 return g.hull(p)

if __name__=='__main__':
 c=tuple(F(x) for x in json.load(open('reference_chamber.json'))['centre'])
 r,out=solve(c);print(json.dumps(out,indent=2))
 lam=tuple(F(round(x*10**8),10**8) for x in r.x);body=exact_clip(lam,c);v,m=g.mass(body);cc=g.mul(m,1/v)
 out.update(lambda_exact=lam,plane_target_exact=c,body_size=[len(body['points']),len(body['edges']),len(body['faces'])],own_census=g.census(body,cc),own_centroid_float=list(map(float,cc)))
 print(out['body_size'],out['own_census']);g.dump('centroid_cap_report.json',out);g.dump('centroid_cap_body.json',body['points'])
```
