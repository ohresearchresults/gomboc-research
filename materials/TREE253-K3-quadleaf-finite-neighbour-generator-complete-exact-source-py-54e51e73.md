# material-54e51e73fc01

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Finite genuine-map neighbours of native55, not a complete K3 census.
A native dual edge is removed and a face diagonal added; TREE253 is retained.
Only validated spherical polyhedral maps, exact K=3, no 056, and a single
quadrivalent leaf of the complementary Hamilton path are output.
"""
from itertools import combinations as C
from pathlib import Path
import json,hashlib,sys
assert __debug__ and len(sys.argv)==2
BASE=Path(sys.argv[1])
PIN='58126aee072933749b18eca00ac4d32842e56e6ac8d662d06713bacef28bf96e'
TREE={tuple(sorted(e)) for e in [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(0,7),(7,8)]}
Z=[6,5,4,3,2,1,0,7,8]
def canon(c):
 r=[]
 for x in [c,list(reversed(c))]:
  for k in range(len(x)):r.append(tuple(x[k:]+x[:k]))
 return min(r)
def edges(c):return {tuple(sorted(e)) for e in zip(c,c[1:]+c[:1])}
def cycle(es):
 ad={v:[] for e in es for v in e}
 for a,b in es:ad[a].append(b);ad[b].append(a)
 if any(len(v)!=2 for v in ad.values()):return None
 out=[min(ad)]
 while len(out)<len(ad):
  opts=sorted(v for v in ad[out[-1]] if v not in out)
  if not opts:return None
  out.append(opts[0])
 if out[0] not in ad[out[-1]]:return None
 return out

def validate(faces):
 if len(faces)!=10 or len({tuple(sorted(c)) for c in faces})!=10:return None
 inc=[set(c) for c in faces];owners={}
 for i,c in enumerate(faces):
  if len(c)<3 or len(c)!=len(set(c)):return None
  for e in edges(c):owners.setdefault(e,[]).append(i)
 if len(owners)!=17 or any(len(x)!=2 for x in owners.values()) or not TREE<=set(owners):return None
 if set().union(*inc)!=set(range(9)):return None
 for i,j in C(range(10),2):
  I=inc[i]&inc[j]
  if len(I)>2 or (len(I)==2 and tuple(sorted(I)) not in edges(faces[i])&edges(faces[j])):return None
 # Each vertex link is one cycle, not a disjoint union of cyclic links.
 for v in range(9):
  links=[]
  for c in faces:
   if v in c:
    k=c.index(v);links.append(tuple(sorted((c[k-1],c[(k+1)%len(c)]))))
  if cycle(links) is None:return None
 ad={v:set() for v in range(9)}
 for a,b in owners:ad[a].add(b);ad[b].add(a)
 for k in range(3):
  for removed in C(range(9),k):
   left=set(range(9))-set(removed);seen={min(left)};todo=list(seen)
   while todo:
    v=todo.pop()
    for w in ad[v]&left-seen:seen.add(w);todo.append(w)
   if seen!=left:return None
 if any({0,5,6}<=I for I in inc):return None
 windows=[i for i in range(7) if any(set(Z[i:i+3])<=I for I in inc)]
 if len(windows)!=3:return None
 pe=sorted(tuple(sorted(o)) for e,o in owners.items() if e not in TREE)
 pad={v:[] for v in range(10)}
 for a,b in pe:pad[a].append(b);pad[b].append(a)
 ends=[i for i in pad if len(pad[i])==1]
 if len(ends)!=2 or any(len(pad[i])!=2 for i in pad if i not in ends):return None
 if sorted(len(inc[i]) for i in ends)!=[3,4]:return None
 path=[min(ends)]
 while len(path)<10:
  opt=[v for v in pad[path[-1]] if v not in path]
  if len(opt)!=1:return None
  path.append(opt[0])
 quad=next(i for i in ends if len(inc[i])==4)
 return {'incidence':[''.join(map(str,sorted(I))) for I in inc], 'dual_faces':faces,
         'dual_edges':sorted(owners),'tree_edges':pe,'path':path,'quad_leaf':quad,'windows':windows}

def main():
 b=BASE.read_bytes();assert len(b)==2630 and hashlib.sha256(b).hexdigest()==PIN
 data=[l.split(':')[1].split() for l in b.decode().splitlines()]
 out={}
 for ni,row in enumerate(data):
  I=[set(map(int,s)) for s in row]
  de={tuple(sorted(I[a]&I[b])) for a,b in C(range(10),2) if len(I[a]&I[b])==2}
  fs=[cycle([e for e in de if set(e)<=s]) for s in I];assert all(fs)
  for rem in sorted(de-TREE):
   who=[i for i,f in enumerate(fs) if rem in edges(f)];assert len(who)==2
   i,j=who;merged=cycle((edges(fs[i])|edges(fs[j]))-{rem})
   if merged is None:continue
   base=[f for k,f in enumerate(fs) if k not in who]+[merged]
   remaining=de-{rem}
   for fi,f in enumerate(base):
    for a,b in C(range(len(f)),2):
     add=tuple(sorted((f[a],f[b])))
     if add in remaining or add==rem:continue
     aa=f[a:b+1];bb=f[b:]+f[:a+1]
     if min(len(aa),len(bb))<3:continue
     nf=[c for k,c in enumerate(base) if k!=fi]+[aa,bb]
     nf=[list(canon(c)) for c in nf];nf.sort(key=lambda c:tuple(sorted(c)))
     rec=validate(nf)
     if rec is None:continue
     key=tuple(rec['incidence'])
     if key not in out:out[key]={**rec,'generated_from_native':ni,'removed_dual_edge':rem,'added_dual_edge':add}
 records=[out[k] for k in sorted(out)]
 p=Path(__file__).with_name('neighbor_k3_quadleaf.json')
 raw=(json.dumps(records,sort_keys=True,separators=(',',':'))+'\n').encode();p.write_bytes(raw)
 print('K3_QUADLEAF_NEIGHBOUR_TEMPLATES_NOT_COMPLETE_CENSUS',len(records),len(raw),hashlib.sha256(raw).hexdigest())
 print(json.dumps(records[0],indent=2))
if __name__=='__main__':main()
