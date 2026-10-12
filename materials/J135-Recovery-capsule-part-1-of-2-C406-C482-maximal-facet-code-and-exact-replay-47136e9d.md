# material-47136e9d7939

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J135 Recovery capsule part 1 of 2 — C406/C482 nonwinners

This focused recovery closes the two actual inputs needed for finite planar-patch continuation. It is not the complete 19-unit FINITE_PATCH_RECOVERY_CAPSULE.md or the broader search archive. The full readable Library capsule was recovered and read through EOF; its 68299 bytes have SHA-256 be3b0f854697a2fc97159eaeebaefa0da37d97ea2c2bf51481db029700ab32d9. That Library filename/hash alone was not durable research state. This two-part source closure is durable only together with its explicit pre-existing engine dependency below.

Required sources: this part; Recovery capsule part 2 of 2 containing literal MERGE134_78A_RAW.json; and engine131.py (5318 bytes, SHA-256 57c193dfbdc155935de187e4c6b01f0115bd1dba1c65d89b383076abd0c7f63a) from already preserved [internal-source-reference], whole material SHA-256 5ef7761abe1e21f2c93a1c41c838f85e52e12d110f70fd059d649455de972859. All three materials must be supplied for a fresh computational successor. The part1 engine source has been read completely; no historical archive or sandbox is needed.

Write the fenced files literally, preserving trailing newlines. Run OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python REPLAY_PATCH135.py using CPython3.13.5, NumPy2.3.5, SciPy1.17.0. Do not use python -O. This reconstruction was executed in the coordinator runtime, matching both old output hashes. It is one Fraction implementation plus its maximal-facet extension, not independent engines or an independent verification of a worker's reasoning. Marker: J135_C406_C482_RECOVERY_PASS_NONWINNERS_ONLY.

COORD_PATCH78_203 is V78/E203/F127, C406, own211, weak000, primitive-zero000, P[], one Q about .23176595562232488. Its facets are 111 triangles,11 quadrilaterals,3 pentagons,1 hexagon,1 octagon. The 16 planar patches save25 true edges. COORD_PATCH_RELAY90_241 is V90/E241/F153, C482, own211, weak000, primitive-zero000, P[], one Q about .2317657494654277. Its facets are138 triangles,11 quadrilaterals,2 pentagons,1 hexagon,1 octagon. The twelve listed relays really cost38 edges, leaving8 to E249. Both newly integrated own centroids are used. Neither achieves110; canonical own110 remainsC622. The first78 points of the C482 source equal the C406 reconstruction exactly; this equality was checked in the runtime, allowing the smaller representation below.

## poly134.py
Bytes: 5167. SHA-256: 2692ed9a5ccdfe958361127af684b280b063edf0bed23cdcf51deafd8c28ef15.

```python
"""Exact maximal-polygon hull and homogeneous equilibrium audit.
Qhull nominates triangles only; exact supporting planes are deduplicated and
all coplanar input points are reduced to exact planar convex polygons. Every
true edge has two owners; Euler and connectedness are checked. No triangle
fan diagonal is counted as an edge or used in either persistence graph.
"""
from engine131 import *
from math import gcd,lcm

def primitive(values):
 D=lcm(*(v.denominator for v in values));a=[int(v*D)for v in values];g=gcd(*a);assert g
 return tuple(v//g for v in a)

def planar_cycle(X,ids,n):
 drop=max(range(3),key=lambda i:abs(n[i]));axes=[j for j in range(3)if j!=drop];order=sorted(ids,key=lambda i:(X[i][axes[0]],X[i][axes[1]],i))
 def turn(i,j,k):
  a,b=axes;return (X[j][a]-X[i][a])*(X[k][b]-X[i][b])-(X[j][b]-X[i][b])*(X[k][a]-X[i][a])
 lo=[];hi=[]
 for i in order:
  while len(lo)>=2 and turn(lo[-2],lo[-1],i)<=0:lo.pop()
  lo.append(i)
 for i in reversed(order):
  while len(hi)>=2 and turn(hi[-2],hi[-1],i)<=0:hi.pop()
  hi.append(i)
 out=lo[:-1]+hi[:-1];assert len(out)>=3
 if dot(n,cross(sub(X[out[1]],X[out[0]]),sub(X[out[2]],X[out[0]])))<0:out.reverse()
 k=out.index(min(out));return tuple(out[k:]+out[:k])

def hull(X):
 ch=ConvexHull(np.array([[float(t)for t in p]for p in X]));planes={}
 for tt in ch.simplices:
  a,b,c=[X[int(i)]for i in tt];n=cross(sub(b,a),sub(c,a));assert dot(n,n)>0;h=dot(n,a);sg=[dot(n,p)-h for p in X]
  if max(sg)>0:
   assert min(sg)>=0,'Nominated plane is not exactly supporting';n=mul(F(-1),n);h=-h;sg=[-t for t in sg]
  assert max(sg)==0 and min(sg)<0
  key=primitive(tuple(n)+(h,));planes[key]=[i for i,s in enumerate(sg)if s==0]
 entries=[]
 for p,ids in planes.items():
  n=tuple(F(t)for t in p[:3]);h=F(p[3]);t=planar_cycle(X,ids,n);entries.append((t,(n,h)))
 entries.sort();fs=[t for t,nh in entries];hs=[nh for t,nh in entries];es={}
 for fi,t in enumerate(fs):
  n,h=hs[fi];assert all(dot(n,X[i])==h for i in t)
  assert all(dot(n,cross(sub(X[t[(j+1)%len(t)]],X[t[j]]),sub(X[t[(j+2)%len(t)]],X[t[(j+1)%len(t)]])))>0 for j in range(len(t)))
  for j in range(len(t)):es.setdefault(tuple(sorted((t[j],t[(j+1)%len(t)]))),[]).append(fi)
 assert all(len(v)==2 for v in es.values()),'Incomplete maximal boundary'
 es=dict(sorted(es.items()));vs=sorted({i for t in fs for i in t});assert len(vs)-len(es)+len(fs)==2
 seen={0};todo=[0]
 while todo:
  i=todo.pop();t=fs[i]
  for k in range(len(t)):
   for j in es[tuple(sorted((t[k],t[(k+1)%len(t)])))]:
    if j not in seen:seen.add(j);todo.append(j)
 assert len(seen)==len(fs)
 return fs,hs,es,vs

def mass(X,fs):
 tri=[(f[0],f[i],f[i+1])for f in fs for i in range(1,len(f)-1)]
 V=O;M=(O,O,O)
 for a,b,c in tri:
  d=det(X[a],X[b],X[c]);V+=d/6;M=add(M,mul(d/24,add(add(X[a],X[b]),X[c])))
 assert V>0;return V,M,mul(1/V,M)

def audit(X):
 fs,hs,es,vs=hull(X);V,M,g=mass(X,fs);Y=[sub(x,g)for x in X];S=[];U=[];H=[];weak=[[],[],[]];zero=[0,0,0]
 for fi,(t,(n,h))in enumerate(zip(fs,hs)):
  assert h-dot(n,g)>0
  sig=[dot(n,cross(Y[t[j]],Y[t[(j+1)%len(t)]]))for j in range(len(t))];zero[0]+=sum(s==0 for s in sig)
  if min(sig)>0:S.append(fi)
  elif min(sig)>=0:weak[0].append(fi)
 nb=[[]for _ in X]
 for a,b in es:nb[a].append(b);nb[b].append(a)
 for i in vs:
  sig=[dot(Y[i],sub(Y[j],Y[i]))for j in nb[i]];zero[1]+=sum(s==0 for s in sig)
  if max(sig)<0:U.append(i)
  elif max(sig)<=0:weak[1].append(i)
 for (a,b),(i,j)in es.items():
  d=sub(Y[b],Y[a]);dd=dot(d,d);aa=-dot(Y[a],d);bb=dd-aa;p=add(Y[a],mul(aa/dd,d));n1,n2=hs[i][0],hs[j][0]
  g11,g12,g22=dot(n1,n1),dot(n1,n2),dot(n2,n2);D=g11*g22-g12*g12;assert D>0
  c1=dot(p,n1)*g22-dot(p,n2)*g12;c2=dot(p,n2)*g11-dot(p,n1)*g12
  assert mul(D,p)==add(mul(c1,n1),mul(c2,n2));sig=[aa,bb,c1,c2];zero[2]+=sum(s==0 for s in sig)
  if min(sig)>0:H.append((a,b))
  elif min(sig)>=0:weak[2].append((a,b))
 assert len(S)+len(U)-len(H)==2
 P=persistence(Y,es);Q=persistence([mul(1/(h-dot(n,g)),n)for n,h in hs],es.values());assert len(P)==len(U)-1 and len(Q)==len(S)-1
 return dict(V=len(vs),E=len(es),F=len(fs),strict=[len(S),len(U),len(H)],weak=list(map(len,weak)),primitive_zero=zero,S=[fs[i]for i in S],S_indices=S,U=U,H=H,P=P,Q=Q,volume=V,moment=M,centroid=g,face_histogram={str(k):sum(len(f)==k for f in fs)for k in sorted(set(map(len,fs)))},degrees={str(k):sum(len(nb[i])==k for i in vs)for k in sorted(set(len(nb[i])for i in vs))}),fs

if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--tag',required=True);a=p.parse_args();X=[tuple(F(t)for t in row)for row in json.load(open(a.input))];out,fs=audit(X);V,M,g=mass([sub(x,out['centroid'])for x in X],fs);assert V==out['volume'] and M==(O,O,O)
 b=(json.dumps(serial(dict(name=a.tag,points=X,faces=fs,audit=out,centred_mass_check=True)),sort_keys=True,separators=(',',':'))+'\n').encode();(R/(a.tag+'_EXACT.json')).write_bytes(b)
 print('MAXIMAL_EXACT',a.tag,[out[k]for k in('V','E','F')],out['strict'],out['weak'],out['primitive_zero'],'P',[float(z['depth'])for z in out['P']],'Q',[float(z['depth'])for z in out['Q']],out['face_histogram'],'BYTES',len(b),'SHA',hashlib.sha256(b).hexdigest(),flush=True)
```

## REPLAY_PATCH135.py

```python
"""Recover C406 and C482 using the literal planar-patch input and 12 relays.
Requires engine131.py from the preserved J131 part1, and poly134.py.
All output hashes identify exact bytes, not an independent verification.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
import engine131 as e
import poly134 as p
R=Path(__file__).resolve().parent
raw_bytes=(R/'MERGE134_78A_RAW.json').read_bytes()
assert len(raw_bytes)==8814
assert hashlib.sha256(raw_bytes).hexdigest()=='76b8528a90f408072151fb5e0af0dd7b89336f6cc0579527d0160e0b98875c26'
raw=json.loads(raw_bytes);N=raw['N'];K=len(raw['patches']);C=[]
for k,patch in enumerate(raw['patches']):
 for i in patch['vertices']:
  row=[F(0)]*(3*N+K);row[3*i:3*i+3]=map(F,patch['normal']);row[3*N+k]=-F(raw['normal_scale']);C.append(row)
rr,piv=e.rref(C);free=[i for i in range(3*N+K)if i not in piv]
assert free==raw['free_indices'] and len(free)==len(raw['free_values'])
z=e.lift_free(rr,piv,free,list(map(F,raw['free_values'])))
assert all(e.dot(row,z)==0 for row in C)
X=[tuple(z[3*i:3*i+3])for i in range(N)]
relays=[
['250725239961/1000000000000','-43409421599/1000000000000','338951008191/500000000000'],
['129278737909/200000000000','-16998997/781250000','171811716473/500000000000'],
['15631997581/25000000000','-21158541791/1000000000000','378860490231/1000000000000'],
['332760724731/500000000000','-20992378263/1000000000000','38419304887/125000000000'],
['301126933419/500000000000','-18983022567/1000000000000','412942374631/1000000000000'],
['682600720231/1000000000000','-952954163/50000000000','270162699259/1000000000000'],
['697577260141/1000000000000','-16143967723/1000000000000','232146780017/1000000000000'],
['36079901501/62500000000','-16369520527/1000000000000','222903685919/500000000000'],
['355201217963/500000000000','-12414170959/1000000000000','193398139241/1000000000000'],
['735626208637/1000000000000','-3528449557/1000000000000','14387184957/200000000000'],
['369693605057/500000000000','406632419/250000000000','7587012971/250000000000'],
['740704276253/1000000000000','7692910891/1000000000000','-5716431173/500000000000']]
Y=X+[tuple(map(F,row))for row in relays]
by=json.dumps(e.serial(Y)).encode()
assert len(by)==12543 and hashlib.sha256(by).hexdigest()=='b53bc9abfbf36355620dd6bb45ad6fbc4d1825f3f3d2f574ce50997fadf19479'
for name,pts,size,sha in [
 ('COORD_PATCH78_203',X,37951,'3b65b4c8d0e9958afeed18bc52d76327511aaa39c3baaa1680b47052ca9bc12b'),
 ('COORD_PATCH_RELAY90_241',Y,39243,'e5e9fcb58d4e022c5f25d41a25361ee781adf9c013d605cef6b9a53ada2d2395')]:
 out,fs=p.audit(pts);V,M,g=p.mass([e.sub(x,out['centroid'])for x in pts],fs)
 assert V==out['volume'] and M==(F(0),)*3
 assert out['strict']==[2,1,1] and out['weak']==[0,0,0] and not out['P'] and len(out['Q'])==1
 b=(json.dumps(e.serial(dict(name=name,points=pts,faces=fs,audit=out,centred_mass_check=True)),sort_keys=True,separators=(',',':'))+'\n').encode()
 assert len(b)==size and hashlib.sha256(b).hexdigest()==sha
 (R/(name+'_EXACT.json')).write_bytes(b)
 print(name,out['V'],out['E'],out['F'],out['strict'],float(out['Q'][0]['depth']),len(b),sha,flush=True)
print('J135_C406_C482_RECOVERY_PASS_NONWINNERS_ONLY')
```
