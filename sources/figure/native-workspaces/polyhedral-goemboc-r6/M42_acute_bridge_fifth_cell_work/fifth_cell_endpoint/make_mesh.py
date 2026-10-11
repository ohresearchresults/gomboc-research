#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction as Q
import csv,json,numpy as np
R=Path(__file__).resolve().parent;cycles=json.load(open(R/'face_cycles.json'));X={}
for r in csv.DictReader(open(R/'coordinates_active_centered.csv')):X[int(r['source_id'])]=np.array([float(Q(r[k])) for k in ('x_exact','y_exact','z_exact')])
ids=sorted(X);idx={i:k+1 for k,i in enumerate(ids)};tris=[]
for c in cycles:
 for j in range(1,len(c)-1):tris.append((c[0],c[j],c[j+1]))
with open(R/'body.obj','w') as f:
 f.write('# exact own-centred M42 acute-bridge fifth-cell endpoint; decimal rendering\n')
 for i in ids:f.write(f'# source_row {i} -> vertex {idx[i]}\n'+'v '+' '.join(f'{z:.17g}' for z in X[i])+'\n')
 for t in tris:f.write('f '+' '.join(str(idx[i]) for i in t)+'\n')
with open(R/'body.stl','w') as f:
 f.write('solid M42_acute_bridge_fifth_cell\n')
 for t in tris:
  a,b,c=(X[i] for i in t);n=np.cross(b-a,c-a);n=n/np.linalg.norm(n);f.write('  facet normal '+' '.join(f'{z:.17g}' for z in n)+'\n    outer loop\n')
  for i in t:f.write('      vertex '+' '.join(f'{z:.17g}' for z in X[i])+'\n')
  f.write('    endloop\n  endfacet\n')
 f.write('endsolid M42_acute_bridge_fifth_cell\n')
print('wrote',len(ids),'vertices',len(tris),'triangles')
