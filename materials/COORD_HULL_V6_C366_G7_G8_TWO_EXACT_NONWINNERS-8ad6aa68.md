# material-8ad6aa68e1c0

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Two exact C366 own211 descendants of the protected-SU hull search

## Evidence status and exact identities
COORD_HULL_V6_C372_FINAL_G7 and COORD_HULL_V6_C372_FINAL_G8 are DIFFERENT rational bodies. Each has V=63,E=183,F=122,C=366, strict(S,U,H)=(2,1,1), weak000 about its own ordinary filled-solid centroid. They are nonwinners, not improvements of the accepted C622 own110 record. They do not improve the archive's smallest own211 complexity either. Their value is a changed low-complexity geometry with a smaller rooted polar-basin bottleneck, and exact manageable coordinates for continuation.

Both are derived from the FINAL checkpoint of V6_372_1 (seed37262,gamma0.0001,perturb0,initialtrust0.005,steps150,actual79 iterations), whose exact binary64 endpoint file SHA256 is 905691e890fdc75d7ecf2fabb698f93339781d99a0882b31fd12de31a802c876. Each coordinate was converted from its float.hex string to the exact binary64 rational, multiplied by the stated integer grid and rounded to nearest integer, ties to even. The FULL resulting rational inputs are below; they suffice to reconstruct these bodies independently of that floating endpoint or optimiser execution. Do not mistake a hash of the endpoint for its recovery data. The numerical method and endpoint preservation are separate from this exact-body recovery capsule.

Authoritative source dependency: NC57 immutable result figure-0398,73935 bytes,SHA256 b6c84be62ea56d1c11575d4d6309563f525d734f79b0ad2a299f0b7abd2ccdd3. Its self-contained RECOVER_NC57.py reconstructs37 exact sources. Required audit units are EXACT.py, EXACT_NEW.py and INDEPENDENT_TRIPLES.py; their complete code is in that immutable capsule. Parent read completely0->eof in this coordinator turn. Optional rooted-cut source is the complete ROOT_CUT_EXACT_V2.py in material [internal-source-reference],12589 bytes,SHA2560491aa00d7307fb0a43a80b62b2690cc8a56699644e7e31e969a88ad8b7150e9.

## Full checks actually executed
For BOTH inputs, the NC57 point audit exhaustively enumerated all supporting point triples, rebuilt maximal supports and true edges, ran independent A and B hull reconstructions, separate filled-volume/first-moment integrations, two distinct all-feature S/U/H and weak-sign tests, and a third centred integration. A uses raw-origin integer determinants and global support/vertex tests; B uses exact plane-pair line clipping, a different interior fan and local face/edge tests. The third integration used122 positive centred tetrahedra and returned exact zero first moments. Independently enumerating all support-plane triples reproduced every vertex and maximal-facet owner set. This is not merely a floating hull or Euler inference.

G7: strictS REPORT[41,74],U REPORT[58],H REPORT[(56,61)],weak000. The stable owners mapped to the frozen FINAL point-row order are [0,2,39] and [18,20,51]. Minimal common centred denominator98 bits; maximal centred integer98 bits; audit raw denominators at most30 bits. Third-integration working denominator104 bits. Exact volume5401438123509222489817/6000000000000000000000.

G8: strictS REPORT[0,95],U REPORT[58],H REPORT[(56,61)],weak000. Stable owners mapped to FINAL point rows are [0,10,39] and [18,20,51]. Minimal common centred denominator111 bits; maximal centred integer111 bits; audit raw denominators at most33 bits. Third-integration working denominator117 bits. Exact volume5401438252823075859621097/6000000000000000000000000.

The first stable carrier changes between grids. Do not merge their face indices or owner triples. Their coordinates are substantially more economical than the accepted C622 construction but costlier than the 60-bit centred denominator of the unmodified NC57 C372 input.

The exact rooted-cut routine was also executed on BOTH new REPORTs. G7 primal rooted margin is about9.402354653834208e-7; polar optimum bottleneck about-0.04947034665617415, polar rootREPORT74, unique tight cut bridgeREPORT51->19. G8 corresponding margins are about9.88541964129174e-7 and-0.04947294159370488, polar rootREPORT95, bridgeREPORT7->51. Both have a sufficient robust two-S polar-generator radius23913/1000000 in the exact componentwise own-centred chart and same-labelled-generator scope proved in [internal-source-reference]. This remains a scoped exclusion, not a physical vertex displacement bound. Compared with the parent polar bottleneck about-0.0908681 this is an improvement of the geometric objective, but the positive primal margin has decreased by roughly two orders of magnitude: an important tradeoff, not unqualified progress toward a robust winner.

## Reconstruction and verification commands
CPython3.13.5, standard library only, assertions enabled. Preserve each JSON block below with exactly one trailing newline as G7/CHECKPOINT.json and G8/CHECKPOINT.json.

 python -B -S RECOVER_NC57.py NC57_SOURCE 4
 python -B -S NC57_SOURCE/EXACT_NEW.py points G7/CHECKPOINT.json G7/proof
 python -B -S NC57_SOURCE/INDEPENDENT_TRIPLES.py G7/proof/REPORT.json G7/TRIPLES.json
 python -B -S ROOT_CUT_EXACT_V2.py G7/proof/REPORT.json G7/ROOT_CUT.json
 python -B -S NC57_SOURCE/EXACT_NEW.py points G8/CHECKPOINT.json G8/proof
 python -B -S NC57_SOURCE/INDEPENDENT_TRIPLES.py G8/proof/REPORT.json G8/TRIPLES.json
 python -B -S ROOT_CUT_EXACT_V2.py G8/proof/REPORT.json G8/ROOT_CUT.json

First reconstruct the NC57 source dependency using its full literal decoder, not a local filename assumed to survive. Output proof directories must not already exist. The point auditor translates the rational input by its arithmetic mean for an interior raw origin and records both that translation and the original-input centroid. The report's `points` minus its `centroid` are exact coordinates with own centre of mass0; `newraw_to_input` is the point-row lineage map. No physical mass is pinned at the old origin.

Expected main terminal markers for each grid:
 NC57_EXACT_BODY_AB_ALL_FEATURES_CENTERED_MASS_PASS points COORD_HULL_V6_C372_FINAL_G7 ... VEFC [63,183,122,366] strict [2,1,1] weak [0,0,0]
 NC57_EXACT_BODY_AB_ALL_FEATURES_CENTERED_MASS_PASS points COORD_HULL_V6_C372_FINAL_G8 ... VEFC [63,183,122,366] strict [2,1,1] weak [0,0,0]
 NC57_INDEPENDENT_ALL_PLANE_TRIPLES_HULL_COMPLETE_PASS
 COORD_ROOT_CUT_EXACT_PASS 63 122 9.402354653834208e-07 -0.04947034665617415 23913/1000000
 COORD_ROOT_CUT_EXACT_PASS 63 122 9.88541964129174e-07 -0.04947294159370488 23913/1000000

Exact bytes and SHA256 receipts:
G7/CHECKPOINT.json 1968 fc96c778a7cbf054f32961720b75f0e2719a60654614f4f231dfdd0014a91388
G7/proof/REPORT.json 19442 2e79def1fe584c45b20cbf703903e45ba6e7d91891815c24620571cdd1c12596
G7/TRIPLES.json 143 74ab04df2673e1e808c3cf8f0a8fff8a17134df309eca7c020ebb1b9434bc8f8
G7/ROOT_CUT.json 27357 8446c50d403c89ae521ef70735bb36abb7bf537ed89d46a91b5ab55ffd29788c
G8/CHECKPOINT.json 2158 c054e2a5cc7ef6c8e0166d589eed26c47fa9739e462eac487ecef03ebfaab991
G8/proof/REPORT.json 21373 c352866aa2eee361c941c064073494ff15560fdc06e959d5b1ae3e4d59eabf41
G8/TRIPLES.json 143 b6e2ea93d994fa66343b4b0c137678aa530000d6e5a6f280ecc84f5d48481b0c
G8/ROOT_CUT.json 31260 1dc8fede3f58e37a40e9c9d9421de113104a6c817ab65f42328138ba7a4b794b

## Complete G7/CHECKPOINT.json
```json
{"endpoint_sha256":"905691e890fdc75d7ecf2fabb698f93339781d99a0882b31fd12de31a802c876","grid":10000000,"identity":"COORD_HULL_V6_C372_FINAL_G7","rounding":"Exact Fraction(binary64 fromhex) times integer grid, nearest ties-to-even","rows":[[-10114093,-1621935,-3022261],[-10103226,-2247279,-2556058],[-10037757,-679808,-3732415],[-9998945,-2969825,-2014094],[-9880227,133641,-4270528],[-9812314,-3730833,-1370018],[-9650731,948968,-4747784],[-9548331,-4424676,-776475],[-9344584,1795577,-5184515],[-9191653,-5080096,-222387],[-8959771,2795414,-5680109],[-8772548,-5700735,415100],[-8567966,3418248,-5977345],[-8296680,-6246901,933556],[-7983024,4264410,-6342628],[-7752559,-6744041,1561160],[-7392447,4932853,-6624020],[-7164325,-7170481,2092958],[-6686122,5649962,-6867009],[-6510232,-7566301,2573487],[-5886816,6388112,-7066826],[-5769044,-7825181,3045470],[-5072417,7018144,-7174371],[-4974996,-7984387,3532337],[-4201422,-8184186,3953507],[-3402696,-8255357,4344295],[-3447873,8168762,-7263231],[-2609509,-8288755,4698397],[-2507989,8668973,-7181412],[-1814077,-8266254,5018308],[-1497925,9186313,-7076451],[-996073,-8153552,5311536],[-569025,9478752,-6901247],[-186917,-8001047,5561911],[100053,-817990,4885812],[419325,9710860,-6679309],[657333,-7770312,5777996],[1560271,9956276,-6378644],[1596076,-7486936,5884152],[1549039,2347442,3553469],[1972839,-2988828,6589171],[2198977,-7130656,6081536],[2578695,10026401,-6027202],[2983623,4687250,1907262],[3028515,-6686050,6152372],[3627667,3649007,2780745],[3526859,10034157,-5648562],[3480363,3020767,-3463898],[3752146,-6257799,6141684],[4221911,-3722153,6447950],[4149399,5333962,1300304],[4408257,-5759068,451936],[4509948,-5717899,6079740],[4514866,10032065,-5224227],[4565807,7554970,-640118],[4673215,5450237,-3962201],[5058038,8634963,-2314082],[5252425,-5213285,5854287],[5448467,9860415,-4762009],[5509057,-5523231,1506678],[5776545,3673600,-1128469],[5799173,-4537361,5729891],[5939269,-5215262,2797763]]}
```

## Complete G8/CHECKPOINT.json
```json
{"endpoint_sha256":"905691e890fdc75d7ecf2fabb698f93339781d99a0882b31fd12de31a802c876","grid":100000000,"identity":"COORD_HULL_V6_C372_FINAL_G8","rounding":"Exact Fraction(binary64 fromhex) times integer grid, nearest ties-to-even","rows":[[-101140928,-16219348,-30222609],[-101032257,-22472785,-25560575],[-100377570,-6798081,-37324154],[-99989454,-29698249,-20140940],[-98802270,1336410,-42705280],[-98123139,-37308333,-13700181],[-96507314,9489681,-47477842],[-95483307,-44246761,-7764750],[-93445840,17955770,-51845149],[-91916533,-50800961,-2223868],[-89597713,27954143,-56801090],[-87725481,-57007348,4151002],[-85679658,34182485,-59773453],[-82966804,-62469015,9335561],[-79830240,42644099,-63426277],[-77525586,-67440413,15611605],[-73924472,49328532,-66240203],[-71643246,-71704811,20929582],[-66861223,56499622,-68670094],[-65102323,-75663007,25734874],[-58868161,63881115,-70668258],[-57690444,-78251808,30454697],[-50724171,70181439,-71743714],[-49749959,-79843875,35323368],[-42014216,-81841860,39535070],[-34026961,-82553565,43442946],[-34478730,81687621,-72632308],[-26095091,-82887554,46983967],[-25079894,86689730,-71814124],[-18140766,-82662539,50183076],[-14979245,91863130,-70764513],[-9960729,-81535515,53115356],[-5690255,94787521,-69012474],[-1869169,-80010469,55619107],[1000533,-8179895,48858115],[4193247,97108597,-66793085],[6573327,-77703116,57779965],[15602714,99562757,-63786442],[15960763,-74869359,58841523],[15490387,23474422,35534693],[19728390,-29888282,65891713],[21989767,-71306560,60815355],[25786950,100264013,-60272023],[29836233,46872502,19072619],[30285153,-66860499,61523723],[36276670,36490067,27807451],[35268588,100341573,-56485619],[34803627,30207671,-34638983],[37521464,-62577986,61416838],[42219114,-37221526,64479496],[41493994,53339619,13003044],[44082572,-57590677,4519361],[45099476,-57178994,60797404],[45148660,100320649,-52242266],[45658070,75549699,-6401181],[46732152,54502368,-39622011],[50580376,86349633,-23140822],[52524251,-52132854,58542873],[54484671,98604154,-47620093],[55090566,-55232312,15066782],[57765453,36736001,-11284688],[57991735,-45373607,57298906],[59392691,-52152619,27977628]]}
```
