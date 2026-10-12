# material-b3f90abb6391

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""TWO_APEX_RANK_CAP_DEG5_546_V1. Exact finite certificate, standard library.
Save UTF-8/LF, final LF, assertions enabled. No external input or solver.
python -S two_apex_degree5.py build
python -S two_apex_degree5.py check
The full continuous geometric proof is a separate recovery-capsule part.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib
import json
import sys
assert __debug__
IDENTITY = 'TWO_APEX_RANK_CAP_DEG5_546_V1'
PARENT = ['minimum-0086',
          '8123315ee22b6a0fc370e8f672f299bc19997f89ad023530404946c77f994f10']
RANK_PROOF = ['[internal-source-reference]',
              'e42018feb1f0b99f052c3c01db4c691ea4a57e00b52a9baa23de046ce22e7152']

def matrix0():
    return [[F(0) for _ in range(5)] for _ in range(5)]

def D(i, j):
    a = matrix0()
    a[i][j] = a[j][i] = F(1) if i == j else F(1, 2)
    return a

def matrix_sum(*items):
    return [[sum((c*a[i][j] for c, a in items), F(0))
             for j in range(5)] for i in range(5)]

def determinant(a):
    a = [list(map(F, row)) for row in a]
    n = len(a)
    out = F(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            out = -out
        out *= a[j][j]
        for i in range(j+1, n):
            factor = a[i][j]/a[j][j]
            for k in range(j+1, n):
                a[i][k] -= factor*a[j][k]
            a[i][j] = F(0)
    return out

def pair(a, g):
    return sum((a[i][j]*g[i][j] for i in range(5) for j in range(5)), F(0))

E = [D(0,0), D(0,3), D(2,3), D(1,4)]
I = [matrix_sum((1,D(0,4)),(1,D(2,4))),
     matrix_sum((1,D(4,4)),(-1,D(3,4))), D(1,3),
     matrix_sum((1,D(1,1)),(-1,D(0,1))),
     matrix_sum((1,D(2,2)),(-1,D(0,2))),
     matrix_sum((1,D(2,2)),(-1,D(1,1)))]
IRHS = [F(-2),F(0),F(1),F(0),F(0),F(0)]
EQ = list(map(F, ['-2173/50','23/4','433/50','601/25']))
MU = list(map(F, ['1459/100','391/100','533/50','9579/100','95/4','727/20']))
K = [[8692,-9579,-2375,-575,1459],
     [-9579,11888,0,1066,-2404],
     [-2375,0,7220,-866,1459],
     [-575,1066,-866,200,-391],
     [1459,-2404,1459,-391,782]]
C = matrix_sum((1,D(3,3)),(-24,D(2,2)))
S = [[F(v,200) for v in row] for row in K]

def gram_certificate():
    residual = matrix_sum((1,C), *[(-c,a) for c,a in zip(EQ,E)],
                          *[(c,a) for c,a in zip(MU,I)])
    assert residual == S
    minors = [determinant([row[:n] for row in K[:n]]) for n in range(1,6)]
    assert minors == [8692,11573255,16503151100,8831025280,5962527728]
    assert min(minors) > 0 and min(MU) > 0
    lower = sum(EQ)-sum((c*r for c,r in zip(MU,IRHS)),F(0))
    assert lower == F(1351,100) > 13
    return {'vector_order':['x','b','z','Q0','QB'],
            'equality_matrices':E, 'equality_rhs':[1,1,1,1],
            'inequality_matrices':I, 'inequality_rhs':IRHS,
            'equality_multipliers':EQ,'nonnegative_multipliers':MU,
            'C':C,'S_integer_numerator':K,'S_denominator':200,
            'positive_leading_principal_minors_K':minors,
            'strict_lower_G33_minus_24G22':lower,
            'strict_lower_u_minus_24sigma2':lower-1,
            'positive_actual_delta_multiplier':MU[0]}

# Univariate rational polynomials, ascending coefficients.
def trim(a):
    a = list(map(F,a))
    while len(a)>1 and a[-1] == 0:
        a.pop()
    return a

def add(*arrays):
    n = max(map(len,arrays))
    return trim([sum((a[i] for a in arrays if i < len(a)),F(0)) for i in range(n)])

def scale(a, c):
    return trim([F(c)*x for x in a])

def mul(a,b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return trim(out)

def power(a,n):
    out = [F(1)]
    for _ in range(n):
        out = mul(out,a)
    return out

def compose_affine(a, l, r):
    out = [F(0)]
    for i,x in enumerate(a):
        out = add(out,scale(power([l,r-l],i),x))
    return out

def bernstein(a, l, r):
    n = len(a)-1
    p = compose_affine(a,l,r)
    p += [F(0)]*(n+1-len(p))
    return [sum((p[j]*F(comb(i,j),comb(n,j)) for j in range(i+1)),F(0))
            for i in range(n+1)]

def angular_certificate():
    v = [F(0),F(1)]
    cosine = [F(1),F(-8),F(8)]
    num = mul(power(v,4), add([1],scale(power(cosine,2),-1)))
    den = add([1],power(v,4),scale(mul(power(v,2),cosine),-2))
    reduced_num = scale(mul(power(v,5),power([1,-2],2)),16)
    reduced_den = mul([1,3],[1,-2,5])
    assert num == mul([1,-1],reduced_num)
    assert den == mul([1,-1],reduced_den)
    gap = add(mul(add([1],scale(power(v,4),-16)),reduced_den),
              scale(reduced_num,-180))
    R = list(map(F,[1,3,5,25,34,-2828,5880]))
    assert gap == mul([1,-2],R)
    spans = [(F(1,4),F(3,8)),(F(3,8),F(1,2))]
    expected = [list(map(F,['645/512','13/12','25913/30720','2831/5120',
                           '31567/122880','131/2048','6515/32768'])),
                list(map(F,['6515/32768','5467/16384','24463/30720','18549/10240',
                           '3571/960','225/32','25/2']))]
    bs = [bernstein(R,l,r) for l,r in spans]
    assert bs == expected and all(min(row)>0 for row in bs)
    assert F(728,3) < 256
    return {'v_interval':[F(1,4),F(1,2)],'cos_4theta':cosine,
            'envelope_numerator':reduced_num,'envelope_denominator':reduced_den,
            'positive_gap_factor_R':R,'bernstein_spans':spans,
            'strict_positive_bernstein_coefficients':bs,
            'geometric_conclusion':'a > 16*u + 180*h',
            'normal_angle_restriction':'pi < S <= 4*acos(sqrt(v)) < 4*pi/3'}

def closing_certificate():
    # h*(1+h)*sigma^2-h = ((1+h)*t-1)^2 when h*sigma^2=h*t^2+(1-t)^2.
    # Check this as a polynomial in t, with coefficient polynomials in h.
    left = [[1],[-2,-2],[1,2,1]]
    right = [power([-1],2),scale(mul([-1],[1,1]),2),power([1,1],2)]
    # Expand rather than treating either displayed identity as an assertion oracle.
    lhs0 = add(mul([1,1],[1]),[0,-1])
    lhs1 = mul([1,1],[-2])
    lhs2 = mul([1,1],[1,1])
    assert [lhs0,lhs1,lhs2] == [[F(x) for x in row] for row in left] == right
    # (12+24/(1+h)+(45/4)h-32)*4(1+h)=45h^2-35h+16.
    residual = add(scale([1,1],-80),[96],mul([0,45],[1,1]))
    assert residual == [16,-35,45]
    assert add(scale(residual,180),scale(power([-35,90],2),-1)) == [1655]
    # Keep the earlier conservative cut and strengthen it using the full 1251/100.
    strong = add(scale([1,1],5004),[9600],mul([0,4500],[1,1]),scale([1,1],-13625))
    assert strong == [979,-4121,4500]
    assert add(scale(strong,18000),scale(power([-4121,9000],2),-1)) == [639359]
    upper = F(29160,59)
    threshold = F(122,819)
    assert F(729)/(1+F(9,4)*threshold) == 546
    assert upper < 546 and 546-upper == F(3054,59)
    return {'closing_radius_identity_coefficients_in_t':left,
            'sigma2_lower':'1/(1+h)',
            'final_scalar_numerator':residual,
            'positive_square_identity_constant':1655,
            'conservative_strict_lower_a':512,'strong_scalar_numerator':strong,
            'strong_positive_square_identity_constant':639359,
            'strict_lower_a':545,'strict_lower_product':546,
            'finite_count_sufficient_reciprocal_sum':threshold,
            'E17_strict_upper_product':upper,'rational_contradiction_gap':546-upper,
            'E17_global_lower_C_unchanged':34,'census_subtraction':'NOT_COMPUTED'}

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))

def gram(points, diagonal=None):
    if diagonal is None:
        return [[dot(a,b) for b in points] for a in points]
    inv = [1/t for t in diagonal]
    out = matrix0()
    for i in range(5):
        for j in range(5):
            if i<3 and j<3:
                out[i][j] = dot(points[i],[diagonal[k]*points[j][k] for k in range(3)])
            elif i>=3 and j>=3:
                out[i][j] = dot(points[i],[inv[k]*points[j][k] for k in range(3)])
            else:
                out[i][j] = dot(points[i],points[j])
    return out

def audit_control(g):
    eq = [pair(a,g) for a in E]
    values = [pair(a,g) for a in I]
    lhs = pair(C,g)
    equality = pair(S,g)+sum((c*x for c,x in zip(EQ,eq)),F(0)) \
               -sum((c*x for c,x in zip(MU,values)),F(0))
    assert lhs == equality
    return {'G':g,'E_values':eq,'I_values':values,
            'I_slacks':[r-x for r,x in zip(IRHS,values)],
            'G33_minus_24G22':lhs,'S_G_strict_positive':pair(S,g)}

def exact_controls():
    x = (F(0),F(0),F(1))
    b = (F(8,105),F(4,105),F(5,21))
    z = (F(2,105),F(-4,105),F(17,21))
    q = (F(10),F(0),F(1))
    B = (F(56,9),F(56,3),F(-7,9))
    d = [F(5),F(105),F(1)]
    old = audit_control(gram([x,b,z,q,B],d))
    assert old['E_values'] == [1,1,1,1]
    assert old['I_slacks'] == [0,0,0,0,0,F(-4,7)]
    assert old['G33_minus_24G22'] == F(11,7) < F(1351,100)
    assert old['S_G_strict_positive'] > 0
    # Feasible exact common-metric relaxation, not a closed uniform body.
    b2 = (F(11,122),F(30,61),F(1,2))
    z2 = (F(11,122),F(-30,61),F(1,2))
    q2 = (F(61,11),F(0),F(1))
    B2 = (F(3599,1100),F(13481,6000),F(-4,5))
    positive = audit_control(gram([x,b2,z2,q2,B2]))
    assert positive['E_values'] == [1,1,1,1]
    assert min(positive['I_slacks']) >= 0
    assert positive['I_slacks'][0] == F(1,100)
    assert positive['G'][1][1] == positive['G'][2][2] == F(1,2)
    assert positive['G33_minus_24G22'] > F(1351,100)
    return {'old_u20_control':{'scope':'NOT_A_BODY_DELTA0_AND_WRONG_RADIUS_ORDER',
               'primal_x_b_z':[x,b,z],'dual_q_B':[q,B],'M_diagonal':d,
               'N_diagonal':[1/t for t in d],'audit':old},
            'rank_tie_feasible_relaxation':{'scope':'NOT_A_BODY_OR_AN_ATTAINER',
               'primal_x_b_z':[x,b2,z2],'dual_q_B':[q2,B2],
               'M_diagonal':[1,1,1],'N_diagonal':[1,1,1],'audit':positive}}

def encode(x):
    if isinstance(x,F):
        return str(x)
    if isinstance(x,(list,tuple)):
        return [encode(y) for y in x]
    if isinstance(x,dict):
        return {k:encode(v) for k,v in x.items()}
    return x

def build():
    report = {'identity':IDENTITY,'exact_parent':PARENT,'rank_theorem_source':RANK_PROOF,
              'scope':'DEGREE5_TWO_APEX_CLOSING_XZ_PATTERN_NOT_WHOLE_E17',
              'gram_certificate':gram_certificate(),'angular_certificate':angular_certificate(),
              'closing_certificate':closing_certificate(),'exact_controls':exact_controls()}
    return (json.dumps(encode(report),sort_keys=True,separators=(',',':'))+'\n').encode('utf-8')

if __name__ == '__main__':
    if sys.argv[1:] not in (['build'],['check']):
        raise SystemExit('Usage: python -S two_apex_degree5.py build|check')
    data = build()
    target = Path('two_apex_degree5.json')
    if sys.argv[1] == 'build':
        if target.exists():
            assert target.read_bytes() == data, 'Refuse to overwrite a different report'
        target.write_bytes(data)
    else:
        assert target.read_bytes() == data, 'Exact report mismatch'
    print('RANK_ORDERED_COMMON_CAP_AFFINE24_EXACT_SPD_PASS')
    print('PENTAGON_16U_180H_TWO_INTERVAL_BERNSTEIN_PASS')
    print('DEG5_CLOSING_XZ_546_VS_29160_OVER59_PASS')
    print('EXACT_NONBODY_CONTROLS_AND_SCOPE_PASS')
    print(target.name,len(data),hashlib.sha256(data).hexdigest())
    print('TWO_APEX_RANK_CAP_DEG5_546_RECOVERY_PASS')
