"""Exact old-cover intersection with newly certified nine-arrow subgraphs.
No geometry samples. Standard library only. Run after check.py.
"""
from itertools import permutations,combinations,product
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
from inputs import TREES,OLD,NEW,PLAN
assert __debug__
def serial(x):return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def tree_code(p):
 ch=[[] for _ in p]
 for i in range(1,9):ch[p[i]].append(i)
 def walk(i):return '('+''.join(sorted(walk(j) for j in ch[i]))+')'
 return walk(0)
def rooted(p):
 for i in range(1,9):
  seen=set()
  while i:
   if i in seen:return False
   seen.add(i);i=p[i]
 return p[0]==0
def determinant(a):
 a=[list(map(F,r)) for r in a];out=F(1)
 for k in range(len(a)):
  j=next((j for j in range(k,len(a)) if a[j][k]),None)
  if j is None:return F(0)
  if j!=k:a[j],a[k]=a[k],a[j];out=-out
  p=a[k][k];out*=p
  for i in range(k+1,len(a)):
   t=a[i][k]/p
   for j in range(k,len(a)):a[i][j]-=t*a[k][j]
 return out
@lru_cache(None)
def canonical(edges):
 # Complete root-preserving isomorphism test; degree classes only prune.
 groups=defaultdict(list)
 for i in range(1,9):groups[(sum(b==i for a,b in edges),sum(a==i for a,b in edges))].append(i)
 parts=[groups[k] for k in sorted(groups)];starts=[];n=1
 for c in parts:starts.append(n);n+=len(c)
 best=None;bestpi=None
 for ps in product(*(permutations(c) for c in parts)):
  pi=[0]*9
  for st,pp in zip(starts,ps):
   for k,i in enumerate(pp):pi[i]=st+k
  code=tuple(sorted((pi[i],pi[j]) for i,j in edges))
  if best is None or code<best:best=code;bestpi=pi
 return best,bestpi
if __name__=='__main__':
 v=json.loads(Path('shadow_verified.json').read_text());raw=Path('shadow_exact.json').read_bytes()
 assert v['tag']=='NOVA24_F9_11_SHADOW_VERIFIED_V1' and v['cases']==12 and v['matrices']==3024 and v['coupling_matrices']==6
 assert v['coefficient_sha256']==hashlib.sha256(raw).hexdigest()
 bad={}
 for k,(o,ex,rows) in enumerate(PLAN):
  es=tuple(sorted([(i,TREES[o][i]) for i in range(1,9)]+[ex]));code,pi=canonical(es)
  assert code not in bad;bad[code]=(k,pi,es)
 allowed={tree_code(p) for p in TREES.values()};reports=[];oldtotal=0;newtotal=0;maxarcs=0;maxtrees=0;subsets=0;single=[]
 for o,p in TREES.items():
  base={(i,p[i]) for i in range(1,9)};optional=sorted(set(tuple(e) for fr in OLD[o] for e in fr));oldgraphs=[]
  for mask in range(1<<len(optional)):
   subsets+=1;extra=tuple(e for j,e in enumerate(optional) if mask>>j&1);edges=tuple(sorted(base|set(extra)))
   choices=[(0,)+q for q in product(*(sorted(j for a,j in edges if a==i) for i in range(1,9)))]
   if not all(rooted(q) and tree_code(q) in allowed for q in choices):continue
   L=[[0]*9 for _ in range(9)]
   for i,j in edges:L[i][i]+=1;L[i][j]-=1
   assert determinant([r[1:] for r in L[1:]])==len(choices)
   oldgraphs.append((extra,edges,len(choices)))
  maximal=[x for x,e,n in oldgraphs if not any(set(x)<set(y) for y,_,_ in oldgraphs)]
  assert {tuple(sorted(x)) for x in maximal}=={tuple(sorted(fr)) for fr in OLD[o]}
  kept=[];covered=[]
  for extra,edges,count in oldgraphs:
   witness=None
   for es in combinations(edges,9):
    if {a for a,b in es}!={1,2,3,4,5,6,7,8}:continue
    code,pi=canonical(es)
    if code not in bad:continue
    k,srcpi,srces=bad[code];inverse=[pi.index(i) for i in range(9)];transport=[inverse[srcpi[i]] for i in range(9)]
    assert sorted(transport)==list(range(9)) and transport[0]==0
    assert tuple(sorted((transport[i],transport[j]) for i,j in srces))==es
    witness=dict(certificate=k,permutation=transport,subgraph=es);break
   if witness is None:
    kept.append((extra,count));maxarcs=max(maxarcs,len(edges));maxtrees=max(maxtrees,count)
   else:
    covered.append(dict(extra=extra,**witness))
    if len(extra)==1:single.append([o,extra[0]])
  newmax=[(x,n) for x,n in kept if not any(set(x)<set(y) for y,_ in kept)]
  assert {tuple(sorted(fr)) for fr,n in newmax}=={tuple(sorted(fr)) for fr in NEW[o]}
  oldtotal+=len(oldgraphs);newtotal+=len(kept)
  reports.append(dict(ordinal=o,parent=p,old_count=len(oldgraphs),remaining=[dict(extra=x,trees=n) for x,n in kept],maximal=[dict(extra=x,trees=n) for x,n in newmax],excluded=covered))
  print('NEW_FRAME_COVER',o,len(oldgraphs),len(kept),len(newmax),flush=True)
 assert (subsets,oldtotal,newtotal,maxarcs,maxtrees,len(single))==(592,82,25,10,4,21)
 assert sum(len(r['maximal']) for r in reports)==11
 obj=dict(tag='NOVA24_F9_11_FRAME_COVER_V1',old_subsets=subsets,old_graphs=oldtotal,excluded_graphs=oldtotal-newtotal,remaining_graphs=newtotal,maximal_frames=11,maximum_arcs=maxarcs,maximum_trees=maxtrees,forbidden_single_extras=single,records=reports)
 b=serial(obj);Path('shadow_cover.json').write_bytes(b)
 print('EXHAUSTIVE_NEW_COVER_PASS',592,82,57,25,11,10,4)
 print('REPORT',len(b),hashlib.sha256(b).hexdigest())
 print('FIVE_FORMS_REMAIN_NO_NEW_C32_WHOLE_TYPE_OR_GLOBAL_BOUND')
