"""Bind both exact primal-star constructions to their audited convex bodies."""
import json,sys
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
source,proof=map(Path,sys.argv[1:]);sys.path.insert(0,str(source.resolve()))
import exact57,rational56

def mass(P,faces):
 D=F(0);L=[F(0)]*3
 for cy in faces:
  for k in range(1,len(cy)-1):
   a,b,c=[P[i] for i in [cy[0],cy[k],cy[k+1]]]
   dd=exact57.dot(a,exact57.cross(b,c));assert dd>0
   D+=dd;L=[x+dd*(i+j+k) for x,i,j,k in zip(L,a,b,c)]
 return D/6,[x/24 for x in L]

d,fs=exact57.source();P=exact57.physical(rational56.points(d)[:137],fs);V,M=mass(P,fs)
for name,v,side,lost in [('STAR7',7,1,5),('STAR111',111,0,107)]:
 a=json.loads((proof/('final_'+name)/'A.json').read_bytes())
 b=json.loads((proof/('final_'+name)/'B.json').read_bytes());assert a==b
 raw,r=exact57.star(d,fs,v,side);PP=[p[:] for p in P]
 PP[v]=[x+F(r['t'])*F(y) for x,y in zip(P[v],r['direction'])]
 want={tuple(p) for i,p in enumerate(PP) if i!=lost}
 assert {tuple(map(F,p)) for p in a['raw_vertices']}==want
 for p in PP:assert all(exact57.dot(row[:3],p)<=row[3] for row in raw['H'])
 assert F(a['ordinary_volume'])==V
 assert [F(x)-y for x,y in zip(a['raw_first_moments'],M)]==list(map(F,r['first_moment_change']))
 print('EXACT_HULL_EQUALS_PRIMAL_STAR_AND_VOLUME_MOMENT_IDENTITY_PASS',name,flush=True)
