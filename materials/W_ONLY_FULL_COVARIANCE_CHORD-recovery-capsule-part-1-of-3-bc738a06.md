# material-bc738a0657e8

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# W_ONLY_RESIDUAL_FULL_COVARIANCE_CHORD_ATLAS_V1
## Recovery capsule part 1/3: exact polynomial kernel and complete numerical locator

All three parts and the already preserved exact geometry unit [internal-source-reference] are required for complete recovery. Save that unit as lift_core.py,5750B,SHA256 a28576fb18443f2d0a10e06a2a82fa9e08132e29a7aefb4713f20da9d7577195. The two code blocks below are entire runnable source files, not excerpts. Restore their code contents with UTF-8 and one final LF, excluding fences. No external exact geometry, old atlas checkpoint or old numeric witness is an input. The final verifier uses only SymPy and the exact kernel/core; the locator is not an acceptance oracle.

### atlas_common.py
4146 bytes, SHA256 0b16f4295901bad2e9e6c37071cee1db7bcc1af959226a6b30cd014fa30035a1.
```python
"""Exact polynomial data for the fixed actual W-only covariance/chord atlas."""
from functools import lru_cache
from math import comb
import sympy as S
import lift_core as L

R = S.Rational
X, Y = S.symbols('x y')
ELL = R(540000000000000,25985706405752941)
THETA = ('1/10','9/10','3/25','3/5','3/20')
BODY = L.geometry(THETA)
RAW = BODY['raw']
C = BODY['g'][:2,0]
GAMMA = BODY['g'][2]
H, K = 1-GAMMA, 1-2*GAMMA
SIGMA = BODY['Sigma']
Z = SIGMA[2,2]
D = SIGMA.inv()[:2,:2]
REGRESSION = SIGMA[:2,2]/Z
P = S.Matrix((X,Y))
BASE = [p[:2,0] for p in RAW[:7]]
SUPPORTS = []
for i in range(7):
    e = BASE[(i+1)%7] - BASE[i]
    n = S.Matrix((e[1],-e[0]))
    SUPPORTS.append((n,n.dot(BASE[i])))
PORTS = [(a,b) for a,b in BODY['primal'] if a>=7 and b<7]


def clip(poly,n,h):
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        fp=n.dot(p)-h; fq=n.dot(q)-h
        if fp<=0:out.append(p)
        if fp*fq<0:out.append((fq*p-fp*q)/(fq-fp))
    dedup=[]
    for p in out:
        if not dedup or p!=dedup[-1]:dedup.append(p)
    if len(dedup)>1 and dedup[0]==dedup[-1]:dedup.pop()
    return dedup


def polygon(a,e):
    n,h = SUPPORTS[e]
    bound = (n.dot(C)-GAMMA*n.dot(RAW[a][:2,0])-K*h)/GAMMA
    return clip(BASE,n,bound)


def area2(poly):
    return sum(S.det(S.Matrix.hstack(p,q)) for p,q in zip(poly,poly[1:]+poly[:1]))


def makepoly(f):
    return S.Poly(f,X,Y,domain=S.QQ)


def row(A,eta=0):
    return (makepoly(A[0,0]),makepoly(2*A[0,1]),makepoly(A[1,1]),makepoly(eta))


@lru_cache(None)
def chart(a):
    v=(2*C-RAW[a][:2,0]-P)/K
    ys=[p[:2,0]-C+(p[2]-GAMMA)*v for p in RAW]
    w=v+REGRESSION
    cv=D.inv()+Z*w*w.T
    t=Z*(w.T*D*w)[0]
    si=D.row_join(-D*w).col_join((-w.T*D).row_join(S.Matrix([[(1+t)/Z]])))
    tr=(makepoly(cv[0,0]),makepoly(2*cv[0,1]),makepoly(cv[1,1]),makepoly(Z))
    return v,ys,cv,si,tr


@lru_cache(None)
def constraint(a,b,kind,datum=()):
    v,ys,cv,si,tr=chart(a)
    aa=ys[a]
    if kind=='spoke':
        return row(L.sym(aa,ys[b]-aa),-H)
    if kind=='top':
        j=int(datum[0])
        return row(aa*aa.T-ys[j]*ys[j].T)
    if kind=='chord':
        n,h=SUPPORTS[int(datum[0])]
        d=-n.dot(aa)
        s=h-n.dot(P)
        reflected=K*ys[b]+2*GAMMA*aa
        return row((d+s)**2*aa*aa.T-d*d*reflected*reflected.T)
    if kind=='floor':
        q=S.Matrix(tuple(map(R,datum)))
        coeff=(q[0]**2,2*q[0]*q[1],q[1]**2,q[2]**2)
        factor=makepoly(ELL*(q.T*si*q)[0])
        return tuple(makepoly(c)-factor*t for c,t in zip(coeff,tr))
    raise ValueError(kind)


def certificate_polys(a,b,terms):
    rr=[makepoly(0) for _ in range(4)]
    for term in terms:
        weight=R(term['weight'])
        assert weight>=0
        rows=constraint(a,b,term['kind'],tuple(term.get('data',())))
        for i,f in enumerate(rows):rr[i]-=weight*f
    determinant=rr[0]*rr[2]-rr[1]*rr[1]/4
    return (rr[0],determinant,rr[3])


def bernstein(poly,tri):
    """Exact coefficients on a closed triangle, using its actual total degree."""
    p0,p1,p2=tri
    # Expand by exact polynomial multiplication, avoiding expression substitution.
    lx=makepoly(p0[0]+X*(p1[0]-p0[0])+Y*(p2[0]-p0[0]))
    ly=makepoly(p0[1]+X*(p1[1]-p0[1])+Y*(p2[1]-p0[1]))
    px=[makepoly(1)];py=[makepoly(1)]
    for _ in range(poly.degree(X)):px.append(px[-1]*lx)
    for _ in range(poly.degree(Y)):py.append(py[-1]*ly)
    f=makepoly(0)
    for (i,j),c in poly.terms():f+=c*px[i]*py[j]
    n=f.total_degree()
    coeff=f.as_dict()
    values=[]
    for i in range(n+1):
        for j in range(n+1-i):
            value=S.S(0)
            for (u,v),c in coeff.items():
                if u<=i and v<=j:
                    value+=c*R(comb(i,u)*comb(j,v),comb(n,u+v)*comb(u+v,u))
            values.append(value)
    return values


def split_triangle(tri):
    # Longest exact Euclidean edge; deterministic tie-breaking.
    pairs=((0,1),(1,2),(2,0))
    i,j=max(pairs,key=lambda e:(tri[e[0]]-tri[e[1]]).dot(tri[e[0]]-tri[e[1]]))
    k=3-i-j; m=(tri[i]+tri[j])/2
    return [(tri[i],m,tri[k]),(m,tri[j],tri[k])]


def triangle_sign(poly,tri):
    bb=bernstein(poly,tri)
    return min(bb)>0, len(bb), min(bb)
```

### floor_local_locator.py
4366 bytes, SHA256 171193ba0f8168d87a2e90291e2e18dab7ee0833be52c4d5c829fc1535e8751e.
```python
"""Numerical locator only: fixed-shear full covariance floor, true top/chord port.
No numerical verdict is a promoted theorem. Exact certification is separate.
"""
import json
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog
import lift_core as L

ELL = float(L.R(540000000000000, 25985706405752941))
THETA = ('1/10', '9/10', '3/25', '3/5', '3/20')
BODY = L.geometry(THETA)
RAW = np.array([list(x) for x in BODY['raw']], dtype=float)
CENTROID = np.array(BODY['g'], dtype=float).reshape(3)
SIGMA = np.array(BODY['Sigma'], dtype=float)
Z = SIGMA[2,2]
REGRESSION = SIGMA[:2,2] / Z
D = np.linalg.inv(SIGMA)[:2,:2]
GAMMA = CENTROID[2]
H, K = 1-GAMMA, 1-2*GAMMA
PORTS = [(a,b) for a,b in BODY['primal'] if a>=7 and b<7]
BASE_SUPPORTS = []
for i in range(7):
    e = RAW[(i+1)%7,:2]-RAW[i,:2]
    n = np.array([e[1], -e[0]])
    BASE_SUPPORTS.append((n, n@RAW[i,:2]))


def quadrow(A):
    return np.array([A[0,0], 2*A[0,1], A[1,1], 0.0])


def sym(a,b):
    return (np.outer(a,b)+np.outer(b,a))/2


def prepare(v, a, b, chord=True):
    v = np.asarray(v)
    y = RAW[:,:2] - CENTROID[:2] + (RAW[:,2]-GAMMA)[:,None]*v
    beta = CENTROID[:2] + GAMMA*v
    w = v+REGRESSION
    cv = SIGMA[:2,:2] + np.outer(SIGMA[:2,2],v)+np.outer(v,SIGMA[:2,2])+Z*np.outer(v,v)
    t = Z*w@D@w
    inv = np.block([[D, -(D@w)[:,None]], [-(w@D)[None,:], np.array([[(1+t)/Z]])]])
    tr = np.array([cv[0,0], 2*cv[0,1], cv[1,1], Z])
    basis = np.zeros((4,3,3))
    basis[0,0,0] = 1
    basis[1,0,1] = basis[1,1,0] = 1
    basis[2,1,1] = basis[3,2,2] = 1
    fm = basis - ELL*tr[:,None,None]*inv
    objective = quadrow(sym(y[a], y[b]-y[a]))
    objective[-1] = -H
    rows, labels = [], []
    for j in range(7,10):
        if j == a:
            continue
        rows.append(quadrow(np.outer(y[a], y[a])-np.outer(y[j], y[j])))
        labels.append(('top', j))
    if chord:
        upper = [float((n@beta-h)/(n@y[a])) for n,h in BASE_SUPPORTS if n@y[a] < -1e-14]
        if not upper:
            raise ArithmeticError('No far chord endpoint')
        tau = min(upper)
        reflected = K*y[b] + 2*GAMMA*y[a]
        rows.append(quadrow(tau*tau*np.outer(y[a],y[a])-np.outer(reflected,reflected)))
        labels.append(('chord',tau))
    for q in ((1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,-1,0),
              (1,0,1),(1,0,-1),(0,1,1),(0,1,-1),
              (1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)):
        q = np.array(q, dtype=float)
        rows.append(np.einsum('i,kij,j->k', q, fm, q))
        labels.append(('floor', q.tolist()))
    return objective, tr, fm, rows, labels


def locate(v, a, b, chord=True, maxiter=80):
    objective, tr, fm, rows, labels = prepare(v,a,b,chord)
    for it in range(maxiter):
        res = linprog(-objective, A_ub=-np.array(rows), b_ub=np.zeros(len(rows)),
                      A_eq=tr[None,:], b_eq=[1.], bounds=[(None,None)]*4,
                      method='highs', options={'dual_feasibility_tolerance':1e-9,
                                             'primal_feasibility_tolerance':1e-9})
        if res.status != 0:
            return {'status':res.message, 'iteration':it}
        value = objective @ res.x
        active = [(labels[i], float(-x)) for i,x in enumerate(res.ineqlin.marginals) if x < -1e-9]
        if value < -1e-7:
            return {'status':'NEGATIVE_LP_BOUND', 'value':float(value), 'active':active,
                    'trace_dual':float(-res.eqlin.marginals[0]), 'x':res.x.tolist(), 'iteration':it}
        f = np.einsum('k,kij->ij', res.x, fm)
        vals, vecs = np.linalg.eigh(f)
        if vals[0] >= -1e-8:
            return {'status':'LOCAL_FLOOR_PASS', 'value':float(value), 'x':res.x.tolist(),
                    'eig':vals.tolist(), 'iteration':it}
        q = vecs[:,0]
        q /= np.max(np.abs(q))
        q = np.array([float(Fraction(float(t)).limit_denominator(100000)) for t in q])
        rows.append(np.einsum('i,kij,j->k', q, fm, q))
        labels.append(('floor', q.tolist()))
    return {'status':'ITERATION_LIMIT', 'value':float(value), 'x':res.x.tolist(), 'eig':vals.tolist()}


if __name__ == '__main__':
    for pt in [(0.1,0.26),(0.1,0.24),(0.12,0.28),(0.25,0.15),(0.15,0.15),(0.2,0.08)]:
        v = (2*CENTROID[:2]-RAW[9,:2]-pt)/K
        print('p9',pt,'v',v,flush=True)
        for a,b in PORTS:
            print(a,b,json.dumps(locate(v,a,b)),flush=True)
```
