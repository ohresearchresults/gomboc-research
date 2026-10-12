#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import hashlib
ROOT=Path(__file__).resolve().parent

def read_edges(name):
    E=[]
    for line in (ROOT/name).read_text().splitlines():
        if line.strip():
            u,v=map(int,line.split()); assert u<v; E.append((u,v))
    assert len(E)==len(set(E))
    return E
G=read_edges('C650_polar_edges.txt')
H=read_edges('H213_edges.txt')
assert len(G)==325 and len(H)==213 and set(H)<=set(G)
assert hashlib.sha256((ROOT/'C650_polar_edges.txt').read_bytes()).hexdigest()=='3039216e06fa3dd0d5790c6cb53cdc79eeb1bed17c98357cbea64c866a6d88fe'
assert hashlib.sha256((ROOT/'H213_edges.txt').read_bytes()).hexdigest()=='171a223c0e2ee52c36ba1076ec588d34aa056cc07efbde2f5d2c6104a805d911'
N=137
adj=[set() for _ in range(N)]
for u,v in H: adj[u].add(v);adj[v].add(u)
assert min(map(len,adj))>=3
for a in range(N):
  for b in range(a+1,N):
    root=next(v for v in range(N) if v not in (a,b)); seen={root}; st=[root]
    while st:
      u=st.pop()
      for v in adj[u]:
        if v not in (a,b) and v not in seen: seen.add(v);st.append(v)
    assert len(seen)==N-2,(a,b)
rot={}
for line in (ROOT/'H213_rotation.txt').read_text().splitlines():
    i,s=line.split(':',1); rot[int(i)]=[int(x) for x in s.strip().split(',') if x]
assert set(rot)==set(range(N))
for i in range(N): assert set(rot[i])==adj[i] and len(rot[i])==len(adj[i])
seen=set(); face_count=0
for u,v in sorted((u,v) for a,b in H for u,v in ((a,b),(b,a))):
  if (u,v) in seen: continue
  face_count+=1; a,b=u,v
  while (a,b) not in seen:
    seen.add((a,b)); rr=rot[b]; k=rr.index(a); a,b=b,rr[(k-1)%len(rr)]
assert len(seen)==2*len(H) and face_count==78 and N-len(H)+face_count==2
deg_groups={
 F(1,4):{42},
 F(3,4):{80},
 F(1):{1,2,4,5,9,10,11,12,22,23,25,26,27,28,30,31,33,34,35,36,37,41,49,56,61,62,63,66,67,70,71,93,98,99,101,109,135,136},
 F(1,2):{0,3,13,14,15,16,17,18,19,20,21,24,38,39,40,43,44,45,46,47,48,50,51,52,53,54,58,59,60,68,69,72,73,74,75,76,77,78,79,83,84,85,86,87,88,89,90,91,92,95,96,97,100,102,103,104,105,106,107,108,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134}
}
ydeg=[F(0) for _ in range(N)]
for w,S in deg_groups.items():
  for v in S: assert ydeg[v]==0; ydeg[v]=w
cuts=[
 (F(1,2),(2,100),{55,67,101}),
 (F(1),(10,34),{1,6,11}),
 (F(1,2),(26,36),{25,65}),
 (F(1,4),(26,41),{12,27,28,30,31,35,42,61,62,63,64,66,80,81,82,98,99,135,136}),
 (F(1),(28,30),{31,35,64,66,98,99,135}),
 (F(1,4),(12,61),{28,30,31,35,62,63,64,66,81,98,99,135,136}),
 (F(1,4),(26,61),{27,82}),
]
wupper={}
def setw(w,pairs):
  for e in pairs:
    e=tuple(sorted(e)); assert e in set(G) and e not in wupper; wupper[e]=w
setw(F(1),[(1,11),(1,34),(2,67),(4,5),(4,10),(10,11),(12,136),(22,23),(25,26),(25,36),(26,27),(27,61),(28,35),(28,62),(30,135),(30,136),(31,66),(31,135),(33,37),(35,98),(36,37),(41,70),(61,63),(62,63),(66,99),(67,101),(70,71),(98,99)])
setw(F(1,2),[(2,134),(3,109),(6,114),(13,71),(34,100),(45,71),(48,49),(49,106),(51,109),(56,92),(56,95),(93,95),(100,101),(109,110)])
setw(F(1,4),[(12,42),(41,42)])
for e in G:
  u,v=e; lhs=ydeg[u]+ydeg[v]
  for w,ban,S in cuts:
    if u not in ban and v not in ban and ((u in S)!=(v in S)): lhs+=w
  lhs-=wupper.get(e,F(0))
  assert lhs<=1,(e,lhs)
bound=3*sum(ydeg)+sum(w for w,_,_ in cuts)-sum(wupper.values())
assert bound==F(851,4)
print('C650_POLAR_MINIMUM_213_EXACT_CERTIFICATE_PASS')
print('G=(137,325), H=(137,213), faces(H)=78, primal abstract=(78,213,137), C=426')
print('LP_dual_lower_bound=',bound,'integer_lower_bound=213')
