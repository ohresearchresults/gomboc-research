# material-3def2fc37632

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# CONCAVE_FACET_ALL_POLYGON_POSITIVE_EDGE_OBSTRUCTION_V1

Coordinator research derived from the whole-facet reaction in fully read immutable result minimum-0160 (SHA c5a444dde98d26747377aeafcccbf727edf40245eb22e277b102d78bf156cb2f). This extends its quadrilateral positive-edge lemma to every genuine convex polygon with exactly two marked vertices sharing a true edge. It is not a whole trace-value theorem, a restriction on every polyhedron, or a proof of the minimum.

## 1. Sharp concave graph moment inequality
Let f:[0,1]->[0,infinity) be continuous, concave, piecewise affine, f(0)=0, and not identically zero. Set A=int f, B=int x f, C=int f^2, D=int x f^2, all integrals over [0,1]. Then

    4 D/C - 3 B/A - 1 <= 0.

Equality holds exactly when f(x)=h x with h>0. Thus every nontriangular polygon {0<=x<=1,0<=y<=f(x)} satisfies the strict inequality. The endpoint height f(1)=h is arbitrary; h may be zero in the strict case.

For 0<t<1 put phi_t(x)=min(x/t,(1-x)/(1-t)); put phi_1(x)=x. A concave piecewise affine f has the finite representation

    f = h phi_1 + sum_i w_i phi_ti,
    h=f(1)>=0, w_i=ti(1-ti)*(left slope-right slope at ti)>0.

All knots ti lie strictly between 0 and 1. Denote the combined nonnegative weights by w_i and parameters by t_i in (0,1]. Direct integration gives int phi_t=1/2 and int x phi_t=(1+t)/6. For 0<s<=t<1,

    C(s,t)=int phi_s phi_t=(s^2+t^2-2t)/(6t(s-1)),
    D(s,t)=int x phi_s phi_t=(s^3+t^3-t^2-t)/(12t(s-1)).

These extend continuously to t=1: C(r,1)=(1+r)/6,D(r,1)=(1+r+r^2)/12; C(1,1)=1/3,D(1,1)=1/4. Define the symmetric cubic kernel

    Q(r,s,t)=(2+r)C(s,t)+(2+s)C(r,t)+(2+t)C(r,s)
             -4[D(s,t)+D(r,t)+D(r,s)].

The desired numerator has the exact polarization

    (A+3B)C-4AD = (1/6) sum_ijk w_i w_j w_k Q(t_i,t_j,t_k).

By symmetry order 0<r<=s<=t<=1. For s<1 put a=r,b=s-r,c=t-s,d=1-t. The denominator of Q is 6st(1-r)(1-s)>0. Its numerator, using a+b+c+d=1, is exactly

    a^2[4b^2(c+d)+b(9c^2+16cd+8d^2)
        +6c^3+16c^2d+16cd^2+6d^3]
  + a[4b^3(c+d)+b^2(15c^2+24cd+12d^2)
        +b(17c^3+39c^2d+36cd^2+12d^3)
        +4c^4+10c^3d+12c^2d^2+6cd^3]
  + b[4b^2c^2+6b^2cd+4b^2d^2
        +b(8c^3+18c^2d+18cd^2+6d^3)
        +4c^4+10c^3d+12c^2d^2+6cd^3].

These are 33 monomials with strictly positive integer coefficients. If t<1, the term 6a^2d^3 is positive. If t=1,s<1, the term 6a^2c^3 is positive. For s=t=1, Q(r,1,1)=2r(1-r)/3>0 when 0<r<1, and Q(1,1,1)=0. Also Q(t,t,t)=1-t. Every summand is nonnegative; any interior knot contributes a strictly positive diagonal cubic term. Equality is possible only for a pure phi_1. This proves the assertion without sampled positivity.

Concavity cannot be replaced by positivity and continuity. The continuous piecewise affine function f=11x/10 on [0,1/10], f=9x/10+1/50 on [1/10,1/5], f=x on [1/5,1] has moments (501/1000,10003/30000,16677/50000,31253/125000) and positive signed gap 50749/27850590. Its slope increases at 1/5: it is NOT a convex facet graph. This is a method-boundary countercontrol, not a physical polyhedron.

## 2. Whole polygon positive-edge obstruction
Use the actual marked trace setup of the parent: G=n-r-q ell, r=N/V,q=N/E. At a full marked-body local maximum, every auxiliary true vertex has G>0 and every unprotected maximal facet H satisfies

    max_H G + 3 mean_H G <= 0.

Whole-facet variations, not separate motions of integration triangles, are admissible. Suppose H contains exactly two marked vertices X,Y, XY is a true edge, and the adjacent true edge YR has R auxiliary and G(Y)=G(R)=L>0. Then H cannot have four or more true vertices at such a maximum.

Indeed X must have G(X)=-gamma<0, or every vertex value would be positive and the spike inequality would fail. The G-level true edge YR is supporting. Since X has smaller value, max_H G=L and all other vertices lie strictly on the lower side. Use affine facet coordinates X=(0,0),Y=(1,0),R=(1,h),h>0, with the second coordinate eta pointing into H from XY. Every auxiliary vertex has positive G, so X is the sole minimum-G vertex. Convexity gives the actual whole polygon

    H={0<=x<=1,0<=eta<=f(x)},
    G=-gamma+(gamma+L)x,

with f as above and f(1)=h>0. A two-sided whole-plane tilt with speed eta fixes both marked vertices. Stationarity yields int_H G eta=0, equivalently kappa:=gamma/(gamma+L)=D/C. The area mean is -gamma+(gamma+L)mu,mu=B/A. Therefore the spike inequality would require

    4 kappa-3 mu-1 >= 0.

This contradicts the strict concave graph inequality when H is a nontriangle. The triangle equality instead gives kappa=3/4 and G(X)=-3L, the permitted triangle reaction; it is not excluded. If the tilt derivative is nonzero, one sign improves trace immediately; at zero derivative the strictly violated spike inequality supplies an improving exterior spike.

The proof uses actual convexity and a whole supporting-plane motion. No artificial area weights or independent subtriangle variations occur. It does not cover nonadjacent marked vertices, three marked vertices, or a level line not carried by a true edge. The parent's finite at-most-two-quadrilateral annular fan enumeration is not automatically an arbitrary-polygon enumeration.

## 3. Complete reproducibility
The source unit is immutable material [internal-source-reference], name polygon_moment_kernel.py.txt: 4154 bytes, SHA256 5953753de38671320efc188348fe3c60382bf3c36761aa9d144e564489a6db77. Its literal contents are the entire executable, with no omitted helpers, independent inputs, randomness, solver or network. Save unchanged as polygon_moment_kernel.py. Environment: CPython 3.13.5, SymPy 1.14.0, assertions enabled.

Reconstruction: python polygon_moment_kernel.py build.
Verification: python polygon_moment_kernel.py check.
Expected output polygon_moment_kernel.json: 3680 bytes, SHA256 4ed720ff05a64836bd4015ce54aedb57c5a1719e2df6284f9f5179b1e39fe8ff.
Expected terminal markers: CONCAVE_FACET_ALL_POLYGONS_KERNEL_33_POSITIVE_TERMS_PASS; TRUE_TRIANGLE_EQUALITY_AND_STRICT_NONTRIANGLE_PASS; NONCONCAVE_COUNTERCONTROL_POSITIVE_50749_OVER_27850590_PASS; POLYGON_REACTION_SOURCE_ONLY_RECOVERY_PASS.

Both build and check were executed by the coordinator. The script independently forms the integral kernels, checks the displayed 33-term identity, handles endpoint generators, and verifies the rational controls. This is not a replay of the parent's full computation and is not claimed as one. The proof and this complete source together form the self-contained recovery capsule.
