# figure-0586

Historical AI scientific report · saved 2026-09-28 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# NF93 — a finite-cut obstruction requiring a new stable carrier and a substantial cut

Transaction `ae1fd3ff685f558d24704461`; branch `[internal-source-reference]`; Nimble Finch 93.

## Result and acceptance boundary

**No new exact own110/additionalweak000 endpoint is promoted.** The new result is a necessary-condition certificate for finite halfspace surgery on three exact R82 images. It is not another birth certificate and does not exclude the full projective/affine/new-support family.

For each of the fixed exact seeds **R82**, **BUFFER**, and **BIRTH43**, let K denote that seed and g_K its actual uniform-volume centroid. Let L be any full-dimensional intersection of K with additional halfspaces, and suppose its **actual new uniform-volume centroid** c satisfies

`||c − g_K||∞ ≤ 1/2048`.

The certificate gives two conclusions:

1. **With at most nine additional halfspaces, a sole strict stable equilibrium with no additional weak stable equilibria cannot lie on any old facet.** This permits arbitrary retirement of old facets, new intersection vertices, new adjacency, and changes of equilibrium labels. It is not restricted to an old witness policy.
2. **With at most three additional halfspaces, a sole stable facet must be new and must cut strictly inside 68/75 of the old body’s centred inradius about c.** Thus it must penetrate the old centred inscribed ball by more than **7/75 of its radius**, or approximately **9.33%**. The code also gives a positive rational lower bound on the volume that must be removed.

Consequently, in this centre neighbourhood, keeping old facet18 as the eventual sole S and trying to connect the other basin to it using three new polar vertices cannot complete the task. A successful near-centred three-cut construction must instead install a **new sole stable carrier**, retire both old stable roots as terminal roots, and accommodate a finite—not infinitesimal—cut into the old inscribed ball.

These conclusions do **not** assert that the required cut or its mass compensation is feasible. They also do not prohibit a successful construction whose actual centroid leaves the stated cube or whose projectivity differs from the three fixed maps checked here.

## Sources and distinct starting objects

The complete new journal was read through EOF:323208 bytes, SHA-256 `fed7c7cefe542a6e5af0665f6e69a4c651ed9e48e332d9a6f2351ff5e69038c6`. The unchanged exact sources and results remain those supplied earlier in this chat:

- `figure-0581`, SHA-256 `f4d4df1390c5e9bd18047aad823f3cd12e8c85751a66dbfc62ae50f67c779461`.
- `figure-0582`, SHA-256 `a3072e33bc5eac5dada0e55a6b4430fba0140e447e3dfa86c86e886588ac9626`.

The required geometric input is the complete82-row `KH93_C434_R82_G6.txt`,1888 bytes, SHA-256 `9765712b5ffaa464ed4d677974256294c6d867b77fe77b930d166853f66a92a7`. Its rows mean `n·x ≤ 1000000`. Those rows are literal in the supplied parent. fileciteturn7file0L32-L118

The three seeds used by the certificate retain their existing exact classifications; they are not new constructions:

| Fixed seed | V/E/F | Own strict S/U/H | Additional weak | All positive P | All positive Q depths, decimal presentations |
|---|---:|---:|---:|---|---|
| KH93_C434_R82_G6 |160/240/82|2/1/1|000|[]|.11600403115840405|
| NF93_R82_ORBIT_BUFFER_G12 |160/240/82|2/1/1|000|[]|.11601261582503426|
| NF93_R82_ORBIT_BIRTH43_G12 |160/240/82|3/1/2|000|[]|.11616939941430654; 6.686788244330881e-10|

In particular, the small BIRTH43 bar is still positive. Its disappearance alone would not remove the original surviving Q branch. The original R82 stable input facets7/18 and physical vertex7 are different index domains. fileciteturn6file0L109-L120

J99’s separate F99 body is not used. Neither its geometry nor a three-cut edge guarantee is imported into this calculation.

## Why arbitrary cuts do not evade the old-point obstruction merely by deleting facets

Translate the proposed child’s actual centroid c to the origin. Write the old polar points as

`q_i(c) = H_i / (1 − H_i·c)`,

where the fixed seed is described by `H_i·x ≤ 1`. All denominators are positive because c is interior to L and hence interior to K.

Appending k physical halfspaces gives

`(L − c)* = conv((K − c)* ∪ {w_1,…,w_k})`.

An old supporting plane may become redundant, but its old polar point remains a point of this enlarged convex hull. Removing its facet label therefore does not remove the point from the geometric argument.

Assume L has one strict S and no additional weak S. Its polar then has one strict unstable vertex and no weak unstable vertices. Every non-root extreme vertex has a strictly positive outgoing radial chord. For an old point that is no longer extreme, a convex-combination representation supplies a first chord to an extreme vertex with nonnegative radial score. A nonnegative chord between distinct points still strictly increases squared radius:

`|v|² − |u|² = 2u·(v − u) + |v − u|² > 0`.

Thus every old point has a finite radius-increasing path to the sole polar root. This argument does not require the old point to remain a vertex, nor does it prescribe the new hull’s adjacency.

For a chain with n nonnegative radial links, endpoint radius ratio R and endpoint angular separation φ, the necessary inequality is

`1 ≤ R cos(φ/n)^n`.

Indeed each link gives `r_previous ≤ r_next cos θ`, all link angles are below π/2, spherical triangle inequalities give `Σθ ≥ φ`, and concavity of log cos bounds the product. A shorter chain can be padded with zero-angle links when applying a fixed link-count upper bound.

## The exact angular and radial data

The source checks the following inequalities throughout the **closed** centroid cube of radius1/2048 for each of the three fixed seeds. Radii and angles in this section are those of the old polar points at the variable point c, not values at a substituted nominal centre.

| Old input point | Radius relative to q7 | Angular separation from q7 |
|---|---|---|
|18|strictly between13/10 and34/25|strictly greater than5/2 radians|
|33,79,80|strictly less than11/10|strictly greater than2 radians|
|Every other old point except7|strictly less than1|not needed|

These bounds also make18 the unique largest-radius old polar point throughout the cube.

The ten-link obstructions use the exact rational inequalities

`(34/25) (5953/6144)^10 < 1`,

`(11/10) (14701/15000)^10 < 1`.

Here5953/6144 and14701/15000 are Taylor upper bounds for cos(1/4) and cos(1/5), respectively. The angular lower bounds are checked without floating angles or square roots: a negative dot product and a squared rational inequality place the normalized dot product below a rational lower bound for the relevant cosine.

Suppose the radius-increasing path from old point7 first reaches another old point. That point must be one of18,33,79,80. Before it, every intermediate extreme point must be new. With at most nine appended halfspaces, that prefix has at most ten links. The displayed inequalities forbid every such prefix.

The sole polar root cannot be old point7 either, because old point18 has strictly greater radius and remains a point of the polar hull. Therefore **the sole polar root, and hence the sole physical stable facet, must be new**.

This is a whole-old-point-set obstruction. It survives old-facet deletion, root turnover, and new incidence. It is not a statement about only the original persistence birth label.

## Three cuts require a finite inward penetration

Now assume k≤3 and let w be the new sole polar root.

The path from q7 to w cannot pass through any other old point: its first such old point would give a forbidden prefix of at most four links. Its path therefore uses only new points and has at most three links. Since q18 is the largest-radius old point, its path to w likewise uses only new points and has at most three links.

Let α be the angle from q7 to w and β the angle from q18 to w. The two radial-chain inequalities give

`r7 ≤ |w| cos(α/3)^3`,

`r18 ≤ |w| cos(β/3)^3`.

Assume for contradiction that `|w| ≤ (3/2) r7`. The exact Taylor bounds in the source prove

`cos(31/60)^3 < 2/3`,

`cos(19/60)^3 < 13/15`.

The first chain then requires `α < 31/20`. Since `r18 > (13/10) r7`, the second requires `β < 19/20`. But this contradicts

`angle(q7,q18) ≤ α + β < 5/2`.

Therefore

`|w| > (3/2) r7`.

Using `r18 < (34/25) r7` gives

`|w| / r18 > 75/68`.

Let R(c) be the radius of the largest ball **centred at c** contained in the old seed K. Because18 is the largest old polar radius,

`R(c) = 1/r18`.

The new sole stable plane is at distance `h_new = 1/|w|` from c, so

`h_new < (68/75) R(c)`.

This does not compare unrelated facet directions or assume that the new facet is parallel to old18. It says that the new plane cuts into the old centred inscribed ball itself.

### A physical removed-volume consequence

The removed region contains a spherical cap of that old ball with height greater than `7R(c)/75`. Consequently,

`Vol(K \ L) > π (10682/1265625) R(c)^3`.

Only one compulsory cap is used, so there is no summation of overlapping hypothetical cuts.

For a uniform rational bound over the entire centroid cube, the source uses

`R_lower = [1 − H18·g_K − ρ ||H18||1] / norm_upper(H18)`,

where `ρ=1/2048` and norm_upper is an exact rational upper bound for the Euclidean norm. Since π>3,

`Vol(K \ L) > (10682/421875) R_lower^3`.

The program reports this exact rational bound and its ratio to the actual old uniform volume. This is a necessary removal amount, **not** a certificate that the other cuts can balance the removed first moment or retain U1.

## What the result changes in the constructive search

The original two-S policy retaining elder18 as the eventual sole stable facet is not merely numerically difficult in the certified region: with three appended halfspaces, it is geometrically incompatible with weak-free S1. Tiny cuts that leave the new nearest support outside68/75 of the old centred inradius also cannot complete S1 there, even when they change the BIRTH43 saddle structure.

A constructive continuation should therefore allow a new cut facet to become the sole stable carrier and allow **both** old7 and old18 to cease being terminal roots. If the actual centroid is kept near the seed’s centroid, the new carrier needs the finite penetration proved above. The other cuts and projective parameters must then accommodate the full new uniform first moment. Alternatively, an actual centroid excursion outside the cube or a different projectivity can escape the certificate’s hypotheses; neither is excluded.

The intended live-mass plane-insertion and projective scouting was not converted into a new durably audited110 endpoint in this continuation. Exploratory floating root counts, reduced Q values, and unpromoted checkpoints are not used as exact conclusions here. No whole optimization path is claimed certified. In particular, no disappearance of the small BIRTH43 bar is reported as completion.

## Scope limits

The certificate concerns **three fixed exact seed images** and arbitrary appended halfspaces with the child’s actual centroid in the specified cube. It does not cover every A,b in the previous uncut projective box, much less the full orbit. A different literal rational map can be checked by the same inequalities, but inheritance is not automatic.

It does not prove that all three-cut children have S≥2: a sole **new** stable facet remains an open possibility. It excludes S1 on an old facet and supplies a necessary finite-depth condition for a new one. The nine-cut threshold, cube radius and68/75 constant are sufficient certified bounds, not optimality claims.

The statement needs only S1/no-weak-S to derive its obstruction. It therefore applies to a proposed110/weak000 target, but it does not itself prove U1, exclude weak U/H, or provide a final full census for any newly cut body. Those remain endpoint acceptance requirements.

For the actual assigned82-facet family, at most three appended halfspaces still give F≤85 and E≤249 for every surviving full-dimensional intersection. The cut gate neither changes nor strengthens that combinatorial guarantee.

## Complete exact recovery unit

The only geometric input needed by this unit is the unchanged1888-byte R82 H file identified above. The two exact projective/affine maps are included literally. The code reconstructs the old maximal facets, integrates the actual homogeneous mass of each image, verifies the complete closed-cube inequalities, and emits the full rational certificate.

Save as `NF93_CUT_GATE.py` and run:

```sh
python NF93_CUT_GATE.py KH93_C434_R82_G6.txt
```

Expected terminal marker:

```text
NF93_FEW_CUTS_NEW_STABLE_CARRIER_AND_DEPTH_CERTIFIED
```

The output is `NF93_CUT_GATE_CERT.json`. The program prints its byte count and SHA-256, together with the source byte count/SHA-256. Assertions must remain enabled. Python3.11 or later and the standard library suffice; no numerical optimizer or new external research source is required.

```python
'''Exact few-cut stable-carrier and finite-depth gate for three fixed R82 images.
Python 3.11+ standard library; input is the unchanged 82-row parent H file.
No optimization, selected reference-centroid substitution, or bar tolerance.
'''
from fractions import Fraction as Q
from itertools import combinations
from functools import cmp_to_key
from pathlib import Path
import argparse, hashlib, json, math, sys
if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)
PARENT_SHA = '9765712b5ffaa464ed4d677974256294c6d867b77fe77b930d166853f66a92a7'
RHO = Q(1, 2048)
D12 = 10**12
MAPS = [
 ('R82', [0,0,0], [[D12,0,0],[0,D12,0],[0,0,D12]]),
 ('BUFFER', [-4641661,14544682,15933638],
  [[999999876029,9471659,-318407],[0,1000000829662,-9622288],[0,0,999999294309]]),
 ('BIRTH43', [-72670400,326347079,222805411],
  [[1000040061449,176516264,-5973064],[0,999988291884,-143098423],[0,0,999971647940]])
]
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(a,t): return tuple(x*t for x in a)
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def apply(A,x): return tuple(dot(row,x) for row in A)
def inverse(A):
    d=det(*A); assert d>0
    col=[mul(cross(A[1],A[2]),1/d),mul(cross(A[2],A[0]),1/d),mul(cross(A[0],A[1]),1/d)]
    return tuple(tuple(col[j][i] for j in range(3)) for i in range(3))
def exact_hull(N,D):
    points=set()
    for i,j,k in combinations(range(len(N)),3):
        c0,c1,c2=cross(N[j],N[k]),cross(N[k],N[i]),cross(N[i],N[j])
        den=dot(N[i],c0)
        if not den: continue
        num=mul(add(c0,add(c1,c2)),D)
        if den<0: den=-den;num=mul(num,-1)
        if any(dot(n,num)>D*den for n in N): continue
        points.add(tuple(Q(t,den) for t in num))
    X=sorted(points); faces=[]
    for n in N:
        ids=[i for i,x in enumerate(X) if dot(n,x)==D]
        assert len(ids)>=3
        c=mul(tuple(map(sum,zip(*(X[i] for i in ids)))),Q(1,len(ids)))
        drop=max(range(3),key=lambda k:abs(n[k]));axes=[k for k in range(3) if k!=drop]
        v={i:tuple(X[i][k]-c[k] for k in axes) for i in ids}
        def half(a): return 0 if a[1]>0 or (a[1]==0 and a[0]>=0) else 1
        def cmp(i,j):
            if i==j:return 0
            a,b=v[i],v[j];ha,hb=half(a),half(b)
            if ha!=hb:return -1 if ha<hb else 1
            z=a[0]*b[1]-a[1]*b[0]
            if z:return -1 if z>0 else 1
            return -1 if dot(a,a)<dot(b,b) else 1
        f=sorted(ids,key=cmp_to_key(cmp))
        orient=dot(cross(sub(X[f[1]],X[f[0]]),sub(X[f[2]],X[f[0]])),n)
        assert orient
        if orient<0:f=f[::-1]
        faces.append(f)
    edges={}
    for f in faces:
        for a,b in zip(f,f[1:]+f[:1]):edges.setdefault(tuple(sorted((a,b))),[]).append((a,b))
    assert all(len(e)==2 and e[0]==e[1][::-1] for e in edges.values())
    assert (len(X),len(edges),len(faces))==(160,240,82)
    assert {i for f in faces for i in f}==set(range(len(X)))
    return X,faces

def mass(X,faces):
    W=Q(0);M=(Q(0),)*3
    for f in faces:
        for j in range(1,len(f)-1):
            a,b,c=X[f[0]],X[f[j]],X[f[j+1]];w=det(a,b,c)
            assert w>0
            W+=w;M=add(M,mul(add(a,add(b,c)),w))
    return W/6,mul(M,1/(4*W))

def cos_polynomial(x,n):
    return sum((-1)**j*x**(2*j)/math.factorial(2*j) for j in range(n+1))

def sqrt_upper(q,grid=10**12):
    # An exact rational upper bound for sqrt(q), without a floating square root.
    a=q.numerator*grid*grid;b=q.denominator
    k=math.isqrt(a//b)
    while k*k*b<a:k+=1
    return Q(k,grid)

def certificate(H,g,V):
    n2=[dot(n,n) for n in H];a=[1-dot(n,g) for n in H]
    l1=[sum(map(abs,n)) for n in H]
    lo=[x-RHO*y for x,y in zip(a,l1)];hi=[x+RHO*y for x,y in zip(a,l1)]
    assert min(lo)>0
    far={18:Q(34,25),33:Q(11,10),79:Q(11,10),80:Q(11,10)}
    gaps=[]
    for j in range(len(H)):
        if j==7:continue
        R=far.get(j,Q(1))
        gap=R*R*n2[7]*lo[j]**2-n2[j]*hi[7]**2
        assert gap>0,(j,'radius upper bound')
        gaps.append(gap)
    # This stronger lower bound also makes 18 the largest old polar radius.
    elder_gap=n2[18]*lo[7]**2-Q(13,10)**2*n2[7]*hi[18]**2
    assert elder_gap>0
    angular=[]
    for j,R in far.items():
        theta=Q(5,2) if j==18 else Q(2)
        L=cos_polynomial(theta,5) if j==18 else -Q(19,45)
        gamma=dot(H[7],H[j]);angular_gap=gamma*gamma-L*L*n2[7]*n2[j]
        assert gamma<0 and L<0 and angular_gap>0
        C=Q(5953,6144) if j==18 else Q(14701,15000)
        assert R*C**10<1
        angular.append(dict(old=j,angle_lower=str(theta),radius_ratio_upper=str(R),
                            cosine_lower=str(L),angular_gap=str(angular_gap),
                            ten_link_product_upper=str(R*C**10)))
    # Three-link paths to a common new root cannot have radius <= 3*r_7/2.
    U7=cos_polynomial(Q(31,60),2)
    U18=cos_polynomial(Q(19,60),2)
    assert 0<U7<1 and U7**3<Q(2,3)
    assert 0<U18<1 and U18**3<Q(13,15)
    # A compulsory cap of the old inscribed ball is removed. pi > 3.
    radius_lower=lo[18]/sqrt_upper(n2[18])
    removed_lower=Q(10682,421875)*radius_lower**3
    return dict(closed_centroid_cube_radius=str(RHO),centroid=list(map(str,g)),
                volume=str(V),minimum_radius_upper_gap=str(min(gaps)),
                elder_13_over_10_gap=str(elder_gap),angular=angular,
                three_link_cosine_upper_7=str(U7),three_link_cosine_upper_18=str(U18),
                required_new_root_radius_over_junior_lower='3/2',
                required_new_face_distance_over_old_inradius_upper='68/75',
                old_inradius_uniform_rational_lower=str(radius_lower),
                removed_volume_uniform_rational_lower=str(removed_lower),
                removed_fraction_uniform_rational_lower=str(removed_lower/V))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('input',nargs='?',default='parent/KH93_C434_R82_G6.txt')
    ap.add_argument('--output',default='NF93_CUT_GATE_CERT.json')
    args=ap.parse_args();raw=Path(args.input).read_bytes()
    assert len(raw)==1888 and hashlib.sha256(raw).hexdigest()==PARENT_SHA
    t=list(map(int,raw.split()));m,D=t[:2];assert m==82 and D==1000000 and len(t)==2+3*m
    N=[tuple(t[2+3*i:5+3*i]) for i in range(m)];Y=[mul(n,Q(1,D)) for n in N]
    X,faces=exact_hull(N,D);out={}
    for name,bi,Ai in MAPS:
        b=tuple(Q(v,D12) for v in bi);A=tuple(tuple(Q(v,D12) for v in row) for row in Ai)
        inv=inverse(A);den=[1+dot(b,x) for x in X];assert min(den)>0
        Z=[mul(apply(A,x),1/d) for x,d in zip(X,den)]
        H=[tuple(sum((y[k]+b[k])*inv[k][j] for k in range(3)) for j in range(3)) for y in Y]
        for i,f in enumerate(faces):
            on=set(f)
            assert all(dot(H[i],z)==1 if j in on else dot(H[i],z)<1 for j,z in enumerate(Z))
        V,g=mass(Z,faces);r=certificate(H,g,V)
        r.update(VEF=[160,240,82],projective_denominator_min=str(min(den)),
                 b=list(map(str,b)),A=[list(map(str,row)) for row in A])
        out[name]=r
    obj=dict(parent_sha256=PARENT_SHA,scope='fixed images; arbitrary appended halfspaces; actual child centroid in the specified cube',
             nine_cut_conclusion='A sole weak-free stable facet cannot be an old facet.',
             three_cut_conclusion='The sole stable facet is new and cuts inside 68/75 of the old centered inradius.',
             images=out)
    data=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode()
    p=Path(args.output);p.write_bytes(data)
    print('NF93_FEW_CUTS_NEW_STABLE_CARRIER_AND_DEPTH_CERTIFIED')
    print('OUTPUT',len(data),hashlib.sha256(data).hexdigest())
    src=Path(__file__).read_bytes();print('SOURCE',len(src),hashlib.sha256(src).hexdigest())
    for name,r in out.items():
        print(name,'rho',r['closed_centroid_cube_radius'],'removed fraction lower',float(Q(r['removed_fraction_uniform_rational_lower'])))
if __name__=='__main__':main()
```

Convenience copies: [source/input recovery bundle](sandbox:/mnt/data/NF93_CUT_GATE_RECOVERY.zip), [the complete source unit](sandbox:/mnt/data/NF93_CUT_GATE.py), and [source/output manifest](sandbox:/mnt/data/NF93_CUT_GATE_MANIFEST.json).

The [exploratory working snapshot](sandbox:/mnt/data/NF93_FEW_CUTS_WORKING_RECOVERY.zip) is separate. Its numerical checkpoints are unpromoted and must not be treated as exact successors to the literal R82/BUFFER/BIRTH43 parents. The promoted conclusion of this handoff is the explicitly scoped finite-cut carrier/depth obstruction, not a new110 body.
