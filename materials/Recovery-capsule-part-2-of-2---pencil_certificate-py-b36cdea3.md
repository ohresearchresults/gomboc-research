# material-b36cdea35fb1

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

#!/usr/bin/env python3
"""Complete fixed cut-stack projective pencil: recover and check exact stresses.

No input checkpoint or hidden cache is required.  Mode `build` discovers integer
weights with a deterministic, seed-free floating LP and then verifies the entire
continuum in integer/rational arithmetic.  Mode `verify` uses the generated JSON
and NEVER calls a numerical optimizer.  The analytical geometry and perturbation
argument are in the companion proof.  Assertions must remain enabled.

Observed source environment: CPython 3.13.5, SymPy 1.14.0, NumPy 2.3.5,
SciPy 1.17.0; OPENBLAS_NUM_THREADS=1.  Run:
  OPENBLAS_NUM_THREADS=1 python -B pencil_certificate.py build
  OPENBLAS_NUM_THREADS=1 python -B pencil_certificate.py verify
"""
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
import argparse
import hashlib
import json
from fractions import Fraction as F
from itertools import combinations
from math import comb, gcd, lcm
from pathlib import Path
import numpy as np
import sympy as s

DEG = 17
PAIRS = ((0,0),(0,1),(0,2),(1,1),(1,2),(2,2))
EDGES = ((0,2),(0,3),(0,6),(1,2),(1,4),(1,7),(2,5),(2,8),
         (3,4),(3,5),(3,9),(4,5),(4,9),(5,9),(6,7),(6,8),(7,8))
ARROWS = tuple(ij for edge in EDGES for ij in (edge,edge[::-1]))
CYCLES = ((0,3,4,1,7,6),(0,2,5,3),(0,6,8,2),(1,4,5,2),
          (1,2,8,7),(3,9,4),(3,5,9),(4,9,5),(6,7,8))
TETS = ((0,1,2,5),(0,1,4,5),(0,3,4,5),(3,4,5,9),
        (0,1,2,8),(0,1,7,8),(0,6,7,8))
IDENTITY = 'FULL_CUT_STACK_FIXED_PROJECTIVE_PENCIL_ALL_NONZERO_PSD_V1'
GAMMA = F(1,2**26)
ETA = F(1,2**53)
DELTA = F(1,2**68)
SCALE_EXPECTED = 1343519457280
DENMAX_EXPECTED = F(506018631541267125,14)


def symbolic_geometry():
    """Actual seven-positive-tetrahedron moments, not assigned vertex masses."""
    a = s.Symbol('a')
    r = s.Rational
    beta = r(2,5)
    p = [r(1,5),r(2,5),r(3,5)]
    q = [r(1,4),r(1,3),r(1,2)]
    u = [r(1,5),r(2,5),r(2,5)]
    ps = r(4,5)
    d = [1+a*x for x in p]
    e = [1+(1-a)*x for x in q]
    ds = 1+a*ps
    base = [s.Matrix([0,-beta,0]),s.Matrix([0,1-beta,0]),s.Matrix([0,0,1])]
    vs = s.Matrix([-ps,sum(u[i]*base[i][1] for i in range(3)),u[2]])
    vr = s.Matrix([q[2],0,1])/(1+q[2])
    frame = s.Matrix.hstack(vs,vr,s.Matrix([0,1,0]))
    T = s.diag(ds,e[2]/(1+q[2]),1)*frame.inv()
    vertices = (base + [s.Matrix([-p[i],base[i][1],base[i][2]])/d[i] for i in range(3)]
                + [s.Matrix([q[i],base[i][1],base[i][2]])/e[i] for i in range(3)] + [vs/ds])
    Z = [(T*x).applyfunc(s.cancel) for x in vertices]
    assert Z[9] == s.Matrix([1,0,0]) and Z[8] == s.Matrix([0,1,0])
    weights = [p[2]/d[2],p[1]/(d[1]*d[2]),p[0]/s.prod(d),
               (ps-sum(p[i]*u[i] for i in range(3)))/(ds*s.prod(d)),
               q[2]/e[2],q[1]/(e[1]*e[2]),q[0]/s.prod(e)]
    total = sum(weights)
    D = s.factor(total*T.det())
    J = s.zeros(3,1)
    for tet,w in zip(TETS,weights):
        J += w*sum((Z[i] for i in tet),s.zeros(3,1))
    g = (J/(4*total)).applyfunc(s.cancel)
    N = 12*a**5-7*a**4-80*a**3+1975*a**2+22400*a+40500
    Q = 20000*(a-5)**2*(a-4)**2*(a+5)**2*(2*a+5)**2*(3*a+5)**2*N
    assert s.cancel(D-N/(5*(a-5)*(a-4)*(a+5)*(2*a+5)*(3*a+5))) == 0
    H = []
    R = []
    for i,j in ARROWS:
        h = (Z[i]-g)*(Z[j]-Z[i]).T
        h = ((h+h.T)/2).applyfunc(s.cancel)
        H.append(h)
        rr = (Q*h).applyfunc(s.cancel)
        assert all(s.Poly(x,a,domain=s.QQ).degree() <= DEG for x in rr)
        R.append(rr)
    for x in Z:
        for z in x:
            n,h = s.fraction(s.cancel(z))
            assert s.Poly(n,a).degree() <= 1 and s.Poly(h,a).degree() <= 1
            assert h.subs(a,-r(5,4))*h.subs(a,3) > 0
        assert all(sum(z*z for z in x.subs(a,aa)) < 25 for aa in [-r(5,4),s.Integer(3)])
    return a,Z,g,D,N,Q,R


def bernstein(poly,a):
    """Elevated degree-17 Bernstein coefficients on a=-5/4+(17/4)t."""
    co = list(reversed(s.Poly(poly,a,domain=s.QQ).all_coeffs()))
    mon = [sum(F(co[h])*comb(h,i)*F(-5,4)**(h-i)*F(17,4)**i
               for h in range(i,len(co))) for i in range(DEG+1)]
    return [sum(mon[i]*F(comb(b,i),comb(DEG,i)) for i in range(b+1))
            for b in range(DEG+1)]


def initial_bernstein(R,a):
    scale = 4**DEG*lcm(*(comb(DEG,k) for k in range(DEG+1)))
    B = np.empty((DEG+1,34,6),dtype=object)
    for j,hh in enumerate(R):
        for k,(x,y) in enumerate(PAIRS):
            for b,v in enumerate(bernstein(hh[x,y],a)):
                z = v*scale
                assert z.denominator == 1
                B[b,j,k] = z.numerator
    common = 0
    for x in B.flat:
        common = gcd(common,x)
    assert common > 0 and scale % common == 0
    B //= common
    scale //= common
    assert scale == SCALE_EXPECTED
    return B,scale


def split(B):
    """Exact de Casteljau halves; each output has 2**17 extra scaling."""
    n = len(B)-1
    work = B.copy()
    left = [work[0]*2**n]
    right = [work[-1]*2**n]
    for k in range(1,n+1):
        work = work[:-1]+work[1:]
        left.append(work[0]*2**(n-k))
        right.append(work[-1]*2**(n-k))
    return np.array(left,dtype=object),np.array(right[::-1],dtype=object)


def all_trees():
    """Enumerate all 4641 undirected spanning trees and all ten rootings."""
    out = []
    for chosen in combinations(range(len(EDGES)),9):
        parent = list(range(10))
        adj = [[] for _ in range(10)]
        for e in chosen:
            i,j = EDGES[e]
            ii,jj = i,j
            while parent[ii] != ii:
                ii = parent[ii]
            while parent[jj] != jj:
                jj = parent[jj]
            if ii == jj:
                break
            parent[ii] = jj
            adj[i].append((j,2*e))
            adj[j].append((i,2*e+1))
        else:
            for root in range(10):
                seen = {root}
                todo = [root]
                rr = []
                for v in todo:
                    for u,idx in adj[v]:
                        if u not in seen:
                            seen.add(u)
                            todo.append(u)
                            rr.append(idx^1)
                assert len(seen) == 10 and len(rr) == 9
                out.append(sorted(rr))
    trees = np.array(out,dtype=np.int64)
    assert trees.shape == (46410,9)
    masks = np.array([sum(1<<int(i) for i in t) for t in trees],dtype=np.uint64)
    assert len(set(map(int,masks))) == 46410
    return trees,masks


def mats(X):
    out = np.empty(X.shape[:-1]+(3,3),dtype=X.dtype)
    for k,(i,j) in enumerate(PAIRS):
        out[...,i,j] = out[...,j,i] = X[...,k]
    return out


def positive_rows(P):
    for a,b,c,e,f,h in P:
        if a <= 0 or a*e-b*b <= 0 or a*e*h+2*b*c*f-a*f*f-e*c*c-h*b*b <= 0:
            return False
    return True


def exact_positive(B,ids,w):
    return positive_rows(-sum(int(ww)*B[:,i,:] for i,ww in zip(ids,w)))


def robust_stress(C,ids):
    """Discovery ONLY.  Every returned integer is subsequently checked exactly."""
    from scipy.optimize import linprog
    A = C[:,ids]
    sc = np.maximum(np.max(np.linalg.norm(A,axis=(2,3)),axis=0),1e-50)
    A = A/sc[None,:,None,None]
    n,k = len(ids),len(A)
    nv = n+3*k+1
    U = np.zeros((9*k,nv))
    for h in range(k):
        for i in range(3):
            U[9*h+i,:n] = -A[h,:,i,i]
            U[9*h+i,-1] = 1
            for j,(ii,jj) in enumerate([(0,1),(0,2),(1,2)]):
                if i in (ii,jj):
                    U[9*h+i,n+3*h+j] = 1
        for j,(i,l) in enumerate([(0,1),(0,2),(1,2)]):
            U[9*h+3+2*j,:n] = A[h,:,i,l]
            U[9*h+4+2*j,:n] = -A[h,:,i,l]
            U[9*h+3+2*j,n+3*h+j] = U[9*h+4+2*j,n+3*h+j] = -1
    eq = np.zeros((1,nv))
    eq[0,:n] = 1
    c = np.zeros(nv)
    c[-1] = -1
    lp = linprog(c,A_ub=U,b_ub=np.zeros(9*k),A_eq=eq,b_eq=[1],
                 bounds=[(0,None)]*(nv-1)+[(None,None)],method='highs')
    if not lp.success or lp.x[-1] <= 1e-7:
        dirs = np.vstack([np.eye(3),[[1,1,0],[1,-1,0],[1,0,1],[1,0,-1],[0,1,1],[0,1,-1]]]).astype(float)
        dirs /= np.linalg.norm(dirs,axis=1)[:,None]
        L = np.einsum('ki,bnij,kj->bkn',dirs,A,dirs).reshape(-1,n)
        c = np.r_[np.zeros(n),-1.]
        eq = np.r_[np.ones(n),0.][None,:]
        for step in range(60):
            lp = linprog(c,A_ub=np.c_[-L,np.ones(len(L))],b_ub=np.zeros(len(L)),
                         A_eq=eq,b_eq=[1],bounds=[(0,None)]*n+[(None,None)],method='highs')
            if not lp.success or lp.x[-1] <= 1e-7:
                return None
            mm = np.einsum('n,bnij->bij',lp.x[:n],A)
            ev,v = np.linalg.eigh(mm)
            if np.min(ev[:,0]) > 1e-7:
                break
            bad = ev[:,0] <= 1e-7
            vec = v[bad,:,0]
            L = np.vstack([L,np.einsum('bi,bnij,bj->bn',vec,A[bad],vec)])
        else:
            return None
    w = lp.x[:n]/sc
    w = np.rint(w/max(w)*10**8).astype(np.int64)
    keep = np.where(w > 0)[0]
    return [int(ids[j]) for j in keep],[int(w[j]) for j in keep]


def build(B,Z,a,trees,masks):
    """Seed-free exact-checked discovery; no randomness or external inputs."""
    zfun = s.lambdify(a,np.array([list(z) for z in Z],dtype=object).tolist(),'numpy')
    nodes = []
    calls = 0
    def visit(B,lo,hi,pending,depth):
        nonlocal calls
        mid = -1.25+4.25*float((lo+hi)/2)
        zz = np.array(zfun(mid),dtype=float)
        ev,v = np.linalg.eigh(np.cov(zz.T,bias=True))
        W = (v/np.sqrt(ev))@v.T
        val = np.array(B,dtype=float)
        C = -np.einsum('ij,bnjk,kl->bnil',W,mats(val/np.max(np.abs(val))),W)
        before = len(pending)
        certs = []
        while len(pending):
            first = int(pending[0])
            calls += 1
            if calls % 500 == 0:
                print('DISCOVERY_CALL',calls,flush=True)
            result = robust_stress(C,list(trees[first]))
            if result is None or not exact_positive(B,*result):
                break
            ids,w = result
            bits = np.uint64(sum(1<<i for i in ids))
            covered = (masks[pending]&bits) == bits
            assert covered[0]
            certs.append([ids,w])
            pending = pending[~covered]
        nodes.append({'interval':[str(lo),str(hi)],'certificates':certs,
                      'trees_in':before,'trees_left':len(pending)})
        print('DISCOVERED_NODE',str(lo),str(hi),len(certs),len(pending),flush=True)
        if len(pending):
            if depth >= 9:
                raise RuntimeError('Uncovered leaf: this run has NOT proved the theorem')
            left,right = split(B)
            middle = (lo+hi)/2
            visit(left,lo,middle,pending,depth+1)
            visit(right,mid,hi,pending,depth+1)
    visit(B,F(0),F(1),np.arange(len(trees)),0)
    return {'identity':IDENTITY,'nodes':nodes,'calls':calls}


def verify(record,B,scale,Q,N,a,Z,D,trees,masks):
    """Only integers/rationals and exhaustive exact combinatorial tests below."""
    assert record['identity'] == IDENTITY
    denmax = max(bernstein(Q,a))
    assert denmax == DENMAX_EXPECTED
    nb = bernstein(N,a)
    assert min(nb) == F(2008125,128) and max(nb) == 125664
    assert F(2008125,128)/202125 > F(1,16)
    # The five positive absolute denominator factors have these endpoint maxima.
    denominator_bound = 5*F(25,4)*F(21,4)*8*11*14
    assert denominator_bound == 202125
    # Endpoint segment interpolation keeps all normalized vertices in radius 5.
    assert all(all(sum(x*x for x in z.subs(a,aa)) < 25 for aa in [-s.Rational(5,4),s.Integer(3)]) for z in Z)
    counts = []
    rows_checked = 0
    pos = 0
    def visit(B,lo,hi,pending,scale):
        nonlocal pos,rows_checked
        assert pos < len(record['nodes'])
        node = record['nodes'][pos]
        pos += 1
        assert node['interval'] == [str(lo),str(hi)] and node['trees_in'] == len(pending)
        for ids,w in node['certificates']:
            assert ids == sorted(set(ids)) and len(ids) == len(w) and ids
            assert all(type(i) is int and 0 <= i < 34 for i in ids)
            assert all(type(v) is int and v > 0 for v in w)
            bits = np.uint64(sum(1<<i for i in ids))
            P = -sum(ww*B[:,i,:] for i,ww in zip(ids,w))
            threshold = GAMMA*sum(w)*scale*denmax
            P *= threshold.denominator
            P[:,0] -= threshold.numerator
            P[:,3] -= threshold.numerator
            P[:,5] -= threshold.numerator
            assert positive_rows(P)
            rows_checked += len(P)
            cover = (masks[pending]&bits) == bits
            assert len(pending) and cover[0]
            pending = pending[~cover]
        assert node['trees_left'] == len(pending)
        counts.append([str(lo),str(hi),len(node['certificates']),len(pending)])
        if len(pending):
            left,right = split(B)
            mid = (lo+hi)/2
            visit(left,lo,mid,pending,scale*2**DEG)
            visit(right,mid,hi,pending,scale*2**DEG)
    visit(B,F(0),F(1),np.arange(len(trees)),scale)
    assert pos == len(record['nodes'])
    # Exact rational guards for the parameter-to-vertex Lipschitz proof.
    eps = F(1,100)
    smin,smax,qmin,qmax = F(79,100),F(81,100),F(49,100),F(51,100)
    umin,umax = F(38,100),F(42,100)
    assert smin+qmin*umin > F(9,10) and smax+qmax*umax < F(11,10)
    assert F(41,100)-F(39,100)*(1-umax) < F(1,5)
    assert max(1/smin,1+1/qmin) < 4
    assert max(1+1/smin,1/qmin) < 3
    assert 1+smax*(1+1/qmin) < F(7,2)
    assert 1+(1+1/smin)*qmax < F(11,5)
    assert 1-F(61,100)/smin > F(1,5)
    assert 1-(F(1,3)+eps)/qmin > F(1,5)
    assert 1+(1+1/qmin)*F(61,100) < 4
    assert 1+(1+1/smin)*(F(1,3)+eps) < 4
    assert max(1/(smin*F(4,5)),1/(qmin*F(1,2))) < 5
    assert F(11,10)*7+4*3 < 20
    assert F(11,10)+F(3,5)*3+F(1,5)*2+2*3 < 11
    # Uniform refill collar and full ten-transverse-parameter tube arithmetic.
    assert 7*(24*25+24*5+8) == 5096
    assert 5096*ETA < F(1,32)
    assert 1+2*5*5096*32 == 1630721 < 2**21
    assert 10*2**22+20+2**23*ETA < 2**26
    assert 2**26*ETA == GAMMA/2
    assert 60*8+16*20*64 == 20960 < 2**15
    assert 2**15*DELTA == ETA
    result = {'identity':IDENTITY,'rooted_trees':len(trees),'node_counts':counts,
              'positive_integer_matrix_rows_checked':rows_checked,'gamma':str(GAMMA),
              'bernstein_degree':DEG,'global_bernstein_scale':scale,'denominator_upper_bound':str(denmax),
              'normalized_vertex_radius_bound':5,'normalized_six_volume_lower_bound':'1/16',
              'same_incidence_refill_vertex_radius':str(ETA),'ten_transverse_parameter_sup_radius':str(DELTA),
              'scope':'One entire actual projective pencil and its explicit same-incidence transverse tube. Not the full eleven-parameter incidence or all E17; no new own110 attainer.',
              'marker':'FULL_CUT_STACK_PENCIL_ALLROOT_GAMMA_TUBE_EXACT_PASS'}
    return result


def write_json(path,value):
    text = json.dumps(value,sort_keys=True,separators=(',',':'))+'\n'
    path.write_text(text,encoding='utf-8')
    return hashlib.sha256(text.encode()).hexdigest()


def main():
    if not __debug__:
        raise RuntimeError('Assertions must remain enabled')
    parser = argparse.ArgumentParser()
    parser.add_argument('mode',choices=['build','verify'])
    parser.add_argument('--certificate',default='pencil_stresses.json')
    parser.add_argument('--report',default='pencil_verification.json')
    args = parser.parse_args()
    print('SYMBOLIC_BEGIN',flush=True)
    a,Z,g,D,N,Q,R = symbolic_geometry()
    print('SYMBOLIC_READY',flush=True)
    B,scale = initial_bernstein(R,a)
    print('BERNSTEIN_READY',flush=True)
    trees,masks = all_trees()
    print('TREES_READY',flush=True)
    path = Path(args.certificate)
    if args.mode == 'build':
        record = build(B,Z,a,trees,masks)
        # Never write an unchecked certificate as the successful output.
        result = verify(record,B,scale,Q,N,a,Z,D,trees,masks)
        certificate_sha = write_json(path,record)
    else:
        record = json.loads(path.read_text(encoding='utf-8'))
        result = verify(record,B,scale,Q,N,a,Z,D,trees,masks)
        certificate_sha = hashlib.sha256(path.read_bytes()).hexdigest()
    result['certificate_sha256'] = certificate_sha
    result['certificate_bytes'] = path.stat().st_size
    write_json(Path(args.report),result)
    print(json.dumps(result,sort_keys=True,indent=2))
    print(result['marker'])

if __name__ == '__main__':
    main()
