# material-ef03f8f4792e

AI research material

---

"""C622 finite exact simple-vertex ear controls. Not a global C lower bound.
Input A.json is reconstructed from the two canonical scoped16 source capsules.
No floating-point computation is used. Run: python -S exact_ears.py A.json chunk.json BEGIN END
Then: python -S exact_ears.py merge out.json CHUNK_FILES
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from math import lcm
from collections import Counter
import json,sys,time
sys.set_int_max_str_digits(0)
assert __debug__

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [enc(v) for v in x]
 return x
B=lambda x:json.dumps(enc(x),sort_keys=True,separators=(',',':')).encode()

def build(source,out,begin=0,end=133):
 data=Path(source).read_bytes();assert sha256(data).hexdigest()=='142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0'
 r=json.loads(data);X=[tuple(map(F,p)) for p in r['raw_vertices']];faces=r['faces'];nv=len(X)
 V0=F(r['ordinary_volume']);mom=tuple(map(F,r['raw_first_moments']));g0=tuple(map(F,r['raw_centroid']))
 adj=[set() for _ in X]
 for i,j in r['edges']:adj[i].add(j);adj[j].add(i)
 # Pre-clear vertex and edge denominators. Only the actual mass numerator changes.
 den=[lcm(*(t.denominator for t in p)) for p in X];A=[tuple(int(t*d) for t in p) for p,d in zip(X,den)]
 E={}
 def edged(i,j):
  if (i,j) not in E:E[i,j]=tuple(den[i]*a-den[j]*b for a,b in zip(A[j],A[i]))
  return E[i,j]
 results=[];witness_sha=sha256();start=time.time()
 simple=[v for v in range(nv) if len(adj[v])==3]
 for v in simple[begin:end]:
  witness_sha=sha256()
  cy=sorted(adj[v]);a,b,c=[X[i] for i in cy];N=cross(sub(b,a),sub(c,a))
  if dot(N,sub(X[v],a))<0:cy.reverse();a,b,c=[X[i] for i in cy];N=cross(sub(b,a),sub(c,a))
  h=dot(N,a);assert dot(N,X[v])>h
  # Strict separation from every other vertex certifies the actual single ear.
  assert all(dot(N,x)<h for i,x in enumerate(X) if i!=v and i not in cy)
  ear=det(sub(a,X[v]),sub(b,X[v]),sub(c,X[v]));ear=abs(ear)/6
  assert 0<ear<V0
  earcentre=tuple(sum(X[i][k] for i in [v,*cy])/4 for k in range(3))
  vol=V0-ear;moment=tuple(mom[k]-ear*earcentre[k] for k in range(3));g=tuple(t/vol for t in moment)
  CD=lcm(*(t.denominator for t in g));CG=tuple(int(t*CD) for t in g)
  Z=[tuple(CD*a-d*t for a,t in zip(p,CG)) for p,d in zip(A,den)]
  nfaces=[[i for i in f if i!=v] for f in faces if v not in f or len(f)>3]+[cy]
  edges={tuple(sorted((i,j))) for f in nfaces for i,j in zip(f,f[1:]+f[:1])}
  nadj=[set() for _ in X]
  for i,j in edges:nadj[i].add(j);nadj[j].add(i)
  assert len(edges)==len(r['edges'])-sum(v in f and len(f)==3 for f in faces)
  assert nv-1-len(edges)+len(nfaces)==2 and not nadj[v]
  U=[];radii={};usedprimitives=0
  for i in range(nv):
   if i==v:continue
   ds=[]
   for j in sorted(nadj[i]):
    e=edged(i,j);d=dot(Z[i],e);ds.append(d)
   if max(ds)<0:
    U.append(i);rr=[]
    for j,d in zip(sorted(nadj[i]),ds):
     e=edged(i,j)
     # For symmetric perturbations max|M_ab-I_ab|<=epsilon,
     # exact absolute support on the six independent entries.
     coeff=[Z[i][k]*e[k] for k in range(3)]
     coeff += [Z[i][k]*e[l]+Z[i][l]*e[k] for k in range(3) for l in range(k+1,3)]
     D=-d; BB=sum(abs(s) for s in coeff)
     kk=max(0,BB.bit_length()-D.bit_length()+1)
     while (D<<kk)<=BB:kk+=1
     rr.append(kk)
    radii[i]=max(rr)
  assert len(U)>=2,(v,U)
  pair=sorted(U,key=lambda i:(radii[i],i))[:2];k=max(radii[i] for i in pair)
  # A strict dyadic lower bound gives strictness throughout a closed box.
  eps=F(1,2**k)
  # Full all-other-vertex check is independent of the adjacency sufficiency theorem.
  for i in pair:
   for j in range(nv):
    if j in (i,v):continue
    e=edged(i,j);d=dot(Z[i],e)
    assert d<0,(v,i,j)
   for j in sorted(nadj[i]):
    e=edged(i,j);d=dot(Z[i],e)
    coeff=[Z[i][k]*e[k] for k in range(3)]+[Z[i][k]*e[l]+Z[i][l]*e[k] for k in range(3) for l in range(k+1,3)]
    assert (d<<k)+sum(abs(s) for s in coeff)<0
    witness_sha.update(B([v,i,j,d,coeff]));usedprimitives+=1
  record=dict(delete=v,VEF=[nv-1,len(edges),len(nfaces)],triangles=sum(v in f and len(f)==3 for f in faces),U_all=U,selected_U=pair,metric_closed_box_dyadic_power=k,strict_adjacency_primitive_count=usedprimitives,ear_volume_sha256=sha256(B(ear)).hexdigest(),centroid_sha256=sha256(B(g)).hexdigest(),centroid_denominator_bits=CD.bit_length(),strict_witness_sha256=witness_sha.hexdigest())
  results.append(record)
  if len(results)%20==0:print('EXACT_EARS',len(results),'elapsed',round(time.time()-start,2),flush=True)
 report=dict(object='CANONICAL_C622_ALL133_SIMPLE_DELETION_U2_AND_LOCAL_METRIC_BOX_V1',parent_A_sha256=sha256(data).hexdigest(),degree_counts=Counter(map(len,adj)),facet_size_counts=Counter(map(len,faces)),simple_triangle_counts=Counter(q['triangles'] for q in results),count=len(results),rows=results,strict_witness_stream_sha256=witness_sha.hexdigest())
 assert len(results)==min(end,133)-begin
 report['range']=[begin,min(end,133)]
 Path(out).write_bytes(B(report));print('CANONICAL_C622_EXACT_SIMPLE_DELETION_RANGE_PASS',len(B(report)),sha256(B(report)).hexdigest(),flush=True)

def merge(paths,out):
 reports=[json.loads(Path(p).read_bytes()) for p in paths];reports.sort(key=lambda r:r['range'])
 pos=0;rows=[]
 for r in reports:
  assert r['range'][0]==pos;pos=r['range'][1];rows+=r['rows']
 assert pos==133 and len(rows)==133 and len({r['delete'] for r in rows})==133
 assert Counter(r['triangles'] for r in rows)=={0:94,1:16,2:23}
 q=reports[0].copy();q.pop('range');q.pop('strict_witness_stream_sha256');q['count']=133;q['rows']=rows;q['simple_triangle_counts']=Counter(r['triangles'] for r in rows)
 q['maximum_metric_closed_box_dyadic_power']=max(r['metric_closed_box_dyadic_power'] for r in rows)
 q['minimum_strict_U_count']=min(len(r['U_all']) for r in rows);q['maximum_strict_U_count']=max(len(r['U_all']) for r in rows)
 assert q['maximum_metric_closed_box_dyadic_power']==22
 assert q['minimum_strict_U_count']==20 and q['maximum_strict_U_count']==87
 assert all(94 in r['selected_U'] for r in rows)
 Path(out).write_bytes(B(q));print('CANONICAL_C622_ALL133_SIMPLE_DELETIONS_STRICT_U2_METRIC_BOX_PASS',len(B(q)),sha256(B(q)).hexdigest())
if __name__=='__main__':
 if sys.argv[1]=='merge':merge(sys.argv[3:],sys.argv[2])
 else:
  assert len(sys.argv)==5
  build(sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]))
