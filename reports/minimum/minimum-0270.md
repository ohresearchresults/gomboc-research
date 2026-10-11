# minimum-0270

Historical AI scientific report · saved 2026-09-27 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# H5_UNCAPPED_PAIRED_PACKET_REALIZABILITY_V1

## Status

**No broader capped macro-region is established in this continuation.** The accepted 605-cell theorem remains the last completed computational exclusion checkpoint:

`minimum-0265`, SHA-256 `25188a07474082ebc6f8dd203e30be8b846af688ab2bc49e36ad2200f5ea5036`.

The substantive result below is a precisely scoped structural limitation of a possible simplification of the paired method. On the **entire Gamma-blind box**, the actual geometry admits a genuine SPD metric and its actual inverse satisfying a maximum-top spoke escape and a basal-polar escape simultaneously. This is not merely a feasible independently chosen pair or a singular limit. Consequently, the spectral/common-inverse three-facet constraints cannot be discarded from the 49-case method, even though W and A and the actual centroid are retained.

This does **not** show that the full capped three-facet relaxation fails anywhere outside the accepted macro-region. No such capped physical or relaxed survivor is promoted. It supplies an exact negative control against an uncapped simplification, together with a complete physical own222 family on the already identified literal H5 body.

### Reading and execution limitation

The retained consecutive-reading record for the new journal reaches character 360000. I requested the remaining tail through EOF, but the subsequent runtime calls did not leave inspectable returned contents in this continuation. I therefore cannot attest to a completed read of that tail or to a newly completed computational verification. The new journal's supplied identity is 374836 bytes, SHA-256 `ca1e1dcbcfd5af39075949f3b128316e918a2c2ecdf9f1e05821415996b9d2ad`.

The mathematical work below uses the literal H5 family, moments, incidence, W/A statements and accepted parent already present in this chat. The complete verification source is included, but its execution is **not claimed**. No output hash or regional completion marker is invented. This handoff is not a computational successor to the accepted 605-cell atlas.

## 1. A physical realizability theorem for the uncapped paired packet

Consider a full-dimensional uniformly filled two-layer body

    P = conv((B,0), (T,1)),
    T = conv((0,0),(lambda,0),(0,lambda)),

where B is a planar convex polygon in the nonnegative quadrant. Assume that x=0 and y=0 meet B, that y=0 is a true lateral support of P, and that the body's actual volume centroid is

    g=(c_x,c_y,gamma),    0<gamma<1/2.

Put h=1−gamma and B_x=max{x:(x,y)∈B}. Suppose

    B_x >= 2 lambda.

For the H5 incidence, a point attaining B_x can be chosen as basal vertex 1 or 2, and both are true neighbours of top vertex 8.

### Theorem

There is a genuine SPD metric M for which all of the following hold strictly:

1. Top vertex 8 is the unique maximum-norm top vertex.
2. A true spoke 8→b, with b∈{1,2}, has positive primal escape derivative.
3. The true basal-polar arrow q0→q1 has positive derivative under **N=M⁻¹**.

The metric can be constructed rationally whenever the body has rational coordinates. There is an explicit positive interval of full-rank metrics realizing these inequalities, not just an infinitesimal rank-one witness.

### Actual-centroid estimate

At height z, the horizontal section is

    (1−z)B+zT.

Its x-coordinate ranges from 0 to (1−z)B_x+z lambda. For a uniform planar convex body with x-range [0,L], its x-centroid is at most 2L/3. One direct proof is radial integration from a point on x=0: the radial variable has density 2t on [0,1], hence mean 2/3, and every far endpoint has x-coordinate at most L.

Averaging over the **actual section areas** therefore gives

    c_x <= (2/3)(h B_x+gamma lambda).                 (1)

No section masses have been chosen independently.

Define

    L = (c_x−gamma lambda/2)/h,
    U = c_x+gamma(B_x−lambda).

Then

    U−L = (gamma/h)[h B_x−c_x+(gamma−1/2)lambda].

Using (1) and B_x≥2 lambda,

    U−L >= gamma(1−2gamma)lambda/(6h) > 0.            (2)

Thus the following interval is genuinely nonempty.

### Explicit metric construction

Choose any beta_x∈(L,U), choose tau>0, and set

    beta=(beta_x,−tau),
    v=(beta−c)/gamma.

For epsilon>0 define

    G_epsilon=diag(1,epsilon),
    eta_epsilon=epsilon^2,

    M_epsilon = [[G_epsilon, G_epsilon v],
                 [v^T G_epsilon, v^T G_epsilon v+epsilon^2]].       (3)

Its exact inverse is

    N_epsilon = [[G_epsilon^−1+vv^T/epsilon^2, −v/epsilon^2],
                 [−v^T/epsilon^2,                 1/epsilon^2]].   (4)

In particular det(M_epsilon)=epsilon^3>0. Both matrices concern the original body's actual centroid. No polar centroid or auxiliary metric is reset.

Write

    alpha=(h beta_x−c_x)/gamma.

The first physical horizontal coordinates of the top vertices are alpha, alpha+lambda, alpha. Since beta_x>L,

    alpha>−lambda/2,
    (alpha+lambda)^2−alpha^2=lambda(2alpha+lambda)>0.                 (5)

The leading, epsilon-independent part of each top8 maximum comparison is therefore strictly positive.

Choose a genuine neighbour b of top8 with b_x=B_x. Its first horizontal coordinate is B_x−beta_x. The leading spoke derivative is

    (alpha+lambda)(B_x−beta_x−alpha−lambda)
      = (alpha+lambda)(U−beta_x)/gamma > 0.                         (6)

All remaining terms in these three comparisons are polynomials of degree at most two in epsilon. Equations (5)–(6) consequently persist on a positive interval.

The polar escape is even simpler. The actual poles are

    q0=−e3/gamma,    q1=−e2/c_y.

Substitution of the **same inverse (4)** gives the exact identity

    q0^T N_epsilon(q1−q0)
       = tau/(gamma^2 c_y epsilon^2) > 0.                          (7)

Thus the whole required local packet is strictly physically realized.

For deterministic rational recovery, take beta_x=(L+U)/2 and tau=1. Form the three degree-two polynomials in (5)–(6), including their remaining coefficients, as p_s(epsilon)=a_s0+a_s1 epsilon+a_s2 epsilon² with a_s0>0. A sufficient rational interval is

    0<epsilon<=min(1, min_s a_s0/[2(1+|a_s1|+|a_s2|)]).

This gives a complete reconstruction recipe at every rational input satisfying the hypotheses.

## 2. Application to the entire Gamma-blind box

The unchanged literal H5 body has s=1−lambda and raw vertices

    z0=(s/4,0,0),                 z1=(s(1−3x/4),0,0),
    z2=(s(1−p),sp,0),             z3=(sq,s(1−q),0),
    z4=(0,s(1−3r/4),0),           z5=(0,s/4,0),
    z6=(s/16,s/16,0),             z7=(0,0,1),
    z8=(lambda,0,1),              z9=(0,lambda,1).

Its outward maximal cycles are

    (6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8),
    (9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).

Apply the theorem on

    x,r,p∈[1/10,1/5], q∈[2/5,1/2], lambda∈[13/100,19/100].          (8)

The horizontal maximum is attained at basal vertex1 or2: vertex1 exceeds vertices0 and6 in x, vertex2 exceeds vertex3, and vertices4,5 have x=0. Moreover

    B_x >= z1_x >= (81/100)(17/20)=1377/2000 > 2 lambda.

The actual moments use

    A=(31−24xp−24rq)/64,
    D=lambda+2A(1−lambda)^2,
    K_z=A(1−lambda)^2/2+lambda/2+lambda²/4,
    gamma=K_z/D.

Throughout (8), A≥691/1600, and

    D−2K_z=A(1−lambda)^2−lambda²/2
       >=4244851/16000000>0.

Thus 0<gamma<1/2, and every body in (8) satisfies the physical realizability theorem. W and A also hold on (8), by the accepted reference-frontier result; they have not been weakened or replaced by an arbitrary origin.

**Consequence.** On every actual body in the Gamma-blind box, at least one of the two local cases

    (top8, spoke1, polar1),    (top8, spoke2, polar1)

has a strictly feasible common physical inverse pair when the spectral domain is omitted. A purported uncapped exclusion using only W/A, these paired arrows, and top maximality would therefore be false on the entire box.

This is a limitation of that **uncapped local packet**, not of complete U1/S1 requirements. It does not furnish a monounstable metric: W already supplies a basal U, and the other basal vertices have not been required to escape to it. Nor does (7) make the polar system monostable.

## 3. Exact own222 calibration family

A fixed control makes the distinction concrete, including all true-edge primitives and physical weak points.

Use the same actual body already appearing in the accepted macro parent,

    theta=(3/20,3/20,3/20,9/20,4/25),
    Vol=397961/3000000,
    g=(1369878641/6367376000,
       1294745471/6367376000,
       490761/1591844).

The body is not renamed. The **metric family is new** and is different from the parent's standard integer own446 metric.

Take

    beta=(7/20,−1/100),
    v_x=858702959/1963044000,
    v_y=−1358419231/1963044000,

and use (3)–(4) for

    0<epsilon<=1/1000.                                             (9)

For every epsilon in this interval, the complete physical census is

    strict S={1,5},
    strict U={1,4},
    strict H={(3,4),(6,7)},
    physical weak points=0,
    zero primitives=0 of 68.

Thus this is an actual **own222, weak000** family. Top8 is the unique top norm maximum; 8→1 and q0→q1 are both strictly positive. No singular endpoint epsilon=0 is included.

### Direct sign certificate

Let alpha=v_x−7/20. The first coordinates in the flag representation of M_epsilon are

    r0=−7/50,       r1=791/2000,    r2=91/250,
    r3=7/250,       r4=r5=−7/20,    r6=−119/400,
    r7=r9=alpha,    r8=alpha+4/25,

where

    87/1000<alpha<88/1000.

The second coordinates are y_i+1/100 on the base and y_i+v_y+1/100 on the top. Every absolute second coordinate is less than756/1000. Every nonzero leading primal derivative r_i(r_j−r_i), on a true directed edge, has absolute value greater than1/625. The remaining terms have absolute value at most

    (23/20)epsilon+(7/10)epsilon² < 1/625

on (9). The only zero leading pairs are the edges4–5 and7–9. Their first nonzero terms are respectively

    epsilon t4(t5−t4), epsilon t5(t4−t5),
    epsilon t7(4/25), epsilon t9(−4/25),

with signs negative, positive, negative, positive. Hence every primal sign is strict and fixed throughout (9).

For the polar signs put

    w_f=q_f,z−v_x q_f,x−v_y q_f,y.

The following rational bounds follow by substituting the literal centroid and support planes:

| f | Strict lower bound for w_f | Strict upper bound for w_f |
|---|---:|---:|
|0|−13/4|−81/25|
|1|−341/100|−339/100|
|2|−273/100|−27/10|
|3|107/100|109/100|
|4|22/5|443/100|
|5|473/100|119/25|
|6|203/100|41/20|
|7|57/100|3/5|
|8|36/25|73/50|

All |q_f,x| and |q_f,y| are less than5. For each true directed polar edge f→g,

    epsilon² q_f^T N_epsilon(q_g−q_f)
      =w_f(w_g−w_f)
       +epsilon q_f,y(q_g,y−q_f,y)
       +epsilon² q_f,x(q_g,x−q_f,x).

The absolute leading term is greater than2/5 on every such edge, whereas the two remaining terms have total absolute value less than

    50 epsilon+50 epsilon² <=1001/20000 <2/5.

Every polar sign is therefore strict and fixed as well. The minimum and maximum polar flag coordinates occur at facets1 and5, giving precisely S={1,5}. Combining the primal and polar signs on the seventeen genuine edges gives exactly H={(3,4),(6,7)}. No primitive zero can be mistaken for a physical weak contact here: there are no primitive zeros at all.

The support planes n_f·z≤h_f used in this calculation are, in the original facet numbering,

    ((0,0,−1),0),
    ((0,−1,0),0),
    ((−100,−300,−21),−21),
    ((2000,500,1171),1491),
    ((25,25,17),21),
    ((1500,2000,1171),1491),
    ((−1,0,0),0),
    ((−300,−100,−21),−21),
    ((0,0,1),1).

Together with the coordinates, centroid and metric formula, these are complete literal recovery data.

## 4. What the control says about the full three-facet domain

The accepted macro proof retains, for k=5 and its cell reference C,

    26C/31−CXC−Y >=0,
    5CXC+Y−30C/31 >=0,
    CXC+5Y−30C/31 >=0,

where

    X=M/tr(CM),
    Y=M⁻¹/tr(C⁻¹M⁻¹).

The control above is **not asserted to satisfy these three inequalities**. In fact the accepted parent, applied to case(8,1,1), implies that it violates at least one of them for every accepted cell reference whose cell contains this body. The actual escaping rows and both top maximum comparisons are strictly satisfied, so the contradiction must come from the retained reciprocal spectral domain.

This separates three different questions that should not be conflated:

- The uncapped local paired packet has a genuine physical solution, even throughout the Gamma-blind shape box.
- The accepted capped paired packet is infeasible on the605-cell macro-region.
- Feasibility or infeasibility of the full capped packet on the remaining shape domain is still undecided by this continuation.

In particular, the own222 control is not a counterexample to the accepted theorem and is not evidence that a failed capped numerical call is physically feasible. It does show that replacing spectral certification by an assertion that the actual local rows themselves are impossible would lose an essential premise.

## 5. Complete verification source for the fixed control

The source below is standard-library Python, with no external files or parent executable as inputs. It reconstructs the actual boundary volume centroid, recovers all maximal supports, checks the positive apex7 fan, proves the polynomial inverse identity, certifies every primitive on the whole interval (9), and computes the complete strict/weak census.

**Execution status: not observably executed in this continuation.** The sign proof above is analytic; the source is a reproducible finite verification unit, not a claimed completed run. No precomputed output byte count or SHA-256 is supplied. When run, the source reports those values for both itself and its full report.

Save as `h5_uncapped_pair_control.py` and run with assertions enabled:

    python -B -S h5_uncapped_pair_control.py

Expected terminal marker:

    H5_UNCAPPED_ACTUAL_PAIRED_222_FAMILY_PASS

```python
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import hashlib
import json

FACETS=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
        (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
Z=[(F(21,100),0,0),(F(1491,2000),0,0),
   (F(357,500),F(63,500),0),(F(189,500),F(231,500),0),
   (0,F(1491,2000),0),(0,F(21,100),0),
   (F(21,400),F(21,400),0),(0,0,1),(F(4,25),0,1),(0,F(4,25),1)]
Z=[list(map(F,z)) for z in Z]
PLANES=[((0,0,-1),0),((0,-1,0),0),((-100,-300,-21),-21),
        ((2000,500,1171),1491),((25,25,17),21),
        ((1500,2000,1171),1491),((-1,0,0),0),
        ((-300,-100,-21),-21),((0,0,1),1)]
PLANES=[(list(map(F,n)),F(h)) for n,h in PLANES]
E=F(1,1000)

def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def sub(a,b): return [x-y for x,y in zip(a,b)]
def cross(a,b):
    return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0]]
def outer(a,b): return [[x*y for y in b] for x in a]
def zero(): return [[F(0) for j in range(3)] for i in range(3)]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(3)] for i in range(3)]
def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(3)),F(0))
             for j in range(3)] for i in range(3)]
def bil(x,A,y): return sum((x[i]*A[i][j]*y[j]
                            for i in range(3) for j in range(3)),F(0))

def moments(apex=None):
    o=[F(0)]*3 if apex is None else Z[apex]
    D=F(0);K=[F(0)]*3;cells=[]
    for f in FACETS:
        if apex is not None and apex in f: continue
        for j in range(1,len(f)-1):
            a,b,c=[Z[k] for k in (f[0],f[j],f[j+1])]
            d=dot(sub(a,o),cross(sub(b,o),sub(c,o)))
            if apex is not None:
                assert d>0
                cells.append((apex,f[0],f[j],f[j+1],d))
            D+=d
            for k in range(3):K[k]+=d*(o[k]+a[k]+b[k]+c[k])/4
    return D,K,cells

def interval_sign(poly):
    # Dividing by a positive power of epsilon is valid on (0,E].
    p=list(poly);order=0
    while p and p[0]==0:p.pop(0);order+=1
    assert p
    while len(p)>1 and p[-1]==0:p.pop()
    n=len(p)-1
    b=[sum((p[j]*E**j*F(comb(i,j),comb(n,j))
            for j in range(i+1)),F(0)) for i in range(n+1)]
    if min(b)>0:return 1,order,b
    assert max(b)<0
    return -1,order,b

def enc(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [enc(v) for v in x]
    return x

def main():
    assert __debug__
    D,K,_=moments();D2,K2,cells=moments(7)
    assert D==D2 and K==K2 and len(cells)==9
    assert D/6==F(397961,3000000)
    g=[k/D for k in K]
    assert g==[F(1369878641,6367376000),F(1294745471,6367376000),
               F(490761,1591844)]
    X=[sub(z,g) for z in Z]
    poles=[]
    for f,(n,h) in zip(FACETS,PLANES):
        sl=[h-dot(n,z) for z in Z]
        assert all(sl[i]==0 if i in f else sl[i]>0 for i in range(10))
        for j in range(len(f)):
            a,b,c=[Z[f[(j+k)%len(f)]] for k in range(3)]
            assert dot(n,cross(sub(b,a),sub(c,b)))>0
        H=h-dot(n,g);assert H>0
        poles.append([x/H for x in n])
    hull=set()
    for i,j,k in combinations(range(10),3):
        n=cross(sub(Z[j],Z[i]),sub(Z[k],Z[i]))
        if not any(n):continue
        vals=[dot(n,sub(z,Z[i])) for z in Z]
        if min(vals)>=0 or max(vals)<=0:
            hull.add(tuple(t for t,v in enumerate(vals) if v==0))
    assert hull=={tuple(sorted(f)) for f in FACETS}
    for i in range(10):
        ns=[PLANES[f][0] for f in range(9) if i in FACETS[f]]
        assert any(dot(a,cross(b,c))!=0 for a,b,c in combinations(ns,3))
    edges=sorted({tuple(sorted((f[j],f[(j+1)%len(f)])))
                  for f in FACETS for j in range(len(f))})
    ef=[tuple(k for k,f in enumerate(FACETS) if i in f and j in f)
        for i,j in edges]
    assert len(edges)==17 and all(len(f)==2 for f in ef)
    gamma=g[2];h=1-gamma;beta=[F(7,20),F(-1,100)]
    vx=(beta[0]-g[0])/gamma;vy=(beta[1]-g[1])/gamma
    assert vx==F(858702959,1963044000)
    assert vy==F(-1358419231,1963044000)
    u=[F(1),F(0),vx];v=[F(0),F(1),vy];e3=[F(0),F(0),F(1)]
    w=[vx,vy,F(-1)];e2=[F(0),F(1),F(0)];e1=[F(1),F(0),F(0)]
    MC=[outer(a,a) for a in (u,v,e3)]
    NC=[outer(a,a) for a in (w,e2,e1)]
    # NC is epsilon^2 N. Prove M NC=epsilon^2 I as a polynomial identity.
    product=[zero() for k in range(5)]
    for i in range(3):
        for j in range(3):product[i+j]=add(product[i+j],mm(MC[i],NC[j]))
    I=[[F(i==j) for j in range(3)] for i in range(3)]
    assert product==[zero(),zero(),I,zero(),zero()]
    P={};Q={};proofs=[]
    for (i,j),(a,b) in zip(edges,ef):
        for i0,j0 in ((i,j),(j,i)):
            p=[bil(X[i0],A,sub(X[j0],X[i0])) for A in MC]
            sg,order,co=interval_sign(p);P[i0,j0]=sg
            proofs.append(('P',i0,j0,p,order,co))
        for a0,b0 in ((a,b),(b,a)):
            p=[bil(poles[a0],A,sub(poles[b0],poles[a0])) for A in NC]
            sg,order,co=interval_sign(p);Q[a0,b0]=sg
            proofs.append(('Q_scaled_by_epsilon_squared',a0,b0,p,order,co))
    assert len(P)==len(Q)==34
    U=[i for i in range(10) if all(s<0 for (a,b),s in P.items() if a==i)]
    S=[i for i in range(9) if all(s<0 for (a,b),s in Q.items() if a==i)]
    saddles=[(i,j) for (i,j),(a,b) in zip(edges,ef)
             if max(P[i,j],P[j,i],Q[a,b],Q[b,a])<0]
    assert U==[1,4] and S==[1,5] and saddles==[(3,4),(6,7)]
    assert P[8,1]>0 and Q[0,1]>0
    for j in (7,9):
        p=[bil(X[8],A,X[8])-bil(X[j],A,X[j]) for A in MC]
        assert interval_sign(p)[0]>0
    # Actual W and A, independently of the physical metric.
    for i in range(7):
        for j in (7,8,9):
            r=[2*g[k]-(1-2*gamma)*Z[i][k]-2*gamma*Z[j][k]
               for k in range(2)]+[F(0)]
            assert all(dot(n,r)<b for n,b in PLANES[1:8])
    assert all(dot(q,X[j])>-1 for q in poles[1:] for j in (7,8,9))
    report={'identity':'H5_UNCAPPED_ACTUAL_PAIRED_222_FAMILY_V1',
      'scope':'Uncapped physical local packet. Not a capped survivor or110.',
      'epsilon_interval_open_at_zero':[0,E],'vertices':Z,'facets':FACETS,
      'edges':edges,'edge_facets':ef,'planes':PLANES,'volume':D/6,
      'actual_centroid':g,'positive_apex_fan':cells,'poles':poles,
      'beta':beta,'shear':[vx,vy],
      'M_coefficients_ascending':MC,
      'epsilon_squared_N_coefficients_ascending':NC,
      'strict_S':S,'strict_U':U,'strict_H':saddles,
      'physical_weak_points':0,'zero_primitives':0,
      'top_maximum':8,'positive_paired_arrows':[[8,1],[0,1]],
      'all_68_polynomial_sign_certificates':proofs}
    raw=(json.dumps(enc(report),sort_keys=True,indent=2)+'\n').encode()
    Path('h5_uncapped_pair_control.json').write_bytes(raw)
    source=Path(__file__).read_bytes()
    print('SOURCE',len(source),hashlib.sha256(source).hexdigest())
    print('REPORT',len(raw),hashlib.sha256(raw).hexdigest())
    print('STRICT_SUH',len(S),len(U),len(saddles),'WEAK',0,'ZEROS',0)
    print('H5_UNCAPPED_ACTUAL_PAIRED_222_FAMILY_PASS')

if __name__=='__main__':main()
```

## 6. Remaining task

The unclosed target is still the remainder of the Gamma-blind/W/A shape domain under **all three** reciprocal constraints with valid whole-domain reference bounds. This continuation provides neither a completed additional cell partition nor an exact feasible capped case there.

The constructive theorem supplies an adversarial calibration for further methods: on every thin-top shape satisfying its hypotheses, an uncapped physical pair can satisfy the genuine local paired obligations. Any successful larger exclusion must retain the independently justified spectral restrictions, add further genuine U1/S1 obligations, or use another actual-body identity. The exact own222 family distinguishes that requirement from numerical failure, false centring, independently selected polar metrics, and singular feasibility.

The accepted global bracket34≤C_min≤622, the605-cell joint exclusion and its reflection remain unchanged.
