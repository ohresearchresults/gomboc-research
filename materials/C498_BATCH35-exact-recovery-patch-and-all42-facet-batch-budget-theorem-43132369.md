# material-43132369363c

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# C498_BATCH35 exact recovery and all42 facet-batch budget theorem

## Exact identities and complete source dependencies
This is a NEW literal facet-deletion construction derived from the unchanged canonical V176/E311/F137,C622 own110 body, not an affine alias or a claimed110 descendant. The exact source-complete parent is immutable result `figure-0411`, SHA2568fcc52aa7ec1d0556b774912061d81594425ea912bf5bfee8caada67a4026e0b, which the coordinator read completely. Its exact16-unit recovery is already preserved in TWO ordered materials, both required for this patch:
1. `[internal-source-reference]`, COORD_C622_CANONICAL_SCOPED16_Recovery_capsule_part_1_of_2.md,15305bytes,SHA256d5846089dd79e70e4aa35f67d5d66b8480c3dd72bca1de45359a281931f632aa.
2. `[internal-source-reference]`, COORD_C622_CANONICAL_SCOPED16_Recovery_capsule_part_2_of_2.md,20685bytes,SHA256c4a0ef05c36066f7b2851dc18ea1c3cda599f724130ec0ce7a89785613cde5b1.

Recover their unchanged16 files into `source/` using their assembler/manifest. Both complete parents, not merely their hashes, are necessary recovery inputs and must be explicitly attached for a worker using this material. They include the full literal canonical GENERATOR.json, core/RECONSTRUCT.py, exact independent core/check_A.py and core/check_B.py, centred_mass.py, and the numerical contact-atlas dependencies. The base source archive is68603bytes,SHA25663b9a7de970fa8fb01f43ce10bec573441e5afeebe4ef2d3b7031ea6fb64c9ca; source/GENERATOR.json11841bytes,SHA2563cbd90d799189108f26b941800c8fa79a6f1c5abb17b2db614f0e54f57fffee7. All16 decoded source hashes were actually checked before this research.

## New exact budget theorem
For a full-dimensional bounded3-polytope put D=sum_v(deg(v)-3). Euler and the degree sum give E=3F-6-D. In canonical C622, D=94. Delete k facets and retain a bounded intersection. Every retained old facet remains genuinely active because its old relative interior survives. If old nonsimple vertexv retains spanning support normals and at least3 incident facets, it survives with its retained degree. Therefore a certified total loss ell of old degree-excess gives E_new<=311-3k+ell. New nonsimple vertices can only improve this upper bound.

The following20 facets have only degree3 incident vertices:
[48,55,69,70,89,93,99,100,101,105,110,112,113,114,115,117,120,123,124,125].
They are NOT all triangles: only99 and117 are the simple triangular facets. Removing those20 plus any ONE facet from
[1,4,13,14,16,17,18,22,28,32,35,43,44,47,51,56,63,64,67,72,73,80,81,84,85,95,96,102,106,107,108,111,116,118,126,127,128,129,130,132,134,136]
loses exactly one unit of old nonsimple degree-excess. For all42 sets, the verifier below exhibits an exact spanning triple at every old nonsimple vertex and a single common strictly positive spanning-normal dependence on retained input facets[0,2,6,46], proving boundedness. Thus all42 literal bodies satisfy F116,D>=93,E<=249,C<=498. This is an exact geometry budget theorem, NOT a mechanics theorem, and it does not say all deformations of these inputs retain the certificate.

## Exact nonwinner C498_BATCH35
Choose extra facet35. Remove exactly the21 original input indices[35,48,55,69,70,89,93,99,100,101,105,110,112,113,114,115,117,120,123,124,125], retaining row order and otherwise changing nothing. Fresh independent A/B reconstruction yields V135/E249/F116,C498, strict S/U/H=[16,34,48], additionalweak=[0,0,0], all primitive zero counts0, with the actual uniform filled-volume centroid. A and B agree byte-for-byte. It is a useful changed-incidence construction under the requested edge budget, but NOT the requested class110 and NOT a new canonical best. The canonical C622 strict110 remains unchanged.

A separate finite floating halfspace scout found all42 bodies numerically V135/E249/F116 and none110. The exact all42 claim is only the proven edge budget; the full exact mechanics claim here is for extra35. Do not upgrade the other41 numerical censuses to exact audits.

## Reconstruction and verification
Save the two complete new code blocks below respectively as batch_budget.py and REPLAY_BATCH35.py beside the recovered `source/` directory. CPython3.13.5 standard library only, no numerical library, no RNG, no nondefault parameters beyond the literal deletion set. Run:
`python -B -S REPLAY_BATCH35.py > replay_batch35.log`
The runner actually rebuilds canonical input/mass, proves the42-member budget, constructs the exact extra35 input and runs both exact audits. Terminal markers:
`C622_BATCH21_ALL42_E_LE249_EXACT_PASS 20 42 40477 92a21195124f96a126aa70b91d6f850ed6375b422cf845df83a20f4d6fc25dee`
`C498_BATCH35_EXACT_AB_PASS 135 249 116 16 34 48 weak000`

Source byte identities:
- batch_budget.py2705bytes,SHA256627d8499903bed51fb7215521289c6b25557d2b0b7032735546f4b9ea1402346.
- REPLAY_BATCH35.py1378bytes,SHA256aa39b9c4735d85b415cfcddd90d998d4925160aa412dd0a86f0b6b6025409222.
Recovery output byte identities:
- raw.json15437bytes,SHA256ac01d1625274b64f336a715e1f5462f40686f647f0b7d1a4d90a5ee21765adb5.
- A.json311825bytes,SHA256142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0.
- batch_budget_certificate.json40477bytes,SHA25692a21195124f96a126aa70b91d6f850ed6375b422cf845df83a20f4d6fc25dee.
- batch35.raw.json14215bytes,SHA256a95d26cce18382ca01e82e46b1f269ce9c36a639fc680f7446d27762e07f5a39.
- batch35.A.json and batch35.B.json each255560bytes,SHA256ac0cf61e1de30447bd5d0548679a67f5a8f4646ca12551e86995f8dc7a848e6f.

```python
"""Exact canonical C622 facet-deletion budget certificate.
Reads unchanged canonical raw.json,A.json reproduced by SCOPED16.
No geometry or mechanics of a changed body is inferred from floating sampling.
"""
import sys,json,itertools,math,hashlib
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
B=lambda a:json.dumps(a,sort_keys=True,separators=(',',':')).encode()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def main():
 raw=json.load(open('raw.json'));rep=json.load(open('A.json'))
 assert hashlib.sha256(B(raw)).hexdigest()=='ac01d1625274b64f336a715e1f5462f40686f647f0b7d1a4d90a5ee21765adb5'
 assert hashlib.sha256(B(rep)).hexdigest()=='142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0'
 H=raw['H'];inc=[set(i for i,f in enumerate(rep['faces']) if v in f) for v in range(rep['V'])];degree=[sum(v in e for e in rep['edges']) for v in range(rep['V'])]
 assert degree==[len(o) for o in inc];D=sum(d-3 for d in degree);assert D==94
 simple=[i for i,f in enumerate(rep['faces']) if all(degree[v]==3 for v in f)]
 choices=[i for i in range(rep['F']) if i not in simple and sum(min(1,degree[v]-3) for v in rep['faces'][i])==1]
 assert len(simple)==20 and len(choices)==42
 common=sorted(set(range(rep['F']))-set(simple)-set(choices));bound=None
 for ids in itertools.combinations(common,4):
  ns=[H[i][:3] for i in ids];w=[(-1)**j*det(*[ns[k] for k in range(4) if k!=j]) for j in range(4)]
  if all(t<0 for t in w):w=[-t for t in w]
  if all(t>0 for t in w):
   g=math.gcd(*w);w=[t//g for t in w]
   assert all(sum(w[k]*ns[k][j] for k in range(4))==0 for j in range(3))
   assert det(*ns[:3])!=0
   bound=dict(input_rows=list(ids),positive_weights=w);break
 assert bound is not None
 certificates=[]
 for extra in choices:
  removed=set(simple+[extra]);ranks=[];loss=0
  for v,d in enumerate(degree):
   if d==3:continue
   left=sorted(inc[v]-removed);assert len(left)>=3
   tri=next(t for t in itertools.combinations(left,3) if det(*[H[i][:3] for i in t])!=0)
   ranks.append([v,len(left),list(tri)]);loss+=d-len(left)
  assert loss==1
  certificates.append(dict(extra=extra,removed=sorted(removed),retained_old_excess=D-loss,edge_upper=311-3*len(removed)+loss,rank_witnesses=ranks))
 out=dict(object='C622_BATCH21_ALL_SIMPLE20_PLUS_LOSS1',simple20=simple,choices42=choices,boundedness=bound,parent_excess=D,members=certificates)
 data=B(out);open('batch_budget_certificate.json','wb').write(data)
 print('C622_BATCH21_ALL42_E_LE249_EXACT_PASS',len(simple),len(choices),len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__':main()
```

```python
"""Exact replay; requires the unchanged canonical SCOPED16 as source/."""
import sys,json,subprocess,hashlib
from pathlib import Path
sys.set_int_max_str_digits(0)
def run(*a):subprocess.run([sys.executable,'-B','-S',*a],check=True)
def check(name,n,h):
 b=Path(name).read_bytes();assert len(b)==n and hashlib.sha256(b).hexdigest()==h,(name,len(b),hashlib.sha256(b).hexdigest())
run('source/core/RECONSTRUCT.py','source/GENERATOR.json','raw.json')
check('raw.json',15437,'ac01d1625274b64f336a715e1f5462f40686f647f0b7d1a4d90a5ee21765adb5')
run('source/core/check_A.py','raw.json','A.json')
run('batch_budget.py')
r=json.load(open('raw.json'));D=[35,48,55,69,70,89,93,99,100,101,105,110,112,113,114,115,117,120,123,124,125]
r['H']=[row for i,row in enumerate(r['H']) if i not in D]
Path('batch35.raw.json').write_bytes(json.dumps(r,sort_keys=True,separators=(',',':')).encode())
check('batch35.raw.json',14215,'a95d26cce18382ca01e82e46b1f269ce9c36a639fc680f7446d27762e07f5a39')
for t in ['A','B']:
 run('source/core/check_'+t+'.py','batch35.raw.json','batch35.'+t+'.json')
 check('batch35.'+t+'.json',255560,'ac0cf61e1de30447bd5d0548679a67f5a8f4646ca12551e86995f8dc7a848e6f')
r=json.load(open('batch35.A.json'));assert [r[k] for k in ['V','E','F']]==[135,249,116] and r['counts']==[16,34,48] and r['weak']==[0,0,0]
print('C498_BATCH35_EXACT_AB_PASS 135 249 116 16 34 48 weak000')
```
