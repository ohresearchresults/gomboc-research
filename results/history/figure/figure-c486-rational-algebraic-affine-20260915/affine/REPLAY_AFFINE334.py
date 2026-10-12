"""Source-only exact projective/affine image of the durable C486/R12 body.
Usage: python -B -S REPLAY_AFFINE334.py CORE C592_SOURCE R12_SOURCE NEW
Python3.13.5 standard library only, assertions enabled. No optimizer input.
"""
import hashlib,json,math,subprocess,sys
from fractions import Fraction as F
from pathlib import Path
assert __debug__;sys.set_int_max_str_digits(0)
W=[160244033420,-551074883587,-405940322882]
AA=[[223130167327,1144696532243,-506678711666],[0,223130179325,-1776865151697],[0,0,20085534550802]]
D=10**12
SOURCES={'raw.json':'89b725797808088bd7d467dadb64df6a3235e1097d7e19d25d99e68271fe5614','A.json':'8ee12742068e4246b3b7daf688703b3ce6f1c9803202a7d05f96e3ad8806ac21'}
EXPECTED={'raw.json':(48126,'e5c4f5132a9108ee61c8bae372ac5eb539946cabb5ef13b2ccdc4503e41d8215'),'A.json':(369749,'da8cf5eb7aae13cde167d16cb62113bef626df482b295d9d07c8a132c9c76ac1'),'B.json':(369749,'da8cf5eb7aae13cde167d16cb62113bef626df482b295d9d07c8a132c9c76ac1'),'MASS.json':(223,'98f285fc688c4dbb4673f56a3654904fef1d492e1d76e6c05803de2f9573c1bd')}
B=lambda o:json.dumps(o,sort_keys=True,separators=(',',':')).encode()
SHA=lambda b:hashlib.sha256(b).hexdigest()
def inverse(a):
 m=[list(row)+[F(i==j) for j in range(3)] for i,row in enumerate(a)]
 for i in range(3):
  j=next(j for j in range(i,3) if m[j][i]);m[i],m[j]=m[j],m[i]
  d=m[i][i];m[i]=[z/d for z in m[i]]
  for j in range(3):
   if j!=i:
    d=m[j][i];m[j]=[x-d*y for x,y in zip(m[j],m[i])]
 return [row[3:] for row in m]
def construct(source):
 raw=json.loads((source/'raw.json').read_bytes());w=[F(z,D) for z in W];a=[[F(z,D) for z in row] for row in AA];ai=inverse(a);H=[]
 for row in raw['H']:
  h=F(row[3]);q=[F(z)/h+w[i] for i,z in enumerate(row[:3])]
  v=[sum(q[i]*ai[i][j] for i in range(3)) for j in range(3)]+[F(1)]
  de=math.lcm(*(v.denominator for v in v));z=[int(v*de) for v in v];g=math.gcd(*z);H.append([v//g for v in z])
 return dict(H=H)
def verify(source,output):
 for name,sha in SOURCES.items():assert SHA((source/name).read_bytes())==sha
 old=json.loads((source/'A.json').read_bytes());new=json.loads((output/'A.json').read_bytes())
 w=[F(z,D) for z in W];A=[[F(z,D) for z in row] for row in AA];assert all(A[i][i]>0 for i in range(3))
 P=[tuple(map(F,p)) for p in old['raw_vertices']];images=[];gaps=[]
 for p in P:
  de=1+sum(wi*pi for wi,pi in zip(w,p));assert de>0;gaps.append(de)
  images.append(tuple(sum(x*y for x,y in zip(row,p))/de for row in A))
 vertices=[tuple(map(F,p)) for p in new['raw_vertices']];assert sorted(images)==vertices
 mapping=[vertices.index(p) for p in images]
 assert (new['V'],new['E'],new['F'])==(118,243,127) and new['counts']==[3,3,4] and new['weak']==[0,0,0]
 assert new['active_input_indices']==list(range(127))
 assert new['stable_face_ids']==[47,89,91] and new['unstable_vertices']==sorted(mapping[i] for i in [63,65,79])
 bits=lambda x:max(abs(F(x).numerator).bit_length(),F(x).denominator.bit_length())
 c=list(map(F,new['raw_centroid']))
 receipt=dict(identity='COORD_C486_PROJECTIVE_AFFINE_R12_OWN334',V=118,E=243,F=127,C=486,strict=[3,3,4],weak=[0,0,0],original_R12_to_new_raw_lex=mapping,stable_faces=new['stable_face_ids'],unstable_vertices=new['unstable_vertices'],saddle_edges=new['saddle_edges'],minimum_projective_denominator=str(min(gaps)),primitive_H_bits=max(abs(x).bit_length() for r in json.loads((output/'raw.json').read_bytes())['H'] for x in r),raw_vertex_bits=max(bits(x) for p in vertices for x in p),own_centroid_bits=max(map(bits,c)),centred_vertex_bits=max(bits(x-y) for p in vertices for x,y in zip(p,c)),actual_volume_bits=bits(new['ordinary_volume']),actual_first_moment_bits=max(map(bits,new['raw_first_moments'])))
 (output/'RECEIPT.json').write_bytes(B(receipt))
 print('EXACT_C486_AFFINE_334_IMAGE_BIJECTION_AND_OWN_MASS_PASS',flush=True)
def main():
 core,child,source,out=map(Path,sys.argv[1:]);out.mkdir(parents=True,exist_ok=False)
 subprocess.run([sys.executable,'-B','-S',str(source/'REPLAY_OPPOSITE.py'),str(core),str(child),str(out/'PARENT')],check=True)
 old=out/'PARENT/C486';new=out/'C486_AFFINE';new.mkdir()
 for name,sha in SOURCES.items():assert SHA((old/name).read_bytes())==sha
 raw=construct(old);(new/'raw.json').write_bytes(B(raw));sys.path.insert(0,str(core));import check_A,check_B,centred_mass
 for name,fn in [('A',check_A.run),('B',check_B.run)]:
  record=fn(raw);(new/(name+'.json')).write_bytes(B(record));print('FULL_EXACT_C486_AFFINE',name,record['counts'],record['weak'],flush=True)
 (new/'MASS.json').write_bytes(B(centred_mass.run(json.loads((new/'A.json').read_bytes()))))
 for name,(nb,sha) in EXPECTED.items():
  b=(new/name).read_bytes();assert len(b)==nb and SHA(b)==sha
 verify(old,new)
 print('SOURCE_ONLY_C486_PROJECTIVE_AFFINE_R12_OWN334_REPLAY_PASS',flush=True)
if __name__=='__main__':main()
