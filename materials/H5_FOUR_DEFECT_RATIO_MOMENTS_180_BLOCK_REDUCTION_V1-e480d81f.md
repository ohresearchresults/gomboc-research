# material-e480d81f0600

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# H5_FOUR_DEFECT_RATIO_MOMENTS_180_BLOCK_REDUCTION_V1

Coordinator research. Exact predecessor used: minimum-0238, SHA256 d3964294432974c93c8579efb0406ab475aa488fc7524e04ed40baad8ab5d185, read completely. This is a new moving-ratio moment/degree reduction, NOT a replay of its all-root q-cube exclusion, and NOT a new all-ratio exclusion.

## General four-defect geometry and actual moments
Write Delta=conv(O=(0,0),A=(1,0),R=(0,1)). The H5 basal polygon has cyclic vertices (b,0),(c,0),(1-p,p),(q,1-q),(0,d),(0,a),(u,v), with 0<b<c<1, 0<a<d<1, p,q>0, p+q<1, u,v>0, u/b+v/a<1. Set s=1-lambda, 0<lambda<1. Bottom vertices are (s B_i,0); top vertices are (0,0,1),(lambda,0,1),(0,lambda,1), labels7,8,9.

The full triangular frustum conv(s Delta at z=0, lambda Delta at z=1) loses exactly FOUR tetrahedra: the A-corner with bottom triangle (A,(c,0),(1-p,p)) and apex8; the R-corner with bottom triangle (R,(q,1-q),(0,d)) and apex9; and two O-corner tetrahedra with bottom triangles (O,(b,0),(u,v)), (O,(u,v),(0,a)) and common apex7. Scale every bottom coordinate by s. Their interiors are disjoint: the basal cuts are disjoint and every height section consists of the corresponding scaled corner defects of the homothetic containing triangle. In detail the section of each defect at height t is the affine image (1-t)s times its basal triangle plus t lambda times its corner O,A or R. Along each side, disjointness is preserved by the nonnegative additional side interval t lambda. The retained intersection has the literal H5 facets. The O defect can be nonconvex and is deliberately split into two triangles. No arbitrary physical masses are introduced.

Define planar defect areas dA=(1-c)p/2, dR=q(1-d)/2, d0=bv/2, d1=au/2 and A_B=1/2-dA-dR-d0-d1. The basal first moments are
Bx=1/6-[dA(2+c-p)+dR q+d0(b+u)+d1 u]/3,
By=1/6-[dA p+dR(2-q+d)+d0 v+d1(v+a)]/3.

Each removed tetrahedron has volume s^2 times its planar area divided by3; its first moment is that volume times the mean of its four vertices. Subtract these exact tetrahedral moments from those of the full frustum. The result is
V=A_B s^2/3+lambda/6,
Jx=s^3 Bx/4+s^2 lambda(1-2dA)/24+lambda^2/24,
Jy=s^3 By/4+s^2 lambda(1-2dR)/24+lambda^2/24,
Jz=A_B s^2/12+lambda/12+lambda^2/24,
g=J/V.
These formulas recompute the actual uniform solid centroid; they do not transport a fixed centroid by a projectivity. They are polynomial identities before division. In particular Jz-V/4=lambda(1+lambda)/24 and 3V/4-Jz=A_B s^2/6+s lambda/24. Thus 1/4<g_z<3/4 in the genuine interior.

## Full q/cut cube with moving ratio
Keep b=a=1/4,d=3/4,u=v=1/16, c=1-3x/4,p=(1-q)y. For the complete closed four-cube (x,y,q,lambda) in[0,1]^4,
A_B=(31-8q-24x(1-q)y)/64,
A_B-7/64=[3(1-q)(1-xy)+2q]/8 >=0,
7/192 <= V <=1/6.
The lower bound follows from V-7/192=(A_B-7/64)s^2/3+lambda(3/32+7lambda/192). The upper follows from 1/6-V=(1/2-A_B)s^2/3+s lambda/6. Neither ratio endpoint is a zero-volume singularity. Lambda0 is the pyramid over the basal polygon, with at most eight true vertices; lambda1 is a tetrahedron with repeated bottom labels. Only the open four-cube is asserted to have the genuine displayed10/17/9 lattice.

The exact source checks34 incident flags and all56 strictly positive nonincident support polynomials over this entire open cube, not sampled hulls. Its eight apex0 fan volumes, in order0128,0982,0923,0934,0457,0479,0675,0789, are
s^2(1-q)y(1-x)/8, s lambda/8, s^2(1-q)(1-y)/8,
s^2(1+8q)/96, s^2/48, s lambda/24, s^2/192, lambda^2/6.
They are nonnegative on the closed cube and reproduce V,J exactly. At lambda1/2 these moving formulas equal every literal parent q-cube volume and first-moment polynomial, not merely its values at sample points.

## 180 Bernstein matrices, not an executed all-root cover
For one constant nonnegative directed-edge stress w, W=sum w, let outgoing/incoming totals be s_i,t_i and G=-sum w_ij sym[(Vz_i-J)(z_j-z_i)^T]. Put e=(-(1-b)s,0,0), f=s(1-q)(-1,1,0), k=s^2(1-b)(1-q)/6. Then
B1=k(3s_1+t_1)ee^T/4 >=0,
B2=k(3s_2+t_2)ff^T/4 >=0,
G=R+yx^2(1-x)B1+xy^2(1-y)B2.
R has multidegree at most(2,2,3,4) in(x,y,q,lambda). The generally indefinite mixed x^2 y^2 coefficient remains k[w12+w21-(t1-s1+t2-s2)/4]sym(ef^T), and must not be discarded. The source checks these polynomial identities on all34 directed true edges, hence on every constant nonnegative stress.

For a subbox x=a+hX,y=c+jY, subtract h^3 y X^2(1-X)B1+j^3 x Y^2(1-Y)B2 instead. Cancellation of the cubic X,Y coefficients again leaves degrees(2,2,3,4). These removed terms are PSD on every closed subbox. Therefore 3*3*4*5=180 tensor Bernstein matrices suffice for a common stress on a full four-dimensional box. Exact positive definiteness of all matrices after subtracting eta W I implies G>eta W I, hence sum wD/W < -6 eta tr(M) for every nonzero PSD M, since V<=1/6. This implication supplies neither such stresses nor complete tree coverage. Degree4 interpolation in lambda requires five exact evaluations of known polynomials, not sampled feasibility. Shrinking x,y boxes shrinks the discarded corrections cubically, so they do not create an artificial fixed residual obstruction in a refined positive-gap cover.

## Complete source, reconstruction, observed execution
The complete10103-byte standard-library source is material [internal-source-reference], h5_ratio_exact_source.txt, SHA256 035a7fef8c842e81fe97d06409370bd02686a0fba4874a38a59fd8d0863a2eda. Read/attach that complete exact material for a computation. Save its bytes as h5_ratio_exact.py.
Reconstruction and verification: python -B -S h5_ratio_exact.py out
Requires CPython>=3.11 standard library, assertions enabled; observed CPython3.13.5. No numerical solver, packages, inherited code, external data, random seed or hidden parameter.
Expected marker: H5_FOUR_DEFECT_RATIO_MOMENTS_180_BLOCK_PASS 34 180.
Generated out/h5_ratio_reduction.json:196956 bytes, SHA256 e3bbf10c36418e7462ddec6ba43b6c8a317cabbf6fee1ca6fbc12dff95a8ff88. It contains every exact moving-moment and directed-edge residual polynomial. Normal execution observed PASS. No proof-assistant claim.

This source is sufficient to reconstruct the NEW symbolic reduction only. A computational successor using the parent's646 stresses must additionally receive literal parent minimum-0238. Source recovery does not itself prove any new all-root exclusion. Global34<=C_min<=622 unchanged; no attaining construction, whole-type exclusion, covariance cap or S>=2 conclusion.
