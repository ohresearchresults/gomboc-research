"""Freeze a finite actual-hull nomination; exact supporting-plane grouping.
SciPy proposes triangles only. Every accepted plane and complete contact set
is tested with Fraction. The emitted VF complex is then certified independently
of SciPy's proposal tolerance by the complete GMP maximal-facet auditor.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import reduce
import math,json,sys
import numpy as np
from scipy.spatial import ConvexHull
ROOT=Path(__file__).resolve().parent
sys.set_int_max_str_digits(0)
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def plane(a,b,c):
 n=cross(sub(b,a),sub(c,a));h=dot(n,a)
 if h<0:n=tuple(-v for v in n);h=-h
 if h==0:return None
 row=(*n,h);d=math.lcm(*(t.denominator for t in row));z=[int(t*d) for t in row];gg=reduce(math.gcd,z);return tuple(t//gg for t in z)
def freeze(src,digits,name):
 inp=json.loads(Path(src).read_text());base=json.loads((ROOT/'J90_DETACHED_C390_G8_AUDIT.json').read_text());x=[tuple(map(F,p)) for p in base['vertices']];g=np.array(inp['frame_shift']);D=10**digits
 ap=[tuple(F(round(F(float(v))*D),D) for v in row) for row in (np.array(inp['apexes'])+g)]
 x+=ap;xf=np.array([[float(a) for a in p] for p in x]);hull=ConvexHull(xf);planes={};rejected=[]
 for t in hull.simplices:
  row=plane(*(x[k] for k in t))
  if row is None:continue
  sl=[row[3]-dot(row[:3],p) for p in x]
  if min(sl)<0:rejected.append([t.tolist(),float(min(sl))]);continue
  planes[row]=[i for i,s in enumerate(sl) if s==0]
 faces=[]
 for row,cy in sorted(planes.items()):
  n=np.array(row[:3],float);n/=np.linalg.norm(n);c=xf[cy].mean(0);p=xf[cy]-c;u=p[0]/np.linalg.norm(p[0]);v=np.cross(n,u);ang=np.arctan2(p@v,p@u);cy=[cy[k] for k in np.argsort(ang)]
  if dot(row[:3],cross(sub(x[cy[1]],x[cy[0]]),sub(x[cy[2]],x[cy[0]])))<0:cy.reverse()
  faces.append(cy)
 es={}
 for cy in faces:
  for a,b in zip(cy,cy[1:]+cy[:1]):e=tuple(sorted((a,b)));es[e]=es.get(e,0)+1
 print('PROPOSED_EXACT',name,'VEF',len(x),len(es),len(faces),'rejected',rejected,'edgecounts',sorted(set(es.values())),flush=True)
 assert all(v==2 for v in es.values()) and len(x)-len(es)+len(faces)==2
 out=dict(name=name,base='J90_DETACHED_C390_G8',grid=D,rounding='ties-to-even of each exact binary64 raw apex times 10**digits',apexes=[list(map(str,p)) for p in ap],faces=faces,source=Path(src).name)
 (ROOT/(name+'_INPUT.json')).write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
 with (ROOT/(name+'_VF.txt')).open('w') as f:
  f.write(f'{len(x)} {len(faces)}\n')
  for p in x:f.write(' '.join(map(str,p))+'\n')
  for cy in faces:f.write(' '.join(map(str,[len(cy),*cy]))+'\n')
 print('J91_LITERAL_VF_FROZEN_NOT_YET_AUDITED',name,flush=True)
if __name__=='__main__':freeze(sys.argv[1],int(sys.argv[2]),sys.argv[3])
