# material-c672e654a6eb

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Recovery capsule part 1 of 2: every whole facet for every concave three-piece homothetic profile

Object identity: ALL_CONCAVE_THREE_PIECE_HOMOTHETIC_PROFILES_EVERY_WHOLE_FACET_V1.
The complete standalone source is part2, [internal-source-reference],15953B,SHA331b7473f4840cff16f05dc335f5661fefb9ada6830b3c32d4dc16f88dbd885c. Save that exact text as three_piece_all_whole_facets.py. The two parts are the complete proof/recovery capsule. The literal deterministic source, not a hash or a sandbox file, regenerates every coefficient and every actual control.

## 1. Theorem and exact scope
Let D be ANY compact full-dimensional convex planar body, and let h be a continuous nonnegative concave function on a compact interval, positive in its interior, with at most THREE affine pieces. There is NO restriction that its endpoint heights vanish. Fill

    P={(h(z)u,z): u in D}

uniformly. Let g be its ACTUAL volume centroid, Sigma its uniform volume covariance, and T_F the uniform second moment of a genuine WHOLE flat facet F about that SAME g. Put alpha_F=distance(g,aff F) Area(F)/Volume(P). Then

    alpha_F T_F <= (3/2) Sigma

in the positive-semidefinite order for EVERY genuine whole flat facet, including nonzero-height endcaps. This remains true under every nonsingular affine image. No symmetry of D or h, equality of segment lengths, balanced end heights, or independent choice of the centre is imposed.

The constant3/2 is sharp. Rectangular prisms attain it. Genuine three-piece profiles with two zero-height endpoints also approach it: over the square[-1,1]^2 choose middle heights1,1, middle interval[0,1], both outer lengths1/n and both end heights0. For the whole central x=1 facet and test(1,0,0), the exact quotient is15n/(10n+4), tending to3/2. Each finite member has true V/E/F=10/20/12; the prism limit changes incidence.

This result extends the prior zero-endpoint three-piece theorem, whose smaller proof and strict positive-definite genuine-three-piece gaps remain useful. It does NOT prove the arbitrary-concave-profile theorem, the universal3D whole-facet theorem, an S2/U2 exclusion, a full E17-incidence exclusion, or any new actual own110 attainer. The accepted minimum bracket34..622 is unchanged. The previous curved-completion control disproving fixed-centre affine-tail localization is also unchanged; no such localization is used here.

## 2. Actual-centre matrix reduction
Translate D so that its ACTUAL area centroid is0. Define

    V=int h^2, M=int z h^2, mu=M/V,
    E=int z^2 h^2, S=E-M^2/V, N4=int h^4.

Then Volume(P)=Area(D)V, g=(0,0,mu), and Sigma=diag((N4/V)Sigma_D,S/V). For a genuine maximal affine piece I write h_I(z)=A+Bz and D0=A+Bmu. Its supporting-line extension is positive at the interior centroid, so D0>0. Set

    P3=int_I h^3,
    Pz1=int_I h^2(z-mu),
    Pz2=int_I h(z-mu)^2.

For a WHOLE base edge e, let T_e and c_e be its actual centred second and first moments and alpha_D=distance(0,aff e) Length(e)/Area(D). Direct facet integration gives

    alpha_F T_F=(alpha_D D0/V)
       [[P3 T_e, Pz1 c_e], [Pz1 c_e^T, Pz2]].

The accepted arbitrary uniform-planar whole-edge theorem [internal-source-reference],13829B,SHA240b58ed6bde2703c5788573c8c20ca2a4278a3abc1cfc66fb8f607645eb646d, proves alpha_D T_e<=(3/2)Sigma_D and alpha_D<=2/3. Since T_e>=c_e c_e^T, it is sufficient to prove

    H=N4-D0P3>=0,
    R=(9/4)S-D0Pz2>=0,
    HR-D0^2 Pz1^2>=0.                         (GATE)

Indeed V[(3/2)Sigma-alpha_F T_F] is bounded below by alpha_D[[H T_e,-D0Pz1 c_e],[-D0Pz1 c_e^T,R]], which is positive semidefinite under GATE. The mixed term generally does not vanish and is explicitly retained. This actual mixed-profile reduction is also fully developed in the accepted two-piece material [internal-source-reference].

## 3. Two complete charts for all concave three-piece profiles
For three genuine positive-length pieces, affine normalization of z sends the inner knots to0 and1. Height scaling gives inner heights1,q>0. Reflection and rescaling permit q<=1; the case of an originally rising middle segment is recovered by that reflection, which also exchanges the outer lengths and end heights.

Write a,b>0 for the left and right lengths, ell>=0 for the left endpoint height and t>=0 for the right endpoint height. Concavity is EXACTLY

    (1-ell)/a >= q-1 >= (t-q)/b.

The second inequality and t>=0 imply q>=b/(b+1). Thus put

    q=(b+x)/(b+1), t=x y, 0<=x,y<=1.

The first inequality is0<=ell<=1+a(1-q). This entire interval is covered by two charts:

    bulged:   ell=l,                 0<=l<=1;
    monotone: ell=1+a(1-q)l,          0<=l<=1.

Together with a,b>0, these are two COMPLETE five-parameter domains. They are not a selected sample, equal-width slice or fixed-centre family. Their common boundary ell=1 is intentional. Reflecting back covers q>1 and right-monotone cases.

For polynomial arithmetic multiply ALL heights by the positive quantity b+1. This is a nonsingular horizontal affine scaling of the actual body. Define

    B=b+1, Q=b+x, T=(b+1)x y,
    L=(b+1)l                         in the bulged chart,
    L=(b+1)+a(1-x)l                 in the monotone chart.

The scaled profile is the affine interpolation through

    (-a,L), (0,B), (1,Q), (1+b,T).

All moment gates are homogeneous under this height scaling; their signs are unchanged.

## 4. Exact global polynomial certificate
For integers n,j>=0 define the polynomial

    F(n,j,H0,H1)=sum_{k=0}^n binom(n,k)
        (k+j)!(n-k)!/(n+j+1)! H0^(n-k) H1^k.

This is exactly int_0^1 u^j[(1-u)H0+uH1]^n du. For each of the three pieces let Pnj denote int z^j h^n. Their exact expressions are

    left:   (-1)^j a^(j+1) F(n,j,B,L);
    middle: F(n,j,B,Q);
    right:  b sum_{i=0}^j binom(j,i)b^i F(n,i,Q,T).

Sum P20,P21,P22,P40 over the pieces to obtain V,M,E,N4. No moment or centroid is supplied independently of the actual profile. For the selected piece i let s_i=(a,1,b)_i. Put Dn_i=s_i V D0_i. The three explicit numerators are

    a B V+(B-L)M;
    B V+(x-1)M;
    ((b+1)Q-T)V+(T-Q)M.

Using that piece's Pnj, set

    Hn=s_i V N4-Dn P30,
    Z1=V P21-M P20,
    Z2=V^2 P12-2VM P11+M^2 P10,
    Rn=(9/4)s_i V^2(VE-M^2)-Dn Z2,
    Detn=Hn Rn-Dn^2 Z1^2.

These are precisely

    Hn=s_i V H,
    Rn=s_i V^3 R,
    Detn=s_i^2 V^4(HR-D0^2 Pz1^2).

Every cleared factor s_i,V is strictly positive and all remaining rational denominators are positive factorial constants. Therefore polynomial nonnegativity of Hn,Rn,Detn proves GATE without a loss in the continuous domain.

For each chart, the source constructs these nine lateral polynomials and four cap polynomials from Section5. It groups every polynomial by the nonnegative integer powers a^i b^j. For each such block it fixes the maximum degrees in x,l,y BEFORE conversion and converts to the tensor Bernstein basis on the closed unit cube. The exact one-variable identity is b_k=sum_{j<=k} c_j binom(k,j)/binom(n,j). It is applied independently to all three axes. The source asserts that the final coefficient dictionary is the complete rectangular tensor index set for the block. No coefficients are dropped or sampled.

All tensor Bernstein basis functions are nonnegative on[0,1]^3 and all a^i b^j are positive for a,b>0. Every regenerated control is nonnegative. Hence each gate polynomial is globally nonnegative on its ENTIRE chart.

There are26 certificates and1245442 exact rational controls:199221 zero,1046221 strictly positive,NONE negative. Detailed counts, written as total(zero), are:

    bulged left H2723(374),R11357(1208),Det167040(14603);
    bulged middle H1460(2),R9720(252),Det99522(2200);
    bulged right H3320(1136),R15498(3910),Det170669(18282);
    bulged caps Lt868(0),Ln3894(0),Rt1593(374),Rn9881(4004).

    monotone left H3614(946),R23256(4460),Det309328(57800);
    monotone middle H1829(309),R15369(2139),Det171968(25690);
    monotone right H3212(908),R21553(6072),Det172948(49490);
    monotone caps Lt1038(154),Ln2732(466),Rt3429(0),Rn17621(4442).

The bulged chart has497545 controls with46345 zero; the monotone chart has747897 controls with152876 zero. This is a GLOBAL exact sign certificate, not floating optimization, finite parameter sampling or proof-assistant formalization. The complete literal deterministic source is the exact representation of the full coefficient data.

## 5. Endcaps and actual facet mergers
At a left endpoint of nonzero height L, let Z=M+aV=V(mu+a)>0. At a right endpoint of nonzero height T use Z=(1+b)V-M>0. Let h_e denote L or T respectively. Since D was centred at its actual area centroid, the cap's mixed moment is0. Its two necessary scalar block inequalities are exactly the signs of

    (3/2)V N4-Z h_e^4,
    (3/2)V^2(VE-M^2)-Z^3 h_e^2.

These are the four cap polynomials included above. If h_e=0 the endpoint is an apex, not a two-dimensional cap; the construction creates no ghost facet there.

At equal adjacent slopes, the corresponding lateral pieces are coplanar and form ONE maximal facet. One must NOT add inequalities for artificial fragments. Delete the redundant profile knot and use the accepted theorem for EVERY WHOLE facet of every nonnegative concave TWO-affine-piece profile, [internal-source-reference],18894B,SHA9db28182e955108523e5d157a00e1660c4e415c68ed4aec4e12d92922ba4cd4a. It covers all nonnegative endpoint heights and its own endcaps. Its further affine/prism/pyramid degenerations are already included there. This gives the correct whole-facet interpretation on all chart boundaries. Profiles with fewer pieces are covered directly by that predecessor.

The old two-piece executable requires the helper [internal-source-reference],12673B,SHAfd43cd9771d265d3942b4839175ed54dedef7ab3180f0dc8443ebacc089f6c26. This new executable includes ALL needed integration, hull and physical-census routines literally; that helper is NOT a computational dependency of the new source. The planar and merged-facet theorems remain explicitly stated analytical inputs, not secretly independently reverified claims.

## 6. Ten actual geometric controls
The source builds and independently integrates actual rational polyhedra, with full maximal-support tests, true edge incidences, uniform volume centroid and covariance, every WHOLE facet moment, pole identities and every principal minor of the full3/2 matrix gap. The exact true-edge physical packets are evaluated with the same actual centre. Triangulation fans are used only for integration; their diagonals never become physical edges. Redundant collinear profile levels are removed before constructing faces.

Raw bases are square(-1,-1),(1,-1),(1,1),(-1,1); pentagon(0,0),(3,0),(4,1),(2,3),(-1,2); triangle(0,0),(3,0),(1,2). Each is translated by its ACTUAL area centroid. Parameter order is(a,b,left height,q,right height), with middle heights1,q:

    square bulged positive caps(2,3,1/3,4/5,1/10):16/28/14,own S6 U12 H16,weak000;
    pentagon monotone left(2,1,5/4,3/4,1/4):20/35/17,own S8 U12 H18,weak000;
    triangle rising middle(1,2,1/4,3/2,2):12/21/11,own S5 U7 H10,weak000;
    triangle left apex(2,1,0,2/3,1/6):10/18/10,own S7 U8 H13,weak000;
    square two apices(2,3,0,1,0):10/20/12,own S8 U10 H16,weak000;
    square left merge(2,1,3/2,3/4,1/4):12/20/10,own S6 U8 H12,weak000;
    square right merge(2,1,1/3,3/4,1/2):12/20/10,own S10 U12 H20,weak000;
    square double merge(2,1,3/2,3/4,1/2):8/12/6,own S6 U8 H12,weak000;
    square prism merge(2,3,1,1,1):8/12/6,own S6 U8 H12,weak000.

A tenth actual control is the nonorthogonal affine image of the pentagon monotone body, using

    A=[[1,1/5,1/7],[0,1,1/6],[0,0,1]], translation(2,-3,1).

Its whole hull, centre, covariance and native physical census are recomputed. It has20/35/17,own S6 U12 H16,weak000. The native Euclidean census changes, as expected; only the matrix inequality is asserted affine-covariant, not the equilibrium count. None of these controls is110 and none replaces the canonical C622 construction.

## 7. Reproduction and observed evidence level
The complete source is part2 [internal-source-reference]. Save exactly as

    three_piece_all_whole_facets.py,15953B,
    SHA256331b7473f4840cff16f05dc335f5661fefb9ada6830b3c32d4dc16f88dbd885c.

Use CPython3.13.5,SymPy1.14.0,assertions enabled. No external inputs, computational helpers, seed or precision parameters are needed. Reconstruction and verification command:

    python -B -u three_piece_all_whole_facets.py > three_piece_all_whole_facets.log

Expected outputs:

    three_piece_all_bernstein_controls.jsonl,23623764B,
    SHA2562785b318da36d4943d60edb7982a6e15378c9c7c0ff20756ddf9d729cf1076eb;
    three_piece_all_whole_facets_report.json,896366B,
    SHA25656f3470b7afb6e0a0ee4e2a8fb2f4f3ec50d347100e0a1c8f9ad70877ec31e7b;
    three_piece_all_whole_facets.log,1731B,
    SHA256a1468f171c0b8fd1f553c96925aa810bb7e4466da773b038e9e4268fe8a36b3d.

The coefficient JSONL contains ALL literal regenerated rational controls, grouped by chart, piece, gate, positive-power monomial and complete tensor degree. The report contains the exact certificate metadata and every actual coordinate, facet, edge, centre, covariance, facet moment, minor and physical primitive of the controls.

Terminal markers:

    EXACT_ALL_THREE_PIECE_PROFILE_CHARTS_PASS 26 1245442 199221
    ALL_THREE_PIECE_HOMOTHETIC_PROFILES_WHOLE_FACET_EXACT_PASS

Both normal and fresh SOURCE-ONLY executions were observed completing successfully, with byte-identical source and all three outputs. No mathematical assertion failed. This is a proof based on exact rational global polynomial positivity plus actual geometric controls and explicitly named analytical predecessor theorems. It does not by itself enlarge the class from three affine pieces to arbitrary concave profiles.
