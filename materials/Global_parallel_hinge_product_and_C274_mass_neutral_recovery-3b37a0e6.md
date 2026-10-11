# material-3b37a0e6fe18

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Parallel-hinge product theorem and a globally mass-neutral C274 construction

## Accepted scope
This is a globally valid finite actual-material replacement, not a local cell graft with omitted surrounding mass. The new exact body T43_MASS_NEUTRAL_TWO_HINGE_39 has V49/E137/F90, C274, own strict222, additional weak000, primitive zero000. It is NOT the requested own110. It preserves the complete homogeneous volume and first moment of literal T43 all-G3, including its 46-bit-denominator centroid, while modestly reducing BOTH positive radial/polar bar depths. This offers low complexity and simple mass arithmetic, not a persistence record or a target construction.

It is complementary to FINAL76_G6's detached stable carrier and to the RA44 common-base local cancellation. No stable-root detachment occurs here. The general product theorem below can be used on other polytopes without changing its proof, but the endpoint and finite-search statements concern literal T43 only.

## 1. Exact independent-domain theorem for parallel section translations
Let K be a compact full-dimensional convex polytope, n a nonzero height vector, and h1<...<hk proper interior heights. Let each vj satisfy n·vj=0. Define

F(x)=x+sum_j vj max(0,n·x-hj).

Write Dj for the exact single-hinge velocity domain: v in n-perpendicular for which x+v max(0,n·x-hj) sends K to a convex body. Then

F(K) is convex IF AND ONLY IF (v1,...,vk) belongs to D1 x ... x Dk.

There are NO extra coupled convexity inequalities beyond these individual domains. A small simplex of separate motions is therefore unnecessarily restrictive. The product concerns convexity, not equilibria, mass neutrality, or metrics.

Proof. At a height z in the projection interval of K and for a transverse direction u, let s_u(z)=max{u·x:x in K,n·x=z}. The family of sections is convex as a three-dimensional body exactly when EVERY s_u is concave: necessity follows by taking convex combinations of section maximizers; sufficiency follows because support inequalities in all transverse directions characterize inclusion of each Minkowski combination of sections in the intermediate section. For a polytope these functions are piecewise affine. F translates the z-section by T(z)=sum vj max(0,z-hj), so its support is s_u(z)+u·T(z). The only changed derivative jump at hj is u·vj. Concavity requires precisely u·vj<=s'_u(hj-)-s'_u(hj+) for every u. Each condition involves only vj and is exactly the condition for the jth single hinge. All other slope jumps remain unchanged. This proves both directions, including boundary velocities.

A global affine section shear and translation can be added separately. Although they preserve convexity, they do not preserve Euclidean equilibrium class. Do not turn a statement about normalized hinge profiles into an exclusion of all affine images.

For an explicit rational implementation, each Dj is obtained from the facet inequalities in [internal-source-reference]: if facet m·x<=b has min_f(n·x-h)<0, require (n·p-h)m·v<=b-m·p for all original upper vertices p; if max_f(n·x-h)>0, require -(n·p-h)m·v<=b-m·p for all original lower vertices p. These finitely many exact inequalities give the whole bounded rational polygon, not just a tangent cone.

F is a global height-preserving homeomorphism, with determinant1 on every slab and inverse y-T(n·y). Consequently

V(FK)=V(K),
M(FK)=M(K)+sum_j vj Jj,
Jj=integral_K max(0,n·x-hj) dx=n·Mplus_j-hj Vplus_j.

Thus actual centroid motion is affine in all velocity parameters. For two hinges, the exact relation v2=-(J1/J2)v1 makes the TOTAL first moment constant. This is a whole-body law, not a law for an independently selected cell. Jj>0 at a proper interior height.

If ej old true edges cross the jth plane strictly and fj old maximal facets are cut into two nonempty relative interiors, Vnew<=Vold+sum ej and Fnew<=Fold+sum fj. Euler gives Enew<=Eold+sum(ej+fj). Flattening or coplanar mergers can only lower this upper bound. No integration diagonal is counted as an edge.

## 2. Exact truncated-linear moment formula
The supplied endpoint verifier computes each J twice. One computation integrates the exactly clipped upper polytope. The other uses every oriented tetrahedron (0,a,b,c) in a facet triangulation. Set zi=n·xi for its four vertices, f(t)=(t-h)_+^4. Its contribution is Vtet*f[z0,z1,z2,z3]/4, where brackets are confluent divided differences. Repeated knots use f^(r)(z)/r!; at z=h all derivatives through order3 exist and equal0. The formula follows by three repeated applications of the fundamental theorem of calculus on the standard simplex: the divided difference equals the simplex integral of f'''=24(t-h)_+, while the tetrahedron Jacobian is6Vtet. Oriented tetrahedra permit any origin; the endpoint's independent clipped-positive-tetrahedron computation checks the resulting value exactly.

## 3. Concrete physical body and current landscape
Use the integer T43 coordinates from the dependency, then divide by1000 AFTER applying F. Take
n=(1109015,-1001188,-321285), h1=-881234080, h2=597414158.
The cut planes contain old true edges[0,11] and[24,29], respectively, and cross2/4 other edges. They split3/5 old facets. Hence E<=123+2+4+3+5=137, achieved by this endpoint.

The source computes exact J1,J2, takes the two common mass-neutral cone rays
(3502706519,3218994175,2059653361),
(498651322049,297849789535,793090747583),
scales each to the first boundary of BOTH exact single-hinge domains under the linked velocities w,-(J1/J2)w, then uses amplitude1/12 on each scaled ray. This completely determines the exact rational body. All convexity slacks are checked. The full two-parameter simplex of nonnegative amplitudes with sum<=1 is globally convex and mass-neutral; ONLY the nominated 1/12,1/12 endpoint has a complete mechanical census here.

Executed exact endpoint:
- V49/E137/F90,C274,own S2/U2/H2,additional weak000,primitive zero000.
- Volume 11420873431/6000000000, exactly unchanged.
- Centroid (-401851815357/4568349372400,-296228326389/1427609178875,10735281965769/45683493724000), exactly unchanged.
- One P bar depth .5339905490324327 and one Q bar depth .6510356958639293; original T43 depths .5341742685943558 and .655896727661406. Decimal depths are displays of exact fractions reconstructed in the ledger.
- Canonical U26/31; stable faces23=[7,26,31],41=[17,31,23]; H edges0–5 and31–46. Stable faces still contain elderU31.
- P root26->31,component11/cut34,attaining edge0–5,path[26,3,0,5,7,31]. Q root41->23,component48/cut29,attaining dual edge56–79; full path and every cut edge are in the regenerated ledger.
- Coordinate denominator maximum327bits, centroid denominator maximum46bits. Low-complexity mass arithmetic is distinct from low coordinate arithmetic.
- Primitive signs negative/zero/positive: edge[197,0,351],side[110,0,164],all-vertex cones[2112,0,240].

## 4. Durable recovery and receipts
Dependency: the COMPLETE finite_hinge_exact.py in [internal-source-reference], material SHA d62d046640d6365501698bb41185ba3e351e043f8935a5c0a02bd3654d2deb00. Its standalone source is12917bytes,SHA5efb192313d80dbfa4dcea4f14187464bae76c07c5f058dfb853ee8e9e0e4154. It contains every literal T43 row, hull/true-incidence integration, strict and additional-weak census, exact positive P/Q reconstruction and helpers. Supply that complete material with this one to any computational successor. No FULL76, old sandbox, NumPy, SciPy or optimizer is required.

Save the exact block below as mass_neutral_exact.py:4926bytes,SHA256 edaf0c4d39fa72306d6045e93360de57ffdeca8d8939befcd7ce11ee6c0fd5e1. Run python -B -S mass_neutral_exact.py alongside the dependency. Coordinator actually executed under CPython3.13.5, standard library only. Expected marker GLOBAL_MASS_NEUTRAL_HINGE_EXACT_PASS [49,137,90] [2,2,2] [0,0,0]. Full output mass_neutral_39_exact.json:93316bytes,SHA256 43303d9ed89e29f8dcd4ced0f1b710000f757f46acf227e2170f59cb92c151a1. It reconstructs physical vertices/supports/true incidence, actual V/M/c, all positive bars and their cuts/paths, and both upper-mass crosschecks. These are exact rational checks and analytic proofs, not proof-assistant verification.

```python
"""Complete rational global two-hinge mass-neutral T43 reconstruction.
Requires only the preserved finite_hinge_exact.py source unit in the same directory.
No numerical optimizer or originating sandbox is needed.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
from itertools import combinations
import json,hashlib
from finite_hinge_exact import P,hull,moments,dot,cross,sub,add,scale,controls,primitive_plane,complex_from_supports,integrate,census,barcode,rational

def dd4(knots,h):
    z=sorted(map(F,knots));table=[max(F(0),x-h)**4 for x in z]
    for order in range(1,4):
        result=[]
        for i in range(len(z)-order):
            if z[i+order]==z[i]:
                v=F(factorial(4),factorial(4-order)*factorial(order))*max(F(0),z[i]-h)**(4-order)
            else:v=(table[i+1]-table[i])/(z[i+order]-z[i])
            result.append(v)
        table=result
    return table[0]

def hinge_integral(n,h,faces):
    out=F(0)
    for ids,m,b in faces:
        a,c,d=[P[i] for i in ids];vol=F(dot(a,cross(c,d)),6)
        out+=vol*dd4([0,dot(n,a),dot(n,c),dot(n,d)],h)/4
    assert out>0
    return out

def main():
    n=(1109015,-1001188,-321285);heights=(-881234080,597414158)
    rays=[(3502706519,3218994175,2059653361),(498651322049,297849789535,793090747583)]
    faces,edges=hull(P);V0,c0=moments(P,faces);z=[dot(n,p) for p in P]
    J=[hinge_integral(n,h,faces) for h in heights];ratio=J[0]/J[1]
    domain=[controls(P,faces,n,h)[2] for h in heights];steps=[]
    for w in rays:
        vv=(w,scale(w,-ratio));limits=[]
        for k in range(2):
            assert dot(n,vv[k])==0
            for (_,m,_),B in zip(faces,domain[k]):
                d=dot(m,vv[k])
                if d>0:limits.append(B/d)
                elif B==0:assert d<=0
        step=min(limits);assert step>0;steps.append(step)
    v1=scale(add(scale(rays[0],steps[0]),scale(rays[1],steps[1])),F(1,12));vel=(v1,scale(v1,-ratio))
    assert add(scale(vel[0],J[0]),scale(vel[1],J[1]))==(0,0,0)
    slacks=[]
    for k in range(2):
        ss=[B-dot(m,vel[k]) for (_,m,_),B in zip(faces,domain[k])];assert min(ss)>=0;slacks.append(ss)
    def image(p):
        out=tuple(map(F,p))
        for h,v in zip(heights,vel):out=add(out,scale(v,max(F(0),dot(n,p)-h)))
        return out
    cp=[];upper=[]
    for h in heights:
        zz=[t-h for t in z]
        cc=[tuple(F(zz[i]*P[j][a]-zz[j]*P[i][a],zz[i]-zz[j]) for a in range(3)) for i,j in edges if zz[i]*zz[j]<0]
        cp.extend(cc);up=[tuple(map(F,p)) for p,t in zip(P,z) if t>=h]+cc
        pp=[primitive_plane(m,b) for ids,m,b in faces]+[primitive_plane(scale(n,-1),-h)]
        ux,uf,un,ue=complex_from_supports(up,pp);uv,um,uc=integrate(ux,uf)
        assert dot(n,um)-h*uv==J[len(upper)]
        upper.append(dict(volume=uv,moment=um))
    points=[image(p) for p in list(P)+cp];planes=[]
    intervals=[(None,heights[0]),(heights[0],heights[1]),(heights[1],None)]
    for ids,m,b in faces:
        lo=min(z[i] for i in ids);hi=max(z[i] for i in ids)
        for slab,(lower,upper_limit) in enumerate(intervals):
            if upper_limit is not None and lo>=upper_limit:continue
            if lower is not None and hi<=lower:continue
            W=(F(0),)*3;B=(F(0),)*3
            for k in range(slab):W=add(W,vel[k]);B=sub(B,scale(vel[k],heights[k]))
            planes.append(primitive_plane(sub(m,scale(n,dot(m,W))),b+dot(m,B)))
    X,ff,pl,ee=complex_from_supports(points,planes);V,M,c=integrate(X,ff)
    assert V==V0 and c==c0 and M==scale(c0,V0)
    audit=census(X,ff,pl,ee,c)
    PX=[scale(sub(x,c),F(1,1000)) for x in X];QX=[scale(p[:3],F(1000)/(p[3]-dot(p[:3],c))) for p in pl]
    audit.update(name='T43_MASS_NEUTRAL_TWO_HINGE_39',VEF=[len(X),len(ee),len(ff)],C=2*len(ee),
                 volume=V/10**9,centroid=scale(c,F(1,1000)),moment=scale(M,F(1,10**12)),
                 exact_mass_preserved=True,vertices=[scale(x,F(1,1000)) for x in X],facets=ff,edges=sorted(ee),
                 support_planes=[primitive_plane(scale(p[:3],1000),p[3]) for p in pl],
                 P=barcode(PX,sorted(ee)),Q=barcode(QX,sorted(tuple(sorted(a)) for a in ee.values())),
                 normal=n,heights=heights,velocities=vel,rays=rays,steps=steps,amplitudes=[F(1,12),F(1,12)],
                 hinge_integrals=J,convexity_slacks=slacks,upper_mass_crosschecks=upper)
    assert len(audit['P'])==audit['strict_counts'][1]-1 and len(audit['Q'])==audit['strict_counts'][0]-1
    raw=(json.dumps(rational(audit),sort_keys=True,separators=(',',':'))+'\n').encode();dest=Path(__file__).with_name('mass_neutral_39_exact.json');dest.write_bytes(raw)
    print('GLOBAL_MASS_NEUTRAL_HINGE_EXACT_PASS',audit['VEF'],audit['strict_counts'],audit['additional_weak_counts'],
          [float(b['depth']) for b in audit['P']],[float(b['depth']) for b in audit['Q']],len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':main()
```
