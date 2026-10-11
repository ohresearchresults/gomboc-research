# minimum-0248

Historical AI scientific report · saved 2026-09-26 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# H5_MACRO_FULL_TRIANGLE_ALLROOT_ENERGY_ATLAS_V1

## Result: the full macro prism is closed

For the unchanged actual uniformly filled H5 family, define

    Γ = {15/16<=x<=1, 1/4<=r<=1/2, 0<=lambda<=1/16,
         p>=0, q>=0, p+q<=1}.

**Every one of the 48,790 labelled complete rooted primal trees is impossible under every common nonzero PSD metric at every parameter point of Γ.** On the genuine subset—x<1, p,q>0, p+q<1 and lambda>0—every physical SPD metric therefore has **at least two strict unstable vertices**, including when other weak contacts occur.

This closes the requested **p+q>1/2 residual on the whole macro x/r box**. It also independently closes the lower half at lambda<=1/16, rather than inheriting the older half-triangle theorem only at lambda<=1/64. The earlier norm-coupling cover had 26,689 trees on this same genuine macro domain; the new result covers the entire 48,790-tree universe directly, not by adding partially overlapping counts. The earlier half-triangle and coupled-norm scopes are recorded in the supplied notebook. fileciteturn26file0L31-L35 fileciteturn26file0L65-L71

The exact atlas has **1,456 integer stresses, 1,264 distinct supports, 27 closed triangular parameter cells, and 8,267 stress/cell applications**. Its acceptance checks **6,613,600 shifted positive-definite coefficient matrices and 19,840,800 positive leading minors**. Every cell covers all 4,879 trees at each of the ten roots. There are no unexcluded tree alternatives inside Γ.

This is not an all-shape H5 or whole-E17 exclusion. The inherited all-x/r five-arrow caps remain useful outside Γ; they are not globally superseded by this macro-box theorem. The reflected macro box also closes by the unchanged physical reflection, but its count is not added to this one. No global complexity bound, canonical graph-orbit count, or attaining construction changes: the accepted interval remains **34<=C_min<=622**. fileciteturn20file0L9-L11

## 1. Reading, source identity, and route

The complete new journal was read consecutively through line 1692/EOF, including the entire literal parent **minimum-0247**, SHA256 **f31e0f04d48f1b80f427df0b3ac4342cd2b61e84f1edaaf280330521e356cce1**. The journal's verified identity is 326191 bytes, SHA256 **223670530111c1f5a3b7096a55d851bf5f0ca22a3f78a9299a94ef5603fe2bfd**. Earlier unchanged sources remain available in this chat; no required dependency was missing or silently replaced.

The parent source **h5_path_energy_cap.py**, 19488 bytes, SHA256 **c594ce7bfcba34b06dc6bfe290d8939edc80dd6a11d3cbdb9b68509968ca8c09**, was retained without changing its labels or moment formulas. The path-energy source identity is the corrected **6dc7106cabaa16510d7f067ac60cff45a53c08dd55482a97025aa011b8ad4866**, not the obsolete alternate hash. fileciteturn26file0L89-L107

The substantive change was to allow **coupled original-arrow stresses on different basal routes**, instead of requiring one source component's fixed residual fit to certify itself. I searched for common nonnegative weights on the original polynomial coefficient matrices, rationalized them, and independently checked all resulting integer certificates. The only parameter subdivision in the final atlas is in the physical p/q triangle: **x, r and lambda retain their full displayed intervals in every cell**. No quadratic lowering, frozen centroid, spectral cap, or independent polar metric is used.

## 2. Literal body and actual moving moments

Put s=1−lambda. In cyclic order,

    B0=(1/4,0), B1=(1−3x/4,0), B2=(1−p,p), B3=(q,1−q),
    B4=(0,1−3r/4), B5=(0,1/4), B6=(1/16,1/16).

The ten vertices are z_i=(s B_i,0), i=0,...,6, and

    z7=(0,0,1), z8=(lambda,0,1), z9=(0,lambda,1).

The true maximal-face cycles are exactly

    (6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8),
    (9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).

Use the oriented fan

    (0,1,2,8), (0,9,8,2), (0,9,2,3), (0,9,3,4),
    (0,4,5,7), (0,4,7,9), (0,6,7,5), (0,7,8,9).

With

    A=(31−24xp−24rq)/64,
    bx=509/3072−3xp/8+3x²p/32+xp²/8−rq²/8,
    by=509/3072−3rq/8+3r²q/32+rq²/8−xp²/8,

the actual volume and first moments are

    V=A s²/3+lambda/6,
    Jx=s³bx/4+s²lambda(1−3xp/4)/24+lambda²/24,
    Jy=s³by/4+s²lambda(1−3rq/4)/24+lambda²/24,
    Jz=A s²/12+lambda/12+lambda²/24.

Always set **g=J/V**. These are the unchanged parent moments, not freely selected masses or a basal-centroid approximation. fileciteturn27file0L29-L57

The new verifier checks all four fan identities as full five-variable polynomial identities, all 34 physical/parameter reflection identities, and all 34 zero incidences. The 56 nonincident support inequalities have 36,048 positive and 8,752 zero Bernstein coefficients, minimum positive coefficient **1/1536**. Positive coefficients occur on every relevant included macro boundary face, proving strict nonincidence for the entire genuine domain, not only at a sample.

The elementary bounds 7/64<=A<=31/64 imply **7/192<=V<=1/6**. Thus all indexed endpoints used in the polynomial proof retain a well-defined actual centroid. At x=1, lambda=0, or physical triangle boundaries, labels or features may collapse; the coefficient theorem includes these limits, but the statement that the body has ten true vertices, seventeen true edges and nine true facets is restricted to the genuine subset.

## 3. Retained edge energy and the uniform matrix certificate

Write u_i=z_i−g, Δ_ij=z_j−z_i, and

    H_ij=sym(u_i,Δ_ij),       D_ij=tr(M H_ij).

For a nonnegative integer row w with W=sum w_ij>0, define

    P_w=−sum w_ij sym(V z_i−J,z_j−z_i)=V C_w,
    C_w=−sum w_ij H_ij.

The crucial acceptance statement is

    P_w/W > 2^−30 I                                             (1)

throughout its assigned closed parameter cell. The weights do not depend on the physical metric.

The full degree is **(3 in x, 3 in r, total 3 in p/q, 4 in lambda)**. Each application therefore has 4×4×10×5=**800 symmetric 3×3 Bernstein coefficient matrices**. Every coefficient of P_w−W 2^−30 I is proved PD by its three exact leading principal minors. The source uses arbitrary-size integers after clearing denominators and reconstructs the full original power coefficients by the inverse Bernstein transform. It neither samples a parameter grid nor interprets a coefficient-space dual as a physical body.

Since Bernstein basis functions are nonnegative and sum to one, those 800 tests imply (1) at every point of the closed cell. Consequently, for every nonzero PSD M,

    sum w_ij D_ij/W
       = −tr(M P_w)/(V W)
       < −tr(M)/(2^30 V)
       <= −3 tr(M)/2^29.                                      (2)

Thus a complete tree containing the row's positive support cannot have all selected arrows weakly nonnegative. Strict matrix positivity removes the need for a singular-kernel qualification in this atlas.

### What is being coupled

For each actual edge the exact identity is

    −2H_ij = u_i u_iᵀ − u_j u_jᵀ + Δ_ij Δ_ijᵀ.

The verifier checks all 204 scalar entries of these 34 identities after clearing the true centroid denominator. The final positive stresses retain the edge-energy terms; they are not only norm-order obligations.

Among the 1,456 rows, **198 supports are connected and 1,258 are disconnected**, counting nonisolated components of the positive-edge support. Their component histogram is

    1 component:198; 2 components:826; 3 components:407; 4 components:25.

Their support-size histogram is

    3 arrows:273; 4:608; 5:404; 6:150; 7:19; 8:2.

All 34 literal directed edge directions occur. There are 6,320 positive integer weight terms; the largest individual weight is **146** and the largest row sum is **512**.

This coupling is within the original negative-arrow cone. In the supplied path formula one may take v=0, mu concentrated at the source, and eta equal to an arrow's weight, obtaining the elementary matrix −eta H_ab; nonnegative sums give the rows used here. Individual elementary matrices need not be PD. **I do not claim 1,456 successful individual G−rrᵀ fits**, nor a stronger SDP relaxation. The new result is the exact common-metric positivity and complete coverage of their coupled sums. This is consistent with the path source's coupling scope. fileciteturn20file1L29-L57 fileciteturn20file1L98-L104

## 4. Complete closed parameter cover and labelled-tree census

Begin with these three counterclockwise triangles:

    T0=((1/2,0),(1,0),(0,1)),
    T1=((1/2,0),(0,1),(0,1/2)),
    T2=((0,0),(1/2,0),(0,1/2)).

T0 and T1 cover p+q>=1/2; T2 is the lower half. For a triangle (a,b,c), with edge midpoints ab,bc,ca, child digits 0,1,2,3 mean respectively

    (a,ab,ca), (ab,b,bc), (ca,bc,c), (ab,bc,ca).

The first path digit selects T0,T1,T2. The complete leaf list, with numbers of stress applications, is

    000:291, 001:303, 002:285, 003:299,
    010:353, 0110:390, 0111:430, 0112:347, 0113:421,
    012:309, 0130:340, 0131:321, 0132:258, 0133:292,
    020:266, 021:283, 022:275, 023:278,
    030:292, 031:283, 032:253, 033:262,
    10:323, 11:275, 12:259, 13:258, 2:321.

The source verifies the full prefix-tree partition: every subdivided node has all four children, no leaf contains another, all triangles have positive oriented area, and the total area is 1/2. There are **26 upper-half leaves and one lower-half leaf**. Their common x/r/lambda box is unchanged. Overlap along closed boundaries is harmless because every applicable certificate is valid there.

For the actual graph, enumerate all nine-edge subsets of the seventeen true undirected edges, keep the 4,879 connected subsets, and orient each toward each of its ten roots. The resulting **48,790 different nine-arrow masks** have root counts

    (4879,4879,4879,4879,4879,4879,4879,4879,4879,4879).

Every positive stress support is literally contained in at least one enumerated tree. For each leaf, the union of the masks containing its assigned supports equals the entire tree catalogue. This checks **1,317,330 tree/leaf alternatives**. It does not guess source-component extensions or add coverage from different parameter domains.

The checkpoint stores all 1,456 complete integer rows in the declared directed-edge order and every leaf's exact row IDs. The verifier regenerates every full tree and performs the support unions. It also independently recovers the parent's 208 five-arrow extensions, root counts

    (0,0,88,45,23,0,0,0,28,24),

and the twenty older seven-arrow extensions. These are comparisons on the appropriate intersections: the parent cap p>=9/16 and the older lambda<=1/64 prism. They are **not** extra counts added to 48,790. The parent's larger all-x/r cap scope remains distinct. fileciteturn28file0L15-L39

Finally, under SPD M, every weak selected true-edge arrow strictly increases uᵀMu, because the edge increment has positive squared M-length. If there were only one strict unstable vertex, choosing a nonnegative incident escape at each other vertex would give an acyclic complete tree ending at that vertex. The all-tree certificate contradicts this. It follows that U>=2 without assuming that other contacts are nonweak.

The physical reflection (x,r,p,q)->(r,x,q,p), with label permutation

    (5,4,3,2,1,0,6,7,9,8),

gives the same all-root theorem on **x in[1/4,1/2], r in[15/16,1]**, the full p/q triangle, and lambda<=1/16. This is a reflected domain, not 97,580 alternatives on one body.

## 5. A different support and a genuine actual-refill negative control

An illustrative row, ID185, is

    11 D06 + 9 D23 + 8 D54 + 4 D82,       W=32.

It shares **no directed arrow** with the parent's five-arrow support. Its three nonisolated components are {0,6}, {2,3,8}, and {4,5}. It is certified on leaf000, whose triangle is

    ((1/2,0),(5/8,0),(3/8,1/4)),

with the full macro x/r/lambda ranges. It is a coupled four-arrow obstruction, not a small adjustment of the earlier cap threshold.

The same row provides a useful negative control against transporting fixed stresses after refill. Use the **same physical SPD metric in both bodies**,

    v=(2,−1,1),  M=v vᵀ+I/10000,  N=M^−1.

Its condition number is 60001. At the genuine home point

    (x,r,p,q,lambda)=(31/32,3/8,1/2,1/12,1/32),
    V=151381/1572864,
    g=(360746071/2480226304,
       95582397/310028288,
       159829/605524),

the actual strict census is **(S,U,H)=(5,2,5), weak000**, and the weighted mean is exactly

    −48415801031067971/406360277647360000 < −1/10.

At the distinct genuine point, still inside Γ,

    (x,r,p,q,lambda)=(31/32,3/8,1/8,3/4,1/32),
    V=689131/6291456,
    g=(2620950215/11290722304,
       144972407/705670144,
       722923/2756524),

the own-centred strict census is **(3,2,3), weak000**, and the SAME weighted mean is

    35175600080224531/1849871942287360000 > 19/1000.

The code reconstructs both complete bodies, eight positive fan volumes per body, exact centroid, M and its same-origin inverse, every pole, and all **136 nonzero primal/polar true-edge primitives**. Neither is an actual complete-tree survivor: the second body is excluded by other atlas rows. What fails is the unrestricted reuse of this particular stress outside its certified parameter cell. The partition is not justified solely by numerical locator failures.

## 6. Evidence boundary, reproduction, and pins

The accepted certificate is a **literal rational checkpoint plus an exact verifier**. Numerical common-weight/eigenvector-cut searches and coarse integer rounding supplied candidates; only the full integer/Fraction checks and complete support unions above are acceptance evidence. No unsuccessful LP, untested library gap, or coefficient dual is presented as physical feasibility. The recovery reproduces the fixed rational proof, not a claim that a fresh floating search on another stack chooses identical rows.

The exact verifier uses **Python>=3.11, standard library only, assertions enabled**; CPython3.13.5 was observed. The discovery environment used NumPy2.3.5 and SciPy1.17.0, but neither is a recovery dependency. All triangle coordinates, supports, weights, moment formulas, transforms and checks are included in the capsule below. No old workspace, parent output, network request, or external archive is required.

Normal exact execution and clean reconstruction runs passed. A cold directory containing **only the recovery capsule** reconstructed the readable verifier and complete exact checkpoint and reproduced the checkpoint/report byte-for-byte. This is executed exact arithmetic plus the proof above, not proof-assistant formalization or independent-author peer review.

Save the complete section7 capsule as **recover_h5_macro_allroot.py** and run

    python -B -S recover_h5_macro_allroot.py output

It creates **h5_macro_allroot_verify.py** and **h5_macro_atlas_checkpoint.json** in the current directory, checks both identities, and executes the proof. A subsequent direct check is

    python -B -S h5_macro_allroot_verify.py output

with that exact companion checkpoint beside the verifier. All nondefault domain, degree, gap and enumeration parameters are fixed in the recovered source.

Final pins:

    recover_h5_macro_allroot.py — 29568 bytes
    SHA256 20d2e91ae4dc8a4d33f4eaf2358221945185e9e41a8905fd2bb7c18d51f67cfb
    h5_macro_allroot_verify.py — 22505 bytes
    SHA256 632ddc6e2c95385f04f2c4a6afbc8f374b5a71bf909d5cb06713d801ea034b10
    h5_macro_atlas_checkpoint.json — 80669 bytes
    SHA256 baf01cca35d6ed92ab6e4cf24fc89732fd137c3dfc3bf6a8da3e011a3899fbd0
    h5_macro_allroot_report.json — 60560 bytes
    SHA256 e2f35b29f486ed98b3d39e38577495a75277960474daac3bb616290bec04889c
    direct verifier stdout — 1658 bytes
    SHA256 738d6d1c8572e770c66020f06f9e359a3f7000695e0392a9242917b160ab0d38
    capsule-only cold stdout — 1709 bytes
    SHA256 7d056dc8ef721b5e8e3f2b73b4a90ae1df55cfc84e903660f0dfb9e6292d012f

The tree stream SHA256 is **72e12d24ceaf3c70e6a673ecd46f0a355500c9bd1f0823356a78d8d6330800d2**. The leaf/application coverage stream SHA256 is **668296f09c99e04153c7a3be27fe84da45dd02ec9c9068c54ae09ee7c9ac0a0c**. The report also contains each leaf's full row-ID list, exact triangle, common coefficient denominator, coefficient-basis hash and positive normalized shifted-minor minima. The multi-million-matrix proof is regenerated rather than supplied as a hash-only missing object.

Expected principal terminal markers, in addition to one PASS per leaf:

    H5_MACRO_CAPSULE_RECOVERY_PASS 1456 27 22505 80669
    H5_MACRO_ACTUAL_FAN_REFLECTION_FIDELITY_PASS 4 34 34 56 36048 8752
    H5_MACRO_FULL_TRIANGLE_ALLROOT_PASS 1456 1264 27 8267 6613600 19840800 48790
    H5_RETAINED_EDGE_ENERGY_COUPLING_PASS 204 1258 34
    H5_ACTUAL_REFILL_STRESS_REVERSAL_PASS 2 136
    H5_MACRO_ALLROOT_RECOVERY_PASS

**Continuation:** the full original macro prism, including p+q>1/2 and the expanded lambda<=1/16 band, should no longer be treated as a surviving-tree search region. The useful next geometry lies outside this prism/reflection and outside the other inherited closed domains. Reevaluate these small integer rows with the new body's actual moments; the exact refill control shows why mere transport is invalid. No assertion is made here about all remaining x/r values, larger lambda, nonparallel/projective H5 moduli, or the global minimum.

## 7. Complete lossless recovery capsule

This is the entire capsule. Its payload includes the readable verifier and every integer of the exact checkpoint. The decoder reconstructs and hashes both files before executing the proof.


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


Supplementary copies: [complete recovery capsule](sandbox:/mnt/data/recover_h5_macro_allroot.py), [readable verifier](sandbox:/mnt/data/h5_macro_allroot_verify.py), [literal exact checkpoint](sandbox:/mnt/data/h5-macro-output/h5_macro_atlas_checkpoint.json), and [exact report](sandbox:/mnt/data/h5-macro-output/h5_macro_allroot_report.json). The embedded capsule already reconstructs every proof input and computation without these downloads.
