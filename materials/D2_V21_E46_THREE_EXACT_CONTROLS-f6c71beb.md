# material-f6c71beba009

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Three simple rational V21/E46/F27 controls

All three bodies are homogeneous at their OWN filled-volume centroid, strict (S,U,H)=(3,3,4), additionalweak=(0,0,0), C=92. They are useful small nonwinners with203 true-edge headroom, NOT110 or replacement of the accepted110/C622 baseline. This exact capsule is independent of the numerical search sandbox. It needs the unchanged full d2_exact.py in material [internal-source-reference] (7931B,SHA141ad514d226afe665910f93da6569e463b54621494d556f79aa2c9df42e221c).

Reflect each listed integer quarter representative independently in x and y and divide by10**g. There are exactly21 extreme vertices, eight D2 vertex orbits, and27 maximal facets. The full exact conversion enumerates all supporting point triples; exhaustive H audit reconstructs exactly the V hull, computes two-origin filled-volume mass, maximal facets/true edges and all direct/polar/mixed strict/weak mechanics. One full auditor with internal crosschecks, not two independent auditors.

G3/G4/G6 centred common-multiplier bit lengths are46/59/86, respectively. Actual centroids are (0,0,-120482561947/253055728800), (0,0,-10040765832038859/21089577089720000), and (0,0,-753021437122391680059539/1581630573595943882000000). In the exact emitted ordering S facets16,17,26; U vertices9,10,11; saddles edges0,22,25,45. BASE is26, top is vertex10. Never transport labels from numerical triangulation or another body. There are no primitive zero U/Q arrows and no boundary facet feet. G3 volume105439887/50000000.

The frozen numerical precursor had57 input points but only21 extreme vertices. This capsule removes only exact nonextreme input points; equality of the old and reduced exact vertex sets was checked. The names D2_V21_E46_G* identify these minimal21-point recovery inputs; their output byte receipts differ from old D2_V1_BEST_G* inputs with57 supplied points. Only this capsule's literal arrays and receipts are authoritative. An intermediate compaction note gave other arrays/centroids/receipts; those do NOT match the actual saved input and are not these objects.

Write both complete Python units below as UTF-8/LF with one terminal newline. recover_d2_v21.py2273B SHA11ae32055bfc1377b308f2395055ab81d8444fa798962c965fff5c4bce68b91b; d2_vertex_exact.py2730B SHAab5e26b4cda0740d49156f0353ce399673048431d59f6f11f35b4d3e583512ba. Place the unchanged dependency beside them. CPython3.13.5 standard library only. Command `python -B -S recover_d2_v21.py D2_V21`; expected terminal `D2_V21_E46_THREE_EXACT_CONTROLS_PASS 9`. All nine input/H/full-audit receipts were freshly cold-reproduced.

## recover_d2_v21.py
```python
"""Three exact V21/E46/F27 controls, all strict334/weak000; not110.
Dependency: complete unchanged d2_vertex_exact.py and d2_exact.py.
"""
from pathlib import Path
import json,hashlib,sys
from d2_vertex_exact import convert,raw
ROWS={3:[[0,0,1000],[0,1376,-1000],[0,1393,-950],[158,1328,-1000],[278,0,565],[506,0,-340],[595,814,-1000],[671,680,-1000]],4:[[0,0,10000],[0,13762,-10000],[0,13928,-9500],[1578,13285,-10000],[2784,0,5648],[5058,0,-3401],[5949,8136,-10000],[6713,6798,-10000]],6:[[0,0,1000000],[0,1376244,-1000000],[0,1392809,-950030],[157798,1328466,-1000000],[278373,0,564817],[505788,0,-340143],[594887,813566,-1000000],[671290,679804,-1000000]]}
EXPECTED={'D2_V21_E46_G3.json':(442,'36e9859f115c138f7851501e6055899224f8ea8c085312fd1e3f831bd435726d'),'D2_V21_E46_G3_H.json':(1064,'4d23910bc90579bf4e0b60db468dcfa86acb23bc59b91fcda144ebc244abf496'),'D2_V21_E46_G3_audit.json':(6272,'e116f613531d8de982465afd695fde8a23efe5385a29879908e7e74250e5b0e6'),'D2_V21_E46_G4.json':(461,'df636233b0eddfc24516d9cf3f860941e11486536c0819ac68f9521b30d121c2'),'D2_V21_E46_G4_H.json':(1334,'4359b9dc47fb022abbcd8861964ad481723b8545ac6d1bc72fdba44e24a6f1cc'),'D2_V21_E46_G4_audit.json':(6367,'4b52a6c0c1e4c113398f5479c19a596b040f3ee1495f9aa941b913b7fe6c789b'),'D2_V21_E46_G6.json':(499,'9be8c469710dbd018221749e23c43394a8d6afb49ecf36799e396411ace71e76'),'D2_V21_E46_G6_H.json':(2143,'4f6197d9c246f2a98060cb8dd9e87d108699444de9f01e79b55782359e6f921d'),'D2_V21_E46_G6_audit.json':(6526,'4152833d1f51b3488b99444fcf5e8e86f66b362eb6cf1ea16e0e5ce71a5d0fb1')}
def main():
    out=Path(sys.argv[1] if len(sys.argv)>1 else 'D2_V21');out.mkdir(exist_ok=True,parents=True)
    n=0
    for g,rows in ROWS.items():
        name=f'D2_V21_E46_G{g}';d=dict(name=name,denominator=10**g,representatives=rows);h,a=convert(d)
        assert (a['V'],a['E'],a['F'],a['strict'],a['additional_weak'])==(21,46,27,[3,3,4],[0,0,0])
        for fn,obj in [(name+'.json',d),(name+'_H.json',h),(name+'_audit.json',a)]:
            b=raw(obj);assert (len(b),hashlib.sha256(b).hexdigest())==EXPECTED[fn],fn;(out/fn).write_bytes(b);n+=1
        print(name,a['strict'],a['additional_weak'],a['centroid'],a['centred_scale_bits'])
    print('D2_V21_E46_THREE_EXACT_CONTROLS_PASS',n)
if __name__=='__main__':main()
```

## d2_vertex_exact.py
```python
"""Exact V-to-H D2 conversion and own-mass full audit.
Rational integer representatives/denominator are reflected in x and y.
Every supporting plane is enumerated from all point triples. After exact H audit,
all reconstructed H vertices must belong to the original V set and every V point
must satisfy every H inequality: these checks prove equality of the two hulls.
Dependency: unchanged d2_exact.py (7931 bytes; SHA141ad514d226afe665910f93da6569e463b54621494d556f79aa2c9df42e221c).
"""
from d2_exact import dot,sub,cross,audit
from itertools import combinations
from functools import reduce
from math import gcd,lcm
from fractions import Fraction as F
from pathlib import Path
import json,sys,hashlib

def raw(x):return (json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
def convert(data):
 d=int(data['denominator']);assert d>0
 p=sorted(set((sx*a,sy*b,c) for a,b,c in data['representatives'] for sx,sy in [(1,1),(-1,1),(-1,-1),(1,-1)]))
 planes=set()
 for a,b,c in combinations(p,3):
  n=cross(sub(b,a),sub(c,a));g=reduce(gcd,map(abs,n))
  if not g:continue
  n=tuple(v//g for v in n);h=dot(n,a);sg=[dot(n,x)-h for x in p]
  if min(sg)<0<max(sg):continue
  if min(sg)==max(sg)==0:continue
  if max(sg)>0:n=tuple(-v for v in n);h=-h
  assert h>0,'origin must be strictly interior'
  planes.add((*n,h))
 assert len(planes)>=4
 Q=lcm(*(h for *n,h in planes));reps=sorted(set((abs(a)*d*(Q//h),abs(b)*d*(Q//h),c*d*(Q//h)) for a,b,c,h in planes))
 bottom=[r for r in reps if r[0]==r[1]==0 and r[2]<0];assert len(bottom)==1
 bottom=bottom[0];reps.remove(bottom);caps=[r for r in reps if all(v>0 for v in r)];assert caps
 cap=max(caps,key=lambda r:r[2]);reps.remove(cap);reps.append(cap)
 common=reduce(gcd,[Q,*[abs(x) for r in reps for x in r],abs(bottom[2])]);hd=dict(name=data['name'],denominator=Q//common,bottom=-bottom[2]//common,representatives=[[x//common for x in r] for r in reps])
 result=audit(hd)
 original={tuple(F(x,d) for x in v) for v in p};vertices={tuple(F(x,v[3]) for x in v[:3]) for v in result['vertices']}
 assert vertices<=original
 assert all(dot((a,b,c),x)<=h for a,b,c,h in planes for x in p)
 result['V_input_proof']={'reflected_input_points':len(p),'all_supporting_triples_enumerated':True,'H_extremes_are_original_V_points':True,'all_original_V_points_in_H':True}
 return hd,result
if __name__=='__main__':
 path=Path(sys.argv[1]);data=json.loads(path.read_text());hd,report=convert(data)
 for name,value in [(data['name']+'_H.json',hd),(data['name']+'_audit.json',report)]:
  bs=raw(value);path.with_name(name).write_bytes(bs);print(name,len(bs),hashlib.sha256(bs).hexdigest())
 print('D2_EXACT_V_TO_H_FULL_AUDIT_PASS',report['V'],report['E'],report['F'],report['strict'],report['additional_weak'])
```
