"""Exact physical stellar caps on large nonstable facets, within both C readings.
The coordinate origin is only a construction reference, not a mass-centre claim.
Every old/new vertex satisfies every proposed plane exactly; full B reaudits mass.
"""
import sys,json,hashlib,itertools,numpy as np
from math import gcd,lcm
from pathlib import Path
from gmpy2 import mpq as Q
from canonical_atlas import ROOT,Chart
from audit_free_supports import audit as freeze
sys.set_int_max_str_digits(0);sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'));import check_B
check_B.Q=Q
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def plane(a,b,c):
 n=cross(sub(b,a),sub(c,a));h=dot(n,a)
 if h<0:n=tuple(-v for v in n);h=-h
 den=lcm(*(int(x.denominator) for x in (*n,h)));ints=[int(x*den) for x in (*n,h)];g=gcd(*ints);return tuple(v//g for v in ints)
f=ROOT/'artifacts/canonical_atlas/VC47D_supports71';c=Chart(f);g=c.graph(np.load(f/'own_strict121/STRICT_NUMERICAL_q.npy'));base=ROOT/'artifacts/VC47D_large_caps';base.mkdir(exist_ok=False);np.save(base/'source_supports.npy',g['Y']);r=freeze(base/'source_supports.npy',base/'parent_exact_g12',10**12);X=[tuple(map(Q,p)) for p in r['raw_vertices']];rows=[tuple(map(int,(*n,h))) for n,h in zip(r['normals'],r['offsets'])];faces=r['faces'];possible=sorted([(len(face),fi) for fi,face in enumerate(faces) if fi not in r['stable_face_ids']],reverse=True);chosen=[];cost=0
for size,fi in possible:
 if cost+size<=248-r['E']:chosen.append(fi);cost+=size
 if len(chosen)==3:break
assert len(chosen)==3 and r['E']+cost<=248
for power in [4,5,6]:
 eps=Q(1,10**power);P=list(X);added=[];H=[row for fi,row in enumerate(rows) if fi not in chosen];valid=True
 for fi in chosen:
  face=faces[fi];a=tuple(sum(X[v][k] for v in face)/len(face) for k in range(3));p=tuple((1+eps)*v for v in a);added.append(p);P.append(p)
  if not all(dot(n[:3],p)<n[3] for fj,n in enumerate(rows) if fj!=fi):valid=False
  for i,j in zip(face,face[1:]+face[:1]):H.append(plane(X[i],X[j],p))
 if valid:valid=all(dot(n[:3],p)<=n[3] for n in H for p in P)
 out=base/f'caps_eps1e{power}';out.mkdir();data=dict(source=str(base/'parent_exact_g12/audit.json'),source_sha256=hashlib.sha256((base/'parent_exact_g12/audit.json').read_bytes()).hexdigest(),chosen_faces=chosen,face_sizes=[len(faces[i]) for i in chosen],epsilon=str(eps),formula='cap point (1+epsilon) times arithmetic mean of exact host facet vertices in the source coordinate frame',added_points=[[str(v) for v in p] for p in added],exact_plane_admission=valid);(out/'construction.json').write_bytes(B(data))
 if not valid:print('EXACT_CAP_REJECTED',power,flush=True);continue
 body={'H':[list(row) for row in H]};(out/'H.json').write_bytes(B(body));a=check_B.run(body);pv={tuple(map(Q,p)) for p in a['raw_vertices']};assert pv==set(P);assert a['E']==r['E']+cost;assert a['F']==r['F']+cost-len(chosen);assert a['V']==r['V']+len(chosen);(out/'audit.json').write_bytes(B(a));s={k:a[k] for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};s['audit_sha256']=hashlib.sha256(B(a)).hexdigest();(out/'summary.json').write_text(json.dumps(s,indent=2)+'\n');print('EXACT_MIXED_CAP_COMPLEX',power,s,flush=True)
