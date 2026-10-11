"""Source-only exact C476 own222 nonwinner derived from the rational C486 R12.
Usage python -B -S REPLAY_DELETE476.py CORE C592_SOURCE R12_SOURCE AFFINE_SOURCE NEW
"""
import hashlib,json,sys,subprocess
from pathlib import Path
from fractions import Fraction as F
assert __debug__;sys.set_int_max_str_digits(0)
B=lambda o:json.dumps(o,sort_keys=True,separators=(',',':')).encode()
SHA=lambda b:hashlib.sha256(b).hexdigest()
def verify(parent,out,aff):
 raw=json.loads((out/'A.json').read_bytes());old=json.loads((parent/'A.json').read_bytes());D={42,63,83}
 P=[tuple(map(F,p)) for p in old['raw_vertices']];w=[F(x,aff.D) for x in aff.W];A=[[F(x,aff.D) for x in row] for row in aff.AA]
 images={}
 for i,p in enumerate(P):
  if i in D:continue
  de=1+sum(x*y for x,y in zip(w,p));assert de>0
  images[i]=tuple(sum(x*y for x,y in zip(row,p))/de for row in A)
 V=[tuple(map(F,p)) for p in raw['raw_vertices']];assert sorted(images.values())==V
 assert (raw['V'],raw['E'],raw['F'])==(115,238,125) and raw['counts']==[2,2,2] and raw['weak']==[0,0,0]
 assert raw['active_input_indices']==list(range(125))
 assert raw['unstable_vertices']==sorted(V.index(images[i]) for i in [65,79])
 assert raw['stable_face_ids']==[46,88]
 bits=lambda x:max(abs(F(x).numerator).bit_length(),F(x).denominator.bit_length());c=list(map(F,raw['raw_centroid']))
 record=dict(identity='COORD_C476_AFFINE_DELETE42_63_83_OWN222',V=115,E=238,F=125,C=476,strict=[2,2,2],weak=[0,0,0],deleted_original_R12_ids=sorted(D),original_R12_to_new_rawlex={str(i):V.index(p) for i,p in images.items()},stable_faces=raw['stable_face_ids'],unstable_vertices=raw['unstable_vertices'],saddle_edges=raw['saddle_edges'],raw_vertex_bits=max(bits(x) for p in V for x in p),own_centroid_bits=max(map(bits,c)),centred_vertex_bits=max(bits(x-y) for p in V for x,y in zip(p,c)),primitive_H_bits=max(abs(x).bit_length() for row in json.loads((out/'raw.json').read_bytes())['H'] for x in row),volume_bits=bits(raw['ordinary_volume']))
 (out/'RECEIPT.json').write_bytes(B(record));print('EXACT_C476_OWN222_RETAINED_VERTEX_BIJECTION_PASS',flush=True)
def main():
 core,child,source,affine,out=map(Path,sys.argv[1:]);here=Path(__file__).resolve().parent
 for n,v in json.loads((here/'MANIFEST.json').read_bytes()).items():
  b=(here/n).read_bytes();assert len(b)==v['bytes'] and SHA(b)==v['sha256']
 assert SHA((affine/'REPLAY_AFFINE334.py').read_bytes())=='ec205eccb50fd705f71703f4ac35fc4d6f5f0ee13ee871b512652b8e42d3a359'
 sys.path.insert(0,str(affine));import REPLAY_AFFINE334 as aff
 import delete334_exact as delete
 out.mkdir(parents=True,exist_ok=False)
 subprocess.run([sys.executable,'-B','-S',str(source/'REPLAY_OPPOSITE.py'),str(core),str(child),str(out/'PARENT')],check=True)
 parent=out/'PARENT/C486';target=out/'C476';delete.main(parent,target)
 sys.path.insert(0,str(core));import check_A,check_B,centred_mass
 raw=json.loads((target/'raw.json').read_bytes())
 for name,fn in [('A',check_A.run),('B',check_B.run)]:
  a=fn(raw);(target/(name+'.json')).write_bytes(B(a));print('FULL_EXACT_C476',name,a['counts'],a['weak'],flush=True)
 (target/'MASS.json').write_bytes(B(centred_mass.run(json.loads((target/'A.json').read_bytes()))))
 verify(parent,target,aff)
 for n,v in json.loads((here/'EXPECTED.json').read_bytes()).items():
  b=(target/n).read_bytes();assert len(b)==v['bytes'] and SHA(b)==v['sha256']
 print('SOURCE_ONLY_C476_DELETE42_63_83_OWN222_REPLAY_PASS',flush=True)
if __name__=='__main__':main()
