# material-98271e77193c

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Recovery capsule part 1/1 — COORD_D717_FIXED_DELETION4526_EXACT_SOURCE_V2

## Exact finite theorem and scope
For the literal 32 D717 input points below, with their common denominator717, delete any zero, one, two or three of the30 originally exposed input rows. Inputs5,6 are originally interior and are retained in every case. Every one of the resulting4526 uniformly FILLED convex hulls has at least TWO STRICT UNSTABLE equilibria at its own ordinary volume centroid. Thus none is own110. This excludes only the finite fixed-coordinate deletion family; it does not exclude moved points, added points, deletion of four or more exposed inputs, affine/projective images, or any broader family.

The complete standard-library source below is sufficient without any sandbox, attachment, previous code or solver. It enumerates all4960 input triples and proves every triple noncollinear and every quadruple noncoplanar. Exact integer side masks then select ALL supporting triples for each remaining point set. Each hull is checked full-dimensional, closed, oriented, connected, Euler2 and simplicial, with every edge on exactly two oppositely oriented maximal triangles. The origin is strictly interior. One exact positive origin-tetrahedron integral gives ordinary volume and first moments. A second separate sum over positive tetrahedra about the derived rational centroid gives the same volume and exactly zero first moments. Strict unstable witnesses are checked against ALL other remaining input points, including the retained interior points, by strictly negative radial escape. True C=2E is checked >=32 before mechanics. No floating hull, randomization, approximate sign or optimizer enters this proof.

Counts by deleted exposed rows:0 ->1case,C168;1 ->30cases,C162;2 ->435cases,C156;3 ->4060cases,C150. Minimum strict U is2 in each group. This result does not provide a full S/H census for all4526 hulls and is not a new own110 construction. The accepted record remains C622.

Scientific parent: literal immutable D717 result figure-0393, SHA2562ee8abc72403f981770152547d685735c7cc724a253f7ac7b354dff4fc7e19f1, read completely. Every coordinate needed is repeated in full below, so the proof's reconstruction has no source dependency.

## Reconstruction, verification and observed identities
Save the Python fence exactly as exact_deletion.py, including its final newline. Run with assertions enabled:

`python -B -S exact_deletion.py absent-output-directory`

CPython3.13.5 standard library was used. Python3.11+ is compatible; no external dependency, seed or precision setting is required. The directory must initially be absent. Source5189bytes SHA256aaec2a81d0cb7ef5fa8f50bb72478c3fca276729d0e233f98f673e66fe2cfea2.

Both the earlier one-integral version and this strengthened two-positive-integral version were executed to completion; the4526 case records agree byte-for-byte. This exact V2 source was executed and produced:
- CASES.json1764691bytes SHA2561bf98f43d7cbde5687705a58e994f043899ff2f5d4708814b52a7abe71e6964f.
- SUMMARY.json737bytes SHA25644de2af0f6aa9145c62242eb53d76d298eeac4ed44e118cc785e3000c53dc5cb.

Expected final terminal marker:
`D717_ALL_4526_FIXED_DELETIONS_HAVE_AT_LEAST_TWO_STRICT_UNSTABLE_EQUILIBRIA_EXACT_PASS 1bf98f43d7cbde5687705a58e994f043899ff2f5d4708814b52a7abe71e6964f`

Each CASES record preserves exact unreduced ordinary volume and centroid fractions, actual V/E/F and C, every strict-U witness found, its positive integer margin, and original deleted input labels. The complete deterministic generator replaces the1.76MB output, not an abbreviated output array.

## File exact_deletion.py
```python
"""Exact finite exclusion: delete up to three original D717 exposed inputs.
Enumerate ALL supporting triples using integer side masks, not floating hulls.
Every retained hull is simplicial (checked), closed, oriented, connected, full
-dimensional. Exact ordinary volume moments give two strict unstable witnesses.
This only excludes coordinate-fixed deletions in the explicitly stated family.
"""
from pathlib import Path
from itertools import combinations
from math import gcd,lcm
import json,hashlib,sys
assert __debug__
D=717
P=[[-1513,11,-219],[-1477,17,494],[-1401,170,-806],[-1132,451,399],[-1477,-104,-537],[-967,306,301],[-860,296,185],[-1366,-514,-149],[-1369,-243,830],[-1144,534,-1191],[-1008,-649,1324],[-324,1060,643],[-418,-983,-854],[0,1524,443],[-273,357,-1439],[-389,-1400,1971],[186,1064,677],[-16,-1695,-631],[421,-1700,1941],[208,834,-1594],[445,1739,226],[503,-2352,-213],[587,1751,-1733],[917,-1905,1672],[883,-2307,125],[600,2569,-394],[884,3415,-1871],[1046,-1956,1524],[1034,-2222,582],[978,1104,-648],[188,-2248,1078],[764,2962,-989]]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def pack(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def catalogue():
 rows=[]
 for i,j,k in combinations(range(32),3):
  n=cross(sub(P[j],P[i]),sub(P[k],P[i]));assert n!=(0,0,0),'collinear triple requires maximal-face extension'
  z=pos=neg=0
  for t,p in enumerate(P):
   v=dot(n,sub(p,P[i]))
   if v>0:pos|=1<<t
   elif v<0:neg|=1<<t
   else:z|=1<<t
  mask=(1<<i)|(1<<j)|(1<<k)
  assert z==mask,'A coplanar quadruple requires polygon grouping; no conclusion is asserted'
  d=det(P[i],P[j],P[k]);mom=[d*(P[i][a]+P[j][a]+P[k][a])for a in range(3)]
  rows.append((mask,pos,neg,(i,j,k),d,mom))
 return rows

def body(keep,rows):
 faces=[];v6=0;mom=[0,0,0]
 for mask,pos,neg,t,d,m in rows:
  if mask&keep!=mask:continue
  if not pos&keep:sg=1
  elif not neg&keep:sg=-1
  else:continue
  assert (pos|neg)&keep,'not full-dimensional'
  assert sg*d>0,'Origin must be interior for the positive first integration'
  faces.append(t if sg==1 else(t[0],t[2],t[1]));v6+=sg*d
  for a in range(3):mom[a]+=sg*m[a]
 assert v6>0
 vertices=sorted({i for t in faces for i in t});edges={}
 for t in faces:
  for i,j in zip(t,t[1:]+t[:1]):edges.setdefault(tuple(sorted((i,j))),[]).append((i,j))
 assert all(len(e)==2 and e[0]==e[1][::-1]for e in edges.values())
 assert len(vertices)-len(edges)+len(faces)==2 and 2*len(edges)==3*len(faces)
 adj={i:set()for i in vertices}
 for i,j in edges:adj[i].add(j);adj[j].add(i)
 seen=set();queue=[vertices[0]]
 while queue:
  i=queue.pop()
  if i not in seen:seen.add(i);queue.extend(adj[i]-seen)
 assert seen==set(vertices)
 C=2*len(edges);assert C>=32,'Operational search floor checked before mechanical tests'
 # Independent positive tetrahedra about the derived centre: exact first moments zero.
 den=4*v6;Z={i:tuple(den*P[i][a]-mom[a]for a in range(3))for i in vertices};cv=0;cm=[0,0,0]
 for i,j,k in faces:
  dv=det(Z[i],Z[j],Z[k]);assert dv>0;cv+=dv
  for a in range(3):cm[a]+=dv*(Z[i][a]+Z[j][a]+Z[k][a])
 assert cv==v6*den**3 and cm==[0,0,0]
 # c_int = mom/(4*v6). World centroid is c_int/717.
 remaining=[j for j in range(32)if keep>>j&1];unstable=[];margins=[]
 for i in vertices:
  w=[4*v6*P[i][a]-mom[a]for a in range(3)]
  vals=[-dot(w,sub(P[j],P[i]))for j in remaining if j!=i]
  if min(vals)>0:unstable.append(i);margins.append(min(vals))
 assert len(unstable)>=2,'This finite exclusion would fail'
 return {'VEF':[len(vertices),len(edges),len(faces)],'C':C,'volume_num':v6,'volume_den':6*D**3,'centroid_numerators':mom,'centroid_denominator':4*v6*D,'strict_U_witnesses':unstable,'witness_margins':margins},vertices

def main():
 out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False);rows=catalogue();allbits=(1<<32)-1;base,active=body(allbits,rows)
 assert active==[i for i in range(32)if i not in(5,6)];records=[];hist={}
 for n in range(4):
  batch=[]
  for drop in combinations(active,n):
   keep=allbits
   for i in drop:keep^=1<<i
   r,v=body(keep,rows);r['drop']=list(drop);records.append(r);batch.append(r)
  hist[str(n)]={'cases':len(batch),'minimum_U':min(len(r['strict_U_witnesses'])for r in batch),'minimum_C':min(r['C']for r in batch),'maximum_C':max(r['C']for r in batch)}
  print('D717_FIXED_DELETE_EXACT',n,hist[str(n)],flush=True)
 b=pack(records);(out/'CASES.json').write_bytes(b);summary={'scope':'All subsets obtained by deleting zero, one, two or three of the 30 exposed ORIGINAL D717 inputs, while retaining inputs5,6 and all undeleted exact coordinates/717. No moved/added point or larger deletion is excluded.','cases':len(records),'catalogue_triples':len(rows),'histogram':hist,'cases_bytes':len(b),'cases_sha256':hashlib.sha256(b).hexdigest(),'terminal':'D717_ALL_4526_FIXED_DELETIONS_HAVE_AT_LEAST_TWO_STRICT_UNSTABLE_EQUILIBRIA_EXACT_PASS'}
 assert len(records)==4526;(out/'SUMMARY.json').write_bytes(pack(summary));print(summary['terminal'],summary['cases_sha256'],flush=True)
if __name__=='__main__':main()
```
