"""Source-only exact replay for the new finite Finch3 homogeneous polyhedra.
No precomputed vertex clouds, moments or equilibrium reports are read."""
import sys,json,time,hashlib,argparse
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'core'))
import radial,check_A,check_B,centred_mass

def encoded(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def info(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def bit(x):
 a=F(x);return max(abs(a.numerator).bit_length(),a.denominator.bit_length())
def execute(name,out):
 cases=json.loads((HERE/'CASES.json').read_text());case=cases[name];gb=(HERE/case['generator']).read_bytes();assert info(gb)==case['generator_info'];G=json.loads(gb);out=Path(out);out.mkdir(parents=True,exist_ok=False)
 raw,P=radial.reconstruct(G)
 for i,row in case.get('replace',{}).items():raw['H'][int(i)]=row
 b=encoded(raw);assert info(b)==case['raw'];(out/'raw.json').write_bytes(b);r={'case':name,'generator':case['generator_info'],'raw':info(b),'audits':{}}
 for mod,n in [(check_A,'A'),(check_B,'B')]:
  t=time.perf_counter();A=mod.run(raw);b=encoded(A);assert info(b)==case['audit'];(out/(n+'.json')).write_bytes(b);r['audits'][n]={'seconds':time.perf_counter()-t,**info(b)};print(n,A['V'],A['E'],A['F'],A['counts'],A['weak'],flush=True)
 assert (out/'A.json').read_bytes()==(out/'B.json').read_bytes();assert [A['V'],A['E'],A['F'],*A['counts'],*A['weak']]==case['census']
 X=[tuple(map(F,p)) for p in A['raw_vertices']]
 if not case.get('replace'):
  assert set(X)==set(map(tuple,P));idx={p:i for i,p in enumerate(X)};assert len(A['active_input_indices'])==G['n_supports']
  for f,cy in zip(A['active_input_indices'],A['faces']):assert {X[i] for i in cy}=={tuple(P[j]) for j in G['faces'][f]}
  EE={tuple(sorted((idx[tuple(P[i])],idx[tuple(P[j])]))) for cy in G['faces'] for i,j in zip(cy,cy[1:]+cy[:1])};assert EE==set(map(tuple,A['edges']))
 r['mass']=centred_mass.run(A);(out/'MASS.json').write_bytes(encoded(r['mass']));assert A['face_primitive_zero_count']==A['vertex_max_zero_count']==A['edge_primitive_zero_count']==0
 g=tuple(map(F,A['raw_centroid']));r['bits']={'H':max(abs(v).bit_length() for h in raw['H'] for v in h),'raw_vertices':max(bit(v) for p in X for v in p),'volume':bit(A['ordinary_volume']),'first_moments':max(map(bit,A['raw_first_moments'])),'centroid':max(map(bit,g)),'centred_vertices':max(bit(v-c) for p in X for v,c in zip(p,g)),'common_centred_denominator':r['mass']['common_centred_denominator_bits']}
 r['census']=case['census'];r['C']=2*A['E'];r['strict_carriers']={'S':A['stable_face_ids'],'U':A['unstable_vertices'],'H':A['saddle_edges']};r['volume_decimal']=float(F(A['ordinary_volume']));r['first_moments_decimal']=[float(F(x)) for x in A['raw_first_moments']];r['centroid_decimal']=[float(x) for x in g];r['facet_histogram']=dict(Counter(map(len,A['faces'])));r['degree_histogram']=dict(Counter(Counter(i for e in A['edges'] for i in e).values()));r['primitive_counts']={'face_sides':sum(map(len,A['face_signs'])),'vertex_maxima':len(A['vertex_max_escape_signs']),'edges':A['edge_primitive_count'],'integration_triangles':A['integration_triangle_count']};r['source_only']=True;r['strict110']=A['counts']==[1,1,0] and A['weak']==[0,0,0];(out/'RECEIPT.json').write_bytes(encoded(r));print('FINCH3_SOURCE_ONLY_EXACT_NONWINNER_PASS',json.dumps(r),flush=True);return r
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--case',required=True);p.add_argument('--out',required=True);a=p.parse_args();execute(a.case,a.out)
