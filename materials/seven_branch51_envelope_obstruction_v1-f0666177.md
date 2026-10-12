# material-f0666177195a

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# SEVEN_CORNER_5_PLUS_1_ENVELOPE_OBSTRUCTION_V1

## Theorem and scientific consequence
There is NO convex planar seven-corner polygon Q with0 in its interior, -Q/3 contained in Q, and a weak rooted boundary tree whose two branches have lengths5and1. The proof includes all zero selected-arrow walls and does not impose equal turns, tight radial steps, a uniform-area centroid, or actual3D realization.

More strongly, only the two containment tests -A/3 in Q and -B/3 in Q are needed, where A is the root and B the first vertex of its length5 branch. Four subsequent vertices are replaced by a single convex reachable envelope. A complete exact two-dimensional rational certificate has just26 closed leaves,51 binary-tree nodes,and maximum depth10. Two leaves close by a norm bound and24 by support separation. This is a finite interval proof over the ENTIRE parameter rectangle,not sampled numerical infeasibility.

Together with the prior3+3 root-axis obstruction and coordinator4+2 theorem [internal-source-reference],the only remaining seven-corner rooted-boundary form is6+0: the root is an endpoint of a six-step chain. That form is NOT excluded here. Thus the global seven-corner shadow question is not yet settled. The planar minimum remains7or8; the actual homogeneous3D complexity interval remains34<=Cmin<=622. There is no new actual3D body, U1 witness, proper110 attainer, wholeC34 exclusion, or canonical-count subtraction.

## Exact source relationship
The fully read immutable result minimum-0209,SHAadebd2f62354466c4f5cdadbb45aec998631c8d8854876b6c92411d83403ff1c,establishes the<=6corner theorem, -P/3 containment for actual uniformly filled centred3D polytopes,and transport through closed exposed true fibres. The current argument is a new planar theorem and reproves every chain estimate it uses. The previous exact equal-turn5+1 family [internal-source-reference] is only an ansatz extremum below1/3; no reduction to that ansatz is assumed. The present all-shape5+1 obstruction supersedes its former global-gap status,not its literal coordinates or lower-coefficient controls.

## 1. Geometry and the first descendant
Normalize A=(1,0) by a Euclidean similarity. Orient the long branch counterclockwise and write its vertices A,B,V2,V3,V4,V5. The short branch has vertex C below the x-axis. All selected arrows point toward A and satisfy

    vi dot(vparent-vi)>=0.

Since0 is interior and these are true corners,every consecutive angular increment along a chosen weak arrow is strictly between0 andpi/2. In particular

    B=(bx,by), bx>0,by>0, |B|^2<=bx;
    C=(cx,-d), cx>0,d>0, cx^2+d^2<=cx.

Along a nonzero weak arrow norms grow strictly toward A. Since -A/3 belongs to Q,some vertex has x<=-1/3. It is not A or C,and is therefore on the long branch. Thus

    |B|>=1/3.                                           (1.1)

Let

    s=by/bx,
    w=|B|^2/bx.

Then

    B=(w/(1+s^2),s*w/(1+s^2)),
    0<w<=1,
    9w^2>=1+s^2,
    0<=s<=sqrt(8)<3.                                    (1.2)

We will cover the larger closed range s in[0,3],retaining the necessary norm inequality.

## 2. The convex four-step envelope,without fictitious vertices
For any j<=4 descendants after B,let theta be their cumulative positive angular displacement from B. Their radius is at most

    |B| product_(i=1)^j cos(delta_i)
      <=|B|cos^4(theta/4).                               (2.1)

The last inequality follows by adding4-j ZERO terms solely in the scalar Jensen inequality for log cos. No zero edge or extra corner is inserted into Q. The actual cumulative angle lies in(0,2pi).

Let K4(B) be the closed convex hull of0,B and the radial region described by the right side of(2.1) for0<=theta<=2pi. Then B,V2,V3,V4,V5 belong to K4(B).

Enlarge C radially to the boundary of the disk with diameter[0,A]. This cannot shrink conv(A,C,K4(B)),because0 belongs to K4(B). Write the enlarged point as

    C'=(cos^2 psi,-cos psi sin psi), 0<=psi<=pi/2.

Set z=tan(psi/2),so0<=z<=1 and

    c(z)=(1-z^2)^2/(1+z^2)^2,
    d(z)=2z(1-z^2)/(1+z^2)^2,
    C'=(c(z),-d(z)).                                    (2.2)

We henceforth use C' in the relaxation. The original polygon is contained in

    H=conv(A,C',K4(B)).

Therefore -A/3 and -B/3 must both belong to H. No other negative vertex containment is needed in this proof. Radial enlargement changes only a containing relaxation; it is not asserted to preserve an actual polygon or its centroid.

## 3. A rational family of exact envelope support bounds
For t>0 put

    f(t)=1-10t^2+5t^4,
    g(t)=5t-10t^3+t^5,
    F_t(B)=(bx*f-by*g,by*f+bx*g).                         (3.1)

The complex form is F_t(B)=B(1+it)^5. We use ONLY the rational parameters

    t=k/100, k=35,...,73, and k=75.                       (3.2)

For every such t,f(t)<0 and0<t<1. Put alpha=arctan(t) and phi=5alpha. These facts imply pi/2<phi<3pi/2. For a point in the radial region(2.1),

    F_t(B) dot X
      <=|B|^2(1+t^2)^(5/2)cos(theta-phi)cos^4(theta/4)

when cos(theta-phi)>0;when it is nonpositive the support is already<=0. The positive interval lies strictly inside(0,2pi). Its unique maximum occurs at theta=4phi/5 and equals cos^5(phi/5). This follows by differentiating: tan(theta-phi)=-tan(theta/4),and the positive-cosine branch gives5theta/4=phi. Consequently

    F_t(B) dot X <= |B|^2 for every X in K4(B).            (3.3)

The factors cancel because cos(alpha)=(1+t^2)^(-1/2). The endpoint B itself has F_t(B)dotB=|B|^2 f(t)<0,so it also obeys(3.3);0 does too. Thus taking a convex hull introduces no gap. All estimates include weak radial arrows and limiting zero-radius points in the relaxation.

Define

    a_t(s)=f(t)-s*g(t),
    b_t(s)=g(t)+s*f(t),
    c_t(s,z)=a_t(s)c(z)-b_t(s)d(z).                       (3.4)

Dividing all support values by the positive bx gives

    F_t dot A /bx = a_t,
    F_t dot C' /bx = c_t,
    max_K4 F_t /bx <= w,
    F_t dot(-A/3)/bx = -a_t/3,
    F_t dot(-B/3)/bx = -w*f(t)/3.                        (3.5)

The entire test is now on s,w,z,not seven independent vertex coordinates.

## 4. Eliminate the radial variable w
For every direction in(3.2),a_t(s)<0 throughout0<=s<=3. The executable checks both endpoints of this linear function exactly.

At the SINGLE direction t_B=3/4,

    f=-3116/1024<-3, g=-237/1024.

Since f<-3,the target -B/3 has larger support than the envelope K4(B). Since a_t<0,the point A cannot support that positive target either. The point C' must therefore satisfy

    3c_B+w f_B>=0,
    w<=u_B(s,z)=-3c_B/f_B.                              (4.1)

Together with w<=1,put

    U(s,z)=min(1,u_B(s,z)).                              (4.2)

At any direction t_A=k/100,k=35,...,73,the target -A/3 has positive support whereas A has negative support. Thus at least one of K4(B) or C' must cover it. If

    3c_A+a_A<0,                                         (4.3)

then C' cannot do so,and necessarily

    3w+a_A>=0.                                          (4.4)

Equations(1.2),(4.1),(4.3),(4.4) are impossible over the full(s,z)rectangle,as established by the26-cell certificate below. This elimination preserves necessary conditions only;no sufficiency or attainability of the envelope is asserted.

## 5. Exact interval certificate and why each leaf is valid
Every cell is a closed rational rectangle [s0,s1] times[z0,z1]. The executable derives exact bounds for c(z) and d(z). The function c decreases on[0,1]. The function d is nonnegative,increases to1/2 at z=sqrt(2)-1,and then decreases. Thus its lower bound is the smaller endpoint value;its upper bound is the larger endpoint value unless the interval contains that unique peak,in which case the exact upper bound1/2 is used. The peak containment test is the polynomial sign test z^2+2z-1,not a rounded square root.

Write C_L for the lower bound of c,and[d_L,d_H] for the bounds of d. The code scales f,g,a,b,c_t by the common integer G=100^5. Let a_H<0 be the upper endpoint of the scaled linear function a_t(s),and let[b_L,b_H] bound the scaled b_t(s). Put

    m=min(b_L*d_L,b_L*d_H,b_H*d_L,b_H*d_H).

Then throughout the cell

    G*c_t <= a_H*C_L-m,
    G*(3c_t+a_t) <= a_H*(3C_L+1)-3m.                    (5.1)

The negative sign of a_H is essential and is checked. These bounds may discard correlation,but always enlarge the feasible set and hence are safe for an exclusion.

Using(5.1) at t_B gives a rational upper bound U_H on U. There are two terminal tests:

**Radius leaf.** If U_H<0,or9U_H^2<1+s0^2,then no positive w<=U_H can satisfy9w^2>=1+s^2. The comparison with the square is used only after separating the negative-U case.

**Support leaf.** At some t_A,if the second upper bound in(5.1) is strictly negative and3G U_H+a_H<0,then(4.3) holds everywhere on the cell,while even the upper bound on3w+a_t is strictly negative. This contradicts(4.4).

A slope leaf s0^2>8 is also implemented as a valid redundant test,but none is needed in the finished cover.

The deterministic binary subdivision always retains BOTH closed halves and never prunes a cell by a numerical feasibility decision. It terminates with

    51 nodes,26 leaves,maximum depth10;
    2 radius leaves,24 support leaves;
    exact covered area3;
    exact Kraft sum sum_leaf2^(-depth)=1.

Each terminal test is computed in Fraction arithmetic. The report records every exact rectangle,direction and rational margin. The complete root rectangle[0,3]x[0,1] is covered. All physical parameter endpoints and all finite weak-arrow walls are therefore included. This proves the theorem.

## 6. Actual-shadow interpretation and remaining question
For a polygon with a sole strict radial maximum,every other true corner has exactly one weak outgoing boundary arrow. Both cannot be weak because the inward direction to0 is a positive combination of the two incident edge directions. Along weak arrows the squared norm increases strictly. Removing the one unused boundary edge gives two branches at the root,including the possibility of a branch of length0.

At seven corners the unordered branch lengths are(3,3),(4,2),(5,1),(6,0). The first is excluded by the known x>=-1/4 chain bound,the second by [internal-source-reference],and the third by the theorem here. Only the endpoint6+0 form remains.

For actual homogeneous own-centred3D shadows,the condition -Q/3 subsetQ is necessary and true exposed fibres carry the radial-maximal obstruction. Thus the new result is universal across all actual3D families and all planar SPD metrics after an invertible planar change of coordinates. It is nevertheless only a necessary-form reduction. No new3D centroid realization,globalC34 exclusion,or rank-two-to-proper110 lift is asserted. Even a successful U1 lift near rank2 has separate same-reciprocal-metric S1 obligations,as recorded in the shared notebook.

## 7. Complete reconstruction and observed evidence
The following3887-byte source is the entire exact construction/verifier. It imports only the standard library and does not call an optimizer,read a checkpoint,import a parent source,or assume a numeric centroid. All directions and subdivision decisions are literal or deterministic. It was executed with CPython3.13.5,assertions enabled. Build and check both exited0,and their output matched byte-for-byte. This is one exact implementation,not a proof-assistant formalization or independently authored verification.

Save as branch51_cover.py,UTF-8/LF,and run

    python -B -S branch51_cover.py build > build.out
    python -B -S branch51_cover.py check > check.out
    cmp build.out check.out

Pins:

    branch51_cover.py:3887bytes
    SHA2566eb915177204ef71d673cf8b6094e92ea6813b47ad5e26125f56bf2e707f9d25
    branch51_cover.json:5055bytes
    SHA25639f4293227fc613093427fa6e21435bb422f4a409e9b8d96090ad44e8e106de0
    identical build.out/check.out:214bytes
    SHA2567cd90e59bed56abee732c01a5c4a02a2abc43e6207e0cf397f55b851a3eeb62f

Expected stdout:

    SEVEN_CORNER_5_PLUS_1_WEAK_ROOT_ENVELOPE_EXCLUSION_PASS
    EXACT_COMPACT_TWO_DIMENSIONAL_COMPLETE_COVER_PASS
    51 26 10 {'radius': 2, 'support': 24}
    5055 39f4293227fc613093427fa6e21435bb422f4a409e9b8d96090ad44e8e106de0

```python
#!/usr/bin/env python3
"""Exact rational necessary-envelope exclusion for the 5+1 seven-corner form.
Standard library only, Python>=3.11, assertions enabled.
The executable validates a two-dimensional compact cover, not a sampled search.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,sys,time
G=100**5
TA=tuple(range(35,74));TB=(75,)
def coeff(k):
    return (G-10*k*k*100**3+5*k**4*100,5*k*100**4-10*k**3*100**2+k**5)
CO={k:coeff(k) for k in TA+TB}
assert all(0<k<100 and k*k<2*100**2 and CO[k][0]<0 for k in CO)
# A_t=f_x-s*f_y is strictly negative for every s in[0,3].
assert all(max(fx,fx-3*fy)<0 for fx,fy in CO.values())
assert all(CO[k][0]<-3*G for k in TB)
def cd(z):
    q=1+z*z
    return ((1-z*z)**2/q**2,2*z*(1-z*z)/q**2)
def cd_bounds(z0,z1):
    c0,d0=cd(z0);c1,d1=cd(z1)
    dh=max(d0,d1)
    if z0*z0+2*z0-1<=0<=z1*z1+2*z1-1:dh=F(1,2)
    return c1,c0,min(d0,d1),dh

def terms(k,s0,s1,cl,dhlo,dhhi):
    fx,fy=CO[k]
    al=min(fx-fy*s0,fx-fy*s1);ah=max(fx-fy*s0,fx-fy*s1)
    dl=min(fy+fx*s0,fy+fx*s1);du=max(fy+fx*s0,fy+fx*s1)
    assert ah<0
    mindd=min(dl*dhlo,dl*dhhi,du*dhlo,du*dhhi)
    cup=ah*cl-mindd
    # upper bound for 3*C+A, with C=f_x c_x-f_y d-s(f_y c_x+f_x d)
    activeup=ah*(3*cl+1)-3*mindd
    return ah,cup,activeup

def decide(box):
    s0,s1,z0,z1=box
    if s0*s0>8:return ('slope',)
    cl,ch,dl,dh=cd_bounds(z0,z1)
    ub=F(1); bk=0
    for k in TB:
        ah,cup,ac=terms(k,s0,s1,cl,dl,dh)
        u=-3*cup/CO[k][0]
        if u<ub:ub=u;bk=k
    if ub<0 or 9*ub*ub<1+s0*s0:return ('radius',bk,ub)
    for k in TA:
        ah,cup,activeup=terms(k,s0,s1,cl,dl,dh)
        if activeup<0 and 3*ub*G+ah<0:
            return ('support',bk,k,ub,activeup,3*ub*G+ah)
    return None

def pack(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,(list,tuple)):return [pack(y) for y in x]
    if isinstance(x,dict):return {str(k):pack(v) for k,v in x.items()}
    return x

def run():
    root=(F(0),F(3),F(0),F(1));stack=[('',root)];leaves=[];nodes=0;maxdepth=0
    area=F(0);kraft=F(0);start=time.monotonic()
    while stack:
        path,box=stack.pop();nodes+=1;maxdepth=max(maxdepth,len(path))
        proof=decide(box)
        if proof is not None:
            leaves.append((path,box,proof));area+=(box[1]-box[0])*(box[3]-box[2]);kraft+=F(1,2**len(path));continue
        if len(path)>=34:raise AssertionError(('unclosed',path,pack(box)))
        s0,s1,z0,z1=box
        # Alternating normalized widths gives a deterministic complete binary partition.
        if (s1-s0)/3>=z1-z0:
            mid=(s0+s1)/2;left=(s0,mid,z0,z1);right=(mid,s1,z0,z1)
        else:
            mid=(z0+z1)/2;left=(s0,s1,z0,mid);right=(s0,s1,mid,z1)
        stack.append((path+'1',right));stack.append((path+'0',left))
        if nodes%20000==0:print('WORK',nodes,len(leaves),len(path),round(time.monotonic()-start,3),flush=True,file=sys.stderr)
    assert nodes==2*len(leaves)-1 and area==3 and kraft==1
    counts={}
    for _,_,proof in leaves:counts[proof[0]]=counts.get(proof[0],0)+1
    return dict(theorem='SEVEN_CORNER_5_PLUS_1_ENVELOPE_OBSTRUCTION_V1',root_box=root,TA=TA,TB=TB,coefficients=CO,coefficient_denominator=G,nodes=nodes,leaf_count=len(leaves),maxdepth=maxdepth,area=area,kraft_sum=kraft,counts=counts,leaves=leaves)

if __name__=='__main__':
    assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
    report=run();data=(json.dumps(pack(report),sort_keys=True,separators=(',',':'))+'\n').encode();out=Path('branch51_cover.json')
    if sys.argv[1]=='build':out.write_bytes(data)
    else:assert out.read_bytes()==data
    print('SEVEN_CORNER_5_PLUS_1_WEAK_ROOT_ENVELOPE_EXCLUSION_PASS')
    print('EXACT_COMPACT_TWO_DIMENSIONAL_COMPLETE_COVER_PASS')
    print(report['nodes'],report['leaf_count'],report['maxdepth'],report['counts'])
    print(len(data),hashlib.sha256(data).hexdigest())
```

## 8. Discovery status and reusable method
Floating exploration suggested that the envelope relaxation itself might be inconsistent at coefficient1/3. No floating output,optimizer convergence,minimum margin,or sampled direction is a proof input; the exact rational cover above establishes the final theorem from scratch. Its finite normal bank is an exact sufficient certificate,not an assertion that only those normals define K4(B).

The general reusable mechanism is to retain the first descendant B,replace its next m descendants by a convex monotone radial envelope,and use rational normals from B(1+it)^(m+1). When the relevant angular maximum is internal,the envelope support is exactly bounded by|B|^2. Paired containment at -A/3 and -B/3 can eliminate the first descendant's radial scale. This does not guarantee that the same small certificate closes the endpoint6 case or larger polygons. Those extensions require their own correct angular ranges and actual coverage.
