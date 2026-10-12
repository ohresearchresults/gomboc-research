# figure-0536

AI research report · 2026-09-24 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# COMET65 continuation closeout: no verified successor; exact raw entrances preserved

## Disposition

**No strict own110/weak000 body with E≤249 was established in this continuation. No post-COMET65 geometric successor is promoted.**

The interrupted continuation left no inspectable post-parent candidate, completed search trace, changed construction source, or successor audit in the available execution state. I cannot substantiate a finite surgery from that interval. This is an execution-evidence limitation, not a negative mathematical result about the permitted geometry.

During closeout I recovered the literal COMET65 source, reran its tetrahedron/cube/closed-weak/false-weak controls, and completed fresh full exact audits of **COMPACT_G6** and **FAST_WHOLE_G7**. All six parent input/audit/summary byte receipts matched. I also constructed exact active-only H descriptions and verified that removing the inactive rows leaves the entire body, maximal facets, and true edges unchanged. The resulting carrier index is supplied below. These are recovery and representation checks on existing bodies—not new physical constructions or an independent second hull implementation.

The strongest reconstructible construction remains the COMET65 parent, whose two selected mass-normalized bodies are own121, not own110. Its finite senior-carrier replacement transfers the root rather than annihilating it.

## Source and context receipt

The current journal was read through EOF: **1175 lines, 275597 bytes**, SHA-256 `63cda4372af3e6645b2f663af7f302f2e38455231754ce461ad3b7874c4917f4`. Earlier unchanged source evidence remains identified by the preceding literal results; it is not credited as newly executed research.

Required parent: `figure-0533`, advertised immutable SHA-256 `6aa21ca52fdb0068aa59d800caf2fa2e36ead25a908f543a7b5e31e353c596a8`.

An outer-serialization limitation remains: the current journal's rendered parent span, from its `# COMET65: lower-edge...` heading through EOF, is 50541 bytes with SHA-256 `3178e1aa3c96f49b2738ad8006d36d47d443dbd3d81bf9b3d24dcabc12c3e2f1`, rather than the advertised immutable-result digest. I do not identify those serializations. The inner executable capsule **does match byte-for-byte**: `COMET65_RECOVERY.py`, 31215 bytes, SHA-256 `71c9dd01716002444939609be61cac7532fe5a5ba283d124b43525e9afb34d00`. It decodes the stated fifteen-unit, 91978-byte dictionary with SHA-256 `57191f83eb4c225d16b0f07c793e9d1943f0391e5972ef6da650bd530ea3f2ae`. Both freshly reproduced raw audits match the parent's receipts, so no coordinate or mechanical disagreement was found for these entrances.

There is no missing exact dependency for continuing from the two raw bodies in this handoff. What is missing is a substantiated **post-parent research result**, not their geometry or auditor.

## Freshly observed exact checkpoint state

All values in this section refer to the **raw bodies at their own uniformly filled volume centroids**, not to the mass-normalized counterparts.

| Body | Maximal V/E/F | C | Strict S/U/H | Additional weak | Primitive zeros | Positive P/Q | Remaining true-edge budget |
|---|---:|---:|---:|---:|---:|---:|---:|
| COMPACT_G6 | 92/138/48 | 276 | 1/2/1 | 0/0/0 | 0/0/0 | 1/0 | 111 |
| FAST_WHOLE_G7 | 130/195/67 | 390 | 1/2/1 | 0/0/0 | 0/0/0 | 1/0 | 54 |

Their closed-equilibrium sets equal their strict sets because there are no additional weak equilibria. The complete audit retains every vertex outgoing test, every facet-foot side test, and the four mixed-edge conditions. No positive bar is suppressed by a tolerance.

**COMPACT_G6 actual mass**, approximately:

```text
V = 2.046321411885632
M = (-0.12467126124556197, -0.036785821617103885, 0.1192196809380044)
g = (-0.0609245744688175, -0.017976560966151797, 0.05826048647369944)
```

**FAST_WHOLE_G7 actual mass**, approximately:

```text
V = 1.9646089693546063
M = (-0.16126667563778715, -0.027420680148476564, 0.14546608999900723)
g = (-0.08208588994214196, -0.013957322080986188, 0.07404327897718714)
```

These decimals are displays only. The self-contained source below reconstructs and emits the complete rational volume, first moments, centroid, vertices, planes, and all mechanical tests. COMPACT_G6 retains the useful 60/61-bit maximum vertex numerator/denominator complexity reported by its parent; it does not require the 20536-bit mass-normalized coordinates for further construction.

### Complete raw COMPACT_G6 positive interface

```text
S = [1]
U = [7,78]
H = [[34,36]]
closedS = [1]
closedU = [7,78]
closedH = [[34,36]]
stable polygon = [0,61,57,53,31,1]
peak = 78
elder = 7
component = [36,37,40,44,53,57,61,64,65,67,70,71,72,74,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91]
cut = [[0,61],[2,65],[4,70],[5,74],[6,75],[9,77],[12,85],[14,86],[16,90],[17,83],[19,79],[21,81],[21,84],[31,53],[34,36],[35,36],[37,62],[40,66],[66,87],[76,79]]
attaining_path = [78,80,71,64,44,40,37,36,34,33,32,30,28,27,25,24,23,3,7]
birth approximately 1.6345979340731003
death approximately 0.8862271891435458
relative depth approximately 0.4578316963026865
Q positive interfaces = []
```

### Complete raw FAST_WHOLE_G7 positive interface

```text
S = [0]
U = [7,95]
H = [[37,38]]
closedS = [0]
closedU = [7,95]
closedH = [[37,38]]
stable polygon = [0,1,71,67,60,54,30]
peak = 95
elder = 7
component = [38,39,40,41,44,45,54,60,61,63,66,67,69,71,73,74,75,78,79,81,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129]
cut = [[1,71],[3,75],[4,81],[5,84],[6,91],[9,96],[10,106],[12,110],[13,114],[15,120],[17,124],[18,113],[30,54],[35,38],[37,38],[40,72],[44,76],[62,107],[76,123],[103,107]]
attaining_path = [95,86,79,78,75,71,67,60,54,45,44,41,39,38,37,36,33,32,31,28,26,25,24,23,2,7]
birth approximately 1.475832211150304
death approximately 0.8485892582935802
relative depth approximately 0.42500966445761024
Q positive interfaces = []
```

**Raw FAST's stable facet is 0, not the normalized MASS_FAST65 facet 3.** The polygon is the corresponding stable carrier; canonical plane ordering changes under normalization. Likewise, the raw relative depths above are not numerically identical to those of the rational, slightly anisotropic normalized bodies. The latter's values and labels remain as stated in the parent, not substituted into these raw audits.

For exact recovery of either bar, use the emitted rational centred coordinates X_i=v_i−g. Birth is X_peak·X_peak. On the stated saddle edge a–b, put A=X_a·X_a, B=X_a·X_b, C=X_b·X_b; death is `(A*C-B*B)/(A+C-2*B)`. The source independently verifies that death is the maximum cut weight and the minimum weight on the attaining path.

## Executed representation improvement: active supports and current carrier indices

The original raw input files contain **60** and **78** rows, although only **48** and **67** support maximal facets. I reconstructed each active-only intersection exactly and verified identical rational extreme-point lists, canonical maximal faces, and true edges. Thus the active files are the same physical bodies—not successors with improved geometry.

After this explicit pruning, COMPACT permits 37 additional supporting rows under the sufficient `F≤85 ⇒ E≤249` bound; FAST permits 18. Without pruning, counting all input rows would give only 25 and 7 automatically safe additions, since inactive rows may reactivate after motion. These are combinatorial allowances, not guarantees of mechanical feasibility.

The following maps are freshly computed. “Original row” means the original raw input ordering in the included literal arrays. “Active row” means the zero-based ordering after the verified deletion of inactive rows.

| Body and carrier | Geometric label | Original H rows | Active H rows |
|---|---|---|---|
| COMPACT elder star | U7, neighbours [3,6,8] | [6,15,55] | [4,11,43] |
| COMPACT junior star | U78, neighbours [72,80,82] | [26,35,36] | [17,24,25] |
| COMPACT saddle | edge [34,36] | [10,59] | [8,47] |
| COMPACT stable face | facet 1 | [1] | [1] |
| FAST elder star | U7, neighbours [2,6,8] | [4,11,43] | [4,11,43] |
| FAST junior star | U95, neighbours [86,101,108] | [17,25,64] | [17,25,57] |
| FAST saddle | edge [37,38] | [21,48] | [21,48] |
| FAST stable face | facet 0 | [1] | [1] |

Accordingly, a concrete **candidate carrier block for investigation**, not a sufficiency theorem, is COMPACT active rows `[8,17,24,25,47]`, with stable row1 retained or released deliberately. FAST's analogous active block is `[17,21,25,48,57]`, again with stable row1 optional. These blocks identify the current root and saddle carriers; they do not encompass or cancel the entire P component by definition.

The parent's nonsimple controls remain valuable: uniform WHOLE30_SEED is a genuine 151/227/78 body with a degree-four contact, while the old floating active-triple mapper duplicates a point there. That is an implementation limitation, not a geometric exclusion. Those controls and their many real positive bars remain preserved by the full literal parent; they were not newly reaudited in this closeout.

## What remains unresolved

No new finite root cancellation, actual-mass compensation construction, contact-preserving deformation, or scoped impossibility theorem was completed beyond the parent. No finite-search count or optimizer success is credited to the interrupted interval.

The continuation target remains simultaneous cancellation of the last positive P bar and preservation or recovery of S1 at the actual filled centroid. The primary raw entrance is COMPACT_G6 because of its 111-edge reserve and simpler arithmetic; FAST is a distinct shallower-bar alternative. Historical mass normalization is unnecessary for the original goal and is not a cancellation mechanism. The parent's normalization was a real affine remodelling followed by full exact re-audit, not evaluation at an assigned centre.

For a nonsimple continuation, deduplicating coincident active-triple intersections is necessary but not by itself a valid differential model: all incident supporting planes must remain concurrent when a contact is claimed to be preserved. No such new feasible contact deformation is certified here. The exact active-only inputs and carrier maps remove an avoidable representation ambiguity and provide an executable starting point without repeating historical recovery work.

## Self-contained recovery capsule

This capsule contains **four complete units**: the unchanged full parent exact auditor, the unchanged exact H reconstructor, both complete literal rational inputs, and the actually executed closeout/pruning verifier. It has no external source dependency. It reconstructs two **existing** COMET65 bodies and their active-only representations; it does not encode a new successor or the entire eighteen-body historical ledger.

Decoded dictionary: **30386 bytes**, SHA-256 `a129c2e5370305465105a4adb5b56ad152f6d5f517504853800ffc05a85e231b`.

Observed environment: **CPython 3.13.5, standard library only**. No numerical libraries, random seeds, or optimizer replay are required. The six expected parent receipts are embedded in `closeout.py`. The inherited `exact65.py` preserves its historical COMET64 ancestry metadata so the old receipts remain byte-identical; the new closeout index separately identifies the required COMET65 parent.

Save the following as `COMET65_CLOSEOUT_RECOVERY.py`:

```python
import base64,hashlib,json,lzma
from pathlib import Path
DATA="""{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;C8Vt^j!cwh=^wd9I>w0ujlNmuKlM#IP>Of98SE0WE=G++>zi^azoF+s2bgYJ?vP{9mnzhnmNhPAsa
LdvO~FrfG4lH-<%Q5B3j3b@^JO9eyB7^7xot3d&}3jsmuuL(D6p7LYI#W&QYI@-e=4ub6h$F6)>m>_oEy_1n&|GvuC1Os$qk;m+o7?Cv5ha3
i(0$5OARD*{ZiNz#x2{?H}~~5wA8VpSy^RuTE(~i^x4PB$D9`BSu~e{q9xAgKrlGd&T0H*jpz@)Qv@Ak6GCZm}|`C&Vlws=aq10eErGk)m;U
FR>Gkz&G5RDi`fZkLYVQhcF5g2{Fw+oPZGIt9!faUcUstW%QL@m;+}|;oJajgcmt&XDv`@=c~b|`U>p2a{Mt&Dy|8nP&+{v7FY3i0MU*aM+N
}UpCK}&Z&+iIohWxOJ+Y&MVuP9MCdP^r7@In3Zzs%5p5MQAKvy+bFyElBMxe4C3wqgT0Q}%zuz!O2E&wFvpWDAy;CRmmS(UWtq^6Ct`Cd;Sz
6cqp>8ODki!jNSTi&3CR*05z}dHXR|xdvs^8r$30-%b=K#bC=C?7l0(6sB7$s9qCVjKm@}+y@<b5UQ6PvA=}?&#wgqqQNz2$(SK32}K%vM~c
;Ml7p<c>Qf9z!#8uf?(XX61L?(`sP@w#y^L{hjIPUXv$PHNRA35Ea9<-%7W)~FZHlgGj>xeY(l9Hm;$iVKIX>r16Mi|jSr@H<ysvV6n4zNS%
n=hz)cx=Wo-Oc}hs=M_rTf*^yhQTm2EXTl@+o_=0nL0j*sx|$h2lkb5IcJOx}y`s-C)j=Bn+5rnHzwB>ZW&&dum9FZ5`(*is#Z|)NLS2x%NJ
j!O%#V%@m#ndZc@Nb8-Xx>t^?LD}<?i=&F3a2B*SpfI3E;8$}{K+VouQ1h>@LRz4v(r`cW_vEKaRpSDFv#JrEL9la7}1<u{SXEDGjw)>A>kS
z|m4SE$#fqP_EBPZtgo@&O&@)2@2#5mz7T4dJXU4twj(CRM_x&8sN3fOOmQq9Q=WX~;I4}xd|$KT!xH8dy265d_%hn2Xmq})Un=mY4tyLF-a
9?m;Li@CqmTV*I{h;WbG``bUL-$df8*4{=m`I-rEhWC`XwE+QFgo6s+Jn<QOqYAo`DF6+!*D)0opB%MIR-N-mX>!MGWs-B&8_~Vo$yU9E!ub
m5@Yb?sVc`nU$>x|l!}w52KZVYdcosed)Cu+|E?>TTBn-yZKK`;^HS#b-4~3)a7q*Ed0oVvqt&E#Z`d)uDd}(hcXVguKBQ21gtfN)S<SDMGc
A-}NOjD>}?CL0$Ifw&f)v>$P{5WW_)c_8LqpRc81+P;iCw8D|p|06|Rl(&XG6+S4ZsH#r9;+DG6^>;$F6w#6)!@bvRky97+?7%=LKH|$oz@0
!T$e+|PZQxvr{<bNn2NfStphkd%ztZIfvJ!Nc1q9^la!OeO?&8Cnag;Ub*JdAerr`YG_4juge9Sx$Av@EtL3!jbI^G-*FpLQvnhiG24P2*Ta
rQAI9@=4Bx8Dm_Gg25^axThagT%GJswq|HuG+gcc03V=1Io{Nfl#Ggawj|DM)>+QtEseESk<un$1gmPnv!RyS&9)?s0|w$}t&zXuF3XdvTby
YN+^bl~T#5smmSvv_5S8NTF;1Ma3i<n>k8A@9oM=XcTX97B@jFpQ>SN47GAXAtR9T$peQ;mZPnT6u3gSOnVzlrdfO+OiJE~x>G?4Iu7E_8rm
i7JlUDxg!ll<lXly&*U9$XC1)y1-VqQ!rc=j6?c?+9wS%&+;j2!gemzYN*W67;B|vU^DlOJ?W2}7e)MbdFD|Senk(%N+g(`+F#fTfQNb|zfh
*#hhcWH&W^l6qemL`b=hGGG&1%PZowCh|%sK1!z?G6Myxaxxp)C~z#bsQNZ*u{QE1N#o3G8OvH0Z$`w1o8l)&lg~VEQYy5>{Qd4)a7B2Ov-C
f3c+|_pJV5mxJaj;?RbpGC^_Y$@y<FOq#xQNN_@H5*ozC%uW%I#y-xsBt4^r!@xS~7_-B<buKP)c(x4rP{*B`>&Dy<wITp5o0oE!F2fk~=y{
|3=R)c49HQhxWR4ev^p07w@9jPG_7YC1Fjl5~)8DE#m<Q_vJ6Fkjn!>MT}#v~&0s-NR`O%>c5_>Crc&Y7i~v)0P%Y(F3}ZF`{7Vp{aXwJ{VI
=&Hq2jKUHt-wGmQ#H>mgRe3c^9a8XF?wO~rovIQ4Rk4oq2SbrHf9|>J4#X7XsN&|cc2rG=L~>Pz{mBe>U-Al1U!SZ}RSU?mQLSHey{veC15T
s{6PUHv0G)Qzij#x)%$bDA{VboxsPTcBg^aSsQLefnw{&YZAZ+!oq}txZrc8o%hU~cJWg~5$mM*m?O$le}m7e{EGb-uA!HNvkyEhs5+0f3pv
VSwLeWesS>YOG0&9d;GDA=t_-fzxeT;9Y0Zt1whr;YKSq+2z%suzxbfe1FmxzIVgrD!4>(uzp3;$gbj;tVbH)NVMh2CUWt9=*W+yw(qvrAcG
^5u=ijSiJD^RomQ0B#r^MoHXlJ7{W&^5{}=TWDo$bfAVf5x?}LdaH4l`-127rkFfw-ZMs+wyYa<i_h&K8sSpcW^Z|A;bABLLwERn0vDs(NP(
1XE5PdXF1D!3`oDpdGpkF8jA3;NgxsUQRp4Dd3mo2&z;X-oqY3e^ROAoq-<S1#+mMUy|1l6aYy{d<)a}voS(faMJ_C*eIXRD%#vUnS}3H|_D
85wnN+TchX@QA6Aa6W#zNG`hlon#S5{+y(n*o3*?TL}ix!(aphWGe|(EktdT?S}F(-dB|n)z(XqCrdX_s*A#w{wK<z;*W~CIYs38O*1Vls!&
8`V$S8)a+yJ$_%aq`kRm_EaYRBCOA>_UMr^Y7pa~54WLDg_x+WPINEgK{sRLNehRNmj<VJ}|SOdjfzG+|YM5XP1j0l*IGsleHWG)P#;%7g_h
XziTC8d=GFz<_IwR3!jf^w^{2O(M3EUp|%`Q+gPuy3~RbR;Gga~WgZs`A0d08umxht#ft+f$G^)y%rWXunlV&P0wW@)mqGwLGWK#GL>n!jgi
*3p|^~5WPNoXrtH$HGvpwwI&;bh{A96u-hf8X0qe-w4^p>Nhm%mHyqGAlf$ch73`{7s_c2O*YgeE05X@eFh!fI<ys&_!Z(7rEBoyT0=x0V_c
t0!9vuQu2k7%nWEx@W`Gl4dkw6p&f#OLzphxc)a=t%m`|Aql)^lL}h!;CcZnaob0mSq&3GUQ_Vya>r;*Hxlwy6k^m>pj7!+Km&a7DvrNdYt$
Qc&)T`cl6|%a5qrv39#J(LTh+1S7c4PdY;#0#jo-L`UL>!n}EL?bpFhv&3!MGn>VD2DALX%ciULv`hf9Ss^g?;xtdVs2S+GJMp$Ypd2qHVtn
i{^T?=5T~0yA4p{YUP~yt71)e|q&Wpz##sO0&bMI~6>P26G-mhS5k|S0(UH@NWH7N~SMonJdE4Qg}U5HF2);O`ei(O>h=e9mAK6P>vDp%=8(
!E_yw)X#dJH^uW<XhMF@$i)5N6FNvs=H+1ka4*|XFCAyr$c2rY^4Ii(^E*L&^ZMgePp^gG=Y<H(a0n2a`C*Wp2b4bC}2}a@TL2B#mA0+Gl3{
z6v4&Jw)(xgYC@8;c=9r03jkezB2t^_5Z_l514uU1U}&QeP8^SQsZ+A*Nh2{`DwHM~iMw0XEiJOY>21aO+-27e{G2sxweNk4ZqumoXeVM2;S
y_tEaXa1(?Q;b3zvk=<uiSp<7G?%c^p!}re5Y`YcH19Kj>ORP(ohTdp`ud>PT;%sVw=Q#pr+~@2Rp?vQmT2>S-+t3HOjO<yLbXL%KIP0)WVZ
uX~CnTwW0Pis2}(uN=Z0Jnh_<4Od+e=tk<IdGjoC!i+Q9gU@2mNmmxD+~wR_rd)5YohR+q?#M~riUH#fS8)qs@}ln%W+CRz=`apBJH`>D)o?
+6?X_OZ_Oy1LlJ<rCm{c9`A9TEE_)$twM^2eYa*R&p)V@xXeI9x(CdRb~tCez&0$4Yk+N|AL+;@&FM&tS=c*pVrgq-`o_m~)?M)s~0+%VKOI
MD%VzqknyjW~(Vb4$#HS`ZIft|o&5F7ZjFgpdr}Fb9#d%kVNt<_n(4z4bA1b3Gr&bC8`Zs};&tnpzi;DajGMq&_ZcRB=-tq(LV>>IjR*O1H<
8td$xX>KGk#oJ>~i=N~sKivI^*LDYeg42|LLD(hs@P~=kUvS80Oe#|tC7&RJM*?GMB$8s`f5^(<m0vUmreSrn}@z!>V@#&y3&IMo0(=}?kO(
El^-*cv0NZE?#?;t2AWZ4YOPS@>K=_xVwU)r%tiR}k1e(Hm3+>Ag|T?5IQ`cbvhlEd=+z@=HkKH~J}9<YNm<3p<ZL$vOfqFkUmiF=+9U_ndV
n!>^N!H}d9`iH9R-w)~RxLQ%=|CMYL=VGWiTo^JQaak(g=Eh3MVyUvU9Ksv5n4%W@p((lMxW`59jxY!beOM^f^#_m`1SV9)8+{&japt)Ru<Q
)?-_hmcaSgdhwy)e*MmKoAHmY@_FSm5Zy|G!MM~Q&(i<a&5hJXYkVdfJozZ;ojKA&_JR+>XiJr01Q=qwT~mXqW=xV&Fs6d^gr4bK?@ebIw!G
?OFV(|(^k$SZt;w6!vA9KG7gN;4kwZ0|hZzeL)TFj9j3!3BCuV%+1LJwlIAz8QBlHiZ6^Yb;tyn74{S24ke%Wws$LBR^C|q{AhCTYbVQeod3
qCmv*l9`l<Zrnh6Z<vHgs7-&Jk-|N$Q27=)|@>_WP``WXN-p=DFd-Y$H=Nq@d^^3mXF+fp>1~g|9wge7}O*EX8BD(f#Z@y5&RwPpO+uD}DO1
BU72xTnR>+!)q)woD0UyI4i+!VW3h`|S>j^XMc#9(@U9=8@osQm%;20^?@D+uSE(YlcIZL>6i<>%9KE-PWpmv8~$-P|DtZmOlqornlJ<3x&N
zGLS$;Z{);Yo@yji}uYcs$%3pK9TdIN_aXL`jxSXKrN-nczU2Sef{mtta&UO?j9)B^l!V0U2ygZ?clGwvH#XavoZiIqP;B$ze3F8)o+e_ze;
wCBIS-{k=qmtOwH!y+Tx4d8Ot?+kQLrh>Rlay;;Gv?IUS~CXjr8#Hq~BX1l8Q|rE3Hpkis*IpIlJ0^3y7?9BE;`@y>>3z$a&fyi<psdA1K+W
P4boqE(<WE#4N0r_#W%(P$S<8*Td0b}v8_%}i@_RY1ii?J-m#nS<--T(p*rUHAL<jx{a(W4088%KmIE3o?VQoGtx7BbIr)aA_r-)H^Gt4@z$
{c;}|%+Bc>kOle?nFt5#~&tNv!J?ODl<m;)k9~;sB@BHBfl!%QBp%*psWw68EixUuHYHIzV&OfYpO5|P{+Eb0TZIQ*HFh{GPqq}7-e{t=xDU
<PZJ*JY-5TYg2qorGB={$cKF7Gl*MMMv|@X-2lde{VaJ3GM}pmdKQl%UF=Bbe(XN*-1fEYha(!dJDGa(uc`pdg!m_fHUP$zsP=uNv>--io;C
kTh(7SxjY&pFq<vb%Z*@!zF2QN#TOxe;PuSxMVzzAkCnNP2uGV#XF#2>EJw-Gw-%-Dx5Z`p==oB{&w27mWyWCV-d`*>&SN|BUwak+_IpyC;k
|tXp`jGz_HF^3foEpG05V}*wgr4zPH51fQIx(r%P0)&ByY-VURRT2wROGU8iC1cjV~_;787stM21Pn)Vp*k*={PH;nijr9_I~2trty$<s_5H
;B*b>quWUD+HXZ+w*w|esBWi(OI|i+b<Dq0jLpQ=(oOVRFIB?CEL1bg2AVMi%PP$3vAt#vKD3KA3tk36gICky&?=F-!WMEtzK3c_=%nd3M$*
|1BkhjYU2idnglJEE`2Bc`~m9{LdlOZx7JYnoDAaLqnZrJnR`VRlNr3Ga{QY><NytnZReZyvxhwRvH=KYc8hfumtQ*Ej(l<*i45ldJAp%8dn
T%|CCXorjpm^lFzKfuYP*g>dUPNs>FTD4mVUU-ad${d4tk|=vso+B1l<~rr^?~DD_zFK*|&;V_gUId)ViUCtSOZR!?Ng!iGK=B34U-e+FF4P
sAP&_Z_gd<+JT$Yx}*P1dgqig%)c<zqnp@rljLeb;aJmEz#0shXcG!44p^ABLTlR=aKR0WWa!SfD?fAP{?te=?RZoRtvJ7(qS=eIw*vXeYH#
_&31KAq5Jqgu?OMD<gkMuDy2?VJ>|9r<LNNOID1LIO8xCuB9yCZ+MwZVjz+D(r6MoY^4#%IPso?dmdc>ULCUYc^grHM(3?5}%<g{!0l2flvb
vCU4qWMV?-bY~#U-PZ+#)B@_!brmaewoB`08aopcxhzRxVHvmJw!4nm|}`s&>h4;4G7~0JiO&P^RiG*6do}<ciIsoTWg4C9h0~7?96JoZvj)
IotE&t;}I46Pn4!lZZA@>(S~-%hCDb^_J*K+1gh#Cg=1lwzoRm`o$N%#!8Q!!T)@7LA}Ge-h!&Utrmudl@0Yg)Z`)KQ{Oyy*%fM7j2i4x{b~
?9|7P0~QbkCjUtkoC$B1+Q#YdnI&+RA(za5v}A%WrVZ)KOWxrc-GqNB)E_p-%~WS=f33AKEW+H>YS`Uce}|HW9|L5dG#6@JWU8Q&mUpzBk)!
(InTim(~hIZZ6d{p&mo&Zt5f8vN^LRczE4lDw=|V@W826_`rAYaLNlC`H%u%bGdFaU+!~vLXMY)h?0k;+t2lolr*WA{Z!Ha=BW<itkv%{kW!
&uu!3i|fa&)UM=)hoa#f#-3ijhZ+6Dg17=bsN@*IY~4{eo}q^_q;&Xgja2>T}sd~#uKvtjz(=)-)?-w78ekS9Dqg<T!cjFV&!kW|l>=E}bMS
%8>G@@tA#Hu!AIECOw+#f*+^xu^`LklgB`=7S5c2$v54*(+X?#h1DE2+-93#IuKgbAd3CR0EO!&2yJ-RUK8cKA<fq1%jAw+Q?g??)XH=0lR{
17wtY#X5rXv1;?Xan^m@*Z$Qwj2Z62%hC0RJ#Fj{Tb;2$a>9IA?xCCeHuBp^l;grKukJfsY4hdANtyiUA7+|v%+RRz~67oHj+-mkQ5HCQxS>
czqb#5|$yl&j2k^H_a63*N!NXG+V%nxhx;*aglf_mpukn;4ZdQ%NjeM0j2N%-8ZY4Ozcw1ewMq=H=VDW2b?-Z%{GVJ!-8vJuFErihE*RS?`y
1qmDV8Nu&`S`NT^P=A?yTsv6kZ{(>;!oC)ZIHnTS<g{_g_d6tlVZXkj5Sn}yn3knK7hylF65w-CVaY9~=j>mH|1ylWMtg#B6u|Lrg&p_)t7k
hn_1@*~4<JyTyW0&gH3Yk%+{T>Gie@r#>g+tNH=ZZ843a8OJu^b1Aqq9o0E+k`qoK#}*W5b+vVo09CDt@y8M_i8?N;W{kylDROO>{<>Gfh?^
l5~~CbJ0=|CijT=Q*~d6lviB1fwaDS^gcjEMe;q1mv?48UpIll)Qd|qFV9y{GoHjSZjt7Wh=D6%koOSwCEO4w9k(<Qn71OzXO8u<31m9++nI
8^ajw=Q=#oo_!fZfNHn43yvq2uF}cQQM;4(?5)ld_Y6d`$43gxKcQjm$+B)e+NbtIuJb=v(*73$)@-J!$Ifs<a;=<Va6qpn#cMQh7Br=aD0j
|cM)Nahn_+b#h`CWa5BDm|)#l*oi$CF}k#N5N1Wgn>O0pxM-M+58h91~Jv0GR=8R|<h^j~v%~G5&ulV7xt@kWRgEoSV~=(EM9u@&vq<G9jy%
ICy!!JW#sS#4h{XQVzAU+|!{8xb{XDLM*&PKkh&=AkW8dgg7XD^#>kA%DCafD^M=5{?RN_9=q2IOTB-*eN<CI>UT6hVo{7IPi9KSwz<0{Ej%
b5XC3=v_)%$AOQ7_t3?k%=wE`LGl@iMeNUsQV?i!K<Mi<$9c1P>#<yvddvX3T3jwgP^!{Onb6m$Y)e`|f7^!0lZ16sab`sR~_FDpAI>mj&-m
9MC#aCk=JRG{w@AC~Y#V1NIh5@#)Vp@{AJ)7qKP2ebSLe-9jhQDjy7RwXM$NN=3UmJ&=HSw`aKP`Ew=V8^MeaW@eZ9MfJQL`}LVp)ELFpMUN
hn0WaP0+r=>!JfBBx#R`5@o?WpOOWfN2_Q`hd&+{r`dWI>3~DxN=ElkDQs<Mn6iRnB=)5mB%}70o>C)oq!`qNIJ(K*T9e}`A5pt<BNA`{Ngl
pZ(f%sx#`uj8L)xc`m)=}KfviVg{>R~26$=Wuqf83g$gYgB5*eEGuECbJ~ilRpf7EJv#z(8U4SyP{y0wh5lzDM}f-XrcYnP4h;X{gI-g^-`k
EB^cxi^Qqs*EB=X07)&2;qU$Sfx!D1{_$3PpV|5NxdVBxh_&?L`GB=)VY<$;3{VRY*~(cc9wy^2C%2=4C3DhN9{-<7QsaMDC4AWM+gO|>e;W
r(4EB(vN#6MN$sZ`K!}6cv(srmuHMGvMQ5lR!AoqyHA0>;46j*u!G~mH5ecq|cZJ!Jb9!x<M$$vTMRF{4pdeJuZyuknle#p=k$w6PjFw)h%n
>JX$n^|B_3<?N(28WBms7y7YKHuf?{oIQ&dDhvgp(~!&CcmU<tW;Mw1|_QwyWzvo*tS2EhZ{;;E}U7r$dj0PPpL-w|9!18>KSnXz~|?i-Vuw
dBuQ5mP)Ia(RmHaao}%Q~Vq{~ZvySLPpfvW`gqTsP)W#IVH|u>jLo);1NZJV?+#eWb;=y8ZMR}6oFCkIHmBV;Qp3O<GJ4XG<ynaVr1|J{xN5
7UBsJB!%mNumhay`XsK89p%xoO=*97L-82|R*+W9rUVaIsYO)$EGAh6V-NKiYoP{fUdoV@#_TtR-x5cH#u$N&p!bFRSpQnvW04ds^PzRgZ^P
YErA1Q7v*l_goGul2}C@{?KP|O9G0lLuJw4vqif)^T5$*025*==wrU6%(eD0HVkzd_{daw)?fE4O7y0#x7sYSslO%MfB^QSt!9vcw*ucc|AN
^;VmCfHPs~$O*1AD7Y{-wjL983L|HeSIgqGuo=KS+3-{&ls9K|avmsz;pV2@uVIEPyhQ9m!@bOJ7NGJ@8?GoOw{*&IDH2MkCdt$=29C~0|*O
lG-wLCuP-F2a2XJ+_@f<eUQV@LNU}iCGNasbv56_PxCobFR%8_YPOZ8_8@`28_?kSQO58NucC*h%h^=2?WTSBS&e?A~mXPTx^Y|U4pl<X7=m
K-?vo-XgfvibtT^vn$2DfL~}z-xmOg;`;Qq#Pc8k0VIk_^q^e+RYX{Ssx|7Z~{FxV4VQ?_DrkIT-AG!4WweD?6E8<eK_UQZ7nb-Ba|L#DB+7
&qK#4>i8A%Np<?ZNJVw?~RzwY%L=lKH22a@n0+upOBM(~w?g_b3yb(#*HmbF!B?dGnn8P~;+^s1B_@#OABBLf{c(Vu+gb+#SsQ&eA`|dY!8x
N!n3dTU@VFR#d?bnCB>s{CA3fRe6f|Qhy^{dcf+%{<Fv&)&m;RFS0i;7-)Nqi3Yj_X+v>Oy+ns79wLewK7?eMT|q5{kEO7d5Dm$P!Emg}wF&
Tj)K2ekRkeuGB1=6BjF`>cQIKxZbwecBR<HY+vW)fVYpj8Y=r{i$JX;nP5`(6;hoD)e<1B$uKi-jqw|o2usXd^78;*wp;bQ7<wL`|A#Jld8d
jimbhA>{?jyt<r{XgE%$cQdNKnQ!wtI~o=R{?aOoxZLAyGiZyUgMnh>vabU=Exq!HpMT61f?YMggfT>Y+8r@TIXVD$b3GnFwIY&j7y9*EAML
E_Z^3&O^%7g2y!OWA~08<P*qF}QyFwp3uvd{&!}W4d87<}MT)Yx{q8xshRs8*zq2g;hxy@$Tr_}vKM;eFcE`^#So3s551#0c4**tP!fZ(a^;
VwHt%@93hotO<>7#2eP)DOsk@?SAeo(`%<0S{?!2yID(j6G{(&=zi%e$&#blDsnT7<u2VR8`KGkxC;#jcajt%22Y^A~^BFUGl9+_1JhKlp1E
1%GWevxH_AR2mToxp5InO<qXpI|ZWr_TS}>T2k8mNqzsMpR0INg_~E)EX1~pU|tbH8m8bIS(z;@Xjw@2v)a8IWE&0P=`Xz-z>pGYU8%Av*#-
bhe{}gn-WpsPLHa1y;s%H}gyC8Eb?Wqc-8e^jm<>8QMbI^=<rw;Oo?!8sYf=mq>Ty_NJ>|_!J|#;-(Q8+zb9cRV?utU;jF$fPwGO$|gv5m$$
X*1@T~$r7qmoy^c)eG`UULo=M<@fZvoBglfmZ<1)>$Q5Q9<&!Sm$TSy#;WqL7bxNl$svr-}%P$f=x_hXYXEok;md=LQ6_72snOpw=G)0^8GW
~bguOE4z3-Rt3urK0T!Gw<$j^3$ji-x|IH)e6vo{2a!dQ(w+)F*8uFBdLd~kan*|+y#~>JH^yuH99$2Slt%bU8fRl^K26(?`z&BH|?dN5$Zm
G2x<)8NFpmRbF5djz88ILB=?C?6ab<J=G;dF{YC(x`WtqFd-o;eQENhM3nN5MGO?9B-d%`kb&=xWioV!qAE3ES~xVFHU=swnTgP782Q>d0j=
W}rC+^5QAnbMgO>g*=a8`k$cD7s2OQ{7}sV^<92Sbc3d6p7$%NAATD@mEQ}M^r7sGs4uIHC^AdS4el_c7$rIje=F2L(o4i8YTGRId$7z<BVP
*ql{i2wLZI3D1W2V50`nKDl}0%_AbpqF6<v|>9c-Tm7BL$E-!P<d>AgUo&ng04Zh<4vfyP!hkeNjz(~~3)3P`n3=$ckbOhY3Dic32HXnAS>B
MU~c(FKf&E`_>Dt)z8MX$0y5HbZHm4#$ah%5Kro4wY)Z=@SD*z>T6et^F=uCksCmbSSo}U~<8{_7Bkd!d~>ROcGISnUkp5>QwV>&BTtB;h@d
{kcA>A=W)17S|a%jEYSLZ!RY^h_vjs>==R<}y&B(p&rS3k7UDqEdb9i7N7|zp?@l`aEw95GG}LVq$rI^Rg<`7V<wZWG<QRDA<ttfk>fHgR1U
?f@`JhQFUJ8S0uk9(;{YY<s+<aVvv#Z1}6;5@?#HUQMZk5j4+`5!_h(4!sd>Rofo@jry#DtWs()r>f)6>t1&wA^^1<1rfb0j!|M6H=nb>mJ!
gh9~T1^)A=_>p|qEmyBoQ~$A>7}!&K#aU~(ywX$aAo|oGSQN-*0gxx?&FK<AuWc43je2r0R#2tZMsmx>Gmax}M-E7}uS3moqIM;5Cp{HX27`
!ndi<j-pb4FwI5f%8Mo-EIm!nnBfFv|>;->44eO`9pR1hU|DHr)ttQhY+m|XK*Es7sA0qJks8NZ1BZ5SgLOEq<b3b@3`e_Qcj+`AmlE7TBrf
_n(o_suQ)H?JR#taxEajH;3JX-?%cge1}ah~v}<=>0$y9@FkUkU#S!{CyTxd7x+-GEAKx(Y@|bj{vaT`@x6t55nU*2U#BxT=#QRyLaM8DZ;y
t=us9~Qbt?6tLQ{i4@&{$?EHd}s%s2!Vvp1pn@Jg<k^Ym?VLy42la>&*2Y9KmPaHkQ0y7LQgwY~$6BZ)0C_ddnXAG$aw)6W`F=}P5wVM#UsT
E#X6K>L*a6>_5I>O-+O-2wv*Np;-c(NGv9XBS;`Cj5As`w@Hf>8weA`6DNcMx}B6Daqh_Zz%opQw~(cfiLMfli$kA53Er&!0%VrM)S>LrU-L
-E#Z`!R-j*6mw+{21Ny6Oy+x4FNT<&mgs*<625n~a?s|+jQ3W%^$3r_8P{OmuIIuwJIOx@2Et_hbkuIO=3@6LXUTo**jL^Buq$Q0_M!pVbX0
mI172Vef~~@v6?dGoIQp*X#z%1UIOn=wmju_Gcn6zfZVGuq%)6w=cjfy7NYhK@mOCWBZun7qVtn}g#|&CM>klfHtL0H&Me{4g{iaG25Ahcvi
7jSJ?u0=_%Y7gTEQ@lUq9d(1oMS&a=!7oopr#HhwoW}%w=moz0Y2{U(}FGKA4!7W3TqmAcETCSDgP&dI077qT@<v=I$fseS*a5e9(abRr~A^
EoHCkCQp7D|O4;{u72}pR_wg<eIoy`UzYX^O4-yxuUw#Yr(fFDd<fo99li!JS8B3b<gsTqpw3&-x;;<(xVPh|#TV*L&C6{|u421Dch1}PGs5
^LTt=io?yp^V>uJ;1nIUll`d4r`%qI21s%&&;gXa97z&mgAO|B7TZwgLHYjp`+6@V<>42nebfR0mvPz|YsN<5w)aDWcwMz=RE~jQz}1+|t*t
kQYoBpKiace`Aww-^@v*PQKJN<$9vMl6DuovWP{F=$HECE6=cjlAdt13I8=BA?BUK_IhU^=)XcWH8pa*1L8Z5`YrOD9N%8GzsgkTdV{^!8Nc
YWN&4SG<W%h+mtA+2)sofxwcIVM6|XF51&B))uwR9%*XqIV-vX|t8e{GKiUEiIt$2SDXm)jpdF9%I9t{224wvr?;+2V`2+E73C$JBwv2>r0P
jIZ>P(lA-Hfpeqp|&Zs6o5oq8|v*c_*#GaB93WZ5#ao?h>WXEmACB~L)VgcV2^!`zk5l5QNyFf!#5hSfcFvtFtp&dY3Nx`HE)3bw`a6Gzxl4
VI;|q3_$WKo+3@l}>+qVnD0M%(5fyJfY__`-gG2ap)~!u{hoWE>9T%Zif~@!_>GeHykCh^LesOMbmt+;GKIC*z>k9+Ku*R6eSX|@q+TVrQXV
PG=1#KrALrHY?-!}>&6#<gh_2Pb&bO$2qyt+&7H{k|zifcMlZNRj*DKrOXlb*snVz`3A%LUuFO90xJcKG`ug+tikK6pDxy_-2Ax>@w))Y-Rc
ige+s&tcy=W%hs+zYjV~zuZ8+q-9@dM8AF&-wB>v&SD)#;wodgs#TX6J>fQc1Hb&Nh-#eP=p?aisN%qX!CYV&WgM&#yommFAHwp@Tobe9g#=
ZQSSenCuImx}SP}!UTOgnP9)cL0#M@=PwrPDVNk}4^AwUa>?EUdFO@T7%Z?Gn@bmuLzJN(R#^LIybzrRr`Cd541Mjq>lBNVQQhtX)e-2%q6K
qed6aA48TsCdREHTt%gfoqT++bX?#iIB=#oNpg2Z;0M8g`zeOU&fqwZ0M9mLJmQ7;;@vZiQC@Ezs&d*nj+wy>YjLBKOKSS_Donj`0x3|`xCF
XIfxK8LHPIrmkM%Tvpl47^T|7Pb#PB8O5P$KzIXZ2)%Kwr+Xh5u%lD8kxV9dS|JYB=yLkdhZ?-Pa$7{r&7Gn}w;F)Xwo=Lj-S17I=7MvM)R!
U>?3gq~|kylji3GdZlHShh!8zhPs>@nsn4^q}LBZ3?qH7)-P)OEzRv?tckkgj%oT$jU)x)g4dkw*BLtJ_&`vg~1Q0Z$?4>an3cr%V56I0(YQ
Yd7l|J(QYYsEZ>ZVi_%zIyQ)70cq{jqp;lRNF>N4fx?O~X}pF(O^d#<Dof}9q;=vdi1Qo#A`?XacNa9Bzb=4GNm;fjxGGJQo;FML)i73|1?@
fUOU4F#la+^My+Ry60RHEi1(k~4QL27%jJg8E$U<WYz3qL96w)kLCnSJ={YWE`24W5U0CQk0z@R*cmImoIb6=b&nVj=vOe~eW+xCl7puuS|%
W6FSP(V56Fri543hkAB=f*q*W*e73yVX5dxdo>cH`%|-aeeC7(m;8--XZ%gvW_P2n`uME$<ag2TOXJhByu6Fp($Xytfk*aC|c>9N-I1i4av>
WeWMv8<7fmQIZz*u;)|5ERZHP`U{HJrS5Ctjqz0%5PZ+6E9DzkV%9<n~HM2qi44y6~<%yETN!lVuLtF9F(1?CHXlp1Z=6&d8|LX2(u35({OQ
0CJ$1sb~ne!AIlav2Ats6(y7G%{k^sctDqgB){98M;pU$b}|ga|Mnx#le>c#+$C3#`@yUd@9~;UX^cpW<L|egw`>{lBMZ>J!+x2^hs>8gm<q
F~Il>qRHz$s>0g+QCtwBlF2oW?A|@H$nXf4pe)#&RD#^a$h)*rCU3nJ!~@-AMj`M4U7L`Jg@2V9Dicyq`i{CW^KME?b-Y$L@n;9=@tTWs9rJ
6u%VxG}Ny_r}NhEl>);RBBFBPQ(amlkIOGa&)SXJi{hO%4%yL|(RDzcF&ZOPRPAFeXBJWdJ($a4%Swf+iflzsTvEL+a8NRB{I5EJbv8C#mYt
b&n<Csa}UU_EU2m&yKU`M(a(`mQk;a(98dnA5SYzGpXy(IND9EN2=AbTliYI<o)2?ZD?wXu*BljILjS$_ZeMeMEvcmb@xR{1n%JjqpZu^RlG
Yk<b<A#*DXaGLOFoL-&j|&}UBh@)Cy`Iy6uNs_?S05u6~m*#&^oU09fQZa?;Th_O)4_iz#RvL~di=r_v~QY@f5N=RQ3V@n@sa;(U%Wz%1`!n
~NRzX3UwXsMK-hc?ohaYvdV(up=PDqY0^6L@c3pkxw<QtfWD6RA0+{%typpN{|_D|9u0I+m@TA0miWEx|4qID_#(Ls!+>%MXZGrtn<<NQ9Dq
=B~PBeV-l3I{dP&a}T0z;|Xpn=57>`p+I(zxc9P)t&jI3oqXg)`#ZK_pkHWJ7BH`DJz3v}`t_t)-y#)94@f42rUx=hE5mT{ct8h@>L^yzQ0m
hwa#>tL=UZhaTg>Jfa*nW;fK5G36cZcLe&wv36uIyd*alo`n=6G$+*tw4?0A<@vctbOyd5QuWEPaEvx(nFZR6HppUG+NA(H;mHWoxkNa6h$f
k-xU7u$jmJ^8^5g??!GV_agF2%+T>0Rw#GH!QW>0O6X15qbG|(4o}nuKpP6|6JO$^5DL%QrllStY9@kbxjk^pFB-ece+KGZlaJ&lnWHHhVhy
i<ar|&JN)iE6k_nTFJym%MhvjpV%`;AGHU&!<6>RenRXUc?d60qLv}{tkH1Z;Szc%c&1zj%@}oGdVdyJ<C|4r*xR@%xC$nbpL(Kq2TA1cTk+
+oMZL4=Ny+bDNdU6OFH8GqE*+^=6R@(ul622rir*mG`G(uD6@c<-K5Ie1DTf&lAY^i~~OxLVjx~C=`w>>M*>J#8)D+#KGD~hI^O<7cq*CAcB
Srs)uf3pciCMEikGns+MP_2ln*7fcON7#XxJq5(TCU@L~C@uMEw48$25DK_El^&1&Gv{G-{eIVn`0Z@0`6PN7dT=EM8v+NO>r_6fZ{J06XXR
%XYYxvls{@b$(BZ+iG%3+<@D4KhuqM4edyD}2OP9}gV$JTny%V3^sPYBj$;arqPwALfQqm+#7Z`SkyA49r`FTVJi~h}Oficd&JuO^+usyJjt
A`CrrcVv~8i%W|@(?28^SL}73=j3v3VgjJg%BgrQur6hjdT$^^C^5*0)Itr=HaI^c`QCIwQEqQ<pVQp{$d?Y<P4q2tv#>y2&~7c?CYu5eXFP
EvC~9PPN1LWwXMScei8o6!UoZF?Nbt0&x}t345WrwukcQ{E56^OTX3&haybuDIxF0{SUEFSJSho*gb?PKrnK}P)>b9XtRdgDw2a}iq9=@%^y
XZCN%FkdamA)h+MaQa7TS1seqT(s$eS4-F-_blbedqZ!HCq2tciL6<Rt0jpI*U!00EF*vh4u?mq$ugvBYQl0ssI200dcD"""
raw=lzma.decompress(base64.b85decode(''.join(DATA.split())))
assert len(raw)==30386
assert hashlib.sha256(raw).hexdigest()=="a129c2e5370305465105a4adb5b56ad152f6d5f517504853800ffc05a85e231b"
files=json.loads(raw)
assert len(files)==4
root=Path('comet65_closeout_recovery');root.mkdir(exist_ok=True)
for name,source in files.items():
 assert Path(name).name==name
 (root/name).write_bytes(source.encode('utf-8'))
print('COMET65_CLOSEOUT_SOURCE_READY',len(files),len(raw))
```

Reconstruction and verification:

```sh
python -B -S COMET65_CLOSEOUT_RECOVERY.py
cd comet65_closeout_recovery
python -B -S closeout.py
```

The decoder was executed and all four recovered files compared byte-for-byte with the sources used in the observed run. The complete closeout verifier was executed, including both full audits and active-row equality checks. Its decisive terminal markers were:

```text
COMET63_TETRA_CUBE_CLOSED_WEAK_AND_FALSE_WEAK_CONTROLS_PASS
COMET65_EXACT_FULL_MASS_MAXIMAL_COMPLEX_MIXED_CENSUS_ALL_INTERFACES_PASS COMPACT_G6 [92, 138, 48] [1, 2, 1] [0, 0, 0] [1, 0]
COMET65_EXACT_FULL_MASS_MAXIMAL_COMPLEX_MIXED_CENSUS_ALL_INTERFACES_PASS FAST_WHOLE_G7 [130, 195, 67] [1, 2, 1] [0, 0, 0] [1, 0]
COMET65_UNCHANGED_TWO_RAW_BODIES_SIX_PARENT_RECEIPTS_PASS 6
COMET65_ACTIVE_H_PRUNING_SAME_BODY_PASS [48, 67]
COMET65_CLOSEOUT_DECODED_SOURCE_BYTE_MATCH_4
```

The two audit lines additionally print elapsed execution time and their receipt dictionaries; elapsed time is not a byte-replay target.

### Exact artifact receipts

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| COMPACT_G6/audit.json | 13261140 | `d74ed3885328b7667ef94170c1e3285f193b25c6bdc3be179357c5da9b255cf9` |
| FAST_WHOLE_G7/audit.json | 31556089 | `538e6d1f2c5a53c060c6d871accd4356b4b3f25209449d0a8ea1c953efadf175` |
| COMPACT_G6/active_input.json | 1565 | `527dad0a8a94a801742c0ad93cf3fdfb378b91ba1a40f3f422867d3fd690e46f` |
| FAST_WHOLE_G7/active_input.json | 2285 | `304ef6b3ead6e16cc9d8e518af300241031db5137b383f31e723daf0d5891dfb` |
| CLOSEOUT_INDEX.json | 191626 | `e66577c9d72aa2419146e30102e696c109661b379c5a4b9fa296d128bd7f41d8` |
| COMET65_CLOSEOUT_RECOVERY.py | 15784 | `c497cf052a69968bb1991c57a252aa8b88040be49ca616a7dfdb61d1a9ac0c65` |
| COMET65_CLOSEOUT_SOURCES.zip | 27624 | `85f95f46245f652f73ea571b5d9077a2d54a2723523423464e2286196ab07344` |
| COMET65_CLOSEOUT_AUDITS.zip | 18491846 | `b650eaa252c1dbe464f1e01fbad42ce1192173aa0ea82bbbeb771c1ac0928fd4` |

Convenience copies: standalone closeout recovery (`COMET65_CLOSEOUT_RECOVERY.py`), complete closeout sources and observed log (`COMET65_CLOSEOUT_SOURCES.zip`), and both full exact audits, active inputs, and carrier index (`COMET65_CLOSEOUT_AUDITS.zip`). The inline capsule is independently sufficient for recovery.

**Scientific endpoint unchanged: COMET65 own121 entrances remain valid; the last S/U/H defect pair has not been cancelled.**
