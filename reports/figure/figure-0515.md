# figure-0515

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# RN29 — finite two-apex geometry and own-mass repair

## Result and limitations

**No strict110 polyhedron was constructed.** The principal exact successor is `RN_TWO_RECON_G1000`: a uniformly filled, nonsymmetric V29/E81/F54 polyhedron with strict(S,U,H)=(2,1,1), additionalweak000, and coordinates on the 1/1000 grid. It is a finite redesign of the actual delivered two-apex body, not its diagnostic polar and not an assumed-centre model. Both added apex labels survive. The first is now the unique unstable vertex; the second is no longer unstable.

Our exact replay of the delivered two-apex body gave V49/E141/F94 and strict7/6/11. The redesign changes exposed vertices, maximal facets, carrier roles, roots and mass together. It releases **both retained P49 blocking carriers31/46** through loss of labelled vertices. It therefore does not operate under the old fixed-complement hypothesis. Its own new19-face basin nevertheless has a different exact five-carrier obstruction to one-point fixed-complement coverage. That is the precisely scoped negative result; it is not an E<=249 exclusion.

The useful tradeoff is fewer vertices and longer true edges, not closeness to cancellation. The remaining polar bar is deep: relative persistence0.9454988735952181, versus the original P49 bar0.6657206359138741. RN29 has r/R=0.09528432231049547, worse than the two-apex parent's0.23920824647575076; but minimum true-edge length/R=0.09927922625614473, versus0.036155188594102744 in that parent. Its29 exposed vertices permit up to56 further exposed vertices while retaining the sufficient bound E<=3V-6<=249. No claim is made that this cheaper, thinner body is an easier final cancellation problem.

## Source authority and continuity

The supplied common notebook, branch material and complete rendered literal parent were read before research; the six recovered source units were also read. Only the delivered P49/two-apex source was used as an exact starting body. The separate H49 body was not supplied and was not used.

There is an outer-serialization identity limitation: the required parent is `figure-0513`, advertised SHA256 `dc118830831a140cc2146e42047b9a6eaaa11261161c46440c61444f99fdfae9`. The accessible rendered literal from its RH08 heading through EOF measures31023 bytes and hashes to `f897379a87719e23e299530af6d56d6e07007a83ef37a1e7a356ed552ceb1c36`, not the advertisement. Adding its final newline does not resolve the mismatch. The whole journal is286195 bytes, SHA256 `10bc8fd551405f9a9850289005b2e55ab30e85758fc421238c9f30bc2313d642`. The inner six-unit recovery and all four advertised finish receipts matched exactly. I bind the geometry to those matching exact input/audit hashes rather than pretending that the advertised outer hash was verified.

An unfinished earlier executor's scratch arrays were absent from the resumed runtime. They are not exact predecessors of these objects. In particular, the lost numerical28-vertex nominee is not this new29-vertex checkpoint. The delivered parent was reconstructed again and the finite numerical construction below was rerun with a complete preserved source. No conclusion is drawn from the interrupted earlier joint-tree run.

## What was computed

`scout_new.py` rebuilds the current convex hull and differentiates the full tetrahedral uniform volume and first moments at every evaluation. Starting from the actual two-apex body's lexicographic49 vertices, it uses the exact parent's volume and centroid to set the initial floating coordinate frame. Its first stage performs2000 Adam steps, learning rate0.002, gradient-norm clip0.5, with complete physical squared-log-bar loss plus an acyclic Dijkstra escape-tree cosine penalty of margin0.005. Roots and witnesses are recomputed, not kept as a fixed old packet. Arc costs are max(margin-cosine,0)^2+1e-12. There are no random steps.

The second stage uses L-BFGS-B with physical quota1 and polar quota2: only the largest polar bar is exempted; all other positive bars and all selected nonroot cosine deficits are included. Both margins are0.001 and the local weight is5. It completed four accepted iterations and seven calls. Requested maximum2000, ftol1e-15, gtol1e-10, maxls40 and maxcor15 are all in the source. The literal grid freezes, not optimizer status or thresholded bar counts, define the exact bodies.

An additional five-parameter determinant-one affine stage uses fixed positive physical and two-root polar forests, cosine margin1e-5 and SLSQP. It completed four iterations. It slightly reduces the remaining bar, but its preservation is precision-sensitive: only the1e6 denominator freeze retains211. All three coarser failed freezes are preserved and fully audited, not rounded into success.

| Exact body | V/E/F | Strict S/U/H | Positive P/Q bars |
|---|---:|---:|---:|
| RN_P_REPAIR_G1000 |30/84/56|4/1/3|0/3|
| **RN_TWO_RECON_G1000** |**29/81/54**|**2/1/1**|**0/1**|
| RN_AFFINE_GUARD_G1000 |28/78/52|3/4/5|3/2|
| RN_AFFINE_GUARD_G10000 |29/81/54|3/3/4|2/2|
| RN_AFFINE_GUARD_G100000 |29/81/54|3/2/3|1/2|
| RN_AFFINE_GUARD_G1000000 |29/81/54|2/1/1|0/1|

Every row has additionalweak000, zero primitive equalities on both sides, and no boundary face foot. The fine affine body's remaining relative bar is0.9439493314463258 and r/R=0.09643649550200477; it needs denominator1e6 and84 centred-scale bits, versus44 for RN29. It is a supplementary nonwinner, not the preferred arithmetic checkpoint.

The optional unconstrained affine multistart used PCG64 seed260923,24 planned starts, sigma0.3 and the exact bounds/options in `affine_scout.py`. Only starts0 through19 completed before interruption; the partial log and saved numerical checkpoint are included. No24-run completion, exact successor, or exclusion is claimed for that experiment.

## Principal exact body, mass and incidences

The following complete29 integer triples, divided by1000, are the exposed vertex set of RN29. The canonical recovery input also retains20 strictly interior nominated points so source labels can be audited; discarding those interior points does not change the physical body.

```json
[[-659,-1041,-427],[-560,-633,436],[-435,-383,715],[-395,-386,-68],[-368,-384,-323],[-311,-135,860],[-209,-108,-632],[-168,96,919],[-30,314,906],[91,513,829],[119,626,-531],[131,-89,-732],[173,674,713],[184,803,-380],[218,924,-166],[218,925,301],[247,796,567],[313,874,406],[349,624,-492],[353,919,231],[359,187,-623],[363,649,590],[370,930,49],[428,383,-287],[435,867,-118],[437,776,-300],[463,381,-431],[524,681,249],[562,585,-314]]
```

Actual uniform mass data:

```
V = 760561253/1500000000
M = [525160275377/24000000000000,
     869586344297/8000000000000,
     -83992881403/6000000000000]
g = [525160275377/12168980048000,
     2608759032891/12168980048000,
     -83992881403/3042245012000]
```

Stable faces are16 and49; unstable vertex0; the saddle is true edge[18,20]. With lexicographic vertices and sorted primitive outward plane rows, all54 maximal facet cycles are:

```json
[[1,15,14],[1,2,15],[2,5,15],[5,7,15],[0,1,4],[7,8,15],[4,13,6],[3,13,4],[6,13,10],[0,4,6],[6,10,11],[8,9,15],[1,13,3],[9,12,15],[1,3,4],[0,6,11],[1,14,13],[12,16,15],[14,15,22],[15,16,17],[13,25,18],[20,28,26],[15,17,19],[10,13,18],[15,19,22],[18,25,28],[10,18,20],[17,27,19],[12,21,16],[14,22,24],[20,26,23],[14,24,25],[13,14,25],[24,27,28],[22,27,24],[23,26,27],[7,21,8],[16,21,17],[10,20,11],[9,21,12],[24,28,25],[26,28,27],[8,21,9],[19,27,22],[5,27,7],[17,21,27],[18,28,20],[0,11,20],[0,20,23],[1,23,2],[7,27,21],[2,27,5],[2,23,27],[0,23,1]]
```

The81 true edges are the unique consecutive pairs of these cycles; their two owners, primitive plane rows, saddle edge identifiers and all exact signs are generated in the full audit. A and B, the delivered two-apex source vertices12 and48, map to RN29 vertices0 and27. Their degrees are6 and11. The original P49 unique-U label4 maps to RN29 vertex6 and is not unstable.

Source vertices removed from the exposed hull are exactly `[0,2,3,5,7,8,9,10,11,13,17,18,20,22,31,39,40,41,43,46]`. Old retained P49 face31 had two-apex source labels[11,13,14], now[null,null,1]. Old retained face46 had labels[44,46,45], now[20,null,26]. Neither remains a maximal facet. This is an explicit bypass of the old five-carrier hypothesis through geometry/topology change, not centre translation.

## Complete principal positive-bar landscape

The physical positive-bar list is exactly empty. The polar list has exactly the following single bar; all coordinates use the actual centroid above, not a separately filled polar centroid:

```json
{"peak":16,"elder":49,"birth":"18651185891782216867880907008000000/420180620973137926795548295304049","death":"30835547022337376198161920000000/12746053791754746133098172054571","relative":"1517870971207036554607916687484098071597/1605365181912273065104553709015260194867","component":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,26,38],"cut":[[0,18],[1,49],[2,51],[3,44],[4,53],[5,36],[8,23],[9,15],[10,15],[11,42],[13,39],[16,32],[17,19],[17,28],[23,26],[26,46],[38,47]],"path":[16,12,7,6,8,10,38,26,46,21,30,35,52,49]}
```

The audit verifies the full17-edge cut, its complete19-vertex component, an attaining path, every cross-component chord bound and maximum-spanning-tree domination for all406 physical and1431 polar unordered vertex pairs. It also emits all edge weights and complete positive escape forests. Thus the empty physical list and the single polar bar are full landscapes, not selected-score reports.

For RN_P_REPAIR_G1000 the complete polar list has three bars:20→16 and44→50 have singleton components and relative persistences2.1192640998116646e-5 and1.634923349585317e-6;16→50 has component19/cut17 and relative0.94531908908718. Those two small bars are exact positive bars, not zeros. The capsule reconstructs their full rational records and likewise every bar, cut, path and edge weight for all six exact rows, including all coarse-grid nonwinners.

## New exact one-point obstruction after the redesign

Let n_i,h_i be RN29's integer plane rows, so n_i·x<=h_i/1000, and let q_i=n_i/(h_i/1000-n_i·g). The following **new** packet rows1,17,26 interlock with **new** complementary rows15,18:

```
1  [-468432,233937,250,114348799]
17 [-6809,11959,6542,11546855]
26 [3461,6104,-20098,14905001]
15 [-17881,-4940,-61734,43286537]
18 [-2587,70984,-152,65050482]
W = 358456992196886861636212255132061260869
left numerators = [921190375773185774928244820709368421,
160690100821975166463719648736009119252,
196845700999138509397564361575342773196]
right numerators = [137156285257220169269110645178643788580,
221300706939666692367101609953417472289]
```

Each side sums toW and every numerator is strictly positive. Dividing byW gives two convex combinations of these q rows with the same point:

```
[-7550673336232459341482966919973776000/39828554688542984626245806125784584541,
 33215898718571278108925095853600896000/39828554688542984626245806125784584541,
 -65237611825093491259124624195440640000/119485664065628953878737418377353753623]
```

Consequently no added point can strictly see all19 current packet facets while seeing none of the35 complementary facets: its scalar product with this common convex-combination point would have to be both greater than1 and at most1. This is an exact rational identity, checked after the two floating LP nominations. It does not cover releasing any of these carriers or changing their side roles; it does not prove two points suffice; and it does not exclude any finite mass repair or E<=249 construction.

## Verification and useful continuation

`exact.py` exhaustively enumerates supporting triples, merges maximal coplanar facets, certifies the true two-owner edge graph, global support inequalities and Euler connectivity, and integrates the actual volume/moments with its origin-shift and divergence crosschecks. `verify_new.py` adds a separate support-foot mechanics calculation on those certified incidences: all-point vertex supporting tests; face-foot polygon inequalities; and edge-foot support against every vertex, with equality-set tests instead of the parent's two-normal cone coefficients. It also reintegrates mass with the rational vertex-average tetrahedral apex. Both implementations agree on every strict and weak set for all six bodies. This is independent mechanics and an additional mass implementation on shared certified incidences, not a second independent hull engine. Distinct exact vertex distance signatures certify trivial Euclidean symmetry for every new body.

The most useful continuation is RN29 with its source labels, full19-face basin and new blocking carriers15/18. A coordinated release of those carriers together with the adjacent retained material is a genuinely different problem from the original P49 five-carrier cell. Both apices remain available as geometry/mass handles and56 additional exposed vertices fit the sufficient edge budget. The deep remaining basin, poor r/R and coarse-grid failures warn against treating this merely as a smaller scalar or reusing a one-point nomination without an own-mass audit. No constant-class continuous path or sequence of Morse cancellations along the numerical deformation has been certified; the endpoints and the scoped obstruction are exact.

## Self-contained recovery capsule

Save the complete source below as `RECOVER_RN29.py`, then run:

```sh
python -B -S RECOVER_RN29.py rn29
cd rn29
C92_GMP=0 python -B -S verify_new.py
```

The exact replay uses only the CPython standard library. Optional numerical replay uses Python3.13.5, NumPy2.3.5, SciPy1.17.0 and Torch2.10.0+cpu, float64 with one Torch/BLAS/OMP/MKL thread. Complete source units, nondefault inputs/options, literal grids, affine hexadecimal pins, exact expected receipts and the recorded finite logs are all inside the capsule. Numerical replay commands are in `README_RN.txt`; it checks regenerated base grid nominations rather than silently promoting changed floating output.

Expected markers are `RN29_INLINE_RECOVERY_PASS 17 56469`, six `RN_EXACT_DESCENDANT_PASS` lines with the table's classes, `RN_NEW_FIVE_CARRIER_OBSTRUCTION_PASS`, and `RN_COMPLETE_EXACT_HANDOFF_PASS`. A clean-directory decode and full replay were executed successfully after packaging.

Capsule decoded56469B SHA256 `f627fb2d5eae97ebd7bbfaf33c4a077458a916cdd2255567082222c39bded3b3`; compressed17484B SHA256 `bc866660d5fb4c2138c0d7a79ce3184188087967c441f1e08e6cad68faeb93de`; base85 length21855. The recovery source is22871B SHA256 `cc428ed4b90f5334cb185766b6ebda94cf01eed92e5c9fdada62dda959231528`.

Principal receipts:

```
RN_P_REPAIR_G1000.json: 2336B 20ff297822f6674ccdfbb1b22c44249ad739d009bfa7545a0b5e2945db6cfc5c
RN_P_REPAIR_G1000_audit.json: 49407B 05d237f407c1661cda9d03449a4a5723308443e4d8dfebcfce481b1be39d34d7
RN_TWO_RECON_G1000.json: 2337B 24f020913c72cc151d7d581bf4b9d0503f6c29f2173aa80e9d7b0efd7e503244
RN_TWO_RECON_G1000_audit.json: 46900B 01963c7d92b97243985e838c30ecc40f353c3141ea8d120888a0df3807efbdc2
RN_AFFINE_GUARD_G1000000.json: 1678B 6a6529c15094253b307f0393084eeb334709ef05208b4b1083d8fd4de89161b9
RN_AFFINE_GUARD_G1000000_audit.json: 65524B 63ebe61ce87d4a88e0140940f6f1eceb30f172f0622eb6dd4c0cc49b7a9ec840
RN_CERTIFICATE.json: 46019B bb3537555d49f36062cbee5e51b8b824de6ab245d8bddef7f075f804bed41425
```

`EXPECTED_NEW.json` carries the remaining complete receipts, including every coarse-grid input and audit and both source-body audits. Convenience bundle (`RN29_handoff.zip`); the inline capsule below does not depend on it.

```python
"""Complete RN29 recovery, CPython standard library only."""
import base64,hashlib,json,lzma,sys
from pathlib import Path
DATA=r"""
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;M|l%3|#;{h=iqrocag;lgCWijh<R#Rf>q2`ayH1upeQWEfkGg!Ye0f-
m0(uUx*eDgpR2+;7_<(J92}^sUlYu!OehOdezXJm|V3y#tKYO13di@(Y5lLFsH+R_tW3dwAO|Jg|y-
ABc|1H)*Jw9*Zu33=m51|g9Duqj&WBHOECldPrQzY>BKV|H{SJ(5Nt`%S)~Ft=k~abYq5!4LXr_~_bCS#4_FJA2<g+iN9tKD6nz*
`*H5)X7vV&p^n6wV1c*a)0rj_^zb~DK$hG!;2?v>;#a}`R%)ZYf8l>4dmHv5Ab7E{h>9V^wL`ph{%fRljB7azCqmv8BE6=-
n1Y`DfR~>1L;*yk7F^pJq+@XkmXL&eV(2fPt<8?N&Djq65(~@f167rEyD`-
n^u{XJoYr~NyEZzy281i}?xcykM<#VYKBo6ry?+r=V-<)f>NF>gBPU+TglLtMN)Sr-OgK5DyG!x)iX-GHvZgu@#mS;Gu{7d%>tlq
&s-
JK?e%SPnSYpUHnZ@gMcd=r2EOKo>rQ+fWA!ZUcCPjvnB4_Oak%QEl3(CxHoH9J#o+IdIgD+>f`(z46WdSdO#Dq9$Q=H2u_gaS>_2
GN~U?bj(faGuHOnE3gk1HmQ=34E=*gRx>6$k9(m!c_^>^7;pqWT%CR2Rw83<pkzG?X;A`Z@eWl^5!hdhw&Sy^*f4r>9^6;G&L~9(
?_I^-QshaxVB>(S|REg0&PBxawEtsA5rm-yS1+&X49)mB91xI2c3gA$o;|i>X)jvS_1w=3U7eq*~jDbB~L@5w67nnihv)Vp(`gPF
Nx!+{XhzLjNB>Mvo5Z$Q3&fm0%sPR&T{^s>fu*DYIyvhe{V7uD=w4Mh6xeY(MT8~AQ!lF-Kf3i<qznM_+QM!R@ZNn&+vt!8O0R3h
?Pf;S@XT>uWk}K=_-PUE25q-QMJseylmPNHEs})<NzBs1iW)koWYI<)=J}re&{KI*Z$7l=h#zAEJ6{*-
s)KpU|GDEkN9S9)+1H(MNZSDqpaT{$)yy<!jUu~&f=`#3*#tY<z(z|fjwT}!hS=O)I4Z6h=7TsH43+xt4%@ay92OS!1ZM_JU=2*>
j@R}|I!1khRU`Hv^$vtn(QTSD3B_Tm|nb1e)%~M2yK+6I10FfucSTT!O^98S-hf-Rh>v{tshe`w3_|UrbUKuxu7-
)!LO273Jwn1^*ke!l20?yd`fM*yW(+Y17NYZih;v#Zxm}S!nv!)ojwgKO&hQAV^K>uIx<KoPJUt(f=E;^2`TqzjUtsh5ZwCa0{yd
h<s@l=b-
#hyhKJs3CD{tQ9eXLV((6m5AC!w^x9P$Ygu(C1IEXJ;Fe2DL6qW!NlrejT=_hTfwr{iOX77+CrLe|uYcDzgUdoEx_D0Vs`|EAYop
vDI<YhStHNPbtr}Hk-UA+ijH&qhO1AAL3!wYm}O`|U9{5Su^()`M~gNT!0UH<NMfSG()_{#p7ayN{oGR{^uE>{wXZ8kkj%byHXSB
{e9iU@}A8r-T#nK5*ijRWisWTfZ3TK393c=-|whjvnKwngwaOjLXQ-v$Y<l5+4%bVwvu=vY_b_k#Cw9y^(UU42{<-
HD!$gGMNex9o-
fz1S})dt1}X(F=334OmR>UV8SwCbt$cIA=mHkF5cFdN_%>*sN}Yh~`r9j@V?KMx!9Epj37aXFBVEm;vSCcC0D)zZlgL#X_a6*;gB
h;rL3Ky3bG30A5uHzdqv9Ac`{f`-
*9>3oO@y`dg@kB*t3aW?A}FCEXpNtB7$T)(MGR%A>VHeVa?yCP|;>MmcgKshLigFpa07)^W?$f84>Czmp}Yz6OwpVA`{p{(H-
}rkh$ZO$9QPSn`s%iORCUSXX*jo{_9}aT0xGI2{RV2anH2vAARBkbnzwOHA3XB8c5FiZ+DICu2seajf7-
rTN?I;uk&~jiu68HZ7}&$9)BN^xu<#B_$<E=cZ`mB$_Dz4jMNdmU8?&Ep0M#tEu>VMf)fbUGC8Zv`Z?+<Kqcb41Jo~2`MeB8kHHa
HT!QSV^!+NW;TS4j{-Q0UP5rw!nv?;eRLV66FFz1kFR}pxWTy5!l-
w+q@Vfe8>DSfS!RwWo^UmyXT$xA{_1y=qnuxhk+o7`EH<L8bC6bB0QzE-Of66|;V6QzCdZ;<aDlwIaHTb<Nvz|kP9%A<lv@F5xrH
)dC)%H?Fj%$<4C*PW3$CO#Z#EZu2)b9uKT<JA4j@E>K7w=PKJQ$-
Fi}J&S#un>pK_pjxE+E%jde>`KXMWqeKbf@MLlgr&pG0!;8_^s<z$T3wCV8kQc;Cva;9QhK_RI`gq0Q@QA751Zl*>jD)<7Ms9>y#
o%cqPppT*R4a}Zxs`Nfa_$#>wK>f~+6l4U@v@oG*a*DY14|-
cC^o=LdKY|O2hMdkcAPW6x%|l`|TL0h1syGA7E`yzCdWd9M7gU}Hf73v|F25eCuo{>{Ty~neW+A+5o!J5~lAkuc)3#5-
st*H&xstNURXIX+D5_Vpgkl1vkTN*rTONSs<B10rB(5g*kj?AjR|nSl7z8ZGV=cFvB9B;Hcb`kN>s-
hh1O42{nP>~nyvX6@mT0pKA>~hY;uT#>k`zXGH}zt+)AV(!Gy-3j7GmDVO}Q4$<YQ=ysyDr7Lhy`3wrQ|n%FUL39P2o-
i?)<@9dUsBlN@Yl4R=G`Kx>P9+hu}D{PXW(N?Q<ww(><AXYuXOR-XP`@>EZEG$|R68|}CLa#LRsXZE&BadK%mweUbif#iRLTdFEi
(|xtsers52tVdPWzP!xPkX7ST_9XbzZ9EMi;{_#hC^TL<6~-1_tKLp!)4!+e?r;@i&~|11nYyc}UZK-N_yOw&2D8dNf;9<Oyy>~F
$JfGsRg=Akq{^Js<x(u*mgsPVoD%=&;bG_y(43i1aCSs}sNd%6!a*n$GDOs|HrHE(h@wk`d?%Dc<Zy&?AOS9%*VtnB^8LO&Ls&d%
aLI=e_@S(43-qLF(i93B9}MVM7)q%uvQb%%d!CBTv}mwyX7j4Sv3#3R(D6`gD3$-an%8M-hj-?v6v)yo2nVNb$XAycJ*38-
)Y!I>iV9G@L24Px{H<kVDCrRr^`0?OlMVX_!!m4?s}K0z6-
Ao>G$E!jJ@;hqh$t4$dthH=P~M8aUQD@)LwzKgy~IyQv4HFjGe^x6u~r(V;xIA)57ys|bMmw2<J=)9=x?!)WR_1s=i>EI!Odd^({
<7}0<bHtP$ZpH>yVH3lHPjI#|L-
`Kq6#peo%>R*|kWoi2z98$~38p=&O~{D}aY3H<80zWPLjIj{sylYXOW~fB9_eFb$7+J99PpV_W#NPg<O`8}pG9Ao%&qb~Wb~Q_(b
*8FEV=wIoA`1BAr~;@~zE{s{!peRCr%l5BjV`R~U=FSaCE`(wX^bU6w-sl&<MTM-
X<9ws9xj1_DO&2`ZUt)baiI|(lMH%C?IVy9<G_C^!AzE6%4PdRArcD4JIec^tHgfD(s+OeV+Gee-
`No<`lKFzMi#95zVe1fqL@7V8ss8_jciNP2Vo038PfzaaxAZMSoU93)Cfdx1;(b<;ZFCpIr)50A0p;3@BT_J@Zhvpc+Fi80H%y{6
5;p;3IdSs}Q>II+%K<YBR$nMwNBG)T%8`9x!%8Jwjy2`RZoyGItXH4*PWs=ILBrnE&)}D|!`&@S?S&lIX%9%Xvn1&$6cZoz~v`94
*in_w?ZwBf~-OABoPIjmkSW9sB=S1!^Hrci`teZ@3hI`B$do~m4N#qnT#!BOPQy_)kBC=p>7)S5vTn(fZlH-iST&;1P(spn6AVqZ
9h)l=N2kQn>ufkUCrqk#U4<oP<$J=xTmd_o0!ycd?$qcp#DlMcspuN$ZVVH%=dU?EU5}X02C8MSVG19)qZNPP#7Fl8ax&LtSU218
pW~|E2(pl%VZQhJ+xm~fR2i_d0-plagp_`1|==$8q-w3rs3iTw!c=R-`c%yqc--
$byPte#4FrJBVOA9~yWSiv=o6kHj&#^n1UElNWF?V{RARktK6AzySn5bh!+pF&CszvN>CPI{m7_sLUrZAC)stNxX<8j8EcL1J1Z%
1ucEYU)3iiQO#e^Nm2_@IBX-9gG3*RRkqF|JscL&s}ICMJKcSw%8b@g9?-!Xz-LQp*+#FI#7L?jjAY%3$pNwu^Xk5_A%X>_{n5xx
bokMHI2hv<+Q`q374CiYo#k2Jw{FyJsbGA6CjI-E^1IAFIygdAX^K=?5L+=}cgKm+tZpe$0i|=0gO`9y=_v3@(4y|4Fm=-
35DhTmWX5{$w9lOiO_AiqgV?;rIT-BPZD-
%FKdbGXmf#o7!o&gR?X{J4t!srv#oNgAq{K>a`E{QaTA#KXxS!^v%zZcrRQHJs#>UU>W8NuL2X6r(gYA;DLn9iEjmPRXTVDxJ|{Y
h$xsAv6Ji7yN&2Oby09H?vvLK1$d;RCnIEt{qDu9%}j;k&CV4Ys-I3_bLt$5#`ozZ_Wf?G{c7EK*li!lfTg1O-
MqWv>g5+2nQ8;}?A6R5o=m5wy7=|5)m5%Tw)_a{O-{MpA+|Z{iTB=q#0!@x2^;am>;09`%a0GF>x+COe-
4m_A3&9vUqQS6s0R62&ZGDu^33EXTgq5n)EeE#dtL`k-N`G5@Bd3bZ-O;vPa<V-
biXPyq1aG1JiqTjnm2mj`0!T`hG}li_dP_^s38Cy>$=ZM(VN_DM7}aath5&;493Gvzm=TPNB>+rBvJUfT{%rFKIeK$i(XmnQA0Tf
$ky}LF%0|3cwaH#L2i;v;vRbd>{b3!belBr`-0>IlyOU4X_OdhED+)`32BRFV~YOTeOD{O%I_4L-
H#CZrm&W;nge0CVp0*<U9hp9&IUbsjvolUc!ebY>3N+iYmBICHH`4i3PO&HZGH5y#T=6&`x!>09Y-
*wn7wBPMakSkTEWx18&ItBFPgNIgX}V?6r}a{q!mIickNj{>=lmpD$jauuPoiff!%vQRrZY8*7&HIbQqa_t&5boFz|UDDCOv+J+Q
nLIVM6V-
?NJ85(iav`Yb<u?@>sTpgn*;3B3bOpD<NFV16AbK{CC$nPwH$Fi(7+<5n>&P;xn$fBq^*t=aG>6=u+VlxcNU%3q=Oh{W-
rFB#$3A>vD=nQMt~(JU8+_H=1dnFw$=q+){?CImrsqtfpGbe8z1pQTQ`a#M<5vq73Av7kB^_%339g&sWF@y@~QW*-
MQYTz#8{8GP-Qh6|hSC6_WCEXHV)vHdUkiTDq-
@tr!*IJ>snKcTv&avy$@KEHqChi?Mo&kLF#lC(ba4`_Q#j@AM`IO=6oDM%os_!^J$e@76tnrg2N_YU?{4rIv#M3HssW!<2y&vISc
wBnXW?~0ZMpEJnwrJ51Kms1r)2^WC#kHQ<<bm6o6>UI?wh%{UE9h!iNGF>@)zfHgM-Km>a5u|M3}5-
}AwN3_qF&D@wk)7WW3}m#37{AZ@ozs3w4{YZO^?c?k4mwK|K_!8hPhG)7~DFK8M4<Ki3Yru8jp)u+!^4vA}N<ug6m(=jQG3`dw-
2P$x7sromG3`@(as?H$tQepW9Na?ry53oJ)@Y%skEKdGU!&SF{ntp|{tlQE&6Fw1yma*}*wViKq-@YgOmL2YJYVNh;%sFYbP~)-
5B1ePfP}$7NK&-
dv3_Q13NK;h1JCEEt{hYzr`MDzf7GKJ2i7N8sf%ZPSy=ShYn~6ATEr>%EsXg|mSNa5_(>>ja=@dxJ$5hKJa$eA$vf^8eF%O1}|nA
EM{Y8HKyBW-F^)e+n$o{vfkA<~hUXL;=uGB7G-L-`3-(r|qEHMGDye=qVMpNVV!^t<SA(?nb65PY<^zPW~bNBUfvQJ*vivn-
P2PeLs_<;Ak2l%tG;(k=4Z9^}?-
FS1NV^*Tm}R_%=J)QWm>Z|3HeXu_+$t272OD9_Dk{OJjE=caP*bIM9>I<(RSq{qOA(TEHF)nDnIvnI=C0LPWQmYbj<;morOUeILT
iFwyXm_^Jdz6I%tdbI;F@p^mx{p&&PoNt3O25m8<@3s~Lg9gUE^K9G&FlqihmEv#K}9iD(>qsFuZ6W!HdfLuNXQrerM1sINeSFhn
plt|i!U>2@<FA~e)I?cyrb?}PCdNuoyL$3E$6M_P;$w=VB%As_2%@sd4^&jFWKesWMFsagUJ4K1y$f^wj+^5AeH|m+_JUfw|8rXl
$!m!W3e!_;kjbRHDbrd2&Kybvr%X`Ard#oH=;ghT?BT`jfH}tAU#JQ9>+nbccast?oGL)in6h`D2hIg=shar~?xKm5Co-
M80=sZchuF2VM^-
wx!$$LP2r;yj$2~ZsYp|Db!<ZVIHjyMmVJu5Z)u?7rHWfg+EUXZy0N${3Fi&9IZf~~Sdek4x4rSyIo2T5ZN?#B$9zve*709+uu=H
bq%e?_rw&nBs&#p(AyzmI<d<UW-i%Cj*S=wB{3r($Y^y9G<bo_6|ydMLwnLZnIbS8y7-U|C>V(d`ON4ObI(-
z8p@jscJRY03?chK?=Z@Yl0$?-
uXW4|St9W~NWMt%SofC%IorP}}9>GG*XmXmbAnf)IjGLjaifEN_Uh3fKw_zWm2Yyr_YNqOAEl+;W}L1&04>hA1LU<ZwpU0`dY%rD
4ml{kGOKlpkLOhE#0eX9Ng*nLosMn4W~wwM}C|#_rKD??s6I@?p!<kew{x{766qCqJ<-LTW~pskc!GLJEQ+BHn4b<iOCkV4e9&-
Pz|y!sOPs&aQSreV)3VJqL){@^O{EVMt!S0xp!OP4?K4$Q>%yxX8KCgzcihilSkrgzKD1RC7ZUlV7pOD#iJ@yN{nXdh|t6&o`v1l
~4u+qWS2I;W@$VsszpIA^iHI2_SH0H}S8Ql8fxU4)Ssln@f}{k+kL}KoajmOs(43rs33<=Dk?P)<Z%UwWeew`J}l3u)yLFXsy#@3
Ig>BC$p8TDnXAYHkBjVe)T1EKr|F<N2u!@aY55I_bM47Y`f5r$uyu_rav@+U<V<58^k6IR$yKCt%TP%EZUZ6_4rK|!h%wFbo+w2)
-7V;edzQm<=>Ao{b^zKPcrUGg|e9_zZ5J~5GW6>fEEqplRNH`ELd|*X?gUs<~b)|@JI^wQu(x7;a&<#5|NJlk}uwTvI?APvU1`h-
~=y?M1#xtQmnz7rMeo);z^Gk>{?>)=`k;O8}8*)16~a9J^vt=Fq<tVM>>l$1!@;^&?-
NJMOuqswq;Vb55oGU%1BtGk*$guuHjVye<|ji4}qQkBgJwOlVLQX;hHvf6wVU3JEaq9JJVM8GG-
T2uHw>cCdm$0kZdvI@IZT>NU@uGW|9($`02Z-
&%K|}eewQxgEYTo_cmIy4E_`bJ<p>2669P<PH)GPVFgsatS?3iwyq2)6*iL~oso`T4Amt|DSQy>SD#(BsB7HHkE^Xiby~OvoBaEQ
w(1s)ZT-Q)ZB^auFNnTcFiN{E({ru|s(3lP46S|V2bBL+WH*>Z*Qrtd$i8BT48GRj_%)b)?_OlT?DHaG$jlnc@4jlje-
G2aRP+cm>qCd;^w9NsBL}tfIl9XBr}J1sqi*tIyB)WY>Z5yw*{G}_qsrp8JH1HDq8_@<#YtXKsPX#O#2J?M5}};VSo6U*s5+P@-
du$A2|(?}Al%KFbhv}bT~#J4cG!K7NrwLL$*WzBGERq$`QL=ASI#E}yG&J?HLJ{UXtZUQH}h-
BQ3brM(O(ebZ3DYK$+^7w946FKQi6k|B(wbtzSrl1EzE0!pE=wIyJ><j(@c-
or(x;(FDCL6u&>Y4hRvwAnKmc#Z)ANJ%9oN>3vX|s7$<;4_RR3a4vGynxUYPKM;r3=UX}df1sc6mEWbjN?~Ei}n%kD|(Fk=3SJcr
=_h1I5sLHDmid~5?$)%rP@kXwVoj~NFXzzTB?a)(hj&eNHU|uGXoC0aUj?=&BV(2~mlu}-
U&5uT?w9>235jD0}sn4;bL{5w1E3Mv0@<}9xYbrKvbt_YT6C17Ku-
l=}h3~BLJu5L2zAMAW=0Et7zpOrb#U=9{$60f720}F!S5q!eO6Eg*K{18lh>Jlg@U=_efJbRIVFhwAJW!VhOT%p+K$7dcn(J3t&E
}wAE1XJ}9i!fnItK#?4eSC=fUbT%s2VY=8c_=Ne&x?}-zG9QTQxy|R8Fj%_FYMvQI%<!S80wjcjk;D3ygG3j2zB-
58(%xFA7Xh8;JtsSt>Yz182-
rcyB@z#zc=BzZf)jDpBauUSL&Vm4oVZMv+{l3<i%8|42qRL?A}SA{eFvkl`G6wwQ08#ZWfmtT@G&nS}#zWuwjz6|aV9eOq$YpwrK
Wb%~G*ibz>1>$*J^q2%<&<_QAO_$5U|s3W)`b>N=|i7ND;sNl$i!9xR${%-
D(7QZpRA_SWRClv?Nq{R2Vw3TSxjgj>(AZPKaD~nzZ5g-
|d%n1^1zJK79fF&5~MH#~rL7CBBSsT+4fMgRsBj772@CG(Q0fP<JS#yej@|EQPw8rAlyssrE!$#L*o(@rub=iuX=q3Bux^`!GOv*
U{Rj+V1_g!h9slV}KP@q3)io@+)McJ}*OV&Qwh)*QfjDQ`a!V}z!dKhikR~-
=?^S4o@5}Dz^cqc+?cJ!Oh#5xAkg+~L9KeqLwYhJGfckBhDtHQR<Q3IRKX-
SUHWntg%i1kc3FRu?>@dRommJH@`>Wr^sJR?O|Uos4;yx0HQ2~PuCxnSYNrGegB#VB7*8%$sh-wv&5Ru~tq2_6YeXLluAUFp9?EV
gK_M{k}f{7Pw@Q8c1bJP!@V`Vhi33LMR&Loo+DN=20(w<CFDM=Up&>GO(}wAC3|(l&Sj=*DX!ffn@?fdT*w%nk~e-
W*KdTJ5tw_J4m#l9V#-x^~y^opj9>9*awV!Lox6qPzv}C=M1jY?uMF&8am<0}&2@ElY-
0S8Mif>;w^Hmzr*baOltFR$v?9yBYprZ{YjM<T@rhDW~h4OF<HMBR?=Ig?goluv3cyyL2S|k1*I^6dKk-
5Pkc&M>EZzE<q!L8nI;{M=TEuaFq*M1_WQu_sEUP9k0o&D?yW%lR_Z{`&EdwlFZ}Z&rbaGq8oquF&+o)1J)6}Xl+|^ra_{lf9<%N
J;qA|@%69aLVSsW1~>%TOkdrRGg(2kcd?1a$;zojiN9rLaqdygGeM8&nFssv6Z&lcUa+~hZvyUPyw@E^<OIc)OtUULR>I<ikZL;C
)#T7mfKXfhMLB&p#V_en9m2cd<c4~6cdJ#6#|{Em5Z$i!o8KUQABVcvkGL(T$!A<k<nQ>{?2MXZ2~CaLO1o@a>XCyx4(vTS79rim
z)v2%>={IoZ}+l^9UPPkN}=Bs#u=Rqp2#fT?{49#8Jz=1;^}5Lp@L;)ia2tV9XL^vftT_8YPk>Q-
`r$9VYmgEl+?AVQ$ZDP57vItB@MW1Le9M@!6Lbw>p!7n-
GBFqF?}yZ`5TqH5~r3K+GlOp&#1K@vouV#rd)Vq>(nqo>^zNjG75Jmy@-
29C(z=|&jW4Pq8=(~_5mN?f+jbUa^vRk{wXWlb5g=ZYC`0n83}R7bJf?$K|V_EA>wb7+9hulm~w0sQqfwZ@2GZSaCG@aF4=+b%y#
+Rv3(A%^};}xu{?B=JVITItjU#S*+`oRHzUdVcQ)!&Vhm70o7+!0su$_PVW}nu%Pazv(l4tsc;F1d^?pheE~ZKoqt~8=dG=)C@(w
EEKo~6|bv7yQzVCEV3Msp$9=fw`EQon<yg;en?WJ#zXXxFq<Dk$+K(J5CmGwSz!MK|SmieP+4Klw7j8jpT<#W5o!kb^@vYlQR-bv
0ffDL&s7L{qM(H*jU8sC8=5q)WnSONs<`9`j>P$+$<BboVO^^v_4+HDo%7bI%Xp;x?fJ)I6&>L!Xe>mB`Ab=OEh`CJqra6M{*fqM
A%>>Y){WFCiUWu|8i`O>lL{y@kHZgB_vFJzTx!WaG$WC?vftBl2tG5lxUaL-
&93fVZiW(#ArDZ)!h#EmWQzwN=+ItYTnYSxdAT(ZN_(1Wdn4mOaz(93BsHv%g6!Vr5+S1D;y5N9JA+1;bx@P8`fNi~=vk)dnW$*h
`r_w&YHt#A(^lEsS8Z?BK)L5&Ah{_R_4b8p!TY5Qm_+iH(en_;-j&>A1Yf+;u+68MC>Jtnj>KXcV-
?|@E9kEXpaW=<D&LuOMe@*wTbwlgQR9cAcOeiHl2--xEo2LQ$lI8ASD>L(i0IPb_&*_zU~QH*}C0cTbyWUK3I2%h|wL~D~urZ4so
J+A^&Jrfb-^e6!kpuHbVr$)QZSP!*G)LjTptVY4IP$LZe+9B-
NsVx0@HWF=HvA$2Tt4nytJs!*T@R)iUpS3@DqTE8F3=2i$?fy(Am<%&>1z9gtqSQk6m)U$Xp_ySw&<|=<3(gJMIgZXOKhPD0`!w_
Ez(`!D1OKzHN^2RB-CCSgOwsEmv)75Z$K{2JPNVs9rtcU#>@g0HZkOLYzT0oR4>!z2$Y=$N^22F?uN%J<8!Xf~A7`niu=5QmW43Y
j4-o^`BT(nLwfjrt%fvuhQ9pHBbp9G3tA=`dZe30xK1dVY;|haBD*V~5WX91SFu^Gx>iV>GIQ4EoXb#6hwdl-xy(oc}dvQnxuayA
DpY;(Hu=R)?;yspcm3Y`8OqX34vnK?E&J^MeSb5h$*gzI9fXm<s5+<6FK`00xT~NT`DK<XCDtff+A36xRaYVw9+rzv0{|UNPPX8M
4GJBA#O^<BZ`B~}HA=Ff5N-uYQ;B_3eqRqaLQ#WwQ&k+=-
;XR}sA^<z@D0bRFfC0{K7jmq%B%IUNGIW&W^EJ=0H=dML=mg<tSW8}gTA9gs<(Y3wq4`R8t4}HU%(5@|mmtM1eQ6qL^3S{$kX^B1
xxARLDFIp8&Y$dHv)?NT;7Xn9wPY$}?Z#t#WN)$b9sqoeA;Jm46kHalJ+1H4r8}pI|E~4QNScUsb^NR#Lqy9$xpx@imYrQ=7uUPR
i0TzVyZXsUAC`N-
YOvNTZHF$Zb@!VNgbfRdtEeDDFNG=SOpjg&Nz**4e{XWAx_+fUlPzUW7#ZkvlF`RCCQY~xb3x6BM*~<9b)eJa5kpyXMr<@!*F{&G
{&UqN=Iz5_wV9nKL1Ar0={q>WMw~CBPH{2&q`d8`i|ch6*Hvi??qk+%xs3e@MRwqd>r;Pb*fhl$IB%z<3(MB2tK*~wUnW_-
2o8_0LV;3BTPkOBhf>GmYULlVdC-Vp#yx7Ve&iBW>8W^>gsV(Gww7ti*`B>kZSc7(wc;})l@fqW)#AY1uW0}w+ZCOiPa5ZFuLLiD
eL`43W?d8zO61;_f&R`AVu!MoXu~{0hmuETi>pir42QM6mQa@uOI)I|3Rl~mw1m9YYMD;-
otjfta=`kVpckodVar%;(1CZ*BJ4+G2$()uEkW3~_u@#&ydTd|)2_Sr+_Ll@I6r&9U=3paLtjFrZ4u7T$WOvbG>)~Pmu<Qu<jtwg
SIl3L2CrM{c+(_z{Dn%B52F&yw*#agF+zgF5HFcE7P7g2EC>(^S_sp!)7W*k`P+W#KJyeW<{L`N(di6=C6-
b>U8cckUhS%o;xKxKmT_jKE|_02OqMG{kPBHc4#E<%m-
PDa#V1_(wPO;awR)$z+^HGJXj6`T96VK;@w|fTmPDox9@kho_p9N*t<noOLYZZgcnsa>OvY@LLluR5%4M_^Kb%3R<@MAQK0esM2m
!RXoB7Fn3Z<uf;|C>gwnsw<LP+L}uV_Pb$>#(hG*8qTe0O__Z*N0r*EKbBln|sq>93+5LT2@2$b1ZE(g5vfjl$bxp{Ot!G~HfL`z
~xC!ul~HY<ftJ=7lF@&Jg~m+6gQmG-
W2A#^2_qWn(=MRZh2L+1TJWG;TOm`b{2JiA$p)K|ldsFEHl8bWSx<JIwNzWUTYJg)&8a&dLX;wP@pDb*>%pH`Ltv^bXUj=Q?|FPO
nt5Q*y<})0?0H!i127&#R(>8s8&TvGX6)v#?KOg8wob>z9mfnf|D9AAqs}D%dDdq)=t3($H04Em~&=^2a7)Do+rim5D`?XKBUT{R
Xa0C&-K%-
Urb&A<6PYIQ$7Jo;QtRI3BOHO{cexozf0B3SJB|1|tC+(Ulx0DeQ#_`n@t$gr4W;CDtiQ#CO+nKyjgAExLAi3LfRMQuZ^;+62@|N
I@omep7G`t|A?G)CvFZ$gWP!rZm(33NPmRn>ikF1FQwHyN?Ox!4O@eKD}sOHC;MUv($_3I|j*VdMRK=q835(RU;!q3PSjq*881Vv
IFBfkUh7?<8pBBBaSI7rICySQpdWMU0uDD%>^A#AsG1LqcB~+ha{!9^DLa2c&>~z$Z-
ABxtQl4@Pk$%vS4rBl3@M6=J&&t<M)GTjRf1%1lB77D2f}wp}o{idve5L7~U+w!q!m#@b-
dR9$gH=Jm6f5QO~|ZPP_5JyrF{?3>TQxTs?(XuZKH)Ux5^aU(iz1^Co3hxw%t8>^An9PFk{MTU`^|HI%RV{X8AJz*rH7XGw<jZj@
W<jFDn>zObdjdZsG#V>u3&tk%6Fr4~i^YVcB=yv$X*%+f0DScYHt%{cb3(SY&(IuATLQSv;G;!(sf_RfD7FG8g`#b()4oR>Xkx~j
)%Dkh2jlu(MUnSC7wBY&QfV^Tl7KVNBZ2g7Xm9Wd4s&A0ug(ly{@isEfr3gr;rUIQsbMjy?SPZ%tAE<a^BJ#f*4h&=~x4IkE6I>a
^#F!}|SZk?P7w}zMIbVHWIbKS_kYWx-;Ab_kU<Oy2>3|NvWh&F^&pVU-AG~O~v+)fym=c;N+q^O%I5a~HI<+^=pnC7{Z@CWrSo(v
m4&g+z(4qH{2IBuJz#(j?KA_&y=dBLPrBXCIBo$1PTSUhV<G=6q{4Z&i!*EmLJeW$sJYgGvYSx{*7ka1*@(O?4HMy4QPO%UU+o14
9P;tbW)aWnd*(ym&;=@~6Db}`V}$UZ(hA9_F`80k1#zYcKQJ7Knce|mXTh-o3wJPk;gZ(w?~c|_-
&l=b2^KIB4J5u^c5QME_CGdM`c{|P3G`@BKTrHnto!+5=*!zc0x?dCbQaD5<J7@3RR)k$dnf_}dZZgBpe>+oE>?$*zu$54t-
h}&Pu+HX-UvoHneTqw1jzH_eZFg7;XPYMRRV8DA*Tx&sJ)Wf(X&M!|Zze}}@1s3a*KEe$o4g95i0v4IWxXXS(ZYUN0t|R;)#JSp4
z5b&IDFi^e%VZC$kdd&e(2Vt<FtQ-Gyz0`}|NRZ=rig|&vFE!It(Ig;r81R>qnw4TCN<@Pc9Z+r9u*Cq;<MrrB+b7uX!Z$Q)Ef&h
2Ll*3?}_cqsXJ3!iAH86I>rCX=RPM^A8*1_nH&e|)m3|OkQ&!|?8~RHVr7!^zS`r5QE+x~2j!6ddu#!Q%X<X=$ul0I&TtZ4Lx4o9
ocV3~_>-$sV`?c<*CN{?C#LnC9MmiXtHvad1l<z0%E!mi9-3t1E}RskD0~UidBg%k$EWLH7%3Su?y-
J%OFoxr<3q;1KL*duv1qXPkOcBtoiqX9m=|FAw*E8cNB{O@^W2@_L|n8js;s~`I&n4EFcjGQ&cKQIY%8FkA-
R2p=CfG?`*gzdUUe9GBBdNuS!7{tKBTw;VZ@@*?Oqu{IG~>K=Wd+|WWR^2nm&$)66Y5O*+goT^ULDd^7#sDyd|_3J5MTWa`iW7tW
%Dy4gtDy?@5KAp>c*4&NY3{v-|D3p-
f%QedpFV<*r6e)`>~*Fidg14fW?5cz@0K!f(}kr26(zl;`fs0!q^G+1fAA=dp><Y=}8&!1b1OYFVr*!ALaXy?%y?cRI@@^3GI$g(
>_6+nG1a@S^5DV5696!4I2Gk+#(-W?^*w->Z@HIDVY{t9FG?3;W+?eVpRv)u$-ty(wo~tuN+>Go-a`u!z_b=E77z5Tmi-
U)q2iNf!dD$h4S(5huksjHI8<xG|b`CM6Y{Z8|6++sAk{grpl4BYOV|utmSp3!sPIOj?~op8u+g>=;8P5LiN8PyP+jq30lviP*8*
c6&bY*2rgWg-VKNeC(@NEoD?HNYjMSp#B|2N>k*d?Wo%4JgL;nn;w74q3ZCThQ|8=hZl~FJ|U^zMKza5fG0j3ost;upC9QWR~>z@
3eJlVpABNDi#6=_uB`Pr+c2zTk!%v6FXDbYbX*)@y{Vr|{~J@n&*(7jhM1-
{uEXxK34a_as7=4zlqS0ypy~NJB>+FqP*y$J2FP^tUX;#%wC1$y_l4SRaAleNTRNR!Y9j*q>jm?GIVl|P-
VBS<PRtWJN$#5%aepJ-uWP1DALPr|Eq*OFu*MokA@@3&gzUFa+EO-5a_+#t=3Fb)myrHsY9x&a<+iu;S7tmS!PT&)Y-
<`@A&bDDU;>r)N_ns(T-Tt@w&0oO9#nB{qi0<3-7&?O?k7uq-Cjz&Nv4Zp;>=A!ih0A>&TSR!VM*RHkj?mm{Z@!DYE{2P6(xQdb|
61SyIIAvMAx_R1-
nYH>uc$f|Bfd7{A?a9)Nsc!U1tR4&TF9tvE<y9qcN`Y;ptL4n1q#kobbGiZAwdB{>O{9w8xKPQ!j|Yr#bdb+hdPNWI_DN4S1X6)V
FP<sUzKu1lhm1B>1D<Ny_0)EAygJ1V8AOAvP%W?7E~s>>4bvZ#J&WjwfRACe=KxCK^i9t%y__3XB785Ru-qn4+MkCxML-
n)lJjG}fqqh42u`@ppy?QZI%&>L6vy-
i)QFVL<+EzdwEEtXmT|n(tFvuBrc@H+q2+vp<x5wb5Fke}#3AdGIsqIOeR&_S8P4cyh2HG;X@$8r6V1-baB5+T&6rB-TMkAJJz}_
xZ5LE3HUEzgbD&(Eu>B_Doo2Nu8BDU!Oo{XKsVHRN38z{g7B$w7{QiJg-
>dOaC+S2r7pP)j4~={Uz_`bn`2M=HQIHw`K$UY9?2FXKVB1Ta8@EwZ<6W_*oxXq8F)Y`!0T0==0(53OjE_8D0Y<E(M~+^s_2EJO<
nJj0V{ZyJxtzPKwe}$SQx&x~_%cbo*N3>2#^Qt#j!$dD@_&QAIOA<+UW=X7}~IObfe3P}V|Xy3?%1d)wOU;*yGyto&~0o=>l}(1k
49EmO7DcYVK|eYhOauAZhTu$SHJZEB2n)G^~j?!hD`E41BDb)ZMtplHlmOKaEC2y42L_W<)lzv@?`w!R6?aStI!$T)hglKy%ov%U
y(YX)xMZe{%AO{_$_{6ogOtZ*g(%T*T4l%*s;XhJB1xJOI+dRclv-
6rLQt%kpP_d<qMU|vuK_Ol~Hw>Fguo{xBJ`O+$%k(uv6wcoNaaOH9#Zhr-s+-
s={TYB;3N+gPwdSca_d$tQeW1RU<`Lz#Ky!%zxF;mc#e9CRA9+ROg=~XBaA3j3Og2#{3dwe<~E{dUm@6r+wyxwm_Ai~Lvo@4^@rT
d{MXAZ^9D2GEUKjL4l_Fm-
4fxLv6H~L+x`<^D`FFXkElkepYHm#dARDy(gHR6?TY=qEt$iDF=(e2+#)Vq|OIJds5P&IM_3Q!Wss<qtaTY@&oP_EHKPt@a4_i{)
Qk!%m?u(!J_{>cPUH>GYgl(?L5_@|}N2;s2twgX=w=zzmA{0i9jo^hq^Jb_g1{6>@?R!5S*ak8?p+{LKR!9yOL@X0GUeqy+$rrd6
yq&93Z!meyCvn|YW+A~6hsQL_T<uN#YLTjjz)EP}O0S6!Z@HfaRWd#wO>5yYVa>s`~hmR7&4&9ps`>Pf@$1i((!p$eXhjn%%PtVY
0aP#Qx0{k=aK<ug%8)%Tu&-CQTCrFc<;@mnPJO;NBKO<tSgNO|@<#jD{2yO8i-6fQl=QC=V!X*xs@cO%)o-
(uU?9CLVb}tiz#vPElJlMZm68P?-pIQ%QUL-BBK!HTD+IsABV2`?G|Mk9y2IUW{&6n_-
70?sSmK6rht<z?0u{rSMTcBfCWQ@!;P}yZp0qg#87Q4Ec(alm4NK_^r;yhDl{PjHDpR1zoDz%UgEm&lrsaUa?G@SK}W&|hpa8!qA
oj%IAbWf*1J`=3GUsR{B{rO7|&wR#V(S?S$Lypnx&r#I*`IaT(rF?r_dv7XAkgBE!cit4#`7p4Z<o~rHSdSi<pCq0hwTfh%d$pT>
lFVVGuv-Zo<hAz;L`(<3PE{x0pV|VFJ7zxLs$+^ml-
*bQ+dHOO4CU%J*N9$ocIUM;xq;vHVek3tsCVg<5Kg00r2Zk0V<^DvOsSi?eCT6*4J{QqQ=9^EAWF=@4vo2eaH1#X!R*J=;U2*S+g
K%<F;){PXq359+)oV=C5K5aH()^*cNE}<B@x>DZso<By#MN>yw{T?m7TO)z~}w(V6>eYJe~#lfT}Bu;c07|>EX+Te>N_WJYQ4#rd
F7#*!)ES;u~ptS$6yX1EVE;_zB(iZL~9wZ~v{Lk%Jh&aYv+0m)LY`hWOEBu%8eH^5v7`hbM;BxFJh%CMBF~h^d`)QobZ;dKSiUR(
>_O(xZA6d`r|svn#oMP)Jpw$-
ORR_racbvs|(s>zT%Tunf#W7gYzDSY)L?n9OZhLqwyAzPn`8M3s99!~(ay@w|hWRM`9HcvJ|4I9oD?d*7fJdBbT~Ly_y*@JM>Ej;
_1y1UkD@+9VZr`8GVlh7l&^^7btZRPbd_iM<L&^Jt70yeRQhjzpr=Y+I;Zh|W_Gg7=1}fC?4H6!-
8YaJ{<@nimtpk}My0gE`jE^fH8)?FU+y$O~LS-GFbu^u%dSz|%PUfgIUrV6=zqK-
>rvQdx*`>#<(rNIk$*vW)xkservyESGf_T;V7F&lZ14lywH>vr6)WSR4IC7<aASi<3)Bmb5N70fhapa$+P1h-
UEkND~4y#tMtTJ91*Sm_O`dz%q>ms#I*yHTd~d;`~n_Nky*bWIg}MmRc!LR7jfH#lCh3rEpEXA21Pjv}5r1C5985oLRtvn82+K@C
N4~%PI)m&C5b}aDK$I8h$^W{dL*$pD&v_k-}kYj{Mn_N-eAroc%AEaohaZ>@gz^WZvPphZm+|U4-
A^4#Ro7OFCSlAH_V5{oCH!U+aUNE18co^6i*bf*}{WF2ZdA&%Gk!VGed~Sslw3Hk>0fndO9Q4qvh-
W<KoLG6QHG=NcVt?u|plRn;jy%4q|BwdVW(uF34+buplA$@!<}f0!q+lTQivJ);u4;sq{T<nGy@3jIsTfCfXb!?A20EQS$0v%!{@
osL>viq_1kDkQ7dHR#xa>I$#`*xTtFWzF{o!j&aeh3AX=V>aD-Cx%8Vec;KUQnAH>)rnJXdNfOnKh8^l%2TBF(|rG>sPYB~(JJhm
4+^!#;BOfjN)P*oh{mNn5$eFUMoOlYfD(ym*I@b1j_9{>2cq*7NGC<Y#3up#RCNp1l3!luCNb6h^C%=NHyc4AfP3Zp6~#*%RMGiM
yY#b4sanqta_V<CCqqHu5%CiHJ;+q@Yp_ANi^?uFQA7E!Vw4q{=LYzvk{n!nODb}(0{#k_6-
LPt%$#W7aN0+Kjeqz8Y`Zu4dO^2qAZr3K74Zp+9`!nfvlE=a>WM?f+*4VdMCz%cH#m<K%tj=|V2*sa9EOYK;8APAuZ$a;*6VCdDs
1f47L|(p&ALsL0*$M36)A|^06?Ah9HuV`14%-CiOnCJht2<d&Ik!6TA}}#hZYedAVvKC48QWYrOXIIUGx|xI1H@KLri-
}OVvf$upVOYa?h*Vd0&J)8)zV#1W!&nEeA4FcAozr!PxdJd}LiZ9Y<p$`zp%zXcdt-Bkq@06{JO5t1-
m>5r57G8CE|%Sgga_n^C#~hlOa|p?*<&{3XG+cmjO@F!2^R>VBBq_&6(7j*2kYLuKsvX)Xz?!rwGI8=++(=%SD<s2@wS4Uf%5O9<
BVcl}hEc++<QZr{=DgT4>O?<Q9!z86pWHZ7)Yuw@&)iY+E00apQ?`ORcT^6jZPR>{mO2hIo&XJXbuIX=>rNd|Q<Tr8{$_er>iowJ
QsY7i2>CA4@%T|@va5G6{ouR^HZoSGqHTzy1Q3wjBTh65=UzkNfq8%-
hRFZm08EV06PBUPanBT$&Wri{j<{iSa}l9cHZ=S;W**Sb#1Jj2&UJnmaP=7>%r{NR$t7yqNYqoF|LQ)4210g{}887dvi4&8rDwx2
QTBN0Mo^Cj5^0c$<RC`HUB0S&$>V<~e=q@1M#l>P4yok~5~>t~qC!LpSxFup)mGxk~n=q#5NTV|X$gzlePp*SIFfpqvF_D5GF7dD
OJWRd^Xuie0Ie=Z%H->yd_S%)mAlQVTut==LOiZ(s8dswFIK4xBb!a#y3$c%EKJH}3!LVj?5+-
$c^{9Z%1H?H0+vjb8^+Ex1!lmGb|HXbVhzKp3zcIr)4sz}bm`ii+sB!ty5kNCF>s{ks$W;7*Nxwm^>xBN?^(>lS!+t4TxTm67Xb2
y6k2kyi@BllPd5Kh)+hGkmJf<`sgWX4E&M~z91odZZebcI4kqkQk&`TOy^;s33VyKtbb0BE9t%uA<PT%f|2^84s<(DE*NaJ0yYeQ
U5HDN~oEnF@A_Y<@PUpj*dJorbmookTvuhQuk_XAHjhM7=GrVdD%-
cM&K|Zk3??W|cbR)6HgYn*jCIfhFL=vhM2<hYcZZAudF9RAK0m#cR*f>|u|z#K%Gnod^@rM$^+sliDv1Az6ljr2YKLAP@IC|Mq2-
nL>s0<7U5^e=!R|p-
;f?3>}VGc)Du6*vwve8T~L5tL_%hHHbZ3?JeU&WAUAzTUJ9n>(u?4*K#UO*s>KLt)`O3;%D~789uVED^uW^&K3BiOf>qeFzFMqI>
N>cs@_PMmNCclUC-a6l!2Rn=s?44Up07)XBM1FgZ26|Pk#KR?qcoN&olFeg}0I-p?W=hI_iZjxF%vth<lxr+cJ6v@M9xVQX<-
y!mb24xP>CDk7FTEsoRH9;}ZriQx!Z7FHH}IhDdXZ7Zh2bHl$L|J}4p(UWmkiv#_i)L>|&YSRS{phf1X!)vv|nGd5G!xF+Z>kK23
Dec`X$x47?Dz0cJYn965Iu7DGOQ3ad!pSbRKxQ&scx>X7Z1Q&4xw0aBxTA26v<Cx2+w`m-
^C#|$ToY%l${ib>N4%|5yaOpXJ)Y9L--
}iV>l=@fAHi5J^YK{Uy{y@LM*Pq%zuHo%0Mf^ClIX~)|x6|*}^3>2LSj%YXIiSXGd#rJls}A_1@=fd@v@PRJm`?pjuHu^7le}<U!
vgB-dQ~1E(9R3{>MbwTCL&Zg-9j*xkOU-eOTQ1{NMGGj<p6QHb~^<9d&NSJ#5*+G7hX;*m+WuQvwc2WZqpH|v;b~4h#^N79u&Q@*
d4M#FFG;Lnq5%947X<qRIB`gR*t=Sv4Tn}o_`O2+&b3FBXDumfx;woe^4gyXTQTw;fg8OL~TBj3Sh|h*Ku?SKDRR+KgmN!I!Ucxr
B|ltM1ClY5bs?HT;majd#w3zjmQF`cX!eLMHre50HuU?eprqN^w{4M@A*zj9D?wk*B(kIAZq77=Hk#3$hfAv&^g%0<uh91>j^&<%
<B0E=0^1Yf5|trJl}vw3WjJGCCH~W(k`P<i6ob`iy!eSC?Tk$=`gq)gCN`-
z`L;Qu~fh(Ds|HBf4_I_`$}FZ?;zkdjO{oc<AheVH3^N>Z3ZNvF+(H6L5I2_SF-
r1m2+Njr5{bA&?1rQIX$qYAYB8}s$ldO{r!LyqZCf2H4xVAhe7xKAB)9f=v$X7Q;8UKn~J78vdi*MnCQ`FabFx#)XQJ>gsJf<5Nw
ToaEB&>^eB8PbKUOyB#YyY5{Q&+r2uSwE06ZNGh#hCbpy9<={R)7_63+=bP&i2B$k(X6RU{bK2C`tX}CSsXuyb*@|Z$GWQzQVHt^
u=HexG>qdN(q-p&Pl_f7u)-t_50#_F#|*Pst>iA&&mC!(#C_VH^c>J?`#vbK}yZ0h@CMynE2+Ij>&#tpu`5?>j+hF3d(N-
1S=^dHORkzl+8jnO%!wp5;Rkbw&};A}fu{d0Gs>D5_--
==CzC<yY6+o19ehyoJaa1Af1?olbWiJFWj62szL(F;+R=j8UG%FF1qHo60WPe9f~Xc1woiC`%in4u_W@I-gpp^It)XSWoW-
^#2mW>-
*iKhxhB5Z#8q&0dhT$azFvs>A(RnGlW}Fa+UVQ`tRIhW!#Dd$artnP<Difp8+Ie4&;AfA!jo)(mm#tI))+N7smDdiwp(s<R<5FLs
_A(T#@Stm0egef;hA8V0B4BHw2SO|f0B?_08z$j*;o&1<r4gOI?}WkWzOLx*NGjuvSRS~=Z|jHNYSd_4t&z#q0$YlF1Yjd>10%qA
h^R(iKEoJ$g-Bo^<0UBr9-65<-w*^WyDkb#m}f_-hBmy0q<20h+>uIOl_bR~kT{NfgA&(3)u*fg2~IwQRqSy#+CK%i0W$7WrfN)=
%vH<gBhN;V9~NP-0F%v(+ygZ+t~%#l0Avc{HqoPVCgiG-
$zlx+Pi#}Qc)z=}9Owjb7fo4ALWQ<P2p?RAlX9*dR)SjSLg1h*maU2Fz(xfXRgx_U!>tI{74Ls!`QwFZXG)NN|B7%M3@*F*zg>As
|UimvXyY+)Csi43ozx`GTN=omd7Jv9$;Qvj0|tE}^6FRpw~vX3d***9g95xtcMow}yaPZELe80vC(Pg1E<UN-
1yGG1Anip)4BtHJdsNzaavbhMHjHhq_Ldz;CMQvXl3Tgk5Ah%&Ay=`z!Yl(-
Bc{$(f3YpQ{ZzY=c^+tKVsb~sQRh8Y2(%Mu7M%BRLD#+wmxhw}E7{AZbzWNz9A|C0F}XWie#n=SCc+L%rrGcl3$U-
|FsEA0#mp*6z1>-
OZfLX&kDVw?8!22U*dFBjh%@;!PiK*(Kr&dVGKebwyQY{1ut(TCy}ta_`)lK@2dJ}&(O+=&Vme1Nb2OUBRD&5}5k6bU;6lL_^7@8
Zd*q&1^`IM+T%N$Z>2UiFM|TQbNU)~t8b1AW$n*#|Uc=U=%No9UD<6j{ipask@jEk$`sm)ncj(8#+tzx2}9f@Jbm06g$t^o%^=<4
(cX!x3TD9*&iE|K)n7E&|@lS?1^(lH^?>4yQXMb+Hn1$e|}K`k*O9tlUuMudYsy%j1Q|>@ZT)F``|txOSQ9lJnQQ!3#Z*T|^u-
&V5K-
L6HX(YoAnMT`L_thRf=F+}Vh!Y)ja8k^pV4yn^R6f;`UwhSmNyA$^K~W`%>ugaL}0;oADLY8y;ahSsxE_^skcm9J*7;$a+DqTe|G
)UXek#c}ie`)9ca6(H{<+T<szTVo~rJ8ZJ!c-hNK*xUqCEXr;J>tr4lf-
f^)Q7oX#F%XZ5_zqYR2*H)f!l(=5HAyBCA|#cdZ7^>0S~z5zB3Fu_lC&h&U@>%Oi%`iR;vsEJ1F`s=Toq7!2b7-
vrVU*!=>lcXAkAar)T?tU*$+8y>HE)`9&m0T*iI8@!$qpc+%C=`aXX9|os0}L2G&Z22$U3T4fe}PnVh9mqPT!sp4t%&wdDEuwPtF
gTp0_pk114b0zB3Wm6gO-
H}YaAj?zpXUrzii5Jcr_lf(a9eOjx5s*c_fjesxjD>N<pziIO!#z|uT<jj=O&3gh%si5l2cGtR2HW32Q*|Sy=9Bc_J(AmFrX_g9J
!Vu~}1<J6wEL@ZQTo8j;NCZP~T*r$@6S*^It_34v>9V`4q*g-
JZ>Kr4sE(G!h(5YVxc*8ZKDf+Kbn~W3tb!2H<Iah0_0}+^nZQ4e_7;oX;_W%uvT+(PIOdFbK2-
R>^^dRr;}f)pH=mh9IS5vy9$2z7_qhf690=lnLNMv@S@RBxLcgYCt~Vq_#x?}itl9845^Xe(9K-)>_7|TVb+Dv0T-
f39^ZPyUK4xF~JE%ESEw=6!*R;|zJJN&g9d^f&i&KEVVM~Jm)kW&IQ3UJPV^JyCA-
M*BoC{}j42M8XUtc_EeYo&1J5NYMXSyEJFGF-
L2a;=~g#U+3ba$&Vb!X`7<ShfzY|EBgI)pg0I!6#vi6vsnF(DL~u18saqsQKWxh1t{_8RuGQAu#U9YgJ<%H_b0t(B<bE8!;lFF!3
$|LaT3f}d!v+sL96)PWaJ2zF+N_J+3)^Bv_G4Enp_@~)z$b3cGBwgvg0heOiHH=YmZOV&qMNN2~Dd}CSGP~|AhC^cZ#EpLq;Y&R~
K^U)az|AU!i7t9islISW*!dwCNk!8z}e|4P1;Kg~l)`LQlQSPm%Ba9%wo`xz-(bo@N5+WGA=4vm@7pH+l9u=JnVZYOs-;RQN?}-
B|WUq-GOk8n8*R=NM`%-o|IBV>vfg8dq&Ge$O=A{r90nPtJ-q;D~Vs9TaH7-
;RxrCC}!W@7K&ho0MLI=<mjO4FG(9B6iV~;QeLJ1LqnAMXwcbN8y)21jN1_5u4GviHu`o}Wu<^h@h)LwdChNt>beWbCs8Q~u;Y=)
$GDiIo~?jcdZ;VoO-WpwI9po^gx*#I|u6}XtMm#Tu@Uv^6-o)p&PjWK|8A=u8Nua)dOVWmh1Ju9(z6H0Z1pm#g5-uI7yk1cK-
8;`P)zC7dr?9e+gb%WYg00F3o0hPG}IOXP8vBYQl0ssI200dcD
"""
z=base64.b85decode(''.join(DATA.split()))
assert len(z)==17484 and hashlib.sha256(z).hexdigest()=="bc866660d5fb4c2138c0d7a79ce3184188087967c441f1e08e6cad68faeb93de"
r=lzma.decompress(z)
assert len(r)==56469 and hashlib.sha256(r).hexdigest()=="f627fb2d5eae97ebd7bbfaf33c4a077458a916cdd2255567082222c39bded3b3"
u=json.loads(r);assert len(u)==17
out=Path(sys.argv[1] if len(sys.argv)>1 else 'rn29');out.mkdir(parents=True,exist_ok=True)
for name,source in u.items():
    assert Path(name).name==name
    (out/name).write_text(source,encoding='utf-8',newline='\n')
print('RN29_INLINE_RECOVERY_PASS',len(u),len(r))
```
