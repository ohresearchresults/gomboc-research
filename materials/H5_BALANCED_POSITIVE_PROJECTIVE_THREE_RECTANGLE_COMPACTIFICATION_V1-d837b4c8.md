# material-d837b4c864ea

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# H5_BALANCED_POSITIVE_PROJECTIVE_THREE_RECTANGLE_COMPACTIFICATION_V1

## Status and exact antecedent
This is a coordinator analytic theorem, not a completed all-root exclusion. A continuous PSD-stress computation on the charts is in progress; no numerical sampling is promoted to a universal conclusion. The literal geometric antecedent minimum-0231 was read completely, SHA256 caca8b2fe76419e5069d48126156237d6afc6c344dae2add7fdfcced9a7be10b. It supplies the actual H5 incidence below. The present theorem fixes the original top-size parameter rho=1 and the central basal geometry. It does NOT rename its two new chart variables as the original rho, nor cover all three positive-projective parameters.

## 1. Actual body and the full two-dimensional domain
The seven bottom vertices are (B_i,0), with
B_0=(3/20,0), B_1=(7/10,0), B_2=(1/5,4/5), B_3=(2/25,23/25), B_4=(0,2/5), B_5=(0,1/5), B_6=(1/20,1/25).
The three top vertices are Y_7=(0,0,1), Y_8=(1,0,1), Y_9=(0,1,1). This is the literal central H5 body with original rho=1, not a new incidence type. Its outward maximal cycles are
(6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8), (9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).
Its true edges are 01,06,07,12,18,23,28,34,39,45,49,56,57,67,78,79,89.

Apply T_{s,t}(x,y,z)=(x,y,z)/(1+s x+t y), then uniformly refill its actual hull. The COMPLETE positive-denominator domain is exactly s>-1 and t>-1. Necessity follows at top vertices8,9. Sufficiency follows because every projected source point belongs to Delta=conv((0,0),(1,0),(0,1)). In the preceding compact-lambda coordinates at lambda=1/2 this is sigma>-2,tau>-2, not the previously bounded normalized1/25 square.

Put u_i=(1-B_ix-B_iy,B_ix,B_iy), i=0,...,6. Let d=(1,1+s,1+t)>0, considered up to a common positive multiplier, and D_i=d.u_i. The three top denominators are d_0,d_1,d_2. For any chosen bottom anchor k, apply the unique affine map that takes its projective image to0 and the projective top vertices7,8,9 to e_0,e_1,e_2. The resulting exact bottom coordinates are

    X_ij=d_j(u_ij-u_kj)/D_i,  j=0,1,2.                    (1)

To prove (1), the original affine barycentric coordinates of bottom i relative to bottom k and the three top vertices are (1,u_i-u_k). A projective map multiplies each such coordinate by its anchor denominator and divides by D_i; their sum remains1. Normalizing the transformed anchors therefore gives (1). This is a passive affine normalization of an ALREADY uniformly refilled projective body, not transportation of its old centroid through a projectivity.

## 2. Three compact rectangles, with removable singularities resolved
Choose l in{0,1,2} for which d_l is largest and normalize d_l=1. Let m<n be the other two indices. Define NEW chart variables

    eta=d_m+d_n in(0,2], h=d_m/(d_m+d_n) in(0,1),
    d_m=eta h, d_n=eta(1-h).

These eta,h are NOT the original physical top-size rho and NOT the original projectivity s,t. The three closed rectangles eta in[0,2],h in[0,1] cover the entire positive quadrant after the stated normalizations. The rectangles deliberately include points where the selected weight ceases to be maximal; this merely creates overlap, not an invalid body when eta>0 and0<h<1.

Choose fixed anchors k_0=2,k_1=4,k_2=1, each satisfying u_{k_l,l}=0. Every opposite-side pair has both other barycentric coordinates positive. For u_il=0, cancel the common eta factor in (1) BEFORE taking a boundary limit:

    X_il=0,
    X_im=h(u_im-u_km)/(h u_im+(1-h)u_in),
    X_in=(1-h)(u_in-u_kn)/(h u_im+(1-h)u_in).               (2)

For u_il>0 retain

    q_i=u_il+eta(h u_im+(1-h)u_in),
    X_il=u_il/q_i,
    X_im=eta h(u_im-u_km)/q_i,
    X_in=eta(1-h)(u_in-u_kn)/q_i.                          (3)

The top vertices remain e_0,e_1,e_2. Equations (2)-(3) are rational and regular on EACH ENTIRE CLOSED RECTANGLE: opposite-side denominators are positive convex combinations of two positive constants; all others are at least u_il>0. No endpoint is deleted and no large-parameter cutoff is used. The same algebraic construction works for any fixed H5 basal geometry with this zero pattern and strictly positive remaining barycentric entries, although the numerical inputs here are exactly the central body above.

## 3. No loss of three-dimensional volume or actual centroid
The chosen bottom anchor is always0 and the top vertices are always the three standard basis vectors. Thus EVERY closed-chart hull contains their fixed tetrahedron and has volume at least1/6. The coordinates are uniformly bounded on the compact rectangles; for the displayed rational data the elementary bound |X_ij|<=50 suffices.

For positive eta and0<h<1 the chart is affinely equivalent to the genuine projective image and has the literal10/17/9 lattice. At the boundary, repeated labels and hidden vertices are allowed; it is not legitimate to call them genuine E17 bodies. The hull stays full dimensional. The exact bottom supporting plane, after cancelling an overall positive factor, has normal

    n_l=eta h(1-h), n_m=1-h, n_n=h.                       (4)

It never vanishes on the rectangle. Each limiting labelled face fan is a continuous limit of actual outward face fans. With

    D=sum_{oriented fan triangles(a,b,c)} det(X_a,X_b,X_c),
    J4=sum det(X_a,X_b,X_c)(X_a+X_b+X_c),

one has D=6V>=1 and the ACTUAL uniform centroid g=J4/(4D), INCLUDING closed limits. One proof passes the interior identities to the limit: the convex hulls remain uniformly bounded and contain the fixed tetrahedron; their indicator functions converge almost everywhere off the limiting boundary, so volumes and first moments converge by domination. Equivalently the supporting-cycle centroid lemma applies. No artificial origin mass or polar recentering is used.

The all-SPD question is unchanged by the affine normalization. If W has the transformed top-minus-anchor vectors as its columns, then x_projective-g_projective=W(x_chart-g_chart), and the physical metric transforms as M_chart=W^T M_projective W. This is a bijection of the SPD cone.

## 4. Boundary anatomy
At eta=0 all five bottom labels with u_il>0 coincide with top vertex e_l. Only the opposite-side pair, together with the three tops, can remain distinct: at most five distinct labelled positions, still spanning three dimensions.
At h=0 and eta>0, all bottom vertices and the two top vertices other than e_m lie in the plane X_m=0; the body is a pyramid with apex e_m. At least two bottom labels fail to be extreme. The opposite-l pair lies on the line X_l=0 with e_n; their coordinates are X_n=1-u_kn/u_in<1, so one lies between the other and e_n. The opposite-n pair lies on the line X_l=1 with e_l and has X_n=-eta u_kn/u_il<0; again one lies between the other and e_l. The pairs are disjoint because the basal polygon avoids triangle corners. Hence at most five basal vertices, two additional base top vertices and the apex remain: at most eight actual vertices. The h=1 argument interchanges m,n. The boundary eta=2 is only a finite chart edge, not necessarily a degenerate body.
These counts are geometric statements, not a new lower-bound theorem. A forthcoming direct stress cover may include the repeated-label boundary arrays without invoking any historical low-vertex exclusion.

## 5. Consequence for the unresolved task
For this fixed actual balanced H5 body, excluding U1 under all SPD metrics throughout its COMPLETE positive horizontal projective quadrant is now a bounded continuous problem on THREE TWO-VARIABLE RATIONAL CHARTS, with true moving volume centroid and a uniform volume floor. This is substantially different from testing a bounded projectivity square or a finite set of large projectivity values. It does not itself prove the desired all-root exclusion, any whole-incidence closure, the C34 prohibition, density of proper110, or a new attaining example. The accepted global interval34<=C_min<=622 is unchanged.
