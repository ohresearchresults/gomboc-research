# minimum-0246

AI research report · 2026-09-26 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# H5_COUPLED_REFLECTION_NORM_CUTS_AND_PHYSICAL_ORDER_BLIND_CONE_V1

## Result

Coupling the reflected-hull inequalities across different source components gives new actual common-metric exclusions. On every domain below the physical triangle is **p,q>0, p+q<1**, the height range is **0<lambda<=1/16**, and intrinsic shape degeneracies remain excluded. All exclusions hold for **every nonzero PSD common metric**, with the body's actual uniformly filled centroid.

| Shape domain | Local source-component rule plus the basal parent | Coupled norm rule | Additional coupling exclusions |
|---|---:|---:|---:|
| 0<x,r<1 | 22,941 | 22,941 | 0 |
| 4/5<=x<1, 0<r<1 | 24,900 | **25,180** | 280 |
| 15/16<=x<1, 1/4<=r<=1/2 | 26,409 | **26,689** | 280 |
| 4/5<=x,r<1 | 27,939 | **28,315** | 376 |

The first row is a calibration, not a new all-shape result. The second and fourth rows are new continuous shape domains for these counts. Relative to the supplied full-domain 22,941-tree theorem, they add 2,239 and 5,374 exclusions, respectively, **on their stated domains**. The local column on the new domains is newly evaluated, not attributed to the parent's published domain. The supplied parent gives 22,941 globally and 26,409 on its macro box.

The more consequential result is a proved limit of the norm-only continuation. Even an unrealistically strong oracle granting every possible spanning basal-hull norm inequality leaves **exactly 5,189 rooted trees** feasible in the necessary scalar-order model. Allowing every possible two-point hull inequality still leaves **3,185**. This is an exact combinatorial obstruction, not failure of a finite chord library. Moreover, a rational **actual SPD metric on a genuine body** satisfies the complete T56 norm ordering and every relevant reflected-hull norm consequence, throughout an explicit metric cube, while a selected true arrow stays below -1/25. Thus recomputing the actual centroid or enforcing actual metric-realizable norms does not by itself repair this norm-only loss.

**No complete actual-centred PSD/SPD weak-arrow survivor is claimed. No all-root U>=2 theorem follows from this handoff.** The current partial atlas leaves 22,101 trees outside its cover on the macro prism and 20,475 on the high-x/high-r corner. On the intersection of the original macro prism with lambda<=1/64, the original twenty-tree stress adds its fifteen remaining root-2 trees: the union is **26,704**, leaving **22,086**. That twenty-tree certificate has not been extended to lambda<=1/16, to the strip, or to the high-r corner. Its original domain and support are unchanged.

These are labelled-tree counts, not canonical orbit counts or whole-H5/E17 exclusions. Bounds 34<=C_min<=622 and the separate attaining construction are unchanged.

## Input and evidence status

I read the new journal consecutively through line 1770/EOF, including the complete literal parent minimum-0245, SHA256 3a4889dd902249e2904ddfa747f00575a10c16646d44cf15224164893c8056be. Both newly supplied proof/source units were read completely. Their bytes and hashes, and the new 367,210-byte journal hash 7fb04ad8028dab9fa72423daeceea074050606e0f138c9e0d51b64e58f869004, matched the manifest. Earlier unchanged sources remain available in this chat; no required dependency was missing or silently replaced.

The new source below is standalone. It does not require an earlier workspace, the old 5,982-stress library, the unattached half-triangle checkpoint, or a solver. The accepted findings come from exact integer/Fraction calculations and the proofs below. Exploratory planar-projection and basal-path searches did not yield an accepted complete physical weak-arrow tree and are not used as exclusion evidence.

## 1. Literal geometry and moving centroid

Put s=1-lambda and

    B0=(1/4,0), B1=(1-3x/4,0), B2=(1-p,p), B3=(q,1-q),
    B4=(0,1-3r/4), B5=(0,1/4), B6=(1/16,1/16).

The spatial vertices are z_i=(s B_i,0), i=0,...,6, followed by

    z7=(0,0,1), z8=(lambda,0,1), z9=(0,lambda,1).

The unchanged face cycles are

    (6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8),
    (9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).

There are 17 true edges. The apical neighbours of basal labels 0,...,6 are (7,8,8,9,9,7,7). The actual fan and every moment formula are embedded in the source. In particular,

    A=(31-24xp-24rq)/64,
    Bx=509/3072-3xp/8+3x^2 p/32+xp^2/8-rq^2/8,
    By=509/3072-3rq/8+3r^2 q/32+rq^2/8-xp^2/8,
    V=A s^2/3+lambda/6,
    Jx=s^3 Bx/4+s^2 lambda(1-3xp/4)/24+lambda^2/24,
    Jy=s^3 By/4+s^2 lambda(1-3rq/4)/24+lambda^2/24,
    Jz=A s^2/12+lambda/12+lambda^2/24.

Always use g=J/V=(c,gamma). The literal geometry and these volume moments are the supplied ones, not a surrogate basal measure.

The source verifies the four full five-variable oriented-fan identities. Since A>=7/64 and

    V/2-Jz=(2A(1-lambda)^2-lambda^2)/24,

we have 0<gamma<1/2 on the present lambda band. Set t=2gamma, so 0<t<1. For a basal point b and top horizontal coordinate a, retain the actual reflection

    w(b,a)=2c-2gamma a-(1-2gamma)b.

In centred physical coordinates B=(b-c,-gamma), A=(a-c,1-gamma), its image is

    W=-(1-t)B-tA.

## 2. Reflection imposes a strict norm obligation in either direction

Let S be any basal subset containing b, with three noncollinear vertices, and suppose w(b,a) lies in relint conv(S). Here S denotes the actual scaled basal points. It need not be a source component. For a common nonzero PSD M write n_i=X_i^T M X_i.

**Lemma.** Either selected weak cross-layer arrow produces a strict obligation:

    a->b  implies  n_a < max_{k in S minus {b}} n_k,
    b->a  implies  n_b < max_{k in S minus {b}} n_k.              (N)

For a->b, suppose all the other norms are <=n_a. In the M^(1/2) image, A.B>=n_a and n_b>=n_a. Consequently

    ||W||^2 >= (1-t)^2 n_b+(2t-t^2)n_a >=n_a,
    W.B=-(1-t)n_b-t A.B<0.

B cannot vanish: that would force A and every other vector in S to vanish, whereas the centred vectors from three noncollinear basal points span R^3 because gamma>0. Interior containment gives a convex representation of W with positive coefficient on B. Applying the functional W contradicts W.W: the B term is strictly smaller and each other term is <=||W||sqrt(n_a)<=||W||^2. This extends the supplied local lemma by retaining its norm consequence without insisting that all vertices of S belong to one source component.

For b->a, assume all other S norms are <=n_b. With d=A-B,

    ||W||^2=n_b+2t D(b,a)+t^2||d||^2>=n_b.

Containment and convexity give the reverse inequality. Equality forces D=0 and d=0 in the metric image. Equality in Jensen, using positive coefficients on all vertices of S, forces their images all to equal W, including B. But W=-B, so B=0; again the spanning condition forces M=0. This proves the strict second obligation and covers singular PSD kernels without assuming distinct projected vertices.

The current result uses genuine basal hulls. It does not transfer the parent's stronger indexed-endpoint statements to these new counts.

## 3. Coupled norm cycles and an exact decision procedure

Every weak selected tree arrow also gives n_i<=n_parent(i). Combine those monotone inequalities with all obligations (N). This finite necessary system is decided exactly as follows: remove vertices in decreasing possible norm order. A vertex can be removed when its parent has already been removed, or it is the root, and **each** of its strict-max obligations has at least one right-hand vertex already removed. Repeat to a fixed point.

If removal stalls, take a maximum-norm unremoved vertex and follow parents until the last unremoved vertex on that path. It is still maximum-norm and its parent is removed. Its failure to qualify supplies an obligation whose whole right-hand side is unremoved, contradicting the strict inequality. This argument permits tied norms and hence PSD kernels.

Conversely, a complete removal order supplies a strict feasible scalar assignment by assigning decreasing distinct numbers along that order. Thus the procedure is complete for this **norm-order model**, not for physical metric feasibility. It is not merely a heuristic cycle detector.

### A two-component contradiction missed by both single-component tests

On the entire strip x>=4/5, r in (0,1), both containments are certified:

    w(z0,z7) in relint conv(z0,z2,z3,z4,z5),
    w(z1,z8) in relint conv(z1,z2,z3,z4,z5).

Consider root 0 and the complete true-edge tree

    1->0, 2->8, 3->2, 4->3, 5->7, 6->0, 7->0, 8->1, 9->3.

Its first reflected obligation is n7<max(n2,n3,n4,n5). The tree gives n4<=n3<=n2<=n8 and n5<=n7, so n7<n8. The second obligation is n8<max(n2,n3,n4,n5), which similarly forces n8<n7. Contradiction.

Neither source component by itself encloses its reflected point in the certified hull required by the earlier rule. The exact enumeration verifies that this example was excluded by neither the old local rule nor its reversed-cross-arrow version. It is the shared norm comparison between two components that closes it.

### Actual scalar certificates and counts

For ordered basal chord i->j put n=(B_jy-B_iy,B_ix-B_jx), h=n.B_i. For target b and its literal apical neighbour a, form

    R[b,i,j]=V s h-2 n.Jxy+2Jz n.a+(V-2Jz)s n.B_b.

R/V is the actual reflected-point slack. The code generates all 294 guards at degrees (2,2,total-triangle-2,3), giving 216 coefficients per guard. It accepts nonnegative Bernstein columns only when every relevant included macro boundary face also has a positive coefficient. The full/strip/prism/corner runs accept **64/73/86/91 guards** and certify **14/21/43/40 target-subset pairs**. The ten chord guards needed by the displayed two-component contradiction are included in the strip certificate.

All 4,879 unrooted spanning trees and all ten roots are regenerated. The exact coupled rootwise counts, in label order 0,...,9, are:

    full:   1560,948,686,686,948,1560,1916,4879,4879,4879;
    strip:  2296,1816,899,686,948,1641,2257,4879,4879,4879;
    prism:  2296,1903,1271,1355,1245,1725,2257,4879,4879,4879;
    corner: 2595,1931,899,899,1931,2595,2828,4879,4879,4879.

The new coupling beyond the local rule is (124,124,0,0,0,0,32) on the strip and original prism, and (84,80,0,0,80,84,48) on the corner. The reversed single-component rule alone adds no trees in these four certificates. No negative coefficient of an unaccepted chord is interpreted as a physical obstruction or survivor.

The reflected strip follows by the unchanged coordinate/parameter and label permutation (5,4,3,2,1,0,6,7,9,8); it covers a different set of tree labels on r>=4/5. It is not extra coverage on the original one-sided strip.

## 4. A structural ceiling for all spanning-hull norm rules

Grant a hypothetical oracle much more than real geometry permits: for every selected cross arrow at basal endpoint b, impose (N) for **every triple S containing b**, whether or not the actual reflection lies in that triangle. All larger-hull max rules are weaker. This artificial system is stronger than every geometrically valid spanning-hull norm model.

Let R be the component of the basal root in the selected undirected basal forest. If the root is apical, put R empty. The complete removal procedure succeeds for this artificial model **if and only if |R|>=6**.

If |R|<=5, no first vertex outside R can be removed: at a top->basal entry to R, at least two of the six basal labels other than the target are still unremoved, and their pair supplies a blocking obligation. An apical root likewise cannot start removing basal vertices. For |R|>=6, an explicit strict scalar assignment is

    n_i=100-depth(i) for i in R,
    n_i=20-depth(i)  for i outside R.

It strictly increases along every selected arrow. Every right-hand basal pair contains a high-norm R vertex; no basal vertex in R has a selected upward arrow. Therefore every artificially granted strict-max inequality holds. These scalar assignments are not claimed to be norms of actual metrics.

The surviving count is exactly **5,189**, rootwise

    (739,743,743,743,743,739,739,0,0,0).

There is also an independent counting formula. For |R|=7, delete one of seven basal cycle edges, choose one of seven basal roots, and choose a rooted forest on the three top vertices. Its rooted Laplacian is

    L=((5,-1,-1),(-1,4,-1),(-1,-1,4)), det L=65.

Hence there are 7*7*65=**3,185** pure basal-route trees. For |R|=6, the omitted basal vertex is attached through its mandatory spoke. Removing one spoke to top 7/8/9 changes the determinant to 50/46/46. Three basal vertices attach to 7 and four to 8 or 9, giving 6*(3*50+4*46)=**2,004** more trees.

Thus **43,601 is an absolute ceiling for exclusions using only selected-tree norm order and these spanning-hull strict-max consequences**, even with an impossible perfect supply of all triangular rules. It is not a count of actual excluded tree cones. The real geometry may supply far fewer rules, as the partial atlas shows.

Granting every two-point hull rule as well replaces pairs on the right by singletons. The same argument shows that exactly the **3,185 pure basal-route trees** still survive, one may use the same high/low scalar assignment. Consequently merely adding smaller reflected hulls cannot complete this strategy either.

These ceilings do **not** apply to the original arrow inequalities, to inequalities retaining edge energies or metric correlations, or to barycentric/SOS methods that preserve such information. They identify the precise norm-order information loss, not a limit of one-sided PSD separation itself.

## 5. An actual SPD countercone to norm-only completion

Use the genuine body

    (x,r,p,q,lambda)=(31/32,3/8,1/4,1/4,1/128),
    V=5984879/50331648,
    g=(82630529815/392225030144,
       6565559545/24514064384,
       6050927/23939516),

and the new physical metric

    M0=(1/1000)*((307,24,13),(24,597,240),(13,240,98)).

Its leading principal minors are

    307/1000, 182703/1000000, 270561/1000000000.

Its same-origin physical inverse is

    N0=(1/270561)*((906000,768000,-2001000),
                  (768000,29917000,-73368000),
                  (-2001000,-73368000,182703000)).

Take the unchanged complete T56 tree, root 2:

    0->1,1->2,3->2,4->3,5->6,6->0,7->0,8->2,9->3.

At M0 **all nine squared-norm increases exceed 1/5000**, and every basal squared norm exceeds every apical squared norm. More strongly, on the entire closed symmetric-entry metric cube

    |M_ij-(M0)_ij|<=1/1000000,

M is SPD, all nine tree norm increases exceed **1/10000**, and **all 21 basal-minus-apical norm differences exceed 1/100**. All positive rescalings give a corresponding conic family.

Because the tree's cross arrows are exclusively top->basal, every reflected-hull max-norm obligation is satisfied, even if every conceivable nonempty basal right-hand side is granted. The exact checker also enumerates all **160 actual pointwise closed spanning reflected hulls** at this body, producing 68 relevant selected-arrow obligations; all pass under the same actual norms. Thus this is not merely a collection of fictitious scalar norms.

Nevertheless throughout that same metric cube,

    D(1,2)<-1/25.

At the centre its exact value is

    -322204493663682323/6426214893879296000.

The exact weak-arrow failure is substantial, not a numerical tie or a collapsed label. At M0 the selected arrows 1->2,3->2,4->3,7->0,8->2,9->3 are negative. The full actual census is

    strict(S,U,H)=(3,4,5), physical weak points=0;
    S={0,4,6}, U={1,2,3,4};
    H={(1,2),(2,3),(3,4),(4,5),(5,7)}.

All 68 true-edge primal/polar primitives are nonzero. In lexicographic undirected-edge order, with smaller-to-larger then reverse primal direction, and smaller incident facet index then reverse polar direction, the complete sign strings are

    P: +--+-----------------++------++-+-
    E: -----+--+---+----+---------+-+---+

This body and all its exact primitives are regenerated by the capsule. It is a nonattaining control, **not a complete physical tree survivor**. In fact the supplied original-cubic stress already excludes this entire T56 tree cone for every nonzero PSD metric on the original prism, which contains this body.

The missing information is transparent in the exact identity

    2D(i,j)=n_j-n_i-(z_j-z_i)^T M(z_j-z_i).

Strict norm growth, even with all reflected-hull comparisons and actual metric-realizable norms, need not pay the edge-energy cost. This is the next genuine obstacle for the basal-only residual, rather than another unexplained finite-library failure.

## 6. Recovery, observed execution, and continuation

The complete lossless standard-library recovery capsule follows; its payload contains every byte of the standalone verifier. CPython **3.13.5** was observed; Python>=3.11 with assertions enabled is required. No NumPy, SciPy, SymPy, external geometry package, parent source, saved matrix, or optimizer is needed to reconstruct the accepted results.

A normal verifier execution and a separate cold directory containing only that verifier both passed, reproducing all five JSONs and the receipt byte-for-byte. A third directory containing **only the recovery capsule below** reconstructed the exact verifier and reproduced all five JSONs identically. These are executed rational certificates and analytic proofs, not proof-assistant formalization.

Save the following capsule as recover_h5_coupled_norm.py, UTF-8 with its final newline, and run

    python -B -S recover_h5_coupled_norm.py output

It creates the hash-checked h5_coupled_reflection_norm.py in the current directory and executes it. The decoded verifier can subsequently be run directly with python -B -S h5_coupled_reflection_norm.py output. No downloads or previously generated files are needed.

Final pins:

    recover_h5_coupled_norm.py: 11237 bytes
    SHA256 6132d5a37a6f7a9396b0eab0e303b43962930d1ea6863e26c23bacccd064c8b4
    h5_coupled_reflection_norm.py: 21802 bytes
    SHA256 cadd50024b0defbf5f2c6851afd8e8955be5a49a31bbd8888a7f0dae84ecbc72
    output/coupled_reflection_report.json: 17727 bytes
    SHA256 d1942ae56e4b85d1108bb00b1a11ee6cb5bdbeb69c885c5e37ec264bc991638d
    output/full_coefficients.json: 561402 bytes
    SHA256 b245bbf4b37158609794b3de02d0e42728cf17873f0817656d1afb4597c8315a
    output/strip_coefficients.json: 639888 bytes
    SHA256 9d5dd4d4b6cb86fb4869e6bb2e3e7d26849e40063bce3a6817d2b2fdd33024f0
    output/prism_coefficients.json: 736577 bytes
    SHA256 5670354028ebc7820bccc854f7a201fe9fd91d3cef551014e10c9f96fd662dc0
    output/corner_coefficients.json: 682456 bytes
    SHA256 2af7402ad7406be6a0cac13f7042012caf7bae8e4b656ad6dcda9801793e2593
    stdout receipt: 510 bytes
    SHA256 cf8c8402cc2b423278e6f9e6b5f639b4a6fb50d829221e8db37a226f1cf71d43

The capsule adds H5_COUPLED_NORM_SOURCE_RECOVERY_PASS 21802 followed by the decoded-source SHA256. Its complete stdout is 618 bytes, SHA256 e1576d71e71d427cdace13ad18e55e1f76858875641e8010c62813926833be13. Expected verifier markers:

    H5_ACTUAL_FAN_IDENTITIES_PASS 4
    H5_COUPLED_NORM_COVER_PASS full 64 14 22941 0
    H5_COUPLED_NORM_COVER_PASS strip 73 21 25180 280
    H5_COUPLED_NORM_COVER_PASS prism 86 43 26689 280
    H5_COUPLED_NORM_COVER_PASS corner 91 40 28315 376
    H5_MAXIMAL_NORM_ORACLE_BLIND_FAMILIES_PASS 5189 3185
    H5_ACTUAL_SPD_NORM_BLIND_CONE_PASS 9 21 68 3 4 5
    H5_COUPLED_REFLECTION_NORM_RECOVERY_PASS

For continuation, the coupled criterion can prune source-component combinations before actual common-metric work. For the 3,185 pure basal-route trees, and more generally the 5,189 spanning-hull blind trees, retain basal edge energies, common quadratic-form relations, or a genuine PSD separation. More chord subdivision and norm-order propagation alone cannot finish them. The rational metric cube provides a ready exact regression test: an alleged norm-only all-root argument must not reject its satisfied necessary norm system by silently substituting actual arrow feasibility.

## 7. Complete lossless executable capsule

The unabridged payload is the complete verifier source, not a reference to another file. The decoder checks its byte count and SHA-256 before running it.

```python
#!/usr/bin/env python3
"""Lossless, standalone H5 coupled-norm recovery; standard library only.
Usage: python -B -S recover_h5_coupled_norm.py [output-directory]
Reconstructs and verifies every source byte before executing the verifier.
"""
from pathlib import Path
import base64, hashlib, runpy, sys, zlib

PAYLOAD = b"""
c-pl*`*YhkkH6=y(0(_!k{mjb<hNaBChaEQcCSq{N!shJ&!^EVi4t3KB|Fcr|N8+Tsh90`_hzoUu_Y1!K@bE%5cI$Oa=6a3LqARq
qvSzbKCf=mq_g*rfBfV3o))C*<va?tEV`aY!75G@ElIP57OYpf<|UyPJ$b>3%Gzl%f7bkY45ioJBA&-lez12=<g_E+Ik4@CmahQG
%R+4)`<a(LYlt+_vUQ?8#;aS+%kwD1W^ye`JRh1q*t;a0d74CHXh>UnS(L1_>v$gJOiR{_D2oGcuBFRWyog_-3`)}sT1qouJYBDr
$ZHZsArkv%lrExG_Ix-`5lIjmYrps051-y0e{e59eZF{i;$D7!dv$Sg;$EDbemHq|_5RbD`|k7ArTfJ`ScH3*zaKljz7`F7ecO(l
PREZrLBA8(!@wUxNq5kTf^ZOyu7lCg_wDc+N{7xM@SJ`STBFDde5>C%*!z^lH*o@d2yXIpoduC5$nTA!LBHQ|I@ajA6NcB<T`TYh
*M8J<g1$Ehue<iZv#gOn>h}V_XIsACbwWRkqK@bH`UB|fTQ3Kym9dku^YR<_&p(4fCteTE&e!dm(dF+S?PT!JySHB%z~}4vN^#Ng
y2Ifp3`dsZbVrdhvbw;GH|P$oEvq-^dA1eU{eHI}cDuo~-2*7Q-yM!R!O-gU{peut>Ne6A-c!5)UPyV;%nM-fG+;(M`*fw<h%t!+
(57I%&XLmq)!-Tic7<95%D8u(r3>vEP=$KLi)EUvv{P9CebP<^OuPczG@TbP%PbAo!HR)4FF?&bA|PNF9w?mz!&;`zgN3MCLKSGK
sy&C-J^6g=<yghEyF5*pmOtlvdspwTKAdnJ6zSck&*vXbeyi%v*{6$-LV=FYesj-%|F6sUsBE7ueml8v-+p)xh3`I{oq&4jdw-r>
eA2jPSj^N~T5s?4_}$4R78rfjV_nu^4zrnMGGoXF%wje?4OpK_Y^WQWY)@1Fj1e0`SqJJyfZ2ubE>Ib;5j^$byGPhVcsHS?GinED
3Oeva`0`26!6%}mT7eRxNp)RG+hU5k#T5OM-~LHGS)olaa*$*c8n3lC!(+Z_n%XtY;A<^TH0piXpUOW30cZqziI>JT)2^rXc(#8%
9osYWJG6K8=^Xom%>x7Q-vF50J3qcSIlF=xet!Px;tBv>4IxCEI@+PnE_JoX`XnZcgk+iD_x6H0m?-UhOe}@bwdT5U60cm>$fNl+
d*YTkF4&Es3wfNN(F-EuiJhBc4Z#jV{&Wx?1nKhGFbn8t-h>b1U{#{L-j7d>2O*n#_JAFKIsj!~<c5h&J$$c_%A*qRJJu%YN_(OT
?G;rFXg!(VE8XzIQ1!yE^daPeOq1IR7w3j=0)S*?tcBD284nL`qLp#aP7TX6_a6$pELyEI#0dp0*UhM9E;*=hlted@BOqGfff(8k
)#fFCvia|3g+jjeD}7Ql@O{6HTvtG|?XU>7-^S7k>|#CNE~?k>+vHPcaJ<*l;yd=ZMT{Ft|H8#o@%96${DD&bdv<4<8wla_MUBIY
8i&^7k4Azz#$^X99bRSYD2yL=$g*YFho``NRh-N8Q9&n_zP#{r!>%ili=D{4<R&rz5+Gh$g}5thzEp@u-*#{U+RlX-_x2F<!OM(T
Hh<5j)~wZ=X!p~2#_heD2&5IdH^(+85Tb_Zii}Z7f4wlCTF=Du6MI&oCxb;8pg?sDLG!8o1DqgB^ITw688W=7J!|<>XV&)M1D@;|
lTQ|wS)!K7CmYLbQEQ5>%SH9sSgs`PCzi1#`^H}Qas{3kx7$LdZ@FQdg7pKFPHRZJ(|S7W%I76p!uL03x4+daK0;-OU9#^286NS$
29qhjr9ym_dTZn@kL4{NC|8a5TXP?m9ASfB<hR9M;9KAybE9Looo?%?wZyNi_02r&cLncH{M6`Kup(Il$3)Is%fsP5e&bWe*@rJI
Y6Dj5+u=}PJvXp2tlGzKd;%;9-Imyd^@Sg|@>YJ>*?&3gQ^_A3`qb*Q-h#aLp{n)L65<1#u6gKm_g`8s@Kp#-KtI=^vB|B_qB+}v
_V9x$&8nKbWnbAB_J<tsHTcyq@8-`*x`@4bVMCTHIRIidknH1f()CPpqRqVpXvMTU6N&+^LQtXsUR5Tlcz|gJXm@-H-%S3^_SBq?
!(1%hXXVs~;bs8~x$za|U&#c3mi8cg;5hGaCi%=WnV25<8sIBFgz#XRasY^xeI7p4&2HJb4$Q_oSdI{;g)<l%hxdB>heDae<^%f1
ztG;so6ikI=KK$ZQX?(+o_jv5s(cEfqanb@LJ%u21M|ybc87@45j6w>aG0`a8F?$-Y4{AB-;Kc?O;&NTj*6Ou8*is~Go0*iu@_(x
=-a~gyBSS=1$#?!Ob7tR$>U$A;0;X$JG0qz?92+-3;qQZ?Y8Z-1kN8=YwkO(KhWTaGOr|kvCoY!ZBc6iqH0LeE&+vL4!q?uO2D%#
MS%(@M5QV(YHBSInE(;W9Vg(_KX`NZ8r=O9)R+NJY@V{)xNbRdj86@8<-w}nn=N{Z;fc{x0#9aZp0-+s*M@52Hg3;Tv(>ua+u~kU
Mtcz_K*lro(JBekokrKNL5X2Ql^Zzia^|N`YO#r)bFMtxdm^?Z4M4b(_VOT<{z~%1VUJ|o!zh;3NCjk-WU|g~)(O;=tafJm_tVZ6
{J8|^ZpDY4m$J|}I8FPItf0@rPpKESV>tt0#~%k#E{W8YJb40aCZ98WhUV1!9Hl8}yyMd;NTcdBHl)_zUFh#sb+Q5X%viGrQ}|Po
t#WE*>7xR#Y#`7mu}G1vyIn9DgQGQu6T+hh{EChq$4EyhE-^aUoU6ju*`l>iptdd06P&HBX8j#YGGK`6?OENSdueg0*J~C?y?$V!
((4rq_Cr|=PXMwD{gFiqX%3GjwdSBXX|?JdsPyxtq;{pspjvu-0f$|)(J~$m!Uz{1*ka@U4gLTICHszE$Qec~iMIL~+SN9+cke+}
Kyt=ID-6sU#H`k)7-=u58DvGd9OvYPPeJ7*#g$pxU_}&P@>UV`mUdaC0s(0yiz(WjRqNe*SSY|2OA;$2k-Tioo_UlAi(#6xn&ktE
EDV4PCY6`L1VW{N@lEE^@Z=aOS)tBExdDU6!ssT8qFkDu3IdlkRGuzZHAyJtV~KK0Q4zrO%Qnr*qLlLKS(-$%+A1aSL6eWHv6d=P
SmstJd-lezKqVy<GNy`CQT%V{kocj;E!Ys#*3|=tHd)6>r2XF0{4{(%&^`kS%*Z5MrqBuk#z`<=Q<$$J)4El{#(-l+->`xj*e{f=
S(h#?J}_bC#Ym96rA(k>xFA5a`Nk^z{ZnwdqM9`#T_eQW0#6-Eo{iwhBG7>07J#`hoz+-WS~j<ZKY)r6W1o?Kv`il7;M<|wV%$~B
eQ+kWQXtUBDkyB89?izabE9jr;0ktxdwYAw7Z;!Y^HN&=sOr{>U=J3MZ55FnMs6L5`uybLBR4AHED9Hm*wEa=xGOjQa!dxpV2%iH
VTkGL@yGKIh%Z89B8*kXA8g>;1^(MlUr#Ri>z<}xujg}pY><V=4UO2}Y(9&P4*2XkYR*!ibTRVvmyniOoG%2D-BX(<wU_D&U}rmO
kY-7gZEJ8_^8)WXNa+0J-POr&)lT-i%<h7)dwq+Ix<l3<_UR9wsn8zTebyZgM&(B}%2-4j{~m>!)CMp}HVl|O0Db6>VBkihl0?4?
VsM<^UtmHr9B0&L_7ED}LZdg>%7z*T0Pc1a8v_8bodL+M(}Tfry6`aoCjKTTBdfE6%noLXksW~!Sinus2IOJSrVimBy-=|;7+QaY
7htA0f`&((3Ke{zVrS?KH(2>D9o>24CB{=}`f4%CQ**3b?^Om+TY*F%Q^LI>;JrB(baw<azi*{u%;S8;$l90%y=je*ATz7lswdHp
C<)RqPHv3UziWhBFphr^t{2PP5X2CKq5tlZCy&;S<<Zj1&_&6)p)>eztefV({@;mi9uV!wP-}?y04t8Sx@DE7yhmQ+V1fV#j~R5>
^`BR;mIFx58+g_6kSp;Pkv=A1d}KNS>tl2x5QFLYt>^Um`dA)I9Ef+SJh+XX!uTf2SB4tSg_qwOm*uE|<6^&g6PIrPrR;?`qKkpC
bgg1Ya%)D;3*QoPn1tTS<FDT*u(Ji}<tieI#EE<GF(~MRc6Kw=3EmbsKv7aGy3&E+J2qRTD<-z?3Y>%Ccj&x=mN^uaT1+{2?0!)y
`h$g|Zj;z4tPdT>#2`)KBEwG6IjT6!PPv=FRi5wk%}U}y5G`R_$X}^#82}c~HHTBOwzqZduX!m`@J*G|Dg9d%<gDSkl(FfXG{vy~
su9l5<Cmxs-+-laGgf_x0M&D}GMItrTf)|eMIOQBc<VV1^acYh;2F^F69AQnlpCddqDyv3Cp?#Q!eeeHr}}r`g&`7^>R#Cnf#-&2
k!pJmFqgt~zymgg*t<wqoj1;X(xZ!C_@#LG^^)@o>Cs&%Qk9ndXCF^w`Kv#kUj7eGJKvPx)UxD^ww*wIR?1EZxg5j9W62G;j4oFz
`V=Qv%|%Z<<vyc}H<o&hdapzbnxA-0#YX_*94c>$NSI`Px{a-}i_19SWd6Wr92&^czV23M?*ZCc-DIyd5$iBl+$T44h2O7_aqj4#
<j}wz%%8qI;uiacAItr3Z@8`3*En6+qBIL}-IP{Jm-?@d)kJ`mb+Jejx3b^V$7pZr#H#%2V=_v*l9)c0dQ*t-dnJAe)=vxrCkZks
G_!J=L3U9By>9QfA}!{(wDm=MRc3W;1&_I4Hs=LvG<Zyx>Qq+Cf*Ju)>8hm(M4d+uQKHSkkofURoYGS#r196RgM+?ary;BnE{}@{
_Itwq>0|n0RdKqwqQPnwC*P|fSCX6XMlp{0hKmB>8)6A*;SMO_x?#yC$&!MCmcCU1UYYo~>45(oJl+NmnzkQwq%Pkp7DqNxu`fuV
*=BVy$2ulQU#zdGKaX#u5nXzPs?<D_*LbYvorpl*nX{@{ESHO=XEsAucQ9SVHZOiNFn{63-J5~(0+vxU$5vBy@)UxF;MRm@kO~t#
-oj|nR<9BYn1>u;Yb!@3TxeV7Mhp$%kB;JB?eW$?89*$(X*^Txg26Hb3Kjoqn>+E)FkSqLz{Cd`-PETjV$2M4+aiI$|KjNKh|a3e
LtKknkT^JWR{2R-zz9JIFiTUMp(|Y7l?#(_tI(+^1g~pjv7}uw8&x$ayyMg9ta%g)V%&&S(tsn`F(6I7nd00xCs^PY1r=4uqbT98
*7wP`b+nGSQp$oV(xj@*rJmXoEp18>MC8-TLg(92GR6;DbAcNoSaMgDD_SxH1$DHo&0$UU<;iRruM=(TP_CuNr)_7}vMq3@rwBab
ZCiDg-X|fL&09MBwXKa#?h?RX5<;oG{*3dsv)dyPAfDg_AH{<=+qZX0i-vFQqk-Ymx{JO=M`{dbV8XK;Rsy1pPLny7q^88m>|b2H
`*j)@+}ciahmcSa-VB79@j0jQ!kI{u*Qd#QLDS8zp+3jaJfzWOV1*<v3<S+cGVG#i%M;FVM=B;B&Nw%Sl6;*TRii331MSo6{a6fl
d1Qc)-zQ1*xU*84T@u`G3P9emeoP~J@)oc`%?WDOBmk>J<SnSOv0pQ{5d-V71j_>}XOONF+)%~UrYqVol+GcpKJ&;GNp|FF$|Y)t
|32N&s{sYN<6po7WllrIHZ-l~m@d6ItG2vNYb(@uk)b5gj-0X+dUI-Tu8<;cN^r7DSKwb)=DM;WO3SJ$CQc1D%{WOB2?+xNCTWsn
{Ne!IAu$TjP;*?SNj59MOXHrwek|WSUE8vFs|C9f7xz27;Um<>)|{li(}bvuK*cGCdDP+MlHV~wLL3aR)0tqMQ>k;xx~8`y$Z#Xc
j(A_}tOYg}aXzSQbZ7vTJP1z?W3|lLs~J%Ms+$))xd9_*Vf6+14<difvCOuxpVdTy9X3(&j*dc-1Hv2lysP<8Vvx)qW8ncRJZ+`{
2z9<XI=cVWHh0;7(OQ-Z_oP!~?P2*9(Q33`)$)V&GDIaQqDNDu&=)MpXJ&m9Pf?co=0jPO?WtvPavNa~DkR%|#0O};>4*xKJsK|9
2-;#Fs7mnAr#j%$cJlI^px*V0ptmj|F}8~>fQ!0gomFi93;bAyIUx)34V{7cFWgDr2^W0p=3Qh~%2f&`*^VZl13)}xRoYu=ras@{
yiZCuu`;L3$+ZWbv~Zk%sn4zIGDohC>?V$az}f{0?Ct<6rc(uaJ6Kt>DH5E1j@1@UGN@zpv?Y6JW4`_0=iL9pyxW|6Kc9NA!i(Lx
GF8QpOr&>EulCb)Zq$Yi!0IHy?Wp5y84PkPwon$JNVcB1d=Tei>uyL{HXKLcW(b12EeM`^7rdMFirh0))S0=lqm<0ZO<F}+RXkPs
KB8UoO>a}J>LAMRebtdAeN2q$qD%T%e6t@7Z|xuKy+L(gJr|)0eLUUfG)u)difySm`@YdtWQ5BNsa(dnJY5w12kt3oAou%B#v!)s
IHgkmP<V1eSG`{0%kU|>zJ)&{>!gRor-ROj4Z5BBAC|!%CRNshBGQ!tn!VnvHP}Z-sZ#~O(*QvmY<|xkj)=LU)Pd5DJ?vFcHawv|
xDQij*k#Ue*!b(x-zHy!)}YnzRcL?UhS6hf8~!($0pH!?sZGhIwNMXCf)Bu1zb9R0kxo;~cJOLBfyEI0hxE<F=LbxuyPLIXR&ajD
xwnzK(J?n{V5c%sipG^<BXj>z=eJ~#PkR>Y_ThgK;p(@HPOE3_cU#>)9!gkNw|0D@R`QKNl;FQGT_$ftg{PH#zZyzmnl@278z?pV
N70c+%()iboa$nirq6gI*h{ya+~s_oyW&QY>p#0<{ueY^6-qW-g4H<Lh~CnjwGz1KBP;4?Zs}uG>{0>^I#A*I(Q^up7_rg>Z{uqz
@&<MmExb6Ph$>ECtKDde$SYf@kLy;kL5sG$!lJwCu&-|5YsY+z`7Blz6(&Ws>JOw|sqrdesKt;?^>qTyjf=PPT%zFORXrJ}c3~4@
yZtT<?O!8SNW+a2cXjKnTq2M7jy3GpPd#aHT(L8g(qq6*wSXe|((K^5Q#sg8bJP$eEDvtJ^b+Fbb`5WMB~9*_-0R58V;>{b6+_7M
0-<O{RBfTXdQ4r)NBT>|9Uxv})TuiS>ID;3nn4uLg^qRlmR%*b9je#2dJVeEbq3-??^Q_51!J>V&pmyt55Tm}BV3|_XP_fvnk{WW
t0O-3d$3F`(LRCh<;_ExJbv0ixnEGI7(9(@Xz`j<paEAj;4VB^Yo9RX<%f$ygMi#j!4&o~7bZr0lPpMa>NBdg=c-Jo2DL{o6VqD%
MAD^o9c1{!`;7SnOt(@14OOEW{?{HOKm}RHKE(s(&)N+vEg<*<UB>Iv^(xB5MUh%wo4jKp@1@WU6M3dc=j@)iX0ljdWcHZ7-HPq)
`_0>Q8O!B52T!UH@#R$)kYxn#!B%=f>#5`*lVtGuSYkgfYCRFu1dnAunRujxF_i{I=zcs0fR9xIFrV<Gp!HEK;4Qzg-KggzcZ$S&
MG_b3W3vqP!y6_Eit7i*m?wCQ+3r%9G0d&J0#CpQFTY!efob~mPH6&6v|!3)_6Nik$1YsdOq4J4i;TZ+kt?)g-0j=uzjtO+BNh)W
DsxmBJ?wIq+jV?r3qDnvhvAO`89#T1M7GT;dqyKv5fqJ+pBqnRHCN%dqAZwFOxO?Jd`*$DbpFhWD@>Tod#W-_DLp)W#0%enxIc%$
Td&YjVi3DmioArq4<VZ4pv51m+5gbOJ`Wl>x$?;D_BqF!<}RLEWUw_W@7EZoM#siv5l~djn_!jfJ^5ujL+J&+Wq)p5s+rtKNA&LS
ODW_(%!#@@g;!r**o_d}3s(MF^C`b@ywWrp(&E^&Ivu=(Eg(MDeB4vxf!UU2)ibBfjhKxb9K+~X1Lky@jmeYn-5cR6T@LHu0~-xh
az(Vn(Sfd7tybThoN-k2k2N;s-1!Jz2+9md6E7&Cp)<fdIl_f^c<c2Atx?^5#^3;I(noQXr*&4%xvnW9=gN~e_qIj_erg<OD}5VZ
V|c78MQLc-uzEqS)ukN~p0sv{BmVkcqLh~*WhU7$%_F%J3|4DU#s``Z6Zv+>r}(ONbw9m}_2=%pSP$v^?_b7JSE$nYk)?Qg*yr&6
gBx0kce<wqpmb5|&!1n^DkLE9YsuA2QiIX|L(I<<4`V8OK}<_1?v^)%(!8FAu+uTv#7V+S0r*M)C<$|-Zd-X932C=r&L`j0{ky~4
a?&Lmu&CEa=Nm&7DCSyY<7WtO>>aU=SRK^XsgPXMHuamlO9TcRWQ9xY6D+Y$6<6Y`5a5jmvwTW$I03{%Tw851gL~H0V#G6#&^+{T
#*4E$3@y6B+K(F7coda#aNhB%fAAHWX7~Z4K+c0Ij%Pv^=nz(JqNR^~gX1<#+*Y|tz1t8kU>yl_h73<iW|hq5%5KiR=iU9-y!0m?
fNnKCq1nNrC-n{%{oc{RSatC3Z*|a|lzrIf9_;5ZUyihb82d=NFPQ-zYo}V`N`MeUh%-^8luYmqzn5NcA2lwc2wX~!sLe<|y%uwp
od)$YGn&0pzi~1LBDyc0>sb!h>~`Z0LOo1ZGFseM1SFW+SW%qKL;q>gOs{9`jAS5QZ)Z%ER}&3oKMRUNj#D8Z8BwQ0K@;$|)!nfe
>yQV`a*z-9tiDFjZ6ZS7M*s|j4U4S32QWaT(W!zFiO+mzgp{ny8-XkY7Zw`<;!^S~fbsT;5c*{?WF^Vb&nTAir%o!G*OF!qGlPt{
Nb`x95Us)%Sv6AJgp0=p;@x~x4>f+~d@6IgM9l3H3h;MJ`ZX}sBA!6f?Gf?gC&f>w$eSdy=0IGU`}p<QY*VI-pn@?MdCL*^K3{P|
A!d++GYAKC;(H<Assyz0sYh|WaKAaX-<;z1*Xb2^k|{@fYl=3y)|j0zAD3P>y4WPzIa?~JDkAD^AHxcdabB}=KS~*<bc4T_FI?sd
Uv51nB#kEar<5*CDPzqn;Y)TY^MrqxC|vZXn4c<{ugDgr>>|6COHf^$C_9bc?a3p-N~-(TC5*0Ym5F$Du6(ZY`x+;W*hD>9*q7;w
MF%Jc$H#=>rkkAl2SQwiDbMT6Gs*fffA!!^E+pdYjb8rd@!MZLa;wDee-hCtqx(gau*f#eDS>wBek+n_VSlG*-lO|~KO#k$sDCmY
9LqJ{r1--0>o~(;Qi@R^ef&o=evI=fjYEBW!}O2(_#@NL^zj)yyYtAy^D|et<dje=wlhqp1pu1HuPxzQeT>S$bdsl=e}j36u}pep
BEU-#yEqB5$jgxwdQ1&UBCJHKH2!Q(yvE4!5>srk<RkL6&fN|ay>IfUwhztDBI0KA?i}~WuAi<G%s(!DpKa(E_w*4-G*4mBblD(L
`WIVC;0c>+1D@-+YrNPg5cTmkW49&lT1*Bvn5TIZ)`Pq>FcP2{{wxqh#I%gcLAQN6)mx~wNgvCVPnC+v1;n#vUNulI*ED@xS>Hst
!o-&*M}jtnDFHy&5AJ|PL*LgaFZIY0yG*^U(}W7kb=};?z~3Q5OK&rVD{{Lp^)Yl?zI@ilpNp5@T?z~9W4YKh!=;gTFGdGIESvzz
OO&N9vK+7C2gK|Tn~etP60`n~X)mW;p8rO7e#wMEO`^&8s`%YO6f0iAj~IntJvx%axV46jw@J4sZLo-@;$cMPR+CJGaNRKS*Eg;^
&O9`$7wcpdFQOB`&kX&z{At3)I)_y_Dt@9+m)n{3>R@pn#+e~bwdB3A=qUzklit&ty!u|rTjce7R%HSl-<jzsk2xs{#W%xJmD3ph
s;}Y|o;lF((}D7(*!LVy(1;e3(ecW0K`uk#pydtH`dB{f7_NWHE86mxhD25X+2kW@f@=#{gb;)e8|mWSc8(SuSOPI>XDI@;RSu~b
#;17o+$Lk71#>T6;2>_?G${`D${#y)MGwV&6Dhi4Ka;Es{Hea<cUPZ}Ke(sIXYTvoPR>9^?@un>^J8#Zy1Kb>^h&qZD!(VeYv-Ml
fM?~ISGfx)T2ns^D1Hs_)0dMAYD#C6vjw=#dml4Km;9#nTOPBG`<=nGaj-dKP_%J=Ics+R<MG$`AEE!m(5H*zcOOpVuMwUee|-O;
kOd_I;Mu&sLx3<r1(C{c84~75b8HQ^BOR@)ZDQ~GrNoO9lFok#@l>%Y7d2u08#grZ3V%#L90&4rUCwpaMQwLoSOsy$<8L?``7`Xu
vYQ9|H5HYRE{n_~nPI5k_S#aSZSf1DIuQR~9fZzF
"""

def main():
    if not __debug__:
        raise RuntimeError('Assertions must be enabled; do not use -O.')
    raw=zlib.decompress(base64.b85decode(b''.join(PAYLOAD.split())))
    expected='cadd50024b0defbf5f2c6851afd8e8955be5a49a31bbd8888a7f0dae84ecbc72'
    if len(raw)!=21802 or hashlib.sha256(raw).hexdigest()!=expected:
        raise RuntimeError('Embedded exact source failed its identity check.')
    source=Path('h5_coupled_reflection_norm.py')
    if source.exists() and source.read_bytes()!=raw:
        raise RuntimeError('Refusing to overwrite a different source file.')
    source.write_bytes(raw)
    out=Path(sys.argv[1] if len(sys.argv)>1 else 'h5-coupled-output')
    print('H5_COUPLED_NORM_SOURCE_RECOVERY_PASS',len(raw),expected)
    sys.argv=[str(source),str(out)]
    runpy.run_path(str(source),run_name='__main__')

if __name__=='__main__':main()
```

Supplementary copies: recovery capsule (`recover_h5_coupled_norm.py`), readable decoded verifier (`h5_coupled_reflection_norm.py`), and exact report (`coupled_reflection_report.json`). The embedded capsule already reconstructs every coefficient and control without these downloads.
