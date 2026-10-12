# figure-0513

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# RH08 finish — exact two-point whole-basin access and a changed uniform nonwinner

## Disposition

**No strict110/additionalweak000 body was obtained.** This closeout supplies a completed, bounded construction experiment and an exact geometric theorem, rather than a claim that the interrupted long optimization campaign finished.

The new result is:

**The fixed-complement point-cover number of P49’s entire 41-face unwanted polar packet is exactly two.** One point is ruled out by a five-face rational convex-intersection certificate. Two explicit rational points see every packet face and no complementary face. Their actual uniformly filled convex hull is a new nonsymmetric, nonaffinely equivalent body with **V49/E141/F94, C282, strict(S,U,H)=(7,6,11), additionalweak000, primitivezero000**.

The operation replaces the entire old packet without spending a true edge, but it does **not** cancel the equilibrium defect: the new body has **five positive physical bars and six positive same-actual-centre polar bars**. Both inserted points become unstable equilibria; the parent’s unique unstable vertex remains a vertex but is no longer unstable.

| Construction | V/E/F | Strict S/U/H | Additional weak | Positive P/Q bars | Status |
|---|---:|---:|---:|---:|---|
| RH08_B1_Q2_G3, P49 | 49/141/94 | 2/1/1 | 000 | 0/1 | Unchanged parent, freshly reproduced |
| RH08_H1_POLISH_G4, H49 | 94/141/49 | 1/2/1 | 000 | 1/0 | Unchanged complementary parent; not re-audited here |
| **RH08_P49_QPACKET_2POINT_G3** | **49/141/94** | **7/6/11** | **000** | **5/6** | **New exact material nonwinner** |

The two parent classes and their 108-edge reserve are inherited from the literal parent result, not new discoveries in this closeout. The new construction also leaves **108 true edges** below E249.

## What was actually executed

No post-parent optimizer checkpoint or trial ledger was available from the interrupted continuation. Consequently, I do not count the parent’s 21 optimizer runs as new work and make no claim about unrecorded trials.

The completed finite nomination experiment specifies **43 linear-programming calls**: one separator feasibility problem, one convex-hull intersection problem, and one support-extremum problem for each of the 41 packet faces. The support-extremum problems retain all 53 complementary normalized supports below 0.99 and constrain each raw point coordinate to [-100,100]. Their solutions are rounded to three decimal places; the first qualifying pair in deterministic enumeration order is selected. The complete executable experiment was replayed and reproduced the selected integer points. Its numerical statuses are not used as mathematical certificates.

Separately, exact rational execution reconstructed P49, proved the five-face obstruction, verified all 188 point/parent-plane signs, constructed the new filled hull, and checked maximal facets, true edges, actual mass, every strict/additional-weak equilibrium and both complete landscapes. A separate cold directory reproduced all four expected output receipts. This is repeated execution of one inherited complete auditor, **not a second independently written mechanics implementation**.

## 1. Exact obstruction to one-point fixed-complement access

Use P49’s canonical parent facet numbering. For each integer plane row (n,h) emitted by the parent auditor, define the raw support functional

`q = 1000*n/h`, so the physical inequality is `q·x <= 1`.

These raw functionals are used only for visibility. Mechanical classification and the parent packet itself are computed at the actual physical volume centroid.

Three packet faces and two retained faces suffice:

| Role | Face | Integer normal n | Integer h |
|---|---:|---|---:|
| Packet | 60 | (831759,-1771669,-495695) | 4858978158 |
| Packet | 67 | (1291173,1035560,1181) | 7291214587 |
| Packet | 72 | (1801768,-3064212,-5770221) | 26635883164 |
| Retained | 31 | (-38307,-4996,22483) | 239700528 |
| Retained | 46 | (116634,18229,-56546) | 625149893 |

Let

```text
W = 1856143518829908327659417506030614331

a60 = 175858320410747467712011121217455502
a67 = 1170093794496896585250448672021248997
a72 = 510191403922264274696957712791909832

b31 = 215016319553396724124630241363628480
b46 = 1641127199276511603534787264666985851
```

All five integers are positive, and both `a60+a67+a72` and `b31+b46` equal W. The exact identity is

```text
(a60*q60 + a67*q67 + a72*q72)/W
  = (b31*q31 + b46*q46)/W
  = (271822366327161456349876663644618000,
     43372780420150674534368087690043000,
    -128275369939394823829003461762242000)/W.
```

A point beyond all three packet planes would make the left convex average evaluate above 1. A point beneath both retained planes would make the right average evaluate below 1. This is impossible.

Thus no single inserted point can see every face of the whole packet while seeing none of its complement. The certificate does not depend on a guessed mass centre. More strongly, those five fixed inequalities and side requirements already obstruct such a point regardless of changes elsewhere.

**Scope:** this is a fixed-visibility-partition obstruction. It does not exclude one-point equilibrium cancellation with a different visible set, removal of additional complementary faces, moved supporting planes, multiple points, or general finite geometry/mass redistribution.

## 2. Exact two-point access

The two raw physical points are

```text
pA = (-3739,-12796,-4871)/1000
pB = (6547,416,2693)/1000.
```

Their complete visible parent-face sets are:

```python
visible_A = [36,40,54,55,58,59,60,61,64,65,66,69,70,72,75,78,80,84,85,86,87,93]
visible_B = [40,43,45,49,62,63,65,67,68,69,70,71,73,75,77,79,80,81,82,83,85,86,87,88,89,90,91,92,93]
```

Their union is exactly the parent’s entire 41-face packet:

```python
packet = [36,40,43,45,49,54,55,58,59,60,61,62,63,64,65,66,67,68,69,
          70,71,72,73,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93]
```

Every complementary face is strictly retained. The minimum normalized complementary slacks are respectively

```text
92738812/9370675841
1494694/149882137.
```

Across all packet faces, the minimum of the better of the two point excesses is

```text
1633162637/19809575457 > 0.
```

No point lies on any of the 94 parent support planes. Together with the obstruction above, these inequalities prove that the fixed-complement cover number is **exactly two**, not merely at most two.

## 3. New finite geometry and actual mass

Define

`Knew = conv(P49 union {pA,pB})`

with constant positive volume density. The exact construction is a V hull; no H-to-V rounding or diagnostic-polar recentering is involved.

The maximal-complex comparison is:

- All **41** old packet facets disappear; all **53** complementary old facets remain maximal.
- Exactly **41** new maximal facets appear.
- Old extreme vertices **44 and 47** disappear; the other 47 old extreme vertices remain.
- Exactly **42** old true edges disappear and **42** new true edges appear.
- The final complex is **49/141/94**; every maximal facet is triangular.

This is not an affine reparameterization of P49. The parent’s maximum vertex degree is 12; the new body’s is 22. The complete degree histograms differ. Both new point coordinates and the actual mass are substantially changed; the volume more than doubles:

```text
Vnew = 926588874581/1500000000

Mnew = (
 -308790516222637/3000000000000,
 -13851852856197233/12000000000000,
 -855517446616063/6000000000000
)

gnew = (
 -308790516222637/1853177749162000,
 -13851852856197233/7412710996648000,
 -855517446616063/3706355498324000
)

Vnew/Vparent = 1853177749162/897008511419.
```

Numerically, the actual centroid is approximately `(-0.16662757599063063,-1.8686622023253017,-0.23082444385135878)`. The sufficient centred multiplier has **54 bits**. The new r/R is approximately **0.23920824647575076**. All 49 exact vertex distance-multiset signatures are distinct, which proves absence of nontrivial Euclidean self-isometries.

### Complete literal extreme-point definition

Divide every following row by 1000 and take the convex hull. This 49-point definition gives exactly the new body. The receipt-bearing constructor retains the parent’s redundant nominations and has 70 input points, so its input JSON has different bytes from a minimal 49-point input.

```python
NEW49 = [
[-5349,-4181,-2657],[-5335,-3957,-3045],[-5320,-4491,-2030],
[-5248,-4771,-1284],[-5195,-2972,-4660],[-5158,-4951,-660],
[-5025,-5087,-3],[-4842,-5189,619],[-4651,-5245,1158],
[-4426,-5283,1653],[-4221,-5231,2196],[-3957,-5132,2779],
[-3739,-12796,-4871],[-3628,-4986,3372],[-3287,-4698,4017],
[-2832,-4319,4672],[-2359,-3800,5287],[-1853,-3147,5831],
[-1308,-2413,6258],[-820,-1553,6555],[-345,-646,6698],
[75,281,6684],[441,1216,6513],[716,2140,6187],
[738,5871,1706],[829,5591,2655],[871,5954,744],
[903,5158,3543],[915,3016,5720],[924,5889,-205],
[954,5672,-1117],[1028,4540,4393],[1044,3820,5115],
[1286,5295,-1845],[1310,4849,-2586],[1756,3730,-3551],
[1833,4341,-2936],[2113,3135,-3787],[2489,2597,-3860],
[2591,1927,-4061],[2840,1331,-4039],[2863,689,-4088],
[3310,176,-3676],[3728,-42,-3170],[4064,-3,-2674],
[4281,-101,-2258],[4486,67,-1781],[4626,419,-1256],
[6547,416,2693]]
```

## 4. Complete equilibrium census and whole landscapes

At the new actual uniform-volume centroid:

```python
stable_faces = [9,24,42,73,86,92,93]
unstable_vertices = [12,24,25,27,31,48]
saddle_true_edges = [[4,34],[4,35],[12,13],[12,14],[12,41],[12,48],
                     [24,25],[25,27],[27,31],[31,48],[32,48]]
additional_weak = [0,0,0]
primitive_zero_P = 0
primitive_zero_Q = 0
boundary_face_feet = []
```

Inserted points pA and pB are new vertex IDs **12 and 48**, and both are strict U. Old U4 is still vertex4 but is no longer U. This is loss of the old root and creation of multiple new roots, **not successful U1 recovery**.

Every positive bar is retained below. Depth means `(birth-death)/birth`; displayed depths are approximations, not zero thresholds.

| Landscape | Peak → elder | Component / cut | Relative depth |
|---|---|---:|---:|
| Physical | 27 → 25 | 1 / 12 | 0.00236556306046 |
| Physical | 24 → 25 | 1 / 4 | 0.000956443516786 |
| Physical | 31 → 25 | 1 / 4 | 0.000198014192483 |
| Physical | 48 → 25 | 1 / 21 | 0.173293749313 |
| Physical | 25 → 12 | 28 / 34 | 0.468340914033 |
| Polar | 92 → 93 | 3 / 5 | 0.173313389739 |
| Polar | 86 → 93 | 2 / 4 | 0.109938395769 |
| Polar | 9 → 42 | 1 / 3 | 0.00423012164727 |
| Polar | 93 → 42 | 13 / 15 | 0.519200411351 |
| Polar | 24 → 42 | 1 / 3 | 0.000387173898743 |
| Polar | 73 → 42 | 1 / 3 | 0.000865135020606 |

The exact generator returns all rational births/deaths, complete components, complete true-edge cuts and attaining paths for **all eleven bars**. It also checks all-pair chord domination against the true-edge maximum spanning tree: **1,176 physical pairs and 4,371 polar pairs**. Equal merge levels are processed simultaneously. There is no selected-root-only acceptance or discarded small positive bar.

The full audit recomputes supporting triples and maximal facets, true two-owner edges and connectivity. Actual volume and first moment agree at two tetrahedral origins and under three coordinate divergence identities. Stable feet are checked directly against all other facets and crosschecked with same-centre polar conditions. Unstable vertices are checked through true edges and against all other vertices. All true-edge interior feet and two-normal-cone strict/weak cases are tested. The Euler/Morse equalities are consistency checks after direct classification.

## 5. Scientific consequence and continuation

The new theorem identifies a concrete restriction on **single-point fixed-complement access**, not a general obstruction to the branch. To reopen that exact single-point task, at least one of the five support inequalities or its designated side requirement must change. Merely moving a reference centre cannot change the contradiction.

The two-point body demonstrates that full old-packet replacement is affordable at E141, but its large actual mass shift and new high-valence apices create substantial physical and polar defects. It is therefore preserved as a **different-architecture nonwinner and exact failure control**, not ranked above P49 as a near110 entrance.

The most useful next finite experiment is coordinated motion of the blocking support carriers `{31,46,60,67,72}` and retained material, or free deformation of this already-replaced two-apex architecture, with actual moment compensation and complete two-landscape reconsolidation. The parent’s U1 condition must be recovered or replaced explicitly; the old U4 label must not be protected by assumption. H49 remains a separate S1-first physical body, not a recentered diagnostic polar of P49. Its unchanged complementary status is supported by the literal parent.

## 6. Source integrity and execution limits

The latest journal was read through EOF, including the literal parent payload. The named parent authority is `figure-0509`, advertised SHA-256 `0e2f8f8024ed8bd10c8a6c694f0cb7f50722833913adacafe783831623b738a0`.

There is an outer-serialization discrepancy worth retaining: the journal’s extracted heading-through-EOF parent text is 61,608 characters / 61,634 UTF-8 bytes with SHA-256 `02602d4f638465ab84166bd4ea1f4cce1c9d7ca32b837ad5961d3cf657f1d5b0`, whereas branch prose gives 74,772 characters and the advertised parent hash above. I did not establish the preimage of that outer metadata hash. This is not evidence of a different geometry: the journal bootstrap and uploaded bootstrap differ by 14 formatting bytes but decode to the **same** 31,684-byte archive, SHA-256 `4766281bc5a6fc2649dbb6a72d57196df8982270a79e343525a9865043dbdeb9`. All 28 original manifest entries matched, and the fresh full P49 audit reproduced its original exact receipt.

The latest journal file itself is 323,888 bytes, SHA-256 `193b191d19cafa6490334c0d75ed8585d0a2034256527b9587de60e4f3bc9e1f`.

No full affine orbit, general insertion family, two-point repair family, or uniformly filled strict110 class is excluded. No long optimizer trajectory is claimed. The exact acceptance here is the finite two-point body and the narrowly stated minimum-cover theorem.

## 7. Self-contained recovery capsule

The inline capsule below contains **six complete units**: the unchanged parent `exact.py`, the literal full parent input, the complete exact constructor/proof/checker `finish.py`, the complete finite nomination program `scout_cover.py`, `EXPECTED_FINISH.json`, and a README. It needs no original archive, research library, earlier sandbox or optimizer checkpoint.

Exact replay uses **CPython 3.13.5 standard library**. Explicitly set `C92_GMP=0`; this compact capsule uses Fraction and does not require the parent’s optional GMP adapter. Optional numerical replay uses **NumPy 2.3.5 / SciPy 1.17.0**, single BLAS/OpenMP/MKL threads and default HiGHS solver options. The literal rational points, not a cross-platform floating trajectory, define the exact successor.

```sh
python -B -S RECOVER_RH08_FINISH.py RH08_FINISH
cd RH08_FINISH
C92_GMP=0 python -B -S finish.py
# Optional completed finite nomination replay:
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 C92_GMP=0 python -B scout_cover.py
```

Expected markers:

```text
RH08_FINISH_INLINE_RECOVERY_PASS 6 28869
RH08_P49_FIXED_COMPLEMENT_ONEPOINT_IMPOSSIBLE_PASS
RH08_P49_FIXED_COMPLEMENT_COVER_NUMBER_TWO_PASS
RH08_WHOLE_Q_TWOPOINT_FILLED_BODY_PASS 49 141 94 [7, 6, 11] [0, 0, 0]
RH08_TWOPOINT_COMPLETE_FINISH_PASS
RH08_COVER_SCOUT_43_LP_PASS
```

Observed cold-reproduced receipts:

```text
RH08_B1_Q2_G3_audit.json
  89755 bytes
  f8f470eefe4ff65758fbac34d4b5e7d67194849ff167a2e8c41b619e77c8d0e7
RH08_P49_QPACKET_2POINT_G3.json
  3497 bytes
  21a9dd48a07aa11b40be9ca0ea791f3d5e12c5b4c6fd8882747d2d7ffdb9c773
RH08_P49_QPACKET_2POINT_G3_audit.json
  98580 bytes
  f092e033102f33ee58efe4e621e3a04c93077c71d868f426c427ae9c12a355a2
RH08_TWOPOINT_CERTIFICATE.json
  24779 bytes
  1a7298df165e3d3ddd16d98b7e2325bfaf313b7274c16e9c8de1ddc554c24153

Optional numerical ledger:
RH08_COVER_SCOUT_LEDGER.json
  27018 bytes
  583904d0e381f041be3587d557349335e3a6a046616b5f21b9e13879965bdb73
```

The degree-histogram comparison is reproducible with this additional complete source unit after exact replay:

```python
import json
from collections import Counter
for name,maximum in [('RH08_B1_Q2_G3',12),('RH08_P49_QPACKET_2POINT_G3',22)]:
    with open(name+'_audit.json') as f:
        report=json.load(f)
    degrees=Counter(v for edge in report['edges'] for v in edge[:2])
    assert max(degrees.values())==maximum
    print(name,dict(sorted(Counter(degrees.values()).items())))
```

Convenience copies: complete recovery program (`RECOVER_RH08_FINISH.py`), new exact input (`RH08_P49_QPACKET_2POINT_G3.json`), full exact audit (`RH08_P49_QPACKET_2POINT_G3_audit.json`), visibility and whole-landscape certificate (`RH08_TWOPOINT_CERTIFICATE.json`). The following inline program is the durable source; these links are supplementary.

### Complete RECOVER_RH08_FINISH.py

```python
from pathlib import Path
import base64, hashlib, json, lzma, sys
PAYLOAD = (
'{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;Bdqy!d(D8h=iqrocag;lgCWWtY+wO%}h_y<3+Z2X|d^^f7BBc{hj)3M4brR(7Eg0xQaEv'
'oS^r44MnL>dNN6wYAd(hfCw?Sm;1NWKks-Loyx_l!Q9?$a2^btUBWIpXf}jf$}T`SnABV1rZ2uT-AF<1NKF3}$`ZBuf=6({#uYLd'
'WzV&dsa=+;*LZ>`hKJcmxJXU%C4NHL^{9kaP`3xg1l7d{T!V+7mOKyJb98y5347FJ?p=B8La_n4)zjQEoBzB!lQeG9a(qx1y|3Xi'
'^C!`;xvqBfO(3gzq`Ru)!Wi|EcQxxvl~#^Ff+sBm^x<7dz;L1UTa(9zmr%#Y3vj<uU!yT95+1SPpZnToQ|qML_{0+a9iQAFVvWN~'
'pnF67umiSQMKg?8b|@|BifI1`yX|V-3H`PzN50zK7O=M|l+=n_3{3qRISuE{j7HZ`H!2`qP^_ePzusn8W3&Sy421cE7!IVR7AAxo'
'O6;Fo+A{mLGc55c2@{9$1;eS8O*!1^w?F_`Di#Ix1qgmlzCAKyK>0m%oc3qQWc`)96>pWUYlCSl)d~@x+}-n|SHTl~XtNrx6&}0;'
'vcjwYcEs|brp_>YTC{%@1AOTVp~0BPS(;FYE=bW^qiV?YWj#c+h*^?K^SH$zDYVY;Vue3kV~1;&m8sRgx72UxPWF=&#AskZz|@l+'
'-gWM;AgkJ8&^ho?8Eh_)vUMQpgscI%1q!IHs82yWWBwO1u?Tiv4nHW&fP{A)`!lj8Zxxa**^xE+geyYQro52Zf6dER+IfdA!STfv'
'SzZR2^j%xn;E!qIt)?yTbSiaIO-h!rTrmD{t-N6x`P_k140q6<DJMV&&goVkSS9eUwE{4uf-9;XuL3m!Wbpn6wwB%F!_T`@o7~3a'
'82YnENNK!m@nI}(0Fh(LH0}Lh3R4yvIP1pAaT$L$o^&vZ*3jXhBX#M;`AaZ&txZ$N*jfW$bmi&A*K*s#mmBdQ<GCWNkhz7XsF;JI'
'XpY(tIS_v^{j3X3kp(suu}j8U!e&MRr0S0&XTo$)3dMC5sSCdW8Va%T!cFF1)!5HC5(>*8N<`=a#SMoG_pcsgNt%896uLX`Zz1TI'
'!xaku%8N5!@4qAOGutvOH&{imiODGoJNk^TvP~Fh?3@!IL@1mEN~qUKm}sY2T^@_BxT^Q0Mb;B;8A~GALy;xx)K<PB1N}AS?)b0h'
'W>|m**rAasPu6Lt%A<@xw_sz=$FZ<3OYvl@bg8Vfl&youT;VY$97@X+e4Ewe$snMNCBP^I(=z2=41>)*vBmpmhXRS;?VlY4^v2<M'
'JS}1ZMiD@vu=Ki$KH~@B+#EoyvM#W6!}w;*7WE-Y_q6H*^UxV>jaZ`zi|;N{rbR|e0%l=ZK_`D6-m-PnFN4UI$73r3@5rL2K1EI8'
'&_Mlt{gi;9AaLdIB&lg&5qAX*uc8!x@GH|?U%l@{B9FYt$O-!;2fzj*V9o}kozM_k9W^Lu%P{^{jEt*DoXQCH&?Is&AP?j!?E_m1'
'101eY>Ts^QwVcsy#LC&Ud<Sj=;_&K`3xT-o%jNHym+S|(g^^{$(Ar~DQbD67a*F$~^YWkKyJHps)fk8;RIMJpQ|&FC15521FzD_)'
'M+YEYsaFq46%lRxb`*AEuV~bCm|RA$Oaw^KkSIfy+JHNOYe_N;0~Y7cl#(qqj-W0#$gi2(SZzfjRd)>5x6)FVYGSnZw47#QZwH?}'
'9W67}!zAf~^;F)~ZfUc03|ZWC+ZRv5mi%S&KJUE{Hs^@`ojF5B7j#L;DP-fgE4ja{e@R3kWDgfFpc;6n9g0-cLeVZErgE;kU8XAf'
'QhT`U8su;9LWRG&+5wKYcfxv}eJbsr^<Wl?ftjwCZBY58RXM@IzxEjMLccAJRRPGcU;F%#5!%+td1mXB9D?-s0-ac|J^eMK8Zg<i'
'O&bi{+$<VV4E0A*9WFoqHl}b%x26&U?(5{?{!;DhL$J27!DxjscXXsM@a~M8&BsCqTpFI_WP<Jsfe4uQy53w&Jb`N(Qn(A3ArOcm'
'2$nX(o}f%miikjUBFB0f3B~bw;i>}|U&b6K%%i1<a|aTx=Fwm+Q*&ksN*ZG+Z9d25_j3k;5@OBO?fRw8N_Vo7YPwa<Rl4s_X`C`u'
'Hk5$)y>Ky=PyBo9!SlVSRbBH(jP{Z4RF>XV<a!!y(c~lt7UAFh*4w07f3l5{yMlUv>Jk1xs!*||ttRM@6+fffn*kE?O_8d-h;0^z'
'Fq;owie@ezk(z=zSL!Hm?@N}jv}^W;ef5o-C$z)K5RANeRqL)IZwg52&@J$oLUMOZsAZhzFcRm80Sr`v%{1pOF_)T;+}%)WdkiH?'
'lauf_dMyEGzvjjIQDGyTVtdu<5dhmN6|(Mg9l05``%oK+&w_yJ!AS0q+If5~*WYi_Tuo-$%4dD(hx5Hy<?H+n@}+X<LZG$XZF%Z0'
'2u^4DCHRI*(T%TeOd50c>$(YoeGM|d*mpZV*`9XR2#CjhZg{Wm41Uu@YLTrjM<(QT@_)R*QFdwMa@8cGCVNCAS=I1SLzUJ6f3tBX'
'i5;=Kk>NaRn(`o+O})Y<ZlWU8sNEYPu4#HZYGmii^J|d}v0w~kM!;{!`*DF(b(}WhFwdJzIXi4=qp*{A!*fQ66pjdMSY}zYH$0-L'
'p<$I56e_ojpHl>ra8=g@(Q^2U|2}wVVX|UfwJ()VN8pkZzSx0%*CU4*Gps^_kBzAozL&-5fuT<&L4pw)H5)S}B&&*HA;C>&hILSZ'
'o@u6hS=y^YytTX`LJ=*%V{$Q+$GQ(BjOBy~a|{SK%UAMkQJHBUx{N$$XzsdB(n2<Y=HAR>{a*r_T0Na`{D+^l)#SQv0A8nFe<C#J'
'_MnsQ*WQ86&AYPM{gbI%0pTVZAig?4^;jyaS2}OVv{0qnPR$CKoAb{FqZyAdBTNMPC;i+J=oJi8`KJgqp$@fD@8Dc!WB6u$fiXV#'
'G4i{h2-XiAF%OYD*=Ul>wm|#J5x*guhKRQfMc|G;0Zrp<gy{}~M;dQaFK-UuMJQUw3@(EYY^jvqIZ*RGhNOE#Z0pfRUAf1eE<ZdV'
'9|AVs8@Z4M3Us6?Y#7D~*lhLQsyw}!8SOsM@SW8;St#8opV_P;8r)f=?%usH5ao?qE{FIy4qU<I@6DL}IiFAv=oV6IoBYWZS_XZ!'
'l#jtoDzm|b@s83TKnz<%e)oS65zdc$<$lJ?@(#k{G*1=AAw%n|PLG9`9NY$so8eE%UM>?*MkNiChY19dgykw;W>_>1d1#rbmz;<Q'
'5v?rApxYCeam_W}uNtm>*MJANZ;Z$emmDfs^XIVbQIR-T(3QaZ$CFv>whBvjT<nDa%f7)|2y*~zz{o695BXn@O7aTYnqzlFV>WGp'
'A1_Uj;n$CG%tu{~w~p<q4l!n9cz`b%(42Nh^ljcu>}u?4_jIe`H;$78<&RHRVQ+DU%;e50Z#*T)IjB;on%r`~D47^p_e;cxdPLxb'
'K+ckuF~T@lv70u2#$q2{gcC4H20!j)dsDOKM??Oxx>e|zdN4!omN_&w@l0N1lH9;=@|41+ts2UZY<{O#GhxupM>nVAX&ik=Z}>Pa'
'@$6p;+;A_Qw;g0Z4II}7E4PhUd#Coo@&!-7Plr^MmFXFRP$kB#_Gz^*j-Q#g5`^39W+iZ2>KvS&xx1vp_Ta_O&au&U%2c4n4P_se'
'M;a*!7dxNA0G1r-xh@0N6vZe%bNG`#M?EHVb+Wv#`m`qtVZX3(*R2{W$gE97$znm21>zEqT<RW%mElpAF6NLniJlk!%IW&JtDi^7'
'X7^pH7?zkVe#HZRTqzg$_=nWK_~g~|qk66)AKW|wH;n;rDPgvnH?$Q5M%_+x)1L&SQAjTp3)zVz`P&@1Z&f5Abl#<+K)ZBC-?}N1'
'%-3^8BFKy@id)JXgA7tIe+iVm-uvP$%^CUz5#Ry`9$dxYj<(Dx_8BORiP7{ud}!AnXxuw!X6hxgqB*4Ew+hnRkuIA{nu&O>;Esa#'
'xyIxcEQZ8znmHRHLIKZN@on1sfC6bPBiX&!hUigUcA=U&{{KB8QU*LG;_*E}mcl^s6Ov++uv%AQG{yzh|E9Xv6`hLtLHzM*>fskx'
'@Zxa8&|byG=Gd`qG~kr{?yj1;2ZN`A@L_=Ju&lM#N^&Mo8e&z$vlb?+r9!XB)+L)Y&WYk!y$u|;rh_8!FUYkB3PzaNZhfBkwCx!&'
'-!GzdzdC4gpZOh4m_e|GZW|pOTPY0K5F`*6P}_dvjwpY6HoKx!PX4O9;3xMwpt`)ePb9p`FHzP7?Xj-8K9vVDD4?!^sQ(slkJ-*3'
'|Mqkkmi8AlQ>op*QqgfY4)zL;GmO?c<?%b(ePh~2@u!5}^umJzWE;p2I1^8dvZu%gH0|;>hp@@Hrq@HF0}m`i3)je075Oin%d}&9'
'H@3hm^ARXT1b(W_kPZX!BH`ub_4DbIPa_9vv9E+IY2*+(%T$s%Q7vmOYID~;beyTTGxE#J=A+8Lc04aK#EJ%yef28raKep4lOTTf'
'r+N-zfX8J^@E`4U^PgD<!5m~H?C(hR0+2UABxw^mG>`j<B5!Klz!dkY>E>p89Ak@F=}Z;a_}{rWcqCIMm&r$f6dCLYHfN%3Djc`A'
'Di#2tQ1SfftW_=Dd;e{2B&e=!F{I!0A(`}+=-mS8PxhPOb@NQ$FaM+iZYl%+YO21DsRt=ZUmeC5BN3CU5x=vas|kn5<zcx2g>r)2'
'DYn&><0SpQAI#)2=F0#J&n4ZYs?sva<j3u$DK{RG3M`OVGZ-=B+Yt}20-ocGjcgm4iyKuW$zA5`^U{ab27o1Z!U9?#@f|xqc+*?!'
'z|jUXhyTEC&$XiRpd!!*g|rMAMgm(65KmU4>Bx^Xj~|0gC5Umi<o8bD20vJ*kX3~a5|;&mzbENZ{q2yv;e`!}!|$JN>HD<qMF5xQ'
'*I7aWENndl(Uzj3AxgR4;8id2L`0uNm&`=A+*KOsSYsxw5UKUB7H+DKDv|{x0Is|{qg0N=ZB~2Q5!S+F%9p9l4yweGq1!-=3y!&R'
'{3URh>9arHt;Hq3TP*#GA?#FuaBEbG+F9KE*1&2mutmH_4eMWyGutx)s}oNxb(H4pzrk^5Cy&Z>wGk&2vR%2;qm_upjb#x~4D#=c'
'Sa+Sa+qNZ4C4E)p^;-K`!Rve36b18<gE-R#-8Joj{Yayb?(J~+Hs1YVCMP{fLg1&`gDVq^>rGX&mMI07^S8(tnGO%v)b%HMGt0q|'
'YDy9pid@6YfSHFy8JV{3G(n;X1(X;S0Pl|)*{KC-`CLVJg{;lRmC{sF+uCDAt>^(wkNbs&cdL?qqmbCKtGurTsOLZ-Po8CC{Cb}g'
'+N&FtvX)uNs)5J-G&shFLfRfggzDlS9>jevOw%-REdrpetG5;w8b5st-=VcTmVbLr+;y;s?7>_?OY|4{4|Cdl9tV=0&$3-{U2cS('
'P^)(lM}qDdgxqaDN?EdCTadBJ(o>Ia_O(g~TBOq7YRe)GT4Z^?r0?}95$se(g24y;6KrB!xN|CQ2D6~Qv6pR$r_e~_gHFwbb%?lT'
'YFAU(aLe!ZYulxX#-XijSR^Ei=$_?Tv<vQnVfAfkJn3?zD@26A+bxVf`T94uz?7y5yr^%+&{u50ue0{cKoNQb7L%h1Qs{3W#EkU|'
'G0U79#S17wCmlMvWEQ`k#=xgJ1j{6O_6w5vH7J_1uK`zJ5vN=P-2W7<FmECUh2aX)l)lP`)PIYMdcoaF!Ny(0Us+VpeZB1Y2&4T1'
'lwodr+hnBns!R#ptTTr{D)83l+eUYn4GpVACMkFzMIC^ymYC1Pm7HCbda(yUBl$jp=@g*d%G6(_K3(~YYOpkJSEim^4ugOzQm#*g'
'NMt4P46<MN0AhmWkHvP8_~E4aq*MDiQ)>VoFOAQ|kaN)07HN~shJ25Vxhg*LNRq?(kyI281JZpD_Vmt0dM@ZvR<c4%cq2d-JuV?*'
'X)u^fpZl>_hlggHpZ8rATE|YcF=ZG=LqA8TDOkc%_?GYUA4-mDj6QK7$=CC^b1;=SyV2{)&>{2Ao=w84TEFclm=}gsk1`3?%VGa('
'Q*NI~S28_i?0Ch1PpmLOV=RXa@cqp!i*^XS@+gF4-Rx0!m-VIS9ajmB-{_F9E#R*?`jCTBWgKJ(IgWpzDsz-1_NK&1Qpb{s;2Sgu'
'+CRKlGV?$?zW|ijAd;Rw_r|=ktELA22LaYlhHDH}E_FWv;83l$g~!+oT$Ao=qgc8PAd3UWIO=-jd_s9~HyC{Y`v%y>2Q?H%Yl;)u'
';G~C?40Chjf^2B0=cer`^(AQY22@Fgep$znOCf^44@$GjI9p)yR8MI>QqLu<m6dq$7~3eQ>Ss`Y+DsjoGm-DQoX;ukbckHDhpvy;'
'Mz>ZYlN396N@8ECF>^FT<?0<Nne>PQKK~FqV&PxEGOQEf>(#G3(SXeR6*heqiFpJW&hPl=;cyia_^PDvh+muY-eQ|;oEYbzT{qeD'
'TbOOEaW#~&i9uY*jfnu~gCq7)pwaK>xynk$>S=^ZjC4_Xm(R-WzC<)TxpgE16mlFqTKr<zy(T{c-0+<eLQVLp(9#O+4V;vE!=YtE'
'NBF}-ZORsB$bue{CcAuWwY?88YZ|FB1Jx{+QC$bP(*!pLnWqA_EEIRp_3twY>8!q0iTjo!PY`#9yq(`RI~P7SW}bZnPJ#&4oQ@eo'
'Kei8lW6tb+tSaU%C}t_vDdinA>Up_<(>5`N_JpkNHx=XE=5OCn-RQ4#ss2x@-yk9y9?QNxkgzQh0f{7%@s14v#gQ2|&_Q*}ZP{q5'
'x`7OCk_nH)*vO2-Vyh!@i12RY28@Z9cd!}&M^wsC<Hiyrlu{-iL3Qw8ZQyrB#MHp_$mRvbFtLx>Ua^*xM5q&u+efPlYk=CBq-#-T'
'yiq5AFPy~qh@$PomB+C`_E5#arT~}qNri|(yf1T~8(EHOjsoy<sg8^}k6gE9U*TpJ(M>&6kp)MCCxM%xI#i#!S51W5eDrHa$pxW@'
'f?qf`mYLCbF}&tj1~OoP##8XH&G=nbu9KR9IFngccC@~7plZBp75!Y+fl-1P@a8#!y<98e=}s<ZT>atsyOZ<Xb0D7I-ldahZ?iK5'
'qOmxiw=Y;(V+Q#Lvsa#&%dVjJK5M&@1YXJl?Z-RH(WNP@*rY1D_3D^RKI=rZP>-BvvB-6-{+)p78*-NR>^a@ZJRzh6N``(&71K?}'
')DK)~)ArBaow{o_Ei;f$vTm<RetX)ZpjDkJO{T$76Co%09pOU7SXQ6?-IqBLq~U_r98s#5z&}nD0z<=^kiK{}`vRCO=&Mx<i+S4Q'
'M>~7Z6yrsz!%1`BX@)P#l|klYnKYf>JCy8GSJvt;{EuzcD|Xu}Y#)Rq8I;-7ir(6LFy&OoMsI8=(q}}OE-Pbd$SZ2F@>ml%R=9X>'
'niYPeRfy{mjeeKwi5m~w8`WH1o$j9e&p9Dw(_Q?NeIZ{-0|tg5sr@2}^BeXgSGd6L&N~#5W$8cV)d6kgS??mBxR0)dyi!%bxh#iV'
'w(J8@r<jgP9R05s@!G=cg+JcIo$_$ns18lGEP%Hobt{6TiejR2!F+I?sGT>OtMM>$N$d#4!cKN*uDYH+7q~L4osiaieO@n+VuP{t'
'+lh1$_v{f7?_HCL`Nw66q&pUSXTqm+`@l8L9}AP<+f<jz_)M$Q`_$}s?Q&ST1x%<t`R@VhL(PJ4Vx+5@LVV))Q`YLz`u0U_Xh5sD'
'K@Xi#B;#T2EQY-VEtnb9m$GQ_xA3>h_)#t<4NEKxqK#0oyQ_IpkvX;oHgQx#AM9Ah4&^#Zdz%3ATbZ%ST=9Mew*|Pb+5B|*!ZwJW'
'c_TBQm`GLyWf=f?$Y3oEJ|!f@)$S$mR{-}{8^*(&gHT$Cp!Pl!w?Xw)Kd$y3sNL;YK9>xQC3Rm{+cgn*(Tcfi%M@3+wNVDu55zX-'
'P<on42nom;Rq!v?3XCF7EMm0SqkS=Tuw@^pu^)lrk9^GG<3Xu^X^81jE*8ZZJntv1QO;vDLE6qmY%ow0#Ch9^tXTruxC5?bNrJ)q'
';K%n<?a8W3)>Z~TS-|$ULAThnP2p4W3FfeXrC*#_k|oq#&r$=fe5qk1Mw)Lc!U5tZwRqll!fjH`Z&v}XzUGw*XJ$tKLtZ{(-#ff;'
'dJY1bge^F+ITvX(q;=F2IQ!`XN%l~0XB1Tu?VqD0z_g;g=Dsadz4}W*M(NRo&V3;sC;%MNm_*L)$_!=ta>hW;)Lpiz9aqsl2S%(-'
'M)4$7A#cz2=v@2V*U@U&)9E`m-{nvu`4Z9Rz~A5q$hw_KTw{%{dl`<+<|F`@2KA5pUU6;%0fPK+-bbra;bCH)YR>Pq2-Za@aqz8Y'
'6WPR;6@($j&~)iLgg@o4E>>=+X5vtNt*P9W_ohcXm372?$dhgZBjj97fNviM_s;p0yjph7DblOMr`r`;=s&aI>UkYp1l6`}xA@I_'
'*d|OI=rrZFtxx~}qGFa!XXYYB!#qvpYwc3$ItGVR*Wd8K#^swZK-3rVa{XfVHG7XI?kMHv)xAuKS;=`h3*!Y|z@$$h7xxCM`Nrt?'
'dy<`Ct#@ICH;Go1D8%Hx_JafMRF=OAe(DGJ7|%8C%r0ykf@Q{=G^#lca&~t}?@_(7{z1Jzd)0kia#sk{HlJ`eHJ1jQ`XJ*Zp}@yt'
'm{?COC6>mD)~lA?@ghQU_~1a`R;(a($}<pEZF~R!y{&`UBh3H9$s7D{f3{3syElw)wRIj-a!7-X0njZ;yG%#2^K8{>_Ujsp;pfAA'
'$+X&OEwi<sv8Ot=l$RO6>|gvuiD-)h--)M^wuHHPwEwP-FK0-3iR^7=&InRzvW=x9KRtpu{-?>Uy46PN2I!LEHShTqNC#kQ_g~el'
'F`e<Dh$nEfrYh~CXxUJbsvvte-Hp}S^M%*NcI&$APD~j5_1cOnyOB0?GJ;G7mL=g=oDPZXRBa+3;i~<#4A)$h?L1Nc3eg~~UF%FF'
'IK}Evj1eKU0w&V5fVvb|dVm44LQ(Rlj#j)O?>N(hh(?|R4?|Sr_GVkxY7;X0yy^>2u4j(c|3V7PI2O%<S4q07)OgYd<g>|pE&cCI'
'u^@;+E>YFiYPGf6^6)NQXJI<hhq!_MOPyLF2yY={d^)G)y4*LG`m?=D!L$_Vg5|SU_F|ASZHjhYNc|48BsSVHVrS$AtxlQ-5cP*^'
'szAvqPrjeUDt2n|h;_m3bTt@<v=5TyQN$bgPV_f+D2kt`VlsZ(+oDP%gIjV!P2#pfp0XBl($=8HQ{RK~(hZ-a>gH?Uyb(q45&PR^'
'*7l_-7=g;m>L#DE1gTwL5$#^HBSUx3#JcQR^K1ljE}Fp^sjRG6QZFi(<t)v!2A(BZ<>%G45Ov#kXHt>#5j#rn_nbOIdhv_wnqNa3'
'{HayMpzm`QQBg^RoUtGjw?@^+tP#1I`MnkCDc!3x6DQi-CDYezuD$|Xpb`dxP_?U7*HeArYzEE@s`BqyxHoAK7z52<>?dB#4p}Bn'
'IMBc%H>iNksxx=`V7E?<U!%(C8R7Ro9{dV6l<^-lG}4R#V{V1pz->Y7V)YTvalL9*moPXl;Ut5L_*8ZuRyUbe$qWiuXMJXcp|PSj'
'DtgxteJei@_V_VU40_;1c`xsA8A$2n2$X8{2$N}{Js^H|pg#zAcCjq`9~VI!mp1w8kOZsJ2n5g=A+iq*p%%PRM*S-CX#eQ<nuqKO'
'^*~^5Z^?;wa2U#Gh!qSRAKzJz#*X^K<$ljY6!lXXk{2hOP?iWOqH6GIYq?^xtWJPqp4ZuLY^)j`&taEU^>ZLo6Ii#xn+qpW8M+zz'
'=keBk%viP1K2doUiDJJx8yY{{93eXzFZSUS;@@juqV1>Q<r<aN@fa9J26{{Zbf;iSv*Ag+m!|O$b%c*yX1#?j+@TlT%<&K-@1^l`'
'$q9p7yXIeuHGCiC-{}NPt4z9<?&3k6qQn|(n)wPW!Wthd{Nh9XU_vO^-r@BDMVcqv9W(l2KT4#$l6BcL@iFY2Rj=}$q?;Icg;%P+'
'71<Pryl7>xd-l8s&?;<66s~rPq(2FYRNfRCQDJUuI{M2#ZXG<+VY{d2G!)m^9U;)dgQBM?$VaWu)T_I>JE}AlMF)>=*if}tU1>hI'
'+N$`02Bh+wUDMbi1i!0Cjsh1G@s*f)2|Xfjy`o8**;$6!5N9!1wj*yCFRu_VDTBz70i2wDiLBD~%QroEa#}ARkCNuyDcQpXt;_(A'
'nl1a&e)wN$AA44#($-oeOOw=<`9AY2VOp!Q$8Z!mezwr=t+2Jk-Y22+LdC_a5hh>r@L<3q^z<G*`wWg1wyFERo-n^D9|7hV`O@OS'
'je<0zA41h|wY4e;wHD5HfNnX1p-5bTs)(=oCuumH5bMLXFc?(kdPff*?QO=hQ#&O$9<WI_R&_{rNMf)O@bjyvsr=il&{(&0h+E=T'
'PiKy1?kCIBkL^a!K4<MWzaHnTm^#M>b-`Ux=!zODUx<>q_s>}}?oz65{j@Jh%3jS_k*~(>P$<DNYZ&(R6OX@mTj<6@e$(nF8~qTa'
'K_XToF94{|9EQ|S(jS54!8NBk-(pt3pioPd)D=v>=>Dn$%!}Yd>?4abI^;p+U$=R&U|2v{A;$8UP;l@jB|5cBsVGt>!X1CO+anyO'
'a~V_59rvF%7jL7+j8iJBec)p9n<+a6&WpOaOU|jHTwnlhC0Yd??nsZ;(kL>6v#bT=M9gO!!Du#{Y=?UpWFvBETn!j=9LA(@Qpv%8'
'8yw=*p$hKT+7>8Fl>?Vf&AzT974=<2&NHg472IM{7!~9EZ%ZTeXjdzffFt3VFJuI%-96sgwelZbXShO6FeO%*`gO(BYn6OjC4Z)o'
'*5;@|0R{MrVPNIM-}_3AK|<-|w5BLom+|A4W0=b+a4I4lYF~WPu)$Q9?|9x{LwIZ;8<d~MWFDND;1srp-Lcj_^FYdBVh1e(>o37x'
'01eQoV2mw_m$>$vKUBB|O4<G1Pq$Td5{Eo|=hhulOjqQlR`8iPL!}XvxZePmy83(O=qv8v+Cw=<^)ynUCjYR@4`MF!4(focyQY0E'
'zIf6p+jkKs?Kdv%@hNo7IcJJ6IHfS{4Km7HkErD(0M?zsDK;GLQI8C8#xYF;(0{D&vkp*7o3~P%2N**CPhe~qn~w3sC(NEm2qTla'
'!f2GNu<EYB;&W`yvJ0wGr?nt6oC0hUr6QmKFG6~DL#?q*{2r235E+U@XX@YEh@r9UUMU%(D#J<{IR2S++Bi<KuYhDts~A4ZlZDuh'
'4kxXX0;Q!?0~ouxU^U~3aj(OpLn`m@;6a^3x}3MgF!WOAIU-*<`|B3Iml{{4Wn`UVIH7=yx7uwvcWqLw*nrmf098r4JQMBL;~`UY'
'm`;X_=3!nKbgC249g09W!S2iIJ-6zvV$=aB*4rz~d`M>g7|6)=54YR?)$p3(8N|=qL&K_$Oh`1~Jsf^21UU|fZHoQdt`TTM1!D5t'
'Gc!cPg)+-3EffN@H6Y9!-(2+<EcPK7V!|8GQ6T;pDM3mMQOVolL3e@wP{Zo-Dhr6jnijZV{0t&ywkSFYg}`rEH&SSahU$){aKeLf'
'ES)A|2EezO$Jw|#@!!n&@4c{eP^Kzl-aQoS#JxwN7u`pAx5R2B0`X(bB1kozH(2<dVuZal`ddBo{>50_v%Uw)e_BvtpWXYn$=Dna'
'7fN@lB$oz04TfvV2<&FZUuEg=I7cNJD8Zzn_8n78>1D%y2UMw=?QB?_vu!vsp#F6ye~~o6U;MyKZ~2Sxm-l$+Y*eY%gt0<~MjuNo'
'sJI}#87UW}QVc<STXUk=9=A8Cw-Hj*b_jtCoL$Lo0hx+q#sdg7@!K%(4HR@*X0JMOfRwp5N;sS7w+S|p#%vObx3Mid7f+haV^s~*'
 't~=96Q-2;{fAr)7;KL`7#@%?tBRK_ct_ML2dbpKY9a{>*u0|mg*nropT&`va%M!kH&K%eKS*V*mFj_mA5VhZ(VrNM^vWt9BXDHw3'
'_WXUC_wOZrxDFcZ7%<>|!hO|*?Q$+ND=JPElH*sMq8TB}rTxVS!AN`PvSOJPls%@VKsCuELIMG9_&|xhm<pRRtuY*@NJM*JSRgeQ'
'bnMZkmtWOb^u`zzp7MAY6%!GBNxRde>F&w?2_mRqW^}K!5OR;rD%29Ftg$ar%nU|HAy-`M-3f$Bg;VJX>%6=!wN{LB8^7b6>Z|vX'
'<O<%nbnRbzCIFHJ-1w}E82sS)H8*h$#33bZ>mq}xMG$~ub)#x(BeoBgmVxD^4nAzCwhM@;ury0cOC(_7@Nbi~4SaAuB+91F9@V9b'
'leX+x<li@_%5Bbh0Y*i{UP?54h-)hHb=9$J1p+>=_WYW|C+0nZQW^CAi3XI%6g-gH$IamAB#Sh?Pyvt#*rsuOCO@gwRCRt5h<BDx'
'D?0nw@;KLr!Txb1IdL@n3z(b(8!V}hNY+=;iX?AQqo;51<={Qch+{#0n*Yv>G3_@Ln~8y24t`nx{3=DnMp<}&*V}O<w-d7O@9i*Q'
'X;<zLH_UtS;9-RTLt<Exbw1Mc$Xzac)RP{*A=Sp`IozVjHi|s9!lW;_{_RorgeX+TpT^5bYvi{7U0C<>_KoTvExUd+J&a&cjOO6v'
'=rUG_YC!}_IW6jP%e8V;fTztj(Qz^8H{HoG9asEYNa<Gm`H}_bbgq1PQ2o9@1c$~D=Hc3Rw9|A|hCPFdvjNN=?dv!`Af3glwWY4;'
'XlaWtxXIs1*%GkXY3?Sbj?l}yI58Xovhy46(8TusdAS&c%?1JK6jXkgMMEAxJzFKBsJCW?Z%WAk-n1L8|KFP<72-7*AG8bchBkh1'
'q>*PEl<rRWd1<uP_(=hXYEF-5<Zr!o<-;==9FhoU&j0`bTV`78JqSI300G`j#o++}n4qe=vBYQl0ssI200dcD'
)
b = base64.b85decode(PAYLOAD)
assert len(b) == 9988
assert hashlib.sha256(b).hexdigest() == 'd5900c77391bdee2956e6ca4f198d076a885d040ac4e6477874297531095bcbc'
r = lzma.decompress(b)
assert len(r) == 28869
assert hashlib.sha256(r).hexdigest() == '3770fd70c9c4c9cf9a3ecb28218da1780d184c95ab50214e200e94689349b0ea'
units = json.loads(r)
assert len(units) == 6
out = Path(sys.argv[1] if len(sys.argv)>1 else 'RH08_FINISH')
out.mkdir(parents=True,exist_ok=True)
for name,source in units.items():
    assert Path(name).name == name
    (out/name).write_text(source,encoding='utf-8',newline='\n')
print('RH08_FINISH_INLINE_RECOVERY_PASS',len(units),len(r))
```
