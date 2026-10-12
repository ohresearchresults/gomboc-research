"""Independent direct matrix reconstruction and actual-volume controls.
Standard library only. Neither numerical locator nor root0 generator is imported.
The fixtures check identities, not mechanical feasibility of escape trees.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction as F
import sys,json,hashlib,collections
sys.path.insert(0,'nova54_recovery')
import comb,exact_check as C
FS=tuple(tuple(map(int,s))for s in '014 021 032 043 125 154 235 347 365 376 458 487 568 678'.split())
M=[[5,1,2],[1,4,1],[2,1,6]]

def sub(a,b):return [u-v for u,v in zip(a,b)]
def cross(a,b):return [a[(i+1)%3]*b[(i+2)%3]-a[(i+2)%3]*b[(i+1)%3]for i in range(3)]
def dot(a,b):return sum(u*v for u,v in zip(a,b))
def det(a,b,c):return dot(a,cross(b,c))
def volume(V,t):
 a,b,c,d=[V[i]for i in t];return det(sub(b,a),sub(c,a),sub(d,a))

def fixture(cofacial):
 V=[[5,2,-6],[5,5,-6],[2,5,-6],[0,0,0],[12,0,0],[0,12,0],[2,5,6],[5,2,6],[5,5,6]]
 if cofacial==1:
  V=[[4*x for x in v]for v in V];V[0]=[11,-1,-33]
 elif cofacial==2:V[3][2]=-6
 groups={};normals={}
 for j,t in enumerate(FS):
  n=cross(sub(V[t[1]],V[t[0]]),sub(V[t[2]],V[t[0]]));assert n!=[0,0,0]
  val=[dot(n,sub(v,V[t[0]]))for v in V];assert max(val)==0 and min(val)<0
  f=tuple(i for i,v in enumerate(val)if v==0);groups.setdefault(f,[]).append(j);normals[f]=n
 allfacets=set()
 for t in combinations(range(9),3):
  n=cross(sub(V[t[1]],V[t[0]]),sub(V[t[2]],V[t[0]]))
  if n==[0,0,0]:continue
  val=[dot(n,sub(v,V[t[0]]))for v in V]
  if min(val)<0<max(val):continue
  allfacets.add(tuple(i for i,v in enumerate(val)if v==0))
 assert allfacets==set(groups)
 for i in range(9):assert any(det(*ns)!=0 for ns in combinations([normals[f]for f in groups if i in f],3))
 trueedges=set();cycles=[]
 for f,js in sorted(groups.items()):
  e=collections.Counter((a,t[(k+1)%3])for j in js for t in[FS[j]]for k,a in enumerate(t))
  border=[(a,b)for a,b in e if e[a,b]>e[b,a]]
  assert len(border)==len(f)and all(e[a,b]-e[b,a]==1 for a,b in border)
  outgoing=dict(border);assert len(outgoing)==len(f)
  t=[min(f)]
  while outgoing[t[-1]]!=t[0]:
   t.append(outgoing[t[-1]]);assert len(t)<=len(f)
  assert set(t)==set(f)
  for a,b in border:
   assert all(dot(cross(sub(V[b],V[a]),sub(V[c],V[a])),normals[f])>0 for c in f if c not in(a,b))
   trueedges.add(tuple(sorted((a,b))))
  cycles.append(t)
 all_edges={tuple(sorted((t[k],t[(k+1)%3])))for t in FS for k in range(3)}
 assert trueedges==all_edges-({(2,3)}if cofacial==1 else {(0,2)}if cofacial==2 else set())
 fans=[[tuple(sorted((a,)+t))for t in FS if a not in t]for a in range(9)]
 cells=sorted({t for ff in fans for t in ff});assert len(cells)==63
 d={t:abs(volume(V,t))for t in cells}
 assert [t for t in cells if not d[t]]==([(0,2,3,5)]if cofacial==1 else [(0,1,2,3)]if cofacial==2 else [])
 assert all(volume(V,(a,)+t)>=0 for a in range(9)for t in FS if a not in t)
 D=sum(d[t]for t in fans[0]);B=[sum(d[t]*sum(V[i][a]for i in t)for t in fans[0])for a in range(3)]
 Y=[[4*D*V[i][a]-B[a]for a in range(3)]for i in range(9)]
 s={t:[sum(Y[i][a]for i in t)for a in range(3)]for t in cells}
 J={t:[[s[t][a]*s[t][b]+sum(Y[i][a]*Y[i][b]for i in t)for b in range(3)]for a in range(3)]for t in cells}
 moments=[]
 for ff in fans:
  assert sum(d[t]for t in ff)==D and all(sum(d[t]*s[t][a]for t in ff)==0 for a in range(3))
  moments.append([[sum(d[t]*J[t][a][b]for t in ff)for b in range(3)]for a in range(3)])
 assert all(Q==moments[0]for Q in moments)and det(*M)==97 and M[0][0]*M[1][1]-M[0][1]**2==19
 G=[[sum(Y[i][a]*M[a][b]*Y[j][b]for a in range(3)for b in range(3))for j in range(9)]for i in range(9)]
 out=dict(cofacial=cofacial,raw_vertices=V,actual_maximal_facets=cycles,true_edges=sorted(trueedges),
  triangles_to_maximal_facets=[next(j for j,f in enumerate(cycles)if set(t)<=set(f))for t in FS],
  six_volume=D,actual_centroid=[str(F(b,4*D))for b in B],centered_coordinate_multiplier=4*D,
  metric=M,flat_cells=[t for t in cells if not d[t]],actual_six_masses=[d[t]for t in cells],
  uniform_second_tensor_numerator=moments[0])
 return dict(d=d,Y=Y,G=G,s=s,J=J,out=out)

def direct(rec):
 p=rec['parent'];z=rec['z'];kind=rec['kind'];spec=rec['fans'];A=len(spec)
 ff=[[tuple(sorted((a,)+t))for t in FS if a not in t]for a,_ in spec]
 shared=kind!='ordinary';volume=kind in('volume','cycle');cyc=kind=='cycle'
 if shared:
  cells=sorted({t for f in ff for t in f});fi=[[int(t in f)for t in cells]for f in ff];inst=[(None,t)for t in cells]
  if cyc:fi=[fi[0]]+rec['relations'];A=len(fi)
 else:inst=[(a,t)for a,f in enumerate(ff)for t in f]
 nr=len(rec['relations'])if volume else A-1;start=9*A;end=start+8*len(inst)
 assert len(z)==end+45*nr+(A-1 if shared else 0)and min(z[start:end])>=0
 K=[]
 for b in range(nr):
  Q=[[0]*9 for _ in range(9)];at=end+45*b
  for i in range(9):
   for j in range(i,9):Q[i][j]=Q[j][i]=z[at]*(2 if i==j else 1);at+=1
  K.append(Q)
 for u,(a,t)in enumerate(inst):
  chi=[int(i in t)for i in range(9)]
  g=[sum(fi[b][u]*z[9*b+i]for b in range(A))for i in range(9)]if shared else z[9*a:9*a+9]
  hs=[b[u]for b in rec['relations']]if volume else [fi[b][u]-fi[-1][u]for b in range(A-1)]if shared else [int(a==b)-int(a==A-1)for b in range(A-1)]
  eta=z[end+45*nr:]
  q=sum(eta[b]*rec['relations'][b][u]for b in range(nr))if cyc else sum(eta[b]*(fi[b][u]-fi[-1][u])for b in range(A-1))if shared else 0
  Q=[[g[i]*chi[j]+g[j]*chi[i]+sum(h*W[i][j]for h,W in zip(hs,K))+2*q*(chi[i]*chi[j]+int(i==j)*chi[i])for j in range(9)]for i in range(9)]
  ls=z[start+8*u:start+8*(u+1)]
  for i,v in zip(range(1,9),ls):Q[i][i]+=2*v;Q[i][p[i]]-=v;Q[p[i]][i]-=v
  yield t,Q,ls

def main():
 fixtures=[fixture(i)for i in range(3)];rows=json.loads(Path('root0_certificates.json').read_bytes())
 report=json.loads(Path('root0_report.json').read_bytes());assert len(rows)==134
 stream=hashlib.sha256();nm=0;physical=hashlib.sha256();relations_seen=set()
 for r in rows:
  rec=r['record'];assert rec['root']==0 and rec['parent']==r['parent']
  h=hashlib.sha256();sides=[[0,0]for _ in fixtures];blocks=list(C.scalar_matrices(rec,FS));ds=list(direct(rec));assert len(blocks)==len(ds)==r['matrices']
  for (t,Q,ls),q in zip(ds,blocks):
   assert Q==q;bb=C.bareiss(Q);assert bb==C.ldl(Q);h.update(comb.encoded([Q,bb]));nm+=1
   for f,sums in zip(fixtures,sides):
    mass=f['d'][t];G=f['G'];p=rec['parent']
    sums[0]+=mass*sum(Q[i][j]*G[i][j]for i in range(9)for j in range(9))
    sums[1]+=mass*sum(2*v*(G[i][i]-G[i][p[i]])for i,v in zip(range(1,9),ls))
  assert all(a==b and a>0 for a,b in sides)
  physical.update(comb.encoded([r['index'],sides]));assert h.hexdigest()==r['scalar_sha']
  stream.update(comb.encoded([r['index'],len(ds),h.hexdigest()]))
  if 'relations'in rec:
   spec=rec['fans'];cells=sorted({tuple(sorted((a,)+t))for a,_ in spec for t in FS if a not in t})
   key=tuple(tuple(b)for b in rec['relations'])
   if key in relations_seen:continue
   relations_seen.add(key)
   for beta in rec['relations']:
    for f in fixtures:
     assert sum(v*f['d'][t]for t,v in zip(cells,beta))==0
     assert all(sum(v*f['d'][t]*f['s'][t][a]for t,v in zip(cells,beta))==0 for a in range(3))
     assert all(sum(v*f['d'][t]*f['J'][t][a][b]for t,v in zip(cells,beta))==0 for a in range(3)for b in range(3))
 assert nm==report['root0_matrices']and stream.hexdigest()==report['scalar_stream_sha256']
 out=dict(identity='NOVA54_ROOT0_INDEPENDENT_MATRIX_AND_PHYSICAL_MASS_AUDIT_V1',records=134,matrices=nm,
  scalar_stream_sha256=stream.hexdigest(),physical_identity_stream_sha256=physical.hexdigest(),fixtures=[f['out']for f in fixtures])
 raw=comb.encoded(out);Path('physical0_report.json').write_bytes(raw)
 print('ROOT0_INDEPENDENT_DIRECT_MATRIX_RECONSTRUCTION_PASS',134,nm,flush=True)
 print('ROOT0_ACTUAL_DETERMINANT_ALL_FAN_AND_FULL_CYCLE_TENSOR_IDENTITIES_PASS',flush=True)
 print('ROOT0_GENUINE_COFACIAL_0235_ZERO_CELL_TRUE_EDGE_23_REMOVED_PASS',flush=True)
 print('ROOT0_GENUINE_COFACIAL_0123_ZERO_GAUGE_TRUE_EDGE_02_REMOVED_PASS',flush=True)
 print('PHYSICAL0_REPORT',*comb.pin(raw),flush=True)

if __name__=='__main__':main()
