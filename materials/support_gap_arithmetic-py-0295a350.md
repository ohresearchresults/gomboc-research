# material-0295a3503734

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Exact finite algebra for MONOUNSTABLE_FIRST_LAYER_SUPPORT_GAP_V1.
The geometric equality theorem and the accepted nine-vertex PSD obstruction
are analytic inputs, not assertions proved by this arithmetic control.
Python >=3.9 standard library; assertions must remain enabled.
Run: python -B -S support_gap_arithmetic.py > support_gap_report.txt
"""
from fractions import Fraction as F
from itertools import combinations
import hashlib
import json
from pathlib import Path
assert __debug__

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))

def control(vertices,faces):
    y=[tuple(map(F,p)) for p in vertices]
    triangles=[(face[0],face[j],face[j+1]) for face in faces for j in range(1,len(face)-1)]
    edge_boundary={}
    D=F(0); J=[F(0)]*3; L=[[F(0)]*3 for _ in range(3)]
    for ia,ib,ic in triangles:
        a,b,c=y[ia],y[ib],y[ic]
        assert all(det(sub(b,a),sub(c,a),sub(p,a))<=0 for p in y)
        for i,j in ((ia,ib),(ib,ic),(ic,ia)):
            key=tuple(sorted((i,j))); edge_boundary[key]=edge_boundary.get(key,0)+(1 if i<j else -1)
        d=det(a,b,c); s=add(add(a,b),c); D+=d
        for i in range(3):
            J[i]+=d*s[i]
            for j in range(3):L[i][j]+=d*(s[i]*s[j]+a[i]*a[j]+b[i]*b[j]+c[i]*c[j])
    assert all(v==0 for v in edge_boundary.values()) and D>0
    g=tuple(x/(4*D) for x in J)
    Sigma=[[L[i][j]/(20*D)-g[i]*g[j] for j in range(3)] for i in range(3)]
    u=(F(0),F(0),F(1)); vals=[dot(u,sub(p,g)) for p in y]
    h=max(vals); b=-min(vals); variance=sum(u[i]*Sigma[i][j]*u[j] for i in range(3) for j in range(3))
    alpha=4*D*h; beta=4*D*b
    Q=32*D*sum(u[i]*L[i][j]*u[j] for i in range(3) for j in range(3))-40*dot(u,J)**2-3*alpha**2+2*alpha*beta-3*beta**2
    delta=40*variance-3*h*h+2*h*b-3*b*b
    assert Q==16*D*D*delta
    # Strict negativity toward every other vertex is stronger than the
    # true-edge condition, and verifies these controls are not U=1.
    strict_u=[i for i,p in enumerate(y) if all(dot(sub(p,g),sub(q,p))<0 for j,q in enumerate(y) if j!=i)]
    return {'D':str(D),'g':list(map(str,g)),'variance':str(variance),
            'h':str(h),'b':str(b),'Q':str(Q),'defect':str(delta),'strict_U':len(strict_u)}

Dnorm=16*6; Jnorm=3*Dnorm; Lnorm=12*Dnorm
uLu=9*Lnorm; uJ=3*Jnorm; alpha=4*Dnorm*3+uJ
Qnorm=32*Dnorm*uLu+40*uJ*uJ+8*alpha*alpha
primalnorm=9*(4*Dnorm+Jnorm)*3*2
constraints=36+420+160+16+1+7+9+1+20
assert (Dnorm,Jnorm,Lnorm,uLu,uJ,alpha,Qnorm)==(96,288,1152,10368,864,2016,94224384)
assert max(Qnorm,primalnorm,6*3**3,2*26+2*700)<2**27
assert constraints==670<700
assert 10**3<2**10
assert F(4)-F(26,2)+27+F(26*10,3)==F(314,3)<105
exponent_cap=105*26*20**26
assert exponent_cap==18320719872000000000000000000000000000<2**124
assert 16*96**2*3==442368<2**19

tetra=control([(0,0,0),(1,0,0),(0,1,0),(0,0,1)],[(1,2,3),(0,3,2),(0,1,3),(0,2,1)])
cube=control([(0,0,0),(1,0,0),(1,1,0),(0,1,0),(0,0,1),(1,0,1),(1,1,1),(0,1,1)],
             [(3,2,1,0),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)])
assert tetra['Q']=='0' and tetra['variance']=='3/80' and tetra['strict_U']==4
assert cube['Q']=='1344' and cube['defect']=='7/3' and cube['strict_U']==8
report={'identity':'MONOUNSTABLE_FIRST_LAYER_SUPPORT_GAP_V1','variables':26,'degree':10,
        'coefficient_height':2**27,'constraint_count_bound':700,'Q_l1_bound':Qnorm,
        'primal_row_l1_bound':primalnorm,'JPT_log_base_bound':105,'JPT_log_exponent_cap':str(exponent_cap),
        'Q_lower_bound':'2^(-2^124)','relative_gap':'2^(-(2^124+19))',
        'scope':'Actual homogeneous V=10,F<=9 admitting a nonzero-PSD rooted weak tree; includes every U=1 SPD body.',
        'all_E17_excluded':False,'actual_110_attainer_found':False,'tetrahedron_equality_control':tetra,'cube_control':cube}
data=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode()
Path('support_gap_report.json').write_bytes(data)
print('SIGNED_BOUNDARY_SECOND_MOMENT_IDENTITY_PASS')
print('EQUALITY_CONTROL_HAS_U4_NOT_U1')
print('JPT_COEFFICIENT_AND_EXPONENT_BOUNDS_PASS')
print('support_gap_report.json',len(data),hashlib.sha256(data).hexdigest())
print('MONOUNSTABLE_FIRST_LAYER_SUPPORT_GAP_FINITE_ALGEBRA_PASS')
