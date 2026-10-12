"""Rational bicap nomination reconstruction and exhaustive exact hull audit."""
from pathlib import Path
from itertools import combinations
from math import gcd
from fractions import Fraction
import sys,json,time,hashlib,numpy as np
sys.set_int_max_str_digits(0)
from bicap_search import coords,ROOT
sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'));import check_B
from gmpy2 import mpq
check_B.Q=mpq

def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def blob(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()

def audit(theta,b,t,out,D=10**12):
 start=time.time();q=np.load(theta);X=coords(q,b,t);out.mkdir(parents=True,exist_ok=False);h=int(round(np.exp(q[-3])*D));u,v=[int(round(w*D)) for w in q[-2:]];P=[]
 for i,(x,y,z) in enumerate(X):
  xx=int(round(x*D));yy=int(round(y*D));zz=0 if i<b else h*D+u*xx+v*yy if i<b+t else int(round(z*D))*D;P.append((xx*D,yy*D,zz))
 # Exact common-grid points preserve both designated cap planes.
 N=len(P);s=tuple(sum(p[j] for p in P) for j in range(3));Pts=[tuple(N*p[j]-s[j] for j in range(3)) for p in P];den=N*D*D
 co={'source_theta':str(theta),'grid':D,'cap_integer_H_u_v':[h,u,v],'bottom_count':b,'top_count':t,'common_grid_denominator':D*D,'original_integer_points':P,'translation_sum':s,'translated_denominator':den,'translated_integer_points':Pts};(out/'coordinates.json').write_bytes(blob(co));planes=set()
 for ia,ib,ic in combinations(range(N),3):
  a,bb,c=Pts[ia],Pts[ib],Pts[ic];nn=cross(sub(bb,a),sub(c,a))
  if nn==(0,0,0):continue
  hh=dot(nn,a);pos=neg=False
  for p in Pts:
   w=dot(nn,p)-hh;pos|=w>0;neg|=w<0
   if pos and neg:break
  if pos and neg:continue
  if pos:nn=tuple(-w for w in nn);hh=-hh
  if hh<=0:raise ValueError('average point not strict interior')
  row=tuple(den*w for w in nn)+(hh,);div=gcd(*row);planes.add(tuple(w//div for w in row))
 H={'H':sorted(planes)};(out/'H.json').write_bytes(blob(H));print('EXACT_PLANES',len(planes),time.time()-start,flush=True);r=check_B.run(H)
 Pin={tuple(mpq(v,den) for v in p) for p in Pts};Pout={tuple(mpq(v) for v in p) for p in r['raw_vertices']};assert Pout<=Pin;assert all(dot(h[:3],p)<=h[3]*den for h in H['H'] for p in Pts)
 (out/'audit.json').write_bytes(blob(r));summary={k:r[k] for k in ['V','E','F','counts','weak','stable_face_ids','unstable_vertices','saddle_edges','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};summary.update(C=2*r['E'],seconds=time.time()-start,goal_candidate=r['counts']==[1,1,0] and r['weak']==[0,0,0] and 34<=2*r['E']<500);summary['sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.iterdir() if p.is_file()};(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print('EXACT',summary,flush=True)
 return r
if __name__=='__main__':
 source=ROOT/sys.argv[1];meta=json.loads((source/'construction.json').read_text());theta=source/sys.argv[2];out=source/sys.argv[3];audit(theta,meta['bottom'],meta['top'],out)
