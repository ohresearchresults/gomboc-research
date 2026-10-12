# material-c62b1baaaae1

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# H5_RANKONE_TRIANGLE_QUADRATIC_90_270_REDUCTION_V1

## Evidence, scope and exact parent
This is a new coordinator analytic and executed algebraic reduction, not an all-root free-d exclusion. It reduces the number of sufficient Bernstein matrices on each fixed-shape-parameter box/physical-cut triangle from150 to90 at fixed d and from450 to270 with independent d. The lowered matrices can be more conservative; fewer matrices per cell does NOT imply fewer cells or a faster complete search. No C bound or attaining construction changes.

The literal immutable parent is minimum-0240, SHA256 e9e9cb5a41c6f3efb409de269963537ed1616b34e6847d48b16feac43b6c92b7, read completely through EOF. It proves the entire H5 cut/q/compact-ratio four-cube at d=3/4, and supplies executed540/450-block independent-d reductions. Its accepted r slice is1/3 when d=1-3r/4. The following coordinates retain exactly that object and its labels. The new source is self-contained for its own computation; reconstructing the parent's5982-stress atlas is not required for these identities.

## Actual geometry and moments
Let x,r,lambda in[0,1], p,q>=0, p+q<=1, s=1-lambda. Basal vertices are
B0=(1/4,0), B1=(1-3x/4,0), B2=(1-p,p), B3=(q,1-q), B4=(0,1-3r/4), B5=(0,1/4), B6=(1/16,1/16).
Put zi=(s Bi,0), i=0..6, and z7=(0,0,1), z8=(lambda,0,1), z9=(0,lambda,1). The interior is the parent's genuine10/17/9 family. Closed boundaries are its actual positive-volume collapsed-label limits, not automatically genuine E17 bodies.
True edges:01,06,07,12,18,23,28,34,39,45,49,56,57,67,78,79,89.
True oriented facets: (6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),(9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9).

Actual basal area and planar moments are
A=(31-24xp-24qr)/64,
Bx=p^2 x/8+3px^2/32-3px/8-q^2 r/8+509/3072,
By=-p^2 x/8+q^2 r/8+3qr^2/32-3qr/8+509/3072.
Actual uniform volume and first moments are
V=A s^2/3+lambda/6,
Jx=s^3 Bx/4+s^2 lambda(1-3xp/4)/24+lambda^2/24,
Jy=s^3 By/4+s^2 lambda(1-3qr/4)/24+lambda^2/24,
Jz=A s^2/12+lambda/12+lambda^2/24.
The physical centroid is g=J/V. No vertex-average, transported centroid, independent cell masses or uniform-polar-centroid premise is used.

For fixed nonnegative weights w_ij on true directed edges define
G=-sum w_ij sym[(V zi-J)(zj-zi)^T], W=sum w_ij.
Then sum w_ij (zi-g)^T M(zj-zi)=-tr(MG)/V. Thus G positive definite rules out the selected simultaneous nonnegative arrows for every nonzero PSD M. Covering ALL rooted trees is a separate obligation.

## General collinear two-vertex lemma
In dimension n, suppose only vertices a,b move as va=a0+p e and vb=a0+(1-q)e, and a fixed genuine vertex triangulation remains valid on the shape chamber. All other vertices are fixed. Every simplex determinant is affine in p,q because the two moving directions are parallel. A simplex containing both endpoints has volume proportional to1-p-q. Hence actual V=V0+alpha p+beta q, and the homogeneous quadratic part of the unnormalised first moment is
J[2]=(alpha p^2-beta q^2)e/(n+1).
For simplices containing both endpoints the mixed pq term cancels in (1-p-q)(p-q); for one-endpoint simplices the displayed pure terms follow from their simplex centroid. Summing gives the formula. Consequently the total-degree-three part in(p,q) of every edge-stress matrix is a scalar times ee^T. This is actual-volume geometry, not a numerical rank approximation.

For example an arrow from a to a fixed vertex has cubic part
p[n alpha p^2+(n+1)beta pq+beta q^2]ee^T/(n+1),
and an arrow from a fixed vertex to a has
p(alpha p^2-beta q^2)ee^T/(n+1).
The corresponding b formulas follow by exchanging endpoints. Thus mixed coefficients need not have the same sign. One must not simply declare the entire cubic part negative PSD.

## Exact H5 cubic and the triangle fold
Write f=(-1,1,0), so the moving physical direction is s f. Define external weighted incidences
Ia=w12+w82, Oa=w21+w28,
Ib=w43+w93, Ob=w34+w39,
a=w23, b=w32.
All are nonnegative. Put
A0=x(Ia+3Oa+3a+b), D0=r(Ib+3Ob+a+3b),
E=x(Ob+3a+5b-Ib)+4r(Oa+a),
F=r(Oa+5a+3b-Ia)+4x(Ob+b).
Then the entire homogeneous cubic is EXACTLY
G[3]=(s^4/32)(-A0 p^3-E p^2q-F pq^2-D0 q^3) ff^T.
Only ten directed arrows have nonzero cubic parts; the source checks all34. The coefficients E,F can be negative.

Choose constant-in-shape envelopes
Lx=max(Ob+3a+5b-Ib,4(Ob+b)),
Lr=max(4(Oa+a),Oa+5a+3b-Ia),
L=x Lx+r Lr.
Because x,r>=0, L>=0, L-E>=0 and L-F>=0, with the last two inequalities coefficientwise in x,r. Replace G[3] by the quadratic
Q2=-(s^4/32)(A0 p^2+D0 q^2+Lpq)ff^T.
Their difference is
Ctri=(s^4/32){A0 p^2(1-p)+D0 q^2(1-q)+pq[L(1-p-q)+(L-E)p+(L-F)q]}ff^T >=0
on the WHOLE physical triangle. The positive/negative mixed cubic terms are retained in an exact identity; none is discarded with an unjustified sign.

The source constructs this fold separately for every unit arrow. Their nonnegative weighted sum gives a linear stress basis, usable without redesigning a linear weight locator. Alternatively the aggregate envelopes above are tighter: max is subadditive, so the aggregate L is no larger than the weighted sum of unit-arrow envelopes. An LP/SDP locator may instead introduce Lx,Lr as auxiliary variables with their displayed linear lower bounds. All these versions have the same proof.

## Combined degree and matrix count
Let e1=(-3s/4,0,0), e4=(0,-3s/4,0). The parent's exact single-corner corrections are
Cx=x^2(1-x) B1, B1=s^2 p(3 out1+in1)e1 e1^T/32,
Cr=r^2(1-r) B4, B4=s^2 q(3 out4+in4)e4 e4^T/32.
They are PSD. They are only linear in(p,q), so do not alter the cubic just computed. Therefore
R=G-Cx-Cr-Ctri
has degree at most2 in x,2 in r, total degree2 in(p,q), and4 inlambda. The new source checks this for all34 independent directed-edge basis matrices, hence for every nonnegative constant stress.
A quadratic polynomial on a triangle has six Bernstein coefficients. Together with the interval bases, 3*6*5=90 matrices suffice at fixed r; 3*3*6*5=270 suffice with r free. Positive definiteness of these matrices implies R>0 and hence G>0 throughout the closed cell. Replacing each matrix by H-epsilon W I gives the usual uniform trace gap. No actual90/270-block ALL-ROOT atlas is claimed here.
For p^i q^j the degree-two triangle coefficient at(K,L), K+L<=2, is binom(K,i)binom(L,j)/[binom(2,i)binom(2-i,j)], with zero when an upper index is too small. All six complete monomial identities are checked.

## Local refinement and limits of the reduction
Simply subdividing the global R does not remove the conservatism of its global correction. Recompute the fold in the local triangle coordinates to recover convergence.
For any affine subtriangle parameterization(p,q)=a+Uu+Vv, u,v>=0,u+v<=1, the homogeneous cubic is still rank one: h3=(c30 u^3+c21 u^2v+c12 uv^2+c03 v^3)ff^T. For fixed other parameters choose A>=max(0,-c30), D>=max(0,-c03), L>=max(0,-c21,-c12). Then
h3-(-Au^2-Dv^2-Luv)ff^T
=[A u^2(1-u)+(A+c30)u^3+Dv^2(1-v)+(D+c03)v^3+Luv(1-u-v)+(L+c21)u^2v+(L+c12)uv^2]ff^T>=0.
For parameter boxes the c coefficients are s^4 times affine functions of x,r. Nonnegative coefficientwise envelopes in the local bilinear Bernstein basis give the same degree bounds. Their size is O(diameter(triangle)^3), uniformly on compact remaining-parameter boxes. Local x/r cubic folds likewise have cubic-width loss. Thus if a fixed stress has a strict gap on a compact physical cell, sufficiently fine local refolding and Bernstein subdivision eventually certify it. If every complete tree has a pointwise strict separating stress on a compact family, continuity, finiteness of trees and compactness yield a finite atlas with these local reductions. This is conditional existence, not an executed atlas or a bound on its size.

## Exact local control
With x=1/2,r=1/3,lambda=1/2 and stress w70=w82=w94=1, the actual physical triangle
p=3/8+u/4, q=1/4+v/4, u,v>=0,u+v<=1
has all six locally folded Bernstein matrices positive definite, verified by18 exact positive leading minors. It lies inside p,q>0,p+q<1. This checks a genuinely nonempty physical region, not just a formal polynomial. It rules out those three simultaneous weak arrows there, not every rooted tree; that region was already within the parent's all-root family. No new census or target-class body is inferred.

## Additional exact reflected starting sector
Reflection (X,Y,Z)->(Y,X,Z) with label permutation(0,1,2,3,4,5,6,7,8,9)->(5,4,3,2,1,0,6,7,9,8) transforms(x,r,p,q,lambda) to(r,x,q,p,lambda) and preserves the literal true lattice. It transports the actual uniform centroid and SPD metrics by isometry. The parent's entire r=1/3 all-root theorem therefore also excludes the entire x=1/3 section with arbitrary r,p,q,lambda. These are two continuous sections of the released five-dimensional family, not its entirety.
The parent's matched-vertex actual-refill collar2^-41 also excludes every genuine member with min(|x-1/3|,|r-1/3|)<=2^-41: only one matched basal vertex moves by at most(3/4)*2^-41. Its half-gap3/268435456 is retained. This is a useful cross-shaped starting set, not a macroscopic free-d completion. The two sections inherit the stronger original gap3/134217728. This reflection corollary is analytic and does not require a fresh atlas replay.

## Complete recovery and observed execution
Complete executable material [internal-source-reference], name h5_rankone_triangle_fold.py.txt, contains all7082 source bytes, SHA256 ebe7d7eecfda26b850098d05078b079b4d68db6f4b82c4611b6c649ae978ed03. Save its exact text as h5_rankone_triangle_fold.py and run:
python h5_rankone_triangle_fold.py report.json
Observed CPython3.13.5/SymPy1.14.0. No solver, random seed, external input, omitted helper or generated predecessor is needed. Normal execution and a new directory initially containing only the exact source both passed and produced identical report.json,2687B,SHA2564211be9b6f76d6553e4c21d35474bd4f098c7e3ac1eef77d6ee867f5d800ca55.
Expected markers:
H5_RANKONE_TRIANGLE_QUADRATIC_90_270_REDUCTION_PASS 34 90 270
LOCAL_THREE_ARROW_SIX_BERNSTEIN_PD_PASS 1/4 18
REPORT_BYTES_SHA256 2687 4211be9b6f76d6553e4c21d35474bd4f098c7e3ac1eef77d6ee867f5d800ca55
The source checks actual polygon/fan volume and first moments, all34 full stress/cubic identities and degree bounds, six triangle basis identities and the18 local positive minors. It does not re-enumerate48790 trees or assert their free-d exclusion. This proof and the complete executable together are the recovery capsule. Accepted34<=C_min<=622 and the independent attainment requirement remain unchanged.
