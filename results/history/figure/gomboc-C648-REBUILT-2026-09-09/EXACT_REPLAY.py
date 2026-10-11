from pathlib import Path
from itertools import product
from fractions import Fraction as Q
from collections import Counter
import sys,json,hashlib,tempfile,subprocess
assert not sys.flags.optimize
sys.set_int_max_str_digits(0)
import RECONSTRUCT,check_A,check_B,EXTRA,ARCHITECTURE
R=Path(__file__).resolve().parent
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def emit(name,x):
 b=canon(x);(R/name).write_bytes(b);h=hashlib.sha256(b).hexdigest();print(name,len(b),h,flush=True);return h
def controls():
 tests=[([[1,1,1,1],[1,-1,-1,1],[-1,1,-1,1],[-1,-1,1,1]],[4,4,6],[0,0,0]),([[s if j==i else 0 for j in range(3)]+[1] for i in range(3) for s in [-1,1]],[6,8,12],[0,0,0]),([list(p)+[1] for p in product([-1,1],repeat=3)],[8,6,12],[0,0,0]),([[0,-1,1,1],[0,-5,1,1],[-2,3,-1,1],[2,3,-1,1]],[3,2,3],[0,2,2]),([[-1,0,0,1],[1,0,0,2],[0,-1,0,2],[0,1,0,1],[0,0,-1,1],[0,0,1,1]],[6,8,12],[0,0,0])]
 out=[]
 for H,count,weak in tests:
  a=check_A.run({'H':H});b=check_B.run({'H':H});assert a==b;assert a['counts']==count and a['weak']==weak;out.append({k:a[k] for k in ['V','E','F','counts','weak','ordinary_volume','raw_first_moments','raw_centroid','edge_primitive_zero_count']})
 assert out[-1]['ordinary_volume']=='18' and out[-1]['raw_first_moments']==['9','-9','0'] and out[-1]['raw_centroid']==['1/2','-1/2','0']
 invalid=[[[1,0,0,0],[0,1,0,1],[0,0,1,1],[-1,-1,-1,1]],tests[0][0]+[tests[0][0][0]],[[1,0,0,1],[0,1,0,1],[0,0,1,1],[1,1,1,1]]]
 rejected=0
 for f in [check_A.run,check_B.run]:
  for H in invalid:
   try:f({'H':H})
   except AssertionError:rejected+=1
   else:raise AssertionError('invalid body accepted')
 assert rejected==6
 return {'fixtures':out,'invalid_inputs_rejected':rejected}

def complexity(raw,a):
 def bits(rows):
  f=[Q(v) for row in rows for v in row]
  return dict(count=len(f),max_numerator_bits=max(abs(v.numerator).bit_length() for v in f),max_denominator_bits=max(v.denominator.bit_length() for v in f),total_numerator_bits=sum(abs(v.numerator).bit_length() for v in f),total_denominator_bits=sum(v.denominator.bit_length() for v in f))
 c=list(map(Q,a['raw_centroid']));X=[list(map(Q,p)) for p in a['raw_vertices']];C=[[v-c[j] for j,v in enumerate(p)] for p in X]
 assert all(Q(m)-Q(a['ordinary_volume'])*g==0 for m,g in zip(a['raw_first_moments'],c))
 r=bits([[Q(v,h[3]) for v in h[:3]] for h in raw['H']]);r['raw_vertices']=bits(X);r['centred_vertices']=bits(C);r['volume_and_centroid']=bits([[a['ordinary_volume'],*a['raw_centroid']]])
 return r,[[str(v) for v in p] for p in C]
def main():
 meta=json.loads((R/'EXPECTED.json').read_text());data=json.loads((R/'GENERATOR.json').read_text());hashes={}
 raw=RECONSTRUCT.recover(data);hashes['RAW.json']=emit('RAW.json',raw)
 if 'raw_sha256' in meta:assert hashes['RAW.json']==meta['raw_sha256']
 a=check_A.run(raw);hashes['A.json']=emit('A.json',a);b=check_B.run(raw);hashes['B.json']=emit('B.json',b);assert a==b
 assert [a[k] for k in ['V','E','F']]==meta['VEF'];assert a['counts']==meta['counts'] and a['weak']==[0,0,0]
 assert a['edge_primitive_zero_count']==a['face_primitive_zero_count']==a['vertex_max_zero_count']==0
 e=EXTRA.finish(a,b);hashes['EXTRA.json']=emit('EXTRA.json',e);hashes['CONTROLS.json']=emit('CONTROLS.json',controls())
 ar=ARCHITECTURE.run(data,a);assert ar['ordered_vertex_pair_zero_count']==0;hashes['ARCHITECTURE.json']=emit('ARCHITECTURE.json',ar)
 bits,centred=complexity(raw,a);hashes['FRACTION_BITS.json']=emit('FRACTION_BITS.json',bits);hashes['CENTRED_VERTICES.json']=emit('CENTRED_VERTICES.json',centred)
 summary={k:e[k] for k in ['V','E','F','C','counts','weak','degree_histogram','facet_size_histogram','stable_input_rows','unstable_vertices','unstable_raw_coordinates','edge_primitive_count','edge_primitive_zero_count','face_primitive_zero_count','vertex_max_zero_count','primal_relative_margin_floor_1e12','polar_relative_margin_floor_1e12']}
 summary.update(tag=meta['tag'],ordinary_volume_float=float(Q(a['ordinary_volume'])),raw_centroid_float=[float(Q(v)) for v in a['raw_centroid']],fraction_bits=bits)
 hashes['SUMMARY.json']=emit('SUMMARY.json',summary)
 if (R/'FROZEN.json').exists():assert hashes==json.loads((R/'FROZEN.json').read_text())
 else:(R/'FROZEN.json').write_bytes(canon(hashes))
 print(meta['tag']+'_TWO_FULL_INDEPENDENT_EXACT_AUDITS_AND_CONTROLS_PASS',flush=True)
 if '--cold' in sys.argv:
  with tempfile.TemporaryDirectory(prefix='contact36-source-only-') as td:
   p=Path(td)
   for name in ['REPLAY.py','RECONSTRUCT.py','check_A.py','check_B.py','EXTRA.py','ARCHITECTURE.py','EXPECTED.json','GENERATOR.json','FROZEN.json']:(p/name).write_bytes((R/name).read_bytes())
   subprocess.run([sys.executable,'-S',str(p/'REPLAY.py')],cwd=p,check=True)
   for name,h in hashes.items():assert hashlib.sha256((p/name).read_bytes()).hexdigest()==h
  print(meta['tag']+'_COLD_SOURCE_ONLY_ALL_NINE_OUTPUTS_MATCH_PASS',flush=True)
if __name__=='__main__':main()
