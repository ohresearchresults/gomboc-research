"""Exact arithmetic complexity and complete primal/dual rooted escape witnesses."""
import sys,json,hashlib,collections
from pathlib import Path
from fractions import Fraction as F
from math import lcm
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,k):return tuple(x*k for x in a)
def bits(v):return max(abs(v.numerator).bit_length(),v.denominator.bit_length())
def canonical(v):return json.dumps(v,sort_keys=True,separators=(',',':')).encode()
def run(a,raw):
 P=[tuple(map(F,p)) for p in a['raw_vertices']];g=tuple(map(F,a['raw_centroid']));W=F(a['ordinary_volume']);M=tuple(map(F,a['raw_first_moments']));N=[tuple(r[:3]) for r in raw['H']];D=[r[3] for r in raw['H']]
 assert all(M[j]==W*g[j] for j in range(3))
 C=lcm(*(x.denominator for x in g));gi=tuple(int(C*x) for x in g);bs=[lcm(*(x.denominator for x in p)) for p in P];aa=[tuple(int(b*x) for x in p) for b,p in zip(bs,P)];zz=[sub(mul(p,C),mul(gi,b)) for p,b in zip(aa,bs)]
 adjacency=[set() for _ in P];owner=[set() for _ in P];dual=[set() for _ in N];edgeowners={}
 for f,cy in enumerate(a['faces']):
  for i in cy:owner[i].add(f)
  for i,j in zip(cy,cy[1:]+cy[:1]):edgeowners.setdefault(tuple(sorted((i,j))),[]).append(f)
 for (i,j),fs in edgeowners.items():
  assert len(fs)==2;adjacency[i].add(j);adjacency[j].add(i);u,v=fs;dual[u].add(v);dual[v].add(u)
 def ed(i,j):return sub(mul(aa[j],bs[i]),mul(aa[i],bs[j]))
 def exit(i,j):return dot(zz[i],ed(i,j))
 def relative(i,j):return F(exit(i,j)*C,bs[j]*dot(zz[i],zz[i]))
 def eta(i,j):return F(exit(i,j)*bs[j],C*dot(ed(i,j),ed(i,j)))
 def forest(adj,root,positive,relative):
  parent=[];bounds=[]
  for i in range(len(adj)):
   if i==root:
    assert all(positive(i,j)<0 for j in adj[i]);parent.append(-1);continue
   candidates=[j for j in sorted(adj[i]) if positive(i,j)>0];assert candidates,('no exit',i)
   j=max(candidates,key=lambda j:(relative(i,j),j));parent.append(j);bounds.append(relative(i,j))
  depths=[]
  for i in range(len(adj)):
   seen=set();j=i
   while j!=root:
    assert j not in seen;seen.add(j);j=parent[j];assert j>=0
   depths.append(len(seen))
  mi=min(bounds)
  return {'root':root,'parents':parent,'depths':depths,'max_depth':max(depths),'floor_1e12_min_selected_relative_exit':int(mi*10**12)}
 pf=forest(adjacency,a['unstable_vertices'][0],exit,relative)
 delta=[C*d-dot(n,gi) for n,d in zip(N,D)];assert min(delta)>0
 def pexit(i,j):return delta[i]*dot(N[i],N[j])-delta[j]*dot(N[i],N[i])
 def prel(i,j):return F(pexit(i,j),delta[j]*dot(N[i],N[i]))
 df=forest(dual,a['stable_face_ids'][0],pexit,prel)
 keys=[{57,71,134},{71,134,135},{71,135,136,137},{17,71,137}]
 chain=[next(i for i,o in enumerate(owner) if o==key) for key in keys]
 ce=[]
 for i,j in zip(chain,chain[1:]):
  assert j in adjacency[i] and exit(i,j)>0
  ce.append({'edge':[i,j],'eta_decimal':float(eta(i,j)),'floor_1e9_eta':int(10**9*eta(i,j)),'floor_1e12_relative_exit':int(10**12*relative(i,j))})
 path=[chain[0]]+chain[1:]
 while path[-1]!=pf['root']:path.append(pf['parents'][path[-1]])
 assert len(path)==len(set(path))
 stats={'name':'BQ13_C632_THREE_LINK_OWN110','V':len(P),'E':len(edgeowners),'F':len(N),'C_2E':2*len(edgeowners),'counts':a['counts'],'weak':a['weak'],'stable_face_ids':a['stable_face_ids'],'stable_face_cycle':a['faces'][3],'unstable_vertices':a['unstable_vertices'],'apex_degree':len(adjacency[98]),'face_size_histogram':dict(sorted(collections.Counter(map(len,a['faces'])).items())),'vertex_degree_histogram':dict(sorted(collections.Counter(map(len,adjacency)).items())),'integration_triangles':a['integration_triangle_count'],'plane_integer_max_bits':max(abs(x).bit_length() for r in raw['H'] for x in r),'raw_vertex_coordinate_max_bits':max(bits(x) for p in P for x in p),'raw_centroid_coordinate_max_bits':max(map(bits,g)),'centred_coordinate_max_bits':max(bits(x-c) for p in P for x,c in zip(p,g)),'volume_bits':bits(W),'raw_first_moment_bits':max(map(bits,M)),'ordinary_volume_decimal':float(W),'raw_first_moments_decimal':list(map(float,M)),'raw_centroid_decimal':list(map(float,g)),'centred_first_moments':[0,0,0],'new_chain':chain,'new_chain_owners':[sorted(owner[i]) for i in chain],'new_chain_exact_positive_checks':ce,'new_chain_then_apex_path':path,'primal_forest':pf,'dual_forest':df,'primitive_zero_counts':[a['face_primitive_zero_count'],a['vertex_max_zero_count'],a['edge_primitive_zero_count']],'edge_primitive_count':a['edge_primitive_count'],'face_primitive_count':sum(map(len,a['face_signs'])),'all_vertex_support_comparisons':len(P)*(len(P)-1)}
 return stats
if __name__=='__main__':
 p=Path(sys.argv[1]);s=run(json.loads((p/'A.json').read_text()),json.loads((p/'raw.json').read_text()));(p/'STATS.json').write_bytes(canonical(s));print(json.dumps({k:v for k,v in s.items() if k not in ('primal_forest','dual_forest')},indent=2));print('FORESTS',[(k,{kk:vv for kk,vv in s[k].items() if kk not in ('parents','depths')}) for k in ('primal_forest','dual_forest')])
