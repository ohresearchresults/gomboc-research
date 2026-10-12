# material-e73c8dc04724

AI research material

---

"""Exact finite canonical-C622 single-ear obstruction, stdlib only.
Run a range: python -B -S exact_ears.py A.json EARS_0.json 0 30
Merge five completed ranges: python -B -S exact_ears.py merge EXACT_EARS.json EARS_0.json EARS_30.json EARS_60.json EARS_90.json EARS_120.json
A.json is reconstructed and verified by the complete canonical scoped16 capsule.
"""
from fractions import Fraction as F
from pathlib import Path
from math import lcm
from collections import Counter
import hashlib,json,sys,time
sys.set_int_max_str_digits(0)
assert __debug__
PIN='142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0'
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def introw(v):
 d=lcm(*(x.denominator for x in v));return tuple(x.numerator*(d//x.denominator) for x in v),d
def digest(x):return hashlib.sha256(json.dumps(x,separators=(',',':'),sort_keys=True).encode()).hexdigest()
def main(apath,out,begin=0,end=133):
 raw=Path(apath).read_bytes();assert hashlib.sha256(raw).hexdigest()==PIN
 A=json.loads(raw);X=[tuple(map(F,r)) for r in A['raw_vertices']];faces=A['faces'];nv=len(X)
 assert nv==176 and len(A['edges'])==311 and len(faces)==137
 V0=F(A['volume']);g0=tuple(map(F,A['raw_centroid']));J0=tuple(map(F,A['raw_first_moment']))
 IR=[introw(x) for x in X];adj=[set() for _ in X]
 for i,j in A['edges']:adj[i].add(j);adj[j].add(i)
 simple=[v for v in range(nv) if len(adj[v])==3]
 records=[]; witness=hashlib.sha256()
 for v in simple[begin:end]:
  abc=sorted(adj[v]);a,b,c=(X[i] for i in abc);N=cross(sub(b,a),sub(c,a));h=dot(N,a)
  if dot(N,X[v])<h:N=tuple(-z for z in N);h=-h;abc.reverse();a,b,c=(X[i] for i in abc)
  assert dot(N,X[v])>h and all(dot(N,X[i])<h for i in range(nv) if i not in abc and i!=v)
  # Degree three gives a genuine tetrahedral ear. No old remaining vertex is
  # coplanar with its new triangular support, so that new triangle is maximal.
  ear=dot(sub(a,X[v]),cross(sub(b,X[v]),sub(c,X[v])))/6
  ear=abs(ear);assert 0<ear<V0
  ce=tuple((X[v][k]+a[k]+b[k]+c[k])/4 for k in range(3))
  Vol=V0-ear;J=tuple(J0[k]-ear*ce[k] for k in range(3));g=tuple(z/Vol for z in J)
  G,D=introw(g);Z=[tuple(D*r[k]-d*G[k] for k in range(3)) for r,d in IR]
  fs=[[i for i in cy if i!=v] for cy in faces if v not in cy or len(cy)>3]+[abc]
  es=sorted(set(tuple(sorted((i,j))) for cy in fs for i,j in zip(cy,cy[1:]+cy[:1])))
  assert len(X)-1-len(es)+len(fs)==2
  adj1=[set() for _ in X]
  for i,j in es:adj1[i].add(j);adj1[j].add(i)
  assert not adj1[v] and all(len(adj1[i])>=3 for i in range(nv) if i!=v)
  U=[];robust=[]
  for i in range(nv):
   if i==v:continue
   ri,di=IR[i];kreq=0
   for j in sorted(adj1[i]):
    rj,dj=IR[j];e=tuple(di*rj[k]-dj*ri[k] for k in range(3));d=dot(Z[i],e)
    if d>=0:break
    coeff=[Z[i][k]*e[k] for k in range(3)]+[Z[i][k]*e[l]+Z[i][l]*e[k] for k,l in ((0,1),(0,2),(1,2))]
    B=sum(abs(q) for q in coeff);neg=-d
    # A strict dyadic lower bound for neg/B, obtained by integer comparisons.
    kk=max(0,B.bit_length()-neg.bit_length()+1)
    while (neg<<kk)<=B:kk+=1
    kreq=max(kreq,kk)
   else:U.append(i);robust.append((kreq,i))
  assert len(U)>=2
  robust.sort();pair=[z[1] for z in robust[:2]];k=max(robust[0][0],robust[1][0]);eps=F(1,2**k)
  witness=hashlib.sha256();guards=0
  for i in pair:
   ri,di=IR[i]
   # The global support version is also checked, independent of adjacency.
   assert all(dot(Z[i],tuple(di*IR[j][0][l]-IR[j][1]*ri[l] for l in range(3)))<0 for j in range(nv) if j not in (i,v))
   for j in sorted(adj1[i]):
    rj,dj=IR[j];e=tuple(di*rj[l]-dj*ri[l] for l in range(3));d=dot(Z[i],e)
    coeff=[Z[i][l]*e[l] for l in range(3)]+[Z[i][l]*e[m]+Z[i][m]*e[l] for l,m in ((0,1),(0,2),(1,2))]
    assert (d<<k)+sum(abs(q) for q in coeff)<0
    witness.update((str(i)+','+str(j)+':'+','.join(map(str,[d]+coeff))+'\n').encode());guards+=1
  t=sum(v in cy and len(cy)==3 for cy in faces)
  assert len(es)==311-t
  records.append(dict(delete=v,triangles=t,VEF=[175,len(es),len(fs)],U_all=U,selected_U=pair,metric_closed_box_dyadic_power=k,
   centroid_sha256=digest(list(map(str,g))),ear_volume_sha256=digest(str(ear)),centroid_denominator_bits=D.bit_length(),strict_adjacency_primitive_count=guards,strict_witness_sha256=witness.hexdigest()))
 report=dict(object='CANONICAL_C622_ALL133_SIMPLE_DELETION_U2_AND_LOCAL_METRIC_BOX_V1',parent_A_sha256=PIN,count=len(records),range=[begin,end],
  simple_triangle_counts=dict(sorted(Counter(r['triangles'] for r in records).items())),
  degree_counts=dict(sorted(Counter(map(len,adj)).items())),facet_size_counts=dict(sorted(Counter(map(len,faces)).items())),
  minimum_strict_U_count=min(len(r['U_all']) for r in records),maximum_strict_U_count=max(len(r['U_all']) for r in records),
  maximum_metric_closed_box_dyadic_power=max(r['metric_closed_box_dyadic_power'] for r in records),rows=records,strict_witness_stream_sha256=witness.hexdigest())
 b=(json.dumps(report,sort_keys=True,separators=(',',':'))+'\n').encode();Path(out).write_bytes(b)
 print('CANONICAL_C622_EXACT_SIMPLE_DELETION_RANGE_PASS',len(b),hashlib.sha256(b).hexdigest())
if __name__=='__main__':
 if sys.argv[1]=='merge':
  reports=[json.loads(Path(p).read_bytes()) for p in sys.argv[3:]];rows=[r for q in reports for r in q['rows']]
  assert sum(len(q['rows']) for q in reports)==133 and len({r['delete'] for r in rows})==133
  t=dict(sorted(Counter(r['triangles'] for r in rows).items()));assert t=={0:94,1:16,2:23}
  out={k:reports[0][k] for k in ('object','parent_A_sha256','degree_counts','facet_size_counts')};out.update(count=133,simple_triangle_counts=t,rows=rows,
    minimum_strict_U_count=min(len(r['U_all']) for r in rows),maximum_strict_U_count=max(len(r['U_all']) for r in rows),
    maximum_metric_closed_box_dyadic_power=max(r['metric_closed_box_dyadic_power'] for r in rows))
  assert out['maximum_metric_closed_box_dyadic_power']==22
  assert out['minimum_strict_U_count']==20 and out['maximum_strict_U_count']==87
  assert all(94 in r['selected_U'] for r in rows)
  b=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode();Path(sys.argv[2]).write_bytes(b)
  print('CANONICAL_C622_ALL133_SIMPLE_DELETIONS_STRICT_U2_METRIC_BOX_PASS',len(b),hashlib.sha256(b).hexdigest())
 else:main(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 0,int(sys.argv[4]) if len(sys.argv)>4 else 133)
