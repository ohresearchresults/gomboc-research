"""Complete exact endpoint replay, with two independent hull/mass/mechanics audits.
Only Python standard library. Run without -O; output directory must be absent.
"""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from math import lcm
from pathlib import Path
from collections import Counter
import rational56,check_A,check_B,centred_mass
if not __debug__:raise RuntimeError('Assertions must be enabled')
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent

def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def sha(x):return hashlib.sha256(x).hexdigest()
def spec(b):return dict(bytes=len(b),sha256=sha(b))
def check(b,s):assert spec(b)==s

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def times(a,t):return tuple(t*x for x in a)
def source_check():
 for f,s in json.loads((ROOT/'MANIFEST.json').read_text()).items():check((ROOT/f).read_bytes(),s)

def owner_check(a):
 owners=[tuple(i for i,cy in enumerate(a['faces']) if v in cy) for v in range(a['V'])]
 want=json.loads((ROOT/'FACES.json').read_text());old=[tuple(i for i,cy in enumerate(want) if v in cy) for v in range(178)]
 assert len(set(owners))==178 and set(owners)==set(old)
 mapping={i:owners.index(o) for i,o in enumerate(old)}
 def cycle(c):
  k=c.index(min(c));return c[k:]+c[:k]
 assert [cycle([mapping[v] for v in cy]) for cy in want]==a['faces']
 assert (16,18,71,94) in owners and (71,94,109,116,119,126) in owners
 return owners

def fraction_cost(xs):
 xs=list(xs);return {'numerator':max(abs(x.numerator).bit_length() for x in xs),'denominator':max(x.denominator.bit_length() for x in xs)}

def metrics(a):
 P=[tuple(map(F,p)) for p in a['raw_vertices']];g=tuple(map(F,a['raw_centroid']));Z=[sub(p,g) for p in P]
 return {'primitive_H_bits':max(abs(v).bit_length() for r in a['normals'] for v in r),
         'primitive_offset_bits':max(abs(v).bit_length() for v in a['offsets']),
         'raw_vertices':fraction_cost(v for p in P for v in p),
         'volume':fraction_cost([F(a['ordinary_volume'])]),
         'first_moments':fraction_cost(map(F,a['raw_first_moments'])),
         'centroid':fraction_cost(g),'centred_vertices':fraction_cost(v for p in Z for v in p),
         'raw_common_denominator_bits':lcm(*(v.denominator for p in P for v in p)).bit_length(),
         'common_centred_denominator_bits':lcm(*(v.denominator for p in Z for v in p)).bit_length()}

def clearance(a,w,bounds):
 P=[tuple(map(F,p)) for p in a['raw_vertices']];g=tuple(map(F,a['raw_centroid']));N=a['normals'];h=a['offsets'];C=lcm(*(v.denominator for v in g));G=tuple(int(C*v) for v in g)
 ds=[lcm(*(v.denominator for v in p)) for p in P];aa=[tuple(int(d*v) for v in p) for d,p in zip(ds,P)];Z=[sub(times(p,C),times(G,d)) for d,p in zip(ds,aa)]
 hh=[v*C-dot(n,G) for n,v in zip(N,h)];assert min(hh)>0
 edges={tuple(e) for e in a['edges']};fedges=set()
 for i,j in edges:
  ff=[f for f,cy in enumerate(a['faces']) if i in cy and j in cy];assert len(ff)==2;fedges.add(tuple(sorted(ff)))
 def bound_check(x,y,b):
  xy=dot(x,y);assert xy>0
  assert xy*xy*b.denominator**2 > dot(x,x)*dot(y,y)*b.numerator**2
 def forest(pairs,count,root):
  parent=dict(pairs);assert len(parent)==count-1 and set(parent)==set(range(count))-{root}
  maximum=0
  for i in range(count):
   seen=set();v=i
   while v!=root:assert v not in seen;seen.add(v);v=parent[v]
   maximum=max(maximum,len(seen))
  return maximum
 for i,j in w['primal']:
  assert tuple(sorted((i,j))) in edges
  e=sub(times(aa[j],ds[i]),times(aa[i],ds[j]));bound_check(Z[i],e,F(bounds['primal']))
 for i,j in w['polar']:
  assert tuple(sorted((i,j))) in fedges
  b=sub(times(N[j],hh[i]),times(N[i],hh[j]));bound_check(N[i],b,F(bounds['polar']))
 gap=F(bounds['inactive_gap'])
 for v,(p,d) in enumerate(zip(aa,ds)):
  for f,(n,hf) in enumerate(zip(N,h)):
   x=hf*d-dot(n,p)
   if v in a['faces'][f]:assert x==0
   else:assert x*gap.denominator>hf*d*gap.numerator
 return {'status':'EXACT_ADJACENT_ESCAPE_AND_INACTIVE_GAP_BOUNDS_PASS',
         'strict_cosine_lower_bounds':bounds,'primal_depth':forest(w['primal'],178,96),
         'polar_depth':forest(w['polar'],137,3),'primal_arcs':177,'polar_arcs':136,
         'scope':'Endpoint inequalities, not a perturbation box.'}

def fixtures():
 result=[]
 for name,H,c,w in [('tetra',[[-1,-1,-1,1],[-1,1,1,1],[1,-1,1,1],[1,1,-1,1]],[4,4,6],[0,0,0]),('weak_prism',[[1,0,0,1],[-2,3,0,1],[1,-3,0,1],[0,0,1,1],[0,0,-1,1]],[4,4,6],[1,2,3])]:
  a=check_A.run({'H':H});b=check_B.run({'H':H});assert a==b and a['counts']==c and a['weak']==w
  assert (c,w)!=([1,1,0],[0,0,0]);result.append({'fixture':name,'counts':c,'weak':w,'rejected_as_winner':True})
 return result

def run(name,out):
 source_check();out.mkdir(parents=True,exist_ok=False);e=json.loads((ROOT/'EXPECTED.json').read_text())[name]
 gb=(ROOT/name/'GENERATOR.json').read_bytes();check(gb,e['generator']);d=json.loads(gb)
 raw=rational56.recover(d);rb=canon(raw);check(rb,e['raw']);(out/'raw.json').write_bytes(rb)
 records=[]
 for label,engine in [('A',check_A),('B',check_B)]:
  a=engine.run(raw);b=canon(a);check(b,e['record']);records.append(b);(out/(label+'.json')).write_bytes(b)
  assert [a[k] for k in ['V','E','F']]==[178,313,137]
  assert a['active_input_indices']==list(range(137)) and a['counts']==[1,1,0] and a['weak']==[0,0,0]
  assert a['stable_face_ids']==[3] and a['unstable_vertices']==[96] and a['saddle_edges']==[]
  assert a['weak_faces']==a['weak_vertices']==a['weak_edges']==[]
  assert all(a[k]==0 for k in ['face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count'])
  assert a['edge_primitive_count']==1252 and a['integration_triangle_count']==352
  assert a['centred_first_moments']==a['centred_centroid']==[0,0,0]
  assert tuple(map(F,a['raw_vertices'][96]))==(0,0,1)
  owners=owner_check(a)
  print('TWO_FULL_EXACT_COMPONENT',name,label,a['counts'],a['weak'],flush=True)
 assert records[0]==records[1]
 mass=centred_mass.run(a);assert mass==e['mass'];(out/'MASS.json').write_bytes(canon(mass))
 cost=metrics(a);assert cost==e['cost'];proof=clearance(a,json.loads((ROOT/name/'WITNESSES.json').read_text()),e['bounds'])
 receipt={'status':'ATLAS56_C626_TWO_INDEPENDENT_FULL_EXACT_AND_THIRD_MASS_SOURCE_ONLY_PASS',
          'object':name,'VEF':[178,313,137],'C':626,'counts':a['counts'],'weak':a['weak'],
          'generator':e['generator'],'raw':e['raw'],'record':e['record'],'mass':mass,'cost':cost,'clearance':proof,
          'merger_raw_vertex_ids':{'16_18_71_94':owners.index((16,18,71,94)),'71_94_109_116_119_126':owners.index((71,94,109,116,119,126))},
          'face_histogram':dict(sorted(Counter(map(len,a['faces'])).items())),
          'degree_histogram':dict(sorted(Counter(map(len,owners)).items())),
          'fixtures':fixtures()}
 (out/'RECEIPT.json').write_bytes(canon(receipt));source_check();print(receipt['status'],name,flush=True);print('RECEIPT',spec(canon(receipt)),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--object',choices=['ADAPT','D3_SMALL','D3_STRONG'],required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();run(a.object,a.out)
