# figure-0455

Historical AI scientific report · saved 2026-09-21 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Bright Raven 76 continuation — whole-interface support replacement to C228

## Outcome

No strict own110/additional-weak000 body was found. The strongest durable successor is **`BR76_C228_REPLACE2_G3`**, an exact uniformly-filled H-polytope with

- `V=76, E=114, F=40, C=228`;
- strict `(S,U,H)=(1,2,1)`;
- additional weak `(0,0,0)` and primitive-zero `(0,0,0)`;
- sole stable face `0`, cycle `[0,24,26,22,16,14,5,3]`;
- unstable vertices `[1,25]`;
- sole saddle true edge `[53,55]`;
- **`Qbars=[]` exactly** and exactly one positive physical P bar.

This remains a nonwinner, but it is a much stronger exact continuation seed than the authoritative incoming checkpoint `BR76_A_WHOLEP_CUT31_M61_M95_G3`, which was V116/E174/F60/C348, own121/weak000 with a 33-vertex/31-cut physical packet. :contentReference[oaicite:0]{index=0} The new body reduces the maximal-complexity count by **60 true edges** (`C:348→228`), shrinks the whole dying P component from **33→26 vertices** and the cut from **31→24 edges**, preserves the unique stable region and keeps the entire polar/stable side canceled.

Its actual uniformly-filled volume is approximately `90.03103941097532`, and its actual homogeneous centroid is approximately

`(0.01850761425521118, -0.038335769646674345, -0.028990722374116082)`.

The exact volume and all three exact centroid fractions are generated and byte-pinned by the recovery capsule below. The exact audit uses 148 positive centred tetrahedra and independently checks its raw/centred volume-moment identities within the same exhaustive Fraction implementation.

## Exact whole P/Q landscape

The sole P bar is peak `1` → elder `25`, dying on true edge `[53,55]`. Its exact birth, death and gap fractions are emitted verbatim in `BR76_C228_REPLACE2_CERTIFICATE.json`; the complete relative depth is approximately

`(birth-death)/R² = 0.41504583572435244`.

Against the incoming exact checkpoint's approximately `0.5236152701894085`, this is a **20.7346%** reduction in the complete relative P bar; against A's approximately `0.608565442002`, it is a **31.7993%** reduction. This is a whole radial-H0 comparison, not a local escape surrogate.

Complete strict-upper dying component (26 vertices):

`[0,1,2,3,4,5,6,7,8,9,11,12,13,17,18,19,21,30,31,35,41,43,48,49,53,57]`.

Complete 24-edge cut:

`[[0,24],[2,25],[4,10],[5,14],[6,10],[8,15],[11,20],[12,32],[14,21],[16,31],[17,28],[18,20],[18,38],[22,35],[30,32],[30,36],[41,45],[48,74],[49,51],[49,61],[53,55],[53,70],[57,62],[57,71]]`.

Attaining path:

`[1,0,3,5,21,31,35,48,53,55,26,24,25]`.

There are no positive Q bars. Thus the only remaining Euler-neutral obstruction is one physical U/H packet: one extra U and the saddle edge on which the bar dies. The construction did **not** merely relay the old root while retaining the old interface; the complete component/cut and maximal support structure are substantially smaller.

## Finite mechanism actually used

The useful mechanism was **support pruning followed by finite active-support replacement**, always rebuilding the changed H-polytope and its actual uniform-volume centroid before scoring it.

Starting from the authoritative one-cut checkpoint, a greedy finite support-pruning pass removed 17 input supports with original checkpoint labels

`[46,48,26,33,6,3,2,25,52,12,50,15,43,29,51,56,55]`,

producing exact `BR76_CUT1_DELETE17_G3`, V82/E123/F43/C246, strict121/weak000/zero000, Qbars empty, with a 29-vertex/27-cut P basin and relative P bar ≈`0.499427170565`.

A six-stage active-support replacement then appended, one at a time,

`[25,-75,-88]`, `[-4,-73,-85]`, `[-23,-98,-55]`, `[-24,-70,-84]`, `[-20,-90,-65]`, `[-32,-72,-81]`

(all at denominator 1000), and after each stage discarded rows that were no longer maximal active supports. The resulting exact `BR76_MC6_G3` is V86/E129/F45/C258, strict121/weak000/zero000, Qbars empty, with a 33-vertex/27-cut P basin and relative P bar ≈`0.421672656051`.

Deleting four further active support rows `[2,4,10,5]` yielded exact `BR76_MC6_DEL4_G3`, V78/E117/F41/C234, strict121/weak000/zero000, with a 28-vertex/24-cut packet and relative P bar ≈`0.419746707171`.

Appending `[-6,-93,-67]` and canonicalizing active supports yielded exact `BR76_C228_REPLACE_G3`, V76/E114/F40/C228, strict121/weak000/zero000, 26/24 packet, relative P bar ≈`0.417125753688`. A final replacement with `[5,-71,-93]` gives the promoted `BR76_C228_REPLACE2_G3` above. Relative to A's original 59 active supports, the final body retains exactly **38**, removes **21**, and has exactly two new active supports `[-6,-93,-67]` and `[5,-71,-93]`. The earlier `[31,-61,-95]` checkpoint cut is no longer active in the final body.

This is the substantive new mechanism: **the sole stable chamber survives a large support-complex rewrite while the physical packet contracts dramatically in both combinatorics and depth**. It has not yet annihilated the packet.

## Preserved exact intermediate nonwinners

All were independently exact-audited at their own homogeneous volume centroid by the same Fraction H-poly auditor:

- `BR76_CUT1_DELETE17_G3`: input 701 bytes SHA `d24feaedd2aa292e5fcf0d33e88da590d4002171c63228dac3d3ca178076016e`; report 21314 bytes SHA `6a612c81df31f1339ba8628ffce318d18c9f1a6181653ac60c224af5447125bc`; V82/E123/F43/C246, own121/weak000, component29/cut27.
- `BR76_MC6_G3`: input 720 bytes SHA `b7d1f56ed0e8a6e8cd9a1e7db4fa6a739b48c4559fba9fa40f2d64eff5f679ac`; report 23124 bytes SHA `be3f5950bfb58dba70b16dae084036b8db3aa9027ef0d8b58e12e75811a41ca9`; V86/E129/F45/C258, own121/weak000, component33/cut27.
- `BR76_MC6_DEL4_G3`: input 661 bytes SHA `d461a874ee294dff99a6eebeb5937fbf3cde0b5f86c547e53facec396d29d294`; report 20894 bytes SHA `2b7cb1503ffb036664f9d03713cbd0c87507739af1bb32dec140aa2e5e882398`; V78/E117/F41/C234, own121/weak000, component28/cut24, relative P ≈`0.419746707171`.
- `BR76_C228_REPLACE_G3`: input 650 bytes SHA `d9770f8b9fa58ec9a38f7595490ce998c56103ea8fadb6156304e81df9fd87d5`; report 20262 bytes SHA `aebfa025e83bf7392324b26be4603bf97d9ce2179126e2f8c0c369b23df93110`; V76/E114/F40/C228, own121/weak000, component26/cut24, relative P ≈`0.417125753688`.

The promoted final endpoint is the only one made fully standalone below; the intermediates remain exactly reconstructible from the authoritative incoming checkpoint plus the literal deletion/replacement sequence above.

## Actual finite search boundary — not exclusions

The following were executed and are finite evidence only:

- all 2,211 pairs among 67 previously nominated A-side one-cut S1/U2 directions: no U1;
- 3,000 random triples from the same 67 directions: no U1;
- 3,600 dual-root cap-pair combinations: no U1;
- 1,000,000 random SPD affine Gram metrics on A: minimum observed U count was 2; no affine-orbit exclusion is claimed;
- 45 fixed-endpoint physical bridge trials on `BR76_MC6_G3`, with link counts `12,14,16,18,20`, bulges `0,.05,.12`, twists `0,±.1`: no S1/U1. Several reduced total physical persistence far below the support-replacement route (roughly `0.096–0.17` relative depth) but birthed many S/U/H equilibria. This is useful evidence that **bar destruction and equilibrium consolidation are distinct tasks**;
- 2,200 one-cut nominations from `BR76_MC6_DEL4_G3`: 293 S1/U≤3 candidates, none U1;
- 2,600 one-cut nominations from the first C228 endpoint: 323 S1/U≤3 candidates, none U1.

Environment for the numerical nomination work was CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0. None of these bounded campaigns is a family exclusion or stationarity claim.

## Most useful continuation

`BR76_C228_REPLACE2_G3` is now the preferred compact BR76 seed for whole-interface work. It has only 40 maximal supports and E114, leaving **65 support slots** under the sufficient `F≤105 ⇒ E≤309` bound and **196 true-edge slots** below E310.

The next mechanism should target the **joint annihilation of the remaining U/H packet**, not merely the death edge. The bridge experiments show that a coordinated physical chain can destroy much of the radial persistence but creates many roots; the support-replacement mechanism shows those roots can subsequently be consolidated while keeping S1/Qbars-empty. A promising next stage is therefore:

1. introduce a finite multi-carrier/bridge change spanning several exits of the 26/24 component, allowing temporary U/H births and root exchange;
2. use active-support replacement/pruning plus actual-mass recomputation to reconsolidate to S1 while driving the physical root count toward one;
3. audit every accepted endpoint with the complete P/Q landscape, not a local hinge or fixed witness tree.

No new rigorous global obstruction was proved this turn. The observed support-replacement “packet floor” is finite evidence only.

## Durable standalone recovery capsule

The final endpoint is fully self-contained: the bundle below losslessly embeds both the complete exact H-poly auditor and the complete recovery/verifier with all 40 literal H rows. It has no dependency on prior sandbox files or Library state.

- bundle `RECOVER_BR76_C228_BUNDLE.py`: 7887 bytes, SHA-256 `21da8135f05139c0ec95dcb1adc83e3a48a8ee69a469fac2fe7507350109078a`;
- embedded `exact_hpoly.py`: 8946 bytes, SHA `54e4c8f2f6f1b45955f42b6518c4a1586d94cccc8f4dfe3ae866cf5b22f3aca6`;
- embedded `RECOVER_BR76_C228.py`: 3608 bytes, SHA `ad50624425961466c63930d8dd1527ae8ef965d5f4d5d12dfb59556b69bb752c`;
- generated input: 649 bytes, SHA `9f1e49535bcf15ad97c0f83600447de6f4293527449abd55e2e64b51c7053d37`;
- generated exact report: 19993 bytes, SHA `a2e5473cd22942fc747fd6b346587c5d17155ed70a9cdcc6cb67aee8f187f6b1`;
- generated exact certificate: 17021 bytes, SHA `f0f697e6f46d2352699ad106aecc4f7278ff56d25f7f4379e00df714820a706f`.

Run:

`python -B -S RECOVER_BR76_C228_BUNDLE.py BR76_C228_REPLAY`

Observed terminal markers:

`BR76_C228_REPLACE2_EXACT121_WHOLE_P_BASIN_PASS`

and

`BR76_C228_BUNDLE_SOURCE_ONLY_PASS2`.

```python
#!/usr/bin/env python3
"""Self-contained source-only bundle for BR76_C228_REPLACE2_G3."""
import base64,hashlib,json,subprocess,sys,zlib
from pathlib import Path
PAYLOAD=(
    'c-pl)3vb&v(tkzU1wKnD?O2lK=dwVW$91vWHk)S;t{~{;Scxq;lI++i`rp5qAtg(;TkPH9wunUzhr@YuNNK;l3D>TlJJUrn+q4#&H^Vo-{&Kv`(qk`*kHdJS'
    'EH?QxiOsKZG+!iXu0(m5=1DTk*khK&Z0_b$mTfXNb+hR#^1jBCG?^=t6sSf?oGEhJg#;*Wrd$+A%h)GU1yULYOF#S?e~p81q6A5<y3EstX_zn5Sjm=ib$zr^'
    'CP}KS*+z+C<uzImiY8{bK~S5KFBh{=UBCU=oNVbGn$!H*ocVGF-F$b>Q7-1-3|FH1X_95N1ypye+ehBmu$wOYKufooY_$>A7NbnIbcE?*R1ytB(hT!UqC!_<'
    'F@#IR=PXav^;Uz}YsJfXn7VnAYDzRw)~z6nlX(;)gmYa9XIZFB8s932-;cl5(7rdMa5Fc{qRB>GXWH;<tiXRj(VflI^}F^~7dR?8XaEb5pEq`p`46yPLib7H'
    '7N9thi)YDf6`E?Sv)Ev<$%2A~GmiQx;99xV8RzYS@~0#Y#lWx139QQ%HDK^hW6Ejjg4m5rNtd%w@srtd4sM)=i<#?(f#PkHbec(?rWu#>3Sw*L5r`oJC(fgG'
    'e5Sli!!%UV<Rw#LCmJc?^D<hwvoOwQ8!{UZk%oh{3<f`@h7-fw7erlMXRdC*pUGo=<QmX5pld+a7`Y~NP3W4?HKhjDJUCKSz&ZkO6ENXvXiXK!2#78qZw17V'
    '5W~=<AZHsvLDwtzI#Mw73QZj;AVilCT`wuTZYdZ>Q>;T2h^B;WDImlU5Upl$^+G*cvonpsb0eRx@GN3}8AQ1nxVc-{9~_lOv4D*m6}N5J+K4Q{$0B0q?m`7j'
    'mTDULUyA-GrXgCxwnvb!GDvtx6kOVk0|iW{;;8nHcM7Xh5>-}!82MqQP<8{)R>0X|9iR$HGYe%#%-lT6CYvaJP(qlpQKs%}k}bfyl(@B4ena<(1?5%7zkL@?'
    '<PXRphh++G`N`Zv*^sW9y75D(mh5TFEHr}uEw~IA92^5BNGCQcJ9@QaKnHlxwzDC87D|*++zkCB&ZBr4)`l^V(Vb(q(0+pmjEUnI`6YISt8Bcmxh^K%0XJzL'
    '2I?x4t4KW~`*&5<;<m90mASi)=I#vA^+IeFKvOCP6z2%5+M`Jp=GfTkER7g35z1^93hh)hGXW(>gd4F%9rcb<WFZzuvA)-&Ms_FY3TB0%U>uf#jUvkxF9gFa'
    'A=)MHVE7Sv$07m8$k5=BR6wba8<*rGbyB5(EqAd9<3LR#O$b^5CRv$(gh!z#hHG%kJPqgJP>GWil$R;V1myE05F;nD;EW45R<6vgzE<R7TVJ}<s=A6nx#T7#'
    'Q{zcw+ca|$u}N0fA8|=K6l5ovy`?2B?#3Gx^W{;l{UY~){3l)>XW-WwQ(+^BrF;#xib@554nrjj9zZr167Rx|(w7K#G>or$AihNTRD>=VCx1!G02Z{6h(lVc'
    '1!2S<|5gwR*)?WV_4mpNJdW)D6OBiE&!1kw(Tw4Cb(ySWz`Saj&Bwq*Wnwrhr@k|Wsf+TSkamHm^E6FTRc-hQ>|n8*k|vtyol%x8L3u!niOEIgCG`~%x@Dx)'
    'G3nCZ__HF{A&&Bpx{Ikm5o5JD{GoSLwBrVk5Q@XG@F(dpm4HKN$dZ>Bj7X$P)>>eWd8TSRQ3z_85E(INXOxy?9uG&b@YuDBaPl+)cqPEq_Pll*__Qft_A6~i'
    'e7;f@7(BLMvtNe58v3l~2FPxMfi}K94ROXwY&}nGRZNhge6K8;<s9}fTyW%X_&Ce$(IO339Mkd0U#2|Ex5zKk2=<&Ch=Uz@<26xPi8z<bjbXY?5&8>9n%bTQ'
    'VH(gMdMOlR^+BnNcnt}LV%Fc(5&TV|!g#F_%M7`NKNhbK>eSzW2BmT<X@?(3IwLB9`S@=9Bpl{RurMB)c0H;vfr}Cgt9_5T8pDPU4UNUxZ|xy!6=uSg_;wa$'
    'P?TXF&A|Hss1I#Tt2-gBTpSGi4HH;zacwB(;bF+0VQa&pf~YZZ2kyo0!07}lcVi#Bo=ptBYj2kmp;V|5)FXyIagm%yAE`kRtBwBPLWej7oLDUUsrm8kAK;cu'
    '{lq@9KguYE9Vf<AxQcRVHjKY91f?o`(m@IDDlrUV7h#tTi<k*&0TXPaB@3Yt`_}$G%5v9#;-Fjs7ye1Wii1X+Agx8RP<OQbSh#9rH<9QNe`u*kO%N~C^SED3'
    'ATGGnr$Xu#7WCn<4_jcGM1ja(Ng6>Ps(V>xG%3SDDFoSkITNY9I9yz)ZEbYVReZAYM;iflJ>&Ts;g4vH;Q@)nR-rTL_Dy{^dmZ#|;il+gkK*?&ly3GY2>A9?'
    'SXe#?s-8sbzvV#y+@tdD8J%O%V)EP!Q&|v5Sqh!12Nu-odOmyC9tpkjv*Yfl&@D&$_n;n~b&jB5A6<fXfwMyrkQmxF6%~F4eu<_?!5E7qi>Ua^VV?lgWRUc+'
    'bSeGy%#hYF_RLY)uU!^-ETV8lxvKjODfn_6xi*7ekAD5XrOY!!Xwnd>G=8Ydx}pru&uGJdiCk?n_$M)Bi6+adG_qy&N}FJj_v{gzIL8+%7UxY-mey5CrLH7p'
    '*OtZ|YAR3VQ^cAU3HBBX=X?6SrY8M<peFskhLE-(evw<dS_th_%a>IL&R_<yxS#}giQco2=d4OVOX_g`c+2U6hga_cvJ3;9m-h@=RzH)#7%#3AhPQ>sM%qqk'
    'L}+xEFudQxlEsOL)~zryiB@Z0E)|Qr&uEe)IXQUDrUW?__K3mHQTBSezZ{cu73m%)i!P@7YHmHWp=gDY+W%Zh*X5bvr&`)a+spsk*};m}WuyQC`GXY;R*+3N'
    'IRXx0{}|$iw1=TWKvW~(=Ab$(6CZh{_@!X7M=_gM)z8XywGNH}YtG_1FHFI(F=unpfKhGqz~lI6K5xeJqj+A#_CqzaXF8{oEEy@*5V`EmHJGIxKa6HZ1qq>X'
    'vpPp06`==m3Qw8o8VNgRGed)23DN5zlQX@U10En0RyY2+)jt&G9D_FPpBerj=3jg)_}7o8GS9GS;jPjV5CxiDT)<2ef10F$x@4<r1f7s!mTakw-peMq$0;>e'
    '*bKs1?(&njr%mJNeVKR>ST&Hm7&<{Q-@oH0;>z+=c27lDJvlmUzCU^o?uPTXoOy1Vsb8vWc~P2AWyr4CTH7l5i#?h}@zZu+|4$ErU&H~Bh-^1h(#;phe(VdR'
    'MGa42)e3Xrrd(8^RXR{VgNZUR0w~%jS>`pyP`VU63R2rnB_T>Km;`J7!lR*RaeRoTJ&L$!)h9|-M|J66n3P{05lKAu6mIy;oqK_+ybjgoD^?A!c)9%wF036W'
    'Zn$KY(erWt<l%De9k^|hqpGmmnA8Gk#AeN+sr^<T^tOW@R^+fYoC4|;y(EqK?ySNGaqt~~+2euWFGH|IVch@%PR04WAi}~~5T?A~jbU;VCwNB7ak`~PN|2^P'
    'w*b6o?7>}Z2b(XNwxc4nm}hf$FEoH30b6+N8DvG5ztk8#|JvS&<Eag=UntL%2Nm?UYwayQZnY*pKG3PQxcppr@`whbdI^0lpw|GcUB=M80EAtJ)o?Ojz?n79'
    'vtxe=MID{!U4Oc*^?=7(tUB8%>KEpr_cNmCh%-;ct#;!9i30_6RGPQrfkM|8DxlysF?8^P7<8KRZv;b&HSF&re~NJ!a6D2UiYqyO;C7*yc>xJB+#jxFl8Q(N'
    '=oB8WQaOk$YQJ#xvFvDMhTXjKj)eLFIq5$+oueWlcX6irvA{m6m@-f((qy>9ykIkg*spRLLK@gIYwuo_x_RzKF<yu-fMMt=@3=6J;)VGOoZu9+1qn&Pq^u%W'
    'd4F+@x0$nLfHMU;^01R<X0zl4WZAh_s-@QNI~T5h*DTRwU*}vXT`mjo?b&ox03Yo`r7BqjZ*{8PH^eKR@1y5uKCVFRLvHx|ObQ}2(o(}N?q!hd0sfc#`I!#f'
    'ZSAmgic2EN_0s;aXRc~1;m>$w^Cj?INV?j~T@ZX@dq1OA+5Z{qRmA;qp^_!Ovp~-1y#+2=umdH?lJ2`eto_-<T>T;lLA&{PH|>|Hs<=BPe`gpp5&%t&5%pbq'
    'yP5k}C0M$%%60Zo0n(L(nbP|Z9Aff%lP<jFJ$JCZ$3{9%?Mk<Hp}f*6r|`;+YI$#2dmBe`#x9)n@jY4V0glNH>^7i^i5JUUyoo7aLa{skiJkM0?1KNnPPuXP'
    'k%^iVvIy-JOl%}fY%?~)GE|J+%fWj&dXK{>HSH4)?pd5RE+(%YXr~lytvnVBE8>ej9NwOmHC9~q^YK`|Cg0Y53y~=n;$nhrUon*}g5?<($3!O7yPp{eZiCFO'
    'Hw*bSTgI|^%Q8r|cuD?&WOgL{{#tZP#QR%0F46BluuI&>Ic)8JQRCSoi1QF8^Ds|0d}r6ZWPmC*OPcXR#J`|cU|VkiN0pnhQ(Vb7Im~mXVUW6HW4up+6OEfb'
    'L4nga|8jDA<9xXM{O7-&o2%P%=i>b2=Jx9R+WCC{$@zG4eeGP_{`sf#@%;3|$*12>uboSPH8lL-10vsX(2*Pm4kL~;hYi7T8W{QLXdFK_Y0VNhP?H7T>TRH$'
    'P9Iidyo(y8yz&+pX2`c81roj#q4~jbzED$Er(oEu@dECP;ov|Go6)w%vJiq7-x_CJZ7}#ZY)~kG2gXpW7UVMZ+tV<u-_VJGV2wNYJBPmu_&bF^c^YHlti>92'
    'X9j?9UT73<3QeJ0C_`}dH|)*T`RV7o^DF25Rj=!u8b<%;U+sK-ga6Ly{dATrQ$K7b@oWR(>?ic95ZNwiIalYGf1aG48_vJX*4Ow7KUPR#Q?Gv{q^Q>)PLxFy'
    '$M`)&2)ly@k1Ps8C7(jV&HOZ4<S_sAlGsqpmTtBzyz-3$H-&mJ@=_PpMowA<kL4Fe@=GG|eG!=HKl!8xvntFjP%fb>M=Bx|qvSMrGw?MQP77l3hSdo>et%+2'
    'x)a^&SOd$NbPTU+>3zTB>Q=uS3_3pi*PnEPNocxZzuWaEmS-3f)AikM<7@o;r_0+LL2WS6!_L4mEzh6mmKzLuetXh4yX|(T(+k2b&>onU(d%>ut`}HVXoTI4'
    'XX$>gZJB}D18QKC&sUP1YlK#(XZnF*3_8Zd?{#{UpzE2PuGR1PR-pHEpb_-i?!XUxzw3M5o*Rb!iQex`x}FZ?&Q5Ml__x}35ktM*ZZqMw!^S~x08gY(B8KB}'
    'vp=wyZdj~oST=*M)n&THx&!QV2OWSLZD#az?05QoW)21b>zUZM+FjN(EsL4`E{#L8Y4#1)(Fxz|w^_5JL*FENhGjs%(`B7r8~Zwpce(&Gb%Vxr6UMC$jQ43A'
    '$2wiT?6;xW1)65NLw&u2;}(q5`p{~2dWcT!nb7L=f!hIbV<52}EZ#+8y55s>P3l_MwFV4K2wlSj$vP&m*Tzwh7rH>e>?38<#BLjuVfL^)fUXJanr#%r><vIm'
    's3aWhpl;2M&W!$mx*gU>o^(_<>H^ptfP$&pYa_RPW>_c>O0IW6M7@LR>hybH8o(ePtTx)L3%G5>wLr@{SgL7R)ax*k$RJeHz!o4_qT6Ky9U!Pf%QA^sYIkWZ'
    'i;?;)WCoVA4C=rT7}n~Mo>>z`?qUbH0Lh_m+faF*e*Sogm&+h7Gg*g$C$S#uvjNjV7T~~Spm)8`P-avZ10$JW1TYog_gQDafFoE2Xx-kxb`H*mycvxA6U1uM'
    'qB;V*q6gG0vMA^RpRhFY3_38-@Ol>(!DkO_fX}|f1N)J20UzfhGlqPU`hh1}v(I|C8nUK~XICdZGNEjfkvoIFyFynC!UY7lJh}P6$2tRgpa>LK$l50n0n!E8'
    'P%ilm+|*S)ZCDg%GIO>74DJ9Ut!cOpBG}7wb?1vf<$v@^Anw~L9>jOk$iExKQGL4Ln3q+@nLv&1I9dxo#GuVzZPa&~M*Z~(iaTAj($EbYZ<AAX%6XZ)1uia5'
    '^r1m_WUcvA5T#g)W0fOz_izoBnv*<HuecELcx7A1H2Jq`f>s#&Nf4_0uO1`366tmZbSy*O2~chh0w38trqyKKV83m&kPjsNl16zbMTN<-5|`Bu&XJ&`#(Me>'
    '`A(2ceJ~i9CFca%ZbUz3-4RF!B}lybTI1cisa`PIHs@nVzL>H*5YrHewdrvDlNA*rV*1c+Vi*Rf!a}fkX;pxCDy}WUK4C1r1wuKysL6}<ta3ya=QJRLe2=6!'
    'Ff?o+NXudzLo@@|AR?wc)84ZLOrv7IVWUNg)&3G7ULKzxxI`>Vds?PO?qS?0OMRS+X_pA%z*2y2ZwknQZo@dod?Y{V;oEN}FBq&>)~Hy4E0@JLl^5!29NAja'
    'A4hxFEoSwo2_%XmSb3pwW$?MXR`)OBFY(LGaK<kxDgg<{jR$uD3>;q>lFJZp?~0=NU@b$Z6y4CB`wyT0Ja;ag_b1oCe-cL#sM#Gjwm7Fy=hQuqRZsrqdll(*'
    'vZ5bKXWFam%Yhvt<V-`nCzl<Ej+2dH-Cfw$^M=CjSm|-Y(%<UD<xv7D$);U7Rt#(Q1Ac#U&?DrZBJ3=U=AlVjJ3;Xn;%5{<K#bBh1Tc*?F1JU}#t^-dKuhf0'
    '-e8-2afqJCr0WmIw!E_QYl#o7|KH?3N@Rz8<@EgO=J$)=Pfu>nWk#zdG`~n_;!udokIMsFZKy$6zrp0Tz~pX#-$c={$eLn2k>g2a92pU#z8v-G|3>)Hv03cH'
    'l~eNmnOJV?2li<=XMX>G!^wUf'
)
MANIFEST={
    'exact_hpoly.py':(8946,'54e4c8f2f6f1b45955f42b6518c4a1586d94cccc8f4dfe3ae866cf5b22f3aca6'),
    'RECOVER_BR76_C228.py':(3608,'ad50624425961466c63930d8dd1527ae8ef965d5f4d5d12dfb59556b69bb752c'),
}
def sha(b):return hashlib.sha256(b).hexdigest()
def main(out='BR76_C228_BUNDLE'):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    data=json.loads(zlib.decompress(base64.b85decode(PAYLOAD)).decode())
    assert set(data)==set(MANIFEST)
    for n,t in data.items():
        b=t.encode(); size,h=MANIFEST[n];assert len(b)==size and sha(b)==h
        (out/n).write_bytes(b)
    subprocess.check_call([sys.executable,'-B','-S','RECOVER_BR76_C228.py','EXACT_OUT'],cwd=out)
    print('BR76_C228_BUNDLE_SOURCE_ONLY_PASS2')
if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else 'BR76_C228_BUNDLE')

```

## Evidence tier / limits

The final body has one exhaustive exact rational H-polytope maximal-complex/mechanics implementation with exact mass identities; it is not independently double-audited. The support-replacement searches only nominated rational geometries. Every promoted V/E/F/C, strict/weak census, mass value and complete P/Q basin statement comes from the exact replay. No finite failure above is upgraded to an exclusion. Canonical accepted own110 remains C622.
