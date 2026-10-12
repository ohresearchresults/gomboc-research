# minimum-0249

AI research report · 2026-09-26 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
>
> The report limits its exclusion claim to the displayed H5 macro box and explicitly leaves the general E=17 case open.
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# H5_MACRO_ALL_TAPER_FULL_TRIANGLE_U2_V1

## Result: the entire physical taper interval is closed on the macro box

For the unchanged uniformly filled H5 family, put

    Ω = {15/16<=x<=1, 1/4<=r<=1/2,
         p>=0, q>=0, p+q<=1, 0<=lambda<=1}.

**Every one of the 48,790 complete labelled rooted primal trees is excluded throughout Ω for every common nonzero PSD metric, using the body's actual volume centroid.** On the genuine subset

    x<1, p>0, q>0, p+q<1, 0<lambda<1,

there are therefore **at least two strict unstable vertices for every physical SPD metric**, including when other weak contacts occur. There is no remaining taper gap on this macro box.

The earlier parent closed only lambda<=1/16. Its literal identity remains **minimum-0248**, SHA256 **b2e860c49dd2d48909fe2a2be1b6d0e5ca2bd1ef23a5e535b74da345b7798c63**. Its 1,456 integer rows are retained unchanged; the successor adds 4,243 accepted rows and the remaining taper slabs. This is a parameter-domain extension, not an addition of disjoint tree counts.

A further exact geometric control shows why some old supports genuinely stop working: the three arrows **1->2, 2->3, 9->4**, excluded by an old small-taper stress, are simultaneously **strictly positive under one explicit physical SPD metric on a genuine five-dimensional prism around lambda=1/2**. Consequently no nonnegative stress supported only on those three arrows can exclude that prism. The complete-tree atlas succeeds by using additional arrows, not by pretending that the old partial obstruction persists.

This closes neither all basal H5 moduli nor all E17 bodies. It supplies no attaining body and does not change **34<=C_min<=622**. The all-root theorem is uncapped: it does not assume S=1, covariance conditioning, an independently selected polar metric, or absence of weak contacts.

## 1. Input and evidence status

The entire new 1,579-line journal was read consecutively through EOF, including the complete literal parent and its recovery capsule. Its manifested and verified identity is **345295 bytes**, SHA256 **56eb2a1ec2afbbfe065edff2634892571abc75a7af2c3da89165d5b8887f8416**. The complete readable parent verifier was also available and read; its unchanged identity is **22505 bytes**, SHA256 **632ddc6e2c95385f04f2c4a6afbc8f374b5a71bf909d5cb06713d801ea034b10**. No required dependency was unavailable or replaced by a guessed source.

The new accepted object is a literal integer checkpoint plus an exact standalone verifier. Floating common-weight searches supplied candidates; the mathematical acceptance consists entirely of original-polynomial reconstruction, exact positive-definiteness tests, complete parameter partitions and exhaustive support coverage. No fitted-stress failure is used as evidence of a feasible complete tree.

## 2. Unchanged actual geometry and centroid

Let s=1−lambda and

    B0=(1/4,0), B1=(1−3x/4,0), B2=(1−p,p), B3=(q,1−q),
    B4=(0,1−3r/4), B5=(0,1/4), B6=(1/16,1/16).

Set z_i=(s B_i,0), i=0,...,6, and

    z7=(0,0,1), z8=(lambda,0,1), z9=(0,lambda,1).

The literal maximal-face cycles and oriented fan remain

    FACES=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
           (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9));

    FAN=((0,1,2,8),(0,9,8,2),(0,9,2,3),(0,9,3,4),
         (0,4,5,7),(0,4,7,9),(0,6,7,5),(0,7,8,9)).

Use the actual moments

    A=(31−24xp−24rq)/64,
    bx=509/3072−3xp/8+3x²p/32+xp²/8−rq²/8,
    by=509/3072−3rq/8+3r²q/32+rq²/8−xp²/8,
    V=A s²/3+lambda/6,
    Jx=s³bx/4+s²lambda(1−3xp/4)/24+lambda²/24,
    Jy=s³by/4+s²lambda(1−3rq/4)/24+lambda²/24,
    Jz=A s²/12+lambda/12+lambda²/24,
    g=(Jx,Jy,Jz)/V.

These are the parent's homogeneous-volume formulas, not transported or freely fitted centroid data.

The new source checks the four fan identities, 34 reflection identities and 204 cleared edge-energy identity entries symbolically. On the full taper interval, its exact support check has **25,056 positive and 19,744 zero Bernstein coefficients**, minimum positive coefficient **1/6144**. All 34 specified incidences vanish identically, and all 56 nonincidences are strictly positive on every relevant genuine macro boundary stratum. Intrinsic degeneracies are not called genuine ten-vertex bodies.

In particular, 7/64<=A<=31/64 gives

    7/192 <= V <= 1/6

on the entire closed parameter domain. The upper bound follows from convexity in lambda and endpoint values; the lower comparison 7(1−lambda)²/192+lambda/6 is increasing. Thus the centroid is defined at all indexed limits. Lambda=0 merges top labels; lambda=1 collapses the seven basal labels to the tetrahedral endpoint. The proof includes their indexed arrow systems, without asserting that those endpoints have the genuine 10/17/9 incidence.

The extension crosses the old height hypothesis, not merely its certified numerical margin. Indeed

    V/2−Jz=(2A(1−lambda)²−lambda²)/24,

so **g_z>1/2 for every lambda>=1/2** because 2A<=31/32<1. The high-taper slabs therefore cannot be justified by silently retaining the earlier basal-reflection premise t=2g_z<1; their original-arrow matrix certificates are independent of that premise.

There is also an all-positive-ratio interpretation. For 0<lambda<1, multiplying both horizontal coordinates by 1/(1−lambda) makes the basal vertices B_i fixed and the top triangle have size rho=lambda/(1−lambda). This is an affine transformation, so uniform centring is preserved and its metric is absorbed into the arbitrary common SPD matrix. The theorem therefore covers **every rho>0** on the stated basal macro box.

## 3. Exact original-arrow certificate on all six taper slabs

Write

    u_i=z_i−g, e_ij=z_j−z_i,
    H_ij=sym(u_i,e_ij), D_ij=tr(M H_ij).

For a nonnegative integer row w and W=sum w>0 define

    P_w=−sum w_ij sym(Vz_i−J,e_ij),
    C_w=P_w/V=−sum w_ij H_ij.

Every assigned stress/cell pair satisfies

    P_w − W*2^−30 I > 0.                                  (1)

For every nonzero PSD M this implies

    sum w_ij D_ij/W
        < −tr(M)/(2^30 V)
        <= −3 tr(M)/2^29.                                 (2)

Hence all positively weighted arrows of that support cannot be weakly nonnegative under one common metric. Strict PD of the certificate covers singular nonzero PSD metrics without a separate kernel exception.

The polynomials retain degrees **(3 in x, 3 in r, total 3 in p/q, 4 in lambda)**. Each application has **800** symmetric coefficient matrices. The verifier reconstructs the full power coefficients, restricts them exactly to the chosen triangle and taper interval, and checks all three leading principal minors of every shifted coefficient matrix with arbitrary-size integers. The restriction matrices themselves have nonnegative entries and unit row sums. No term is lowered or discarded.

The information retained by these stresses includes the exact identity

    −2H_ij = u_i u_iᵀ − u_j u_jᵀ + e_ij e_ijᵀ.

Thus the certificate keeps edge energies rather than using only norm-order implications. These are coupled stresses in the original negative-arrow cone, not a stronger relaxation or a claim that every individual source-cut Schur test succeeds. This agrees with the coupling scope of the supplied path-energy mechanism.

### Complete parameter cover

Every cell retains the full x interval [15/16,1] and r interval [1/4,1/2]. Only lambda and the physical p/q triangle are partitioned:

| Closed lambda interval | Triangular cells | Stress applications |
|---|---:|---:|
| [0,1/16] | 27 | 8,267 |
| [1/16,1/8] | 27 | 9,053 |
| [1/8,1/4] | 27 | 10,909 |
| [1/4,1/2] | 12 | 6,785 |
| [1/2,3/4] | 3 | 1,520 |
| [3/4,1] | 3 | 1,355 |
| **Total** | **99** | **37,889** |

The last five slabs are new. The first slab preserves the previous theorem inside the self-contained combined certificate. Partition knots are certificate choices, not asserted mechanical or incidence-transition values.

Start with

    T0=((1/2,0),(1,0),(0,1)),
    T1=((1/2,0),(0,1),(0,1/2)),
    T2=((0,0),(1/2,0),(0,1/2)).

For (a,b,c), put ab=(a+b)/2, bc=(b+c)/2, ca=(c+a)/2. Child digits 0,1,2,3 mean

    (a,ab,ca), (ab,b,bc), (ca,bc,c), (ab,bc,ca).

The first digit selects T0,T1,T2. For each of the first three slabs, the complete 27-path partition is

    000,001,002,003,010,0110,0111,0112,0113,012,
    0130,0131,0132,0133,020,021,022,023,030,031,032,033,
    10,11,12,13,2.

For [1/4,1/2] the paths are

    00,010,011,012,013,02,03,10,11,12,13,2.

For each of the last two slabs they are simply 0,1,2. The verifier proves the full prefix partitions, positive areas and total area 1/2 separately on every slab. Adjacent closed slabs overlap harmlessly at their endpoints.

### Exact support coverage

The checkpoint contains **5,699 distinct integer rows and 4,788 distinct positive supports**, with **27,256 positive weight terms**. All 34 directed true-edge directions occur; the maximum individual weight is **308**, and the maximum total row weight is **512**. Support sizes are

    3:552, 4:1712, 5:2094, 6:1119, 7:208, 8:14.

The numbers of rows having 1,2,3,4,5 nonisolated support components are

    1281,2843,1430,143,2.

Every row is used in at least one certified cell. These figures describe proof supports, not canonical polyhedron orbits.

The verifier independently generates all nine-edge connected subsets of the seventeen literal true edges, obtaining **4,879 unrooted spanning trees**. Orienting each toward all ten roots gives **48,790 distinct complete nine-arrow trees**, exactly 4,879 per root. A row excludes only trees literally containing its positive support. The support unions equal this entire catalogue in **each** of the 99 cells, checking **4,830,210 tree/cell alternatives**.

The combined exact positivity count is **30,311,200 shifted PD coefficient matrices / 90,933,600 positive leading minors**. No count is added across different physical domains to manufacture an all-root conclusion.

For a genuine body and SPD M, a weak arrow between distinct true neighbours strictly increases uᵀMu. If there were a sole strict U, choose a nonnegative incident escape at every other vertex. Strict norm growth gives an acyclic complete tree ending at that U, contradicting the certificate. This proves U>=2 even with other weak contacts.

The unchanged reflection (x,r,p,q)->(r,x,q,p), with label permutation (5,4,3,2,1,0,6,7,9,8), gives the same all-taper theorem on the reflected macro box. This is coverage of a different shape domain, not twice as many alternatives at one body.

## 4. A genuine change in the old three-arrow obstruction

The retained old row428 is

    22 D12 + 36 D23 + 7 D94, W=65.                          (3)

It is certified on small-taper cell000 and excludes those three simultaneous weak arrows there, independently of the other six tree arrows.

### Fixed-weight failure under actual taper motion

Keep (x,r,p,q)=(31/32,3/8,1/2,1/12) fixed and use the SAME physical metric

    M1=v vᵀ+I/10000, v=(1,−5,3), N1=M1^−1.

Its condition number is 350001. At lambda=1/32,

    V=151381/1572864,
    g=(360746071/2480226304,95582397/310028288,159829/605524),

and the weighted mean in (3) is

    −3988828137876188339/3301677255884800000 < −1.

The complete actual strict census is (S,U,H)=(4,2,4), weak000.

At lambda=1/4,

    V=2365/24576,
    g=(125335/968704,135409/605440,729/1892),

but that same weighted mean is

    153354993071097/161192345600000 > 9/10.

The complete census is (3,2,3), weak000. All 136 primal/polar primitives across these controls are nonzero and recomputed at their own centroids. This is exact loss of the fixed stress, not yet a claim that its entire three-arrow subsystem is feasible at lambda=1/4.

### Entire three-arrow cone failure on a genuine high-taper prism

The stronger control uses ONE fixed rational SPD matrix

    M2=(1/10000)*((469,−1795,1114),
                  (−1795,6882,−4270),
                  (1114,−4270,2650)),
    N2=M2^−1.

Its leading principal minors are

    469/10000, 5633/100000000, 1539/500000000000.

On the whole genuine prism

    x in[61/64,63/64], r in[23/64,25/64],
    lambda in[31/64,33/64],
    (p,q) in conv{(31/64,13/192),(17/32,13/192),(31/64,11/96)},

the SAME metric satisfies

    D12>1/64, D23>1/64, D94>1/64.                           (4)

The source proves (4) by expanding the three actual cleared polynomials V*D_ij−V/64. All **2,400 scalar Bernstein coefficients** are positive; their minimum is

    462116329632079451/4323455642275676160000.

The basal subprism lies strictly inside old cell000. Consequently the same basal family changes from an excluded three-arrow subsystem for lambda<=1/16 to an actual strict common-metric realization near lambda=1/2. No particular critical transition value is asserted.

At its central body (31/32,3/8,1/2,1/12,1/2),

    V=661/6144,
    g=(97801/676864,15267/84608,1429/2644),

and

    D12=41250133947/1732771840000,
    D23=23087771/338432000,
    D94=10306157373/433192960000.

Its full physical census is **(5,2,5), weak000**, with U={3,8}; all 68 primitives are nonzero. That full census is asserted for this exact control, not for the entire prism of (4).

For every nonzero nonnegative coefficient vector c on these arrows, (4) gives

    tr[M2*(−sum c_e H_e)] < 0.

Thus their negative-arrow cone contains **no nonzero PSD matrix anywhere on this high-taper prism**. This is a genuine mathematical limit of continuing that three-arrow obstruction, not a solver or finite-library failure. It remains only a partial packet: there is **no complete physical surviving tree**, and the all-root theorem excludes one. Additional arrows are essential for excluding its complete-tree alternatives in this region.

## 5. Reproduction and evidence level

The exact reconstruction uses Python>=3.11, standard library only, with assertions enabled; observed CPython was 3.13.5. NumPy2.3.5/SciPy1.17.0 were used only to propose rows. The fixed literal checkpoint and exact verifier, not a fresh floating optimization trajectory, define this successor and reproduce its claimed results.

Normal exact execution passed. A separate clean directory containing ONLY the final recovery capsule reconstructed both inputs, executed every exact check, and reproduced the verifier, checkpoint and final report byte-for-byte. The complete source, parameters, integer rows, cell assignments and negative controls are encoded below. No source ID, older sandbox, downloaded matrix, optimizer or external archive is a hidden dependency. This is executed exact arithmetic and the proof above, not proof-assistant formalization or independent-author peer review.

Save the section6 capsule as recover_h5_all_taper.py and run

    python -B -S recover_h5_all_taper.py output

It reconstructs h5_taper_allroot.py and h5_taper_checkpoint.json, checks their identities, and runs the proof. Subsequent direct verification is

    python -B -S h5_taper_allroot.py output

with that checkpoint beside it.

Final pins:

    recover_h5_all_taper.py — 71429 bytes
    SHA256 742af6838b4b75ff451dcabb14e09aa147d0e01e125197846047839c8064bbd6
    h5_taper_allroot.py — 24952 bytes
    SHA256 d4cbe0ec179adab9e896e4906ff9e9e3dee096c1b89b6935dbb5adda5bff1bbe
    h5_taper_checkpoint.json — 371431 bytes
    SHA256 68d0191894ed0e76728813ee6c6314b68165f2be7c3728ba31a0083e4b71cdee
    h5_taper_allroot_report.json — 248230 bytes
    SHA256 bc8443358eed0d51e4c562d3c2d3cebfbfcd289ac1d29e29b490f8eb481d56f4
    direct-verifier stdout — 4550 bytes
    SHA256 8efc4cdf9e78207b90cdc282ba6e25ab765a6aa55ea2c068815f6c18c07d67a1
    capsule-only cold stdout — 4602 bytes
    SHA256 90bf7cdcefc643c459113c179ff9e34b2835d7f1cbba05de2a04e6fe03afe38f

Tree-stream SHA256:

    72e12d24ceaf3c70e6a673ecd46f0a355500c9bd1f0823356a78d8d6330800d2

New full coverage-stream SHA256:

    23ac7a680b41636f6725d425eb95d2084ca23d842aaa93e0e0229b37dbc5fd68

The report preserves every cell assignment, exact coefficient denominator and basis hash, positive shifted-minor minima, full physical controls and the partial-packet certificate. Every coefficient is regenerated from the embedded source and input, not left as a hash-only object.

Expected principal terminal markers, besides one PASS per cell:

    H5_TAPER_CAPSULE_RECOVERY_PASS 5699 99 24952 371431
    H5_ALL_TAPER_ACTUAL_FAN_FIDELITY_PASS 4 34 204 34 56 25056 19744
    H5_MACRO_ALL_TAPER_FULL_TRIANGLE_PASS 5699 4788 99 37889 30311200 90933600 48790
    H5_FIXED_STRESS_TAPER_REFILL_REVERSAL_PASS 2 136
    H5_GENUINE_THREE_ARROW_PHASE_CHANGE_PASS 2400 68
    H5_ALL_TAPER_RECOVERY_PASS

**Continuation:** taper continuation on this macro box and its reflection is finished. The remaining useful H5 question is independent basal-shape enlargement outside those boxes and the other inherited closed domains, not another search for a complete tree at larger lambda here. The genuine three-arrow control provides a regression test for any proposed support-transport rule: both its actual positive arrows and the independent all-tree exclusion must be respected. Whole H5/E17 coverage, global minimality and attainment remain separate.

## 6. Complete lossless recovery capsule

The following unabridged standard-library capsule contains the readable verifier and every exact checkpoint integer. Both reconstructed files are hash-checked before execution.


[Encoded source block omitted; the code in this passage is incomplete.]


Supplementary copies: complete recovery capsule (`recover_h5_all_taper.py`), readable exact verifier (`h5_taper_allroot.py`), literal checkpoint (`h5_taper_checkpoint.json`), exact report (`h5_taper_allroot_report.json`), and recovery bundle (`h5_all_taper_recovery.zip`). The embedded capsule reconstructs every proof input without these files.
