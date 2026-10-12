"""Exactly close the homogeneous centroid by three tangential apex moves.
Base and cap data are unchanged literal J90 recovery inputs. No optimization.
This emits the corrected rational vertices/faces and correction certificate;
full convexity, equilibrium and mass checks are performed by vfaudit90.cpp.
"""
import sys,json
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,s):return tuple(x*s for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
b=json.loads(Path('J90_DETACHED_C390_G8_AUDIT.json').read_text()); cap=json.loads(Path('J90_BALANCED_C452_G14_CAPS.json').read_text());x=[tuple(map(F,r)) for r in b['vertices']];g=tuple(map(F,b['centroid']));ap={int(k):tuple(map(F,r)) for k,r in cap['apexes'].items()};cycles=dict(zip(b['active_input_planes'],b['faces']))
def moments(ap):
 vs={};mom=(F(0),)*3
 for fi,w in ap.items():
  cy=cycles[fi];v=F(0)
  for j in range(1,len(cy)-1):
   a,c,d=[x[k] for k in [cy[0],cy[j],cy[j+1]]];dv=-det(sub(a,w),sub(c,w),sub(d,w))/6;assert dv>0;v+=dv;mom=add(mom,mul(add(add(sub(a,g),sub(c,g)),add(sub(d,g),sub(w,g))),dv/4))
  vs[fi]=v
 return vs,mom
vs,R=moments(ap)
lines=Path('J90_DETACHED_C390_G8.txt').read_text().splitlines();m,D=map(int,lines[0].split());n=[tuple(map(int,s.split())) for s in lines[1:]]
a,c,d=n[6],n[14],n[16];ts=[(0,a[2],-a[1]),(0,c[2],-c[1]),(-d[2],0,d[0])];ids=[6,14,16];cols=[mul(t,vs[i]/4) for t,i in zip(ts,ids)];den=det(*cols);assert den
rhs=mul(R,-1);ss=[det(rhs,cols[1],cols[2])/den,det(cols[0],rhs,cols[2])/den,det(cols[0],cols[1],rhs)/den];changed=ap.copy();steps=[]
for fi,t,s in zip(ids,ts,ss):
 shift=mul(t,s);assert dot(n[fi],shift)==0;changed[fi]=add(ap[fi],shift);steps.append(dict(input_plane=fi,shift=list(map(str,shift)),shift_approx=list(map(float,shift))))
newvs,newR=moments(changed);assert newvs==vs and newR==(F(0),)*3
faces=[]
for fi,cy in zip(b['active_input_planes'],b['faces']):
 if fi not in changed:faces.append(cy);continue
 k=len(x);x.append(changed[fi]);faces.extend([[a,c,k] for a,c in zip(cy,cy[1:]+cy[:1])])
name='J90_EXACT_CENTER_C452'
out={'name':name,'base':'J90_DETACHED_C390_G8','apexes':{i:list(map(str,p)) for i,p in changed.items()},'shifts':steps,'added_volume':str(sum(vs.values())),'moment_residual':list(map(str,newR)),'target_centroid':list(map(str,g)),'expected_volume':str(F(b['volume'])+sum(vs.values()))}
Path(name+'_CORRECTION.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
with Path(name+'_VF.txt').open('w') as f:
 f.write(f'{len(x)} {len(faces)}\n')
 for p in x:f.write(' '.join(map(str,p))+'\n')
 for cy in faces:f.write(' '.join(map(str,[len(cy),*cy]))+'\n')
print('J90_RATIONAL_MOMENT_CLOSURE_EXACT',[(v['input_plane'],v['shift_approx']) for v in steps],flush=True)
