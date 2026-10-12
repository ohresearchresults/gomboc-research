# material-aba5be49ea2a

AI research material

---

#!/usr/bin/env python3
"""Exact algebra/controls for NORMALIZED_RECIPROCAL_SUM_FIBERS_V1.
Python >=3.11, SymPy 1.14.0. This checker complements, not replaces, the
complete analytic continuum proof. No input data, RNG or network access.
Usage: python -B reciprocal_sum_fiber.py build|check
"""
from __future__ import annotations
import hashlib
import itertools
import json
from pathlib import Path
import sys
import sympy as sp
assert __debug__ and sys.version_info >= (3, 11)
assert sp.__version__ == "1.14.0"
R = sp.Rational

def canonical(obj: object) -> bytes:
    return (json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n").encode()

def strings(xs):
    return [str(x) for x in xs]

def calculation() -> dict:
    x, y, z, eta = sp.symbols("x y z eta", real=True)
    T = x*x + y*y + z*z
    Q = x**4 + y**4 + z**4
    poly = 48*eta**2 - 8*T*eta + T*T - 2*Q
    rsq = (x*x-4*eta, y*y-4*eta, z*z-4*eta)
    assert sp.expand(2*sum(a*a for a in rsq)-sum(rsq)**2+poly) == 0
    assert sp.expand(poly.subs(eta,z*z/4)+(x*x-y*y)**2) == 0
    heron = (-x+y+z)*(x-y+z)*(x+y-z)*(x+y+z)
    assert sp.expand(T*T-2*Q-heron) == 0
    assert sp.expand(6*Q-2*T*T-2*((x*x-y*y)**2+(x*x-z*z)**2+(y*y-z*z)**2)) == 0
    k = sp.symbols("k", positive=True)
    h = (k*k+1)/(k*k+k+1)
    axial = k/(k+2)+1/(2*k+1)
    gap = k*(k-1)**2/((k+2)*(2*k+1)*(k*k+k+1))
    assert sp.factor(h-axial-gap) == 0
    assert sp.factor(axial-R(9,10)-(2*k*k-25*k+2)/(10*(k+2)*(2*k+1))) == 0
    stream = hashlib.sha256()
    count = 0
    for lam in itertools.product(range(1,7), repeat=3):
        a = tuple(R(i,sum(lam)) for i in lam)
        invtrace = sum(1/t for t in a)
        b = tuple((1/t)/invtrace for t in a)
        ss = tuple(a[i]+b[i] for i in range(3))
        q = sum(a[i]*a[j] for i,j in itertools.combinations(range(3),2))
        e = sp.prod(a)/q
        assert all(a[i]*b[i] == e for i in range(3))
        assert sum(ss) == 2 and all(0<t<1 for t in ss)
        order = sorted(range(3), key=lambda i:ss[i], reverse=True)
        s = tuple(ss[i] for i in order)
        r = tuple(abs(a[i]-b[i]) for i in order)
        assert r[0] == r[1]+r[2]
        tt = sum(t*t for t in s); qq = sum(t**4 for t in s)
        assert 48*e*e-8*tt*e+tt*tt-2*qq == 0
        assert tt-12*e >= 0 and (tt-12*e)**2 == 6*qq-2*tt*tt
        assert 0<e<=s[2]**2/4
        aa = ((s[0]+r[0])/2,(s[1]-r[1])/2,(s[2]-r[2])/2)
        bb = tuple(s[i]-aa[i] for i in range(3))
        assert sum(aa)==sum(bb)==1 and all(t>0 for t in aa+bb)
        assert all(aa[i]*bb[i]==e for i in range(3))
        xx,yy,zz=aa[0],aa[2],aa[1]
        assert xx>=yy>=zz and xx*zz>=yy*yy
        orig=sorted(a,reverse=True)
        ratio=max(orig[0]/orig[1],orig[1]/orig[2])
        assert ratio==xx/yy
        assert sorted(aa)==sorted(a) or sorted(aa)==sorted(b)
        stream.update(canonical(dict(lam=lam,S=strings(s),eta=str(e),ratio=str(ratio))))
        count += 1
    # A nontrivial repeated-largest-eigenvalue fibre with two distinct pairs.
    S = sp.diag(R(82,91),R(82,91),R(18,91))
    D0 = sp.diag(R(80,91),-R(80,91),0)
    O = sp.Matrix([[R(3,5),-R(4,5),0],[R(4,5),R(3,5),0],[0,0,1]])
    assert O.T*O == sp.eye(3)
    D1 = O*D0*O.T
    A0,B0=(S+D0)/2,(S-D0)/2
    A1,B1=(S+D1)/2,(S-D1)/2
    for A,B in ((A0,B0),(A1,B1)):
        assert A.trace()==B.trace()==1 and A+B==S
        assert A*B==R(81,8281)*sp.eye(3)
    assert A1!=A0 and A1!=B0 and A0*A1!=A1*A0
    # Commuting strict pair-hull control with no ratio-9 lift at the SAME sum.
    S = sp.diag(R(9,10),R(11,20),R(11,20))
    Arel=Brel=S/2
    slacks=[R(82,91)*sp.eye(3)-S,9*Arel+Brel-R(90,91)*sp.eye(3),Arel+9*Brel-R(90,91)*sp.eye(3)]
    assert all(min(mat.diagonal())>0 for mat in slacks)
    assert Arel*Brel==Brel*Arel and Arel*Brel!=sp.trace(Arel*Brel)/3*sp.eye(3)
    root=sp.sqrt(609)
    av=(R(9,20)+root/60,R(11,40)-root/120,R(11,40)-root/120)
    bv=(R(9,20)-root/60,R(11,40)+root/120,R(11,40)+root/120)
    assert sp.simplify(sum(av)-1)==sp.simplify(sum(bv)-1)==0
    assert all(sp.simplify(av[i]*bv[i])==R(1,30) for i in range(3))
    K=(25+root)/4
    assert sp.simplify(av[0]/av[1]-K)==0
    assert sp.simplify(2*K*K-25*K+2)==0
    assert 609>11*11  # K>9, without floating-point comparison.
    assert R(182,209)<R(9,10)<R(82,91)
    return dict(identity="NORMALIZED_RECIPROCAL_SUM_FIBERS_V1",symbolic_identity_count=6,
        rational_spectral_controls=count,rational_control_stream_sha256=stream.hexdigest(),
        repeated_top=dict(S=[strings(row) for row in sp.diag(R(82,91),R(82,91),R(18,91)).tolist()],
            rotation=[strings(row) for row in O.tolist()],eta="81/8281",distinct_pairs=True),
        strict_hull_no_bounded_fibre=dict(S=strings(S.diagonal()),relaxed_A=strings(Arel.diagonal()),
            relaxed_B=strings(Brel.diagonal()),strict_LMI_minima=strings([min(v.diagonal()) for v in slacks]),
            actual_A=strings(av),actual_B=strings(bv),eta="1/30",max_adjacent_ratio=str(K),
            ratio_polynomial="2*K**2-25*K+2",ratio_exceeds_9=True),
        scope="Exact algebra and controls plus a separate analytic proof; no E17 exclusion or actual polyhedron construction.")

def main() -> None:
    if sys.argv[1:] not in (["build"],["check"]):
        raise SystemExit("usage: python -B reciprocal_sum_fiber.py build|check")
    result=calculation()
    data=canonical(result)
    path=Path(__file__).with_suffix(".json")
    if sys.argv[1]=="build":
        path.write_bytes(data)
    else:
        assert path.read_bytes()==data,"report differs from exact reconstruction"
    print("RECIPROCAL_SUM_FIBERS_EXACT_PASS",len(data),hashlib.sha256(data).hexdigest())
if __name__=="__main__":
    main()
