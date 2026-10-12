#!/usr/bin/env python3
from pathlib import Path
import csv,json,math,sys
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
from numeric_hull_proposer import evaluate,score_target
D=10**12
rows={};line={}
with open(ROOT/'input_rows_lattice.csv') as f:
 for r in csv.DictReader(f):
  i=int(r['source_id']);rows[i]=(int(r['x_int']),int(r['y_int']),int(r['z_int']));line[i]=r['lineage']
def sub(a,b):return tuple(a[k]-b[k] for k in range(3))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(a[k]*b[k] for k in range(3))
# choose far-separated base points to make Nz robust: 0,5,11
p0,p1,p2=(rows[i] for i in (0,5,11))
n=cross(sub(p1,p0),sub(p2,p0));h=dot(n,p0)
assert n[2]!=0
sg=1 if n[2]>0 else -1;K=abs(n[2]);S=D*K
out={};corr={}
for i,p in rows.items():
 if i<17:
  zrat_num=(h-n[0]*p[0]-n[1]*p[1])*sg # integer-coordinate z times K
  out[i]=(p[0]*K,p[1]*K,zrat_num)
  corr[i]=zrat_num/K-p[2]
 else:out[i]=tuple(z*K for z in p)
P={i:np.array([z/S for z in p]) for i,p in out.items()}
r=evaluate(P,plane_tol=1e-9,strict_tol=1e-10)
assert r.valid,r.error
print('plane n/h',n,h,'K digits',len(str(K)),'S digits',len(str(S)))
print('base correction integer-unit max',max(abs(v) for v in corr.values()),corr)
print('AUDIT',len(out),len(r.active),len(r.edges),len(r.faces),(len(r.stable),len(r.unstable),len(r.saddles)),r.centroid,r.volume)
print('stable',[(r.faces[i]['cycle'],d) for i,d in r.stable]);print('unstable',r.unstable);print('saddles',r.saddles);print('score',score_target(r))
with open(ROOT/'input_rows_common_lattice.csv','w',newline='') as f:
 w=csv.writer(f);w.writerow(['source_id','x_int','y_int','z_int','denominator','lineage'])
 for i in sorted(out):w.writerow([i,*out[i],S,line[i]])
json.dump({'version':3,'source':'common-lattice exactification of robust lobe candidate; rows 0..16 projected to exact plane through rounded rows 0,5,11','base_plane_integer_coordinate_normal':list(n),'base_plane_integer_coordinate_h':h,'original_rounding_denominator':D,'common_denominator':S,'base_z_corrections_in_original_1e-12_units':{str(i):corr[i] for i in corr}},open(ROOT/'common_lattice_projection.json','w'),indent=2)
