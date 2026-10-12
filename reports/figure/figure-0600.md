# figure-0600

AI research report · 2026-09-28 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# KL13D — whole-return-path motion, an exact finite offset obstruction, and circuit-directed carrier retirement

Branch `[internal-source-reference]`; Keen Lynx 13. This is a continuation handoff.

## Result

**No own110 body was obtained.** Three new rational bodies were constructed and exact-audited. Each has strict `(S,U,H)=(6,1,5)`, additionalweak000, primitivezero000, **P=[] and exactly five positive Q bars**. The whole-path attempt retains actual U1 but fragments the previously single Q into five defects. Its smaller principal Q is not cancellation or a new own211 record.

The strongest new result is a **finite, exact closed-offset obstruction on the resulting current body**. It rules out completing the specified Q return route while retaining a small, explicitly listed physical-ray/intersection cell, for arbitrary centred support offsets—not merely small steps, a fixed centroid, or a numerical trust box. A strictly positive linear dependence proves the obstruction. A subsequent physical construction removes all fourteen targeted old carrier vertices and three additional vertices, while keeping the old unstable point uniquely unstable at the new actual centroid. This escapes the retained-ray hypothesis, although all five Q defects remain.

The complete literal capsule below contains the selected KL13C input, three-body recovery, exact auditor, proof, consumed numerical fields, and producing units. It needs neither the B/C workspace nor a hundred-file reconstruction. Unselected B/C sources are not silently republished or reclassified.

## Reading and source authority

The updated407556-byte journal was read consecutively through EOF1757, including literal parent `figure-0597`, SHA256 `82b11fa3879c76581cb4e9e089ab615df89e92b585ccb0720e21e5d256c4c02d`. Both supplied method materials were read completely. All three supplied byte counts and hashes matched the manifest.

The actual extracted `geometry121.py` is5112 bytes, SHA256 **`b64da8c4140fba3954b28323d603be3813b0643ed6aca18b195a2b62f2c44bf1`**. This agrees with the J121 heading. J122's prose correction to a hash ending `bf2` is not the identity of its supplied dependency. The literal code was retained, not modified to fit that erroneous hash.

## 1. Complete Q return-path motion with a one-U quota

The consumed parent is exactly `KL13C_CARRIER2_CLEAN_G8_MINIMAL.txt`:1779 bytes, SHA256 `fbe86daca4468cc5da6bd46dfab884da7dfcefc559d4ad1a00082899f96b51c2`. It is120/180/62, own211, P=[], Q approximately .302080624656288, with23 sufficient new-H slots.

The supplied J122 producer omits TWO physical guards. I changed that quota to ONE and recomputed every other actual physical vertex's angular outgoing witness at every finite trial. Positive outgoing chords strictly increase squared radius; if every vertex but one has such a chord, the omitted vertex must be the unique strict maximum. Numerical signs still require exact endpoint verification. The original two-guard quota was not treated as U1 protection.

The initial full route, in **submitted support indices**, is

`2 -> 26 -> 7 -> 27 -> 24 -> 1 -> 35 -> 46 -> 10 -> 39 -> 11 -> 52`.

The first five arrows are negative; the remaining six form the old positive return to elder52. All five negative arrows were targeted together, while the positive return and individual nonpath witnesses were protected. The largest initial negative angular magnitude is approximately .2747655503. This is not the junior root's local best guard, approximately -.1719602008.

`D_S` admitted two finite steps and rejected its third:61/56/59 optimizer iterations and119/107/118 model calls. It did not complete the requested six rounds. Its accepted second state gives `PATH_ENTRY_G7`. `D_U`, starting from that complete saved normal field and omitting only the four numerical coordinate-gauge equalities, admitted all six requested rounds:112/108/114/84/55/41 iterations and287/315/321/243/218/149 calls. It gives `PATH5_G7`.

Every admitted step uses the rebuilt homogeneous body and its actual centroid. Removing g/log-volume coordinate constraints does not remove mass integration. Subsequent normalization is a common translation and dilation. The rational freezes have small, **nonzero** actual centroids; neither exact zero centroid nor exact volume preservation is claimed.

The exact comparison checks that **each of the five original negative angular guards becomes less negative**, while all six return guards remain positive. Four new Q branches nevertheless appear. The endpoint is615, not211 or110. Solver status did not determine acceptance: finite inequalities were evaluated separately and the retained rational bodies received full exact audits.

## 2. Exact obstruction to offset-only completion of the current route

This theorem concerns the literal normal directions of `KL13D_PATH5_G7`, not old H80, R82, or the entire free-normal family.

Let integer normal rows be N_i and let h_i be arbitrary centred offsets. An actual interior centroid, wherever it moves, gives h_i>0. For an independent retained triple T, define

`v_T=N_T^(-1)h_T`,

`F_(T,j)=h_j-N_j v_T`,

`P_(T,k)=-[(N_T N_T^T)^(-1)h_T]_k`.

F>=0 is a necessary feasibility condition for the old triple intersection. P is exactly the outgoing radial score along its old tangent ray `-N_T^(-1)e_k`. The index k is zero-based within the sorted triple.

The sign of the centred polar chord i->j is the sign of

`Q_(i,j)=(N_i.N_j)h_i-(N_i.N_i)h_j`,

whose omitted denominator `h_i^2 h_j` is positive.

The complete certificate has **39 rows:16 F forms,13 P forms, eight Q-path forms, the off-path form42->41, and h35**. All descriptors are literal in the capsule. Exact rational elimination gives rank38 and39 strictly positive integer multipliers, maximum bit length2654, satisfying

`sum_r lambda_r R_r(h)=0`

identically in all62 offsets. Only38 offsets participate, but every column of the identity is checked.

**Therefore no offsets satisfy h35>0 and all other38 listed forms nonnegative.** This permits zero physical-ray and polar-chord guards; the contradiction does not depend on demanding a positive numerical margin. There is no displacement bound, offset bound, prescribed mass, or fixed-centre assumption.

The eight necessary path chords in the circuit are

`2->26, 7->27, 10->39, 11->52, 24->1, 26->7, 27->24, 39->11`.

The ninth chord is42->41. The circuit does not require the other three positive return arrows. At the audited current body, all16 feasibility forms, all13 physical-ray forms, the off-path form and h35 are strictly positive; exactly the expected five path forms are negative.

This is a **selected finite-cell obstruction**, not a root-free exclusion of S1 or U1. Another physical outgoing ray, a different Q route, retirement of a participating intersection, or changed normal directions can escape it. In particular, it does not turn failure of the unrestricted free-normal solver into a geometric impossibility claim. Its actionable conclusion is narrower: arbitrary offset/mass repair inside this retained ray/route cell cannot finish the current Q path, even while allowing weak boundary guards.

The floating linear program only nominated rows. The proof reconstructs all coefficients from literal integers, computes the nullspace exactly, verifies strict positivity of every multiplier and verifies the zero coefficient vector. No floating infeasibility flag is used as a certificate.

## 3. Circuit-directed physical carrier retirement

Take the circuit's13 physical-ray triples together with `(9,16,33)`. At the exact actual centroid g of `PATH5_G7`, form for each triple T

`q_i=N_i/(D-N_i.g)`,

`w=(1001/3000) sum_(i in T) q_i`,

`new_raw_normal=w/(1+w.g)`.

Round only these fourteen new normals by exact ties-to-even on10^9. Multiply every old10^7 normal row by100, preserving every old physical halfspace exactly. The full deterministic constructor is embedded.

`KL13D_CIRCUIT_RETIRE_G9` has **146/219/75**, strict615/weak000/primitive000, P=[] and five Q. All fourteen targeted old vertices are gone, and three additional old vertices also disappear. Exact counts are **101 old vertices retained,17 removed and45 new vertices**. The fourteen new facets are **twelve triangles, one quadrilateral and one pentagon**, not fourteen isolated triangular pyramids. Mass is integrated over the entire filled intersection, not by summing assumed disjoint caps.

The old unique U on original supports52/53/54 remains the same exact physical point and is still the unique strict U at the new actual centroid. The verifier constructs positive true-edge witnesses for every other final vertex. This is actual U1 preservation, not merely preservation of an old point or an old-reference classifier.

In the common raw frame of PATH5 and this child,

`-269802272/10^15 < DeltaV < -269802271/10^15`.

Each Delta g coordinate lies in the open interval `(a,a+1)/10^15`, with lower numerators

`[14506965,-109465581,-1063073]`.

All five Q branches survive. The construction escapes the hypothesis retaining physical rays at the removed vertices; it does not itself supply complete polar escape. The75-facet child leaves ten arbitrary new-H slots under the sufficient F85 bound.

A further free-H trial from this literal child did not produce an admitted successor. Its first candidate, after160 iterations/368 calls, proposed progress .42856394 but had minimum constraint approximately -.01250656 and displayed10P/19Q. It was rejected. No later round or exact census of that rejected candidate is claimed. The complete source variant and parameters are included; this failure is not a family exclusion.

## 4. Full exact census and homogeneous mass

Every name below has prefix `KL13D_`. Every additional-weak list is empty and every primitive-zero count is000. Canonical S/U/H IDs belong to each separate exact audit. The common S lists correspond to submitted supports `[2,7,24,26,27,52]`; input22 is inactive. Physical U/H labels are not transferred between rational bodies.

| Body | V/E/F | All S | All U | All H |
|---|---|---|---|---|
| PATH_ENTRY_G7 |118/177/61|[2,7,23,25,26,51]|[0]|[[31,89],[87,115],[62,111],[62,107],[11,113]]|
| PATH5_G7 |118/177/61|[2,7,23,25,26,51]|[1]|[[19,69],[70,115],[60,109],[60,112],[33,114]]|
| CIRCUIT_RETIRE_G9 |146/219/75|[2,7,23,25,26,51]|[14]|[[40,85],[86,143],[76,123],[76,127],[52,130]]|

Density is one. In the following table, each integer a denotes the rigorous **open interval `(a,a+1)/10^15`**. Complete rational volumes and centroids regenerate from the capsule.

| Body | Volume lower numerator | gx lower numerator | gy lower numerator | gz lower numerator |
|---|---:|---:|---:|---:|
| PATH_ENTRY_G7 |1000000001547300|7369530|12777508|-289055|
| PATH5_G7 |1000000010660617|-694530|-3034168|-1770250|
| CIRCUIT_RETIRE_G9 |999999740858345|13812436|-112499749|-2833323|

### Every positive bar

**All P lists are empty.** Each body has exactly these five positive Q bars. Entries are depth lower numerators under the same open-interval convention. Root and death-edge associations are checked in each separate audit. Complete exact birth, death and depth fractions regenerate without a bar floor.

| Q root; death edge | PATH_ENTRY_G7 | PATH5_G7 | CIRCUIT_RETIRE_G9 |
|---|---:|---:|---:|
|2;[1,23]|249254486642427|223983250439344|223983534415641|
|23;[23,26]|7553037968991|14716383119168|14716349789998|
|25;[2,25]|6473418246505|12249674078834|12249663710173|
|7;[7,25]|6147357492719|11676056849988|11676033003843|
|26;[7,26]|5526980972862|10635580716314|10635558696236|

## 5. Verification and recovery

The endpoint engine is unchanged `exact115.cpp`,11038 bytes/SHA256 `d7fd1244c086a0c5354844cca3453c42b26ed31a55b89720aa9e3987f0a06736`. It performs exact H-triple enumeration and boundedness, maximal-facet/true-edge reconstruction, two homogeneous-mass sums, direct/global mechanical tests, the full strict/additional-weak census and every positive bar. This is one inherited physics engine plus additional exact identities, not two newly independent equilibrium auditors.

A fresh directory decoded only the17 selected source/input units and completed the full replay. **All eleven expected byte/hash identities matched.** Observed terminal markers include:

```text
KL13D_FINITE_OFFSET_CIRCUIT_EXACT_PASS 39 {'Qoff': 1, 'Qpath': 8, 'fan': 16, 'interior': 1, 'nonU': 13} max_multiplier_bits 2654
KL13D_THREE_EXACT_615_FIVE_FULL_Q_BARS_AND_17_RETIREMENTS_PASS
KL13D_SOURCE_COMPLETE_PATH_OBSTRUCTION_RETIREMENT_NO_110 3 11
```

Exact replay needs Python standard library, C++17 and GMP/GMPXX, with assertions enabled. Numerical producers were executed under Python3.13.5, NumPy2.3.5, SciPy1.17.0 and torch2.10.0+cpu, float64 and one BLAS/OMP/Torch thread. Exact reconstruction does not run an optimizer. Complete consumed binary64 normal fields and exact rounding checks are included; bit-portable optimizer trajectories are not asserted.

Save the entire Python block below as `KL13D_CAPSULE.py` and run:

```sh
python KL13D_CAPSULE.py KL13D_RECOVERY
cd KL13D_RECOVERY
python REPLAY13D.py
```

`METHODS13D.md` contains complete producing commands, nondefault parameters and executed-stage boundaries. `STARTS13D.json` preserves the consumed normal fields; thin restored wrappers are explicitly not byte aliases of older diagnostic-rich files. `EXPECTED13D.json` contains the eleven-file receipt set. No unavailable parent workspace is a runtime dependency.

The capsule is31850 bytes, SHA256 `61873f73014dc1b313496c84d65f0c0e3e7efa9f468f182b201f8873f0a17da5`. Its decoded17-file canonical dictionary is64501 bytes, SHA256 `fc59f76b81062e0b1a3d619bdd159228a18a4f09e79ebfb2bd2a641a22df33ca`.

The next construction should change the complete current escape route together with a ray, normal or intersection condition identified by the exact circuit. The retired-carrier body is one explicit admissible starting point; the compact PATH5 body retains greater facet reserve. Neither lower principal Q nor removal of every targeted old point removes the five surviving basins. The selected offset-cell obstruction should guide the next geometric change, not be enlarged into an impossibility claim about other witnesses, normals or homogeneous bodies.

## Complete literal selected-source capsule

```python
"""KL13D selected source recovery; Python standard library only.
The embedded data contains every selected exact input, proof, auditor and
producing unit. Recovery itself is not a claim of an own110 construction.
"""
import base64,lzma,json,hashlib,sys
from pathlib import Path
DATA = """
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;QRDm>RkXmh=iqrocag;lg9+B!_;iMcLx-qr*fv8w@}J;^_Lgk&gfQj)?<DB-nNY{oVTj+
vMb5V15}fYM80bd`Md^N*g!d#CL9$f?DXQ($))h7hg~?CRV<`jJBVxxfEfisSM})Pv9I4n_gmx1C)&KhwrH1t;=kGf=S!#{REVMS
)ITE3R8sS+_-7z;>)VLYUo3p;H&UscSo`gpc^DXy3&HjzHpKh1`9bkoDM+z#Oiq?JL0m}d70~7)!j)4Jm_9F+5`pwb-!Kg|bxA66
ZQZLm5W62-3xoc2^%X7R2+MIS#K?;XLeg_Ym);iOEhX&!)Z^3~Zspn;>LZ@QSuMk4PERko+-JAMB*jIfTW=JiFa3Fq6kyS1h~V~j
X&I<a4MB6Y8l^ov9E6-S@zQ{4XZ*MT4p$AMp;)7{Rd8R%oBvvJ9rO}0VA?!7ZL3g5AqKMgfIIw4xXFoF4V|fzU=YZCg$jJhtc&ch
)P&YD^yo%i?ICAM1ybK{yEqpik7EMJc#E-;V3G;jkHh=lV%ptN4p^nJjKruG>?NkPQ@V<y+Xjs9;&Z*H?4B>%Sytl{55Z?}ym1+6
M<GdVgS6_P7;ya|<<N9R09>iaj}+=g-p={R?J%mDO>zhtg#7}L`Gpx_RSid`#AEGBy+-z~MbBMgIdHx@VN0K>BVAq|A4Y^3RJGo@
<{A4NQN-J3yLq}|*uS~XR}x4L0m3CX$e=%3N4k~_Q$RYUup8x%R8EOy;`#GnTHrp%9XjF8KOO%JnQ~-JYPjMk6cZB7Gr>44gZ%D-
1G6e)oA=NHoELTKxfpic?N<WTigPVeXp}|ykII1)2?^UklBHWR5!9#ebNg``XHt$!*i5Oz(ojm6e(zfSh8ViF8m;CZGrCT<%TTRT
^8ZKzJg(Cg=SIG2=y9(lTP}=<7QIE#*6R!G3`CBAb<5^bfi#em;3p-svYBTWT%$?ct<PN7A$6~9J&eiC>6QL4h15BUp=Qdv-*}LR
0}iw$^;x<Ji-rMixJWYUxIjQ+<F>V%i^Q&t5%2^nNXmE=rF}BbXw`psC!3Rt;(j{4RD=Sz7gdGy=43lUgI91y;<R$zkWl}*K|uTA
J(ZmH8?vXsU-bG47zI)GeRa((H$X;Q&>Dy3cb5Sjr`v*csE4j-;s%yN-t!hg#Ea`G0lUV-t78fo>~;?L7iFyYEQ;I8Z1Z3lSWl4F
>1?Bie;7HoB}U_?6z9is%W7`+e<NH|OtLvlQg~i;ay!WZGcoX!jGU}`x%+Nr^9TUNfHgoyxICF+N1(r}C^HaL!}vbFc?axS`ORAf
D8dO&9HdpXK#Z>mX5d#i^87Ojk(iy+|13_M=qVL(bhLQipil%UQfA~L48&AF7`dJhF+7~}vAV&=d3+9^#Y6-}fieQN3^5w{Uj2Gj
abw|{(?kD}Yw?fs!RJXVUp|AGE;OHjJLHJW4LClMb6*oN`(JE?0j4}*rDYnVF`W{XsuU@lc-A8XX~3xbyU{7L0Vv8qAAIGR?6APj
{ywz30}UCcX`ouU860%gH}e<Vta?*bA7l+x)kQDhdgi2V4$pE#$zn3aw`DgxUKnyx?Ti%@DppA<!48`3oP%9RpU=j52(s`hluO5?
W6qw{|EA}HHbjSe4Q^jI#I%Ko<W@c34CBAg3eL0bg2qA&u6$ACOxTuPRQvxrSnE_rs9(SKb(qH?4`90ZP&o~~?yL8?U@~Tw?OGeV
SKf5w-l+|HW0t3&WP;iSgPx8M5Sveuvx7F86O%Yj8-|Br^;>TVZuq!-Pe5r6nV7(Gq7C}@YgWdoPifh7#*H;oY2fQT2CTUiHN=zi
MxbM(s!F;Dl82j&Nis#eSSX%PzC&YZ{SM5@|1<9!C53?{^^4$=7OlX5BVf^YBtOB@qzUKYQbb&Itk%W-|Gr)aeJ|EH{w$l3V$1Hi
kn2AG=RR3>=W2T4;5y^(NbWC(+KLF!`=ag^Pj_7@ywU<nJ|N_pD%Y9HiUES^BZUK%Wy87k(19Iuj;{MaY-q^;<jJa{cXpyD&E{1>
5+yb9eW1DO|J$7DKivRnp1^ja@IW|l;aK+Mo~c#~xQcIh>nAbXAA*VG;YnOI0I&jGlf4Iv@EhGX6kM<jyZEaAL?AvZY~^Fe$YWn1
Bi<P4@1ibN4sI~+$D937xXHfmTyaa<J%5>Cjlk=uqVt8BmvY15KVZrk%K;WmLl6UsK7FqfBiRTh{f9IepNaKq;q!Y`sRq4Q!@JXh
@XtSl1B+32!}`p-sBE5!H2bpb(R{VIo_467YZjaSd+%Y~q;#ax9);zKd>lEEgkZXye3fd7z+$`g`6*-HP`!30c~;y>HA1Um3f%Xt
>;a*SF?;+d)|{jAFg6;wb2!k+sVWyMtbC;TrnvdBR)^ObNA@q4z)(16&5!EneOAhMFjNvOPLD`BkFnby!$vHnTIJRG&NGRxbvy2x
_BRkx0Gw8hi=b|BWi~OGI&xFIuP9pYorJzN&vG9eeR-5Z8bfR6B7TomHcQFn_e!gp<ht<>1;4)-b!r1kgW6vTsb|DJ-aQG46FR9w
j}fxtdc=yFUyPy}JBIEkoL=Ii>u~?D8ouSogMlxx-B~MkpI1ftMxt}}Mbo087@R?e`gzO<N~(4nT#KgvXD1KUfqkZtE=iG(Rr_!*
TJ^)z$@(qb^}+4&M{3T$`nh+-J&N|5TBO?>AQ69xq)IjlBdXD!`mQ>|NwDUxuruHLeX4>`J<izh8Dq|L?IvkoP^YF?xhS8sg9#^l
efRUEjwbO18iPp_0wY54HC|E)2bSkn9hi_1rOm1PL3p9>+_p2i-;;YnS1JT9n2d!uq6*RocLH@atv=n(EdQHnII2VuD6Dn=d|g!~
n7S>L%?{0M<<_&OO991!p~L7ts9FjjsbDBaiPO{iP3J&nH$<x?ilji)9FKgNU!<2oYTdG+#RG~d#@m6_<haydxq{R?C@{ZjHsth)
pH*!Q8vb=3mfAIZ7mZOT)bQ3DX$8gC(y3X-jqN!wOLW-kx;wd(=%w&ha6o|PjcYiE>)p$nFRj`Tu7FTi3ek-w)uP>HJQ&xW(k3e5
P|csG1x#pYz9?h4v!i09J)h<oY}Tv5)_mqBk=IAKZ=fN`4IAA-zz9&PUi6V#2-4gD>mYfqJb-#*&ikdB){?n&w47q*#YSHOm-Ln9
-)`?~<62Lp;GUh;$#P{6nvk)ZIwkal$Dz@GYIfQ1TkT%PRnGTmLSqLg;H&Ul7Tc0yQUDV(6M~a?B-;lOaHK8@freqezXQ6^-5#A>
-@Iyb<W6O^HF7R<Hh<$?fz;B5o$GY&ONf}vEPUlnY3}5l=4i2qWcX<rZRTOrpOfRPeIiAu6VT$AE;&JGNr3f_YUUwRGwk&J{@DVG
*c5tmSRZ8k1wjMlO9mA0v1PXu1813tY`T1Y3+c@GU7vet5B}-n1jROt;nKlxRumCTgIRLmbgtRaK_lra(NGZF5D@e;PLP%wE4KNf
pAERGLh+h#;2}!oj@?z5&!vSXH^UBSyW48KChOpq$`)y2XyfgCVEI#mUYv4mS9T%t-BcKQRyNu}rEta4eKSE$dk)*XD#-`1QxUpv
RGgq$q1bjp=1UqHw23W_U8i;@UjtVDv09HzUdCHZ^}9FKTQb@uSF+;55hNW4P?mPY|N4;-*Chj2P@#F5=9|RRz9DQ`YowYN^xEj<
0-G_@GZrJqAZk&|J?NO*yG-tgN)pv~75Zay*=sHM%iK3GL165($1YjT>m&x|*UIWEhkJ9bC<2cqod+kh2{vWOuSQv<Iq#Ci^-iKl
?wtD}#imsPPIeOqlx%5gglSag1TcwUl}7pA=E=kRkY^8z>s&EJQ{b_U@-VCz_(|M?3zxQ~jIju~2pR2%G@_(qrw%Iv=t`*=9BADB
2Tj;+kK&@TZkIIUqA%}jYgu{ea_2e>rH$BPiCryZWJa^lEHo*Iky>j265q1qt3Qrltm_f4yO$HYW8_dD!ZohYy<D1S`&5#W0gwL7
+-IRV5(}@u73_5VrUvMHNn%A9p<aQX`f_?iisno5E(P7Z7cX|ypV~euro;7L_>99}AfGoMJJ3c1{IBBfmrd=!=zc$|jo#a2^`W)q
IfHt;9!e~(eiWFs5tJA+$gSFvuR4X6NICCXH&NN8C+GX{>MQVisZWdNi47+?RJ@Q3iMz)|ILh3SvRKTpSs)b*7(N->Sd9naCL$nG
O3vOeG1$H^5UYG=_vIWbYAaqqT=iGo%W2>=!sZ!WsgW@_2H`+m_7A!i9cXWIcqn=!EthOUy;LOrS9=$O;=9XY?7%;jxoH1jq?K=}
3D6Jz{Wf<ajN=vG0NI(Yq*}w?%NKb&O+2d(fA0W<=Ne>g4L?tm@PW_G8O2=AE^S1&Kb_toJmUL`PCKDl$5@Xb6=MZM5mn|QrePW%
=y7H>g7Fh%g41;LVYm?b8+~7>GgorsVGcYn%Rg9HV2su?r#VVoMGs-iIDx9<s8)xLcxgex-aCg}w}d`;rBBQg`)G$|LRu$>)^jL?
P6^e%i0{S-%Cy$9X5%)2-%%~I^B%bG)C8#4&__=F(TV<AfL^MX^T<yv;*|!dqO?JxsH?BwB$60_hIhuo=j$|s8`3k15po<cB2I1A
So5bT<JW(~z;MDH5cyulMk46q%3GCTU@HZn84t2;>vj^=%14Ld4E+erB>os`a1v;Z$3YD)wp-`L>Zn@FNgq23BOFctN}Lq9V9S~d
r13bh5XkwD_6}NbmA7%Ss(~ZDo0xa05&36sqR}izkUkzICf1fh#L{j(LTFDLbAHFZ`wJ)vh(hQ<#&i<o^v{RdahdrNHBOayNu=AJ
?s7-UKn5Hl^WZNJJUoP9_8hG-bdC8iElgu;^J=O>*S=1?Fkw>Bp2Hs<&8|FxYk^r63vcq1y(|GwTe37neB<^$t4FMqADSj-^_QEJ
5t!c)BmzRyiJvLn)GpA%n6*eVYpSNLnKbt$9^pC%yy05aQ2hT{d$@qeQgJCU16$*)azz$9b$u5z1M3I@s!~J4{1}6so(I-ldvAV@
!!nUUsYh$At}k+_lKw-JP)SpV@R&*@sd=~^DN=!es}4yk_&q400^hixp2W~U6&E&?^hsJq2C1BmAP)EH+?bcTAyF#1_|k+_N;dj%
ss0C{jdWl?;{V75XQkD^A`U{P;!jfJ6p)+f$bV{elJmLGP7Kk@`G@X;eu4gGW7_aVXRy3uXwCxtFYGVhmv$GW@LGk<0@vrbUQGmK
O6mptTC1-Dk$FwE{e#+qz;NTo#C<iiv9Jr$Q<?O9DrXPIC_TtL1^pH$jVSH-B~RpIj=UFLPaRMe1PW&beJ@j_Z;c1;WJZstqd^Go
&6P$cxTn2I8VkqY=}_B5rO|S0)JO0U&jeweq16x`0$jLB{--UX6d0WGBgher<4*6>V{B<Boqph^05Ht0T!;Vr6^q!;DSr%+?g$$o
Aw`cdMlr0E7K!$rDJsQYjUk=4vuEEk51JW?TQV0ZuuspRu^KK$v&kZBa<H@NYS`64j#p#P-HocDpHUr%Vrr;xcGX5DhZd)-74>JO
kP-!-_U+w$9UF{SZ)<7rLKK0-_B1|vV}bqD>N>QhE<!0aO_wU?F<qRlPhgiJ4|d)GKTFIm$$&5s?+{N4*Vsn}r#}nM-sFhg)fmwL
nKq9t@sS2#s^!52mD=WVRFjxgpHYt8f(VUUE+%T#lV=2T_!{_5CyMSr+bz7K9OFB^XhK!I%eetmod~Ra6WKLZ62}PNh+js!@;3M0
eq(z8;wTW|b_p#_)3&bin>kltjgo6Ov8M|cCV|i5Q;FY}7dXFi>CXLbA6Y4%x0i_Ok9AVObkZyZM|#Gk1^`byzX@Z#>m+tTq*%EW
rk{fJQS724R_g9~-e&&Qz-7q(?2T@nw(-qtgQ)W_#OJ=^JtZFN(B~3ZKBt3Cd!RX)LXzI+HYZJ`&svtJDLq!}1bqu$u<x2d;~Dpq
`i*In0VR4~4Jou!XQzRhqPxB|(tU5mLj@4eL^<X;Yf%zv+_*Ue%2+!UzO$56t<7KfWukZ;HWnW3x23T*A3(Vh*VaEEbOQVZW4ftC
`bQ1(j>1=S5Wg2+`tM?L!>^q_(s^_!@+xGJWE?*jjZd%Dn$_$sIKIu!q;9Smd0FXU+%*+=3WXI<WwV4}x_&^J{}3f2ajX|BIOfti
2kCB_rUk~%-c}mwCVs3ua!V$LZIVOH5ubHFLn^b}395^AN5(}%gl=%I7cpJ#^u8gT9QK;hP`>Do_8XkYdE9TV)pC?8rSc%szv}3S
6VoQc<L{lS@^uOL9_ulhpg5AwE+WvyZSoJ2RltF6XI<IWWPeZg)Q|G}1~~!z5o^d(uo!QNEgE7CG*;)7T1}N+mGh=`7zp6!K-#GT
*Kv;gSny0tjtOkdJG~=F`|I`Jg%9Myy;Od3?J!2A!#4f*uBr5eONxyP{Xtjva9iEnUTQH&%4jmMNzIz%+BZt9d0a!yG;8W_!&Z=h
q#E?`kdoGCBy2Hidhobvzu5lAK`1<Ixrne$h96Bi-@Ix0;~b1JFn$R>MflQ<2hPa}+dUrJeIrSzH$?{$zN2;jabqCb?OShr7dA<A
cYsjDL6EK1s#7*&BO2PWha!)b){Tt0*ouolDLMHidpE<pcbz6G=jMX$={m>W<~97r6NiFR67!Ginc+5(tZ!t~h{B+j*l%U{jt93f
XuJZYZXhW$W)Bfmo{zf%b507<x-+-buFjzbE}ON78$A5=9TroF9<Zx&T8G;p_vourIORMP*!{Xc-uaQllfzG+YS;xYdVQNU7|>r6
S{;EX-JhEd4%oSgcPI3p0tNDatKgaim<181>Z|U%Bm=$r6*{%XR4|Cx<jF<=s-lZ`-yyt`1y|FM6GwUW>?%?MrTx{+Z`49f4(>}g
lrcg`0dtiy_*0f##T5Y;m<@CsX+x$CZ_6i0YtJ_RgQ-R|5F-@Bqjt*8wL04sw}1we+w`g=Tk1j0k<JpdVzLKA?&*b|hyT8gjiJ8+
uej!4BCnTR30~$k4{O8na6+KA{I9m`1z0?cdG^{UB%DM|`VKVf@I@D4&JayV`EPT&)RIQV$WaHLM4VYzQrPKXG~Ev7NJf;3M#2))
%Gvp?U6lNpu32^SybjpnOXC=~EBg_yi<I7zEz7XPkXC(q$qJAGfeo_=9uAGY(;(yVuiE6RNB6W+*bW&U_2KJ<turrLn=`l6kMueC
c(}%NvbG?f1h%539r$x0ZX0YNe4GA89^s_#xLak)A(!AvC96>Jf4w7ji`4ZqEF8?dhqf25hf}<8{|#>?=L=yb;eYsA)n!nO=TtXy
rDd%m*BA=O=-S?H;1-fSNHnUv!Vs)!iT%qf_L)nO!$<Fsa6;EKcDVEhY96@iQqrEp^iSjGei3CF#4_&V7Jl;W;*!E+kj69eRKOcN
R8?VRkg27)dvNoW@Qi2QXh37B*h(EZjp|P;BVxBDwT?!Fk+^#tbl196eUbk>jq1whg!(Jm8fqwVOfg)3IJDNjT<*I6=1exdli5S*
CI%S)016dIy~sc^@SYc(PJ)0vu)}Zzc+jnj8Vj(qljGdabQ`vewDT0_ar3{{sj%$cUNqMSG`hg(kviOfd@Te}zh`Q5?E_4ecMWQ?
fUIFh)>W(wASj~GD7$Fqz1>d|1Ed^xw-Wu?5qRF>Z;h&hrhDiqd=Upy5m{fNmLD*h_wZ7=8?rh<?o0SC&S|&K#=uNuhv6eg7$cVM
t|al2x%fBAxwi|2XH*0@g;?m`q8#lny~byq=zo24PD0{k7jN^lPLoXtBaaMN>r1`p^*(+|WbD&`d_3K;h90f)FAzYfB;YvgvCclW
Hd!ptPuT@z6BOZ(X^4JBN4^2Qt>NgH#EEQan{6}UkFxX~$lFv?H?G*hh8)Qjo`rpzNP7r_R)BTXU0I>A-+({H_$K$mI8l-*rztFw
C$E8uI?f<y4TI0Vfh}ZTyttCo9T)j8TZfWZJ<+b~`839kMyH4v9jOvgpy`XeF+`!?xd?8J@AX|%#22GdtT^J7=Iq1`8Iq26s$RP-
UT&fEhV2yNA~~UpqV|H%a^1FS3KyNr1EE`FAa*AS1V%G{#)5AQKz%xiovii`;8)oDV;nqTh%+K6kl;V+@J!IW^9-b_FZNJ_=Vt~z
O9sYmqe?;h4WuJ91r3e9r#<3`A;y^;p`Z+)(dBqWc;!l%rR#JEFTUdPP0ip8H?CqzV#eutId`TT_Js6Og;-<z@Oh6}fM;-_KM)^I
+rVp7oRw=k)Wvev5)`<ua(It(&BG}yiIi#^*L^y;d6M=*amcU1(#JK@w5O;zbF%9GHmva!7L;GdCDjI9_0V0<-}fh*)(xZ=AMo)x
L4p#mdil#&3LT+^{mB`ZRC*lqdlPl17G2S{MmO)g@w2`E5vz^o4)R|)NJQ5o)gV-ktrdw^C#ERS1w7CxFAbn5e~Ptf^`xXtZO!%X
G>Bc8v~v#pJvk2>C&OOH>ePN@TBvM#^ua2M=z?j`z~o?{J-mQfXb?gdv?SvHu&PJSo5KXR9_v*nFkS`epx(!d$;l;+ABd)H*)r8?
$N9!Z^Km|ThCilk7h>FfSGn2iWqv(@?UJdWvHjpl)F1-`rvx@I?x~q&Yk3Cy<)^<->gsD5{H+MU$6_7czp?q+XQ!MzszdZe<Y=pm
XC$NFoOKLND)Aqy`aptIhnNUaNw}&duY2W^GJYfN>o+X5xBM_$OP+I50{8+#Xi-aV@_+tI9+G80Uip%oJ07Y_cF&ToTdaJ3?)yet
k6a*Ofp&EpESdCC7DKg}GGHmHxor&0x0DHi!7VzMi>|*Ku6%Nn!KXTg_7~CR+M@lWK5PTO6|VZ<l<yd@BRsA~U|U^P@CaOmp5$Tc
$L)e9C&!cqTAfsFAHP+I;e}4l^n!<Rb54v<<k1Yva~9VR*42}$*hnZ1p8}K?`o-mac0jA_7hrDtcNMk}3EN3yQ_1Gn=QvZlb92=m
AdwD#hzNypA>XH+(Qe0!!*i!ok>sO<pwgX{<%I{hdIS1eAr3;uUPR<GzPB7|kmpFh9kb8IAfS9Lf^%E%W4$c@G6^35`603B^&3$G
@b-no!^#}h_~55}IF(pIKMMV^E8t3)h{=V2)`QClZ{Xw;l$wAAvh`SZAbb;-@{Po5rhAs!Hq1XK+lIygria`9Gh%!ZKTu2;fO@?A
!*y2<0C;MZIdr6-TWuvHPNDtXeH&^Ns=-+5*S|&CcTcj+`+rt$r&n6(*mkcSCh5moxNXiy{Z<8XODeqOxE_^>c1Yj5ix{R$JE@c{
WVBovLMO`_SDkNv+u#=kR)a7<c%g+?mTm+y)3Bidm%K?&CYiSFk4aITTW2MVPuRE0e4kIDHLMJM)f}xqRP%S;`J^fc2c_X1ap{}{
fKiMgIpk~oTQ*<vjzz!0v!qp5?X%FVD1a^(e)3&Vw01?f++P0_6i;xa2h4%z9B*?~3*Mgi!Uv!<xe*{%AOkg-QhE&jwjKb05%?dq
K{6u{x(0C?R!10!8o7b+6mai#v@epIR34^<Z|~Y!6O}vUeDM8ZQsUJ_X!NXTgU6>Vz<bU!N@_5g&ht$XWN-a7=L<Z(RichK;NTj|
3Xv=x(RWiP&A>K+X8nhz`15RYlF<9=ozd2P*cmu*mU*_g)pod_9#jh>7U_Ye_dR{wvk8Vjwz{PXb>0*%b_Fd~q@B44vyY5`7G-ei
>s0YD($(CFAGrPuLFJWrHNc>UM?#m_aJr+slFQGug{vA0RzIF5UPvbI+lK6}M5dw_%t(C!ycY17Izp`ic@8tK8ucwVIRb!Uk_(}=
i9ggwOb}Qvzn4aCfA)7{rA{60Kkrfn`)T>7x-F4U;T(F8+?8mo99DvFugeu9{)-2RzUM;mMUtkQW36~o!crRo9U<@v63EO&TY?}U
bed8o3s9atq<0{V{d1YUFT=V?yOgjO$%IY}%@kRKLh5(vt7&RVQTe>E4%OqO$XLi7Xg6=xNCGDDM{_v{`;FJ3lIFKAUb*<7;J|e}
Cem__-e{~p^)s@H%bT@)%^Z0=5JBBJGLK_7G@+-qno@p7!shbRj@&rx^08CAFoikZMHuvL{!Z7-<Oy1Ec!-llr$kOGWu*hQZgY}v
^@KeU6m|M<%HKcp=z45_E@{&GpNvLX65hX@u}G+Ukq?b)Bt3buaMCYr){bG+O>32OwUaQafq79=;^?ehdQ3dkOpoNE{6hwC`DLHx
YslENXPuVbFJA-8a*7A}BD5aRd80CC0=!D3acLl1yvf5^@gmjYE2H0}X%W^;$03I^LWxK85_W!vN-}7<)!P&7l`?FJ53=!l$G(Sd
TDnNvWjn<JEJ9R_r$yq2F%+YF=k0<Yp^va%{9l3I<jG&G6z{7$7M8yw_;sKF>QtHb4=$1T<j0fcO^*B1cqg4M0!5*!aT7*kGpuY_
6XR~g$&hl{X~x6bE8;u#UNFjYBYh?*j5T;AjTa^gRZY8<T=W5ucfr_N8=CKZVVD-nnMZy*a8a3gz0{`mYNaGDL%)S2N!pq`J@J1V
Z&(Gceyt~3_H4P?fqo19x4hZH-(&R(r2(7oQ61e&h3+K~)aW<vHgLH8WRsC$LbFjrP6*GN)Z#=KGs@Mjf$4!_-4X)y>BG?n25>vU
w}OIep=qQ<Of^ign-{0oWrZsRnYXO+8&3dLmVla0iY7HYHytO&s&XP?)3#83snfe$k|cM)IA3asf}J^+>?K+PMam`a-kUX@=hmWP
RC_7YfhPMF%hR*wAuYf4y9E=@?chl5-YT`W^&?0QvNr<tE63*Ex1P+&av3b8<)B=~&3$(ai_E?re9IpkwoCM<zn$k34e}nLiJ-}_
xP;lk_Nge@SIJZi6*YJ(2|U_DA(4fRv6`8^>tUhtC7>SnA)VI&H1KNW-U>Vk(>A@tBrS(3>I@#Bx`|2cr4_su>JJR6gxsH(oS)t}
>tQ>1&9bFH>YuxzB$k-Tjc<#a@pEu{0uKb@pv&%mX!&wzEk!BmbRi1a?lwmi@X_z42N&l&IaVO<53j|ax~!Ym()U8wHhG%ZV+$fB
cxYdrp{*rdu*ehM{OvW?TTOmzndX5wcO6EGh#x6~r$e#8+Me@tag#DiXevrL3_x0BBh2HESbvol?#h{1X6UeH{)T)cM@BtcMN_G4
F-<d7ik#a5<k9PhwRY;m-2Sy$lzS`0iT`L!x7$f!$3=M|Wu1o6ZrCZDaE-t`Wo>tCEz6lQ_gP^t{7)*vgh)j8;*5t6S1|T?Vn=rN
11z<v0G@RdhQ-T%zInW9$Kg-n`IT3Tk$|5g|C6uOoTFNb3lJk2`=aP?%l2H*d!c^E9*a_KZue@~yP1nodM`$H;J<yGj-3&jR)Wr7
O6-NL0(+ChZMCeYnEJDx+xjJ5ZRZY3LE0Uzg(qOV$uDQWvq!romS-OEAU3Cme0$hjY|w9Q@1OYo2;=cU!FoTCX;ELZWa)nQVWa@n
JZ)jwFG8R9f9Gnar9;)$4my4@c*S}Ir*qQ6Njc<@^ShX##<hlFP?|^ZeuD@x+$!BAJoLm-|0M7X3>@wC{U-FUs|!C(Dj+9hhJ-&P
llAgfQ^BJBR!>L3_)m>{T&v}2OjY*6Qq9-oPX@>*4p!eq3BsreQvDkl$6h=lPH`+FbTp1FdcXPTBY;twi44m3X?2_nRvNC{3c;!@
su2gCA+pxJDZ=q)8c4mAu}+b7ivJ6rc&HtJak;%kijaWI9=)imc3W`0Hiy9lM)gCZ;4;z#x9<6>2x>$Z4DgJ4fv-~|K8X0Gnqa$P
O=fTK;(th;xeUNnQ>>P+<XRx`N<@sZnE{Bzd^W2)mRriX&Xf905y?xNu~vvR>uN0tjWgf!(*+?OkzPLbZksFXoNZfzJuUp=BB&Nj
UiYXNVk*yREeT(;lY6ic0TVoe$a@KwYM~<`GOpJaK-4Tem?ptAsmb;@I_BMM)z~NW)KA&|;h}2szuN8g1&P*G>dE_AQ6Len9AvvW
e>Jv81f8hn>Wf~LVkx02rnfJcwrM_9lT8;MJ%Mws^twqg++N)@=yDMn0C98l3{g-#l~AObo9jLBVV>SS(<GCt75g|6RQmS1Hsno9
#LO#Tr0op9IU9J1QB}8cdW%Cv0a?blyus)3cI6#%iiz~~E6a18>Bi9cG9wCBx8~;*yV6-)j%8%&34GghQyxAGn0Va)wLF>}>*<4F
PLTz)YQCC5qOzvVB&gNj&>XhbA`nKKkqBVZNYlO=zUC;?ke0e)#E-n1k-_$#8vfKhc@%eM8-8=u^<W=%3(-1s{c!7VVcAb`Fa=cg
e4KOC?~jzx;GiFCg`O!wKl;zK5y`rv*xGMddeBTXaV9*TQ_=Yldm0!&AGM<B1v@_x$ni^XGqz3v%5?y&{X4<+tl;#B$nBC|5csSt
28a>cDW!Qj2Umdo@X*fbz~{@-K1pB&e54$wc=HUk@&&tg-K2XQKn|c7g>hzAAn|W(vCb&j%9MH~QW?%7rU3YD7?obz&)NriHgO1>
#y|hEo6iR7+-%~C$Y^?;)1oj<?z~z`e9V=*SOobrR9d$M_$pP#TL|-kf@OSnK3T3{*4;%)96w8rg5%yDG#g1bwiS(+@nl(~0qg99
ezusP={9OwF^#mjEzSwN@FX`|*)p4*8pd$OWH&s?wU=oapb!Yk=0v{R*uLQNRYj$l;8>x<5}JkPU4!<uAQg`SjTiGd>x7-i_ljg*
Yk<v_Ta3`SQXk!hM{#0gk6vmu@jfcaL>{C+Vd7=%au109_S57b1dc{c_R!zxiRProB~7~8)oh9gp7^f&I0nDFzITe1P>z`xKuBP5
1aNYX<Coy4w4U%Pk}fFe3$sHWgYO;ZknEY{Y6hMa^XrTYn{*<X4*Z<gE?cE+i8*RIHZE4sRW~PdMxWjtJ}AZ)#|0cfc-a8f_Hy}P
MXkx+n|vDBp>$W?O6F0pT|t6oE0qL{!_Dz5n_Cj0M!$;tm5yBzEzCL1q8Is=Fe@tNz1vq}(%JBlM(5ecQg%y#Zm>O3NFATK7SsC%
Cxk5>nlyk`Z!^B}5(_2|MSBfb3z*cPHQTRl?qHH=D-a?kRFc(X3Eiebi=XWrO2BL&5gmc92N{pdhtVg3h&Hh=TO41{mEOml#YOkO
5$h|DrboeTcuS36na1SO;GZgqx)=&a-?s?^9Ec#wJ343qO$L6U7)>wpVssUlD}nNaKeRFw{Doc|UfyoqzX9kAvXyH(rZZ(5@Dr1k
@a*OgGXPe9QD~84_;b|FD-ZSEe4fF0slG>iqB}*9CQ<*BR$kqNtbadyh6MOCb0n)-%0xQ9V~{P4W4MqR<SktuKFg0!2JzoH@jd-d
qnfo=QUPTx<(QNU$Kd&cpcR-s$!9$l>@WQS=)rRkncu(m-`Pxoo)`oCSlKe|t<U)tO~+0Ut`XwJ5MStBv=(WkPdGvuS-MD!pN%2g
s7a%Zjh$(Zo37;Mt^@sP+gj<iDNC3br!@tE{COM>no9!b3@L3Rx|T)7pnU1)Wr9n9td*15k5bumC>n@C9pciU%jO`}bcCxhGQ9i;
D}!IS^G_=l=ORATtVb&f>MQq~$xKQ1g)19qy&jX(8$dY#1Cgzb>^uC$<LN8Q2nWe|Zak=#mqunsrHY*XCR3m|NPyJyQBMi_{nt$e
BNEyq&a2W(P3PnRMahapE_NlE)}qL@+Iqzp5s4L&T_(os%#TG9f-shSuV*E|Ig%gygg>Hh!7UZx;rTZ?sq6aR6~+NZ>Yv;+`pU!*
9V(*-s9STa`!81AA>yUZ^U*_R$OGD=quGNrJ;PgUY8XGu#cU24$UEsD*CO}@)~DO2I=fPXWX{ngcr1QIQw?GLg%k$YGpk{(v++vo
x;zU}YS=>*hC1qfm6o@Pf4ozuu%!7J-KS=4ldr$m>1<IDkI1)T29ttNtbR~@21=>ZV5+`_c*PCf^{X@z`iYsiqb#QXfxg&|!2EjW
5t8pQ)BK{Xapr9prP)l;MlF4_$5m);rJCRH`5GK#;}NwBnuuh%$?mTSA{U(8+dRd{RE=&<jk4u@I-j55kP=ZTq*(3o|1BC49<b|Q
$gK_Rv=%Jwl_a#2jy29jPJkUunDkxu*u%F}#lxWl6v7(*$|oV02>QlANR5>>Hm%*30vq!xQCL5$CYyj9a-^%}9CMmZX6#YV0FbHj
h#idLFe?Xhpww(LtO6JAv(r`l)&!O~amOIXN#^#<<UQ2zG6RU!JJE&3dsbvuMYL&Lf_qN%LV;`P(PtGUXWS&d^@L$FF#DcTu?+#f
36(JWYE{Zgro5muim3XrsOoF}-*37UuS`;)!z|^nfnYX+wpK%Oml}J+6O4_i?ik{->n@E&oEuus7;MZJB;+z$jW`H90iGl}t#Lay
&oG4If@N6y!i|)E$!%`JYp!8Dgqx^5Nz(O^VC$vVYCAz!R#(yZ!LO%k{$%~$Z}2B;HKj6p-$Knsr79E+y*1Us0Xzn`h7!w-k=T>`
C-}dgnsng#>Sn26(7tCvDzToMER`eDQiG!Q`u%O4sc`H)_Y{c$LuWbNfug3nTEG?T;86)dfKFTC&m72H4$O=A!#<y*kEJ;Rgi>y*
iPMYyZ;YLy&{*qFX93b50jn4cohKRm%03(E(XF55VeOT>wtsGEn}r8c%L4}}vrBjO1@-|Sw!ds{RO`s`(+Q1W2<e1&VyE*6DYSfD
RT|cXS<b|9F!||`wj(Cz-VJh?cFb%3A@#uh^pnU%7Nhx1zTq9&-3nKUws@TJo70ykf%Mu4{zN!w^I9yHMER8`=`%$dag>)L^d3Yu
xs^>qZ)-=-M!;`bS^sOI$+>kLrp<U7wq!JLQ^I(!^uufEK~9$#lTtd-n;;zwB=YEsG=405pgDEaCe56kJ$@>0_kiXm=oJ2NjMdLH
wV!N8bEOY$Qmu%&uAj8?nA@RoTYtYHAHe{_QvDXKi)lOwk{7$jGCXOCr_;q-N7If8D>&&lCwM;P1mM!*uPUB4-zK)!g)i)W=1LY~
`8HFJDpxJ|IP|;xY8*uVUDT?GcA9|>>4cY77Y1#}Djry(3JDut2jp#L>b&f%cTLS;KwGHQhI;XtUnq2|6V)H}gNrVbywK9g9aZrf
E^V<IZ-e<zVY(2g^o0VnKeX=qQnOJO(zfsc5WYGWq_FcJ)n=aCiigohX<aYD%PR-*{<z1_Akt|_U?ot<SvM8iZm{t=PQ(E&+|=&%
T{#7pyPO!LK!9{2>Om#s^)CSXoO+=7uWloD5H*^ig%{#oSAJSIl6ZbyIT85#X{#tp*fxuNs<43n7=XOnkzLm!;DzV>ESb!n?@rn)
KWv^AA^1}4wK!T6R|7;j4!X}7+N%EUVW{X5bPP!{``g!ff0j6$JGWd+b552=@>IU_@p1AtHzaY@=)0CfYd<-8mt&GxY->*JKUJQL
F#BtM(yJ)U=>mT+xH6!q=Yu&RRk(db4~!(>OH~5AoOXH0Ph+&W8yK_f0y>|nh{6P<df5&FD-kq4H;G}25i2ImBKRl?5$-o2G^5el
hsJKdYNl|9q!!gXz@+sf6c!r5#~YMv-Q2UwAP9TAg}}t)_n-GyIeHFj>x2>L!H4EW0)sf&Kdx4!g3l!z?eUag*02`}9lqzsNf9Hs
g;~WgLD{(lL`7PDUlvnp%&00Jj#4_U!WUgi1XXzlp#xJ`K?sJofT4(gS|R!UtX1qhTb|J6fY>syI}J9lygb5&y%?ZylTyxUYn|1v
f_#wP!}d@@oXGTZoDiXh{w^SU&(RMcdmSninSTAJp8J0AL$K9CDvfE+474pnD-XFEhESMA|DA_d%zM!BG(Q}8_hYBi#yu+{tCgs<
HUDclsIGU~<NPW4gr@DCA4)iXB98B9Ys_!y(8(FXMJsH-XGs(O8XFa{fVx*ZPJ5N_a8q^0E$vv>fX1eEAxNn_9(1u77uu^WOFQKi
F{KTQg3wdbm5wpD!Ycm1<cALv8u?fVG=<5~#J4wC@K!WO8KYP_V6<HRM9t6kKZgwK)IT3_EiFr9y^qVsq|QPH3B7A~zGR9LBH900
?}ZLsyoB;0f|~!p0p(BwPD*!T<ik2D@rnMvb6muve%OH7fK?$<MKV<j*hs}~*kX?FA4H;dAxHMo_ejznfT_>yZoH3+-t#;kRw2$S
^mcq=(%4r7LuD=xgbO6mVEWJoM!fp#DD>fP`FV=T#<ISr^F)bk^e_NF2MuUYvoZ)Z2N)ns^=OYDjuPDhX68<-KhrdFd(o+CvS-2V
M<FkCrIIUSH@tNt!Ja<R&bS(K?6zXl&VAq0Pus~E%&Xv6sFf7lbIN<PS2N5XqM7(!(S)m>&gHM0-C8!wOzUQUTC&_4xKTwKqe{+z
-dS5}PB)dM@j^Ya>RJSF*HkjdS@Mw50k*OOf5s^p6Sj$Y;+(cs@Qb_F=x4rKUBtF7BCcQ<yU}5%E?S|~1S`KncwqSlO^Lm{A*}R%
G_B)PnkAgyY9mds;<)yK7@hVlL&v(Y@Pkit=-kB<`yjO1MDI6N=FqU@dzMIE?A(c#+G8`JU<uKuWTDo*zX%12Mcrkf0()eiFlvP#
Vd0h0{MteNd#V)SGFRB&!Zh>@>fBwRL_JJEl{q)Be2yO7jQhC=8_k4%RjtQrf>*s&i6{)eV@(y2kTGC!_bvM+s_l@4yXdtHfHC~$
DmhD_f@9hkuK3wnx0qY*9=<NGHH>z#D~O^C5S7h|>Plcy5=BOz7nxmO$`62$VYJAjgZ8|LkTW;i8c}q!bnB>P@XagTegp8jY&kAj
sN_1DvtDHHbOUKGfl>fk_i)c;f=AlAI&h|Fx3w9^JmX9#?uc12W_}}y^VAQ{;A^d5@*6TUj$bBF)nqXC&B0>BD3a!*a>j3b0Y~N{
cq)l<EXDw-JGylH8xTfJpS#JFK8hE4mfkLoYjabI<+sam)U67lG*0@&ejbUZrSt|?8zj&8#e}az#BmK|TY06>zkU&BwmgU3%)=IY
jy9zz@tBC;68^_;$fh{9uOlAevyKwksf!wm`Y5K(eUZs|puidkQz=<1(Hy-qSID?;x%I&0JI8P_3hgZ=)4XxxW**X1B$l}1*Q71u
)kDc1f%$?zHHzmAc@LgcVW<_zYrN0QFF%pzx4u$Ze31+MF8Kf6I`PV5sq0YbRPcJa8$wXNo2)~}U(T?QBV9*Czi1zBLcS-6qpS!C
4A>{CYRxm3pnwIU4+m8<Gz&wVW*YKHM6O^n)U(=G#%#=dor4ewd%se?CvKL)TdQw;$iQlWD8#AD*is_>`JQuTpJi|#!fDvQ$G>p7
8Ag;IUL;<vLP>j@zkIiY>;%443201FgwKuP_Gjxf=jNjFQXtzD(bhGt5rNhj1vxR?ck?2k2n!t#+$Ju80UUalbKLfLBdl`;Bw)vm
2*njq?zVG(QqwwO*c~T+cHn%&v;bFmg=e%xfr^D?#lyD1Wb@L#sZpsJEf|jJmeg^oXyoASU-rlC07;Z(yO80byW~LbEX&hhuxw++
qgZ@x!x>8j1E`7%y$%}7WgkN91@fb-g_R-J@U_kuOb5W)`I{qfe3iHOAGDXWac_niQk#*pq;<05h2g8Ls^4<EImor%`=B{(0sgAt
sMi428L&9rEa`ap%~uaPR53~&L9JL#T6~+6Oe+9^2MJ_95~<KwR*hf9XNFEfkC|>y+jzIJ#0o5Ww03{07e4NsJm|rE<R%PbORQ1s
lYerW@Lwl*YIFmjds!LrdId%}6jd|_N%VDr&{BsWhPynVE-#n_fMx<}k`8uYi~j;~J!SXoW_@WvnVe_c`w|6E7#$jAXOHo){c>$l
PfEqPa@8bI*_>mS2SJt~Wxn_XDeYxwJ{svS{>8%$Q1?ry4x6ctkVRw%;Zkw7GEg|oEw(})K^?okRA&hny&f-+;F#P%|44JiQHn~J
?`UiO9Ig3(%x|)1f1+qVujM@#W#GrTF}B}0-g5tb_Q}be(!?w-w*lo(hS=#cgjD_yjea?1ot6y6SG`hC9Thv=IHSOi^AzslbPr1!
Ju_h@Y=!?V7~IlF`*ReMy3%Me$YkmKP<_N1RA);wWS@5^3Wob<Wa`^4Lxt+o&D!oNY}JjQjya~iuysW@BP^x%G~Zjtb`QJ|d%7g;
2s3$Komv(qC2<9(j>n7Bl5=&^e*buqH^Wz@+lZZ8aNBiPHYz*4FCuMH2|0Wk6c~oXGff>|FTQ%3w>C@@J)IUQjEL51L_AC4+_y)8
v<t2Z0Aq1^q)p=V2RDAh$#BAKKME?Vtj8x=9&->U5ruH?TOL`tstej1RO=vQucYry27UABf2I5*)L>b!C1Y(Iw|Ky+8CBm=gl>|%
kl(D(WCjcbFI45kz22rnd@XfZ{DdnP*Rb8)yqerAjBX9)u_y7dVofk53&;DSSY%Z8A1OSGNLQ0I5Bd{k{Up<#_0DaEOd-ykND_k6
tVS!z*j`-+BWJ>D1R>p41G!4H@T}RvWcBx?EHacAU@uXg0giNe3;`QUS}yD2p`&-L7dg}l9=KY&5h_3d4G^MSt_jWrq97p){~xLG
DN8&R6%qHUUW~L?>UKC>Aa>lFqB<wQ_))7S1_RDQmUnV~m_H)N9U2}o{x2f!dWiEU?Im0)+1O%dn_zDuYvJ&c?iR<}vC^BF??bt$
bl{?WmmHu#_)1y7lM_mmX?$+QX2umkLE-t)dJ=3VOMhbOtrh4S;qVTu7<hJ@B?`;aS%Uh(#Jk`EAP%_25w4$-Bkg{}>jC1yH6~DQ
=s+GT5hx(OWdF<X65mawr})jY#l3L^R$zgrRKKysnk!DC1>nPqKiYKzl<I~+cnQfpZ5(n$=R)0R-P-^@O_7GXBNP$7Whlxv6+Yfd
$l79^>+`;x_b`HY3m{ZwVQ>;g0>YTqeqVn<P`b42N)?WUVzG<AD|M}Iato700FdP4XMLiU)8g!mvxDP5w7od1u>Q}PC#{wCGWItx
yf!nrYp7Za?)ohS)av1?ENW=|+`1fR`V|xXYx4xi>_SQur_M-<|7ENh`OqWLOJKWC`8WJ?yM;OmVS3`W0*1~rZ~>$`96QSPKsp)B
|5ue|+-&GQqR8J*T_Tj&7`y_{9=oOZqM`b`R+9YUM(s1*4H;lxSSA9sb*Xvg?i0-kUlM!D_OgFoe_zv*L<~o<^0b$+m=>Yeb#F9K
<w0P)jJoNYX>yC%c=j8+0EHSQvA*K7D8|LBbDcMJJ>n-TG3OC5p3$sQtYUd={LBt3Ia@GgJhVpqSj_4OzXYoG5B1qT#+>^l>=RD&
&Q9|AeIUEp`lRu1lM#_>MT-fXZabn1chcA~MR1WTI>;Rf^N%)bH31E1?Fd=!VQsiae3qfADlKxPgOlsCxhW1?gtYlBg3a?YRsILq
xo5=<0*QU=_{?{qGH(w_yHV1E;B*-s2H#xTeBA*-8?R<TQAjzGG^u!DtYbVzRox#Eaud}gk^2ZEbEX+*;a#Xxjo4D*hhyg{MZG*B
ICVuAxbA#PR%<g{GzrR{i{5QWk8!8A%uE)#qZNqYRPYevnV=58928y;i+<F7O}P$ixs^J8j~dwp)Ap>k80_!=VWiNJh6Q{wO5j~0
D({#uwGtFD-TeVP{wBj_H+deh&X=6EabMJ{1X#EL=;BwhEaR}UjD(ClTs@aIF)O6wPST(E@-h~@`nGl&fCOBLalc^jSWcgFp)BO5
@_|pG6<LV!mo_gZB9r|LruC(*o!{PYR{1Kn&++0M?X~e><w=y3^BCJxYaVxVmbn8TBW{MG?wUWU_eYHW1<vu<c*h{v-9HTD1jaUj
3n*eNb(;ej6{l$VcW*D9OA9LdlP{kmh!g5*#RSDAG6fQyn9GRe+d-$dm@DZUv<5~VE_ib4D@r=tMF}dOgz#$^y9Y|Atx$f!P%iBv
ZPdR1i3D+KuUi)@0tzJFJC6cihJc#Cd<Qp(9KS@aJGQ8HX}><M$I5%TjGO!gP3VYcUYPeGUE2rT)t6Osd8jHCVyJV)E;*hJ(pScZ
vzgJHw{G*XeZfsk+kVY>z_Cn>vEPYC_}5>2@rx7OfC_#pH2wH&Edvq8KIz$Wjz;XlUd13dorqxo8xoa>CD*h~-l*A|M|UVp7TNT$
gn7Iid{1H2_`~KeauX(CvMxud=fh8S6OTc~s`uH>4hWw_Q<r52GY5~{M4UiJ;E=_oG!Ds3={q7E@t^G^{eU4HoRHDu)z`t2zJ@k*
nHS;*=G<ESHD^Upl%`MenF(|y@Fl%8*RiFqF#C($7@{LA;%o|atH{ZMa!!6rg~Lo(gLIh-*)<$1Oxs*pW$|5&6!4k0#0$^$XqGIE
G@U0BWI)1tda+rR+Wfcv7Xy#0Y6+QfVlvIe%w4wU3oIjPwR8H;x!YyeMhnOkHFpkEpDk_xxaIiYEcG_6r7RCS2=z)OPp~)4`sTZg
=sE96k2&Gft2ohXik$yn;`!HCN|tKb4)QS-E@n$pi16rOA8c^>559k19L|sIUavo@C22Iw=pmG^mD|`<J>WTUixO|k5Wr_(y<r%H
o3vo}3Y)eGQZS*Qpfb6QuYKz3iFAFEyQ=Je$NqPN4F82Id-2F5zR88RrFWHpKU6G*26#~kBex=5{f1#`G_h(up-~#3gtwf+9k66Y
wht&ybbHrnvXd$9JFLsi-ZtLQhw45m+(cY3S87rz(2_orOyO~(2NZ)Y-hOWzOeSSV5m{%XnW|gPzRsSY$i~P)cY4V0Tpd9F^a*-g
oUiIqm$u9Zto6ozY*0*I2cV6Vr42CwZL+Ig_kfT>J>El{&D(4nq{vw3K!EX%N!4?cr_`@{_D`Qro6|PSpO<;HX4D=%z0MAcW4DKE
KE(e8!ee?U)0e}C-`3R}Fo+0Lq^a`ig{Z#H7UaFvxE+ny<hj6=frUUzm-Z1fS+$R<44l*>vMF54dxhD<h6Oqr>TnQUK1-8EpEwXq
H<)mw<2G&O-B?A7`NtWuCBR41%o?Lr?uYxmn|5`D^W`QAXj9dbRt2^IqM(C@n5JszKP1={aM-tK2*!8zkTXW-yS^(8y;f7zwWUy-
+Xu^wSn%}Rdgxp1M<yA0T_Wg^i(wUtNmV2{bL^}rc6sD7XZENskX&EV>KS&8#^-1G?>+;Vqr)M6EBHE^MX!mmltgR`^GxvaLlhJd
g2@w1wT!{3;X^~oCf~|_uJ95pVLhloi*|j^d;d6Wr0O1^@K=Wv&e-fm#F8#WM@$zJbYy#_c-riG*-ko+`8qy=(vEA^ic>C+l7f6u
fJe6U@i)NRV`izQ%(?M^;`0PaP9+|r)&f+Pm4qp@<gP%oaQGrl1;<%eATVqJt&e}DiR4ck(Q(LBy|(-L+OuXpL4$812pq5m(}|pi
EQ7nz88~_0=I;H~w&nx^KWvs)lIe;=xmQ<fXx&YXTvjitfkar#_YRMA%quxU^tv<2qV%ggcp<ED*ZR#E9A!&J9j}Hk4l;-$u1mXf
_EqTJ9##HaDk6^tt1OVfA&l`(e){dn1s?#q32VNaV#Fme^m6GR07JWdqKC~VB8r%Zu_l9x{XeOVb_t{~*`KC^q4&-Qu2^V>=$PdD
(che?Q%e@b=4TblfY3&D?R1Cwn?P?G$L`cHc%s4nhfqu1;^-hqLhk}&+@x{Ir8BO(U(%VG)tP%6jtH-EHZCm8G%f5JC3OKYQXL0d
mkby-7`H)hKYR_to%RmGYMfDPJ8V(~P7AN1eV64b>!LX`y`?(56?BAW=M(5$CtG>f7bDA?Jr`iatWZJ;22jsD47mwlZ@!m8n0$$k
tdI4dr}-Y8D5(Uo0eE*kD><U&!Px=x;K^_sgSM-4KB43m`1RnOJV3M^o1ObUFW0$kh-_k82smuVTtI&{6@Vt{R4j)thwHiFw;s;`
>m8wFbW&8rz~=M}G-cm7!Z6zRg&~Lq?wRAB-LB>aQR2`@D{Xb@;G)QNQJ-E1qDrt&lBb;pYPMKg97pyj-YIgJrD2MXIdk{pvragY
JH}eWN-GMp9bcqZJB648kDIfdIE<fgRaJV9g$qC>=k|EV0yld|$RKzS<iEN=LO0;se1FxAz^OI7)!7q8b|j1h{&pfbYG-Ya(9)&_
WQa`B_dqNljwK#RmW#8Qv(i1!X@vNn>*q>%9K8_FJNM+Sp7z#Ptj1{Xo6r=_y5S>Yg9g)-+%}F9Hub<jA!%(F`-bfYP;S|S+}a@?
MLI$ebPoP?*8+P`;8g*BrSfAhfO2k<?o%K7j&8LC)`~WIp(x}WU%Vah-A&2+L-_G55VznlQ~=JN3heX-w@z3oB}rcYD>F7I-8YGZ
B6jzsp9B3)y2Q;!?7@6~RWcHJ8tg|y$r{-7r<+kryJwx0)vuxJVd%46v9oVmGLfv>F81ul2IBS8W2fmlYV?SCgAkbP&CrjjzSKz7
b93T_NlNfJl8KV6yVJ?mdVWZqZWL_j``X4G2~KiYEfWChQ82QVc6zFmEL&NCR1z$XeXzBm@Xi^4n`}=M+KRX{8ewfFVb}Dwgdqb8
^MM2pI9%5t10}4NL?=L4n9`Y}l4vhx9j3drcYJ^h>H$*9Gm5nYcsvx)v_*X5?9A8Fy1UQqyo__1Nd04~G$Z}wY3rSQ@x=xO@DQ|`
l3w^}@-lzcXcJf#E)$p|M=NA2=VfQK`%(qpRi$c9tx6?w*jPP&ebOk``g*JDg~Dl6=51AD)!JevU8%87BZ?%F{Q?ey>;na18gdvT
s)<x{O$el^Y%KQx0Ei_(j9R!C<|*NA6tAASCZ~{BpI-pjaOa*O*irP&MFTsleq8%08~qk?;J911e!mI!&VN1|HL^um9iE(4cZ;VZ
nw!F8q$jU@8z4vtqki=0g*V+FJv?cDDi5(Mqn^2)S|SB+Km&QCXvE&}M2*MOsjabpeP-@DT&x6R-hbgS64r^XBNmYuo{oUC5GTcy
IrzVKP>P}uINZR#X@{0FYVQZ;==hka%$D#e!7})D@jtI##?O+SEeVpS#aG7UCs-#~*gHIbT@&|e{%dzid=_~#cWumJ7rRxaO#puF
l$;&#q62l&jt!x_G)Oh;j1R`h|Kzo#rEtwTQ3U0G;F>s9!}&4YD0h=XqD|D?1n>p*emvX)YGE?US8FDz-klKyE4*^yWF3#(YXIXI
r_2v4flVZ5kaH~>I{^?FGS9h`xuv8QL~E&aS8Y}7XSUTl2`;q*!-qkDJi)<?77u%IQx7>1n+&ZyHE|F1C%VEXQnh;aG4SELaN!E9
9}*~uAHC#hr`xg$33+9%dZDO=OOUrlDA@yC5c5Bl5Xd<=AY#1qbVuGvgfs5A*H{xO63hXeV$47y+;{qK%<H?U*s4XasEN}(0CFIB
@VG;qQXx%d=D!p6l>w6KyNzC|%sx+@J`Fg~0fO;Kyr?;|Tt|V3kO8Sd<)I*Gt?50lhL~ZhT_GxvQmT+xv$9@64;|A6&i0pK6#uco
i-PE6h_lEH;mUFp`A@RL(h%0?HsN?t!u4eH;WBCPb7K~ylt+akbtq@IA#g5~MrVB6IIm|VDI1ymoVQLu@AOMR$>=e$7ehvaG}211
X~{9S5Z21)1>WwA;e^&k9cVy5A1gFfbwIwm<&c{22U}#KO_)~O>8wl~jXHx*yq6iZi%4&p16wS==j{_aHy*-UM?scWwU+`Uwj%~@
@=_Gbm{lGf{kk{#0@%ein0e!~FQ{i_k2t?Rju!<X6K}XysjI7;kf9jGX|7=M?l`A$2m2yhm+d@Ltxy|Zx7M}j{4ZaOI@`|ucc)2}
fx|z=jd7GGP+302t?YYjot<@N(P+DpC_!?}?|a9)kYD!cK)wd}SZ^)KL|m<1{c$-_t{URnq9S4q9nF$n3Z0+#V^FKH8?Gsu%8$CN
G&+aGb=3FQQKp8W>FQ+g`5{2k`Pg+#b?!Z`ep>`OMOBm{pRz#;d*{>JXm#<zESrc%U%5(Wj|(8YLb`i)x-RcCu>e<Xl$vOq?@iol
9`%JF^l?hU5LT{VN7M0jbDJX$IC|>Ni*kar2L$%M_+M1v_WDLI9^{al(MO`dL`bl|MGQz>RZrEI>J(k%xR1upp^gMe0?^dOOf1Z~
)%>Yb3pb<cC-2G^*2Y_dSWt`^mG)whN%hE?e3ja~?F|aAqXSHi(Sb>r7hRoDqlI!DkZX?}BH<8nt|<b`k&(gxLubOb1gar;E{^$P
XT!zsONT&MZ4Vn0*la5UXuQaPV@$g#WKw}$yPCZ$oIr6e&`cPSzN;Hl+3&|H)wJ#q_9f$UM0qpo%Wr}#9ya^k^SbBi(eHv$uD*8Q
95i<TmroU^GnxMxoTe2Vz(Ol_^AqA22eWB)$t7q*DcDqaUPbamq_1N)hfS0p4nk2&svXUW)m4Z5*(i0oMkgCwGXMggBQJ{&$SiJ0
cK=Vj71BSL<+Fl%|3A_9RQ?dR<;Yxs)jN6;#zDGrkmPr0hgjL+LnQ)W#FQM4MAlnp3O6>hLLdvK6PSMUJHK*|$Kr8UQm*-$dY8mt
t;G|n$0hslCOwa$b?Vhg4l-C?>P=lWmNk&cvzuSseJlfJ*qG75L?CkzQJ#X2^A7YU4~43IPIKg@K3`s@0|!h0U4GyxN<Y^e9({ED
rdZusg^?wGd*=qV2wWk{m|l9EmP^<8gkrdR5-p4DiKXjWsppo!#Kj*VP(_~L@x>yPfo2uw(xVlxE`#%w)@iXX$U=CwViC6IWtwS#
c2a!ssm-|x!+Q_&E#Y+GQ(0$^H7E4mDk8!+CCE)!I>t%^MivWNk2ZuzC5r`MAT??_cyzJFf%xN3H2ji^*v#XzluFHl-@2T`w6dSD
(IHx%TS;@!XDw<*LvCkZpn)&+DIRbPXC7u6gO?5|Qm1n|(_eVa?HlO+3o5iFdN_;9Gu-ytIr%&mkHZ{w+GV!}F4&q=_e(H1UHYJF
$f+%q&bGK7tNGDt8d(;;eF{UBbXcMHK3bmQp?f)~tB!zb4Shn@9}Eoyi?@5M>whje8AZ=s{PBv3)wKm!{;7~9jaDlsNFnT=P*t%l
7YtsL@yCD}yW1Kc(Zk+B`eTmK-7u*=b|+xEE)Vs`(;$02r60oxq=C&p0aCpTT>{DL4<=x3M)T2Dg?5j^q!{na%-Q*K1-;<K4;UXH
VS^ZN81Bd9whc|bKJhxw#HNWYV*gNRXN}uDb^vq!Cx%7Hm;Xp6!K?jVeFL-t$-E??aWZY*XkM;n8quy$cV+C_iPVzdXYFX=r`+IK
Am%*t?%XmWNE@E*!xSMrqsL}w!Cxi5^}`5T1K-Dr7wd%fAsXT~XKYZgC~n83C$b8U>*`&5sN@qXD&<vViCA%&GPm857y_k9#LkMK
?139E>v&|AQq)pQ+r4kOkHT*G$a1fjx&~f>b^~pk%rj$Im^=_RH>f1tacnu(w)y)EZZV-6H8%d3dP1>9tIB+d=gnork9q$Poup1f
0i^2jFfNI6*VLKQ?^tEy-9v1=?#;-K(Ez+qKbd6X9bjDzS?}d>xy--gG!CbJ**{b7>3p|HnLYd8@-K^1XKTC76f!<GX6JPy8B)Tb
p4-qCN-Q9I>$%rmsmq9Ax5tnFH1tBikw6z}difpH`IiSe_8|J2DL~FZM#V&3^)p!)e@%^Kiy>#|d^j#IOgKAFdv1EhvtoPeH7f^G
hFO&#>)kB!N}@PyP+;3X4<#myMs-7CO949PM~g(bHh<>NLE{fFb9suNmR?VC^X9{tc%*<mf5BR_K)A@ZvMR6M(`RxmLGXI`Pse|X
=ks}*>Ky9_&pPkuz2y}&ZH*QU*2l}Wk;`?zP!Xp_7$c!-HiI}d@@plAP73FL{GsM_sd;YYWKx)!UOaQ=p<{>x!%(lwj+bo{u4Jjq
pg<USL?s&4X!9+RfKDUzR~W%pU?)>mmd9J(%A_X(=>ww5AP{FYP=BG;ZD{Axb}C+lZ}*p;aVN-Pd@bmXz(?f#!U;MdB9wZmc63Mu
L?F5D*qT~p`EB<qPb-vt;_nB|j#cJb_^;GRj*phAH*|ychKX|FLKVUQBC3Q_-Sov)bqeu^OHAgZ*N6BHxzL(LY+29DY4)T`(6@%4
%~N!mBBmsFAO&PO{ds@RNk3Xw9a@?jz+D;)YniqwqQ=oHM4328ceES8S{n!Z_FE4iCViS!<tE&xxwuVesd0O=%QXc!64xb9ES~ci
_9(FAj8iNrb)J4@vI_i0<-Z1BFflM4*#`)Ugnm*M5jKg*2;yQKw{qz<fQdQ|8-{^`AL@YZh~5D&JySYdFHt}K7|MnU(G3tQ^{L~F
F2`Z-y=}^{f^D%-<eD+@#7ymkkCVzKev<4w-=nnAgivPHk--|0c&bRd(Uyl?<vdb@=B#OBEfok1rkMt19co1Q7|kX~$Op~=Z`#@b
R815|nEg1jO~!Qe+^zzZTTmra23A&xCF$RZCJ$6a&ZZV=@IEY$BtR6Hl<x?!&#*u3{8hdn8*0d|n0h=xq;7X5@td6u=SP2heBi0@
)rgQ5lUY4yoaPK|Kyjnsr?3`SJ-rD9kWK-83Rsnt|GMk$nxIVFE^am}wP4{0Kk<M2V{0Hj^s)3Zdv{sQ`M?PcTgvMs7oMbq*;~mL
P&)yPW?lEQ52hGRWSOh>p6gH3Lj)qTz$<2-Qsb=sSU$~X1UoQZp+xc?TX{mj(nbP1XyeGQL;a<faRzbW6*XH~9`Df{9_lem8oq#A
1zFb<Y$PdBs~|h4nYjNy>kn>Rb9a4lz8$l+)LZKku0xbe9KQdad)#?M{i{yE^Vp&H865+mNR@_^&_0su4^e~|O?mYSDyZ;>=fHX6
Xj+>f_v3h|yQEI%88DOY+-mT7^^!B5{Ip58-tXQhMd&P_y#Np5efIyt&J7iMWO%KdsvgIbEC2kMLdcM>u;c%T%ybLQuWju*M_Zk^
Ort;7^1^t#aykqQT)P1M&VqAQ#PO+XesQr+CE!*$4(=}lhoS~3qa|o{cmNxBt<?0ljBK&J@3>Wc_4a<Za61y{AXeuVQGuwzB;76!
@9@<#-=OF9ru0Ea*U+NBJ?<QQVp=0r1P5g94nT-%_cj;rSk+Fe>C`5;Aj+9g1BW#9mFj%WDs7+FSg~J1S-v74c%Mhr4J7a)nncp!
i;TtM>0fO(IyqW-HI~zp7=UC<>grR}r-6j^vc<B@Rqgx1NN3n)BkRrWs;6BKSM=W?UAIO+kIyb0|5HlUli-(7X(z1bXW~3i=d3M;
8_{fHy;#x=NeUE!kwW|!>x4mmris>%8uaBkG?_>^NZsr}MmfNE1`N_Ik1UGFgD?={IB)=a?>!6F!HIZuC~6P`eszt>-zvyE5vax3
Azc_H{s><k(2nK&?svVjaqg-@eb@P^?4%$QJEHxu5JcfJY9;J0a-?9<k8gD1W~^1skJ~aP%O)PJ@jBBgl4neR_1<dQO#)`wA!~IQ
L#kev3_);H(m@kCQt4N7YI+)h&L4|GeVT>`+9@DV4G#5A$6|c=vBnt5yF+VD*nErS(#PNUSpDCQZ}|&&Occw7<(-j~#?hhSrDqYt
a?xXLT-{-&&fTwt`=s9qcN>O0Yz5~qkg3+C#}lZ7+j_%!uljYuZCK!~VW-{t186EFcVS-9Td&CVy|&(9p5Od*u4T|F<rV-05p)gs
CO{^!LjG+WMWs8ljKOm%NHA*ozCP)snX3!$^lRp0gqx|tB3F~=I!h6WT1b&)1xX|IF>;~A1n<eR$GuUj;N|ovAHY3{20MtkcDwfa
btO;5K<}Ez-va{IZkJ=0zy_cV4zAtS3s6l#W7{5zT_lUvz~Z6@bEr{sa1@4Jtp%g!7%c87L^ta(+2Z11itsvfO}@Mhqmm2>MwiA|
)exj|X{D^;_Ab_Ylg|N;w;q``fj#bMio_D>05kb%H^1&YnjIPzXSc)Jpe?0w7fvX32P*o0p0t`}xZjt8GXVa@CQnFPxnn39Kxc_Z
emz5_Om4{$#d%s>h0HqpZg3>m+;S?T3Y`nPl7Z^Azns>M^Bca#`65)BH;#j-6*d3HDzzrJ7?_k9D$xME#iL-ysg_ViD%$Ea7B8kW
ARLTD{$;`b;-KANn@$C4o#zmQoXLYT{>L!B71_lowZ)2YwPWL*;X7i-ho*0ol!ET0AiO&s1^(Hs1X$PV0S!nx>0VfpUu`*lL!9qr
3ioq5xrrk=GyZn~Khz=bjs*rJty8VO9T66vIU?xWsqYmSY7d~MIa)BhkBXz#%i*e9=9+0wUsL7}N8-<oCNmFF$|X7CP|K_8Vyd+b
lJu@~Njn=#R2eS|(+G0L>_T}N-s9djVa*R8s33jREVj>MNSFjds|D&cwWNRP`)X$*`7=?I&jgHcm>VWsFP7pmTYrDZL{K8UtrLEV
;F>}uPHqSb`16{|aYl*23>or}p1QIpsSHnnJ?9OrTte{sMN!UN$rxqSu<pvvJLou;y_>c8v%qJ^vs1x}u$`OwdqlrZ(cZewEHX7_
g@0g1oOazb#gJ3J)r;}G$bJ~x6Bf>fO@11NE|4<4e+NxCh%r>#EVIh;{v^dM7=&am+&;>IM!xEuMq2gan4RvRmnnfmOP%F&jNZi@
`MQB@sYzgs-@b)9`A;V_kMj0A_QV2IbWBd$w)b2>as8uqUP2u|ay9dYfa7kvgA<eTM*S)*%QkOYy$46#<erW7k8}1k_}2Ylgmi(|
fKX{xpN?tR9P69)l<c1s`xzW6uX90SEH|Ew0+LK;K~7%8(y16iN)VV`AFo?#0wa@%!_qptVOY>$tM}Rtk7|STDGPs(VEZ-C61{gn
TIRCq@3Vu#Oc1K7IKS;dWE0YkM=Xt;MMc7Vtl&7=yRe>I=_&sSTQxgHq*Hq6xzJ`rUC~Nr`$Ji1Iqf3hCzwP~mXG|k&h$ES2vpF*
57d|SNz2~|MwrJG61t6pxUSA<nnHV&T9-caEb!PzFS0_=E~evW9?s@?PO|fk-=%*s$il025rDen+R<N6#5zmiquZ626X6ODhB)bB
jCj~+gV?B8z-M&G?slXYS9@|fY0-5}JQU3=GUa-<XDuL{-fJWBzb;4PoNKQ;hPLVZ2eWf#MIY<HrK^2iiC08sl6jiRhUVwB7NI27
EN-`DIT0Q-#W1Mt2~xm7$;HW-)<PGlu!}!anGQ;eP2Ir0ha`q!LUJvjv#$`fSq&q*xu@{+YZwj^7=eAX3}j|XSUqXTrYeOwwr5+<
1*C2W$Nup1IHEpo0-EKSoW*8oqTty=)uNg4sNQ<3E<e^8pX2DRo_qE4&=iKLhRGi5=@V6B?LPxMCg=#y_BmUc1ipLte2?-lZ%Wr`
h{B~ig&;XMq?&lK0*Qv-+_!-lsA2p=`qSiJ@D&R13uhP`=kFbut&#<Yl^E}@;nDVde;_G_zV}G2a%`dNfyv#zcRZQ_WcIhgtmzk+
Otlr~4GLPe4=~;hWQs@)<wc_Sfm*83OH;qZQXOSzx6`YB=_6W;0lqRVS=5fj06ChUD>rt8dDfyjZEkw;j*p#pEHJU#pdgTzw#{A$
x4_*|Go*>Sg|o<g<9a!2cKGW=6q<ob7Cn1~;4JR*{1HZ`%=yvph$6E8Ply&^flLRj^HN#PQwjGOpMjoeda-GQ@^Fi6t1HGgCDa>o
0g=u{?B%O}Ku@-ca&>w7@HCWBf<lorzZSIx@7XgM!1u)7nRVHO>WAhMEQ`U_JZKT9!30{AMdr%|=~`p?e<e9HaK&o_n0bEywl;pv
RD{_k{|oQ~$^zUvrwH(=APl2j{q0@oOypv=gCRR4xhvtjI!r@(eS0HOZ6JwyK73Qgi^==?{4;+e|1(IS<BB$9r^_B16v_dT3|Zmw
g|>*}{~j5_qs2)<{#q?@KN3Oi;LWe(8v~YQ2-EP8&e&r1>_z&4azsUOD<JNI6N-uxqDne!lw#!q-0#H$6caU6r+}Tvz0NANEzf2B
h1cl#je!UP;KNfkw-?d%y}E9K;<^7i!MPFb@K;Cu6fYW|5i8?KI_4g~b=fB?`5Zfv;(|i(A9MSKlGUA|ZI>y%H&?a4?u}ymCPre2
uf0?caK#WEmB2peYk5#L?92=scY$!E<*;+`@Na)D8em8aXhRA=VcXx-FL^hl<{0=8H*j*;rVi?|XoYALx#ro70;nuaW8Xp7<UPMs
5|7NdAGY}@e~^4caTob5OqCMOERKZ8U_hf3$4K-%flcp2ErwZ!>c6v!oWcBuQ!wf0n`a{<18QxGZWWkTCd~tI-yyJuJ<${xk;rn<
Vp&9kw=!G)10{7qy7V?P$t%L2?J@QyyGRBsn~C@RP5J&Hu8F7N_oe4ipr}v~j0?8&#?9uwT{q(N9cf)VvP-bi%i<k&hAVKvuBq!@
A+C|gHse>wsB7O9l!E7z9WisoFI&`J@Nvz8n#+@^R({MN2)YzGUlUKGB9P2q@OEGdxK7U0P=3?Eib>)VI%6m(F!eSKKC+l89`}MW
*j~xmnQ^t`3r(1%HQHzQrtRMsOIgOFISge&r#VOn(w>SYV9VRNtG-akj3yXjfaY%n%2(j0TMh)0f7xOm&5!D^|GOz)*O?tA{&ab0
e6p3?^dDaY+~?rF{cP+8t)vlHoVUsIkp`?V*9VUqG~Bv=j)&HiW>0#lr#uzURMw|Fo(QP|hpp|xz2CB!=n+B+c9VyrOvLDFLd0P1
K^(4eGWp>(mK=qWPlYSl+fX;J0I%3d{#|k$IoJ-f1DK39$d$sAGUrd3jr>l4^a_}gVY(j8U6PW3BNn){-;Kt&^PU&q!g7AzPwtNo
xSc%Fu&A7Rnz_s~wr%bUG!B)X!*M#UC*q;Gjj|xj2EaKNg>;>$e6^rLS}{Ro4h-Ab5$N}!g^s?b0%ZcYX1vW-NdHu`ABi&Kp}9(C
N2X|Xmo2)!9r3kUH(+%lqs32a%8YkiaFG3fQ%4VP9kfUR`*{V1N*HqXo;n{vUG54dff%1eF2DpmTh`<Lda!7wR?LtQbdh6g%rKnc
GIF4aSntMV8o;gHH*gY#R~E1=**qvE;SoHq8u$7Zk{y@KoWnx_)YiS+T;AV$i>5pMJ`T_dnH)BI?zO4ofdP@eZ%1mRkhRAx_!D33
%spIn?_-asFWG4?4a(_AUh^24aev*cLv}62&wrV)&(Dsk@jl5Ap%d(>ySC(Yo5!!j5`dM_4b0OfY3iZ;<>T8!-5|}Wjn9|3b(aid
5q+f`MQu`xOE79Bh-4GySlyoiSU;PRAt?=aJElNqQtEIJM*(!~a!{g~QQEi+D{4`tdHcB{`~~Td&28-ggBRcxRc6e-VJnkWBsJ{N
CJ^M$DRds}PU$4ep&is!A4@=Ya7LH27M9>Mw=yWbe@$d!HEMf9CiUEKW=9~MTjDl_qp7F&2DwrVADI^SY|4+DDZ@A>me;myD~gHe
(;O(qBqMy`p6`%UgSGO5P+S{hN^>JyeGxb$82kv-S)2m3TokBUxt}cVI+#u-vClYWXhS^O55`;nX(OC*sk*5-=|SIvI~H4s$MKkN
{i}@V(<k|w$ho7d_u$skRlt`SU9J6+n6ywcQfn_RP(ckmEsfAx>K;&(PRNZ%VP{!v?vN)=ZN}3MLay89xrIE-9wND}-{Vl-?PO9W
70Rjn%V5d?OaK4?1|PZcgPnN$00D-+0rmF-^JNTevBYQl0ssI200dcD
"""
def main():
 raw=lzma.decompress(base64.b85decode(''.join(DATA.split()).encode()))
 assert len(raw)==64501 and hashlib.sha256(raw).hexdigest()=="fc59f76b81062e0b1a3d619bdd159228a18a4f09e79ebfb2bd2a641a22df33ca"
 files=json.loads(raw);assert len(files)==17
 root=Path(sys.argv[1] if len(sys.argv)>1 else 'KL13D_RECOVERY');root.mkdir(parents=True,exist_ok=True)
 manifest={}
 for name,text in files.items():
  assert Path(name).name==name
  p=root/name;b=text.encode()
  if p.exists():assert p.read_bytes()==b,name
  p.write_bytes(b);manifest[name]=[len(b),hashlib.sha256(b).hexdigest()]
 (root/'SOURCE_MANIFEST13D.json').write_text(json.dumps(manifest,sort_keys=True,indent=2)+'\n')
 print('KL13D_SELECTED_SOURCE_RECOVERY_PASS 17; run REPLAY13D.py for exact checks')
if __name__=='__main__':main()
```

Supplementary exact copy: KL13D capsule (`KL13D_CAPSULE.py`). Full working archive, including numerical checkpoints and exact reports: KL13D handoff (`KL13D_HANDOFF.zip`).
