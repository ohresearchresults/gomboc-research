"""Second exact proof: quadratic extremization for perfect-mass two-cap slides.
No Bernstein producer is imported. All weak-U intervals form a complete cover.
"""
import json,sys,itertools
from pathlib import Path
from fractions import Fraction as Q
import BUILD,FROZEN_STARS
CAPS={99:BUILD.CASES['PAIR99']['caps'],117:BUILD.CASES['TRIPLE117']['caps'],84:BUILD.CASES['PAIR99']['caps']}
def maxquad(co,lo,hi):
 a,b,c=co
 def ev(t):return a+b*t+c*t*t
 values=[ev(lo),ev(hi)]
 if c<0:
  x=-b/(2*c)
  if lo<x<hi:values.append(ev(x))
 return max(values)
def verify(base,deleted,families):
 P=[tuple(map(Q,p)) for p in base['raw_vertices']];g=tuple(map(Q,base['raw_centroid']));moving={i for cap in CAPS[deleted] for i in cap['vertices']};faces=base['faces'];raw={'H':[list(n)+[h] for n,h in zip(base['normals'],base['offsets'])]};apex=next(i for i,p in enumerate(P) if p==(0,0,1));certificate,_=FROZEN_STARS.certify(P,faces,raw,g,moving,[apex]);adj=[set() for p in P]
 for i,j in base['edges']:adj[i].add(j);adj[j].add(i)
 for f in families:
  u,w=f['u'],f['w'];assert u!=apex and len(adj[u])==3 and w in adj[u];a,b=sorted(adj[u]-{w});e=BUILD.sub(P[w],P[u]);local=[set(v) for v in adj];local[a].add(b);local[b].add(a)
  partition=sorted((Q(l,1<<d),Q(l+1,1<<d),v) for l,d,v in f['tiles']);last=Q(0)
  for lo,hi,i in partition:
   assert lo==last and i!=apex;last=hi
   assert all(not set(cy)&moving for cy in faces if i in cy)
   assert not local[i]&moving
   vi=e if i==u else (Q(0),)*3;z=BUILD.sub(P[i],g)
   for j in local[i]:
    vj=e if j==u else (Q(0),)*3;d=BUILD.sub(P[j],P[i]);dv=BUILD.sub(vj,vi)
    co=[BUILD.dot(z,d),BUILD.dot(z,dv)+BUILD.dot(vi,d),BUILD.dot(vi,dv)]
    assert maxquad(co,lo,hi)<=0,(deleted,u,w,i,j)
  assert last==1
 return dict(status='INDEPENDENT_QUADRATIC_PERFECT_CENTROID_CAP_COVER_PASS',deleted_support=deleted,families=families,apex_certificate=certificate,scope='0<s<1 with the planned true local stars, compatible supporting geometry, both cap boundaries fixed, and ACTUAL filled-volume centroid c0. Arbitrary cap parameters and shape are allowed subject to the retained supporting constraints. At least two weak unstable vertices; no strict110/weak000.')
if __name__=='__main__':
 p,j,covers,out=sys.argv[1:];j=int(j);r=verify(json.loads(Path(p).read_text()),j,json.loads(Path(covers).read_text())[str(j)]);Path(out).write_text(json.dumps(r,sort_keys=True,separators=(',',':')));print(r['status'],j,flush=True)
