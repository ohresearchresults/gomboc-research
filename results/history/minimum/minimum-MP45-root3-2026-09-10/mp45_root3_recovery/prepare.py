from pathlib import Path
import json,hashlib,sys,time
sys.path.insert(0,'nova54_recovery')
import comb
from mp45_mass_gate import geometry
FS=tuple(tuple(map(int,s))for s in '014 021 032 043 125 154 235 347 365 376 458 487 568 678'.split())
A={1200,1205,1472,1752,1775,3058,3124,3149,3966,5772,7000}
G=comb.catalogue(True);g=G[45];assert tuple(map(tuple,g['facets']))==FS
pp=comb.parent_trees(g,3);assert len(pp)==9140
print('CATALOGUE',comb.pin(comb.encoded(G)),'TREES',len(pp),flush=True)
shape=comb.code(pp[1200],3);tri={frozenset(f)for f in FS}
def broom(p):
 out=[]
 for i in range(9):
  q=[i]
  while q[-1]!=3:q.append(p[q[-1]])
  out.append(q)
 b=list(reversed(max(out,key=len)))
 assert len(b)==8
 return b+[next(i for i in range(9)if i not in b)]
sel={i:list(p)for i,p in enumerate(pp)if comb.code(p,3)==shape and frozenset(broom(p)[5:8])in tri}
assert len(sel)==66 and A<=set(sel)
plan=json.loads(Path('nova54_recovery/plan.json').read_bytes());S=comb.shapes()
good={comb.code(p)for p in S if comb.generic_safe(p)}|{comb.code(S[i])for i,power in plan['generic']}
unsafe=[i for i,p in enumerate(pp)if not comb.safe(p,3,FS)and comb.code(p,3)not in good]
offset=19062-unsafe.index(145)
assert offset+unsafe.index(1481)==19249
print('ROOT3_SCOPE',len(unsafe),offset,offset+len(unsafe),flush=True)
assert {i for j,i in enumerate(unsafe)if plan['codes'][offset+j]=='X'}==A
out=[]
for j,ix in enumerate(unsafe):
 if ix not in sel or ix in A:continue
 serial=offset+j;ch=plan['codes'][serial]
 if ch=='A':params=['ordinary',[3],[3],8]
 elif 'B'<=ch<='J':params=['ordinary',[3,ord(ch)-66],None,8]
 elif 'K'<=ch<='S':params=['shared',[3,ord(ch)-75],None,8]
 elif ch=='T':params=['volume',list(range(9)),None,8]
 else:
  assert ch=='U';params=plan['exceptions'][str(serial)]
 out.append(dict(index=ix,parent=list(pp[ix]),serial=serial,plan=params))
assert len(out)==55
obj=dict(graph=g,terminal=sel,old=out)
b=comb.encoded(obj);Path('input.json').write_bytes(b);print('INPUT',len(b),hashlib.sha256(b).hexdigest(),flush=True)
print('LITERAL_OLD_PLANS',json.dumps(out,separators=(',',':')),flush=True)
print('BOUNDARY',len(geometry()[0]),len(geometry()[2]),flush=True)
