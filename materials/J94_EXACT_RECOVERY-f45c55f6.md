# material-f45c55f64d9f

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J94 exact finite outer constructions and the tiny-bar boundary control

This capsule plus the complete J90 source core in material [internal-source-reference] suffices to reconstruct all three literal rational bodies. That material contains the unencoded nine-unit J90_CORE_REPLAY.sh (32579 bytes, SHA256 525ebd08fc99ca4a5f46552533508bec54c80465b03a9a7a9f77f939bc4f5efb). Its exact90.cpp, make_vfaudit90.py and J90_DETACHED_C390_G8.txt reconstruct the old130-vertex host. No original sandbox, J91 checkpoint, numerical optimizer or SciPy facet proposal is required for this recovery. Extract each complete file block below, including its final newline, to the same directory as those J90 units. Run `python J94_REPLAY.py`. The output markers are J94_EXACT_NEW_WITNESS_ESCAPE_PASS and J94_COMPLETE_EXACT_RECOVERY_PASS. This complete replay was executed and every recorded input/output hash matched.

Environment used: Python3.13.5, g++14.2, GMP C++ rational arithmetic. Producing numerical methods additionally used NumPy2.3.5, SciPy1.17.0, PyTorch2.10.0+cpu, with one BLAS/torch thread. Those numerical methods are separate recovery materials, not needed to recreate these exact bodies.

Exact outcomes at each body's own homogeneous volume centroid:

* J94_INTERIOR_C440_G8: V136/E220/F86, strict211, additionalweak000, primitivezero000, P[], Q[0.16179081487085792...]. Unique U retains original input1; H is old input edge40--109. Stable faces have original input labels [133,39,135] and the retained21-gon. Its own centroid differs from the old C390 centroid by approximately (5.353319169686291e-11,-9.167313105587036e-11,3.994660008993867e-11); it is not exactly old-centred. This improves the last Q of C434 at a cost of3 edges, not the equilibrium class.
* J94_CHAIN_C444_G8: V135/E222/F89, strict312, additionalweak000, primitivezero000, P[], Q[0.1603966521511199...,0.0022177548212978034...]. Old primary input133 and134 retired; retained_input_indices maps compact VF indices to original130+seven-apex inputs. S original faces are [39,136,31], [33,135,39], and the retained21-gon; H original edges39--136 and40--109. Unique U is input1. This is a useful finite witness-policy escape, NOT a class improvement. At its own exact centroid, max over all130 original vertices of p135 dot(pj-p135) is strictly negative, about -0.0007128399590730804. Nevertheless p135 dot(p136-p135)>0 (about0.0008319409434116792) and p136 dot(p23-p136)>0 (about0.000847523966873516). The replay asserts all these exact signs. Its new vertex is outside every old single-step witness ball, but the two-step chain remains valid. All mass integration is for the actual final hull.
* J94_TWO_CAND_G18: V136/E220/F86, strict312, additionalweak000, primitivezero000, P[], Q[0.1617907510959148...,6.615379650992725e-29...]. A floating-point two-stable continuation missed the second tiny Q and extra stable triangle[134,39,133]; this exact boundary control prevents promoting that numerical endpoint as own211. Backoff and G8 freezing produced the first body above.

These are nonwinner constructions. No own110/C<500 is claimed. Canonical own110 remains the earlier C622 body outside target.

## File J94_REPLAY.py
Bytes2947; SHA256 9c08904d008626f79eb016bab5cc0540da58a61347887e5bced8ba0316359c5a.
```python
"""Rebuild the three literal J94 rational bodies, and run complete exact audits.
Requires the nine exact source units from J90_CORE_REPLAY.sh. No old sandbox,
SciPy hull proposal, J91 method or floating-point nomination is needed here.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,subprocess,sys
ROOT=Path(__file__).resolve().parent
sys.set_int_max_str_digits(0)
NAMES=['J94_INTERIOR_C440_G8','J94_CHAIN_C444_G8','J94_TWO_CAND_G18']

def digest(path):
 b=path.read_bytes();return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def shell(cmd,stdin=None,stdout=None):
 with (ROOT/stdin).open('rb') if stdin else open('/dev/null','rb') as fi:
  with (ROOT/stdout).open('wb') if stdout else open('/dev/null','wb') as fo:
   subprocess.run(cmd,cwd=ROOT,stdin=fi,stdout=fo,check=True)
def main():
 expected=json.loads((ROOT/'J94_MANIFEST.json').read_text())
 for name,meta in expected.items():
  if name.endswith('_INPUT.json'):assert digest(ROOT/name)==meta,(name,'recovery input mismatch')
 if not (ROOT/'J90_DETACHED_C390_G8_AUDIT.json').exists():
  shell(['g++','-O2','-std=c++17','exact90.cpp','-o','exact90','-lgmpxx','-lgmp'])
  shell(['./exact90'],'J90_DETACHED_C390_G8.txt','J90_DETACHED_C390_G8_AUDIT.json')
 assert digest(ROOT/'J90_DETACHED_C390_G8_AUDIT.json')==dict(bytes=128029,sha256='c35f4ebdd391bed82599d28c4cee0c6ab57ac24192eb8942e7f70fa64be787ef')
 shell([sys.executable,'make_vfaudit90.py'])
 shell(['g++','-O2','-std=c++17','vfaudit90.cpp','-o','vfaudit90','-lgmpxx','-lgmp'])
 base=json.loads((ROOT/'J90_DETACHED_C390_G8_AUDIT.json').read_text())
 for name in NAMES:
  d=json.loads((ROOT/(name+'_INPUT.json')).read_text());x=base['vertices']+d['apexes'];ret=d.get('retained_input_indices',list(range(len(x))));v=[x[i] for i in ret];faces=d['faces']
  text=f'{len(v)} {len(faces)}\n'+''.join(' '.join(p)+'\n' for p in v)+''.join(' '.join(map(str,[len(cy),*cy]))+'\n' for cy in faces)
  (ROOT/(name+'_VF.txt')).write_text(text)
  shell(['./vfaudit90'],name+'_VF.txt',name+'_AUDIT.json')
  a=json.loads((ROOT/(name+'_AUDIT.json')).read_text())
  assert a['checks']=='EXACT_VF_HULL_MASS_DIRECT_GLOBAL_CENSUS_FULL_BARS_PASS'
  for suffix in ['_VF.txt','_AUDIT.json']:assert digest(ROOT/(name+suffix))==expected[name+suffix],(name,suffix,'output mismatch')
  print(name,a['V'],a['E'],a['F'],a['strict'],a['weak'],flush=True)
 a=json.loads((ROOT/'J94_CHAIN_C444_G8_AUDIT.json').read_text());d=json.loads((ROOT/'J94_CHAIN_C444_G8_INPUT.json').read_text());g=tuple(map(F,a['centroid']));p={lab:tuple(F(s)-c for s,c in zip(a['vertices'][i],g)) for i,lab in enumerate(d['retained_input_indices'])}
 def chord(i,j):return sum(x*(y-x) for x,y in zip(p[i],p[j]))
 assert max(chord(135,j) for j in range(130))<0
 assert chord(135,136)>0 and chord(136,23)>0
 print('J94_EXACT_NEW_WITNESS_ESCAPE_PASS',flush=True)
 print('J94_COMPLETE_EXACT_RECOVERY_PASS',flush=True)
if __name__=='__main__':main()
```

## File J94_MANIFEST.json
Bytes1275; SHA256 3011ba64bec86fb8ea6922513d08d520e34ccae165ea416e537889d1d781cbae.
```json
{
  "J94_CHAIN_C444_G8_AUDIT.json": {
    "bytes": 195714,
    "sha256": "789a972488a6fc72164ae32abea2f97514e496609899479cc347c2218bd34447"
  },
  "J94_CHAIN_C444_G8_INPUT.json": {
    "bytes": 2710,
    "sha256": "50e3f5c56406c4e3e3952a2717db05b4c7ac6736d92c1423d0a00858bb466354"
  },
  "J94_CHAIN_C444_G8_VF.txt": {
    "bytes": 20553,
    "sha256": "14357bb4cc62036ff0948148c81ffd8bcb28766445e87cad8df08b6f5c16dd46"
  },
  "J94_INTERIOR_C440_G8_AUDIT.json": {
    "bytes": 129694,
    "sha256": "13915fca3819099ea38ba046b571e97b784fbdecba3845a4abd664f64ae6e3eb"
  },
  "J94_INTERIOR_C440_G8_INPUT.json": {
    "bytes": 2171,
    "sha256": "f735b2f93d4a94e6fbc91afe9def9a41bda7c846c692f4bdd7ef1adf6e80c0b0"
  },
  "J94_INTERIOR_C440_G8_VF.txt": {
    "bytes": 20585,
    "sha256": "ff837292fba4aac849e627e5d25ab499428719c999f21784a3a021e6cad2fb81"
  },
  "J94_TWO_CAND_G18_AUDIT.json": {
    "bytes": 198592,
    "sha256": "5153d92e0da4b7f39a7ce4f6078b211170f74cf79f9b6671a45b447dad7a63d7"
  },
  "J94_TWO_CAND_G18_INPUT.json": {
    "bytes": 2528,
    "sha256": "98f2ed1524c2ed132a595da65d0edf1883875ae27d5f4a17ca88ced25eeed5ec"
  },
  "J94_TWO_CAND_G18_VF.txt": {
    "bytes": 20943,
    "sha256": "4241d05b279c68ad86e49212a3523f251d98f901f3d3ee385dd7511e05d61364"
  }
}
```

## File J94_INTERIOR_C440_G8_INPUT.json
```json
{"apexes":[["-76382877/100000000","3912347/25000000","2150961/50000000"],["29620437/100000000","-47025603/100000000","4414267/20000000"],["5727033/10000000","-34534091/100000000","-17674343/25000000"],["-33089867/100000000","45644493/100000000","3942683/20000000"],["-36034933/100000000","4492639/10000000","1674579/10000000"],["-5256273/20000000","25719253/50000000","8716771/50000000"]],"base":"J90_DETACHED_C390_G8","faces":[[135,28,134],[133,39,135],[134,39,133],[130,5,13],[134,28,36],[31,23,130],[36,23,134],[23,5,130],[33,28,135],[39,33,135],[134,31,39],[134,23,31],[130,13,31],[134,133,135],[23,36,2,5],[24,39,31,13,0,1,3,34,27,15,14,35,20,22,19],[6,2,36,28],[10,7,30,41,42],[33,39,24,57,41,30],[42,38,8,10],[12,25,47,84,106,114,78,128,0,13,5,2,6,7,10,8,9,4,16,17,11],[57,24,19,92],[9,8,38,32],[92,19,22,54],[32,51,4,9],[7,6,28,33,30],[111,54,22,20,110],[16,4,51,52],[47,25,44],[103,110,20,35],[17,16,52,63],[69,84,47,44,79,96,45],[103,35,14,107],[63,70,11,17],[117,107,14,15,21,29],[115,124,18,1,0,128],[12,11,70,67],[112,67,70,63,52,51,32,38,42,41,57,92,54,111],[69,45,91,85,80],[117,29,43,90],[97,58,49,89,64,59],[127,90,43,123],[121,76,79,44,25,12,67,112,129],[85,48,80],[79,76,96],[120,109,40,26,27,34,37],[123,43,29,21,122,116],[106,84,69,80,48,100,99,86],[102,95,91,45,96,76,121],[62,88,83,75,46,65,104,89,49],[56,122,21,15,27,26],[101,77,94,50,60,61],[87,82,62,49,58,113],[95,73,100,48,85,91],[112,111,110,103,107,117,90,127,98,119,129],[60,56,26,40,61],[100,73,99],[101,61,40,109,68],[81,71,93],[113,3,1,18,126,87],[81,93,108,55,78,114],[97,37,34,3,113,58],[73,95,102,65,46,108,93,71,86,99],[118,120,37,97,59],[128,78,55,75,83,72,115],[124,115,72,74,105,125],[55,108,46,75],[123,116,53,98,127],[88,74,72,83],[94,77,104,65,102,121,129,119],[98,53,50,94,119],[74,88,62,82,105],[125,105,82,87,126],[56,60,50,53,116,122],[118,59,64,66],[120,118,66,68,109],[101,68,66,64,89,104,77],[106,86,132],[132,81,114],[126,18,131],[132,71,81],[86,71,132],[131,18,124],[131,125,126],[114,106,132],[131,124,125]],"grid":100000000,"name":"J94_INTERIOR_C440_G8","rounding":"ties-to-even of each exact binary64 raw apex times 10**digits","source":"J94_BACKOFF_0_9999.json"}
```

## File J94_CHAIN_C444_G8_INPUT.json
```json
{"apexes":[["-38197411/50000000","3916687/25000000","4310677/100000000"],["14816101/50000000","-47047717/100000000","22091927/100000000"],["11537887/20000000","-34617779/100000000","-14112023/20000000"],["-33366769/100000000","1133967/2500000","9945891/50000000"],["-36764653/100000000","44247739/100000000","4164783/25000000"],["-1907467/6250000","46080339/100000000","22604531/100000000"],["-15677639/50000000","48870667/100000000","4035291/25000000"]],"base":"J90_DETACHED_C390_G8","faces":[[133,33,134],[133,134,39],[130,5,13],[28,36,134],[31,23,130],[33,28,134],[39,134,31],[130,23,5],[33,133,39],[134,36,23],[31,130,13],[134,23,31],[23,36,2,5],[0,1,3,34,27,15,14,35,20,22,19,24,39,31,13],[36,28,6,2],[30,41,42,10,7],[57,41,30,33,39,24],[42,38,8,10],[13,5,2,6,7,10,8,9,4,16,17,11,12,25,47,84,106,114,78,128,0],[92,57,24,19],[38,32,9,8],[54,92,19,22],[32,51,4,9],[28,33,30,7,6],[110,111,54,22,20],[51,52,16,4],[25,44,47],[103,110,20,35],[52,63,17,16],[44,79,96,45,69,84,47],[14,107,103,35],[63,70,11,17],[15,21,29,117,107,14],[0,128,115,124,18,1],[70,67,12,11],[42,41,57,92,54,111,112,67,70,63,52,51,32,38],[91,85,80,69,45],[29,43,90,117],[58,49,89,64,59,97],[43,123,127,90],[67,112,129,121,76,79,44,25,12],[48,80,85],[76,96,79],[34,37,120,109,40,26,27],[21,122,116,123,43,29],[76,121,102,95,91,45,96],[83,75,46,65,104,89,49,62,88],[27,26,56,122,21,15],[101,77,94,50,60,61],[87,82,62,49,58,113],[95,73,100,48,85,91],[110,103,107,117,90,127,98,119,129,112,111],[26,40,61,60,56],[73,99,100],[40,109,68,101,61],[93,81,71],[1,18,126,87,113,3],[78,114,81,93,108,55],[3,113,58,97,37,34],[93,71,86,99,73,95,102,65,46,108],[37,97,59,118,120],[128,78,55,75,83,72,115],[115,72,74,105,125,124],[55,108,46,75],[53,98,127,123,116],[72,83,88,74],[65,102,121,129,119,94,77,104],[94,119,98,53,50],[105,74,88,62,82],[125,105,82,87,126],[60,50,53,116,122,56],[59,64,66,118],[118,66,68,109,120],[64,89,104,77,101,68,66],[114,132,81],[71,81,132],[18,131,126],[71,132,86],[48,132,80],[18,124,131],[86,132,99],[99,132,100],[132,69,80],[132,84,69],[132,114,106],[100,132,48],[132,106,84],[131,124,125],[131,125,126]],"grid":100000000,"name":"J94_CHAIN_C444_G8","retained_input_indices":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,135,136],"rounding":"ties-to-even of each exact binary64 raw apex times 10**digits","source":"J94_FIXEDCHAIN_0_3.json"}
```

## File J94_TWO_CAND_G18_INPUT.json
```json
{"apexes":[["-381914388269621541/500000000000000000","156493883415679463/1000000000000000000","8603844495271673/200000000000000000"],["296204369767894271/1000000000000000000","-94051208003306741/200000000000000000","220713339980697143/1000000000000000000"],["2290812057412281/4000000000000000","-345340937295424477/1000000000000000000","-706974031367918143/1000000000000000000"],["-41362299879664513/125000000000000000","456445228022746397/1000000000000000000","197133974756708019/1000000000000000000"],["-360348534222567463/1000000000000000000","89852899734733449/200000000000000000","33491589022498247/200000000000000000"],["-16425942522470139/62500000000000000","514384669603990319/1000000000000000000","17433436909327471/100000000000000000"]],"base":"J90_DETACHED_C390_G8","faces":[[135,28,134],[133,39,135],[134,39,133],[134,133,135],[130,5,13],[31,23,130],[36,23,134],[23,5,130],[39,33,135],[134,28,36],[33,28,135],[134,23,31],[130,13,31],[134,31,39],[23,36,2,5],[24,39,31,13,0,1,3,34,27,15,14,35,20,22,19],[6,2,36,28],[10,7,30,41,42],[33,39,24,57,41,30],[42,38,8,10],[12,25,47,84,106,114,78,128,0,13,5,2,6,7,10,8,9,4,16,17,11],[57,24,19,92],[9,8,38,32],[92,19,22,54],[32,51,4,9],[7,6,28,33,30],[111,54,22,20,110],[16,4,51,52],[47,25,44],[103,110,20,35],[17,16,52,63],[69,84,47,44,79,96,45],[103,35,14,107],[63,70,11,17],[117,107,14,15,21,29],[115,124,18,1,0,128],[12,11,70,67],[112,67,70,63,52,51,32,38,42,41,57,92,54,111],[69,45,91,85,80],[117,29,43,90],[97,58,49,89,64,59],[127,90,43,123],[121,76,79,44,25,12,67,112,129],[85,48,80],[79,76,96],[120,109,40,26,27,34,37],[123,43,29,21,122,116],[106,84,69,80,48,100,99,86],[102,95,91,45,96,76,121],[62,88,83,75,46,65,104,89,49],[56,122,21,15,27,26],[101,77,94,50,60,61],[87,82,62,49,58,113],[95,73,100,48,85,91],[112,111,110,103,107,117,90,127,98,119,129],[60,56,26,40,61],[100,73,99],[101,61,40,109,68],[81,71,93],[113,3,1,18,126,87],[81,93,108,55,78,114],[97,37,34,3,113,58],[73,95,102,65,46,108,93,71,86,99],[118,120,37,97,59],[128,78,55,75,83,72,115],[124,115,72,74,105,125],[55,108,46,75],[123,116,53,98,127],[88,74,72,83],[94,77,104,65,102,121,129,119],[98,53,50,94,119],[74,88,62,82,105],[125,105,82,87,126],[56,60,50,53,116,122],[118,59,64,66],[120,118,66,68,109],[101,68,66,64,89,104,77],[132,81,114],[106,86,132],[86,71,132],[132,71,81],[131,18,124],[126,18,131],[114,106,132],[131,124,125],[131,125,126]],"grid":1000000000000000000,"name":"J94_TWO_CAND_G18","rounding":"ties-to-even of each exact binary64 raw apex times 10**digits","source":"J94_TWOFLOW.json"}
```
