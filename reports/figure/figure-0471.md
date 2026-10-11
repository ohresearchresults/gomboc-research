# figure-0471

Historical AI scientific report · saved 2026-09-22 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Steady Comet 83 — exact one-cap obstruction and two-cap packet turnover

## Outcome

No exact strict110/additionalweak000 body was found. The requested first question is closed exactly for literal parent `SC83_BF35_REPLACE5_PACKET24_G4`: its complete 24-vertex physical packet is **not strictly linearly separable** from the 42 retained vertices. Hence the conditional fixed-old-vertex one-cap `V62/E93/F33/C186` architecture does not exist for this parent. The active branch memory identifies parent `figure-0467` (SHA-256 `c2b59f1bc19ca564bc7e3ed9432e0d24ff61b02d7274838f277e0ef3b9d99837`) as `V66/E99/F35/C198`, strict121/weak000/Q0 with packet24/20. :contentReference[oaicite:0]{index=0} Its literal payload and exact source receipts are authoritative. :contentReference[oaicite:1]{index=1}

The minimum number of strict old-vertex-preserving caps needed to cover all 24 old packet vertices is **exactly two**. A 2-for-2 active-support replacement using two simple rational caps removes every old packet vertex while retaining all 42 old complement vertices, but the rebuilt actual-centroid body becomes strict `(18,10,26)` and recreates a large positive polar landscape. This is a durable topology-control nonwinner, not an accepted successor.

I read the continuation journal through EOF; mounted file receipt is 143951 bytes, SHA-256 `170db21ff31da09a7383327290b5bc1e539b571c5cde9b4cdc69f042d2689ce4`. I also re-read and executed the exact parent source `BF35_PACKET24_RECOVER.py`, 15772 bytes, SHA-256 `590eb1e51405f5441ea1ed2e75406138a9be723aace312aeb0ab25eecff38359`.

## 1. Exact separation obstruction

Parent packet:
```text
[0,1,2,3,4,5,6,7,8,9,10,11,17,20,21,23,24,25,34,37,38,39,46,47]
```

A point in the relative interior of packet triangle `[9,37,47]` is exactly the same point as a point in the relative interior of retained segment `[22,40]`.

Homogeneous parent vertices `(x_num,y_num,z_num,den)`:
```text
v9  = (-549665000,-13590000,144565000,835421409)
v37 = (-4822620000,303498865000,-397953565000,734015704611)
v47 = (76122894000,191736818000,-91733688000,345182808491)
v22 = (-28660941770,36905999740,3062668146,94269089849)
v40 = (385555645,-1358847205,-2650962451,5200264873)
```

Positive packet weights:
```text
λ9  = 525135952716041589288764563335992743260143181543/1071060342339989472377648927443728739875898010500
λ37 = 45781242882015685192367938439135917834474394301/535530171169994736188824463721864369937949005250
λ47 = 90872380771983302540829697445892832189361208071/214212068467997894475529785488745747975179602100
```

Positive retained weights:
```text
μ22 = 5161492821296408099162486019068312802478024351/6426362054039936834265893564662372439255388063
μ40 = 1264869232743528735103407545594059636777363712/6426362054039936834265893564662372439255388063
```

Both weight sets sum exactly to 1 and
```text
λ9*v9 + λ37*v37 + λ47*v47 = μ22*v22 + μ40*v40 = q
```
with
```text
q = (
-1475486304247386423068026612662934160679981350/6426362054039936834265893564662372439255388063,
 563396875728195214621595563265810411123341580/2142120684679978944755297854887457479751796021,
-477108553926704902247232620504304184580868290/6426362054039936834265893564662372439255388063)
```
approximately `(-0.22959900046711826,0.2630089330435477,-0.07424240183087262)`.

Equivalently, triangle `[9,37,47]` lies in
```text
9327619480157589952962215*x
-14498032747038305940969959*y
-216209378806492962508979*z
+5938672329829808992700000 = 0,
```
while retained vertices22 and40 evaluate with opposite strict signs. Therefore `conv(packet)∩conv(retained)≠∅`; a single strict separator is impossible. This is an exact rational certificate, not a numerical LP failure.

## 2. Exact minimum two-cap cover

Two caps:
```text
CAP1: -25*x -25*y -5*z <= 9
CAP2:       15*y -25*z <= 14
```
keep every retained vertex strictly inside. CAP1 rejects old packet vertices
```text
[0,1,2,3,4,5,6,7,8,9,10,11,17,20,21,23,24]
```
and CAP2 rejects
```text
[20,25,34,37,38,39,46,47].
```
Their union is all 24 packet vertices. Since one cap is impossible and these two suffice, the minimum cover number under the retained-vertex strictness requirement is exactly two.

For fixed normals `n1=(-25,-25,-5)`, `n2=(0,15,-25)`, the open offset rectangle
```text
332765750000/40347733449 < h1 < 324535300000/32658023069
244669610000/18186581257 < h2 < 5169394470000/345182808491
```
i.e.
```text
8.247445929537028 < h1 < 9.937383512600274
13.453304199535955 < h2 < 14.975816705931873
```
keeps all retained vertices strict and guarantees coverage by the displayed packet sets. Exact widths are
```text
2226792239118162950000/1317677209759304934981
9557869445943790280000/6277695195141041053187.
```
This is a sign-pattern/coverage rectangle only; I do not assert constant secondary incidence throughout it.

## 3. Exact `SC83_BF35_CAP2_TURNOVER_G4`

At `h1=9,h2=14`, adding the caps makes old support inputs0 and8 inactive:
```text
old0 = [-9597,-1911,-8888,10000]
old8 = [8653,2816,-16402,10000].
```
Removing those and retaining the caps gives this complete active 35-row input:
```json
[[5940,-21966,12330,10000],[-3565,-11566,19679,10000],[-10450,14813,-7021,10000],[12742,-19585,-1317,10000],[15623,-12580,-9222,10000],[14388,-5675,-14615,10000],[12347,8530,-9554,10000],[-3698,17983,5678,10000],[-10231,3210,18702,10000],[1875,17326,141,10000],[-8459,-2975,20153,10000],[-12905,7486,-8878,10000],[-9765,17843,1405,10000],[494,-16683,17384,10000],[-9265,17774,-1933,10000],[-10698,5673,17646,10000],[9928,-21771,4765,10000],[14544,-16380,-5876,10000],[12444,-2244,-16648,10000],[11230,5364,-14490,10000],[8881,-29,-18310,10000],[-9944,17443,4550,10000],[-11512,9662,14926,10000],[-10115,81,19337,10000],[-4436,18247,-3171,10000],[-6531,-6901,20349,10000],[-12003,15052,8092,10000],[-12171,12594,11656,10000],[-11908,14037,10055,10015],[-11098,7965,16569,10098],[-11191,16296,6148,9982],[-118072,113520,134887,100551],[14943,-9383,-12716,10042],[-25,-25,-5,9],[0,15,-25,14]]
```
Input receipt: 899 bytes, SHA-256 `f7304d0b8193d8dde8516a987ed6d1fccf0f853b78f971340730b0a05e6408a1`.

Exact maximal complex:
```text
V=66 E=99 F=35 C=198; 2E=3V.
face histogram: 5x3,8x4,9x5,8x6,2x8,1x10,1x14,1x18.
```
All 42 retained old vertices survive; all 24 old packet vertices disappear; exactly 24 new vertices appear. Thus this is a genuine whole-old-packet turnover.

Actual uniform volume is approximately `0.7078546952263959`; actual filled-volume centroid is approximately
```text
(0.22596298410758153,0.14135474275253543,0.12716710856895944).
```
Exact fractions and all maximal face cycles/true edges are regenerated in the audit report. Common own-centred coordinate denominator: 3837 bits.

Strict census `(S,U,H)=(18,10,26)`, additional weak `000`, primitive-zero `000`.

S:
```text
[0,1,3,4,5,6,7,8,9,10,13,15,17,25,29,31,33,34]
```
U:
```text
[0,13,20,32,44,46,47,50,51,65]
```
H:
```text
[[2,13],[7,36],[10,49],[11,52],[13,20],[17,56],[18,57],[19,59],
 [21,32],[24,44],[27,34],[27,64],[28,55],[32,36],[35,53],[38,58],
 [40,62],[42,61],[43,60],[44,46],[45,47],[46,47],[46,65],[48,50],
 [50,51],[51,54]]
```

### Complete P/Q topology

P roots:
```text
[0,13,20,32,44,46,47,50,51,65]
```
Nine positive P bars; `TP ∈ [743460918761,743460918762)/10^12`. Complete bar topology (`death` is the attaining true edge):
```json
[{"peak":13,"elder":20,"death":[13,20],"component":[13],"cut":[[13,2],[13,14],[13,20]],"path":[13,20]},{"peak":0,"elder":20,"death":[2,13],"component":[0,2],"cut":[[0,1],[0,3],[2,13],[2,14]],"path":[0,2,13,20]},{"peak":44,"elder":20,"death":[24,44],"component":[44],"cut":[[44,24],[44,38],[44,46]],"path":[44,24,14,13,20]},{"peak":46,"elder":20,"death":[44,46],"component":[46],"cut":[[46,44],[46,47],[46,65]],"path":[46,44,24,14,13,20]},{"peak":47,"elder":20,"death":[45,47],"component":[47],"cut":[[47,45],[47,46],[47,51]],"path":[47,45,20]},{"peak":50,"elder":20,"death":[48,50],"component":[50],"cut":[[50,37],[50,48],[50,51]],"path":[50,48,45,20]},{"peak":51,"elder":20,"death":[50,51],"component":[51],"cut":[[51,47],[51,50],[51,54]],"path":[51,50,48,45,20]},{"peak":20,"elder":65,"death":[46,65],"component":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,27,29,30,31,33,34,35,37,38,39,40,42,43,44,45,46,47,48,50,51],"cut":[[7,36],[10,41],[10,49],[11,28],[11,52],[15,28],[16,25],[17,56],[18,57],[19,59],[21,32],[22,26],[27,64],[30,25],[34,63],[35,53],[38,58],[40,62],[42,61],[43,53],[43,60],[46,65],[51,54]],"path":[20,45,47,46,65]},{"peak":32,"elder":65,"death":[21,32],"component":[32],"cut":[[32,21],[32,26],[32,36]],"path":[32,21,12,3,0,2,14,24,44,46,65]}]
```

Same-physical-centre Q roots:
```text
[0,1,3,4,5,6,7,8,9,10,13,15,17,25,29,31,33,34]
```
Seventeen positive Q bars; `TQ ∈ [3216963882168,3216963882169)/10^12`. Complete bar topology:
```json
[{"peak":9,"elder":7,"death":[7,9],"component":[9],"cut":[[9,1],[9,6],[9,7],[9,13],[9,24],[9,34]],"path":[9,7]},{"peak":13,"elder":0,"death":[0,13],"component":[13],"cut":[[13,0],[13,1],[13,6],[13,9],[13,33]],"path":[13,0]},{"peak":1,"elder":0,"death":[1,13],"component":[1],"cut":[[1,7],[1,9],[1,13],[1,25],[1,33]],"path":[1,13,0]},{"peak":3,"elder":0,"death":[3,16],"component":[3],"cut":[[3,6],[3,16],[3,17],[3,33]],"path":[3,16,0]},{"peak":17,"elder":4,"death":[4,17],"component":[17],"cut":[[17,3],[17,4],[17,6],[17,32],[17,33]],"path":[17,4]},{"peak":4,"elder":0,"death":[3,17],"component":[4,17],"cut":[[4,5],[4,6],[4,32],[17,3],[17,6],[17,32],[17,33]],"path":[4,17,3,16,0]},{"peak":15,"elder":29,"death":[15,29],"component":[15],"cut":[[15,7],[15,8],[15,22],[15,23],[15,29],[15,33]],"path":[15,29]},{"peak":25,"elder":0,"death":[1,25],"component":[25],"cut":[[25,1],[25,7],[25,10],[25,33]],"path":[25,1,13,0]},{"peak":8,"elder":29,"death":[8,15],"component":[8],"cut":[[8,7],[8,10],[8,15],[8,23]],"path":[8,15,29]},{"peak":31,"elder":29,"death":[22,31],"component":[31],"cut":[[31,7],[31,22],[31,27],[31,28]],"path":[31,22,29]},{"peak":10,"elder":0,"death":[10,25],"component":[10],"cut":[[10,7],[10,8],[10,23],[10,25],[10,33]],"path":[10,25,1,13,0]},{"peak":5,"elder":0,"death":[5,32],"component":[5],"cut":[[5,4],[5,6],[5,18],[5,19],[5,20],[5,32]],"path":[5,32,4,17,3,16,0]},{"peak":29,"elder":0,"death":[8,10],"component":[8,15,22,29,31],"cut":[[8,7],[8,10],[8,23],[15,7],[15,23],[15,33],[22,7],[22,27],[22,33],[29,7],[31,7],[31,27],[31,28]],"path":[29,15,8,10,25,1,13,0]},{"peak":7,"elder":0,"death":[7,31],"component":[7,9,21],"cut":[[7,1],[7,8],[7,10],[7,12],[7,15],[7,22],[7,24],[7,25],[7,28],[7,29],[7,30],[7,31],[9,1],[9,6],[9,13],[9,24],[9,34],[21,12],[21,30]],"path":[7,31,22,15,8,10,25,1,13,0]},{"peak":6,"elder":0,"death":[5,6],"component":[6,19],"cut":[[6,0],[6,3],[6,4],[6,5],[6,9],[6,13],[6,16],[6,17],[6,34],[19,5],[19,18],[19,20],[19,34]],"path":[6,5,4,17,3,16,0]},{"peak":34,"elder":0,"death":[6,34],"component":[34],"cut":[[34,2],[34,6],[34,9],[34,11],[34,19],[34,20],[34,24],[34,33]],"path":[34,6,4,17,3,16,0]},{"peak":33,"elder":0,"death":[0,33],"component":[33],"cut":[[33,0],[33,1],[33,2],[33,3],[33,10],[33,11],[33,13],[33,15],[33,16],[33,17],[33,20],[33,22],[33,23],[33,25],[33,26],[33,27],[33,32],[33,34]],"path":[33,0]}]
```

The recovery audit emits every exact birth/death level in addition to these complete components, cuts and paths. The important conclusion is that deleting every old packet vertex does **not** imply cancellation of the equilibrium packet: after actual mass rebuilding, many new P roots and Q bars are born.

## 4. Additional exact controls and finite metric evidence

Exact offset controls inside the cover rectangle:
```text
(8.3,13.5) -> strict(17,7,22), weak000, Pbars6, Qbars16, C198
(8.3,14.9) -> strict(18,9,25), weak000, Pbars8, Qbars17, C198
(9.8,13.5) -> strict(18,10,26), weak000, Pbars9, Qbars17, C198
(9.8,14.9) -> strict(19,8,25), weak000, Pbars7, Qbars18, C198.
```
Four lower-left controls, including exact `(h1,h2)=(33/4,673/50)=(8.25,13.46)`, all gave strict `(17,7,22)`, weak000, Pbars6, Qbars16, C198. This is finite exact evidence only, not a complete offset-chart exclusion.

A separate finite floating SPD-metric scout on the exact `(9,14)` geometry reached numerical S2/U2. Two checkpoints:
```text
G1=[[2.8031828543099926,-0.11781704549251884,0.11635293285725273],
    [-0.11781704549251884,0.27489373283067287,-0.0359681308879609],
    [0.11635293285725273,-0.0359681308879609,1.3299411639060061]]
numeric S=[0,9], U=[0,65].

G2=[[1.350020996252005,0.01389585097886214,0.1344054299293896],
    [0.01389585097886214,0.31645875267406137,0.15432931191124574],
    [0.1344054299293896,0.15432931191124574,2.429074089268606]]
numeric S=[0,9], U=[20,65].
```
These are not promoted: no rational freeze, mixed-H or weak audit was performed. They only motivate an exact fixed-incidence Gram-cell continuation.

## 5. Recovery capsule

Exact dependency:
```text
parent assignment figure-0467
parent result SHA c2b59f1bc19ca564bc7e3ed9432e0d24ff61b02d7274838f277e0ef3b9d99837
BF35_PACKET24_RECOVER.py 15772 bytes
SHA 590eb1e51405f5441ea1ed2e75406138a9be723aace312aeb0ab25eecff38359
```
The literal parent payload contains the complete parent-source decoder and replay markers. :contentReference[oaicite:2]{index=2}

The new complete verifier patch `SC83_CAP2_CERT.py` is 6395 bytes, SHA-256 `2621f3baf946e585200f264c90c2a1a1ab3a91ae15f69eb9193fb562cbde79f6`. The following source-only decoder contains its complete bytes; compressed payload is 2804 bytes, SHA-256 `2181793620d5f4a1135e3bd78eb1f414820f7eb277248e6c94fe4f0dfcc5c0a1`.

```python
import base64,hashlib,lzma,pathlib
B64='''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'''
x=base64.b64decode(B64)
assert len(x)==2804 and hashlib.sha256(x).hexdigest()=='2181793620d5f4a1135e3bd78eb1f414820f7eb277248e6c94fe4f0dfcc5c0a1'
b=lzma.decompress(x)
assert len(b)==6395 and hashlib.sha256(b).hexdigest()=='2621f3baf946e585200f264c90c2a1a1ab3a91ae15f69eb9193fb562cbde79f6'
pathlib.Path('SC83_CAP2_CERT.py').write_bytes(b)
print('SC83_CAP2_CERT_SOURCE_RECOVERY_PASS',len(b),hashlib.sha256(b).hexdigest())
```

Run:
```text
python -B -S RECOVER_SC83_CAP2_CERT.py
python -B -S SC83_CAP2_CERT.py
```
where the first command names the decoder above after saving it as `RECOVER_SC83_CAP2_CERT.py`, and the exact parent source is in the same directory.

Observed exact markers:
```text
SC83_CAP2_CERT_SOURCE_RECOVERY_PASS 6395 2621f3baf946e585200f264c90c2a1a1ab3a91ae15f69eb9193fb562cbde79f6
SC83_PACKET24_ONE_CAP_IMPOSSIBLE_TWO_CAP_COVER_PASS
SC83_BF35_CAP2_TURNOVER_EXACT_PASS 1206103 b6505ea6c16041b34150e26c0b4af89837addd13fde164a3f5102f03b0f71341
```

Generated outputs:
```text
SC83_BF35_CAP2_TURNOVER_G4.json
899 bytes
SHA f7304d0b8193d8dde8516a987ed6d1fccf0f853b78f971340730b0a05e6408a1

SC83_BF35_CAP2_TURNOVER_G4_A.json
1206103 bytes
SHA b6505ea6c16041b34150e26c0b4af89837addd13fde164a3f5102f03b0f71341
```
Evidence tier: one exhaustive exact H-poly mechanics implementation with the parent source's three exact mass identities; no second independent full mechanics audit is claimed.

## 6. Most useful continuation

1. The fixed-old-vertex **one-cap C186 path is exactly blocked** by the triangle/segment convex-hull intersection.
2. The smallest strict old-vertex-preserving packet cover is **two caps**, but exact whole-packet turnover alone transfers rather than annihilates the equilibrium structure.
3. To reopen a true one-cap C186 route, move at least one carrier in the exact obstruction set `{9,37,47,22,40}` by a coordinated support replacement, then rerun the exact separation test.
4. Independently, the two-cap C198 body is a focused fixed-incidence affine-metric problem: physical U signs are linear in SPD `G`, stable/polar signs are dual signs under `G^-1`, and mixed-H must be included. The finite S2/U2 checkpoints make exact Gram-cell feasibility more targeted than adding further arbitrary caps.
5. Do not repeat literal one-support deletion; that layer is already closed. Do not optimize TP alone: this two-cap body has lower TP than the parent while being mechanically much worse.

Final acceptance still requires exact own-centred strict110, additionalweak000 and E<=249. No such body is claimed here.
