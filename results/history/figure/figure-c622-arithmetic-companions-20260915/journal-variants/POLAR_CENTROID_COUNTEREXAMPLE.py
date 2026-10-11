"""Exact filled-volume centroid counterexample to centroid-preserving polarity."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib,json,sys
assert __debug__,'Assertions must be enabled'
assert len(sys.argv)==2,'Usage: POLAR_CENTROID_COUNTEREXAMPLE.py NEW_REPORT.json'
T=[(F(-2),F(-8,9)),(F(2),F(-8,9)),(F(1),F(10,9)),(F(-1),F(10,9))]
Q=[(F(0),F(-9,8)),(F(9,14),F(9,28)),(F(0),F(9,10)),(F(-9,14),F(9,28))]
def cross(u,v):return u[0]*v[1]-u[1]*v[0]
def sub(u,v):return tuple(a-b for a,b in zip(u,v))
def dot(u,v):return sum(a*b for a,b in zip(u,v))
def polygon(P):
 n=len(P)
 assert all(cross(sub(P[(i+1)%n],P[i]),sub(P[j],P[i]))>0 for i in range(n) for j in range(n) if j not in (i,(i+1)%n))
 assert all(cross(P[i],P[(i+1)%n])>0 for i in range(n))
 d=[cross(P[i],P[(i+1)%n]) for i in range(n)];A=sum(d)/2
 M=tuple(sum((P[i][j]+P[(i+1)%n][j])*d[i] for i in range(n))/6 for j in range(2))
 return A,M,tuple(x/A for x in M)
# All intersections of pairs of polar support lines; no omitted polar vertex.
verts=set()
for a,b in combinations(T,2):
 d=cross(a,b)
 if not d:continue
 q=((b[1]-a[1])/d,(a[0]-b[0])/d)
 if all(dot(t,q)<=1 for t in T):verts.add(q)
assert verts==set(Q)
A,M,c=polygon(T);B,N,d=polygon(Q)
assert (A,c)==(F(6),(F(0),F(0)))
assert (B,d)==(F(729,560),(F(0),F(9,280)))
# K=T x [-1,1]. Its polar has sections (1-|z|) Q at height z.
# Integrating their area and first moments gives 2B/3 and N/2.
VK=2*A;MK=(2*M[0],2*M[1],F(0));VP=2*B/3;MP=(N[0]/2,N[1]/2,F(0))
cK=tuple(x/VK for x in MK);cP=tuple(x/VP for x in MP)
assert VK==12 and cK==(0,0,0)
assert VP==F(243,280) and MP==(F(0),F(6561,313600),F(0))
assert cP==(F(0),F(27,1120),F(0)) and cP!=cK
report=dict(identity='FILLED_CENTROID_POLARITY_COUNTEREXAMPLE',T=T,polar_T=Q,K_volume=VK,K_first_moments=MK,K_centroid=cK,polar_volume=VP,polar_first_moments=MP,polar_centroid=cP,scope='Polarity need not preserve own uniform filled-volume centering; not a Gomboc or a refutation of a vertex/facet lower bound.')
b=json.dumps(report,sort_keys=True,separators=(',',':'),default=str).encode()
p=Path(sys.argv[1]);assert not p.exists();p.write_bytes(b)
print('FILLED_CENTROID_POLARITY_COUNTEREXAMPLE_EXACT_PASS',hashlib.sha256(b).hexdigest())
