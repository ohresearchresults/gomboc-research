# material-c07bde4136e9

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# COORD_C622_TRIANGLE53_COMBINATORIAL_CENSUS_V2 — complete source recovery

This is an exact finite combinatorial result, NOT a family of realized convex coordinates and NOT an equilibrium result. Canonical parent is VQ20_C622_ROUTE88_118_G12, immutable result figure-0373, SHA256 8a9f5de8374e75eb2e09766c3546f750afd74102ae1fc3bddef86c4da45dc68d. The parent is actual V176/E311/F137,C622,own110/weak000. This computation does not improve the accepted C.

## Exact dependencies and replay
The canonical source and its full independent auditors are recoverable from BOTH ordered complete SCOPED16 materials:
1. [internal-source-reference],15305 bytes,SHA256 d5846089dd79e70e4aa35f67d5d66b8480c3dd72bca1de45359a281931f632aa.
2. [internal-source-reference],20685 bytes,SHA256 c4a0ef05c36066f7b2851dc18ea1c3cda599f724130ec0ce7a89785613cde5b1.
Their complete decoder and REPLAY_SCOPED.py regenerate canonical A.json,311825 bytes,SHA256 142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0. No FULL76 dependency is needed. Save the single source block below as TRIANGLE_CENSUS_V2.py,UTF-8 with LF and exactly one trailing LF. It is4670bytes,SHA256 a23f78ea7273b8905bd927accbaa8662a2fe3b8912547f8fb1ec3aad2760a979.

Command, after canonical reconstruction:
python -B -S TRIANGLE_CENSUS_V2.py CANONICAL_PROOF/A.json NEW_TRIANGLE_CENSUS_V2.json

Environment observed: CPython3.13.5,standard library only,assertions enabled. No seeds,tolerances,numerical geometry,or external solvers. Expected output JSON16154bytes,SHA256 4d77735c117e3d80f13d0309e56ae95bc7a7842561d73c6f75ce2d9d6995a57a. Observed terminal: C622_TRIANGLE_COMBINATORIAL_CENSUS_PASS.

## Mathematical scope and results
The canonical apex-incident and stable-face-boundary edge sets have disjoint union size64. Among the remaining true edges,69 touch at least one of the51 triangular maximal facets. For each edge the source merges its two physical rawlex labels, removes repetitions and collapsed two-cycles, reconstructs surviving oriented face cycles, and checks simple distinct facets, two oppositely oriented facets per edge, Euler, E'=E-1-common-neighbour-count, proper pairwise face intersections, and vertex3connectivity. The last check runs a complete articulation test on G-v for every surviving vertex; tetrahedral,cycle,and disconnected controls are included.

Exactly53 pass these necessary combinatorial checks:51 lose one triangle and give proposed175/309/136,C618;2 lose two triangles and give proposed175/308/135,C616. The16 rejected candidates consist of14 one-triangle and2 two-triangle cases; each violates proper face intersection and3connectivity. V2 strengthens the two-shared-vertices test to require the edge to have exactly those two incident facets. Its counts equal the earlier V1 census; V2 is authoritative.

The two passing C616 targets are physical rawlex edges[11,17] (dropped original supports8,9;common neighbours13,94) and[137,173] (dropped supports45,83;common neighbours134,141). These are not polar edge labels. The first endpoints own[5,7,8,9]and[8,9,20,54]; the second own[45,76,83]and[45,46,82,83,84,103]. No coordinate contraction, facet planarity, convex realization, actual own-centroid mechanics, or full reduced-body audit is asserted. Further facet suppression must rebuild support labels and the contact atlas; deleting support rows or averaging endpoints alone is insufficient.

## TRIANGLE_CENSUS_V2.py
```python
"""Exact combinatorial census on the canonical maximal face lattice.
No realizability, equilibrium, or convex-coordinate claim is made for a quotient.
"""
import sys,json,hashlib,itertools
from pathlib import Path
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
assert __debug__ and len(sys.argv)==3
p=Path(sys.argv[1]);out=Path(sys.argv[2]);assert not out.exists()
assert hashlib.sha256(p.read_bytes()).hexdigest()=='142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0'
r=json.loads(p.read_text());faces=r['faces'];es={tuple(e):[] for e in r['edges']};adj={i:set() for i in range(r['V'])}
for f,c in enumerate(faces):
 for a,b in zip(c,c[1:]+c[:1]):es[tuple(sorted((a,b)))].append(f)
for a,b in es:adj[a].add(b);adj[b].add(a)
assert all(len(x)==2 for x in es.values())
root=r['unstable_vertices'][0];sf=r['stable_face_ids'][0];stable=faces[sf]
protected={e for e in es if root in e}|{tuple(sorted(e)) for e in zip(stable,stable[1:]+stable[:1])}
def biconnected(g,skip):
 # Complete Tarjan articulation test on G minus one vertex.
 nodes=set(g)-{skip};disc={};low={};parent={};time=0;arts=set()
 def dfs(u):
  nonlocal time
  disc[u]=low[u]=time;time+=1;children=0
  for v in sorted(g[u]-{skip}):
   if v not in disc:
    parent[v]=u;children+=1;dfs(v);low[u]=min(low[u],low[v])
    if u not in parent and children>1:arts.add(u)
    if u in parent and low[v]>=disc[u]:arts.add(u)
   elif parent.get(u)!=v:low[u]=min(low[u],disc[v])
 dfs(min(nodes))
 return len(disc)==len(nodes) and not arts,sorted(arts)

# Controls on the connectivity algorithm: tetrahedral graph, cycle, disconnected graph.
k4={i:set(range(4))-{i} for i in range(4)}
assert all(biconnected(k4,v)[0] for v in k4)
c4={i:{(i-1)%4,(i+1)%4} for i in range(4)}
assert all(not biconnected(c4,v)[0] for v in c4)
k4twice={i:set(range(4*(i//4),4*(i//4)+4))-{i} for i in range(8)}
assert all(not biconnected(k4twice,v)[0] for v in k4twice)
def quotient(edge):
 keep,gone=edge;new=[];dropped=[]
 for f,c in enumerate(faces):
  cc=[]
  for v in c:
   v=keep if v==gone else v
   if not cc or cc[-1]!=v:cc.append(v)
  if len(cc)>1 and cc[0]==cc[-1]:cc.pop()
  if len(cc)<3:dropped.append(f)
  else:new.append((f,cc))
 t=len(dropped);common=sorted(adj[keep]&adj[gone]);g={v:set() for v in adj if v!=gone};edges={};errors=[]
 sets=[frozenset(c) for f,c in new]
 if any(len(c)!=len(set(c)) for f,c in new):errors.append('repeated_vertex_in_face')
 if len(set(sets))!=len(sets):errors.append('duplicate_face_vertex_set')
 for f,c in new:
  for u,v in zip(c,c[1:]+c[:1]):
   edges.setdefault(tuple(sorted((u,v))),[]).append((f,u,v));g[u].add(v);g[v].add(u)
 if any(len(v)!=2 or v[0][1:]!=v[1][1:][::-1] for v in edges.values()):errors.append('nonmanifold_or_orientation')
 if len(g)-len(edges)+len(new)!=2:errors.append('euler')
 if len(edges)!=r['E']-1-len(common):errors.append('graph_edge_count')
 bad_intersections=[]
 for i,j in itertools.combinations(range(len(new)),2):
  s=sets[i]&sets[j]
  wrong=len(s)>2
  if len(s)==2:
   e=tuple(sorted(s));wrong=e not in edges or {new[i][0],new[j][0]}!={v[0] for v in edges[e]}
  if wrong:bad_intersections.append([new[i][0],new[j][0],sorted(s)])
 if bad_intersections:errors.append('nonpolyhedral_face_intersection')
 conn=True;separator=None
 for v in sorted(g):
  good,arts=biconnected(g,v)
  if not good:conn=False;separator=[v,arts[0]] if arts else [v];break
 if not conn:errors.append('not_3connected')
 return dict(edge=list(edge),incident_facets=es[edge],incident_facet_sizes=[len(faces[f]) for f in es[edge]],dropped_facets=dropped,common_neighbours=common,V=len(g),E=len(edges),F=len(new),C=2*len(edges),errors=errors,separator=separator,bad_face_intersections=bad_intersections)
rows=[]
for e,ff in sorted(es.items()):
 if e not in protected and any(len(faces[f])==3 for f in ff):rows.append(quotient(e))
counts={}
for row in rows:
 key=str((len(row['dropped_facets']),not row['errors']));counts[key]=counts.get(key,0)+1
result=dict(identity='CANONICAL_C622_TRIANGULAR_FACET_CONTRACTION_COMBINATORIAL_CENSUS_V2',parent_A_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),status='FINITE_COMBINATORIAL_ONLY_NOT_COORDINATE_REALIZATIONS',protected_edge_count=len(protected),triangle_count=sum(len(c)==3 for c in faces),unprotected_triangle_edge_count=len(rows),counts=counts,candidates=rows)
assert counts=={'(1, True)':51,'(2, True)':2,'(1, False)':14,'(2, False)':2},counts
assert [q['edge'] for q in rows if not q['errors'] and len(q['dropped_facets'])==2]==[[11,17],[137,173]]
out.write_bytes(B(result));print('C622_TRIANGLE_COMBINATORIAL_CENSUS_PASS',json.dumps({k:v for k,v in result.items() if k!='candidates'}),flush=True)
```
