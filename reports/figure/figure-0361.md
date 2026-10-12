# figure-0361

AI research report · 2026-09-13 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Calm Finch 31 — exact one-pair cancellation at C618, not a strict110 endpoint

## 1. Outcome

**No uniformly filled, own-volume-centred strict(1,1,0) body with C<630 was obtained.** The strongest completed result is two different exact rational C618 bodies with strict counts (1,2,1) and weak counts (0,0,0). Each has V=176, E=309, F=135. One of the original double deletion’s two extra unstable–saddle pairs has genuinely disappeared, but one remains. Neither body is a positive answer to the assignment.

Both new bodies passed two independent exhaustive exact audits, a separate exact centred integer-tetrahedron mass check, and source-only cold replay. In addition, the SEQUENTIAL generator was reproduced byte-for-byte by cold-running the numerical construction from the original GRID7 generator and rationally freezing it. This is an obtained coupled geometry/mass mechanism, not merely an optimizer proposal.

The preferred continuation object is FINCH_SEQUENTIAL. FINCH_C618_121, called JOINT below, is the alternative joint-then-single-basin construction. JOINT is useful for diagnosing witness migration, but its remaining saddle has moved away from its unstable vertex.

The actual GRID7 generator, not D9 or CAP, was recovered and its stated hashes checked. The original double deletion was independently reconstructed and re-audited here as own132/weak000. All137 physical inequalities were reconstructed before removing the indicated physical rows. GRID7 has no immutable worker assignment ID; no conflicting parent payload was substituted.

## 2. Exact objects, maximal complex and actual mass

For either main object, reconstruct all137 H rows from its literal generator in the capsule, remove original physical rows99 and117, integrate the resulting uniformly filled body, and translate by that body’s own exact volume centroid. All135 retained inequalities are maximal facets. The edge census counts true maximal edges, not triangulation diagonals.

| Object | V/E/F; C | Strict S/U/H; weak | Equilibrium carriers in its own exact lexicographic numbering |
|---|---|---|---|
|FINCH_SEQUENTIAL|176/309/135;618|1/2/1;0/0/0|Stable face3; unstable vertices82,96; saddle edge82–85.|
|FINCH_C618_121, JOINT|176/309/135;618|1/2/1;0/0/0|Stable face3; unstable vertices83,96; saddle edge84–89.|

Both have facet-size histogram {3:49,4:31,5:28,6:11,7:8,8:3,9:2,10:1,13:1,20:1} and vertex-degree histogram {3:134,4:35,5:4,6:2,44:1}. Each incidence sum is618. There are348 oriented integration triangles,618 facet-side primitives,176 vertex maximum-escape classifications, and1236 edge primitives. Every facet primitive, vertex maximum, and edge primitive is nonzero. Complete facet cycles, true edges, rational vertices and all sign arrays are deterministically emitted by the supplied auditors and checked against full-report hashes.

Vertex96 is (0,0,1) in both raw bodies. The remaining non-apical unstable vertex is incident to original physical supports55,94,118. JOINT’s canonical vertex83 is not the parent’s vertex83: the lexicographic indexing changed under deformation. Reconstruct the exact complex before transferring vertex identities.

### Own-volume centroid

The following decimals are orientation aids, not defining coordinates or coplanarity tests.

| Quantity | SEQUENTIAL | JOINT |
|---|---:|---:|
|Filled volume|0.4888107746644826|0.4880008236835783|
|Raw own centroid x|−0.012816641720460105|−0.012969735312600657|
|Raw own centroid y|0.005852911671696761|0.005913152343771209|
|Raw own centroid z|−0.009076415755956373|−0.008608743598973956|

The re-integrated original C618/132 body has volume approximately0.48862746700999565 and centroid approximately(−0.01282694458722602,0.005958831446863503,−0.009199452334373567). Its centroid was not reused.

Here is a complete deterministic exact definition of the large centroid rationals. Let X be the exact lexicographically sorted vertices recovered by either supplied exhaustive auditor. Triangulate each outward maximal facet cycle from its first vertex. For triangle t=(a,b,c), put d_t=det(X_a,X_b,X_c). Then

    D = sum_t d_t
    volume = D/6
    first_moment = sum_t d_t*(X_a+X_b+X_c)/24
    g = sum_t d_t*(X_a+X_b+X_c)/(4*D).

Every operation is rational and every input is supplied literally by the generators and reconstruction/audit source. The centred physical inequalities are N_i·y <= h_i−N_i·g for retained integer H rows (N_i,h_i). Thus the centre is completely specified by finite exact computation, not left as an adjustable parameter. Replay writes its full numerator/denominator strings. Both independent integrations agree exactly; the translated filled first moments and centroid are exactly(0,0,0). The third integer-tetrahedron integration separately verifies zero first moments and the same volume.

Maximum bit length below means max(bit_length(abs(numerator)),bit_length(denominator)), maximized over the indicated data.

| Exact data | SEQUENTIAL | JOINT |
|---|---:|---:|
|Primitive raw H integers|331|332|
|Raw vertex coordinates|693|704|
|Ordinary volume|33414|33577|
|Raw first moments|66661|67002|
|Raw own centroid|66660|67001|
|Centred vertex coordinates|66663|67004|
|Third integration’s common centred denominator|66736|67070|

Both generators freeze their free controls on grid10^12. Contact reconstruction produces larger exact rationals. These are not small-centroid-denominator constructions.

## 3. Obtained high-dimensional geometry/mass mechanism

### Contact chart and differentiated mass

The GRID7 plan has318 free scalar coordinates. Exactly six—the coordinates of dependency-free deleted supports99 and117—are structurally inactive on the double-deletion body. The retained-support Jacobian had numerical rank312. All312 active free controls differ from the original generator in each new rational endpoint. This is the full contact chart, not an eight-parameter projective-affine family.

At each plan node, prescribed coordinates are solved from its contact dependencies; unprescribed coordinates are optimization variables. Analytic forward differentiation passes through these small linear systems. Physical vertices are recovered from independent triples of retained incident supports. Multiple contacts remain identities of the chart rather than decimal coplanarity substitutions.

Actual filled volume and centroid are recomputed at every trial. With B=sum_t d_t*(X_a+X_b+X_c), the differentiated mass equation is

    dg = dB/(4*D) − g*dD/D.

Vertex-escape derivatives include both vertex motion and −dg. The centre is never an independent optimization variable. Central-difference diagnostics at the exact endpoints, with a fixed random direction and step10^−8, gave centroid derivative errors approximately1.1×10^−8 for SEQUENTIAL and8.4×10^−9 for JOINT, and relative vertex-escape derivative errors approximately5.9×10^−9 and8.7×10^−9. These numerical diagnostics do not replace the exact endpoint checks.

### Fixed identity reserves and physical-motion metric

For a directed edge v→w, the vertex witness is dot(X_v−g,X_w−X_v), divided by its fixed entry edge length. For a facet side v→w, the exterior-foot witness is −dot(q,cross(X_v−g,X_w−X_v)), divided by fixed entry normal and edge lengths. A positive witness excludes the corresponding unwanted unstable vertex or stable facet.

Protected identity floors were initialized once as max(10^−8,0.2*entry_witness) and kept fixed throughout the declared phase. Nonincidence floors were max(10^−12,0.05*entry_slack). The retained stable facet and apical unstable vertex had separate strict guards. A 2×10^−8 feasibility buffer was used by the corrector. Witness switching never multiplied an existing floor by another fraction. Changes to the protected set explicitly moved affected vertices into the cancellation basin.

With J_X and J_q the full physical-vertex and retained-support Jacobians, the step metric was

    W = J_X^T J_X + 0.04*J_q^T J_q + 10^−5 I,
    T = inverse(transpose(cholesky(W))).

The correction minimizes ||u||²/2 subject to linearized fixed-reserve and target constraints, with parameter displacement T*u. This avoids poorly scaled coordinate-box steps that spend motion on sharp chart directions. The supplied implementation uses SciPy SLSQP for numerical proposals; solver success is not treated as a mathematical certificate.

After a proposed displacement, actual mass and all nonlinear guards are recomputed. Further minimum-motion corrections repair curvature error. Unaccepted trials are discarded. Trial points can leave the protected region; **no certified continuous no-birth path is claimed**. Exact endpoint audits establish the final equilibrium classes.

### Witness-cycle failure, distinct from diminishing floors

The joint search exposed another failure mode. Near apparent cancellation, protected vertex85 switched its witness to85→82 while the requested cancellation still sought82→85. Fixed positive floors alone do not prevent this contradictory selection.

For every centre g and distinct v,w,

    dot(v−g,w−v) + dot(w−g,v−w) = −||w−v||² < 0.

Both directed escapes therefore cannot be positive. More generally, no directed cycle of strictly positive escape witnesses is possible: sum

    2*escape(v→w) = ||w−g||² − ||v−g||² − ||w−v||²

around the cycle. A greedy selector can consequently approach a zero-length edge instead of cancelling its intended basin.

The usable repair is to maintain a root-reaching escape forest after including target arrows. A witness switch must preserve that property, or the affected whole basin must be explicitly reclassified. The successful SEQUENTIAL phase fixed the other witnesses and cancelled146→147 while allowing the already-existing extra sink82 to remain. Five accepted outer updates, starting with target increment0.003, produced the exact SEQUENTIAL freeze. The apical sink and all other protected identities remained guarded at accepted iterates.

Physical correspondence matters: in the double-deletion indexing, deletion99 supplies the basin at146, whereas deletion117 supplies the basin at82. SEQUENTIAL cancels the former, not the latter.

## 4. Precise nonwinners and execution limits

The alternative JOINT construction used12 accepted preconditioned SQP steps, then18 completed outer projection attempts, of which12 were accepted. The next attempted iteration did not complete. From the retained checkpoint, three accepted single-basin updates cancelled the146 basin. Its rational freeze is FINCH_C618_121, independently verified as121, not110. The preceding near-zero joint target was not itself a cancellation certificate.

Further scoped repairs of JOINT’s remaining two-edge basin, full-forest repairs, and original single-deletion99 and84 searches did not yield a positive endpoint. Some exploratory commands reached execution limits; only completed iterations and saved checkpoints are retained. No outcome is inferred from unfinished iterations. For example, the original single-deletion99 search completed7 attempts, accepting4, with target escape approximately−0.0148901; the single-deletion84 search completed6 attempts, accepting4, with target escape approximately−0.0251649. Those deformed checkpoints remain numerical nonwinners, not additional exact constructions.

Four targeted reinsertions were also reconstructed and checked by both exhaustive exact auditors. No additional defining data are needed: use the same two literal generators, deleting only the indicated original support.

| Generator; deleted physical rows | V/E/F; C | Exact strict S/U/H | Weak |
|---|---|---|---|
|JOINT;{117}, restoring99|176/309/135;618|1/2/1|0/0/0|
|SEQUENTIAL;{117}, restoring99|178/312/136;624|1/2/1|0/0/0|
|JOINT;{99}, restoring117|178/312/136;624|35/42/75|0/0/0|
|SEQUENTIAL;{99}, restoring117|178/312/136;624|1/4/3|0/0/0|

JOINT’s restored support99 is redundant: its exact vertex set, maximal facet cycles and own centroid remain unchanged. Restoring117 without retuning its free plane is not a shortcut to110. In SEQUENTIAL that reinstatement produces extra unstable vertices81,83,84 and saddles81–83,83–84,84–87, in the reinserted body’s own numbering. These are finite computed nonwinners, not global exclusions on reinsertion or contact redesign.

For the nontrivial reinstatements, raw-centroid maximum bit lengths are67249 for JOINT/{99},67134 for SEQUENTIAL/{117}, and67181 for SEQUENTIAL/{99}; corresponding volume bit lengths are33704,33651,33674. All reported reinstatements also have zero facet-, vertex-maximum-, and edge-primitive zero counts.

C620/222 from deleting28,127 was not advanced. No new exclusion of that stratum is claimed. Neither blind pair deletion nor the two-to-one screen was repeated.

## 5. Exact verification, hashes and actual cold executions

Auditor A enumerates support triples using integer Cramer’s rule, tests every inequality, constructs maximal facet polygons, and certifies boundedness through nonnegative normal-cone decompositions of the six coordinate directions. Auditor B independently clips every support-pair line against all inequalities, constructs its own endpoints, true edges and facet cycles, and checks bounded intervals. Their integrations use different facet fans and different interior tetrahedron origins. Their stable-face, vertex and edge-cone tests are independently expressed. Neither reads the other’s geometry or moments.

For both main bodies, complete A/B reports matched byte-for-byte. Edge normal-cone checks were performed on all309 true edges; saddle counts were not inferred from the index relation. All six exact cases in CASES.json completed A/B and full-report comparison. The two main cases additionally completed third mass integration and cold source-only replay. The four reinstatement cases were not separately cold-replayed.

| Main object | Generator bytes; SHA-256 | Complete A/B report bytes; SHA-256 |
|---|---|---|
|SEQUENTIAL|11719;6c54387c241db636661bf12181fc3dfe7bb773a7b730d49ef1f8bb9d7ea826b4|361370;913c9fb4f7cb59adda09c6c7eacb80f004798c2e130e61e9ebc317d531f5ce0f|
|JOINT|11722;677a39a02bd67a514cf1f7366e06301c77d3da3498c5cdd6984fecd53dc61801|362908;e9b59e62768d07bf11e70b58375d34b1dac7edf949840f2f52185318a7c8e9ab|

The cold directory was populated solely by decoding the literal source capsule. No precomputed H system, coordinate cloud or report was used to construct either replayed body. Actual cold A/B execution times were approximately10.997/5.902 seconds for SEQUENTIAL and10.122/5.663 seconds for JOINT. Both executions ended with COLD_SOURCE_REPLAY_COMPLETE and strict110=False. The third integer-tetrahedron checks returned exact centred first moments(0,0,0).

Environment: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, Linux; OPENBLAS_NUM_THREADS=1 for numerical work. Exact reconstruction and verification need only the Python standard library. Assertions must remain enabled. The capsule contains21 complete text files: defining generators, reconstruction, both auditors, mass integration, case definitions, numerical construction controllers and continuation code. No helper module is omitted.

After extracting the capsule below, run:

```sh
cd finch-source
python -B -S replay_nonwinners.py --case FINCH_SEQUENTIAL --out verify-sequential --mass
python -B -S replay_nonwinners.py --case FINCH_C618_121 --out verify-joint --mass
```

Both output directories must initially be absent. The other four exact cases can be replayed by their complete names in CASES.json. Their expected full-report hashes and deletion lists are literal case data.

The SEQUENTIAL numerical construction was also cold-repeated from original GRID7, rather than a floating checkpoint:

```sh
python -B -S - <<'PY'
import json, RECONSTRUCT, check_A
G = json.load(open('GENERATOR.json'))
H = RECONSTRUCT.recover(G)['H']
R = check_A.run({'H': [h for i,h in enumerate(H) if i not in (99,117)]})
open('A_99_117.json','w').write(json.dumps(R,sort_keys=True,separators=(',',':')))
PY
OPENBLAS_NUM_THREADS=1 python -u single_alt.py - NUMERICAL_REPLAY .003 10
OPENBLAS_NUM_THREADS=1 python freeze.py NUMERICAL_REPLAY.npy REBUILT_SEQ
```

The actual resulting REBUILT_SEQ_GENERATOR.json was byte-identical to the11719-byte supplied SEQUENTIAL generator, SHA6c54387c241db636661bf12181fc3dfe7bb773a7b730d49ef1f8bb9d7ea826b4. Numerical reproducibility was observed in the recorded environment. The frozen rational definition and standard-library exact replay do not depend on reproducing floating optimization elsewhere.

## 6. Continuation without losing the obtained cancellation

Start from FINCH_SEQUENTIAL and its freshly reconstructed exact complex. Its remaining forced route begins82→85→89. The repaired146 basin must now be protected, not left exempt. The root-reaching path selected at this endpoint is

    82,85,89,92,94,98,101,105,108,112,115,118,121,126,130,
    146,147,149,150,151,152,153,155,157,158,160,161,163,165,
    166,168,170,173,175,174,172,171,169,167,164,162,159,156,
    154,102,96.

The approximate sum of squared edge lengths is0.5908275862, compared with squared-radius gain0.6478438961. The telescoping identity therefore does not give a total path-energy exclusion. Redistributing local radial gains while accounting for shared actual mass remains the constructive task. These decimals are diagnostics, not a feasibility proof.

The supplied continuation.py starts a new explicitly scoped phase from the exact endpoint, fixes identity reserves, verifies a root-reaching forest, differentiates actual mass, and emits complete rational defining data even when its numerical target is not reached. For JOINT it explicitly includes vertex84 in the cancellation basin83→84→89 instead of falsely protecting84 while requiring the opposite arrow. A zero-step SEQUENTIAL recovery was actually run and reproduced raw-H SHA725d810f74100f0f37a7c8392e986e50ec27abacc57cc0891a53e80f32e93da0.

```sh
OPENBLAS_NUM_THREADS=1 python continuation.py --case FINCH_SEQUENTIAL --steps 6 --step .0002 --out next-phase
```

This last command is a continuation recipe, not an executed positive result. Any successor needs exhaustive exact A/B, true maximal-edge counting, its own filled moments and a new cold replay. The remaining failure is one explicit U–H basin, not a demonstrated obstruction to C<630, the full contact stratum or intermediate combinatorial changes.

## 7. Complete literal source capsule

Save the following complete Python unit as recover_finch.py and execute it where finch-source does not exist. It requires no journal, attachment, network resource or downloaded helper. It verifies the25545-character capsule and80723-byte decoded source map before writing all21 complete source files. This capsule contains the exact parent, both complete new generators, exact verifiers, construction code and continuation helpers; it is not a hash-only reference.

```python
import base64, hashlib, json, lzma
from pathlib import Path
CAPSULE = (
    '{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;X6`KlU)Ekh=gPkz)OB1JNP^0()NMShR4OByKZ*+d~I$Hz1PP}h~|;OqUSHAPJQiHuX##^6lPF9jF1YwEe?D8@1INzPAnXy*`;xw|LDoPHA`5ONlI>Sp;e)K=iF8YP4MTwmRU8Z$7r(i-g}r)4Ra<@?#JN^7GgD<iEKT4kil!23o#Zn-L3;uN3K?YfmhkHb=yYwgcj>xZV#FLHQzZ2fmlP@t>(Mt$~p?i=~xfq^t#4ZgP;ez6N9Jwy0uX=z7;n$fM+c!U=XjPP6|&O_{wqVFh6==f&0wqZsouRL^yjE5U#`Pz)7?ut<ErXNo{KMk2&PG75WkNlog>&Q+o{f+a9N?2r-NY+xp4_j}35l6=4$7SdT=DEXgknwL;0?P{4ET+2tvI@^#WVpFO6*kx~vs|C4DM$5jIX|0ureoXYrjhDC@bRGW0s``8LpB)fbDKl3;)RxLC6msi;xv!iUmE~Y*;s2OPi=eqYgItzDyMQU@ijMQ$>GF;o_&HwqkZv?IhMaCUex`U*_E6ZwK5|odXa2+O)l858@$vq{z+YdPbOcH!t08Zu=4tA;0!Y*>2#t-j5DZ^{V{zGzJ1wN77SifRroVhZcKND@0F~L-lx-YATQ^f4{cMF<r&p!+I5&j*}(DUB3jqXoS-I1q|jl(3A*!0>>oQh_4G3yDk4`Kn?W^A_;l6gKh{=bRN2i$dY3_siFAd=l_$rMN60$L^CC6^une<eq?6Qv8_sb7a68E<^x<c0ObRL)Rdd>Nif82UxL7?(m>8w$E8?+nlim`#k;mebEWtk!$i&8h=>fVi_STM6^BL2Q5{Ga>6o;zRa73TT34W#B!kOf>ax^%FPNOntM%+GL^b5%-D%HhiZk1Tky>h{uTwPblT*H`ORZ#RfM03w}CQI8vhB@465|Mti$-#onP(=7IuE(gKFNBgTL~r~&VPfB56qx7Z9&aQF*{Oa`|z$=0Cv<yNsv(w8Kqv6x{RruC9e(Ay*=TY_ZE=0GKPh_c~3nSB@&A!m<g=yF{}<T)r<F&GhQY8bw<TDXMX>Jdx3$>{m!qG10l8j&?DKnm?dAmCs-Z_^d<Vl9*Bdp@*3Mg*?;@Y2_Kc?EtYRT?hBf^G>VWYN&sx~(jCDUSy`)}F5{vnj8XTS`bO=@04OdpID`ijJh8a(259qC4k1eHqp^q_<bc@0hhoL2wkelt;eJ<O(H4zCW0679{YM?Qq+p&-E`$DV6sqy2QI3b*Dae)I814*g!C9A=4HLPC2R&$T|DiK?q}mG2f}X)0P!bieLWwU)=7v!afY%_zFdq!Gv@3izw{LY@b@qFS{ILs&>|-%{0%*qW8yUMBYCtry!$BT-k=@L5;-*Phb1_Wt-b9uJ=eFnP@9!`F^Y2lM+O_<7yg2N-`U)a#)&)U6QBt(G=!v_FudC^XC(}pPI!47>p+;M;TaJc-+|eb!q1YFdl_l@xL6r$g~=%!N%2#uR<nhm3jTKaHiG38qnlfpCzu3Fy!dp4Sl4ekPAz%A@3<H*||^hg^ao)1kL0t2)tk-LbzHdxl>=7@jn9V_?29gbQP95JlzUAY4}d(rB@7DI_swoqK`O7yB$PejT&}^@fgG9ZC}{C5HDG!Pro&HNgz4WF0g*CBk;y<7K0mjp@#?bNf(3Yo`$<59T>+^338-2<fOGm5t$@{%i0p9_sC>#KEtjzg00Pn{Wg`P;{c16s;iv{9KUfS<!aY@lwm>;1N9v_$r>ovurl>26qtpw{4MStY?)C&KUCxq<rE(F4)-<?$s6u8Jb8C|8tiBwI>&P9b(mecQTcIuB3rpPkg|JaXZ#xEaxh?8`Qx>@xps4?*A?{y*yS=Q_8aVuK-1dsET>R;lb<>Io^AY4wIkHzo7;kYq<YP_aXYC^rd>k&UY+E!-%6^IDPjR17U!qXUQBJB{c*TJHS^trCmwQ`6~Vu|m^p%=eOP8>QtB<g0C8d?WIZaUmeiP@`V;{q<fN;@59Qy7Zb%w|fYL}4@Xm}+r;FB92VkD+o9O{5tuuHank82FNQEFI@RM55{4)>-+C||bB9foxQq~8IGh5T0`(u|}HEo!*T{p`>n`2k6F#GW44~8Aar=XzlU+<HhfG00PF`TCP42b1fl%mkJBM-`*3E5=N?P-W-7PEm=&#Hnw-8}a}Y!BpFq(Zk?IzOJ^E-CShp8`?7y9xf`7w*Mjo4}l4`}26EPWTs{l%JGF!KaSMhgeJ<?yg7cbm2z4uMA*7b2@~O7_Xc*VIG>$?kDeDsLb#*lEEqHZ>1aL(jz;MKXJ_qk=}dgpgz*Du=5G<YUM$xofekuaNy=K_Z#)wfZlYil}BBdS?F|jUD5^NW?}aS{LNkbR?AR#mYLxIbs=B`I(r^yH3AwS)D5J*;64318?A+2r+saPB4Q$9LYMr)h=5SNffR?pT>y-1j-&_*-ir}LLV%)ZFi<`i5ju=dSjV&=qOE9#?h;ihe9wUfdJt3|FrlTyktWN3?za;|Pd#1NJoQkKsxPYR2jn9IJw$05xFY>X)+2%F7pc0bD!UiY)rg1f>z=@`mHYW1PO`T@&-Kw`CgANO#hry*o~Xf-WCmu#b|htwNKeHabv?FYLZk+2jv4qPuiz?`n8ooZM7DE!0PV_$pCqs;BYeki!8U#sX`NC$P~JNVo5z9*^I@OXRXoGwK(u79BA3hxtERb#2lAn8)Q;w-V(V&`4+5@cR?#;4M=}qXpsDJ+cscuRv)>V$t8}mk{q-xiW4_^d>L%TYu&Lx<gl}&;%@WZIAIju#=E1Yx(BmU%wt0XDO!zDdGWq_QTZwyWIpC$paGmjYuLb(&7pg+Y=t>6zq*<igat+8&mT?XCctFAk3vGA%Eq1L%|A<a)fD$EjOp4Do<RZ>#^<?U~200zG(-FrMVq0JJ8A1kvRKKzVb=OxyfOoH&Ch@w%q|&rITWv2F01N_hrdL&B_8=KrfPFMa8t$k>QV7e_hctTz$-v5)do_<EH%yeDtddhV)aUa!QzJcG`D*?ZIK4pQ2j1wlnm=`u+SfN2CW_IDf_OM9KH6`$AYUXg4B|;gX|;Ic9qkGmb7Ihyo-M+?GN^gnQl`7eg4IT3VYsv)<-Q5AfP3_h&?h@~#vwYsIY>4rvUoa$>Y@>WaV;-n9IKO2Oq5GXeu!E=+5$dj8!ODH{WkY2+Uj{2E>YSLd<$#T&H{z5z->vqHPT65RF7h$^9RSCcc>=giX#M^%zP)oMt4kCOf1v3J;EVd(SsP1c!!C(NiB%m;BKaOu9EK9nx#1Ss1S7^)+!G;q`-XqghK^oytT{h7E6LuV;NU|Q#B%Q5D9T?Ozj$t$J=*Xo=_-qf_}?559!_KVYJ36T?bS(o^j>c!Ms&5&b<u<=+;z4r-wi=2)`1icW7YuV#g_uo3xfvU31KEB0yn#Bkl6J3Hf!#8-+~&IsBb<PJ<V^4w0cGt0}nRY`c0|)gHRpjS@^3vRO1Oh+wQCe389>TTPixMU3ztJ5P=Z0%L$EPr+>p{?&32^BaK>!d-SLdsP`jdAF|DdY!{mPi9C*QM-Nz%Jy%ESDjry3>5E}LkJjMkt6{|##i0|C?Fykp=S?-S3QbdiLmg?EyMZ#-f$X+Wt=t`i+i-=*Qb^WTEF}@Q-PmJKPX|_azm>#ro9&Bw7oEPSLBXjVWr2R=1edp9oA3A?6|`-Snt3YEzM8HgnfXdvKc6?0RO2zrllH#pf%jOR1Y*<DRO-TYFRNfuN?5f*vwz2&GF?{mw{!5Lo#vA3Z@kN&6^~S%VN^%dV$?KlEhZPW0DFa!Gv;l&;J4;<YB;sz4*?BTCy{GA+Mi1>lBs(Zj~75nw2aiAtJoGA0ch6XeL!_TLqZ&boy{b5xlCR@!>%q{TAZu9dZe%ofB5sSZIy`_)=Vn^BzpB5p$Q;ZfpqzuJzF)>f^xXq7sW+e^nwIKmo<+-w6O_Ga&zh0xEvX<US@?9P&@fH4y_0N|g#7m-*LRD234hBL8C?XuMH|V>%yncu@HY=G|c-0IKpGv!<g3aXz>Hwf8}2o7M#R@}TRV=5dpa>FW4)&0_^a_YhSWLPA@LFV`B4#1j*EEb?M@t0>cPPCRp@STr15J=eM*4-yQtAovdIa@ft#uq4po&t{7jg=&~&Xy&**x1_WTSBDJjO_sWFS%o+-aAYKlNq5d9GZr>L->xXcK&rse36P{Il11*FP)M4~vc`7*Pn))HazH+m*GjCJFtln%KnJLaALI6P(NN`e8O#ml^B=Rx*aoPG#eu*BKlBi5?WGOrlxMA~p{<1556ZmvF)9PBpv{&6*l4aS6%T2lulDJ%sjPR{e&HfFDA^lSJBM}p!R4AToOnqCWwDm8m#shwGx|W@t@G0wZSs3$1#qQ7Xj?@O1w5cZCuzDd3vn!Ut(8l^<j?z&Mlj)M#X8zdGp-WLH&Z6xozp2egQO3dFGGXKe%+zBxRC&fU^0LQ;3(#W%FexqqP_0F?+zOf2%PjgPC8R3n;g049W<=V4)tCqEnClmy0Fv-wcnF!=FIm<>oY$#<vY{UW-+h8Rhj>Ove_x;MfPEQ3au#-1jaCSsRwEBuD~9N?!cQU@<{MES*&U-C5Ms|TCJ6$%Bs+g#AzOPMXZc;?H>Fj<wxwIWUGF_s_|3z<AtIQq61Tg_<{$syFiOtcunTD^@Oe_MoX{N4EVwPaWE(_mTw#D_--UvTEV_mJU>L+z6()r`pFqH%S=(p=aq7Z9rjAD?2)D~g1FG4;wf^c;*Hc?RhqQsy)A$I2xl!E#oV4Qzbn^|c)Kd#oUz16NeReyj_sXqE6p48k4s(wi?d>Rd%<xLJ@a|V(R<a*Fu)Y5DDqL|+9TOYFM%VeQtgXT&Rd6F@ylP$lO%j#H3~&<3mG{0Jn$C<HdzJeL`LkKd}_MjvVDr_EZlNV8wE2Pd(|?HT<lGq!*7@!Gq~xao(1{sI7I_0N#E?TitC^DIz8}$TQ|J+PGhPr;p6SE{`JT4*8A(F3>uP+w1mLsh+7oz%U*x>?Be1V+zq)uk!^zks=bsxq=HpMVUF=h8282jaqO|@65rJvUxdK1=GCjdR*;oVAT~61g>Q3&`9$BN$+!nfiXvV3`k5)9d8aAnVtByXlLlqsll%sFmMP;C%^=+`b`$}7QM2-OR*VB}2f$Z>;3U7ZBhY%hss{n6rtn#suj!TV7<;5&AH#R3PRGnRwQr)Sr3O%l{x2<k&+YF2=mxE0d*}x2qfBI}$M<5+=FmC-i}!%`!GlZbfKNy(Zx)O{C;Jy~GO)np4RCwG(u|Tb0^MRSYE>Dixr3woY=hucOdDO7x%N<_>jJ#jKD*izICZ6?lCgxvK#0Zc;^XUZgSCU_+)n!nuxkx7!f<xc@6O#3u54dY-HT8fPpBLTGTBV&NjG1EIz(KRa;Ze2#ulr_b&^=!rT!q+sb4@RzGo&1+-J+Kxj4&6#a8zd38~yr3(3s7d6z;h{U=h5wQ3e%(uoJK(V34AFhfZl;O-w9M;aRjQ=cAsa&1&mI^X&kE*Yr_J&eUJdSY0dz`WVNXmo<}Je;fBd0GbYI(JTnt2^0`wJU(ZWDB(tYL@GJnMa3O*Nw0-19LBqX!|J_&!=J`UyE-`F9BcEm$v#)8Rymhzz2L<0#3KZ2gL20rTdc-j+P@^#@HXBme_<#_enpPNYrFrHNKbfn)06v$f@by&{AJ(j5)P8Nm0>SnbCDv<W!88E)uu<To=LE2tm@1!PG_*FJ~dOVA3BrqNnWGTWvGqpDguvE#CM(H0OUCUXjWfuRxLD>qy$noR&)j6kQcs{hH4ZS3Wr_$G>At4lf*q8+L1}Jxz28u-(s9)QHKx@vd&%VoH4x;i+{HeNqtRWJoUvL??<frH>LSLq?DmK<JC})lsJ(?X;nYr2yhnufwV2c0ZYd#dN|w_OzK*N?Dm>Oh(gy7sKrP4^>d&VScM=kioaSI?#WYy}FGmnSyHGY}lZYi%g!T<W};fZcc6`ro6^dlLjAtMf3lb&EOr;ufNZ;8`sRjD>)dTo1MP65hdY~ukX7;2Qb?5bja)o;L4@jZ=B89G3Kixcn42W#hD!(DKV?_XiGy0m~t*xulRT|LpQODq`3=HPWI>&4n9Sf77e+2lVV7!s&j%dAq-ZXUpVm)`Lk<o3A=|+ZH21Yn`8JZ5-|d7B<I}EeL%esI!!kXCoVF1AP+w>GnRzi+~Kcl^!LVerJ0q<?yKza6lIdd%{uf06<Q(`kA^cb3mjXXT<UB}qcbo&;~EH3bgDdO?m*Wbl96gLPIZK|Y|wT%B9uRwBkQSeYJuV;PkcT;>_{}8Aa6C;k=rY)#V9#>ejkbk?EduUFe_y<bje63`hI{W*(WzF4TEL-$x5WsRPaPGUjr9}-)Qz6RA%zz+5^93@8bYkLkinADbIIwSzdV{k}FpGOb*#JXep2N5pTu$d0~g%JH!z|smqJ|y@XqKe<R%6VNjcbw%<6Wnx9y0px1H0)Z3%XGW#kFRUk>dE&;FvUUv;j0he%iF>19aZyH*Ff$fZ>tDVWqKQv5Q1#|wJ#6s9gVri2(NdE)JKV9LnJ6o4#WA@R9DoJdfhiG<pydP8F{eSVQ#;X;L?$B+aL3{*gb$6R1H-k|_;peGLJM_I(<E`n0y4$K-D(Vn4mg&*+pJ@8Gs*K_@*5*5{A|PmOxUqpMuU;PgAUW9<bwrKjU_y4tW<3ftF#%7c87*N)*iFk;{i=iiKUi=XyJ&<3PAc2&o)rAVBfpWH+=d?=uHTBM`VmPYHaGk^OOTw^+OFHy<wiC9hINHJP*+H@Vv!eO#tRf1r|h+uNeRkRGA=}GMfn_L6;Xdrx>`jBRqXBclf41_p5s{wOc6FOlr1SB$Y~~lB}=E#m=(`rKnxC93N05_h0MbFg~n=7`IrqaE};-+2~V<?+Nc3w$tu6D&O?y*R=v{y69U_YKz`seL_SG~0-EE+8qiMh$3X3RgZwCCbZT!xsj8<3aG5J?mM=C|?go3!uzxsJ99q|Lg&>o@Pjm%~bjZU7SMwN^T0N{^F0wO)2u3<%F^ZlgX;N}%Zx;Zjzt7B_x)xpXws?}|gIwv~NWY|GhlaVc4RsipAKbIO-9U5Sw%+}pn5ic~4iv`_)Qd|>#K1hNh+lbD#z3~^Wir98xNk!bQH1rezX&*+nuOyA-V~KMuuf0nprcr%XZ{?E4NXSVh{K4(UOeP}HPN(0l|os#qd=>z{d;l=H|zH{y=USgEeUe553dkt1h-3{%n8e5A5T_}Y~{oEJZYxD!kz$A{Tig#obF_b1H!5lS)|_62kY~*L70r<u$Gj&-!ZJ%nmiQt6n_lQ*onHEaud=85xc=)!RZI_xuf?RRVuGrKWk1C5Ntv{7AyJ1q$eo6MO(cyyYOk&GSNysf)LdP`1IT;kNjdr?c~6~c85)X<;S!(nx<aK$%el%&o_np!_T@=ND2m#{l)$LR{#cy3OesGuQcZAs6In`<D(Z*v^_CM^oL@`0K0AYS%^8kzLboqi2=paySlH};oOf!{LmB`r`qv<%b#3j*wIeK>-pYTU`@b48^%jui08}bY)<?VjSx-P`bIgkegFE(<=K__2f@mHJXx^73NgiRXO31mwrJcH*J?RThIkkYDCIIR2bKY)@66K3E`I;boW3#TmgA-#-4ilTh(9zITk!=kwYJYzQ%aZ*a~i9vXfb$D%t{y5>YBwDdCOgyY!U1?M4HkF&r4MbTw$NAJzFPExqcSl2(phEUN>_m+9zg1)MFa7A=uW}0F@uVh7jNT5BBL<bw~YXWQs%@YW~IWTe$s@rD?unNRTLTYM~StO=+aHW#4M-K-@aY`EPj`fMWs4T?KTOcfqpGfU^?yefSA1DHNH~({V%<^pGY5FDlzzTs-+Y2S03Xq8-Max6D4;{=~SRv_BTIyg*LZMsy?$7pN2IBUiHOY~W>k8*3%K6%1<JVnFPc2r4jOdvv^Te<Dym`HfXyd2d1@eq$Hhjg<T_#cx4#qB*y4rx#a<mWU{?@8(_L7l^1c5^4EduyI^740HAtboUcz1!}QUmuI|5xXh)cNR~mqzYY<qtFi=46y>m`I2gO;E&HTvu#o0th$DRt;R`-}A4!_FA$|Ev1@eJeg-&=7**sT{Owrn(eM`5CIdtzHw8jPbgoRx0Gk7F(wLzxXodJouPyT%B-U}~(8(>htr1kcg^g!-&{&!9==xpK23UiOQ<QGL(FF6Z2Q@bdjj9hMhYub_Gwpq#XIgWW)P~fVy<*}YjeRgGhU!6H#-rC-Hc<Q^lT+Sp2^T}f&0hD9@+D+OE(;PBsjS+B5vhyfST6Fp$Svaw46V&+c8K-*!n>n`n{uczyRwP{+dfr{o0-*Q}pFBWm({lo+U0C@dXRQ3R*(ljYUUGI<F}esjZJhUsDQAHQ@o{(`Lg`go^?F48>g9^C>-shruUbJr8~kk{9R_jtB_z77V|L3yf54b5ky<7(fu;uiL+ZdE|9~iQUosImzdwt<j2(%}iIFYDSCR?ZhJomwrX?MO`m=C@(yV>zoT`A3p#rP}pHK!v8`62T)UD$|N)+rcHFrm%Ht$k~Xh8l=jTz;_yw!m`i|Vkx|5xuDp&+;nm92J?z;a^3#4Ng?Q!OsXEjsZn<NFom+=94UTI3&V&BOg;IRQ@lptZm;d%52Dl>+dZu2zYYDo9dH;4ppiLYgeRbi{btyB)s@^euNU1a{Hg'
    'GVE?<TyEI>)ArESWICf%I_(GTAd@#rxY%X|xpE+tml^6Z9#@8k{WAl9Wpg)&`Sl$wngE5gh!`~cas3|ApBpHZY-?{xi6>gmT{ZpYVg|J1OU4&m#sJ~l=6P4FhU4qL;VmXit1Z)kX1mDmOCqC_GR^mMkOlTBwD0<E>)(gp#Rq5ABuL|L%!z-<Pb+<<qW=ZA;kxT)$mOkHo^7zCbzM=BAuMjMIMh^6mMull&K@xH?>#LX1*E2MdUGpd8_rmw=}F5!G*(Jr#${O^xJpHO%)UY7T9A(TG8Y9zZp6C~QZ87GW+6lAZzH^2UOYUL#~EKS3Na#ID=d-T=LDabk9hzCK*buoxQ~W(V7(=#>WcS<1A%rL5~3)b8*zmLZ!dnO%&6CmfjlXo*95c@@EF?asFL=wW)Eo5&>4O=q#}Jq3fEXRfwr3>MBLjH`#kOf4NEMIvvi>SbpDqDT!TW{h<Wqhg6t>NvCX>64$hb7bHjfoK|EK-69h@9Kpt4d0xG=t=}6M)Wh~|6r#Q<Q_S5v8FzSI|?tG(`iGw1OSjl?)C`A<0T#3HHDF^N4OLw{d5w4S{G+&+K(_=YnoM@m*xd~M`3h~3S#DJBws=l^yes~{4FvUdF{Pk)wD@E)X7iZ@M3IYVN{5Pjl_L?tk8TKZF7u4nV+3(xeMOv<@yzn)nH8t{xZo&^5Rsrw<ZQwDT??l+&4PgZ$uEPuZBO+0!Na5OK8#<PlJ3E<!sf`>IkIr-L!-#IFn1(8<xsj;bxer51as!npqYRK>8c@3iNL=eP0)tQ1O}zcDdoqFGo2gA9V#Ohkp9_Te0PEF$v%$qgMXNV--M?=<rgw_iYMnY<G$7SW_ROKkAJ3r@Y+s*0hdp?p^lA**BDIUmF%08)l)1x_;Cp{ak3Xcnd8a#9(GuzvWnO@w-{4Wyzen0-go03f9^^5<aUAQtD<vU4adzMh#)noj&`=&`VVY&#&dc}>3Tsn91ckKoF&>*qZhK!`_cqm0D6?pAb*rM=yx?6+0ej~=CH+iux;rQ4U`b1{OAVV934Jzz1`exuM0FTVmhpsQ{B(i)_t8Of_y*bF)3?y`mhY(DX?6e>kGNbpK-Tv(?dHX+8m(HmxF@}Iu7$>Nh0tqpczrZo3D15T%-{zZ$N6{o-D2KV5Brv0{yke&mlRWLShE*3ZddIpR|gFA_A`Kp_a*L*ZpMU(%X>)reUV?%Hn3zDM8Np@s?}B0U*GhfpM`>xZT_2rz@?b1F>pceEm(TZ)HTQG516i~85lt|ME9--FE!Wv)vS6KUe_>Vtz)|+shMIV-hl$sDfq{fH!_n>=+qy0V1dD_B+3=PXt5C}a~CT6t;hp8?JjSRJH<MbXlsbIrj3P<+16ckReoanYsF5n;+;;@Cb(dA;Y4-A<FN5qi?1k=@#FcSkqU(a$Xdn;NGxa27Vc5$&uc-PVGCPHl|(y5UQnRm)64M9j44L8M>2^>aJ$r-x3D&V%vg_19O2=+B)=MfpB6`8;*%;*ZqX<;DA8g+%mZsmIQsEGUN81Y;!jk8c#H(PFneE&HajRu+~meLdUgZ2y8`LL!SNY!IjhN@uqKOCoYljf{(Li<zig!=jy3eN2@)8$fCP;)IaS7lc1kM0gF1y@kC^()@`*&p8z)3>jCqzJMLcAv?6x7pP8`#oHT=E#JJUFQW;ik%il>Tm0^KB#V69d+-9SXJI5>#2u>=hfmYPI9>fgPS$RV|weWi%O=ELiqcqyQ(t5xnO8YaqZHQBW&c-^D+(#~{Z=X%REEmnZzAsmFd?JF^{8&U|bZ-Zr<z&C%=#;*bxD#>G9f@s4(3aS)TROb@Iq|^M?IIIOJK-E+kNitSNB}?KE!DstlYm^;VCJ47@9j54JQba<+;Ll#-pA6Az141Tjr{P>;>dVsSeJ>Xt+k*R?Pgj^aT~%}j^Oh=%JR|FlOfb_`r}!Xk-)5SY=PnZ-F1+H2*LjetNN-!z=oUIsQ@7o_Gp8&9K%`m=oq>$AP+VB2_i<X9R4BV|+J94y!wE4z6azL}AH`B_FiT@)p5~s{p2^FQjlT;n*XTJVv0KI%@p$H$-6J_VrtPemNxeZ@+($)fF~6j^>CY^Hi{hW)9#-7VNo3%h|L8nrc#*iM4@bKU+_!t3OZGJ{(JDrR*bMfBmSbqgAqG-az$U6054VcWw&i-vLDG!f?A22c*Hk)Wn|E<fsbmRab2S+6JK`B{b!iSH+A9l3NrZi`=)Qc^ClTLT3BlsVRDPu=3$~S-o1Tt+iHJxB#ni7rr^G0)g?Dnji&#T^yL{R(l=z(+E^V=SH%PLi9PLVa9XA;;Y+UbjOd!iUGjMU*BnB3Ai#!5rEs|R%m?fV_>@1wO!9iG}p=JHLLNxn7m-=T(Gg!YY7_3F2@ftA6-Clf8$}7RA37vC-18B_7m+1;P%o7BqMjTaPcXg5{q4dUR55YL~GfTEl5M7iiZ+7$ori!?mzote&(sWX>NbJ;j^dq$5DyjvKqO7g75|02L>UC5aqzJ!ROlk1G1Su%A0Zi%J<%p^aQKV2=_n5_A5t*}ZiKwMBOC!@cV?F6+0Lnow?hp--D73ZB|2)yD{kY&R+tBZ}PtB0eNviV9w46TSC8|fCq-&k>AT%<E$BH80xBrJ6&E=`7o37iW!PE0ES;dJ;f@duG7Ting8_c@m5}D1Lw43sHhPUVNGFyVy?;X@5{nOUbZu^r#y`oF6#jD15uVGcusZQqg&|EuR+j_u^I1W>6<>Sf)s8m94c*N$glcs&OYZ|!G)w45x$<#dw|8U&+;D3MiLSM%uqd3CAdZ@;Gi4muST7f=La~Zeuj)g}bXDWd_LvG2E8S4{(SePJiA_DDH5@Rv*QNtE@8{gIdQN=xGocD`e<WYAqzL5O!tKP<qusn6eJRl=l-bmXXhp%%rcdiv4%H(d{eN!b)*JVbWInFUMb88Yh8l8))1gJHW<@9_lBJ>|_^Cw3kgkO38|6Q%Aiu@DdhV(}G>T{aQaeUyj^v9)F6UuKVxrv+>R|2G$N@wS2*MWP+$7KEAn)-2~(|`khr)#JcZNcKKvHeC`rg<+1gCY)xGOY}p;g*chFTr^8v(c9Fa+z9WbYFGt$qnLDh#?37sc8)g=o1p3m=TsMK+nQ5AbUq&Uad*-1LkCG6&mRT2Bu7uv5Ly_w<VQ=H1-ICNF=%<Z#^pf(rl5-UYUBi`fA+N1lD0ogAF4OaidUp4{fw4`M}RAV^&GtM(yu0WNZJlS#$IzA)O*i_%>iERY9lKO(#p!0giCgM`}rW>W<ge53b0uH()_0lb`uGxeZ>X8J`PcN0t$G0>5tBsM;+_4I8vVi^M)t6+IvNwD%7wS>At9tP4ON#EO`4kmVLECz?2h12Yt74=6(qwxNK!OL-ez)I*ZWqEyK@HFalSm*LRO6p^>ZBZ3+*$Rk`VzGC>3XV)*TqmQ4`#Be)2aP-q}=W(ogcZ?DM0#8GKBDK0sdO9ii$;H1H)=JiNXdnB1GJLjgv}EqRFS@*kHMdXP;%GvY8k9fERft8qk0Pb!m02$B-B1*6eNEb_QX7!j&p778S=b&YipEgQavR@&ohKXd<NBTxWY|WHTJe=5KOQ<lIJ+YN`H?(UX0t`$_S$^!z<gsGib_K^2LHzAtG%I(1;OBJaH3Z>xt2CwHuIES<6>&`DGmu@N(qFOu)*BX@~O2r4c;P|eAPf9N2agM&LbszcsvOt0u5O(nMxV-%TEc)oqq0@o$k3X%Ec-R&V2BJ=*u)O(U()q4{g>kWE4%INQB!Q3#;K>=w?Cna-BG1s0#5C=@tW)Ziay0P?FYU<3Ty*bX^YDQgxdV;A9TT5>nYBh^1kL$GTpsvkc9&U33L{?4RN&R{Us}y&a7)ThxCM>xP-Kq1Iw+Mh&+(oc{0tcKJ__6h5~|nq?)MLs-C)c3yNdE^Z=>If<uK4LeO+Bpf6gX)Wsm-e~@s+-=0!x~Z~rpZ9soTswg^T;+Lfr!QKMY?5C8RdmvaW?TscEv$>88S>`Zht(iPdf4}e_~$+3$U(mADyAKTGkWe`=yG7E#P=%J^p`RHuPvBEWRd1wnz4xf{bv00IJcRQnIf(-5KsfB(QMR<b|CkCzyH-{NqfVb3Uqz8?SuwHj<Uu+C#yQoCR71Xc{>FT^7G9e7v-)sSYmsdhycpq6wXfA-qUM(vV2T!IMi@+m^R9klQ~+wyFnnz3$TwwIq-!+9X;LJEmOonUOl!qRv1Jx4WlFF<Gf~N<*Y3?dKu7O7~8bF=xxsDn&J`=;yuG!-e2MUTh;3M<3wb!ZDjqd&I#wMz-<wYLhK8i`&>BK4RX+`Go3VNkIg`FK2&I-ogBO>kZl^se|w2QG_)ks7reAu2a;QtzeUBBY^#KR`2p3CZrtpC-kf3*Rg$LPxD0^c%0%cR34GTDCl+p_dO&3fT_?z(<C=xagl}>_gVn=g@@kn)H+5t=4AHyMBlMu_KQNgKAxN<9x|8jO)GlO`BX@!#0ytEu1CuO4qYHE!7(I*`hgLupc^wCEl_8UKz0A0_)cZw%NT2r$_d>#qOd}0FAAG}BH~jL!Xfb$TVTd7ryM@~n`4d%xVuG=P+NGL0Ljds4s)$RvHb4Y|rE!O74Ax!Ain{Qpi($Yh`s}0*sX`wpgW*nZ=(Zr;KN!Qm|5)GiNEai~b!y95t;VsbAiB^v^C)o~HcgP$I$=ao(I<d>AeN$F?8nJ!_-sXxFRu$Xs1qp9k{aRNJ3xD?J65vl{)a-KB%l(&X-Be{>Eq(!ISXhNYtZ+JODFfalM}s5hW2O&n=F+e%a<PT-O!?m8_aT#7Hp&qb?VSI3kh9XK*Ta?mg1dWfVILi>`7I3ZIXT;e8sED@Woa!QKb?<Gc;{xqxl!-8}C^$Z0X*8+?<?CrDx>!%xxEWrI7aKL|KNrb?t3lfB@eO^}2Zlmv$4V69TNk$kOdI3ieHf`FWu|iZ!zkNw|NkTO>A!Nrx%fb_2dYfjD9%WFC;l`lcxOfB4W;`Zy}&$<k_6sW}rhl!#Qx08i<%2uqtmTfu-NG-R8!EM<(n@X5id%b&sapW<ra6{q;EYL1dqb{Ar7XLAe|NaVSzkrL8I_sC$TI<C=A${%*0Mcpj+jVduL0IED@i!|DR`X9;hI3v-fKQ+|WH8_M^{SUrY{E}tmsDzXoXv~1g>-Y=7PqjUnAF}^^DlpL1;v$lNp))rMM{LXJO7UY=K_4R%L?{1<tF>O%<&5+POXY964^=IsqP0|O4pyLXf*j&8q{@^5CZT+8T>7(G@X!mqi?t}@bCOYyiqiF1>MC3*oCxmh@m1^G6*qtj!|3`gISH<j^7<pm<xHt4^~mUkTqnTIJRLq#`__@Fmgj9jh7M0+LH}K=h@7kJRl<k)DPP)?mqfKAkZ?2E5+mj|CYUEIi>qx*NW+#<<;1-nLGb(3A>PfjyC1B8hz?rzY2AA-)=C?m)H%{=&XluyBBTCh{h|wm8K%17lsQz1UYoIO4sWc3V?vX;Ufnjl2!n&yvdUM@@ytSiaMf%-ZHzBzVlu^)8?$O;T_eL@houM(O>}Ho`Km2>koqzTGW<>(c;LFn-O;s+-4s}|00mpPw(1CE5M6<9rPk*%4e3b(<b}R=is`kIG;_m<IN$Cy@JXt;X^O4mIBH~JbJLd+d({i+WptphS&35CR}jyiW(^d)XJm7u_$$b)*ffLrHvQJVB$5-m_%Jjw^M_!0a_AW@lioN6S_aS=D1M&*Q?1~#2je46yiA;*Qh^V;QVCmRwoP}w&<(EYNrlp=aCo)jRS4?QHz2(@|9;2i73Gd#a2>Go++sOFFYubP?W4%L+cyDKy72E!WrVAR;W^10n@W-%h3{tsKwQZ@AES$L$H+`AeE!TgYd`3U<aLIFOPeswV~Il;FQ7F_AAPe8s4W}>?CCA?Xo0Xkgy=9n`8+}}6)kR}gVP~m8tYB~H&;-<w0ZEVwUBj#ts}N^tHI9aR7K%c-}{W+2Dx8fiflfClXx=x=Y3Yg+O755a0haBmHZ=Y_Y!6|a9PT4Z;JkRqdjygalB=Q)2KctJp?4TE!pK)?(;uL#eVy2*nd)zn4JG=*Y6U3HJZM1<O$voC~%n#NAK>O;qFB9wDd66O2~R=PD=@n?m$NzHd^jrr12iLU&dsO!QCMA9<W+6$D<>GH3M#Am`fO)pv^RXTicp7KZhLqdO(6CYvQ{4#Pk^cA|6g+(j?8p!?ugEW2Ph%YQYqK$@GwZeb(piswvE>OHgM0;1ozuR+#1F#eUFJh1VJKCM4EzR(V!#9%nSE(0BLp|17u#<qASEWl5S}Ta&o^8nI0sjiSo)dWP|f?$VHcTcf`EiByQK>5k)jw7pvP6HxBDX#Ot?Q=O@3De2EY8!Z^x4tG*0(WmP)GWA5PMPp@YULPJ#C%d`4o3YpM2n7CcpN|I12dM8c(qQKCwo9XQd)GtOh}=hBs1^}G!&nS##{?Kgbf&EC94XI(aob%6d3+%OiOrNcQL4;Y3{OLxcUMGB_#N#c)+H7qA=BlpnV-J(5Nwsufi~djk~IAX3Qg@<9oZOw^)M@kfn?0JfpCz~z+&U?&)XavvZ;&a#0+I8$$6y?q7GsJ(C_dLc}OI9{$q$M=Q?x57(#a!XW1W7CG@o0uZjVx!YYg2&(OU!w7aO2>En@)BJ`&50^l?e&lSr>czO2Ft1G(Xm|=q{?NLFRt;EBQ$k~|k%;l5v;F)=~1xR1W=%o=BC{!ZTTz+?g^nTNo-emndqk|7h(C6End)GLx60FU5=*I_8hfnwTflB|5x0S3lVWvgj&2f+@nIH3{wx$|p2C@EMchIJ0vt4>Qu?(hkn)CHV@NG+iSQVq27btI0qJaNe!(MP4!a*Jy8H-h^E*B|mX6Wy}3Y4HLg;K18Y4=c0oVTN8N$$+l_eXwk)>_9Zs=}gkGv3=+h)vM(E@k_nK7W4j`*qo@+*BbsvZJ?#*$N@knwj^PbArBZUjz2W=acOatXkiiKW7~D<o7u|P|rtcQZOkv9f@nX0{oO4*PFS$7z8x0b8WQM23w**NgpsQqHb1r^6o`gZ17%pm?BWm3s|7yX<hW51S7tOf6^{tyGCQKeeDgjU`|>MWylUKljpM1n4MHr;=vtN)U=2<R0IhA$NpvvitgloNYPnb0O}<_w{G3BdPGrGI}Pd0Y+Rr9Qoz16?bHU6Ckr`82YZnegDU3Xz}A6$D)V;)bHNx+##B12g)WTnVI=xMEvDW^q>$?So@3YT*xTXX7E~&5?V&22)NGdHIf(FsE0g>xDZb|?Z=EZ<t**|T1!esZfIB9I7Xsd2df2_jE^vdqj=1_8X4t+x8hq(A9PH?5KfR_UwdzSTbCb__s>XMV?g0%9Jdw1Q1o1<g&op%rP*p;_vpJ0w$jmMU>fC&b?Mhmu)P1CI@DDA#7K*%z<!88M@Pg*Oj&8qe>o$}{AeFJ0D@bK07>1frA3P8T3!#cDaV5ql#jw%IwUx0i$=ZR(G70H<p1xzN8H$g|O~vJ}1#jd9*#su+u4ow7Q|fY5w&^*eN~Mk(P8E1@ue6V|IHvHo`}N@`e7bJ>d?RtggzF&du3d`lC=Qyj<AY_OSQ>!}mNrzcG139EVk+kb!>=xIsc8L;kZ=xdbsEsu>=wHQ^d!KCc5Av_#J5Pz)YIF<#FDY0uK`=+7&=#!BN-r83QIAvV(4*P`;yPRB#@t>eqwP3*Au;}z>t}|l5PFcMe-tNzve<}kA~T_Ez3IELfu5D^J0abju&h7i^bd{IK-cgHJ-F!JAe3ntw5Cu{J(OUST+3rQhJ(hL=S9jpqzr7QRG${-GTk#A|2uWW^smWorxfBs<ObH``w+UH)*^Nh8X!?J*^l3@qrE!n07%Ej_cE^_XV?F7AmRJN6JqhQ^DkKNH$XAY4&i)#mf9Z&o4h)dEB?ixM-%Mpz>UbwNrqjfT$-ve`B2KvTqQV%>x#74dRA^PjI38AU89Mpt<<8REz&2^44Js$I4}I^e@AMb)AQX(8M`33uPZz6#P)Z4y&gAJd~-}ZQcS>GkxcAWpAB52>#b%|D2OE(XiM2s0P=gqc<D)Km@r4R}WEA>6M4^LNQi57f*!iPrR;-Jn7PU3(DZf8v#?0o9AaVM7=zHIzC|7IUi74Ur4#dOAEYUJ%7k?HiEc)Ti8{AfX;O>{De81%e|P%6f2Fw@9^8@ezK!sUJR1~uB2SrQcN0qjiVJE4!!v$1JdsQDdY5DFFRc$3J*u^Bdgn39q!KmEcgOs52Qb%&zntscXqP87!vOe9BjQ2>sjYr|0--dxb9C%GNXOU25}T~AM?_XLal*1ADa~&a|tAPKJ#;4$)3|z8GByhm&woktNvS&3xS#BL<8?o0=h_isDTUcLQV7RToEvXJNDMsVsqK|VMZP-W+e%QX`0<YIi7?e%N<y%`~PTvvg9{#)Fr!;A+E*zcsH(^_s|(A=Amt7@yiWL)(j2xrWC|wG-Td5l-q_-MU<7;#78zcS;I|0&BV;mFaf~8x1_iTVG|G<WlzG(b?`qQH~u@(Dv$(DQBvc^MGgmEMWBuS8~!xZ-k?N4O8vJG-N&Q_nk-jgEbs5{=G31kRO(+qvn`Zj9;^&ad<aF?Ph+#*>l{<i5T$2rxtfORlZC0G>(;>6;eLH4yxkb+-o5wf3dz#>@<wC_p=OUD>x5g+Lv1xc7yTG4$ir17_Zdpw8~Dk>GZDxhT@qc^8vT2quDMEB67?oo'
    'R)URp*JRT>zIbV;-@cPQH{D_=6fi(^DmyjxpJ}b(3_|Yd91W*Guw3?+9bl2JZA?}%NLDLXz}LEJ$hm6BH*fx#L4x7KpF|)g^gJ9W#w2kEMgxp(_21Wa(Z{a#B7Z#|?sofX$YU0LwAI|0Uh!$$HzWK4Aq6Q5z#;GUV^Uu8GRI}R)V<;M$LTAVXSH{gu+yV#e3|&{^}^`J1Lhz`@_({4MLb?`)dohSQAJV^tIVE+!N3AQ@FTJ7AwJRlQRG31g|jk{q7d`0;E=L5WJmv(SBkBz4pTRdE<Iy{Vr_tE^7s3k@NF)RT<<LBYP~(?dFK<*M>oDSNJK;>s6Ch4$d`wZL_mi5L$IGpfe!-&5-zgHi0>Q3K{I%J5?cCR84L<lG4P&)I+2M*rr##L<h-`^EKE2;Cf~2lwTIc+tw%UB4?4xAV5H_EOcTaCjjU@|e!~2{zT*L2;dgbMCj`@4@D}cHnZfS5^^QaJz%4u|EcoqZ6xqQRq#0atI63hW;;|vL4$7!APQ=1dijyj}uQ2!JiYe7G2*)nYh{V1_18IRXf=!(;RoQZ-IPa#Tsq_@=?~_=CPzl4H&Y>W5qAkJ6TDw3J@*O<3I=e^mOyt4t+)1bW#X639EBEZU0{DIJLgv(_#i*nj&0Ef9JhlMfPii|#)pZCfd}`;O8Vm40FNK#*LwuYV=EsNg)va{!kaAd@BnG<|h?v`5iJi}R0dnGXz-%sGjHkDI5EJ<WT*qU#6ww2}$}&7Am7)k%0VV4r-)Y}|8y<5DS=K>2)Y|@t#yHSEg13yU7*}Lx_&zBDB<bJ(7=v&K*4!tfzN9-Uk{Ed&fM++vq5fGvj3$>%%7#fBlIn~{tAYw9G~^uZ0N_J!3SH<^+sBVcDF+#KZ(|&!roh*BzpVAH0KTOkrEF-lY-HgzH5#6_LR|iY8R9ABNyu4gY4c&wsW@xR3%?_K)WbUT^{>iv`U(-!yoD=UE%dhn;(ktwCV<m$@kh@(vxfp9lb_J1ui;=at!2%!mgXzUR!2o1@QL~%I+~v|fxC?jw_>M;)Dhb@BO$}#(=A|v<m;VmhQt>hBA$q!ci85?hMaVrqv2aUuBOzm(jo}#OGbm+A4Fox%YfR8SF=QA*atLUIXLdAp6;opI9M&j9P&gwr)-4m2yex%9*Dt_OYJCdLE;*=!RbX~#Tk;_sm4YrTn-qc8z+o#tk37cLN*%MrPVoJ%e3&4Xe%7EMX44))#s&qkdv>eJjTkR$kyZnkqXJ4vQ)LCbiy{*=*lxpvN(}K6>=wIOzw3Nz_t5{g#Y!w<>^3en{V%mb=5&s7Qrq`Jo+d%a2;Nop0sE4;UOKB-BaE)S0e=yc~kpOk#aw+;ssr%fM6dMeJPhV2^^hDXUG<oX!38Ch2fiDeP4cMX`!AS<9e^`2-?pje9W&n7R>v>njq{{wo$2(>A{R$2e@W3FVycPO;ZG7S~2(k9Ny{id0YTUIux5%eI=fi`rEX0VGZ^A>BFJ<yM#sG3Ebhsy@`(vW+|5QeFxT`Demi98MP>jCSyRMG?QDQ6|Y<$-a=%%2{<y$WkSCfYZZ5zcuX3snSvpc7X>ptxCSiFz;P#f^%fzS>0-@buojZQP;!zmU&H|5Dk<k<r;OXPwdIMcqCJs%l*HpoN2(E#%WUCUspDiA5wn>|JeIEp=FsNKc7|7#2Z~lx$5cDBusnIu@~a4MOKGl1q?kc~Da)0Uq_<r<r>*pEb?h2xFd=@#&E^vr5K|YKS}%TI)I`tjJgj3^m<|Ohx`0U?0$$=+-2@7_-D(8Mu(hbot5!qa#wP$7>xWnV?puW-un<L4f`u*9eSbwaOxrFv3WSi7k-H%7Tvd?lcuiJfPX5vzCTvv@#>L-)amgbFBm%_c3&GfpG5YRk@Ain7NEI^i*v6}idsvYQVS9(>g}-zP9CYyDBWfJt4qKRJL~apX!hDEJ?erPkyWA|vScSd<BvR3jY-@ob%J_MpcUbgVL5+X7X+V)`EWONvg4D~5QH-Ko!n-@d?Zz#ly)&lJ%v{|GLXW2DCuN!j_NJXG@D|m5b=b#eUiIo3rL0B93FXOG))A~IZGDyvN0hj!MO`8@Zc!O<6|_d~^}LX4x!7$PP51n<xHu%97lea-5hA1&6k^rFwp`u4nx9R1F=r0*QzlXD{3#X7P1l**6o~ZD0dHYh`+)^ive_Zp4Oobxs7Sa@4h73GMNak@LM}3+=Zl)f(Q3r)T<s5Ly?4rO)wjGth3fGOxi2t4L<r3l1r%d4bnfks-&8wedW(3bEZ(qOa_Sz@A}<VCf>X{yR6%PAc8YKCPNY6*!0PWK5L%<!K}iEK;vjXw26EEz+_q*huwfff@ghJ#!3J)DPS3uZG$@mxqb5nBvth%o+?N|)J|-~-hxf<EP5geN!ObQihp~@yAb-T$IA&y-V|%+^<Dit^^(kTG>k>-a+QJsN)?4O2A?|x<_@5=8**Mj+((&mYWAcH%^T;8Zb18_&b9nvM2T_b&<sqPp6QKtcQrb=}xV(1l(a^;-xywss0C2Y$+)cv=MIH)0VB00~@zR#AaB$lW^r&c2S(4WVwrK+72cl=TDEOP=V@S8yKYKeE9P^@Dt2Vgf9vJc(e93k&wD@Z2n*Ko@fOS8G!m;jXSz$Pe>M8LQ#*}MNK)b)2d>bspaUJ@+n43%Kx4=WZH~~GXXyXj<NIQ*EemG99U#}>}Ev(8fb<d+r23FwuIBjYGUIz&~K#_XF*bmGY?9G-mW^_$Bh&p(72TsvBLG+@e%mi27<p$rPWCnb646(l+XB>o0CIS)DE`lK%gy<Ff#Oyq(Xm7<ERg?6(OK0<&+9W?Se<=|?L?a6;|LFUgIJ^<={8MNvyGxWSR791xAbFl@nPxUFqcOn~QW?zVPJqRl{qZI*QcS>ltqmAM9T*78Dk^^4OL(@d!t0A(WSEnsNjfvHJC!jomwXz8L@M%;@F-*_oDqA5+X(_|YiS6ey;aG`yYx~n;Kh*qbO(^#;ac$ux1>Ovx1-hj#R>Jq^b_ThTeDXt5!QFwINX@5GfX>Ml@O6HD)8$mnRBCkKU`Pt%+CgtzC(iI++ZKk6*N*STzic@QY}4<EN5oK+5qY>h3KCUru?G8JSj=SR=2vO`|BXwX7amofow@uofevtjhEo?l0HVj^|B?|ZfS=lge7|CD_uxf%L5L>goKMAjm_I|Raj^SZO1&b8bvFI&=+k|?SV`;r<w)_)S_bw+5t;Vc?T=7tC4bh+ABNg<a=6n8hhUObWWp4KF$Blb0aS(qrY(pQ0UU~gQo&7EP}+Yh<)y#SF;KThIDj$Y25|wV&%8F%<r1vg;{;|YzNa%VOHyt%hrodEy`DBH1FP(_9lpQCeilbS#CiUmg6ZTBV)bJW=9?V;t_0vDPus*#z&L}#LZQE;qnypunp>)jB6vvWS_?{P0GjW2~LoA!B>;aq(=OM+g^;gY8We726irx&$ip-C3ziQu8M&Xwik}muo3XElj6x*ebe8smtKDkGvrP%0UQ<L#3bTfeVFZQzVvf`z#l1;G<;FI00N_6Xj?{uZb&{;zZ8{p5PB`ik)FeF7_c6B(q=S+{F+X3ODefGmd!^tZ5SBk4cY9OZ^#3XJ-E|jWvg9+*+k#w^p(<PhgKZebJpBaRTkxscqAH9Cx3i#L<AMYEQpBJ-e5*EM^V8vf`nPgC(X-b!LJlYkFqJ)wBg5y4oEY2t^|s~o`e^FYMPi8G$H>t6MN;k=E^W-L6O@dIGz;tF;*_$e|LpUyfbAhW%`I559w>UYECXoa>d1Iisw!HUWRwFFWA(1hq6txy48)Y>a!J;C)eYNYy_cH@CE7l@jad0@Pf#ZGv=&tbdE!2K@vqWXLtai$nmvJs1%972e~@9QafB(nu~P2q{dn|f$(~Uy(h1Dgd2i^^O0Hk^y%rwNdiFZL#uNAAW?hU(Jb@Mar({9Wr`!L$>$K;&G17r;AmfcxvYxnN3BX~DeHznREkLRuMiusie1RCGzu!U3}{2y#tn`32Vsfg4u2uU^%{T?NJIWZifC_CCHF9V`nD~OmKj;TmJ7IWGezCnKhTpkMl0*7q!8E25&Z_3s6KeIwjdC&y$s)>a}RHJ{LG<()*6d>2SA6j(SMM3GaK)?SY|}Kx?|PuS<C%b-q^>+#wV!k+zIu<_X?Ng%_Yh*Q#T0!A~x%j%wBfW3-Y?BseJK=2eF}$IyPB4!Wzei`EKO{e&;Pp4-eoVI439GC#*BvdfNZ`ty6boNdgWhlDC|BfzjlA2<$SuDdzg)75=>u@>`kB1X02VR+Q?aWd9j;#h`y8{p!YBAuR8cml9#8L?DaHPG8t7O}O%^z&VPjSb(qtFguO8rRp2+toeDGnX~{?SrTCpvA_97%6(ib;v1vqH^QQ%UdJ)1>f^;-y4<2n`rf;&Lbc%^Z!Ch}5|d<`;y0uWZ^_~6z^sn2J6o@U+Y^XRci<SCvPc_BcsWh~CkUZXiUL|K&>YwI^pt1D+BRIOfnv(LRr{%1o7wb43rd`lL-+6HIu?H?%~Cs2+bu;Q42Sxwf6_hL^`*M|^wx=h>ner(?Vb5|0Y*thyA$^4p>}t(5mV>#l_Zj3GTIi`j?<Vww$HZN5C>#z`;kPVBc+UFXC0?)BLOOFhW^{#>Tngs&f5CYOUfAExOj7^_E_LE<}RU7AQ(4)))=2H5MJjjDfby*nD@lpDV5je{|IJmc$`D7?~+hUp@*TPv&WSu1=h7cd@qJHrbga1NezhI)o>5F&diQEhe#k`$b6+I;IFU~EmU`#25<UaJe%q<paGTu#>_ox<iPWipBu{LN>Z?WKRSZ|k70~!I9g!x|4}LWe-nDYci$ny_~V#QJ0&1=g<*6yXXp8UFCUslIcK@*1z2RoTn>SWKX=yNeVsVd8Xi&b6>WJHN;VMYT7c?FNC4A7b&Ma5Yvm}`__JLdHZYJ}!dJgXaO*M)GwHH!=kpN1vF~>+&H;;9dq{FY99Y8j>0W>fyyw<-t@e7$*JU{|l$$F}K_obVbAsUCR@KqlpWp&94Zbc2s-ncID;cRgW%!ae0>zKl-fBUuex^G4bK$B>BjwEuZ-}!{Fgo{IFib|k`)nNhv82qvj@h3L)Iac59n&c_*e%R|m7f=@2;yn_lE{?>d<1I|=U`{eWO~?WJ~3s^I$Y})kjW0p3iSQVQwd6fkGfxAC~#ZN#+Vk*Xxf2fW(+WX+rMT8vk2RX5_^Ke9O|n)9JQj2Izl&ir!S)ijC}yF?=lWLV59x>>t(><bX!6beT;gt5{lrf3@U|?{F2^Q>RIsg`aI@cYU%csH$^hCqivu}3P1da5L8vYNilIOnK3ibSqb~K5*`4NB(0Pm9K)~Y{V_+)xk6HB1mJZlaMN$dn);u|CxnT?Ek*Gp@fyz9RRxu&M@I%e_0S^pplvv9q4<Cy2!b3TX1iHpoGo$*^W5@pIjzqdugg1FG)5RD<Buwtq(VUo#{GnKHphS6AbjKkk_;2GvU{3FXc%^oS{cC<W9rmNp-gSwOV<SLd`zH$ZjGx3(ink?fBoND$~bJr%959(GLlLsICp9*-Hky^C3hkCZqADbX3@KUJ;6V@{Y#++nQ%u(h(+B?j#O!+(3B^+>+$`EL)vliJ?TI<gErl^Pc<-}0=<vCFf+Go?rEny9nGv`9xN+k2#V%eN-D`WgED~B(3VbQE@Fa`{?eWH)$_OQ2pV4(Ia$by(14>{^`CLkc|+c;4F`Z~_t?)<5n~$)|Ksm@mSrID_-&|RD`WfXUpx1(&6aQCh|+Ptg@gq4Jx;5kV>P?GQYr(JIVF-$RDr8nWBM&aXMr<JLWELZv3feR+s;Fa(R^sg*ak;{v~~AcyIAupALW=HES9%t6pmyAIIJ%Fl<7+~)}uzW+ng8GcQ`4Lz{|`1s`zTlx9SG|QKS*v*kAk!BLSgTo21smF5JT|45z4qawW!p*?yO?5%u1me=Z>yXB(d?uFu4w%3Q_)qMW%xa$y>&7nMex4P^+SPw?_b5h-=B2iw$REwJ7xAQ0G9sm#v5?W2Po>p^^b6BK(a*lL`xG;Fp^_z7OS*~igIIuP@%S%VETi3D3->eh>wxS9Ccn2tKu$`Zo5d+pS4bLbZkEBT-*1unc}qn|Lc&~h?RIXXX#*t==Q#1i3slES4lb?vmMBIs>H58JIK3HJG2_N<Hvkt5nE=Coyr)HpCIoG=6NnV-RFdQd(Z>BECUw8K+LF~~+a&B(OUe<IyjEmN>aPHJi>u(m~ck6LBqX(`c~Pd~KE+#D!-$R;u1K>P<IrI)JpKyDfgg<o2+ZCBx=&&+BAk>@yK<nDnZL*ui-@iy+Pco~cwn59_SBujIAQVeVV|E*`lA-SmQ-?^52;FQA!IX}q`GzKB`VK8{3--MbipYx&Xz`J2=k#N6wS%%z2Y5R#^AGsr13g~>NVl-G#p}}c1*y|<f+&6ng-i;FMnev~0*~K0^o>N$C>`z~zZ?&kowSO+8gc-nPXLSbS-gMVjBu`wty~7#yLWii7c}eh7zz`B;uHhjO+gB`BwJPLie=jd?7GeUEF3+JqX^yJiOoW-ab#qBUd?>d9!grecq~CIuC^>NQmg%~sk<gacP(^Ic77uLfnbH~Mp7fN<w6fLG`f{o*Ddv?NpYhR1dvy8S?1EBIZAG&_*_wzTPuYYI!nfwnUEY9Guov09MG|9LjWYf&Y|--%zIll#)(lzBsaX{`(EAm9RVH&`{HwHB{>hOrpP62ReZR<N7Loe%)8Vok+NwffK*3|pUh1U%^~WI~s$Wa-mHL3{x{HD3${k_SI$iFW4~WXa(3R3un;>qY6l`r1@2781+m3sz<M%*|XAh<>pUN<IfS1#6k7u}JKOo@?<+*N8jztFU!RlpXr?A=n;maU0w_2Tmg|x}<M6$OF-etWP>5!#ITGN#xdnn8h6td>Q6`#SQd{%&#7B3^_@Bi1qn#Sa#+P=8(v|Y<5IzJGVefYG0a`^^SsO-(mfsWs0W$HI;&w*z}G_RxQ))V}Q{2F5b7mhRFWVY(~y7qnvEVAWJCjzi_O@?VAHk7Am3A}-VZ$$Ds$*++sHVq=e2uul(e1v;6_dK&&vCrM*nWJ^<PR&-}pqac}6#J^GT??_b#?oS%8Z~0(B4{lXWqF|0IA{z;5P7@o>_4?hXqM?)9+-4cGX=E)7X%0D+plg#g)EVrf-m~}RDL(Li9Bo>0u(siGQz|Qy?}hV2X=nnlA1*8d{SSBmC&{0pw)&BOyzt^o~4{p9`B)dF3zLsy9_n_2)Z#V5q4ka0SY>V;60(>QQLa&<Q*`IU{)REuD?leipzTeF;g(V0m;M&ALw}<JVbD44?Wre=D1}bOD&P+n3=L97~sBa4lcaeC)GR`^4!8C4_?JO>-*_T#zmARJW9T1sr^`f(6ZZ|_Yl6gj0Msv0fjUo24s!zp{uyDzD|CiPF7}pAKRr9i+$~N>7I(GkqM1&FHgYys|kAF+nUd0pC;{dl+Zm^W|UDX)=&Oj1C*8N$Km3V{{(pc<()(O?ap^G$L&s8h<IoC2s7+wu@$MO=OQP2-d5MugTTy`a(`yz@JBOXbEe_FC+1PN<z|Y#f_n46X?$wA@YKdajfl>ZIiFuFI`6&*-u$}C9u#a|;Cv8rysaUj5*|dkP2NFuuIMQqF=_RAXx!v;`<S`2xsY@S!O}se!5&=@`)tevkOGG0^km<<8QmW?)z(sY0=uB?VbquRXQASwE1~m?I8-Y=lvX-$jN1=HhZu8<hT^aF;ZnC`-g{YMRPPZmqJ91^8|(k^U4u0P3D=|WZ=9cDW+`$E@`P)B!%$aXPkSGZTu=ocK(9d>05^E*i8`x~?N=$W5`werr>u-1Wvx!ebM7F|Pt^0Moy#v$F-}(bJxPxA>r_5lynw~?sQH<mtD2=s4HZLGTxTDN?ySt&!C9V@t!R=Nl&ci-wEEIAh@hytV(h8%!*Xv-tAW=6!J}w7=^J0iI_LigefDoa*j<~q8cBHBrW+2%=QqtbZR>s0TT;%iY2%|G^hvj9J0#xPn>g%$yhs}_n0m+nd3YEv6yOW@Amyev!Q&D?gxqZ}mc|qZo=2Yy2VTBFF@sLy`3aPTpE{rRjIb@2)Dmdw*DYLAyu6BG7n$dKcPm>03n(l6dDVCz2T_V@<#BJvPL48Y#y4)hT9&7XhbZf2;)&di3cl^ap)yFss>#434~oiLtKSq#CAI2<e?7wn5DYz<j1-|v1g5G1$jK#4_<qlFikI+V#Z%}~%bnC+`E`^<={|0-?BQSpQyy`)C~xhb*$+l&^mf`iRL<~ivtg`W<ql7cnB(bq+-*v2fU6)0hnXfju^x`~{r^trjCMGQuYl`Ly<RrOQ*OVox*xp+wC)8+XFuSu8Y_0<p97jS+0PJ4$%loLncNK+&28Rrw8GjUnJcZ_(Ky5OS#GT>YWwq*3?v^8mCnQ0h{jfEoOE<sfhf>w{lI?Kf%6cyfL($)gYYKG%BdvG%M$(9erUAY7%B!_^^mtI-0OIaZ88+TiCw`qB5~MZ&4lukAYVw%5Mbq~#u{ODZCXzGFHc!KJxQy0aV!*4?%_mK_d=ppn&{`e!)Ourj*hUsW!^Ba*SGZtrTnBePV=JHOvqx=n#o%ei8a=&fq||G0&H=lZE7m95GG#fLrWsf=lc4%3F01Liz5Bw8$tZ~s@0oP?jHwknn8Aeg?J&VT69=|nlL147RV^20=8If5e_@LELUH}r#KUeO?E+q'
    '==cBt2?mvkVoP3|00FO`0n_#b38}FPvBYQl0ssI200dcD'
)
assert len(CAPSULE) == 25545
assert hashlib.sha256(CAPSULE.encode()).hexdigest() == 'c088a374365b2edd9035938a0b0cc7887a0d17920100cf48a33b0949b231d091'
raw = lzma.decompress(base64.b85decode(CAPSULE))
assert len(raw) == 80723
assert hashlib.sha256(raw).hexdigest() == '6d4247c5d308b5cbc0a8de84beb5d54abef338336fcf51df5272ec7273ba314f'
sources = json.loads(raw)
assert len(sources) == 21
out = Path('finch-source')
out.mkdir(exist_ok=False)
for name, text in sources.items():
    assert Path(name).name == name
    (out/name).write_bytes(text.encode('utf-8'))
print('EXTRACTED', len(sources), 'COMPLETE SOURCE FILES')
```

Supplemental artifacts: full source, exact reports, cold receipts and exploratory logs (`FINCH_RESEARCH.zip`); standalone detailed JSON handoff (`FINCH_RESULT.json`). Neither artifact is needed to reconstruct the two main exact bodies from the literal capsule above.

**Final status: two cold-replayed exact own121/weak000 bodies at C618; one extra pair cancelled; no strict110 endpoint below630 and no global exclusion.**
