# material-b7092044e734

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""Exact formal arrow-cone countercontrol, not an actual polytope.
CPython 3.13.5 standard library; no external inputs or random search.
Usage: python -B -S reciprocal_gap.py build|check
The continuous and infinite-hierarchy proofs are in the companion text.
"""
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import sys


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def trace(a):
    return sum(a[i][i] for i in range(3))


def pair(a, b):
    return trace(matmul(a, b))


def diag(values):
    return [[values[i] if i == j else F(0) for j in range(3)] for i in range(3)]


def det(a):
    return sum((1 if (p in ((0,1,2),(1,2,0),(2,0,1))) else -1)
               * a[0][p[0]] * a[1][p[1]] * a[2][p[2]]
               for p in itertools.permutations(range(3)))


def minor2_sum(a):
    return sum(a[i][i]*a[j][j]-a[i][j]*a[j][i] for i,j in itertools.combinations(range(3),2))


def addv(x, y):
    return [a+b for a,b in zip(x,y)]


def arrow(x, displacement):
    return [[(x[i]*displacement[j]+displacement[i]*x[j])/2 for j in range(3)] for i in range(3)]


# Small exact polynomial ring in three variables, sufficient for the identities.
def padd(*polys):
    result = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            result[monomial] = result.get(monomial, F(0)) + coefficient
    return {m:c for m,c in result.items() if c}


def pscale(poly, scalar):
    return {m:c*scalar for m,c in poly.items() if c*scalar}


def pmul(p, q):
    result = {}
    for i, a in p.items():
        for j, b in q.items():
            m = tuple(x+y for x,y in zip(i,j))
            result[m] = result.get(m, F(0)) + a*b
    return {m:c for m,c in result.items() if c}


def square(p):
    return pmul(p,p)


def symbolic_checks():
    a,b,c = ({(1,0,0):F(1)}, {(0,1,0):F(1)}, {(0,0,1):F(1)})
    bc,ac,ab = pmul(b,c),pmul(a,c),pmul(a,b)
    p = padd(ac,ab,pscale(bc,-1))
    lhs = padd(square(p),pscale(padd(square(bc),square(ac),square(ab)),-1))
    rhs = pscale(pmul(pmul(a,bc),padd(a,pscale(b,-1),pscale(c,-1))),2)
    assert not padd(lhs,pscale(rhs,-1))
    reciprocal_gap = padd(pscale(padd(square(a),square(b),square(c)),3),pscale(square(padd(a,b,c)),-1))
    sum_differences = padd(square(padd(a,pscale(b,-1))),square(padd(a,pscale(c,-1))),square(padd(b,pscale(c,-1))))
    assert not padd(reciprocal_gap,pscale(sum_differences,-1))
    # Heron's spectral polynomial: D=4bc-(a-b-c)^2.
    delta = padd(square(padd(a,b,c)),pscale(padd(square(a),square(b),square(c)),-2))
    heron = padd(pscale(bc,4),pscale(square(padd(a,pscale(b,-1),pscale(c,-1))),-1))
    assert not padd(delta,pscale(heron,-1))
    return ['cofactor_dual_cone_identity','reciprocal_gap_sum_of_eigenvalue_differences','triangle_spectral_identity']


def diagnostics(m,n):
    s = matmul(m,n)
    t = trace(s)
    u = trace(matmul(s,s))
    return {'trace_product':t,'trace_product_square':u,'triangle_delta':t*t-2*u,
            'reciprocal_gap':3*u-t*t,'relative_gap':(3*u-t*t)/(t*t)}


def construct():
    identities = symbolic_checks()
    eps = F(1,20)
    basis = [[F(int(i==j)) for i in range(3)] for j in range(3)]
    identity = diag([F(1)]*3)
    constraints = []
    for i,j in itertools.combinations(range(3),2):
        for sign in (-1,1):
            x = basis[i]
            e = [eps*basis[i][k]+sign*basis[j][k] for k in range(3)]
            constraints.append({'kind':'offdiagonal','i':i,'j':j,'sign':sign,
                                'source':x,'target':addv(x,e),'matrix':arrow(x,e)})
            x = addv(basis[i],basis[j])
            e = [eps*x[k]+sign*(basis[i][k]-basis[j][k]) for k in range(3)]
            constraints.append({'kind':'diagonal_difference','i':i,'j':j,'sign':sign,
                                'source':x,'target':addv(x,e),'matrix':arrow(x,e)})
    assert len(constraints)==12
    for record in constraints:
        a = record['matrix']
        assert det(a)==0 and minor2_sum(a)<0 and trace(a)>0
        record['value_at_M0'] = pair(a,identity)
        assert record['value_at_M0'] in (eps,2*eps)
    q,r = [F(1),F(0),F(2)],[F(2),F(0),F(0)]
    b = arrow(q,[r[k]-q[k] for k in range(3)])
    assert b == diag([F(1),F(0),F(-4)])
    assert det(b)==0 and minor2_sum(b)<0
    n0=diag([F(1),F(1),F(1,10)])
    info=diagnostics(identity,n0)
    assert info['triangle_delta']==F(39,100)
    assert info['relative_gap']==F(18,49)
    assert pair(b,n0)==F(3,5)
    # Gershgorin enclosure valid for EVERY M satisfying the twelve weak arrows,
    # after the allowed normalization tr(M)=3. See analytic proof.
    radius = 8*eps+4*eps*eps
    low,high = 1-radius,1+radius
    assert (low,high)==(F(59,100),F(141,100))
    actual_inverse_upper = 1/low-4/high
    assert actual_inverse_upper == F(-9500,8319)<0
    # Uniform interior-cone margin at the blind pair, normalized by -tr(adj A).
    t,u=info['trace_product'],info['trace_product_square']
    radical=F(9,5)
    assert radical*radical==6*u-2*t*t
    assert (t-radical)/3==F(1,10)
    # Sharp fixed-M reciprocal-defect floor for the one dual halfspace.
    btrace=trace(b)
    bnorm=pair(b,b)
    floor=btrace*btrace/(3*bnorm-btrace*btrace)
    nstar=diag([F(10,7),F(17,14),F(5,14)])
    star=diagnostics(identity,nstar)
    assert trace(nstar)==3 and pair(b,nstar)==0
    assert star['relative_gap']==floor==F(3,14)
    assert star['triangle_delta']==F(12,7)>0
    return {'title':'MUTUAL_ALL_AGGREGATE_COFACTOR_BLIND_CONE_AND_RECIPROCAL_GAP_V1',
            'object_status':'Formal rational arrow-form matrix system, NOT a polytope or a mechanical construction',
            'epsilon':eps,'primal_constraints':constraints,'M0':identity,
            'dual_source':q,'dual_target':r,'dual_matrix':b,'N0':n0,
            'dual_value_at_N0':pair(b,n0),'blind_pair_diagnostics':info,
            'normalized_primal_spectral_interval':[low,high],
            'actual_inverse_dual_uniform_upper':actual_inverse_upper,
            'all_cofactor_uniform_relative_margin':F(1,10),
            'fixed_M_sharp_gap_floor':floor,'Nstar':nstar,'Nstar_diagnostics':star,
            'polynomial_identity_checks':identities,
            'continuous_proofs':'Companion proof: complete arrow cone, all SPD matrices, all scalar aggregates and arbitrary mutual cofactor iterations; no finite sampling claim.'}


def encode(value):
    if isinstance(value,F):
        return str(value.numerator) if value.denominator==1 else str(value)
    if isinstance(value,dict):
        return {k:encode(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):
        return [encode(v) for v in value]
    return value


def main():
    if len(sys.argv)!=2 or sys.argv[1] not in ('build','check'):
        raise SystemExit('Usage: python -B -S reciprocal_gap.py build|check')
    data = (json.dumps(encode(construct()),sort_keys=True,indent=2,ensure_ascii=True)+'\n').encode()
    path=Path('reciprocal_gap.json')
    if sys.argv[1]=='build':
        path.write_bytes(data)
    else:
        if not path.exists() or path.read_bytes()!=data:
            raise SystemExit('Exact output mismatch or missing reciprocal_gap.json')
    print('ALL_THREE_POLYNOMIAL_IDENTITIES_PASS')
    print('TWELVE_STRICTLY_FEASIBLE_RANK_TWO_PRIMAL_ARROW_FORMS_PASS')
    print('ONE_STRICTLY_FEASIBLE_DUAL_ARROW_BUT_NO_RECIPROCAL_METRIC_PASS')
    print('MUTUAL_COFACTOR_BLIND_PAIR_DELTA_39_OVER_100_PASS')
    print('SHARP_FIXED_M_RECIPROCAL_GAP_THREE_OVER_FOURTEEN_PASS')
    print('FORMAL_MATRIX_CONTROL_NOT_A_POLYTOPE')
    print(path.name,len(data),hashlib.sha256(data).hexdigest())


if __name__=='__main__':
    main()
