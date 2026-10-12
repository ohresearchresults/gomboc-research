# material-2f4fa0fcb3d4

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# GLOBAL_TRACE_LOCALIZATION_WITH_RADIAL_CUTS_AND_SCOPE_CORRECTION_V1

## Exact sources and evidence status

1. New coordinator proof RADIAL_MARKED_CONE_CUT_DOMINANCE_V1, material [internal-source-reference], 13889 bytes, SHA-256 4660697874d9d2e92c4958e563f398e70704fb93fdce16c06f3308d2adcfdd02. Its mathematical theorems and proofs are unchanged by this note.
2. Complete accepted worker result HIGH_TRACE_VARIABLE_ENDPOINT_LOCALIZATION_16_V1, assignment minimum-0142, 40674 bytes, SHA-256 8fb94d359f15a77c8c5b7d6b1395ea099a9bbaecc6be1bbb741498706df275c2. Read from cursor 0 through eof:true in this coordinator turn. In particular, its Sections 5.1-5.4 explicitly extend the arbitrary-body polyhedrality theorem to zero C/D endpoints, and Sections 6-8 treat proper-patch resolution. This accepted theorem is used as a working mathematical premise; no independent replay or source-authentication claim is made.
3. Earlier coordinator high-trace attainment source [internal-source-reference], SHA-256 52786c239b2ed0a438f276cb7c2baa108b5617168f5398a25da747e2b7515379. Read completely. This earlier source alone only invoked the positive-C/D version of the polyhedrality theorem, but it is not the latest authority on the zero-endpoint extension.

## Scope correction to the radial-cut source

The radial-cut source Section 8 correctly distinguishes its new nonstationary convex-body theorem from the earlier polytopal local-max A-star proof. However, its statements suggesting that zero-endpoint high-trace polyhedral localization is still open overlook the explicit accepted extension in minimum-0142. Correct them as follows:

- Zero-endpoint high-trace polyhedral localization is ALREADY PROVED in the full joint variable-endpoint maximum problem, conditional on the accepted arbitrary-body local proof as expressly patched in that result. At a maximum, the positive root-G integral supplies the needed sign hypothesis.
- The remaining zero-endpoint question is the VALUE of the original trace on those actual finite bodies, not a missing general polyhedrality proof.
- A maximum restricted only to c=0, to a fixed facet lattice, or to an arbitrary fixed number of vertices must not silently be given all variations of the full variable-endpoint maximum.
- The radial-cut theorem remains stronger in a different direction: it compares every actual convex body with its z>=0 clip, without any maximum or finite-localization assumption. Its global balanced bound T<=2 and global endpoint-ratio obstruction also apply before maximization.

The correction is scientific scope, not a defect in the radial integral, exact cut formula, A-cut proof, or B-cut contradiction. Earlier historical notebook wording that leaves zero-endpoint polyhedrality open is superseded by this source and the literal accepted result.

## Combined high-trace localization theorem for the entire enlarged convex-body class

Use A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0), P containing their tetrahedron, and P contained in x,y,ell>=0. Allow arbitrary bounded convex boundaries and enlarged coordinate support facets. With

ell=a+(d-a)x+(c-a)y+(b-a)z,
n=(a+b+c)x+(a+b+d)y,
T=(int_P n)/(6 Vol(P) int_P ell),

allow all nonnegative endpoint values, not all zero. Let tau=51/25.

If this enlarged class contains any actual body with T>=tau, its global maximum M>=tau is attained by a marked positive-root POLYTOPE. After the genuine affine A/B relabeling, a maximizer has a>b>0, lies entirely in z>=0, and has at most 16 true vertices. If exactly one of C,D is on ell=0 the bound is 13; if both are on ell=0 the bound is 12. These are true-vertex counts, not input-label or triangulation counts.

Proof. Sections 3-4 of the accepted result establish compact attainment over the full variable-endpoint convex-body class, positive common-edge endpoints, a genuine positive-area root, and

int_F G/|grad ell| >= 6 V^2 (M-2)>0,

where G=n-N/V-(N/E)ell uses the actual maximizing body's moments. Previously its selection of unequal A/B endpoints at the equality threshold used a proper-polytope balanced premise. The new global balanced theorem from the radial-cut source is stronger: a=b implies T<=2 for EVERY enlarged marked convex body. Hence EVERY high-trace maximizer now has unequal A/B endpoints, even when the initiating body is nonpolyhedral or has enlarged coordinate facets and even at M=tau.

The boundary extension and incidence accounting in Sections 5.1-5.4 of the accepted result therefore apply directly: the maximizer is polyhedral and has the 16/13/12 bounds according to the number of zero C/D endpoints. No approximation of local maxima by positive-endpoint local maxima is used. Finally, if the maximizer contained any negative-z point, the new strict A-cut theorem would replace it by P intersect {z>=0} with larger trace, a contradiction. This proves the combined statement.

## Quantitative consequences on the maximizing stratum

Normalize mu=ell(g)=1 at the actual volume centroid. The accepted high-trace compactness bounds and the new endpoint theorem give

1 <= t=6V < 45/7,
4/25 <= a,b <=4,
a>b,
b/a <100/121,
a-b >2184/5525,
a >12584/5525.

All marked endpoints and max_P ell are at most 4 under this normalization by the accepted affine-height centroid bound. The actual pointwise tetrahedron-container formula, together with z>=0, gives

x,y,z>=0, x+y+z<=t<45/7.

Indeed 6 Vol(conv(Tetra,p))=1+(-z)_+ +(x+y+z-1)_+ <=t, and t>=1. The affine coefficients and all actual maximizing bodies are thus in an explicit bounded domain. This is not a statement that arbitrary parameter tuples in that domain are realizable.

## Proper-pair and mechanical boundaries

The combined theorem concerns the CLOSED enlarged marked class. It does not assert that an arbitrary marked maximizer at M=tau can be made proper without losing any trace. The accepted properization K_rho=conv(Tetra,rho P+(1-rho)q), q in the relative interior of the root, preserves the respective 16/13/12 vertex budgets and approaches M with T(K_rho)>=rho^4 M. It provides a proper counterexample above an input value when M is strictly larger than that value. At equality, the original proper-polytope counterexample itself can be used only when one was actually supplied. No nonexistent strictness in a limit is inferred.

For proving an upper bound on the enlarged class, this distinction causes no problem: exclusion of all high-trace marked polyhedral maxima suffices. For proving a mechanical E17 prohibition it matters: the trace problem remains an auxiliary relaxation, and neither clipping nor properization preserves the old centroid, original face lattice, equilibrium census, or common primal/polar metric.

The current value frontiers are the one-expanded/both-nonpositive all-positive octant sector, the one-zero-endpoint octant value complement beyond the accepted NF/CH/low-covolume completions, and any other specifically unclosed actual finite sectors identified in the shared notebook. The accepted global mechanical bounds remain 34<=C_min<=622. No attaining class110 object of complexity 34, no general E17 exclusion, and no exact minimum are claimed here.
