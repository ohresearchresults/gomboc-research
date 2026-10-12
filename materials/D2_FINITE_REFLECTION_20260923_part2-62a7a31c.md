# material-62a7a31c8b3d

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# D2_FINITE_REFLECTION_20260923 — Recovery capsule part 2/3

Part 1 is [internal-source-reference] and contains the entire exact auditor. This part contains every rational input, generated input/output byte identity, and the executable recovery/verification command. Part 3 contains numerical provenance; part 1 plus this part suffices to recover the exact objects independently of optimization and every old sandbox.

## Accepted exact nonwinner ledger
The centre is the actual homogeneous filled-volume centroid, computed as exact fractions in the reproduced audits. All five have additionalweak000 and full maximal-complex checks. None is class110. G4/G6 means decimal denominator 10^4/10^6 for the representative H normals and bottom coefficient, not coordinate rounding of a V hull.

* D2_REFLECTED_SEED0_G4: V79/E134/F57, C268, strict(5,5,8).
* D2_REFLECTED_SEED0_G6: V81/E136/F57, C272, strict(5,5,8).
* D2_REFLECTED_SEED1_G4: V85/E140/F57, C280, strict(5,5,8).
* D2_REFLECTED_SEED1_G6: V85/E140/F57, C280, strict(5,5,8).
* D2_ROOTED_00_G6: V99/E166/F69, C332, strict(45,47,90). This preserves a materially negative rooted-chord search outcome: a lower summed barrier objective can coexist with many more equilibria.

These exact values are from the literal inputs and current exhaustive integer audit; any different transient context summary is not an alternative object identity. In particular the rooted control is S45/U47, not S47/U45; its C is332, not272. The four baselines have C268,272,280,280 respectively.

## Recovery source
Write this block as recover_d2.py, LF and one terminal newline: 4162 bytes, SHA256 e073c05d483d94108ac2920bef1131d7e4eedb8bdc06babc393c6c0ecad837ef. Put d2_exact.py from part 1 beside it. Run `python -B -S recover_d2.py`. Expected: five D2_EXACT_H_AUDIT_PASS lines with the counts above and hashes below, followed by D2_FIVE_EXACT_RECOVERY_PASS. The script verifies both inputs and outputs byte-for-byte. Tested with Python3.13.5, standard library only.

```python
"""Recover and exactly verify the five D2_FINITE_REFLECTION_20260923 objects."""
import json,hashlib,pathlib,subprocess,sys
DATA = [{"bottom":17570,"denominator":10000,"name":"D2_REFLECTED_SEED0_G4","representatives":[[6587,411,-16958],[1376,54,-17547],[15671,1387,-14233],[4230,1462,-15223],[21734,952,-9489],[7248,3181,-10081],[22968,14,-5668],[9140,3908,-5060],[21786,955,-3414],[10059,3902,-1223],[19911,1552,-1211],[9934,3600,1329],[16972,1637,1494],[8584,3228,3137],[12519,1313,4191],[6112,2618,4848],[6055,659,6347],[2663,1426,6453],[8467,2438,6989]]},{"bottom":1756995,"denominator":1000000,"name":"D2_REFLECTED_SEED0_G6","representatives":[[658660,41132,-1695753],[137621,5430,-1754722],[1567054,138737,-1423303],[422982,146193,-1522328],[2173374,95178,-948916],[724830,318138,-1008088],[2296802,1445,-566848],[913997,390843,-505969],[2178552,95530,-341440],[1005913,390165,-122323],[1991085,155160,-121099],[993388,359976,132921],[1697215,163707,149425],[858406,322755,313677],[1251853,131302,419147],[611184,261775,484793],[605496,65910,634700],[266280,142551,645347],[846664,243819,698887]]},{"bottom":15428,"denominator":10000,"name":"D2_REFLECTED_SEED1_G4","representatives":[[4909,303,-15118],[960,186,-15425],[10935,1823,-14007],[2039,640,-14739],[18964,1836,-9743],[4846,2421,-10960],[23847,1208,-4263],[7382,3640,-6012],[23461,4,-1419],[9607,3916,-1412],[21529,1329,-823],[11542,3515,2005],[19240,1900,870],[11392,3203,3472],[14206,1584,4066],[8023,2856,4918],[5817,661,6828],[2749,1365,6928],[8569,2556,7397]]},{"bottom":1542845,"denominator":1000000,"name":"D2_REFLECTED_SEED1_G6","representatives":[[490926,30296,-1511812],[95976,18629,-1542507],[1093492,182331,-1400651],[203865,63979,-1473902],[1896435,183561,-974309],[484568,242088,-1095990],[2384724,120825,-426305],[738199,364017,-601163],[2346133,443,-141907],[960704,391589,-141241],[2152917,132913,-82278],[1154228,351522,200455],[1923963,189975,87026],[1139248,320312,347159],[1420630,158404,406559],[802252,285601,491787],[581657,66121,682754],[274869,136510,692839],[856918,255595,739729]]},{"bottom":3043046,"denominator":1000000,"name":"D2_ROOTED_00_G6","representatives":[[965664,35081,-2258315],[73869,18316,-1700060],[1342441,88574,-1273087],[226772,269611,-1496460],[1402447,74830,-770412],[224317,816575,-765369],[1329440,20041,-287300],[415817,870329,-391629],[1191352,133621,-38465],[464171,830359,-93998],[1049569,195048,152398],[529637,718786,165647],[894104,290950,295560],[627786,572950,343580],[742417,339928,407781],[346211,455500,434418],[521589,188628,545512],[143635,261918,525962],[600221,329734,501333]]}]
EXPECTED = {'D2_REFLECTED_SEED0_G4.json': [1036, 'e5fd5e6844e2543b5bf13caa9ae5e312a268bc293c9c018daeb890d0379f0752'], 'D2_REFLECTED_SEED0_G4_audit.json': [19318, 'b610c4e1b4c80595a0f3e65117cb4e39640bc3cb5e7d3abdbf18da0bd93099a5'], 'D2_REFLECTED_SEED0_G6.json': [1154, 'b59d82439a2e886e68d071b79fe2b8590b155d2e32fdb610980598f64f9bdda7'], 'D2_REFLECTED_SEED0_G6_audit.json': [22067, '49ee6762e462ff9a84024f1be2edecb28b0d5f4ad7da34c040a185aaad8f2a3f'], 'D2_REFLECTED_SEED1_G4.json': [1035, '16d3ee3ec9766ac6b26dba9f9f943ab3119449806403a96c4749dc1a3cd453ff'], 'D2_REFLECTED_SEED1_G4_audit.json': [20152, 'e189367d290ab84d51ca54a34f76354246e419d7915aa77574adf1b633e5785c'], 'D2_REFLECTED_SEED1_G6.json': [1153, '26eddd949ac438450d73ae7d5531f9628eda4347bca99bb0797bf092ac47fa3f'], 'D2_REFLECTED_SEED1_G6_audit.json': [22877, '7bdafd1c2d00ad4c3e531346f5839bc471209bb9949f53766db8b1b3c2626b71'], 'D2_ROOTED_00_G6.json': [1143, 'e66c84611050370b3c8100faf2b6a0e0e557b432be83564474be78e4cb0f6e7a'], 'D2_ROOTED_00_G6_audit.json': [27880, '529d458aa97e22ae919d34c47eee7f35684b9e7da3b681720a1e10854e13f54d']}
def check(path):
    raw=path.read_bytes();assert [len(raw),hashlib.sha256(raw).hexdigest()]==EXPECTED[path.name],path.name
for data in DATA:
    p=pathlib.Path(data['name']+'.json')
    p.write_text(json.dumps(data,sort_keys=True,indent=2)+'\n',encoding='utf-8',newline='\n')
    check(p)
    subprocess.run([sys.executable,'-B','-S','d2_exact.py',str(p)],check=True)
    check(pathlib.Path(data['name']+'_audit.json'))
print('D2_FIVE_EXACT_RECOVERY_PASS')
```
