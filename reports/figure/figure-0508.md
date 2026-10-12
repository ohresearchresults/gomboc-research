# figure-0508

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# CH95 — genuinely nonaffine MASS continuation: five exact nonwinners

## Result

**No strict110/additionalweak000 body was found. A new, genuinely nonaffine MASS descendant was constructed and exactly audited:** `CH95_MASS_RECON71_G6`, with **V71/E206/F137, C412, own strict312, additionalweak000 and primitivezero000**. Its physical landscape has no positive bars; its polar landscape has exactly two. The incoming literal MASS body had V75/E218/F145 and strict25/1/24, with 24 positive Q bars, not the class or facet labels of S3_PROJECT73. The literal input and auditor were used directly.

This is a **root-count and true-complexity improvement**, not stable-basin annihilation: 22 of the 24 positive Q features disappear, while the two surviving features become deeper. The new body retains r/R approximately 0.47333, close to MASS's 0.47905 and very different from the old S3 geometry. The G6 minimum selected positive TRUE-edge cosine is about 9.66748e-5, approximately twelve times the incoming MASS margin. Actual volume and centroid were rebuilt after every finite shape change; no reference-centre substitution was used.

Three fine independent freezes are own312; a coarse freeze and a subsequent BASE-targeted nonwinner are also preserved. All five exact new bodies have E206, therefore **43 actual edge units of headroom** below 249.

## Exact endpoints

All rows in this table have V71/E206/F137, additionalweak000 and primitivezero000. Coordinate bits mean the sufficient physical multiplier emitted by the inherited auditor, not a minimal denominator.

| Identity | strict S/U/H | Positive P/Q bars | r/R | Coordinate bits | Minimum selected true-edge cosine |
|---|---:|---:|---:|---:|---:|
| CH95_MASS_RECON71_G5 | 3/1/2 | 0/2 | 0.473330273572 | 71 | 0.0000306272167321 |
| CH95_MASS_RECON71_G6 | 3/1/2 | 0/2 | 0.473330805185 | 82 | 0.0000966747848646 |
| CH95_MASS_RECON71_G8 | 3/1/2 | 0/2 | 0.473330589059 | 111 | 0.000100271496521 |
| CH95_MASS_RECON71_G4 | 5/11/14 | 10/4 | 0.473348559005 | 58 | Not a U1 certificate |
| CH95_BASE_TARGET71_G6 | 5/1/4 | 0/4 | 0.461534850794 | 83 | 0.0000623322945234 |

G5, G6, G8 and G4 are independently rounded from the same saved binary64 HEX checkpoint using exact Fraction multiplication and ties-to-even. They are not successive grid-to-grid roundings. G4 genuinely creates ten physical bars and two additional small polar bars of birth-relative depth approximately 2.4477067e-9; none is discarded as noise.

For the preferred G6 endpoint:

- Actual filled volume is `120682771216622033/100000000000000000`.
- Actual centroid is `(0,-54151292437842885020329/4827310848664881320000000,0)`.
- Strict S are facets `[40,96,136]`; U is vertex `[66]`; H are true edges `[[2,51],[18,35]]`.
- The maximal facets are 136 triangles and one quadrilateral. BASE is facet136, cycle `[67,68,69,70]`.
- The input still has 75 rows. Rows `[2,4,37,39]` become nonextreme; they were not silently removed from the continuation input. Their two C2 orbits may reactivate in later geometry.

The actual top remains source row70, now extreme vertex66. Thus this result does not claim physical-root lineage turnover. It does establish nonaffinity: an invertible affine map cannot change the number of extreme vertices from 75 to 71.

G5 is the useful lower-arithmetic alternative. Its exact volume is `3620461629017401/3000000000000000`; its actual centroid is `(0,-16245308680947104383/1448184651606960400000,0)`. Its labels and complete packet sizes agree with G6, but its exact coordinates and fractions are distinct.

## The whole remaining Q package, not only the stable roots

Use the G6 audit with SHA-256 `31a055c46ce2c2105f1e35c92ac381e52d90c1829e08ae7b1c33efed1344b0cb` for the following facet indices. Define relative depth as `(birth-death)/birth`.

The dominant bar is peak96 to elder40: complete component **34 vertices / 36 cut edges**, relative depth approximately **0.500060636516**. The other bar is BASE136 to elder40: **25/20**, relative depth approximately **0.318623934172**. The incoming MASS had corresponding depths approximately 0.464262289750 and 0.275853488871, with components 37/39 and 21/16. Hence the dominant interface shrinks while the BASE interface grows, and **both surviving wells deepen**. This is not monotone progress under every merit function.

Complete G6 strict-upper packets, true dual cuts and attaining paths:

```json
{"peak":96,"elder":40,"component":[72,73,74,75,76,77,78,79,80,81,82,83,85,86,88,89,91,92,94,95,96,109,112,114,115,116,117,118,120,121,124,132,133,134],"cut":[[1,116],[20,124],[23,121],[24,117],[25,132],[26,132],[32,133],[33,133],[50,82],[56,80],[62,79],[65,72],[66,72],[67,73],[68,74],[69,76],[70,77],[71,78],[75,100],[81,101],[83,84],[84,85],[86,87],[87,91],[88,102],[89,103],[92,93],[93,96],[94,105],[95,106],[108,109],[110,112],[113,114],[119,120],[123,124],[134,135]],"path":[96,95,94,92,91,86,89,88,85,83,82,80,81,79,78,77,76,74,75,73,72,65,59,63,99,97,98,136,4,0,6,8,10,11,12,13,14,16,17,18,19,20,21,23,24,25,26,27,29,32,33,34,35,38,40],"death_edges":[[65,72],[11,12]]}
{"peak":136,"elder":40,"component":[0,1,2,3,4,5,6,7,8,10,11,45,48,52,53,57,58,59,63,65,97,98,99,113,136],"cut":[[1,116],[2,119],[6,9],[7,119],[10,122],[11,12],[11,125],[30,136],[43,45],[45,46],[48,49],[53,54],[54,57],[59,60],[64,65],[65,72],[99,100],[104,136],[111,113],[113,114]],"path":[136,4,0,6,8,10,11,12,13,14,16,17,18,19,20,21,23,24,25,26,27,29,32,33,34,35,38,40],"death_edges":[[11,12]]}
```

The full regenerated audits include exact birth/death fractions, every graph node and edge, all equilibrium indices and the physical escape forest; the lists above do not replace those generated certificates.

Both unwanted stable triangles contain the unique physical U:

`face40=[8,65,66]`, with source rows `[10,69,70]`;

`face96=[32,66,41]`, with source rows `[34,70,45]`.

The actual saddle edges correspond to source pairs `[3,55]` and `[20,38]`. Therefore the stable top star and the physical escape/death interface are distinct, coupled carriers. Repairing one local outgoing polar score does not by itself modify the complete two-sided package.

## New exact local U1 certificates

`check95.py` additionally verifies a full-dimensional Gram-metric neighbourhood of physical U1 for the new bodies. This is a **feasible local cell**, not an affine exclusion and not a joint S1/U1 certificate.

For every selected positive true-edge escape x to x+d, and every negative outgoing top-root edge, let s be the positive signed margin. The verifier checks exactly

`s^2 > delta^2 |x|^2 |d|^2`.

For symmetric H with operator norm at most delta, `|x^T H d| <= delta |x||d| < s`. Hence all selected escapes and every strict negative root exit survive under `G=I+H`. Since delta<1, G is positive definite. Positive escapes strictly increase squared G-radius and connect every nonroot to the existing root. Consequently the affine image remains physical U1 with no additional weak U.

The verified radii are **delta=1/32768 for G5** and **delta=1/16384 for G6, G8 and BASE_TARGET_G6**. The same checker verifies 1/131072 for the literal parent as a comparison. Every exact positive slack is regenerated in `CH95_HANDOFF_REPORT.json`. No claim is made that these balls preserve S or exclude a remote S1 affine chamber.

The new G5/G6/G8 and BASE_TARGET_G6 have **zero retained-halfspace mass-floor blockers**, tested at their own new bottom heights and unchanged top height. The parent theorem and its scope are inherited, not newly invented here. The zero count is only a necessary-screen result. In particular, G6 still has BASE-distance/inradius approximately **1.167440541006**, so BASE is not the uniquely nearest support.

## Numerical construction and finite failures

All numerical work below is new. It does not replay the unavailable old LEAD optimisation. Variables are the 105 coordinates of 35 half-points and three bottom-rectangle parameters; mates are imposed exactly by C2 and the axial top is fixed at `(0,1,0)`. Each evaluation rebuilds the floating hull, determinant-weighted filled volume and first moment, then the polar at that same physical centroid.

The successful reconsolidation uses all-point physical cosine escapes, omitting the top root, and polar cosine escapes omitting BASE and one C2 pair selected by maximal non-BASE polar norm. Same-orbit polar candidates are removed because their outgoing dot products are nonpositive. It does **not** claim that arbitrary chosen all-point witnesses are true edges: the exact endpoint auditor constructs and checks a separate true-edge forest.

Its loss is

`100 sum relu(1e-4-bestPhysicalCosine)^2 + sum relu(1e-4-bestPolarCosine)^2 + 1e-8 ||parameters-parent||^2`,

with the stated three polar exemptions. This deliberately seeks S3/U1 reconsolidation, not a disguised S1 certificate. L-BFGS-B took **75 iterations / 176 evaluations**, passing through temporary extra physical roots, and ended numerical S3/U1. The independent exact freezes established the classes in the table.

Complete campaign ledger:

| Run | Actual work | Endpoint / limitation |
|---|---|---|
| flowA | SLSQP, requested and completed160 iterations;416 evaluations | BASE-rooted whole-Q log energy about0.77905069 to0.12718925; numerical S43/U25. Hard inequalities were not satisfied at termination. |
| flowB | 21 accepted feasible steps and one failed attempt;471 evaluations | U1 retained numerically; energy only to0.77620215. Step sizes collapsed at the imposed2e-6 guard. This is not stationarity. |
| flowC | Restart of flowA; requested450; only448 callback records and904 evaluations survived | Last saved energy0.101974464516, numerical S43/U45. The shell interrupted the run. No450-step completion or terminal result is claimed. |
| repairA | L-BFGS-B75/176 from literal MASS | Numerical S3/U1; source of the four independently audited grids. |
| targetA | BASE-only polar exemption,39/193 from repairA | Numerical S5/U1; independently audited BASE_TARGET71_G6 is exact514, not110. |

The entire BASE-target attempt is a useful negative control. A small final non-BASE polar cosine deficit, about0.00516, coexists with a dominant exact Q depth about **0.515088699693**, a BASE depth about **0.318897827920**, and two additional exact singleton Q bars of depth **0.0000265712042030**. Local score reduction has again transferred or fragmented stable roots, rather than annihilating the whole Q package.

Every method is included in full in the capsule, together with all five frozen terminal/last-accepted checkpoints, their identities and the complete run-level ledger. The supplementary archive also preserves every captured per-iteration ledger. Cross-platform bitwise replay of optimiser trajectories is not claimed. Exact endpoint recovery needs no optimiser or numerical library. None of these finite campaigns is an exclusion of its parameter family.

## Literal G6 geometry

For direct recovery of the principal body, divide this entire half-array and tail by 1000000. Append all 35 mates `(-x,y,-z)`, then top `(0,1000000,0)`, then the four tail corners `(a,b,c),(-a,b,c),(-a,b,-c),(a,b,-c)`. Keep all75 source rows, including the four nonextreme ones. Take the convex hull, compute its filled-volume centroid and subtract that centroid only after integration.

```python
HALF_G6 = [[457549,-476424,4200],[455928,-469860,142701],[431226,-462724,253058],[414594,-463893,367648],[342861,-451364,453247],[275617,-453498,545481],[183681,-430269,611203],[73045,-412691,657589],[-41899,-373148,694522],[-166799,-352874,697732],[-290990,-325449,681518],[-406235,-348320,621819],[-514129,-298397,578415],[-606553,-271337,509729],[-684329,-236186,435162],[-745583,-199370,358049],[-792094,-167522,278140],[-824011,-120466,213821],[-845480,-77645,153092],[-857900,-32400,104215],[-864721,797,54958],[-866363,46447,19231],[-863907,92273,-6964],[-857982,140669,-25189],[-848740,190767,-38786],[-835913,242739,-49462],[-818986,296589,-59337],[-797253,352444,-69836],[-769751,410523,-81558],[-735330,470471,-96530],[-692399,533138,-113400],[-638137,599783,-125527],[-569013,670355,-133493],[-479812,745976,-130336],[-347680,832991,-133654]]
TAIL_G6 = [223168,-570002,405531]
```

The capsule below also carries the original MASS input, all original binary64 HEX pins and the exact freezer. Thus it reconstructs the G5/G8 alternatives and the nonwinning controls without using the G6 table as a rounding parent.

## Audit, source fidelity and limitations

The complete uploaded journal and all three source files were read, including the literal parent payload. The three source bytes match their advertised hashes: exact_lead.py11008B `6b41211b97ddc5c026736d6a9e5670deb4739cd985fccab7dd40d681224d3923`; recover_lead.py9006B `0cb0cd79115afb6adde8fbbdb2f08a3e03d6b56a7143b6947f2646d0086e77f8`; metrics_lead.py1992B `a2d991bdda7e43b28948e60b85b69083f0b6d7bd896b871fb9cc6aa54137b4ac`.

There is a transport-identity discrepancy that I cannot resolve from the supplied pack: the journal advertises immutable parent `figure-0504` as35434B/SHA `f740e005dbf2f0c6e453b2e714bad2d5264ee3cf0655192400b4dd9f953fba04`, while the literal substring from its `# QF71` heading through this uploaded journal's EOF is35030B/SHA `74f8b7d539722942a51857dbe341fd01d095f348df43eae683b35ff759174a6f`. The inner encoded qf71_recover.py nevertheless decodes to exactly21772B/SHA `de29fe2a20d974364e0694cc023e8bfd928d5dc999e7eb09c13443003f2ea4e5`, matching the advertised inner source. No geometry or mathematical conflict was identified. I do not claim the outer advertised hash was reproduced.

The full old affine proof and old numerical-producer materials mentioned by ID are not supplied. They were not reconstructed or newly verified. No new result here depends on their missing bytes: the new exact capsule contains the literal MASS input and the standalone auditor. The old affine conclusion is inherited context only; it is not transferred to the changed71-vertex body.

Exact acceptance uses exhaustive supporting triples, maximal polygonal faces and true two-owner edges, two-origin filled-volume integration, direct facet-foot/polar agreement, full mixed edge-cone and segment tests, additionalweak distinct from primitive zeros, and simultaneous equal-level complete P/Q forests. These are the inherited full audit and new exact certificate checks, **not two independently written full mechanical auditors**. Cube, tetrahedron and weak-prism controls passed. Two cold executions regenerated all13 exact receipts; repeated execution is not independent mathematics.

## Recovery and continuation

Save the complete code below as `RECOVER_CH95.py`, then run:

```sh
python -B -S RECOVER_CH95.py CH95_REPLAY
```

Exact environment actually used: **CPython3.13.5, standard library, assertions enabled**. The recovered numerical producers additionally use NumPy2.3.5, SciPy1.17.0 and Torch2.10.0+cpu, float64 and single threads. Their full commands and nondefault settings are in `NUMERICAL_LEDGER.json` and in their complete sources.

The decoder contains16 complete units: eight Python units, literal parent input, exact receipt manifest, run-level numerical ledger and all five frozen numerical checkpoints. Decoded canonical dictionary:70748B, SHA `755ccaea554f57bcc1eac4511974b91f8a595b36d964f89027f22453ed8520cb`. Compressed XZ:19060B, SHA `981ee5335f65a1e5086a864472650402ac0f1376ceae8720c839738fbc6a8542`. The supplied decoder file is24851B, SHA `17026c3c724a87ad5d812f27a7ca01875e1273fc223d5ff9befc42180f51a176`.

Principal observed receipts:

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| G5 input |3968|a1bd4183302e1413025e5e9142f1e808a249c7f4b6b43f1acf21630e7f67ac03|
| G5 audit |144560|594d7c314a384fa4edde4bd55fbbeb2f5ee1e85e10bf46848adf6bcdd7ab1d7a|
| G6 input |4192|838ff2df343fa0da01b93a2a187a429c5949d390a0bb4c608487665eab03efeb|
| G6 audit |158442|31a055c46ce2c2105f1e35c92ac381e52d90c1829e08ae7b1c33efed1344b0cb|
| G8 audit |190824|588bfa67a1150bfb5e5be08bcd2a2a8e1015721d0f735e913f61fd480a0948ad|
| G4 control audit |139252|76340dc400d54cd0356312299ce347c446f3c167811bc495a54d02b6b53ba9b8|
| BASE_TARGET G6 audit |161148|ca1fbb40fa68d4af5dd11d1dd856b28c025a3905db4d0944caff9195f75f5ec4|
| CH95_HANDOFF_REPORT.json |145774|e61394a651e93979019bd899853eeacb0c313ad1e8b1dd431ad9c921707f1c53|

The complete13-receipt manifest, not just this table, is inside the capsule. Observed terminal markers:

`LEAD_C2_CUBE_TETRA_WEAK_PRISM_CONTROLS_PASS`

`CH95_FIVE_NEW_EXACT_BODIES_AND_U1_CELLS_PASS 5`

`CH95_SOURCE_ONLY_FIVE_NEW_BODIES_THIRTEEN_RECEIPTS_PASS 13`

`CH95_INLINE_RECOVERY_PASS 16 70748`

**Most useful continuation:** use G6's thicker S3/U1 geometry and its actual true-edge reserve as the new nonaffine entrance. Jointly move the top-star source carriers `{10,34,45,69}`, the current saddle-interface carriers `{3,20,38,55}`, and BASE parameters, while judging the complete34/36 and25/20 Q packages at the new filled centroid. These labels belong only to this new input. They are a suggested coupled block, not a proved sufficient operation or restriction of the search space. Allow temporary roots and incidence changes. Inactive source rows are deliberately retained for possible reactivation. The successful quota-three repair is a reconsolidation tool; repeating its near-zero loss cannot by itself produce S1. A successful continuation must turn BASE into the actual sole stable root, not merely remove the remaining small local deficits.

Supplementary copies, not the sole recovery data: complete archive including all captured per-iteration ledgers (`CH95_COMPLETE_SUPPLEMENT.zip`), decoder (`RECOVER_CH95.py`), full exact handoff report (`CH95_HANDOFF_REPORT.json`).

### Complete self-contained recovery source

```python
"""Complete CH95 source-only recovery; CPython3.13.5 standard library.
Usage: python -B -S RECOVER_CH95.py OUT
"""
import base64,lzma,json,hashlib,sys,subprocess
from pathlib import Path
PAYLOAD="""
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;S^g+GF<>Yh=iqrocag;lg9zQDdLTm8Uv={sAxFr599no$+r;V;e&{~6KQ}?Zf5uA!U+6}
2QtqUb!d%gN|7UI5$u}-HhV!}ElYK`bb##C7j3d&790b(Z2!W~pl&cn4soetHvDIWj{~)_f5yJcPKs25ftR>o2}~?-N-;{*g5+;z
b>X_|W4?k%&aC2E7o|Mgl!L9Ra}~&9tr@WMQoPd+!?>@`nk`~=Cd}hP5CS9Z+xiF8`)m~%>G)L>k)^}K{_*=uIAoMRoj00zKe>1J
(_r{#4Aun~WR#$-^Nj2SRpqHr<=70zfYxvqPIauoHZMhmna{<`2}VNMLqqc$vZU*I4_!C6A$C=)>USS+cV_Pm)wE#$10jML@id@P
dwm6&o^x+fZq$V_l~&$ySWZGcBZo>Mo9)G%w)u8Rqy9|gr&Yy`A-w0rwQt`Uc`=+uGSzSc+*P{IzQ1&7=&(R=pDSEzL5J^bF&Zxc
12d`MF-RyUu(Hj3v+9mTC=8gC{4a<BYEWaX&4Ce6uRW~n{g$rdV1Zk5-P(gc;9O^Psjd6q>J$nrJh=L+7?Budp((LxTYft)4Rs@U
S`bA@L|uPjQ~!EMAFc+s<*heDeQD^AZ?h4&;2i6SK0963cjS6vnJGt`;79)ruN$$i{8YCpI!UHqGPJRS4&s9E`|ZBMTzPM<k=?ot
Rmq0U{%z?XOE}Z;Wuhyz!cALkXh)4tdzN-ibc!Fojpu7<$r}e<R8XLMP^WdyV}^bGhROKC)V)$+FZSJ&737Xj>Ida(6l-O^R?4Au
y(}YW=bN!7{=_Arvx8(Lvtw*=k%9oqei!VKyPnSFyb7X5Vx~G0c$tna7TKVQ$C6PsondlFvRCQ(gF{ymXGKLD!u<bE#s}n%wKEb~
6RnO`&Rrf>x}p8s*iIOPYHzVf)2TW6mU(^FyDz$%x#g>~3U>oNu6Y^P$8fnjA)c8qz2RM<zs&vCy1%``axyVc?=aE5Y9I#{`eg&d
CHtM9-Y~2-U?UY{;l2)Cw6N5|<&axqyN6h%YWS3W2UW~=7uy~B_k&k6@gITl7c4gO;jyM?>|CNK9{Pu(e~jKGsn!ex{AXviyQ;D_
Zh`(%T<S^D%mGc6_c}#m_!7Aqid{Dm7?Q-mo&c$!b4dNgJN0PxsQxzx00CUc+9Nd;PcOTC^IUC;sTy`<N+4W5@%r=xZYzz-fmyu>
OFX?y%*EsLm$=eY`2_{?1eTx}t1aqrK!V9br%grrBfgL`>=a~;u#JpuM0zI9O1OSNn*ccrhNxie-M02)3y^1t<pd*S;^Y4j^%EIp
D3ro@6*|iwZLqAw-0=s{J>(C)3@Ov34DUb*&UZfaJQB|poRJpRSO9PxRHQZYe^)dSLbakSh+6+B69O|9hkha-;vT;0bVk8`5acnq
(A*cUXTU9j_rAv115-1!_%J&<fAJ>tJZ~L}W`xj*<L_HRA4l+TIr?=+Yft~5779+U0{>=S;z7+WP_*FNy*5>NKmq?s<t4hEjx5E1
CQTx|<S2+4?2wmXjJiEjey>;Qp%yLKa=J4lnun;q7J!^A@k11}5ZWR@1CRQqDV9{q>wCKWN_gJ!6hsa-ba1EH1I3{(=>Kfx6aaWM
tMjMsy0uVY`?1+>|9=4u*DizZTWFr3>-w1J7CUlf+alz3x6#)Ye4*!%bV`s}2yV@hb2-#TNfKPX)E%Y9-1QkggXn$w|L1pnA8sa`
vgX2Ry(nLP;jA5k6(uyxsDbLqLC3s~5Mcp4%o=96QqU|2z(wyXWdsa9ZO)kDQd9hq9AmnWU>@%NcH5CqB>WSkFfGbIFn06nG1HED
HGp{hf(tmOfDZIOGY{4!>Z&#5SU+lVp9U+J1o>ee8yF_HiF0bdYUhR$=CAIdF=Kp~?JDG(2z5zE;R9UB3Y2OxX^@rIlViAO)^(G(
6vR1!ms9z}uNKRqkjX@|*g|SDZdlU~n*D_ovYI1-2NEr~4xO>V=rTR3NbwLMLkhW>wj4z*N4X0Oh4CRQ>c+btH0%dvbT!?-IP-(i
34!pumRQ_`O#uID=K0SBK{CJpSMAnV6EE!g`({sfWyH*Q=v~Bgr<KqH#KU9%?2R^cXS@DQ*#)#Jj{#g~Jh>poHvWc^0*&BNpK<Qr
o22TO=z`q+0NhzI+xN2&X6kg~D^3s8_8C3ELV}HX6hWEfKXFv6REmJ|SdQ~PP->*yJU25`p#UbeK7>(Mn}mAtiuM@)(To=WeLy3%
&cFZd*K0Zo)Y6%j_OwU<trW}HGH<=&z86h3k7@J!^c3XDNp*?L+Y(<ok6<vaocWdEQ#82k-nA%Ui-&%mI^scapaCEs5>k`)sZRq1
?<VQ&N>U8{6}Y=@qrDIR5ax;|U5g^y354c$6Yz1C1_~H+n3rLtq;ZErzfuGEi`?6)Cp4=j-3tb?Nuo@-;*z>@K4?kEy~b;oo32_G
h)OEypfo}*Z5i<BrL*41$#@oC3ot|HZ-Yl@FzP!o6=S1c%>Wer_T?V7SRyx{;nQl0jBuEukG^;>Sj^f&jMjkvYt8`X!*`TZ^|bca
&iuMr!+-`j`u2?=ZWVSz{a+O*jveQ2hhPlQ==-QVSCLT>{FrRgSnUtF59{~B0Iz=k{rw5vMeI29l@<mD)aCqoFyXHSRn@1bB4d`v
@2B|Bt?y5Vy;2#+KuTvD6kR}|=yntny0g?~*#j&<`a*Clu4p!743>~)EQnw=u^lL69sf!s30nAR=BA*++l%)Oxo{^Va)-|@1%iWc
$6b!pta1w};#*B$*r`2T+$x6%DbdYH@H}8hamT%0rXGu^+Vht4FW`Xb2k7#Bp{NPUc3%T6l0&@hoTTX}Z_dsKAt1BttX3I@Jzaxw
3t-eec1Sl~`onn#7K60-(~2q)<<rN=D{QnjqRUG{gpF>H2R^6^u)^tn4zef-6|ymXM|84Y_SnhgrRCdU9`ON<uB0OzfY(BG54bXY
lS4v8`dr?ay%o=@EcKXB>s}&z?|zr$8Iw_|q!iJCnKK5um8dLlc9y|{(oehK<aNM5+MW@Rs3P$+w>mDP?<Ch!jPnpsKma?(dl{VP
h-Gon-smlhr<Z~0J1#nn)GxbbhT6>WFwV~>PNL%ROel`6;8iXzt%+;K7zyHjtaFgxR+ix-4UXOde#D_|s&S@gVW!q<=&sFffC*Z<
B*g^c6L%87T^OizVl1s7)^jLIgo7y=VSNEaI2e!cvcL^hE%H^S@Oa;z@IMTjsa^Xr%L=C+|G=UxV(^8Wm*5>nz|gv_w`506shlRp
!a<m^hwrDk-Ox8+YJD&yz1Nfk<~d6$wL0v;b}2j68>{Yt_zKa@&e?xk1T7?aC7_6~1tD)QYY13JSNY4R+GOZ>(Tsvx1@lO`x=q=9
O!Nu?<zsO3gli}ANmvjiaEKBMY9gz7T%zclQmRApQlQV7fmV4QKZ$17pkKz49wtf4enIt^4jDt$SOcmP>=Z)wWbGPRKc(<AHV!s1
t636+oLro-7K6U6C3Wa<fQkG9nSBqFC;3O5`AiTqIu{j2+kMxZjElDy#dhH}EXf_=1&PmBj;rx?Y_%ZGep(v&GXU;@P^AuuIh2P-
3_7Y{5$5MS)<@kk5q^$Ki=BUJE~^zCRc8qpzIanT1!)L1VD)=*$m}=SFPU{fYYK_C=I;kXy2GR}`rw<&0s^0@Sd%$xFNmH?hq;DA
+uXUOr=Q|ZdtK+8B4K6dRH@CLoVZIafbz@{)iGGlJCcLhd+<~T+!p-x<?~z)Gf$w-t6DHJf2~4ghNnVb6}vTi5tA{V)Nr&U*hl_`
7iHTVdRrP?-tva10FyT6@x)unVP?{DNGa^?VpXkiUrI5v>({W8Oahf)yl|L#t_NQ-fC~aS;pMJNE05VAE?CZGU-xe;93=<V(Sgl_
h6NR+sce{;bHwFQHv|1dnf<GtN8DW!bz-y86+L>T+k{vwmc-!k-|E-QKP{b*y>dG_BqZ4R-ce74BaM{sC;G7-m1*YGwRI1W8k`_D
&Etqp>$fs9PG68kZNA_h>^6x|NW`?@mFX<vK77rHL?(XItB5G8_n_z@zu;T(YJ7e&^*+$fO4j960edo;KIS8V=w@!Fa$>$<P$&5s
NIUO2n7`%}!R~8Op(zO~n{HQT455A_&P9+bPY|zVOH(*^TM6%f=woH&c_+qDaRUbuf;z6xyFuCKOdPIBJT%pO)*3sE+fa?@VsawP
dNAZC&9@1T#ksBf_i;=d+I_ZjhHpr}5068iF6IhLV=!|F-9FfXu@H(pLSZe8O~|5iE`iG93~uiKle6xT;sam&0o=uNa_P2LYS&O*
c`+$|d0%M7dDB&?$}mJOIu>AV#{1zP>YwU({=V!rE@9__qZMxvqjaagPQop;WbKAK3ETMo%c$li?#axENNjhPE(-U|;<s9xRikV_
cMCe=HF?$DScGW9N4kJZIy8iO7z??#QA#?i;gDq2-Algq(iS<IdtF<pcXW`F4K4}n6J|i}NU@FaQgGArLmrdbh!p>w4IL}L_m^|N
^g0$n6*I>y>6e3%x=-2&`;L;CURCKg4s|?~8O(u(lKH#!VIUbmWQL8U=?DtY+)Yr6xBX-R(uNkz2#WJs)3Bz#LZip)sp7T%2PfsQ
0ma#um>Y-SWLc$`5=DW&v6G;oKcF^)N&=|)EEcWLiH{l<+FS{Cs>0&l`+TAHo=CvvHQ<AFu}<)PRLZk75geTSCCKGd_SH%AK$YVL
K)n;!gM;JR+>`hNdC{Z;X)x09O+l|41IY!t$nZCQqJ5L<IY~ZarTHY32m#{eVdd&}s`X2~Ro4w!zq7K07F!YfGecct&Y)0^Ur$ZA
5W{EKLL6?%9ie(bS-;GV1(v5b9cZea%tU5~iMDlj%zmvWaC0L~{z#EUrSHve`yuo@v&Z357C;*s62sMPf)gfC`_<QkC>MaD1-rep
X{oulsk~;0rn!l!SS|}>UAIyvn(IUg!mWKi8C~x_B5614(9uxDCDdm@v9A+2aZah?sS%qR;z}G_m!L{k(kf5!N(pnxPl3VbTaP$A
Ut#-iS(5@=Uz3|DT^!N^yREUlXRu)F(=Why#J$wS`b*%^*(>hz$xhQnoM{)A0gA?;RSOcKDk*wWTgy5cDi_EDZ7R;Jla=p)BSp7x
%k%fZEnWX)(3%6Vts0mJU*YgHWGSY<gZrbZpw(_6p4#MwF^LDTA&0I~)6OOwylmuU^&jjnDGEF4gIG}9eX&C(Co7qlE97jE@^EXl
5ZlL+)gOnG&g-_N`&j$4V^{gq8DYN=Q*U}4mLd5+Z~sA!Ydb4F@A+5Ah)g@pxx53X<-PO0JG7i3SWtz*f@E$5^7xb!a<Abzace{r
+2Tb^gcdH`ouvI8H&B^t=E`ybnD73b(y&(q!e1PBrK&Hg(-f0{6BKbV$=kJTJ#ydWN>Ge!N%DRE*Zf^rH=cP$pHaGu*6d)n`b8Sk
m+%kmvv!l+p^%f6I(goCV<iakRWzT{B;8LWnQs)Yq&Igg-e6%n_cU^%JOC0W|6LTKEwjKw3BOH>IuCEvEXWS5vg_=AHOT6s$t18N
0k_^d?w&h9_zmX>gngH&iCUiy5I?qcx*Or_A?u9pC|x^2@&lz~AcxcKHdEeJfzE;eT7(fOgyc7u-a>$V_y-4H;Amh!;njG$AlXP{
I%!fllS+BH49=jh69`RR+h0O5LF^kBpAQ=im-Ja`etb#U@(R(|gXvou<7=joC-HrE>dLQXN^T?Bofo}NDTU+idN_Y>2%ez5p>Z;c
k;7@=ed!nj-3-AZRULEuGOY&S#o5)fPQ<7v7^l}xTXJgiYp!x|SyFE%?{7t`q)s8ieY(D#RIKKZN4X#|l#tR`eR!tl={TZ)5=cBo
_T#&Ol6lLO76Nr_*!&9#sp?nNJEd`dn<fif9t4Ito@nl`<WPbsMoid0_MahWMGXl*WUZ`b<gjNnQ_r7J#EkN5c*}p{8*Wd3loQ&e
>$y3WU{<n~obIv@hGQ$<gBaZw+Q6m{SiWd>TA<M+Tr;7QzN>Ga=>cnkmgiD1B+$Kux}6ruH0dE@hX5DxZcm^S%2vPO@ujcfs(_wZ
1v}w#5{1grd&kYPS^GT=!U*wFTMRd>EoFUxo7@fnKtWx`@fy2K<-_GuD3=dAi-4SSQ9F*k%wlyyh<*FVZuMxujkkl{v}uZ7e<bi#
A#XRB#q<JpdV*tGz8g{?tBx92u&|6s&HN^o^4iA(qDX?NPNLq}YyoDJHkn;q4M|2&cbnfT#@sR(hJ93C3Qxc!DV1=-ic!$jBwWl&
MQTxvaZd}z$@uMd$(4|N^-*G!JK~z5`Fz^S=`DU^_0r|Ym0TQRTq#|r=Hu+8K@NG_p%(J;lR+F@%uf5;R12*NeRrCTB;7ceyWlAt
{o0cqNf$}jU#e0Kxvu<jCt9u406_0vrR7v~$9p3!q%UCkhc)WPU<MIQn1$nE9Pch06S4Db`R=i2aP2R!*iIBA!EYLO)|Fc~2;4IR
A?88#T&etT`XDi67RyBGfMRzwj@DgkE}0r5+6=J0m!?;C8tKOB9u;EYpaT0gOSlgX^?ZBc8;|L57HI|=06z_<*8L^H`tJ_un^88i
6cV1Cd#(9{rjN`=K?Y#$O#>^+SJWG6%n;$YLYb8hS-%Pkc8pYrBL*%#$!2Q)V=9xE$9Iu};2@e=`kd%irWc>Pw{AGzQ-5rN(_-^~
&FMp?lmt<?cJ2xe(cCj{E=JF)Qoz2%vXecCt1W*G$kzw&J~xV(dpZ3);Wrg*?bq;U+)MhPy);{D_t!dt%}8S78`4pYAQ-{2^8K#b
$LF%_-ZF|Pv&uwpJA{Qf#`2Rb5r6YiQCXXZkd_oy@<khbZ~+W(p!aU1(pqr9%E}E%ML5^3q184=b?gF@vK;=L_j+hmkBxtpDSAX9
y%Gi|EXQoVhXi>-uQ$CmMjs_zWZ=LTD_yxUz|V1vg2+}I>U>i?+=~JSgX!{q#^Q#=R3BOh>LA(QBt4#)=!fKrUSwl|hhT{;Ss?GM
6k6m6ezw2NH(!}>co@6OYp-{cjiBum)rJy#U~wBX8|Y^&3gIf1y>FfQj2!pf4H2&Sf{~8z_sG0GJ@aDci~;3c#CDrIzLfSmPq~?0
9Ztc#ptVona>K|p@vlFJ`L?7F{acv>nZX4nrgM0Jg+oNyJliX**U{@>?&ci-;Za@mRWWXpAyl`%g2|(u&FH5Uq4cI<gYit=vKJ;u
d5ZM@J}xS6+}CT?f?dVFlRDjs0G1wVKs##MN_LFooF;~*4P>63+zd7U0krA&CX%o}K2hypG0(!G<C5yxYSmIuXGn*c8$~&|8Ssg)
(K{$nr@1Ax*>8F(aeB+=7#W|1)4HBQcm%6LAC_?t8KuJoZ<A<#s{*F8`ds`QUj^9zalQ*jmg$F&OK%zpV__)vQxChEmdEfZ#+4_G
g~xQDRBZAhAYWu8!g{mb!=cgH$;GOy_T4<LOsDaCi&=if-t_WT_IsTgNk;^V)wOQ!rtL0)Nq)%yipUVUVEgTfQQ&gp5sh1=^%79f
#RgWx1&T8d3u@x@c0eq@mru^@JQpU+82eq-jMd#3ft=#S%vu3^-xAWzr1c)Vsu2)840=hWrXR=$Ov3gFNte7MCik_~b5p};<Qd=y
D0qL}hPP$AaO(;iNwm!|^9vRD(B$_X>9=04Av>GzYl3Ae9PrN74#=e44qzG)Bz$>G)|%bC`<8D$OGgySBFqMFy9D+SU786kl@7YO
mkuNEV%`?e;{>>qCp^ZuP!A%q2c8A<Q>BK4;*SI2*6BSp690ltb%o)4rEsYZQI(?el4kLb^rh-H2s6qVzvwG>C9(?)@&twaol?%=
@1{dY!O9~n)KCBnr2Vo!D9F$VBMG`^yE(3d9arLiTOH)4#>)knbJXySV-Z+iC^E}qcjgEG{&Sniz}p?gJf`2z;znB!n2!(JEk19`
hOI2OlXTNd!E;8h5$lCU+uJ^5hbKLiT!azg2v>#dYA>%Cau&jN0A!98DB**!GJ6syQW$ta*X8IhM==t-Oyxy##XiaMxc90V2RO&*
MU2k$DYt~gT%(pBSKhr6dg(n=<r&k<@HWWanK1Ud4Eo@MTE?@w97g0Saz4HO@(v&s4WD}af4x^7%|H?!q0`f_li-1=-y-Hi71yC3
*NE>;K$^`{d1Z{P0~?m*nJvmv^zT=<*pI&K#)3KH%G$15)GRM*HN5Ote?eDB#__dZAZQ$+Cl{}G=NOc17A|VYN0W+gQYpA+{<9l&
vp2DU)d@yTaX)g29P>$}iYL`ESS#pVh-q__H%Lr8IFb`KaIwFB+l9#6welEDg<X;HR@QrHZOfhwD6#$^Ye%R4sgzaf1sz`L<w`>s
DA7%#Gm@~rgi$v<^a<*0rW+fifuV$efOT;}Cm>#JxRM>OGV$97aRxVitD-OB`98?_N_tt-xNiVBonY259%eBDJORrAionK!SFj=%
w<WCeFKHtb3f|xI!RX~mfv*c+czt9U3}q)}k#3pf%H=g_<Pq!Kj=A@;k*b|5ePz!TS6)~;NKV{0_1JJz9u}sVzFrVBEL>Z(Dj^*9
;gKS}Q%L*d>p9v17vUd)>vH!c&6NRded~bJq5HvHB_W>7Lw;z$au{stR@^i9AAuc@5&jJy58bUXgh-L&6C>8$^i&&HHruE$s>ura
rYPQR>U`}*tJ1wgX-oydBKh6Wf0GC$a06X5uVPMZ>c2h&a_0Q+D75cDMRW|Cn-tdcL`aOvK`kDn>VOXca2e1UVcZiEUj=10W#SMD
*&*9<r?uuPD}jZIY+#49k)@mBe+{S6<b(ny#J?%EdCMgKT--%e-Gt$y>J91&!A`ojg-j6EQ2PTEWe`5YnQ%&|dz0iiR?_J6wt4<h
&TM_+bU0P5EWPI^(xT)pYrNv3K*dzcD=X-H!2Txz<@-(Pmz@m#<~J8a7CfYp#`c&^4&|<5p;q}(a~c2HLtTWUxsb^6vFJkG0^aVm
_kI{)WpjTT`nE4~MKljCuRRFByBpIbxMz2RP6f_C5bA)y6f?dnUm0J+c7PY6uvYzs+x|jNR0ht`8Cn!^eK%^HH0mFMdc{l~ERI6<
6fyR{(CE*HBz1*SsaBHQJ+(2ycfkR|bSRe=QD*oT1!!(A8=fJ-SWDUkpQ_{>GA}~K4n>q#Ds>KwP+OG16+-?uJ>dwE7Y_2&lTO6;
_uF~RnyfLjg%T-rH<xvR8UONDgnD>IMVNA_WaX2q*=G+RlT4sV9-EW!*nw{<5dnwW2j=&U2st-vz6}}#Ac~m`7@(>$di5y>$&T|-
#h>#(7&4pt6`{>|eOX!)JBF$}P9@tqgkMv}`1&t;ay*iD3?=i0<Jb*3#d_ckCTTUKFM7oLQ}%~SY_{q@&s1P)aCLx$nnB_R);aLF
3Tz$hCfMPWr-#<Gy-miP6Go&r4m%up&oe`2?ZDQ{3IeMz3WX)i(hKnfem6NbNHh^gHg$wu_@F`s9{6f2*2qyf1@3)uJ1a#41;kbI
mR)}TZ1rc1&X6ru$2mawClQ}P<M(<0W2*&>0|IB35p|_LSR}3#RRWbwIc`^^*@U6}WEXQ&hG3=l<UViSj}jEGWL%mY;|pP^JE*B!
H6~iC*ASFm0U_%4P@F(0S~dy!*H-{V#7cR%cPQ`N=heGK%ouXZjstOTXs?BjIw*uH)KrD^0r`k7(qaePBhu#LBi9gtPg=PohRw>n
4Yg#Z5Zg=0a9ivn>!U<88OA-%ZqdD?DAAky9wG3f>Zl8loor+-Q9ya2LgT83GU?ZPO`iRAnU;c@^$n7{Co`|D{v^;iPP|B46qqvi
-O{LX%HmGt{Zy%lv2}yzFGx|r7v!2CCwP<mWHB4@mI0ZkJEESZAR(dPHdf8es;L&EoH8{unN@GPNoIDVQLhL@>O))Q<dFXec5R1S
gjOO$j6yiIF|oA{MlFu7EZm=j6#>!Mgg-eKyRymKWKjlVD?JXtqY=M6f^!tPhMCa>VJ>RJ>8zA~ts44$FHk`gaBk1b@F8-Fx3_>W
2Dpro2u;^*C3`R&>xn6=ZyV(o5`Vw&k`1cnx7@_Oig<vgO1%R&Vr+!8_H2Lf8;w-X1rA^&S8}=Hh2Gjp1pWaghv*L>oZT#vJ_xhw
F^gIAS5MN~VHs4;)~qb~TXEgWAG&$Z{_D<x5fIQR@7r(5COn~emHAIq<$nm#%MD~|hQcPy_SU!HCKME2Uh8^gO;gEx0?f<oV=T-2
Idv9Ot>}h_gDx5#V@+%N!xss~dOeI6S6TFvm+h|V`kh^GO+QD&9}#i0S38$~kiA}OEx*w^tfq#{CQ&u&{Lsg=8FpF#^>;|{*=-<M
P)`0#Fdww;bA?!LM$7VLF~RpaK;QJcTxb|TpbI88RuaLj%}+7;uljudOEXp#*DPoM2RMpKBeJJ%vQH*d46Lx;3=c6tH|Ija%|^|7
$2jCoL;ar5?LZ<l*)Iofo$*^jnjhh|6DBQR`xDxB_zL*3+=QY2kM81GoYutEG=aulG@7o&WPVPsP3y{HvJ!#lHtk3)9;)3pg1PK3
4(>k9J~)lUn^9WM)BSw%0YURU)uo7TS|u3OGted1JHeE)ni13%Fucm-&8)q3F}86b9*|2=!PT}Lef|N{3E1fgNLA@lzQc`Fl#D)y
5~FSFl5JBTv@yZd2gdTjLL5-F`kh;`V4xQJ!61Uo5P6p^sE@?z5cPA@V+H4FM;93efk_kS4&tUUz5-B?bPNm|Sb|0YYV62@hrk*v
k+c^$7k!YgCsw)nJm<>^j362j$F0YaGFu?sjk&Yfp|>G4>lA3~{P4;)29#{Y@wOkE&~S3b>EA-njyB{&R2f-pBrbWfdB;93<1?se
<q##H<V_HijPNN7py;~TjsA++h@9zU(CSXRY9;xwnWBv^^l<}zf953g7DAX)RM;_Qu0#8M3Qr=HKcvX-g_^?cpC51@_7({pNyUJ&
%9sG8-tutuC(qm}bA}@64}xRm#{$0LoYkRs;xGoN6QGuQ37kc{z^%%hia*@wL9nu$hB-J=$UYxnpd#+U3jftK$pi-b1y7qEPG3M*
$WazkiD(X=iarGTF$(c8k(C2*Wl|5!&mk!mi17QvPx&f<YuV5WHP_T35L|>ZXSUSbmd)#Rfc11l*HyX_%5ENPCgzgd=l1n$)9I*W
SqP!agW6;V<E!5C+=u`=Dvt(W9T-j!K$uc40ED!U)ltn+LC>ryM(tK}W+*T5<f}~U`NvlU9FlJ_a(md`WS%9VO-#zeKb1Z_rj5WI
XAtnZV94Xo&$r|I(8@)mU&7R5rEZr1!jiu~dbeYhanm4O2jK3g_iWqjp<^2=K+q}+2J-0)JkTF5RSkEbU}KNx4{T2Az&1gq(Q;|<
cOT4I1P>t++ESl+L-LKxNdU&g0@ij(Ov3cqc~RTtv*hj@(bQ0+_N2LWvuQjDlkMq=6qAjW33DaQ%bGTkml_;NM{YN7LSLQB@DE8x
Tma!Fs`B+PFp>xkGThM)4Xpa`emw5F&Z4EeZfned?p$p%H_8g?XP&@9nJB#{T5r2>F_GZu<BEUBB#K+i?jUR?8zvuzw_rJwX}X9S
d3@cDWFgE+<)xOUW<ud*li<!1e=4B<)w}JU4V$>ezLe6~k}RH#;6X80Pl5NYxWsh!AuTVs0j35r1E!GCv`q9d`e#Rbdk8gkyL2%X
&*L`lk_tNsbe+xRSBJ+&Zv|CI_ofP(gA5mIlO(07$j3wjBf?y9!r!*+Fw%<1tke@5rib)N)O1KX_*>@?9d@xNbvxQ>j*1G6lXc7a
f-!M9U`c~6Cfu;$z^CEta7PIWJKQOXxg^{l64IwWM_s1HnUdd!8xt?!soXTX1;z5SSVks3FjgY!F&^u>YzyB<o&GSTkq;Wvp11Wb
UM+$%d%ilpa2heEfPs70LPQ<X0yl5}B3fOn3wvN>-m8rWmn>%cdX()xPrIcfBg~h@FgZ6xVz9&>5Zi$YdRdGuE(ST)mic@>V#CkB
D~A_4`NTPD1sGlM8^3yC?@E=eQ+Z#CCh+cH{E5MveaScwIXb@!t;+1}v`!$z<5!1Z%CJ6?Yz3yg4Fqt|#nKYzwUhjo936IJL;KYg
D_{e;^u7m@u!&x-H6k@?xu0;r<F#*n<Rrg<t{Kb24E>xf_FHI6<o%(>!_EoDp84h{iR>17`SPDMx0BN!XKzguDjSPG8tNO{2omBg
`z<>qC%$_(ARPLdcq~Xr!H!Atn?$4=r}e0+YG6Z__DK8<tMFleNbXi3f^wibdynrGnqI7wo+<^Q+=jxcXAhm{<=u2-d8$h(eFT0U
Q*2$5-3Uw{O_XNosI0a#p)=94kg%tS*A&=@5$KdCX~0C$0mAU3&Cpf1qB(NF_f{Zpu3>zo^!rhvq|f#`?K56OeVVAGOw|IL6uO=C
WQ;$Of#n9GZO`<_xYDT1Y8o`LRHUOo@+$VN;BXVCE49ZXYDP^NycMzeWDRW~<*l2plBwvzw9O}GCHxMW1Q3wm&5iqb35K6xis{z&
=kjGkQbV)>OHA}@vF&A>pvKCWoP*u;@Svr!E%M}vopz|P((<@uUJs3y^ezCvhV>os8hkZ6_`hZ2C}*$Hkentt!|pa^u3r%2y5uu3
rTO|Wn@h@8_XGQpR7I+*1Dz*e2QY1uOnLhSe+Cw~3<{jcX8p$%-8LwEuI&YV`09g?)wA;TU)}u_coKsjVk%403+ae-kXo}&5fOjJ
<sV`3O3+AkyZ!&5J%x>O*Jl~fXD_%@>`<8#IYe*Yik|GB@}WU%!w@6gumvS_H6AZZj=XZMnJakeRn?&Zn!&9)7Vqvg<S#Q?Z~+h|
Jnx}7h;;oDUhdl1KE!D*@Xv096q7%2tmsK~mhXLDaR(_=I|-#@@tx*IOP%P)esGd|Cwmksi`B9KiAy&}dlk+FW?CV)cC`65WWKcF
94*)9OZFb(8UJ*{x-|o1B<CN%?qTA~v(XA+xjDs`w5J}_jVoT<69#N08v=ayr(qS0ah<b+XUzyr8EMnqH$P%qd}>|d5c{_@Z7N_a
cHJNeFsLP7!Li=7fHDMHz?CQ$3zidRzs5pg*av8`H}5%e2O;qRFNE8j1ljJiMwu%ryG+EpGytfbClSsI+>k}Djo7<A4@T$fwvBD|
1%i`A1v$NWPNZMa8A_Yuh8UtZBy}dfZxQ=dO;p%@#i8j5kOVM7$}i<<N0iKaG~YcP2U2DZ)M&GUsK<6KM%`NOx2*xJGA?)TTSN=I
z;c+s(Wnkf&fq!ClG~qI3?)e20WfZL@FQ-J7u~|>bhe>CmFQJBUT|%~G|Ju}kjmd4e;&T2Mj%j6nKX=a76eHG%jUey+eiOK$Hs3V
5=d3lUm&=R9u@C&%$b@LR{}>^25dcS8pWYc>EOEbyh!FG5_XvCqJpphz3T!#MU;@cG0dS(QDx+6Q@qg=>0Kp@`Y}eS3dwF!8^xJv
I%T$fBG|sHa2w{RAAlfK%N$f~K!_GvObcc^;5x9_G&^2h$mqNQ&TnV+Pc>o}jxJ7`*QoLS<}T53{@{1|E|}G1JE^Z8CEdq_mBf&M
SVEv~qYlWlH$YnK1~7rEA!CBLvgmJNwn+XnKJz;As3Z2wy0e9(^$O_lex?Qe?F+Y*^0Lb|o;hjpJc=r3t%dlLiahW4Rd!;%q4b#y
-cN*bQ)9@>xWPaAVtz2=fwsA_Lv}C&V#GoUL5oX(8B+0iTo7$ny+dbao9=6f!=|>uv-^SjSa-eq2UAX~Zgf{Y=!1N^&xS6@bXr|u
f7^8mB-$~~3lzreTN}Rlu<4IqX9~qJ<Yk}>kUm8PBzoK9$%*sAdJBPf5ia4UKNvSV3ZQpTaKPN-Ykfs)jXLnjE3Y9Y9w=flv|?NK
`H;vwZkpZ^sFG#AzEq<IJ7ZFASiy-n!>1o~*bV3@;!dl$8>?7C&p)0&S0joD9o;Y5XG7`;1$F;_Ev7Z}Q@i)O3ldRSuADYDVZneE
i*AY5nUwt3uqTASkaAo8P>tv`#8DV;_abqSg7oV8mh#G=Ba19Ny+_ZJAOMUORGQT5p!l$VlU31UI5@I58s_-TAq>5BzUuyt$9aOi
8j-T6J<ZVV6uTsN^Zg;-)kx;z91OMFcx%feio1M_r9KQIt`?t^IVwdtOqOI9U@B27?*ScJ+1;%r>UaJR7?Z<ESOwUh245xIBR2|!
J&w~0_)A8PbNvTdj;KD7S|0+D<|->kW=d<6^kpFg*7ah|LMNSa%A@eiNiFj}%@x))abUvx19j|craBMd!4-3s_-H-jZs9cfKI<KY
CPx@{khDO{?We+8sYbtIPtx1@Q@4C48)vE$TCc@?do%`JUMGho$7w%gAj$zmbswoC)oCn|E#%jW?Ph*D9guy;p^P#PB4mZwbe%CS
mcdA)4xCl|DI=;0L9OW`x?KND`z{PwE(*8TVH(jjb-5t6xMuy!&>e1SX=3M&&R_E8J8C{kKVnN%=ru>6Mw{oq<YWe{eA51{nL{o;
hb7z^)Hos*zePj+C{~?1n{g@|OaAqXmv_^Pzaz+~XyU>D&4ERFi#=V1L_WY(4a!l%fi*of)b*FDtp}X`Jn8;kIN>hi@JR8fvIU)s
I;1%w63_D4@{SzWK#f^yf1zY?#X0>xh_OIbROzu74oeV~W^+cX@5_Qznp+Qk1sALJzJLaO4a|MnOVO7~l9Ie#TVq>N2WmlgDp($y
@%jdaI=x<|v4S?TK2Kf5I=^+;c5E7(m+iKpGBX9IAXZOfRQHVAea`cen&?&&YrpfC5Ztv5{mLa};K*o2D<~IO_ep_Co?`0O%5-fQ
Qf?aE2QI1ynoXeD(due?DhLSm>6MS6eWP6s;zbF(;oJ{;e1kH7aT86Yg$;$posB$Y-@7;K&$!57YS${b92aav{&f*zz+8|5SQ4kH
5fxQ3)@#Sj6PRZmORj{pPS~lVYK%8S7=o0(KNN1^8eDUGtx48};HYtt+Q&Q>cEaen!R0h{gm%MJ8Fh-@7p(Onp$vUd?srn-;wKg5
=o*rZ99EYi{~NOkB8B7Cd>#;Csa=)p(6F(J($BOki@Pa#J|>?9%AHTAR_KX<Y{OV~F<5(b3ED-uVwyi^^rDv>+Z3Q2yla%ch5h;L
>Fb520y8xSgqg^5_<~*Fa2_z#+t`TGM@DUB+>tg$7IHS=D?b|u`oqZso7XANwnxzJ_!{!u{k>@P)0Jf+EB4xvdWiedl6KW_Q=})r
jVGVcu!TLYgVL^k5GBVD-Cjm2+qB)5hoRyf`&=i?c4+wCG)7_r%43E_ucIO+M+r*ZAWdn|frEoo!d~d_hr3ZIU+Y5^oQgZRdd7bw
$TZX^etv~!AbW6@=)&u14E133B7BLcg~@})AAbP%#L*Zu<n^;3KxwmL0QOcD<&_x)t*Z31h+1^ZeW}`nN~Xk%6|va6-RU!0>9ihH
!+U>hsQl@(U(&lPMYg{Wn6Piw3bp+EgU%IH*v}>;^sU+A^<Mb5)CeDd_XTasGyGMMp+Sv;j~edQ>XnFo|02O#2%|A1G5i>2vqC*h
74K{{4$ag3$mrkhbe94npcvKWnB;NshM!2cGCb6%>EtJkgD<h8$Rg6}q9HyhX`8*gpFu5fDN;5b2t%)68l<9=Edu%Aco;y|@mPdS
!}kDxzhYX{(_MO2C<aN^qk7yPsqgJ;kCxaI`PRsD_3Lc*4dwjm8nH}oK#Czm4WV!k6w+HF0-10xi>wz4lCn9k<jg;`UIAzr3%m(u
l%72gEH!Np6bttB8N(qu#z?Q@lT%cA%1T{!Obw?Ph_>_~(LV&x7rxPNg*!;GmYk;rI8rn_A9%s9+#%@))K?|k3vbDGk$qa5ycgsT
FGom1C6wwK2hy(;UREM%9a>2^hw#8)3T63vpJ#$iX_+HLd!*QNs;Z(9BlgI@pXL?-r$=P%v?w$1l2f^}g<c?JI^aPvtCbA!g}3jp
fEmI0WH$ye_m4g(35U4wt{yacfW(viU4&xeEa*HmAIkYIn0njWiW&K`V}oIeK|M__Lh<dBSE7LCAOsO=lxKccMp1CJ16=~Qwt!Kv
hZ|?{RT|85d8vu!Ulk!|=@&GTj0jp6un@W;e$F)%D)BOq(fGv=UZkSu4<k+z7d?tLihw9!#m``{j?>1r!`VUWKar6$7VRPKd|R6e
N07|1S2It?8xfs}`ByBSpoHF=4(6s|@x#Y75_R4H3;;XPBNRPdGwFnbSy1ctNInAnp9F4$5fECdz_oGA#@EXx2X00ss6lWW*}`j2
K<U`V0F}KHG4uSgKjo9I^`QOfwPe!n3l*sH{+WQU9q<pV+}^^xu?@(-{FB=hHIUjP{p<IsQeeXYG8ATg&BCo_lZ%m#m6)vGo{kpv
LP282kj#`SQOn|O2)QI|&x&Z;Eke-%UYzpjckujWLJi>=_!$Yp1nc0znji!y;4|L1V5SwX2FnYEW+`WlD9-=E=5Z^cW|>QGYwQQ9
aTd(G)UeZ@Z8<VHo4T+BV=DHF>EIY_jLK0I|4?gT`?@Jt`C}h^CN(}(;O=MW1#czmYT_LD28=JKX3NV&h59|d&wkA0=nsc(3ZHmG
KEwYdf;xkO^rr$r*m*glRIlN@lSfaG8MC68QinY#&%vXi9Nn^Yg<CN2IQZ9_j=8@4GR>z;LI#Ax_40<6j)V8qeh73;pgN(V(*G=<
NUCYZgYjcv$D@u^C0@h4;R*7FwL@<ejY@f)<BY6cQZ1N^{|xU0E5y*)n*G)wtS16)q2zWKhzwvr0xri^hQ#-fH6Z}lHRGmy7$0Mv
%HNf=Bwq0&_J<sqLiRsWeH5}kpf{$5@E$*lZA+3_7s}q7MDlfu)X8k<Opg}glOY?bEuQ?kh3B7tI`#8QpH8di0iMpOl?k!Mw<s(&
M&k-OUQ*ysWfqZ7*q`>+gjdueg||*tyPz#&NFt4WK)iyv;l{V;>JBOcH-oAOT%P7`hTKk4wm}I&3gsRSb+h1%ntbK(?maLz8-R47
6!Wk#BIqzCA6tYe;GtilA#Gyw^ncy@x>*B9&UWNF(U^Fe0Bp-7g|}J33r3ICo|PjT_=>!_21_#=OK;JTS9NGcKGet`-SO?EfU}vE
*z9>extKP=GhBO}afy{AxSi%SXIOL&`KRXdprL1;oYjL0vNqnq-a*jJ`p%H4ZzmL%tP69@?H%5!{IeN>(0x_be-Us7h1d(>#OXHH
SN$)FaP-3PeB5#%{iK88K4j|rGjBwvyoLOewCKCSfd%)MG>Pu&Pj7^#HNz3W(*ToT_}Exyi)DpU)pzUWkeyx7NqinEqV<?L1$)_^
f~NUAq8{YRc?5|fCG&MXuCV)cc)dg^4px7(Icrgb$vrq-!kNu<sYU2bK=&8&vDrgE_GGwY<RZ}ywad#n4)?Z_`Dr?L%6y#N0U3g%
4{+7Sexo`8zv;41f3}Nfs67o6t%-L`muaKP^bxSD7Uz4Oca|xW;SSfBTsZz%p+?4(Ryqr;peR22Q@@PMGy0x(LX&WiZ1TyYXJy}6
-(DCvTgXTCXiEe4&z;Ukl%Z~m^6@CS5)rlGCY%iCi~z6O7{E(p>bFK8HE?RKEKwrlFBYBP3pgtLxgYk09$-4BJ?!=m`-@r^bS}5x
_A&R?!!hZ&A{5giHN%@ihg&`Xo(dlvVu!}~ojZwc+vn3Tjc1+wOn4t54sarh3-^QZ+Sy3)%I!FQ9?r1Rs9gT8xI&rwN9<)1oBvXI
4p0zDW=0hXl41rx%JYy7%Z-Lt2^}<jdn-EfKwK~k(%kMBtPb8w{gGh!fuht$l2GLGp><+!^mhwGlT6t3jfeV6!qX2SMtcxz9Xew~
S{kLmPQ04)=pKI|X<;fF3znY~^r|axRc*&4qO0P>ZhCJODWnHuqwUfnZsELXNqPw%_Z;HmRH8IJ2Vx7Iv6FG8HuuJ)6A0%JiYS)%
O9-cZ+1LzidlkPswyQXrWl1R83z=^yDb~)b1imZY0w71|uyxh1-SR-(`Pkv{(eaZ|XNlXpXkY)h5cZhH*dZ_}I{gbJ_4AD<IMCfu
dczk`RCn2L6F^9oR7U$~M2FU<FrB3R)XrP-c(6Dv92u@oCsuy`b)mX?{q~KRqUcRJ^5Oa%w3)%)$x(lm4cg~4J<58&dG{cqWsy;G
MNud!`$|n6G-sndv_=G7F(PFkuKlQKh=u(NT~1a2LgHoQnO<Q-+*k93$x85!Gfg_!*;fz_`VCkNh!{X=HfO;%xrlD3C3tc{Pki=j
4%RC^B-+qt;UyNSjTRS%l1D`!IUGCHg>{@itE{YaX(pA>d#!2<dIX5LS<fZxm?g=LL3J>B$c!}I_5>sx9WEYr@KvI?=17U4@$IUD
VQ@BEf9+|974-PCo8bu)bgT)_<%K0}UwabEh{tJ2Q5gJ73+fR*OSe>=K;M8l7v7Z|JK7J6VP_zOQYSbW$0(AA3=G5wvS3F+_Qs)V
{3uEN7A0rIerqZ0dXCgQjrp|?Ok5X^uk!VL;F#(M9-b0TrX)Q9zo40s;;sJ!R8C^!DP3tRf|^}~B{Nh5YB=ihhRC%V2!{JxgZ9+V
@lBo|!%&t6A7!ci8a7q@cnGeFCf8+CL!<dT-zU-+^57InWkCy=0xEv}J%SV6SXJZogk{PCrurs_+b~<%vYkOWYw$+*NkqqCgk1OX
ShZrUBARty!3{w+Cj0zgJ-NTQRbp`W6)RL(p?n5gUt)#mv}~QEiRCltk}Lh&ZTf~re>UGzwzVDB(5v#Rgm2clb*iU5dVx}=Kfsc^
qRriJt0Sh?Z0pq$p{rmY%ANQhDLp7u<S1(^IA-x?phxTexBH>W7%A@Vdc5*TW9L~vr#{n^VJN94XFG-cnxdS%Ah4XEn)WkAf+v3s
$dHrmN_h{j`2#cnTJsc7J#!03%6&C&UND#A(SY--g%VWvJ{W9=ABK-H1MeKj4oAYCrCqQ#s_H`jAQk_>?dwYp8}<*64-^_WfYO9i
-?o;9G_*CnjoygQ1i<8p8m4q&I|M6zxpMuo63h;4wmS+L^x)CG&nFpZ{T#Qq-rh2Xlw7Mk3HF1YkZ?jKRXUgAuD^z=G1h~?bHu~l
a$8&xlu>$d|BJY<lu)4UiPDe_t61+ZQ@eR8vA*L_mpT~$h5|xG=$kZk)7<Qbuh82>(WJGXDX+!Ue(hu1p)0F2jbO&kb2_lI%O9Wv
Te?`lm}&vnlW8$0j>+?sj8%HuJHOAn9}bb{SqzHeLr0=Yy<i>N0RvLE^`jWQ&Gmi=DzU=rFcB~!z&<3wfS+A%_!!lLMA@7Y2P4VB
OAZmwYx}b#N&9$+ZxOJ9B|RS+NhTd}{r%;%M(neZ$Vp0VX{%^I0;W*_EVk)ee??wQa{oxxI>kAoHS(Vj&J*Ejj;`la{|I8|9}IL8
hz48b#5sepXgdC4m24lHawX2^g4SQ`e=}@l!TNBLN*Ml?_kL9zp4E0OMh!h)!oXB$aMGLN{FkDr<wG!N3|;L;C`~-}E+f#H!ISH_
y`TKW<RBdH5rQ5oRMVj4CZ+uMeV;DC2u3x0FS2`4(TH6!Kzh1AO2E11b@zk~$i7||OK`dRs!h-WT%f*+G(V(Prm)A1%b?Ma^S;b%
4|Y1ECKFvKSp~T5ZDcVQgSw_IyZi(f5`)$a&d%dV_Tk*MD8F9#2D+1`>3nIQ`Eo2aql%%i+RcCU;+KOu$a80lJjooJu(M@d2mDDp
z-5MOi|Jow<-5#kn!y!o-G%IrJd`v)h1M^IuA~rvj!S3uieJqT$9n_DaB_ZBS%Trj`FfA?OeJq^jEij+t-D>!=F;s(1)S!;Uwy0Y
|9*rS8~ElFXnqPv!Gi5WUkVxfO4mcqe?>_NDD*##aKyN!><4p#u!_On%omd6;R@hpL)I<6lqn^yk37hNZOyz4p2~0W>~(SDe+Onk
CImF}Ebi2UhP)!#n8>b!`?92b<~J@XxGtK6#X;A1xC@*XTY0qst>xn3kV5fNdry|Zym#9$TpkM0E_YuDN~a|}t}ZOQ1yfRYUq@z{
z#V+g`vgJ0@V;1C@~ZV0&uuYoHHx08uV~N54d>Z_5^`|H22M_!#tvn1wR+64mQU38Ack6Vsy0G0QoYu=hCQA7#C)W9{DLn1mP#Ne
ncgcO*lQy)M(a&RfSFrP_McEwEeuLY2Wn}5Oht>?FK2<mmyAtPMxg%v-P?DI#;LCWQx-g~aDf^QG_kdGM}kM1UWs)LNd}`JXH&zb
+X^R#<;ok(OvMgd`2s?6L)o>5+mZZnBc80rGtJ4LIj>q}f;Y!9RIb@yqQOimAU?PivjmP5I)bSOG9MfP?rae3QQ>M(yBm-sF}&fx
wLd|SJ7aEdowviSAob*!j~=jaw|WFoqx<U{!sUsUoMB?zDVWRh#_SStpQNOvZ2#g|IZx-O;%zW2fYD%LI7O}`5rX3YY$7Vx$D44@
qWgtqfYYgiJQ2>Dgd?jr8-vbs&55w*V3ZuO!o>a;C$pIH`q)4&A2z=Pe?(6cz1i*L#x1u`GMF~IgYBT%T>L6L#&cRod^{})zx&}M
r(ETqZ$@F-2-Aaf257Txq}^QQvJ_5hPY%C?%=bHBl*e&$EEaG+^9=I3#x=l+6j<L8^=uAPDy>H`kvnI;tKAvIA^)ksJ{Ye;#T!AV
>Ru8<DlGT*4((TI_gyKU-NwBg3`9-^VL-98i;(naPyXUQ63lofcq=0fLcy>&8+k8RJ;cMOUUni3fv(2mHZZ7`TG@+2>sIiB445W~
)JB@95p-M_)#W&7-k&q@04`}z;6p=oQ$BA$14q8i5b-C`Llx34|EO=+tRGErvGHbnkZ}tM#Nk+LByV%b3!IJ6YL{$g`%DeAf<)Vc
{gv(ILI${OKU6a4w2sPQqB7go9JIOjAKl%=R!^pxgB2&lqK5eGN5qR@g1}$q>uHghNvl!n8@&Eur%Of$bV&4`?FF6JDmtW{O=f**
Qhi{Q#qIQ%QMYv~y;4cA)9l77`QKw7AVXU;qRq)#>q(Di0V`9!DGxMbB*ACHu#&J&{|e~H{@NWhVJB+J?I~I8j=QSe1i7`D0asso
<rO<;BE`FihEM0J*3J{Y{Zy@BTf2Z9{^8<XBqmI*R-r&0EGgu}$X~-W-?^r*W|!{jlHX!nUu|nkQ|TF_(2=qHnXaXcx-qF$He1Pq
StzF0xY^goiIwIfn8;uDN4^Epq~&*y@OM!P;U*YBv>$rvc7|>iV8-4&jqKrr6-;tpb+S)&7!lHys%bpyR;kFw?dAuoHu-+JV-ZqO
b3VTqAXpYQM6`Wg{_ZUrAW}xMXlrOtbm1{92D~wV(3nw7kS%Ze`mAKax6|(a(3Zx37P15q!qZA^XWx_};|9qlEX_|7AqrM&K0F;G
H1d+c5>sNBdGqn`OtH-@2%UXpbBWDSLcz{y^WLiH9BQr@gv8-B#i&w&1qzdof&EZJ!5oKRcdLvD_56F*fz3{yQY#<H*B5L2cbpU9
Mb%zqk&z5Sewo}8%Z_%e7-XYOjqK|BO)KNW6k5slHso$Fr0!-{iCnVlCjtwoACQgb=5*gdfq!nQiN^=zL77py!*)@oF9<B}vx<kh
EMF!qMzB!%o+zT{WZGw`;Q>1+rCjhI1lEKs3aYxs!q}5-W~Zd!Y|XBJqsuF=fufoe9@eG|<s7C4JXodK6g6sXnMrVTw89yKO^lHO
AU2tU|HnhzJLp2c>AdHh&2X%V^zTMyw<dJyXtRv+FNWx%&1`J0klvSV@kbhu&wR+qCcot0Vc_@Z#c@LZ_c3E38W~p$0TBY}U>j<9
48cKBz~uRwr8%l=t(`u-6=!m8CK2x5`3^q;IIy~*(#38y%M+^tHJhx+f$0m~)1MvBxeFIIv-#4C!gMYHSMnG@kR+svHiq_mg9dVL
mi)(7X2W#fVu6KCp3Sw3GWBI!G%D?q)M@a0)sztR+(pksWKqzVhr3m}1@M~d)o(Nov2oA?W<ACm3--eECIplJz3B*l7Y;aRqn4<=
6*WNFa>jftMM-R=o_lmUF@l;mJnhEq{qdxq)+dhUzT`2Hy%7xl3OECn2u?t^e1rG~{Q;Eyt;I4b8fdrq@tX#lbCTlu9+RvBaF)^d
Kr@tbgnKRiEwP-4M~bnqqR4DiWSS=quA6@(AwG60`?YrGz%@l!>A;-u8g8O4w1|GX2dL&yJbvs-<;)p@89wur4#ydyZ=S>Cf4yWi
`d^Q#t2CJ&%lbW9?;y9MdsFruV%S+5<J8}Akw-a`^B@Oey0IWDn<2e3OZ&?^Mf#^~*-g3i4O!(C^t%XW1}y5(KrX&;iPKYJyxowG
r*-|r1N9QA=DuRM6dMnf<2<C5EJm`TS;&}qZ!4w%lC2SWrf-dkTrInh|EgMehsil5nD@#zOLg##xr!!_gFlC-$wFZrD_zq+Pgyuj
8&q^vX<rfbS-v>5Q;~5PU>d&d@GcQcn8aI^HiK&?%tBD$!0eFK25k=@{}k2;78X^9QOfb~hSw&g2ylLb84V@nozr=VMA7r>8~Ae8
zdRa;D<lt^8f^w<;jRYdH;i0G9n*2m9V8#;cz@+7iHnXkZADv$l4-as-O^H4?LE(&my;CIVJW?6&1l3%*N+gusX?qy!-@|J$VN;Q
1m^Q`4&)ld^?df{;n42%W@d+8xnEVe{TLa+E*e@uYQ(PEl5gh~Ik(QEw)>&__^k~Ti+w5v=8#ZWK_nvbA@4G7UBzflf4`w642Mcb
B9>uF@VFSB@yC0M9Y)VzM`R@|rNd`0SoPZ#<aG91&;+OlWoo76GXjc42|-MzzT(PPgTdXe=5F@$uuw$V{1ZJBd~LDx5vNU^8n@+K
c+VYsOYUA-E<}NG)+)<jDVA?LP^l})KC(mo&*J+H$Zcu%9vHf1mgl(U(AxWk;OD|GLCIbZ79y|kMAH!MMiGAK@R_4G6p7)u_rGOg
8qR~tT&`4PI=iTwO2e)yaushs5cMnnuB(qceIaVZ7{Q|-h?m5_eWe_O_B}$t2eACvWKq~v{*BrDG3tPGUL2dquvF3nM2|BW{j`pL
9%v7Vi&}T<%ztAMtdff;r#d2Y``r;@VDmI1ywi7-w!|TZt<T@{3>t0AuodDM7J#lEx?&gM3Ddx6PiY?6O~!;*^=M||S%aPpV9m04
*=uwrq6cyfPbLVu`pJj_eUYn(Ig90<!@Z1;l!ZO3COWI^F&BaihBu0(oA8BB==+{ndE&~WUtX~o*hxTWb-9-9c(su<_MG54m<-78
#`(%#1Rg578U}%ei1078og&#buTyc*B%~+2@>+Lb=P)IUN<}lY7~Xd~C2ftI7czH8m71jwyYRgv8NJX5CPMqxnI#_P`^SU1HgNt4
#bsfkK=e5eTzW_W;W~{{iBSDc!d@_491Fo1lL3XplX|J|+K^_L6Fv0>py7SrE<dvrPCydfUP>8~e2)k`8{S0EvYO3-gBzeIE!!}~
DEI<x0+j{&kXl2hhmRF7j{J<KNc$eGX@RH%>VHgo1xNnz*4ZpUd}R#VxTda0l@Ps-C9ZU}Rts<?Ev*pIpL)(O<@&M@=2}85<G|bx
lHp9y<_X=DEnKFUhV<Y;M?!0SUuB}vTlZWjfX%8{<Q`)g*ysz0nmOI;Xg1YseS-WVVHBlt_xYFT<Mniq&#R(x2p}M%$;y=C5n%p7
t3HwObd`;d_j?4z@R*r;{A<fFnU`HbMgX+A`t<zFM`eR-B>a}1I_4;RLy)1D)+KHxhzo@lz&t}~0%*@1Jwum&NHjLRDCJ`OS<e1E
Z_%dbutqGo$)Ygd-aH1gZd@g>RuggYzUu_7p|;h}i~!=PJ}G%c0#V-2jKN579FI<)!e~ku+%Ro^yY$SNS<TEtm`@S}LX!!k@q*bU
)!pF@{r4k*FA1$>F}5h~Wk}>OMdwd7G(rbrskUy9afy6>Rj#VY3yU<-O;#r@_eTb90&x1%U>vHcJ+YaYeOJ8mWGR46nQ)&7dyEo2
4&FZuTEE#l`=83uXG;v9o?4&CmK(v5(3lK<4@IcC@9UH8GUS&jFan*AIF&HZi1=-shjIblaA<iA`UeKAMjB7q#sgPY4OU2it6AzT
C=(p{k3BZtrRw&P(0g5zq(w9X(C80!c%}nacbVe;rJ{a5;HoB}_ZzF-dOzX^vSa||h9VBXaxBT?S7<y*hos4o7?Ckex_He{@S-in
@)pDKvMQ!!ICn0NyFY?$60|RNY(y0Xud0@k?O?aAllQ&i@qc~b(;RsppSsdLS5AitaMqreP7a_At*B@Ijaqg$@@m9GvEn`hY`*S0
1yL_$<n~XCX1dmJ?NWtf%SU>QT!PPKoDVRQEu>sKVFbYcp*<(mB-T2qcRZrWUs=_>%A)FA59dA9bZB}KJi*cbT;rT<2h}X^OvvK%
AiN}-?Kkz`9@~y8JL6#xQ>9cjKh*=;uB{LHZtg3SBBs_44dbQ>#2?<`k6ld<x1tgz<5_jlK2p3B29;ESK~_)_+DJMbAit#j9gI+%
?;%+(mE+8@C){nr`4*Yn(z%G|j`@3Xj)od11T?UOdh}U(xLrB(KSJENQQvs8P3OX}50%2F8R((cr7>F=@O<An>76lzAeA8y2*AHX
t!_8h_`{*J2IiBqCnr9qE!lb6W|sy$eEih1S39RSB>EiL$YItYzCf1RC*!4+e=~=-5x;UI$uLT3WU@a100000@o}t5+bT~$00GXF
0o<qr0CTO8vBYQl0ssI200dcD
"""
raw=lzma.decompress(base64.b85decode(''.join(PAYLOAD.split())))
assert len(raw)==70748
assert hashlib.sha256(raw).hexdigest()=='755ccaea554f57bcc1eac4511974b91f8a595b36d964f89027f22453ed8520cb'
out=Path(sys.argv[1] if len(sys.argv)>1 else 'CH95_REPLAY');out.mkdir(parents=True,exist_ok=True)
files=json.loads(raw)
assert len(files)==16
for name,text in files.items():
 p=out/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(text.encode())
subprocess.run([sys.executable,'-B','-S',str(out/'REPLAY95.py')],check=True)
print('CH95_INLINE_RECOVERY_PASS',len(files),len(raw))
```
