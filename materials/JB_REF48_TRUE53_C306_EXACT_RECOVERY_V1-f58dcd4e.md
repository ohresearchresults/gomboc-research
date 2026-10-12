# material-f58dcd4e248e

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# JB_REF48_TRUE53_G8 — exact C306 own211, complete literal geometry recovery

Status: accepted NON-TARGET control, not own110. This capsule preserves the complete geometry without an originating sandbox. The exact point cloud below consists of all 53 extreme vertices of the previously audited JB_REF48_G8 78-row cloud; deleting its strictly redundant inputs does not change the convex body, mass, or equilibria. It is an explicitly different INPUT SERIALIZATION, not a renamed different geometric body. All quantities below were actually re-executed on this 53-row input after its recovery.

The earlier 78-row serialization was JB_REF48_G8.json,2439B,SHA404f1706651ef885d6ea69104e8159798046a9311a22ccdbf650de0dabb6beee; its audit5620B SHA29b631e8896907dda7e07e6e9198a44e3b2320b7969c293493eb146151a4b65f printed the full 53 extreme rows. The local filesystem then became unavailable before that raw78 or its continuation was durably preserved. Those hashes alone are NOT recoverable raw78/checkpoint sources. In particular later JB_REF48_CONT_G8/G6 own211 C300 receipts existed, but their full point data were not printed or archived before this loss; do not use those continuation names/hashes as exact parents. Recovery of the 53 printed extreme rows below does not require the lost redundant rows or any floating optimizer.

## Exact verifier dependency and commands
The complete immutable `exact_poly.py` is in [internal-source-reference], JB_C168_OWN211_EXACT_RECOVERY_V1.md,13684B,SHA2b1c5045a6bac634a6858e76e723cf3820fe4185a0ef3253bb1a845d696b84e2. Its exact source unit is6134B,SHA898f77989193886996d6f2dc121ccdfdf611b8a9ac52fd3207557eac6a69c0c4. That whole material must be explicitly attached with this one to any fresh worker requiring verification; an ID alone does not deliver its bytes. No other dependency is needed. Standard-library Python3 is sufficient (observed3.13.5).

Write the literal JSON below with LF final newline to JB_REF48_TRUE53_G8.json, write the exact source unit from that dependency, and run:
```
python exact_poly.py JB_REF48_TRUE53_G8.json
```
Observed reconstruction input:1706B SHAef52650d1f2e0976e1ef05ae83ce842ae76b04607e60f9a910d4c743769b83a4.
Observed verification:
```
EXACT_POLY_AUDIT_PASS JB_REF48_TRUE53_G8 (53, 153, 102) [2, 1, 1] additionalweak [0, 0, 0] primitivezero [0, 0, 0] P/Qbars 0 1 Qsum 0.5613951111564266
JB_REF48_TRUE53_G8_AUDIT.json 5627 d13109be7e4070a278d66a38f82a23608b0910165f9b85b215c4bcce2f52fe15
```
The auditor enumerates all supporting triples exactly and explicitly rejects nontriangular maximal facets. It computes true edges, actual filled volume and first moment, strict and closed weak S/U/H and both full rational radial merge-tree landscapes. All 102 maximal facets of this body are triangular. No Euler-only or floating count substitutes for these tests.

## Scientific content and exact invariants
V53/E153/F102,C306,own strict211,additionalweak000,primitivezero000;96 free edges remain under E249. S=[49,90],U=[52],H=[[37,52]] in the exact lexicographic hull order. P has no positive bars. Q has exactly one positive bar: peak90,elder49; component[10,11,16,24,36,50,51,52,63,76,82,84,87,88,89,90,91,92,93,95,96,97,98,99,100],25 facets; cut19=[[5,10],[6,11],[15,16],[11,18],[23,24],[26,36],[38,51],[45,52],[51,59],[63,64],[76,77],[81,82],[84,85],[86,88],[94,95],[77,97],[78,90],[92,101],[93,101]]. Attainingedge84–85; attainingpath[90,92,93,91,88,99,98,95,96,82,84,85,83,69,70,48,49]. Its normalized depth is
1910422100012007629628789062514902137212964682967538244657166793275108825315944057289638415451578940646339706441069/3402990268434470412026047767104693232052597627919669920043064899588580597078586963375841881811937640202404294268440 = .5613951111564266.
Volume=238956409072726900814753/120000000000000000000000.
Actual centroid=[-103553729236749945953748955803/367625244727272155099620000000000,-27501559286828971812430181510357/4779128181454538016295060000000000,-72631440359231855916551962741539/4779128181454538016295060000000000].
Actual first moment=[-448732826692583099132912141813/800000000000000000000000000000000,-27501559286828971812430181510357/2400000000000000000000000000000000,-24210480119743951972183987580513/800000000000000000000000000000000].

This arose from physical outward facet-cap additions followed by unconstrained live-hull root-free joint P/Q descent with the actual centroid. The core joint solver is complete in [internal-source-reference] (20132B,SHA52e84d6f4b5c34e43abd5cf47ece3ce0af50bc3035e9cb35813385e4a3bd532e). Exact old numerical refine_caps.py1906B SHA c40fd8d10f7752b1911a2bdd74dc3a5e53ba966624a3a77f9a2eaf3428cddd3a was lost before its source text was archived; its SHA does not preserve it. A reconstructed implementation must be labelled as such, not claimed byte-identical. The geometric body is fully recovered independently here; the old full producing trajectory is not.

The cap experiment used initial exact JB_CONT211_G8 (literal in verifier dependency), selected48 current facets by descending area/height², outward cap at the facet mean plus .01*RMSradius*unitoutwardnormal, then joint solver1200steps,lr.0008,power.5,pweight3,qweight1,epsilon1e-16,seed0,noise0,gradclip10,record_every100. Live own-center/RMS normalization is an inert similarity. The surviving positiveQ25/cut19 is still deep: reduced scalar depth versus JB_C168 (.69616) is useful but is NOT cancellation, and C306 is not a complexity record. Next continuation should start from the literal recovered53 points, not lost raw78 or an alleged C300 endpoint.

## JB_REF48_TRUE53_G8.json
```json
{"denominator":100000000,"name":"JB_REF48_TRUE53_G8","points":[[-108419680,-10280925,5776723],[-107020179,-10892051,28921744],[-106003805,-16322819,-10379241],[-105153036,-27026836,13198720],[-103378933,-93309,-21846730],[-103125950,903877,46855447],[-99385355,-40589601,-2804328],[-98652763,-33225503,-15297551],[-97859228,-21890866,-31518415],[-95033629,12693448,63832763],[-94423443,13183736,-24349249],[-90844078,-50483030,-18846162],[-90236483,4630574,-45957709],[-88676254,-40819795,-35367678],[-83017025,-27028161,-52520448],[-82813646,22625009,79813870],[-78619473,-58220780,-34052817],[-71525158,-15782251,-67289615],[-71502873,-51662926,-50868239],[-69524242,15460415,-65174104],[-68733571,-69140047,-21921886],[-66793853,29998604,94073286],[-61362706,-50598859,-61915860],[-60492783,-66893875,-45378338],[-58757843,733875,-76586282],[-56010727,-75858414,-30903651],[-49816081,-46821964,-72257845],[-46762930,35683111,106564350],[-46523442,-27577988,-78077884],[-43766974,-62909426,-60533523],[-37787442,17956296,-81994935],[-37374421,-78101271,-45202607],[-32325518,-29226185,-83866409],[-29657556,-53171013,-74559395],[-22256434,41931855,115205193],[-18881347,-74075944,-56184359],[-10882441,-51320271,-78248089],[-1484051,-29730599,-85193764],[2067778,-81003192,-10886601],[2200816,-59614504,-69804944],[6244973,-74825643,-49110171],[7024954,48758431,118385858],[11328544,3018632,-75306242],[13989585,-71893807,-45492196],[15786592,6106563,72746694],[37330102,55246547,113983809],[55222823,-8639145,-53249415],[59089123,-20924475,-41305857],[59933639,-31933890,-22474421],[69556992,31198454,-49160440],[73757453,62216001,98984425],[102199083,65462332,76296956],[160050838,71195398,-3880501]]}
```
