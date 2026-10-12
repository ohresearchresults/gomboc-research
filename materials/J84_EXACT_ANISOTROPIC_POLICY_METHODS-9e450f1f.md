# material-9e450f1f5e4d

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J84 exact anisotropic S1 policy and whole-cell U trap — complete methods

Dependency: exact84.py and complete J82_S1_ROBUST_G6_INPUT.json from [internal-source-reference] (the self-contained main J84 exact capsule). These two new complete source units need that material, not a missing workspace. They concern the unchanged literal J82_G6 geometry, not RA40_LATTICE220, B7, or an arbitrary physical deformation.

## Findings and proof scope
centre84.py constructs171 exact halfspaces:86 interior support conditions and85 outgoing polar witnesses, exempting stable root16. For each other facet it selects the own-centre witness maximizing its exact infinity-cube bound. This defines one convex sufficient S1 policy region, not the full union of possible S1 regions. Seven LP-nominated extreme directions are frozen by exact3x3 Gaussian solves and moved99/100 toward the nominated closed vertex from the exact own centroid. All171 open halfspaces are then checked rationally. All seven reference centres retain S1, with U3/U7/U9 and corresponding H2/H6/H8, additionalweak000; largest certified tested infinity displacement .005551191744394392. These are reference centres, not new homogeneous bodies.

The mixed-integer stage was a finite nomination attempt and reported infeasible; this was NOT treated as a mathematical exclusion. The complete-cell conclusion instead comes from trap84.py's exact nonnegative LP-dual combinations. For every directed radial edge, it finds up to3 nonnegative rational multipliers of the exact policy halfspaces and checks the exact coefficient identity. Hence each stored upper bound is valid independently of numerical LP optimality. Edges with nonnegative upper bound are merely potential edges. A31-vertex block lacks any potential path to vertex0; all actual outward cut scores and all vertex0 outgoing scores are strictly negative over the entire CLOSED policy polytope. A maximum-radius vertex of that block supplies a second strict U. Thus U>=2 throughout this whole policy polytope. This does not exclude other S1 policies, large centre excursions, or finite boundary motion.

The stronger practical fixed-surface cube exclusion of radius.3883 is separately in [internal-source-reference]; do not conflate its17-block/27-edge cut with this31-block policy cut. Both are exact coordinator computations. Neither is a general obstruction to the desired figure, and canonical C622 remains unchanged.

## Reconstruction and manifests
Save source with LF/final LF alongside the dependency files. CPython3.13.5,NumPy2.3.5,SciPy1.17.0. Commands:
OPENBLAS_NUM_THREADS=1 python centre84.py
OPENBLAS_NUM_THREADS=1 python trap84.py
Observed markers:
J84_EXACT_S1_DIRECTIONAL_REGION_PASS
J84_ENTIRE_FIXED_POLICY_CENTRE_CELL_U_GE_2_EXACT_PASS

centre84.py5197B/SHA c9a71175cb27f6ef8d1db52d3c81f1c12cb30376d6a022134db0653f6c55aebb
trap84.py3099B/SHA d084f7e6056bb8f10046a8c7594b5478fe03af99900ec4795c914893487ab6b6
Observed output J84_CENTRE_REGION.json78663B/SHA b395c637bbea7dbeee362c888e00528da9b42a3e833ff542c7b2d989d45f1a21
Observed output J84_CELL_TRAP.json77869B/SHA 0ee1e94ea68a0d6ba7d22ea69836d14a46acf4346b6dc5028a0c9714e6d3afb1
Exact halfspaces/certificates and classifications are authoritative. Another LP tie choice or MILP status message in another environment may give different valid output bytes; that is not silently promoted to the same report identity. Every claimed bound must still pass its rational coefficient checks.

## centre84.py
```python
"""Exact anisotropic S1 policy region; LP/MILP only nominate rational points."""
import json,itertools,time
from fractions import Fraction as R
import numpy as np
from scipy.optimize import linprog,milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix
from exact84 import load,topology,mass,audit,dot,sub,cross,scale,ROOT
P,F=load();edges,planes=topology(P,F);vol,g=mass(P,F)
# Exact facet guard A+B.c>0. Policies maximize exact centred infinity-cube bounds.
constraints=[];policy=[]
for n,h in planes:constraints.append((h,scale(n,-1),'interior'))
for i,(n,h) in enumerate(planes):
    if i==16:continue
    best=None
    for j,(m,k) in enumerate(planes):
        if j==i:continue
        nm,nn=dot(n,m),dot(n,n)
        A=nm*h-nn*k;B=sub(scale(m,nn),scale(n,nm));N=A+dot(B,g)
        if N<=0:continue
        norm=sum(abs(x) for x in B)
        ratio=N/norm
        if best is None or ratio>best[0]:best=(ratio,j,A,B)
    assert best is not None
    ratio,j,A,B=best;policy.append([i,j,str(ratio)]);constraints.append((A,B,[i,j]))
assert len(constraints)==171
# Normalization does not change exact halfspaces.
CN=np.array([[float(x) for x in B] for A,B,k in constraints]);AN=np.array([float(A) for A,B,k in constraints]);norm=np.linalg.norm(CN,axis=1)
CN/=norm[:,None];AN/=norm
GN=np.array(list(map(float,g)))

def solve3(rows):
    M=[[R(x) for x in constraints[i][1]]+[-constraints[i][0]] for i in rows]
    for k in range(3):
        q=next((j for j in range(k,3) if M[j][k]),None)
        if q is None:return None
        M[k],M[q]=M[q],M[k];t=M[k][k];M[k]=[x/t for x in M[k]]
        for j in range(3):
            if j!=k:
                t=M[j][k];M[j]=[x-t*y for x,y in zip(M[j],M[k])]
    return tuple(row[-1] for row in M)

results=[]
directions=list(np.eye(3))+list(-np.eye(3))+[np.array([float(x) for x in sub(P[40],P[0])])]
for direction in directions:
    rr=linprog(-direction,A_ub=-CN,b_ub=AN,bounds=[(None,None)]*3,method='highs')
    assert rr.success
    order=np.argsort(abs(AN+CN@rr.x))[:10]
    candidate=None;active=None
    for inds in itertools.combinations(order,3):
        c=solve3(inds)
        if c is not None and all(A+dot(B,c)>=0 for A,B,k in constraints):candidate=c;active=list(map(int,inds));break
    assert candidate is not None
    # 99/100 toward a feasible closed vertex is strictly in all original open guards.
    c=tuple((x+99*y)/100 for x,y in zip(g,candidate))
    assert all(A+dot(B,c)>0 for A,B,k in constraints)
    rep=audit(P,F,c)
    results.append({'direction':direction.tolist(),'active':active,'vertex':[str(x) for x in candidate],'reference':[str(x) for x in c],
                    'displacement':[float(x-y) for x,y in zip(c,g)],'linf':max(abs(float(x-y)) for x,y in zip(c,g)),
                    'strict':rep['strict'],'weak':rep['weak'],'S':rep['S'],'U':rep['U'],'P':rep['P'],'Q':rep['Q']})
print('EXACT_DIRECTIONAL',[(r['linf'],r['strict'],r['weak']) for r in results],flush=True)
# Local primal edge disjunction; all nonroot points need a strictly positive outgoing edge.
dir_edges=[(i,j) for a,b in edges for i,j in [(a,b),(b,a)] if i!=0]
k=len(dir_edges);nv=4+k;rows=[];lo=[];hi=[]
for A,B in zip(AN,CN):
    row=np.zeros(nv);row[:3]=B;rows.append(row);lo.append(1e-8-A);hi.append(np.inf)
PN=np.array([[float(x) for x in p] for p in P]);tau=1e-7
for e,(i,j) in enumerate(dir_edges):
    u=PN[j]-PN[i];u/=np.linalg.norm(u);const=u@PN[i]
    M=max(0,tau-(const-np.max(PN@u)))
    row=np.zeros(nv);row[:3]=-u;row[4+e]=-M
    rows.append(row);lo.append(tau-M-const);hi.append(np.inf)
for i in range(1,len(P)):
    row=np.zeros(nv)
    for e,(a,b) in enumerate(dir_edges):
        if a==i:row[4+e]=1
    rows.append(row);lo.append(1);hi.append(np.inf)
for i in range(3):
    row=np.zeros(nv);row[i]=1;row[3]=-1;rows.append(row);lo.append(-np.inf);hi.append(GN[i])
    row=np.zeros(nv);row[i]=-1;row[3]=-1;rows.append(row);lo.append(-np.inf);hi.append(-GN[i])
obj=np.zeros(nv);obj[3]=1
res=milp(obj,integrality=np.r_[np.zeros(4),np.ones(k)],bounds=Bounds(np.r_[PN.min(axis=0),0,np.zeros(k)],np.r_[PN.max(axis=0),10,np.ones(k)]),
         constraints=LinearConstraint(np.array(rows),lo,hi),options={'time_limit':30.,'mip_rel_gap':1e-9})
ms={'status':int(res.status),'message':res.message,'finite_nomination_only':True}
if res.x is not None:
    ms['candidate']=res.x[:3].tolist();ms['linf_objective']=float(res.fun)
    c=tuple(R(round(float(x)*10**10),10**10) for x in res.x[:3]);report=audit(P,F,c)
    ms['rational']=[str(x) for x in c];ms['strict']=report['strict'];ms['weak']=report['weak'];ms['S']=report['S'];ms['U']=report['U']
    (ROOT/'J84_REFERENCE_MILP_EXACT.json').write_text(json.dumps(report,sort_keys=True,separators=(',',':'))+'\n')
print('MILP',ms,flush=True)
output={'own_centroid':[str(x) for x in g],'policy':policy,'constraints':[[str(A),[str(x) for x in B],k] for A,B,k in constraints],
        'directional':results,'milp':ms,'scope':'Fixed original surface and one S1 witness policy; no material modification or global optimality proof.'}
(ROOT/'J84_CENTRE_REGION.json').write_text(json.dumps(output,sort_keys=True,separators=(',',':'))+'\n')
print('J84_EXACT_S1_DIRECTIONAL_REGION_PASS',flush=True)
```

## trap84.py
```python
"""Exact dual bounds and an entire fixed-S1-policy-centre-cell U trap."""
import json,itertools
import numpy as np
from scipy.optimize import linprog
from fractions import Fraction as R
from exact84 import load,topology,dot,sub,scale,ROOT
P,F=load();edges,_=topology(P,F)
data=json.loads((ROOT/'J84_CENTRE_REGION.json').read_text())
constraints=[(R(A),tuple(map(R,B)),k) for A,B,k in data['constraints']]
CN=np.array([[float(x) for x in B] for A,B,k in constraints]);AN=np.array([float(A) for A,B,k in constraints]);nn=np.linalg.norm(CN,axis=1);CN/=nn[:,None];AN/=nn

def gaussian(M,v):
    M=[[R(x) for x in row]+[R(v[i])] for i,row in enumerate(M)]
    for k in range(3):
        p=next((i for i in range(k,3) if M[i][k]),None)
        if p is None:return None
        M[k],M[p]=M[p],M[k];q=M[k][k];M[k]=[x/q for x in M[k]]
        for i in range(3):
            if i!=k:
                q=M[i][k];M[i]=[x-q*y for x,y in zip(M[i],M[k])]
    return tuple(row[-1] for row in M)

def upper(a,b):
    rr=linprog(-np.array(list(map(float,b))),A_ub=-CN,b_ub=AN,bounds=[(None,None)]*3,method='highs');assert rr.success
    active=np.argsort(abs(AN+CN@rr.x))[:12]
    for inds in itertools.combinations(map(int,active),3):
        M=[[constraints[i][1][k] for i in inds] for k in range(3)]
        lam=gaussian(M,scale(b,-1))
        if lam is None or min(lam)<0:continue
        assert all(sum(lam[j]*constraints[i][1][k] for j,i in enumerate(inds))==-b[k] for k in range(3))
        u=a+sum(lam[j]*constraints[i][0] for j,i in enumerate(inds))
        # Every recorded inequality is proved even without numerical LP optimality.
        return u,{'rows':list(inds),'multipliers':[str(x) for x in lam],'upper':str(u)}
    raise RuntimeError('No sparse exact dual recovered')

bounds={};proofs={};potential=[[] for p in P]
for a,b in edges:
    for i,j in [(a,b),(b,a)]:
        d=sub(P[j],P[i]);u,pr=upper(dot(P[i],d),scale(d,-1))
        bounds[i,j]=u;proofs[i,j]=pr
        if u>=0:potential[i].append(j)
reach={0}
while True:
    nxt=reach|{i for i in range(len(P)) if any(j in reach for j in potential[i])}
    if nxt==reach:break
    reach=nxt
B=sorted(set(range(len(P)))-reach)
cut=[(i,j) for i,j in bounds if i in B and j not in B]
root0=[(i,j) for i,j in bounds if i==0]
print('B',B,'CUT',cut,'ROOT0_STRICT',all(bounds[e]<0 for e in root0),flush=True)
assert B and all(bounds[e]<0 for e in cut+root0)
out={'B':B,'cut':[list(e) for e in cut],'root0_edges':[list(e) for e in root0],
     'proofs':{f'{i},{j}':proofs[i,j] for i,j in cut+root0},
     'all_directed_upper_bounds':{f'{i},{j}':str(u) for (i,j),u in bounds.items()},
     'scope':'The entire closed exact policy polytope specified by J84_CENTRE_REGION.json. Not the union of all S1 policies; not a physical deformation theorem.',
     'conclusion':'Every centre in this polytope has at least two strict U: vertex 0 and a maximum-radius vertex in nonempty proper B.'}
(ROOT/'J84_CELL_TRAP.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
print('J84_ENTIRE_FIXED_POLICY_CENTRE_CELL_U_GE_2_EXACT_PASS',flush=True)
```
