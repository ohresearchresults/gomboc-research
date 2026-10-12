# minimum-0119

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# SYMMETRIC_CONSTANT_DEFICIT_ROOT_TRAPEZOIDS_203_V1

## Determination and scope

The universal compact weighted maximum is not determined here, and no threshold counterexample is claimed. A complete five-parameter class of genuine triangular-pair bodies is now excluded: **every symmetric constant-deficit root trapezoid defined below has T < 203/100**, for every 0<b<1 and 0<=q<=13/16, with no restriction on its overhang, height, volume, or the three root-shape parameters. The new certificate is self-contained and does not invoke any earlier trace inequality. Applying the already accepted endpoint-floor theorem for q>=13/16 extends this class exclusion to every q>=0; that last extension is inherited, not a replay of the old endpoint certificate.

A second, negative result is complete on a continuous interval: **narrowing the actual transverse widths of nested genuine triangular-pair bodies can strictly increase T throughout an interval**, while preserving the same root plane, endpoint values, and projected density-coordinate domain. Thus filling the transverse fibers toward maximal width is not an extremizer reduction. This is not a failure of the valid transverse Steiner symmetrization, which preserves the moments in the symmetric endpoint setting.

The new class permits substantial overhang and values of q outside the old small-endpoint chamber. Its restrictions are structural: all vertices outside the canonical tetrahedron are on one symmetric trapezoidal root, with constant transverse deficit. It does not cover arbitrary symmetric root polygons, unequal c,d, or additional positive-density vertices. No reduction of a global maximizer to this class is asserted. The global minimum bracket and all incidence censuses are unchanged.

## Input authority and reading

Read the complete supplied journal and literal parent through EOF, including its encoded recovery; decoded and read all five complete source/checkpoint files. The journal is 303982 bytes, SHA256 a9164a8a1be672d83dc975e5bd8d5c85684b7374091fdc8f6f21b175c2cc7025. The required parent is minimum-0115, immutable envelope 52111 bytes, SHA256 31f05520aa6dbb2d24198b670bc41133b0fc57ba7366eea3e348fab85bb2f081. Its envelope was authenticated; no alias, incidence, or scientific conflict was found. The parent recovery was decoded in sources mode only; I do not claim to have rerun its old full certificate suite.

The parent establishes a compact actual-body overcover, while explicitly leaving its maximum and boundary equality problem unresolved. This distinction is retained here. Its objective is the original weighted J In/(6 I4 Iell), not the uniformly refilled image objective.

There is no missing computational dependency for the new result. The complete older endpoint-floor recovery is not separately attached as a literal parent in this pack; its theorem is an accepted notebook premise, used only for the optional q>13/16 extension. The new q<=13/16 theorem is independent of it.

## 1. The exact actual-body class

Use A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0). Put alpha=1-b, h=1+b, and choose

    0<b<1,  0<=q<=13/16,  0<eta<r<R.

For t=r,R define z_t=[1-(1-q)t]/alpha. In the following order let

    P=conv(A,B,C,D,
           (eta/2,r-eta/2,z_r), (r-eta/2,eta/2,z_r),
           (eta/2,R-eta/2,z_R), (R-eta/2,eta/2,z_R)).

The actual affine root slack and numerator are

    ell=1-(1-q)(x+y)-alpha*z,
    n=(h+q)(x+y).

Thus the original endpoint values are (1,b,q,q), and

    V=integral_P 1, B_ell=integral_P ell, N=integral_P n,
    T=N/(6 V B_ell).

Every added vertex has positive x,y. Consequently the ENTIRE maximal coordinate facets are exactly ABC and ABD, and their true intersection is AB. For q>0 all eight listed points are true vertices. The four added points are a genuine quadrilateral root: their projected xy area is

    (R-r)(r+R-2eta)/2 > 0.

Their physical root area is this quantity times sqrt(1+2(1-q)^2/alpha^2). No auxiliary triangle or vanishing root is substituted for this facet. At q=0 the root can acquire C,D and some listed root points can cease to be vertices; the actual hull and limiting moment formula, rather than the eight-vertex description, apply.

The theorem is invariant under genuine affine transport followed by the corresponding canonical normalization. It imposes no mechanical metric. The exact controls below use I at each body's own actual volume centroid; none is 110.

## 2. An affine density-coordinate reduction that keeps the original moments

Use the AFFINE coordinates (x,y,w), w=ell, whose absolute Jacobian is alpha. This is not the balanced projectivity and is not a uniform refill of its image. Put s=x+y and t=x-y. The projected anchor triangle is

    D0=conv((0,1),(0,b),(1,q)),

and the two projected root points are E=(r,0), F=(R,0). Let D=conv(D0,E,F). In (s,w,t), the actual body has fibers |t|<=W(s,w).

At the three projected anchors the widths are s; at E,F they are s-eta. In any convex representation of a projected point, write lambda_root for the total weight on E,F. Its maximal transverse coordinate is s-eta*lambda_root. Hence, EXACTLY,

    W(s,w)=s-eta*p(s,w),

where p is the minimum possible lambda_root. Equivalently p is the lower convex envelope of the five lifted data values 0,0,0,1,1. The two transverse endpoints can be chosen consistently because all fibers are symmetric. This proves the width representation from one convex body; p is not an independent volume density or a freely fitted moment.

Since dx dy=ds dt/2, integrating over |t|<=W leaves precisely W ds dw. Define

    Vbar=integral_D W, Sbar=integral_D sW, Bbar=integral_D wW.

Then V=Vbar/alpha, B_ell=Bbar/alpha, N=(h+q)Sbar/alpha. Set

    A6=6Vbar, M24=24Sbar, E24=24Bbar.

The ORIGINAL trace becomes

    T=alpha*(h+q)*M24/(A6*E24).

This identity retains both original volume factors and the original density integral. In all twelve exact controls it is separately checked against true three-dimensional hull integration and against J In/(6 I4 Iell) on the balanced image.

### Complete projected subdivision

The lower-envelope facets can be enumerated from the ten triples of the five lifted nodes. Besides p=0 over D0, the possible supporting planes are:

    high: p=[(1-q)s+w-1]/[(1-q)R-1], when (1-q)R-1>0;
    low, q<b: p=[b+(q-b)s-w]/[b+(q-b)r], when b+(q-b)r>0;
    low, q>=b: p=[b+(q-b)s-w]/[b+(q-b)R];
    middle, 0<q<=b: p=1-w/q;
    middle, q>=b>0: p=1-w/b.

Their support conditions follow directly by testing the other two lifted nodes. For example, the low q<b plane has value below 0 at (0,1) and value at F at most its value 1 at E; the competing low plane through F would fail at E. The high plane through F is valid precisely with its positive denominator; the competing plane through E fails at F. The AEF plane fails at B. Planes through A,B and one root point fail at C. This exhausts the lower facets. Coplanar equalities join adjacent cells and cause no loss of coverage. The q=0 case follows by continuity, with its zero-area middle triangle omitted.

Here are the resulting exact integrals. A triangle with vertices (0,H),(1,q),(t,0), positive twice-area z, and widths 0,1,t-eta contributes

    C(t,H,z)=(zU,
              z[U(1+t)+1+t(t-eta)],
              z[U(H+q)+q]),   U=1+t-eta,

to (A6,M24,E24). Set C=0 when z<=0. The anchor triangle contributes

    core=(alpha,2alpha,alpha(h+2q)).

For q<b add

    low=C(r,b,b+(q-b)r),
    high=C(R,1,(1-q)R-1),
    middle=(zU,
            z[U(1+r+R)+1+r(r-eta)+R(R-eta)],
            z*q*(U+1)),
    z=q(R-r), U=1+r+R-2eta.

For q>=b replace low and middle by

    low=C(R,b,b+(q-b)R),
    middle=(zU,
            z[U(r+R)+r(r-eta)+R(R-eta)],
            z*b*U),
    z=b(R-r), U=r+R-2eta.

The high and core contributions are unchanged. These formulas are integrations of affine widths over the entire lower-envelope subdivision, not interpolation of sampled bodies. On a triangle of area H with values Wi,si,wi, the formulas used are integral W=H*sum(Wi)/3 and integral sW=H[(sum Wi)(sum si)+sum Wi si]/12, with the corresponding formula for wW.

## 3. Complete continuous certificate

The exact finite certificate proves the stronger denominator-cleared inequality

    G=(203/100)*A6*E24-alpha*(h+q)*M24 >= alpha^2/100000.

Both denominators are positive: the fixed tetrahedron supplies A6>=alpha and E24>=alpha(h+2q). Therefore G>0 for b<1, proving T<203/100.

For q<b put S_A=1/(1-q), S_B=b/(b-q). They satisfy S_B>=S_A. Four regions exhaust all r<R: R<=S_A; r<=S_A<=R; S_A<=r<=S_B with R>=r; and S_B<=r<R. For q>=b, the two regions R<=S_A and R>=S_A suffice. The following substitutions cover these regions completely. In every row q=13Q/16. Variables explicitly described as unit range over the CLOSED interval [0,1]; orthant variables range over [0,infinity).

|Case|Substitution|Unit variables|Orthant variables|
|---|---|---|---|
|below|b=q+(1-q)k; R=w/(1-q); r=uR; eta=vr|Q,k,u,v,w|none|
|straddle|b=q+(1-q)k; r=u/(1-q); R=(1+w)/(1-q); eta=vr|Q,k,u,v|w|
|middle|b=q+(1-q)k; r=[k+q(1-k)u]/[(1-q)k]; R=r+w/[(1-q)k]; eta=vr|Q,k,u,v|w|
|beyond|b=q+(1-q)k; r=b(1+u)/[(1-q)k]; R=r+w/[(1-q)k]; eta=vr|Q,k,v|u,w|
|qhigh_below|b=qk; R=w/(1-q); r=uR; eta=vr|Q,k,u,v,w|none|
|qhigh_above|b=qk; R=(1+w)/(1-q); r=uR; eta=vr|Q,k,u,v|w|

Actual middle/beyond parameters have k>0. Their k=0 certificate face is only an algebraic closure, not a body obtained by dividing by zero. The q=b seam is covered by qhigh, without division by b-q.

After substitution certify

    100000*(1-q)^4*(k^4 for middle/beyond, otherwise 1)
      *[G-alpha^2/100000] >= 0.

The multiplier is strictly positive on every actual domain. The result is a polynomial. Unit variables use tensor Bernstein coefficients; orthant variables remain in ordinary nonnegative powers. Coefficientwise nonnegativity therefore covers the ENTIRE unbounded orthants as well as the unit boxes. There is no volume or height cutoff and no infeasible-cell pruning.

Exact counts:

|Case|Leaves|Nodes|Coefficient count|Positive|Zero|
|---|---:|---:|---:|---:|---:|
|below|127|253|266700|266028|672|
|straddle|18|35|37800|37716|84|
|middle|1|1|4800|3782|1018|
|beyond|1|1|4800|2251|2549|
|qhigh_below|3|5|6300|6300|0|
|qhigh_above|3|5|6300|6076|224|
|Total|153|300|326700|322153|4547|

The zero coefficients are intentional. Strictness comes from the separately retained positive alpha^2/100000, not from falsely calling all coefficients positive. Tensor degrees are (6,3,4,2,4) in the four ordinary cases, (7,7,4,2,4) for middle, and (7,7,2,4,4) in the reordered beyond variables (Q,k,v,u,w).

All 153 exact leaf paths are embedded in the recovery. A binary-prefix verifier checks every split, equality seam, leaf, and Kraft sum 1. The coefficient vectors generated by repeated exact de Casteljau bisection were independently compared at EVERY leaf with direct restriction of the original power polynomial followed by the power-to-Bernstein transformation. All 326700 coefficient comparisons passed. This is a continuous algebraic proof, not a finite numerical shape search.

## 4. Root, patch, and balanced-endpoint boundaries

For the strict class, positive root area and exact coordinate facets were proved geometrically above. Neither is inferred from compactness.

At eta=0 the coordinate triangles generally grow into patches. At eta=r the near root edge can collapse; at r=R the entire prescribed root trapezoid can lose area. The actual hull integrals have their continuous limiting values. Whenever the limit remains a full-dimensional body, its patch functional is at most 203/100 and therefore strictly below 51/25. A zero-area root is never called a facet. At q=0 use the actual merged root and actual extreme points, not the generic eight-point incidence.

The affine coordinate map divides by alpha, so it is NOT used at b=1. Nevertheless, for a sequence from this class converging in the parent's compact weighted body space, the ORIGINAL weighted integrals are continuous and its limiting functional is at most 203/100. Thus that part of the b->1 boundary cannot carry equality 51/25. Arbitrary b=1 bodies remain covered only by the independently accepted balanced theorem. At b=0 the inherited zero-common-endpoint theorem applies; it is not obtained by dividing an image formula by b.

No monotonicity of the parent's general patch resolution is asserted. No bound for all coordinate patches, all root-area-zero bodies, or all balanced bodies is inferred from this special family's limits. The parent's root-preserving contraction construction remains a separate tool.

## 5. Genuine controls and the transverse-filling obstruction

All twelve inputs are literal in the embedded source. Every hull is reconstructed from exact supporting triples, maximal polygonal facets, and their true edges. Two different actual tetrahedral fans give identical volume and first moments. Supporting-plane triple intersections independently recover the vertices. Every original body is recentered at its own exact uniform-volume centroid; its polar and all four primitives per true edge are computed with M=N=I. Across the twelve controls all 768 primitives are nonzero and every physical weak census is empty. None is 110. Eight-point 8/17/11 controls are not the target 10/17/9 layer.

### A nonwinning high-trace body

The exact parameters

    (b,q,r,R,eta)=(59/250,1/1000000,83/100,1,1/1000000)

give a genuine 8/16/10 body with a quadrilateral root, strict S/U/H=4/4/6, weak000, and

    V=27914051995961/152800000000000,
    B_ell=96163301613444399883/1833600000000000000000,
    N=21384330527091954377189/183360000000000000000000,
    T=16337628522698253144172396000000000/
      8052922204022901906678461954617689
     = approximately 2.0287826094404164.

It is in the already closed prism/small-q sector and is not claimed as a new record. It is retained because it gives a simple exact near-extremal control of the new family. The lower-complexity-parameter companion (1/4,1/100000,5/6,1,1/10000), also 8/16/10 and strict4/4/6, is retained with T approximately 2.028697719749602 and V=14875284979/81000000000. Full moments, weighted images, and mechanics for both reconstruct from the source.

### A real positive-endpoint overhang

Parameters

    (1/8,67/1000,13/16,134/125,1/10000)

give true 8/17/11, strict4/4/6, weak000. Here q-1/15=1/3000>0 and R-1/(1-q)=22/116625>0. The two root heights are 553/2000 and -22/109375, so the real body uses both signs of z. Its values are

    V=21333063727/105000000000,
    B_ell=22777346232709/420000000000000,
    N=13885145822496887/105000000000000000,
    T=971960207574782090000000/485910578714324468846443
     = approximately 2.000286164064386.

This proves the class is not merely the old prism or small-endpoint chamber. I have not asserted that this particular control fails every earlier Phi/Psi sufficient test. Its uniformly refilled balanced image has trace approximately 1.93948582047; the inverse weighted image integrals recover the displayed original T exactly.

### A complete negative width interval

Fix

    b=3/10, q=1/2000, r=18/25, R=3/4,
    0<eta<=29/50.

The bodies are nested decreasing in eta, keep the SAME density-coordinate projection D and root plane, and have exact coordinate triangles and a positive-area quadrilateral root. Their actual trace is STRICTLY INCREASING throughout this interval.

For these fixed parameters the affine moments at eta=0 and their slopes are

    (A0,M0,E0)=(676109/800000,71111423/40000000,61078049/64000000),
    (A1,M1,E1)=(-8439/100000,-4118691/20000000,-5070039/200000000).

Write A=A0+A1*eta, M=M0+M1*eta, E=E0+E1*eta. Apart from the positive constant alpha(h+q), the derivative of T has denominator (AE)^2 and numerator

    P(eta)=M1*A0*E0-M0*(A1*E0+A0*E1)
           -2*M0*A1*E1*eta-M1*A1*E1*eta^2.

Its complete degree-two Bernstein coefficients on [0,29/50] are

    388324891327300334217/25600000000000000000000,
    8296366300605920574513/640000000000000000000000,
    174486508672707989341641/16000000000000000000000000.

All are strictly positive. Thus the failure of width-filling monotonicity is continuous, not merely a comparison of samples. It also holds between two strictly positive eta values, so it cannot be blamed on a patch limit.

For the wide eta=1/10000 body:

    V=845127811/4200000000,
    B_ell=1908683961211/33600000000000,
    N=44037778257129/320000000000000,
    T=3236776701898981500000/1613081898029061339121
     = approximately 2.006579272790691.

For the narrower eta=29/50 body:

    V=15923801/84000000,
    B_ell=5369379443/96000000000,
    N=89861490357/700000000000,
    T=172534061485440000/85500929743822843
     = approximately 2.017920296333444.

Both are actual 8/16/10, strict4/4/6, weak000, with the SAME maximal facet cycles in the stated vertex order:

    012, 023, 031, 135, 142, 154, 246, 2673, 375, 4576.

Their root projected areas are respectively 22047/1000000 and 93/20000. Their own centroids are recomputed, not held fixed. Exact supporting-plane inclusion checks verify narrow subset wide. At eta=0 the patch body has true 8/12/6, coordinate pentagons, V=96587/480000 and patch T=28251770688/14079583577 approximately 2.0065771500622556; it is not relabeled as a true triangular pair. The narrower genuine body exceeds this patch value as well.

## 6. What was tried, and what remains

The principal reframing was to integrate in the ORIGINAL affine density coordinate w=ell, rather than vary three tail fractions independently or replace the balanced image by a uniform body. This produces a finite exact lower-envelope description for the chosen family and retains the coupling of all three physical integrals.

Numerical root-trapezoid exploration guided the family; the original complete optional locator and its full frozen checkpoint are retained in the recovery. It used NumPy2.3.5/SciPy1.17.0, one BLAS thread, differential evolution seed87126, population multiplier15, maxiter500, tol1e-10, polishing enabled, one worker, and the exact bounds embedded in its source. The saved checkpoint at evaluation11547 has T approximately 2.0287826414403733. This is only a locator and not a maximum or exclusion certificate. No numerical search is used by the exact acceptance commands.

The full compact weighted maximum remains unknown. The present upper bound is not asserted sharp even within this family. The most useful next extension is to allow different endpoint deficits eta_r and eta_R, then a convex nonconstant deficit along an arbitrary symmetric root polygon. The lifted-envelope method still integrates each genuine cell exactly, but its regular subdivision can change and must be classified. The continuous width counterexample shows why simply replacing the deficit by zero cannot justify this extension.

More importantly, reducing a global body to conv(T0,F_root) would have to eliminate all additional positive-density vertices while preserving or improving the ORIGINAL ratio, not just one moment. No such reduction was established. Unequal c,d and general coupled convex lower/concave upper graphs remain outside the theorem. Root-area-zero, coordinate-patch, and b=1 boundary strata outside the closure of this family remain as in the parent. This is a complete new shape-class exclusion and a reusable negative variational result, not a resolution of the whole research branch.

## 7. Exact recovery and actual verification receipts

The complete autonomous source below contains the exact generator/verifier, all 153 leaf paths, all twelve body inputs, the continuous width certificate, the optional original locator, and its complete frozen checkpoint. No journal, parent file, old sandbox, coefficient download, or solver is needed for the proof.

Environment actually used: CPython3.13.5, SymPy1.14.0, assertions enabled. The exact computations use rational arithmetic. The optional locator alone needs NumPy2.3.5/SciPy1.17.0. Its historical output path is retained in its original source; it is never run by build or verify.

Save the following complete block as recover_root_trapezoid.py, UTF-8/LF with a final LF. Run:

    python -S recover_root_trapezoid.py sources work
    python recover_root_trapezoid.py build work
    python recover_root_trapezoid.py verify work

A case name may be appended to build/verify to process below, beyond, middle, straddle, qhigh_below, qhigh_above, or geometry separately. All six polynomial cases and geometry were actually built and verified. A second clean source-only build reproduced all seven reports byte for byte. The compressed recovery was itself decoded in a fresh directory and its geometry build/verify reproduced the final pin. All leafwise independent power restrictions and all original-versus-weighted-image identities passed. One multi-case tool invocation timed out after its completed earlier cases; the remaining cases were subsequently run to completion, not counted from that interrupted invocation.

|Object|Bytes|SHA256|
|---|---:|---|
|recover_root_trapezoid.py|12044|24234471583201696cee92a371471c42b9abbc78a5019e5f5a41bae1268a2f2d|
|Decoded complete three-file payload|21592|79edc330c3afeac99d0bc2b927b5b728dcd44fbb11d5a01f68388ad5a7b10b49|
|root_trapezoid.py|19232|e9109cd723fa9885f440ea00ef4402e5c128072d52f1726aceaeb68595f1a48b|
|below.json|46112|b14565b5becdabf3dfc9f2a6c157f5fa9911c53e6f6b3420fd46bc519e041a5e|
|straddle.json|13284|27bd7cbe95557d80dc6dade8b5d817c373b1ea2f0ca7f69138c3f06d09108fb5|
|middle.json|26544|698f5681847a89c2b6596e6b59cbf2b3f0c2c517d7bcd03a63236f52a930b7c7|
|beyond.json|33657|52791c20e7ea30658583a8d144b7cd66ee4136d5bf7b660391fecd43f48f5b1c|
|qhigh_below.json|5818|8e31383aa93adf06589fb79c88f909184cdbf850eab0be7803ef08f8f35c674a|
|qhigh_above.json|8649|a558b9a28f63d25604213a4f3e80c01366b105c5cc7ea041dba8af8bc8d2fb54|
|geometry.json|87860|20d9e86c5f268c597622be76e3bfcf5796fb4a50ef616e841c1581fedbb607f3|

Terminal markers include ROOT_TRAPEZOID_EXACT_PASS for every case, SYMMETRIC_CONSTANT_DEFICIT_ROOT_TRAPEZOIDS_203_RECOVERY_PASS, and ROOT_TRAPEZOID_203_SELF_CONTAINED_RECOVERY_PASS. The report stores the exact power polynomials and coefficient-stream hashes; the source regenerates every coefficient, so those hashes are not being used as substitutes for missing arrays. Verification is exact computational algebra plus the geometric proof above, not a proof-assistant formalization.

Convenience copies: autonomous recovery (`recover_root_trapezoid.py`), plain exact generator and verifier (`root_trapezoid.py`), and all exact reports (`root_trapezoid_reports.zip`). The complete recovery below, not these links, is the durable handoff.

### Complete autonomous source

```python
# SYMMETRIC_CONSTANT_DEFICIT_ROOT_TRAPEZOIDS_203_V1 recovery.
# CPython3.13.5; proof child requires SymPy1.14.0.
# Sources mode is standard-library only. Locator is optional, never proof.
# Parent minimum-0115, SHA256
# 31f05520aa6dbb2d24198b670bc41133b0fc57ba7366eea3e348fab85bb2f081.
import base64,hashlib,json,subprocess,sys,zlib
from pathlib import Path
assert __debug__
PAYLOAD_PIN=(21592, '79edc330c3afeac99d0bc2b927b5b728dcd44fbb11d5a01f68388ad5a7b10b49')
SOURCE_PINS={'root_trapezoid.py': (19232, 'e9109cd723fa9885f440ea00ef4402e5c128072d52f1726aceaeb68595f1a48b'), 'trapezoid_search.py': (1303, '21cdd0a16567ccd2ff6d76a586e5989400f3968e0989e6fb320da81bd277ace1'), 'trapezoid_best.json': (601, 'f092bdce635e60866e6407adc69eeab342dbd7ec902afa2853ff638b1b75d342')}
REPORT_PINS={'below.json': (46112, 'b14565b5becdabf3dfc9f2a6c157f5fa9911c53e6f6b3420fd46bc519e041a5e'), 'beyond.json': (33657, '52791c20e7ea30658583a8d144b7cd66ee4136d5bf7b660391fecd43f48f5b1c'), 'geometry.json': (87860, '20d9e86c5f268c597622be76e3bfcf5796fb4a50ef616e841c1581fedbb607f3'), 'middle.json': (26544, '698f5681847a89c2b6596e6b59cbf2b3f0c2c517d7bcd03a63236f52a930b7c7'), 'qhigh_above.json': (8649, 'a558b9a28f63d25604213a4f3e80c01366b105c5cc7ea041dba8af8bc8d2fb54'), 'qhigh_below.json': (5818, '8e31383aa93adf06589fb79c88f909184cdbf850eab0be7803ef08f8f35c674a'), 'straddle.json': (13284, '27bd7cbe95557d80dc6dade8b5d817c373b1ea2f0ca7f69138c3f06d09108fb5')}
BLOB='''
c-qB0Yj@(flHd1Nc=~?82Jx^VB!N+%O?Rhnx^L2*b~2fnOE??@2HXMLu}wmf&41sjlH>=k^ga7wGd&=wN~Kb%R1aC^<y{m6$smcG
(0vZPaV>m$*LinK|6TokadCQWfB880`2E|}^~tyE!Kc&DUp{`h9@yW%Uk|SBlgrb8fB*97YG5^*gB!DU>wmm_N@juIteMT)0n@IY
7MD+E&1}^gUF~z^j1n*KH7D|t*}_e{5!0MFb|Y+!HP?5Bb9W3>E}h8r6M#*Ds{efT)bh@szkmGe`)GDrefsv{M-zH_i^Vd*9?<c@
od=<-U7ej+2kl$GX-*mk2Uf#z+T-ES8e1*%_-NQZYz#*&(`+_}jmhZXaOfO1+ill%nr^doG;xMU2Y@_j9N|R11zIS$n0Rxy?k&O~
N|+W0^9MI#n*HscO!M93F^KM%7DSr6O5DhI=Gxdv9L<XX=#FVJf5gtz?PwthM%xg#He7o1@&5o-Z}Oyl`eL7cy#8+gt@S>hT%Gno
qVUzx0^ikwi57b+ZG`fgcq1oqHQ!mdF^xZU1CVI+RMWmMyhOuZ+63C2`CN<L2iFHq#IoM{lPFkd6S*3(Cgzq~o>=>=ke2=^34(cw
G>?{pku#dP62XI67Z66lV(9q}QD$KjjF+QC;x3$ImPcdL(U{Fg3kePZJoknQ;}WX3zO2lg7-8&Z9QZ7Lif?_PH`-t@c8AO9U~ubS
efj6b3ID8vE;6&xFuL05<rUOTtihiFdUax-e!J$SeTr35XamqDUi!bP5|BGTJ-Io(;xDBb)_pvlyQPlSE1Bokxq03=FELG(?X;{)
Hew)btzLxNYjE4Nt@9?}ZEdx;v~ITLTe7m9qX{@`HG!vEGdRHtWxLde$`E$#qZEdim>?&ZXccRACWc&#z19M~Hn6a56K@+mNwc-9
-EQvggD~6L54Cqfw?VegMb4+WAGUoC8Pwhh-43yLjAkP}>%6reYVU#WhGh^{vI|;bujz@Z1Jx~9qIDNGt;AlKy%V;N=38{%rk!a`
9=h3PZ=JKfW6rjk*G|a3UUqBS`1!W1T;yw=A6w06ZDot?yL%MpunF7WGe3_!bX%*vgTLJ~vbSpEcKF*Aw)1Ll(TGi`y?1>3jnVC$
V{f+FJJ!+OxsLXpb<AMfN7~kE?-<|SIljF^y7t-(rF%>1=PBk^$}GZF+jdN{tmb(^|My}13Kcb%-8lQ<_M4p8zrcz83!K<{IeCkZ
x4C$mhkYF6ckXWZJ`RdIcNfM!sBON*gKfUeg>Amghi$&aiTx%g_AhW^{{knwS7ra2ytN{4t;fFAu=nbt{f0K$Z|I`ERTJ$k<JntB
vG-aZ`wcr(gxh=IyJ5Q^_FkUsH+Zt&;K|;@)22j=^=+JO=f}?Ub4U9oWqS){dn;voV}2RuB2ij+Y1$|gr>DRlXZ8D;H=PZ#bgCiq
%7&b>BqPwAVesHeG)tmcDcb9;f9sFki55AJgGI1#{Up|h?4Cu;X0Fk>^)>htCkeKjEF(YG^tN_0bRuT8G|x}mY2?hcxKMjEnD)rs
`MjpiAdm_UGjc*bVQ1`Fk;Xr7qCNl48=Z&-(DVj_|BMX&CpRle)y*0t;&b^=_FUHgEb9O_D)3R(0nadG>sjUAfPbPN408YbFgNNm
zc1@{H8Q$LKdRVOtDGAH7J=*e5dZ_nh{}2dV^nPHEXD#le^yK*$1$u7$Eika$c7dDzB)9@k%YVR*e$RzOxbvg31VRj1H<y4TL!mt
gWD30Dj|U;)6MEVfU2ehj)KVL&^TmP8NUohpE&tp#VX&c8A|ad%W&@M@p7R@!DH`dpAMj)2zsFDNQ(g{3`b-z55pk%PlQH}KXvsc
(i7Sj2J<IBSa{A{A31TVck(zWep-Z2cup0IW_cJC*9L<JH;TQ$9}GAziG#<Iz)5wO{a|-&$sX7vk840_7|dh6G}P|3NV7Fp`=Q-w
OYK2>EE#X8=`J<Ye^C!}^quioFN3IJqw@>GB*d-K`%hNQ!)e7Xtxk3}#pJOJQ&xv5b7TC!?iI!EZ(Q+18)wrv?9k{!f1Kcs?!zI!
uZV7U1&f58L8-DsyeQ(!I$?Hg8w6f?G(<J)=FYQ@(mZ3Y@?+NTabF*0_@R@2SGmXKyfey67)NqQB%-MDn6>07fnkBJ!yzuguk`wV
HATO$cp#Fz6Wg<d<-4^-*-JvL2Q7|m3sNWSf}L{QnVYstU`)Y+*mTwnc1oQ)mru&4)!dGQDO^-@c<Fhx*qr6ErOW^rJT72mG4*n*
tlz<BajS0ZOECv!v_oKO<oF|Zt`o`fv=%RivHmjb42LWNg<y8a21D3+C`Zw&+IguBRSyRA(CC?c&P@RiqOl8Fh{p2)%;#fXpv4WD
+SeRImtfEJxaO`x#~<sV;OL&^#RAf68|5FMG-VpgP~#>uZtWTjA`Eg6nja)WI?8(GW1`H`PI*{^&&YKLb1zPGqno(VBIYlP!0&v9
g?1;xutJ?-4T**|Leh=bg1ZAci~#JQid>@a`tS4siT*9{T|;=YJNGGu@q9Pdv6Hj%Vr5Jb#EBL8utbL~MD~0PR*_g4BM;EeFpRFZ
;xEq~kJ>%<j1bpfF5JjTTpejC9)n~C%hhwlL!it{%w1n6S}0NHH;%mYyTlvs^+n&Dr`cf2o%Wo*;*99hNJic{Ahnd3BAD}3L<GkL
I=ODb;`AE*vSPCPEb#cxA{LF!R!H&L3w7dv0mnuMI`sLfh>h&joG^4j^So70IM!#QZxlI>6%JO4fenGP(B#pL22K<?PkO2XY96vf
j~Z)JH_=g%KI;u5RjaLH-CXOw8gJ;tp3ob7w8;FW?<H&)tYE=N#R?($7wCeMzz3IOFLFnT;J5nzgA1X0;^HE>;KMxH<6YWbjxVtw
ph}!4SuTd^Ff_-H+9(L0^eloPM(}wj^3oA(^>myt%o^N!zf25gish^_MIcaK1;$+H254je#+DO3tmoX01I({@uZN)#?%2gpzhgg*
GL<|iF)EFrWR&MY8BAyu!1~Oq&I7QiYr3TEP|}6x1GPH?V-tei<rEkiML_1QH5PRq^#&0(_W!!t2lFxSp?G`Gf-dcB?9t!U{EdB2
3fqz0Im%^JUJ>dj+ayA6J+IGTu(iM)yQb>q#h^8rzU7V8d0qv&_NGGYopeTr{LQWjcjt4kTVMwI=#HUOHTyX!JkGqitD%K(jQ8f6
9D%65syrEWi-@k+lbSwEq-S>e29j4B9S1?5pVeU~W6f-B7xp<ydOnA^ylZ1IilA@xXTKoUb7m{4j=d@Dx&eBWi8t~nt9Fz)W?Vks
uEjIQI%wymN$clyX0>HF#^H6?yZXwglx}bRl2LR0Q80G(we_6UX6{N1sb?uw6a*7;mdwkn1pn;Jv-~P^X|y%@dK%Ux)4;czKtY18
Wbn*r5w0KyvWCP3JVSTxIuBqdVz7_m>39#x!(zm)>r=DQ^<iQ$Z)7>rgBN??CY@x)J_rMt*C#*l=fTLCYt%2_4%Lc^Vx-jy=_&#!
9PzQPL?RNxh{ExoFjz^PD2X4vWJaSK&^*?{-#AghMG7-oMv<0>0Yob7&Zg=4xLs6oeqG7SN6tTNWfHB_2jjgGllnt3)-ZA<ev2?%
1Euj}a07%xbHPD{$%Po#_ZG_q7xdWzb}v<(6;^jxQ1urEuu$HEOQvY`zL6<1^nG@tKma%|Lf)X7+dBiXPx!W7^}#UKCrq0nrxB}!
zl1$BAtatoTB=z6_4Ooe+0cO3oE;Mjfi!@y!MT-#p*MWN7<GlFCYvo_zIJmx5z*jzC3RLD8*5<@>ZuwytKUgGNC9yg`~}T{gZALO
#L}`|dd;U?1y9<gyloy-W*(Ty?)e7+N{#wj{rm%V!VZ-809@3e0%UWN24lx_zT*RWxo);)D|trG+4+a<K)b|jW`B@$1xBgF$f&R_
am8Blg4Tn}g+m#M7{O!~_<ag}L!(}|jEzm3ie5QH+!vH@ki8TcLyW-*!%+vcuwtW%{Gq2W*hq$WY=o3!h^*YPE&@R>aWQ`|`dgG-
*g5)S(k|i_WqExc1xqm1H~~8Pp#Yg=vTfI>?I(NDUh9=qYpI{9ArYe;S;WPbO}srLEu3iT`TX?qiX}6MFJ~Cg(1k1}ZqadZr%Kjv
|MKjXRqCR~K?06?n4W<VJLRWMUp_QsW(9d<p@#_WSJi!eMo|#Q`Cj1o&3<{<v-(vBKA>dwnJhK1ts$UHmP~9j1ys@;yTm!@fZ{~V
MT~{*647~>>X%y%`9gKXM{0R#)NzR~w;%E$o!N3ew~&%pl}j%54SnY&B#OZ@NmDSy7xOG|sHd}o=y;@NWmNTahSaWbvX~@x?<v>5
WS6~82V<t3V*_2;$o*(e&}+^AWuYAAZtqRnvcxDJc~(K-^bLy<8uU0Icog<<!=WjE7Un=8feP-V9&%XN-2hP<hho&j08Dh8iIUQB
Gyyfdn22$#E*5Ixg!*S-CTBooUx<w64(8A=ubG@68DW$)<S#|)Sso7S#F~W|h6{Z`t-b_>0Qq`-gNf>$tQuX&l0dn9Q7yzZDrWJG
&M5E`&tK*a>|%(kMaR&nj&sV^FVH}jAJ2{78^5EshZ0^dm5rRsHt^kBM#y?YMAGrOkXm(>b9~5sb)3uiz+%rw3&@05H9D?BIRSRs
LofSmOh+FeXWk=cS_VvG9i`u$^66--muW$=5zZtVpY>I}KFxI_Jh^VYvp&$4s}>d`{!2P5LCKx<I!#nY&d+*Hm6S}J(c0O`8S}<5
DF@M3)<2);MnTAZca`YgdK%fJ(avybyATBQb|84aaU_yYj6?n+W{P^D%n8{JOgM9NfV<Z&vdw#ouovd+j<71E|BKKtii&{}$m=Ik
03(5FNkz!ml&(_UDuN6~;seF%U|TJ6@mY<V-^~k75R8~tlz?LumYzhc_PE@OM0e5YSE$fgz}ROh@)P)I5g~$k!28m;MAAaO2uV!X
8P1qcGto?5)k*kxn(HF%w5ZV`gR}vgRM=1DawcqoDQ9KU>wt-TEru$%{}pFO6>Bu2QNbdS%R<SNJJq41;z1wtuS72=f}3Q+*z`!|
o2;S+QLWF?=SGNxOpx{?Gin(0Pv}>$5ezXFC!5pH_;vgk50Eg?n?SjEt|*RFbrH%L<t9Uq*h7`woM*pqta!t*PxpfN@Vj4bc1P}f
9&dOX<R-^gXY&Ll=TJ?i1a4F}P9sV2$1&HX5;OY#slF?)tlcEyYurPRe)pNv!q8R;S)`7YX_qCDVbt4OhMJ&we&d;N47CK$8z~-1
q{5#!Th|V&fXD?n4?r#JKpu-C;JE9rvDDh6MG{VT9?XnA=hG{>(ka3X6FcR?pk3={5Ez*ev9;$7k^%^qb5%C`6bWP?`1f8;|At-g
3?SP6q2-S~<7J2si9LT>CHo6=^MEJ1j1XadLN7f;?kE5?qxU0{Xz8XpS5u(^!QHVqjmR7KFYN1<eYUY5`bFPPu@@H}<O_X%#ZPqR
Y3#V+%g0-sY$*Mijy|ZI1(=|hl`mP-h&j~sHEY6<7n+Rvc;~ZYIW|Z|M|1x#>F|E%|LUb?<X_pA@1$Z9rwzrm&1A@5wr}v)&8$lV
RQ!^qc3Tyg@U-;Fgngz@cEeFCF4$B`W>vq*y!^$s#AU+uf&pfk0cM#2HW-;N{76%jk?Y6HSU=06#WT#Ukmpjr`xozt4G)deQs3AN
vVQQMVp5;YK&VxeGn7!!vR5uf5ddXuXLM)<Sj1mRMIhk=fAKoKoO}UA&8^gb?S}X32w4#N!!TacbGb*?xq}e48#`mH&YWm5cjKZ3
mmUs=Ac2+oIVA@cdGAhGAf``XJDeHCU@BwY$ehrG_WMs!&RO$MoV4&SJheu-{)M*pFA9R00Q^({4*@?F;74yF06%)OKEqlHm?^*n
0keMLxF~!8Lds@+qT^v``k8A&lONtg=d8&RO|x86voFp%Gs_9700@VDTH9zCPJhCX2qd0I-j2o_(l9=)ot}MK_go1_?&~y%isV}E
4wMx-fuv0GgJM-S8Jn)dAeE?r4Fu(PmUGyjtk*You}XIrwz8*GX<N^$EcB+s_V8YX%xdn>AfkTvk9E9<t$5pP3JlGEurTr#bYLNm
SYmNleZ`i(EdIe_y4?YxpEG8(9eOZj*OgltO1Z-wlFh!eopb}K0=xR-OxT_)VQKylUoe`H-F`x&9|e$@I+2q-TTE{-ahZn-XxEvC
Gl!eiVRy#O%CLLY;4{4E)BVba<*Nq#Q>LmXuSzibHtE}>x=HQ1T^>^cqr-T`Yd^YK6?YTj*r?OU-OC!j{0M8>)7`qo;<$=m&p=fc
MOCG$XPlDmOQU;(w(|zfCi|QH8!H!3`M_`F5c*%0zl|ylQvP@M8`ozQ)!M!0-|Bk1d{b6uh2plx_FIbuucQ+uM61wU(7s_-OBRWE
R#n77|G@|r0^c3B7!=Wc-%w%O3(D7e6~`ZmIFqEdX0Z*|!6;f)sl`E%@E31~WyjIfdgwVngxeYR{aOp2?TBfu0W65U8m~py9f<oB
$YFL}^1ZM>uKbSPyYy|pk2<-2;O$%NfVJ7-D}hl)r9MS?M}<MIf2Sit6~tZ7Tx|-T0-qlaojG1%8Ef9cnYv8Fqj${%X$6rt_3%Ag
&!_ZJdvv|&EKy+_?j9G9bkb9<R6Ze!B+N-6go&qDZ+K61t4JlwurnW?6I;KVdjNx{5h^~F;Y&}4jfXVq6GkNyOG6s7u5tl3QK@2%
GDB*TuP;1*K9$Yze0_dq{i;!5x}ux)AtW?~Nup>rB(vVLutGRH9BkvfOHFqgB<ty&2=fv53vLd-7$H13n6b$Ou9&xBcJUC*DYixu
>n;rvEg;{o^aKx^ITunca+^f`ZW!T9z{X}4NUjNn38V7*m66AU11I$`>LR}=8~&ISQ3zlXpp5wxiM9^egjm}7T&-;qG0b|_vn%Rv
W&L3-h{Uhb0Ld#~ilmC`20+?x_>FhCdSAiFeJy{0|G)JMm|x2R7xfYhqO3IfsstLr`L(p%>LIl7JUnM%87$a9UH9f6n4eX?v1@+K
=)L##qZn*7*uovn9N!zoJPoebT`Bbrqu?i`Z|->DM6Sc>Vj|r;#CwSb_!wmy1|Yu0at<iM)U&Vr>pDeYHh`AmGv;E(j4TfSBEAPp
-$QEn%KpgZx>b=I<_kG1)C^eyL7@P@kVhjpeCKx9whqSHbNe$40KR;?{NwtHzW_wt8P!W>y;WlHX*S@iDJrUgq?Nmux`y4VAHZju
K6Ci$YUu`clSZ(p=|Cc@7Y^2t5vfU4OClEDL_q8#0=FcR;`*R~F5gI4LznciCXmyoO_)@I#!Ry=?ZY}=oJ90y-E7l$t8Q9q&Il7k
9=$OQ)f6)TrewdPI$<}{`DJ~4CyK;;_V==m>j$b&=p>`r+g;KjTqhb}z8sO14~_w;kugF&kC0R&xAKh~kFmFa;C_JeEH0Dmd{A!}
dzOs!RS)&s5$O>%K0JE4>!>jFK_&+5fvh^|rwV(EVFPsRDRK3CrR!4vJvEWkWrOugJ%s#rciB`1g-bC9CIhKY%lyIauFCxy@6F7c
-MLTVQYrDzBvbi-_>3b-!0T_^2vBDzGPlP=6iWDa#E)xCW+F*B+akA|*2wAO?_XF)hvJU0p+c)aXOIC^=>+TnugJJl2PJ@40U@XB
Xks+apMu8(k1ZoBZ=B4~k&nRK#%`=#*9wV<OhfjoxUz634R+CBr;V)<I^B<y=kES^2TJ;mz=_E&Om=F@eD+B_U&<c#>S{FbOa3@}
FT$NnxPD=lPa5UZM)jgm)=x|*Rj>}(5cm;j!zPne5e-YSGbCx#WQIR4a?B2tV25txbGkG<LC>KI6;UwhA}jO)*R%^H>z1mQ%hqND
hQk;#<`!tbN9jiGl?Jp>ATd8k0`Q|=@>J?`N_^Fdb8(_9IvWgHmf*}XDaH8nInW>_`{rGo^x<9PJ&-01<N;3*ahefJH`!3#JLNQu
T@PYMbJy|p^kO6)4aFX2<&XvFEA~0N6F~RhwqxO(Q$#diM6_tWR%@1PorZY4#PAuIk<#iFC<!{nbB2|g$ijgYQ`5*j?1`V^niEYQ
D9zKGtR=3Isb(}&;{H1R91v_C@q<9>9i&Atc6kn$p6}yN<fL@z7z$czi@UKG>EfbA%&()R%iI;rW)R#_P3;EU(vZ`t?#(`>lLb~e
Z;5O6^h8kH)H5o*l5!ZOT;#9bPawLT4Qr^tZ%`5v#q)cfd8ORt{}f;FmAlhO65?xOORp~L_{%}H@p2Kyx>!pw3aCDO4(Jv>i7Iw6
xCK3i@D^5ql{#R;)^A&OLp1w!8n{xbA??!Ift}z+EM_OHJw~8)gW*$xw_$;y^|y4Sl)@UA+Ofm~@r#SO>FH#IPrpmWAKx0B{&n*4
dT@DibyZ>{3A#OxW3aVrrPP?e8p<Z~WjxDkg&g8P{OK?I^yBxNQ~Php1x~(58YD6p;Ez?&dwGKaZj!;E)DfHI)_=#|rN4;<79&nb
rtdoMUT)uA-@fZ;Rt>${k=1UQtyZIX*laTG_T3GF8Z{Hz51ZD}@o~G^XqpHaf%lCOYMKYFLu?Ul6q|azMy<g#`Y>x?x3yeDqh>YR
X47gPgD*QgKC+Ii6v31q@YlAQX2UveADNb0ZL|@^%oE*?(yE#5hI!a-9~`$EZL@U%fJ5wb)NEJ>hlj__;}$^M2SiAWy9wG!rLlL6
WBfZjZd+F4paD$f#@Gby8KaNVyeC0!5!Q~`r;|Lg8n8?U&89_@G~36At%lh?f;qy{whu*r%WO4Tt=4hlpnYJqrTA{?x9a4;+lbLL
j+&q*mUY-V1YVA6P0&w3Fpn+MvW{^UL@9RNF;Y4@G_CgQngYfUR*h!jr|{$(r$Kz{r-$Qu>HFpBw-4thSA%bVTnw(y?9-D^p!cQk
7nf@-7ymjhv>2Tr1~c;DMS<VD>+=%+K$si@T&Q@f)eq%QqQxUGe5%C|c6xZ?CD1+w{)4+ZTh8a~2ObZdLg*G1Is{?jExcz}^%#4T
iHq(4s0`ePV7|nMmQ15dzJQl<ko~;cKeT&H??)JWRU_smPCYW1I2Ii7G1H)hTTA8iAfV9i*%%tVdG1EJATV`8=JNZl&7%sGyG!nt
qdLa)m)s9);u?7`cO>0lLwPhkl1J0{y<|~!Nr%<=ElNw^PLyof)(68AICL)*+(hS$XX4T?vDICT+%VBH(J3Eag^(HGA;0XM)hL~!
D+t|yU)C1rF&akqffydfI($J$gXcCS?<ezqR^NLi7WO)<(XR#!pyG)uwwTz01q%v>eDZ(8A8Od!=q|Ya06=_wreCHv;}#I=Rsy5m
GN?kq<~7f~Q8<F{1qPD~b?R_aUZDR6M33$w!ZLL74?wOtNkzXl*o`dS)QO_O?)iN!3B=oQbWFqX)Sp@9rNPw0*c1VWkc6*yoAp~f
ICjUJc2}2dF>iFyu5-O=GWlj4ok-46O!p#Qn$CkE=sDpt#KuOdRk+zrIB6L<Di}C<j~FNg(}krI5eE&CFrkj*d%6(V`g*Cp@RK_F
zxozG1N-z5ygT{me4s$0qlw@L6Y~(<mCH1`*<TMJRIJdIp7g`%)pbd9WeMamYaUnW9!@pl+c&C?GGaZw)@U)XakwSiYMYt0=J5ek
YK<mq(l`8>SrN*@BEp`?CJ_c<3|pR?2Xv_)(gS|bXfRk`PI3eUSZTo_!(X?=i#(JB$q9Y>{_RvvD5_1CK76i<(|Y&%U;hi3@}r{
'''
def checked(raw,expected):
    assert (len(raw),hashlib.sha256(raw).hexdigest())==expected

def main():
    assert len(sys.argv) in (3,4)
    mode=sys.argv[1];assert mode in ('sources','build','verify')
    out=Path(sys.argv[2]).resolve();out.mkdir(parents=True,exist_ok=True)
    raw=zlib.decompress(base64.b85decode(''.join(BLOB.split())))
    checked(raw,PAYLOAD_PIN);files=json.loads(raw);assert set(files)==set(SOURCE_PINS)
    for name,value in files.items():
        data=value.encode();checked(data,SOURCE_PINS[name]);p=out/name
        if p.exists():assert p.read_bytes()==data
        else:p.write_bytes(data)
    if mode!='sources':
        cases=[sys.argv[3]] if len(sys.argv)==4 else [p[:-5] for p in REPORT_PINS]
        for case in cases:
            assert case+'.json' in REPORT_PINS
            subprocess.run([sys.executable,str(out/'root_trapezoid.py'),mode,str(out),case],check=True)
            checked((out/(case+'.json')).read_bytes(),REPORT_PINS[case+'.json'])
    print('ROOT_TRAPEZOID_203_SELF_CONTAINED_RECOVERY_PASS',mode)
if __name__=='__main__':main()
```
