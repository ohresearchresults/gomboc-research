# material-c23e9d7f45f6

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# GENERAL_ROOT_ANCHORED_CAP_ERASURE_AND_TWO_ANCHOR_HEIGHT_ONE_V1

## Scientific status and dependencies
This is a coordinator-authored analytic theorem about actual uniformly filled convex bodies, obtained by extending the endpoint-preserving overshoot mechanism in the completely read immutable result minimum-0155, SHA 0c62c07b9b3fc29f391b55135b5056c9a7f3992257a198d2c4910687f8cd8ecc. That result uses the zero mark C as ray center. Here an actual point of the root supplies the center and allows arbitrary nonnegative c,d, including the all-positive stratum. The proof below is self-contained, apart from an explicitly optional previously accepted trace upper bound in Section 6. It does not rely on a finite certificate, a numerical search, or an independently chosen centroid. No code materially produced the theorem.

The high-trace G-sign consequence is new and follows from the literal tetrahedral integral, not the inherited joint-mass theorem. The result minimum-0158, SHA dc5a857ac21b3a00a6c6532258d95c8dd2f7740134c37e86d65e3261f57764a5, separately identifies the two-anchor representation and proper33 at a genuine all-positive joint maximum with G(C),G(D)>=0. The cap theorem itself assumes neither that representation nor stationarity.

## 1. Definitions and physical class
Let A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0), and T0=conv(A,B,C,D), with Vol(T0)=1/6. Let P be a compact full-dimensional convex body in x,y>=0 containing T0. Let

    ell=a+(d-a)x+(c-a)y-(a-b)z,
    n=(a+b+c)x+(a+b+d)y,

where a>=b>0 and c,d>=0. Assume ell>=0 on P and that F0=P intersect {ell=0} has positive relative area. All integrals are ordinary three-dimensional Lebesgue integrals over the actual indicated body. Put

    V=Vol(P), E=int_P ell, N=int_P n, T(P)=N/(6VE).

E,N,V are strictly positive. A proper33 body additionally has P intersect {x=0}=ABC and P intersect {y=0}=ABD, with AB a true edge. The larger marked supporting-patch class does not require those equalities. Both are eligible for the results below. A positive-area root is more than is needed for the cap inequality; it suffices to have a root point o with n(o)>0. Positive root area guarantees such a point because n=0 in x,y>=0 only on the z axis.

For H>=max(a,b,c,d), let Q=P intersect {ell<=H}. Write

    v=Vol(Q), e=int_Q ell, nQ=int_Q n,
    R=P intersect {ell>H}, W=Vol(R), F=int_R ell.

Assume W>0; then F>HW. Q contains all of T0 and has positive volume. The root and all canonical marks survive. If P was proper33, Q has exactly the same two maximal coordinate triangles and their common edge: intersection cannot add points to a coordinate section and it removes none of its triangle, since ell is affine and each endpoint value is <=H. Other facets and the equilibrium census need not survive.

## 2. Exact containing-tetrahedron point budget
For p=(x,y,z) with x,y>=0, set s=x+y. The visible-face pyramid decomposition of conv(T0,p), whose barycentric coordinates relative to T0 are (1-s-z,z,y,x), gives exactly

    6 Vol(conv(T0,p))=1+(-z)_+ +(s+z-1)_+.

Only the two faces opposite A and B can be visible. Their two exterior pyramids have disjoint interiors, including when both are visible. For p in Q this hull is contained in Q. Therefore, with t=6v>=1,

    s<=t,       z>=1-t,       s+z<=t.                 (2.1)

These inequalities use the volume of this same Q. They are not bounds from a freely specified moment completion.

On the actual section ell=H, the identity

    n=(b+c+d)s+a-H-(a-b)z

and (2.1) imply

    n <= B_H(t):=(a+c+d)t+b-H.                        (2.2)

The coefficient b+c+d is positive and a-b is nonnegative, so the inequality directions are valid even when a=b. If a positive cap exists, this section is nonempty and B_H(t)>0.

## 3. Root-anchored perspective comparison
Choose an actual o in F0 with q0=n(o)>0. For every p in R, write w=ell(p)>H and

    r=o+(H/w)(p-o).

Convexity puts r in Q intersect {ell=H}. Affineness gives

    n(p)=(w/H)n(r)-(w/H-1)q0
         <= (B_H(t)/H)w-q0(w/H-1).

Integrating over the SAME removed cap,

    int_R n <= (B_H(t)/H)F-q0(F/H-W)
             < (B_H(t)/H)F.                         (3.1)

In particular no assumption about axis intercepts, root visibility, section chords, shell aspect, or normal count was used. The term q0(F/H-W) is the explicit positive strictness margin. The potentially negative coefficient of w before integration was never discarded or assumed nonnegative.

Define

    gamma_H(t)=B_H(t)/(Ht)
              =(a+c+d)/H+(b-H)/(Ht).

Actual moment addition then gives

    T(P) < [v/(v+W)] [ T(Q)e+gamma_H(t)F ]/(e+F).     (3.2)

This is a coupled comparison of V,E,N for P and Q. Neither centroid is held fixed; each is the center of its own uniformly filled body.

## 4. Universal high-level cap erasure
For any tau>0 put

    H_tau=max{a,b,c,d,(a+c+d)/tau}.

For H>=H_tau, gamma_H(t)<=tau because H>=b and (a+c+d)/H<=tau. Thus (3.2) yields

    T(P)<max{T(Q),tau}.                              (4.1)

The conclusion remains strict if gamma_H=tau. Strictness follows from q0(F/H-W)>0, and also from v/(v+W)<1. In particular,

    T(P)>=tau and W>0  ==>  T(Q)>T(P).                (4.2)

The upper threshold may therefore be clipped without loss in any search for a trace >=tau, while preserving genuine proper33 when it was present.

If P is a Hausdorff local maximum in the entire eligible marked-body class, T(P)>=tau implies

    max_P ell <= H_tau.                              (4.3)

Indeed, if M=max_P ell>H_tau, intersect at levels H tending upward to M with H>=H_tau. These convex bodies converge to P in Hausdorff distance, retain the required marks and root, have positive removed volume, and strictly increase T by (4.2). This contradicts full-class local maximality. The assertion is not licensed for a fixed-f-vector maximum or a maximum artificially constrained to a prescribed G-sign sector.

Without the convention a>=b, exchange A and B using the affine map (x,y,z)->(x,y,1-x-y-z), which fixes C,D and has absolute determinant one. It exchanges a,b and preserves n, V,E,N. The invariant formula is therefore

    H_tau=max{a,b,c,d,(max(a,b)+c+d)/tau}.

For c=0, a>=b and tau=2, H_2=max(a,d); this recovers the general endpoint-preserving threshold in the one-zero parent, without assuming d<=a.

## 5. New two-anchor endpoint sum and height-one consequence
For THIS same P let

    r=N/V, q=N/E, tP=6V, G=n-r-q ell.

Assume G(C)>=0 and G(D)>=0. Set s0=a+b, S=c+d, m=max(c,d). Then

    2r+qS <= 2s0+S.                                 (5.1)

Since T0 is contained in P and ell>=0,

    E >= int_T0 ell=(s0+S)/24.

The identity T(P)=r/(6E), which follows directly from N=Vr, gives

    r >= T(P)(s0+S)/4,       q=T(P)tP.               (5.2)

For 2<=T=T(P)<4, combining (5.1)-(5.2) gives the stronger coupled endpoint bound

    S <= (4-T)s0 / [2T tP+T-2].                      (5.3)

In particular tP>=1 and b<=a imply S<=a; if a>b, then S<a. No projective stationarity, covariance completion, joint first-moment upper bound, proper33 condition, or two-anchor representation is needed for (5.3). For all-positive c,d, T>=4 is already impossible by (5.1)-(5.2), so the displayed range is not an omitted high-trace possibility.

The individual mark with endpoint m obeys r+qm<=s0+S-m. From (5.2),

    m <= (4-T)(s0+S)/[4(TtP+1)].

Since S<=2m and the coefficient is <1/2 for T>=2, it follows that

    m <= (4-T)s0 / [2(2TtP+T-2)].                    (5.4)

At a=1, a>b and T>=51/25 these imply the explicit strict bounds

    c+d < 98/103,       max(c,d)<49/103.             (5.5)

The rational constants follow by setting tP=1 and s0<2 in (5.3)-(5.4), whose right sides decrease as T or tP increase. At T>=2, more simply S<a and m<a/2.

Consequently, for a>b, G(C),G(D)>=0 and T(P)>=2,

    H_2=max(a,b,c,d,(a+c+d)/2)=a.

Any positive cap ell>a can be removed with strictly larger trace. Hence every genuine full-class local maximum in this sector has

    0<=ell<=a throughout P.                          (5.6)

When the independent two-anchor representation is applicable, (5.6) is an actual extra constraint on its lower homogeneous star:

    (a-d)x+(a-c)y+(a-b)hA(x,y)>=0

on the actual projected body, equivalently the same bound on each lower boundary point. It is not a replacement of hA by zero. Both stars may still be nonflat, and positive-ell auxiliary vertices can still exist.

The threshold conclusion does not assume the clipped Q preserves G(C),G(D)>=0. It need not. A full-class local maximum can be contradicted by any admissible Q; a sector-constrained optimization cannot use that step without further argument.

## 6. Optional removed-volume diagnostic
This section explicitly uses the previously accepted universal adjacent-triangle trace bound T(Q)<20/9; Sections 1-5 do not.

A boundary-point fan from o in the root gives e<=3Hv/4: each tetrahedron has one vertex at ell=0 and three at ell<=H. For general convex bodies, approximate by inscribed polytopes retaining o; for polytopes this is the literal nonnegative fan over maximal facets. Triangulation diagonals here are integration devices, never physical edges.

If H>=H_2, gamma<=2. Set zeta=W/v, k=e/(Hv)<=3/4, f=F/(Hv)>zeta. Formula (3.2) and T(Q)<20/9 give

    T(P)<[(20/9)k+2 f]/[(1+zeta)(k+f)]
         <=[5/3+2 zeta]/[(1+zeta)(3/4+zeta)].        (6.1)

For the last inequality, the fraction decreases with f and increases with k. Thus zeta>=1/12 implies

    T(P)<132/65<51/25.

The exact general threshold for the right side of (6.1) to be <=51/25 is

    612 zeta^2+471 zeta-41>=0.

This extends the same removed-volume diagnostic of the one-zero parent to all endpoints at H_2. It does not close arbitrary cores below H_2.

## 7. Sharper exact section relaxation and limits
For a>b, eliminating z at ell=H from (2.1) gives the additional actual-section inequalities

    x,y>=0, x+y<=t,
    (a-d)x+(a-c)y <= (a-b)t+b-H,
    (d-b)x+(c-b)y <= (a-b)t+H-a.

Maximizing the positive linear functional n on this five-halfspace polygon produces a finite, exact, parameter-dependent improvement of B_H(t). These are necessary containing-tetrahedron inequalities, not a proof that every point or section in the relaxation belongs to an actual body of volume t/6. No piecewise optimum or extra value theorem for this relaxation is claimed here.

All statements are analytic and independent of numerical search. No equilibrium-class preservation, C34 attaining object, whole E17 exclusion, registry decrement, or universal T<51/25 follows from them. Global mechanical bounds remain 34<=Cmin<=622, with C622 only an attaining upper-bound example. The remaining two-anchor high-trace sector still requires both nonflat stars, upper defect >1/64, all genuine root/polygon reactions, and now the actual height-one bound and the tighter endpoint inequalities. Negative G(C/D) and bounded-height non-CH one-zero cores remain separate live directions.
