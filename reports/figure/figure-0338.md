# figure-0338

Historical AI scientific report · saved 2026-09-08 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Vivid Harbor 06 — literal recovery correction, physical witness refinement, and two exact nonwinners

## 1. Verdict and source correction

**No homogeneous own-centred strict (1,1,0) body with true E<500 was obtained.** The strongest clean new endpoint is **VH100_R12**, a rational, uniformly filled, actually centred convex polyhedron with **(V,E,F)=(100,294,196), (S,U,H)=(2,1,1)**. Its sole remaining relative squared stable–saddle barrier is between **109091234010/10^12 and 109091234011/10^12**. The second retained endpoint, **VH168_BULK_R12**, has **(168,498,332), (12,1,11)**. Its largest barrier is between **32444790385/10^12 and 32444790386/10^12**, but eleven stable–saddle pairs remain. Neither is a Gömböc or a replacement for the inherited C1370 result.

There is a consequential source conflict. The journal describes `WB24_R14` as 24/66/44 with barrier about 0.5036567, while explicitly warning that its coordinates were not printed. :contentReference[oaicite:0]{index=0} I recovered the actual Library archive `GU22_complete_working_handoff.zip`, not merely its filename. Its archive SHA-256 is `420096f08179c9cb00c060a06f2ccc15b831530b673cda206f051120f5625aa0`. Both copies of the defining `WB24_R14.json` in that archive contain **33 integer triples**. Rebuilding their hull and integrating their actual mass gives **33/93/62, strict211**, with barrier in **[569990360800,569990360801]/10^12**. The old replay wrapper's hard-coded 24-vertex assertion is wrong for this literal input. The separately recovered `WB33_corrected_exact.zip`, SHA-256 `6ca109447ded178b74c8b482644840526c7637df05282f5de97334907356171c`, agrees with this correction.

I therefore use **WB33_R14** for that literal geometry. Its 1,605-byte defining JSON has SHA-256 `b0081310bb4f9ea9ac7e9086c49c7b8ced22fa82add6136d37bab88b13325e1f`. I did not recover a distinct 24-point, 0.5036567-barrier body. GU22 was also reconstructed and its original complete replay passed; its erroneous illustrative face list was not used. WB33, not an invented WB24 and not a renamed GU22, is the recovered starting checkpoint for the new branch. The complete WB33 definition is included in the literal capsule below.

| Literal body | True V/E/F | Actual-centroid S/U/H | Weak S/U/H | Largest positive relative squared bar |
|---|---:|---:|---:|---:|
| Corrected WB33_R14 | 33/93/62 | 2/1/1 | 0/0/0 | 0.569990360800… |
| VH100_R12 | 100/294/196 | 2/1/1 | 0/0/0 | 0.109091234010… |
| VH168_BULK_R12 | 168/498/332 | 12/1/11 | 0/0/0 | 0.032444790385… |

All three bodies in this table were reconstructed again by the cold replay supplied below. The 168-point body improves a height diagnostic, **not the equilibrium count**. The 100-point body is the preferred clean continuation seed.

## 2. Constructive mechanism: new witnesses, full geometry, real mass

The original rooted-ball identity remains useful:

`p·(q−p)=|q|²/4−|p−q/2|²`.

Thus `p=(q+|q|u)/2`, `|u|<1`, gives a strict outgoing radial witness. A complete acyclic forest of such arrows proves a unique unstable root at its **reference origin**, even when parents become nonextreme retained points. It does not put the filled solid's volume centroid at that origin.

The effective refinement in this continuation inserts a **new intermediate witness outside the old edge segment**, rather than adding another point constrained to an original-GU22 witness envelope. Suppose `p·(q−p)>0` and p,q are noncollinear, put `a=|p|`, `b=|q|`, and let

`d=(p/a+q/b)/|p/a+q/b|`, `k=d·q/b`, `r=(a/k+bk)/2`, `y=rd`.

If the angle between p and q is θ, then `k=cos(θ/2)` and

`a < b cosθ < bk²`.

Consequently `a/k<r<bk`, so both **p·(y−p)>0** and **y·(q−y)>0**. Replace `p→q` by `p→y→q`. This creates an explicit two-arrow escape route with additional supporting material and a new usable ancestor. Subsequent motion is not restricted to the original points' diameter balls.

For selection, the implemented refinement ranked weak existing arrows by descending `1−cosθ`, with index tie-breaking, and inserted at most the requested number. The direct 100-to-168 refinement inserted 68 such points. Thereafter the actual convex hull, its supporting planes, its filled-solid volume and its centroid were reconstructed throughout optimization. This was not a fixed-face perturbation and not a collection of independently weighted point masses.

For a current outward triangulation with `d_f=det(a_f,b_f,c_f)`, discovery used

`V=Σd_f/6`, `M=Σd_f(a_f+b_f+c_f)/24`, `c=M/V`.

The main successful search variables were **all Cartesian coordinates**, with constraints imposed on the **actual centred positions** `x_i=p_i−c(P)`:

`x_i·(x_parent(i)−x_i)/|x_i|² ≥ reserve`.

At restarts the forest was retargeted from the new actual geometry. A later variant dynamically selected the best witness over all retained points during each evaluation. Positive arrows strictly increase squared norm, so a complete one-root positive forest cannot cycle. A separate full-three-vector ball-coordinate branch imposed the three actual volume-centroid equations; its unsuccessful results are not used as endpoint certificates.

For the polar repair, poles were computed from the physical centre: `q_f=n_f/(h_f−n_f·c)`. Angularly normalized escape costs, reverse Dijkstra and path-use weights covered **every** actual pole. Two-root stages exempted the largest pole and the stable root associated with the largest remaining barrier; one-root stages attempted complete cancellation. A height decrease alone never supplied the acceptance test.

The executed progression included an exact 56/162/108 strict211 checkpoint with barrier about 0.319999, followed by the exact 100-point checkpoint. Further witness insertion and supporting-geometry motion gave the 168-point bulk checkpoint. All final point positions were allowed to move; **set inclusion of the unchanged WB33 or GU22 solid is not asserted**. The supporting-geometry changes are therefore outside the excluded fixed-original-witness additive family, without pretending that a volume difference between differently normalized endpoints is an added-material volume.

## 3. Exact physical definitions and ordinary moments

The capsule contains complete integer tables `I`, denominators `D`, and actual outward maximal facet cycles `T` for all three bodies. For each table define

`Q=conv{I_i/D}`,

`W=Σ_(a,b,c in an outward boundary fan) det(I_a,I_b,I_c)`,

`M=Σ det(I_a,I_b,I_c)(I_a+I_b+I_c)`.

The delivered constant-density solid is exactly

**`P=conv{(4W I_i−M)/(4WD)}`**.

Hence `Vol(P)=W/(6D³)`, the raw first moments of Q are `M/(24D⁴)`, its raw centroid is `M/(4WD)`, and the three first moments of P are **exactly zero**. Both audit implementations independently integrate the raw body and then reintegrate after centring.

### VH100_R12

```text
D = 1000000000000
W = 3753727299588899175519679655026603617
M = [110332267603849604865000995169615184146074560814,
     -2768874983775456772287391183497277972865547620,
     110598142157011596794125259466480147123351387497]
```

Its volume is approximately **0.6256212165981498**. The raw centroid is approximately **(0.00734818080790878, −0.00018440837351708385, 0.007365888177940103)**, not zero. The exact rational centroid above, not these decimals, is subtracted.

### VH168_BULK_R12

```text
D = 1000000000000
W = 3584139092055092541290333350585887367
M = [-334047780584377025409456296877591100712287683181,
     -85767415667440706523441160471790919924566134632,
      313274241270578658010579939603646734171312399581]
```

Its volume is approximately **0.5973565153425154**. Its raw centroid is approximately **(−0.02330041971061166, −0.005982427960005797, 0.021851428838588392)**. Calling that input origin its physical centre would give an unjustified claim; all delivered mechanical statements use the exact integrated centre.

For the recovered WB33 parent, `D=10^14`,

```text
W = 3356680172842014703619109890315856973552743
M = [-2059087737181972865719894708502135740072830,
     -1457238210809796348793678234112554101803042,
      -894131444717644023930208115815155083735237]
```

The reconstruction also emits **all second ordinary volume moments**, independently checked with an interior-apex tetrahedral implementation. If `s=I_a+I_b+I_c`, its integer second-moment numerator matrix is

`R_kl=Σ det(I_a,I_b,I_c)[s_k s_l+Σ_(v=a,b,c) I_v,k I_v,l]`.

Then `∫_Q x_k x_l dV=R_kl/(120D^5)` and the centred matrix is `R/(120D^5)−Vccᵀ`. The complete rational matrices, not just inertia eigenvalue approximations, are regenerated in each `*_extended.json`. Thus all moments needed for homogeneous centring, plus the full degree-two moments, are explicitly recoverable without numerical integration.

## 4. Maximal incidence, full mechanical census and robustness

Every maximal face of each retained body is triangular. Their actual maximal cycles are the literal `*_T.json` tables in the capsule; every true edge is a distinct consecutive unordered pair in those cycles. Auditor B reconstructs its own full hull from the point table without using T. Auditor A independently checks every proposed support against every input point, reconstructs its full contact polygon, and verifies a closed connected maximal boundary with opposite edge orientations, rank-three vertex normal cones and single-cycle vertex links. A missing-facet negative control is rejected.

### VH100_R12: complete strict/weak lists

```text
S = [[0,26,7], [0,5,22]]
U = [0]
H = [[12,50]]
weak faces = []; weak vertices = []; weak edges = []
true-edge primitive zeros = 0 out of 1176
```

The complete retargeted primal forest is regenerated deterministically by maximizing the exact escape dot product, breaking ties toward the smaller index. All 99 arrows are positive and end at 0. Its minimum relative dot product lies strictly between **72644/10^12 and 72645/10^12**. The polar forest has exactly the two listed stable roots; there is no omitted polar root.

### VH168_BULK_R12: complete strict/weak lists

```text
S = [[12,50,20], [12,55,50], [12,32,21], [20,50,55],
     [12,21,55], [20,55,25], [20,25,24], [24,25,55],
     [24,55,32], [1,24,32], [0,5,22], [0,104,61]]
U = [0]
H = [[1,24], [12,21], [12,32], [12,50], [12,55],
     [20,25], [20,50], [20,55], [24,25], [24,32], [24,55]]
weak faces = []; weak vertices = []; weak edges = []
true-edge primitive zeros = 0 out of 1992
```

All 167 retargeted primal arrows are positive and terminate at 0. The minimum relative dot lies between **270485/10^12 and 270486/10^12**. The polar forest has all twelve listed roots. Input, face and edge indices here refer exclusively to the respective frozen integer table, not to an earlier unpruned numerical cloud.

For **every true edge**, the exact certificate solves its perpendicular-foot parameter t and both coefficients α,β in the cone of its actual incident facet normals. Its ledger contains the signs of **(t,1−t,α,β)**. A saddle requires all four positive; weak cases are checked independently. Classifying nonsaddles by their first negative component gives:

```text
WB33:  [11,28,27,26]       + 1 saddle = 93 edges
VH100: [53,54,92,94]      + 1 saddle = 294 edges
VH168: [96,94,138,159]   + 11 saddles = 498 edges
```

No saddle count was inferred from Euler's formula. The full edge ledger, both primal/polar parent arrays, every path, every strict and weak feature list, all support planes and the actual centred rational coordinates are generated by the replay.

There is a separate exact **fixed-body reference-centre robustness** certificate. All ordinary edge primitives are affine in a reference displacement δ. Taking half the minimum absolute primitive divided by the L1 norm of its coefficient preserves every primitive sign throughout a closed cube. This proves the complete census is unchanged for:

```text
VH100: ||δ||∞ <= 7/100000000 = 0.00000007
VH168: ||δ||∞ <= 1/2000000   = 0.0000005
```

The actually computed closed-cube radii are approximately 7.602221540947628e−8 and 5.12851131850307e−7. The corresponding open cubes preserving the chosen primal forests are approximately 1.5204443081895257e−7 and 1.025702263700614e−6. These are robustness statements for unchanged geometry, **not displaced-centroid solutions and not capacity estimates for a mass compensator**.

## 5. Exact whole-boundary basin data

A new exact sublevel checker reconstructs connectivity of `∂P ∩ closed_ball(0,r)`, rather than trusting a numerical persistence score. Each maximal-face/ball intersection is convex. Two adjacent face pieces connect exactly when their common true edge meets the ball. Exact minima on faces and edges therefore give the entire connected-component filtration. The union-find implementation records all positive finite bars and checks that their deaths are exactly the independently audited saddle edges.

VH100 has one finite bar, born at `[0,5,22]`, dying at `[12,50]`. The surviving minimum is `[0,26,7]`.

VH168's surviving minimum is `[0,104,61]`. Its complete positive finite bar list is below. Each integer k certifies the exact relative squared height is strictly in `(k/10^12,(k+1)/10^12)`; the full rational birth/death radii and ratios are emitted by the checker.

```text
birth stable face   death saddle   k
[0,5,22]            [20,50]        32444790385
[12,50,20]          [12,50]         4359234204
[20,50,55]          [20,55]         2855316541
[20,55,25]          [20,25]         1353470158
[12,55,50]          [12,55]          435564203
[12,21,55]          [12,21]           33603080
[20,25,24]          [24,25]           17307265
[24,25,55]          [24,55]           12726263
[12,32,21]          [12,32]            9638881
[24,55,32]          [24,32]            1232704
[1,24,32]           [1,24]              17202
```

Here the relative squared height is `1−r_stable²/r_saddle²`. The extremely short last bar is still a **strict, exactly present** stable–saddle pair. Neither a small bar nor a small sum of bars is cancellation.

## 6. Executed audits and cold replay

The original two exact auditors were executed on the retained rational bodies. Both enumerate supporting triples independently; it would be inaccurate to describe the original auditor B as incremental. Their physical implementations differ: A uses an origin fan, all-point vertex tests and a Gram normal-cone calculation; B uses its own three-dimensional supporting-line polygon reconstruction, an interior-apex integration, incident-edge vertex cones and cross-product edge coefficients. All common output fields agree.

For a faster portable cold replay I additionally implemented a standalone **exact integer incremental hull** in B, and a **certified complete maximal-boundary verification** in A. The latter starts from the literal T only as proposed incidence: global support/contact tests, closed manifold checks and full-dimensional normal cones establish that it is the complete hull. B reconstructs from I alone. The canonical audit output hashes match the executed original exhaustive implementations. These are independently implemented software checks within this research, not external peer review or proof-assistant formalization.

The exact capsule below was decoded into a **new, previously nonexistent directory**, and its replay was actually executed there. It independently reintegrates volume, first moments and all second moments; rebuilds/classifies every face, vertex and true edge; regenerates both forests and exact sublevels; and matches the frozen output hashes. It also checks a regular tetrahedron, a cube, exactly rotated/translated copies of all three bodies, and rejection of an incomplete maximal boundary.

Observed terminal receipt:

```text
TWO_EXACT_AUDITS_MOMENTS_FORESTS_ALL_EDGES_RIGID_AND_MISSING_FACE_CONTROL_PASS VH100_R12 [100,294,196] [2,1,1]
TWO_EXACT_AUDITS_MOMENTS_FORESTS_ALL_EDGES_RIGID_AND_MISSING_FACE_CONTROL_PASS VH168_BULK_R12 [168,498,332] [12,1,11]
TWO_EXACT_AUDITS_MOMENTS_FORESTS_ALL_EDGES_RIGID_AND_MISSING_FACE_CONTROL_PASS WB33_R14 [33,93,62] [2,1,1]
CONTROL tetra [4,4,6]
CONTROL cube [6,8,12]
VH100_211_AND_VH168_12_1_11_EXACT_COLD_REPLAY_PASS_NO_110_PROMOTED
```

Defining-byte hashes:

```text
VH100_R12.json       4211 bytes
b85a8730625481f4965199204b4faea306d718aca03efc488a185da9fceac52f
VH168_BULK_R12.json  7036 bytes
7e436c1da555bf0f56936abc0184a3da4afc0fc245ccba28508aa20122ae4d10
```

Canonical A/B audit hashes:

```text
VH100 A ea8147601f59b1c3a8f6a2c95139401e509241f26086b09b7bf5dc374b9d9845
VH100 B 4b8a078ae0e9faaeae1b59b50ae6b91a610505217fd8a775af8737899a194b8c
VH168 A d0e95b20ce384ff8ac7b0c51e03ebc06f77d5f66f7bcbb99a6bd1c073591a789
VH168 B f6e433424722ac56ce1cb00eea4e8276e7a6b43fde47f524d4c6184a82351fba
```

The literal manifest contains every additional source, incidence and certificate hash. Exact replay requires only the Python standard library, tested with **Python 3.13.5**, and must not use `-O`.

## 7. Unsuccessful finite branches and the remaining gate

Several explorations moved substantially beyond local cap adjustments, but did not produce a winner. Dynamic all-point primal witnesses with the major-bar/two-root-minor objective lowered a numerical major bar to about 0.01186 in a 166-vertex own-U1 cloud, while leaving about forty stable faces. Full-ball ordinary-mass-equality trials likewise retained many polar roots. These are numerical observations, not additional exact successor claims; their endpoint coordinates are not needed to reconstruct either retained exact body.

Direct attempts to repair the 168-point minor forest, sum-square-root persistence objectives, fixed supporting-cell constraints, affine/projective deformations and greedy vertex deletion did not yield strict110. A greedy deletion screen on the literal 168-point checkpoint could remove two vertices while retaining its numerical twelve stable equilibria; its next chosen deletion increased that count, and no further individually removable U1-preserving vertex was found in that particular path. This does not exclude coupled deletions or a different forest.

I also executed two genuinely whole-polar replacement families. Geodesic new-pole chains, and radial lowering of an entire one-root pole forest, could make the **reference-origin stable census one**. Reconstructing the primal solid then created additional unstable vertices, and the ordinary centroid moved. One geodesic-chain screen had reference class `(1,2,1)` but actual-centroid class `(39,32,69)`. Restoring a reference primal root by a second chain did not restore the polar or physical-centroid conditions. Some floating maximal-face screens had more than 168 vertices but fewer than 500 true-edge candidates because of nonsimple contacts; no exact edge count or own-centred 110 is claimed for them. Rationally preserving those contacts would be mandatory before promotion.

Thus the open constructive gate is specific: **cancel the complete remaining polar basin while keeping a complete actual-centroid primal escape architecture and all ordinary-volume mass effects**. The trials above are finite unsuccessful experiments, not exclusions of those families. The earlier original-GU22-witness envelope obstruction does not close the moved-geometry/new-witness frontier used here.

## 8. Most useful continuation

Use **VH100_R12** for a clean strict211 restart: up to 68 additional supplied points remain within the unconditional 168-point/498-edge bound, allowing 204 additional edges in the triangular construction budget. Its remaining packet is exactly `[0,5,22]` versus `[0,26,7]`, with saddle `[12,50]`. Retarget both forests at its exact physical centre rather than inheriting the weak chart that generated it.

Use **VH168_BULK_R12** when prioritizing its substantially lowered major basin, but respect its **498 actual edges** and all eleven existing finite bars. It has almost no immediate edge headroom. The exact packet list above identifies the supporting region that needs a coupled replacement; deleting one tiny bar or one redundant-looking point at a time did not supply cancellation. Whole-panel replacement, preserved maximal polygons, or a coupled contraction that changes the forest before adding more geometry is a more appropriate next experiment than exceeding the size budget silently.

For either seed, the acceptance test remains the complete exact actual-centroid census, not reference-origin root identities, optimizer feasibility flags, a small persistence objective, or an Euler-compatible count.

## 9. Complete literal exact recovery capsule

The following program embeds **all three exact coordinate tables, all actual maximal facet cycles, both independent audit implementations, both moment implementations, complete forest/full-edge certificates, exact sublevel reconstruction, controls and the manifest**. There are no historical-file dependencies, omitted helper functions, optimizer inputs or archive-only coordinates. The canonical decoded fourteen-file mapping is **50,028 bytes**, SHA-256 **3c6f7fbf3269a7bf852edd658fe5ba6709df48ad92a47126d0196641daf271e8**.

Save it as `recover_vh.py` and run:

```sh
python -S recover_vh.py VH_cold
python -S VH_cold/REPLAY_VH.py
```

The destination must not already exist. `VH_cold/output/` will contain every rational audit and certificate described above.

```python
from pathlib import Path
import sys, json, base64, zlib, hashlib
B85=r"""
c-pmn3v<(0()M5Ru=Q5#pn#6<ibqs23+%8vzzi^#o#1lGlAIVEJ7YV6FvWlWo~Qfh<^*Q=zW3V;k)?C#)2Hv<()shw%f~<d@bJIW
U%tP0aee3b&KvpfKiB6M%W78*iuJM_R3GwUH`r9gdbQncE{ok_y&B}Ja&T2`7V|}s^Tv4a<Mr+g54Jlz$~Wa;xtMM8&Go%Et4Hg>
YK;*tSA+M9-Pz#i#l6A9<#MoCU0m)4XZiN5+79wfHMqz(yTN)s*qv4AzN<F*a&Vrn7V~Pm!#E1uo7Lj{VvUAxx9gR|-k8bRUT@#5
=9~372HEk>z_$7kKkbwJvRv$@52v&BB|*Hdo5%vE^0e3TyXj(8Y^w8WwF4lwakp8uE%J-1eo|DMo#LaapMTg@tFkJmok#7YyG`D-
BLLgW*|NH-mfN~XbHg?}UlWuqpem~i4!qjcP3@yMt9-k~T!ZPftY(*|)9IVl%NH+RXT-vAI-M_;)pR<#x2d-4<yAEt-2=+e5xB*0
^Fg&L)_`~TVRXEyc9)x#Ao*T-d491SesH#!YWl9a-e#{imzA@v&^zC)H`{D@;NZW<2cywF9b-7s5qIy`!wcti_I$mnM#pbJI9UhX
!;6!Hrw0=Ue;(n_>(O|Y-SPlq4d(03;2lV2FyknL#eDGYo9tk*+Eu3;p}^^Gv&dJc%W8XYY_X7^yqjd%4F5XsICXvZ;C+?9JHVq8
*TH`$Le01h>aM0$d0I^`HjDGcZgEvjKUSOdmTleM2nDdV!OqSXo9%9D(Jw<DxWI(|e}XO_GTCV$As>x5`FjUFGus|FXQOslJk7EX
CkOaD-ICqPc3=UKUD=?Xe7_NfvfGwBGv`CStLOP*H5BC6%#_KtF4uXv9S%t#_YWFA<D&zTNM25NfPFZs(Z9;iD+h9byHGbjIoPf*
H$^p7Ha?i#1K*x+bvjv*j?cb!(Ao8_LW8kg^|D$G(QcGw82ZF+hGpw}+q2vYBYA%Btol$cPBG`uwlx!n!(yWK<u21@;0i+JV2r=_
&fk@b&9M5gzz(h73C-3^+2yA<S2A0diyKS0xQVMFdfz>;i0Wf%{Q7gvr>}4Az$s+2GRr9qUQS58E!m$O`~sSKjQ>A5m`oG_2fsYV
k8y`8A=#7+<#GM9rtilGlW#-Ul{uR}=lO@ldA^*^^P-Zjulvs-&>@D}$1?J(cF@a}ZE-~**KPE3+i07Y<x+X8eg3^rEJ${Hx!i5D
KMx*)bDe|l4vuHeK}TdB9Cv;QBRL1PXgxUo;2bo9^5D3+ly;vuzMv2?(^=2n5|ehm-YyHJ*3u8{M&ltUsNTARyX@cD^7k8bwuDUD
94ldFe?hh~lf|s<p_ovrZFuN}(@h-C?g-@CSo;5C@Cr0Pfc##Rj%tqO^<cB!0XL<f8`5UAUGnF>!9OV}){AnmfL5`xlFd#b67F%h
N12M)@gKndql4o|4&?6f$;lPC>u!Ab$T_+KPagTWx;pVDcf-R+N|aYbrAq0Epg9K_gN~Ju{{SI($p|EHwO(GHSKR#052cSD<#vAT
jc_Za-G09rcc1WX-0IBn=k5|_&yZRUR4^ZnWTA5|G{3<JpR(*r?Qb;aJiE>H@h#f#k@NcG_{fNw!;Ti!#cuFWK!RF(yxFWb#}@!m
o-Vi5@g`qvtGyP(gM5XFi`sH)Y@GKwY^#D}f>~q+=(g2vc<}ny7t_bTJ^bhE>BFBNJ$?OZ`s~HC$ItQi$%~hdU*Ye=AAXoVe)O-$
ucj}b{_E+Z>BHxbrq7<fdiC`Azot(f{`2wlpD&)je)-~u>5mUzy*hBLNVP)A>1?AjUtVs{8u<&I1)5xLvy<V$t^&0lI438@!G9+X
{vPpvxH{sk`ieg$xD1@Yi6$dwcu-u<Dt25rZyhTq7a}L6sr-Js_xoM@8$(4-;uvo-nsl|>Q|En7tEz?axG$lFNsKVb(@&#YMK4Df
TO?Z)9f+cmvG<T++x_yraowqBj9?kRqGW2kshQ%AZqh$r{P1XMt#u-N`uqhRy3-$DzIgWH_2Wke{efX0O{bi6I?b|!>6A9Wbb4^C
w!oX!9p{eD`O<hI)?obq`R2}}H+PP4xBZXv=FU^x!v>ke#F1yB6gz<Hz@%Xi7|%J1lQ50rC^T;B%5Ejb#BSsp&-0xiL@zf?yf_HZ
6una~4Wl?=Q{TjC8XNRBf#YK|6NO<EnaDW`V$Y9_2@*dd2?R;x#jzi!fg3q!==xFU`zAt5AD1!a2N*G0hN;0ENf7&y@Azq&1}1ca
$R!Q=iEr@OPZFP`hF?i!(#Uwm30!oF<21rToTD%eLo`jJ$V&)k5PD${M^O^GjtK%z7bZcFIw6`Ez!jOmBbagQg}$3cegZ1vR327{
>6{?JkZItf1?P_ZF!He06z#Ec-vv6|)bnD;k5Vs4;=uPpt|m?}6P9h<!0`gt3u2%Wm_es7_B_BBgpmxGru-SiVd{9P2|cv)uqBR(
jGMSYY{HZv9${V}B?!Va;X;9c6l+I!$Ao_B0hA>6h{+>Ac6}_!1?WC@BmsVa^u+Vg(E|baZWIG)Z0e<G<wn@`AVyQJ&GS<exL6Pd
2ZlX23KE?^^;`@axlWjnpb|gzeJ8@T@29Tk1%Xge<a;JbfZh~a=lLGGao;^B0zF}+AR$-gPO&W@iGb9Ai!cs6;LNxnx6}Y;AT&-A
3nkz%zK87sIe4)P9Ab?i^DxDZpr`9aoF01$+(oJJBH+cvGO>mPq=wnCI8bH;x>6*8@~{b*lyFAIkAWjlee49W>?wLgx+K?Ndf$NT
&=gdeM6U0W3IR+6A`r4mQfUjsVzn-aCxDnrjT<EZ7ql5*^YAcmLqpE+A|E&leGjZbwgCkvXdMFcM}}k+yMYfu!KNXWAEzNO4892o
2(~Z*QK4xHdPowZ`w7DFQ&1id!0k-EC;@n&^hjD_R3CIAoOuLR2k(0>mP)b+{V<5Yk`aD^R>*tcj!+~6FbGBh@3?6Qx(r<KpKBtJ
HfCbO5KJpOh4lo9;3MHW5>f|{?t+bhG0+*f9h1lgqycBdx&ksMa0Y~cs6+4^F%H@XYGhDI2CRb=3_N0IQj7@ElsbMKl76uJ!ktGz
5wQa{A{luR2p{qWyX-pX8)DB>AXu8h&PzcN5G|l0KLinCS+R++{D@2fp#z4}J&g%X7?Bqo5Vy-UfGt4`5m?40(Lxpy|JY6+WDP8G
P+$-ZLI8|y3%mrBA6l9YTtGzvCHe#GTLKo2AXBkzfIk8Eg45VC#5RIMUD7LBMlqNTFhpc#AA*Bq33<*j4R|&Mo<j&O3jD<LKuQVO
3rYZjg>1?pWo=*}2s|tZ;vB<=;93XB43ZFx>Iykyc+d}o0%*}8abP1MC!rre6X*nniev5(&;fRg05V7vR2P!XAm<VXc*bTyrTC!;
(16qtL0Uis0rG^xh_vlMoB=@ah{(kw3T}!GaF<K$nZU;$P>*p7z|>GQkt_QXM9>@1!4R$B2nbsjLX+!{AOaGqw3L)9M28KAAOYb4
nG}=>h!>m`f$M$jVQ73vLar#`GNIz24V?sx3)u^ekV4)8GF(GQs}zH7pajKMLw;i^DPRmB?VvCq3cyH~hdgk&=vVSvOvON|OI-&7
Gr)f#XNBA$7$B*!0U@42jzPjf=z=)WFaih>D8SXlpjpBt7{CSo2E#z`foVc)IHsWr^+I8Gl2Z^t!DC~9P3)tWU>+zAbPNH93;7kK
+7z=<Nv5I77vIIuE*0JpNE+G~WDF9ev<*Q|5cd!&6pT<mU|di+)EvPCu0s{eM<65URBCEk9^^AfyA-Set01I&1XV-9s9b<-q1*-$
QP=}#G1VEU*aPE<!jjpK2qP>JSP?|2k97!vLY7i_LG+~L;7GL+00SR^Z#>5X31F*0G=y438w?Y%f;{M93U3$W>iCc^L4+L(Nbw=s
fNrqpNVtvCJffZez5}tBuu-64%1<a0P=B0=PK0U1Elw%dVA>=Al=cgSxnL`XCUr$9lOrQfG&{5hkOHV<;LSL=2KiHJ2tq;60p%Cu
HdxH1X2h06Vz_}%U91X5jMx_tGFSm90qem4Fwn@=9+WsFAK>sKvA!taAiE%Cz_OSGW&njE#5PPo@F>J*sQe4O`G7LTc<2))DeNG~
EyL}Fsf6FLnv+ndz!^!K!~xE5K~qqOkWCmOfhdfXHv(`8sLu68QbJk-dWa!N3UH+-!WDd@ng|;dqpc?@6}Bd%Dv%FS2}l^=qA(DW
hqi!eV1U`!p{a@~ATGddw0eDN&_I0@4{8^}9Gv44lUxCK4*cuVM1TzvB}#0t=@K8)g)}-+iY-V8@^T6S2KN$w0%JrRL#%)Xpssuv
JRYShWCD;4G{S23ebLrjOAKltPQYZK?u7EkfzrYz__U>!CtzF0G)`mM*dP!uq^W}aa)7CrVg!7twgM)ELV`GqNwR2(DPcNc55Sxd
j-bO(Fa$0DkARFY37Ue!z>_Za2j($WPD>o-k`)OM9K@RuLxOTY;&z1&1U}f<7g|*N2b={yOF(ImzT6)}AqxWx)F4736lDdw6oxHi
F<b@025Nx$LkaIX)M?P~*cz2yG>$QOND{&xfsZ(4f`*ic&`(qx+At2tJe2?RFkmsjGN2~|rG!n3U<*SK3ZS&<Ax=S9ko_=NV7Gw5
-Gq)2cn1b72$3Z3)9!XfD8bvoE`&6xA(lXZ;A)6H*b0$w5&KcmQg}eTQ(gfG+KJFtKs7f_yd79_AjXIS1e^mD0gG6r4@QSY29O~^
M8ClKAp2tf;om@_z!ZZ<#{3S(h4_V3h3_C57<>Z71b%~O0^*060`r10lwv=nh3l$LhlYa50LcxFg*LDTXi`J3Lasu;8&F*!q9dV+
Pv9sDF+7(8nFbz$RYQAH^^iwr3RX8HC-rYiyBdZMw$cHM1LGi8&r|!*g`wxso})yC>j)tYuMD_%V5v|prgRg8=AnmS`WVU>N_UuF
*gmQ%hvG@32^<fqA<!5_Jsm#>c*Isi4n)+!AWvWXvRG#)xw}}dIHTM+{D<rD$?ISxE4skZ*e(Jp4iqRprc{MgfFFn52YZSR@Tpe8
Mc`y?qfdxpaU2~X0}ux|$W_Awcm+v;7kpAXP(;xLLUt(6pzg#sMN?=(3ON|d6q~e}x%p6Nkg#;g>AYF}=TdIMRt0*=mY52bis-*U
91pBNiFJAiB~ktWn0_8m4qy^GP+%sY9tc%m3uu9Blal%ak}X_0P-H+!hlxn(Fr{FaPCj)*5jIMG=lIUa35-6_am>*m&SU<P01<8q
5r7w=v&b)o1n5MmKK2|D47i!N+7f~Rof3VHmNxhRD_C#h68IAj9)dm9PJEa+u@VNK+v&yL)SDnoQD)H9SfpC+0*aWZf%Fn=Kx)GJ
l(w)HxUHd%5Req?rO~_S9@`O&FXN_qiS3ZV2u<LK*1^QM8wNTtghiU@UHUXejDFa|3K^baTm_Q1EM_49+-8;ZZ(Iv6#6+mLgH_lx
0GYW8PT=drP}yR2Ta<vScnLwBCQfScK+sb=8$CE}>l1^bzj&$G!4g~@jF)LM1un&|!reI3OA|Vr#n%RKxYAf51D^-JHh^~%3x&iE
9KtwMM8#xVr6By^sQBaRV}l*`byETvO70T1v0^t!co}<o$!T2+qTAd}?O+@?v>^J9_(i-71aQyd(b(B!IbtM;SaF0o1Hof#*PHql
NXVL4S4L|CTNNniBn;UJa)up2W{YBr1ppW7B~~m80%CYqXv8C72>Q9Fu_Z%8JQ!av2Ewu+rZsNy*C-=m*-mPqw#3MZ!e#++Xjd3>
BF|1l(u^$<F=vg$P=O+rLxmbRf{8A(2C}(=MDUPNsBlH=NP!Ayu#psr3W@mP4lJ_RShQJOk#n%BNb$<?Et&YXn>-ig2uy%u#TCF*
;0&cAA0j1`nQ%|29~~W4ehRz@c?^Osv0f&$G-Yr=B~}N8y`$;?{jtNsiI74J_F1wCbt65F?ubzXv6$+h9GvD6p9drg;V4<BiblGK
XkvK)vMbf0&_H4t39%=dkdaNJ>ty`FNjwE5_Lb7GWk8QbDc7ereTW2Y2xTbtiCiT{#(}{rbPiR4F%_FB18Pd7BxnUV(8uV3?v{c>
C1yYiz?9mt`^N5-6Do>anOG4J8oRw*vn~r#Ep8erfJT%=U@`4kz#`&Av;+sj;GU)PQ0ag^P^x<sb0;F*N$yFi{i#LlsKkm`b-dEJ
iDA=JvEk8$lB*=t$6TOJ2{sCpj(j1)`Vzf`GCk=XS?FV>sDw9#3Gg>?l_C;8*3n&guH8Xfp50qN(N6MMVE2WdWlkayFvUXnxblQA
XeC+sXb7og3^b1HOu)P}<@lkl(-)Y93yAP~`Xp2qMyJ@KiCB(xegf?)m0}b1F=>JbnoQJ!h?41dKmYKbzn#&51r0+!rPCiVsP6}i
lo{IX^k3lb!mY3-KCE-P-2wL>_84O|hLIoI-7yA*fho&mum}zf>}CKA`v$%qTyW?-xD+s?;UdE35j{qmP8@}h+Xico&I#;GMw1fe
5MYIhW`V8D!~^VG$VT`Aux^=TNEsJRVe7^W1*<*b!`g&f!(a{VQihvgk25v{(?1TFIPfe9!MOApvIPq<nF5dBrJn&}GBE1lcmzTM
;ys5Fn}OYkUordwct?y>!0cnBEE3`mQ-(0%G{w{fa3EX>lQMjYsT0QPgnH=Q0$|1j;Mc*cbQxDRB+fKq;4WnfgTw`#`0%=5?2;T|
Q_}{Gz=ZH{VSuK-v0f#t=9KYzL30R<zz4#9VQK&kAQL7$)Ouwe2<`>_J~ZW;14BQ9F#vchE>lq&z495Wh+^@)#L%Vx;=>0?B=f>(
9On?R3^y3$k}?*O!a;G<*w98xV9&$H0&+u}&>%`YkPmngjuLz`I9HH+9@All5jTmaGsYUjXMwQREEIM$WsDv!5YPjH^4&mv0T*sK
ta^Cy@XlO@BU92D=^6BrFnB6ti7pr;46yxRG}_{Dr6?NUG}EyJ<@o9e_)J3ilG{3Btkrl-ki<0mk}#z25vyAjg4XD#z^`Jc1>PWO
%$3{_GX-g27>SmZGtS}B@q@0H#0EA8K+wkv8GB=lO~fiZgpfHUIF;lWNn9oLGMFG?fE*4*q?RPm3BNMn{}`VD6ROw3Xaz`saTHe#
P56%tCTYS8SjEl(F_DHK;Bb5J`#p8+0>fA+2!oE02cl;XP3QONSA$5>NNm<4-**|G1|PwiW^6H%ARAqRh$)STAxiZYv6t|_LhKIR
D{zVjU?4%L8o-4RB=qMsI23`j0|UBY%o#lEG87ijeehgn$cQ=_G-Toj&ZG>=XaztAO~H^!u}`3MlPJ-LWJ@mw&BshoNko8|7Z_*^
vxBvn&Q%B8aI%0Q5(s;^eiGoqrb2*(Ou={oJXCS-j1R_O@)q0W&~1$=GZIcAaA6p5foNC=jo6SqeP%Zy*gy_UyfS{AU<LSpD%#8^
F(eG<z<$O}rk_Aplym_kDs~>!A$DfSlmVzrg5VOTg3QGz3~Dg}!#t@gTgpTSz3`Z^bR!X3I{XmxA#)`urcZrMk3a{&-w!;jomhsH
1tMUb`ym``kf^W8p^(`S!@L8du*}<mV^b^=D`)r$QZG`Si0$+J0Ae7enuDZInF)lkOPYeu%pi;CQI{d%B*i??-7&K-N#YTgjIBZh
g{f}3#~@&85=Lw!`VO`>Oc;Y$002`N<SS)Qk^#MQ$=$jj0x)%)&^z{-?1RAZeU*wppcjVX+Ee>5UYbz(!FqtK@EF1cV~W8>2q2e3
m;k_k8c7_P0TK%6L?n@jWCmnn(jgQDqZMFB4UjPVf-Z>-2!g&7GCas!BJYvQ#A8ekSCW_^V;JJGf~=#6f(e#}L^`0^z-)kk?9Q;Y
rx8w(vDis&h>;{YW{>H9lR#o7h7y|@f}rIBnTlr0&t)bkWHkWDok0(VJT;ILx{Os}{hp}Z02}Btr$U59!f}v|>I3@;V`P9Km3$MV
yU(Pg%V;cC58>)*&YVgml1N{eN;WzKZc?C}E;LCbAb;Bk4KNODqd7G%WgP%dML{G68V8bE$Ba{rochcP_>B2TWEg4_gJWs1FkICh
hS?!t94aGVmJgbRVJu2hLqcX1fR)P3aHJG#u)LBK@Iuf8jJ9HfDCj_fYF1E%Gn(j<)kT*=g{L%>0%lqn=uV7q8;Bg60@7vpAJe&1
Sw^z0_!$J$_@a}rE0C~E9>D-)fk?_ot4F)sC;GsmzBm{dQev$v3vn2Thp8hWR@QdF3ZP{o>jB4ugA(YYfWZ$)XJ}E<p(OHrj|l~d
f=FfqDgwp@<03#L$d)NXW;P5HYhEM`VXMI0q0PfkD8(C7n6Ud`bTf_MQ3fl$8v}{Nxjot{u#em%hAf~}gWCx$7LjmA6f4-CAk|zh
i6&xZgai;VV#jQ`mT3?~a33?5RK-v=pbrMKAsQo(;Ikq|BC%K)OEe%8BB~`u{2>ZysIXANwIece%bYNGiMAJ`u8}4!VI?sMYK;Jj
eCSu;7o-Rc<Wh0@1cNyRXaw@JCNsd~ti6D0r@a7jqm9duEYpY7o{%@9*rBHZU`*<CQU<rBN(KO9UjaCib2@iI-UdQt=b%tv_rf9o
X*$f2Q?9_E72gOF6D$fPC59fhU+NB021e1HrZ^Oka2g|+F_T*~^qA9w%x1#Yg$Icx0R(Wg-AY!}VD*udPe4#$ISFkZSYIi(3wxy*
3gX9OQjK{dW&>g{GyDx^Vng<j3M#ETaK&=+#Oh@6NknnwOIjH%Jw{_aTg-qtDdeFP9R`VsN5TT$37G<+cC?0?Bz0)kNT{4@58{L_
RZ6XdJE=z1!GBc9uxnHL&mrU7U`v*gNH`k$30o6M#1vK&r76roSTSkLsv?M+KrAep<}ByZ&>G|j>vbR=9j3b^apW`M<+H57qyE*<
9@G^UXIKINB?V>!EwCoc5xwOy0ico0ke7m;kV%h}*r$4PnC4HR#~Ef8XM<@fP<6rx0E{{iT|)L_Ef|CrSPi=>$qaaDKp-u0I=A2j
kE!*9MNv#yLo4YPfo@noBa3%f5d@hI%wkBc5_41HDr>N+iYygq0*$#aZXV;R*c?m<>73NI95gFa;HiYlA%B>sN?9es#Cb%YMRhd`
WtfeGBS!g7cB4BIGj_|=2@8QVLJLSi>d@8D!Lb<NupJn+pzjf|)FV-iNz6eFVfP$*jvk%Ym<i4piU17drFA|(CMD4<m3%rxKa_z)
a3CMJQL(L-BWXfhg$&oRhzi?Ai-Beu*cVV3^|6?_V4}`dPJ|Hx7mQ{LGow;A#oUvW!D0WI(If-Y4j=;)yD;fICM9V%YUa*k$`70_
TE{RyMuF%{+8?YAQp4))!l5oGVZ1<c?IDx5G_}FKtnk5tQk$^_^Knr$gh4(Wf!V+m_7Pc&)s3psAp*%}z8JT3NfQq5(dLR-7DR)_
R=2@Z0>~IG5=FquC&LUEomQyp2*X&vk%etgWMCOa#PNq-l7zWKg2YN5X$Y?3X0cjO$^$^qtOfyPQ1AlJaKE$+E>>AeKf_^qJ*A_Q
Ft!hvXsst&&IpG9+rhM)ONZIe$&JC35HAjOG#$WHUCbjU@vuPn1mai$<4l3W(j(VnX;4{MhR9gh7UX<TmnU90T{$u0oud@&2>Nlw
vxbZV^@7GJ)oEza&<2;pjH5wl_)Id#DiT;V5wY4JVknn|ZV5fJNJ<CA;SW^@9<kbx31SwrN)=v8N)=-O(<Q7eP+kjSR%)@fhmg^q
2|TgE5+`9%04tH~+NoE;&syZ_lk*Hgp?HE31WOsuW2=h9XLq&8m0laAbxIEtt|(Uo8sv7SlFy{5B!Pr9NV&5TzlR40HEyE-q-x0V
AQeB2UI6BR9T$rbC2bm(K&i@%nPtQzG4urWV=9hIC}~P;uP1SO##2C;8cKk^lrm39Sjn%`j*nRkkZ8m}YUF60rd&D%A@J=}_&6|o
U3wWT2hrSN$`m7Oepn|UrKJ?sam0EFnlCJs^wp$+UZn{vMUC{q4Gm?MUsBb%Vu!g66SEdrm>AX`h$`alz%PW*2BKmL9JRMS(4*AN
S}_ZgpL&=%7?}59P-C?E67oG|c^1oi(3Djr5OKt^19Z^Wf&MT`PP~BVWwM`C64CZ19wKJXsVg9st;OP}TK*hUKHxqJTR<qGRPM1D
k%CP#R}_*7tB*V>TBBDhwHgjf$O1|g-^x%%pNRcXwR_-8sF2QELeC4EqlCgbD3?(O<4YVQ2&A^wXZ*y7e)SmK&_yvpn}$;7N|6Vj
6R4!W05t=W!mLT+TLPeWLxzyj5Qd9@I@Xkc!o(0|idy_(T2>;Jq<lFb$FR_X;sO$e<qq^pt;mH9#n4$Sx>{;Ve0pef+rjEEJB?O^
L0Xa^nSz&+7IHR36iC9M)dB8c<W5a$Rz!$FrGc1`aHBV~9RW8OUVb37Ds^j+XS4^njd0>Z`T`_Itd|9@ATc#s82h6o$N+X4)8&l<
TIo`FzyfF1B#RDX33Eh##F!8P;6;|)0{tvBXHj(MYk(mo9GI4gTnb=F2oB=_L@K@nn{Ul;`Zyjbkei4F;1?K&c`hn(2uzqEM$8ss
jXtAG*=dZJxGdN)QftLnmGXW>E7p+6VkcF(3_^fI?lAxe3JJxDVgV#gZeMC8VybbfR%R(cHjHi=b$M9m5wn^gB!RNDAe9I*&GeAI
qu@NzFo+mCz#!J`OF#>p59<>`0z^##E{wzgRlpj1hK7vrzRPGED2~1&?bbxgh$$5q5GOSO%~U`vZ)CYS?|M}D>gvVR9|;Q~VV}9Q
Dp<0>TvN=@ikRKDNQF`Ll=X`tV_mFuVv!(Yy5eX8XkXoC5GgA;`9=Xjb?IVB!r!Hq_F*(=`joaoKph0dLNszZYFJuADZ`u^+Mut<
a(xJCppJDPJ{>k1Y7r~?STrgD2>O?_+nF$8=oKvH#k3b#p_Z_cSI7(oEA0>5VwJB(Q9zeM@F|0)#F3~sR#HMg&`o8@5~V8ZvZd;a
qCzWel0;2MR*dlxYf)&?Mq+nT+DOocHH4C4U_R1gD2t3h-%=7Hj1Jo6LeaCfp7M(N%x6F(5O0;Qdjxbrv`&t1Pq2Vf;#Vo_yP$iR
AQq!EU~o%Y(gsR6Lnvw`GV%tB$IwhfZNWE6H01+n1KkL$GK}QG$AX|%qYG@qIG8oa4Qm+rUP)v^(jsg!v3^-I1TYv$l^CDTxHHR9
DbXM@;CZnAk%co9!wfm6f<*}!xirvOBOmx$)fqFD7xC2$)(3i;*XR2z;G{@O7QiDUH&!{LXBtS+u%u?#4koK7)nvvKg_yFi5CW2d
6ynmCm;<Z1S+CCRW%QXYCxja<NHDNZN#UzG4hCac7`%82kbsmb)#DE1kt7eucCRVz=_KYpQ{U4o(5dTt@YgWm?ll!UMzn+6cWntx
w;abvK(<%p(=9k@DuX)pF<#Wv`*g}*wDiYF*?gyr$dlSEN8?gjK4f&jwmeBnN{lF6COa64a%~X|7gHDTG<7tcDi|puQdJep7)><~
#k5!(ykM+II!L*Xohy->7Gz3Art5^=(4E<+IIXV}TT|o9wcc;blR8yRG$7#<iucE*yS{D~p`=SAkn#s}a>9zTMf`uN-BUrBR?<ip
eW%HjvGj=y7V@dsypBZq<cSQH+C7&t8%;HHsib(*mKhl>T53zLh(9dKgl*}R;!I%;EF@a_V)2y9YQ>viclwsDXR*m`^liP4bT@77
l%}JkXiK*`)sb{bok}XLgfYV9Qj(wEsG8E6C+#Vl?%6FR=eoWHm00op8lp}SSz89@2{4KbPxsMFoAS0u>(EFsLXc8X<!HJJP!e@Q
dfX|mo=A(GVv9E;g-Lb?s6X7A@aXLNO|cQ$)qClZIO<)Nowf@zQBzq(1Zgd%B?T|7d0U21QV`U+77*E+w4Obv`*YC*GwBzYiSV#x
f6{;+w>0XOo_We<_H7ucep2$Wp!>GGjA2||y1XM2T8irw7fI!kg(<dZv&3M6s3|p){k8Q%Iw+?jVmYW*0!h)H<)=hBTxwZjS688;
%K{bJvNmOd#DXhCZ41++kN!v$ae;65-1jV{1;+AVXc6z%Tf#{>w4jbp$l`ub^LnUdJ+VaMZ2=rtT!Sfl)$}0V0?Te%zo*6{*B_=9
N`c?htx|<jXejmUnghES772P<prXPhP&P<XyQi{sp~bS+Q|cN61z3R;W;b>vo+U2dZjyk~7IdmO;)5`@FvhMfIILNTx}yO&td}DA
ifwgcsQp7*?*%WoUT|R7XzKof-DIJd(EcFopk4_w$qeM?$d)y_{J&e56&b0~i7cO}@F%pc7RX7d7%lI*vuleNrR+*y=!+>x389@@
MvZJaP-G{Avu8+0D&PpUXQ!hjL>x=^K;E;|nl>qZWJ9|OV@rz!SoV&z@=R(-1S-D5r`34G0L6`%4J7QumfVpGZ6%xFFRtlI$`?D}
xwh1dG!fg%II)KuHSDPzB1N%OFzK5w`tqUHRS_&ATS!U@XIw4K;$^JWV!jmqnJ8=uO;!Ff_8r-^2>WqrW7kW;6ovH+u6-hJ?rL#X
r^ZmKxG-p<l~h6sM$^p#g@&1EU>Q3OS4sIO<^6$Ov8^K`Dm+_#Mzrg@0<1x`1S*ls*mjOQLA;7Isg%?xp>S$wsTdSyq-Ifzx{|st
=|9vWPbqEWP)+%w5@e_ZDOyk3NA+d~mb1cI`glzhEN6~uG6%V78L3n{%0RK$T$(j8fd#aYVxgtSPQ9(*&@PfxWD9P^ovP)z)-Ec$
2z50UKp-rluYjda-0(px>|$##o5I#W`8w(q;7RSF?xPf;TF0|3{*=m2RYWqEE#_-$8WZ0xI<ULOAG)`~zdEDdO)al=stUO@nisOX
wkXsU+VSf>5Z12gncEgAYjV_jYlXgQe)np`NJ(r>MI_=N?iVX+Eu@0q)Qd{PKnY7KC2a#K#ncdVTLanFw~FM56h)y_-TGF>Q5O1I
!D*{mV-;|M4=saK?v)x%%cC-f@*iU<k(Eh`Ok-h^)}9s8b}>=SW}yPp6sx+zVyexXy46_VvsIFTl4Ol0vU3vF*Rj%)uViC$`;KsZ
yjS(g3eI{MWm7+G%0RU%m06-7v~{(e%GXX6t1A<V1n?zdV{4-&8(OciQ>M(_Qvx?CkE5oJ*9308oXD0X`yy-Vic?W4Ql}b;;!r}8
4xy4{zi3t-^b2*HDq_+i@nC|QNNo+OFVm}m->spoOK`PZRmE)}yWn}fBHXqXxG87V5?PgjT3@Wp(U$W{t*~v-mW6YjVQsy)#kHLx
Y*$z<vh~wOv}kN;&lPneCA7bO=lk%{gD(}&cFJcHRuiVKVa|dtw0JC(OM)<wj0ID^0ZT6UPFJeQoRBa5FdIt?JoVCuul@3sMkYx4
Dp4AxKFe&hu$*~Krb<((^GSS{DN4Q@%GV)179yq$GxC*YaU@u+Ag}iEE!&8NMhU-y!7ma>QLTJ|gK-wwTIOt6vg3PFOTsV+D=QhU
A;GiolLfiHMx=cfJ(-wwr*t7%w-Tp;$KW8LVZ|9U#tCCoYHdXF<&QvWfoM-AEPasAPb88%OIRn$xQ@sNsVj&iR|(VB<5wEclsOQ3
<EhJVS`d1HEq?<FnS=>}ELOz3sdSK}8>?@_1S<y~Tvx65$d6d095Ww5u@-o&x#X+5R1}PPrF<0-+oA6SvxCbpDV=tfN3a6OWwj~a
U`ag8%r{p<^*H!J35N3{kA(tEdz#qg`*!k~0~RmyeP@RB1N#bj$_i?}>nBw(Myh5>O+G(zg7yg`%dCSC#$+jH%-T+=G-aSK#{UAo
Ywa-I;jyF(^kd&8@}#57`T^fLN_?NMDf*0~F~%r`nk<d*)w5)+9qG<vjU5vqE??3N0|UyH7ykl4!}mP{`&PNjG&Rh4W+}nNZW?ii
`9h<V=rXr1@9jpR7CK?mUEhuUlrIn;@%>0<Fn}O_p(0{v+G7qn(aej-L@(pN95rO2pwA*gCK>pKMC`H>SQe`}dDc~Um@)As<G@$?
nQLX3JC#@Ruy167P>YHf8g^Ol?J{hC#6Y0WxFAbAB4#xssafWm@$#t_);#f3A1OcK!9+}o8A!u{e3iv#<rM27JWoF*;K`fwLJ5?;
OsW$ekM#!t2vWfnVsn{P*4VcsiCN`nB-6!cC(CL>Ps&;_L(C5lfRZ(G2a@*^ek;KxKpqRWAwWW=GWhZZv-7NtN2f?*;fCK-@mN|V
@7cyuqQ-JJ`63W@$}scj)>RIq#)RQ?exiU`BA;P<(i@A5rP7!b6>v*MGO+3)@L7Jq5&=hE&vf}#D}&8|h@T^1U0>>Y_8n-}G*DW^
@=+pIddM5fM0>=7zA%tC4FVh9W|Y_S1Ac#lAL(J81Z!F)<sn~vfKAD?A7rOZ?=#1e%BOmKri59{!b(%VZV8AeMnPf})uLlr1kFln
Fbr!H_%=K%av0Q?uSGD=&)RO*)@bQ7t4t_ArTkQib6NWBOCC6p_qth=&Nws6MkNYd>y~c(*L5UGs|wc@g&Xii9#`X6j0t=8vW@XF
n(Orgr%-Q^-V7ujXN`3GN}6%JwhM2%P2|pNUl@&aB8G+a6&gN{?Td8wMKvQ~W3L`RvQa(WQt+gyahsP2m1G@#?Fr;6h2jcQq@dG2
N$lu>JP*~Mt7m7eunr!{;4(R1kg`!RUmwD})DEy9ojQ!i7@)3@mR%hL@SG;L5!>fPirQNgIo8h;Pf9N%0n!En#N4v*1`3eajkU|^
D_S^;lQwRsz8#~klYJYKy=${GRQOW4X~FaCyJm@C!`kn)&BRfaV3OumXtz;JAhCslJrgStP&~1A_CE%!-#?b`?DEUQyY;&L5O1+Q
pDkAMmD&1Ryz@;iA3|>0Jh3+h`F8MA^Nr%|_14i36%Wqy-I-H=*z`-^Dn_4s+iEvmtaj7${KIs++f2*F>0-AXx}!I%-v`-X=sE-b
&wgY#FUw)>3}&O_`unf?Wy1VqF}XX#Kkeu7Hu>tb8u}yKb9*`aY|o=F_bhUL`_LKW`+c{EAEeg@`4FOQUaoh06KyZgWtzh;PE%~w
+pX;>pU<qjqpx9KZ*r95A6$VEv_<_Nd*5XXSKHob;cCw#JDNMG;jI*2XHc{t+eIi$@@Uk2IaxmIc(GnypRQNKr_Nwe0yocVpx<HB
u$RMnb<W^jb)7Bq^I4e>-X0I~*>?E+<n2U12n)bIR9kd8dE0)-u<puFAHN-ZlMUWYv@K>rQ~MQ4nYJ_b;&?E83Iv~UL@aOO4BDS&
(o87dYQ`GdMYovx;0&&v!ADH;^dy%7X7X<_Y1`DhGQ4hPI{MIDjt++(n<?x2oV~vt{LfK6!d}Z}guRjN5X&`qYeAF&v=a*$aks7h
aQJ;-qHw6_S+0S9UY;EDvzzQV>aMq;Mf5%HL-_t|v8?2i#Tarlc#sV|{pKoBhg;CT6PfNr240K?-(~~%_~tVCed3Gt#c&S;yq#b0
<KDxCeN<dyRm-(}A@uIqLjGDJX+NM`TnjM1eV}_tY&`8TS8;uE>`!XCQLcPm6EtPPjQs3~SSWZo!UB5m7uWYT)m63GRyF8vF%9nW
qvRik=L>;l)MHi5`u2Eomy^Gp^chCKg9>(e<P0u0>x=a^UvArvh2uX@xe665=lR7DLJ=+Pr&cexrl);uJQ_S0xUwh23*_kVDOzWl
{CsKwyIAHcVK6=)wZyUj<`%%gLcR<=?8<%1x;hF_q>R|W%n$4mZ23ZKd%H_k?XF-`l#dq5NQ*8fJtsatzaecyO#hq<`+bkR_~p{Y
>auF@o?%G4)p=)tE5Z%zo*mhT7q_6*&P3tG_O}u=x^fCt2}g!<&lwz@^&8c*9bL8G59YnSc|bsRo*UELT$tVS7Ptpgiw8VyV1Bt=
4$8%Owc29)^5sF>t6W?yATC8D@6PU>7Ul4eOX#3R3FICXtJ2=p{rh#d2KwityTh~QzSGF=mMwJ{Va;Hl@>E{i7W(js$gh?hpS$vr
WogpEg+=#sm(1+&uir(YsDqP*611bcS*<S5D}MVK#M@!~3*n5jPVXnR`1zbds~1`D>-g<D{?z#(tT5Y?uEhCddpvdquhIU`Pks43
2Z-9Mh4D$3ZO9Lbf|EHE*Kv2Pq8!0i{q7Jzdz6za-%${WT*k%l?Oih({7)@CCwm?2N4odrW3Bq~iDgP^LDh(ql_0-9aJdEU<KhCd
$i&8qLNnQi@-fXm$j1C~xf}MrEv*I+#m>oORPWG`sM81SIIr*Nm(hoq4*F4Md~5&QHMc3;eG3EZYjJX9ZXs#i_|XxsACK<x&l8~{
uh%qRE=5*e=`%eq1ORdQyu<H{^IBE#4X7F(dwdU!eaZ6zYEa6zc~PxIEB*=VMkIJkZwlV0mcHs8c-)o5^%&Sk;qlq%wudu)Sc}YU
Rl$tkt;=<-IItZ$A1x7Wqy_>Tb>^d8!dv?qAB?z=qfx}xs8)OQz*_>rVsG1IEW6JwxUksSqrYXmLwplnyLI~fAA^U3=4;`_a=ooe
`}+frU_skUIekSA2LP#G&_h|QP6zy;`A+m5k7+rBn7vnz_)qyv|Mj5Ci!+`Mv%^@+#p<2xJ_YhoM<8S28xCDiYj%z_Szh03ch3&e
Y-|^)t75_S*-0%OL^!BWac+tfV!Iu#xSrflBl+rjNW1@VwH<wvx%yS`t$qx=V+hm}JARk(xX$d)Pkr{c;&5+YTR`mI7uUx(b(^>i
Sz}pgkI^`HX1ICsj&h7*>>b3||J*Lb2vS$1<c?77$ddec|M{%@ylW`z@$_z#Wu6|RLFi?eJubECdQ}w=UzrR$Ce>yqE1r8n4|~Xd
qb|(1@(%y=F}sa>EGj=XSghweZmwh{A9d=QVL0u{$H`IC=;lIO$OUu(R2%*344#3RVPyQ?7co>YfZ=rq@{(2;?aw`@sWacNgS%+c
{^r;O`I%#lsnSvB9{+EL8QF36r1P(>`uPvW2@ZeNAOEE}KwYIn{)cKG%eckX`xPeUv*K&l_g?|*zp}pn_SaXd(Y|8*wb);FQLnqW
W#R4kBRj$V!V5~c{~R9rhrf!bc_ugP3SK#bR~YSQ{11P=$N$R4P2B&#wbA;A{}3PlOZG}_1NZC-UEiK{F}g)l|FuE!Ia~U{4O{wE
ZAHwx%B5QNyWKSPUzImH?&;p++n4)a=%;#>Z*3IfbBlc2j@Cpw7N7M;Zov5Sz6;$h?Mq(F&*gqU!lI^^GpIxnSbOYoeRxcF<HZ{8
?_&G#2kU}W7^&-LVDyWbeWrv^(Rb3Hvq``8aPH8ef6MU2sWW&7OAY1~K<oJi&$|>jQ6ItnJl&(mt=oErH8I|{O&u7vrtZ?|^RDT$
ls@nJefAmZZYI&cD{`sZ+ImC928M$C*_!SMD+W-{ox$q71(;4|4aoE6hg{!~K&#c^`T5c6{15~5WYI%s@EwLc;?(~+{Ne6J-ah+i
rIJddA1Hj(?w8*Wxi{UJmKSHah3=!GLmLwA=S{cOxj@+MIjeTJcI2X;@Ad3;wERU-zH<}+M@H-J*KV^YcJy_-(%=Sy>Sh^tfjlLG
6r@>Sf>i3j3P|9A#GX6+sQvdi>ie3ZP6*fJs|3yW<*l9TNGv8Bc5Oi(pQI+zR8C^aG*IIVe#tssi!*qfspH}do@DB~bV9<~YO15b
?BZEMncj2;y>qg%C!KE1v2ok%WVzUa$yK*jU5PR3#-3Y-u!i+i8PxXg#$oh9x3iu!gQfug)kwXypY7l8d(-fkJKL_T8`c-!m%XOl
(~7c_C%vfQEAaG<GnTTSyS+O{DrHcyoY;;<-77!aj^!SRbw9NH><N6?-tW#3dX`iM3LO44gn<?vK7uJQ>TWDg)a#wpmz`+yD`(&Z
Y#-Q=q6ngAlfAx$Jw~h34d&J1qtAA_^>{!%8*otnb6b1(73*_)8tYB=pTkGDw2)K0stu@oy(!u9R;u}Lcko*eNwl4Iqt=jrJ&|-q
@9-c>gwF9n)<EhWawkViGG~=<PU+R(Jl_sD{QRMhb&LFc);Vi(^R;J9+TeNC0OCz3mLvvjZ;c*!8l63`xj#M5P5a6!7}LLTwp(Kp
u6AtT)aMmCe{tAbuj7F|Y3sn*@F2el|2)<|PxMc7Sk|UKo|0EzIFV8hak}NC((XyFPrFBjb`LXEDiZho{>9n#c2R8gXw&0?fApy9
@5B44w$MRmi#d;ulM}nns&bQq!m1A!%SEx+4KAt;r&$!2%Y4J|_uER-qmCY2Nju>Px64Z?8Fl=R#PKiI)qIX2$RF_gKXZueV7*#i
-y1xY17rXF>cw;BQ3p>4!+ISc>x(5Lt(@)A1GjTp?B7b){_VUkBgXaP)1v%R9=DSM?jBY9mkC~GM=q9^%zDn6b67PT_~GugrdFNn
+6iDI+X;f>_FhL{>~*<hWMIF~;r3<{cLBF})0=>1+=s(24G)&t>vL=7_O@K@7qhd~hH`SnsK(4Gn!#%jby_}Q%KY)m7uitGdaX0&
Ht+OE4EU$nUWREe!Bijf2Ey9UEM-}fSNg}`bKIsUD0g{o3_p@FFq;nG;m4=T^(<d5uj_M!tCDfB9nYvWlkNey8m9Fen~JKB!_^fl
4Ll`EpAuhAedC?IG5RJWI*yw><Gay#28rD{Ah(Y3_%~<Wo3pzQ^+Y?SYaRY&de&)gd$-+w*WP2y?eBoaObT(iSwKnJFgeJO{z`pf
syL8VwY}S`Dv(t7dP9j*l{NKnJ*%vb!Wlu!JFph^#%O$%DV?qCvl<+S%p`%Dz#8hc|DjmdF!(oemT+6h;1u8vi3)<gL_=Ayxc{34
RCNRH;UBuFKW;=N8IGL%<%Y?VT`$^r#R(?$L8)?jB_~x?FK}e@@!!XdbX(N2V%6VhHhAD3W6CCqFtU&_h==<<(CXS88&}o%2LO`P
VGSbhUOHleors)qgzcSS;pC&qaZ}&(+1v^`GquvqtjI0hqx1DuB~d_3I2!AA%=@S!`13jnsXZEeQg`!MOc-ktKxn|}ojz+V726Js
VEO@J27T>Auu9$KFSew?c+K&f7VSOyf2V7ewTV$k@9G{E8||+l?@J5oqsV6T_M)MeuVA6GhK1zD_%xF|EY##^%=#6phVI`#ZS~Mf
6RxLDO*ClO$&mJ_nso#x^%NJQqqExtdJ_-IGL`I&OZu&_s12K7nn`x@PI=4u&=3Bp2Mb_6U=Z$&7_I&E?%4WO6HyZn2R5xL)WJ+j
zLN9ct4^w=D#h}`T-!y7Kf7($D3fvT)$FcV;JkJhaLGW=cu~S}YS%E{UKT~4nQmq`%B|yBvaGWGjT|rSwpES|ObMd@e0N-<S_z=K
NrfG0j5#z>qOM(yS^G#NAx4$M+by-jbgXytmZ973GGN0X+)ebvW<uc0X7ksBWuLh^k%%^p@c_Dr*uwbPOp(zIAhr#^tsBlJS>BQO
Vk6)_M)Eak0vRGVG^xPLe%2%>wzbK)xXv*1c$Qfh_*~N?vv0EexO<TFtj!{!Tg~9JQQdhq*@LRMwpNQyC8Sw*!?QO^mP)aIexk@z
!nM)w{ouDWRD$Wyl#NgC<-41Kzm(~o?Mq`!Y7I&z8Gp#PyCa)Fo98P>md{kA_}ZN(gG=T#XV>y@jej<3_N_Pfthi$!@`Q<Un@oGB
|1wX0n;vCK+!H0MF`=5t|I9ndK3Se(qON}!=jGe%&-}PeRp<RwwT&}Fb!`N<4VJn}qO*e=Nx+e)Ha4Z6Wt(0?ol~~SZTZ#BW`8E1
-%PA|eZ9m~Z!|q^^LT$;R+m-Q&wMLw$`b`Plj}BR2j0nhsqQAZo!b#R32i{$q_R7CY-OA_i~WzmvnpR5t>;G)v4iTJSDR{8RE`Zt
F0X6xxjTcDy^(>27`Oth)H&>;2^)^T>ll_7wN<Ig<2I{u{O{~Ur4kLm3kM^OobUECY`<pi_?hV9TNJ3Et<1U>^}lII{+qJ*-^_Z|
N~?U}j(@$Il^9Fh#Ajl4%BB3%bQ@_urxez)VKRouqQfB|JbW}_oQw;v!&|!OpN8KFD@c>OKMkMp7vo)e=XR@FxX%utQymt{7QzO0
2DbdI_O^Z+esJt?qEq|jXXD>%oC2S9_qM@r#OPIl^|+()dGQr!{hj#vooM}iAFWpf@OnSuc!J9FVh^`X-;s89%KKh0>d+}5%5?c^
PvED8>=mTw_|<#<`?LHbm*2}ja@j<9w&EZBwYU{M-((qKQT;S*Zuk?RR%P;fr;DkPC`(#7!?UAWXE*2_-LG%0tp9S=8c|)-?l+?E
w~lGYY4nCw$6wL|6Dtu!?b0FG&qlWC0a3)S-uIvHiO^$J3{P!c#*tW6r`4*`fFa9Sr~-DR*40i6PPUf}J5^)IB-S+?U99254R+Ob
H-MrL)2e4f%Es@nT~{jWRH@Z0thOt^b&s2DWZqd?^Bk-D`F*cNM;UB734|L;L1~~i(ORH-CfazH9d#B^jqWeSuFYC%CN)&f4noY*
(?*mE<hoGRs=aI4yM;CMK`1L&D}|l1fa6v3Q&Bt+8(Pv*_PKVtU?;S^Ule0zt9lP<tn0Im(!0nkKMLi_h$AKAl_UACQL|rggw4@T
+c-@wteb5Dy>$~)Hnr5xNRjHke}A*pMGdS)=lEjQB6v2jMzI8Jsdsvw^}<;=DmFK2z-b(`&%|xlCK;{lCv7bc{>~(Az3=b1?~<fd
2pcJKH<Ki5mhGijFJ{hRJB{?}X4O8QOY5i7G?Uhv42~w$?2j*{()yV+`Pcb7Ika}JiSrj3w09jXMf^gW^|NL+X;$aVI+?Qf_M!dz
{d+v_XUF8veunI}1le9%teX{k@9ZVT><!!Yz4JFRVOyt@`qE1XjT@;hK?oz8Xy(YHkv418ey>HV44m7uSiRQg1=`)7V8Yd?mrKgB
ekSQF(n#Y?c3bXf{Qs6V8h>TR=sV3AjlY;I`oG8&jeAL=@BVj_L^l`ZTNC}W*!OQq;<ZL!6S8{uO?GhW)*l?#6@%i#Zz!XN?;QSe
_@fq7T=T;pewhCA#j|HGo==}Vef-0tSJTHo{rvEU15IyL+akZHx*4s<5=(!7wq908#d3XF4&E<zV0`hpfX=PhUDb!P{BkP=L}Cq8
9}4IX=6gWX+so~}ug?yBDaX^z?>InX{gR8mF!nX+5`7`>>oPd?J97W4DHdwit&{Hoa_hT&`ugG5<*Me(^?EZE!l4(C8Tatec<ll{
z|pv8jo$U<{(ZgCNsrek)?FX|?o=Nxq-JxvfhpR&c=IDI>vK>w96?^n!>s!P!otb>7WVI>y%M(UWT+ddFXX`5aNdsWy9cxVzEZIE
P1Y?}yK>%UwZ-Rj-p%{tc=!iv^pF0ayzAG~T+uST^__&PZ(UtQTdg+!vA#Ysy&{`!wKqo7@a?F^N`2?*zAh5W8+TrR_?=~7{Acu_
e%>p-RD@=I?Az2gSY!{^{ea4kz4|#ehq-;DAo#}<K4FYz@=bPR_Ez*Z>pZUke_Mwd_+-p~+I8P3eX4s4Y=mAqG<e~U<|RW3(OJax
E0X>^fTp2-JUIT*IgoJ<j^&SYAmbez%OB?eLrgc-G8Z`woE{ugfAgip8;_>SCZ;mp!Eu*m(E3x&0XAP)kp3>nvG&EeOm*e>QKs4w
Mth^We*)(pbZvlxh5$S6`4xP~qoNLfywfC0OYEEVd+P$>s#{0=B*W-ED-W|jug67Wn!3H7X#Y8j?x23P;`bgY!B61hTC_ZOzBoje
&gdu0eRYzh)^gQxT+SZ2<KOGurx-N%&*%?ZqQ1<m$oY*^-Z1-Um0WDIMl3ZiV$E-RAz^M8-!(7~n)hO>dGkiWXQBa5ZoIeZy!}G>
b^iIdD?0AQU7G^m?c!90XZ6RP<a}$vZ>{%(Nw*?4qs07;5=2}SdZWZPf6y1zf>?M_A2aF@xlM%coL*(++&Rsv`3a_jJL;Tg&rjwP
=lRL$Wc)r;-G{rQF_c5b5n)NU60BN1aQA97rIGggh<<2&AI;PgZ6B?ikM*ODB)`SI9B-*0{&?Vyj)s4H>vr<9SB*S!o6u*cR9Dd2
xR_X-bGY3CNj*KlcP=n?XHab8AKhM)zC6Yrk^8!?$HC-g?Ic+RzURfIbFp6Lo9triSfB88HC=DYYLj7GVK8I0_*d48zg#hl&Zg-$
lYgC?b=;S$#UCJwpQpuHRlKXp>~>~xnDkn#7OT_gt8UXiLv&hw-?Xa!80{6S?K>E^mZ}~6>u1lKzKqqD-*Yqa&o-~i#cuc|`{MV1
qn>TtpW0f%cK$CFsNLG->m89FUp{>X8=TIC5{gJQ`|QOJ4`1pdQcmZ|<46B`{7Rm*^wE8+C2+9!pFDo}`sbIAr%ztIeEjP5tLek%
kEZNAef9KT&tFY{eE8~BZU0NzAf(8$x`H`#(-Eli=|`-c8PpByH+U9Ti`}(21blk2-imf$?F~>ka32k3`G#d@k3o>vb%pPdyy13V
29&~%t=6(JQL7n)F%!1!i->R6um-fqXL<c*_5Q3{Nx%_U-mqd0`>kHcdBr#9_=tnw8@xWd+}hNY00c+s;!H~0n!)(Ac^ye!&|9x)
Wz<1UdCj>-Lc4y5c}<Mvm~?x_{OO15|Er=nC8W9q<Rh(M2hxR-+UeLNwK>vkR%49(mEAG!m>eH#*S>3aeB8^pcgt?o$f1P$vej|b
+8kGZ%i@473JZufLJbj>gA4;>;VTB>*0)6y^II%|CVAS?-g9Rzx_jPcPQPAxS1>4<!<~chS`h3k9MYyoZm4OxE6l7g%7_aya$3b*
s^Tu0R}$fKLwn=Fm{W^-%JjX4k0XIXZ|%@+w%9c8!50zpG2^Ib43Wyj&w1s@za#rcLcEgc%cwB5)#(J2ew&@)LMAxvJ0DLh^yirj
eR$~I7+vd_B!MVlAR<H7)x$n)l}Q_`yt#KWi>|h@DkV?^wJVI#hiP0VmnGQ>PLi<YWK2=j!`7ZPt}}pAq(_rHzj9m$#877zD%%aK
XtK*UdKhbek)7$nz{NanD-ZxTwi+((v0i2TqnDHMBGao*f!o4PEmFaGw^)^qtyrlMDD$^9YG{$c`&B$hju`Dn<8IN0n1rBTEo-r+
&%E>67-jxx`<s0(ovTb%Gaotf_q0w8TxQu-uO?*4Fm(w%U#Iv_(0StYzN=#qPO4w@YW-xL4>J3hqtt03ebRl<tK`tgHI`aC1w9+C
UgZ<*d8^|fqkWf|qwXB{Wm<V8>dx-7n1P+{nH{(rwayxl92s%C{o|54O(M?SIYz|R-gB82sIL84`)mpz<oS0PG~aYw+^p;2eplx+
Ku$76w$y#xUT&@yS2Uddw6u9!XaSt`Y1}KtvAsrFX8IKnM9N5v<~qE}7@27*eeH9}ee7>aC-eKK3WZs($-$(PBjiAzvdlK@COB@4
`)MyJb6)Mv)@62}mBfE#sE8eL;9TGi_7BW8?eBB@4t9%{(Zo?JWGaHj(mk)cWIsFpi7UKqPq9?Tei}$j+>s;TO(AIjY(p8n?17b8
BXubDTAqkcB)JVMU`5ZV0INkuM~;mqwav&n5&+e)%x@Zw`t}U1K22-Dn%b-{PtOM8{0w&Q*G~5n23x27T7uYev~CAQwOqpY5d#yF
a(21h4b)(+?WW>#Ryl*qEsOSgA2}GXo)iAi=29#>`%!_Sy7&L*y@g`ETvq*|{z+=DHea;!#1|Gzj}~7Cp|@FnEMd$WtFI}lzq)Cy
wK1t%jkd2b82=(hwHS58L#GPIz6~&b2{LmhhrTqLc8gjXP1}CL;l`IzB;m>Lq^KOf%1)j(kVrxDoblZ`EvvbFe+5e~Gqoe}KqC#z
b~#KxVPV^>e(PNtNFq$1)g?drc>r2OrL(nBk{bm%$8C^i*}MM|;GHZd80v7y0?WfKe=#lbp1<DXm-KqCp#~2Bi!B+Fm+Hpt>!QP7
RA_4AvDHuZ6}fY#|6<*_z9T1HZsaIMb8X2GWc#0n7EFFOnPY^bn@gG8T=m43GF2))bUYpD=$Av%2>!7P{5xa)WAKA~ykw^zG|>v(
s+J1pWcFEAyJ`ceDp^oO42tVw*;MD&PQq;&aT_h`d^=>1;v^MN2ao3cy482ty#6)_2*=rFbNwpFyz^0z`Dk+EGauXTXFhf}KLfJs
KHrY^Y7gaO7<El+{Y8+E%@;vF-uxoSxKlg$g>QiDfBoaeM?bpX`skMse&!1w&DU^l)DYHR^r!=@|1XZ&SH)C^QU&r>7;8yAvXP`z
UM^T<J3fQh%dA`mwxHagCFFB>wfPQRyjK@A?-vAN^o*^>H-fJ-H|qpn$1_t0W8Z2e3-lHvnKM_U%aJ$%&Tz)R-69rHTCa#DtG^if
1vj`ZZyAkiUvo#O810;8HvTTMkoUxW<a>dcg+m{ejKM3E4K|^m&`zab9i?uP)lU7mzpFCBs9!?;4Rk^;9BW8zv-))$2>3AzaHODy
S}C7xJ2UI+E1UEB1Em?i<~bYP=RMuqdf3gV`ShahZS&bcrb52edl3A`cISs1M~h*^1lNzykVa|;lpv2F&COVeX)l`0$6}&x^SKm?
4F#IfeXo(@cpw3Co4mRa&1?gJCryH@sgw9j{^MId`)#DSV`lA8Z;Urp$Ahh-5beh3@Qok%_FK0n@NR@DPP0x-qF&MI1DEsEm^i)P
-7_1p=vvl~vPaIZ*{{wswK<-R9Mv0EHBFlw^fr6B_XuXz`FhoRXS-HdQeV?+y`@HiX8h18c-^euPr6w!?J#NTZoYbeTKj2z6fCMW
kT9hUI_1t^ZpHBuLSW?=v5X7dD3YPWaN<-;B&PaNup7NeG9!>BS$%anwLO+geK)=#VF?}a(oE_rz5ob~QP-A<S)CowG_G~#_Q2Vz
W2sXS7tB6f%<vD5L@8aHy1ief&P#N}kcb3j4M#E?WS%wLqx0-fbiT*PZR3nU5glK3tw<|j*{6}QpVY@V&sU3ih5PMU8MAe{sJ3tJ
9OL?z?~Uv7yi5K0y&RY!2TTG5Z|=O3-|`LdxcxpgpZv@xF0X!h{Djv$FURBQKm1<)n>*^E@`2|VhhIFtv%cKXqF`vhp8g^Jytz~5
JS8G>%{)wJrttG*9_3z<hQ?0=*Hk<<A~17)E<T#M=`5bj!?N(>V3w9?5`=H=VD#@~s9=`lZk*(mTcz_nuky;wFlgxJRWwUY9vL@u
L(jzXGRfmO%;yPDY);eMr0847P#w`CgYq=dz~npw#H;*>r!~*hB&w=7<^kq&KQ`5T2Jot|@{1w}F;vcDN4>%;!DupQ?d&O-aZr{C
!0>#47Y9)ul}Y8sCa;n_io$uB8h;*?v&hR6zw*-A%p_G>7PCBby=X2YHt}m2GV$^%4T=P?&HOkDurRL#yond{pykpH%Q*K8Px<y|
Rg#ot8~{^A?niRe$eTN#J~?mpPC@Nah5fR+{g}Oc*S<cDv_31e{&sqORA+szWPR9^{?)JL^K7RMk#$Zr{mikWx1RmkIkvKM;8p)*
srn45_Mo5UL+j0nGq=-pl<*jH$7iQ5O&cNVFH?015)5aaTU34$%;!m7#51=DP38L4tZ<`w9GBrd!rxgjn}GtOS!oJ4#%7otB-x?r
c~tQ<dmcUF<wY13l__SfTUB|${f(*^odbVfRzW-uy`T(=$Rt6YU}w#ImfuR%6;Cgz5^!Bwx<Qq@)!a+HS(pSS^kxy}tCAw{!?2jU
MdZ7MTb0JIif9J7i+FyMs=X>MqofKkJBXHNiw8vjVm8K|$CxfBBFqd7odmOak>|cCyxa?`)aPOF$t_gvgFth)j65&(Lv-Q!6-Al)
z>o(93!|9{12B0M8_0z)cEbPz8PNSaGG$Uzb$zPCo|N-UPs-V|9lj*xe4mGiM&8$oIIjvqz*pq+D4EamFfJk9yxesIFOTQdyhw|A
8pc(eU>!x2=A}uiBF<w20WqtpE-_$7;+Y9}oJUm{P*<Fn6@~>lfad0DRFv~Fsz9_AXu}KVkV7-f1Jc0{|5jo^i_nKeD3cO?N)VSp
9stx}=9)AvjVYrrf*gfxo&|x2{h#|$JWqItcm+}}ZW2Q^OOiMMO@T}SVhXu7OCugv6B;jY=fFY%kq*I>rip?0jY<=FknKra6k%B1
N(>k)E-M}y6qPejJ#d-$Gk0E;Gq(zo!a&}+`P@r_AfH3N`<3s`fl*4oAR#f38n)}p4U}<rmtH>p@rQ^1o&NIuy^Cwv(KJcXvW$V1
s?2>41ezzac>qxlDW5<k1#`-FC=NHRcsxu2oyB9p=h(v__hYy6Kz<Xaqhv)1bNIkB1`lQl2913en-nBw9;7^uCH3537R;f$@Suzh
1V;{$F)spekV(QaPv-^v{Lq{44R6mZ5%{4p@kscjn$O+2S4JQV-<v0?i%kSQR$-Zfa$qF+(4%=6@;Gnbgc17AiqgbU=`|B{bV4&n
?D`R&#*j@>VK_oK!%Sh6`cV!EM+xMYId-DJ4tYUXKz(^YU6SW=a(!L}rEzbYqq7olyibBnu#*X7+-#QcczGUgRT+o`OiDGJ&Z@$n
6>&TZ;-mz{M<5j7H8C^<0=tsl$zdwt-H;oBA&qa`84#aVc?wxw@u;IBNWp7KQ9+Z=Ax^;?k@2I_k7qgPduG67VP)q1(L2ybevAh>
1QzzWj7!Mo$mGGyPeMO6ZV9Pc%n~n5^Sn%Ruf$eWaR})SIpBfvz-+U!(BW@62t>Alhe|^KS0*ogX!=5rHi9`(daxNx=;wtS_@x)S
E@UDw6op}uW7Dd*z*@jkE;@DR*#An8tRyz1C}0RC6!r@A=wam;vG9R;K+Th{Qs@(Kp<lq-EkLSK=)%;3jHt>O3dH0(O;atcyq0o@
gB&JZ341SvL@d0SkHH|cz;x70MV?fUAO-jg4U@3)d>4Wu^`RZmaF$vm-K@iqDR{IRfCuG6_WETx_YA}YbfX82Q9^G5CuJVPekx|M
3rlehgA*(k!5}LjjIqsW%?_Ul+Y7O}3HQ62L0v@#j4+R3FBU$~l;>c;B!ch^LM#NN8Wt%8l^5htiD_gY(&i<kS{21QkM*XeooKwB
CY4z{EI$SA;}j4ku$GHCWmO4410JX~OB0wIP=<kDsK5qW%pt6yRg#!8d-91#9^F1qlZALCzTJ_w8c0o(O%vqp=S>FK&JX$pr8@c0
et+rSo7MC6;IzUBJANW*V^bM}vub%!Z5Ue6Xns`=B*ee>9`rzhl|qfo3w&*Lh%FP>RSqv4J)q?`iQhI=9BoYSYI0l6#u{EDUs9^0
=JNQr(R~|1xHT;Mi@x*ujP)7rXmaRF5TDn#1o1x~*I(q$V&>>c53`fcyvU&O*-MPiFaw}GTK59{{dpwGa8eJfb*uckOPO8jyOcwz
w;$3eJ}g<CPp24HW-`(O{2^WE-XnO@ccpT_eq{K_*hi!LQ76E8^}rqfayPpg@3NCMgCx0xO61Kz!ZY3~y5HApc>lTY<V^aneDu-^
d>t5*95R1!KWGvVpGh=a{f$J!4(ssT&dc65yD)3B3!07X<_@2Yw8ibogo4!Zu|t2e{WQ{~4FqXmrQ3RA!z#Rf3FB27yu6u9_}htz
JD>g!Tj;W2
"""
raw=zlib.decompress(base64.b85decode(''.join(B85.split())))
assert len(raw)==50028
assert hashlib.sha256(raw).hexdigest()=='3c6f7fbf3269a7bf852edd658fe5ba6709df48ad92a47126d0196641daf271e8'
root=Path(sys.argv[1] if len(sys.argv)>1 else 'VH_cold')
root.mkdir(exist_ok=False)
for name,text in json.loads(raw).items():
    p=Path(name)
    assert not p.is_absolute() and '..' not in p.parts
    q=root/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(text.encode())
print('DECODED_COMPLETE_LITERAL_VH_CAPSULE',root)
```

## 10. Complete numerical constructor and continuation source

Exact reconstruction above is deterministic from the literal integer tables and does not replay an optimizer. The numerical programs that materially produced and extended the geometry are preserved separately below, with every helper included: `cartforest.py`, `geom.py`, `search_global.py`, `persistence.py`, `polar_two.py`, `angular.py`, `refine_selected.py` and the full-three-vector `rooted_continue.py`. This source capsule also includes exact-centroid seed preparation and explicit restart commands.

Discovery used Python **3.13.5**, NumPy **2.3.5**, SciPy **1.17.0**, Torch **2.10.0+cpu**, float64 and one OpenBLAS/OMP/Torch thread. A restart using the literal exact VH100 input, `anglebar`, reserve `1e-8`, trust `0.03`, 40 iterations, angular reserve `0.003`, minor weight `200` and cap weight `10` was executed after decoding this source. Its final trial was infeasible and was not accepted; the exact starting strict211 capture was retained. This checks the recovery/source interface, not success of that restart. Numerical optimization paths are not asserted to be bitwise invariant across environments; the exact endpoint definition does not depend on them.

The canonical ten-file source mapping is **27,125 bytes**, SHA-256 **c25266be455c73d065483e747426abcee2b936e7f16496e195c9df37e014d052**. Save and execute the following as `recover_vh_discovery.py`; `README.txt` in the recovered directory gives every command and parameter for the executed restart and the alternative full-ball/refinement continuations.

```python
from pathlib import Path
import sys,json,zlib,base64,hashlib
B85=r"""
c-qZ<4RhPLuIOLU>C72P4*ivM_wCx@PP1)t+IzcM=W91p*W-~T*_LBViX=NuJN@qu07;3G<s{wL_wMVx>qry{f*=ThAi(qW)#d5Q
yFX4_**1ICdv(5E`AOh9OT!CNH`@5gqv3>};YMK=gli`YqR@!K<s&n~D1%Rizja)Aa9uynoY3`+%uln{=Wy_t&7tm5t9#V?sc!(_
!J~25qL(W-fR}Eo`@dS9zHuET?i@aKJFU)v8?T}9_1rgBk+)v@sSziB>L(ij428ieUivFP%zV$7u9wTE3(rXuc*a{Nft~}vXc|F_
%t(C);Ihvl)`P~0?>9HTn?;F{L=gaJP8|5)EHgg|VPG4d!FXotrIQ$OgufDy8>LwaaF7mZ2Gq%nNstOi4?!0CX=)_?GzbZ?mT>}5
=l(MGlhkk$z&Ui6YtQ#!T<4J-dzjN129T~(Bb`U<rDsfhW1Yg-vIssTSulmFQP@mr+<-~EbV9_;as4cngjxnL0)QlD;;;AJPG@}C
J*0Vqx1WC*|9<oFzo{q)<8_wOmw5h|A_AX7MM8mX;?uMP4wFYBdFsbb;$*&r?>cb`^U^Y)>mV^!4%C4k0SX(3K%=!wjFR~G>i}p7
V=$sP3s%7wKWQ02g~?;)Hv<oPCL+j>g1xfDSrBy}KZgO%f3yN}dp!e43_~p-88LJ&Mgy3^1R8Ug>eTT3*oQIzRggK&U<g34&*ACT
ch|^2IJv+y#uPfBk=78>aOb{z7e_&u^*)EO;A!AUAc;RteVEkv(P*{Wf4v{O(b8+@)Nd_PsHuI4))~;gs4zYeRR{<`{v7@}I6eRU
<H^<d{N|7G^?O{GSG;Td`NyDAGPwNk$H~X>A1AlGW1O7-=i}-4^7QKT@~>0g>U55bKR%rQc{%?3^uvGNU-Ls4#M_gBdhK=$ISLoX
E;t;=&}<TK<mf;FV4Tya*@Wfj<N8?o6JWq*Q?1Ib-~0t$fh~+yw+l}&`><$QfCs?La1p%jVEt$v0*iHV3Xp4ciDIT|0_BnmQsTo^
OcRw)5L8;j{Dl64p_mpWO+k*X0jq8m0E>H%p|c8H1A#1k;2K!#O`1oTzF-AV<kAK1^wvob&ZviE9RkD?k}U?xhxW=z(<bn-1KjbL
)5CH=Ku)KyP5_|4g<b<({5D`-@QDyJV>wd)2{L0(;|i^X3~Dz0I7K4=43B9>FP%<@s2CZJ=k3TM7*K+XGJyesGz6HB_-P)5G(zCT
Tx$8@#$QIUuc1tG3^;oUFa>w-<qWKe$U565&dATdd=CGHevD%dGRH{Qal8y*_K4^y^$n~6V#J&I#ss+mr}>z_{`D6If=Mh|pyBe-
h^8QwfNHo5vvm@pKth27_2K^=BZbv3Ku9%|OEUu{&N7%J!FnYnC=}DmKP6?B_?ZKEgGK|f5qK!qR>-d)c!@*d3ry!SaDxn$oF>rV
i-W>Oa^dF?22PBGLWkuT0Q$t6g#g_|OAtda#LS<ecp>QvT!mtO4xP^CFqUloIh3k&?FBHMDM?tIE=hktKl8Unlz1?;K}rKpohfkk
G(%YktP5NW1AWC_Nj(PB2Ra>eM+9sIvJfT@h7iUqLzN4f5f@hK2JvGn1&NlDe#N?Onv6lHC&9L+Qp-(Y9PwOL_JYM7kjO!v^!%w(
qT^+hrq-uxhRYyjQeKdRV!+1u(6xc{j8FX2b<2Z!ap#uZA~Y?#AM&LiTA%EG!o#?=3_@o)YlTs=vOX~&e9F5vw0*}v4bP*{XFb*%
H9rk|OuUWyAFIvYiDrk`Y{somZ$7oIn~7{OYBUb*wpF}Z9}fV@MqXgsO5#EDw+Nf2f4#CgtU0rx`2j4_U;FT38o*-q0%sOM=hj=+
!5+b!${3K3rHRWG#jJwP*4x&#&0rY>uAd@!CrO+~OVG~C9%G*a1KDg9gk!Y7_%*C0ASy18F(@R@hjuBj4Sm2K18>WR(8daE6stx6
9B2^W8Pv-x#K<1@dd=?02&V8E87dG`D;@P85D6H0YK3+?>_4P@IQkqGkN|w|A#FJ^E?eti7>w-x!w^OYPoo2l1yJ3AxgA2)QQyNS
`V4QQrqfRnPHd<qN!Vs%nk$ES!Ai`q%Pptj*{u{v-Nh+N8rI%+o@^)PE-6i#pp_vTC;oD6HC>#zhA7Fv5Q`G)A+<$kHm#(RmW0Lh
nf~uxZXDxW^uTfe-IYd5utSw%Vuk9F3WwIcW>|v#CcuSqAw}uuFiKk>m4hS-hi08YV2-%iHT$J%WdlLf$bst1-k_0!nVZaLB|`zI
ExE+em;%YER`tNi$`V4EU8(|bBE8E>Gar8BCw%s^<dF&ER)Hadd^}r5pzc)Fjk8?)={RE~QW(fhp9F_O3hW2qQy(`LvPJ9!Ny@Me
jtYzsy*iS2oIOOUGCYovp(RW))2W}0fh=R(6F6Q9Y}GG5fCO{aOZbaxPBP1M89CX{uWcpa(E1Crl@nV7l3?(Uq!hBvpfO+oaK;C3
2D*R|)n>y)%B#^a&%cd$6Iuu1RKfy;akX1wwSu6rfR+2uE1#)?F1-)2Dzxs(hJwXW%-{z$QwSH^6KlX=*oE+ge*->f!OjAOZqbtK
V-)qW$csRt6e1u2N$*=IrU$l7GUQ(zTN9_xh5?h(;23&rSOa)`gFp5t$CfW)a`O&yz}S;S4*xBP7y=mJ$nH6UVT0jf)KB87oR2|e
+*b?l?E;*~<8~4s+_#hazSpkS^t768#A)g+?~R4kVG=-USxMY>ql4tW;YN1*u&53caHC_e$#ILBz(X%_z&JDhLLNU&5|A!t5CX>s
h1F(i-92&;ZeH<@HUcvI8|$$d+rM>)u8)99^AX;PdO%1ehaUx71S8U(@WF0&iE)sXL=~Llg<WEpLft?ErkDVk$6W#v#^pMc(}B!1
9^*c2Jhs3}oU#D}YmlME%1vCoX0GYcXl1Z3;H}q;HU+%Z{RyFSWO`ehU<A|xHtf>_z~d-=EO@Z<qSorp3lhr*9iEM&JE8vslS-W@
suCvnBVH9U@~<dFq~JgCB2c5>3Pz-^2?#EUacN25WWzfeVmKPZU&2HaZRNt9E}aav?yyabu=u!R4?829*1KKl2Q_s*1<x(89HEgM
FqoGe$)-x~LiHi2by>j$yEfw;@iGC$12gmMuf^+Ox2u)7V21hp>o@U6I}(msqJ=+}T{Ig{eJ7=<EQW(J(AoHwnzXh_wkvKMOg6Cl
yWa&(MFmB4yWll2s9nKlUv!26QkY*%BvFAgtqw)TG40r_FRb`Jgcc*aCs|%E-<YEUbe!>$J@5rtXzqY6u$o<VWZO)6HO8Q_yxiQ9
|8Cg@J7X@}@O(1jY{$CQ8f-ImpD{OMn~W=E2u)ZCi8E;eO2a1#XHpbxv&J@4#!-nrg@w?X`I%)FyJVA@9n<D$C1@liT(*3>i|noi
zTGMlyzhB@yVXo^c*$+>GVmD~-P`S(?e<BtyDE)6Wwjrm%F^xeT~m8DV^WXW<*pYoFH|Yi%8|c^@eUX9P%T3+Oraou>*EAV)8HOV
<|HY;Rl1nPI2py~hIg;otd94T(R#0}Rxw1!1G`lhUPVtRWqLbZ<!>nZ_YB3(vC#*yryF3OLY7LgUSSnKWe>11fqh-dRw*az&AMQ?
yR-Yi#~i&BokniYS-|9?4OP*Hr1yqP+A_gv111I24t~kyBnp)G$+RoT#4#tUuy(1TBrI1)(H&Pn;J=l#h!T!G636V$f8<MNHSrw7
>vfyn@b#$e4Ua&mt|nYsot9X<XKYAK;aiRAChfwD#s%1gwq4V00BpcZmMT(<Y&+5>1RS-;s7k!L2@^6qMVF5yNVY>S^^a_3<@1&n
v%Y(;Zzb?8?eh1btF*6BPgRjra$Umw;^0gm5%Eub6Wz55Ee<;%$?OJUbYRstDV(3spiA|&E#PX>R3-uL1*@!|bDvP~t4R&<X;C7|
hs5#{nQrGhx_P399Qu7Gwxx~EzQvQ{TeDujZ>r@2ZtP6*ldSzu=lhBA$o-%By$imN82i#^p_2hjt0{BXgpJu4g-xv>@K7yGNPs${
{(MgI))_VES9%AUvP`-ra8}!vm%sK?&@gSF*>E~)&~NTlsP-mMRpz;-ZZ!VsHq*2{pWEnU>K=ko54N?vJ7=;n5aiAhU}dk!aH2r4
*^8J7P1q{sS5AgD!u6YNM$5EWQfuiln!$X42*~VVcXV*nP!`KfjwVYS*Qf7KO*=Z>P2zeBrnp(Mg~VpTMuOX|mG6X>T~UxbyRICx
Ruh54f2ea&>%OQTs@&Daw8`4J4UQEH@Uy9$3}>B1XehSu$ATUi7<a-8JtnOwEJ%=-JDl7~z*b)B!~3sVptBfZ;^SDHGNrPb|0s43
O5cO=8VIvB9Z#GLj9>4m-lg4Jg20-(ow?b_r4HlD0oeT+SikYE9a-!~4tTd@ZJ;|f2(8)1{;k>iwV_)jWY%vs$N9da!jQ$TX0xeo
PHLos@^tL(M6j8*56Pj}FUAyPOEJWM|J32UQ$f~sxp0Zq2`(`Cm$+%}cI_Q|#dU`!flbX3=hh+XvTmJLe_k+7CS>6ZyUh$unhZ=D
l8Tv-h9f2&V7yarXG|u?`p$8WWl`E(P9}TE4Ic%?>#*&|32GbE-`6*nr*c||2+}s3Oqe+{SurKd^p{SY`ku+OEo-yb$+GEkozAO!
wt5-^g;}SL#=B$r`@{M9=_NX0pC1lXI=%ex_T*z1Y!Q7-wWuk%C|C+q@-9#9qO){>b$witd$FmgQ$kIrFElpUX0t=zzfR9ghJ^ad
9MRuX`S%R|D(W$vk~CL1+1k2-d1q$oyWclWx_bil^1Ux|Ed#b@&jMs;Q#RYM|FXaJpW5V;KXffb8lwYhe$**VbS#`K10{d^6F#&y
&B9y6HV4IvI9=J$^3kjfEW9h6I7fDGGCXSJ-kXEF5x3$>39A-pqmSZ@E0?<^Hzr?ta)e9Q`eF}zhX8>s99KBUR(>{*JZ@fnyt){`
YM}#oK4IcS)4@|&KKyE;W5Mj1LFnIuO*UPJX0IMRKsN#SzRyRaZzG0>1OOf;2#?2rxMq(?41htpnLRRJnCS&+Z1xb#Z`u$C9GbVb
RfkKzp2L+>Nt-vZ!cNcMnTQA|?KE{}zT{>sfzdG&sA%FjnpL1r{o)9LnS_8g+1I<?M$96k$(4e8V7FjIt5n!jcVfe;7$24eGtsn#
Rbqls0KcwjfBT1WN$28R9pxfHD-nmmg&%T&uG;`TwV|`}$78Ul#^V)Q9AjnAIb0nAwN8@R8jl7B_?7^>J1xia#*QquOc?=S=BmMb
m>eAu{p%`6rK)&<)~T(B2ANiob}e=Fq<RI~p$m-cjl31v!8L7QpH*AG^}4P$t>gOo-Jfddfjli60MF&sUxOg28v!l7n)==P@#0~P
$s7uz;${lQoIl3c2_#Q4OS#jcnZs78G7krZ!x4RG5!i+JxkXcFqlMQWw7J~1=`OZ`a)*f%roy2M3`7tFKD_}Q42-#cmZTlrXtGYU
qA{1mYRoS|?hY6^_o)(k_}f!6`Fi&a#)~D$6ijwY(=J|MKE;EOzlD=n3_XrpDAL7%ac=CsMvuWi8NIGrD+rr1Qm2qWuh=W>ZC|`a
HHab$iUZKMQMmE9@7K%acZFKKD0D*{{%LfOvw;ySyy!Te$1{#!S`=-FaR^euN{IoRW|t3!XTu)rjPUpkpSt<e;Yez~5S^`Vf-Zwe
(_wDYQEajd$Pw!YA#Og+V8Mb#^S1y@3`QNJ)1LGPfa@KN>|?n*JsV=v5to1A>#)NPvG4Ch4eX$L1RPf2%v@z3fduE!L~NDYKZ`;)
OSlE4h0oeKm>js$!AjiJvD?<+>jpHJfNuGq3GH_1bE^<--sZ^PDwK;d31z;Ic-4v*JZ#U)2hUQM$m5ADVSt=skkrL^1nX9@hsSR<
kN$1dp`SPpB}DE3kvqU-VX|B1l}{F-Zo9hVZq<_8@AcQ6{y#OIYj5WV^Qc4MJ6ca_FmHK2ygo+qRzi2)s?eRT<h7ks1#HCBW=Mqb
B(QI;i{ZhldKeG6M4yV$K`E;a|MIiGTaZOq3jblSj5t#tRS#@kj4BJq!q;O#Jwj_JeEp2@e5=T!Oc%Ao{8bUB=Cn%50(Y$uZkH(Q
%27+I1uYG0+4O={*#0hOcI)n-YybNQ_}AXGn@4u*TJ&+nE9a_dN;?zD4!>pjdb_FCbk{iPs^)RCsCw%0uiv!z1Li(r?>>bNJDG2t
={juJsxR-PKoW8HaR{b7{HkH~PdyARkxJjn*6|XISrFE~XIap~h6x+OFr^333fP^JK<{%8CiYB~nKMBI0H(A<dwOWYE&45Q(QRpD
oF3kIZOeP(Roob0FLsWz<8Dtyr<OjGb({_Xk&&bd4ceIyk$dk8RKW^xY;yZga!;;g(yz)a?h#vG*$n^Oh(GUP%;uHZI~!h&S^yK{
K(GY(*X&(sB{yd8Mtgm4_THnJ-9sQS$?Gt<U*ja%XmnHQnT<9$J)U}K(3?G1gMemvZ}W|mwiaIWqFBkgAg3ZI2>mYk8tWd?#MG`Z
8Qgeg_Z9a&$$Iz^W*)zN31Z8A#Fdmppt#|&38qW$DF&-dQHj+8oH55+@F6s}#Nrzl>>b)F<Zqfvo)bsZlIhT?4C9!l_P_XHO|T1v
`Uatkf&Q*9LS1l$Ow&Ge3cQK7FJMJ)6Y)mIf{a+fC~PalA=1HGH3U&1Nw_RD0VIcxPy;+EPPuh4T%@Ds1-`$*-~K{75*9u_+*l14
Bjj*YIbM`mSd&qso(!v5U=^$_Jk5wziI_`g0$-j)ln4FP_d`x3$C8J6u=H`v*t_!Y05%H|;NXWfq;((NrKBiTA=)i$7?yy89|SH6
J&O5xUtlJLi8W<2yGEYqlB7nEND%_0LLq|Uv?NG;eleUOxu?(?n&ZP8zis(%{GH}??Z0sB@E{Y>P+_R)76io*y3z~IQVUO5rdfJ#
g(3UG5&-ClP$Mw^Wv`?zmi95P_E?BC;n4o_=8H||L_i-V2#Fobry1EC#@r8P^NfEDdfm2YhP*=jrN!J5lYHy1r&uwlmSb!%dZge5
IH*_f!+Hu}{>7mQr$_uEC2K(8tSRmw^XZ)D*d|k!%!qZwGI%ebQZd;QRx-7jc$lf_NT!@8vl2->-|-kmwsMQwlEXs`d6-N`zp2OB
NJc*;*tae4MC5Xk5+p=#&SWDj!IcRkqeqVY6hXSV)Re*F@0oz8WG$UX4&>px_{8Gq!B4pGii4EW*5EYIPy9r6$>ak%=Nr&DUowxl
MURa^>7Z}$)IlG@$&dO1an={8ws=IAFF-uRYeOdhfpE2p@#^Px*hD+E!&gCHQ3=hN)B;5&B7z24iyrJ}Ts~51rH`p1N=Pj7n4%Ee
47<G%k)$zZmq70P96|XKreW^Fo`#^O+wV=%<CjXElb<&=*$_uL*A80eELBGfCc-oUxY#o1(YpULc?#u-i;J2>1);((_{HA*go~Q!
sEa(lXeS5ZLfcne6#J@DX2Qjri`I49N*YPN!D)7t6Rcr<Z09jhv^%00`Q3fZQz;3>j^^2{gzApw$0a8Gh@1qHCAEnO;>+{d2^V>G
!o`ouPDm2Fn5}0s71~LXPvc876vW_4X$qB;#9}pJjv=E}zt=6bKk$E=2p?pszMaVeY=7}Nj5&fQ0g(zPSs_nGc!2D9<ILY?bl~Ld
uY9;u*%guD7;6j5X=o<S!&qfjn52C5klCSBzSf4tL-QR}Xu7Zmvvv1<VO1y5gDti-@I<0%Xnrusd6J(rD9nyVYzyV;Wa0MY?e+NW
>G}2LpC8_huWo+7zJ!v~cjN2#r|09dkAI$A|NL4A#;q-8W;dg*n4JIX2_MSG|LjZ`X)fyH<vL_}!1If9Joe>lloJtPmjt3}9QqF`
89_+e9iOep3gyK<PyY^F(;x7`P*i%6gLhAIL*S*~o7k`~uR$ij!Tu}AV~x8_Sw}S6afngl#!jKAZ7T$&H3yG+Y+}%}nyNn**dRP5
Wk>yTeuX9<Q?(DFtcseX3f!aZWL2=8l!`uPQaA_q?MZDOMc+-i_XfXWq_Wd?(}PLFP3`t!zsPiWKF6V&-LR9~P|9r(sSSJb8kk@e
1|)dWSc;!G9E<lIj>)ia8BtSHFM3fenNC}CSoHHRuu<l5>FfulKpalc$wc3KK1%|ZS(y~_M5j15l4nNDX-Qrxj$l2E=*Jloxxl5M
ey<$OA3LQ_qCfFTJeNKT9K12$BkI5dc>;vw{cwJDdI^G7$kqW^n*zpI^r%2;ZXOAc08#BV9s=iwxRn#vL>^5MCc;V;L1>J!SURlL
IsA!+biorkYwF@rpEiI=<UI<^FEqSQ&);31o_#n!&AYzPE#(b{;A~U~j));3v-^UAbw*_@QJd_fl>a}}CL((<PaZ^d{{Lz2;1A04
ONb|m{3hD4n2gf!DcYA3nduA~#YQ=C>18=fyT_D#&=#ir6Pj$$DRTD2Mr5!r_Pic~IAPe;d7-ZEK!pSzIxQAdZNY-FA%*dP=)b@N
A(8Ef*^kN?R=bql{Rh-%&92|=h%;As-JjJc^#l5Cpx%(qIh2_$6a*#27us=K){f0OT?=wlfOVEjnODe#f`?%eycS+auvIyS$9kEb
PK^`*6mB$I)H-ZnAI*W<ZP@J^%`U!_0Acn(y5S<)inejUT+He=t((S;BC6eJ9pRR<v>_M_Wj<Jx1hev|8@o^WVU^4<+_~g=UU)MK
A9fh#fQ|YXRs!;g55=pJa68Fb@(5lWFo%L6*22>i19yK#lzPcG<-ev;5*dYi6CDg$I@A(7M|~>5u&DT8@4hLH?Z$ctd`Sdsw0_du
V!9V)D1hzq_efzqg~g3WM7b;5+)_r_-efYY%w#m#R!b$5MUDtCTbCyQ8@(ih3<l3NI`-qb;MIOzcA4GZvipCMK&D)xJHg%*<BcKS
KO(}LV!Laj`JdS^l%iQh>}uvGt30NEe<;7lw-mjf2k%qtekpYS1(Ev{xL?HWi_ZUPlzufhpMYszK6;m-`Fdo&PCc27p;Pa<gpT?=
ju)qKV7U9??kq+H7W>n{4n?Xfv5=MpRwRK{0E<96kUW5qNkMuM8ey0jW50l3SU%<o)2PD~iM;GUT*eUhpz`p!gs&<HO4gC><=N~@
?jHEQ3^S2l1`AtHE=!(P?-!bS*HZAxiDhh<B$YHR;MYzyTd8$)m?t#olP~6_Jp31qD#A;N_%PGM&58F_0HYY^zR}}|v~q&>JmxZa
N^3~o=bb^#B}3oebL+m5=Wh0kg$oi6%KU9?6%z0M-fna|<jU*V?QZ9w_+)JxTLnd?kJ!bzVf8#OPfpR(QZOrJ-9)8cO+u;Upy=r*
GY%HRy0KP$my=q+!m#`PJ$EVBeOBbR?xv}%|3Q|@!mkDA-vhKg`6);LC@1Ae<)JJBw3y_fNQnBifq!rbtW&<;fuQV>g=P~#_1+>F
E}-qA2mc)$f$@3RSgWI6OlR5E#r}r-_q)Z*`ji;5vS3Iu^F<y-Vj2l=QuL9sIP?YWZ|q~bUk$%4H^%}<chpl4e7PxGXhjlBZ0~*<
uf?}@ao{b{`ga#I3()+{vs<3UN-P*HrG;t9E6?PtJg@r=nW$2qr=kgXJC9bKOpc}X3L{ccF-3`<hf<S*QcXC4FSykc^r2i6;SkuR
#!mG1-ei(e_kVvl*HT9G1QC%MqPng?FV7k!gp|Nmvp*Ez9Nto-b>ul6uE~5TqN_e~HwDmEOX2vdRF1hH6{MUn<rV<Ob&N?EivVFR
K>rs8GbdYE?ph0@nL}HZumO+gs#FSO+e0ILOPLM**-q&pMsZXNk4Aler|>lt?pFP2B+k)`yoxEiQQ~ZG9>w$N6Em47vG~UF@5NVN
e)Sji`4Z$^csgGKEYM=JP?qn0x|={@+cn3RRhALl0+4IIDY;P(y|3q8U=@{jfzOz6Az24um-*($J7M!|g4z1;P-ZB^&txdz<%^x#
dX)?XVffZnq&cf`*`klAu6|LwHl3mB<V8PJjdvCuQ;v+7Zwa<>TJS4eg(a7netB8l9lzQ&X5u=->SbmQ1{?*h@i32;eiIFPaWC%w
*d1ncu!->t-*t)E-r##?T;RaT8v7pC<qwQXc-|HI!yKDppZ2K~>p*8?6fY%1X%3aLe%V!w6dgU?cORpuuoDmgEwtbVG$%M+%=mrr
4|G-6P6&jn0&OS^;w91Dfr!IWmpb+8FJhBprJJmNR1`QFG<-OcF%5atZ#m+ja!r~ZI3c4Z%6BA5KW-&PxpJKv_FRhR4M6vSR2P`2
FT$pM5Z==VFpTpcikfT02qqmEigy7Dg+E=UrnW=kG&U~;>K2jwXlsq}wz@q0`h@+?-o7ZwgIgz!lG92=okMdOGm+=8|II!9RtAyU
QKTiD9Q=Nu+F(w{>&D;Z5NAxJ_!|>L1k$<tO+#DeT5xSZ{ZcxJ7*{p_qpN3vh>GXDZcxn=_O^Lq_vhR?Z=6)dcfrq}NCc^*ffQbv
PfYk!9+ZGkgTaI0Peb}Bu`S*J<G#lyO-Egb_>%Y;TJc2)O_O418s8Z~qsxJp#?TbeGwPDNKPPzWIB38puDUD9%ZD4@We->IgM54=
L?=F8iAOvRGC?9ZOLOP4JF=koK>U5;raI{3;YL1Q@rSDl7|}8P_Va=(D!7t2=i!k+epd9I_v`H>U)S9vSG*A&(d#6N&~hB`K?TOn
am4G9PH((HS<!o|lWo8Y%d;Ti?#*j*x$We$kd$4shc)xoELpSFT6!yQnNI%V!oM56VZEEP)Ua~1-=K1j+@RL$f19z3o!j3AFLd6E
e;?PHe-+?~LF%a4{g0_u2RanvDb>-_j%UE&PhE3j<nF0K-K8nyv8unH1rgwqvl}1R2a>ZJAJYTqwp_0@aooEHC-E%0PBkN6(*C<q
ut{-o6amoOFMF>Zk<DIkzlf|^V(wCg<o+8O3b)MQ`!09Loht)!u5|Wa+<=<_{RRib)?^ZAX2RAC_#Q(c$iKdV1(0eNHdHtJwVV7W
MmROm<M6dW;M?wS)sR8#YW?Bf-aanNkeW+3Dnh0XNWTUvs{Pd+etspYettC?c1GVSCEZaCx>A!U3eKL-saK~kdC;A>Oyd7!8;f^H
J8m`>*J$FN=LH+uS^aJnV?%59sI?o^r*iJ;?53v8!@7P?TU$4MdEI@<_T4?3>o5w^dd%yG3bMWix+czd_T#wARB=~gH=gew@Do@T
(`m2;4k51U4Y=C8<5yXi&H)N;`=Uq35)eHgwm&E$48BmbsxX`F_7{qG-MIoFPkAqE+D60bwvP&IofZ+RH#k7}i4%I!s--rNNjQV?
A=lWnS%cjY{tquGtHo}})&g2IS@7J1!bp=MfxiX%2!7BzK^8w6AR=H*UM!tFYLrL{cO1ZEgZ&P<kImoD{&Us*-K=w?IW2kd2$YcD
O%^nM(S2)2%$%v0U#adgHG4-LdUPXz(>>I$C@J3vAg==`+-HgA9#dqh_{V@bT-*S{Q|>3zy=1i@b|taD#s9%2<COl$h-|;7!p_c4
K72eSZ(Ix}U8VV}Z~q&Oi$N*
"""
raw=zlib.decompress(base64.b85decode(''.join(B85.split())))
assert len(raw)==27125
assert hashlib.sha256(raw).hexdigest()=='c25266be455c73d065483e747426abcee2b936e7f16496e195c9df37e014d052'
root=Path(sys.argv[1] if len(sys.argv)>1 else 'VH_discovery')
root.mkdir(exist_ok=False)
for name,text in json.loads(raw).items():
    p=Path(name);assert not p.is_absolute() and '..' not in p.parts
    q=root/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(text.encode())
print('DISCOVERY_SOURCE_RECOVERED',root)
```

## 11. Supplemental artifacts and disposition

The artifacts supplement the complete literal capsules above; none is the sole source of a defining coordinate, incidence table or verification helper.

[Standalone exact recovery program](sandbox:/mnt/data/recover_vh.py)

[Standalone numerical-source recovery program](sandbox:/mnt/data/recover_vh_discovery.py)

[Exact replay, original exhaustive auditors, certificates and observed receipts](sandbox:/mnt/data/VH100_VH168_exact_handoff.zip)

[Working numerical sources, retained trials and logs](sandbox:/mnt/data/VH100_VH168_working_research.zip)

**Disposition:** retain WB33's corrected literal identity, the exact strict211 VH100 checkpoint, the separately exact 12/1/11 VH168 supporting-geometry checkpoint, and their complete physical certificates. No strict110/E<500 promotion is made. The strongest unfinished constructive target is whole-basin cancellation from these actual-centroid geometries, not recovery of an unprinted and inconsistent WB24 label.
