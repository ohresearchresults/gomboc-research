# figure-0170

Historical AI scientific report · saved 2026-08-30 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Steady Comet 92 — exact complete replacement of the `E10` residual disk

## Literal determination

**NONWINNER.** The whole disk bounded by `[1,2,8,10,12,11]` has been replaced in one connected event by two internal vertices sharing a true edge. The exact dyadic endpoint `E8A` is open and own-centred but has strict `(S,U,H)=(2,2,2)`, not `(1,1,0)`. This is nevertheless the first exact materialization of the journal’s named whole-disk successor. The complete recovered suite was rerun in the current runtime and ended `ALL VERIFIERS PASSED`; archive SHA-256 is `4dde809e5c9b0deb7cd699e6084d8f5185521ae2f3b75302701e263fc633c5c9`.

## Exact source `E10`

Use denominator `D10=2^44=17592186044416`; rows are label:`(qx,qy,qz)`.
```text
1: (-7715758938572, 2889556079942, -17779918034961)
2: (-8262479746679, 1678647340512, -17660251163923)
4: (-19707343224389, -41384307037227, -17592329907461)
8: (-5658133234447, -11830031585001, -22901357099805)
9: (-24778822577834, -27890508662314, -3487947517004)
10: (-17333854524801, -42073399768973, -17068563828311)
11: (7425371686672, 6793144760174, -22628800214142)
12: (4728022774716, 39660727728711, 500165975828058)
13: (10760034733605, 68069391392350, 42437702267733)
14: (-22123888254578, 15252741379, 1754217266202)
```
Exact volume: `1681266850734491086730347774173197219339093/32667107224410092492483962313449748299776`.
Exact centroid: `(-13084743467721568266078774833771361473855413627251610057/59154318456861104510651131992312016869945697642926309376, 97307922671002678684688269731363929366427954638239779935/118308636913722209021302263984624033739891395285852618752, 816657661288454335992266470234363718618523047275588334629/118308636913722209021302263984624033739891395285852618752)`.
The uncentred first moments are `(-13084743467721568266078774833771361473855413627251610057/1149371655649416643768760270362731887714054341637701632, 97307922671002678684688269731363929366427954638239779935/2298743311298833287537520540725463775428108683275403264, 816657661288454335992266470234363718618523047275588334629/2298743311298833287537520540725463775428108683275403264)`; the verifier proves `M=V*C`, hence the translated moments are exactly `(0,0,0)`.
Maximal faces: `[14, 9, 12] [14, 12, 13] [11, 13, 12] [11, 10, 8] [11, 12, 10] [4, 8, 10] [4, 9, 14] [4, 12, 9] [4, 10, 12] [1, 11, 8] [1, 14, 13] [1, 13, 11] [2, 8, 4] [2, 1, 8] [2, 4, 14] [2, 14, 1]`.
True edges: `[1, 2] [1, 8] [1, 11] [1, 13] [1, 14] [2, 4] [2, 8] [2, 14] [4, 8] [4, 9] [4, 10] [4, 12] [4, 14] [8, 10] [8, 11] [9, 12] [9, 14] [10, 11] [10, 12] [11, 12] [11, 13] [12, 13] [12, 14] [13, 14]`.
Its strict class is `(2,2,2)`: stable `[[14,12,13],[11,12,10]]`, unstable `[4,12]`, saddles `[[10,12],[12,13]]`.

## One-piece disk operation

Preserved exterior faces: `[[11,10,8],[11,12,10],[1,11,8],[2,1,8]]`. Removed internal vertices: `[4,9,13,14]`. Removed disk faces: `[[14,9,12],[14,12,13],[11,13,12],[4,8,10],[4,9,14],[4,12,9],[4,10,12],[1,14,13],[1,13,11],[2,8,4],[2,4,14],[2,14,1]]`.

New internal vertices are relabelled `9,13`, with true shared edge `(9,13)`. New disk faces: `[[12,13,9],[10,12,9],[1,9,13],[11,13,12],[11,1,13],[2,10,9],[2,9,1],[2,8,10]]`. Global incidence changes from `(10,24,16)` to `(8,18,12)`. Intended face `[10,11,12]` and intended unstable vertex `12` survive.

## Exact endpoint `E8A`

Use denominator `D=2^32=4294967296`; uncentred rows are:
```text
1: (530040125, 643855394, -1512448411)
2: (-101975672, -353004289, -2568491886)
8: (401952773, -99192463, -2265838312)
10: (-919221045, -2550270254, -3079245229)
12: (-512240919, 1524361669, 10433736513)
11: (937145320, 115523428, -743279424)
9: (-830715985, -399706071, -606055616)
13: (495015403, 1118432586, 341622365)
```
Translate by the exact ordinary-volume centroid `C=(-3077091269729371946650188678094198717/80292610405748323149698839565001818112, -9535649324942179956197940290482256039/562048272840238262047891876955012726784, 150194951900586327996316620510038458121/562048272840238262047891876955012726784)`.
Exact volume: `10905171760828200534604875467/79228162514264337593543950336`. Exact uncentred first moments: `(-21539638888105603626551320746659391019/4083388403051261561560495289181218537472, -9535649324942179956197940290482256039/4083388403051261561560495289181218537472, 150194951900586327996316620510038458121/4083388403051261561560495289181218537472)`. The identities `M_j=V*C_j` hold in `Fraction` arithmetic, so all translated first moments are exactly zero.

Irredundant outward maximal-face cycles: `[12,13,9] [10,12,9] [1,9,13] [11,13,12] [11,1,13] [11,8,1] [11,10,8] [11,12,10] [2,10,9] [2,9,1] [2,8,10] [2,1,8]`.
True edges: `[1,2] [1,8] [1,11] [1,9] [1,13] [2,8] [2,10] [2,9] [8,10] [8,11] [10,12] [10,11] [10,9] [12,11] [12,9] [12,13] [11,13] [9,13]`. Euler: `8-18+12=2`.

The irredundant H rows are generated deterministically from each displayed cycle: for oriented `(i,j,k)`, take the primitive outward integer normal `n=primitive((Q_j-Q_i)×(Q_k-Q_i))`, support `h=n·Q_i`, and inequality `n·x <= h/D-n·C`. Every nonincident slack `h-n·Q_l` is strictly positive; the exact minimum is `26808305889004762409090940`, and the minimum normalized nonincidence distance is `0.008118650934125917`. The complete twelve exact rows and all slacks are in the linked H/report artifacts.

## Exhaustive own-centroid mechanics

All exact sign decisions are rational/integer. The decimals below are only normalized presentation values. Face rows give `cycle: minimum component`; vertex rows give `label: minimum incident-edge component`; edge rows give `edge: (t,1-t,alpha/R,beta/R)`.

Faces:
- `[12,13,9]`: `+0.0469866965742445` — stable
- `[10,12,9]`: `-0.00255040406437277` — inactive
- `[1,9,13]`: `-0.127672127824426` — inactive
- `[11,13,12]`: `-0.0140166349301122` — inactive
- `[11,1,13]`: `-0.102665471186542` — inactive
- `[11,8,1]`: `-0.0906437293997396` — inactive
- `[11,10,8]`: `-0.17406758420587` — inactive
- `[11,12,10]`: `+0.0946626027022179` — stable
- `[2,10,9]`: `-0.0865442349552789` — inactive
- `[2,9,1]`: `-0.188899201993794` — inactive
- `[2,8,10]`: `-0.109539688490368` — inactive
- `[2,1,8]`: `-0.109345725742711` — inactive

Vertices:
- `1`: `-0.137573633290545` — inactive
- `2`: `-0.108848044517214` — inactive
- `8`: `-0.124945964605107` — inactive
- `10`: `+0.363315851151393` — unstable
- `12`: `+0.989638017890436` — unstable
- `11`: `-0.146510475123153` — inactive
- `9`: `-0.164953820869211` — inactive
- `13`: `-0.0527657303641835` — inactive

Edges:
- `[1,2]`: `(-0.660091548971,+1.66009154897,-0.137313671145,+0.341040380482)`, min `-0.660091548971` — inactive
- `[1,8]`: `(-1.21696447331,+2.21696447331,+0.0816739801348,+0.221286572855)`, min `-1.21696447331` — inactive
- `[1,11]`: `(+2.06659691994,-1.06659691994,-0.237337057658,+0.400444243534)`, min `-1.06659691994` — inactive
- `[1,9]`: `(+1.09093642059,-0.0909364205925,-3.71957504021,+3.78374829246)`, min `-3.71957504021` — inactive
- `[1,13]`: `(+1.25991291378,-0.259912913784,+0.08996517831,+0.151024455985)`, min `-0.259912913784` — inactive
- `[2,8]`: `(+2.83994555109,-1.83994555109,+0.30138396038,+0.0622552485834)`, min `-1.83994555109` — inactive
- `[2,10]`: `(-0.42774780023,+1.42774780023,+0.168555431962,+0.370542388712)`, min `-0.42774780023` — inactive
- `[2,9]`: `(+1.6707899403,-0.670789940304,+0.340240279909,-0.250278269989)`, min `-0.670789940304` — inactive
- `[8,10]`: `(-0.248681749444,+1.24868174944,-0.147150705914,+0.440071084217)`, min `-0.248681749444` — inactive
- `[8,11]`: `(+1.84848100324,-0.848481003239,+0.186570543916,-0.00665736518931)`, min `-0.848481003239` — inactive
- `[10,12]`: `(+0.338672243855,+0.661327756145,+0.195461754373,+0.178619553135)`, min `+0.178619553135` — saddle
- `[10,11]`: `(+1.11680050164,-0.116800501638,+0.436445395893,-0.338013978396)`, min `-0.338013978396` — inactive
- `[10,9]`: `(+1.47437858224,-0.474378582243,-0.0973306215519,+0.189081306738)`, min `-0.474378582243` — inactive
- `[12,11]`: `(+0.825849768738,+0.174150231262,+0.108057786664,-0.0160000518029)`, min `-0.0160000518029` — inactive
- `[12,9]`: `(+0.83925519512,+0.16074480488,-0.00368512208116,+0.0678918746584)`, min `-0.00368512208116` — inactive
- `[12,13]`: `(+0.919283832166,+0.0807161678336,+0.115543262003,+0.153277095472)`, min `+0.0807161678336` — saddle
- `[11,13]`: `(+0.987983746864,+0.012016253136,-0.382678277943,+0.501401208386)`, min `-0.382678277943` — inactive
- `[9,13]`: `(+0.613117151339,+0.386882848661,-1.19579507297,+1.24825062562)`, min `-1.19579507297` — inactive

Therefore stable faces are `[[12,13,9],[11,12,10]]`, unstable vertices are `[10,12]`, and saddles are `[[10,12],[12,13]]`; `S+U-H=2`. The smallest absolute signed normalized feature margin is `0.0025504040643727723`. The transferred residual is stable `[9,12,13]`, unstable `10`, and saddles `(10,12),(12,13)`; the intended stable `[10,11,12]` and intended unstable `12` remain robust.

## Open neighborhood and independent reconstruction

Exact outward interval arithmetic permits every one of the 24 uncentred coordinate entries to vary independently by `2^-14=1/16384` while preserving the full `(8,18,12)` lattice and `(2,2,2)` class. The certified volume interval is `[10891889750923788859421066955/79228162514264337593543950336,10918453852450711534743160523/79228162514264337593543950336]`. A clean-room SciPy/Qhull plus independent tetrahedral integration reconstructs the same incidence and class; Trimesh reads both OBJ and STL as watertight and winding-consistent, with 8 vertices, 12 triangles, 18 unique edges, Euler number 2, volume `0.13764261866940078`, and centre of mass within `1.1e-16` of zero.

## Exact two-control cell and obstruction

On `R={0<=s<=1/5,0<=t<=3/100}`, keep the six boundary vertices fixed and move only the two internal vertices: `p9=Q9/2^32+s*(-64095,-162685,-1048576)/2^20`, `p13=Q13/2^32+t*(-1048576,-1048576,-219488)/2^20`. All 60 nonincident support polynomials have fixed strict sign, so the actual hull stays exactly `(8,18,12)`. The scaled six-volume is `65431030564969203207629252802-61255170908824412511145426944*t+16502980021935997784780242944*s-13917319551898188778594893824*s*t`, with a positive tensor-Bernstein lower bound; exact moment polynomials give the own centroid identically.

The complete exact circuit/equilibrium atlas has exactly two equilibrium walls, meeting once transversely, and exactly four open cells: `(2,2,2)`, `(3,2,3)`, `(3,2,3)`, `(4,2,4)`. Stable `[9,12,13]` and intended stable `[10,11,12]` have all three face components strictly positive on the entire closed rectangle by exact tensor-Bernstein certificates. Hence `S>=2` everywhere in this whole certified cell. This is the precise obstruction: the two internal controls can birth adjacent stable-saddle pairs but cannot remove the persistent extra stable face.

## Smallest unrepresented successor

The minimal nonrepeating compact topology is a nine-vertex disk with three internal vertices `A,B,C` forming a central triangle: `[[A,1,2],[A,2,8],[A,8,B],[B,8,10],[B,10,12],[B,12,C],[C,12,11],[C,11,1],[C,1,A],[A,B,C]]`, plus the four preserved exterior faces, giving global `(V,E,F)=(9,21,14)`. It can couple the persistent stable route and both wall routes in one shared two-cell while allowing the old internal pair to deactivate. A 23-run gauge-fixed numerical probe in this copy found only a hull/area degeneration—best scalar score `-7.774509922011614e-05`—not a strict chamber; this is discovery evidence, not an exclusion.

## Reproducible artifacts

- [Complete exact archive](sandbox:/mnt/data/e10_two_internal_edge_nonwinner.zip) and [SHA-256](sandbox:/mnt/data/e10_two_internal_edge_nonwinner.zip.sha256)
- [Current complete wrapper](sandbox:/mnt/data/steady_comet_92_e10_whole_disk_complete.zip) and [current rerun log](sandbox:/mnt/data/steady_comet_92_e10_whole_disk/current_rerun.log)
- [Full detailed handoff](sandbox:/mnt/data/e10_two_internal_edge_result/RESULT.md)
- [Exact E10 verifier](sandbox:/mnt/data/e10_two_internal_edge_result/verify_source_E10_exact.py), [report](sandbox:/mnt/data/e10_two_internal_edge_result/E10_exact_report.json), [OBJ](sandbox:/mnt/data/e10_two_internal_edge_result/E10_centered.obj), and [STL](sandbox:/mnt/data/e10_two_internal_edge_result/E10_centered.stl)
- [Exact E8A verifier](sandbox:/mnt/data/e10_two_internal_edge_result/verify_E8_exact.py), [H rows](sandbox:/mnt/data/e10_two_internal_edge_result/E8A_H_representation.json), [vertices](sandbox:/mnt/data/e10_two_internal_edge_result/E8A_vertices.csv), [OBJ](sandbox:/mnt/data/e10_two_internal_edge_result/E8A_centered.obj), and [STL](sandbox:/mnt/data/e10_two_internal_edge_result/E8A_centered.stl)
- [Perturbation certificate](sandbox:/mnt/data/e10_two_internal_edge_result/E8A_perturbation_certificate.json), [independent verifier](sandbox:/mnt/data/e10_two_internal_edge_result/verify_E8_independent.py), and [independent report](sandbox:/mnt/data/e10_two_internal_edge_result/E8A_independent_verification.json)
- [Exact two-parameter atlas](sandbox:/mnt/data/e10_two_internal_edge_result/E8_two_parameter_exact_atlas.json), [builder](sandbox:/mnt/data/e10_two_internal_edge_result/build_E8_two_parameter_certificate.py), and [independent 4,941-hull grid check](sandbox:/mnt/data/e10_two_internal_edge_result/E8_family_independent_verification.json)
- [Connected patch complex](sandbox:/mnt/data/e10_two_internal_edge_result/E10_to_E8_patch_complex.json) and [one-command verifier](sandbox:/mnt/data/e10_two_internal_edge_result/[internal-source-reference].sh)
- [Central-triangle probe audit](sandbox:/mnt/data/steady_comet_92_e10_whole_disk/central_triangle_probe/e9_gauge_best_audit.txt) and [raw run ledger](sandbox:/mnt/data/steady_comet_92_e10_whole_disk/central_triangle_probe/e9_gauge_search.json)

## Reusable conclusion

The requested whole residual disk is replaced exactly and robustly, but the Morse block is transported rather than cancelled. `E8A` is an exact open own-centred `(8,18,12)` nonwinner of class `(2,2,2)`. The complete two-control cell is rigorously closed by the global `S>=2` certificate. The next compact architecture not covered by this failure is the three-internal-vertex central-triangle disk, with three ordinary moments retained as dependent hard equations and all actual circuit changes permitted.
