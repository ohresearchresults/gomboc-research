# material-174925c56ee0

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# VF_PAIRED_EXITS_AND_PHYSICAL_CONTACT_SELECTORS_V1

Coordinator analytic theorem and complete exact supplementary controls. This sharpens, without invalidating, the 4^nVF selector bound in [internal-source-reference]. The global radial-index theorem and reduction to weak vertex/facet exit groups are used only in the global application; the exact incidence identity below is independent and holds at every genuine vertex-facet incidence. The full mechanical stress/second-jet framework is the fully read immutable result minimum-0227, SHA256 57bf2cc803fdd3e5ace5587e000d4b1b6372f42306aaff28e467e2b94f1ca8db. No new full-shape escape, density, E17 feasibility or exclusion is asserted. Bounds34<=C_min<=622 remain unchanged.

## 1. Exact true-incidence identity

Let P be a genuine full-dimensional convex3-polytope, with an interior reference point translated to0, physical metric M positive definite, N=M^-1, and normalized true maximal facet poles q_f satisfying q_f.x<=1. Homogeneity is not needed for the identity; in applications all coordinates are at the ACTUAL uniform volume centroid.

Take a true incidence vertex v in facet f. Let e1=Xi-v and e2=Xj-v be the TWO boundary edges of the true polygon f issuing from v. Let g1 be the other facet at edge[v,Xi] and g2 the other facet at[v,Xj]. Define

c=q_f^T N q_f>0,   y=N q_f/c,
v-y=z1 e1+z2 e2,
G_ab=e_a^T M e_b,
alpha=-q_g1.e2>0,   beta=-q_g2.e1>0.

The vector y is the metric perpendicular foot of0 on the plane of f, so q_f.y=1 and y^T M e_a=0. The two true boundary edges are linearly independent, hence G is positive definite and z is unique. Alpha,beta are strictly positive because g1 and f meet exactly in the line of their true edge, whereas the other edge direction lies strictly inward of g1; likewise for g2. This does not assume v is simple.

For the FOUR true directed primitives

p1=v^T M e1,  p2=v^T M e2,
q1=q_f^T N(q_g1-q_f),  q2=q_f^T N(q_g2-q_f),

one has the exact equations

       (p1,p2)^T=G(z1,z2)^T,
       q1=c alpha z2,      q2=c beta z1.                (1)

Proof: the first relation follows from y^T M e_a=0. Since q_g1.v=1,
q1=c q_g1.(y-v)=-c q_g1.(z1e1+z2e2)=c alpha z2.
The second polar row is identical with labels reversed. All poles and both metrics in(1) are from the SAME physical realization. No independent primal/polar metric relaxation is used.

## 2. Four nominal selectors reduce to two crossed pairs

At EVERY true incidence above, not merely to first order,

[max(p1,p2)>0 AND max(q1,q2)>0]
   iff [(p1>0 AND q2>0) OR (p2>0 AND q1>0)].             (2)

The reverse implication is immediate. For the forward implication max(q)>0 is max(z)>0 by(1). Suppose both maxima are positive but neither matched pair(p1,z1),(p2,z2) is positive. After interchanging labels z1>0 and p1<=0. The positive p must then be p2, whence z2<=0. Thus z^T G z=z1p1+z2p2<=0, contradicting G positive definite and z1>0. This proves(2).

The pairing is CROSSED with respect to physical edge labels: primal exit along the first edge is paired with dual exit across the second edge, and conversely. One cannot generally demand primal and polar exits at the SAME edge. Nor is it necessary to retain all four primal-times-dual combinations.

## 3. Physical VF contacts and global packet bound

At a physical weak vertex-facet contact v=y and all four primitives in(1) vanish. All other outgoing true rows at its weak vertex and weak stable facet are strictly negative. In a sufficiently small true-lattice neighborhood protect all originally nonzero signs. Eliminating that VF as both a vertex and facet equilibrium is exactly the left side of(2), hence exactly one of its two crossed positive pairs.

Combine with [internal-source-reference]: resolving every weak vertex/facet group with protected nonzero signs retains all original strict S,U labels, removes every physical weak VE/EF/VF, and preserves strict H by S+U-H=2. Weak-edge groups are redundant. VE and EF each have one forced exit; each VF now offers only TWO paired alternatives. A packet with nVE,nEF,nVF distinct physical weak points therefore needs at most2^nVF selectors.

Each selector retains m=nVE+nEF+2nVF original TRUE row inequalities; contact mechanics is not replaced by synthetic rows. Physical counting gives nVE+nVF<=V-U and nEF+nVF<=F-S. At V10,F9,S1,U1, m<=17 and nVF<=8, so at most256 exact nonlinear selectors suffice, upgrading the previous valid loose65536 bound. This is NOT a bound on arbitrary harmless algebraic zero rows.

The parent's full surface-moment Gordan stress criterion and all-stress-cone second-jet test apply unchanged to these paired selectors. Actual centroid derivatives, incidence reactions and common-inverse second derivative remain required.

## 4. Angle-dependent refinement and its higher-order limit

Equation(1) gives exactly

p1=G11 q2/(c beta)+G12 q1/(c alpha),
p2=G12 q2/(c beta)+G22 q1/(c alpha).                    (3)

If G12>=0, max(p)>0 implies max(q)>0, because if both q<=0 both p<=0. Thus for an acute physical facet angle the PRIMAL exit group alone suffices. If G12<=0, G^-1 has nonnegative entries, so max(q)>0, equivalently max(z)>0, implies max(p)>0. Thus for an obtuse angle the POLAR exit group alone suffices. At a strictly acute or strictly obtuse base VF, the angle sign persists in a neighborhood; these are exact one-group local reductions.

At a right-angle base G12=0 all four rows vanish and their first derivatives obey

dp1=G11 dq2/(c beta),   dp2=G22 dq1/(c alpha).          (4)

Consequently STRICT FIRST-ORDER escape needs only one two-choice group per VF even at a right angle. First-order selectors have m'=nVE+nEF+nVF<=17-nVF rows in the E17 jointS1U1 setting, with at most2^nVF selectors.

Do NOT extend a fixed primal-only or polar-only exact rule across an angle-changing path from a right-angle source. Writing p1=k1q2+k12q1, with k12=0 at the base, gives
p1''=k1q2''+2k1'q2'+2k12'q1'.
Terms omitted here multiply the base q1=q2=0. When the selected matched row q2'=0, the cross term2k12'q1' can still survive. General higher-order escape at a right-angle source must retain the exact two-row paired selector, or explicitly stratify by the new angle sign. Neither the smaller row count nor the pairing proves independence, absence of positive stresses or density.

## 5. Complete actual-body control capsule

The standard-library source below checks(1),(2),both angle implications,genuine support/incidence,actual uniform centroid and strict S+U-H=2 on140 rational tetrahedron/metric pairs, encompassing1680 true vertex-facet incidences. Obtuse/right/acute totals348/50/1282. These actual homogeneous controls are NOT E17 or S1U1 candidates and do not substitute for the analytic proof.

All exact inputs are literal in source:t in{-2,-1,-1/3,0,1/3,1,2},epsilon in{-17,-3,0,3,17}/1000; vertices a=(1,epsilon,2epsilon),b=(1,1,epsilon),c=(1+epsilon,t-epsilon,1),d=-a-b-c;four explicit SPD metrics. Uniform tetrahedral COM exactly0. No seed,external input,tolerance or nonstandard package.

Save as vf_paired_exits.py,UTF-8 LF with terminal newline. Python3.13.5 observed;Python3.11+ standard library sufficient.
Reconstruction: python -B vf_paired_exits.py build
Verification: python -B vf_paired_exits.py check
Expected marker: VF_PAIRED_EXITS_ACTUAL_CONTROLS_PASS 140 1680 [348, 50, 1282]
Source vf_paired_exits.py:6441 bytes,SHA256 9717677b7333fe919bbd3d04539ced70c5f41b194b1d115bb37b5f3a7ddc54c3.
Output vf_paired_exits_report.json:102508 bytes,SHA256 7f935d5eab00fba62b50550f1d1889a65833e5f9e90e72b5ef7efdaeb02a9bb3.
Coordinator observed build and separate check PASS before storage. Literal code and inputs,not hashes alone,are the recovery capsule.

```python
"""VF_PAIRED_EXITS_ACTUAL_CONTROLS_V1; Python3.11+, standard library.
Commands: python -B vf_paired_exits.py build ; python -B vf_paired_exits.py check
The universal claim has a separate analytic proof; these are exact actual controls.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib, json, sys

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(t,a):return tuple(t*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def mv(A,x):return tuple(dot(row,x) for row in A)
def inv(A):
    d=det(*A);assert d>0
    cols=[scale(1/d,cross(A[1],A[2])),scale(1/d,cross(A[2],A[0])),scale(1/d,cross(A[0],A[1]))]
    return tuple(tuple(cols[j][i] for j in range(3)) for i in range(3))
def mat(A):return tuple(tuple(map(F,r)) for r in A)
def sgn(x):return (x>0)-(x<0)

def control(t,eps,M):
    a=(F(1),eps,2*eps);b=(F(1),F(1),eps);c=(1+eps,t-eps,F(1))
    d=scale(-1,add(add(a,b),c));X=[a,b,c,d]
    assert all(sum(x[k] for x in X)==0 for k in range(3))
    vol=abs(det(sub(b,a),sub(c,a),sub(d,a)))/6;assert vol>0
    assert M[0][0]>0 and M[0][0]*M[1][1]-M[0][1]**2>0
    N=inv(M)
    assert all(sum(M[i][k]*N[k][j] for k in range(3))==(i==j) for i in range(3) for j in range(3))
    faces=list(combinations(range(4),3));Q=[]
    for face in faces:
        x,y,z=[X[i] for i in face]
        n=cross(sub(y,x),sub(z,x));h=dot(n,x);assert h!=0
        q=scale(1/h,n)
        assert [i for i in range(4) if dot(q,X[i])==1]==list(face)
        assert all(dot(q,x)<=1 for x in X)
        Q.append(q)
    P=[[dot(x,mv(M,sub(y,x))) for y in X] for x in X]
    R=[[dot(q,mv(N,sub(r,q))) for r in Q] for q in Q]
    U=[i for i in range(4) if max(P[i][j] for j in range(4) if j!=i)<0]
    S=[f for f in range(4) if max(R[f][g] for g in range(4) if g!=f)<0]
    H=[];weak_e=[]
    for i,j in combinations(range(4),2):
        f,g=[f for f,face in enumerate(faces) if i in face and j in face]
        z=max(P[i][j],P[j][i],R[f][g],R[g][f])
        if z<0:H.append([i,j])
        if z==0:weak_e.append([i,j])
    assert len(S)+len(U)-len(H)==2
    angle_counts=[0,0,0]; paired=0;detail=None
    for f,face in enumerate(faces):
        for v in face:
            i,j=[i for i in face if i!=v]
            g1=next(g for g,fc in enumerate(faces) if g!=f and v in fc and i in fc)
            g2=next(g for g,fc in enumerate(faces) if g!=f and v in fc and j in fc)
            e1=sub(X[i],X[v]);e2=sub(X[j],X[v])
            cc=dot(Q[f],mv(N,Q[f]));assert cc>0
            y=scale(1/cc,mv(N,Q[f]));w=sub(X[v],y)
            B11=dot(e1,e1);B12=dot(e1,e2);B22=dot(e2,e2);DB=B11*B22-B12**2
            z1=(B22*dot(e1,w)-B12*dot(e2,w))/DB
            z2=(B11*dot(e2,w)-B12*dot(e1,w))/DB
            assert add(scale(z1,e1),scale(z2,e2))==w
            alpha=-dot(Q[g1],e2);beta=-dot(Q[g2],e1);assert alpha>0 and beta>0
            G11=dot(e1,mv(M,e1));G12=dot(e1,mv(M,e2));G22=dot(e2,mv(M,e2))
            assert G11*G22-G12**2>0
            p1=P[v][i];p2=P[v][j];q1=R[f][g1];q2=R[f][g2]
            assert p1==G11*z1+G12*z2 and p2==G12*z1+G22*z2
            assert q1==cc*alpha*z2 and q2==cc*beta*z1
            assert max(p1,p2)<=0 or max(q1,q2)<=0 or ((p1>0 and q2>0) or (p2>0 and q1>0))
            lhs=max(p1,p2)>0 and max(q1,q2)>0
            rhs=(p1>0 and q2>0) or (p2>0 and q1>0)
            assert lhs==rhs
            if G12>=0:assert max(p1,p2)<=0 or max(q1,q2)>0
            if G12<=0:assert max(q1,q2)<=0 or max(p1,p2)>0
            angle_counts[sgn(G12)+1]+=1;paired+=int(rhs)
            if f==0 and v==0:detail={'rows':[str(x) for x in (p1,p2,q1,q2)],'gram':[str(x) for x in (G11,G12,G22)],'paired_escape':rhs}
    return {'t':str(t),'epsilon':str(eps),'volume':str(vol),'strict_counts':[len(S),len(U),len(H)],'weak_edges':weak_e,'obtuse_right_acute':angle_counts,'paired_escape_incidents':paired,'vertex0_facet012':detail}

def main():
    if len(sys.argv)!=2 or sys.argv[1] not in ('build','check'):raise SystemExit('usage: python -B vf_paired_exits.py build|check')
    metrics=[mat(a) for a in ([[1,0,0],[0,1,0],[0,0,1]],[[2,0,0],[0,3,0],[0,0,5]],[[2,0,0],[0,3,1],[0,1,2]],[[4,1,-1],[1,3,1],[-1,1,3]])]
    records=[]
    for mi,M in enumerate(metrics):
        for t in map(F,('-2','-1','-1/3','0','1/3','1','2')):
            for n in (-17,-3,0,3,17):
                r=control(t,F(n,1000),M);r['metric_id']=mi;records.append(r)
    assert len(records)==140
    totals=[sum(r['obtuse_right_acute'][i] for r in records) for i in range(3)]
    assert all(totals) and sum(totals)==1680
    result={'version':1,'metrics':[[[str(x) for x in row] for row in M] for M in metrics],'actual_tetrahedra':140,'vertex_facet_incidents':1680,'angle_totals_obtuse_right_acute':totals,'cases':records}
    out=(json.dumps(result,sort_keys=True,indent=2)+'\n').encode();p=Path('vf_paired_exits_report.json')
    if sys.argv[1]=='build':p.write_bytes(out)
    else:assert p.read_bytes()==out
    print('VF_PAIRED_EXITS_ACTUAL_CONTROLS_PASS',140,1680,totals)
    for p in (Path(__file__),p):
        b=p.read_bytes();print(p.name,len(b),hashlib.sha256(b).hexdigest())
if __name__=='__main__':main()
```
