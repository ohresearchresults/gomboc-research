# material-13029a0a2ece

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""NEUTRAL_GERM_DECISION_OCTAGON_V1.
Exact scalar-germ screen for the calibrated two-parameter primal carrier family.
Python 3.11+; SymPy 1.14.0. No numerical search or external input.
Run: python neutral_germ.py build ; python neutral_germ.py check
This is NOT an S1U1 construction or a whole-layer exclusion.
"""
from __future__ import annotations
from functools import cmp_to_key
from pathlib import Path
import hashlib
import json
import sys
import sympy as S

SIGMA, TAU = S.symbols('sigma tau')
T = S.Symbol('t')
R = S.Rational


def leading(expr: S.Expr) -> tuple[int, S.Expr] | None:
    expr = S.cancel(expr)
    if expr == 0:
        return None
    num, den = S.fraction(expr)
    a = S.Poly(num, T)
    b = S.Poly(den, T)
    ia, ca = min((mon[0], c) for mon, c in a.terms())
    ib, cb = min((mon[0], c) for mon, c in b.terms())
    return ia - ib, ca / cb


def sign(expr: S.Expr) -> int:
    lc = leading(expr)
    return 0 if lc is None else int(S.sign(lc[1]))


def limit0(expr: S.Expr) -> S.Expr:
    lc = leading(expr)
    if lc is None or lc[0] > 0:
        return S.S.Zero
    if lc[0] == 0:
        return lc[1]
    return S.oo if lc[1] > 0 else -S.oo


def decide(rows: list[tuple[S.Expr, S.Expr]]) -> dict:
    """Decide closure at (0,0) of all A(sigma)+tau B(sigma)>0.

    Coefficients are rational, and A(0)=0. Returned paths are rational
    and analytic after removing removable singularities at t=0.
    Every branch is decided by exact signs of univariate rational germs.
    """
    for a, b in rows:
        S.Poly(a, SIGMA, domain=S.QQ)
        S.Poly(b, SIGMA, domain=S.QQ)
        assert a.subs(SIGMA, 0) == 0
    for w in (1, -1):
        if all(w * b.subs(SIGMA, 0) > 0 for _, b in rows):
            return dict(feasible=True, sigma=S.S.Zero, tau=w*T,
                        orders=[1]*len(rows), method='axis')
    attempts = []
    for eps in (1, -1):
        rr = [(a.subs(SIGMA, eps*T), b.subs(SIGMA, eps*T)) for a,b in rows]
        low, high = [], []
        impossible = False
        for a, b in rr:
            sb = sign(b)
            if not sb:
                if sign(a) <= 0:
                    impossible = True
                    break
            elif sb > 0:
                low.append(S.cancel(-a/b))
            else:
                high.append(S.cancel(-a/b))
        if impossible:
            attempts.append((eps, 'identically normal-blind nonpositive row'))
            continue
        cmp = cmp_to_key(lambda a,b: sign(a-b))
        lo = max(low, key=cmp) if low else None
        hi = min(high, key=cmp) if high else None
        if lo is not None and hi is not None and sign(hi-lo) <= 0:
            attempts.append((eps, 'empty eventual interval'))
            continue
        ll = -S.oo if lo is None else limit0(lo)
        uu = S.oo if hi is None else limit0(hi)
        if ll > 0 or uu < 0:
            attempts.append((eps, 'interval does not approach tau=0'))
            continue
        if ll < 0 < uu:
            path = S.S.Zero
        elif ll == 0 and uu == 0:
            path = S.cancel((lo+hi)/2)
        elif ll == 0 and uu > 0:
            path = S.cancel(lo+T)
        elif ll < 0 and uu == 0:
            path = S.cancel(hi-T)
        else:
            raise AssertionError((lo,hi,ll,uu))
        assert limit0(path) == 0
        exits = [S.cancel(a+path*b) for a,b in rr]
        assert all(sign(v)>0 for v in exits)
        return dict(feasible=True, sigma=eps*T, tau=path,
                    orders=[leading(v)[0] for v in exits], method='interval',
                    lower=lo, upper=hi)
    return dict(feasible=False, attempts=attempts)


def fixtures() -> tuple[list[S.Matrix], list[tuple[int,...]], S.Matrix, S.Matrix]:
    raw = [(1,0,1),(1,R(1,4),1),(0,1,1),(-R(1,3),1,1),
           (-1,0,1),(-1,-R(1,2),1),(0,-1,1),(R(2,3),-1,1),
           (0,0,-3),(R(4,5),-R(4,5),R(1,5))]
    vs = [S.Matrix(v) for v in raw]
    fs = [(0,1,2,3,4,5,6,7),(0,1,8,9),(1,2,8),(2,3,8),
          (3,4,8),(4,5,8),(5,6,8),(6,7,9,8),(7,0,9)]
    for k,f in enumerate(fs):
        a,b,c = [vs[i] for i in f[:3]]
        n = (b-a).cross(c-a)
        assert all(n.dot(vs[i]-a)==0 for i in f)
        slack = [n.dot(v-a) for v in vs]
        assert all(z<=0 for z in slack) or all(z>=0 for z in slack)
        if any(z>0 for z in slack):
            fs[k] = tuple(reversed(f))
    q = S.Matrix([0,0,1])
    m = S.diag(R(108626543272,1008891919),R(417435378368,9080027271),1)
    return vs,fs,q,m


def moments(vs: list[S.Matrix], fs: list[tuple[int,...]]) -> tuple[S.Expr,S.Matrix]:
    vol = S.S.Zero
    mom = S.zeros(3,1)
    for f in fs:
        a = vs[f[0]]
        for k in range(1,len(f)-1):
            b,c = vs[f[k]],vs[f[k+1]]
            w = a.dot(b.cross(c))
            vol += w
            mom += w*(a+b+c)
    vol = S.cancel(vol)
    return vol, (mom/(4*vol)).applyfunc(S.cancel)


def center(vs, fs, q):
    _,g = moments(vs,fs)
    return [(v-g*(1-q.dot(v))/(1-q.dot(g))).applyfunc(S.cancel) for v in vs]


def poles(vs, fs):
    return [S.Matrix.vstack(*(vs[i].T for i in f[:3])).inv()*S.ones(3,1) for f in fs]


def census(vs, fs, m):
    pp = poles(vs,fs)
    for j,f in enumerate(fs):
        assert all(pp[j].dot(vs[i])==1 for i in f)
        assert all(pp[j].dot(vs[i])<1 for i in range(len(vs)) if i not in f)
    ee = sorted({tuple(sorted((f[i],f[(i+1)%len(f)]))) for f in fs for i in range(len(f))})
    n = m.inv()
    rows = {}
    for i,j in ee:
        f,h = [k for k,ids in enumerate(fs) if i in ids and j in ids]
        for a,b in ((i,j),(j,i)):
            rows[f'P:{a}:{b}'] = (vs[a].T*m*(vs[b]-vs[a]))[0]
        for a,b in ((f,h),(h,f)):
            rows[f'Q:{a}:{b}'] = (pp[a].T*n*(pp[b]-pp[a]))[0]
    u = [i for i in range(len(vs)) if max(v for k,v in rows.items() if k.startswith(f'P:{i}:'))<0]
    s = [i for i in range(len(fs)) if max(v for k,v in rows.items() if k.startswith(f'Q:{i}:'))<0]
    hlist = []
    for i,j in ee:
        f,h = [k for k,ids in enumerate(fs) if i in ids and j in ids]
        if max(rows[f'P:{i}:{j}'],rows[f'P:{j}:{i}'],rows[f'Q:{f}:{h}'],rows[f'Q:{h}:{f}'])<0:
            hlist.append((i,j))
    return dict(VEF=(len(vs),len(ee),len(fs)), counts=(len(s),len(u),len(hlist)),
                stable=s, unstable=u, saddles=hlist,
                zeros=[k for k,v in rows.items() if v==0], rows=rows)


def build():
    raw,fs,q,m = fixtures()
    vs = center(raw,fs,q)
    assert moments(vs,fs)[1] == S.zeros(3,1)
    assert vs[8] == S.Matrix([-R(742,5463),R(1901,7284),-R(5399,1821)])
    assert vs[9] == S.Matrix([R(4222,5463),-R(5447,7284),R(377,1821)])
    initial = census(vs,fs,m)
    assert initial['VEF']==(10,17,9) and initial['counts']==(2,4,4)
    assert set(initial['zeros']) == {'P:0:1','P:2:3','P:4:5','P:6:7','P:8:3','P:9:7'}
    transformed = [v/(1+SIGMA*(1-q.dot(v))) for v in vs]
    xx = center(transformed,fs,q)
    assert moments(xx,fs)[1] == S.zeros(3,1)
    assert all(xx[i]==vs[i] for i in fs[0])
    pp = poles(xx,fs)
    for f,ids in enumerate(fs):
        assert all(S.cancel(pp[f].dot(xx[i])-1)==0 for i in ids)
    mt = m+TAU*q*q.T
    for i,j in ((0,1),(2,3),(4,5),(6,7)):
        assert S.cancel((xx[i].T*mt*(xx[j]-xx[i]))[0])==0
    rows,details = [],[]
    for i,j in ((8,3),(9,7)):
        expr = S.cancel((xx[i].T*mt*(xx[j]-xx[i]))[0])
        num,den = S.fraction(expr)
        v0 = den.subs({SIGMA:0,TAU:0})
        assert v0 != 0
        if v0<0: num,den = -num,-den
        assert S.degree(num,TAU)<=1
        a,b = S.expand(num.subs(TAU,0)),S.diff(num,TAU)
        assert a.subs(SIGMA,0)==0 and S.degree(num,SIGMA)<=15
        rows.append((a,b))
        axis1 = S.diff(expr,SIGMA).subs({SIGMA:0,TAU:0})
        axis2 = S.diff(expr,TAU).subs({SIGMA:0,TAU:0})
        simple = S.cancel(expr.subs({SIGMA:T,TAU:-T}))
        assert sign(simple)>0
        details.append(dict(edge=(i,j), numerator=num, denominator=den,
                            sigma_degree=S.degree(num,SIGMA), response=(axis1,axis2),
                            simple_path_order=leading(simple)[0], simple_path_leading=leading(simple)[1]))
    decision = decide(rows)
    assert decision['feasible']
    aa = [z['response'][0] for z in details]
    bb = [z['response'][1] for z in details]
    assert aa[0]<0<aa[1] and bb[0]<0<bb[1]
    for a,b in rows:
        assert sign(a.subs(SIGMA,decision['sigma'])+decision['tau']*b.subs(SIGMA,decision['sigma']))>0
    d = max(max(S.degree(a,SIGMA),S.degree(b,SIGMA)) for a,b in rows)
    assert max(decision['orders']) <= 3*d
    units = [
        ('axis',[(0,1),(0,2)],True),
        ('fifth_order_strip',[(SIGMA**2,1),(-SIGMA**2+SIGMA**5,-1)],True),
        ('empty_strip',[(-SIGMA**2,1),(0,-1)],False),
        ('negative_sigma',[(-SIGMA,0)],True),
        ('blind_identical',[(0,0)],False),
        ('single_lower',[(-SIGMA**2,1)],True),
    ]
    unit_reports = {}
    for name, rr, expected in units:
        out = decide([(S.sympify(a),S.sympify(b)) for a,b in rr])
        assert out['feasible']==expected
        unit_reports[name]=out
    assert unit_reports['fifth_order_strip']['orders']==[5,5]
    assert unit_reports['negative_sigma']['sigma']==-T
    return dict(name='NEUTRAL_GERM_DECISION_OCTAGON_V1', sympy=S.__version__,
                scope='Calibrated carrier-neutral family; NOT S1U1 and NOT global regularization.',
                initial=initial, exact_vertices=vs, faces=fs, metric=m,
                outside_rows=details, rational_decision=decision,
                theorem_degree_bound=15, theorem_off_order_bound=45, theorem_carrier_order=46,
                algebraic_unit_tests=unit_reports)


def clean(value):
    if isinstance(value,dict):
        return {str(k):clean(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):
        return [clean(v) for v in value]
    if isinstance(value,S.MatrixBase):
        return clean(value.tolist())
    if isinstance(value,S.Basic):
        return str(value)
    return value


def main():
    if not __debug__:
        raise RuntimeError('Assertions must be enabled.')
    if S.__version__!='1.14.0':
        raise RuntimeError('Reproduction requires SymPy 1.14.0.')
    if len(sys.argv)!=2 or sys.argv[1] not in ('build','check'):
        raise SystemExit('Usage: python neutral_germ.py build|check')
    data = (json.dumps(clean(build()),sort_keys=True,indent=2)+'\n').encode()
    path = Path('neutral_germ_report.json')
    if sys.argv[1]=='build':
        path.write_bytes(data)
    else:
        assert path.read_bytes()==data
    print('NEUTRAL_GERM_OCTAGON_EXACT_PASS')
    for p in (Path(__file__),path):
        blob=p.read_bytes()
        print(p.name,len(blob),hashlib.sha256(blob).hexdigest())

if __name__=='__main__':
    main()
