# figure-0576

AI research report · 2026-09-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Quiet Willow 49 — finite basin cancellation, protected low-face clearance, and exact nonwinners

Branch: `[internal-source-reference]`. Transaction: `470280e18440c779de0776cd`.

## Outcome

**No own110 endpoint was obtained.** I obtained five new exactly audited rational bodies. The substantial results are (i) a genuine finite enlargement of the clearance behind the unchanged low stable triangle while retaining own121, and (ii) subsequent actual cancellation of the entire unwanted primal basin, followed by reduction of the stable count from nine to two. **S1 was retained in the clearance construction, lost during P cancellation, and not restored afterward.** The final bodies are own211, not110.

| Exact body | V / E / F | Strict S,U,H | Additional weak | Complete positive P depths | Complete positive Q depths |
|---|---:|---:|---:|---|---|
| `QW49_LOW_PATCH_A_G12G18` | 48 / 138 / 92 | 1,2,1 | 0,0,0 | 0.44466831855758365 | None |
| `QW49_THICK_LOW_S_G12G18` | 48 / 138 / 92 | 1,2,1 | 0,0,0 | 0.4442524004820082 | None |
| `QW49_P_CANCEL_S9_G12G18` | 40 / 114 / 76 | 9,1,8 | 0,0,0 | None | Eight depths listed below |
| `QW49_REPAIRED_S2_G12G18` | 40 / 114 / 76 | 2,1,1 | 0,0,0 | None | 0.7925533393030378 |
| `QW49_QBAR_A_G12` | 40 / 114 / 76 | 2,1,1 | 0,0,0 | None | 0.7476531649194527 |

Every entry uses the actual uniform-volume centroid of the rebuilt convex hull. These are true maximal-facet/edge counts, not counts of arbitrary triangulations. All maximal facets in these five bodies are triangles. The three 40-vertex bodies still have 48 material input rows: exactly rows `3,4,6,8,9,19,23,30` are nonextreme. Thus their C is 228 and their remaining edge allowance is 135. No primitivezero000 claim is made.

The full eight positive Q depths of `QW49_P_CANCEL_S9_G12G18`, in descending order, are:

```text
0.7741010277913559
0.007316604080306021
0.0018711778432488212
0.0013039703602311236
0.001099321293932375
0.00029084481723929475
0.0002585999532557202
0.0000068492411045874136
```

These and the table entries are the entire positive-bar lists, displayed approximately. Empty lists are exact: the rational auditor has no positive-depth cutoff. Its regenerated reports contain every exact rational birth level, death level, depth, root, and death edge. The complete recovery code below regenerates those reports with the asserted hashes.

## Input authority and reading

I read all six supplied files completely, including the entire 111,780-byte journal and its branch memory. I reconstructed the actual selected G8 → single lambda1/2 → double lambda1/4 → third-stellar parent. Its input was 2,985 bytes with SHA256 `32cba83de40271ce4bf02ba6ff22d38a839879b64da33c6637089e72876e757b`; its original 8,107-byte exact report reproduced SHA256 `6be7e0521fe41380bb2a19b7559de46c74c58edf764e78c35001a71de2ca702a`. The parent was indeed 48/138/92, own121/weak000, S{45,46,47}, U0/40, H21--30, P0.45529621853755375. Its complete stable triangle lies below the remaining death level, as specified in the supplied source.

I did not substitute dynamicG10 or the separate detached-B family. The raw G10 serialization issue is not a dependency here. The late literal G8 recovery supersedes the historical missing-coordinate warning; there was no missing exact dependency for this computation.

## 1. A finite geometric improvement with S1 retained

In `QW49_THICK_LOW_S_G12G18`, material rows 45,46,47 are **literally unchanged** from the supplied parent. The stable triangle is still oriented `[45,47,46]`. Let its unchanged outward normal be `n=(v47-v45) cross(v46-v45)`, and let `h=n.v45`.

The exact minimum over every other vertex of `(h-n.v)/||n||1` is now:

```text
175206463868794233713688463650765230173
-------------------------------------------------
47555060285555149312145122586500000000000
```

That is 0.003684286442215135, attained at old elder 0. The parent's corresponding clearance was approximately 2.0156240030015595e-12. The ratio is approximately 1,827,863,945. This is a finite opening of the supporting geometry, not removal of a tiny facet by numerical tolerance. Old elder 0 and the other old vertices were allowed to move; holding 0 fixed in the first phase had left the tiny clearance unchanged.

At the new actual centroid, the squared radii of stable vertices `(45,47,46)` are approximately:

```text
0.5279151750047709, 0.24914333833996544, 0.3011463436811575
```

All are below the exact remaining P death, approximately 0.7375925797931231. Convexity of squared norm therefore certifies the whole stable triangle below the death level. U0/40 and H21--30 remain; this phase has **not** cancelled the basin.

This improvement is not unconditional robustness dominance. The exact sufficient fixed-surface S1 centre-cube radius decreased from the parent's 3.1617028314840814e-7 to 2.9237400944695552e-8. Clearance behind the particular protected triangle and the margins of every other nonstable facet are different quantities.

### Numerically useful facet-foot guards

For an outward oriented triangular facet `(a,b,c)`, with raw normal `n=(b-a) cross(c-a)` and current own centroid g, use the three cyclic signed distances:

`d_ab(g)=n.((b-a) cross(g-a))/(||n|| ||b-a||)`.

The orthogonal foot lies strictly inside the triangle exactly when all three distances are positive. One strictly negative distance excludes both strict and weak stability on that facet. This tests the foot directly instead of subtracting almost coincident polar vertices from the microscopic stellar construction.

For the exact centre certificate, put `m=n cross(b-a)`. Each unnormalized side value `m.(g-a)` is affine in a displaced reference centre. Retain all three positive inequalities on each stable facet and one strictly negative inequality on every other facet. Taking their exact distances to the corresponding hyperplanes, together with the support-interiority bounds, yields the reported open infinity cube. This certificate is for reference centres on that unchanged surface, not a license to move homogeneous mass arbitrarily.

## 2. What the whole-basin geometry revealed and what actually changed

Low-superlevel separation does not detach the entire positive-edge attraction region. In the original parent and both retained-S1 successors, the vertices having **no path to 0 along strictly positive radial edge scores** are exactly:

```text
8,9,12,13,14,16,17,20,22,23,24,25,26,27,28,29,30,
31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46
```

This 33-vertex set contains stable corners 45 and 46, although those corners lie below the finite P death. It is larger than the 21-vertex strict-superlevel component supplied in the assignment.

On `QW49_THICK_LOW_S_G12G18`, all 50 directed edges leaving this set have strictly negative exact radial scores. Their common open infinity-centre bound is:

```text
47106107663641802893577048508394358778124487770387643375804033684073359
---------------------------------------------------------------------------------
1695100910356524057639847240324855082550669599008654160000000000000000000
```

approximately 0.027789559533499486, limited by port 8→4. Old 0 remains strict U throughout a much larger unchanged-surface cube, with exact bound approximately 0.9608139037491455.

The exclusion is precise: on the unchanged hull inside the smaller open cube, a maximum-radius vertex of the 33-set is strict U, because its internal edge scores are negative and every outward score is negative; 0 supplies a distinct U. The same argument applies to a changed body only while the stated cut inequalities and a distinct outside U remain valid. It does not exclude changed boundary coordinates, new crossing edges, or unrestricted material replacement. The exact 50-edge certificate is regenerated, not inferred from a sampled graph.

The successful P cancellation genuinely left this geometry. In `QW49_P_CANCEL_S9_G12G18`, old 30 is nonextreme, the old saddle carrier 21--30 disappears, and the **new true edge 40--21** supplies a positive ascent. Material 40 survives as a true vertex, but it is no longer U. One exact positive-edge path is:

```text
40 → 21 → 18 → 15 → 11 → 10 → 7 → 5 → 1 → 0.
```

The first score is approximately 0.002105425125666378. Every one of the 39 nonroot true vertices has a certified positive outgoing true edge, and every vertex reaches 0. Thus the basin did not merely move to another label. The full exact P list is empty, and the direct root audit gives only U0.

Relative to the supplied parent, this endpoint loses 85 old maximal-facet vertex sets and acquires 69 new ones. Eight old material vertices become interior. Its volume ratio to the parent is approximately 1.2028169984924058; its recomputed centroid is approximately `(-0.24891691258262366,-0.28216365786068276,-0.23377517753583318)`. This is a changed filled body, not a relocated reference point.

However, it has nine stable facets. The protected triangle itself remains stable at that endpoint, but eight additional stable equilibria exist. The later repair reduces the stable count to two, leaving own211. In that repaired body the original protected triangle remains a maximal facet but is **nonstable**. The final Q-descent phase also releases its coordinates. S1 has not been recovered.

## 3. Complete equilibrium carriers

All labels below are original material labels, not compact hull indices.

For both retained-S1 bodies: S=`[45,47,46]`; U=`[0,40]`; H=`[21,30]`.

For `QW49_P_CANCEL_S9_G12G18`:

```text
S facets:
[0,12,1], [0,47,25], [2,26,24], [2,25,26], [5,46,47],
[20,33,35], [39,47,42], [42,47,45], [45,47,46]
U vertices: [0]
H edges:
[2,25], [2,24], [2,26], [46,47], [20,35], [39,47], [42,47], [45,47]
```

For both `QW49_REPAIRED_S2_G12G18` and `QW49_QBAR_A_G12`:

```text
S facets: [5,14,12], [25,47,38]
U vertices: [0]
H edge: [2,24]
```

Every weak S, weak U, and weak H list is empty in all five new reports. The exact input rows, maximal faces, edge incidences, mass and full persistence records are recovered below.

## 4. Executed methods, negative controls, and limitations

The protected primal continuation used a live Qhull nomination, actual filled-volume centroid, direct facet-foot guards, global non-U chord witnesses, and the largest finite P depth. Trial hulls were rebuilt and nonlinear constraint violations repaired before acceptance. Its first 51 accepted steps were 15+18+18; the latter two are the actually completed prefixes, not the 25 and 40 iterations originally requested before interruption. Their rational freeze is `LOW_PATCH_A`.

Starting from that **exact** A input, freeing all 45 old rows while keeping 45/46/47 fixed and increasing the required supporting clearance gave 20+16+12 further accepted steps, producing `THICK_LOW_S`. Tightened LP feasibility tolerances and a 1000 constraint scale are preserved in the actual source versions.

Releasing the nonstable-facet restrictions, while still keeping the old triangle stable and preserving the other primal witnesses, gave 28 accepted steps followed by 16 attempted iterations with two additional accepted steps. This produced `P_CANCEL_S9`. The numerical residual P value 1.1102230246251565e-16 was not rounded into a certificate: the subsequent rational audit independently found **no** positive P bar.

The stable-side repair retained numerical U1 and reduced a facet-foot violation objective: 32 iterations, 19 accepted, ending at `REPAIRED_S2`. Its small final loss, approximately 3.7394253427527534e-8, did **not** mean that the remaining Q basin was small; exact Q was 0.7925533393030378. Then 30 accepted class-first Q-depth steps produced `QBAR_A`, with exact Q 0.7476531649194527.

The latter comparison also has a cost. The sufficient fixed-surface same-S-census cube fell from approximately 6.199256599977636e-5 in `REPAIRED_S2` to 7.54373360960701e-9 in `QBAR_A`; these are S-census certificates, not U1 robustness bounds. The final selected primal forest has a smallest exact positive score of approximately 8.548651281948664e-11. Both own211 bodies should therefore be retained rather than treating the lower Q alone as dominance.

A separate 804-case finite scan tried radial contraction, translation toward 0, collapse toward 21, and ordered removal of the original 21-vertex high component, rebuilding the actual mass each time. None nominated U1. This is only that finite scan, not exclusion of those continuous families. An early unprotected high-only continuation lost rows 45 and 47 from the extreme set and moved the stable carrier; I rejected it as a low-carrier-preserving result. The complete producers for these bounded controls are included too.

There is no exact interval certificate for the entire floating optimization trajectory. The finite rational endpoint hulls, actual centroids, full strict/weak censuses, cut certificates, and ascent forests were exactly checked. The exact engine is the supplied `exact84.py`, reused with exhaustive rational hull reconstruction; the cold replay is not an independently implemented physics verifier.

## 5. Recovery and identity

Save the complete Python block below as `QW49_RECOVER.py`, then run:

```sh
python QW49_RECOVER.py QW49_RECOVERY
cd QW49_RECOVERY
python replay49.py
python verify_diagnostics49.py
```

Only the Python standard library is needed for these exact commands. The observed cold-recovery terminal markers were:

```text
QW49_SOURCE_CAPSULE_PASS 31 fd2d8001be16812a2941203a27a60dfc03a180a4d6f0e2896bf759d05d777b3f
QW49_FIVE_NEW_EXACT_BODIES_REPLAY_PASS_NO_110
QW49_CLEARANCE_CUT_AND_FULL_U1_FORESTS_EXACT_PASS
```

The decoded canonical file dictionary is 123,364 bytes, SHA256 `fd2d8001be16812a2941203a27a60dfc03a180a4d6f0e2896bf759d05d777b3f`. The 31-file capsule includes all literal rational inputs, the complete exact hull/mass/equilibrium/persistence routines, diagnostic generators, actual numerical source versions, rational-freeze sources, and `NUMERICAL_RECIPE49.sh` with the full completed-prefix recipe and all non-default parameters. Its per-file byte counts and hashes are checked by the decoder.

The numerical recipe uses the observed CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, Torch 2.10.0+cpu environment, float64, one Torch thread, `OPENBLAS_NUM_THREADS=1`, and `OMP_NUM_THREADS=1`. It runs in a separate directory. The whole floating recipe has not been re-executed as a cold bit-for-bit portability test; different solver behavior can produce a different nominee. Exact reconstruction of the five stated bodies does not execute an optimizer.

Expected output identities:

```text
QW49_LOW_PATCH_A_G12G18_INPUT.json
2982 bytes 47b4e99a7c02472898c0bd540910202a678d3a7952518a58897f86c7aeee46c8
QW49_LOW_PATCH_A_G12G18_EXACT.json
8275 bytes 337a0775168d131c43b35d2b1327f0859c703956648a3b6d698dd9c4d7c81fbf
QW49_THICK_LOW_S_G12G18_INPUT.json
2982 bytes 340d5ea455b997766d9817400d5fb8b93f106c5ad474f6cfdf69fa336d92bed0
QW49_THICK_LOW_S_G12G18_EXACT.json
8337 bytes e2b325a5000ba16fc57dfd563bc28c5f92ac6a50c1e9868385bc011b75d7d09f
QW49_P_CANCEL_S9_G12G18_INPUT.json
2984 bytes 0ad8d7f3bbbab1805ec48aff0f04e8e0a4bf33b519e1852f3156478330dde11c
QW49_P_CANCEL_S9_G12G18_EXACT.json
15188 bytes 9e6ad18ba4d7a78c2888fe6c9f51336c9ce9ebfa593d6176a8e583a9555246a6
QW49_REPAIRED_S2_G12G18_INPUT.json
2979 bytes 1820a2ca63e325a2fecd079d68abc57e97edf684f89bc27aafff26f990b8bcfd
QW49_REPAIRED_S2_G12G18_EXACT.json
7483 bytes 380660b3425535aecd95c3d410b0fde38ccb1faf8f7207dd1e8ccb39738eb94d
QW49_QBAR_A_G12_INPUT.json
2105 bytes 9f51bca707b7eb23ffd715b578dc715208bb1f120dfc75cb255814d632d152c2
QW49_QBAR_A_G12_EXACT.json
6271 bytes 6142372cd942dcd9397de19739ed47311a4b52388e84b635f83314eb2801e198
```

## 6. Continuation

`THICK_LOW_S` is the retained-S1 continuation point: the same low triangle now has macroscopic supporting clearance, but the 33-vertex negative cut still identifies a larger trapped region. Further work must change its boundary/crossing geometry, not assume the 21-vertex superlevel set is the whole basin. `REPAIRED_S2` and `QBAR_A` provide a distinct, actually P-cancelled route with 135 edges of reserve; the remaining task there is removal of the whole Q basin while retaining the actual U1 forest. The local stable-foot loss is demonstrably not an adequate substitute for that task. The higher-Q repaired body has substantially better same-S reference-centre margins and should not be discarded.

The branch remains scientifically open. These results establish real finite geometry changes and an exact P cancellation, not the requested simultaneous110 endpoint.

## Complete executable recovery capsule

```python
"""Decode the complete QW49 exact-input/source capsule. No downloads or packages."""
import base64,hashlib,json,lzma,sys
from pathlib import Path
DATA=r"""
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;o;+6KV1Mlh=oIeoyr591S(ZcUgn{R++EB`PcfD93<Gch^bVhzI#N;ZeJYO(@o7D&qbDm5
ZYxzDxmsd0c)se;=|;+?1Qsn#m=5|Z8Cxjpqp<2j^ptyGzCnA05wFZ>%xSO$uV5MUJ=8DWBJLwd1l#1Ih>`^z|CYiM@SKNna(tcd
5Rch_?S$49R>!#(>W2okE?~RpQmL_ILj0&u83h8I!SW@Qeln!0I}LHWJ><I&7c@C~6-VFuRVAz);~#j8w~b$D7}j{R)X|i0s~M9T
3W@kI_v*Rkzl1ovh<nL)gSn34N&MvB9w2nZB+R~II)m?LztyeE|Itn^N1SqY`u&*<Hi_den%QB~vJ6uWDf|PYq49CQR?>IQSl^y0
v>qKUKgwja>q;0EcAqxzx)%f^p505HJiF)oR-dYBguTRHu5cBbc%WXcyx<U#so5%%T0a*Yp1}V_QNrU%nQ(mbE8^LIn=CG_r0`!+
Lj(}Yva!7l${E#Wq<;f~U0_*i_k=7X)zU!%+RIlJvg4nE*fkF;>?UY=W^f|j5<cQghB1~}M6|dT`uC@McF-f{*Zy9@gc%Np%&&P`
8=ABKfDW-yIbi+`gw#)jvfT1NF(N<gEkc5->8%wr{u*Sm>~ir(xeRVeW(ANQ)Ub1`{m^U3zKNj^h<9|<?$NgmIHf?qdgcb8B|D;9
*j0+HHA|$G&dqf1SV3RFhjaUx<Xcfb5Zs&!b-(|B1HM*Yz$f+s%Euq_88WUtGU$=CBNnA{v=?3Q%x3K2O}`Z3kXib`p(FP2OmExq
^Zw~0O>Tb@KC@%8JDr%?|Gs3Ox>)5uoDqZVD34_8<sInWf>efN(6j~A+XNi1u+k_$+ULio#NKHTjuu{Rz~0_k4#Qz9M%*0Dmt_4s
u~1CIk_%Hoi(CQIl7hd0(db6gKNp6wg@}YQZe`p!LkAv=5!KgF(rK(42%S(JVUnz>f8|wbKCXpoR7w!@nkd8!>wgAhc(9q!)|+Y5
`iIXy!J<^dfsT1tUB<R;I`rJ`kcWnYf!!LwUHhVIX^kQ2Ryyj#SRy$d&!q5nQ{|%VLhsq?O8f|;#v@3-RWzo{1C(^vkW6+hPFowm
iDvYi=>}tB!uwWUdYT*%gHOJiLWc@!keJ=7<hd?A7;9x{b-;(d0Mbk>*7sya?3IrDjr|YsWQ;-OxpMFr@q>YZ(4gEq&6Y3V3N7ma
iWqhP0<m>3@l-QXg)!|$LIdtp4ZI({4Nz2(du&vL^G&#XNtyKQhE=5ngESo_NG+q*7Ui{hm`M5fD5Hcj<bui&K6TgU!yd8@qEyA&
MsC8s{R|f^E?b$19(JV2e<zzzUr<yQn=z=y9#xHRDV3#c+q%rA2grGIm3L&)+yo6@O(4_mRu(|w-E#s(ITbGW!hV7TVQiUVq}BtD
%i#}ax9R|nJyO&C(S5|?zgP*(wMALk9l!;&phwkVN32~;Zf@Z0ehT}`>K405Pw%L(Xdg33P`d5Hqjp8+KGwGJSz(R#n~G%=R^sa~
7OXr}#7{VYO}F`P>toJ~^Ptmwn^GL-*l9}NK3iYGfy_0nt0n)8_YrVz;@SMwWz#+s@5-`Uh0SI5xqF%pHhyk*!ZLfx0xvIR>y2Il
EE!p2d&c6rT(|0#Rf8OE?#rYaaV<0%@B*4*&PR$lrci;(Qi6Ar@3@nlVAfI-ZOu^#6yz7Z(pD3$)t`mw9r}2I^tO>9Fip)9$+oI=
$Ty*aUJRNVOyKntw1Bj&zEm@}`Fxfb5t1l^x_vHJQ{jlz>pzH%6X4%{#z<)g>FqZrpY7#>!~;(K!n8TtN2NJ5CZ+X1(^}TNv+nf-
(*MJ?XYo{RXw>RvFh~4nc>^==2?|TdP;zAiY!|B;4AawUE_c*$7%4u>yVY5h`)sjN789>OC*K8PfLQ_)nM;lvSlfJoQRCK)@2iGe
Ete+~OrEciG~%{6kL5FruEpN)T%zl}kl<uC@@)5rHg<a=k_6hjMiZ8*5z5@efLy7Wz_Ni}kG4AIN2-1b?i$zn|C}U*B3)Z+fw*^t
S!_bb1sy-YIGqL+JxDot8hu{Lg~SH?tw8AbW~}pM>N{;A9fUqWs|3P97#w26(#+IKp9talUj~SjSEsm=1ptpgGN$5N4GRE&h<{cv
dsHV>HbzFdd|hg69Ru4`d2(=f6q(2S?*)VLM=|baZ;7fO6%K;36yC11a4vO&D023`ub68^w<TJ<rh>@eIP)L3qfTWg70Fk9wj-NA
L<R@2+TaXS<eo<di`aw|A-%|S+wIwW*}VUX)|i1y{#S2FWxGp0V2?=C(zR@K=%6=Rqts`JnZZa0iUQR`P@jrcY%xip5zP>Gl|n$3
pb7IuqJdRMoh|Mv5x@U;V~;IRBkHrubVV`jysKTK?BLtt5YXSbYc-Pzt+KH8&`UST@E*5~mUA_vlj!5l<Due&3kP4X)&@z6#Y}cv
^pvnSxT@eJKO<}da<Tt1_gk><amQ@&sLc|uz}Mk7om$n^ziRQ6(*+*XmcrCU?FK9C$>E(|HrJ^S8c7kUeAru<cZ>_Q?315x1-F9{
>3a33=tvC}EpxwvRlohe9L=r~vgEv4^g)WS_`b83b93)#E_sF>wSEZS&t&T@M37`bAuJ+~ZaT(xfp_I(qak?=CluO$<h(NmMR>>V
^ELsqLII8Sv_yKrh*I7gZy_uy@h5EDph=u=HKt}t1XmOI(F7pUetuH9`-*Ku7YMnx8z=rysQ_aCH5W;p;DU#8IUrlNJ~>8rx<hol
;0J%9#Cf^^p~e2gW&<%C7}+j6I$m0}G8C%EVB$M`>_EOaT!+Q2`qGs!X0Cb95$)ab&38dXxiRX6)vPdL*}kLcGkOoNg^cEY8X!e5
<y8A`9(e2wWG7HN;vI6tOB;u-mVXu~INtO)gW<|adBpdz>3!Psa2IpCoY+Up$2J&r<HEPl4Paf<p81OO{{3A!!k*P{)qUZm!F_yM
OcaGN{TpV1>KprcDlgZ0X3`x<EZ7Wcg&Ct6f+afRBMf13!cEu4KKI`Lii@xOFQG5NYX))^q;OLKLK>PCpH66Z+GZ6F2&XsJgmSfL
a@31Kv1d69vE~s_|0IDX>(2-1c|OQa5zDcNp#vc7rU$8@p)R`$bIJ>M@A+1H^jK_mugGJAWn$m>Ih(k74PSxEvc>G;n2n#$%m7}(
=E7A`w66OR&jwoahsv}Z*$z!x1RX6|4^7V7A8_#q@j<~>mUK+SP!^$6aU&Sw0R}Egaqi}Ss*RHmX=HTAUNz8v{sM9oSoPud{274G
9GS&z4j_P3+F|x7>c04R7)HiHt=E~>EdAJ->ES2rw3aUiBpm%)_=J&4p&=0pANj*trm4gy@h>a07Xl^lYi;p7-Y>MW4hS93V(UpB
3vxNGZ|S&rP)9!08uTd}(J^>jdy#VW*!`y&KLjV$MOUR~{NOb&`S2o%zB!RU|0vxy;)deaqWQkw3IOMD{S))bzayzd8H+<FBsMed
;cZ)g-eb#M*v*Iv7%@)z-Nqic+4YEDIO=E9f}Fxxx^DQ+k}n$$*}$|0s`a*kb09|bH9<#x{W%$qi@dCLWNF~7eg+Bc2P_iAoKQr{
nmhT=#rP{vWfLVm59c~$MJtDsyRcKWoi+2?K=<>_TQpj+q3Ul$8hU&cq<hldT(OsiL+ko4ty=KiQF)C#JFS+J$VHMQq9Um%5A`uw
EBB8T2-nNEIpD@e>3HseOx0T5+<5K5aES-{nG=W*F??dZl^l%A66?l@QG+B#y<GrlurxxUtv@I@<Lv##zI;BJpuQH*nRSX);zPnu
jyeSkWk=kul#`fxIbhT)vFKb+p6DLQLYgU1ZIoiiKKo8Ot^P12HBE0&YOiGf9(?XE)Q4#F1@RY^ChZ2Z>OsB<_hHsc847`i-maY+
?fw_yd)<{P`=UUhwp6D!+!$nVM0RkmL(_wIt`vx3BE$*~Qksp~ZHD0psw~2)uGjm}VwFTnHH1W|Tu)4?6iK+Q5#leZXNEig4tk{M
zv9NhhCtg+BLRaoRXd)?2X6{q(uwdh-E&0rD8zTty-`k*6agt<GF(vhsv?iP_ae`iN_!51dGJx&+T-9ktj3*y29iWwg-LwsI^4Fq
IZ8BbzOHFcB8Ms^XH)SAyoe2C$w$e3meXnwtGKrOibLis+Arh%Kc#ZEVI9hcNnjkKWtYgP4D#3oge(hfDLyGA_t~*})f3q1ODA=d
oslqK8j0^6DqyvVyrXTNmAB=nr9YoFdDo00C?06=J*-+p<Z)95#rRK2#6x%pI5iD;lTeNNbrmJ8GbP5Kvnc_=+tbXA{~`gx{n~Yd
b*hi9CKe$Bw18&{H+e`J8BYaP)cy;Zx1t(_tAmJcGrm0|1HlEFBiMb))5@g^nYP}+K%^mNpz%p_PoxzFcNga)e(`l-2sZBOfDdeG
Vh!MNfF2{?!zlsCY6Q2$#Vx-&O8643SCp-k(tB?=v9S?Yw^cW}ka6&Cu--qFEjsfDDaeq219svIS1bRF+rQ0_7`NaOR%kSjU?T3g
KVwZB`qo*G#X!);CRf-1p75w+U*Wz!$+~o{=!PE6f)S||6J`;XmBq$u3a^drlKNAvHNu+(M&jI9oa?_udRevA1<8c`-d1TwnrO5E
1nr+P)xq!>b;KguCeR|#LKbnZbZQo7paX|V#NOAbF+gt;TiNC?*D1f==xk+(kVn<*yD}rVW%{RnQ^ShrwCs1tti${f6QM<l0q_(Q
{yV2)OUJ$z1%~8<s>@XRO%z%q=wl)Zg#&;y&Ty*U%TBftdg0I<jX)k-U|q)V^PkYjo)N<Pdezf#|Ef@Ms&CnONlkCmIdo}L%JzVz
Rb$}08lv>URxwNkw)W16H}Rt#9nn{4RCvzgOYTNPkM`kG_4x!BGnM--*qkSSYy$O<e*N7*!T2P}ydA@($7Cy@W%EEe^h_FdcdRa3
j*LbSO%flhL+8KEq9}h=1cvZ=Nn`pgP^Te6JP{d`;Q<yo7s|AsKMu}588^Y(1j1aNm!(dKKnOQNGjph})*a{ROX`_!71B2$8}zXH
1EvY1`z|%<tiiBW@Di65mY<(PEm)xmf|cX{9Rq_0M$_v;fvoYr6K~{yttSH@tsHZL(CX;Ww|`OPSYN%m8{x+|`sUWSu|b&Za-R@d
VZ2d%e$i$iBq&AdGTX~~kl)r%`nT@|_hr&S0fHY=K^;ES?y#Ak$(fhdmoKX){#tj%W)Tp#phA7xt&=kk{m%ob@TzxLq-qMI>{Na+
DD~Z9?%v!PA!#R*pD4#pz~cmWM6CIZfBU{%^;Frp4IcZUbHbaLhH>N~BJLKKRJIFxrk;;o(~uktCLO&^tJcysrTc$5e|E^irt1qa
LCmQB)!^_2VBT|&l_(hqKr5mVVR`}jBGtn~u}N!P+RuK{1my?)ccjCJ5;;z@f~gova>Erg;gf-BJ>vYoWO&;H+m)wt{KVZxSE@>r
`XZLPu_(@6hVvu>^cS#7GNnl{Mt<0ZI+?c>E)l*bxn@GWf`6YH;zLImCE)+6HD@;m5~f1H3Mo<mMp9O*=+^mt_@WL5nVRLJ2<28K
eVuNI|JQb+*><2;PsqNrXmj}E_2D}l0`C-%0MQ!%(oW1FWcellc*=V6Z<gMOdUQy@s-&R!Cnyct2KQ$$nLjoXb(qw(Epwlr^`XBQ
>VDsgiW+<h5ChaSrE&KlVPnY3#1Qd;1MMp9Lm*ihSYPbr7a%k`J%5&Jrv^48G`k#L2G@%<SjxM#tsKZ=QGEWLPiT~{?>+e2VoynM
O?s79-fki1*5ku1BF|H<ykAQI<@wCPqsxz)0lvu-GPBKrBvBIuPX<R9*viG7YY@whyW@1zh3GL=P)J}}Ws-^_)z1#otjfJnk623C
WmNG^1~*2vc?7mo7_X;UQJ44jH{zfh@a+Gyzz<@K7(=9Sn3E70>kSSX+rlyUv#pn}3@@RDfc>&eYB-L4tWCdqfFDCSq_u`N7s7m9
){nwqy>2WpWK6N)vB)qAhe##=3JmP)?g>lD(`D4)%F=-}_h!Y~^=1@~_Mn##L*L!Tzj)%<aUeiW4rI)!H*pSr@-XF#8J%0?(V9>j
p0Av4{S4to@D9acOc#4d)|Bj&R;3aAuT{qP8!S`=v!#@-?7%9$G3=LeC;wgMPCMz7_yb#p-awCrZ5_{Leh$N%c`)B3IJ3&XSKSM8
2qmXAdbKw;^*nfsR^(tCT&qu=u{MI6ltD^9AFW)<I(;KQE~)LCnId=-0oQZZz^$K)*VN-qpK-Umn@Z!9v9wc@cEU~+3b6jOj@GB)
-Xb+y+zquK=B=}<u(PUtfdsylORnPG3#a4~%Us{iCwOYKLZGtpYE^b^oGEf?*5svs+54$gI?8>saF~5blh5FSq*-UE;Rl4xpCeNs
Tqi3E%W#yi=14QgM{TUEw8||`aP8E@Imm;s`9p+{w0FU)$0e*5Xgb=ze02&g)$~2vD4_0+D8D2jloJ~d*#^-luWnHA0S#bw@HMy-
U7PHd2S%v{sYFD6&B~?rNkS>D3U}L^B=V+|lU4N2GH<wLHJ!g`Lh;OSIK%V+4kqdJEZ${ty`3&M?WB9hDtH#tF_`S-&1#T2GU~C;
!aeyR&I!nhQ{Xf4@VJdq?7(&~D+>d8S1dzxP7i{f%lQ-%%3d5u?&}AkO9Yk&?``;ie+79*KPt*yks{U9Wqo?rg!sncFFALbTP%CH
@5bnFO1r+GAI`=g4GH*Oif~@Tu-)BG#PRtlE#MZZ5*%qf-@u;iLaQ)Y9s#Ti=HEj-0y|mGBZUogho=Q=%xd){o3dB9v|d`7gX|9h
8Hy)GZg{QA0Z4h@P}D3opHR|%`QYJ>ZY^ZH0w`*~q#eT!f~sEa*6#WLjeG4DxT0c(yR`=1p7Yh{SOzsV4#H>iQxd3n>E`{#eaPJz
$yl{*zQIZnG*3aQW%8=b6ALoYq%W{>aL}8?xtq4)J<A^u=PpyS4ggC|CW@E&mP_BM!Z1|8Z<dg0yyAwX{h~+dr*Je@{#7W}T=Na(
5l3W`(j+a6syPI{v2}vN)oild*NO6q#^C0zckvSg>H0c)xk84iU-MUtMk%TbzgYIQPZdM3*Q5YoY7hEg(O@)Z-B{U(<Ew9k(268k
7Ulm57tlItMMo`z=!V{Yudf{jSz86<YM;I<EAGIQiYbKyQcidOdj6ZdlLbJ9h^o{uU<i&a+MXk=-E)0)>ap0)+-YR}G^+?Aj*BFL
MB-4R1AGl-c*WOtcFPw#ex{rvYZk}Xeq$G3IomCa`}Ty7uA}%l^Y6D5szZij#;3_+UAC*{KebSM<NGk~#$t-pshlNnu=3@(gK!Q=
oAx&$1)LNEbFiMY;Fj%uf-D|J!@iL}RSSdqJKJukIMJ!PkSB}ichTL?Ev>ta2;A7|UkcY&bXS(W5sU;hA6tv{o<*?ZHToessQJ~y
y4x<nhGzjoFYe#kpaP0t@0yD3GK})C#}-mMQrXG3bUmkekx@Clbmp*IkC^g(gBSOx;&?U6Zn|jGROV@|i?5+VoShB6lz?B><%SK)
^d%hO{kcJewpHjPb8<nS$Dz)4!=z9f;qEuVLfLEXBA2FSgxV}ukMZ@$L<cth!!a}mz&NfUU1;sFQdjt;CrxFNwQ;6Z?bqKXt*#=c
EcX_#sRgkNW|3<0f549ds#&B_V|6G%`Ihf5gsz#F2&<SbjBCdMPl+`!b>mVuib9#5asFWhD@J=azNx`x$^3>=Zb-lWait%vP8{|g
OM*vzJajX#&}3Uek!6^HuhLR28PEN)Dg1ng6Y(XcITdc$<$yNa!<Nq?3=YxQc5EqwdjlszF(1v;dj=Nu93kNr+HL4A(0B^#$oReZ
bwno>AZ#U%9no`WdR$8>R1^Noe}gwmQe{;&A=M*gYpzcfrTF<O6P9yU-?Ws8qaR+7p~P7q&5yf#jUdBzClO*%X|d2<ABSzE^AJMs
^_sWoG*4&mPaKEQ-E<AS3)kwcQ@+e3&rvV~7vc-3N2gzKQQr~LJ<{K4`b$B{`Z8%j&z<+AU}w|cK&id0jH>=$vGdTDCJp^zrUbIl
(a~UBcDA<ff4ceNtaVh1Rg{xux$Z4SYt3FY=YBzH9q;|B%tdcm7yWoE;;ot6ce&uJ@=m+Owm9W2u&G4Mew!VbF#L4SOmvVGu}SY)
00Pf>|3WGr$2$K}>8`X~`-~rBaHg_0kX|v<C}^#UKH1(2fP%%;7lpj9*|7%VQX}k3*pz}Qr3ez^p}%Kt{P+N^yqzTud?iu)m)Ovc
72aS(c?2{JqPDFtGFiGs9ziZe{N1-?&}e#&DADR|#8o(Kh~h?p{p?3GwzwSHn8HE6Ps3n(iAF3qGFxRQIUJ4yW<V<g=nRMOBd74U
%z%J$uFp@@dhLfR2|l(CL;UtxqV0GX*9SVnt%^pxF}(6IQB((9nWQ)e>mM?7$U_9u`mXfV4N>|QAQBOh0@@1##rq*b#x-qn1SSK^
L6S+jMkaWG?~K|Ig9A7!gz?EkS|iw;1NrtoH9-(tSs^D9Sr5`|D5r0$g88MMQV8H!stnozWB?@{f|8T~hU#VyR8n}L%lI!M0TQ~q
^ZG8Al@8=7+e9Z<v&d-6P_dixS*(VamJCJ*RjshkoPFeLG6iL<(SZ(|vx+t%vI3^{ad*7}fq^L4$r23EUhzU=&XO6jY@d{oIvGSy
{$FzL1tm?01`kdT!^ehJ9{P2?kydR3we$=NE>6v42#@?V-47zG^R!y9i_eI*8C<@Rum~Jo`%idK&pQ)jY;g#vY;fvKW$XGr={9Cj
87vRpZS*}Tkq3lLzp>A6zjO)1@8gl5bv5cbGKHNt$EmCuOfP%X^7&kRX`#;MJ=%Fta2F}sEmHt{{S%#zLEhfBIOjGY;+(<SBmPO8
MOTL1ap~k}u=OoIi5}~k;TOh4<FTz<^u`<(6Hqn6{=@;*g#jj;M@Xh}yIBn+Rp}Lyi7$snLK#(@7@fe$f8ikK>*fKv*M!kSvqtl+
925?Q#%FEHsW)y}AogJEi`D%k4Qc~c@g;2G-IFT(nx^=;06C9+V)6WTha*nZu+BjQfwjj#on(-v(>rL%L&(D<-j}uhRiBAq4yPRl
osR&%**fUUE^bZTkyMK{hE`RF>bGB!`ch>RIl8GHhv<uduyRxf4sDf?Kh#?<2N^{(dfrBULx{Fo?TXxcs#aK>Yvoc%Vj_SwH-%BS
7n6X-)UX%&>`Dk*wY?ENU`;3FC<PxuRqJ)08LUPMSno-G+nQJwjSKy;iw_R%>;FU`cGi8PK>&ajCjaFBUQm^-mgagUvVgmsh4l#4
=6Z<y?yS>-o)VEsOHleXSJ`@B#1`5lvYp#xI=b~smMYFgqZl{(iy1ARZ#9hCQY-Xw;ou+eZLL~5P-@xNrc&KiHb<I5pmP-ok3iWE
?<B;Qi+AuR2L(~r>W{WK?plm}BDJ1;anR>i^OuDb|6d4cg1I&nl|%+Miz%=p-FQ--a^poh$xV^%JA~l77tz!JV{B(Zg3#d>n-tOJ
i+ZQ!-T^M-tX?YUdbt5wq^eGqBkf^Up%CqZJA4^OxmpvVrm^Jzt8-0Q;!Z=qYMdQ<@#Bk278ls!X`m($v>2GQXje^oBgcd_Ljlz1
<@9B!&Sw68G7(tMr~Ug=ytoaP-A6D+T`K6?p<qi4Z{80lhqhB7gQVKXuJi`Jd_`-;7_1#T<=sWV?S-%AY2DMXYlmR5rZ>-M@XM>=
c-v^6FzgCgN$XmXqxjp%9vgzS;QSXO+D2z;U*oMYVgJ7l5w494%W+G>Hi>R!@E61iaLJmfWG`665~g`RbEA#YnXg!-AEd1MWL}Nt
JoKr5Az?9ou%cFAz9mB)$I7ozG7X|D(5(A361O{dFHb9kV>?&*mJ$AdiGEDV*zhq?;#^guC>Nmk-^7ixzcATMMd|K>U-~%`sK?q{
HJUJdIhDfsNpRmrLdB~sEL1`ndz@0eddcGkh9*@wI*n#C>B2sREwH^lP_R=X>|kd&e-`e<60IOzfbFzo+xE*r6~wy3sf?A&BNlmO
jRlo{@WnvM*C62u2cP;DpEj5N%%chmJGi1%Zf_FD#Nh=<p<*Loq<((nI)Vw<CDAF^IDH2ITgF2+%x3i1nJ?cPSZfhz%|=)^!eo!&
VifDX{PyPgu)~J5`3n2)g}V@w>1prGcktoZX^#g5bALU0SW;}j1h@LtOn(JfYtyAlJqrdKlcaY>Tv~hSTnD_8GK<UWa)`v7bH_hp
A?b&5#WdH8!G?@9Z)ZVQoXS&l9oTEZk<Z5N%2&ra<>u!L!WhMwK!!fE^C5<w;qhU5hK2V;wK`9R+IdHto$4YQQR;k$%%K>PFsO)c
to@<X@KJ%@?Hz;*@f5+h@0D-sQj4wW-C7OvI&_#&H<>Y96f~OZF10(IMv6Asf609X&8*Ttj)frQM4JWQ{s1n5z^*D1?pdj8`Z%?a
x~yJB^y<ii0MF|oS4lfca%bBzG`DyLPEu!s9iOTPA1uea%+(0@-7s|%e_V9h5+yb*oIcGOA+1v=&@U0Z`R2R$QQl|AxS{8iZ4`}q
34{K^t-uEf_33f`1Smg1o9~#_5=zU<K^F#eX>Tr-BlZxiv!n%PECFkJ!DTh_ec{dspT62RIE(CN#76%qV;feLJlq$zZ&F-^5I*c9
vMQpO>=mhg%eIX}cOjW`q?1k9LyQ+@p@f;R6Au5>IfW0p^5PdY#xyJdKmRg12WC`Z?ArS^>tq9a6hM>%HhcbZ!Vl)UjtVpld$qX0
j)TJ@o<9(Ou0D$jS>v?bWY6>>@!7-`(gm&}viX&KZQ--+(AoR$dEERfg;(<XGQh-<#zgn1qhshFZvC6{q{SxGtD;p5#9qY<g&yk`
uPO?AXR|R~ia0xuzeJk3Nbj3qO)?HfbwHaM<$rPN%Zstmm6=@K_WONT*oL+O5;1Ewm)1_m<oL(jdaHKn`S{BP?^n$?{4s_J3u?<P
MOrjRCM^5K6sE3jkJwrPP;gmCl7`aZK`jTySchEuFEMW(I>*vk@Wc}mfXYMOM$Gv&4VT1MC@^sMAyGEAU1bKKHXuXmMbc0%adnJ&
fF%U9{bAS~I0A&DI$yO181!L5!GVsY`$3n>oV~NZ1jql`E$~=m;sX%88pA`RPxwoD^kIuD^v{1d5H?gXngsIBcaSrd00xMocaGww
tf_bk**e&zh}ah)N{-^wH$>B$+c*O@wP7(Z5EQ0SzCII3i&u#$7Sd_zW;4^%ej<8KL&$PsW;rki<B%d23WcKb%HQu|go2rh(A0IA
CwId>{8ZUvB=B|G3E#)Lr137K?y|swLbh}<X)gJ`^;HK=IaQuPzhDnlUG_^V3y=k}4X5_Z2SON`OgOm{;AtroA@fVqZHCq;9kTJ}
9}_6^Uz{#;Wt@4<drY(ItofB^2;)bjF}1M0E5Gs32=j!6Z;HU+wo{L_-?e+xlgBzW`st=}^m{X3bL^k)!uS{B-CrRt7u3U>)4a;4
huJ^BZG`RNosA&tMHguWr(u+kyt+uafx@%JPHG~=(=y`)!b;%KR*T`UeLbZ;5))UOsx6T|`i$`X6oYW>BFGLJMXmI6iU8v%Xcq=4
81PLsmhFD==yH(<`KE8SZC8(}7hR{P5e+JR4iGPwTm>}yyS#u$7*!QK2>~R~XeNgTbR2$QbiAUjyBv;g7zur$Fx9bT(2fKL1L{pi
<tT0!D`bzN$}|PR<D(BiPq$yaz{iMn@Pq~hrQE1g(X4lv7>#AQcvJA`nOt*_E*&Pq(JC{i+*~sMz&NhL{&q`z9r8Z(=`s~AWCQ?>
RBjgF_{v-=Vv>9d2dNj}G94UkMPb5tiQZ*NL0e*NetMBJy|XlC4!$Zpv%i7JAI%yb!7M>UqkY8@M``TF-B(c}%Pj6S+sb%V4S4UK
IIm|?$%@Iho5BnC|5tEn?q<0lB=z?CafvgpXy-OJICW!qBrEiQK8&gxX#`O@I~Od~?-VhX8sj3iRfL)#2Wl5lx3Q@m9h4Z)`kyGm
Tp>2r(<PA%CtH8dGod{fAs^=K%wH;mU}Jrf&%b<XHRpEnR?ZgD5Mi6&&KB*l06oS`7x182yxOn<pFGMwxY~0eo@a@J?^nS5w!=I{
MvF!|#%C!!YsO`<eM}W$I2mE@yDAr?q~uWMpM*Z8d!G&r`?2*3T5C!=MA@8PA+vqsn{TsfIZ<nKaLo*ch~D)hcMl&|ZQWqw3kBcz
Ln4@9>VXZpD>S1)Q5~e%JH{iVk~zC!u#DREikS+v%nk_av0fvIs;gE3;`lht>KZ7gv{-krL|Zy6g!EMCHQ?ljtT-!Y9<JI3S|v^?
{++nClwAmIXkOD&@;I!zo{q9gCYG0wZw1F;It<5@V#A^Qr#W>WLkRN<j&N2n8x(Xr#ff%Eqf=@WN!{APcv+{k14i#fjpwDVS%wId
uqvBZJA6n(D=Pdz-zp`TnEpaR<Q1vevEi0yt~r4e63#M*gSbk4m7hkhQCLYg>#80sRNOLCaVt{C8=Y#r__(^iXXYDX-Li)z|Gg>F
K;akxwD6B<Jgut4<lt%Vtb&(n93PS?BA9E`-aF7>G55K=%gK@PIHC<h_=9f=baYA-%}9(V`dgbzFT<iT2~7u#XgT#}F!O)sMIN~O
^<CC1o0P!77BF@i`kRQz!%Plg!Z!d6a0Zo*dERxmT9~9jyZ{S_8OpN`#yGx`+*;?{!G45ahyKK+x*3)}SS{vU>h2;3dNaBaG&Pyf
<xhAf=?<pq<oB(O7gMpd-??jbPecv442fsK*i|(CIm?@*Z_f?aGSXzeTl0d)rR^3mq34{$JM8FILODb|f_K^kXU7}d>Gyq2o2%0;
)R7FV)hVDVB_}?sFK5VwH39PPw=qrv=az(}E}z6Oa2hm!ctNl-C~Ka>tTe}0q$3>jFMxIk%)P=FrV}I-0=?zRY<rqf6U3vH?f&K}
fd9d;yRi1MrbZE<H^mfOfea91DOl8&+`xu;;ZLdX-PB-256xHtq!x@5{-IMXpI^2_jaLRlt~xRKvj2RX^I<q#f@LUKJzIZn^iB7V
{~Tfbi_KPuVvC)wYG!^PV^P6FcvEDPuRz_g;QU)FkiA|q8?iqQ77$$x2JpFYkBCb>P;{^IGApicnBC3jmJ|{$?0DrOnbRL|j8LX4
dH!_XJ!6UDrjA1+O0g|%(WNIlE?qs{Yo8p=KNrppSmG8U<kIL$_KU`=UaaMmMNO|7Ft<>`cM6qy(+<UHx77H$=91t#_HH3E+y|>8
2j0k2iniHNg2n4F>Yl9+_fQ~qWA6nFjgyko`LEh^G}r*MY|4)f@I1M9GvfymWWbxO?IkNglPW&e1lsD7U7`sHS@?b7kOsD75?NTS
P#mxj>qE5>uLBK7FU5oSF>!`kPMG-;?bnkZJLaC)fvcPIDfT&y5$u#IfJ*L%qOO56@LpxO55^<Qr=?RGg6?P5?DF#`RlzS*G}x?w
iT_wCuLx)CwgK7rRwb`+4R0ckFqMY|-wO@j!j~4D0(SC%L4D=ZOH?$SgZN4mH`;mto%HPlEq#KbVGfjPL+~h~lV}44sr-TKXXcy7
Vov?mT7+#78R&y6<I~uUwFA?THCq-s-#jEmo#yNrdBM=X-(k*O{t;PrZR6X*ij65eo|?Uhh4*nbP_#6BOhojS>Ngp_EkmTZ!V7>2
dRWn-sLg~c2Ey2$^^y6yz1d9uap53u1F+jJD{_$YFH$a*ZY@h!nu)w>${wuzjImWV&ryRuN_X#PB@BmeN3PRzKU7~-UNdjYJ}I83
4TwFZJJ<#p0<Q4qiVUr<mGZtx-_c8%)}Lm3?LC<uM$0XRL+V+O%Gkv%KBurnI(#=-`B9dJck+*hsGNUo*ZU2w@nHd7Q%BITjnMgh
&r2_Lx5_iAA)M=25cO>Oo>EQ|`O&Y;9`9|Cbby16#~7~hk!`}QI>df!fR4*CvS#S#7fH9TNX^7M{Ig(q=qh}y4U}0Z<77YZ7_$Yt
GDi;>VmKMuR#~gfF_Ia1%=GpPW?5Z_&G^mpnctsk*~jbW&}E6B&Qhmt_xd54&jlkYm3G!}0D{u}J5=|sO#B&CgKJE%%5Lb4(uW~E
gV94B4ZqsrzEON$w~LF7H`r#mqYM7oE<r|6I}i<EGgw})<+?_rplBKq6l+Vo&O-8xbZ*%u5u0j<eJ^ZSWQ_ZtB=DWgPBqTP1&)|u
{41~K@!Zy_hXd;#L`o^MCjoPu6+$ZFo2+c*Y5|5TX7|{k3ZFLq-&wm1=x$iwFUmH+Pk<<Hao0!6^_libj@b%bS~ElW#Djr|Wy7kW
X7d>;tGQ^0Dbl;#v;g#K@J8M4>p1=QygAZ6!alMxwID2R!)Itk6=Gjv?L3$jx+OM{R)o1G#a^F1%)p;OmMa#>0c}E9Ei?)xYfa`_
PVGAqjz_8v80e2M8u(}KlP|8oo;m|JfQBaYBDO>1ovdUW2Q+-?B^G=cf-<QN?~Ue3e~j$|R7mMWOvM5ITzNV=DC5KH?+(MP$u}I$
y2!+RDe*)A;0n}6kBSyMcJ=Yr*AtDt>7qiYq_0+P{9EK5Zvo9QHS*7;{TyHda7$03qc(Q8oYBJF<s!E3o6hn=<e00E$iO6{mVJ<?
14kblO3GVIv>Am!`z5(HP3DY#z0{IJl@Ko8w6|X{Nu*9=^$V~hbg0B(H>Fy6TV~r76GJ`oGbZeAJXHe?rAXj_nv@U@kqai@^iPl8
PXUDop*s1yNn>}52z+UBsaXNoeNCS*{vkQFSVoTl)fWBMqRVH*$M<PQ88ciSJJlkR4!wPESD-m2ODEQM*XoQ1*_g;3FBSoKY9X#U
W78Q!S(Ptr){u5~cy!yaCpin$8=F$#;rA<{Q(QacgkN{n5VF8IM>fHvA-vRIb!AMnX`VODyPb6FN|Y=vK&|li+bJjyz6?C+mY-)R
y)S@~iujBc0!no?uYimVpqpRloxO&#ucnX7C^a(Bi}dJ32>(k!tPvBX#vh-*&r`buan{Uwxr+ehjI}1Rs{E;X4~6Wb%u(osu3yhg
X;!Te>F?+EOK#M%qti;=oN#(l{PJ^Yo;&M?I^dtkQU`7_+gzZFxG)7Fk<?sM)`-7jwdHzP5)&<DL>olJ=lOisu&w|Vmdb|<)2k+J
eSX+62?U;_ZYJZ_iyJwHJ6O8=@zF(?#v6#P2b>}qeCt)EWlt4EGu@sHr6|mTt?#tEOnxeYEc_a{{Uls^tk}E9xo88}K1d=#!Ujr~
mQnJ6J@YTH1tz!|ex&)U?8~dA{q`IuvjAwNp+GUNDOgr{#Dk=W;q=-Y=3gE%g%l__2zTl8Vcml<sbD*dm-U8d4r$%_)0LhV7$3BA
1L6w4ZV%ivd3>e&bpnUAH^$pRy#XMoDv$CnF511D07$bHnRSDOy2o55rQI@EsB7<eC*qL7w;)pX_hCh9Wf{O}S;smD+&^1B7t<PX
XzX<W#WJ0CzZq2K?~3|`OWqyLM5jurWxF20GpOU#eGC^xqK%5^t;Tua@OK|&7XMSO`q&u>Brxt9y4IOGW_j0`S?;MwwIZ9l6n-vW
aZrR~8QH5SY1Lm{BqD62A8UW==g|FR-Z_g{q+;IUFjCNGi<9(O(gI4mgzYMT)WsNv|GNi$7o`-J;)#-4ueQ7x`}?7wX->@wVRMyq
4C2zkJryJ`wyIzYgvdnPF90$w76SS@$?$(S$xA;ws2Q;=tGw?5Z;IIID9=9+Gv#EEzNHcO1TJdd?E~I6vOBgk+NFoA_mTfTWNFsY
+~68vr9{H0=<4NvV+Iu5X#F7iPTW=~MKh6t2<j+nuv-|pWPWZiRnY{8L|=)n9AjJdzj?Nw6Cc~)WfdjbUV{~btHH}TvDYGE5I!iB
vi`Wet1AH4>-)?2;&9x1B)h5}q)_U%>8-B=^~T+YGEe@!FaVHkr^uNzqOg6`|Mh4qT9f^{p|%d<<jDex+7mE$1MRc1$n=;VMjJoF
9&=FCdTBr;g!0&<yJjY@*`^Wf1WiZ>uZ};E=Ay^_ai=oiv2jZo7uF4&l<{?9{#W$@nE^o$%FIxmele~+#+WBVGkg#{9Ww!+sPZWl
!R6F|UTwOYj(rb=Y<A52W|5K`Gbv2c>9{r+LrH=~YG{Ox1a_7&?|tjZj)|-A8Zcc*Z@8*%lDns-tU8CQ7~ie$AAlc<;go1nw@QOJ
qIhDeviG7VPaW5dJuTu~0_d%I!>MfS34lNp!gEsZWJ?i<H>(tyF8AQ~;X&%w4Yrm^6J}xo2S$s99Sf6#yEe~8(++9oT!ac*OOPL$
NViQ6zMokIP&E53z|LrpcSL(Mf7*CVsU7KiQTyLX{xzMXtyP^Eh9%q@nieEx!fJ$6?rTBFf)0p4vw0e=6OxPK>E+^sl5a+1@B)Q)
NMIv**MfDXk)*1u3)Ng%1J?9M9H|<HbKiiJdpHRO(jfZ$!}V<+ME||jXuQStF&VfMyEh6_Uc|{3_}K_tjVi*@4mTh|h&2Vi&Qn=G
h$LCoRlGb=NKpPvpWGQ<N$}4<pJNMd<#tLL9xm&x_WULxq|!w(tFkV8=sChkI=NVu1O-_B^Wll8M`PQE-xwnXgs+H&cm~#m(<*sU
J*^gEIR{86g#{jKx4(`Tc;wE#vvG?4CZ)QB6o2I>vY5NCE!iBIW5pb<Uj0wJ$9~zwQ_NVd)ij(QqI+b^I2=kN?rATrUN-F+zCmpH
BDcqW!vv2$w;LY;Lg}<LWgi|Vi*BTl-Pyttn&*FVY97By&J#FE-Kr#ASj*0$$f>tP(mrnk)z(3Mft^`J9ZQ|?$ikYJyShcERt|+T
vs@S8qou|yZAmQ-E^bKzav-aTZg7x|&4G-_e+cbap6tOuy9*Zhy&I6M(x-3TUt34-+RJ@6rf?FykD5H~Dod=fi<ZffWz@ahW-P)Y
?MY+4QPn8<sTFd5^sSXP5>+W+wgvd!ROo?is=aYx;i8bvu@0S#IL;tGL52Ftn-Z-r7b^sPr0Tb9O#2Dqou%OBn41X7J-4}eqWgAQ
9)NM7&x~;Ox=PSi>9&+^vUSzzfaW~uv@g(RM-3lJx><)%iV{$!S~SpB$9ioq>{T6c1|kmYT7RRs52exy`_nLsD6o-dNCXVDYx(G_
8GV+O*D60)vg<HvJKE>U`pNTQ+xN_TLb%mBFiWYzVUL_|(oVq4*}j<(HV3<u(CM|-v&iWlPZ)XUN>-nM{jy{=GJX9WGs!tZXfv3`
Othz&qcA%OZ30KE4gH9@1z<04RRTrt8zn<u0uvn+A~m%oxj0FGCd}Yp9mwCDn+pAjI4mCCnTNW#y`EZ+9AaiYq*pe8mmOID(YKxp
l|CVe5ncsgazg7V6H0YByorYr?{Ke+KvX_t%VUUp^C;G1Ku#x#x`w^=Z&7%Ch<qc~MXfGN@sf8w!vnsp5H?f$6QfIM0s>`g1fE`F
`OjadPh30w9F331lPcwcv8*DVqS<RG&}ZwKD!*LS%5=oQ<65AGljU;`nW|21m)e|h-qd=BL(rt#kG(y;L<o<%u(TWME5-q0G!m~{
<AwRxxGPBhx@*M}2xlA+BO$A1){o|pd2<vz5hzrse5%FRUz<V35PS7M_@%Ldy||x<w!v^TKtbq<vjqGPEy18R!v*fzmYCyL-=98Y
q&Hw>p*vyl4(DSOLPrK)G-AFJW1F3z-=^{4%tj<VjKqm1#_|z)IjS)@j}8#|7Su$u7{k4u;8!!NYDQnU+BkT<6(5?4es`;FSdF=E
!L>!|ZWg6<gjf;Nq|otfWghGAQmrTQ_0M7Ba`9Q%)i0fz#|Ox-LI?77RumbRmH+{fBoGcI&iK)O7zF^lX^2^!n~+gX6X}IaA*r|u
er~Yyz6!^-tkjy)!N@l=!><0Y414x{(2onniJX^ArNQxuzPP0w(|&ewyR_utoi|^NO)acN+je)JO&H&J;TvLYez!aQK9?^mRJ%^9
MF@$!{bGY2{kh{236}HJp%sy5+a}RB$bQfVOlH091sp6BvF9i^haYQ#3qN(h7916FV%_BY>$*@#gp0NzQacfe*^72}Y+bJ<oo`v%
hi`Jrm#Z1?T9P&*hML)BKj3J7^mW@^TBc>|Io#Ja)j7JC{|N7>HSpZa@=#y(AamfYDcFER=)O^9sVrezTEL+BBXh0DR8&T{P~ps2
W$KGI6~!R_NtvlD9K165i-z?L?hqq)ZEV5oo|4cTWKrvC;i$MIv6dpod5^P%vAOFuosk;+{^?UzK6;^0)`R(6D>Q6KN>HB){njqt
@mOlHMqdn+B5ceD`;9Gz&3afG(V7VaB;uZEyCzHG=MB%RlDaPn(wD!i=3XqlI~S2I==IMrFOwd4+2wneg__Awb*?HD^b%=iWB&C%
5C0z7+;)pf)-*8+c~ws8BC{b|ToSCE0ahS_KAaz5@;V8CSLSqn9*Yk6_qtPq8uu{zyZzqL^<MVeJG?vHXeb`2$`A&ZlP&V2+#0{x
@yY3~I^KF$eC_~nrTBiqkN_J$TsgNe2^(vso>PY7qUox8FDbZxYftOIp<P>4JHWcM=bggF;F#Yo*^Q=St=7~J^2&tNq_e^h#JRrX
7RoqTzC~R;?hIvpNZ?3qO)3?H;`)$%HqT-`C8SgSx*C=BR*(+TBi=H>oi}VGEO2Ws)+Ms8&Icw6OleY|ABgf(F)iJo(RwlZRVv(P
)M-N#9N}V)DBxqJqc2iy{0gPj)ek*-3lVBxy`BwN1s2AUeo{ebxY{NG6}mdy@0Nbl07?zoD!s#kIwGkD0PEB~RLccQJJE(CiV_W@
)6mIcNNwX*p@YjrF(Ibx{ri3)mducyk!HljJKn#&<BHD0rTh72tRY(|VWwI*i}Bp*8AX_}GewZvm1P!;QHb)Sah+FF9^GZbc?gE5
6!f;yKn~wAX-h~?HH3^Qch9lPwsST6?ig^&AQ)(F18+JiZ7-9y&kOLrfn56KLMU;swdrfh_Oi1Xe%!jEQ1o3Kn;e;xWpxs>cins#
pI_DJS2JReF83|uw&eu1E_@j&444w=w_XJeC*F4~ZQJes<hisB+h2AQoE_y*5d`WCk_{d=1zb%r#&2oA+KJ)KaQ?i86%?W(<;1{g
Qzk(DqW)(~9LT$zg3WNMKw;FtFfY{_^45_jZzw`J{rJ(ZIcv4cjM{8pIK-bh(+H@0o@ZMsp)Sd~qQJN|3VMOhdc;6vGMf$31YRp)
(`PvMBupYrbwIAmF~40&%{VwoI&}#r=uYEZK90ArsKlB!0KglTWEu~y6bYmFs9PF<mgh*#lhkt`#OO;?O}vx^jn;J2&-na*36PBR
&b@+`4i1<xS1yHa!OVwK9sO;q&=bZMF%VFvlG-{s<f41C@lFx}n<MMVcRr&S6=)A@A`W8t*iwia<PLdUIuThQod|!eo*mh(9`mz%
%*l8MPa%GARw;a9$Li|IGrera5?eh!5?~k}L?UC^*u=sRd>-iE4Iqwq!m}WjS4L<2h?11uO|&0}FpOg{#cWfOlKIP>vY$k1-5L=$
fxB(}?AgVoF+G(#W3ssk8|A$r2BBvbFZ>K&<}ffd6M#TDwm!<u|J;OJAWb#MsJE+F&QA4$qoO+j&N~d~0{6A1$QroMGptf`&Zu`f
N{rdMrBT-Odn+x^YJ7Il@-sRgZLyd16$8V1q8F`kVNWT<-;ecv&pL`idFCI)5#HN1Pj;*a;@vB*rWiD2tT3^|iJ`{+JED9py&eio
%02q<(~m8!u5t^WMjz}bn#nsi(3;-$dGS5#o`ae_#>8~|D5DQ@*-K$mEEI>AheRi)zRaE02usw1GtLC@5x{iZ(iJmvg^n-?GQ^|F
d!fUN)OR{;>?19cCQR8Y%+wxo8E`P|%a7aL%Jf*bkeZl%_&<38&dLV<I{l3Y)!k}I%fb(ee}h6pjwMI|Kj1=b?hLu#?o?a|#ko*(
#Tt-Rt#*3eBL$Y<w<cn~Su++wf*2gmy08<}3q<c#sg64tk$r3}&2nc3<tAZ~J#^h#pl}w~?6rz*egYWVUfEWfej;~94LY&<xGzCa
&?Ztd(P3r@iTG^LCI2Q<q-t(;UL8nal;@-Q1V&*z%kE#HfThLM$4XnF5K%&@3rryNy){fwhrv%aBrhM#ec4EuRhkN|99r!}ZM&{w
8@<2=5i>n))5NMFv|PcQ1fQFufo2`4xHuRUzjx=j$!p)qsB-~;ACH5=!?0xH{xcBFqyyb9`f;NXmzV2)W|vHNOUJv3XZwfRD|EqU
Dyz+-zz960k^B~Ml8)9dL9r2mNc6#=lQQ>sdrl21gPJN!9c<BG<s`C9gkhiPJHmAk>qGv9X596Tj%zp*+2aDtF}Cxqav8io!^uQ*
uJ4#%p=!ONAsEg*MYeQkdtBFcd|)H*tM&kaqI=A(7$|%%OXd3U*|^6~PD>E1lMPwOvFTN&ng)99*-%&^P6^TDt;XAJ^=QBaLO5Sl
;s!AK*F^mcd43ccGg@$c)R*gekg4oR0pC<*1XE9W6Ds@*{N73Lnu<~HQHkzO*gI*BK-xpO`oo-~3*_LsRl*$i8<BSyhzX#!a{E7x
v+F${E`(CwGB!ApJGTb(Ku;n0gAfo2Qpt5aIGm$CU|7OWtNEy;|D^G2<{ub9SJie1RKz|eOg-Ison}KZ;h49*lTz+EP86>7Z3Cc<
so7BVeNZ9wVOoAEsQ;J<Gb4tV=4VRKOucOw!F$R%8wAAZy&_RCXQA%c<Bl-Ev_D_JEr9@Bcnk2l7%9bT>|VGB+K`p~1{1Qzly^Km
X^QHqL8?Gji`zVID`Jts*@A~Wi#IXcj;p$0%;%p7SbGfv6#OxpPn1{1^G|N&u9R@EDsUcuN*sqrnul#%kc5b)_O~<c&Zf^0Cr|Qg
Ks{Js)KUSYDNq~oK`J0|vrkgy8oXW`<|9i&?9d#rM<r9?)JhtbGr?26IS8+hZ2m?;0b9cUvEP^v0pan+0yaBsM(i{zNr<lp^7`=w
o}`eN1)7&lEhS$lIuS6EXBRc?Do6&E&xSo{NF2n#le4+5(Q#|qQwy(p30ric=Vgf0Ld5;9l+4g1nxOXyq<QCu!fdG8*bN>o%1AT(
PdzV8kY8%3-)lgTZ(-$i^zEX(d=QP{K4VVVQ|JT+-bTwe^yj&^HNAa82<G50d$a{jo)f(*+v@p`C@zp;QRH<)Jg@Ze5SORZYO=7Y
B<aG71ni!+Rsm*Uk+Do$g8{3GE=u=1M|volA7c5ODm8K$xhFzpsVJ*Bcwyz093^Pxa%PQ?u!FUS{HN|so7{H*JvK(;EPLmmww0Sp
)LY3yoeKf%h_X>;qLg`LFxoO$2UMZ;xT|DSCree)+^nLgxMRq_`}nHA%4AX{axqi9<l<)HX^tlr!MFC+%#|ka0wj1cIJ96Vt=lxw
MBwexX72)hrH31WgFpcK!$Oq!hhWzvaJ6>?s#|AIGY3!{k5-)x_KV<X)Ao|V0&b0P)6O<<Ln)f43!8YNjg<mTf=jh%iruBVw*8Q{
2g}2=5D_qpLqoprPYrknF!fYw$3}TiU#Hx4aL$)|D9gG7u4m@Y{xqC#dOyLG-<8gT+gS%FG07T-(E_X8(Fs<MBs0**;9i1VL-7Q9
w`PL>$b)ILyT%h656GYp+E$l|*WLJj0^ocSZCLK2>roz1O#yz>Pslzuu`zNOHLL0Lvc1#sD|#1Z0O2Fsc<@pw%Ik$}5@yl%*#JB_
EU~`13>oQNB1muQ{PJFh6R~X?i3>gag!`TwXT(UU`O!nln#Jsu+Z?XnBx9ug#nXP)Ej1>ToM}DWp&9E7z%i6aV(z%$APCh*$;tJ5
;l0aaBFhMPS9;`17SwAQihDbZB*fEiIxkMw98)$L*82XpXt9!6JhZwHCG4s0e?7}EV-rL*#0wiX!C-N;z-Bcf)u`CucmjjBsnf48
%G5<Ccklj+YHHQ)E^&^$sJcKe#y_x#uaoRE))xjbuPBPx<x8+UhDX@>k665tqsBw8ag_Gj`YvklXFMom2qp2|!aO-Mn-bU-S=xi2
OO6#{-C&9-xXP9Z%TAp&aw_A6ga}A<ob9v1&k@B^Jj_D%%b2#WN6lRGr$65h`D=f;Qv-%HLw#u7ZH>gyk#T8E%iHYR79J$-4+Hz~
ZN6YgZBM+GL2?RIDNCJ#8DT_gw=-ks<x7cgH(Yb8tjG{6!TN@@0GsWY;Y+3+iCaVim5#D~bO(9Vr5qMuQ7$>Je~@NntP?VjQL3PM
p%Qmq1y`2_J=~TvW~ecgww%z=xkHJ(B^FQCj8vRDWeaYuW9vNqtG@2OX`T8IzB&}fS4jtZ6sD%kpGb8f#3RhZ1~$m480?aXn|5o5
iH5IIDKrF`S%*FWY43v0`=#38xCR*;IF-$a_xqK^?bq+q5F)b2l&{^z8IySU&xSe7o04OPgb3vkW4c7wNl6BRiJfN|5_`kkiO_DU
q}mG$_^oX|t+YxLe~MLvP$_;+NP8;F`*yGzSM91avXBj$<EEmTRWRC)li)O%XVgHiwB><InqHV!CgX@0nIH#SjARS8-L^9V4LxhS
%L75$NQ;=wBmH1kblFdi<ZDY$9%Lk-(jQ9|^2V1-zG~1TTAo65C*XO3dSca1cI>02W`CU8<mg(7w#I?4CeMlQ4e)ND0~(|blkNDw
1ulT;r1j?*Qm<{Wl2A+8L)`^GV|LIc8(YgFheSjAh8~9hOBtWUI9s(0^v|4M3<7{HjmTAuGz|U2IaERBNaXvy)nMzW7+dr>g^6mW
04!2a=~SuA_6C=#t!tvf*sEgWYtuMKa}ffUr-flU9FJfu5WIH&>}OMPO?q?HhJU$2k>&4<7bE})T2CAvZDpmIin4yRN))t1|LHmO
tvXQEw`ID-im%nY?EMAbk3Y)HShpoWnHFhi0`Z!)TskV{|5mKL<>AAJ4F}<n6V(~RFv3<)P(PZJ*d3Zj%s*o!)1)~QM?hcUe86lg
ez2`cb4uH!wwMOI5Sj#}XXVUXso+xB1C&p)BC+N((Bf=kQ$-;kndaRyJl|F+ev8;m@pj}-i5lZ;cSxF*2IHEAa>2U^wIy?lO1U9H
cVorPv60MaG=)_EEP((`^Ru#2iUXg5SWqR1;`WdtC(=SX{;@Y*)Ch5dL%dNd23LM;yh?kj?w)v!;F%)60?Do)wxu^K#0iLdbw|Z&
Hs+c)G@uU-21-VjGv1ZkHEzY9=v`x>&Htjg`bII4j;6!L?-!xSkOO<iZfzNgiVU_dxQ2gTa)GU>qUrLIfU;Th{e2GjXgNyeBrv4R
bi9o{`AZq@tI~4I{_^$Gqc+p#5%tV(`jNfig-C&dgns{8fi9AS$YA6{nIXr-59@)3(b+ic;qJ9@9kkhW+YGcuF%dwi39-4ujxz@r
P!nKp92S>j-+L{?9FHHIIQ`-tyuHDI3_-01*;e@dsWX;5Y4i;+(X(dn;G%bt^b2^cE`UHuX;ii$rA<fK6R?WqHG@8~XBYAru)!Zo
O+hZru74SH1-F#Osmdd;ND!9^vSII#+xtaonvULUdxY(8#UdMU1N3+1=fQ{9@*kyYS6Kxkf~&=uyD6U9k3zVLPmTel>(_Rt?DW3)
oPPrdZ3Bsx<4d9xMPb?3Xu6#QSUoSLnNV8PTu*dA>L_*<5Bv+&O0oXu7g7MmB0@&@qDUE}x4jE0SN_^7)B#|2zW>4i#<SAU47@qP
ow2DJu&do-K@5pZ-0*J`R|s_&H*IuNk2VtPP2+y#RMfqJ!T7E_H4EEZ$nd!vnlDGdWv2{0>$*NHpH5o`5<0{A)-ov+4ItzH3q1Vo
EBKa`O>dwdMgjra2lkhYpagBTwDi*196mb_%MgaKUv+>(pFuOOi#KAKw!r4jDLJg+vEItNAce<v@72Z1R`w6n-yBRw6~<uCiQa7I
ag=pAKT<kt%TsmptcGA76j`$0#mP&;3b+#O=WQv)&pH+f^V=)!WNQA{6-Z%JT_I;pu!F6i+*Ixep=jEK^Rtd#=4(ZqTKqtyZ?1|o
GAuGO-JY2FBQs2t2gP%LV~g)zmPwa^o@-e`dFPT4A@OyzjOlH#UDZUwPs~=TUhR_T`d@}ZkL<+s-kp$5J*xaVC#X7*);>EJJ64f0
n{AN|Dm3-cx(R7h>7F3rFtch({mOaQS=5pXR!|0sggaa4Yda$B;!`ZTP2ZCHQJP$WJ}y%XiyL7I=!}~tu6kJS4@=}?Em*~Tb$QHm
Ovl;Asnga<uh#Zkn!qY=0@E7i=~MdLP&9`$YA&w^KCT)C%Vn-GFEx0dro<avCc?Xrq{1JBBknFipP~O&)=EeY>)X#IYRhT4Fw0pH
kfL;?19T(IQP)25bhXqv_ut&)frw>->@efvR26aUyWtO$8UL%bBb=~rPeV~AdN7p94RV;dOxqxZq=+q}{G0#;uhzG=_n{4a^}ExP
uqPPyJf(h(&9J#*)0@-B9(QJdFZ2M7O-;?Ej?|;~M6LOPJRzk1yi)^J>u$qn&>D2-$~$e(a-MefNQXp<nRq=6D!Bz&Iku7QXNOzP
Ec8_u#mWpti9yrfID!!6FC+_C4ml^!*gR-nuzQUJY@L|5R&SlK)sPLtjQfE;!^d&ko*>B^ZuQpQ+rF(YD!i?rIV;$=d&(s%El4}7
IQ@S@mc!hVevCs`bRLv&0UyqQU}+Ev#V!JdxDG*!at-)7bS$k{r*W6pz^Mra^8Hj?95%Z=F>zGW%J9IfLV0)k2!_t|X?R09rYhb8
)&840W58yH{cbiD8bG9Mgbt#nl%omPK}w0jU29`Y#FQS|X>&2fBy1JVLeAf=gL`ceDKw`}IqIt1DYcshHKQiI*5YD)*sJ{~23HA-
;}!*$J`sQjysIV8h8BOrhlKlUmuLSrU)V>0c&_cGAERofgL~H?ubC_W6dVj=!JtN!rDuH1aIPFac`2jPojR)B(vIMI5pHX1TTpL<
45=<eo})SqdWcNFPgGJpO^aKG;!K2CoEwC`R$WCckI?$-!lyu5%h%pI!@L{PXX;YXyQgS&nzX9+oxa1(GLEj7ca#Hi$T4~Ep6ac!
@{l*bFZfn#M}69lY05&y(>Z8~5e-x)2U!+N{#@o{fLyRUg!7CJ^$HLT{?F=zMseQVQ4DamYjLztVs-U`q8#$dsS9xAVWX#)hmjpQ
_iFW}w!9%Rk>%f6LQe*37c{nLQV)#l_osSj(~L6H0-AOOYCuVUe`c`LXWW&hk~RxmC-p=N+A;AA95J_e3QI$vwkzU)dc*JSqcAFC
yE7P={A2CpX-U=DP`BI*J!9s2RO$00U0%7q)J9Perhj0vP2Kb(u2gr7XivmW9lA;pL)v5#{{vLVOgQ!YmxZ(UTKM3aoZhV?0@~q;
x3{*9*R<nDWgYEJTf=s-782}OEmTA$MdN-eDmP|PK}d_|NE0xQEiVo&_->6Us}!yyL5461IJJwwXaqWSDEo5*(sO~@N>_^rz5QBF
*-K~g7Qr4=1SmPS{PA{8SdnIT<8FeW!|=hR(Te*Wjnj!d5-bA#(7BoCqA&xJ)<n*-;UC;bb({6F0M(B0HHpmZC+qV7nI3D!A%%#^
CB>%m&)hbTsQ&Ri_JB738HnBcQ2CQ?4hNQFxTR;DFw3vD;p-+O5a>_^Rt1a&-gn=em&Jo5G;Tct)#>^5aU?5I8k_o!e=tGtuGe(3
><;X<=<o0tW3!8#8T|;Z9)wOb157+j5<d%}`p-b17LHr}%wtOE7JS~KSE5dRmcAOe{Tbp}O^K@MR#AHP_DCmyHzN!Y(C7pxj|W>l
JVRh+h3XzSCL$3qq3kN1(qfe($t7d(V$7-)sknm>C8SzM<YnMeY0^Up!YZYSSbo6xZSkM)L6#>>9yus20@P_0x~{Uc*oprY8U%6f
_~AGD)9q&tU{c&{(j}q63jKtru|x<4o2eCQILKi&#cbrSmd#A+Ylj=94eggVE+SaPDC^g?_|LkL+d*36g472j;wykBJ(OJS-$qbx
3_xF|&4whnm$2{2IUiMH`f_Z9C;RugWaCjebKm0j>NJC9!q5K3;iPp%n?6gVL<vD0z9y~IBNEee(u9&Psu%_cN-&pOH0jyRVbY3G
OI`0}vr_V$yxX9dbDp8M08dl7z-etI+HnbcB?A9>e^QdJxHeJCiyR^g#b8rs<E4_DcjOcibb&q<RV&9fY(8p)40c2kzhvg;7XIc<
$h!9FhUQoE#rV2Y?1E~tR~I{cy@n$ce-jK241f!+2K`pAMkD=WNb3T#+tYg}xYLl>2X7E1`=?D&v1svxBQ@_)(b4Ezn=l3c193}I
B(c7EOlRdd|KJ!&rFeDSA)tSubh(e={FBW~HV9q1X6Sqs{8-rSKN_xiWU-)wqI?zNSWk4Qc{?nzL{<a>tt4_N%ugEaz1eQ(iPM3w
hnc6ddJ_twF-=GWQ8MYA&P+a`!@em)r>Y;7n2tx}+BrdKwcV1@3;a+~%9g4zScB<sJz0v+LN=+{RmaKtv|9*%N4ysnl%;LSVr9k|
lureEe*>r__Y3xK7Q9qvbym~EI3f<VqzeUkydaF#`%UQ5Sq$G*@mpnH0X0Sw80yl>&)?-O`N%uCX1TS*E`(426VldF?$b;Kiaath
tTPQ1P#DOG=1sf%Wl9LjO`N&p{g4sG*DhMKF3S-KnVGEyvA9PB)d$_`dnlL9A9&n}E{!w5w*A!!q$A1VPMuNfr(^GM;GH~##6jg|
Jx-SD=LE0ur;w6ts7sVzbaI+Tc=}@F^=EL^|KuIuP{7b7oKtrHC+LLXi8aKzk^^G8>IzICb@S=iJy;Dc)4_HK8s;29)blPtkoqsM
cE63EV|`8^S4VQVi&J(Hn|Sco)6$L$B629A98jxH=*&%KA;sHsm`oAOi+y7tHCd8g-i|U-4-7qt7%SSj&xTSl)Q)o;MNHBqvBFJ6
0E}H@q|ct@R|4g1-!9QyB4_Y<gzjLdP($U=y{*?6oqHG7*iuW(GVHO=BtEE&u&ZHUdVz!`IUJ!ImaEP(fF1gkL!iyta7gprVkKT5
vPWA*`G$nzI0W4kiiF3K+>M-7CO8N+611XN?%@-ZP$dYV%aDMjjruEFhJv1|2=ug)A7*1^fq5ozlxH_;Yyuse?=^t_GCouoC5FM@
Q{;%r_hcJMF?_!Sqt`;3t}AM}00O@nYr~oL>pbF#-xvg!@UK_f_EhUeGNQ~rGY~$F-GgEgHP2qMIu6OJ?nzUq$?#Ir^Y8BX%@Vdj
S5|3_eQdJ$WGyPl*#EVgV9?On$1^Olf9!0IKVKeof~B#EL$tv|pY}uo0HbHvO~*6I)Oe5DuNF!tSxMWwpnOgPyn2n)9QO2rSQ79f
<tTr7$XSEPSK8T|quV_(4-e14@qpXXEfD_58@3`Qx$$2IvJcnt1sIfDMU*6!NZ0Veq4+vq%CtBpW*;NKq6uxX%nv<SYBQqj&zL$v
KvBV7m2J3UU3jLSY!@$-+#bm=m71pYbPJen{imp))XPMx$`d?a)f_7u+lmO*pyAZYJ$dG=ox|P&Yg)k-S@x(=_Jug7TRUK#9#7c{
rV{%XcdaQ^kT6P``22$UVq`?LzyX=m6qwfvJ3X0}J`fT~!I(zKdOJF^3@L_=dY#juv^HUcz;WB-QEL1`4-s=7^Sk&+QhpQ<BbXB;
G2xlbgq80_$_*@yuMyZ^ymF5#tH5Do6Qbr9!@vnOssy73i>h;COpjWj@{}!R1#D@Rs?I*+e?Wv#!nsv4N_}cRTAv697N4UnmroY`
$Zei^ay`b11O&Q5&w6Q6Q0uVCEHHeG$UAUXim@vz5IlgCLhyD>p^P=wzf0476E9v$aO`!|blGG-lV~4vD$yh*Jiq+TI^Gmk;Z$%8
8$)>85DRWWJmQN5w8r9teM)7c+aWOg1TfjMX7wO%jAT}$g~w&is<_|NvisCI(t<`Vg9^NWBHLzO{Q%nxXTBU3ho^~)Yi@yQ5V1qI
6cpfmLlk9-Qt*1&c^>V`DOYN`fEZ+Q?nC8SGWdj)0I_o4#jeN*pS!S&J)lTLr0Pupab|dKvzBOM5V&VeCD^_h^B2{xtA2&&;_z<>
YhOKv$Qg<kCAjt%&J8=3=!qWHAZmRiy<p3uMfK17)X#ZIsVQbx_Q5h#qxE?ZEBB<EHmY<Iqd2xe!qLzJgf$m4k*5Q_{1_0R(nO~#
Qk(go7GPx{8RY{Ozs9)ImLa({7O@;|reg!<=B4tBKDWhpr<H3p-kSG?cX8U1phg)G*B@<EO*^k7-#bX;(gI~aZZaKF6uvZ`4Y-*a
&7V&A=3|s{AJ7_Q`gGyd?FpP?Tsg&}uA;KePyw^07UoxrN3KMHF~n+@YL#g=yi2KM+;w3p*B`X-9;8Vka5YMz{4Y6Rlo~D{+&rrt
qP__cGZSu^O)2krLs8`JbRF_VsmC{rrFQ*Qo>a0`C54X13!i#%a$zFgvzLetv&!WpJ&_D<=IKR<j$eaB2da7L1<ovQaSnBS*6Db8
*zGBgIyP`O8WF<q<NnbkMWuCfWLSFB6XA^$!<HeoFm2WF=^&V<CP1;ANiK!#y>W)Gz(j4=ho$r=f_NxGBHDK7vos}h6ksuz6VgrS
9I&vTx1;|F$h@Y8bp{C<K){_Zt%#PUR$jz_OA{{Kf*R9o`Ic)wu4}w}yQ?!N?D-3SYm+rTpNR*O$zOsKNjRk%A*bVg`z?5jR&q&U
I@JXoP73tAMtaH<Z}Z|g+I(r6`q6Ur#20E#H#97KjS(PC$-Rhp)}t@TB=6_;m3nR|IL6jLyfqc|Fqdd6{(wG$ozd=c5!ce4{%CH8
x<|0Id{>8k%9ZtCli_n(fU>7-37^Lf2GOxrJjBeA9hI{`g47RnV3G;fPXS**gr9rm?r86Y(;tSmz|urRi(wZK5ny`w?HT`#T!t+n
xtYpZuJoQV%nd7OV}3bFBHD8~BQ;P5t}EYTL%nQQ1q<Rpe4lVN1=P^wK2K@vCxj;?SHEsA9#pD7a-3bhc^JE=oOpMe?1IacL5Nc;
ncng9dnXtM3H)(x`|md2syZdy`obxy7vSH}wl=zY8L%~_0{22<$1Va`T@(CXbPiyLhQ-=1Gz6rhU1Hut>=6Pq9m^PW3F=*lsD##Y
N@h^2<I-oTvdipN-6={4zS_~HTe)Pj+O4=s&jTph$vOJ2l1Lh?)|2e}XzIe<TO5T$(H++cVkSVa;IKhv^i}>kcMH=xqhvHfahjHZ
llcS{7s=J8PtInB6*SR&Ba4PjY@ulx2-cF3@*zP6K?O@|Vm1!{O530?T?rK`TO9bsNGc}FN`>K5?)TH8tvhjglhVzv9bV!l76$#K
$njr534wPlupelR3^qzW%FB_kYV%M2;{Mj$2C5z*NU#E<EihW$ZU6_Va)dQs+}jk>6nunOAXt$?x4Ghr57jIU+Z1sRTA9kj?b!#j
rj*(d5sb(M7eqlnOrU>hPjNxuG;;jIwFJul1D{@vEmjK>T*Wd1{pMutA23;NhNx3M^nlb>Qkq5kHBX{^^7sU-(iBO=9uiZ0i21IT
Ep8~}NZaF;a4ac^na4oRf-G@gpbuxs>oMM%M|-BZB*`;6=IcDuwZoD;n>_|C+DqsZ^O_gbg<)HljBHcM0iKHJCOZIiPvWIu0|;^_
%PJe3#LLWj`>8=Ls$IqWQ+B*-_Xs;*U6oGg9Fw2a^W7d7p9xD$O7mLaRAD42{c8fmUT^^%?uDrqHQ7@vrGLMgffiA$7vbk7`IpfA
rC7gWL4c1egL>EVih2|Z$*G3-XphZg9+kklS%;p%nyc|ZdON`jY|jTd?>ou3&L8fmjae3S{joTLrT}3m{P&<SV7+1K6n#uc(sh&z
3Upk7|J4hDeL(qcXt+9!p|$Kh?+YxMhqQR2umz6-NtXv>s}w4)Tkl2hU@O9cw&mwfuywE@Zgxz$G0$JGVYR#Cu@O)eS(jSm2?o`y
U86=&G8R}@5PYUGv6LZJ6G#@e)O;wp>ob*)gs%dRAfB{O*MN+MR3|x(vq48aR;UPe29YU3EJyFrUT>G?@&~4jX!%9WierJtJsGpq
B=;hYkQh)F>iSATw-ak8N~1P%k)%O0q5bY5{%Z(bf?qI~HtM-fx{%`n3L#D%0=_iAc$#GXugw|WCePcX<gqX4Ks#_%hzCu=z^{$B
jyd^ZJAm(bH@M+&`i*DoV2F;osjG2qXKJhm4i{nQNqeQCukV9WPl5TsksxD=hjA%yj9Tk*c5cGywn17jJB`aLflV2TU)ez~b?vJQ
^)+DU^XP0~j&$ifhyfa3@}6?Op{DygRuN;E22pF#Fmo~vzm6ff5fX>euG`wZU{h>YX=Uk&>y_Z)RcmX_st|e^4EDwJQ&HR!$I?=@
1oIbGK72()PPjV}+>|`H3B|J|Sb}@!JlU5dt-*CubnYv86T~i9<<|4a@xl{T5-Gg;2>*ZS$J#qG+_bbr?0cCc(&(tJx^Mpma?)!#
TS#^->Y89FA*b7Q!u17q%>&@$(TFz4L!nSc+eV(%V<UHL<C$YIT?E{qE|G$y(x!tJN_rQ}UM@g=8)d|WUTsU_>aBq~@pYxMk|?mi
yCLVHS2_5o(UpzU04}-u4f8;Mw`MDKWIvt#?8T_Nti3=bd(nU+l&7KUg`8X6%k!HdNZd~NM!c<mZIulIBkG5h>%{$$0+A3csf6qF
%U2u*UbF_|e?sTR(SHOW*$qT2dXUyI>TI35w+ffy7y!*uPw=t6ZSjE;KjSTl&8sAPsddyIoA$xray<>in=5heFA@g~r*u>qKcHpC
<G`0{b0I<q#58K}e~L|zewXfi_gJIOX3oo<jFoc00-voB7-kz3k~67*Vrpk7UWAY>2#4?}B!`^fC#;2ZQ+}A=`MOv@Q*vTEf~MTx
4of}GEnmXXBGVK=y)h@M4Y$=3n!&KeJp*aerOD<~P((jeQhPg#jK>^JW)0Gc70`c=RnIzjcO1Gw!&Pp!bscf0lgy*vcH6(FAu;`J
%!IpqT*t-ui#849es<t_nf&pot(-&%yo^WnF^&qRrF2l92%5>jD?jZSD4<aya;Ef}S<PQWkg0i*TzB$bXPStsOMrQbR73-KS>lLL
x3;L7e4fIQ<5PvL#2W~Efm)l1)Gp-cTfzzS0clj2>7_HDe_Zy_hJr5m8RL=fns~Hl>+G<hPZrkz#eqSlN4c;$Q;4neKf?o=GBSM|
^?2r1e9@w-4LB^@JO`f~VC>oP&J-2QX}&gZj%xe%ind@CN=)+nNl5KU{fo-;W-NYW0NAT-H6yrnIs8AXjw^>hw%Da|u<BI@hE%C)
icR}jpdozRM^0^i&)Db@!O!QxaV4<mQ}|^ozM>;~6expqxY)=lkDc4^NozLMj$hmy&n4dpu?<zdDFx?=0SR%=@ZDOM60zL(ou&W)
i1>PBQ3n#q00G;)0p!C66VrbNvBYQl0ssI200dcD
"""
raw=lzma.decompress(base64.b85decode(''.join(DATA.split())))
assert len(raw)==123364
assert hashlib.sha256(raw).hexdigest()=='fd2d8001be16812a2941203a27a60dfc03a180a4d6f0e2896bf759d05d777b3f'
files=json.loads(raw);out=Path(sys.argv[1] if len(sys.argv)>1 else 'QW49_RECOVERY')
out.mkdir(parents=True,exist_ok=True)
manifest=json.loads(files['SOURCE_MANIFEST49.json'])
for name,text in files.items():
    assert Path(name).name==name and name not in ('.','..')
    data=text.encode();path=out/name
    if name in manifest:
        m=manifest[name];assert len(data)==m['bytes'] and hashlib.sha256(data).hexdigest()==m['sha256']
    if path.exists() and path.read_bytes()!=data:raise FileExistsError(str(path))
    path.write_bytes(data)
print('QW49_SOURCE_CAPSULE_PASS',31,'fd2d8001be16812a2941203a27a60dfc03a180a4d6f0e2896bf759d05d777b3f')
print('Run: cd',str(out),'&& python replay49.py && python verify_diagnostics49.py')
```

Convenience copies: recovery Python (`QW49_RECOVER.py`), sources, exact reports, and captured numerical checkpoints (`QW49_FULL.zip`), and this handoff (`QW49_RESULT.md`).
