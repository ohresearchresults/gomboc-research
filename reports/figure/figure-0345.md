# figure-0345

Historical AI scientific report · saved 2026-09-09 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Quiet Raven 29 — exact C792 own-centred successor

## Result and scope

I constructed and independently audited **QR29_CONTACT_H155_C792_R100000000000**. Its actual maximal complex has **(V,E,F)=(243,396,155)**, hence **C=792**. At its actual uniform-volume centroid it has **strict (S,U,H)=(1,1,0), weak (S,U,H)=(0,0,0)**. Both full exact auditors executed successfully, and a fresh replay decoded from the literal source capsule below also completed; all six generated outputs were byte-identical to the first execution.

This is **73 fewer true edges than C938, a 15.56503198294243% reduction**. The requested **C<500 / E<250 is not reached**: another 147 true edges must be removed to reach E=249. This is a new finite homogeneous positive endpoint, not a minimality claim or a verification-only handoff.

I used the latest attached journal's literal C938 construction, not C990 or the obsolete SQ24 assignment. The C938 mapping decoded to the prescribed 35203 bytes and SHA-256 `8864456e0833a2533cda3512bbac6d3d63ea292a3dcd1880dc1488c81788db0e`. I also executed its original two-auditor replay. No C990 coordinates or indices, unreturned worker results, or inherited moment-actuator bounds enter the new definition. The attached journal identifies C938 as the distinct 311/469/160 positive seed. :contentReference[oaicite:0]{index=0}

## Exact definition and actual complex

The capsule is a complete independent definition; no journal, earlier artifact, optimizer run, or parent geometry is needed to recover this body.

`GENERATOR.json` contains **156 integer control triples on grid 10^11**, a 31-row root-contact set, and 36 rational coplanarity records. `RECONSTRUCT.py` first divides every control by 10^11 and sets the root rows' third coordinates to one. A record `(dep=i, anchors=[a,b,c], axis=k)` sets

`n=(q_b-q_a)×(q_c-q_a)` and `q_i[k]=(n·q_a-sum(n[j]*q_i[j] for j!=k))/n[k]`.

Records are evaluated in deterministic topological order, sorting each ready set by dependent-row index. All operations use exact `Fraction` arithmetic. Each resulting rational row q_i is converted to primitive integers `(N_i,h_i)` with h_i>0 and q_i=N_i/h_i. Define

**P0={x in R^3 : N_i·x<=h_i for all 156 rows}, density=1; P=P0-c, where c is the ordinary filled-volume centroid of P0.**

Input row **106 is redundant** and is not counted as a mechanical face. Thus 156 defining halfspaces produce **155 maximal physical facets**, not 156. The reconstruction retains that row because it participates in the rational parameterization. The exact auditors independently recover every physical vertex, maximal polygon and true edge, including intersections involving redundant input inequalities.

The degree histogram is **208 degree-three vertices, 33 degree-four vertices, one degree-five vertex, and one degree-31 vertex**. The maximal-facet size histogram, written `(polygon size, number of facets)`, is

`[(3,26),(4,43),(5,36),(6,27),(7,9),(8,6),(9,3),(10,3),(14,1),(18,1)]`.

There are **482 integration triangles**, but only 155 mechanical faces and 396 true edges. Facet-side incidence is 792=2E. In the auditors' canonical lexicographic vertex ordering, the unique unstable vertex is **131**, raw coordinate **(0,0,1)**. Its 31 incident input rows are

`[0,1,2,4,5,8,10,11,12,23,24,31,33,34,35,38,39,41,43,44,45,46,47,75,78,79,113,114,153,154,155]`.

The unique stable maximal facet is input **3**, with outward primitive normal

`[23154297579746591122256969816032,155103334022750685093400135282535,49323073755394681977591936458345]`

and raw offset

`51722872277566901166500000000000`.

Its oriented 18-cycle is

`[92,133,219,222,224,227,229,232,228,226,212,211,210,195,181,160,129,105]`.

The nonroot degree-five vertex is **124**, incident to input rows **[28,32,67,74,112]**. Its exact raw coordinate is

`(-1757036047591610176150000000000,-13663244820792638781500000000000,23277562752193538913850000000000)/53131243712405535329128266944413`.

The complete remaining cycles, all 396 true edges, every vertex coordinate and every feature classification are generated in `A.json` and independently in `B.json` by the embedded sources.

## Ordinary volume, first moments and own centre

Here is an exact finite arithmetic-circuit specification of all mass quantities, avoiding hundreds of thousands of expanded decimal digits. It is evaluated and reduced to exact rational strings by both embedded auditors; it is not a floating mass prescription.

Let X be the lexicographically sorted exact feasible intersections of independent support triples, as recovered from the included 156 rational rows. Let each outward maximal polygon have cycle `(v_0,...,v_(m-1))`. Form the **482** oriented triples `T=(v_0,v_j,v_(j+1))`, `1<=j<=m-2`, over those recovered polygons. Define, using exact rational arithmetic,

`D = sum(det(X[a],X[b],X[d]) for (a,b,d) in T)`

`R[k] = sum(det(X[a],X[b],X[d])*(X[a][k]+X[b][k]+X[d][k]) for (a,b,d) in T)`.

Then the exact ordinary volume is **V0=D/6**, all three raw first moments are **M0[k]=R[k]/24**, and the exact own centroid is **c[k]=R[k]/(4D)**. These finite sums, their complete exact inputs and both complete evaluators are inside the capsule. `A.json`/`B.json` emit the expanded reduced fractions as `ordinary_volume`, `raw_first_moments`, and `raw_centroid`. The translated body's first moments and centroid are exactly **(0,0,0)**. Its volume remains V0 and its density remains one.

For orientation only, the independently agreed values are approximately:

- Volume: `0.4778490067647064`.
- Raw first moments: `(-0.007114768882504401,0.0035356206841435345,-0.009759873852793864)`.
- Raw centroid: `(-0.014889156996841315,0.007399033238724466,-0.020424597968453334)`.

The filled physical polyhedron's mass was recomputed after geometry changes. I never substituted the normal-cloud centroid, a surface-area centroid, or a prescribed reference point for this volume centroid. No post-surgery compensation actuator or finite-capacity theorem is assumed.

## Exhaustive mechanics and independent checks

At the exact own centre, the complete census is:

`strict faces/vertices/edges = 1/1/0`

`weak faces/vertices/edges = 0/0/0`

`zero face-side primitives = 0; zero vertex maximum-escape tests = 0; zero edge primitives = 0`.

All **1584=4E edge primitives** were evaluated. This is not H=0 inferred from Euler, simulation, or a primal/polar score.

For an outward-oriented face with normal n, consecutive raw vertices a,b and z=a-c, its side primitive is `n·(z×(b-a))`. All side signs must be positive for a strict stable face; all must be nonnegative for a weak candidate. At each vertex a, the exact maximum of `(a-c)·(b-a)` over every other physical vertex b classifies instability: negative is strict unstable, zero is weak, positive is an escape.

For every true edge a--b, set `e=b-a`, `t=-(a-c)·e/(e·e)`, and `p=a-c+t*e`. If its two outward normals are n,m, set `Delta=(n·n)(m·m)-(n·m)^2>0` and

`alpha=((m·m)(n·p)-(n·m)(m·p))/Delta`,

`beta=((n·n)(m·p)-(n·m)(n·p))/Delta`.

The four strict tests are `t>0,1-t>0,alpha>0,beta>0`. Every weak case is also tested with all four nonnegative and at least one zero. Both implementations clear positive denominators before deciding signs.

**Auditor A** enumerates every independent input support triple, uses integer Cramer determinants and all-halfspace feasibility, constructs maximal polygons by exact projected monotone hulls, verifies the oriented closed complex, and integrates first-vertex fans from the origin. Its edge cone test uses Gram coefficients. Six exact nonnegative normal-cone representations of the signed coordinate axes establish boundedness; h_i>0 establishes an interior origin.

**Auditor B** independently enumerates every input support-plane pair, clips its exact intersection line against every halfspace, and recovers vertices and true edges from the resulting intervals. It constructs maximal face cycles using three-dimensional supporting lines, independently agrees with the clipped-line edge set, integrates different fans from a different strictly interior reference point, and uses cross-product edge cone coefficients. It separately compares adjacency-based vertex cone signs with all-vertex escape signs.

Both check positive volume, exact mass agreement, connectivity, oriented two-face edge incidence, Euler consistency, maximal polygons, and all strict and weak feature conditions. Their canonical complete output bytes are intentionally equal; their implementations are distinct, not one importing the other. A source SHA-256 is `ad72cc198140249c1e52a615513354036c04f4c718333a7beed64fba4b43d7f3`; B source SHA-256 is `b0cb62d5486b32d020b60f717f3dfe9d07c6c9a978492928f54c3a38f396fc24`.

Controls exercised both implementations on a regular tetrahedron, a cube with maximal quadrilateral faces, an octahedron with nonsimple vertices, a weak-equilibrium tetrahedron, and a translated box whose exact volume/first moments/centroid are `18`, `(9,-9,0)`, `(1/2,-1/2,0)`. Six invalid-input tests rejected duplicate, zero-offset or unbounded cases.

`EXTRA.py` also constructs complete positive witness forests on the physical vertices and the vertices of the polar of the own-centred body. These are all-vertex/all-facet witnesses, not assertions that every chosen chord is a true edge. Every path reaches the sole appropriate root, with strict norm increase and no cycle. The exact floors of minimum nonroot relative escape margins multiplied by 10^12 are **199581 primal** and **198214 polar**. The polar here is formed from the actual centred support offsets; no separate polar mass centroid is substituted. These algebraic margins are not manufacturing tolerances.

## What produced the reduction

The useful architecture was **moving exact contact planes, with transferable ownership of their dependent coordinates**, combined with genuine root closure growth and distributed rank coarsening. The normals and the physical centroid moved together. During floating discovery I allowed additional critical pairs, then repaired globally selected positive primal and polar routes while preserving actual support exposure. This was not a frozen-normal, fixed-centre, or single-support deletion scan.

Root contact enlargement alone did not supply the reduction. Relative to C938, facet reduction contributes 15 edges, increased root degree contributes 23, and distributed nonroot rank contributes 35. Equivalently, the final degree excess is

`sum(deg(v)-3) = 28 + 33 + 2 = 63`,

so `E=3*155-6-63=396`. C938's corresponding excess was five. Every counted saving is visible in the recovered maximal complex.

A particularly useful final operation closes a five-normal physical contact at rows `[28,32,67,74,112]`. Keeping `112` dependent on `[28,67,74]` and directly making row32 dependent on the same anchors would have created a dependency cycle through a neighbouring quadrilateral. The final exact chart instead contains

`(dep=32, anchors=[28,67,74], axis=2)`

`(dep=70, anchors=[32,74,92], axis=1)`

`(dep=27, anchors=[26,70,92], axis=1)`.

The last two records reassign ownership of the old neighbouring coplanarity relations. This permits the additional common-plane equation without freezing those neighbouring physical corners or introducing a cyclic recovery recipe. The resulting degree-five contact is real, not a numerical merge of integration triangles.

The distinction mattered in practice: tolerance-based hull reconstruction occasionally hid very short true edges, and an intended coplanarity relation could cease to be a maximal exposed face. I rejected numerical V/E/F as acceptance evidence. Exact reconstruction exposed these cases; the final contact completion was imposed algebraically and then fully re-audited. `EXACTIFY.py` in the capsule obtains actual V/E/F from exact Auditor A before setting expectations, specifically to prevent a floating incidence count from becoming an acceptance condition.

Other explored directions included fixed-normal type-cone coarsening with physical moment repair, simultaneous support fusion, and coarse global normal clustering. They produced additional critical pairs or failed the bounded repair attempts. No lower bound or general impossibility follows from those failures. No failed floating candidate is promoted in this handoff.

## Observed cold replay and output bindings

The final capsule was decoded into a newly created directory containing only its **14 source/data files**, with no prior RAW file, mesh, moments, report, or cache. `python -S REPLAY.py` actually terminated with

`QR29_CONTACT_H155_C792_R100000000000_TWO_INDEPENDENT_COMPLETE_EXACT_AUDITS_PASS`.

All six outputs were then compared byte-for-byte with the initial completed execution:

| File | Bytes | SHA-256 |
|---|---:|---|
| RAW.json | 16787 | ec1c23429d88674e022c4d1e0ab2088c25e5381c1f1c457a2d7f9f3a0743d745 |
| A.json | 523813 | 1bf1b155dba32adda76005922408b6b5bb13a94b710d980e147845285d430371 |
| B.json | 523813 | 1bf1b155dba32adda76005922408b6b5bb13a94b710d980e147845285d430371 |
| EXTRA.json | 473027 | 70a959487a8bcfe9c400969d6f86d5defb6b6ac29de43d2e087ba92d65e1bc83 |
| CONTROLS.json | 896 | 6c32a17aea063bfb45de36cc03d427e9c27e3b00473c40c3f2a66e9289f594be |
| SUMMARY.json | 1190 | f21354d9531aa185b43196253e171d9a69d4586910963c81d59cc30faddaf173 |

These are execution receipts from this assignment. They are not external peer review, a fabrication certificate, or a proof of minimality.

## Self-contained capsule and runnable continuation

The complete capsule below expands to **48909 bytes**, SHA-256

`23f037949be6b1bcb90d920606a2a72722ff56e86a29494d33c0268911ca9139`.

Its whitespace-free base85 stream has **19845 characters**. It contains all exact controls, all 36 records, all 31 cap indices, the exact recoverer, both exhaustive auditors, controls, forest checker, replay wrapper, and complete numerical continuation modules. No helper is omitted. Exact replay uses only Python's standard library and was tested under **Python 3.13.5**, with assertions enabled. Numerical discovery used **NumPy 2.3.5, SciPy 1.17.0, PyTorch 2.10.0+cpu**, float64 and one BLAS/Torch thread. Numerical optimizer paths need not be bit-reproducible across environments; the exact endpoint and its acceptance do not depend on rerunning them.

Save this Markdown handoff as `result.md`, save the following decoder as `recover.py`, and execute `python recover.py result.md`:

```python
import base64,hashlib,json,lzma,re,subprocess,sys
from pathlib import Path
s=Path(sys.argv[1]).read_text(encoding='utf-8')
m=re.search(r'QR29_CAPSULE_BEGIN\n(.*?)\nQR29_CAPSULE_END',s,re.S)
assert m is not None
u=''.join(m.group(1).split())
assert len(u)==19845
b=lzma.decompress(base64.b85decode(u))
assert len(b)==48909
assert hashlib.sha256(b).hexdigest()=='23f037949be6b1bcb90d920606a2a72722ff56e86a29494d33c0268911ca9139'
r=Path('qr29_replay');r.mkdir(exist_ok=False)
files=json.loads(b);assert len(files)==14
for name,text in files.items():
    assert Path(name).name==name
    (r/name).write_text(text,encoding='utf-8')
subprocess.run([sys.executable,'-S','REPLAY.py'],cwd=r,check=True)
```

For continuation from this exact endpoint, install the stated numerical dependencies and run, from `qr29_replay`:

```sh
OPENBLAS_NUM_THREADS=1 python CONTINUE.py --generations 8 --out next_contacts
OPENBLAS_NUM_THREADS=1 python ROOT_CONTINUE.py --generations 8 --out next_root
python -S EXACTIFY.py next_contacts/winner.json new_exact --grid 100000000000
```

`CONTINUE.py` performs coupled contact-coarsening trials with complete moving-plane constraints and physical-centroid repair. `ROOT_CONTINUE.py` propagates root contact closure through existing coplanarity records before repair. `RANK_TRANSFER.py` supplies the complete contact-equation ownership-transfer and whole-edge rank-replacement operator. A numerical continuation may produce no `winner.json`; that means no numerical winner was found, not an obstruction. An apparent winner is not accepted until exact replay and a fresh source-only replay succeed.

The most useful next frontier is coordinated maximal-face fusion and higher-order contact architecture with reassignable or coupled coordinate constraints. At the present degree excess of 63, reaching F=106 while retaining that excess would give E=249; at fixed F=155, another 147 units of degree excess would be needed. Those are architectural accounting targets, not claims that either deformation exists. The present finite body is a new starting point with real own110 mechanics, not evidence that further cancellation is impossible.

The supplementary [exact certificate archive](sandbox:/mnt/data/QR29_C792_exact_certificate.zip) includes generated full rational reports and the observed replay receipt. It is not needed for reconstruction because the complete defining capsule follows.

```text
QR29_CAPSULE_BEGIN
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;J*w#!d(D8h=gSFk`Tl2pSN{%n*<|*@NlGizFYmEZJp^~vaUo(9tPWwd4pXMFk348_|>@S
nzFj(084|E#R{}n5&^y24ge2p=TB1*%tp2j<zk5gAO3`W?8;mC=^`nj8|Qi6Q4@~RBq5uYA7pZ_Um0bU&)X$sG1CU1tp4QfFI^3p
O96F>2zVPUvP|e$Q3)I5*EaT(^Ef@~+=)xx1g!lCIB^7=7!MC%w#1Mg|5R^X<b1b^A~6y8*?ggMG-yB4c8TcnoNNUhJXpFEIQNl=
didAbZz*^Z-9ueHx67=&R3G9@f<nMug8I<9j4xvi5{sD2f$Df!D2?PgX&$QyJ~cLDs~_~qe&x9el>m;#NpW7;%Q=^8wjPx>9sxU&
QLVRFhlxnED&*Uy4+$rDXL#;g;PfkRb?fM_7(K<^jD*kWR`Bffn-<na)C_N3E-w;g{zIFY#QNZmdSnCwo#T0mPJOqJ#_IMVWt7VF
aa81O1SV6%twKS=P=o(t`dZ;nZW?$*I58}dn>$ji{-N;+lIhjDC)_jPCy48Zcg#F}Wb0xF3Q>1Da?G)6DgTrJF4>z^7>%rZ4hLV8
9RF)bCW+ka%&p{Vy4+IZ7~nhN3>VhM!xNM^@_?g==I1G(T$%=?-;6X68^TTSas6<_UQhZ|HNj0qMQvv+P22^?6xmNNaY4E_+#7!0
)9<n%f3CWI7r74Wm1LWBO0>=RY~Ry3URrp!mx;!!%@)0IX*61=)xOCGW+@;AWtbg$Qt2l`_%Ys-CPYyBODKWHhp-vh<nF+`BD|Dj
kVA2ni1ubr;lB+avB`HMMH##mKXt=$a)I*+$|f$K%eP*;Iy6XI&)$$tQLnB&QnWO`G0NU(2_a7PlqTd5<G9R8m2Jnud0j8i^8jlr
Mc$k9vIlHACge(dhJ=_jL9;YlD&l5XEdBe|v1=pRi5Nr}mu^q*M|p{DI`CS&?xey?mGi6J%&9LwS^3seF4i+Ox&-!X_So>Uh1K7O
W#x;0?n8|th-xR28r#o8x@JJS)slPsf4>!6asEc@jYIFS-WhCTq#g)llOmQ$XubyXTA83HMskrR?43otKuzCEZz4v_TIlQcR5Rl~
u<-$|(AQ3*n+5Uho?y2>DrrmRD&WyU_z$&2unr<PeIb<)-FidR4DSU4pV<`LL_*<8ia`k_(=8tnr!+H&8h++8oiT6RvOjlRP)gri
H1Yo-i$=-UXbmD3k@?k=l*AF!hy81M04zTA;xlj`tfc%M1#H-%YFobW5wWHz<0e7>aL2xAVL}vmfeXWwndLl?b5d3nJYCN=qV)Uv
`2VZ+E}@qNn@U+NmRTnIwS|c9initF9B$b;&~~i3ZUtx(3^KRgG_CcvX<T%gU(zmwyu!@{-f|oRM8!u+Uy>vmypYc1pN||Zt1>+Z
{Dqv^o~9U{yW0VL0WRc9i4~Z=_$qfMHI$HIIf7?kbN-^PUsCWY&fdC`nLWB%kSN5p?{J&fz4wWKxM!MkdCpHzvX)9<MS}~Z!IG!B
zf?6A8nDZCEnB_344IhxxLNq1j$iX-f;5>VOH~3E&E`FV`kS!ns;wQ>tf)?sEo)^Rc^>;wiNuv}eGh!5>+iT*lCpN{>k*r~4x;1^
hdqc_;R-2oL_HJ#Z=iGkN~!B{`tnpcD>z9Wy?ZEMZx)J5wd59+gACalw8Alf&g;hA#(JH4aA$b27vdZHJj{lSwZmkpY7kz1WSx^0
D&$^fkhsp?t<lpRXaA<?x90D>A&b`~=&5%c`P>|pHSCeG)T!)^4{IF8Cdi!7tU%cm@A7SO_3OQDX?e?@N#qJHYcUj0Y*XOO0mL=e
7@BYMeV8kqp0~$U`5Hi&+u8whtUjpth~;#q;lM6l(cPcHVpK9$cfF*Q8_8jRG)G5HK<yQnibm;liI~BqJyTSXrr@G!AuNbvot8+B
##mmC2geMv>_!C|9%DD~o+z+h!#@g&>f`t<Qf9FvJ`bgHefdcJo!4$vZ@6$*&@C7u2D^Z}XGiTIxDGt^Iyc&~MrVJ2bhSRd1&)p*
Pg1rE*S^<1m(Ii=m`$j|Og_*W=2iK4k`#ReX8b+CfqLfeccGU47crx9JYP`;c1GJM$~CN5YPA4S1paxQ)}smv@zIOiQqg_bUb6^E
+uROz!7P<A)F;|2o8=}g6HBPI)XUVDc2d2FuOJ4}Xnoim5zyk!vbRPsS)I1H8CmhmsoGyUWL1<(UA{D+@}~F(eL6q&G29*qW9_hu
z~5f07t*5ww1t9=bhKo`&Pdy8@Cxd+MwcA*_dl-$x;ET`MU*u4x>NLDkP1e!<3<#u!57*7Ss-ECgulQ`o^bdZx~8;IMnle=d&nKj
bhBq*BcoJZy$=ZZtyA#ABFt+|-kek^^#B0b!u2s?7AC*WS5m5-?is6kL~8e1OUI^%us%;n{|oSL6k_xIvC=HIJ!jZhs%3G?k7bH+
xK&wzc>vqp+?SP_GT&wK@wJU`SU%^0s;x3sN3a6)#meNep(e$lq}a7ymGujr(d%1gerGgcHzb4U(Dpg2*u+dW%4wp0pkmUHOU?9l
nAfdq-Dw}E(rZ!tE5p@UwMXfBUsggl4={rXo;meW)G3Wa26egkiYpqOo&J2|b*x6~_?=|pRrGiXPle6EqWz&oWM_4TMPdR>Baqhd
sDh7-pHb}!c(Uz^_~@GobJ&+^wG&{0Y+9~_1VYMcKR4-NUEaOCm<@dUB7!*e42jfB<yjEyeskC;6C<_1i#m($|51zMV?2axC*p9E
7qR`2l}1Z|u^@ppA98iCZ2FStBmsf2x1v!aGhg59xH{xKYk&!)O%tZC*9xZ!2i8FHATb})y&U*q{r#Ofl{f(@9w_ttIZa1*%Nu(g
IwWeM-CmW`R~=GTy<AM_%>Nk2LZfS)VkEHA#-gn9=Fr-+u1*yn27kE*0X;B0PYDv4rpK5bi+J6<Xen~nC+Muh^ikc!-<(B}FO-iJ
j;I#eFwRKC_ixE#EPFgR$47aFEMpdw44fZ@!FR<IO1D~I1p<-~c@wVW+NT97cJ%z44?}Xcxjg^g#5xdguX-NW8r1}sN9Ds@!78Y>
oY2%Y25mMaf@e_Xv<)W8oTgRdf`*}8%y1e)l2T=n%cLLMs?R=(=!ixwgJ-(QH@2YvM4P{aVCSbflUQ9aB{jp+AkX%h@`m<Iz=U8j
h#)m%Aqo$F{6720*L>|Aw<A=IU@Mki`D}O%@D=<a0l?x%1^4T+rWMO%hJv_}-?T54pBdOKG1ZL&^=!a_(ldpyv~`x3Kom4j>fgz5
tXYt1g8r$W`t5yvb1PWoe(6Rudi5z57N776BAiekLFCSolBMmFczoS{56zN6dR<<*?a2yL1zWbwNOYc{;W+Z63rB?J2pT6zCc(sW
k5{-d(V&R8QWquF^rfn^OBrM~<8(%Tn0k&}Kv|d(#mpsOb>5nl`=IOADw57yA}WY};O3^WXrFQUn<~`E8?i1zGAvJ81;U)Hf6F2h
RRGn?P(>FE1H4?T(&5bABblKHuLBNH;~{3K;D?=O?T?XQ*qAe6;*EqDYMnw1`07Fkt|B!9X<8}d+j@P<?kWJeiBbx1y#QZ0iX6o?
vTW5g_#@^Gu<>{EF9`)`xsM_=XFT&A5A?ZbQTbGf?AdkeHGv`$_(W<*u=Nh$sobU_Q{>;SK*7Ze-&3a1+@u(BPzT_X7izsd&h4wk
3$^z(2ebCJ-bf7JUd^}plA)K0^h8Ly&Wf)f0RE3h&?m}H{f&?!U$uKICryA5OgSWroj2raB*1YWe1WOZ@{29<6G`ZwAmO?M^22b!
Oler&8)m}5FIdJz3>co=lt}&WT>tm;%oW0SW??uz;JV?U8*brJ*D6seh?2V9M+kYd?aQoVeQR0KfF5!%>fJ<uBCpDmE`mV%zEZxX
FALgSU1uyZNxm;D0pl%_bQu`43o!CX_?<`dtj9y6Er7i`WIk!E1PTkb63fZWG-|CdQVsVu^ZXzc)27=%gsfr-yb=ih!8#_s3(qYa
L?K}C+}f5g<Md5jk}d=W7xEq5_4>w&gCJN#8+{;r-rT8w`cl<^*6MiAR9*)&wusS(YIO@6^A0O!^(ECX^-1y8<`hz4Bw3QbTz7+9
F^4gDi5p-(CrAU(F#k~u>k_D6(x=uMuM8h)nwkrE+t~JIEK_3sSwx<RM}5X4pO~qyJ6@yPeU5+yQln;D!zgNCaC)5B{y$K~wfEo+
tRgwj_>(05&U`<-?!k!AoRk&bGaS250Uv!RPB!)TMddrsk<Ag9SZd7`h16>0SnN#BGE<2+0<sxcYU;8=C!~uWUpZ&Fqp%ZM(cNCs
iN55JvuP$}WF{w7T5vM6&6|GOA;SQqQr8lND6c?2Z(+@d0mG_m+^3Q3tY<gv_1;e@*MZ0`mcpyxBE!X_&7Xb3)Oow;1jn)wXRcC1
ln(D$8qLrsK(<J}D~B&kf#jI>hjLJRNg7y4kx9vl$|kZS(eTP4y|zB1tIS*51P6+!Eh<ol4i10Q-Xnm?Wuopf;BWq$;GunoR{C$Y
Jke!%j!j+R0ybm-Hruv+pg;|m-U_xP`(?Vk0wa5!J#A3zlA$sc3DtaYilLryLDFg7k8Q+)Nn(T=5vbLBwoNh0_wL#Szi6@f6`7G!
lGB5c(?~8+i-`d8Kvaod_GVC#{xphggY;K0(gA#(*#H$#g27WFJQnS`R4U`9@-l`>8Wjj-d;xm$>7;%?d3AJ}Np%>nhR~Eu`}<uI
iF`H^%9+R{cU6wv`y}NlH;Z2h$|sNyUz?FT$2+eRCa9WBtZCa6(oT9BwphN!9n6;D0Gb?KUqyj8fe!FiOGifn-tjfYf9d~#?{p}`
i8Xq#ychtawUPRTAOD56oQ5ch2z&9KfBx4k&NAS+ojGho)8gQKWlqR$Rs~l4O9xg%6dI>}cOUzhzx*@KOok&UYoO#?I2c{<RVAE{
;hy=2M~DYZ39#kPLX%=xk3NH0z@o!f)fXlnlDADF{u0k2Fe*=ogb<#e_#FS#x7z)pY~hLWz1H&X216*v2Ib3~kEU^bY*5-rtwB!@
{Eawfb1y9>K!ENPGzO4rUN&=VuV;jOc-yrA8ug2^L1ko$pl(`$(Hd@qW8t9K)xIOsTG4&zA>WKzOZ&*DR_(C>D!KzKvlkFI3EL!K
-NF0Z7m<TPK^Qzn;@_}Kyh#Lk@!Q8n&q{F2w@?P_)I?M(^}uNv*aQp;yQPb2q&siQ=D}51tRg&*lFTQc^ocg6EJ_|g^|WOA%TqfD
f(Z(@U-0yIyYQnhXR>J;k~iVlY@j*RR~KOOQ<$y?Y-tOfxUg&3pt=WG3$F}rZWz~<q(NP<5~zM89r8e~LB#Q&2Z3R(!~0TzbIZca
xPRcmqs2*<v*-5|5936QIbetF0*?f8yAy7ai=k^I=Y-!`HYTJ67eaeDmTSYa`oMHXi$ej4`)%tSFA0A4g#wea-pGU}sD_d~qyd}`
2GZz$6qZ@iS}wO9U{%)^Omys1??jbSRmRqI1e*g*iXL(tPa-n=lb)UTeD?My7fN#=Z}Fn@qI_JXE&sF*?fnY|U7(wAbJS&^uFTZO
L6ObP`(G=5vTeH+hn(+1+um;O`fU0Og!ylt_IaHz1ppeaVt!8GTI?1t7ECO-&6CIKM9f-|LC_mb(*z?KvwO>Dk)=BzU9bKJ8=4CT
@1dtsqI{*nq5+vA_ZX3lU$j+Tf8IETOa^NUt4T7*f?}MG1g+N&iNSX1b3QQEZEA7F2<zr2cQ4-*E`ROei3n(57g%sOvi`Hr%Q>qI
xAweo`&mF@Ou7<&IGQ$;p&R>~H33uX&MJwYSQXKNBE^bL!%i0IWvM%t)pPS7-}zcvtezZYJ7@RJg&s|UKi8Edun>$bzaqzvEA1*6
K?}Co`LSW<W6}^*GGQY+m*9x+QFV*_HpLH#Sc_UfwSjs@hDR$ShA;-d!!yvMw3mcHLErpUbKg{{BuS|>P^+fqn4d~Or^3$r=+$Su
oOTXYa4`R>wmtgirat9vUuL`5Hug!kew3f&llaR5f^Jm6&S7Fcuu^TV36Nax1F03Uc{I>7JPT8&+zaYqJ>Bp3%OVO*L&04Kv7pZb
0bHE?xE0l=PaT1{LN7YTfT;~x@F0$l{;$h)2a%XnL^;ngQ4YeAlCM*x<wX*<>@%J<b7vy|4o#86!dzZ+HKSVS$E6S2jRfM$61Q%h
uV-W<W=%a{x)SBg4}Js6M`y&#_~GI;O`4F83pPVcYGOuuW+-oujEk(E+zX5Gv_P}DPY>h|X+2uo+c1E?bDb1XJ*^a>G#L{@ex<#$
b?4RUGK8o9IHI4K>A|y4CTU&ljP_&d6`-z!D1a_^*wP(XzoRuKJizco%Wd<f3X3lyiED{UUri3|ANFS8?-loa`R|?M!23ZKjOghl
$_fBcA?>s~djFq0FdbJR4G1ZGe=mk^2xW^^d^nGIYsi*}+hU!xVT#;LHDl#B3NY&{Bh82!_|50xLvGFC>8^te*vHya;OSFRrL-8o
cgpFHT|o|i4o?}M&D`QROeQH($QKANH+OaB;qCcY5SgW#s=gOrOx7SuVgBe!4qy6NVGNlSiGY>y<B-2zZdj8Xm7|$>G*k3u80bnZ
7mx!%@3(lfl=cB?FRb<n^|oHckTU+^^{`%Z?~oW|b=Ds~G}{3rHUF8xo}nE}V2+KOj^dQryS}SY92~Y8u3Xa3ky4h-RPb;k;(r-U
H$H1mM&2RmWJ9+w-i60nN_t}+PNuZdw`dCUo%A!Mfg1NT<%S1X)VP|V{06(1%QZ1%of0ikOeb$syCSi~*k7t(h`zicun8Gj+oX{#
Fkx&@rXmS#gfxq;>?^2yUaxI+0D#nvJiMK0?Qp6sSeqS-SodgZjdVF?HVE9v2`Z3jg}g2r>V4pst=9)|o=n}|cF-NU{3Y1Vg;}-2
UlYjxD1PYDL*vEbe;TC^yBH=P@?HAoP>DT7HcvB8p52HjOPC=y^}is@lj%MXxx~$d*%_isqJAh0%E08@jF(BHb{48sJwP{(^*fN6
L1q=wC@RX}{;)mx=*Gx<UqU%v5C<a}z%eO!<)W-pc8~0dpT3nHIw9jedi`Qu9uYaQZXs*+42nd+w?O~m1IJyXldS?2W^ve~Xnltf
j^+N0?ru&|aMX%dYO<naZ05R~&vAZ2n>8@5AJ;SKgU6d6?mO2WN-m&xDLhUc45rA~31`+J%)rc@Ec9vhQayW5<zCBm#F@)-8C}bT
0lq!r6yWD9ps$<Q+R!p@#}i+l7N(c`meFSgY%2>ZrD&XZ&#lEJ1+2b^M~BRk^=#mV%`eS7B0!(^F)uOfAyHFs$ldP=lk&&E@Pj4h
V}n%`<slUlEo#g431?<ot)uaalf}*R0!cMZI+wU0zB$1Dc`r@|QMIG*iYOnAXW_rh4dB+2i#Z<KU-kmSkBXSD3ig$QdrGG@C`VY$
OXU1ZPZgsP7N!4PZnY%cV>)Z0+Nz(|jCo-+4JKbOeHIbs@fxo^h%NaQ?NkeJf1+lXjOv@V=s@sXqMfcW{3<47aG{<N6M|-Nk4)Fo
Yo^GS6;PWKyihR2kEYHGGfOz6OUz2;U3LA&xh{};*(L+Bgpj{<=Z1D_gB_mD1nIU5C4@g4lZ$HC&SA>PM)S68g3)D&fs2qIS;$0f
MmB39sDjI_zgD~X!S8x$-zmL+``WM_O)Rp`zB{Qs^-4IT!Z<BUBQ4K~S+W6XnzY8O%bhvdPb(a>RR7By6w6M&90#cAh#@8x9qTjn
*--?@P&<%=cX1<LC>W{Q%&+agGhXr!P-|In%&g~xvsJd-wV!y^a3+dxH@1q$Kbjr(RD5yGV}MTBewQF_8cdwdP>iva_0;sC?~;I0
A|eZs&7sjl+I*nNMlYF&q;YKYOIp<g)0p|=hM2uLojKQXBCK8cM&molxjxoc`-A#MpE{!_z3`wkH5&D*GFOF_6$A0s6yy^^lAf*b
I8VIxxoL#}375n}df5$hl<H^hNKlP%)F*r!;cw*uLm@Jk8-}4_q9LxO(M0#5^wF(DWELzTS*XY7ySF_>@zbsIkC_OsiWkcJn}pQP
>|F8Ex*qfrjH-t>X^&evKkY-DmJ)(d5u87_U(1v~l<03OWox>i>KooDGgYk#q0qXHk2qsACR#_NRiwwOtx!dKCV<6h@R>=GqX$WT
H^;X`Z$n1Fpx#B*)A^L`JJw`Y#ur%^t=(>OBKY&t^k-A)@DuYA6JvmO`SR@X4m+p+1#+{p&O7VQODaZVCdkoL6lG(f-y)dMq?FOE
kmxBPOw9D4JSXV>o!vDk{IXty-`eGLQWu`ZOXa8Zm?E?)=eWo4RbKYZ8673mMNIb=f<7cj^I?l^@h_=s4_BrrtW)6)ZF@uTP(;r0
LlYdNOBhb2t&dPuOU`%XbC+6&no9Vx7A&9)u>G=35XD0_-0IPN$nGl_4#D9mQ>s!&5i5m^E{K<u%@A(rba>x5-9IQ9N=9#~f&GYd
o3AgTa!8&z4Nr(7MXfJ!ooe#nB_n6p3R}{?%l{bjF>CMITy|_}QA3(}A<Z5)B<L)-=BBv0@BQ*Eys<2bke(IrjgF=2wPN}*AuJ_L
%P=k%@^}soJ4=RJ8=8FOp05<A`jEbXlGXu$U8YL3NS=A{jNrM`WK*^Kg+#M%UXqq?NqzUxXa(wHNK!_l`oY^KBY}*1iUgNXnP^_N
zIzv$!cJNb?<@wOtvkTv<9U$N`BrPHZ^{!HmJTkgWq6+0TW=0a499^9DMvE&1+puKYU<uHw2fW9086u$ZId3xTZR4s=$^hV@8{+t
3n)lJvezdbH7pp-hZ7|eZ)qzoIXw#KKgM;X30e7&DQqm+Zfql0<!5Y|m%|ud2=M<RBZoviBAlaYdfkZG=9(5XKRpGt^R(X2@(tO`
E+~WG0-iVAjlP#~g#oQNuOT)#Ey5W>Dm>MPPDM(-nGuGkx|0t!m(x}Jei;-D*^emerVdKqJZPPX`xw;nuS(@4;?VU_Y>t$gHtqs!
VH@VWsTX>Vo*~Gzf<^>`d#T-P+c-A<O{M91dx|8GyIJh9*XEBa>skuxd6~hQ{4$6RFz018FyE~;J?SNj+1!!P${fNr+@&3_{0L{M
OuO8dK6!R?gf2)*%h)^@aE=@j+r*2&wL1u!J9lpnMKB@oGx=A{wM;_gms1tTwEsIaB}6~WS}cUMxH9*RJc*|%zi~q;Mk&U{y338P
AO;T#=SBFC6nBuzk?cQjI#TYs`jQ9rqbSHMR^v2Z{qu!j=X1*AphcdZf-~K>Sr!`Jmmn%5PE7x>pOUJt!eA3(UIOS$O4dQ)CPx-P
B2-|g&+2;xZ7palf#-C@8gPzzmy6n{fh-i-!b8gj23Zj>-{>N6!<<wt4V@WR2s>qKq^1LsClPei9J#lBjZWCp4JRZ}T7?vv52kzp
p^^l)DE$|lP9`GMRovth@rxi~SJK#TenD^h9vd62#QBuP##CrS2$4_uRP-7isz90B)vA-pfz3=9SUJ^vE$t~0NbS3>NB$jZT24{c
{xG!z+iB?oHk!JzIweMf0IyoQ)7rdFLY*b(ymIMfLqi3@nr33D8Q?%XJfMOweq-Q?jLV6_mG84yrPX8S<k(K)_5RmW);c4}3j6Z&
gtkssyZ6&ap9H=O;V<~_#M5hcgv`$T?kDCq-Iu@$#hpYkqdH+?-p3N}`tVUEqN}%Bf97ML#+sd1&Lg<3H$c&W+1{Wz8K#GTjp>jn
QEwhxA^&bzp~#$iyRQkjjcS1dO@9dILyD~U9lBFDEGf4BXAZ#y4zpkFqR0bpxOGCA6qP|R#!jpB!1T|MU8M%=v}9IQUn+CQ@lqB6
%pyk#&2EwwvhUfD?u>;g1R4)|<3Kk?mWsYmTQ$V!43CXh-C+>|oy58#L^Aay#h;1XtXnjrd=sTjN+q%j@*)UE=@-5eBaNc*aCav#
lU?e^B!$cGA4R{e+uHTf^jHzcw(kaCiPOQ>I$6gJ>}p+h-blUg?P8E@S*=xTbM|V0E1J^I-AC%+4H_RHW0Umu24@Bw15pIZ;>;nZ
HY`?XDPSg9hXn$_yRhikZ5DJw-aSYji}=Y6n-BZ^U~Y_~)7drSUg~MxxPX^m5(@WYWG4JF=+KWw8XAN`RsOR1-3QK1CAJALnI_vX
kbj^kw~PhV0sn&f#;P3iiGp!le$T1&2jKWz9o{hBDEqYBEerWSwu~>1gNkFjM-tuNs5H6wcrBN%HFV#*{kB@vM`__+;DiX}N<AJw
l^q}ZrWx%|<5zfU`~1(}nB0C2ot7%q+ol^2Gj^uZ)Fia<;q!2otrW$PQwH+Q*OC)lq6rBcZMlLKMPgl1PDtZF`@?6+zWZll(0O-%
D%>Jf1O6#73N)=y^^2Crclp!4JxfKyj1t!@Fj0;<cn!}jo@{rvjdY6g!}5Gl)N+0+Ur34*Tm-f2P-q5iwyRjq2%Ql3+Qj$%1Vjv^
d|eo)+`t=dU}qXMKBo=AO=6(Ny7itiL98GnvZ%YE{|8Y!7*oJkYEh5o$(;a^fJY|~KHFxADBR3JcmC@Z7PU2>?`)dUP7fb#IsegO
tM_-ce{Dki3=w$3jJK1nMA0)xOp3ks8GFd=HG3Q8c%2v}ODS!H|LdL;_L&r!B91fl?&Y6p9%$sUepsl^))?KSr*4^otB~_a*Qt<%
AO*mZ-x3bRb#8GD1iOyjZpmdQKD%e+9TUnMtP1kbvC{rV9MgV}N+B)%-$X(M8r6`PF`_TTU{%75Q8UdN>!?luC~Vc2h|sLnRVO{?
s{-f6wx+oJJ^l{!{D+k5R%zRh`ShsK+7SEs`wcF@qT#7kUyG=o>u0o1K=<Nk_Ry%WfwJNQb}8V1o{rj$U~l~oX8<eeOb8L+Ai*EA
oozJdP1$+T3eM&~c^CMRrxM#B5-T41a;>RncF$+$%bpZG)?~Zl*lpL=aQbh@4^{h5&rw-DK=!c6h<@)acHYJdDod|alZnX%8>Y0n
9BuxTHta9J<FE~V3)kAwXL}`CxObDa=(gUg`ChSvq8US1%tB~KWg=p=wR;hc9`l#RQ6s4Kl_Ag+q2oaMSD1`h@6)*A7u)JZHbp#I
Prd;aBkysHnUHw3xoSI3cv6_OlQM5Rr8<aO|4uvFD;(&Ro*~<3OKGv8`32Bn%*kwF`V?v}zDSTY^$crXS3Op*e#vAuy?mY1ZIfju
?YuTpq~hE^pXX+Xj}G$Y9nmA_wY1i5Sna8s5aL);YFP>j!UkieMw!2!2#qz(Y_NOjwJi38;)=yw*@zeN7YU-zxTs~6(s9bFh6$8{
l)`eg5k=-29SXviD=+W1djR^#9J0|s>yuCkg%TR{jTm`je0^zc+F@J);Q{v64k}ygc36SX>hJCu_mMrGb}%|Bn01}7JtEggR=<hc
tL~!C5#^Zyv-$U%)aRLuvru!|iHG>3_)W*wS17~7Ii6$ID{!dr6~|9ohS9sqwwju8F**=J#VLPGY+^Kfnj~x(ZUHEi8cCQsp+S1%
iDjN9Rs4*+O`Z9`LVMStrU=BDkai!p)q<t4T8ACe?zD3A6Z;>$$7d(J7lIM3SKC0ZwZ;Jnd}Nl|*Pjy3L`yq})5WZN?$n(%a~;W=
ery9=hUAZ?`a8=vR4ezj2!v`C#*VC0`xP*Q37mafak(3zgAqfqcfEjg=rf*m-YVUR$a3AiaMI1T420A}1ztity7imytl47hlNA#b
OY|Mb@(?2SWjcYDxGxCUFua1RC2?CdBv?I3?2oq!@Ks^+?8wOei#Ap>=br^5wos#YX)Fw0qDkczH+RNyVHwep;%an`!xc|&E1#Hb
!X<H^AMgJ_NM$#k7t}-<BcZCz2d&60YxK(eucfMNFG>-7hFh5j5=ofJLIP7w$Ma7<da%Y8y!85vu403Ejat&>=^)U{d}3PFa;!?+
=t#C3e31CHpCA@=cJT}Q@!W0s3WY7ZTJm9rorBCV5?fiCPocUY8l<=7H@ag)RZjO_VM-`?P-Y>GN}`1#i;&P1_cJ$;(5G^i<XjE$
=*f}jk1ZLwx}YBg!nsx*PUpMSRm*KVh6PB#q4me=bOia&=|sAP?8Ko?o7bKbrSMXux)E3}mkWIbW(>c^oh=iobLlD|gYb%KMzGNI
>a=Y3J)UK-U3)Fz%+`jAN?FB?hhG@NgjDa^c~u>&Di54}z6ZxbSD={VU5TmUGA}lYU>QJgFc&r78t4~2uq|3oaLCvG_GCF;?-JsV
#Ymu2T?gGW!i(M%%`q4%UDhO%zG3%q0%ED3+H}DU{E;4=I}1oPbF%`^pnX`sq*(VhgU--Kq`gVcO=wYh_2%OXy5!3)PPmLKyW7}I
Phj}qQ(8HnvqiK`rb3wX3w7*$$&E+uIGnQH%fI;jIxZ5SDh<9`7P`?rP%pXhNpupS{*q8FSBU!WcMRA&qx|q)F8HAXVEeC&w0xcT
@g)d6D4*<)-wl_vkL+5IR`X?^S+vMlx{Rk(F#j*wAzkwi=gie$^ToLLNG1TxXRZ(wel|JeZ7M^>5eYmDkZk0VLtI_~hb$h1#m6pl
;!GY43jAwx%Q@wV6tI+r#?a(rChkp=?!Olg#oFoF_GvYR@%r=~W}M48guXw8BPH$O_Z$ZT_+|GJM6cz-Zzi99?$vnJ_0OxoQ`pZu
?7O)u{?8d3=wbjEfK0S?-!kH4?2&6go=G|PD?RZ;FM^?qLshPpsZ9WAby`j*_Y06JAPb!(xPWsAto(8?-R_9Sjy|x&0<l~gw54vH
(TF}mgvT(<1kl6ut~`|Asg-HzS?3$qvtVLEalk;I86P1z=@`&DGw#(Cp?~s}sh$aEzYM|kZm3%Roa@dJL8RB+vGRFMTCg9r-$-FV
CWtv)5&Un3qlL&-$R?zU#LpL&*rS`C8_t$@$1Qh|nVf03R;qKEfsF3WrBjSZ+q%>olC1wik_a6v23@N#!bup8T!>8Gf)!<5_qwMF
$zynQLX>rSVnNu>IZDn9xi->2*PtnAnEf`D?rGd(B9kJMENmGj`I!ipo>zp1Z^q9Y%FY8{?O}J+(<)rpninh3t1YArLE<x!$Z+t6
kVe@Ll8Rc|ZB=?sRg(lP$I#Zfna{f9Fc|g2s#5{XqLH2T#dTff%Fg9ko8A$j2Icv~cB<Vt3>CkfX(C@AnrYj!w}RL4k^O=D4ktB+
i6zS!XQ?IUX!Vnw@WGOQzDW$SJaHOIR2o$i#-?&-S{SO=QHyjvF#@)icv9HwOn=-kFSy~Q)g@Kx2O1S?sx9FNsXecjf{pi>QzRW-
2zHAw)5$CfcZ^T)b}sQKHWsayHC)Y%8_s3T#y_+e+Bk@U@b4EiLo$yIN06#NjMe=>=)rVIkGcaa39rI!N)^qV#i7ocaHh$B5s^*<
rO60d2g&73J>ZwUnGFfXU@O@sQ3<PI=12eH35!gn(vAp-2FX{FDI15Y0a~QUz^}<5MQsO6l|Ngt`yM{cdc&>EE^o2Yz+*FtQvrB`
^C;ih1h5!0Xs+A_&7eMtkC@p@NodlF8v4jV_+f_FuRE*itL<HtLYcl;-s_RC&ki8Yca|uVKlf0YveDZAr$eOwwn%PNq?KYPNE7ZW
E+)#(h>lWB9QvL%MJgiw+A=?|2&q;T6ty3we_R%sk~Fw|%p+o)$@f5_6p2S6C_nOKW2JQtH&FeRo}8leYLA9F0wS2iEuC*yzc5AJ
ugGVcNtVy1sbb2nos65;x_Yb>0+y_}i8raj{>#V>Ry4T{fMGMp79VbsLHi8%9NXh{Oe?}o7$hF^&#ZcU#7pwn*l+~y22Y}+ZsFR<
W}X!qa0TV9lrp|Pzf&JH<fvTjWrUXlq6E)0Z8!dL5wbloC4asd!U^Dxk#jiESS3;<^_fD$BVnQopLL1iCUNwz+_G+Tb3}TEH=l&m
fflUUuuXnIqCH<ew~r$uw6Y0S<I_lI-7fu#fx9F=J>h^ZGxs>_o+YOq)*J&gwV3FX=DWM*hADakj6gOWrk0_SKH=#Y;gyg|>e8;D
4pojT<(c_I2F1^kEwgSHWY^d0r|-CjQb|RuvX#ps?Jc&UypDgBm_eA`-qh)#C)c#XTIUs!$OWwhozZ=8s2_620|mx&9vRIk6oUPJ
eO%69c4vUC+49%IXHrVIeLBRApwOfGNjSqTUe}YJo82~3(T?{qX*(-o$e1h?D!IBww{{o`5?T5SAd0St<j51f#rhf82Xw9eS|Xgb
8}>x$j>zKwk`^gjjS{#XHvE<1tg&XY$Zrx9Ol8~QW&k~8g7c+9)`&~+Sx#PQXFd+=1|U4ryQgO-OK^T<mgb=2Ivpjpretdd7F>Mn
CK0^ijlqu|GBYV_y!*BJ8mBSEwmxyWsb5ay7uaeubR8)$Y#YQpM2<4XwSh?A^%Ye4dX^W=e}oluRA?LsGnCQ2ocmv}tye7f>4?}@
@4nDDAWnxiKxJP(5qc`_TkFVQP)?ir+7$|C71jsTjGrgWWPy~PHAW3_To#_j%rnVuzC)Nr;0!)G!G~?~yvvLft=Bw3<@bT!EVX0G
QA*3tORfls9Me~%7P>zqa7{z)33>GLCPA|}Lpv}kwnh_ZDATs`!?t&tU26yD@2B1v8eRgP#)u;NM+Sj_*~y1@h)ip=Zk*iR*|pK@
n(&(tse=JStf0y&(N@L+D_97u=KxHK_~pO<!(QMymwbX+mmmRZO&cERnDf(7!y`W8RCbTN0d23?<@Z&a-A`WL*}25DB?D9i>2Mpd
&f`Sz(ariEeEWjBw+pn!f9XrC3t~AQ9^>`b45Gd7aq;J7%59kTSr!OTCgB+8h8h4ZEifc}L4IhuW5}as`{Q`Ehl+lv(%fzRkXl?H
iVPcW#_@evUXAZth!5I+`pOJG{!zSDI+!={>kBz5B+d|h?@6ABzJu#tP9Jo|1T3s1bjc{V-(VNXxs!uj_t=+NasCA7<T#$;OsHO#
?P7VOJ$r6Y#9A{fE5>UW#6?!WDeXnyRwP1Htu#4)b$kP@NkOkEjcCYx<9n%I8>OB2RMfde!>s%oLY5V<{;f@WgxFr?fRfvC8Zc;x
gj-|1?$;;qJ(XdoCb_$>2u>pv#4AAqxn{l=8dlo@W8*ljKg<9EhHH8&lhkvTTlRYcqbF_^rAqCHC62}&nA3>BtcPfunuE^aS=iT(
NK!eo6G4gU1NXDyH$tCOrt$9;(}k8k{9$y@gfl#P32`gi;DDW4^Szwm5m(YFRjd=((;;IWypET)wnm<1no9r?v6@pwZ}zlotm*7x
w%VgUr=9z=tzHs;Z;JuQE)BY(zPUTT{RUW*7m%!4u93=xg*gJfvuDnq-obI{nqIN!_*$h@D$}qE+Hco7ZPGJ`Im7CT$9bava|rA|
T*;K1rUHPu4z4wBF&jlr7^t>}>xP`WBCTf|pC@~wZ4F|&^kY<1w+T_!@!Fai+9Na38*FEu+&wGsWVa&KmNS6lxltjH_Z(@rOigOb
Jma$MdVNyT5_q#U&hVI@%IGnIwvS3)SlUV&{JWH%d6i^vu4e)_M~acr#B@O8q>Vq5;^B(tiw{07e`*5(2|YWw7E{ruohtm#-KAe&
TieXLyVF!Z!t`F8+ZMm5G&_)7V&_jt;o$BkV>bB<yY4LN4gRTgep31nu+0U}m&Aq=hNC7MQ^TjM1x^pyW6j!Ai;{0b{rlh>5VV3R
ApE-_qX2c<2dLop2^=7O%^u|WW6@T!K~F9r@oR35TrOYo?bZ7Q5kNv-QrwJ=E=3g0Yr8qEsR2u@_?gu9IjN)za95&F%0;Ji-;6d+
M7a71_K%a1snGPB7Xe_xXZMKtjM(zpuILD95`5dQZ1Khfbck53fTHkDe!lr|`rSaw#M9$1s3b1!L(hxN@$3s0BflL1E;I3u?NKs6
I><fD8jPFrc_WvLWz!sFTf_oXBRD=~5%3{^MI)0${A;trPFPb@>aJkL%f`E#vOZIdmm=I%2nRIwU66wPUoUWOE~2oZpRf+9wNM7Q
FF<1T8fW>>WdeRFjbt=*QWqL%;(6s%W3xWI@ySP9UTR0dDJT`%LnrYs7eIdmWzH@-WzHlo9qQEwcq_@6_z{-+mE;>!>hsdzGPE^d
bmFeMVr=+6sm(pye)H_?4_b+jt+czeljX#er!+7V)d!*ON(wN&lMb;^jEt<Vii<S@kB<O$$5Vnk=JIziP41lEzBPH!BPh4V+TNj-
d%G~4{suj$Tv8+#d0Y*)g3*A0YZ@J7K4LYDy|PL+Mm3OWB`$dnr)oRrhaq_+=|&tN^^Strx9E*CbWw~V<zhA&pR-(ml&0GKiDXM4
pd*70Q#q5Dc~ZJg8)Lu@R>;r?r@iZPyX5Y^BW4AaprM!#Tqv-$DGWPKTiQG6U6ij7FIV6$;ah6i5wznV*H~RRJU>}C3}|x$-mYko
Z6#7lU-@p*qEIYS8@%786IZ$#tj9g-EDRC4Xc;(E=NglOOxKe?odVrc=SQ*yC3(boa!W3UUrfAR*|jd&2%kHE5XYH-ZJIM8=Wo)2
4~;@#ajA=X?Z(H~bM@C(1H_s1q}ooDOQX##m$Ap8{*MCC^3Ba6TSc_{cDZ$RuOtuLJEx<Gx!&brNY+W94|i<OL+sK&=U5x*yj%=F
UHcXhuvm6n0CS@!G=?z?_vhbJ+bP3nl?Kt9-|q((7qe{uW`_51!GppZ42on#5p_=kh3EVnk=9`Ub5#5qJ|=Oaa`e0~=>mW)w8D1$
>FHCN@pEv>I@+>j<>Ev^6$r>|8Y=jiVV4`Z3I})ixr>deURY$E{bk69w%2}77TA+B45?%m4{c#jjz_?`u%b;3m1NI>mflm0WpQgD
e)e{91P?GO04s!~0wkftXdtG8JVmFcVYP$^n=ZVcOasJ^s3k`si+FXIs_#3JJ<BwSbg{&hpEqX^c#I;kK*3XHOawsZiwe54cUgBt
#nlH+6q(tLrz@koecA1Ukr0MB)!Dp-B}!vZw{Zr8CB?=pZZ;_t8Sl0UTq7GA_^>_|7*haWKc#hN<*YU`o|eyQ80KGK$Q^MS<;&AQ
M}KMVFC==-y7Uyjf2;PN^(V#gNcL%jvkA~})6c4y=?Eu9hT<)q{w1vMnRe7JD}%1iApkQbWXcF?uvaROVIODN&aa0_nbI?8@_zU`
%&=EEPK?G`rA@3<duz4v36E#lGr?*vAmm=ef@b~d9`vcHR4^#(Kv|D6Ty0iHz7Boc&4ba%I0n<|4ZrmnAl?8<dS7U{@7y%4kreQ{
XpKH(DasvfB&XE&C+G=(mZE1wOxeY)x6p5LFQw8MO4O+ZFEoaiiS**h?uSzSlRA|&uf|(~+Q5Mf9RaR6usKU9qyRFmGSOMEJl83(
!HQQSvWt&CE^LAH?A)8cGd4|Drs%T3{dG4-^qi-XU2Tf{H8LPA)uj63P(waK?~_#uqnc=~lL&%<PjfXqPp!e=6idn~ll?CBjB0CV
%v^_SEqvE)cHd|lAl@!muz}7pI+kmc)yjG@z1EQ2b?tzqUGP4izg;sB(T$_s>k{hVkMUOyuBd7|GuaQ&^y4xf*d?%)p=n3?E|8{_
tQSWS^e-#T^|i^mut-}LFWz3IPc(aSzaJ1^8j9Y^DZ1PVdPL%aw~Kxhzfs~E8QXjre-A)y0y|nts9GH>SH2|l=z(<7eL5&+r!V`+
tPi*FBtQO*K$6)5K^`Uu3-epQB~HwVe46r{8{)?`&<!^YZKE0MZjiHqzt$ln^b~jDVYH{#2B$ul-iVqOj%O7KUx)S+&Pq|b0WJ(`
i_;|(&zLLMCXR1daC4>&C77k|?ni>P=qW+WG9zc>=(Ap?W<IHv^UQ3LCFUydH7YCSZ$u;C^OYSfYM7S{7a}m!TW;r`fs)h5b5l#d
uhANP*aKN*PA_Sj&CeGQN55~O1UM)XE?w8s4U~;Ajau1ge>G|Qvq{qW6H6Km)euE}3Ox(J7L*T}&3<Uj8ZT8hk|R=cPq10-JrN0n
$0QJjdJJOl!M`Y4OGUdor+~5kd<=O^-u@}_TYhB;;Hh9CV13Eq`l-w?jJmY5V+E|A{C`<7Q}c*cj}q#V{{>`ryvG_1g_w|W&S=uT
*{-OO7}NR(`|VCV2#Ad-FcT}BvA3g+rzyp+WodW!EvW6TyANA0e=M}f<ek9TaD~1<+J84}xq)vfD;gR}7v0WRyU4e!HG>rt<Jq{u
-+uVrNZ!0dYbX2c=%rS<b{^056W{1U%7dVr2=2Oo-eoZQEGXT%iKtP885U0gg$010VKpW_G^bEgoGh93VnLDaS5Q&#_|Jgx#rN_>
K!<<@caEdE1-5UQ0hFTs${HyB`3gnE$kvy}p`l?yqSBB&<NgL_j*57@%o@qgIE0*Xv>_k;&U~=4saciTR;|CR=FZN&a_H+nhr?p)
Tee9C!*UFEYW&aiu2?NWP^B2zo6->cFA%8k486Bre6+`{K}!JnV<%^dEumBYiUsE2r9GOb29wYvb>4!ggk=3LH~$Y!A}%i8BmH*e
pk%|s{Pj0|(9*d#8Fn^x*0p2Y2M06YEL`-eNikH<8GqKsETm#B0OYJDG3K_Ap?}}CJr-o*Er(dhJuSp)1TcNLXat5SW;w3;IYGbh
xBnHoddR@ir9nPi<q_6|XQp>?+-F>ESy62j6<^9~zyKJq3Z*!=qqN6SY{(Y4I#gZ@Z@MvT`)KEwW^d~vm}6>$t`tP1Mg$zv`!SJ%
1HYu<%9N;8C@^_nZ0TA*wahm`RJ#Rh$7;G1l@B{rd(~(;@g<Lh4J;5^I+RIH#=SmiTJDuhmzAZ6;M|{dmTvB8YGsTZ<ChgP#Mibi
Wc0`ZspPtv$4>+re3OSj#89PuZ)J0i+;d&<6ZFgUgFyIqvm_E5mrB&gS(W)l63~mW3<JE1$g&n34XvSsQRCtE4f1IoIk|6!x;6YX
Ct5~UvUx_6-+(T_h4;1TW5HTxKbTR8fyf4#v_hVhe==?p%*ko6VYgxpWiEOYnv|RplyC7|fC^bQl5&Y1m~ef62b8xe3HeU^H62T~
Kz=GoBw!cvIPqBRotS)i;|i`Lmp6(^*?Dyy2I3WfuUP9)aLV`!2;GEtRM<?r39$#jUq~%)YuHZ3+Cq-oaeUIp)W_6${gY{R3Smd5
?~Job<%#cRI4Q0kpax_;*yOddf~jq4Z$y+|V-@P?K^za^4{U_ye^bn>x(<FBq#n7g!OQx+G;Nj^VV1^uX=p!%p8|s~%3&*tYRHwJ
$<3Mm?yIr`vQ02`<AXu}$;f_TK<Le+AP|!+n@w2etPvmy++fdz?&Z^lO4m&g{0bbee{UwT#WLIK-!E+2-mAiJ8hDGDrU8?1SV2Vn
Qvjem9m{1?+BSW|gv`rOoR`dos=r6s>S|I-rwNY!fk(!T=4cH%s_A!VRcGvp2|hhTk}I4oG-$PNy*}~nngrS3o&#4a_|eSKKb#MP
Xlr7%Ong+tR+ztK`PaPcB};Wp>&)K)PqV3&{fL}~J20Oupbm+HU`|AedYgALci{=mAkUI}pTIHzQFuoqgU>P0&eO*0Ttn`;GSle-
-E|-pYf$|TNpG9>V$?vUlwGd2MlOx*g9JQc8FgEZwzoYtpLdSjGsWH37&8j&!t2zG{_ZsOqMT6_KS=l75JvcYKLB$SsUWB(-UNRg
2)YVch_coUGYv5&`E6C;Q!9e??O&Mc`;a~s54^b4s-#)M68mfIBN{#OuxlfA(>(D}FYZUSGP=;Fy<4#az}nJO+0|x+hz!&K8m$}A
P#ssgCD_jx*@0@laPFJdVZh(urHsK|haz6};$&)^?0}{VbE#o`X=L!{XKf;!cADa*%2TuSye-b`tfO~&K5KC3e4G^zT!JtdSWg5D
PZA|y!L>$veriDGE8ujoc53v?^N-3uAU*mnb5lX+I+z(e{OJ7i3&N_nvDmSXgewYPuc&s?ViNLvMAW%=5SeNJpK`vsf9m#i`g21k
{69|5k^`oc8<O^hfWi$v#qSi4x^u=z3(-w2|Abh`*Eh#w`|ci0Or1skO*ljgbLF4^DN%fH{ZB@}G`EA>hH@s69c60YXl49CxVK1Y
MzamJx0klw1fGxy?0YG;mQgHB6G?dfX;96M&wWOW^o*#|`_%IKi@NrAmcALRj=&ycTc8IW{r;c~U`Ed#DQI62&H`jg=<d@0CBEx%
_peZsq$OGsM%gy_<ySw2yT=9>?Ho}*dp9T24Q^MiPQA1w^5!;NEEk%&qL#K54tIt1W^e-kGmu}7_iJg7f0?HSyifWH(FnD`yspMF
<hEsxa(nLOza?zbZ<J7xjRYcM>3N>)-eOB-phykgUZ!iwhBP*3BfQt&Gk(?2L{L~dWis7xEVW+`@PPky!_<x^`SQ>oRTp+qT~3bm
Nwb0+E4!3|JdOxAI|g&17A{EN0PU>0Q%L9@hY4m3*V@czx$SP2EAtR8T3DygeA%`uHli2!Vq!>5&nWRc;FGKbS-II+-bzb(tRuBS
RWnxu5ZIX1>*9-G>eRDQq*tQ_Veb@&NO)oJTfB!whGUxi`%{iQl~7KQR+eLKP2|hax&DbjBS1SLYoEk-kZi%<kO(To4>syuYXz-M
U;qFBm|W_Z1D`o300G{6js5}v;wn7%vBYQl0ssI200dcD
QR29_CAPSULE_END
```
