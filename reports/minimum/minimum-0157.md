# minimum-0157

Historical AI scientific report · saved 2026-09-21 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# ASYMMETRIC_B8_TWO_PARAMETER_ALL_SPD_V1

## Result and precise scope

**A genuinely strongly asymmetric, nonparallel, two-parameter B8 family is excluded at its true uniform volume centroid for every positive-definite metric: every member has at least two strict unstable vertices.** Both the entire admissible motion of one basal corner and the entire admissible apex-length range are covered. The previously supplied free-reference110/own334 geometry lies inside this family. Consequently, its **whole own-centroid affine orbit**, not merely its previously chosen metric, is now excluded.

The new family is entirely outside the old opposite-pair error tube: an exact scalar certificate proves `100 E_basal,yy > S_yy` throughout the complete parameter square. Therefore **no member satisfies `Err <= 2^-30 S`, for any choice of k**. This is not a small-asymmetry continuation of that sufficient inequality.

A second result is a closed, affine-invariant **actual-moment coefficient domain** for variable geometric pencils. A third is a quantitative, all-metric separation of the genuine centroid from every mono-unstable reference chamber. No own110 attainer, whole balanced11shape exclusion, whole E17 exclusion, or registry/census delta is claimed. The accepted global bounds remain unchanged. The previous distinction between the central theorem, its small tube, and the asymmetric reference control was explicit in the supplied journal. :contentReference[oaicite:0]{index=0}

## 1. Exact geometric family

Start with the ten raw vertices

```
P0=(-1+s,-1,0)         P1=(-1,19/50,0)
P2=(-1,67/100,0)       P3=(3/20,1,0)
P4=(33/100,1,0)        P5=(1,21/25,0)
P6=(1,61/100,0)        P7=(41/50,-1,0)
P8=(-a,0,1)            P9=(a,0,1).
```

The complete free parameter domain is

```
0 < s < 91/50,          0 < a < 100/21.
```

Apply the positive projective map

```
f(x,y,z)=1-(21/100)x-(33/50)y,
Y_i=P_i/f(P_i),
P(s,a)=conv(Y_0,...,Y_9).
```

Every projective image is **uniformly refilled**, and its own volume centroid is recomputed. In the inherited eleven-parameter notation the exact input is

```
(s,69/50,23/20,33/100,67/100,4/25,9/50,161/100,
 a,-21/100,-33/50).
```

All denominators are positive on the stated domain. The four strict basal side guards are `s+9/50<2`, `23/20+67/100=91/50<2`, `69/50+33/100=171/100<2`, and `4/25+161/100=177/100<2`.

The actual maximal facets, with outward cycles, are

```
F0=(0,1,2,3,4,5,6,7)
F1=(0,8,1)    F2=(1,8,2)    F3=(2,8,3)
F4=(3,8,9,4)
F5=(4,9,5)    F6=(5,9,6)    F7=(6,9,7)
F8=(7,9,8,0).
```

The actual edges, in the order used in every certificate, are

```
(0,1),(0,7),(0,8),(1,2),(1,8),(2,3),(2,8),(3,4),(3,8),
(4,5),(4,9),(5,6),(5,9),(6,7),(6,9),(7,9),(8,9).
```

Thus the genuine incidence is always **V/E/F=10/17/9**. To see the whole-domain incidence directly, before projective transformation the intermediate horizontal sections are Minkowski sums of the octagon and a horizontal segment. The three left side normals select apex8, the three right side normals select apex9, and the two horizontal basal sides select both apices. They give exactly the six triangles and two quadrilaterals above. Positive projective and invertible affine maps preserve this complete face lattice. Integration diagonals in F0 are never mechanical edges.

### Theorem A

For every body `P(s,a)` in this domain, and every `M>0`, evaluated at its actual uniform volume centroid `g`,

```
U_strict(P(s,a),g,M) >= 2.
```

All basal and both apical root locations, all finite condition numbers, all metric walls, and all physical weak contacts are included. No assumption on S, H, a selected complementary dual tree, or weak000 is needed. In particular own strict110/weak000 is impossible throughout this family and every genuine affine image of it.

## 2. Compact geometric normalization: an actual moving-vertex pencil

Use the real affine map

```
H_a(x,y,z)=(x-a z, y, (1-21a/100)z).
```

Its determinant is positive throughout the domain. Define

```
rho = 7439 s/(17017-1911 s),
lambda = 42a/(100+21a),
```

so both parameters range independently over `(0,1)`. The exact inverse is

```
s=17017 rho/(7439+1911 rho),
a=100 lambda/[21(2-lambda)].
```

In these coordinates the seven fixed base vertices are

```
B1=(-1250/1199,475/1199,0)
B2=(-5000/3839,3350/3839,0)
B3=(300/617,2000/617,0)
B4=(3300/2707,10000/2707,0)
B5=(2500/589,2100/589,0)
B6=(5000/1937,3050/1937,0)
B7=(4100/7439,-5000/7439,0).
```

Put

```
C=(-100/187,-100/187,0),  A=(0,0,1),  O=(-100/21,0,0),
Y0(rho)=(1-rho)C+rho B7,
Y8(lambda)=(1-lambda)A+lambda O,
Y9=A.
```

Together with B1,...,B7 these are exactly `H_a(P(s,a))`. In particular **this is a two-variable affine motion of two actual vertices**, not an independently prescribed centroid or moment fit. O is the intersection of the extensions of the two distinguished base sides. It is external to the base; it is **not** used as a positive fan apex for the interior body.

The actual ridge is nonparallel to the base at every interior parameter, and its height ratio is `1/(1-lambda)`, unbounded in this family. The closed nondegenerate square `[1/100,99/100]^2` is one explicit large closed subdomain of actual10/17/9 bodies. The finite polynomial proof below covers the whole closed square `[0,1]^2`; on its outer edges some labelled vertices/facets degenerate, so those outer edges are not mislabelled as genuine10/17/9 bodies.

## 3. The mass mechanism replacing opposite-pair cancellation

For either genuine apex fan, rooted at8 or9, triangulate only the true boundary facets not incident to that apex. Each fan has nine tetrahedra: six from the octagonal base and three from the opposite triangular chain. For each selected cell t let

```
d_t = det(Y_b-Y_a,Y_c-Y_a,Y_d-Y_a),
D = sum_t d_t = 6 Volume(P),
J = sum_t d_t (Y_a+Y_b+Y_c+Y_d) = 24 integral_P y dy.
```

All selected cell determinants are strictly positive in the open square. Their Bernstein coefficients are nonnegative on the entire closed square, with each cell polynomial nonzero. The two fans give **identical polynomial D and J**, hence

```
g(rho,lambda)=J(rho,lambda)/(4D(rho,lambda)).
```

D is bilinear and J has total degree at most three. This formula is recalculated from actual material volume at every geometry; it is not the image of an old centroid under a projective map.

There is also a useful positive geometric decomposition. At fixed rho, let `P0=conv(B_rho,A)`. The additional material consists of the three true tetrahedra along the visible basal chain, with vertices `(A,B_i,Y8(lambda),B_(i+1))`, i=0,1,2, where B0 denotes the current Y0. Their volumes are lambda times their endpoint volumes. Thus, writing `D0=6 Vol(P0)` and `W=6 Vol(P1 minus P0)`,

```
D = D0 + lambda W.
```

For this exact family,

```
D0(rho)=d0-b rho,       W(rho)=c+b rho,
d0=255170373836575897000000/10176363525290611672309,
b =1569750000/1667920507,
c =113229500000/9301739601.
```

Let `c_B` be the actual area centroid of the current base, and let `m` be the weighted mean of the three endpoint sums `B_i+B_(i+1)`, weighted by those **actual positive endpoint tetrahedron volumes**. Then

```
J = D0(A+3c_B)
    + lambda W(2A+m)
    + lambda^2 W(O-A).
```

In particular the true height centroid is

```
g_z=[D0+(2lambda-lambda^2)W]/[4(D0+lambda W)].
```

The horizontal components retain the actual basal area centroid and actual wedge-volume endpoint mean. They cannot be replaced by a ridge midpoint or by free contact weights. This positive two-part material decomposition avoids the signed-volume problem of a full fan rooted at the external intersection O.

## 4. Full all-metric proof by actual-moment coefficient matrices

Write `X_i=Y_i-g`, and for a true directed edge i->j put

```
D_ij = X_i^T M(Y_j-Y_i).
R_i = 4D Y_i-J = 4D X_i,
A_ij(rho,lambda) = -2[R_i(Y_j-Y_i)^T+(Y_j-Y_i)R_i^T].
```

Each entry of A_ij has bidegree at most `(3,3)`. The exact physical identity is

```
tr(M A_ij) = -16D D_ij.                         (1)
```

Unlike the earlier six-column paired-layer lemma, these are three-by-three matrices assembled from the **actual asymmetric coordinates and true moment polynomial**.

The preserved new table contains **624 complete rows** of positive integer weights on true directed edges. Every support has between three and nine arrows. A row r defines

```
B_r = sum_(i,j) w_r,ij A_ij,       W_r=sum_(i,j) w_r,ij > 0.
```

Let `D_*` and `X_i,*` refer to the genuine midpoint body `(rho,lambda)=(1/2,1/2)`, and set

```
T_* = D_* sum_i X_i,* X_i,*^T > 0.
```

T_* is only an affine-covariant normalization tensor for a proof certificate. It is not asserted to be the material covariance or mechanical metric of another member.

Split the parameter square into the four closed half-squares. For each listed row/cell application, expand B_r in the tensor-product degree `(3,3)` Bernstein basis. All sixteen coefficient matrices `B_r,c,alpha` satisfy the exact stronger inequality

```
B_r,c,alpha - (W_r/2048) T_* > 0.              (2)
```

There are **1954 row/cell applications, 31264 shifted positive-definite matrices, and 93792 positive leading minors**. Integer denominator clearing and Bareiss minors are independently checked against rational LDL pivots. Since the Bernstein basis is nonnegative and sums to one, (2) proves the corresponding inequality for every parameter in the whole closed cell, not merely at samples or at its corners.

The source independently enumerates the true graph: its Kirchhoff cofactor and exhaustive tree count are both4095. With all ten roots there are40950 directed rooted trees. **Every one is covered in every one of the four closed cells** by at least one table row whose support is contained in that tree. The resulting163800 tree/cell checks are not primal/dual-pair counts or additions to a historical registry.

Combining (1) and (2), for the selected row at every actual parameter,

```
(sum w_r,ij D_ij)/W_r < -tr(M T_*)/[32768 D] < 0.     (3)
```

Now suppose the actual body had one strict unstable vertex. Every other vertex has a true weak escape `D_ij>=0`. Along every such edge,

```
|X_j|_M^2-|X_i|_M^2=2D_ij+|Y_j-Y_i|_M^2>0,
```

including a zero escape derivative. Choosing one escape at each nonroot therefore gives a rooted true-edge spanning tree. Its covering row has all summands nonnegative, contradicting (3). A maximum-norm vertex is always strictly unstable, so absence of a strict U is not an alternative. This proves Theorem A.

No polar recentering, independent N, bounded condition number, genericity assumption, or deletion of harmless zero primitives occurs. The obstruction allows all weak metric walls because it contradicts **nonnegative** tree arrows. The complete physical controls separately use the reciprocal pair `N=M^-1` and merge coincident VF packets.

### Exact finite evidence identities

```
624-row input JSON: 29292 bytes
SHA256 415681e34e8dcf3811293188edc1034e8803933c218c06294c4a66256a162257

Shifted coefficient/minor stream:
84413fb46a10725e3558fb98e3d5d822cea76a0d855865d53f9a903aa689ec76

All rooted-tree/cell coverage stream:
91c38230485f43465b881fc58a237a7b57ffe8fd43f896c6f2893a217b57d561

Independent direct rational mass/primitive stream:
c215981cec5d7e26f0f032d84727591b017a40daa087d6666a9afbe2fe455ab2
```

The last check reconstructs the actual bodies at sixteen rational interpolation points and verifies4896 scalar matrix identities by direct two-fan integration. It is an algebra check; positivity on continuous cells comes from all Bernstein coefficient matrices, not from those sixteen bodies.

## 5. A closed intrinsic domain beyond the literal two-parameter family

The same fixed624-row table defines a reusable domain of **actual geometric pencils**, not free moments. Take arbitrary coplanar basal anchors and above-plane A, with `Y0=(1-rho)C+rho B7`, `Y8=(1-lambda)A+lambda O`, the indicated actual balanced face lattice throughout the open square, and genuine positive fans. Form their actual polynomial D,J and T_* by the same formulas.

Require, for every listed cell/row/Bernstein coefficient,

```
B_r,c,alpha - (W_r/2048) T_* >= 0.              (4)
```

This is a **closed affine-invariant matrix domain**, relative to the admissible genuine geometric pencils. It includes equality in (4), since the retained positive term `(W_r/2048)T_*` still makes B_r positive definite. The proof above then excludes U1 for all M throughout every pencil in this domain.

Under an affine map with linear part L, both B and T_* transform by `|det L| L(.)L^T`; hence (4) is intrinsic and does not select preferred mechanical axes. For the explicit strongly asymmetric pencil every shifted matrix is strictly positive definite. Consequently it lies in the interior of this sufficient domain within the space of admissible pencils, and finite valid perturbations of its frozen geometric anchors are allowed by (4). This is not a claim that every base octagon or the entire balanced11shape satisfies (4).

## 6. Quantitative genuine-centroid/reference separation

The certificate also supplies a metric-independent neighborhood of the **true** centroid that no mono-unstable reference chamber can enter.

For the complete compact pencil set

```
D_max=max_[0,1]^2 D,
L_max=max_(true edges, [0,1]^2) (Y_j-Y_i)^T T_*^-1(Y_j-Y_i),
radius_squared=1/[2^32 D_max^2 L_max].
```

Both maxima are reconstructed exactly. D is bilinear, and each edge vector is affine in rho,lambda, so the convex edge quadratic takes its maximum at a parameter corner. No numerical maximization is used.

For every member and every interior reference c satisfying the closed condition

```
(c-g)^T T_*^-1(c-g) <= radius_squared,           (5)
```

there are at least two strict U for **every** SPD M. Indeed changing reference by delta changes each arrow by `-delta^T M e`. With `R^2=tr(M T_*)`,

```
|delta^T M e| <= sqrt(delta^T T_*^-1 delta)
                  sqrt(e^T T_*^-1 e) R^2.
```

Condition (5) bounds this by `R^2/(65536 D_max)`, whereas the magnitude of the negative row average in (3) is at least `R^2/(32768 D_max)`. A weak escape tree is therefore still impossible. This also holds for the closed intrinsic domain (4). It is a conservative proved separation bound, not an optimum radius. The anchoring point in (5) is always the actual g, never a substituted `c_k`.

## 7. A whole-domain negative result for opposite-pair approximation

Use the preceding paired-layer definitions, at the actual g:

```
b=mean_(0<=i<8) X_i,
u_i=(X_i-X_(i+4))/2,
d_i=(X_i+X_(i+4))/2-b,
a_vec=(X8-X9)/2,
S=sum_i u_i u_i^T+a_vec a_vec^T+b b^T,
E_basal=sum_i d_i d_i^T.
```

The exact polynomial

```
(4D)^2 [100(E_basal)_yy-S_yy]
```

has bidegree `(4,2)` and all fifteen Bernstein coefficients on the **whole** closed square are strictly positive. Its complete coefficients are reconstructed by the capsule. Therefore

```
(E_basal)_yy > S_yy/100 > 2^-30 S_yy.
```

Adding the apex error `eta eta^T`, for any k, cannot repair this violation. Thus the whole explicit family lies outside the old small-asymmetry condition. This is a theorem about the entire parameter domain, not a numerical distance estimate at the reference control.

## 8. Genuine controls, including the non-attainer and weak/VF preservation

For three new controls use the compact-coordinate body above and

```
L=((1,0,0),(1/10,1/10,0),(1/5,3/100,1/100)),
M=L L^T, N=M^-1; the rational Euclidean map is L^T.
```

All three have actual10/17/9, true own uniform COM, strict222/weak000 and68 nonzero edge primitives:

| rho,lambda | Strict stable facets | Strict unstable vertices | Strict saddle edges |
|---|---|---|---|
|1/100,99/100|0,4|5,8|(0,7),(3,8)|
|99/100,1/100|0,5|2,5|(3,4),(6,7)|
|1/2,1/2|0,5|5,8|(3,8),(6,7)|

These are nonwinning bodies. They show that the one-sided bound U>=2 is sharp inside the new class. Their full rational coordinates, both positive fans, true centroids, maximal primal/polar facets, poles, all physical edge packets, and rational Euclidean images are regenerated, not rounded decimal inputs.

The literal old geometry occurs at

```
rho=66951/833651, lambda=1134/10567,
s=9/50, a=27/100.
```

Its old metric has

```
L_old=((1,0,0),(1/10,119/50,0),(-101/50,27/20,79/25)),
M_old=L_old L_old^T.
```

Transport it to the compact coordinates with `M=H_a^-T M_old H_a^-1`. At the true uniform COM the exact audit still gives

```
S={0,3,6}, U={5,7,8},
H={(0,8),(2,3),(4,9),(6,7)}, weak000, no zero primitives.
```

At the deliberately **non-own** reference `H_a(-23/50,-1/2,7/500)`, the same inverse metric pair still gives reference110/weak000, S={1}, U={5}. Its base-pole minimum pairing is below -3. It is not an attainer or a control satisfying all uniform-mass conditions. The new conclusion is that **changing the metric cannot make the actual uniform centroid mono-unstable anywhere in this whole two-parameter family**, including this literal shape.

The original paired-layer control source is included **unchanged and complete**. It retains all central222 controls, the genuinely nonparallel small-tube control, the own277/non-own312 height-band countercontrol, and the genuine own446 VF control with **two true-edge packets but one physical point and four zero primitives**. The new theorem does not discard these non-record or weak controls. The old computations are preserved with their original status; they were not rerun merely to establish authorship.

## 9. Input authority, work done, and open complement

The new journal was read consecutively through EOF, together with its full literal parent and the supplied complete source-bearing files. Unchanged prior context remained accessible. Required parent identity: `minimum-0151`, declared immutable SHA256 `fa8bfc0addc71ed7a13ffbc062c6fa049826694e16074d346368b3e470610312`.

The supplied complete original wrapper is27334 bytes with the expected SHA256 `5638ebed4bed5b410652308d62a1f85df28bb2a56a0e89e19f8c3da06ff4829f`. The two original Python source units match their published byte counts and hashes exactly. The old504-row literal input is35304 bytes, SHA256 `559d4be643c8d55d189698cb87165b4278bebf542bce860145d3b82eba71b452`. Those original bytes, including all controls, are now transported completely inside the recovery below.

One representation limitation remains explicit: the currently delivered journal is350437 bytes, SHA256 `d1bbf379ff67ce29e38728c981321e30771c7a6169240fd5257c57f963cdc255`; its rendered parent Markdown from the central-theorem heading to EOF is40885 bytes, SHA256 `3ccc4f4bb5234c15f2976b77dbf0ee35e2b8b7717dba8ac911212c551ce2e58a`, not the declared envelope hash. No cause is assumed and no whole-envelope byte authentication is claimed. The individual original source pins do match. No mathematical identity, incidence, or class conflict was found. The journal explicitly identified the prior truncated DATA as a preservation gap, rather than a refutation of the accepted central result. :contentReference[oaicite:1]{index=1}

The substantive change of direction was from approximate pair cancellation to an actual two-vertex motion with **positive fan volume and first-moment polynomials**. Numerical eigenvector cutting planes helped find integer rows, but no numerical failure or infeasibility was used as proof. The published exact object is the complete frozen624-row table and deterministic verifier. It needs no numerical solver, random seed, missing checkpoint, or external library. Fresh source-only build and check of the new proof both completed and reproduced the new report byte for byte.

The open complement includes the other seven independent cuts and the two projective slopes outside the stated fixed values, all valid pencils failing (4), the unbalanced3/7 and4/6 types, and E17 without a B8 facet. No global completeness or external priority is claimed. These624 rows and four parameter cells are not subtracted from any historical FULL/LOCAL/census denominator.

**Most useful continuation:** vary frozen basal anchors while retaining the two genuine positive fans and their polynomial moment identities, and test the explicit closed coefficient domain (4). The current source makes that a geometric coefficient problem rather than another search over M or free centers. Expansion beyond this domain must preserve actual supports and the common D,J; independent fitted moments or a substituted centroid would destroy the proof.

## 10. Complete self-contained recovery

Save the entire following block as `recover_asymmetric_b8.py`, UTF-8/LF with one final LF, assertions enabled. It contains three **complete** source units: the two original paired-layer files with unchanged bytes and the new exact proof/control unit, including every new integer row. No download or previous local file is required.

```
python -S recover_asymmetric_b8.py build
python -S recover_asymmetric_b8.py check
```

Both commands regenerate/check the new proof; they do not rerun the accepted old theorem. `extract` only writes the three sources. The preserved old proof and all old controls remain independently reproducible using

```
python -S paired_layer_core.py build
python -S paired_layer_core.py check
python -S paired_layer_controls.py build
python -S paired_layer_controls.py check
```

Executed new environment: CPython3.13.5, standard library only. Exact pins:

| Object | Bytes | SHA256 |
|---|---:|---|
|Complete recovery wrapper|43819|a6dd8e89515ae65b6099df153c0822511618a0c094d7c47e13b881ce599c8027|
|Decoded three-source JSON|54971|a3c4a1dcc4bfe0a126ae2ace346b62ba745d0cbdb6267d736003c8c99c7866b9|
|Original paired_layer_core.py|21900|ccc739ad54cd33dee876639a2263267cea4a77f3f29576d87492c9dbad14b531|
|Original paired_layer_controls.py|10294|72aa361fd823cf03e2ce674c4cad0e6904031c91b35a48dbfb94829aeefdf1cd|
|New asymmetric_roof_pencil.py|21869|451617674da0cfab60f956225ffb707839fad021facec377e05deb34d9f752b2|
|New exact report|189976|a4ce8e1b18d369615302e1e814d312aa4a622301c6dd121cbbfe6a747e7ca315|
|Each full wrapper build/check stdout|881|c5667bef4cc23cd7d5efc440e7b5c2830d828c9c51cfc84e7e79cbeb2cf9dc0c|
|Preserved old core report|573022|94cf6a66c3c7310a48fa7e5db60bdfe9db25c9561606d6e5c59c3369f3e870d7|
|Preserved old physical-control report|255063|fb46b517b730a48bab40ecaf6ebc06c28ce864e22f6f53565c714f5698db1c5f|

Expected new terminal markers include


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]



[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


**Transport limitation:** the inline DATA in this response is incomplete and cannot reconstruct the pinned sources. Accordingly, despite the completed local exact computations, this response does not meet the requested self-contained source-transport requirement and must not be treated as a durable computational successor based on its inline capsule. The complete original and new bytes are present in the actual supplemental artifacts: [readable complete handoff](sandbox:/mnt/data/asymmetric_b8_handoff.md), [source units and exact reports](sandbox:/mnt/data/asymmetric_b8_handoff.zip), [complete JSON handoff with the full capsule](sandbox:/mnt/data/asymmetric_b8_result.json). The mathematical statements above have the stated locally executed exact-verification status; their finite certificate remains dependent on those supplemental bytes until the full capsule is incorporated into durable working memory.
