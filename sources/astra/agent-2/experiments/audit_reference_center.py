"""Exact equilibrium census at a specified NONUNIFORM reference point.
The homogeneous body and its own centroid/census remain the source audit's.
This result must never be promoted as an own-centroid figure.
"""
import sys,json,hashlib
from pathlib import Path
from gmpy2 import mpq as Q
import numpy as np
ROOT=Path(__file__).resolve().parents[1];sys.set_int_max_str_digits(0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,s):return tuple(x*s for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def sign(x):return int(x>0)-int(x<0)
src=ROOT/'artifacts/projected_contact_retire/delete_4_35_94_99/audit.json';raw=src.read_bytes();r=json.loads(raw);X=[tuple(map(Q,row)) for row in r['raw_vertices']];N=[tuple(map(Q,row)) for row in r['normals']];H=list(map(Q,r['offsets']));actual=tuple(map(Q,r['raw_centroid']));R=max(np.linalg.norm([float(x-y) for x,y in zip(v,actual)]) for v in X);re=json.loads((ROOT/'artifacts/reference_projective_C490/result.json').read_text());cf=np.array([float(v) for v in actual])+R*np.array(re['reference_center']);center=tuple(Q(round(v*10**12),10**12) for v in cf);Z=[sub(x,center) for x in X];faces=r['faces'];fs=[];vs=[];es=[];stable=[];unstable=[];saddles=[];weak=[[],[],[]];ef={}
for f,cy in enumerate(faces):
 n=N[f];height=H[f]-dot(n,center);assert height>0;p=mul(n,height/dot(n,n));sg=[]
 for i,j in zip(cy,cy[1:]+cy[:1]):sg.append(sign(dot(n,cross(sub(Z[j],Z[i]),sub(p,Z[i])))));ef.setdefault(tuple(sorted((i,j))),[]).append(f)
 fs.append(sg)
 if min(sg)>0:stable.append(f)
 elif min(sg)>=0:weak[0].append(f)
for i,z in enumerate(Z):
 s=max(dot(z,sub(w,z)) for j,w in enumerate(Z) if i!=j);vs.append(sign(s))
 if s<0:unstable.append(i)
 elif s==0:weak[1].append(i)
for (i,j),ff in sorted(ef.items()):
 assert len(ff)==2;d=sub(Z[j],Z[i]);t=-dot(Z[i],d)/dot(d,d);p=add(Z[i],mul(d,t));n,m=[N[k] for k in ff];D=cross(n,m);sg=list(map(sign,[t,1-t,dot(cross(p,m),D),dot(cross(n,p),D)]));es.append([i,j,*sg])
 if min(sg)>0:saddles.append([i,j])
 elif min(sg)>=0:weak[2].append([i,j])
result=dict(evidence_scope='EXACT_REFERENCE_POINT_ONLY_NOT_OWN_CENTROID',source_audit=str(src),source_sha256=hashlib.sha256(raw).hexdigest(),reference_center=[str(v) for v in center],unchanged_uniform_centroid=r['raw_centroid'],unchanged_uniform_counts=r['counts'],V=r['V'],E=r['E'],F=r['F'],reference_counts=[len(stable),len(unstable),len(saddles)],reference_weak=list(map(len,weak)),reference_primitive_zeros=[sum(s.count(0) for s in fs),vs.count(0),sum(s[2:].count(0) for s in es)],stable=stable,unstable=unstable,saddles=saddles,face_signs=fs,vertex_max_escape_signs=vs,edge_signs=es);out=ROOT/'artifacts/reference110_exact_C490';out.mkdir(exist_ok=False);(out/'audit.json').write_text(json.dumps(result,indent=2)+'\n');print({k:result[k] for k in ['evidence_scope','V','E','F','reference_counts','reference_weak','reference_primitive_zeros','unchanged_uniform_counts','stable','unstable']},flush=True)
