# material-7589d5aa6549

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

import depth_incidence_cap300 as m
from itertools import combinations
from collections import Counter
c=m.native_census();ee=c['lex_edges'];rows=c['selected_xz_chains'];all_counts=Counter();uniq={}

def height(n,arcs,root):
 rev=[[]for i in range(n)]
 for a,b in arcs:rev[b].append(a)
 dd=[None]*n;dd[root]=0;que=[root]
 for a in que:
  for b in rev[a]:
   if dd[b] is None:dd[b]=dd[a]+1;que.append(b)
 return max(dd)
def acyclic(n,arcs):
 out=[[]for i in range(n)];ind=[0]*n
 for a,b in arcs:out[a].append(b);ind[b]+=1
 q=[i for i in range(n) if not ind[i]]
 for a in q:
  for b in out[a]:
   ind[b]-=1
   if not ind[b]:ind[b]-=1
   if not ind[b]:q.append(b)
 return len(q)==n
for row in rows:
 pv=row['primal_parent'];threshold=4 if row['dual_height']==6 else 3
 key=(row['mask'],threshold)
 if key in uniq:continue
 base=[(i,pv[i])for i in range(10) if i!=9]
 excluded=[e for k,e in enumerate(ee) if not(row['mask']>>k&1)]
 cand=[arc for a,b in excluded for arc in [(a,b),(b,a)] if acyclic(10,base+[arc])]
 bad=[]
 for n in range(1,len(cand)+1):
  for ids in combinations(range(len(cand)),n):
   s=frozenset(ids)
   if any(b<=s for b in bad):continue
   arcs=[cand[i]for i in ids]
   if not acyclic(10,base+arcs):continue
   if height(10,base+arcs,9)<=threshold:bad.append(s)
 hist=Counter(map(len,bad));uniq[key]=(len(cand),len(bad),hist)
 all_counts.update(hist)
 print(key,uniq[key])
print('unique',len(uniq),'sumhist',all_counts)
