# material-27b39b5e6f07

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# C318_PROTECTED15 — complete exact recovery and protected-path certificate

This is a new exact NONWINNER, not a homogeneous own110 construction. Canonical accepted own110 remains C622. The uniformly filled rational body below has V94/E159/F67, C318, own strict[14,3,15], weak000 and primitive-zero000. At the explicitly different reference point g_ref it has strict121, weak000, primitive-zero000. Thus protecting the old unstable vertex along a positive polar path does not by itself prevent a second physical unstable vertex or preserve the filled centroid.

## Complete dependencies and identities

Supply and read all three prior materials: [internal-source-reference] (complete C330 literal geometry), [internal-source-reference] (complete independent A/B and centered-mass sources), and [internal-source-reference] (complete C288 reconstruction). Their literal instructions reconstruct C288/RAW.json and C288/A.json without an old sandbox. This material adds every new input and executable source needed. Save its two FILE blocks, with their final newlines, beside exact_source/ from the C330 audit capsule. Execute `python -B -S RECONSTRUCT_C318.py C288 OUT318` with a fresh output directory. The command reconstructs every exact support, runs both complete maximal-hull auditors, integrates the ordinary filled centroid, independently integrates184 positive centered integer tetrahedra, checks reference mechanics, and verifies both15-link certificates. The wrapper's expected terminal marker is C318_PROTECTED15_EXACT_NONWINNER_OWN_AND_REFERENCE_PASS. The underlying exact A/B, third mass, reference census and chain predicates were all executed successfully before this material was stored; the newly assembled wrapper is not called cold-replayed until it is separately executed.

The14 intermediate polar vectors use denominator10^10. Their path goes from C288's extra stable polar vertex54 to its retained stable polar vertex0. EXACTLY VERIFIED both at the C288 OWN centroid and at g_ref: every normalized radial arrow x dot(y-x)/(x dot x)>1/2000; every intermediate q satisfies q dot p<933/1000 for the corresponding centered old unstable vertex16; all intermediate norms are below the terminal polar norm. The route therefore preserves that physical vertex with strict slack. This15-link protected path is NOT proved minimal. Failed13/14-link numerical searches are not exclusions. The older C330 free-minimum13 result is for different endpoints and does not transfer to C288.

The exact H-body retains all70 C288 inequalities as input and adds14 new ones. Seventeen become inactive: actual F67, NOT84. Prior floating diagnostics that used the number of input inequalities as F after chain insertion overcounted F and E. The maximal-complex audit is authoritative. The source SUPPORT_BEAM's F=input-count shortcut was valid only for deletion of originally extreme polar points, not arbitrary inserted points.

Generated exact identities (bytes,SHA256): RAW.json5618,c061956cd80e8eb37055c2dcb8278ced98bf9c520e5e32a28acf5d82ff6c65eb; A.json=B.json69487,dd4bac76a24f4652e70360e1d48e4ab04fd0a6449d44f1aacadc5ddcd58a6fde; MASS.json224,ee096d2cf8328e130e0718abcc05abf156371a8f03e31b507cc5f7032bda4a00; REFERENCE.json79,ab40d2625bd0f8a57f15c169eff3103c5b0337f9e689d92fbfb70105196a508e; REF_REPORT.json23215,a9f7c8857a077830f12e8302c86976ac929b6c2d171471ba71f490617f484d42. MASS.json deliberately includes its terminal LF, matching the executed CLI output. No numerical optimizer is needed for recovery.

## Exact reconstruction and gates

<!-- FILE RECONSTRUCT_C318.py -->
```python
import sys,json,hashlib,math
from fractions import Fraction as Q
from pathlib import Path
sys.set_int_max_str_digits(0)
sys.path.insert(0,str(Path(__file__).resolve().parent/'exact_source'))
import check_A as A,check_B as B,centred_mass as M
from AUDIT_REFERENCE import audit,dot,sub
J=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
assert __debug__ and len(sys.argv)==3
parent=Path(sys.argv[1]);rawb=(parent/'RAW.json').read_bytes();ab=(parent/'A.json').read_bytes()
assert (len(rawb),hashlib.sha256(rawb).hexdigest())==(4288,'ff6315752d61fa1a04c065f1b311db6d28e621c5a0f09bea706b297aaf1b264f')
assert (len(ab),hashlib.sha256(ab).hexdigest())==(39507,'93a142eefdf1fb53b4b5a080089c6243f670c66a6e15c8a38be8c428b4971a7d')
raw=json.loads(rawb);pa=json.loads(ab);g=list(map(Q,['-100415011/50000000000','2313445601/62500000000','16788584983/1000000000000']));grid=10000000000
rows=[[745297386,17126492235,-10314660233],[-2060236734,18299087712,-8596900682],[-4995216743,18880224620,-6688946494],[-7968196953,18831219512,-4649506911],[-10883526411,18132949563,-2543559360],[-13644372953,16787118466,-440406039],[-16155884333,14816875220,1588475394],[-18328386387,12266744403,3471722672],[-20080513765,9201847902,5140450213],[-21342167604,5706420860,6530605105],[-22057196787,1881648009,7585239768],[-22185705243,-2157130150,8256623490],[-21687927932,-6280257215,8556397620],[-20563487354,-10361704351,8447474408]]
points=[tuple(Q(v,grid) for v in r) for r in rows]
for centre in [tuple(map(Q,pa['raw_centroid'])),tuple(g)]:
 Y=[tuple(Q(v)/(Q(h)-dot(n,centre)) for v in n) for n,h in zip(pa['normals'],pa['offsets'])];p=sub(tuple(map(Q,pa['raw_vertices'][16])),centre);seq=[Y[54]]+points+[Y[0]]
 assert all(dot(x,sub(y,x))>Q(1,2000)*dot(x,x) for x,y in zip(seq,seq[1:]))
 assert all(dot(q,p)<Q(933,1000) for q in points)
 assert all(dot(q,q)<dot(Y[0],Y[0]) for q in points)
refparent=audit(pa,g);assert refparent['strict']==[2,1,1] and refparent['weak']==[0,0,0] and refparent['unstable_vertices']==[16] and refparent['stable_face_ids']==[0,54]
H=list(raw['H'])
for n in points:
 h=1+dot(n,g);dd=math.lcm(*(v.denominator for v in n),h.denominator);r=[int(v*dd) for v in list(n)+[h]];gg=math.gcd(*r);r=[v//gg for v in r];assert r[3]>0;H.append(r)
raw={'H':sorted(set(tuple(r) for r in H))};a=A.run(raw);b=B.run(raw);assert J(a)==J(b);m=M.run(a);r=audit(a,g)
assert [a['V'],a['E'],a['F']]==[94,159,67] and a['counts']==[14,3,15] and a['weak']==[0,0,0]
assert [a['face_primitive_zero_count'],a['vertex_max_zero_count'],a['edge_primitive_zero_count']]==[0,0,0]
assert r['strict']==[1,2,1] and r['weak']==[0,0,0] and r['primitive_zero_counts']==[0,0,0]
assert r['stable_face_ids']==[13] and r['unstable_vertices']==[3,38] and r['saddle_edges']==[[75,77]]
assert m['tetrahedra']==184 and m['filled_first_moments']==[0,0,0] and m['common_centred_denominator_bits']==10574
expected={'RAW.json':(5618,'c061956cd80e8eb37055c2dcb8278ced98bf9c520e5e32a28acf5d82ff6c65eb'),'A.json':(69487,'dd4bac76a24f4652e70360e1d48e4ab04fd0a6449d44f1aacadc5ddcd58a6fde'),'B.json':(69487,'dd4bac76a24f4652e70360e1d48e4ab04fd0a6449d44f1aacadc5ddcd58a6fde'),'MASS.json':(224,'ee096d2cf8328e130e0718abcc05abf156371a8f03e31b507cc5f7032bda4a00'),'REFERENCE.json':(79,'ab40d2625bd0f8a57f15c169eff3103c5b0337f9e689d92fbfb70105196a508e'),'REF_REPORT.json':(23215,'a9f7c8857a077830f12e8302c86976ac929b6c2d171471ba71f490617f484d42')}
out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
for name,value in [('RAW.json',raw),('A.json',a),('B.json',b),('MASS.json',m),('REFERENCE.json',list(map(str,g))),('REF_REPORT.json',r)]:
 bb=J(value)+(b'\n' if name=='MASS.json' else b'');assert (len(bb),hashlib.sha256(bb).hexdigest())==expected[name],name;(out/name).write_bytes(bb)
print('C318_PROTECTED15_EXACT_NONWINNER_OWN_AND_REFERENCE_PASS',a['counts'],r['strict'],flush=True)
```

<!-- FILE AUDIT_REFERENCE.py -->
```python
"""Exact feature classification at a stated reference point, separate from own mass.
Input is the complete maximal-complex report of independent auditors A/B.
This does not replace those auditors or assert that the reference point is the centroid.
"""
import sys,json
from fractions import Fraction as Q
from math import lcm
from pathlib import Path
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,t):return tuple(x*t for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def sign(x):return (x>0)-(x<0)
def audit(a,centre):
 g=tuple(map(Q,centre));P=[tuple(map(Q,r)) for r in a['raw_vertices']];N=a['normals'];h=a['offsets'];faces=a['faces']
 assert all(Q(c)-dot(n,g)>0 for n,c in zip(N,h))
 den=lcm(*(v.denominator for p in P for v in p),*(c.denominator for c in g))
 X=[tuple(int(den*(v-c)) for v,c in zip(p,g)) for p in P]
 fs=[];vs=[];es=[];S=[];U=[];H=[];SW=[];UW=[];HW=[];pairs={}
 for fi,cy in enumerate(faces):
  ss=[sign(dot(N[fi],cross(X[i],sub(X[j],X[i])))) for i,j in zip(cy,cy[1:]+cy[:1])];fs.append(ss)
  if min(ss)>0:S.append(fi)
  elif min(ss)==0:SW.append(fi)
  for i,j in zip(cy,cy[1:]+cy[:1]):pairs.setdefault(tuple(sorted((i,j))),[]).append(fi)
 for i,x in enumerate(X):
  value=max(dot(x,sub(y,x)) for j,y in enumerate(X) if i!=j);s=sign(value);vs.append(s)
  if s<0:U.append(i)
  elif s==0:UW.append(i)
 for (i,j),ff in sorted(pairs.items()):
  assert len(ff)==2;n,m=[N[k] for k in ff];d=cross(n,m);e=sub(X[j],X[i]);ee=dot(e,e);ze=dot(X[i],e);p=sub(mul(X[i],ee),mul(e,ze));ss=[sign(v) for v in (-ze,ee+ze,dot(cross(p,m),d),dot(cross(n,p),d))];es.append([i,j,*ss])
  if min(ss)>0:H.append([i,j])
  elif min(ss)==0:HW.append([i,j])
 return dict(reference_point=list(map(str,g)),own_centroid=a['raw_centroid'],strict=[len(S),len(U),len(H)],weak=[len(SW),len(UW),len(HW)],stable_face_ids=S,unstable_vertices=U,saddle_edges=H,weak_faces=SW,weak_vertices=UW,weak_edges=HW,face_signs=fs,vertex_signs=vs,edge_signs=es,primitive_zero_counts=[sum(v==0 for r in fs for v in r),len(UW),sum(v==0 for r in es for v in r[2:])])
if __name__=='__main__':
 a=json.loads(Path(sys.argv[1]).read_text());g=json.loads(Path(sys.argv[2]).read_text());r=audit(a,g);Path(sys.argv[3]).write_text(json.dumps(r,sort_keys=True,separators=(',',':')));print('REFERENCE_NOT_OWN_CLASS',r['strict'],r['weak'],r['primitive_zero_counts'],flush=True)
```

## Scientific continuation

This is not a minimum-complexity own211 claim: older preserved C80 pyramids and C138 integer bodies already have own211. C288 offers a different non-pyramidal70-support interface with headroom for35 added physical inequalities under the unconditional F<=105,E<=309 bound. Its exact protected15 path uses14 of those35 slots, although the realized intersection introduces a second reference U and a substantial filled-centroid displacement. The16-bit-looking small number of equilibrium defects at the parent is not a small global barrier: a fresh numerical true-edge diagnostic gives parent polar beta about-0.5594; this decimal is not an exact cut certificate. Next useful work is joint whole-interface and mass redesign, or treating the at-most101 polar points of a longer protected route as a separate physical V-description with unconditional E<=297. The latter changes the uniform-volume problem and must recompute its own centroid; polarity alone does not preserve own mechanics.
