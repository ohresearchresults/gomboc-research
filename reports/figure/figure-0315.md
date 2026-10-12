# figure-0315

AI research report · 2026-09-05 UTC

---

# Rapid Atlas 04 — sparse C3 construction and exact obstruction handoff

## Determination

**NONWINNER. No new homogeneous own-centred polyhedral Gömböc was obtained in this direction.** The strongest retained finite construction is a new rational C3-invariant convex polyhedron with

**(V,E,F,C)=(79,216,139,432), exact own-volume-centroid (S,U,H)=(4,1,3), and no degenerate equilibria.**

It has one unwanted threefold orbit of stable–saddle pairs, not the requested class (1,1,0). Its complexity is below1000, but that alone is not success. This is an independent object, not a successor or alias of the lead’s accepted815-vertex body. The journal expressly leaves the previous C3 assignment’s mathematical outcome unknown; I have not interpreted its transport failure as a negative result. :contentReference[oaicite:0]{index=0}

The material additional findings are an executed exact69-parameter preserving box for the79-vertex nonwinner, an exact exclusion of its entire inherited-C3-preserving affine metric family, and a broader roundness theorem: **any strict C3-invariant110 polyhedron with concentric inradius/circumradius r/R≥47/50 has C≥1008.** The latter is not a universal symmetry obstruction. C3-symmetric homogeneous polyhedral Gömböcs are permitted by the existence theorem of Domokos–Lángi–Várkonyi; their Theorem2 explicitly includes cyclic symmetry groups. :contentReference[oaicite:1]{index=1}

## 1. Exact finite body: every coordinate and maximal face

Let D=1000000000. Number the following26 representative integer triples from j=0 through25:

```text
-455879583 -240434162 -589953430
-416144786 -207644525 -634038674
-362763803 -183227013 -677087572
-297169994 -168366266 -716267620
-221242218 -163613381 -748900894
-137190745 -168869864 -772597345
-47433098 -183400025 -785373637
45534869 -205869305 -785755303
139267703 -234405319 -772860969
231494193 -266677427 -746468445
320231636 -299988928 -707063854
403885596 -331372522 -655877734
481329739 -357671959 -594918524
551959521 -375573161 -527031744
615711991 -381483126 -456075162
673038997 -370816834 -387630902
724833518 -333464548 -333464548
771946352 -282279914 -282279914
813484194 -225505733 -225505733
848224962 -162872370 -162872370
874670621 -94048491 -94048491
890912573 -18590944 -18590944
894380950 64159157 64159157
881316953 155320218 155320218
845435090 257164713 257164713
773185820 375952703 375952703
```

For representative(a,b,c) at indexj, define

```text
I_(3j)   = (a,b,c)
I_(3j+1) = (b,c,a)
I_(3j+2) = (c,a,b).
I_78     = (577350269,577350269,577350269).
```

The map(x,y,z)→(y,z,x) is an exact Euclidean order-three rotation about the axis spanned by e=(1,1,1). The raw body is conv{I_i/D}, filled at uniform density1. The own-centred body is defined below by its actual integrated centroid, not by its vertex average.

Here is the complete list of139 outward maximal face cycles. Indices are zero-based; each semicolon terminates one face, and line breaks have no meaning. This list also fixes the face numbering used by the delivered certificate.

```text
29,55,58;26,52,55;23,46,49;8,34,37;11,40,14;3,29,32;5,28,31;29,61,32;
26,55,29;6,35,38;0,20,23;0,17,20;17,43,46;0,14,17;5,31,8;0,11,14;
0,29,3;3,32,6;2,19,22;0,8,11;2,28,5;8,31,34;2,16,19;9,41,12;
2,13,16;20,46,23;17,46,20;6,32,35;0,26,29;0,23,26;2,10,13;0,2,5;
2,25,28;2,7,10;23,49,26;35,56,38;14,40,43;2,22,25;32,62,59;14,43,17;
8,37,11;1,4,2;29,58,61;38,56,53;1,6,9;1,9,12;1,12,15;0,3,1;
6,38,9;1,15,18;26,49,52;0,5,8;1,18,21;41,53,44;15,44,47;32,59,35;
12,41,44;2,4,7;12,44,15;1,3,6;35,59,56;11,37,40;1,21,24;44,53,50;
15,47,18;9,38,41;38,53,41;1,24,27;44,50,47;43,52,49;43,49,46;40,52,43;
32,61,62;61,64,65,62;64,67,68,65;67,70,71,68;70,73,74,71;73,76,77,74;
76,78,77;0,1,2;72,75,76,73;72,74,77,75;69,72,73,70;69,71,74,72;
75,78,76;75,77,78;60,63,64,61;60,62,65,63;63,66,67,64;63,65,68,66;
66,69,70,67;66,68,71,69;31,60,61;30,62,60;1,27,4;42,48,45;37,52,40;
10,36,39;36,51,39;34,58,55;42,51,48;18,47,21;33,57,54;4,27,30;
37,55,52;24,50,53;7,36,10;7,30,33;31,58,34;4,30,7;25,48,51;30,57,33;
13,39,42;21,50,24;13,42,16;39,51,42;34,55,37;27,59,62;16,45,19;
31,61,58;28,57,60;21,47,50;22,48,25;19,45,22;7,33,36;36,54,51;
30,60,57;16,42,45;33,54,36;10,39,13;24,56,27;25,54,28;27,62,30;
28,60,31;24,53,56;22,45,48;27,56,59;25,51,54;28,54,57
```

The complete true-edge list is deterministically the deduplicated set of unordered consecutive pairs in these cycles, including each closing pair. It has216 edges. Triangulate each listed cycle(f0,...,fk−1) by(f0,fi,fi+1), i=1,...,k−2. This produces154 outward triangles. There are124 triangular and15 quadrilateral maximal faces. The display triangulation has231 edges, of which15 are exactly coplanar diagonals and are not true edges.

These integer coordinates and cycles are the authoritative definition. The numerical discovery formulas below are not needed to reconstruct them.

## 2. Ordinary solid volume and exact centring

For the154 oriented triangles just specified, direct integer summation gives

```text
V6 = sum det(Ia,Ib,Ic)
   = 8280908944600824967324130643

M24 = sum det(Ia,Ib,Ic)(Ia+Ib+Ic)
    = (-19982745409891403154514343801160096,
       -19982745409891403154514343801160096,
       -19982745409891403154514343801160096).
```

Consequently the actual physical volume is

```text
Vol = 8280908944600824967324130643 / 6000000000000000000000000000
    ≈ 1.3801514907668042.
```

The actual raw volume centroid is(c,c,c), where

```text
c = -208153598019702116192857747928751
    /345037872691701040305172110125000000
  ≈ -0.0006032775370305275.
```

For comparison, the raw vertex-coordinate average is approximately−0.0608262623291 in each coordinate. It is emphatically not the physical centroid used here.

A common-denominator definition of the exactly own-centred points is

```text
C0 = 2760302981533608322441376881
B  = -1665228784157616929542861983430008
Q  = 2760302981533608322441376881000000000

Z_i = C0 I_i - B(1,1,1)
x_i = Z_i/Q.
```

The final solid is P=conv{x_i}. Both full implementations independently re-integrated its mass. Its three first moments are exactly zero; this is not merely an asserted translation of an estimated centre.

## 3. Exhaustive own-centroid mechanics and positive margins

The complete census is:

```text
Stable maximal faces:
[0,1,2]
[32,61,62]
[31,60,61]
[30,62,60]

Unstable vertices:
[78]

Saddle true edges:
[0,1]
[0,2]
[1,2]

Degenerate equilibria: none.
Zero primitive signs in the face/vertex/true-edge mechanical ledger: none.
```

Thus the residual consists of exactly one C3 orbit of extra stable faces and one C3 orbit of saddles. At an invariant interior reference, non-axis features occur in threefold orbits; this is the smallest orbit-sized stable–saddle defect compatible with keeping the intended axis face and apex.

The literal candidate is not close to a zero-margin classification wall. Exact rational lower bounds give the following conservative values at this body:

| Quantity | Certified lower bound |
|---|---:|
| Every nonincident plane–point distance | >1/2500 |
| Every stable-face minimum side margin | >1/10 |
| A strict exclusion witness for every nonstable face | >1/2500 |
| Unique unstable vertex’s full adjacent-edge cone margin | >1/3 |
| A strict escape witness for every other vertex | >1/2500 |
| Every saddle’s four-component minimum margin | >1/16 |
| A strict exclusion witness for every nonsaddle true edge | >1/2500 |

The closest computed conservative bounds are approximately0.000403592219 for nonincidence,0.000403589123 for nonstable/nonsaddle exclusion, and0.000403592783 for nonunstable exclusion.

For precise normalization and independent reconstruction, let N be an outward integer face normal, let d=Zb−Za, and let q=Q. A face-side margin is N·(Za×Zb)/(‖N‖‖d‖q). A vertex-edge margin is−Za·d/(‖d‖q). Positive rational lower bounds are obtained by replacing square roots of integer squared norms in their denominators by their integer ceilings. Nonincident support distances use(h−N·Ii)/(‖N‖D).

The full mixed-cone edge test was executed explicitly. For an oriented true edge a→b, put

```text
L = d·d
T = -Za·d
W = L Za + T d
n,m = the two outward incident face normals
G = (n·n)(m·m) - (n·m)^2
beta_n = (W·n)(m·m) - (W·m)(n·m)
beta_m = (W·m)(n·n) - (W·n)(n·m).
```

G is strictly positive. A strict saddle requires all four quantities T,L−T,beta_n,beta_m to be positive. Every true edge was tested; the three listed edges pass and all213 others have a strict negative component. The sign-equivalent oriented face-side formulation was separately checked against these Gram numerators. H=3 was not inferred from Euler.

The intended base’s support distance is approximately0.741581792391, whereas the three extra stable planes have distance approximately0.477238265994. This exposes a macroscopic difficulty: the intended base is not the closest support. A successful continuation cannot merely suppress a small numerical side sign while leaving that global geometry untouched.

### A positive-dimensional exact preserving box

An exact rational interval calculation also passed for a69-parameter chart. Representatives0–15 have three independent real coordinates each; representatives16–25 have form(a,b,b), with two independent coordinates each; the apex has form(a,a,a), with one. Every independent physical coordinate may vary by at most10^-7 from the literal raw value. Apply the threefold orbit generator, and then recenter each member at its own actual ordinary-volume centroid.

Throughout this box, the complete maximal-face lattice, vertex extremality, strict class(4,1,3), and all mechanical primitive signs persist. The15 quadrilateral coplanarities are identities in this chart: each joins matching sides of two aligned equilateral orbit triangles. They were not treated as approximate equalities. The interval checks include10,549 strict nonincident supports,492 polygon halfplane tests,79 rank-three cone checks,432 face-side signs,432 directed vertex-edge signs, and864 edge-cone components.

This is a constrained incidence-stratum box, not an unrestricted independent-vertex perturbation guarantee or a manufacturing tolerance.

## 4. Executed independent acceptance and mesh parity

The first checker enumerated all point triples with exact integer predicates, retained only genuine globally supporting planes, grouped identical primitive planes, and reconstructed maximal polygon cycles by exact planar hulls. It then checked every plane against every point, complete contact sets, every polygon’s global edge-halfplanes, all vertex links, rank-three incident supporting normals, connected oriented boundary topology, ordinary moments, and the full feature census. The point/facet validation contains10,981 exact comparisons in addition to the all-triples hull enumeration.

The second checker imports no discovery or first-checker module. It treats the supplied cycles as untrusted certificates, rechecks all global supports and contacts, computes ordinary volume using nonnegative tetrahedra with a boundary vertex as apex, computes literal orthogonal feet, tests vertex supports against ALL points, and solves the two-normal Gram system on every edge. It returned INDEPENDENT_RATIONAL_FULL_CHECK_PASS with the same exact volume, centroid and complete class.

Both checks were executed again from a fresh extraction of the final archive. The replay also reconstructed the69-parameter box, affine-metric atlas, axial-reference atlas and roundness arithmetic; checked exact translation invariance; and rejected reversed-face, open-boundary and corrupted-point fixtures.

The OBJ contains79 exact finite-decimal raw vertices and139 maximal faces. The ASCII STL contains154 triangles. Both are the exact raw translated copy, not a decimal approximation to the nonterminating centred coordinates. Their known exact centroid is(c,c,c); subtract it to obtain the own-centred presentation. Fraction-based readback reproduced all points, cycles, triangles, oriented edge incidences and volume. The15 flat display diagonals remain excluded from C.

## 5. Exact obstruction for all inherited-C3-preserving affine images of this body

This is a complete continuum exclusion, but only for the stated affine family.

Let R be the inherited coordinate-permutation rotation. An invertible map A keeps ARA^-1 orthogonal precisely when AᵀA commutes with R. Up to an irrelevant overall scale and orthogonal map, the metric is

K_lambda=lambda I+(1−lambda)eeᵀ/3, e=(1,1,1), lambda>0.

Such linear maps preserve the exact zero ordinary centroid. For a face normal N and C=Za×Zb, its side sign after the deformation is the sign of

```text
(3 N·C - sum(N)sum(C)) + lambda sum(N)sum(C).
```

For a directed vertex edge with d=Zj−Zi, the unstable-support sign is the sign of

```text
-sum(Zi)sum(d) + lambda(-3 Zi·d + sum(Zi)sum(d)).
```

The four true-edge signs use these same endpoint and incident-face expressions. All are affine in lambda. Exact enumeration produced167 distinct positive primitive walls and168 open cells, with S≥4 in every open cell.

A smaller exact certificate covers the walls too. Base[0,1,2] is stable for all lambda>0. The threefold orbit of face[32,61,62] is strictly stable on0<lambda<U, where

```text
U = 2609651910664066983243511321482541702582338655
    /622566073703954794892569743509065246094986144
  ≈ 4.191766980070005.
```

The threefold orbit of face[76,78,77] is strictly stable on L<lambda<infinity, where

```text
L = 64612927510019118043787625419889051887426780
    /16131839282221115653052927042321533187444667
  ≈ 4.005304440469412.
```

Exact cross multiplication gives L<U. The two open intervals therefore cover every positive lambda, including each other’s endpoints. At least one extra stable orbit always survives, and **S≥4 for the entire family**.

This does not exclude arbitrary non-affine C3 coordinate changes, a different C3 architecture, or symmetry-breaking affine metrics. The separately sampled symmetry-breaking metric searches were numerical nonwinners, not a continuum exclusion.

## 6. A broader exact C3 roundness obstruction

### Statement

Let a full-dimensional convex polyhedron be invariant under an order-three Euclidean rotation about an interior reference O. Suppose its complete strict reference-relative class is(1,1,0), with no additional degenerate equilibria. If its concentric inradius r and circumradius R satisfy

r/R≥47/50,

then

**V≥253, F≥253, E≥504, C≥1008.**

Homogeneity is not used in this theorem; in particular it applies when O is the body’s own volume centroid. It excludes no C3 shape with r/R<0.94.

### Proof and finite arithmetic certificate

The unique unstable vertex U and unique stable face are fixed by rotation. Any other axis vertex would also be strictly unstable: its invariant full-dimensional normal cone contains the axial supporting direction in its interior. Any invariant face has axial normal and its axial perpendicular foot in its relative interior, so is stable. An invariant true edge would have both endpoints fixed and would lie on the interior axis, which is impossible. Hence there is exactly one fixed vertex and one fixed face, with V≡F≡1(mod3) and E≡0(mod3).

Place U on the positive axis at radius R. The unique stable face is the opposite axial support at distance r. Indeed every closest supporting plane has its perpendicular foot strictly inside its face and is stable; a positive axial face cannot occur because U alone attains that axial maximum.

Every nonunstable vertex v has a true-neighbor w with v·(w−v)>0. Otherwise its radial direction would belong to its normal cone, giving an unstable or degenerate equilibrium. These arrows strictly increase squared radius. Choose a path from a stable-face vertex to U with m edges, radii q_i and successive ray angles theta_i. Let phi=acos(r/q_0). Then theta_i<pi/2, q_i/q_(i+1)<cos(theta_i), and phi+sum theta_i≥pi. Concavity of log cos gives

r/R < cos(phi) product cos(theta_i) ≤ cos(pi/(m+1))^(m+1).

For r/R≥47/50 the exact arithmetic below excludes m≤78, hence m≥79. The path and its two rotated images are disjoint except at U: an intersection gives equal radii at the same position of the strictly radius-ordered path, forcing that vertex to be fixed by rotation. Thus they contain3m+1 vertices.

Put kappa=r/R and delta=acos(kappa). The vertex directions cover the unit sphere by delta-caps: every support direction has a vertex with dot product at least r and radius at most R. Since−log cos(theta)≥theta²/2, each path has spherical length at most sqrt(2m log(1/kappa)). A delta-neighborhood of a connected geodesic network of total length ell has area at most2ell sin(delta)+2pi(1−cos(delta)): begin with one cap and sweep along its edges, each length increment contributing at most2sin(delta) times that increment. Overlaps only decrease new area.

Apply this to the three paths joined at U, then add one cap for each remaining vertex. Sphere coverage requires

```text
4pi ≤ 6 sqrt(2m log(1/kappa)) sqrt(1-kappa²)
       + 2pi(1-kappa)(V-3m).
```

Suppose V≤250. Then79≤m≤83. Replacing kappa by47/50 and V by250 enlarges the right side. Use the rigorous bounds

```text
log(50/47) < 3/47
sqrt(1-(47/50)^2) < 171/500
157/50 < pi < 22/7.
```

For m=79,80,81,82,83, respective upper bounds on sqrt(6m/47) are

```text
1587853/500000
1597871/500000
1607827/500000
3235443/1000000
3255111/1000000.
```

The resulting exact area upper bounds are respectively

```text
9991980123/875000000
9037954761/875000000
1154815251/125000000
14258475813/1750000000
12349103601/1750000000.
```

All are strictly below314/25=4(157/50), a contradiction. Therefore V>250, and V≡1(mod3) gives V≥253.

Polarity about O preserves C3, the ratio r/R, strictness, and the interchange of stable faces with unstable vertices. The polar need not have centroid O because the theorem is reference-relative. Applying the same proof gives F≥253. Euler then gives E=V+F−2≥504 and C≥1008.

The executed Fraction certificate encloses pi using Machin’s formula16atan(1/5)−4atan(1/239), with alternating-series bounds from8 and2 terms. For every m=1,...,78 it sets x=(157/50)/(m+1), verifies0<1−x²/2+x⁴/24<1, and verifies that this rational number raised to(m+1) is less than47/50. It also checks every displayed square-root and area inequality exactly. Status: EXACT_C3_ROUNDNESS_C_GE_1008_PASS.

This is a research proof with executed exact arithmetic, not a claim of priority, proof-assistant formalization or independent human review.

## 7. What was tried, and what the negative results actually mean

The numerical construction used three rotated copies of a variable-twist radial path, not fixed homothetic sections throughout the body. A useful reproducible discovery parameterization is

```text
s_j=j/m, theta_j=(pi-delta)(1-s_j)^p
l_j=clip((theta_j-pi/2)/(pi/2-delta),0,1)
u_j=clip(1-theta_j/(pi/2),0,1)
phi_j=turn*l_j^a + upper_turn*u_j^a
w_j=(sin(theta_j)cos(phi_j),sin(theta_j)sin(phi_j),cos(theta_j))
r_m=1
r_j=product_(k=j)^(m-1)[(w_k·w_(k+1))*exp(-head/m)].
```

Take the three rotations of r_j w_j for j<m and the axis apex. Positive consecutive dot products give explicit reference-origin radial escape witnesses, but do not establish own-centroid mechanics. The actual convex hull, solid centroid and full feature census were recomputed.

The final79-point proposal used m=26 and approximately

```text
delta=.323964056478463
turn=1.704408421434997
a=1.5630509240509838
head=.0004325207047932928
p=.63760509518144
upper_turn=0.
```

It was mapped to the cyclic-coordinate chart, rounded to the displayed integer table, and independently rebuilt exactly. The literal table supersedes all floating proposal details. Exact106- and85-vertex(4,1,3) predecessors were also checked, but are dominated by the final79-point body.

Additional experiments included free C3 orbit clouds; independently twisted and unevenly spaced paths; nonmonotone axial paths; latitude-dependent angular-width source experiments; finite normal-offset hulls; full-coordinate sequential linear programming with actual centroids; one- and two-new-orbit communicating patches; and polar-volume/Santaló-style moment continuation. None produced a verified own-centred110 body. The full-coordinate and added-patch attempts often reduced a chosen score by creating more equilibria or deactivating large parts of the hull. Those smaller numerical hulls were not promoted as stronger candidates.

Two symmetry-breaking affine metric searches on a prior85-point body found numerical(2,2,2) endpoints with best hard defects about0.0006483 and0.0005396, not positive chambers. This is finite search evidence only. Polar-moment repair reduced a reference110 construction’s polar centroid displacement from about0.1243 to about0.0973, but did not isolate a zero and developed very small steps. It is not an own-centred result.

A particularly useful exact diagnostic is available for the FINAL79-point geometry. With the raw body fixed and the reference restricted to(c_ref,c_ref,c_ref), its strict110 chamber is

```text
-17150229/40000000 < c_ref
 < -3965804454884951565000576258678761
    /18913876681644161980335044000000000.
```

The upper endpoint is approximately−0.2096769753571 per coordinate. The actual centroid c≈−0.0006032775370 lies above it by Euclidean distance about0.36212627. An exact182-open-cell all-feature axial atlas establishes this interval; immediately above its upper endpoint the class is(4,1,3). This proves that the finite geometry has a genuine auxiliary110 chamber, while simultaneously quantifying why simply choosing that point would violate the homogeneous-centroid requirement.

No failed numerical search above is a global exclusion of C3 or of nonhomothetic rotational architecture.

## 8. Most useful continuation

The final body provides a small, well-separated, exactly centred restart point with one unwanted symmetry orbit. A shortest actual dual route from one extra stable face to the outer incident face of saddle[0,1] is

```text
[32,61,62]
 -> [29,61,32]
 -> [3,29,32]
 -> [0,29,3]
 -> [0,3,1].
```

Its threefold closure uses representative orbits0,1,9,10,20. The next constructive experiment should replace this entire threefold disk and its complete one-rings simultaneously, allow obsolete vertices to deactivate, and give the stable-foot and saddle-cone changes independent non-affine coordinates. The inherited-C3 affine family is exactly excluded, so another axial/transverse metric polish alone is redundant. The indicated patch is an evidence-based starting topology, not a proved minimal replacement or an established feasible cancellation.

A particularly simple physical moment control is available without changing density. Starting from any proposed C3 patch geometry p_i, set

p_i(t)=p_i+t b_i e,

where each rational b_i is constant on an orbit and is zero on protected features. For triangle f=(i,j,k),

```text
Delta_f(t)=Delta_f0+t Delta_f1
Delta_f1=b_i det(e,p_j,p_k)
         +b_j det(p_i,e,p_k)
         +b_k det(p_i,p_j,e).
```

All higher determinant terms vanish because they contain two copies of e. With L_i=e·p_i and B_f=b_i+b_j+b_k,

```text
6 Vol(t)=sum_f(Delta_f0+t Delta_f1)
24 e·M(t)=sum_f(Delta_f0+t Delta_f1)
                    *(L_i+L_j+L_k+3t B_f).
```

Thus volume is affine and the real axial first moment is quadratic. The transverse moments vanish identically by C3. An isolated quadratic root can hard-wire ordinary centring inside a certified actual incidence cell. If a hull circuit is crossed, rebuild the actual maximal faces and moment polynomial before continuing; a root of an obsolete tetrahedral formula is not admissible. After solving the moment equation, every maximal face, vertex and true mixed edge cone must be checked again.

For independent new C3 architectures aimed at C<1000, the roundness theorem supplies a concrete necessary design target: **r/R must be below0.94.** Approximating an arbitrarily near-spherical C3 existence construction cannot by itself meet the requested budget.

## 9. Portable artifacts and replay record

The exact definition, complete lattice, both full implementations, all exact diagnostic certificates, exact centred rational CSV, raw exact-decimal OBJ/STL, proofs and replay are in [C3_RA04_EXACT_HANDOFF.zip](sandbox:/mnt/data/C3_RA04_EXACT_HANDOFF.zip).

```text
Archive size: 85248 bytes
Archive SHA-256:
0531e46547ac35b13072ca91cfefe40b85095d507b28aa2499f75a7e2524d418

EXACT_BODY.py size: 3372 bytes
EXACT_BODY.py SHA-256:
734e13e1a6be148fc0555d2280104b338a0d6c6042ff0477c4c95bfec4d26477

Raw OBJ SHA-256:
7d50cf73cf874f9fbb9a3d8b5ca22ed47446e53d8321ebe1c0da739b0960cdf4

Raw ASCII STL SHA-256:
fa745a077e42d11ee81604cad416664b803e5b87cf089f966dc7308687fa547b
```

The frozen archive was freshly extracted, all26 payload hashes were checked, and `python -S REPLAY.py` completed with **C3_RA04_EXACT_NONWINNER_FRESH_REPLAY_PASS**. Do not use Python−O. The separate actual replay report is [C3_RA04_ARCHIVE_REPLAY.json](sandbox:/mnt/data/C3_RA04_ARCHIVE_REPLAY.json), SHA-256120bcf5eb96c973f6793a3d5991afc476797633accf9bf994d3856cec4ffbd3d.

The numerical programs, proposals, prior exact nonwinners and frozen search logs are supplementary in [C3_RA04_DISCOVERY_RESEARCH.zip](sandbox:/mnt/data/C3_RA04_DISCOVERY_RESEARCH.zip),920696bytes, SHA-256b2b0f67b2cf3e1d6f81ea036e91fa50e6886c3f0048c994584e659ca5d16650c. Those numerical checkpoints are not acceptance certificates. The complete primary79-point reconstruction data, moment identities, feature lists, predicates and continuation formulas are all present above; continuation does not require recovering a worker-local omitted mask.

**Final scope:** a rigorously verified sparse homogeneous C3 nonwinner, a nontrivial exact preserving neighborhood, two sharply scoped exact obstructions, and a concrete whole-orbit moment-coupled continuation—not a claimed polyhedral Gömböc.
