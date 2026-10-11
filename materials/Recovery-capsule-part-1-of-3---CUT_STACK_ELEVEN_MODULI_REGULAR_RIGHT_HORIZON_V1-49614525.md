# material-496145257730

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# CUT_STACK_ELEVEN_MODULI_REGULAR_RIGHT_HORIZON_V1
## Recovery capsule part 1 of 3: geometry, actual moments, regular horizon and exact nonwinning path

This is new coordinator research, not a replay of a worker's conclusion. The analytic construction extends the genuine cut-and-stack family from eight to eleven independent affine shape parameters. A single affine normalization gives constant actual volume on the entire open operation domain. Unlike the earlier eight-parameter restriction, this larger family has a regular ten-vertex parameter boundary. An explicit rational path to that boundary has true incidence10/17/9 and own457weak000 throughout0<=s<=1/16. It is NOT a110 body, NOT a U1 feasibility result, and NOT an all-metric exclusion. The accepted bracket34<=Cmin<=622 is unchanged.

## 1. Sources and complete recovery boundary

The fully read literal parent minimum-0285, SHA383ab22af4a74c7ba8d2604d95d2f259b60928871a59f7b9d332622ab016f35f, supplies the original eight-parameter native cut-and-stack family and its regional all-root U2 theorem. Its source is not imported by the present two programs. The earlier coordinator proof [internal-source-reference], SHA5e52ae768f93839759e4661c6d80c582df5ff18b34d4da7ad001eef09c65e6c4, excluded every parameter boundary of THAT restricted family using a full-volume gauge and the accepted nine-vertex nonzero-PSD refinement theorem. The new regular horizon does not contradict either result: it uses an additional base-diagonal modulus approaching its endpoint.

This complete capsule consists of the present part1 and:

- Part2: [internal-source-reference], the literal complete cut_stack_regular_horizon.py,6622 bytes,SHA3ba570f2ef54f1e1f7b0e6de573a94a1a0337cd6aa7d758e82aeeac5cf309f48.
- Part3: [internal-source-reference], the literal complete cut_stack_horizon_interval.py,5192 bytes,SHA46d7b0169c0acc7a01fbae945230ade68e5fa6497a03680cf49574691ea2ee3e.

Save the native text of parts2/3 under those exact .py filenames in one directory. No hidden coordinates, checkpoint, optimizer, seed, certificate input or prior sandbox file is needed. All parameters are literal rational numbers in part2. Assertions must remain enabled.

Observed stack: CPython3.13.5, SymPy1.14.0. Part2 uses the standard library only. Reconstruction AND full verification commands are:

```
python -B -S cut_stack_regular_horizon.py > report.json
python -B cut_stack_horizon_interval.py > interval_report.json
```

Expected outputs:

- report.json:53406 bytes,SHA1561b8961531845f02a163eb4a623c9bf344d30057e803d5fadcbfdbcfa3c2bd; marker CUT_STACK_REGULAR_HORIZON_ACTUAL_CENSUS_PASS.
- interval_report.json:180963 bytes,SHAaa9b449d4c272e0358cf97ea62b896405de65860c28d92d68dcc260d2bfb0b29; marker CUT_STACK_REGULAR_HORIZON_WHOLE_PATH_EXACT_PASS.

Both commands were actually executed normally and then from a fresh directory containing ONLY the two complete source files. Both cold outputs were byte-identical to the normal outputs. The observed cold comparison marker was CUT_STACK_HORIZON_COLD_SOURCE_ONLY_BYTEIDENTICAL_PASS. This is exact author computation, not proof-assistant formalization or external review. The core program's three-point-only scope is intentional: the second program separately supplies the whole-path proof.

## 2. Eleven genuine independent operation parameters

Let0<beta,r<1. Put

B0=(0,-beta,0), B1=(0,1-beta,0), B2=(0,0,1),
B-=(-r,0,0), B+=(1-r,0,0).

The original body is the quadrilateral pyramid with base(B-,B0,B+,B1) and apexB2. Independently choose0<f_j,k_j,t<1 and w_j>0 with sum w_j=1. Define

L_j=B-+f_j(B_j-B-),
R_j=B++k_j(B_j-B+),
S=t B-+(1-t)sum_j w_j L_j.

The ten labels are ordered(B0,B1,B2,L0,L1,L2,R0,R1,R2,S). Their genuine convex hull has maximal outward cycles

(0,3,4,1,7,6), (0,2,5,3), (0,6,8,2),
(1,4,5,2), (1,2,8,7), (3,9,4),
(3,5,9), (4,9,5), (6,7,8).

The two removed corner tetrahedra have disjoint interiors in x<0 and x>0. Every stated open cut choice is valid, without coupling among the six fractions. The stack point lies in the interior of the removed left tetrahedron and sees only its cut face, because all four barycentric coefficients t,(1-t)w_j are positive. Thus all listed supports and turns are strict apart from their required incidences, and the body has10 vertices,17 true edges and9 maximal facets.

There are eleven affine shape parameters: beta,r, the six independent cut fractions, and the three independent stack barycentric coordinates(t,w0,w1). For this labelled finite-pyramid operation class these are genuine affine invariants/recoverable data. The two original ghost vertices B-/B+ are intersections of inherited side-facet planes and the base plane. Their two base-diagonal division ratios recover beta,r. Cut fractions are affine ratios on the recovered original edges, and the stack coefficients are barycentric in(B-,L0,L1,L2). The earlier native family fixed r=1/2 and w0=w1=w2=1/3, leaving eight parameters after an affine x scaling.

This parameter count does NOT assert that every realization of this graph has finite convex original ghost apices. The boundary below is precisely a case where one reconstructed apex is at infinity.

## 3. A constant-volume affine gauge on the entire eleven-parameter domain

Set p=prod f_j, q=prod k_j,

d_L=1-(1-t)p, d_R=1-q,
D=r d_L+(1-r)d_R>0.

The actual signed six-volume coefficients of the two original tetrahedra, the two removed tetrahedra and the added stack tetrahedron are

r, 1-r, -r p, -(1-r)q, r t p.

Their sum isD, so the ACTUAL uniform volume isD/6. If J denotes the sum of each coefficient times the sum of its four vertices, the actual original COM isJ/(4D). No vertex-mass model is used.

Apply the invertible affine linear map G=diag(1/D,1,1). The final hull has

Vol(GP)=1/6 EXACTLY,
GP contained in Q=[-1,1]^2 x [0,1].

To prove containment write alpha_j=1-f_j and gamma_j=1-k_j. Since d_L>=alpha_j and d_R>=gamma_j, the normalized x coordinates of L_j and R_j obey

r alpha_j/D<=1, (1-r)gamma_j/D<=1.

The normalized stack has x coordinate

-r[t+(1-t)sum w_j alpha_j]/D.

But1-prod f_j>=max alpha_j, hence d_L>=t+(1-t)max alpha_j>=t+(1-t)sum w_j alpha_j. Its absolute x coordinate is at mostone too. All yz projections remain in the triangle with vertices(B_j)yz, which lies in[-1,1]x[0,1].

Actual centroids and volume moments transform affinely. An original physical metric M transforms to H=G^(-T) M G^(-1); its inverse transforms reciprocally. No Euclidean metric is reset during this equivalence, and no spectral cutoff is imposed.

## 4. A regular right-apex horizon, not a nine-vertex degeneration

Fix open beta,f_j,t,w_j and choose A>0,c_j>0 satisfying

A d_L+c0+c1+c2=1.

For a small positive parameter s put

r=s A, k_j=1-s c_j.

This is inside the finite-pyramid operation domain whenever s<min(1/A,1/max c_j). Write C=sum c_j, C2=sum_(i<j)c_i c_j, C3=c0 c1 c2. Then

D(s)=s delta(s),
delta(s)=1-s(C2+A C)+s^2(C3+A C2)-s^3 A C3.

In the normalized coordinates the vertices are

B_j=(0,(B_j)yz),
L_j=(-A(1-f_j)/delta, f_j(B_j)yz),
R_j=((1-sA)c_j/delta, (1-s c_j)(B_j)yz),
S=(-A[t+(1-t)sum w_j(1-f_j)]/delta,
   (1-t)sum w_j f_j(B_j)yz).

These rational expressions extend regularly to s=0. At that endpoint delta=1, so

L_j=(-A(1-f_j),f_j(B_j)yz),
R_j=(c_j,(B_j)yz),
S=(-A[t+(1-t)sum w_j(1-f_j)],(1-t)sum w_j f_j(B_j)yz).

The three B_jR_j segments are nonzero parallel true edges. The old right ghost apex has escaped to infinity, but the actual hull remains full-dimensional, with all ten true vertices and the SAME nine maximal cycles for every open choice above. One direct geometric proof decomposes it across x=0 into the left truncated/stacked tetrahedral side and the right wedge

{(x,yz): yz in conv((B_j)yz), 0<=x<=c(yz)},

where c is the positive affine function taking values c_j at the three projected corners. The left side is contained in the projected triangle. Its outward non-base side normals have negative x component, so extension to x>=0 preserves their inequalities. The wedge's three projected-side inequalities contain the left side; its upper affine plane has x>0 over the entire triangle and strictly contains the left non-base points. The base pieces glue in z=0, while the two other projected-side planes remain distinct from the left side planes. All other strict incidences follow from the open cut and stack conditions. This recovers the displayed cycles, including the right triangular face(R0,R1,R2).

This regular horizon is ten-dimensional: beta1, f3, t1, w2, A1, c3, minus the displayed one normalization relation. It does not collapse to a contained refinement of a nine-vertex body.

The actual left six-volume isA d_L. The actual right wedge six-volume isC. Their sum isone, in agreement with the global gauge. Therefore the accepted nine-vertex nonzero-PSD refinement theorem cannot remove this boundary. The native-eight all-wall result remains correct in its original scope; it must NOT be extended to all eleven parameters or all realizations without handling this regular face.

## 5. Closed actual moment formula directly on the regular face

No limiting quotient is needed to compute the horizon COM. Set B-=(-A,0,0) now and use the endpoint vertices from Section4. Let

J_L=A(B-+sum B_j)-A p(B-+sum L_j)+A t p(sum L_j+S).

This is24 times the actual first moment of the truncated/stacked left piece. The wedge contribution is

(J_R)_x=sum c_j^2+sum_(i<j)c_i c_j,
(J_R)_yz=C sum(B_j)yz+sum c_j(B_j)yz.

Indeed, the x moment integrates c(yz)^2/2 over the projected triangle of area1/2; its remaining moments integrate yz*c(yz). The standard barycentric monomial integrals on that triangle give the displayed expressions. Since D=1, the actual horizon COM is

g=(J_L+J_R)/4.

The formula was also evaluated exactly on the control below and agreed with its independently computed oriented-boundary volume moment. The complete supplied programs use the original signed-tetrahedral identities and boundary-fan identities, so no unstored helper is required to reconstruct the computed result.

## 6. An exact true10/17/9 control and a whole rational path

Use the literal inputs

beta=2/5,
f=(3/10,3/5,7/10), t=2/5,
w=(1/5,2/5,2/5), A=1,
c=(63/5000,63/2500,189/5000).

Then p=63/500,d_L=2311/2500,C=189/2500, and A d_L+C=1. At s=0 the ten vertices are exactly

(0,-2/5,0), (0,3/5,0), (0,0,1),
(-7/10,-3/25,0), (-2/5,9/25,0), (-3/10,0,7/10),
(63/5000,-2/5,0), (63/2500,3/5,0), (189/5000,0,1),
(-163/250,9/125,21/125).

Their actual volume is1/6 and their actual centroid is

(-3985259/20000000, 65839/1250000, 167023/625000).

Use one physical metric and its exact inverse:

M=((7,1,2),(1,5,-1),(2,-1,6)), N=M^-1.

The leading principal minors of M are7,34,173, so M is SPD. In this displayed affine frame the proper census is

S facets=[0,1,3,8],
U vertices=[3,4,6,7,8],
H edges=[(0,3),(1,4),(3,4),(3,5),(6,7),(6,8),(7,8)],
physical weak=000.

Thus S=4,U=5,H=7 and S+U-H=2. The physical Euclidean body can equivalently be obtained by the linear map with Gram matrixM and then recentered at its transformed ACTUAL centroid. No assigned centre or independent dual metric is used.

The SAME census, true incidence, constant actual volume and absence of physical weak contacts hold on the ENTIRE closed parameter interval

0<=s<=1/16.

Part2 independently recovers the hull from every vertex triple at s=0,1/16,1/256. It verifies all maximal supporting cycles, strict turns,17 true edges with exactly two incident facets, actual volume/first/second moments, positive actual covariance, M N=I, all34 primal and34 dual arrow signs and the proper census. Its three evaluations alone would not prove a continuum claim.

Part3 supplies that missing continuum proof. It constructs the exact rational vertex functions and ACTUAL five-tetrahedron first moments, independently checks the boundary-fan identities D=1 and J=4g, and reduces every guard to a rational numerator/denominator in s. The168 tested rational functions comprise1 positive delta,56 strict nonincident support gaps,34 positive cycle turns,9 positive centred supports, and68 nonzero physical primitive arrows. Their maximum reduced numerator/denominator degrees are21/17.

For each numerator P(s)=sum P_i s^i and denominator Q(s), it checks with exact rational arithmetic

|P_0|-sum_(i>=1)|P_i|(1/16)^i>0,
|Q_0|-sum_(i>=1)|Q_i|(1/16)^i>0.

The signs at zero therefore persist on the entire interval. All168 passed at the first proposed radius1/16, without any halving. Every full coefficient array and positive domination gap is written to interval_report.json and is regenerable from the complete two sources. This is not sampled feasibility or an inferred sign from endpoints.

## 7. Consequences and limits

The new countercontrol disproves the inference that every boundary of the larger cut-and-stack shape domain has at most nine true vertices. It does not disprove the nine-vertex theorem, the original eight-parameter all-wall proof, or the regional eight-parameter all-root certificate. The extra base-diagonal ratio is essential.

The constant-volume gauge removes spurious loss of actual volume but cannot remove genuine regular shape limits. Any all-incidence exclusion must handle the new regular-apex face and additional interior moduli, not just take nine-vertex deletion collars around the old eight-parameter box. The whole regular face is a meaningful target for all-root or joint same-inverse mechanics; the present457 family is only a nonwinning control. Neither full-face U2 nor any U1/110 survivor has been proved here.

Other stack-weight and ghost-apex boundaries must also be classified in their true incidence. For example, a stack coefficient w_j approaching zero can flatten an adjacent facet pair without deleting the stack vertex; it is not automatically a nine-vertex boundary. No all-boundary classification of the full eleven-parameter family is claimed in this capsule.
