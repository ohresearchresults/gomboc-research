# material-cc89f73f6535

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

#!/usr/bin/env python3
"""Exact original-polynomial H5 four-arrow chain certificate.
Run: python -B -S h5_energy_chain_certificate.py OUTPUT_DIRECTORY
Only Python standard-library arithmetic is used. No optimizer is used.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb, lcm, prod
from pathlib import Path
import hashlib, json, sys
NVAR=5
ZERO=(0,)*NVAR
DEGREES=(3,3,3,3,4)
BOUNDS=((F(15,16),F(1)),(F(1,4),F(1,2)),(F(1,2),F(13,20)),(F(1,5),F(3,10)),(F(0),F(1,64)))
ARROWS=((2,3),(3,4),(4,5),(8,2))
WEIGHTS=(3204,2267,1707,2822)
SHIFT_POWER=20
FACES=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),(9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))

def const(q):
 q=F(q);return {ZERO:q} if q else {}
def add(a,b):
 c=a.copy()
 for k,v in b.items():
  c[k]=c.get(k,F(0))+v
  if not c[k]:del c[k]
 return c
def scale(a,q):return {k:v*F(q) for k,v in a.items() if v*F(q)}
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
 c={}
 for k,v in a.items():
  for j,w in b.items():
   h=tuple(k[t]+j[t] for t in range(NVAR));c[h]=c.get(h,F(0))+v*w
 return {k:v for k,v in c.items() if v}
def power(a,n):
 b=const(1)
 for _ in range(n):b=mul(b,a)
 return b
def var(i):
 lo,hi=BOUNDS[i];e=list(ZERO);e[i]=1
 return add(const(lo),{tuple(e):hi-lo})
def total(ps):
 out={}
 for p in ps:out=add(out,p)
 return out
def dot(a,b):return total(mul(x,y) for x,y in zip(a,b))
def vsub(a,b):return tuple(sub(x,y) for x,y in zip(a,b))
def det(a,b,c):
 return total(mul(a[i],sub(mul(b[(i+1)%3],c[(i+2)%3]),mul(b[(i+2)%3],c[(i+1)%3]))) for i in range(3))

def geometry():
 x,r,p,q,ell=(var(i) for i in range(5));s=sub(const(1),ell);s2=power(s,2);s3=power(s,3)
 B=((const(F(1,4)),{}),(sub(const(1),scale(x,F(3,4))),{}),(sub(const(1),p),p),(q,sub(const(1),q)),({},sub(const(1),scale(r,F(3,4)))),({},const(F(1,4))),(const(F(1,16)),const(F(1,16))))
 z=[(mul(s,a),mul(s,b),{}) for a,b in B]+[({}, {},const(1)),(ell,{},const(1)),({},ell,const(1))]
 A=scale(sub(sub(const(31),scale(mul(x,p),24)),scale(mul(r,q),24)),F(1,64))
 Bx=total([const(F(509,3072)),scale(mul(x,p),F(-3,8)),scale(mul(power(x,2),p),F(3,32)),scale(mul(x,power(p,2)),F(1,8)),scale(mul(r,power(q,2)),F(-1,8))])
 By=total([const(F(509,3072)),scale(mul(r,q),F(-3,8)),scale(mul(power(r,2),q),F(3,32)),scale(mul(r,power(q,2)),F(1,8)),scale(mul(x,power(p,2)),F(-1,8))])
 V=add(scale(mul(A,s2),F(1,3)),scale(ell,F(1,6)))
 Jx=total([scale(mul(s3,Bx),F(1,4)),scale(mul(mul(s2,ell),sub(const(1),scale(mul(x,p),F(3,4)))),F(1,24)),scale(power(ell,2),F(1,24))])
 Jy=total([scale(mul(s3,By),F(1,4)),scale(mul(mul(s2,ell),sub(const(1),scale(mul(r,q),F(3,4)))),F(1,24)),scale(power(ell,2),F(1,24))])
 Jz=total([scale(mul(A,s2),F(1,12)),scale(ell,F(1,12)),scale(power(ell,2),F(1,24))])
 J=(Jx,Jy,Jz)
 vf={};jf=[{}, {}, {}]
 for f in FACES:
  for j in range(1,len(f)-1):
   a,b,c=(z[k] for k in (f[0],f[j],f[j+1]));t=det(a,b,c)
   vf=add(vf,scale(t,F(1,6)))
   for k in range(3):jf[k]=add(jf[k],scale(mul(t,total([a[k],b[k],c[k]])),F(1,24)))
 assert vf==V and tuple(jf)==J,'Actual oriented volume moments do not match.'
 return z,V,J

def bernstein_matrix(polys):
 indices=list(product(*(range(d+1) for d in DEGREES)));loc={k:i for i,k in enumerate(indices)}
 den=lcm(*(v.denominator for p in polys for v in p.values()))
 scales=[lcm(*(comb(d,a) for a in range(d+1))) for d in DEGREES]
 out=[]
 for p in polys:
  vals=[0]*len(indices)
  for k,v in p.items():
   assert all(k[i]<=DEGREES[i] for i in range(NVAR))
   vals[loc[k]]=int(v*den)
  for axis,d in enumerate(DEGREES):
   old=vals;vals=[0]*len(indices)
   for row,k in enumerate(indices):
    for a in range(k[axis]+1):
     j=list(k);j[axis]=a
     vals[row]+=old[loc[tuple(j)]]*comb(k[axis],a)*scales[axis]//comb(d,a)
  out.append(vals)
 return indices,den*prod(scales),out

def det3(a):
 return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])

def coverage():
 edges=sorted({tuple(sorted((a,b))) for f in FACES for a,b in zip(f,f[1:]+f[:1])})
 assert len(edges)==17
 unrooted=0;counts=[0]*10;basal_counts=[0]*10;trees=[]
 for es in combinations(edges,9):
  adj=[[] for _ in range(10)]
  for a,b in es:adj[a].append(b);adj[b].append(a)
  seen={0};stack=[0]
  for i in stack:
   for j in adj[i]:
    if j not in seen:seen.add(j);stack.append(j)
  if len(seen)!=10:continue
  unrooted+=1
  for root in range(10):
   par=[-1]*10;seen={root};stack=[root]
   for i in stack:
    for j in adj[i]:
     if j not in seen:seen.add(j);par[j]=i;stack.append(j)
   if all(par[i]==j for i,j in ARROWS):
    counts[root]+=1;trees.append(par)
    if root<7 and all(par[i]<7 for i in range(7) if i!=root):basal_counts[root]+=1
 assert unrooted==4879
 return counts,basal_counts,trees

def save(path,obj):
 raw=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode();path.write_bytes(raw)
 return {'filename':path.name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}

def main():
 if not __debug__:raise RuntimeError('Run with assertions; do not use -O.')
 out=Path(sys.argv[1] if len(sys.argv)>1 else 'h5-chain-output');out.mkdir(parents=True,exist_ok=True)
 z,V,J=geometry();print('H5_CHAIN_ACTUAL_FAN_MOMENTS_PASS 4')
 pairs=((0,0),(0,1),(0,2),(1,1),(1,2),(2,2));polys=[]
 for a,b in pairs:
  terms=[]
  for (i,j),w in zip(ARROWS,WEIGHTS):
   u=tuple(sub(mul(V,z[i][k]),J[k]) for k in range(3));d=vsub(z[j],z[i])
   terms.append(scale(add(mul(u[a],d[b]),mul(u[b],d[a])),F(-w,2)))
  polys.append(total(terms))
 indices,den,columns=bernstein_matrix(polys);blocks=[];minimum=[None]*3
 for k,ix in enumerate(indices):
  v=[c[k] for c in columns];a=[[v[0],v[1],v[2]],[v[1],v[3],v[4]],[v[2],v[4],v[5]]]
  shifted=[[(1<<SHIFT_POWER)*a[i][j]-(den*sum(WEIGHTS) if i==j else 0) for j in range(3)] for i in range(3)]
  minors=[shifted[0][0],shifted[0][0]*shifted[1][1]-shifted[0][1]**2,det3(shifted)]
  if not all(t>0 for t in minors):
   raise AssertionError(('Non-positive shifted minor',ix,minors))
  for i,t in enumerate(minors):minimum[i]=t if minimum[i] is None else min(minimum[i],t)
  blocks.append({'index':ix,'upper':v,'shifted_minors':minors})
 print('H5_CHAIN_ORIGINAL_BERNSTEIN_PD_PASS',len(blocks),3*len(blocks))
 counts,basal,trees=coverage();print('H5_CHAIN_ROOTED_SUPPORT_COVER_PASS',sum(counts),sum(basal))
 matrix_pin=save(out/'bernstein_matrices.json',{'degrees':DEGREES,'denominator':den,'shift_power':SHIFT_POWER,'weight_sum':sum(WEIGHTS),'blocks':blocks})
 report={'theorem':'H5_FOUR_ARROW_ENERGY_CHAIN_MACRO_BOX_V1','bounds':[[str(a),str(b)] for a,b in BOUNDS],'genuine_restrictions':'x<1; lambda>0. Other box coordinates already have genuine strict H5 bounds.','arrows':ARROWS,'weights':WEIGHTS,'matrix_count':len(blocks),'positive_shifted_minors':3*len(blocks),'minimum_integer_minors':minimum,'rootwise_cover':counts,'pure_basal_route_cover':basal,'covered_trees':trees,'weighted_arrow_mean_upper_bound':'-3*trace(M)/2^19 (strict, for nonzero PSD M)','matrix_file':matrix_pin}
 report_pin=save(out/'report.json',report)
 print('H5_CHAIN_CERTIFICATE_PASS')
 print(json.dumps({'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'source_bytes':len(Path(__file__).read_bytes()),'report':report_pin,'matrices':matrix_pin},sort_keys=True))
if __name__=='__main__':main()
