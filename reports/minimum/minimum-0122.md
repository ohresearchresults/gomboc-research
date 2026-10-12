# minimum-0122

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# BEVEL_FACET9_THREE_PARAMETER_ALL_SPD_V1

## Result and scope

**A complete genuinely three-dimensional, boundary-reaching subdomain is now excluded for U1, with no restriction on the positive-definite metric.** Let B be the literal ten-vertex bevel below, let T_p(x)=x/(1+p·x), and uniformly refill T_p(B). For every p in the precisely specified cone C9 below, and every positive-definite M, with the same reciprocal N=M^(-1), the refilled body's own volume centroid has **U_strict >= 2**. The assertion includes every root and all zero-arrow walls; it does not assume S1, H0, or weak000. In fact min_M U_strict=2 for every such shape.

C9 has parameter-space volume 1/16, or 315/5392 of D_B, approximately 5.84%. Its boundary patch occupies 9/16 of the entire polar facet associated with vertex 9. Every radial value up to that patch is included: the projective denominator at vertex 9 can tend to zero without any positive lower bound. This is not a thickened finite metric sample or another one-dimensional pencil.

Two further results are preserved: an exact degree-six adjoint giving the true mass throughout all D_B, including its complete boundary orders; and complete, bounded, fixed-simplex realization charts for the seven simple-vertex radial stars. Those stars occupy 211/337 of parameter space. **The latter geometric chart theorem is not an all-SPD equilibrium exclusion on those stars.** An exact small-coordinate strict547weak000 body in one such chart is retained, as is a genuinely three-parameter strict323weak000 sharp-U2 control inside C9.

The full D_B problem is not solved here. No actual U1 body or strict110weak000 attainer is claimed. No incidence-registry, FULL/LOCAL, or eleven-dimensional realization-space exclusion follows.

## Input authority and reading boundary

The complete supplied journal, including its immutable parent payload and all eight decoded source/data units, was read through EOF. The upload is 330457 UTF-8 bytes, 1977 lines, SHA-256 d8061360661cbff3cf1c83051b43f8811cd9acbf182e7cbf6ad9cb0a63ef9381. No external research archive or research connector was used.

The required parent is minimum-0107, advertised SHA-256 37b21117ba32f0a13744c8144bca7aaf5d013efc95413c0c9bdbc95894ff674e. Its full-pencil theorem is retained as a working premise, not reinterpreted as a full-orbit theorem. The supplied literal statement explicitly uses the newly refilled volume centroid and every SPD metric.

There is a serialization discrepancy to preserve: the literal UTF-8 substring from the parent heading through attachment EOF is 73330 bytes, SHA-256 559e159bdc8eabd0ec842f585adeae0f34d4ce5d8067701ac69f305519a3785e, whereas the journal advertises 74128 bytes and the parent SHA above. I did not recover that advertised envelope by changing line endings. This is not a discovered mathematical incidence conflict. All eight decoded parent units matched their individually declared sizes and hashes; in particular pencil_core.py is 11191 bytes, SHA-256 d272ec9d2ad68879431e0bde4aebbb4be164e542ca95fe546af24007afebb64e. The construction here uses the literal coordinates and supports, independently checks their hull, and needs no inaccessible parent checkpoint.

## 1. Literal body and the complete new domain

The labels are:

```text
0 (-1,-1,-3/4)   1 (-1,-1,1)    2 (-1,-3/4,-1)
3 (-1,1,-1)      4 (-1,1,1)     5 (1,-1,-3/4)
6 (1,-1,1)       7 (1,-3/4,-1)  8 (1,1,-1)
9 (1,2,3)

Outward maximal facet cycles:
(0,1,4,3,2), (1,9,4), (3,4,9), (0,5,6,1), (1,6,9),
(2,3,8,7), (3,9,8), (5,7,8,9,6), (0,2,7,5).

Outward normals and heights a_f·x <= h_f:
(-1,0,0):1; (-2,0,2):4; (-1,2,0):3; (0,-1,0):1;
(0,-2,3):5; (0,0,-1):1; (0,4,-1):5; (1,0,0):1;
(0,-1,-1):7/4.
```

These give the actual f-vector (10,17,9), not a B8 roof. Let Q_f=-a_f/h_f. Then closure(D_B)=conv(Q_0,...,Q_8), with parameter volume 337/315. The polar facet corresponding to X9 is

```text
F9 = conv(Q1,Q2,Q6,Q7,Q4),
c9 = average(Q1,Q2,Q6,Q7,Q4) = (-1/30,-16/75,-9/50),
F9' = c9 + (3/4)(F9-c9),
C9 = conv(0,F9') intersect D_B.
```

The five base vertices of C9, in order, are exactly

```text
(11/30,-4/75,-21/50)
(29/120,-83/150,-9/200)
(-1/120,-49/75,21/200)
(-91/120,-4/75,-9/200)
(-1/120,37/150,-99/200).
```

An equivalent membership test requires no convex-hull routine. Set t=-p·X9. Then p belongs to C9 exactly when

```text
0 <= t < 1,
p·(Xi-X9) >= (t/4)(1+c9·Xi)    for every i != 9.
```

For t=0 these inequalities force p=0. For t>0 they state p/t in F9'. Throughout the closed parameter cone all denominators other than l9=1-t are at least 4/25. Only l9 is allowed to vanish on the excluded base. The entire negative pencil (0,h,0), -1/2<h<=0, is contained in C9; the positive pencil remains covered by the inherited theorem.

Five initial parameter tetrahedra are (0,c9,b_j,b_(j+1)), where b_j are the five displayed base vertices. Their interiors are disjoint and their union is the cone closure. The proof uses exact longest-edge bisections of these tetrahedra, not sampled values of p.

## 2. Actual refilled mass, a legitimate boundary gauge, and the all-SPD proof

### 2.1 One common affine normalization

Write l_i=1+p·Xi and fix s=9. For every physical parameter in C9,

```text
A_s = I + X_s p^T,            det(A_s)=l_s>0,
V_s = 0,
V_i = A_s T_p(X_i)-X_s = (X_i-X_s)/l_i  (i != s).
```

The centroid G of conv(V_i) is obtained by actual positive tetrahedral integration from apex V_s. If g is the uniformly refilled centroid of T_p(B), then G=A_s g-X_s. This equality is checked against a separate origin-apex integration, but the identity also follows from an ordinary invertible affine change of variables. It never substitutes T_p(g_old) for g.

For a raw metric M and N=M^(-1), the normalized metrics are exactly

```text
M_hat = A_s^(-T) M A_s^(-1),
N_hat = A_s N A_s^T,
M_hat N_hat = I.
```

Thus arbitrary raw SPD metrics and arbitrary normalized SPD metrics correspond bijectively. There is no independent fitting of a primal and a dual metric.

At a base parameter l_s=0, all the displayed V_i remain finite and the positive apex fan has positive volume. The nine other labels lie in p·V=1, giving an actual limiting pyramid, with possible nonextreme base labels. Convergence of the finite vertex lists gives Hausdorff convergence of their convex hulls, and bounded-volume integration gives convergence of volume and first moment. **The U2 proof does not infer an interior equilibrium count from that limiting pyramid or from a singular limiting metric.** It certifies the polynomial inequalities directly on every parameter cell and uses only l_s>0 for physical members.

### 2.2 Explicit polynomial fields, rather than a finite mass check

Here is the algebra implemented in the complete source below. In a parameter tetrahedron use barycentric coordinates beta_0,...,beta_3 >=0 with sum beta=1. Choose a positive integer D clearing its denominator coefficients, let L_i=D l_i, and put W_i=4(X_i-X_s). Let T_s be the outward triangulation of facets not containing s, and d_t=det(W_a,W_b,W_c)>0 for t=(a,b,c) in T_s. Define

```text
u_s=0, u_i=W_i/L_i,
S = sum_t d_t/(L_a L_b L_c),
J = sum_t [d_t/(L_a L_b L_c)](u_a+u_b+u_c),
Pi = product_(i != s) L_i^2,
H_i = Pi(4 S u_i-J).
```

Each H_i is a homogeneous polynomial vector of degree 14. Set q_s=D and q_i=L_i otherwise. For every true directed edge i->j define the degree-one homogeneous vector

```text
E_ij = 2 q_i q_j (u_j-u_i)/e_ij,
```

where the positive edge divisor e_ij is 1 for edges incident to 9, 1/4 for {0,2} and {5,7}, and otherwise max_k |X_jk-X_ik|. A constant vector here is homogenized by sum beta. The matrix field is

```text
F_ij = H_i E_ij^T + E_ij H_i^T.
```

It has total degree 15 and 816 homogeneous monomials. Let Z_hat_i=V_i-G and delta_ij=Z_hat_j-Z_hat_i. The exact identity is

```text
F_ij = [128 Pi S q_i q_j/(D^2 e_ij)]
       (Z_hat_i delta_ij^T + delta_ij Z_hat_i^T).
```

The scalar multiplier is strictly positive throughout the closed normalized cell. The identity follows directly from V_i=(D/4)u_i and G=(D/4)J/(4S); no finite interpolation assumption is involved. The verifier additionally compares every arrow field with independently integrated actual mass at each initial cell's rational interior point, and checks common reciprocal metric transport there.

For an accepted row of positive integers (arrow,weight), **every one of the 816 coefficient matrices of -sum weight*F_arrow is positive definite**. Each test uses the three exact integer leading principal minors of the symmetric 3 by 3 matrix. Nonnegative homogeneous monomials then establish matrix positivity for all real barycentric coordinates in the cell, including cell faces. No sampled metric and no eigenvalue tolerance enters acceptance.

### 2.3 Why all roots and weak walls are covered

A vertex is strict U exactly when every outgoing true-edge primitive D_ij=Z_i^T M(Z_j-Z_i) is negative. If a vertex is not strict U, some true edge has D_ij>=0. Along such an edge,

```text
||Z_j||_M^2 - ||Z_i||_M^2
 = 2 D_ij + ||Z_j-Z_i||_M^2 > 0.
```

This strict increase holds even when D_ij=0. A maximum-norm vertex is strict U, so a hypothetical U_strict<2 body has exactly one root. Choosing one nonnegative outgoing edge at every other vertex produces an acyclic directed spanning tree into that root.

There are exactly 5440 true spanning trees and 54400 rooted trees. Discovery enumerates edge subsets. Exact verification independently enumerates 530712 possible parent functions and retains exactly 5440 for each of the ten roots. Mass triangulation diagonals are never used as equilibrium arrows.

The certificate is a conditional shape/tree cover. A row at a parameter node excludes all still-possible rooted trees containing its arrows on the entire node tetrahedron. Only the remaining trees are sent to both exact child tetrahedra. Every remaining tree is eventually discharged. If its selected arrows all had nonnegative primitives, tracing the certified positive-definite matrix against the same positive-definite M_hat would be positive, whereas its defining negative sum would have nonpositive trace. This is the contradiction. Zero-arrow walls are included by construction, not discarded in a genericity step.

### 2.4 Actual verification status

Cold discovery started with **no parent rows and no random seeds**. It produced a complete 4614-row certificate. Global row reuse and deterministic greedy pruning retained 3125 rows. Both certificates were separately checked by the standard-library exact verifier. Finally a fresh directory containing only the frozen recovery capsule reconstructed the sources and literal table, repeated the proof, and regenerated all mass and mechanical controls successfully.

The final, pruned proof has:

```text
5 initial parameter tetrahedra
103 proof nodes; 54 terminal cells
3125 positive-integer rows
7184 row/cell applications
5862144 positive-definite coefficient matrices
17586432 strictly positive leading principal minors
54400 true rooted trees
445311 tree/cell discharges in the conditional cover
```

The last number counts repeated shape/tree obligations after parameter subdivision; it is not an incidence-registry count. The main terminal markers actually obtained were

```text
ACTUAL_REFILLED_THREE_PARAMETER_CONE_ALL_SPD_USTRICT_GE_2_PASS
ALL_ROOTS_ZERO_ARROW_WALLS_COMMON_RECIPROCAL_METRIC_AND_DOMAIN_COVER_PASS
COUNTS 3125 103 54 7184 5862144 17586432 445311
BEVEL_THREE_PARAMETER_LITERAL_PROOF_AND_ALL_CONTROLS_RECOVERY_PASS
```

## 3. Full-D_B true adjoint and boundary geometry

Let L(p)=product_i(1+p·Xi). There is a primitive integer polynomial A(p), of total degree six, with exactly 84 nonzero monomials and A(0)=9168, such that throughout all D_B

```text
Volume(T_p(B)) = A(p)/(768 L(p)),
g(p) = (1/4)[sum_i Xi/(1+p·Xi) - grad A(p)/A(p)].
```

This is an explicit realization of the inherited true-refilled mass-potential formula, not transport of the old centroid. The journal's general centroid-map statement is retained only in that actual-mass sense.

All 84 exact coefficients are reconstructed without a symbolic algebra dependency. Put U_i=4Xi and h_i=4 tau+U_i·p. For the sixteen outward origin-fan triangles, form

```text
R(tau,p) = sum_t det(U_a,U_b,U_c) product_(i not in t) h_i.
```

The exact polynomial division is R=8192 tau A_homogeneous_degree6. This generator, coefficient ordering, and SHA are in the runnable unit below. The alternative positive-product identity

```text
A(p) = 128 sum_t det(X_a,X_b,X_c) product_(i not in t) l_i
```

proves A>0 in D_B. On closure(D_B), its zero set consists exactly of Q0,Q3,Q5,Q7,Q8, the poles of nonsimplicial facets. A boundary zero set with one vertex, a true edge, or a triangular facet is contained in some mass triangle, leaving a strictly positive summand. A quadrilateral or pentagonal facet cannot be contained in a triangle, so every summand vanishes there.

For u=(x,y,z), the lowest nonzero Taylor terms of A(Q_f+u) are:

```text
f0, order2: 256(127x^2+98xy+98xz-y^2+2yz-z^2)
f1, order0: 6720
f2, order0: 630784/81
f3, order1: 168(z-8y)
f4, order0: 4769856/625
f5, order1: 224(y-8z)
f6, order0: 6830208/625
f7, order2: 256(223x^2-203xy-140xz+22y^2+5yz-27z^2)
f8, order1: -1620(y+z).
```

The order at a facet pole is exactly its facet size minus three. The leading form also has a geometric positive-product representation: multiply 128 times the positive nonfacet slacks by the sum over triangles in that facet of det(X_t) times the product of u·Xi over facet vertices outside the triangle. This is positive on every nonzero feasible tangent-cone direction. Thus the polynomial's boundary degeneracies are localized and have explicit geometric orders; they are not mysterious numerical denominator failures. No equilibrium exclusion outside C9 is deduced from these mass identities alone.

## 4. Complete fixed-simplex charts for seven full radial stars

This is a second actual-body theorem, concerning normalization rather than U counts. For a simple original vertex s, order its three true neighbors so the matrix W with columns X_neighbor-X_s has positive determinant. Define

```text
r_i = W^(-1)(Xi-X_s) >= 0,
b = -W^(-1)X_s > 0.
```

For every independent triple a=(a1,a2,a3)>=0, set

```text
lambda = 1/(1+b·a),
p(a) = lambda W^(-T)a,
D_a = diag(1+a1,1+a2,1+a3),
Phi_i(a) = D_a r_i/(1+a·r_i).
```

This parametrizes the **whole** radial star

```text
R_s = {p in D_B : p·(Xi-X_s)>=0 for every i},
```

not a finite box in that star. Its inverse is a_k=p·(X_neighbor_k-X_s)/l_s. The exact affine map from the actual projective image is

```text
B(a) = lambda D_a W^(-1)(I+X_s p(a)^T),
t(a) = -lambda D_a W^(-1)X_s,
Phi_i = B(a)T_p(Xi)+t(a).
```

For every finite a, B is invertible and has positive determinant. The same M,N transform by B^(-T)MB^(-1) and BNB^T. The code recomputes the actual volume centroid of conv(Phi_i) by its positive vertex-s fan.

The four frame vertices are permanently 0,e1,e2,e3, and

```text
0 <= Phi_ik(a) <= max(1,r_ik),
conv(0,e1,e2,e3) is contained in conv(Phi_i(a)).
```

Consequently all these actual bodies stay in one bounded coordinate box and have volume at least 1/6. Every escaping sequence of a has a subsequence whose vertex lists converge to a full-dimensional convex body containing the same tetrahedron. Hausdorff convergence and bounded integration justify convergence of its own volume and centroid. Different escape rates can give different limiting shapes; a single unblown cube corner is not asserted to encode every limit. No conclusion about a singular limiting metric is made.

The simple vertices are 0,2,4,5,6,7,8. Their disjoint-interior radial stars have total parameter volume 211/315, hence fraction 211/337 of D_B. For reference, the ten complete star volumes, in label order, are

```text
2/21, 2/15, 2/21, 7/45, 1/18, 2/21, 1/10, 2/21, 2/15, 1/9.
```

The fixed-simplex chart removes global coordinate collapse in a genuinely three-parameter, noncompact orthant. It does not impose any metric-conditioning bound, and it does not by itself close the remaining weak-tree/metric problem. Its next useful application is an orthant polynomial or stratified boundary certificate using the same actual centroid and reciprocal metric.

## 5. Exact controls and sharpness

### 5.1 A three-parameter strict323weak000 body inside C9

Take p=(-1/60,-8/75,-9/100)=c9/2. For Y_i=Xi/(1+p·Xi), the exact own volume and centroid are

```text
V = 7369532149603250/375485247003421,
g = (
 3406870616718122794327026000/11068602397973713790946170873,
 152646969591469194702289199007/177097638367579420655138733968,
 13861149992144592443575259718/11068602397973713790946170873
).
```

Use M=diag(484,1,1) and N=diag(1/484,1,1). The physical Euclidean vertices are diag(22,1,1)(Y_i-g), with own centroid zero and volume 22V. The complete mechanical result is

```text
S facets = [4,5,6], U vertices = [4,9], H edge IDs = [7,9,11],
strict(S,U,H)=(3,2,3), weak000.
```

Edge IDs use the sorted true edge list generated from the displayed maximal cycles. All 68 primal/dual edge primitives are nonzero. Every common-metric edge-foot identity and the Euler count 3+2-3=2 was checked exactly. The complete rational ledger is reconstructed by mode control.

For every rational p in D_B the flag mode also gives a finite exact U2 construction. Choose the least n>=0 for which a=(1,n,n^2) has nonzero pairing with every centered vertex and every pair difference. Put b=(-n,1,0), c=a cross b. For all true arrows form

```text
T = max(1, (|(b·Zi)(b·e)|+|(c·Zi)(c·e)|)/|(a·Zi)(a·e)|),
K = isqrt(ceil(T))+1,
physical linear map = matrix with rows K*a, b, c.
```

Then K^2>T makes every primal-arrow sign equal to sign((a·Zi)(a·e)). Exactly the two extrema of the generic linear functional a are strict U. Finite polynomial avoidance proves termination, and the same domination argument works for real p. Together with the C9 lower theorem, this proves min_M U_strict=2 for every shape in C9. No general S/H or weak000 assertion is attached to this one-axis flag construction; the specific control above has its own full census.

### 5.2 A low-coordinate, nonwinning strict547weak000 body

Use the complete simple-vertex chart with s=4, neighbors (1,3,9), b=(3/4,1,1/2), and a=(1,2,3). Then lambda=4/21 and p=(11/21,-2/21,-4/21). The uncentered Euclidean frame vertices are exactly

```text
0 (8/15,7/10,0)
1 (1,0,0)
2 (14/31,24/31,0)
3 (0,1,0)
4 (0,0,0)
5 (12/37,45/74,16/37)
6 (2/5,2/5,8/15)
7 (22/75,16/25,32/75)
8 (2/17,12/17,8/17)
9 (0,0,1).
```

Their coordinate denominators are at most 75. The own volume is 128798/487475 and the own centroid is

```text
(214328935999/753429660600,
 10048324859/31392902525,
 2564582434/9114068475).
```

After subtracting that centroid, use physical M=N=I. Exact full census gives

```text
S=[0,1,2,3,4], U=[1,3,4,9], H=[0,3,4,5,8,11,16],
strict547weak000, with no zero among all 68 primitives.
```

The source checks the same 68 primitives in the raw projective coordinates under M_raw=B^T B and N_raw=B^(-1)B^(-T), as well as all foot identities. This is not a U1 counterexample or record attainer. It is retained for its bounded geometry, small coordinates, and usefulness as a starting body outside C9.

## 6. Recovery, exact identities, and what remains open

The two complete source units following this section are sufficient for cold, empty-seed reconstruction; they import no parent files and contain the complete literal geometry, field generator, row locator, exact verifier, mass adjoint, controls, and global row pruner. The executed discovery stack was CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, its bundled HiGHS 1.8.0, and OpenBLAS 0.3.30 on x86-64/SkylakeX, with OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=1 and no RNG. All nondefault search parameters are literal in the source. Exact verification, mass, and control generation use only the Python standard library.

Save the code blocks as bevel3_recovery.py and prune_cone.py in a fresh directory. Reconstruction and verification commands are:

```sh
python bevel3_recovery.py build 9 3/4
python -S bevel3_recovery.py verify certificate.json
python prune_cone.py certificate.json pruned.json
python -S bevel3_recovery.py verify pruned.json
python -S bevel3_recovery.py mass
python -S bevel3_recovery.py control
python -S bevel3_recovery.py flag -1/60 -8/75 -9/100
python -S bevel3_recovery.py frame 4 1 2 3
```

Never use -O. The first build produced the cold certificate SHA below, then the pruner produced the final proof SHA below. Floating-point discovery is not the acceptance test: changing solver or linear-algebra implementations can change which valid integer rows are selected. The stated single-thread stack produced these exact bytes. A different table must pass the exact verifier and must not be called byte-identical without checking.

For platform-independent frozen-table replay, the supplemental recover_bevel3.py contains the complete source units and literal final coefficient table in a lossless, hashed capsule. A fresh directory with only that file was actually tested with `python -S recover_bevel3.py check`; it reproduced every final output and the last recovery marker above. Its `locate` mode additionally performs cold discovery and pruning and checks byte parity. The readable cold reconstruction below remains part of this handoff, rather than requiring the supplemental file as its only source.

The principal byte identities are:

```text
bevel3_recovery.py 24123
fc7ca6255ce59fa9276834f7ed48eb042cc9a39818b8d670038f3d6d86761c5b
prune_cone.py 2534
4335a6847dddef4bff62444cbdc01e3d0cb0795e14487d1c3de24147e4a951e3
cold certificate.json 215946
cb5e2101e053902dca4f8a03b3dde50cb00df32858254281e3f45cfb1d5e37be
final pruned.json / frozen certificate.json 132198
567ce59194fc3b19e585c2b6ca6a0b8e36835c7e7b9fa779636c1b840fc94f34
final verification_report.json 3230
c4645c1a3c0bbca57a956a22d522dad87c8f662dc43d6a00f3db98bda6da7815
adjoint.tsv 965
2b720d9cfc7e46f78179d1dbee58e99f14bbcf574ca66a0731c88b8b385ba45b
adjoint_boundary.json 872
79a3c4a1dd3f9a672f58790262bf471b5418a81db7e4d51c38b3ab00dfe46ad9
three_parameter_control.json 21262
2e9742a6648ef7315a195d86f3260ff0406904814224e54845ee0e1b4e462f5c
flag_body.json 2793
6bccdccf9d7321e85a9eac9c747d84ba7ce6184b813aaed03f9766257b0a1a23
simple_frame.json 9531
c9b9def094f7236bbdca14edf71c102787e3adb6438696e2fcd9082246dc0d50
recover_bevel3.py 48997
bbcb27b8849fe92460bc6f3791830a76d54bace075f2fa4e5aaaee612303ac7a
```

The cold verifier also passed 11794464 PD coefficient matrices before pruning; its report was 3232 bytes, SHA-256 e2d97a4b83f8d40f342d7678710c222ef3a8728d2bd17a38d75a989cb47be65a. Those larger proof data are not a different body or a stronger geometric exclusion.

Relative to this result and the inherited full pencil, the remaining projective shape complement is exactly

```text
D_B minus [C9 union {(0,h,0): -1/2<h<1}].
```

No assertion is made that every point of this written complement escapes every previously known affine-family theorem; I did not classify all such overlaps. The existing four-shape theorem and eleven-dimensional realization frontier remain as stated in the supplied memory.

Exploration of broader facet-star coverage did not produce a completed all-D_B certificate or a U1 construction. The `build all 3/4` continuation mode is not an accepted theorem; it may stop with an unresolved shape/tree cell. Such a failure is not an exclusion proof or evidence of U1. The most useful next direction is to combine the exact full-D_B adjoint with the fixed-simplex orthant charts, which keep the actual bodies full-dimensional at shape infinity, then handle the common-metric weak-tree obligations and their rank-degenerate metric limits. Merely bounding metric condition numbers would miss the remaining problem.

Supplemental artifacts: frozen source-and-literal-proof capsule (`recover_bevel3.py`) and verified complete bundle (`bevel3_handoff.zip`).

## Complete runnable source unit 1: bevel3_recovery.py

```python
"""BEVEL_FACET9_THREE_PARAMETER_ALL_SPD_V1.
CPython 3.13.5. Exact verification uses the standard library only.
Discovery: NumPy 2.3.5, SciPy 1.17.0, OpenBLAS 0.3.30, one thread.
python bevel3_recovery.py build [9|all] [gamma]
python -S bevel3_recovery.py verify [certificate.json]
python -S bevel3_recovery.py mass
python -S bevel3_recovery.py control
The literal parent is minimum-0107, advertised SHA
37b21117ba32f0a13744c8144bca7aaf5d013efc95413c0c9bdbc95894ff674e.
No parent file, numerical solver, or sampled metric is a verification input.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from fractions import Fraction as F
from itertools import combinations,product
from math import comb,gcd,lcm,factorial,isqrt
from pathlib import Path
import json,hashlib,sys
assert __debug__
X=tuple(tuple(map(F,v))for v in[(-1,-1,F(-3,4)),(-1,-1,1),(-1,F(-3,4),-1),(-1,1,-1),(-1,1,1),(1,-1,F(-3,4)),(1,-1,1),(1,F(-3,4),-1),(1,1,-1),(1,2,3)])
CY=((0,1,4,3,2),(1,9,4),(3,4,9),(0,5,6,1),(1,6,9),(2,3,8,7),(3,9,8),(5,7,8,9,6),(0,2,7,5))
AA=tuple(tuple(map(F,v))for v in[(-1,0,0),(-2,0,2),(-1,2,0),(0,-1,0),(0,-2,3),(0,0,-1),(0,4,-1),(1,0,0),(0,-1,-1)])
HH=tuple(map(F,[1,4,3,1,5,1,5,1,F(7,4)]))
ED=tuple(sorted({tuple(sorted((i,j)))for cy in CY for i,j in zip(cy,cy[1:]+cy[:1])}))
ADJ=tuple(tuple(sorted(j if i==v else i for i,j in ED if v in(i,j)))for v in range(10))
AR=tuple((i,j)for i in range(10)for j in ADJ[i]);IX={e:i for i,e in enumerate(AR)}
TRI=tuple((cy[0],cy[k],cy[k+1])for cy in CY for k in range(1,len(cy)-1))
SIX=((0,0),(0,1),(0,2),(1,1),(1,2),(2,2))
MON=tuple((a,b,c,15-a-b-c)for a in range(16)for b in range(16-a)for c in range(16-a-b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def add(a,b):return [x+y for x,y in zip(a,b)]
def sub(a,b):return [x-y for x,y in zip(a,b)]
def sc(k,a):return [k*x for x in a]
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def det(A):return dot(A[0],cross(A[1],A[2]))
def tr(A):return list(map(list,zip(*A)))
def mv(A,x):return [dot(r,x)for r in A]
def mm(A,B):return [[dot(r,c)for c in zip(*B)]for r in A]
def outer(a,b):return [[x*y for y in b]for x in a]
def eye():return [[F(i==j)for j in range(3)]for i in range(3)]
def inverse(A):
 A=[list(map(F,r))+e for r,e in zip(A,eye())]
 for k in range(3):
  j=next(j for j in range(k,3)if A[j][k]);A[k],A[j]=A[j],A[k];a=A[k][k];A[k]=[x/a for x in A[k]]
  for j in range(3):
   if j!=k:a=A[j][k];A[j]=[x-a*y for x,y in zip(A[j],A[k])]
 return [r[3:]for r in A]
def mins(v):
 a,b,c,d,e,f=v
 return (a,a*d-b*b,a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b)
def canonical(x):
 def enc(o):
  if isinstance(o,F):return str(o)
  if isinstance(o,dict):return {str(k):enc(v)for k,v in o.items()}
  if isinstance(o,(tuple,list)):return [enc(v)for v in o]
  return o
 return (json.dumps(enc(x),sort_keys=True,separators=(',',':'))+'\n').encode()
def write(name,obj):
 b=canonical(obj);Path(name).write_bytes(b);print(name,len(b),hashlib.sha256(b).hexdigest(),flush=True);return b

def geometry():
 assert (len(X),len(ED),len(CY),len(AR),len(TRI),len(MON))==(10,17,9,34,16,816)
 for a,h,cy in zip(AA,HH,CY):
  assert {i for i,v in enumerate(X)if dot(a,v)==h}==set(cy)
  assert all(dot(a,v)<h for i,v in enumerate(X)if i not in cy)
  for i,j in zip(cy,cy[1:]+cy[:1]):
   t=cross(a,sub(X[j],X[i]));assert all(dot(t,sub(X[k],X[i]))>0 for k in cy if k not in(i,j))
 found=set()
 for i,j,k in combinations(range(10),3):
  a=cross(sub(X[j],X[i]),sub(X[k],X[i]));
  if not any(a):continue
  ds=[dot(a,sub(v,X[i]))for v in X]
  if max(ds)<=0 or min(ds)>=0:found.add(frozenset(v for v,d in enumerate(ds)if d==0))
 assert found==set(map(frozenset,CY))
 assert all(sum(i in cy and j in cy for cy in CY)==2 for i,j in ED)
 assert all(det([X[i]for i in t])>0 for t in TRI)
 assert sum(det([X[i]for i in t])for t in TRI)==F(573,8)

def trees(independent=False):
 out=[]
 if independent:
  tried=0
  for root in range(10):
   nodes=[i for i in range(10)if i!=root];count=0
   for choices in product(*(ADJ[i]for i in nodes)):
    tried+=1;par=dict(zip(nodes,choices));ok=True
    for start in nodes:
     seen=set();v=start
     while v!=root:
      if v in seen:ok=False;break
      seen.add(v);v=par[v]
     if not ok:break
    if ok:
     count+=1;em=sum(1<<ED.index(tuple(sorted(e)))for e in par.items());mask=sum(1<<IX[e]for e in par.items());out.append((em,root,mask))
   assert count==5440
  assert tried==530712
 else:
  for ids in combinations(range(17),9):
   adj=[[]for _ in range(10)]
   for k in ids:i,j=ED[k];adj[i].append(j);adj[j].append(i)
   seen={0};todo=[0]
   for i in todo:
    for j in adj[i]:
     if j not in seen:seen.add(j);todo.append(j)
   if len(seen)!=10:continue
   for root in range(10):
    par={root:root};todo=[root]
    for i in todo:
     for j in adj[i]:
      if j not in par:par[j]=i;todo.append(j)
    out.append((sum(1<<k for k in ids),root,sum(1<<IX[i,par[i]]for i in range(10)if i!=root)))
 assert len(out)==54400
 return sorted(out)

def domains(gamma,charts=range(10)):
 Q=[tuple(-a/h for a in n)for n,h in zip(AA,HH)];out=[]
 assert 0<gamma<=1
 for s in charts:
  ids=[f for f,cy in enumerate(CY)if s in cy];adj={f:[]for f in ids}
  for j in ADJ[s]:
   a,b=[f for f in ids if j in CY[f]];adj[a].append(b);adj[b].append(a)
  cyc=[min(ids),min(adj[min(ids)])]
  while True:
   nxt=next(f for f in adj[cyc[-1]]if f!=cyc[-2])
   if nxt==cyc[0]:break
   cyc.append(nxt)
  assert set(cyc)==set(ids)
  center=tuple(sum(Q[f][k]for f in ids)/len(ids)for k in range(3))
  vs=[tuple(gamma*x+(1-gamma)*y for x,y in zip(Q[f],center))for f in cyc]
  assert dot(center,X[s])==-1 and all(dot(center,X[i])>-1 for i in range(10)if i!=s)
  for j in range(len(vs)):out.append((s,j,[(F(0),)*3,center,vs[j],vs[(j+1)%len(vs)]]))
 return out

def split(points):
 _,i,j=max((sum((points[i][k]-points[j][k])**2 for k in range(3)),i,j)for i in range(4)for j in range(i+1,4))
 mid=tuple((a+b)/2 for a,b in zip(points[i],points[j]));a=points[:];b=points[:];a[j]=mid;b[i]=mid
 return a,b

def mul_lin(P,L):
 Q={}
 for m,v in P.items():
  for j,a in enumerate(L):
   if a:e=list(m);e[j]+=1;e=tuple(e);Q[e]=Q.get(e,0)+v*a
 return Q

def add_to(P,Q,w):
 if w:
  for m,v in Q.items():P[m]=P.get(m,0)+w*v

def edge_scale(i,j):
 return F(1)if 9 in(i,j)else(F(1,4)if {i,j}in({0,2},{5,7})else max(map(abs,sub(X[j],X[i]))))

def fields(s,points):
 W0=[[int(4*(x-y))for x,y in zip(v,X[s])]for v in X]
 tris=[(cy[0],cy[k],cy[k+1])for cy in CY if s not in cy for k in range(1,len(cy)-1)]
 raw=[[1+dot(p,v)for p in points]for v in X];D=lcm(*(x.denominator for row in raw for x in row))
 L=[[int(D*x)for x in row]for row in raw]
 assert min(L[s])>=0 and all(min(L[i])>0 for i in range(10)if i!=s)
 cache={}
 def quotient(ids):
  key=tuple(sorted(ids))
  if key not in cache:
   ex={i:2 for i in range(10)if i!=s}
   for i in key:ex[i]-=1
   assert min(ex.values())>=0
   P={(0,0,0,0):1}
   for i,n in ex.items():
    for _ in range(n):P=mul_lin(P,L[i])
   cache[key]=P
  return cache[key]
 J=[{}for _ in range(3)];V=[[{}for _ in range(3)]for i in range(10)]
 for t in tris:
  d=int(det([W0[i]for i in t]));assert d>0
  for i in t:
   Q=quotient(t+(i,))
   for k in range(3):add_to(J[k],Q,d*W0[i][k])
  for i in range(10):
   if i==s:continue
   Q=quotient(t+(i,))
   for k in range(3):add_to(V[i][k],Q,4*d*W0[i][k])
 for i in range(10):
  for k in range(3):add_to(V[i][k],J[k],-1)
 out=[]
 for i,j in AR:
  scale=edge_scale(i,j)
  if i==s:E=[[2*D*x/scale]*4 for x in W0[j]]
  elif j==s:E=[[-2*D*x/scale]*4 for x in W0[i]]
  else:E=[[2*(L[i][b]*W0[j][k]-L[j][b]*W0[i][k])/scale for b in range(4)]for k in range(3)]
  assert all(x.denominator==1 for row in E for x in row);E=[[int(x)for x in row]for row in E]
  row=[]
  for a,b in SIX:
   P=mul_lin(V[i][a],E[b]);add_to(P,mul_lin(V[i][b],E[a]),1);row.append(P)
  assert all(sum(m)==15 for P in row for m in P)
  out.append([[P.get(m,0)for P in row]for m in MON])
 return out

def check_row(row,B):
 for k in range(816):
  K=[-sum(w*B[i][k][j]for i,w in row)for j in range(6)]
  if min(mins(K))<=0:return False
 return True

def integrate(Y,apex=None):
 if apex is None:
  tris=TRI;o=[F(0)]*3
 else:
  tris=[(cy[0],cy[k],cy[k+1])for cy in CY if apex not in cy for k in range(1,len(cy)-1)];o=Y[apex]
 S=F(0);J=[F(0)]*3
 for t in tris:
  vs=[Y[i]for i in t];d=det([sub(v,o)for v in vs]);assert d>0;S+=d
  for k in range(3):J[k]+=d*(o[k]+sum(v[k]for v in vs))/4
 return S/6,sc(1/S,J)

def mass_audit(s,points,B):
 beta=(F(1,4),)*4;p=[sum(beta[b]*points[b][k]for b in range(4))for k in range(3)]
 ls=[1+dot(p,v)for v in X];assert min(ls)>0
 Y=[sc(1/l,v)for l,v in zip(ls,X)];volume,g=integrate(Y)
 A=[[F(i==j)+X[s][i]*p[j]for j in range(3)]for i in range(3)]
 Z=[sub(v,g)for v in Y];VV=[sub(mv(A,v),X[s])for v in Y];Vhat,G=integrate(VV,s)
 assert det(A)==ls[s] and Vhat==ls[s]*volume and G==sub(mv(A,g),X[s])
 Zhat=[sub(v,G)for v in VV]
 M=[[3,1,0],[1,2,1],[0,1,2]];N=inverse(M);Ai=inverse(A);Mh=mm(mm(tr(Ai),M),Ai);Nh=mm(mm(A,N),tr(A));assert mm(Mh,Nh)==eye()
 for i,j in AR:assert dot(Z[i],mv(M,sub(Z[j],Z[i])))==dot(Zhat[i],mv(Mh,sub(Zhat[j],Zhat[i])))
 # Homogeneous fields versus separately integrated actual chart mass.
 raw=[[1+dot(q,v)for q in points]for v in X];D=lcm(*(x.denominator for r in raw for x in r));L=[D*l for l in ls];Lp=F(1)
 for i in range(10):
  if i!=s:Lp*=L[i]**2
 Smodel=6*Vhat*(F(4,D))**3
 for row,(i,j)in zip(B,AR):
  vals=[sum(F(row[k][a],4**15)for k in range(816))for a in range(6)]
  ui=D if i==s else L[i];uj=D if j==s else L[j]
  fac=F(128)*Lp*Smodel*ui*uj/(D*D*edge_scale(i,j));e=sub(Zhat[j],Zhat[i])
  assert vals==[fac*(Zhat[i][a]*e[b]+Zhat[i][b]*e[a])for a,b in SIX]
 return {'p':p,'volume':volume,'COM':g,'chart_volume':Vhat,'chart_COM':G}

def adjoint():
 U=[[int(4*x)for x in v]for v in X];R={}
 for t in TRI:
  P={(0,0,0,0):int(det([U[i]for i in t]))}
  for i in range(10):
   if i not in t:P=mul_lin(P,[4]+U[i])
  add_to(R,P,1)
 R={m:a for m,a in R.items()if a}
 assert all(m[0]>0 and a%8192==0 for m,a in R.items())
 A={m[1:]:a//8192 for m,a in R.items()};assert len(A)==84 and max(map(sum,A))==6 and A[0,0,0]==9168
 return A

def mass_outputs():
 A=adjoint();b=''.join(','.join(map(str,list(m)+[a]))+'\n'for m,a in sorted(A.items())).encode();Path('adjoint.tsv').write_bytes(b)
 assert len(b)==965 and hashlib.sha256(b).hexdigest()=='2b720d9cfc7e46f78179d1dbee58e99f14bbcf574ca66a0731c88b8b385ba45b'
 leads=[]
 for f,(a,h,cy)in enumerate(zip(AA,HH,CY)):
  q=[-x/h for x in a];T={}
  for m,v in A.items():
   for e in product(*(range(x+1)for x in m)):
    z=F(v)
    for power,choose,x in zip(m,e,q):z*=comb(power,choose)*x**(power-choose)
    T[e]=T.get(e,F(0))+z
  T={m:a for m,a in T.items()if a};order=min(map(sum,T));assert order==len(cy)-3
  leads.append({'facet':f,'point':q,'order':order,'terms':[[*m,a]for m,a in sorted(T.items())if sum(m)==order]})
 b=write('adjoint_boundary.json',leads);assert len(b)==872 and hashlib.sha256(b).hexdigest()=='79a3c4a1dd3f9a672f58790262bf471b5418a81db7e4d51c38b3ab00dfe46ad9'
 vols=[F(0)]*10
 for s,j,ps in domains(F(1)):vols[s]+=abs(det(ps[1:]))/6
 assert sum(vols)==F(337,315) and vols[9]==F(1,9)
 print('FULL_THREE_PARAMETER_ADJOINT_84_TERMS_BOUNDARY_ORDERS_AND_POLAR_VOLUMES_PASS')

def control():
 p=[-F(1,60),-F(8,75),-F(9,100)];ls=[1+dot(p,v)for v in X];Y=[sc(1/l,v)for l,v in zip(ls,X)];V,g=integrate(Y);Z=[sub(v,g)for v in Y]
 assert integrate(Y,9)==(V,g)
 normals=[add(a,sc(h,p))for a,h in zip(AA,HH)];Q=[sc(1/(h-dot(a,g)),a)for a,h in zip(normals,HH)]
 M=[[484,0,0],[0,1,0],[0,0,1]];N=inverse(M);A=[[22,0,0],[0,1,0],[0,0,1]]
 recipe=flag(p);assert recipe['physical_A']==A and recipe['K']==22 and recipe['n']==0
 def roots(P,G):return [i for i,x in enumerate(P)if all(dot(x,mv(G,sub(y,x)))<0 for j,y in enumerate(P)if j!=i)]
 S=roots(Q,N);U=roots(Z,M);H=[];ledger=[];zeros=[]
 for ei,(i,j)in enumerate(ED):
  f,k=[a for a,cy in enumerate(CY)if i in cy and j in cy]
  a=dot(Z[i],mv(M,sub(Z[j],Z[i])));b=dot(Z[j],mv(M,sub(Z[i],Z[j])));d=dot(Q[f],mv(N,sub(Q[k],Q[f])));e=dot(Q[k],mv(N,sub(Q[f],Q[k])))
  vals=[a,b,d,e]
  if max(vals)<0:H.append(ei)
  if 0 in vals:zeros.append(ei)
  dd=-a-b;de=dot(Q[f],mv(N,Q[f]))*dot(Q[k],mv(N,Q[k]))-dot(Q[f],mv(N,Q[k]))**2;assert dd>0 and de>0
  foot=add(Z[i],sc(-a/dd,sub(Z[j],Z[i])));co=[-e/de,-d/de];assert mv(M,foot)==add(sc(co[0],Q[f]),sc(co[1],Q[k]))
  ledger.append({'edge':[i,j],'facets':[f,k],'primitives':vals,'foot':foot,'components':[-a/dd,1+a/dd]+co})
 physical=[mv(A,z)for z in Z];VP,GP=integrate(physical);assert GP==[0,0,0]and VP==22*V
 assert (S,U,H,zeros)==([4,5,6],[4,9],[7,9,11],[])and len(S)+len(U)-len(H)==2
 obj={'p':p,'vertices':Y,'COM':g,'volume':V,'M':M,'N':N,'S':S,'U':U,'H':H,'zeros':zeros,'ledger':ledger,'physical_A':A,'physical_vertices':physical,'physical_COM':GP,'physical_volume':VP}
 b=write('three_parameter_control.json',obj);assert len(b)==21262 and hashlib.sha256(b).hexdigest()=='2e9742a6648ef7315a195d86f3260ff0406904814224e54845ee0e1b4e462f5c'
 print('ACTUAL_THREE_PARAMETER_RATIONAL_EUCLIDEAN_323_WEAK000_OWN_MASS_PASS')

def arrow_covers(T):
 n=(len(T)+7)//8;raw=[bytearray(n)for _ in AR]
 for k,(_,root,mask)in enumerate(T):
  while mask:
   low=mask&-mask;a=low.bit_length()-1;raw[a][k//8]|=1<<(k%8);mask-=low
 return [int.from_bytes(x,'little')for x in raw]

def findrow(ids,B):
 import numpy as np
 from scipy.optimize import linprog
 Q=-B[ids];n=len(ids);cs=[];rhs=[]
 for i in range(3):
  rr=np.concatenate([-Q[:,:,i,i].T,np.ones((len(Q[0]),1))],axis=1);cs.extend(rr);rhs.extend([0.]*len(rr))
 for it in range(100):
  res=linprog(np.r_[np.zeros(n),-1],A_ub=np.array(cs),b_ub=rhs,A_eq=np.array([np.r_[np.ones(n),0]]),b_eq=[1],bounds=[(0,None)]*n+[(None,None)],method='highs')
  if not res.success or res.x[-1]<1e-6:return None
  lam=res.x[:-1];K=np.einsum('a,akij->kij',lam,Q);ev,vec=np.linalg.eigh(K)
  if ev.min()>max(1e-6,res.x[-1]*.05):
   for scale in [10,30,100,300,1000,3000,10000,100000,1000000]:
    ws=np.rint(lam*scale).astype(int);row=[(i,int(w))for i,w in zip(ids,ws)if w]
    if np.linalg.eigvalsh(-sum(w*B[i]for i,w in row))[:,0].min()>1e-7:
     g=gcd(*(w for i,w in row));return tuple((i,w//g)for i,w in row)
  for k in np.argsort(ev[:,0])[:min(32,len(ev))]:
   z=vec[k,:,0];cc=-np.einsum('i,aij,j->a',z,Q[:,k],z);cs.append(np.r_[cc,1]);rhs.append(0.)
 return None

def build(charts=(9,),gamma=F(3,4)):
 import numpy as np,scipy,time
 assert np.__version__=='2.3.5' and scipy.__version__=='1.17.0'
 geometry();T=trees();ac=arrow_covers(T);FULL=(1<<54400)-1;rows=[];known={};covers=[]
 def install(row):
  row=tuple(map(tuple,row))
  if row not in known:
   known[row]=len(rows);rows.append(row);cover=FULL
   for i,w in row:cover&=ac[i]
   covers.append(cover)
  return known[row]
 stack=[(s,j,'',ps,FULL)for s,j,ps in domains(gamma,charts)[::-1]];nodes=[];start=time.time()
 def save(complete):
  obj={'identity':'BEVEL_FACET9_THREE_PARAMETER_ALL_SPD_V1','gamma':str(gamma),'charts':list(charts),'maxdepth':14,'complete':complete,'rows':rows,'nodes':nodes}
  Path('certificate.json').write_bytes(canonical(obj))
 while stack:
  s,j,key,points,remain=stack.pop();B=fields(s,points);BF=np.array(B,dtype=float)
  multi=np.array([factorial(15)//product_int(factorial(x)for x in m)for m in MON],float)
  BF/=np.max(np.abs(BF));BF/=multi[None,:,None];BF/=np.max(np.abs(BF));a,b,c,d,e,f=np.moveaxis(BF,-1,0)
  BF=np.stack([a,b,c,b,d,e,c,e,f],axis=-1).reshape(34,816,3,3)
  if s==9:
   A=np.array([[1,-.5,0],[0,-1.5,1],[0,1,0]]);BF=np.einsum('ij,akjl,ml->akim',A,BF,A)
  BF/=np.max(np.abs(BF),axis=(0,2,3))[None,:,None,None];assert np.isfinite(BF).all()
  corners=[k for k,m in enumerate(MON)if max(m)==15];trial=sorted(set(corners+list(range(0,816,41))));used=[]
  def numerical(row):
   for ks in [corners,trial,range(816)]:
    if np.linalg.eigvalsh(-sum(w*BF[i,ks]for i,w in row))[:,0].min()<=1e-8:return False
   return True
  for rid,row in enumerate(rows):
   if remain&covers[rid] and numerical(row) and check_row(row,B):used.append(rid);remain&=~covers[rid]
  for it in range(1000):
   if not remain:break
   idx=(remain&-remain).bit_length()-1;m=T[idx][2];ids=[i for i in range(34)if(m>>i)&1];row=findrow(ids,BF)
   if row is None:break
   assert check_row(row,B);rid=install(row);used.append(rid);remain&=~covers[rid]
  nodes.append({'s':s,'j':j,'key':key,'rows':used})
  print('NODE',s,j,key or '-',len(used),remain.bit_count(),len(rows),round(time.time()-start,2),flush=True)
  if remain:
   if len(key)>=14:save(False);raise AssertionError(('UNRESOLVED_SHAPE_TREE_CELL',s,j,key,T[(remain&-remain).bit_length()-1]))
   a,b=split(points);stack.extend([(s,j,key+'1',b,remain),(s,j,key+'0',a,remain)])
  save(not stack)
 b=Path('certificate.json').read_bytes();print('COLD_EMPTY_SEED_CONTINUOUS_CERTIFICATE_BUILD_PASS',len(b),hashlib.sha256(b).hexdigest(),flush=True)

def product_int(xs):
 z=1
 for x in xs:z*=x
 return z

def verify(path='certificate.json'):
 geometry();data=Path(path).read_bytes();obj=json.loads(data);assert data==canonical(obj) and obj['complete'] is True
 assert obj['identity']=='BEVEL_FACET9_THREE_PARAMETER_ALL_SPD_V1';gamma=F(obj['gamma']);charts=tuple(obj['charts'])
 assert 0<gamma<1 and charts and len(set(charts))==len(charts)and all(isinstance(s,int)and 0<=s<10 for s in charts)
 T=trees(True);ac=arrow_covers(T);FULL=(1<<54400)-1;rows=obj['rows'];covers=[]
 for row in rows:
  assert row and all(isinstance(i,int)and 0<=i<34 and isinstance(w,int)and w>0 for i,w in row)
  assert len({AR[i][0]for i,w in row})==len(row);cov=FULL
  for i,w in row:cov&=ac[i]
  assert cov;covers.append(cov)
 nodes={(r['s'],r['j'],r['key']):r for r in obj['nodes']};assert len(nodes)==len(obj['nodes'])
 count=0;apps=0;leaves=0;discharged=0;audits=[];visited=set();initial=domains(gamma,charts)
 for s,j,ps in initial:audits.append(mass_audit(s,ps,fields(s,ps)))
 def rec(s,j,key,points,remain):
  nonlocal count,apps,leaves,discharged
  ident=(s,j,key);assert ident in nodes and ident not in visited;visited.add(ident);r=nodes[ident];B=fields(s,points);before=remain.bit_count()
  for rid in r['rows']:
   assert isinstance(rid,int)and 0<=rid<len(rows)and remain&covers[rid]
   assert check_row(rows[rid],B),('NON_PD_COEFFICIENT',ident,rid)
   remain&=~covers[rid];apps+=1
  discharged+=before-remain.bit_count();count+=1
  if remain:
   a,b=split(points);rec(s,j,key+'0',a,remain);rec(s,j,key+'1',b,remain)
  else:leaves+=1
 for s,j,ps in initial:rec(s,j,'',ps,FULL)
 assert visited==set(nodes)
 volume=sum(abs(det(ps[1:]))/6 for s,j,ps in initial)
 if charts==(9,)and gamma==F(3,4):assert volume==F(1,16)
 report={'identity':obj['identity'],'gamma':gamma,'charts':charts,'initial_tetrahedra':len(initial),'parameter_volume':volume,'D_volume':F(337,315),'parameter_volume_fraction':volume/F(337,315),'rows':len(rows),'nodes':count,'leaf_cells':leaves,'row_applications':apps,'PD_coefficient_matrices':816*apps,'positive_leading_principal_minors':2448*apps,'true_rooted_trees':len(T),'tree_cell_discharges':discharged,'independent_own_mass_and_reciprocal_metric_audits':audits,'certificate_bytes':len(data),'certificate_sha256':hashlib.sha256(data).hexdigest()}
 write('verification_report.json',report)
 print('ACTUAL_REFILLED_THREE_PARAMETER_CONE_ALL_SPD_USTRICT_GE_2_PASS')
 print('ALL_ROOTS_ZERO_ARROW_WALLS_COMMON_RECIPROCAL_METRIC_AND_DOMAIN_COVER_PASS')
 print('COUNTS',len(rows),count,leaves,apps,816*apps,2448*apps,discharged,flush=True)


def flag(p):
 p=list(map(F,p));assert len(p)==3
 ls=[1+dot(p,v)for v in X];assert min(ls)>0
 Y=[sc(1/l,v)for l,v in zip(ls,X)];V,g=integrate(Y);Z=[sub(v,g)for v in Y];n=0
 while True:
  a=[1,n,n*n]
  if all(dot(a,z)for z in Z)and all(dot(a,sub(Z[j],Z[i]))for i,j in combinations(range(10),2)):break
  n+=1
 b=[-n,1,0];c=cross(a,b);T=F(1)
 for i,j in AR:
  e=sub(Z[j],Z[i]);u=dot(a,Z[i])*dot(a,e);v=dot(b,Z[i])*dot(b,e);w=dot(c,Z[i])*dot(c,e)
  assert u;T=max(T,(abs(v)+abs(w))/abs(u))
 K=isqrt(-(-T.numerator//T.denominator))+1;assert K*K>T
 A=[sc(K,a),b,c];M=mm(tr(A),A);N=inverse(M);assert mm(M,N)==eye()and det(A)>0
 U=[i for i,z in enumerate(Z)if all(dot(z,mv(M,sub(Z[j],z)))<0 for j in ADJ[i])]
 assert len(U)==2 and set(U)=={min(range(10),key=lambda i:dot(a,Z[i])),max(range(10),key=lambda i:dot(a,Z[i]))}
 physical=[mv(A,z)for z in Z];VP,GP=integrate(physical);assert GP==[0,0,0]and VP==det(A)*V
 return {'p':p,'vertices':Y,'COM':g,'volume':V,'n':n,'K':K,'domination_bound':T,'M':M,'N':N,'U':U,'physical_A':A,'physical_vertices':physical,'physical_volume':VP,'physical_COM':GP}


def simple_frame(s,a):
 a=list(map(F,a));assert len(a)==3 and min(a)>=0 and len(ADJ[s])==3
 neighbors=list(ADJ[s]);W=tr([sub(X[j],X[s])for j in neighbors])
 if det(W)<0:neighbors[1],neighbors[2]=neighbors[2],neighbors[1];W=tr([sub(X[j],X[s])for j in neighbors])
 Wi=inverse(W);R=[mv(Wi,sub(x,X[s]))for x in X];b=mv(Wi,sc(-1,X[s]));assert min(x for r in R for x in r)>=0 and min(b)>0
 lam=1/(1+dot(a,b));p=sc(lam,mv(tr(Wi),a));D=[[F(i==j)*(1+a[i])for j in range(3)]for i in range(3)]
 As=[[F(i==j)+X[s][i]*p[j]for j in range(3)]for i in range(3)];A=[[lam*x for x in r]for r in mm(mm(D,Wi),As)];t=sc(-lam,mv(D,mv(Wi,X[s])))
 Phi=[sc(1/(1+dot(a,r)),mv(D,r))for r in R];V,G=integrate(Phi,s);Z=[sub(v,G)for v in Phi]
 assert Phi[s]==[0,0,0]and [Phi[i]for i in neighbors]==eye()
 assert all(0<=Phi[i][k]<=max(F(1),R[i][k])for i in range(10)for k in range(3))
 ls=[1+dot(p,x)for x in X];assert min(ls)==ls[s]==lam
 Y=[sc(1/l,x)for l,x in zip(ls,X)];Vr,gr=integrate(Y);assert Phi==[add(mv(A,y),t)for y in Y]and V==det(A)*Vr and G==add(mv(A,gr),t)
 Ai=inverse(A);M=mm(tr(A),A);N=mm(Ai,tr(Ai));assert mm(M,N)==eye()
 ns=[add(n,sc(h,p))for n,h in zip(AA,HH)];qr=[sc(1/(h-dot(n,gr)),n)for n,h in zip(ns,HH)];Q=[mv(tr(Ai),q)for q in qr]
 def roots(P):return [i for i,x in enumerate(P)if all(dot(x,sub(y,x))<0 for j,y in enumerate(P)if j!=i)]
 S=roots(Q);U=roots(Z);H=[];zeros=[];packets={};ledger=[];rawZ=[sub(y,gr)for y in Y]
 for k,(i,j)in enumerate(ED):
  f,g=[f for f,cy in enumerate(CY)if i in cy and j in cy]
  x=dot(Z[i],sub(Z[j],Z[i]));y=dot(Z[j],sub(Z[i],Z[j]));z=dot(Q[f],sub(Q[g],Q[f]));w=dot(Q[g],sub(Q[f],Q[g]));vals=[x,y,z,w]
  assert vals==[dot(rawZ[i],mv(M,sub(rawZ[j],rawZ[i]))),dot(rawZ[j],mv(M,sub(rawZ[i],rawZ[j]))),dot(qr[f],mv(N,sub(qr[g],qr[f]))),dot(qr[g],mv(N,sub(qr[f],qr[g])))]
  length=-x-y;delta=dot(Q[f],Q[f])*dot(Q[g],Q[g])-dot(Q[f],Q[g])**2;assert length>0 and delta>0
  u=-x/length;co=[-w/delta,-z/delta];foot=add(Z[i],sc(u,sub(Z[j],Z[i])));assert foot==add(sc(co[0],Q[f]),sc(co[1],Q[g]))
  if max(vals)<0:H.append(k)
  if 0 in vals:zeros.append(k)
  if max(vals)<=0 and 0 in vals:
   packet=packets.setdefault(tuple(foot),{'point':foot,'edges':[]});packet['edges'].append(k)
  ledger.append({'edge':[i,j],'facets':[f,g],'primitives':vals,'foot':foot,'components':[u,1-u]+co})
 if not packets:assert len(S)+len(U)-len(H)==2
 if s==4 and a==[1,2,3]:assert (p,V,S,U,H,zeros)==([F(11,21),F(-2,21),F(-4,21)],F(128798,487475),[0,1,2,3,4],[1,3,4,9],[0,3,4,5,8,11,16],[])
 return {'simple_vertex':s,'a':a,'neighbors':neighbors,'edge_coordinates':R,'b':b,'lambda':lam,'p':p,'frame_vertices':Phi,'frame_volume':V,'frame_COM':G,'affine_A':A,'affine_translation':t,'raw_M':M,'raw_N':N,'physical_M':eye(),'physical_N':eye(),'S':S,'U':U,'H':H,'zero_edges':zeros,'weak':list(packets.values()),'ledger':ledger}

if __name__=='__main__':
 if sys.argv[1:2]==['build']:
  charts=tuple(range(10))if len(sys.argv)>2 and sys.argv[2]=='all'else(9,);gamma=F(sys.argv[3])if len(sys.argv)>3 else F(3,4);build(charts,gamma)
 elif sys.argv[1:2]==['verify']:verify(sys.argv[2]if len(sys.argv)>2 else'certificate.json')
 elif sys.argv[1:]==['mass']:geometry();mass_outputs()
 elif sys.argv[1:]==['control']:geometry();control()
 elif len(sys.argv)==5 and sys.argv[1]=='flag':geometry();write('flag_body.json',flag(sys.argv[2:]))
 elif len(sys.argv)==6 and sys.argv[1]=='frame':geometry();write('simple_frame.json',simple_frame(int(sys.argv[2]),sys.argv[3:]))
 else:raise SystemExit('Use build [9|all] [gamma], verify [certificate.json], mass, control, flag px py pz, or frame s a1 a2 a3')
```

## Complete runnable source unit 2: prune_cone.py

```python
"""Deterministic global-row reuse, no new numerical certificate rows.
Input: cold certificate cb5e2101e053902dca4f8a03b3dde50cb00df32858254281e3f45cfb1d5e37be.
Output exact acceptance uses bevel3_recovery.check_row (integer arithmetic).
CPython3.13.5 / NumPy2.3.5; OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=1.
Run: python prune_cone.py certificate.json pruned.json
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json,hashlib,time
from pathlib import Path
from fractions import Fraction as F
import numpy as np
import bevel3_recovery as c
assert np.__version__=='2.3.5'
b=Path(sys.argv[1]).read_bytes()
assert hashlib.sha256(b).hexdigest()=='cb5e2101e053902dca4f8a03b3dde50cb00df32858254281e3f45cfb1d5e37be'
D=json.loads(b);T=c.trees();ac=c.arrow_covers(T);FULL=(1<<len(T))-1
rows=D['rows'];covers=[]
for row in rows:
 x=FULL
 for i,w in row:x&=ac[i]
 covers.append(x)
old={(r['s'],r['j'],r['key']):r for r in D['nodes']};nodes=[];start=time.time()
def rec(s,j,key,points,remain):
 B=c.fields(s,points);BF=np.array(B,dtype=float);BF/=np.max(np.abs(BF),axis=(0,2))[None,:,None]
 corners=[k for k,m in enumerate(c.MON)if max(m)==15]
 trial=sorted(set(corners+list(range(0,816,41))))
 def passes(row):
  for ks in (corners,trial,range(816)):
   v=-sum(w*BF[i,ks] for i,w in row);a,b,c_,d,e,f=v.T
   if min(a.min(),(a*d-b*b).min(),(a*d*f+2*b*c_*e-a*e*e-d*c_*c_-f*b*b).min())<=1e-10:return False
  return True
 valid=[r for r,row in enumerate(rows)if remain&covers[r] and passes(row)]
 valid=sorted(set(valid)|set(old[s,j,key]['rows']));used=[]
 while valid:
  rid=max(valid,key=lambda r:((remain&covers[r]).bit_count(),-len(rows[r]),-r))
  if not remain&covers[rid]:break
  valid.remove(rid)
  if not c.check_row(rows[rid],B):continue
  used.append(rid);remain&=~covers[rid]
  if not remain:break
 nodes.append({'s':s,'j':j,'key':key,'rows':used})
 print('PRUNE',s,j,key or '-',len(used),remain.bit_count(),round(time.time()-start,2),flush=True)
 if remain:
  a,b=c.split(points);rec(s,j,key+'0',a,remain);rec(s,j,key+'1',b,remain)
for s,j,points in c.domains(F(D['gamma']),D['charts']):rec(s,j,'',points,FULL)
keep=sorted({r for n in nodes for r in n['rows']});mp={r:i for i,r in enumerate(keep)}
for n in nodes:n['rows']=[mp[r]for r in n['rows']]
D['rows']=[rows[r]for r in keep];D['nodes']=nodes
out=c.canonical(D);Path(sys.argv[2]).write_bytes(out)
print('GLOBAL_REUSE_EXACT_PD_PRUNING_PASS',len(keep),len(nodes),sum(len(n['rows'])for n in nodes),len(out),hashlib.sha256(out).hexdigest())
```
