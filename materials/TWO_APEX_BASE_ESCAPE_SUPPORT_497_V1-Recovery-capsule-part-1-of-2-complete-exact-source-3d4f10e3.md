# material-3d4f10e37ec1

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""TWO_APEX_BASE_ESCAPE_SUPPORT_497_V1. Standard library, exact arithmetic.
All vector controls are NONBODIES. No search and no external data are needed.
Run with assertions enabled: python -S base_escape_support.py build|check
The continuous own-COM and angular arguments are in the accompanying proof.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys

assert __debug__, 'Run without -O: exact certificate assertions are required.'
N = 6
ORDER = ['x', 'max_base_b', 'second_apex_z', 'first_pole_q', 'base_pole_B', 'escape_target_w']
Y = [F(-36), F(12), F(450,19), F(180,19)]
MU = [F(360,19), F(60,19), F(15), F(90), F(135), F(135,4)]
FIRST_SQUARE = [F(-6),F(15,2),F(0),F(1),F(-30,19),F(0)]
SECOND_SQUARE = [F(0),F(0),F(2),F(0),F(8,57),F(-1)]

def dot(a,b):
    assert len(a)==len(b)
    return sum((x*y for x,y in zip(a,b)), F(0))

def scaled(a,c):
    return [c*x for x in a]

def D(i,j):
    a = [[F(0) for _ in range(N)] for _ in range(N)]
    a[i][j] += F(1,2)
    a[j][i] += F(1,2)
    return a

def matrices_sum(*terms):
    return [[sum((c*A[i][j] for c,A in terms), F(0)) for j in range(N)] for i in range(N)]

def inner(A,G):
    return sum((A[i][j]*G[i][j] for i in range(N) for j in range(N)),F(0))

def outer(v):
    return [[a*b for b in v] for a in v]

def forms():
    E = [D(0,0),D(0,3),D(1,4),D(4,5)]
    I = [matrices_sum((1,D(0,4)),(1,D(2,4))),
         matrices_sum((1,D(4,4)),(-1,D(3,4))), D(1,3),
         matrices_sum((1,D(1,1)),(-1,D(0,1))),
         matrices_sum((1,D(2,2)),(-1,D(2,5))),
         matrices_sum((1,D(5,5)),(-1,D(1,1)))]
    d = [F(-2),F(0),F(1),F(0),F(0),F(0)]
    return E,I,d

def exact_identity():
    E,I,d = forms()
    S = matrices_sum((1,D(3,3)), *[(-c,A) for c,A in zip(Y,E)], *list(zip(MU,I)))
    SOS = matrices_sum((1,outer(FIRST_SQUARE)),(F(135,4),outer(SECOND_SQUARE)))
    assert S==SOS
    assert all(x>0 for x in MU)
    lower = sum(Y)-dot(MU,d)
    assert lower==F(609,19)>32
    assert F(360,19)>0
    # A matrix sum of outer products is positive semidefinite in every dimension.
    return {'vector_order':ORDER,'equality_multipliers':Y,'inequality_multipliers':MU,
            'equality_matrices':E,'inequality_matrices':I,'inequality_upper_bounds':d,
            'gram_residual_matrix':S,'square1':FIRST_SQUARE,
            'square2':SECOND_SQUARE,'square2_weight':F(135,4),
            'q_norm_squared_lower':lower,'actual_mass_delta_coefficient':F(360,19)}

def vector_control(name,v,excluded=False):
    v = [tuple(map(F,z)) for z in v]
    G = [[dot(a,b) for b in v] for a in v]
    E,I,d = forms()
    assert [inner(A,G) for A in E]==[1,1,1,1]
    iv = [inner(A,G) for A in I]
    slack = [a-b for a,b in zip(d,iv)]
    delta = slack[0]
    assert delta>0
    q2 = G[3][3]
    s1 = [sum((FIRST_SQUARE[i]*v[i][k] for i in range(N)),F(0)) for k in range(3)]
    s2 = [sum((SECOND_SQUARE[i]*v[i][k] for i in range(N)),F(0)) for k in range(3)]
    residual = dot(s1,s1)+F(135,4)*dot(s2,s2)
    assert q2-F(609,19)==residual+dot(MU,slack)
    if excluded:
        assert slack[2]<0 and all(s>=0 for i,s in enumerate(slack) if i!=2)
        assert q2==F(8245,324)<32 and G[1][3]==F(25,9)>1
        assert delta==F(1,10)
    else:
        assert min(slack)>=0 and delta==F(1,2) and q2==F(489,4)
        # The two poles support all listed primal vectors; b and w remain distinct.
        for p in (0,1,2,5):
            assert G[3][p]<=1 and G[4][p]<=1
        assert v[1]!=v[5]
        assert G[1][1]==F(4,5) and G[5][5]==F(37,80) and G[2][2]==F(13,64)
    return {'identity':name,'scope':'RATIONAL_COMMON_VECTOR_CONTROL_NOT_A_POLYHEDRON',
            'vectors':v,'gram':G,'slacks':slack,'delta':delta,'q2':q2,
            'sum_of_squares_value':residual,
            'omitted_support_control':excluded,
            'not_a_110_attainer':True}

def arithmetic():
    qmin = F(609,19)
    umin = qmin-1
    prod5 = 1+16*umin
    delta5 = 16*MU[0]
    prod4 = 1+64*umin
    upper = F(729)/(1+F(9,4)*(F(1,10)+F(1,9)))
    eta = F(4,9)*(F(729)/prod5-1)
    assert umin==F(590,19)
    assert prod5==F(9459,19) and delta5==F(5760,19)
    assert prod4==F(37779,19)>729
    assert upper==F(29160,59)<prod5
    assert prod5-upper==F(4041,1121)>0
    assert eta==F(1952,9459) and F(1,10)+F(1,9)>eta
    return {'u_strict_lower':umin,'degree5_product_strict_lower':prod5,
            'degree5_delta_coefficient':delta5,'degree4_product_strict_lower':prod4,
            'V10_F9_global_product_strict_upper':upper,'rational_gap':prod5-upper,
            'sufficient_1_over_V_plus_1_over_F':eta,
            'C_minimum_lower_unchanged':34,'upper_object_unchanged':622,
            'new_FULL_LOCAL_census':'NOT_COMPUTED'}

def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x

def build():
    positive=[(0,0,1),(F(2,5),0,F(4,5)),(F(1,4),F(-3,10),F(9,40)),
              (F(1,2),11,1),(F(9,2),8,-1),(F(1,2),F(-1,10),F(9,20))]
    negative=[(0,0,1),(F(2,5),0,F(4,5)),(F(-1,5),0,F(1,5)),
              (F(89,18),0,1),(F(9,2),0,-1),(F(2,5),0,F(4,5))]
    report={'identity':'TWO_APEX_BASE_ESCAPE_SUPPORT_497_V1',
            'certificate':exact_identity(),'arithmetic':arithmetic(),
            'controls':[vector_control('DISTINCT_TARGET_POSITIVE_DELTA_HALF_V1',positive),
                        vector_control('MISSING_FIRST_FACET_SUPPORT_DELTA_TENTH_V1',negative,True)]}
    return (json.dumps(encode(report),sort_keys=True,separators=(',',':'))+'\n').encode('utf-8')

if __name__=='__main__':
    if sys.argv[1:] not in (['build'],['check']):
        raise SystemExit('usage: python -S base_escape_support.py build|check')
    data = build()
    path = Path('base_escape_support.json')
    if sys.argv[1]=='build':
        if path.exists():assert path.read_bytes()==data, 'Existing output differs.'
        path.write_bytes(data)
    else:
        assert path.read_bytes()==data, 'Output differs from exact reconstruction.'
    print('COMMON_SUPPORT_BASE_ESCAPE_TWO_SQUARES_609_OVER19_PASS')
    print('DEG5_9459_OVER19_VS_29160_OVER59_PASS')
    print('DISTINCT_TARGET_AND_MISSING_SUPPORT_NONBODY_CONTROLS_PASS')
    print(path.name,len(data),hashlib.sha256(data).hexdigest())
    print('TWO_APEX_BASE_ESCAPE_SUPPORT_497_DURABLE_RECOVERY_PASS')
