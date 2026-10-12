"""Freeze a floating extra-contact construction using an EXACT retained anchor.
The anchor is the Cramer vertex of three literal rows of the exact baseline.
Every selected contact row is put on that exact rational plane, not a tolerance.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import sys,json,math,numpy as np
from fractions import Fraction as F
from pathlib import Path
from anchor_engine import geom,data

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
p=json.loads(Path(sys.argv[1]).read_text());base=json.loads(Path(sys.argv[2]).read_text());ids=list(map(int,sys.argv[4:7]));a,b,c=[base['I'][j] for j in ids];bc=cross(b,c);ca=cross(c,a);ab=cross(a,b);det=dot(a,bc);A=[F(base['D']*(bc[j]+ca[j]+ab[j]),det) for j in range(3)];L=math.lcm(*(x.denominator for x in A));P=[int(x*L) for x in A];g=math.gcd(L,math.gcd(*P));L//=g;P=[x//g for x in P]
out=Path(sys.argv[3]);out.mkdir(exist_ok=True,parents=True);q=np.array([[float.fromhex(t) for t in row] for row in p['q_hex']]);labels=p['original_rows'];rows=p['anchor']['rows'];root=labels.index(3);anchor={'point':np.array([float(x) for x in A]),'rows':rows}
print('EXACT_ANCHOR',P,L,'rows',rows,flush=True)
(out/'ANCHOR.json').write_text(json.dumps(dict(numerators=P,denominator=L,rows=rows,baseline_vertex_contact_rows=ids,original_rows=labels)))
for k in range(5,10):
 M=10**k;Q=[[F(round(float(x)*M),M) for x in row] for row in q]
 for i in range(len(q)):
  if q[i,2]==1:Q[i][2]=F(1)
 for i in rows:
  axis=max(range(2 if q[i,2]==1 else 3),key=lambda j:abs(P[j]));Q[i][axis]=(L-sum(P[j]*Q[i][j] for j in range(3) if j!=axis))/P[axis]
  assert sum(P[j]*Q[i][j] for j in range(3))==L
 D=math.lcm(*(x.denominator for row in Q for x in row));I=[[int(x*D) for x in row] for row in Q];z=np.array([[float(x) for x in row] for row in Q]);G=geom(z,anchor=anchor);cc=[len(G[t]) for t in ('S','U','H')];v=[G[t] for t in ('V','E','F')];f=float(data(G,root)[0].min());print(k,v,cc,f,'Ddigits',len(str(D)),flush=True)
 if cc==[1,1,0] and f>0:
  # Preserve convention that sole stable row is 3, remapping the contact witness.
  order=list(range(len(I)));order[3],order[root]=order[root],order[3]
  (out/f'RAW_FREE_D{M}.json').write_text(json.dumps(dict(D=D,I=[I[j] for j in order],scale=1),sort_keys=True,separators=(',',':')))
