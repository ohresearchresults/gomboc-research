"""Two independent exact maximal-hull/mass/equilibrium audits and exact readback.
No numerical library is used. Frozen source bytes, not search execution, define bodies.
"""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
from math import lcm
from collections import Counter
import rational56,check_A,check_B,centred_mass,exact57,factory57
if not __debug__:raise RuntimeError('Assertions required')
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
NAMES=['S8_D3','S8_CORE4','S8_D2','C622_SEED','C622_IMPROVED','STAR7','STAR111','C622_D2_G9','C622_D2_G10','C622_D2_ADAPT']
def enc(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def spec(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def times(a,t):return tuple(x*t for x in a)
def source_check():
 for f,w in json.loads((ROOT/'MANIFEST.json').read_bytes()).items():assert spec((ROOT/f).read_bytes())==w

def owner_check(a,fs):
 oo=[tuple(i for i,cy in enumerate(a['faces']) if v in cy) for v in range(a['V'])];old=[tuple(i for i,cy in enumerate(fs) if v in cy) for v in range(1+max(map(max,fs)))];assert len(set(oo))==len(oo) and set(old)==set(oo);mp={i:oo.index(o) for i,o in enumerate(old)}
 def cycle(c):
  k=c.index(min(c));return c[k:]+c[:k]
 assert [cycle([mp[v] for v in cy]) for cy in fs]==a['faces']
 return oo,mp

def cost(a):
 P=[tuple(map(F,p)) for p in a['raw_vertices']];g=tuple(map(F,a['raw_centroid']));Z=[sub(p,g) for p in P]
 def bits(xs):
  xs=list(xs);return {'numerator':max(abs(x.numerator).bit_length() for x in xs),'denominator':max(x.denominator.bit_length() for x in xs)}
 return {'H':max(abs(x).bit_length() for row in a['normals'] for x in row),'offset':max(abs(x).bit_length() for x in a['offsets']),'raw':bits(x for p in P for x in p),'volume':bits([F(a['ordinary_volume'])]),'moment':bits(map(F,a['raw_first_moments'])),'centroid':bits(g),'centred':bits(x for p in Z for x in p),'raw_common':lcm(*(x.denominator for p in P for x in p)).bit_length(),'centred_common':lcm(*(x.denominator for p in Z for x in p)).bit_length()}

def forest(pairs,N,root):
 p=dict(pairs);assert len(p)==N-1 and set(p)==set(range(N))-{root};depth=0
 for i in range(N):
  seen=set();j=i
  while j!=root:assert j not in seen;seen.add(j);j=p[j]
  depth=max(depth,len(seen))
 return depth

def clear(a,w):
 P=[tuple(map(F,p)) for p in a['raw_vertices']];g=tuple(map(F,a['raw_centroid']));N=a['normals'];h=a['offsets'];C=lcm(*(v.denominator for v in g));G=tuple(int(C*v) for v in g)
 ds=[lcm(*(v.denominator for v in p)) for p in P];aa=[tuple(int(d*v) for v in p) for d,p in zip(ds,P)];Z=[sub(times(p,C),times(G,d)) for d,p in zip(ds,aa)];hh=[v*C-dot(n,G) for n,v in zip(N,h)];assert min(hh)>0
 edges={tuple(e) for e in a['edges']};fe=set()
 for i,j in edges:
  ff=[f for f,cy in enumerate(a['faces']) if i in cy and j in cy];assert len(ff)==2;fe.add(tuple(sorted(ff)))
 def positive(x,y,b):
  v=dot(x,y);assert v>0 and v*v*b.denominator**2>dot(x,x)*dot(y,y)*b.numerator**2
 def negative(x,y,lo,hi):
  v=dot(x,y);assert v<0 and lo<hi<0;z=v*v;d=dot(x,x)*dot(y,y)
  assert z*lo.denominator**2<d*lo.numerator**2
  assert z*hi.denominator**2>d*hi.numerator**2
 bad=w.get('bad_primal');badseen=0
 for i,j in w['primal']:
  assert tuple(sorted((i,j))) in edges;edge=sub(times(aa[j],ds[i]),times(aa[i],ds[j]))
  if bad is not None and [i,j]==bad:
   negative(Z[i],edge,*map(F,w['bad_interval']));badseen+=1
  else:positive(Z[i],edge,F(w['primal_bound']))
 assert badseen==(bad is not None)
 for i,j in w['polar']:
  assert tuple(sorted((i,j))) in fe;edge=sub(times(N[j],hh[i]),times(N[i],hh[j]));positive(N[i],edge,F(w['polar_bound']))
 gap=F(w['gap_bound'])
 for v,(p,d) in enumerate(zip(aa,ds)):
  for f,(n,hf) in enumerate(zip(N,h)):
   x=hf*d-dot(n,p)
   if v in a['faces'][f]:assert x==0
   else:assert x*gap.denominator>hf*d*gap.numerator
 return {'exact_adjacent_witnesses':True,'primal_depth':forest(w['primal'],a['V'],w['Uroot']),'polar_depth':forest(w['polar'],a['F'],w['Sroot']),'primal_bound':w['primal_bound'],'polar_bound':w['polar_bound'],'inactive_gap_bound':w['gap_bound'],'bad_primal':bad,'bad_interval':w.get('bad_interval'),'scope':'Endpoint only, not a perturbation box or a continuous path.'}

def fixtures():
 r=[]
 for name,H,c,w in [('tetra',[[-1,-1,-1,1],[-1,1,1,1],[1,-1,1,1],[1,1,-1,1]],[4,4,6],[0,0,0]),('weak_prism',[[1,0,0,1],[-2,3,0,1],[1,-3,0,1],[0,0,1,1],[0,0,-1,1]],[4,4,6],[1,2,3])]:
  a=check_A.run({'H':H});b=check_B.run({'H':H});assert a==b and a['counts']==c and a['weak']==w and c!=[1,1,0];r.append([name,c,w])
 return r

def definition(name):
 d,fs=exact57.source()
 if name=='C622_SEED':
  z,fs=exact57.leaf622(d,fs);return rational56.recover(z),fs,{'leaf_projection_then_equal_geometry_rechart':True}
 if name in ['STAR7','STAR111']:
  raw,proof=exact57.star(d,fs,7 if name=='STAR7' else 111,1 if name=='STAR7' else 0);return raw,None,proof
 if name in ['C622_D2_G9','C622_D2_G10']:
  z=factory57.generator(name);return rational56.recover(z),exact57.quotient_cycles(fs,162,164),{'exact_core_free_rechart':True,'rational_ties_to_even_grid':z['grid']}
 if name.startswith('C622'):fs=exact57.quotient_cycles(fs,162,164)
 z=factory57.generator(name);return rational56.recover(z),fs,{'chart':exact57.complexity(z)}

def witnesses(name,a,mp):
 if name.startswith('S8'):return json.loads((ROOT/'S8_WITNESSES.json').read_bytes())
 meta=json.loads((ROOT/'C622_SEED/META.json').read_bytes());up=[[mp[i],mp[j]] for i,j in enumerate(meta['uparent']) if i!=meta['Uroot']];sp=[[i,j] for i,j in enumerate(meta['sparent']) if i!=3]
 bound='9/500000000' if name=='C622_D2_G9' else '1/50000000'
 return dict(primal=up,polar=sp,Uroot=mp[95],Sroot=3,primal_bound=bound,polar_bound=bound,gap_bound='1/1250',bad_primal=[mp[162],mp[165]],bad_interval=['-41120306/1000000000','-41120304/1000000000'] if name=='C622_SEED' else ['-15406530/1000000000','-15406527/1000000000'])

def gate(a,e):
 assert [a[k] for k in ['V','E','F']]==e['VEF']
 assert a['active_input_indices']==list(range(a['F'])) and a['counts']==e['counts'] and a['weak']==[0,0,0]
 for key in ['stable_face_ids','unstable_vertices','saddle_edges']:assert a[key]==e[key]
 assert a['weak_faces']==a['weak_vertices']==a['weak_edges']==[]
 assert all(a[k]==0 for k in ['face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count'])
 assert a['edge_primitive_count']==4*a['E'] and a['integration_triangle_count']==2*a['V']-4
 assert a['centred_first_moments']==a['centred_centroid']==[0,0,0]

def run(name,out,stage):
 source_check();e=json.loads((ROOT/'EXPECTED.json').read_bytes())[name]
 if stage in ['A','ALL']:
  out.mkdir(parents=True,exist_ok=False);raw,fs,extra=definition(name);
  if not name.startswith('STAR'):
   gb=enc(factory57.generator(name));assert spec(gb)==e['generator'];(out/'GENERATOR.json').write_bytes(gb)
  b=enc(raw);assert spec(b)==e['raw'];(out/'raw.json').write_bytes(b);(out/'DEFINITION_PROOF.json').write_bytes(enc(extra))
 else:raw=json.loads((out/'raw.json').read_bytes());assert spec(enc(raw))==e['raw']
 for label,engine in [('A',check_A),('B',check_B)]:
  if stage not in ['ALL',label]:continue
  a=engine.run(raw);gate(a,e);b=enc(a);assert spec(b)==e['record'];(out/(label+'.json')).write_bytes(b);print('FULL_EXACT_PASS',name,label,flush=True)
 if stage in ['ALL','MASS']:
  a=json.loads((out/'B.json').read_bytes());m=centred_mass.run(a);assert m==e['mass'];(out/'MASS.json').write_bytes(enc(m));print('THIRD_FILLED_MASS_PASS',name,flush=True)
 if stage in ['ALL','FINISH']:
  ab=(out/'A.json').read_bytes();assert ab==(out/'B.json').read_bytes() and spec(ab)==e['record'];a=json.loads(ab);gate(a,e);m=json.loads((out/'MASS.json').read_bytes());assert m==e['mass'];cc=cost(a);assert cc==e['cost'];eq=exact57.equality();assert eq==json.loads((ROOT/'EQUALITY.json').read_bytes());pd=factory57.generator('PRE_RECHART');pf=json.loads((ROOT/'FACES_C622.json').read_bytes());assert exact57.complexity(exact57.general(pd,pf))['free']==314;assert exact57.complexity(exact57.core_free(factory57.generator('C622_IMPROVED')))['depth']==2;_,fs,_=definition(name)
  if fs is not None:ow,mp=owner_check(a,fs)
  else:ow=[tuple(i for i,cy in enumerate(a['faces']) if v in cy) for v in range(a['V'])]
  if a['F']==137:
   assert all(g in ow for g in [(16,18,71,94),(71,94,109,116,119,126),(3,17,49,57,73,88,134,135,136)])
  proof=clear(a,witnesses(name,a,mp)) if a['F']==137 else None
  rec={'status':'ATLAS57_SOURCE_ONLY_TWO_FULL_EXACT_AND_THIRD_MASS_PASS','object':name,'disposition':'WINNER' if a['counts']==[1,1,0] else 'PRESERVED_NONWINNER','VEF':e['VEF'],'C':2*a['E'],'counts':a['counts'],'weak':a['weak'],'raw':e['raw'],'record':e['record'],'mass':m,'fraction_cost':cc,'clearance':proof,'face_histogram':dict(sorted(Counter(map(len,a['faces'])).items())),'degree_histogram':dict(sorted(Counter(map(len,ow)).items())),'fixtures':fixtures()}
  (out/'EQUALITY.json').write_bytes(enc(eq));(out/'RECEIPT.json').write_bytes(enc(rec));print(rec['status'],name,rec['disposition'],flush=True);print('RECEIPT',spec(enc(rec)),flush=True)
 source_check()
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--object',choices=NAMES,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--stage',choices=['A','B','MASS','FINISH','ALL'],default='ALL');a=p.parse_args();run(a.object,a.out,a.stage)
