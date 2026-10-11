"""Exact inherited-rotation and deterministic face-ID reconciliation.
Usage: python3 -S rotation_certificate.py BODY [BODY ...]
Inputs are the literal C650/H213 rotation data and freshly reconstructed A.json.
"""
from pathlib import Path
import json,hashlib,sys
R=Path(__file__).resolve().parent
G={int(k):v for k,v in json.loads((R/'C650_rotation.json').read_text()).items()}
H={tuple(map(int,l.split())) for l in (R/'H213_edges.txt').read_text().splitlines()}
HR={}
for line in (R/'H213_rotation.txt').read_text().splitlines():
 i,s=line.split(':',1);HR[int(i)]=list(map(int,s.strip().split(',')))
def norm(c):return min(tuple(c[k:]+c[:k]) for k in range(len(c)))
def faces(rot):
 seen=set();out=[]
 for a,b in sorted((i,j) for i,r in rot.items() for j in r):
  if (a,b) in seen:continue
  u,v=a,b;cy=[]
  while (u,v) not in seen:
   seen.add((u,v));cy.append(u);rr=rot[v];u,v=v,rr[(rr.index(u)-1)%len(rr)]
  assert (u,v)==(a,b);out.append(cy)
 assert len(seen)==sum(map(len,rot.values()));return out
HF=faces(HR)
assert HF[3]==[1,6,11] and len(HF[2])==44
for name in sys.argv[1:]:
 d=R/name;a=json.loads((d/'A.json').read_text());ef={};owners=[[] for _ in a['raw_vertices']]
 for fi,cy in enumerate(a['faces']):
  for v in cy:owners[v].append(fi)
  for u,v in zip(cy,cy[1:]+cy[:1]):ef.setdefault(tuple(sorted((u,v))),[]).append(fi)
 assert all(len(v)==2 for v in ef.values());edges={tuple(sorted(v)) for v in ef.values()}
 rr={}
 for fi,cy in enumerate(a['faces']):
  rr[fi]=[next(j for j in ef[tuple(sorted((u,v)))] if j!=fi) for u,v in zip(cy,cy[1:]+cy[:1])]
 inherited={i:[j for j in G[i] if tuple(sorted((i,j))) in edges] for i in G}
 same=all(norm(rr[i])==norm(inherited[i]) for i in G)
 reverse=all(norm(rr[i][::-1])==norm(inherited[i]) for i in G)
 assert same or reverse
 ff=faces(inherited);key={tuple(sorted(o)):i for i,o in enumerate(owners)};assert len(key)==a['V']
 mapping=[key[tuple(sorted(c))] for c in ff];assert len(mapping)==a['V'] and set(mapping)==set(range(a['V']))
 contains=H<=edges
 if contains:
  filtered={i:[j for j in inherited[i] if tuple(sorted((i,j))) in H] for i in G}
  assert faces(filtered)==HF
 out=dict(tag=name,orientation='same' if same else 'reversed',polar_edges=sorted(edges),inherited_rotation=inherited,inherited_polar_faces=ff,polar_face_id_to_primal_A_id=mapping,primal_A_unstable_to_polar_face_id=[[u,mapping.index(u)] for u in a['unstable_vertices']],contains_literal_H213=contains,H213_face_ids_preserved_when_filtered=contains)
 blob=json.dumps(out,sort_keys=True,separators=(',',':')).encode();(d/'ROTATION_CERTIFICATE.json').write_bytes(blob)
 print(name,'EXACT_INHERITED_ROTATION_AND_FACE_IDS_PASS',len(blob),hashlib.sha256(blob).hexdigest(),out['primal_A_unstable_to_polar_face_id'],flush=True)
