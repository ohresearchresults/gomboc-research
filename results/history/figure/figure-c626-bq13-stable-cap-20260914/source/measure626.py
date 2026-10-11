"""Exact bit costs, true-complex comparison, full rooted exits, and changed mass."""
import sys,json,hashlib,collections
from fractions import Fraction as F
from math import lcm
from pathlib import Path
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(s,a):return tuple(s*x for x in a)
def bits(x):return max(abs(x.numerator).bit_length(),x.denominator.bit_length())
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def floor(x):return x.numerator//x.denominator

def run(a,raw,parent=None):
 P=[tuple(map(F,p)) for p in a['raw_vertices']];g=tuple(map(F,a['raw_centroid']));M=tuple(map(F,a['raw_first_moments']));W=F(a['ordinary_volume']);Z=[sub(p,g) for p in P]
 assert all(M[i]==W*g[i] for i in range(3))
 adj=[set() for p in P];owners=[set() for p in P];eowners={};dual=[set() for f in a['faces']]
 for f,cy in enumerate(a['faces']):
  for i in cy:owners[i].add(f)
  for i,j in zip(cy,cy[1:]+cy[:1]):eowners.setdefault(tuple(sorted((i,j))),[]).append(f)
 for (i,j),(s,t) in eowners.items():adj[i].add(j);adj[j].add(i);dual[s].add(t);dual[t].add(s)
 out=dict(V=len(P),E=len(eowners),F=len(a['faces']),C=2*len(eowners),counts=a['counts'],weak=a['weak'],stable=a['stable_face_ids'],unstable=a['unstable_vertices'],saddles=a['saddle_edges'],primitive_zero_counts=[a[k] for k in ['face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']],plane_bits=max(abs(v).bit_length() for r in raw['H'] for v in r),raw_coordinate_bits=max(bits(v) for p in P for v in p),centroid_bits=max(map(bits,g)),centred_coordinate_bits=max(bits(v) for p in Z for v in p),volume_bits=bits(W),first_moment_bits=max(map(bits,M)),volume_decimal=float(W),first_moments_decimal=list(map(float,M)),centroid_decimal=list(map(float,g)),centred_first_moments=[0,0,0],centred_common_denominator_bits=lcm(*(v.denominator for p in Z for v in p)).bit_length(),face_sizes=dict(sorted(collections.Counter(map(len,a['faces'])).items())),vertex_degrees=dict(sorted(collections.Counter(map(len,adj)).items())),integration_triangles=a['integration_triangle_count'],face_side_tests=sum(map(len,a['face_signs'])),ordered_vertex_tests=len(P)*(len(P)-1),edge_primitive_count=a['edge_primitive_count'])
 if a['counts']==[1,1,0] and a['weak']==[0,0,0]:
  C=lcm(*(v.denominator for v in g));G=tuple(int(v*C) for v in g);b=[lcm(*(v.denominator for v in p)) for p in P];aa=[tuple(int(v*d) for v in p) for p,d in zip(P,b)];zz=[sub(mul(C,v),mul(d,G)) for v,d in zip(aa,b)]
  def edge(i,j):return sub(mul(b[i],aa[j]),mul(b[j],aa[i]))
  def ex(i,j):return dot(zz[i],edge(i,j))
  def rel(i,j):return (ex(i,j)*C,b[j]*dot(zz[i],zz[i]))
  def eta_floor(i,j):return 10**9*ex(i,j)*b[j]//(C*dot(edge(i,j),edge(i,j)))
  def forest(ad,root,ex,rel):
   pa=[];bounds=[]
   for i,nb in enumerate(ad):
    if i==root:assert all(ex(i,j)<0 for j in nb);pa.append(-1);continue
    pos=[j for j in sorted(nb) if ex(i,j)>0];assert pos,('no exit',i)
    j=pos[0];r=rel(i,j)
    for k in pos[1:]:
     t=rel(i,k)
     if t[0]*r[1]>=r[0]*t[1]:j=k;r=t
    pa.append(j);bounds.append(10**12*r[0]//r[1])
   ds=[]
   for i in range(len(ad)):
    seen=set();j=i
    while j!=root:assert j>=0 and j not in seen;seen.add(j);j=pa[j]
    ds.append(len(seen))
   return dict(root=root,parents=pa,depths=ds,maxdepth=max(ds),floor_1e12_min_relative=min(bounds))
  out['primal_forest']=forest(adj,a['unstable_vertices'][0],ex,rel)
  N=[tuple(raw['H'][i][:3]) for i in a['active_input_indices']];D=[raw['H'][i][3] for i in a['active_input_indices']];d=[C*h-dot(n,G) for n,h in zip(N,D)];assert min(d)>0
  def de(i,j):return d[i]*dot(N[i],N[j])-d[j]*dot(N[i],N[i])
  def dr(i,j):return (de(i,j),d[j]*dot(N[i],N[i]))
  out['dual_forest']=forest(dual,a['stable_face_ids'][0],de,dr)
  chain=[next(i for i,o in enumerate(owners) if o==set(need)) for need in ([57,71,134],[71,134,135],[71,135,136],[17,71,136])];assert all(j in adj[i] and ex(i,j)>0 for i,j in zip(chain,chain[1:]))
  out['chain']=[dict(edge=[i,j],owners=[sorted(owners[i]),sorted(owners[j])],floor_1e9_eta=eta_floor(i,j)) for i,j in zip(chain,chain[1:])]
 return out
if __name__=='__main__':
 p=Path(sys.argv[1]);parent=json.loads(Path(sys.argv[2]).read_text()) if len(sys.argv)>2 else None
 s=run(json.loads((p/'A.json').read_text()),json.loads((p/'raw.json').read_text()),parent);(p/'STATS.json').write_bytes(canon(s));print(json.dumps({k:v for k,v in s.items() if k not in ('primal_forest','dual_forest')},indent=2));print('ROOTS',[(k,{kk:vv for kk,vv in s[k].items() if kk not in ('parents','depths')}) for k in ('primal_forest','dual_forest') if k in s])
