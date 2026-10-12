# figure-0620

AI research report · 2026-09-29 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Keen Harbor 93 — a projective interface construction, its exact complexity obstruction, and finite mass transfer by retiring supports

## 1. Status and evidence boundary

**No new own110/additionalweak000 endpoint is established. No new KH128 successor is promoted in this handoff.** The exact COMPRESSED36 parent remains128/211/85, own121, with one positive P≈0.17714080146714686 and Q[].

The new work is analytical. It identifies a finite, coherent way to compress an entire side of a separating plane, proves that its straightforward retained-support implementation costs **46 true edges on the literal COMPRESSED36 neck**, and gives a replacement-support implementation that avoids that cost while transferring actual material across the interface. The latter admits a direct boundedness certificate and uses at most the original85 support rows, so it has E≤249 without assuming that the31 old common apices survive.

Three fully specified rational controls demonstrate the geometric and homogeneous-mass effects. They are **method controls, not S1 research frontiers**. Their volumes, centroids, strict/weak classifications and every positive P/Q are derived below. A complete standard-library producer/verifier is included. It was submitted for execution, but its output and exit status were not available for inspection in this continuation. Consequently, **no observed execution marker, output hash, cold replay, or numerical search result is claimed**.

### Current source-reading limitation

The retained receipt identifies the current journal as464066 bytes, SHA-256 `3c1bddf089aa565f11289b247ce79fd3db780744b3afd384683fc43603948329`. The retained complete consecutive reading reaches native line1380. Requests for1381 onward and direct runtime probes did not provide text I could inspect; **1381–EOF is not claimed read here**. This is not a finding that the file or previous workspaces were lost.

The mathematical application below uses the already supplied complete literal KH128 parent, `figure-0615`, SHA-256 `9f3dd573897ca4f688ea3e60b5d377809238243ea786a1ffe039e1703c6f1e3a`, as its working premise. No scientific assertion is taken from the unread tail, and duplication with an unread update is not ruled out.

## 2. A coherent finite compression of one whole half-body

Let K be a rational bounded full-dimensional polytope,

`K={x:n_i·x≤h_i}`.

Choose a separating plane

`φ(x)=ℓ·x−h=0`,

with section D=K∩{φ=0}, and a rational pivot p strictly inside D. For t>0 define

`T_(t,p)(x)=p+(x−p)/(1+tφ(x))`.

Apply this map only to K_+=K∩{φ≥0}, leaving K_−=K∩{φ≤0} unchanged:

`L_ret(t,p)=K_− ∪ T_(t,p)(K_+)`.

This is not an arbitrary vertex displacement. It fixes the entire interface pointwise, preserves the projective incidence of the upper half, and moves every strictly upper point toward p. It has the exact convex halfspace description

`L_ret(t,p)={x:n_i·x≤h_i, (n_i+tH_iℓ)·x≤h_i+tH_i h for every i}`,

where

`H_i=h_i−n_i·p>0`.

Below the interface the new inequality is weaker than the old one; above it, the new inequality is stronger. The body is therefore convex, full-dimensional, bounded and contained in K. The pivot is an interior point used to define geometry, **not its prescribed centroid**.

For every finite t>0, the image of an upper vertex remains a genuine vertex when p is strictly interior to D. Passing to t=∞ is a different limiting body, not a finite member whose small edges may be ignored.

### The literal COMPRESSED36 neck makes this implementation too expensive

Use the parent's exact plane

`1064521 x−499671 y−166046 z=509293`.

It meets no parent vertex and intersects exactly23 true edges:

```text
[51,92] [112,113] [52,88] [80,103] [80,120] [76,127]
[36,84] [43,111] [58,81] [21,81] [8,82] [43,82]
[17,78] [0,78] [17,84] [122,124] [126,127]
[55,85] [55,125] [0,85] [26,110] [55,77] [55,121]
```

A transverse section of this kind is a genuine23-gon and crosses23 maximal facets. Each crossing edge gains one degree-four interface vertex. Each crossing facet splits into two maximal facets. Hence, for every finite t>0 and every strictly interior pivot,

`ΔV=23, ΔF=23, ΔE=46`.

The actual family therefore has

**V151/E257/F108.**

The parent surplus38 increases to61 because of the23 new degree-four vertices; indeed `3·108−6−61=257`. Counting a triangulation or silently releasing the old common incidences would not change this conclusion.

This gives a complete complexity exclusion for this particular finite family: **it cannot meet E249**, regardless of its equilibrium census or mass behaviour. At least eight more old edges must be saved before using this interface unchanged, or the interface must satisfy a smaller count. In the general case, including a plane through old vertices, the relevant exact formula is

`E_new=E_old+c+f_cross`,

where c is the number of new edge-interior intersection vertices and f_cross is the number of old maximal facets actually split. The target here is `c+f_cross≤38`, not merely a small number of submitted planes.

There is a second concrete coupling. The crossed edge112–113 is the parent's saddle edge and belongs to stable facet17. Thus this interface **also splits the original stable20-gon**. It cannot be described as moving the P side while leaving that entire stable carrier unchanged.

These conclusions use the literal parent incidence data, not a new numerical hull calculation. They do not exclude a different plane, boundary pivots with separately established incidences, support retirement, or simultaneous changes elsewhere.

## 3. Retiring the old rows avoids the seam cost and changes the physical mass mechanism

Instead of keeping both an old plane and its rotated copy, retain a set I of old rows and replace the others:

`n_i(t)=n_i, h_i(t)=h_i` for i∈I;

`n_i(t)=n_i+tH_iℓ, h_i(t)=h_i+tH_i h` for i∉I.

There are still only m submitted halfspaces. Every one contains p strictly.

### An all-amplitude boundedness certificate

Require

`−ℓ=Σ_(i∈I) α_i n_i`, with α_i≥0.

Then the replacement body is bounded for every t≥0. To see this, suppose v is a recession direction. The retained rows imply ℓ·v≥0. Every rotated row then implies

`n_i·v≤−tH_i ℓ·v≤0`.

Together with the retained rows, v is a recession direction of the original bounded K, so v=0.

Such a retained certificate can always be selected from the original normals of a bounded full-dimensional K. A conic representation in three dimensions uses at most three rows; additional rows may be retained to protect a chosen carrier. Selection and all coefficient checks can be rational.

On COMPRESSED36 this gives a **bounded full-dimensional finite85-row family with E≤249**. The guarantee does not depend on preserving its31 old common apices. It also does **not** certify S1, U1, LOW, or any particular actual E below249. Those remain questions for the new actual hull and mass.

A deterministic starting recipe is available without a new archive: use the literal parent H input; take p as the arithmetic mean of the23 rational section vertices; normalize the displayed plane by10^6; retain the first lexicographic nonsingular triple whose nonnegative conic combination equals −ℓ; replace every other row by the formula above. A chosen t then defines one exact rational intersection. No particular member of this recipe has been classified or promoted here.

### The replacement is a separated gain/loss operation

Every feasible point of the new body above the interface satisfies every original inequality: rotated inequalities are stronger there. Every old point below the interface satisfies every new inequality: rotated inequalities are weaker there. Consequently,

`K_new\K ⊂ {φ<0}`,

`K\K_new ⊂ {φ>0}`,

up to boundaries of zero volume.

Thus there is actual lower-side material gain and upper-side material loss, rather than an unjustified interpretation of a net volume difference. When all facets meeting the upper half are rotated and the retained rows are lower-only, the upper half is exactly `T_(t,p)(K_+)`; only the lower half differs from the retained-support construction.

Let V,g be the original uniform volume and centroid and V_new,g_new the new ones. The separated gain/loss gives the finite moment inequality

**`V_new(h−ℓ·g_new)>V(h−ℓ·g)`**

whenever positive-volume upper material is actually removed. This follows directly by integrating h−ℓ·x: removing upper material removes a negative contribution, and adding lower material adds a positive one.

In particular, when the old centre lies below the plane, keeping its normal coordinate exactly would require **V_new>V**. A pure inward implementation cannot restore that coordinate by tangential pivot motion. A replacement implementation can change the conclusion because of its lower-side gain.

### The first-order mass change is not a rank claim

At a fixed pivot, the normal velocity of a moved old facet is

`v_normal(x)=−H_i φ(x)/|n_i|`.

Therefore

`V′=−Σ_(i∉I) H_i ∫Fi φ(x)/|n_i| dA`,

`M′=−Σ_(i∉I) H_i ∫Fi x φ(x)/|n_i| dA`.

The same facet can contribute inward motion above the plane and outward motion below it. These exact derivatives do not justify adding overlapping finite pyramids; finite endpoints still require their complete hull integral. Section6 supplies a literal finite control in which the actual centroid movement reverses sign when the old crossing rows are retired.

## 4. Actual-centroid steering in the retained model: an exact finite capacity polygon

For the retained-support construction, the upper map has Jacobian

`det DT=(1+tφ)^(−4)`.

Its volume is independent of the tangential pivot:

`V_+(t)=∫_(K_+) (1+tφ)^(−4) dx`.

Its first moment is affine in p:

`M_+(t,p)=A(t)+B(t)p`,

`A(t)=∫_(K_+) x(1+tφ)^(−5) dx`,

`B(t)=∫_(K_+) tφ(1+tφ)^(−5) dx=−t V_+′(t)/4>0`.

Thus, with the unchanged lower first moment M_−,

`g_ret(t,p)=[M_−+A(t)+B(t)p]/[V_−+V_+(t)]`.

All quantities are rational at rational t for a rational polytope: the transformed vertices and their oriented tetrahedral integrals are rational. No numerical quadrature is necessary.

For a fixed t, the entire reachable-centroid set is an explicit homothetic image of the section polygon D. This is a **finite physical capacity region**, not a statement that two derivative columns are independent.

For an unchanged lower stable facet with normal N and a desired interior foot f, put C=M_−+A and V_t=V_−+V_+. The normal coordinate ℓ·g is independent of p:

`a_n=(ℓ·C+B h)/V_t`.

If ℓ·N≠0, exact foot tracking requires

`c_target=f+[(a_n−ℓ·f)/(ℓ·N)]N`,

`p_required=(V_t c_target−C)/B`.

This works only when the resulting p_required lies strictly in D and the chosen facet remains geometrically unchanged. Allowing the foot to vary inside a triangle gives a finite rational polygon-feasibility problem. Keeping an interior foot does not establish S1 elsewhere, and does not establish the LOW inequality against the new actual P death.

These formulas **cannot be transplanted to the replacement-support body's full mass**: its lower half also changes. Only the upper contribution retains the displayed affine dependence when its upper geometry is the same. Ignoring the new lower moment would recreate the reference-centre error this assignment is intended to avoid.

The original COMPRESSED36 S17 crosses the selected interface, so the unchanged-facet hypothesis does not hold for that whole20-gon. On a LOW-platform sibling, the required positional and incidence checks would have to be made on the actual triangle and actual edge budget, not inherited from its S1 count.

## 5. A finite own-mass obstruction at newly created seam vertices

A simple exact family isolates a failure mechanism before applying it to a difficult host.

Start with the octahedron

`K={|x|+|y|+|z|≤1}`,

whose uniform centroid is zero. Use the plane z=1/2 and any pivot

`p=(p_x,p_y,1/2)`, `|p_x|+|p_y|<1/2`.

For every t>0 the retained-support construction creates four genuine seam vertices

`(±1/2,0,1/2), (0,±1/2,1/2)`.

Let

`δ=1/(t+2)`, `k=1−2δ`,

`V_t=5/4+δ/6`,

`λ=δ(1−2δ)/(24V_t)`,

`a=(1−2δ)(5+2δ)/(96V_t)`.

The actual homogeneous centroid is exactly

`g_t=(λp_x,λp_y,−a)`.

In particular `a/λ=(5+2δ)/(4δ)>3`. Tangential pivot motion has too little capacity to remove the downward own-centroid displacement.

Write a seam vertex as s=(s_T,1/2), with |s_T|=1/2. Its radial score toward its old equatorial neighbour is

`−λ p_T·s_T−a/2<0`.

Its scores to its two neighbouring seam vertices are also strictly negative, because λ<1 and |p_x|+|p_y|<1/2.

The transformed upper apex is `(k p_T,1/2+δ)`. The seam-to-apex score is

`C+(k+λ)s_T·p_T−λk|p_T|²`,

where

`C=−1/4+δ(1/2+a)<0`.

The latter strict sign follows from

`−C=(30−61δ+4δ³)/[8(15+2δ)]>0`, for0<δ<1/2.

For either opposite pair of seam vertices, the average of their apex scores is `C−λk|p_T|²<0`. Hence at least one vertex in each opposite pair has every outgoing true-edge score strictly negative.

**For every finite t>0 and every allowed pivot, at least two of the newly created seam vertices are strict U at the actual homogeneous centroid.** This conclusion does not invoke survival of any old root label. This particular retained-support family cannot be ownU1 at any amplitude. At the axial pivot all four seam vertices are strict U.

This is a theorem about the stated octahedral family, not an exclusion of COMPRESSED36, arbitrary projective deformations or support replacement. Its relevance is the mechanism: compressing the upper material and steering a reference pivot can create a complete replacement unstable system at the interface because the physical mass moves differently.

## 6. Three literal rational controls, including a matched finite mass reversal

All controls use t=1 and axial pivots. Their complete inputs, maximal hulls, exact masses and all bars are recoverable from the source in Section8. The classifications here are analytical exact results; they are **not described as observed runtime audits**.

| Control | Mode and plane | True V/E/F | Strict S/U/H | Additional weak | Uniform volume | Own centroid |
|---|---|---:|---:|---:|---:|---|
| RETAIN_H50 |Retain old rows; z=1/2|10/20/12|8/10/16|0/0/0|47/36|(0,0,−17/1128)|
| RETAIN_H75 |Retain old rows; z=3/4|10/20/12|8/6/12|0/0/0|213/160|(0,0,−23/17040)|
| REPLACE_H75 |Retire old upper rows; z=3/4|6/12/8|8/6/12|0/0/0|2197/1440|(0,0,7/240)|

Their first moments are respectively

```text
(0,0,−17/864)
(0,0,−23/12800)
(0,0,15379/345600)
```

RETAIN_H50 consists of the four original equatorial vertices, the south vertex(0,0,−1), the new north vertex(0,0,5/6), and the four seam vertices at z=1/2. Its eight old facet pieces are stable; all ten vertices are unstable. Every edge except the four seam-polygon edges is a strict saddle edge.

RETAIN_H75 instead has north vertex(0,0,19/20) and four seam vertices `(±1/4,0,3/4),(0,±1/4,3/4)`. The seam vertices have positive exits to the north vertex, so only the six outer vertices are U. The eight old facet pieces are S; the12 old lower/equatorial edge carriers are H.

REPLACE_H75 has the literal six vertices

```text
(0,0,−1)
(0,0,19/20)
(13/12,0,1/12)
(−13/12,0,1/12)
(0,13/12,1/12)
(0,−13/12,1/12)
```

All eight triangular facets are stable, all six vertices are unstable and all12 edges are saddles. Thus neither retiring four old planes nor its more favourable mass direction is called cancellation.

### The matched H75 gain and loss are actual separate regions

The two H75 controls have exactly the same upper compressed cap. Retiring the four old crossing planes adds material only below z=3/4. The exact gained volume and first moment are

`V_gain=7/36`, `M_gain=(0,0,5/108)`.

The gain centroid is therefore `(0,0,5/21)`, genuinely below the interface. The removed upper material, measured against the original octahedron, has

`V_loss=1/480`, `M_loss=(0,0,23/12800)`,

and centroid `(0,0,69/80)`, genuinely above it. These are disjoint physical regions, not an interpretation of the final net volume.

The normal own-centroid derivative also reverses sign. For an axial interface z=q on this octahedron,

`g_ret,z′(0)=−(1−q)^4(1+q)/4`,

`g_replace,z′(0)=(1−q)(2q−1)/4`.

At q=3/4 these are **−7/4096** and **+1/32**. The displayed finite endpoints realize the same sign difference. Thus support retirement has an instantiated first-order and finite homogeneous-mass effect, rather than merely an extra linear degree of freedom.

### Every positive bar

The following lists are complete exact rational depth lists. Repeated values represent distinct bars.

```text
RETAIN_H50
P=[1/2,
   636192/1272673,636192/1272673,636192/1272673,
   4/13,
   289/1311314,289/1311314,289/1311314,289/1311314]
Q=[1/3,1/3,1/3,
   7684598/24727923,7684598/24727923,7684598/24727923,
   598418/1909443]

RETAIN_H75
P=[1/2,
   289578289/580724258,289578289/580724258,289578289/580724258,
   234447073/525593042]
Q=[1/3,1/3,1/3,
   144398018/435543987,144398018/435543987,
   144398018/435543987,144398018/435543987]

REPLACE_H75
P=[1/2,200/401,200/401,200/401,16/41]
Q=[1/3,1/3,1/3,16/57,16/57,16/57,4232/11457]
```

There are19 positive P and21 positive Q across these three controls. None is a target candidate, and none replaces the accepted one-sided KH128 bodies.

## 7. What this changes for the actual continuation

The literal23-edge neck cannot be used as a fully retained projective hinge on COMPRESSED36 under E249: its true E is257 at every finite nonzero amplitude. It also cuts the existing stable carrier. This removes a tempting but invalid way to spend the recovered edge reserve.

Retiring rather than duplicating the rotated rows changes both facts. The85-row replacement family can remain bounded and full-dimensional for every finite amplitude by a retained negative-normal conic certificate, without protecting artificial old common-apex identities. Its material gain is on the opposite side of the interface from its loss. The matched control demonstrates that this change can reverse the actual mass response.

For the actual host, however, the remaining task is still substantial: select the retained rows and finite motion so that the **complete current P system** disappears while the actual stable foot and all other facet guards give S1, with a separately checked LOW inequality where LOW is intended. The old S17 plane may rotate unless explicitly retained; retaining a plane does not itself retain its whole polygon or its stable status. On a platform sibling with F>85, the85-row complexity guarantee is unavailable and its actual surviving nonsimple incidences must instead be counted.

No new host-centroid numbers, P/Q lists, accepted numerical trajectories, or successful mass-fitting parameters are supplied for this family. The current analytical result is the exact retained-hinge complexity exclusion, the bounded replacement construction and finite moment relation, and the independently specified control-family obstruction. It is not an own110 record, a full support-space exclusion, or a certificate of an equilibrium homotopy.

## 8. Complete standalone control producer and verifier

Save as `kh93_projective_interface.py` and run:

```bash
python -B -S kh93_projective_interface.py KH93_PROJECTIVE_CONTROLS
```

Only the Python standard library is required. The code exhausts all support triples, supplies conic boundedness certificates, reconstructs maximal facets and true edges, integrates the actual uniform mass from positive tetrahedra twice, computes direct strict/additional-weak S/U/H and both complete persistence lists, and compares every depth with the rational literals above. The vertex mean is only an interior tetrahedral origin, not a substitute mass centre.

It writes full exact reports and a byte/SHA-256 manifest. The expected terminal marker, **not observed in this continuation**, is:

`KH93_PROJECTIVE_INTERFACE_CONTROLS_PASS_3_NO110`.

```python
# Exact finite projective-interface controls. Standard library only.
from fractions import Fraction as R
from itertools import combinations, product
from functools import cmp_to_key
from pathlib import Path
import hashlib
import json
import sys

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def mul(t, a):
    return tuple(t*x for x in a)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def mean(points):
    return tuple(sum(p[k] for p in points)/len(points) for k in range(3))


def cone_certificate(normals, direction):
    for ids in combinations(range(len(normals)), 3):
        a, b, c = [normals[i] for i in ids]
        cs = [cross(b, c), cross(c, a), cross(a, b)]
        d = dot(a, cs[0])
        if not d:
            continue
        weights = [dot(direction, q)/d for q in cs]
        if min(weights) >= 0:
            recovered = tuple(sum(weights[j]*normals[ids[j]][k]
                                  for j in range(3)) for k in range(3))
            assert recovered == direction
            return dict(indices=list(ids), weights=weights)
    return None


def cycle(ids, points, normal):
    ids = list(ids)
    centre = mean([points[i] for i in ids])
    k = next(k for k in range(3) if normal[k])
    a, b = (k+1) % 3, (k+2) % 3
    xy = {i: (points[i][a]-centre[a], points[i][b]-centre[b]) for i in ids}

    def half(v):
        return 0 if v[1] > 0 or (v[1] == 0 and v[0] >= 0) else 1

    def compare(i, j):
        u, v = xy[i], xy[j]
        if half(u) != half(v):
            return -1 if half(u) < half(v) else 1
        z = u[0]*v[1]-u[1]*v[0]
        if z:
            return -1 if z > 0 else 1
        return (i > j)-(i < j)

    ids.sort(key=cmp_to_key(compare))
    if normal[k] < 0:
        ids.reverse()
    q = ids.index(min(ids))
    ids = ids[q:]+ids[:q]
    for i in range(len(ids)):
        p, q, s = [points[ids[(i+j) % len(ids)]] for j in range(3)]
        assert dot(normal, cross(sub(q, p), sub(s, q))) > 0
    return ids


def hull(planes):
    normals = [n for n, h in planes]
    certificates = []
    for j in range(3):
        for sign in (-1, 1):
            u = tuple(R(sign if k == j else 0) for k in range(3))
            cert = cone_certificate(normals, u)
            assert cert is not None, 'No boundedness certificate'
            cert['direction'] = u
            cert['upper_bound'] = sum(w*planes[i][1]
                                      for i, w in zip(cert['indices'], cert['weights']))
            certificates.append(cert)
    vertices = set()
    for ids in combinations(range(len(planes)), 3):
        (a, ha), (b, hb), (c, hc) = [planes[i] for i in ids]
        bc, ca, ab = cross(b, c), cross(c, a), cross(a, b)
        d = dot(a, bc)
        if not d:
            continue
        p = mul(1/d, add(add(mul(ha, bc), mul(hb, ca)), mul(hc, ab)))
        if all(dot(n, p) <= h for n, h in planes):
            vertices.add(p)
    points = sorted(vertices)
    assert len(points) >= 4
    inside = mean(points)
    assert all(dot(n, inside) < h for n, h in planes)
    faces, active, seen = [], [], set()
    for index, (n, h) in enumerate(planes):
        ids = frozenset(i for i, p in enumerate(points) if dot(n, p) == h)
        if len(ids) < 3 or ids in seen:
            continue
        seen.add(ids)
        faces.append(cycle(ids, points, n))
        active.append(index)
    edges, orientation = {}, {}
    for f, face in enumerate(faces):
        for i, j in zip(face, face[1:]+face[:1]):
            e = tuple(sorted((i, j)))
            edges.setdefault(e, []).append(f)
            orientation[e] = orientation.get(e, 0)+(1 if i < j else -1)
    assert all(len(v) == 2 for v in edges.values())
    assert all(v == 0 for v in orientation.values())
    assert len(points)-len(edges)+len(faces) == 2
    return points, faces, active, edges, certificates


def integrate(points, faces, interior):
    volume = R(0)
    moment = (R(0), R(0), R(0))
    for face in faces:
        a = points[face[0]]
        for j in range(1, len(face)-1):
            b, c = points[face[j]], points[face[j+1]]
            six_v = dot(sub(a, interior), cross(sub(b, interior), sub(c, interior)))
            assert six_v > 0
            volume += six_v/6
            moment = add(moment, mul(six_v/24, add(add(interior, a), add(b, c))))
    assert volume > 0
    return volume, moment, mul(1/volume, moment)


def persistence(points, edges):
    radii = [dot(p, p) for p in points]
    events = []
    for i, j in sorted(edges):
        d = sub(points[j], points[i])
        dd = dot(d, d)
        assert dd > 0
        t = -dot(points[i], d)/dd
        if t <= 0:
            level = radii[i]
        elif t >= 1:
            level = radii[j]
        else:
            level = radii[i]-dot(points[i], d)**2/dd
        assert level <= min(radii[i], radii[j])
        events.append((level, i, j))
    parent = list(range(len(points)))
    peak = parent[:]

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    bars = []
    for level, i, j in sorted(events, key=lambda q: (-q[0], q[1], q[2])):
        a, b = find(i), find(j)
        if a == b:
            continue
        if (radii[peak[a]], peak[a]) < (radii[peak[b]], peak[b]):
            a, b = b, a
        birth = radii[peak[b]]
        assert birth >= level
        if birth > level:
            bars.append(dict(root=peak[b], elder=peak[a], birth=birth,
                             death=level, depth=(birth-level)/birth,
                             attaining_edge=[i, j]))
        parent[b] = a
    return bars


def audit(planes):
    points, faces, active, edges, certificates = hull(planes)
    volume, moment, g = integrate(points, faces, mean(points))
    assert integrate(points, faces, g) == (volume, moment, g)
    X = [sub(p, g) for p in points]
    S, U, H = [], [], []
    weak = [0, 0, 0]
    polar = []
    for f, (face, raw_index) in enumerate(zip(faces, active)):
        n, support = planes[raw_index]
        height = support-dot(n, g)
        assert height > 0
        polar.append(mul(1/height, n))
        foot = add(g, mul(height/dot(n, n), n))
        guards = [dot(n, cross(sub(points[j], points[i]), sub(foot, points[i])))
                  for i, j in zip(face, face[1:]+face[:1])]
        if min(guards) > 0:
            S.append(f)
        elif min(guards) >= 0:
            weak[0] += 1
    adjacent = [set() for p in points]
    for i, j in edges:
        adjacent[i].add(j)
        adjacent[j].add(i)
    for i, neighbours in enumerate(adjacent):
        guards = [-dot(X[i], sub(X[j], X[i])) for j in neighbours]
        if min(guards) > 0:
            U.append(i)
        elif min(guards) >= 0:
            weak[1] += 1
    for (i, j), (fa, fb) in sorted(edges.items()):
        d = sub(X[j], X[i])
        dd = dot(d, d)
        t = -dot(X[i], d)
        z = add(mul(dd, X[i]), mul(t, d))
        n, q = planes[active[fa]][0], planes[active[fb]][0]
        nn, qq, nq = dot(n, n), dot(q, q), dot(n, q)
        assert nn*qq-nq*nq > 0
        alpha = dot(z, n)*qq-dot(z, q)*nq
        beta = dot(z, q)*nn-dot(z, n)*nq
        guards = [t, dd-t, alpha, beta]
        if min(guards) > 0:
            H.append([i, j])
        elif min(guards) >= 0:
            weak[2] += 1
    P = persistence(X, edges)
    Q = persistence(polar, {tuple(sorted(v)) for v in edges.values()})
    return dict(V=len(points), E=len(edges), F=len(faces),
                volume=volume, first_moment=moment, centroid=g,
                vertices=points, maximal_facets=faces,
                active_input_planes=active, edges=[list(e) for e in sorted(edges)],
                strict=[len(S), len(U), len(H)], additional_weak=weak,
                stable_facets=S, unstable_vertices=U, saddle_edges=H,
                P=P, Q=Q, boundedness_certificates=certificates)


def projective_interface(planes, old_vertices, ell, h, t, pivot, replace):
    assert t > 0 and dot(ell, pivot) == h
    assert all(dot(n, pivot) < support for n, support in planes)
    values = [dot(ell, p)-h for p in old_vertices]
    assert min(values) < 0 < max(values) and all(values)
    changed = []
    for i, (n, support) in enumerate(planes):
        ids = [j for j, p in enumerate(old_vertices) if dot(n, p) == support]
        if ids and max(values[j] for j in ids) > 0:
            changed.append(i)
    kept = [i for i in range(len(planes)) if i not in changed]
    cert = None
    if replace:
        cert = cone_certificate([planes[i][0] for i in kept], mul(R(-1), ell))
        if cert is None:
            raise ValueError('Sufficient all-amplitude boundedness condition not certified')
        cert['input_indices'] = [kept[i] for i in cert['indices']]
    rotated = []
    for i in changed:
        n, support = planes[i]
        height = support-dot(n, pivot)
        rotated.append((add(n, mul(t*height, ell)), support+t*height*h))
    result = ([planes[i] for i in kept] if replace else list(planes))+rotated
    return result, dict(changed_input_rows=changed, kept_input_rows=kept,
                        lower_cone_certificate=cert, ell=ell, h=h, t=t,
                        pivot=pivot, replace=replace)


def dump(path, obj):
    data = (json.dumps(obj, default=str, sort_keys=True, separators=(',', ':'))+'\n').encode()
    path.write_bytes(data)
    return dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest())


def main():
    output = Path(sys.argv[1] if len(sys.argv) > 1 else 'KH93_PROJECTIVE_CONTROLS')
    output.mkdir(parents=True, exist_ok=True)
    signs = list(product((-1, 1), repeat=2))
    base = [(tuple(map(R, (x, y, z))), R(1))
            for z in (-1, 1) for x, y in signs]
    old = audit(base)
    assert old['volume'] == R(4, 3) and old['centroid'] == (R(0), R(0), R(0))
    expected = {
      'RETAIN_H50': dict(h=R(1, 2), replace=False, VEF=[10,20,12], strict=[8,10,16],
        volume=R(47,36), gz=R(-17,1128), mz=R(-17,864),
        P=[R(1,2),R(636192,1272673),R(636192,1272673),R(636192,1272673),R(4,13),
           R(289,1311314),R(289,1311314),R(289,1311314),R(289,1311314)],
        Q=[R(1,3),R(1,3),R(1,3),R(7684598,24727923),R(7684598,24727923),
           R(7684598,24727923),R(598418,1909443)]),
      'RETAIN_H75': dict(h=R(3,4), replace=False, VEF=[10,20,12], strict=[8,6,12],
        volume=R(213,160), gz=R(-23,17040), mz=R(-23,12800),
        P=[R(1,2),R(289578289,580724258),R(289578289,580724258),
           R(289578289,580724258),R(234447073,525593042)],
        Q=[R(1,3),R(1,3),R(1,3),R(144398018,435543987),R(144398018,435543987),
           R(144398018,435543987),R(144398018,435543987)]),
      'REPLACE_H75': dict(h=R(3,4), replace=True, VEF=[6,12,8], strict=[8,6,12],
        volume=R(2197,1440), gz=R(7,240), mz=R(15379,345600),
        P=[R(1,2),R(200,401),R(200,401),R(200,401),R(16,41)],
        Q=[R(1,3),R(1,3),R(1,3),R(16,57),R(16,57),R(16,57),R(4232,11457)])}
    manifest, results = {}, {}
    for name, e in expected.items():
        ell, t, pivot = (R(0),R(0),R(1)), R(1), (R(0),R(0),e['h'])
        planes, parameters = projective_interface(base, old['vertices'], ell, e['h'],
                                                  t, pivot, e['replace'])
        a = audit(planes)
        assert [a['V'],a['E'],a['F']] == e['VEF'], name
        assert a['strict'] == e['strict'] and a['additional_weak'] == [0,0,0], name
        assert a['volume'] == e['volume'], name
        assert a['centroid'] == (R(0),R(0),e['gz']), name
        assert a['first_moment'] == (R(0),R(0),e['mz']), name
        assert sorted(b['depth'] for b in a['P']) == sorted(e['P']), (name,'P')
        assert sorted(b['depth'] for b in a['Q']) == sorted(e['Q']), (name,'Q')
        a.update(name=name, parameters=parameters, exact_input_planes=planes)
        results[name] = a
        filename = name+'_EXACT.json'
        manifest[filename] = dump(output/filename, a)
        print(name, a['strict'], manifest[filename], flush=True)
    retained, replaced = results['RETAIN_H75'], results['REPLACE_H75']
    assert replaced['volume']-retained['volume'] == R(7,36)
    assert replaced['first_moment'][2]-retained['first_moment'][2] == R(5,108)
    assert old['volume']-retained['volume'] == R(1,480)
    assert -retained['first_moment'][2] == R(23,12800)
    source = Path(__file__).read_bytes()
    manifest['source'] = dict(bytes=len(source), sha256=hashlib.sha256(source).hexdigest())
    dump(output/'MANIFEST.json', manifest)
    print('KH93_PROJECTIVE_INTERFACE_CONTROLS_PASS_3_NO110', flush=True)


if __name__ == '__main__':
    main()
```

## 9. Final scientific boundary

The current KH128 one-sided and fragmented exact endpoints remain authoritative and unchanged. The present handoff adds a proved E257 obstruction for the literal retained neck, a finite replacement-support geometry with a boundedness/edge-budget certificate, exact separated material-moment identities, and a complete rational demonstration of both mass reversal and unavoidable replacement U at a retained interface. It does not assert a new computationally verified S1 frontier, a LOW-preserving host trajectory, or simultaneous whole-P cancellation.
