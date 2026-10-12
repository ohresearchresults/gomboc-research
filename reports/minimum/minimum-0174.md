# minimum-0174

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# NEGATIVE_Z_MIXED_SPECIAL_B_EXCLUSION_V1

## Result

**The negative-z part of the assigned mixed special-B maximum sector is empty.** More precisely, let P be a polyhedral local maximum of the full marked-body[private-runtime-path] problem, with a>b>0, c,d>0, positive root area, all four canonical marks true, G(C)<0<G(D), expanded Fx, and true edge BD. Then

> P is contained in {z>=0}.

There is **no T threshold and no condition d<=a** in this structural theorem. It covers both a simple SPECIAL BD vertex without an ordinary B triangle and the ordinary-B4 case. It uses full-body whole-facet stationarity and full marked-frame exposure, not stationarity within an imposed sign, endpoint, or lattice sector.

Consequently, the literal parent's S5/I4/I5 classification applies to the **whole** specified mixed sector, not just its initially assumed octant part. Combining this new structural result with the already accepted octant value results gives

> T<=203/100<51/25 for the whole specified mixed special-B full-maximum sector.

The numerical corollary uses the existing low-endpoint and coordinator high-c value theorems; the negative-z proof itself uses neither. No arbitrary negative-z root-only VALUE theorem, no other B-star classification, no mechanical E17 exclusion, and no improvement of 34<=C_min<=622 is claimed.

## Input, authority, and evidence tier

I read the entire supplied journal, all 1,867 lines, including the complete literal parent and its complete source through EOF. The actual mounted journal is 311,658 bytes, SHA-256 `f338f7c4e0a12b1aa80d31bee7b51718c1047a3429d49514436e2034b20359d3`. The required parent is `minimum-0171`, published SHA-256 `9b15d20252180b1b48406f3d65ea1211cd57c733e1cfbc3903deb332736ca3df`. Its extracted 15,873-byte source authenticates to `8b61165d38d10e5f96dd8d7f7e2915f73d2975b6ac5ab38f954d7aaee9687aaf`.

The parent expressly left negative z open except for its B4/d<=a triangularity and endpoint inequality. I have not attributed a negative-z result to its identical-hash republication. The branch's older sentence leaving octant high c open is chronologically superseded by the common notebook and active assignment; it is not used as a current open problem. The accepted current octant closure is recorded separately.

The archived B4 effective-volume source was not supplied. It is **not a dependency** of the proof or new computation below. No research connector, archive, or external source was used. The old parent certificate was not rerun in full. New exact algebra and controls were run normally and again from source alone in an empty directory, with byte-identical report and stdout. The geometric theorem is an analytic proof under the accepted variation premises, not a proof-assistant formalization or an inference from sampled controls.

## 1. Definitions and exact premises

Use

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    alpha=a-b>0, s=a+b, hx=s+c, hy=s+d,
    ell=a+(d-a)x+(c-a)y-alpha*z,
    n=hx*x+hy*y,
    V=int_P 1, J=int_P X, E=int_P ell, N=int_P n,
    r=N/V, q=N/E, T=N/(6VE), G=n-r-q*ell.

These are the original uniform integrals of one body; E is the ell integral, not the edge count. In particular q,r>0. P contains T0=conv(A,B,C,D), lies in x,y,ell>=0, and has true protected maximal facets Fx,Fy and positive-area root F0={ell=0}.

The accepted maximum conditions used are: every auxiliary true vertex has positive G; every free maximal facet satisfies max G+3 mean G<=0; a one-mark free facet is a triangle XUV with G(U)=G(V)=-G(X)/3; and every allowed affine whole-facet motion H vanishing on its canonical marks has int_F GH/|grad f_F|=0. The full marked-frame exposures are

    hC=(b+2c)(y-1)-alpha*z<=0 on Fx,
    hD=(b+2d)(x-1)-alpha*z<=0 on Fy.

For G(C)<0 and expanded Fx, AC is a true edge, BC is not, and every auxiliary vertex of Fx has z>0. Ordinary B facets, when present, are the accepted minimum-G-root-edge triangles; there is at most one. These are inherited premises with their stated full-maximum scope.

For a true triangle XYZ and affine H with H(X)=H(Y)=0, the integration formula used below is

    int_XYZ G*H/|grad f|
      =Area(XYZ)*H(Z)*[G(X)+G(Y)+2G(Z)]/(12|grad f|).

Triangulations of larger facets are only used to sum this formula, never to authorize separate motions.

The mixed signs immediately imply

    G(D)-G(C)=(c-d)(1+q)>0, hence c>d.

Assume for contradiction that P has negative z. Then z=0 cannot be a supporting facet because B has z=1. In particular the second true facet at AC is a free facet marked by exactly A,C, not the three-mark ACD facet. This is the important difference from the octant argument.

## 2. No ordinary A or C facets in this negative-z mixed geometry

First exclude an ordinary A or C triangle whose equal-G base is nonroot or is a root maximum. Write its auxiliary level as L>0, so its mark has G=-3L.

For a nonroot base, both incident true facets contain a negative-G point: a free facet does so by its spike inequality, and a coordinate facet contains A or B. Since G is constant on the common edge, each facet lies on the G<=L side. Their actual edge tangent cone gives G<=L on all P. For a root-maximum base the same conclusion follows directly from the supporting plane

    H_X=G-L+(4L/ell(X))*ell=0,

whose body side is H_X<=0. This is the parent's genuine equal-positive-edge mechanism, not an arbitrary sign assignment.

Now apply the whole hinge of the true AC facet, with H=x>=0. Triangulate that whole polygon from whichever of A,C has G=-3L, for integration only. Every contribution is nonpositive when all vertex G<=L. The triangle incident to the actual edge AC is strictly negative because its other canonical endpoint has G<0<L. Thus the **whole** hinge is strictly negative, contradicting stationarity.

On the positive-area root, G=n-r is nonconstant: grad n has zero z component whereas grad ell has z component -alpha. Thus a constant-G root edge is genuinely a minimum or maximum edge. The only remaining ordinary A/C possibility is therefore a minimum-G root base.

For ordinary A, put LA=(r+qa)/3. Its minimum-side support H_A>=0 must contain B, but

    H_A(B)=G(B)-LA+(4LA/a)b
          =-(a-b)(4r+qa)/(3a)<0.

For ordinary C, let K be n on its root base. Its plane and body side are

    F=(K-hy)*ell+c*(n-K)>=0.

At B this requires

    (b-c)K-b*hy>0,

so b>c and K>b*hy/(b-c). At D it requires

    (c-d)(s+c+d-K)>0,

so K<s+c+d because c>d. These are incompatible, since

    b*hy-(b-c)(s+c+d)=c(a+c+d)>0.

Thus there are no ordinary A or C facets. A facet with only D is impossible because G(D)>0 and all its auxiliary vertices have positive G. A free facet with no canonical mark is likewise excluded by its spike inequality.

It follows that the complete possible free-facet list in this negative-z geometry is

    AC, AD when present, BD, one or two CD facets,
    and the optional ordinary B-root triangle.

This is a list of true maximal facets. Free AB is impossible because AB already belongs to Fx,Fy; a facet containing B,C would force BC to be a true edge of Fx; ACD is not supporting; and the other three-mark planes are protected or similarly impossible. There are at most two CD facets, and if there are two distinct ones their intersection is the true edge CD.

## 3. Fy is triangular: the missing simple-SPECIAL case is closed

The true edge BD gives x+z<=1 on Fy. If x>1, it gives hD>=(a+2d)(x-1)>0, contradicting hD<=0. Therefore every point of Fy has 0<=x<=1.

An auxiliary true vertex Z of Fy must have z_Z<0: otherwise it lies in the already contained triangle ABD. Crucially, for **all** d>0,

    ell(Z)=a(1-x_Z)+d*x_Z-alpha*z_Z>0.

No d<=a assumption is necessary to exclude root points on Fy. Also

    G(Z)=(1-x_Z)G(A)+x_Z G(D)+q*alpha*z_Z<G(D).

The boundary cycle is A-B-D followed by its auxiliary chain back to A. Two consecutive auxiliary vertices would have a nonroot edge whose second facet cannot contain A,B,D: its intersection with Fy would then contain three distinct collinear true vertices. It would have to be an ordinary C facet, already excluded. Hence Fy is either ABD or a quadrilateral ABDZ.

Suppose Fy=ABDZ. The second facet of AZ is AC, and that of DZ is a CD facet F_-. Their intersection contains C,Z, so CZ is a true edge. The edges AC,AZ,CZ close the entire true facet:

    F_AC=ACZ.

Let R be C's other neighbor on expanded Fx. It is auxiliary and z_R>0. The second facet of CR must be another CD facet F_+, because an ordinary C facet is unavailable.

There are two possibilities, and treating them differently is essential.

### Distinct CD facets

If F_- and F_+ are distinct, their intersection is the true edge CD. The actual edges CD,CZ,DZ then close

    F_-=CDZ

as a **true maximal triangle**. Its whole hinge and that of ACZ give

    G(A)+G(C)+2G(Z)=0,
    G(C)+G(D)+2G(Z)=0.

Thus G(A)=G(D), impossible because G(A)<0<G(D).

### One CD polygon

If F_-=F_+, write this one supporting plane as

    f=1-x-y-k*z>=0.

At the positive-z point R in Fx, y_R-1=-k*z_R. Its C exposure implies

    alpha+(b+2c)k>=0,
    k>=-alpha/(b+2c).

At the negative-z point Z in Fy, x_Z-1=-k*z_Z. Its D exposure implies

    alpha+(b+2d)k<=0,
    k<=-alpha/(b+2d).

The required interval is empty because c>d, with exact endpoint gap

    alpha/(b+2d)-alpha/(b+2c)
      =2alpha(c-d)/[(b+2c)(b+2d)]>0.

Here CDZ may only be an integration triangle of a larger polygon. **No separate hinge for CDZ was used in this case.** The contradiction uses the two full marked-coordinate exposures on the same actual CD support.

Both cases fail. Therefore Fy=ABD, for simple SPECIAL B as well as ordinary B4, without any endpoint or T restriction.

## 4. A CD support separates the actual root from every nonpositive-z point

Since AD is now a true edge, its second facet is the free AD facet. Normalize the true supporting planes as

    fAC=z+u*x>=0,        u>0,
    fAD=z+v*y>=0,        v>0,
    fBD=1-x-beta*y-z>=0, beta<1.

Let F_+ be the CD facet containing the actual edge CR, where R is as above, and write

    f_+=1-x-y-k*z>=0.

B is not on F_+, hence k<1. In fact the stronger inequality

    k<alpha/a

holds. Otherwise k>=alpha/a>0, and R lies in the segment between C and O=(0,0,1/k), since x_R=0, z_R>0 and y_R=1-k*z_R>=0. But

    ell(O)=a-alpha/k>=0,
    G(O)=-r-q*ell(O)<0,

and G(C)<0. Affinity would give G(R)<0, contradicting its genuine auxiliary positivity. Equality k=alpha/a is also excluded because G(O)=-r<0.

Now use the exact, same-plane identity

    ell=a*f_+ + d*x + c*y + (a*k-alpha)*z.

For a point of P with z<0, all terms on the right are nonnegative and the last is strictly positive. At z=0, ell is also strictly positive: f_+,x,y cannot all vanish. Thus

    F0 subset {z>0}.

This is an actual support-and-root statement. It neither clips the body nor substitutes a surrogate G, and it does not assume that the root vertices were already known to be the only auxiliaries.

The same support also excludes any negative-z point from the BD facet, because

    f_+-fBD=(1-k)z-(1-beta)y<0

there, which is incompatible with fBD=0 and f_+>=0.

## 5. The last possible negative vertex forces incompatible true triangle hinges

A negative-z true vertex Z cannot belong to Fx, whose auxiliary vertices have positive z, or to Fy=ABD. It cannot belong to the root, now strictly above z=0. It cannot belong to an ordinary B triangle because all that triangle's vertices are B or root vertices and thus have positive z. It cannot belong to BD by the preceding identity.

The complete remaining list of incident facets is therefore AC,AD,CD. Two distinct CD planes intersect only on z=0, so at Z there is at most one CD plane. A true three-dimensional vertex needs at least three independent facet planes. Consequently Z lies on exactly

    F_AC, F_AD, and one F_CD.

Their pairwise intersections give the true edges AZ,CZ,DZ. Together with the already true edges AC and AD, these close the entire maximal facets

    F_AC=ACZ, F_AD=ADZ.

The two genuine whole hinges, with H=x and H=y respectively, give

    G(A)+G(C)+2G(Z)=0,
    G(A)+G(D)+2G(Z)=0.

They require G(C)=G(D), contradicting the strict mixed signs. There is no negative-z vertex, hence no negative-z point of the convex polytope. This completes the theorem.

## 6. Consequences, independent useful inequalities, and precise scope

The new theorem removes the z>=0 hypothesis from the parent's mixed expanded-Fx/true-BD classification. Thus the only full maxima in this sector are its actual S5, I4, I5 root-only types. For c<=a, including its endpoint limit, the accepted bound is 203/100. For c>=a the coordinator's accepted bound on these same types is 3/2. Because c>d, these cases cover all positive endpoints. The whole sector therefore has T<=203/100. The reflected statement exchanges C,D and x,y.

An earlier route produced a reusable independent quantitative lemma. Before the stronger mark-exposure contradiction, a hypothetical Fy=ABDZ with true ACZ hinge would satisfy

    4r+q(a+c+2ell(Z))=hy+2hx*x_Z.

The genuine D- and C-apex volume fans give 4g_x>=1 and 4g_y>=1 for the **same** actual g=J/V. Hence 4r>=hx+hy and

    q(a+c+2ell(Z))<=hx(2x_Z-1)<hx,
    x_Z>1/2,
    T< (a+b+c)/(a+c) <2.

Here 6V>=1 and q=6VT were used. This lemma is not needed for the final no-negative-z theorem, but it is preserved because it couples a true triangle hinge to actual common volume moments and may apply when the second mark exposure is unavailable.

The principal new connections are therefore: ordinary-C root-min support at B versus D; opposite-z C/D exposures on a single true CD polygon; a CD support whose axial intercept still has positive ell; and the forced pair of **maximal**, not integration, triangles at the final negative vertex.

The proof requires full marked-frame exposure plus the accepted full-body variation conditions. It does not assume J:4(g_x+g_y)<=6V+1, independently variable star masses, the B4 effective-volume relaxation, root stationarity moment equations, or a stationary surrogate G. It does not cover constrained maxima lacking these reactions, zero endpoints, a=b, nonexpanded negative patches, B5/both-BC-BD stars, or arbitrary nonstationary negative-z root-only bodies. The trace-to-mechanical-E17 bridge and the numerical minimum remain unresolved.

## 7. Exact genuine nonstationary negative-z control and an entire whole-facet ascent

To check that the theorem does not silently promote pointwise signs to full stationarity, I preserved two exact actual B4 bodies and an entire true-facet path. They satisfy the mixed signs, positive auxiliary G, both mark supports, true BD, positive root area, and negative z. They fail the needed whole-facet stationarity, as they must.

Let p=100+t, 0<=t<=1. Use endpoints

    (a,b,c,d)=(1,1/5,1/4,1/100)

and all eight true inward supporting inequalities

    x>=0, y>=0,
    ell=1-99x/100-3y/4-4z/5>=0,
    z+x/p>=0,
    z+y>=0,
    1-x-y/10-z>=0,
    1-x-y+z>=0,
    4/5-449x/600-329y/600-4z/5>=0.

The last facet is geometrically the ordinary B-root triangle with root n-level 6/5; its own-G rigidity is not assumed or satisfied. The canonical vertices have indices 0,1,2,3. The remaining exact vertices, for the entire interval, are

    4=(0,120/121,155/484),
    5=(0,36/31,5/31),
    6=(1405/1854,155/1854,289/1236),
    7=(p/(p+2),1/(p+2),-1/(p+2)),
    8=(1120/1131,20/1131,3/377).

The complete maximal facet cycles, in the supporting-plane order above, are

    (4,1,0,2,5), (1,0,3), (4,6,8,5), (2,0,7),
    (3,0,7), (1,3,8,6), (5,8,3,7,2), (1,6,4).

The complete true edges are

    (0,1),(0,2),(0,3),(0,7),(1,3),(1,4),(1,6),
    (2,5),(2,7),(3,7),(3,8),(4,5),(4,6),(5,8),(6,8).

Thus these are actual 9/15/8 auxiliary trace controls, not mechanical 110 candidates. No S/U/H census is claimed.

At p=100 the original moments are

    V=15905239673/66855682179,
    E=248550459460733/3636949110537600,
    N=7779302949416120743/42505024254852931200,
    J=(783498637559746817/12710373382015699104,
       1844793729138840993173/23838305277970443669552,
       1003132476881003238889/15892203518646962446368),
    T=14833878256761686261461377/7906509257114457394520618
      approximately 1.8761602338495746.

At p=101 they are

    V=3742159783/15730748748,
    E=553606221013/8101335605220,
    N=6930773475453221/37872123687282456,
    J=(2710725904586555/43980530733618336,
       12766071570515030875/164970970781802378336,
       216940680521287651/3436895224620882882),
    T=3887020342105807199535/2071682935893458120179
      approximately 1.8762621802594737.

Both have mark-support maxima (0,0), G(C)<0<G(D), all auxiliary G>0, and exactly vertex 7 below z=0. At p=100, ell(7)=41/2040>0. The two true triangle hinges, normalized by their actual coarea factors, differ by exactly

    [G(A)+G(C)+2G(7)]-[G(A)+G(D)+2G(7)]
      =G(C)-G(D)=-(c-d)(1+N/E)<0.

Both actual AC and AD hinge integrals are negative in this control. Increasing p changes only the **whole** AC supporting plane; the other seven supports remain fixed. The source proves T(100+t)>T(100) for every 0<t<=1, using 140 exact polynomial guards and 233 strictly positive Bernstein coefficients. It verifies the full incidence interval, positive A/B volume fans, original E,N,J, and the actual whole-facet first-work identity. It does not move the CD pentagon's integration triangles independently.

For each endpoint the report also reconstructs every true B-apex facet pyramid and its V,J,E,N. Their sums equal the whole-body moments, and the genuine root pyramid satisfies E_R=b V_R/4. The root geometry is unchanged along the path; the whole-body moments are recomputed, not held independently fixed.

## 8. Recovery and verification

The universal theorem above is the durable analytic result. Its finite algebra and actual controls have this fully self-contained source-only recovery:

    CPython 3.13.5
    SymPy 1.14.0
    assertions enabled; no random input; no parent import; no external data

    python negative_z_mixed_special_b_v1.py > negative_z_mixed_special_b_v1.out
    sha256sum negative_z_mixed_special_b_v1.py \
      negative_z_mixed_special_b_v1.json negative_z_mixed_special_b_v1.out

Expected pins:

    source: 12259 bytes
    SHA256 930be1eeb3fe1f2c4a18c041440943975da5e5d79bb796ea026951b674dc5fdc
    report: 21956 bytes
    SHA256 8f1ee4309d031c61eb3d4c01428b4b36b06e24ed6857446b4203bf8ffd0dd1ed
    stdout: 433 bytes
    SHA256 879e291b6eda97fc3777087a0cb5f0f87d9845f34ccca7fe7272e5b3fe8b4698

Complete expected stdout:

    TWELVE_EXACT_PROOF_IDENTITIES_PASS
    TWO_ACTUAL_9_15_8_HULLS_TRUE_FACETS_EDGES_AND_TWO_FANS_PASS
    SAME_BODY_ROOT_AND_B_STAR_V_J_E_N_PASS
    MIXED_SIGNS_AUXILIARY_POSITIVITY_AND_BOTH_MARK_SUPPORTS_PASS
    WHOLE_AC_FACET_ASCENT_100_TO_101_PASS
    guard_polynomials=140
    positive_coefficients=233
    report_bytes=21956
    report_sha256=8f1ee4309d031c61eb3d4c01428b4b36b06e24ed6857446b4203bf8ffd0dd1ed
    NEGATIVE_Z_MIXED_SPECIAL_B_EXCLUSION_V1_RECOVERY_PASS

Normal execution and an empty-directory source-only run were actually completed; `cmp` matched both report and stdout. Optional copies are source (`negative_z_mixed_special_b_v1.py`), report (`negative_z_mixed_special_b_v1.json`), and stdout (`negative_z_mixed_special_b_v1.out`). Nothing in the handoff requires these links: the entire source follows.

```python
#!/usr/bin/env python3
"""NEGATIVE_Z_MIXED_SPECIAL_B_EXCLUSION_V1.
CPython 3.13.5; SymPy 1.14.0; assertions enabled. No RNG or external data.
Parent: minimum-0171,
9b15d20252180b1b48406f3d65ea1211cd57c733e1cfbc3903deb332736ca3df.
The universal exclusion is analytic. These are exact algebra and actual-body
checks, not a search over all bodies and not an equilibrium/110 certificate.
"""
from fractions import Fraction as F
from itertools import combinations
from functools import cmp_to_key
from math import comb
from pathlib import Path
import hashlib
import json
import sympy as S

PARENT = 'minimum-0171'
PARENT_SHA = '9b15d20252180b1b48406f3d65ea1211cd57c733e1cfbc3903deb332736ca3df'
ENDS = (F(1), F(1,5), F(1,4), F(1,100))
CAN = tuple(tuple(map(F,p)) for p in ((0,0,0),(0,0,1),(0,1,0),(1,0,0)))


def dot(a,b): return sum((x*y for x,y in zip(a,b)), F(0))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def solve(ns,rhs):
    d=det(*ns); assert d
    cof=(cross(ns[1],ns[2]),cross(ns[2],ns[0]),cross(ns[0],ns[1]))
    return tuple(sum(rhs[i]*cof[i][j] for i in range(3))/d for j in range(3))
def cyclic(points,ids,normal):
    axes=[j for j in range(3) if j!=next(k for k in range(3) if normal[k])]
    center=[sum(points[i][j] for i in ids)/len(ids) for j in axes]
    vec={i:tuple(points[i][j]-c for j,c in zip(axes,center)) for i in ids}
    def half(v): return int(v[1]<0 or (v[1]==0 and v[0]<0))
    def cmp(i,j):
        a,b=vec[i],vec[j]
        if half(a)!=half(b): return -1 if half(a)<half(b) else 1
        d=a[0]*b[1]-a[1]*b[0]
        assert d or i==j
        return -1 if d>0 else (1 if d<0 else 0)
    return tuple(sorted(ids,key=cmp_to_key(cmp)))
def moments(points,faces,apex):
    v=F(0); j=[F(0)]*3
    for face in faces:
        if apex in face: continue
        for k in range(1,len(face)-1):
            ids=(apex,face[0],face[k],face[k+1])
            w=abs(det(*(sub(points[i],points[apex]) for i in ids[1:])))/6
            assert w>0
            v+=w
            for h in range(3): j[h]+=w*sum(points[i][h] for i in ids)/4
    return v,tuple(j)
def en(v,j):
    a,b,c,d=ENDS
    return a*v+dot((d-a,c-a,b-a),j),dot((a+b+c,a+b+d,0),j)
def spaces(p):
    # Complete inward supporting planes; only the whole AC plane changes.
    return [(F(0),(F(1),F(0),F(0))),
            (F(0),(F(0),F(1),F(0))),
            (F(1),(-F(99,100),-F(3,4),-F(4,5))),
            (F(0),(1/F(p),F(0),F(1))),
            (F(0),(F(0),F(1),F(1))),
            (F(1),(-F(1),-F(1,10),-F(1))),
            (F(1),(-F(1),-F(1),F(1))),
            (F(4,5),(-F(449,600),-F(329,600),-F(4,5)))]
def work(points,face,normal,gv,hv):
    # Whole-facet integral int G*h/|grad f|; diagonals are integration only.
    axis=next(i for i in range(3) if normal[i])
    ans=F(0)
    for k in range(1,len(face)-1):
        ids=(face[0],face[k],face[k+1]); p0,p1,p2=(points[i] for i in ids)
        area=abs(cross(sub(p1,p0),sub(p2,p0))[axis]/normal[axis])/2
        ans+=area*(sum(gv[i] for i in ids)*sum(hv[i] for i in ids)
                   +sum(gv[i]*hv[i] for i in ids))/12
    return ans

def audit(p):
    hs=spaces(p)
    # Exact positive normal circuit proves trivial recession cone/boundedness.
    assert tuple(hs[2][1][j]+F(4,5)*hs[6][1][j]
                 +F(179,100)*hs[0][1][j]+F(31,20)*hs[1][1][j]
                 for j in range(3))==(0,0,0)
    assert det(hs[0][1],hs[1][1],hs[2][1])!=0
    raw=set()
    for ids in combinations(range(len(hs)),3):
        ns=[hs[i][1] for i in ids]
        if not det(*ns): continue
        x=solve(ns,[-hs[i][0] for i in ids])
        if all(c+dot(n,x)>=0 for c,n in hs): raw.add(x)
    assert set(CAN)<=raw
    pts=list(CAN)+sorted(raw-set(CAN))
    faces=[]
    for c,n in hs:
        ids=[i for i,x in enumerate(pts) if c+dot(n,x)==0]
        assert len(ids)>=3
        faces.append(cyclic(pts,ids,n))
    found=set()
    for i,j,k in combinations(range(len(pts)),3):
        n=cross(sub(pts[j],pts[i]),sub(pts[k],pts[i]))
        if not any(n): continue
        sl=[dot(n,sub(x,pts[i])) for x in pts]
        if min(sl)<0<max(sl): continue
        found.add(frozenset(h for h,s in enumerate(sl) if s==0))
    assert found=={frozenset(f) for f in faces}
    edges={tuple(sorted((f[k-1],f[k]))) for f in faces for k in range(len(f))}
    assert edges=={tuple(sorted(f&g)) for f,g in combinations(found,2) if len(f&g)==2}
    assert len(pts)-len(edges)+len(faces)==2
    assert (len(pts),len(edges),len(faces))==(9,15,8)
    for i in range(len(pts)):
        ns=[hs[j][1] for j,f in enumerate(faces) if i in f]
        assert any(det(*t) for t in combinations(ns,3))
    v,j=moments(pts,faces,0)
    assert (v,j)==moments(pts,faces,1)
    e,n=en(v,j); a,b,c,d=ENDS; q=n/e; r=n/v
    ell=[a+dot((d-a,c-a,b-a),x) for x in pts]
    gv=[dot((a+b+c,a+b+d,0),x)-r-q*ev for x,ev in zip(pts,ell)]
    assert min(ell)>=0 and gv[2]<0<gv[3] and min(gv[4:])>0
    assert pts[7]==(F(p,p+2),F(1,p+2),-F(1,p+2))
    assert ell[7]>0 and [i for i,x in enumerate(pts) if x[2]<0]==[7]
    assert len(faces[0])==5 and set(faces[1])=={0,1,3}
    assert sum(1 in f for f in faces)==4
    marks=[max((b+2*end)*(x[axis]-1)+(b-a)*x[2]
               for x in pts if x[1-axis]==0) for axis,end in ((1,c),(0,d))]
    assert marks==[0,0]
    xvals=[x[0] for x in pts]; yvals=[x[1] for x in pts]
    ac=work(pts,faces[3],hs[3][1],gv,xvals)
    ad=work(pts,faces[4],hs[4][1],gv,yvals)
    acn=24*ac/pts[7][0]**2; adn=24*ad/pts[7][1]**2
    assert acn==gv[0]+gv[2]+2*gv[7]
    assert adn==gv[0]+gv[3]+2*gv[7]
    assert acn-adn==gv[2]-gv[3]==-(c-d)*(1+q)<0
    assert ac<0 and ad<0
    pieces=[]
    for f in faces:
        if 1 in f: continue
        w,jj=moments(pts,[f],1); ee,nn=en(w,jj)
        pieces.append(dict(facet=list(f),V=str(w),J=list(map(str,jj)),E=str(ee),N=str(nn)))
    assert sum(F(z['V']) for z in pieces)==v
    assert sum(F(z['E']) for z in pieces)==e
    assert sum(F(z['N']) for z in pieces)==n
    root=next(z for z in pieces if set(z['facet'])==set(faces[2]))
    assert F(root['E'])==b*F(root['V'])/4
    record=dict(p=p,vertices=[list(map(str,x)) for x in pts],
                facets=[list(f) for f in faces],edges=[list(z) for z in sorted(edges)],
                slacks=[[str(c),list(map(str,n))] for c,n in hs],
                f_vector=[len(pts),len(edges),len(faces)],endpoints=list(map(str,ENDS)),
                V=str(v),J=list(map(str,j)),E=str(e),N=str(n),T=str(n/(6*v*e)),
                g=[str(x/v) for x in j],G=list(map(str,gv)),ell=list(map(str,ell)),
                mark_support_maxima=list(map(str,marks)),B_fan=pieces,
                whole_AC_hinge=str(ac),whole_AD_hinge=str(ad),
                normalized_hinge_difference=str(acn-adn),
                ordinary_B_level_defect=str(gv[1]+3*gv[4]),
                status='actual nonstationary uniform body; S/U/H not computed; not a 110 witness')
    return pts,faces,hs,(v,j,e,n),record


def algebra():
    a,b,c,d,r,q,x,y,z,k,beta,L=S.symbols('a b c d r q x y z k beta L')
    al=a-b; hx=a+b+c; hy=a+b+d
    ell=a+(d-a)*x+(c-a)*y-al*z
    g=hx*x+hy*y-r-q*ell
    ga=-r-q*a; gb=-r-q*b; gc=hy-r-q*c; gd=hx-r-q*d
    ka=S.symbols('K'); la=(r+q*a)/3
    identities=[
        gd-gc-(c-d)*(1+q),
        gb-la+4*la*b/a+(a-b)*(4*r+q*a)/(3*a),
        ((ka-hy)*d+c*(hx-ka))-(c-d)*(a+b+c+d-ka),
        b*hy-(b-c)*(a+b+c+d)-c*(a+c+d),
        g.subs(y,0)-((1-x)*ga+x*gd+q*al*z),
        ga+gc+2*g.subs(y,0)-(hy+2*hx*x-4*r-q*(a+c+2*ell.subs(y,0))),
        al/(b+2*d)-al/(b+2*c)-2*al*(c-d)/((b+2*c)*(b+2*d)),
        (b+2*c)*(y-1)-al*z+(al+(b+2*c)*k)*z-(b+2*c)*(y+k*z-1),
        ell-(a*(1-x-y-k*z)+d*x+c*y+(a*k-al)*z),
        (1-x-y-k*z)-(1-x-beta*y-z)-((1-k)*z-(1-beta)*y),
        (ga+gc+2*L)-(ga+gd+2*L)-(gc-gd),
        -ga/2-(r+q*b)/3-(r+q*(3*a-2*b))/6]
    assert all(S.cancel(t)==0 for t in identities)
    return dict(identities=len(identities),
                coordinate_mark_gap='2*(a-b)*(c-d)/((b+2*c)*(b+2*d))>0',
                root_barrier='ell=a*f_CD+d*x+c*y+(a*k-(a-b))*z',
                BD_barrier='f_CD-f_BD=(1-k)*z-(1-beta)*y',
                status='symbolic identities checked; geometric theorem proved in the handoff')


def bernstein_positive(expr,t):
    num,den=S.fraction(S.factor(expr)); out=[]
    assert num!=0
    for pol in (num,den):
        P=S.Poly(S.expand(pol),t); degree=int(P.degree())
        co=[P.nth(j) for j in range(degree+1)]
        bc=[S.factor(sum(co[j]*S.Rational(comb(i,j),comb(degree,j))
                         for j in range(i+1))) for i in range(degree+1)]
        assert min(bc)>0, (expr,bc)
        out.append([str(z) for z in bc])
    return out

def arc(base,child):
    pts,faces,hs,(v,j,e,n),rec=base
    t=S.symbols('t'); pp=100+t
    X=[S.Matrix(x) for x in pts]
    X[7]=S.Matrix([pp/(pp+2),1/(pp+2),-1/(pp+2)])
    H=[(S.Rational(c),S.Matrix(nn)) for c,nn in hs]
    H[3]=(S.Integer(0),S.Matrix([1/pp,0,1]))
    guards=[]
    for k,(c,nn) in enumerate(H):
        for i,x in enumerate(X):
            val=S.factor(c+nn.dot(x))
            if i in faces[k]: assert val==0
            else: guards+=bernstein_positive(val,t)
    def symbolic_fan(apex):
        vv=S.Integer(0); jj=S.zeros(3,1)
        for f in faces:
            if apex in f: continue
            for k in range(1,len(f)-1):
                ids=(apex,f[0],f[k],f[k+1])
                dd=S.det(S.Matrix.hstack(*(X[i]-X[apex] for i in ids[1:])))
                w=S.factor(S.sign(dd.subs(t,0))*dd/6)
                guards.extend(bernstein_positive(w,t))
                vv+=w; jj+=w*sum((X[i] for i in ids),S.zeros(3,1))/4
        return S.factor(vv),jj.applyfunc(S.factor)
    vv,jj=symbolic_fan(0); vb,jb=symbolic_fan(1)
    assert S.cancel(vv-vb)==0 and all(S.cancel(z)==0 for z in jj-jb)
    ee,nn=map(S.factor,en(vv,list(jj)))
    for val in (vv,ee,nn): guards+=bernstein_positive(val,t)
    a,b,c,d=map(S.Rational,ENDS)
    for i,x in enumerate(X):
        ev=a+S.Matrix([d-a,c-a,b-a]).dot(x)
        gv=S.factor(S.Matrix([a+b+c,a+b+d,0]).dot(x)-nn/vv-nn*ev/ee)
        guards+=bernstein_positive(-gv if i<3 else gv,t)
    T=S.factor(nn/(6*vv*ee)); T0=S.Rational(rec['T'])
    quotient=S.factor((T-T0)/t)
    guards+=bernstein_positive(quotient,t)
    work0=S.factor(S.diff(nn,t)-S.Rational(n/v)*S.diff(vv,t)
                   -S.Rational(n/e)*S.diff(ee,t)).subs(t,0)
    assert work0==-S.Rational(rec['whole_AC_hinge'])/10000>0
    assert T.subs(t,1)==S.Rational(child[4]['T'])
    return dict(parameter='0<=t<=1; p=100+t',moving_support='z+x/(100+t)>=0',
                moving_vertex=[str(z) for z in X[7]],V=str(vv),J=[str(z) for z in jj],
                E=str(ee),N=str(nn),T=str(T),positive_difference_divided_by_t=str(quotient),
                first_work=str(work0),guard_polynomials=len(guards),
                positive_coefficients=sum(map(len,guards)),bernstein_coefficients=guards,
                status='entire interval certified; every t>0 raises original T; nonstationary controls')

def main():
    aa=algebra(); base=audit(100); child=audit(101)
    assert F(child[4]['T'])>F(base[4]['T'])
    assert base[1]==child[1]
    path=arc(base,child)
    report=dict(version=1,theorem='NEGATIVE_Z_MIXED_SPECIAL_B_EXCLUSION_V1',
                parent=PARENT,parent_sha256=PARENT_SHA,algebra=aa,
                base=base[4],child=child[4],arc=path)
    raw=(json.dumps(report,sort_keys=True,ensure_ascii=True,indent=2)+'\n').encode()
    Path('negative_z_mixed_special_b_v1.json').write_bytes(raw)
    print('TWELVE_EXACT_PROOF_IDENTITIES_PASS')
    print('TWO_ACTUAL_9_15_8_HULLS_TRUE_FACETS_EDGES_AND_TWO_FANS_PASS')
    print('SAME_BODY_ROOT_AND_B_STAR_V_J_E_N_PASS')
    print('MIXED_SIGNS_AUXILIARY_POSITIVITY_AND_BOTH_MARK_SUPPORTS_PASS')
    print('WHOLE_AC_FACET_ASCENT_100_TO_101_PASS')
    print('guard_polynomials='+str(path['guard_polynomials']))
    print('positive_coefficients='+str(path['positive_coefficients']))
    print('report_bytes='+str(len(raw)))
    print('report_sha256='+hashlib.sha256(raw).hexdigest())
    print('NEGATIVE_Z_MIXED_SPECIAL_B_EXCLUSION_V1_RECOVERY_PASS')

if __name__=='__main__': main()
```

## 9. Exploratory route and nonproof preservation

I first pursued a small full-plane reduction with lower root vertices and an upper positive-ell auxiliary vertex. Three floating seven-parameter probes were exploratory only. The unconstrained run produced a formula value about 2.0238125668129894 but had G(C)>0; both mixed-sign penalty runs reached their iteration limit with violated sign conditions. None is a feasible full-maximum control or a numerical exclusion. Their initially printed parameter vectors were abbreviated, so no exact numerical checkpoint is asserted as a durable successor.

The analytic proof superseded this search: the decisive relation was a single actual CD support's behavior on opposite sides of z=0, not optimization of independent masses. For reproducibility of what was tried, this complete optional locator packages the executed functions, exact input ranges, penalties and nondefault parameters. It uses CPython 3.13.5, NumPy 2.3.5 and SciPy 1.17.0, with `OPENBLAS_NUM_THREADS=1`. Run `OPENBLAS_NUM_THREADS=1 python negative_z_locator_nonproof.py`. Its final marker is deliberately `NONPROOF_LOCATOR_ONLY_END`, not a feasibility or exclusion marker. No separate cold-replay claim is made for the floating locator. Source: 1,928 bytes, SHA-256 `c874d51083835d85c742a7cdd7e0878ec09d4c1ca6590c4a4abe20922770100c`.

```python
import numpy as np
from scipy.optimize import differential_evolution
A=np.array([0.,0.,0.]);B=np.array([0.,0.,1.]);C=np.array([0.,1.,0.]);D=np.array([1.,0.,0.])
def values(x, detail=False):
    b,c,de,f,w,th,t=x; d=c*de; al=1-b; k=al+b*f
    p=b*f*w*th/d; q=b*f*w*(1-th)/c
    h=k-p-q; R=b*f*(1-w)
    dens=np.array([R-h,R-c*h,R-d*h])
    if min(dens)<=0: return None
    wa,wc,wd=np.array([1,c,d])/dens
    P=np.array([p*wa,q*wa,-wa]); S=np.array([p*wc,1+(k-p)*wc,-wc]); Q=np.array([1+(k-q)*wd,q*wd,-wd])
    U=np.array([0.,1-t,t/k]); H=U[1]+U[2]-1
    V=(1+H)/6; J=np.ones(3)/24+H*(B+C+D+U)/24
    for a,bb,cc in ((C,D,Q),(C,Q,S),(P,Q,S)):
        v=abs(np.linalg.det(np.array([a,bb,cc])))/6
        V+=v; J+=v*(a+bb+cc)/4
    E=V+np.dot([d-1,c-1,b-1],J); N=np.dot([1+b+c,1+b+d,0],J)
    if E<=0: return None
    T=N/(6*V*E)
    if not detail: return T
    pts=np.array([A,B,C,D,U,P,Q,S]); ell=1+pts@np.array([d-1,c-1,b-1]); G=pts@np.array([1+b+c,1+b+d,0])-N/V-(N/E)*ell
    return dict(T=T,V=V,J=J,E=E,N=N,ends=[1,b,c,d],p=p,q=q,k=k,points=pts,G=G,ell=ell,hingeBD=G[1]+G[3]+2*G[4])
def obj(x):
    t=values(x)
    return 10 if t is None else -t

def objmixed(x):
    d=values(x,True)
    if d is None: return 100
    g=d['G']
    vio=max(g[2],0)+max(-g[3],0)+sum(max(-z,0) for z in g[4:])
    return -d['T']+100*vio

if __name__=='__main__':
    bounds=[(.0401,.9999),(.0001,1.399),(.0001,.9999),(.0001,.9999),
            (.0001,.9999),(.0001,.9999),(.0001,.9999)]
    np.set_printoptions(precision=17)
    for seed,fun,pop,iters in [(54329,obj,12,250),(54330,objmixed,15,500),
                               (54331,objmixed,15,500)]:
        r=differential_evolution(fun,bounds,seed=seed,popsize=pop,
                                  maxiter=iters,tol=1e-8,polish=True)
        print('seed',seed,'x',repr(r.x),'success',r.success,'message',r.message)
        print(values(r.x,True))
    print('NONPROOF_LOCATOR_ONLY_END')
```

## 10. Most useful continuation and unresolved whole minimum

The highest-value continuation is an independent mathematical audit of the two CD cases in Section 3 and the true-facet closure at the final negative vertex in Section 5, then integration of the theorem with the already accepted octant value result. The proof deliberately distinguishes one nontriangular CD facet from two genuine CD facets; replacing that distinction by independent motions of a triangulation would invalidate it.

After that audit, the assigned negative-z mixed special-B maximum sector has no remaining value problem: every such full maximum is already one of the closed octant S5/I4/I5 types. Arbitrary actual negative-z root-only VALUE remains a separate problem because such bodies need not obey these maximum, exposure and incidence hypotheses. Other stars, zero-endpoint sectors, and the trace-to-actual-mechanical-E17 bridge remain outside this theorem. There is no new 110 attainer and no change to the accepted global interval 34<=C_min<=622; the whole minimum remains open.
