"""NEW standard-library replay of the parent's conditional graph theorem.
Not the unavailable original dual_frames.py. CPython 3.13.5; no random input.
Run: python -S recheck_frames.py. Tree ordinals are NOT C32 catalogue IDs.
"""
from itertools import product
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
assert __debug__
EXPECTED={253:(0,0,1,2,3,4,5,0,7),266:(0,0,1,2,3,4,5,4,0),272:(0,0,1,2,3,4,5,5,0),278:(0,0,1,2,3,4,5,6,0),285:(0,0,1,2,3,4,5,6,7)}
FRAMES = {
 253: [
  [(1,8)],
  [(2,8)],
  [(3,8)],
  [(7,6)],
  [(8,4),(8,5),(8,6)]
 ],
 266: [
  [(2,8),(5,7),(6,7)],
  [(2,8),(6,7),(7,5)],
  [(2,8),(7,5),(7,6)],
  [(7,5),(7,6),(7,8)]
 ],
 272: [
  [(2,8),(6,4),(6,7)],
  [(6,4),(6,7),(6,8)],
  [(2,8),(6,7),(7,4)],
  [(2,8),(6,4),(7,6)],
  [(2,8),(7,4),(7,6)],
  [(7,4),(7,6),(7,8)]
 ],
 278: [
  [(1,8)],
  [(3,8)],
  [(2,8),(6,4),(7,5)],
  [(2,8),(7,4),(7,5)],
  [(7,4),(7,5),(7,8)],
  [(8,7)]
 ],
 285: [
  [(2,0)],
  [(3,0)],
  [(7,0)],
  [(8,0)]
 ]
}
def rooted(p):
 for i in range(1,len(p)):
  seen=set()
  while i:
   if i in seen:return False
   seen.add(i);i=p[i]
 return p[0]==0
def canonical(p):
 assert rooted(p)
 children=[[] for _ in p]
 for i in range(1,len(p)):children[p[i]].append(i)
 def code(i):return '('+''.join(sorted(code(j) for j in children[i]))+')'
 text=code(0);parents=[];stack=[]
 for c in text:
  if c=='(':
   parents.append(stack[-1] if stack else 0);stack.append(len(parents)-1)
  else:stack.pop()
 return tuple(parents)
def trees(n):return sorted({canonical((0,)+t) for t in product(*(range(i) for i in range(1,n)))})
def determinant(a):
 a=[list(map(F,r)) for r in a];d=F(1)
 for i in range(len(a)):
  j=next((j for j in range(i,len(a)) if a[j][i]),None)
  if j is None:return F(0)
  if j!=i:a[j],a[i]=a[i],a[j];d=-d
  t=a[i][i];d*=t
  for j in range(i+1,len(a)):
   u=a[j][i]/t
   for k in range(i,len(a)):a[j][k]-=u*a[i][k]
 return d
def dag(edges):
 incoming=[0]*9;out=[[] for _ in range(9)]
 for i,j in edges:incoming[j]+=1;out[i].append(j)
 stack=[i for i in range(9) if incoming[i]==0];n=0
 while stack:
  i=stack.pop();n+=1
  for j in out[i]:
   incoming[j]-=1
   if incoming[j]==0:stack.append(j)
 return n==9
counts=[len(trees(n)) for n in range(1,10)]
assert counts==[1,1,2,4,9,20,48,115,286]
alltrees=trees(9);assert {i:alltrees[i] for i in EXPECTED}==EXPECTED
allowed=set(EXPECTED.values());records=[];subset_count=0;kept=0;maximum_arcs=0;maximum_trees=0
for ordinal,p in EXPECTED.items():
 base={(i,p[i]) for i in range(1,9)};extra=[]
 for i in range(1,9):
  for j in range(9):
   if j in (i,p[i]):continue
   q=list(p);q[i]=j
   if rooted(q) and canonical(q) in allowed:extra.append((i,j))
 valid=[]
 for mask in range(1<<len(extra)):
  subset_count+=1;s={e for k,e in enumerate(extra) if mask>>k&1};edges=base|s
  out=[sorted(j for a,j in edges if a==i) for i in range(1,9)]
  if not dag(edges):continue
  choices=[(0,)+q for q in product(*out)]
  if not all(rooted(q) and canonical(q) in allowed for q in choices):continue
  lap=[[0]*9 for _ in range(9)]
  for i,j in edges:lap[i][i]+=1;lap[i][j]-=1
  assert determinant([r[1:] for r in lap[1:]])==len(choices)
  valid.append((s,len(choices)));maximum_arcs=max(maximum_arcs,len(edges));maximum_trees=max(maximum_trees,len(choices))
 maximal=[(s,n) for s,n in valid if not any(s<t for t,_ in valid)]
 maximal.sort(key=lambda r:sorted(r[0]));kept+=len(valid)
 assert {tuple(sorted(t)) for t,_ in maximal}=={tuple(sorted(t)) for t in FRAMES[ordinal]}
 frames=[dict(extra=sorted(s),trees=n) for s,n in maximal]
 records.append(dict(ordinal=ordinal,parent=p,optional=extra,retained=len(valid),frames=frames))
 print('FRAMES_RECHECK',ordinal,len(extra),len(valid),len(maximal))
assert subset_count==592 and kept==82 and sum(len(r['frames']) for r in records)==25
assert [len(r['optional']) for r in records]==[7,6,7,8,4]
assert [r['retained'] for r in records]==[12,20,26,19,5]
assert [len(r['frames']) for r in records]==[5,4,6,6,4]
assert maximum_arcs==11 and maximum_trees==8
b=(json.dumps(dict(tag='NOVA24_FRAMES_NEW_RECHECK_V1',counts=counts,subsets=subset_count,retained=kept,max_arcs=maximum_arcs,max_trees=maximum_trees,records=records),sort_keys=True,separators=(',',':'))+'\n').encode()
Path('frames_new.json').write_bytes(b)
print('CONDITIONAL_FIVE_FORM_GRAPH_THEOREM_RECHECK_PASS',592,82,25,11,8)
print('REPORT',len(b),hashlib.sha256(b).hexdigest())
print('ORIGINAL_281_MATRIX_CERTIFICATES_NOT_REPLAYED')
