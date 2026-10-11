# material-424f1477139f

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

#!/usr/bin/env python3
"""CLOSED_BOUNDARY_TRACE_ATLAS_10_V1. Exact finite-chart compiler and controls.
Only Python's standard library. Assertions must be enabled. No random inputs.
Commands: python -S trace_atlas_exact.py build|check
Outputs are reproducible audit data, not an exhaustive solution of the charts.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
from math import isqrt
from pathlib import Path
import json
import sys


class P:
    """Sparse integer polynomial; monomials are sorted variable-index tuples."""
    __slots__ = ('terms',)
    def __init__(self, terms=0):
        if isinstance(terms, P):
            self.terms = terms.terms.copy()
        elif isinstance(terms, int):
            self.terms = {(): terms} if terms else {}
        else:
            self.terms = {tuple(k): int(v) for k, v in terms.items() if v}
            assert all(tuple(sorted(k)) == k for k in self.terms)
    def __add__(self, other):
        other = P(other)
        d = self.terms.copy()
        for k, v in other.terms.items():
            d[k] = d.get(k, 0) + v
            if d[k] == 0:
                del d[k]
        return P(d)
    __radd__ = __add__
    def __neg__(self):
        return P({k: -v for k, v in self.terms.items()})
    def __sub__(self, other):
        return self + (-P(other))
    def __rsub__(self, other):
        return P(other) - self
    def __mul__(self, other):
        other = P(other)
        d = {}
        for k, v in self.terms.items():
            for l, w in other.terms.items():
                m = tuple(sorted(k + l))
                d[m] = d.get(m, 0) + v*w
        return P(d)
    __rmul__ = __mul__
    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out = P(1)
        for _ in range(n):
            out = out*self
        return out
    def data(self):
        return [[list(k), v] for k, v in sorted(self.terms.items())]
    def evaluate(self, xs):
        out = Q(0)
        for mon, coefficient in self.terms.items():
            term = Q(coefficient)
            for j in mon:
                term = term*xs[j]
            out = out + term
        return out
    def stats(self):
        return {'degree': max(map(len, self.terms), default=0),
                'height': max(map(abs, self.terms.values()), default=0),
                'l1': sum(map(abs, self.terms.values())),
                'terms': len(self.terms)}


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def sub(a, b):
    return [x-y for x, y in zip(a, b)]


def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0]]


def det(a, b, c):
    return dot(a, cross(b, c))


class Q:
    """Exact ordered field Q(sqrt(2)), used only for the cube control."""
    __slots__ = ('a', 'b')
    def __init__(self, a=0, b=0):
        if isinstance(a, Q):
            assert b == 0
            self.a, self.b = a.a, a.b
        else:
            self.a, self.b = F(a), F(b)
    def __add__(self, o):
        o = Q(o)
        return Q(self.a+o.a, self.b+o.b)
    __radd__ = __add__
    def __neg__(self):
        return Q(-self.a, -self.b)
    def __sub__(self, o):
        return self + (-Q(o))
    def __rsub__(self, o):
        return Q(o)-self
    def __mul__(self, o):
        o = Q(o)
        return Q(self.a*o.a+2*self.b*o.b, self.a*o.b+self.b*o.a)
    __rmul__ = __mul__
    def __truediv__(self, o):
        o = Q(o)
        norm = o.a*o.a-2*o.b*o.b
        assert norm
        return self*Q(o.a/norm, -o.b/norm)
    def __rtruediv__(self, o):
        return Q(o)/self
    def __eq__(self, o):
        o = Q(o)
        return self.a == o.a and self.b == o.b
    def sign(self):
        a, b = self.a, self.b
        if b == 0:
            return (a > 0)-(a < 0)
        if a == 0:
            return (b > 0)-(b < 0)
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        c = (a*a > 2*b*b)-(a*a < 2*b*b)
        assert c != 0
        return c if a > 0 else -c
    def __lt__(self, o):
        return (self-Q(o)).sign() < 0
    def __le__(self, o):
        return (self-Q(o)).sign() <= 0
    def data(self):
        return [str(self.a), str(self.b)]


def sqrt_fraction(x):
    x = F(x)
    assert x >= 0
    for d in (1, 2):
        y = x/d
        a, b = isqrt(y.numerator), isqrt(y.denominator)
        if a*a == y.numerator and b*b == y.denominator:
            return Q(F(a, b)) if d == 1 else Q(0, F(a, b))
    raise ValueError('Control requires a square root outside Q(sqrt(2))')


class Atlas:
    def __init__(self):
        self.names = []
        self.constraints = []
    def add(self, name, p, kind='eq'):
        assert kind in ('eq', 'ge')
        self.constraints.append((name, kind, P(p)))
    def var(self, name, low, high):
        assert name not in self.names
        j = len(self.names)
        self.names.append(name)
        p = P({(j,): 1})
        low, high = F(low), F(high)
        self.add(name+':lo', low.denominator*p-low.numerator, 'ge')
        self.add(name+':hi', high.numerator-high.denominator*p, 'ge')
        return p
    def vector(self, name, low, high):
        return [self.var(name+f'_{k}', low, high) for k in range(3)]
    def data(self):
        stats = [p.stats() for _, _, p in self.constraints]
        return {'variables': self.names,
                'constraints': [[name, kind, p.data()]
                                for name, kind, p in self.constraints],
                'stats': {'n': len(self.names), 'm': len(stats),
                          'equalities': sum(k == 'eq' for _, k, _ in self.constraints),
                          'degree': max(s['degree'] for s in stats),
                          'height': max(s['height'] for s in stats),
                          'max_l1': max(s['l1'] for s in stats),
                          'total_terms': sum(s['terms'] for s in stats)}}


def check_discrete(N, triangles, root, pair, r, m):
    assert 4 <= N <= 10
    assert len(triangles) == 2*N-4
    edge = Counter()
    for t in triangles:
        assert len(t) == 3 and len(set(t)) == 3
        assert all(0 <= i < N for i in t)
        for i, j in zip(t, t[1:]+t[:1]):
            edge[min(i,j), max(i,j)] += 1 if i < j else -1
    assert all(v == 0 for v in edge.values()), 'Not a closed oriented 2-chain'
    T = len(triangles)
    for group in (root, pair[0], pair[1]):
        assert len(set(group)) == len(group)
        assert all(0 <= i < T for i in group)
    assert pair[0] and pair[1] and not (set(pair[0]) & set(pair[1]))
    assert 0 <= r < N and 0 <= m < N


def compile_chart(N, triangles, root, pair, r, m):
    """Generate the full integer-polynomial chart, with the fixed 51/25 trace."""
    check_discrete(N, triangles, root, pair, r, m)
    A = Atlas()
    v = [A.vector(f'v{i}', -1, 1) for i in range(N)]
    g = A.vector('g', -1, 1)
    V = A.var('V', F(1,6), 8)
    b = A.var('b', -2048, 2048)
    u = A.vector('u', -384, 384)
    L = A.var('L', F(4,3), 4)
    z = [A.var(f'z{i}', 0, 4) for i in range(N)]
    zc = A.var('zc', 0, 4)
    H = A.var('H', 0, 4)
    M = A.var('M', 0, 4)
    a = A.var('a', 0, 1)
    h = A.var('h', 0, 2)
    tau = A.var('tau', 0, 4)
    normals, heights, scales = [], [], []
    for t in range(len(triangles)):
        normals.append(A.vector(f'n{t}', -1, 1))
        heights.append(A.var(f'beta{t}', -2, 2))
        scales.append(A.var(f's{t}', 0, 16))
    witnesses = {}
    for i, j in combinations(range(len(triangles)), 2):
        witnesses[i,j] = (A.vector(f'w{i}_{j}', -1, 1),
                           A.var(f'c{i}_{j}', -2, 2))
    for i, value in enumerate(((0,0,0),(1,0,0),(0,1,0),(0,0,1))):
        for k in range(3):
            A.add(f'delta_{i}_{k}', v[i][k]-value[k])
    for i in range(N):
        A.add(f'ell_{i}', z[i]-b-dot(u,v[i]))
        A.add(f'range_{i}', L-z[i], 'ge')
    A.add('mean_ell', b+dot(u,g)-1)
    A.add('ell_center_delta', 4*zc-4*b-sum(u))
    A.add('min_ell', z[r])
    A.add('max_ell', z[m]-L)
    D, B = [], []
    for t, (i,j,k) in enumerate(triangles):
        n, beta, s = normals[t], heights[t], scales[t]
        A.add(f'unit_n{t}', dot(n,n)-1)
        cp = cross(sub(v[j],v[i]), sub(v[k],v[i]))
        for q in range(3):
            A.add(f'orientation_{t}_{q}', cp[q]-s*n[q])
        for q in (i,j,k):
            A.add(f'contact_{t}_{q}', dot(n,v[q])-beta)
        for q in range(N):
            A.add(f'support_{t}_{q}', beta-dot(n,v[q]), 'ge')
        D.append(det(*[[4*x-1 for x in v[q]] for q in (i,j,k)]))
        B.append(det(*[sub(v[q],g) for q in (i,j,k)]))
    for (i,j), (w,c) in witnesses.items():
        A.add(f'unit_w{i}_{j}', dot(w,w)-1)
        A.add(f'tangent_{i}_{j}', dot(w,[x+y for x,y in zip(normals[i],normals[j])]))
        for q in triangles[i]:
            A.add(f'separate_left_{i}_{j}_{q}', c-dot(w,v[q]), 'ge')
        for q in triangles[j]:
            A.add(f'separate_right_{i}_{j}_{q}', dot(w,v[q])-c, 'ge')
    for p, group in enumerate(pair):
        ref = group[0]
        for t in group[1:]:
            for k in range(3):
                A.add(f'pair_normal_{p}_{t}_{k}', normals[t][k]-normals[ref][k])
            A.add(f'pair_height_{p}_{t}', heights[t]-heights[ref])
    for t in root:
        for q in triangles[t]:
            A.add(f'root_patch_{t}_{q}', z[q])
    A.add('volume', 384*V-sum(D))
    for k in range(3):
        A.add(f'centroid_{k}', 6144*V*g[k]
              -sum(D[t]*(1+4*sum(v[q][k] for q in tri))
                   for t,tri in enumerate(triangles)))
    second = P(0)
    for t, tri in enumerate(triangles):
        zs = [zc]+[z[q] for q in tri]
        second += D[t]*(sum(zs)**2+sum(x*x for x in zs))
    A.add('second_moment', 7680*V*H-second)
    A.add('root_mass', 2*V*a*a-sum(B[t] for t in root))
    selected = tuple(pair[0])+tuple(pair[1])
    A.add('high_trace', 25*sum(B[t]*sum(z[q] for q in triangles[t])
                              for t in selected)-306*V, 'ge')
    A.add('tau_le_L', L-tau, 'ge')
    A.add('lower_concavity', L*h-a*(L-tau), 'ge')
    A.add('lower_mass', L*h*h+tau*(a*a+a*h)-3)
    A.add('lower_mean', h*h*L*(L+2*tau)+a*(a+2*h)*tau*tau-12)
    A.add('lower_second', 30*M-h*h*L*(L*L+2*L*tau+3*tau*tau)
          -a*(a+3*h)*tau**3)
    return A


CUBE_VERTICES = ((0,0,0),(1,0,0),(0,1,0),(0,0,1),
                 (1,1,0),(1,0,1),(0,1,1),(1,1,1))
CUBE_FACES = ((0,2,4,1),(0,1,5,3),(0,3,6,2),
              (3,5,7,6),(2,6,7,4),(1,4,7,5))
CUBE_TRIANGLES = tuple((f[0],f[j],f[j+1]) for f in CUBE_FACES for j in (1,2))


def cube_control():
    root = (0,1)
    pair = ((6,7),(2,3))
    A = compile_chart(8,CUBE_TRIANGLES,root,pair,0,3)
    values = {}
    def assign(name, value):
        assert name not in values
        values[name] = Q(value)
    def vector(name, vec):
        for k,x in enumerate(vec):
            assign(name+f'_{k}',x)
    for i,v in enumerate(CUBE_VERTICES):
        vector(f'v{i}',v)
    vector('g',(F(1,2),)*3)
    assign('V',1); assign('b',0); vector('u',(0,0,2)); assign('L',2)
    for i,v in enumerate(CUBE_VERTICES):
        assign(f'z{i}',2*v[2])
    assign('zc',F(1,2)); assign('H',F(4,3)); assign('M',F(4,3))
    assign('a',Q(0,F(1,2))); assign('h',Q(0,F(1,2))); assign('tau',2)
    normals, heights = [], []
    for t,tri in enumerate(CUBE_TRIANGLES):
        i,j,k = tri
        cp = cross(sub(CUBE_VERTICES[j],CUBE_VERTICES[i]),
                   sub(CUBE_VERTICES[k],CUBE_VERTICES[i]))
        s = sqrt_fraction(dot(cp,cp))
        n = [Q(x)/s for x in cp]
        beta = dot(n,CUBE_VERTICES[i])
        vector(f'n{t}',n); assign(f'beta{t}',beta); assign(f's{t}',s)
        normals.append(n); heights.append(beta)
    for i,j in combinations(range(len(CUBE_TRIANGLES)),2):
        ni,nj = normals[i],normals[j]
        if ni != nj:
            direction = sub(nj,ni)
            length2 = dot(direction,direction)
            assert length2.b == 0
            length = sqrt_fraction(length2.a)
            w = [x/length for x in direction]
            c = (heights[j]-heights[i])/length
        else:
            left = [CUBE_VERTICES[k] for k in CUBE_TRIANGLES[i]]
            right = [CUBE_VERTICES[k] for k in CUBE_TRIANGLES[j]]
            answer = None
            for tri in (left,right):
                for k in range(3):
                    direction = cross(ni,sub(tri[(k+1)%3],tri[k]))
                    length2 = dot(direction,direction)
                    assert length2.b == 0
                    length = sqrt_fraction(length2.a)
                    for sign in (1,-1):
                        w0 = [sign*x/length for x in direction]
                        low = max(dot(w0,x) for x in left)
                        high = min(dot(w0,x) for x in right)
                        if low <= high:
                            answer = w0,(low+high)/2
                            break
                    if answer:
                        break
                if answer:
                    break
            assert answer is not None
            w,c = answer
        vector(f'w{i}_{j}',w); assign(f'c{i}_{j}',c)
    assert set(values) == set(A.names)
    xs = [values[name] for name in A.names]
    failures = []
    for name,kind,p in A.constraints:
        value = p.evaluate(xs)
        if not (value == 0 if kind == 'eq' else value.sign() >= 0):
            failures.append((name,value.data()))
    assert failures == [('high_trace',['-81','0'])], failures
    # Omitting ONLY high_trace gives an exact feasible equality-law control.
    return {'chart':A.data(), 'values':[x.data() for x in xs],
            'only_failed_constraint':failures,
            'true_fvector':[8,12,6], 'triangles':CUBE_TRIANGLES,
            'true_trace':'3/2', 'lower_second':'4/3', 'gap':'0'}


def stellar(triangles, index, vertex):
    triangles = list(triangles)
    a,b,c = triangles[index]
    triangles[index:index+1] = [(a,b,vertex),(b,c,vertex),(c,a,vertex)]
    return tuple(triangles)


def uniform_arithmetic():
    # L1 bounds hold for every legal label choice, before cancellations.
    T = 16
    majorants = {
        'D':6*5**3,
        'B':6*2**3,
        'volume':384+T*6*5**3,
        'centroid':6144+T*6*5**3*13,
        'second_moment':7680+T*6*5**3*20,
        'root_mass':2+T*6*2**3,
        'high_trace':306+25*T*6*2**3*3,
        'lower_second':30+6+4,
    }
    n = lambda N:4*N+15+5*(2*N-4)+4*((2*N-4)*(2*N-5)//2)
    records = []
    for N in range(4,11):
        t = 2*N-4; pairs = t*(t-1)//2
        # Root uses <=t triangles; pair groups are disjoint and nonempty.
        m = (2*n(N)+12+2*N+4+(7+N)*t+8*pairs
             +4*(t-2)+3*t+1+3+1+1+1+5)
        records.append({'N':N,'T':t,'variables':n(N),'max_constraints':m})
    assert max(r['variables'] for r in records) == 615
    assert max(r['max_constraints'] for r in records) < 4096
    assert max(majorants.values()) == 247680 < 2**20
    # Every omitted elementary polynomial has L1 <= 4096.
    assert 384*3+1 < 4096 and 2049 < 4096
    # JPT Thm 1: with n<=640,m<=4096,d=6,H=2^20,
    # Htilde=H. log2(base)<24+3n<2^11, exponent<2^(10+4n).
    assert 2*640+2*4096 < 2**20
    assert 24+3*640 < 2**11
    assert 10+4*640+11 == 2581 < 2600
    return {'majorants':majorants,'chart_size_bounds':records,
            'JPT_parameters':{'n_upper':640,'m_upper':4096,'even_degree':6,
                              'height':2**20},
            'safe_gap':'2^(-2^2600)',
            'inverse_gap_log2_upper':'2^2581',
            'new_complexity_bound':False}


def payload():
    cube = cube_control()
    triangles = stellar(stellar(CUBE_TRIANGLES,0,8),3,9)
    # Worst-size symbolic audit; these root/group labels need not be feasible.
    worst = compile_chart(10,triangles,tuple(range(16)),
                          (tuple(range(8)),tuple(range(8,16))),0,3)
    W = worst.data()
    bounds = uniform_arithmetic()
    assert W['stats']['n'] == 615
    assert W['stats']['m'] == bounds['chart_size_bounds'][-1]['max_constraints']
    for obj in (cube['chart'],W):
        s = obj['stats']
        assert s['n'] <= 640 and s['m'] <= 4096
        assert s['degree'] <= 6 and s['height'] < 2**20
        assert s['max_l1'] <= 247680
    return {'identity':'CLOSED_BOUNDARY_TRACE_ATLAS_10_V1',
            'purpose':'Exact compiler/audit; no exhaustive chart infeasibility search',
            'cube_equality_control':cube,
            'worst_symbolic_chart':{'triangles':triangles,'chart':W},
            'uniform_bounds':bounds}


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ('build','check'):
        raise SystemExit('usage: python -S trace_atlas_exact.py build|check')
    assert __debug__, 'Assertions must be enabled'
    obj = payload()
    data = (json.dumps(obj,ensure_ascii=True,sort_keys=True,indent=2)+'\n').encode()
    target = Path('trace_atlas_exact.json')
    if sys.argv[1] == 'build':
        target.write_bytes(data)
    else:
        assert target.read_bytes() == data
    worst = obj['worst_symbolic_chart']['chart']['stats']
    cube = obj['cube_equality_control']['chart']['stats']
    print('CLOSED_BOUNDARY_POLYNOMIAL_COMPILER_PASS',worst['n'],worst['m'],
          worst['degree'],worst['height'])
    print('EXACT_CUBE_ALL_BUT_HIGH_TRACE_PASS',cube['n'],cube['m'],'-81')
    print('UNIFORM_CHART_BOUNDS_PASS 640 4096 6 1048576')
    print('JPT_EFFECTIVE_GAP_ARITHMETIC_PASS 2^(-2^2600)')
    print('TRACE_ATLAS_RECOVERY_PASS',len(data),sha256(data).hexdigest())
    print('NO_E17_EXCLUSION_NO_NEW_COMPLEXITY_BOUND')


if __name__ == '__main__':
    main()
