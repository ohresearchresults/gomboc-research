#!/usr/bin/env python3
from pathlib import Path
import re,json,csv
from fractions import Fraction as Q
import numpy as np
R=Path(__file__).resolve().parent;cert=json.load(open(R/'certificate.json'));V=[];T=[]
for line in (R/'body.obj').read_text().splitlines():
 if line.startswith('v '):V.append(tuple(float(x) for x in line.split()[1:4]))
 elif line.startswith('f '):T.append(tuple(int(x.split('/')[0])-1 for x in line.split()[1:4]))
V=np.asarray(V);T=np.asarray(T,int);assert len(V)==61 and len(T)==118
edges={tuple(sorted((int(a),int(b)))) for t in T for a,b in ((t[0],t[1]),(t[1],t[2]),(t[2],t[0]))}
assert all(sum(tuple(sorted((int(a),int(b))))==e for t in T for a,b in ((t[0],t[1]),(t[1],t[2]),(t[2],t[0])))==2 for e in edges)
assert len(edges)==177 and len(V)-len(edges)+len(T)==2
X=[]
for r in csv.DictReader(open(R/'coordinates_active_centered.csv')):X.append(tuple(float(Q(r[k])) for k in ('x_exact','y_exact','z_exact')))
assert np.max(np.abs(V-np.asarray(X)))<2e-14
D6=0.;M=np.zeros(3)
for a,b,c in V[T]:d=float(np.dot(a,np.cross(b,c)));D6+=d;M+=d*(a+b+c)
vol=D6/6;com=M/(4*D6);assert vol>0 and abs(vol-cert['volume_decimal'])<3e-10;assert np.linalg.norm(com)<5e-14
sv=[tuple(map(float,m)) for m in re.findall(r'vertex\s+([-+0-9.eE]+)\s+([-+0-9.eE]+)\s+([-+0-9.eE]+)',(R/'body.stl').read_text())];assert len(sv)==3*len(T)
def keytri(t):return tuple(sorted(tuple(round(float(x),12) for x in p) for p in t))
assert sorted(keytri(tuple(V[i] for i in tri)) for tri in T)==sorted(keytri(tuple(sv[3*k:3*k+3])) for k in range(len(T)))
print('PASS OBJ/STL watertight correspondence');print('vertices triangles mesh_edges Euler',len(V),len(T),len(edges),len(V)-len(edges)+len(T));print('volume',repr(vol),'center_of_mass',com.tolist(),'norm',float(np.linalg.norm(com)))
