# material-a32c686dfc2d

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# D2_AXIS_FINITE_20260923 — exact finite symmetry-stratum constructions
This capsule and its explicitly required source [internal-source-reference] recover all 18 tested homogeneous rational H bodies and their complete exact audit outputs. No110 body is claimed. These are genuinely changed maximal complexes with some horizontal normal components set to exactly zero, not a tolerance declaration that short reflected edges ceased to exist.

Accepted nonwinning examples include D2_AXIS_S0_T10_G4: V79/E130/F53,C260,strict334,additional weak000; G6 has the same counts and more arithmetic. Coarser G3 has85/140/57,C280,334,weak000,centred scale1828bits instead of2763bits forG4 and4430 forG6. Distinct seed1 coarse D2_AXIS_S1_T30_G3 has81/131/52,C262,strict233,weak000,1827bits. It is not an S1 body: rounding makes the nominal bottom plane non-facial and its stable carriers are paired. Seed1 G4/G6 atT30 have85/136/53,C272,334,weak000. TheT3/T10/T30 names are literal experiment identities; repeated geometry with different names is retained, not counted as independent evidence.

Provenance: two explicit DLV-inspired independent-H seeds, set abs(horizontal normal component)<delta to zero for delta=.003,.01,.03, then freeze common integer RHS10^g for g3,4,6. The exact frozen integers below, NOT a fresh floating regeneration, define these objects. Source-complete numerical seed/scanning provenance is in the direct/quotient capsule; it is not needed to recover these exact bodies. All facets are maximal, all edges true, centroid the filled-volume centroid; the polar is based at that physical centroid. Exact audits exhaust integer H triples, test all supports, orient maximal polygons, verify two-owner edges/Euler/connectivity, recompute volume mass from two origins, crosscheck direct facet feet against the polar, and test all vertex and mixed-edge strict/weak signs. This is one exact implementation with internal crosschecks, not two independent proof implementations.

## Exact dependency and commands
Read [internal-source-reference] completely and write its full d2_exact.py code:7931bytes,SHA256 141ad514d226afe665910f93da6569e463b54621494d556f79aa2c9df42e221c. Save the block below as axis_recover.py,LF with terminal newline:7012bytes,SHA256 889b465f097ea1ba612c8c3d0a6153b42f1c583318748b9b237ea34781548196. Runtime CPython3.13.5 standard library only; no NumPy/SciPy/Torch or original sandbox is needed. Reconstruction and full verification command: python -B -S axis_recover.py. It writes NAME.json and NAME_audit.json for each literal name. EXPECTED stores input bytes/hash, output bytes/hash,V/E/F,strict(S,U,H),additionalweak in that order. Markers D2_AXIS_EXACT_PASS for each and D2_AXIS_FINITE_RECOVERY_PASS18 at end. A fresh separate directory replay reproduced all18 input and output bytes/hashes. Hash matching identifies the recovered exact artifacts; scientific evidence is their complete exact audits, not the hashes alone.

```python
"""D2_AXIS_FINITE_20260923 exact recovery; CPython3.13.5, standard library only.
Dependency: d2_exact.py from [internal-source-reference].
All literal integer seeds below are frozen inputs, not regenerated floating samples.
"""
from pathlib import Path
import json,hashlib
from d2_exact import audit
BASES={
(0, 3):(1757,[[659,-41,-1696],[138,5,-1755],[1567,-139,-1423],[423,146,-1522],[2173,-95,-949],[725,318,-1008],[2297,0,-567],[914,391,-506],[2179,96,-341],[1006,390,-122],[1991,155,-121],[993,360,133],[1697,164,149],[858,323,314],[1252,131,419],[611,262,485],[605,66,635],[266,143,645],[847,244,699]]),
(0, 4):(17570,[[6587,-411,-16958],[1376,54,-17547],[15671,-1387,-14233],[4230,1462,-15223],[21734,-952,-9489],[7248,3181,-10081],[22968,0,-5668],[9140,3908,-5060],[21786,955,-3414],[10059,3902,-1223],[19911,1552,-1211],[9934,3600,1329],[16972,1637,1494],[8584,3228,3137],[12519,1313,4191],[6112,2618,4848],[6055,659,6347],[2663,1426,6453],[8467,2438,6989]]),
(0, 6):(1756995,[[658660,-41132,-1695753],[137621,5430,-1754722],[1567054,-138737,-1423303],[422982,146193,-1522328],[2173374,-95178,-948916],[724830,318138,-1008088],[2296802,0,-566848],[913997,390843,-505969],[2178552,95530,-341440],[1005913,390165,-122323],[1991085,155160,-121099],[993388,359976,132921],[1697215,163707,149425],[858406,322755,313677],[1251853,131302,419147],[611184,261775,484793],[605496,65910,634700],[266280,142551,645347],[846664,243819,698887]]),
(1, 3):(1543,[[491,-30,-1512],[96,19,-1543],[1093,-182,-1401],[204,64,-1474],[1896,-184,-974],[485,242,-1096],[2385,-121,-426],[738,364,-601],[2346,0,-142],[961,392,-141],[2153,133,-82],[1154,352,200],[1924,190,87],[1139,320,347],[1421,158,407],[802,286,492],[582,66,683],[275,137,693],[857,256,740]]),
(1, 4):(15428,[[4909,-303,-15118],[960,186,-15425],[10935,-1823,-14007],[2039,640,-14739],[18964,-1836,-9743],[4846,2421,-10960],[23847,-1208,-4263],[7382,3640,-6012],[23461,0,-1419],[9607,3916,-1412],[21529,1329,-823],[11542,3515,2005],[19240,1900,870],[11392,3203,3472],[14206,1584,4066],[8023,2856,4918],[5817,661,6828],[2749,1365,6928],[8569,2556,7397]]),
(1, 6):(1542845,[[490926,-30296,-1511812],[95976,18629,-1542507],[1093492,-182331,-1400651],[203865,63979,-1473902],[1896435,-183561,-974309],[484568,242088,-1095990],[2384724,-120825,-426305],[738199,364017,-601163],[2346133,0,-141907],[960704,391589,-141241],[2152917,132913,-82278],[1154228,351522,200455],[1923963,189975,87026],[1139248,320312,347159],[1420630,158404,406559],[802252,285601,491787],[581657,66121,682754],[274869,136510,692839],[856918,255595,739729]]),
}
EXPECTED={
'D2_AXIS_S0_T10_G3':[976,'29b8c647f7fffaed08bb1f7bcdfd5d93bb53890a9efac1e3a448a631ab0045a9',18912,'33e657f12975b8f2ae36d219881594f722be848d04e47b44b84e3a6bc5f37c6f',85,140,57,[3,3,4],[0,0,0]],
'D2_AXIS_S0_T10_G4':[1033,'368e8294eb64507b6ade790b64f973b03f0a007b300d6338d1840731a36b4d80',18958,'97b0a25c2b92d9b14f5b57388dff620bc988bb9b3dc7a77a5d707d31d1755b75',79,130,53,[3,3,4],[0,0,0]],
'D2_AXIS_S0_T10_G6':[1147,'8e82af4da9ef8dea0f47845d67fc02321c04cdeef250d25e26210fb8ef8f230e',21239,'faa5b058294d68d742a3c14be45632a96d51b1029c712dc84d1609b855473cb2',79,130,53,[3,3,4],[0,0,0]],
'D2_AXIS_S0_T30_G3':[976,'3f03ea9fd428571cc568ac04660069ccac7f04520a03217dca86a933cdada324',18912,'2a253b0c1bd273baf9f15934482936a7e0eab14fe59ac818ecc6eaf297a28ea7',85,140,57,[3,3,4],[0,0,0]],
'D2_AXIS_S0_T30_G4':[1033,'0c0191d214d097242e604a4fe5dce1fd56c1e9271f98bb24390c98e66916aced',18958,'cb1152e0bd7e96f41e6bbead9a4dcad91154e5f677d2f45ed1504e6760b0f012',79,130,53,[3,3,4],[0,0,0]],
'D2_AXIS_S0_T30_G6':[1147,'0f3395b795b94ed58896cea63154158a13dad1c751fd1cbb2582ad25429f3d67',21239,'c8132ba24c4f36419728874b43c634291303895b70177db777cea502a0b632fd',79,130,53,[3,3,4],[0,0,0]],
'D2_AXIS_S0_T3_G3':[975,'21f03fb53ec533468f33f92845779f5a6d3e7d36abf1441b878d4288a2eae777',19097,'9ea3138242b233536214f7c4385fc6b2888b229dcf03fc3e35f8514661cde1a1',85,142,59,[3,5,6],[0,0,0]],
'D2_AXIS_S0_T3_G4':[1033,'33dc45d23e46f330ebaff70b0e1127db4a097f2f7e25979a9a7a0c1a214d80d7',19117,'a8911a211fbb54dafd94edfd7de96314954ba3373a36a9c3d7bba2948da59fb7',79,132,55,[3,5,6],[0,0,0]],
'D2_AXIS_S0_T3_G6':[1149,'f145944d686adcf7dc37ddd30be63767233e0635d081d17a10a252bcbeca9b87',21847,'05985c43a26fbe0977a5a56a1db538a706dc396c809b48b0b6afcb58c21f6298',81,134,55,[3,5,6],[0,0,0]],
'D2_AXIS_S1_T10_G3':[977,'1b52c87770f8a2ae5614af2c5edc643e8959612fcbb5bcd71abb62ff82bc04d5',18360,'ddd76a7435a37b6f60c4647b79f4cbc349fb414b599a6aafa174f62db5909b0d',82,134,54,[2,4,4],[0,0,0]],
'D2_AXIS_S1_T10_G4':[1035,'61367f2cdb37cf7bdf5c32661db25f255d9cd2cce1b06d5f04cc82dc9c682b68',20057,'21e57f3e71bda9f0ed5e40f116f57c66f94d1cf8d84c96ce6b649b2bc18ffbf8',85,138,55,[3,5,6],[0,0,0]],
'D2_AXIS_S1_T10_G6':[1151,'77a742c86c5150f8d630a389f7cbbe2ec6dfa82d5ec1528c96c8a330ddb293bd',22675,'3039a472c030c007ab97197e0169608ae0314d296b90a7d436c171aa45f1a590',85,138,55,[3,5,6],[0,0,0]],
'D2_AXIS_S1_T30_G3':[976,'7bb8f8ea5b1e1e1e0cc095b6f891a3614f3ed7fa09fcbbf0ef1e95481cd26c88',17991,'033d13ed8633ddec05324f64e97726cc2a38d5b943f5e7d14d3fb9b1206a32cc',81,131,52,[2,3,3],[0,0,0]],
'D2_AXIS_S1_T30_G4':[1033,'caad93670a3e98bd91444035b50bf2512a134862bdb310f24c7a77df7e7bbb5d',19875,'2b4607599ffb847484c5bc3d826ec307ecf17ff2b8919e869b950d04e5c773ae',85,136,53,[3,3,4],[0,0,0]],
'D2_AXIS_S1_T30_G6':[1147,'d26cb8aa7478f1e2ce8a3933714c78c0a1677462c1d97d2be3d591a1b40bfd59',22539,'5b5e5eacc3c2d80fc0fe94943b206003b49516bec8b4303e8d876dd4898f9128',85,136,53,[3,3,4],[0,0,0]],
'D2_AXIS_S1_T3_G3':[976,'09118c07574a1ae38e6618c82fbe534b989872833f0072395f7b44f19d76c152',18359,'735b0a4e11d0e0b1a35e7be145140dabd75df2df06e7da5f3ffc85f1a89198e3',82,134,54,[2,4,4],[0,0,0]],
'D2_AXIS_S1_T3_G4':[1034,'33926865cccfd6eb6152cf4b4a66a0d6567197509760b9a0e09892ef918d693f',20056,'37021d76cd2c12085a173aa57a5332ce148ffac8d14194dd5270c889d1b148a1',85,138,55,[3,5,6],[0,0,0]],
'D2_AXIS_S1_T3_G6':[1150,'5fba10d3134a9b98fdf99114b5b93a9152ce8d0f36c04b2f7cfbaee55da0b6e1',22674,'a5dbc0cf16da5a6612de1e832dfbfae92189b9ffe1202ad46786c5ca6684a95c',85,138,55,[3,5,6],[0,0,0]],
}
def raw(x):return (json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
def check(b,n,h):assert len(b)==n and hashlib.sha256(b).hexdigest()==h
check(Path('d2_exact.py').read_bytes(),7931,'141ad514d226afe665910f93da6569e463b54621494d556f79aa2c9df42e221c')
for seed in [0,1]:
 for t in [3,10,30]:
  for g in [3,4,6]:
   name=f'D2_AXIS_S{seed}_T{t}_G{g}'
   bottom,r=BASES[seed,g];r=[a[:] for a in r]
   if (seed==0 and t>=10) or (seed==1 and t==30):r[1][1]=0
   data=dict(name=name,denominator=10**g,representatives=r,bottom=bottom)
   e=EXPECTED[name];b=raw(data);check(b,e[0],e[1]);Path(name+'.json').write_bytes(b)
   a=audit(data);b=raw(a);check(b,e[2],e[3]);Path(name+'_audit.json').write_bytes(b)
   assert [a['V'],a['E'],a['F'],a['strict'],a['additional_weak']]==e[4:]
   print('D2_AXIS_EXACT_PASS',name,a['V'],a['E'],a['F'],a['strict'],a['additional_weak'],flush=True)
print('D2_AXIS_FINITE_RECOVERY_PASS',len(EXPECTED),flush=True)
```
