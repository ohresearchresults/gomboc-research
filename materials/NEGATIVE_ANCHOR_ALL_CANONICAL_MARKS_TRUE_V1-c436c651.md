# material-c436c651e13c

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced; runtime-path-removed.

---

# NEGATIVE_ANCHOR_ALL_CANONICAL_MARKS_TRUE_V1

## Statement and evidence boundary
At a polyhedral local maximum of the full joint marked-body/affine-root trace problem with a>b>0, c,d>0, a positive-area actual root facet, and min(G(C),G(D))<0, all four canonical marks A,B,C,D are true vertices of the actual body.

In particular a positive opposite mark cannot be hidden inside a true edge of its coordinate facet. This removes the mixed-sign redundant-mark complement without any numerical trace threshold, endpoint-size restriction, assumption of proper33, or simplicity assumption. It does not exclude maxima with all four marks true, does not give a universal T<51/25, and does not exclude the full mechanical (10,17,9) layer. The mechanical bound remains 34<=C_min<=622.

This is a coordinator analytic theorem. No computation materially produced it, so the complete proof below is its self-contained recovery unit; there is no omitted source code, seed, numerical certificate or sandbox file. It combines the actual neighboring-facet geometry with the newly proved root-minimum ordinary-base theorem, not with a hypothetical globally prescribed set of moments.

## Exact antecedents and what is used
1. Fully read immutable worker result minimum-0165, SHA256 078f5b8df8a0c5b0ccb7a22bc3fa7aa26301717b0635893ed1c728e9efffebeb, NEGATIVE_ANCHOR_EXPOSED_EDGE_ROOT_BASE_AND_VALUE_V1. Sections 3,4,6 supply auxiliary positivity, free-facet spike and true whole-hinge reactions; strict negative C is a true vertex and AC a true edge; in negative-z maxima no ordinary A facet exists, every ordinary facet has its base on a root-minimum true edge, and an ordinary C facet requires c<min(b,d). Its exact original capsule is already durable inside that result. The result was read fully through EOF earlier in this coordinator turn; its proof sections were reread when developing this new connection.
2. Fully read analytic material [internal-source-reference], SHA256 04184117e8af7a7ea72746ead4f0c91935580419a6b346e2bfc23a0510fbd6ac, REDUNDANT_POSITIVE_MARK_FACET_REDUCTION_V1. Its exact exposed edge and second-facet support are restated and proved as needed below. Its previous non-exclusion and strict negative marker Hessian remain valid: the new contradiction is a different neighboring-facet reaction.
3. Fully read material [internal-source-reference], SHA256 0fdbce320bac57c70047fa72690c53148726aa159ecbfa6d6075fbe7cab488c1, NONPOSITIVE_MARK_COORDINATE_PATCH_ROOT_CHAIN_V2. Only the already established fact that a nonpositive marked C/D must be a true vertex is needed in the final all-marks formulation; no new use is made of its conditional patch or moment bounds.

These sources share the actual-body necessary conditions of POLYHEDRAL_TRACE_STATIONARITY_RIGIDITY_V1 and ROOT_DUALITY_JOINT_VARIATIONS_V1. No independent replay of a worker's computational capsule is asserted or required for the following purely analytic deductions.

## 1. Common actual-body setting
Let
A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
s=a+b, alpha0=a-b>0,
ell=a+(d-a)x+(c-a)y-alpha0 z,
n=(s+c)x+(s+d)y.
The bounded full-dimensional convex polytope P contains conv(A,B,C,D) and lies in x>=0,y>=0,ell>=0. The coordinate facets Fx,Fy and root F0 are actual maximal facets, with F0 of positive area. Coordinate facets may be enlarged polygons.

All integrals refer to uniform filling of this same P:
V=int_P1, E=int_Pell, N=int_Pn,
r=N/V>0, q=N/E>0, T=N/(6VE), G=n-r-qell.
Then GA=-r-qa<GB=-r-qb<0, and every auxiliary true vertex has G>0. A,B are true vertices and AB is the true common edge of Fx,Fy.

A free facet means a true maximal facet other than Fx,Fy,F0. It contains a canonical mark and satisfies max_F G+3 mean_F G<=0. An ordinary facet contains exactly one canonical mark X and is an actual triangle XUV with GX<0 and GU=GV=-GX/3. True edges have exactly two incident facets. A face containing a relative-interior point of a true edge contains the entire edge.

By reflection it suffices to assume GC<0. It is already known that C is true and AC is a true edge. If GD<=0, D is also true by the nonpositive-mark exposure argument. Suppose for a contradiction GD>0 and D is not true.

## 2. Exact exposed-edge geometry
The genuine D-mark reaction on Fy is
h_D=ell+(s+d)x-(s+2d)<=0,
with equality at D and strict negativity at A,B. Thus the nonvertex D lies in the relative interior of a true exposed edge UV of Fy. Both endpoints are auxiliary.

Put alpha=s+d, beta=s+2d, k=(b+2d)/(a-b)>0. The edge line is
y=0, z=k(x-1), ell=beta-alpha x.
Orient it with x_U=l<1<x_V=h. Then
0<l<1<h<=beta/alpha,
z_U=k(l-1)<0, ell_U>d>0.
Along this line G has positive slope (s+c)+q(s+d), so
0<GU<GD<GV.
Also GD-GC=(c-d)(q+1)>0, hence c>d.

The second true facet F of UV is neither protected nor root. It contains D, cannot contain A or B (they are on Fy outside UV), and cannot have only D because an ordinary mark would be a true vertex. Thus its canonical set is exactly C,D, and C is a true vertex of F. Its plane is
HF=beta-ell-alpha x-(beta-c)y=0,
with HF>=0 on P since HF(A)=b+2d>0. Every true vertex of F except C is auxiliary. U lies strictly below z=0, so the negative-z ordinary-base theorem applies to P.

## 3. The second facet is only a triangle or a root-ended quadrilateral
Since c>d, an ordinary C facet is impossible: its necessary condition c<d fails. Ordinary A facets are impossible at every negative-z negative-anchor maximum. Ordinary D facets are impossible because GD>0. Thus only a possible ordinary B facet remains, and its base must be an actual root-minimum edge.

Consider an edge WZ on the auxiliary boundary chain of F, other than UV. Its second facet cannot be Fx: C belongs to F and Fx outside WZ. It cannot be Fy: F intersect Fy is the true edge UV. If it is not root, its canonical set can only be {A} or {B}. C and D already belong to F outside WZ, so adding either to the second facet would produce the same supporting plane. A facet containing A and B is also impossible: AB already has its two incident coordinate facets. Hence a nonroot second facet would be an ordinary triangle with base WZ.

The A option has been excluded. The B option also contradicts the root-base theorem: WZ would then belong to three distinct true facets F,F0 and the B triangle. Therefore every auxiliary-chain edge except UV is a root edge. Distinct facets F and F0 have at most one common true edge. It follows that F has at most three auxiliary vertices, hence at most four vertices in total.

If F is a triangle, it is exactly CUV. If it is a quadrilateral, U cannot meet a root edge because ell_U>0. Consequently its cyclic order is C,U,V,W and VW is the root edge. In particular V and W are both on the root; W has y_W>0 because F intersect Fy is exactly UV.

In either case CU is a true edge, and U is the auxiliary endpoint adjacent to C on the side of the redundant marked edge with negative z.

## 4. The actual neighbor at CU is forced to be triangle ACU
Let J be the second true facet at CU. It is not Fx (x_U>0), Fy (y_C=1), or root (ell_C,ell_U>0). Thus J is free and contains C. It cannot contain D: a face containing the relative-interior point D of UV contains UV, and then J would contain the three noncollinear points C,U,V of F and equal F. It cannot be an ordinary C facet by Section 3. It cannot contain A and B simultaneously because of the actual AB incidence. Therefore J has canonical set either A,C or B,C.

The B,C option is impossible by true coordinate-face convexity. If B belonged to J, then J intersect Fy would contain the true vertices B and U, so BU would be a true supporting edge of Fy. But A and D lie on opposite sides of its line. Explicitly, on the (x,z) plane put
f(x,z)=l(z-1)-(z_U-1)x.
Then f(B)=f(U)=0,
f(A)=-l<0,
f(D)=1-l-z_U=(1+k)(1-l)>0.
A and D both belong to Fy, so this line cannot support Fy.

Thus J contains A,C. The true facet intersections give the three edges AC=J intersect Fx, AU=J intersect Fy, and CU=J intersect F. They form a closed triangular boundary cycle. A convex polygon with these three true edges has no further vertices. Therefore J is exactly the actual triangle ACU.

This argument does not assume Fx=ABC. In the quadrilateral case W is allowed to be on Fx; no unproved proper33 reduction has been inserted.

## 5. One genuine hinge makes the neighboring facet have positive mean G
The whole plane of J=ACU can be tilted around AC in either sign while retaining all four marks. A,C remain on the plane, while B,D lie strictly on the body side. This is a permitted full-class whole-facet variation, not an independent motion of an integration triangle. With transverse speed phi=x/l, the exact triangle product integral gives
0=int_J G phi=Area(J)[GA+GC+2GU]/12.
Hence
GC+2GU=-GA>0.                                      (1)

All auxiliary true vertices of F have G at least GU. This is immediate for triangle CUV since GV>GU. For quadrilateral CUVW it remains to compare W with V. Both are on ell=0 and HF=0, so
alpha x+(beta-c)y=beta.
Since y_V=0 and y_W>0,
GW-GV=n(W)-n(V)
 =[(s+d)-(s+c)(s+2d-c)/(s+d)]y_W
 =(c-d)^2 y_W/(s+d)>0.                            (2)
Thus GU<GV<GW in the quadrilateral case.

Fan-triangulate the actual polygon F from its true vertex C. Every resulting triangle has C and two auxiliary vertices P_i,P_j with G_i,G_j>=GU. Its genuine affine mean is
(GC+G_i+G_j)/3 >=(GC+2GU)/3=-GA/3>0.
The actual polygon mean is the positive-area weighted average of these means. Therefore mean_F G>0. Also max_F G>0. This contradicts the necessary free-facet inequality
max_F G+3 mean_F G<=0.

Even the weaker outward-translation first variation already gives a contradiction: moving the whole free plane HF=0 outward to HF=-epsilon retains the marks and has first derivative proportional to int_F G>0. The positive mean is therefore a genuine improving body direction, not merely failure of a relaxed matrix test.

This proves that D cannot be redundant. Reflection completes the theorem.

## 6. What changed, and what remains open
The earlier possible UV[private-runtime-path] pentagon is first reduced to triangle or root-ended quadrilateral by the root-minimum ordinary-base theorem. The actual CU neighbor then forces a triangle hinge relation. The original stationary field along the redundant D edge, and the exact positive root-edge slope (c-d)^2/(s+d), make that relation incompatible with the mean on F. No root-moment fitting, endpoint cap, Bernstein computation or number-of-facets enumeration is needed.

The former calculation T(D_x)=T(D)-(s+d)Y(x-1)^2/(6VE) remains valid. Sliding D along its own exposed edge really is locally unfavorable; that proposed shortcut was false. The new ascent is a whole neighboring-facet/body effect, not the one-dimensional mark slide.

All-true mixed-sign marks with triangular/quadrilateral/pentagonal coordinate patches remain. The positive-ell auxiliary, negative-z root-only, one-zero endpoint and actual mechanical joint110 connections are not closed by this theorem. No attaining object or numerical complexity record has been promoted.
