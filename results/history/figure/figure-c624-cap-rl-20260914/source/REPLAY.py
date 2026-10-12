"""Standalone exact C624 reconstruction. Standard library only; assertions required.
Stage ALL needs a fresh directory. A and B construct independent complexes and masses.
"""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
from math import lcm
from collections import Counter
if not __debug__:raise RuntimeError('Do not use -O')
sys.set_int_max_str_digits(0)
import RECONSTRUCT,check_A,check_B,centred_mass
from ROUND import rounded
ROOT=Path(__file__).resolve().parent

def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def sha(b):return hashlib.sha256(b).hexdigest()
def verify_bytes(b,s):assert len(b)==s['bytes'] and sha(b)==s['sha256']
def sources():
 for f,s in json.loads((ROOT/'MANIFEST.json').read_text()).items():verify_bytes((ROOT/f).read_bytes(),s)
def validate(a,s):
 assert [a[k] for k in ['V','E','F']]==s['VEF']
 for field,expected in [('counts',s['counts']),('weak',s['weak']),('stable_face_ids',s['stable']),('unstable_vertices',s['unstable']),('saddle_edges',s['saddles'])]:assert a[field]==expected
 assert a['active_input_indices']==list(range(137))
 assert a['centred_first_moments']==a['centred_centroid']==[0,0,0]
 assert all(a[k]==0 for k in ['face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count'])
 assert a['edge_primitive_count']==1248 and sum(map(len,a['faces']))==624
 owners=[tuple(i for i,cy in enumerate(a['faces']) if v in cy) for v in range(a['V'])]
 assert len(set(owners))==177
 assert (16,18,71,94) in owners and (71,94,109,116,119,126) in owners
 assert (3,17,49,57,73,88,134,135,136) in owners
 assert tuple(map(F,a['raw_vertices'][95]))==(F(0),F(0),F(1))
 assert sum(len(c)-2 for c in a['faces'])==350
 return owners

def coordinates(a):
 p=[tuple(map(F,row)) for row in a['raw_vertices']];g=tuple(map(F,a['raw_centroid']))
 d=lcm(*(x.denominator for row in p for x in row),*(x.denominator for x in g))
 x=[[str((d//v.denominator)*v.numerator-(d//c.denominator)*c.numerator) for v,c in zip(row,g)] for row in p]
 return {'definition':'All vertices equal integer_vertices divided by common_denominator. Uniform filled body, own centroid exactly zero.','common_denominator':str(d),'integer_vertices':x,'faces':a['faces'],'true_edges':a['edges']}

def fixture_test():
 answer=[]
 for name,H,c,w in [('tetra',[[-1,-1,-1,1],[-1,1,1,1],[1,-1,1,1],[1,1,-1,1]],[4,4,6],[0,0,0]),('weak_prism',[[1,0,0,1],[-2,3,0,1],[1,-3,0,1],[0,0,1,1],[0,0,-1,1]],[4,4,6],[1,2,3])]:
  a=check_A.run({'H':H});b=check_B.run({'H':H});assert a==b and a['counts']==c and a['weak']==w
  assert (c,w)!=([1,1,0],[0,0,0]);answer.append({'name':name,'counts':c,'weak':w,'winner_gate_rejected':True})
 return answer

def run(name,out,stage,export):
 sources();s=json.loads((ROOT/'EXPECTED.json').read_text())[name];gb=(ROOT/'GENERATOR_G14.json').read_bytes()
 if s['round_grid_power']!=14:gb=canon(rounded(json.loads(gb),s['round_grid_power']))
 verify_bytes(gb,s['generator'])
 rb=canon(RECONSTRUCT.recover(json.loads(gb)));verify_bytes(rb,s['raw']);raw=json.loads(rb)
 if stage=='ALL':out.mkdir(parents=True,exist_ok=False)
 else:out.mkdir(parents=True,exist_ok=True)
 for f,b in [('GENERATOR.json',gb),('raw.json',rb)]:
  if (out/f).exists():assert (out/f).read_bytes()==b
  else:(out/f).write_bytes(b)
 for label,engine in [('A',check_A),('B',check_B)]:
  if stage in ['ALL',label]:
   a=engine.run(raw);validate(a,s);b=canon(a);verify_bytes(b,s['record']);(out/(label+'.json')).write_bytes(b)
   print('EXACT',name,label,a['V'],a['E'],a['F'],a['counts'],a['weak'],flush=True)
 if stage in ['ALL','MASS']:
  ab=(out/'A.json').read_bytes();verify_bytes(ab,s['record']);m=centred_mass.run(json.loads(ab));assert m==s['mass'];(out/'CENTRED_MASS.json').write_bytes(canon(m));print('THIRD_MASS',name,'PASS',flush=True)
 if stage in ['ALL','FINISH']:
  ab=(out/'A.json').read_bytes();bb=(out/'B.json').read_bytes();assert ab==bb;verify_bytes(ab,s['record']);a=json.loads(ab);owners=validate(a,s)
  m=json.loads((out/'CENTRED_MASS.json').read_text());assert m==s['mass']
  receipt={'identity':s['identity'],'status':('C624_GOMBOC_EXACT_PASS' if a['counts']==[1,1,0] else 'C624_EXACT_NONWINNER_CENSUS_PASS'),'VEF':s['VEF'],'counts':a['counts'],'weak':a['weak'],'generator':s['generator'],'raw':s['raw'],'record':s['record'],'mass':m,'fixtures':fixture_test(),'face_histogram':dict(sorted(Counter(map(len,a['faces'])).items())),'degree_histogram':dict(sorted(Counter(map(len,owners)).items()))}
  (out/'RECEIPT.json').write_bytes(canon(receipt));print(receipt['status'],name,flush=True)
  if export:
   b=canon(coordinates(a));(out/'EXACT_COORDS.json').write_bytes(b)
   x=json.loads((out/'EXACT_COORDS.json').read_bytes());d=int(x['common_denominator']);g=list(map(F,a['raw_centroid']))
   assert [[F(int(z),d) for z in row] for row in x['integer_vertices']]==[[F(z)-c for z,c in zip(row,g)] for row in a['raw_vertices']]
   print('EXACT_COORDS',len(b),sha(b),flush=True)
 sources()
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--object',choices=['G9','G14','G8_NONWINNER'],default='G9');p.add_argument('--out',type=Path,required=True);p.add_argument('--stage',choices=['ALL','A','B','MASS','FINISH'],default='ALL');p.add_argument('--coordinates',action='store_true');a=p.parse_args();run(a.object,a.out,a.stage,a.coordinates)
