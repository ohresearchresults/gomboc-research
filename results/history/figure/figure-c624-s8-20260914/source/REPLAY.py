"""Source-only exact reconstruction, two independent full audits and centred mass.
All geometry and acceptance comparisons use integers/Fraction; no NumPy or SciPy.
Do not disable assertions. Use a fresh --out directory for stage A or ALL.
"""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
if not __debug__:raise RuntimeError('Assertions are required; do not use -O.')
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent
import RECONSTRUCT,check_A,check_B,centred_mass,measure,compare
import importlib.util
spec=importlib.util.spec_from_file_location('coordinate_export',R/'export.py');export=importlib.util.module_from_spec(spec);spec.loader.exec_module(export)
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def meta(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def sources():
 s=json.loads((R/'SOURCE_MANIFEST.json').read_text())
 for n,v in s.items():assert meta((R/n).read_bytes())==v,n
 return len(s)
def generator(name):
 d=json.loads((R/('STRONG_G14_GENERATOR.json' if name=='S8' else 'G14_GENERATOR.json')).read_text())
 if name!='G14':
  D=10**(8 if name=='S8' else 10 if name=='G10' else 9)
  d['controls']=[[round(F(v*D,d['grid'])) for v in row] for row in d['controls']];d['grid']=D
  if name=='G9P':d['controls'][168][0]+=1
 return d
def validate(a,name):
 expected=json.loads((R/'EXPECTED.json').read_text())[name]
 assert [a[k] for k in ('V','E','F')]==[177,312,137]
 assert a['counts']==expected['counts'] and a['weak']==[0,0,0]
 assert a['active_input_indices']==list(range(137))
 assert all(a[k]==0 for k in ('face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count'))
 assert a['centred_first_moments']==a['centred_centroid']==[0,0,0]
 assert a['integration_triangle_count']==350 and a['edge_primitive_count']==1248
 assert a['stable_face_ids']==[3]
 assert a['unstable_vertices']==([95,160] if name=='G9' else [95])
 assert a['saddle_edges']==([[157,160]] if name=='G9' else [])
def fixtures():
 cases=[('tetra',[[-1,-1,-1,1],[-1,1,1,1],[1,-1,1,1],[1,1,-1,1]],[4,4,6],[0,0,0]),('weak_prism',[[1,0,0,1],[-2,3,0,1],[1,-3,0,1],[0,0,1,1],[0,0,-1,1]],[4,4,6],[1,2,3])]
 out=[]
 for name,H,c,w in cases:
  a=check_A.run({'H':H});b=check_B.run({'H':H});assert a==b and a['counts']==c and a['weak']==w
  assert c!=[1,1,0] or w!=[0,0,0];out.append(dict(name=name,counts=c,weak=w,winner_gate_rejected=True))
 return out
def stage(name,out,which,coordinates=False):
 sources();expected=json.loads((R/'EXPECTED.json').read_text())[name]
 def save(n,x):
  b=canon(x);want=expected['files'].get(n)
  if want is not None:assert meta(b)==want,(name,n,meta(b),want)
  (out/n).write_bytes(b)
 if which=='A':
  out.mkdir(parents=True,exist_ok=False);d=generator(name);save('GENERATOR.json',d);raw=RECONSTRUCT.recover(d);save('raw.json',raw)
  a=check_A.run(raw);validate(a,name);save('A.json',a);print('C624_FULL_EXACT_A_PASS',name,flush=True)
 elif which=='B':
  raw=json.loads((out/'raw.json').read_text());assert meta((out/'raw.json').read_bytes())==expected['files']['raw.json']
  a=check_B.run(raw);validate(a,name);save('B.json',a);assert (out/'A.json').read_bytes()==(out/'B.json').read_bytes();print('C624_FULL_EXACT_B_PASS',name,flush=True)
 elif which=='MASS':
  a=json.loads((out/'A.json').read_text());validate(a,name);save('CENTRED_MASS.json',centred_mass.run(a));print('C624_CENTRED_MASS_PASS',name,flush=True)
 elif which=='DETAILS':
  a=json.loads((out/'A.json').read_text());raw=json.loads((out/'raw.json').read_text());validate(a,name)
  save('STATS.json',measure.run(a,raw));save('COMPARISON.json',compare.run(a,raw))
  if coordinates:export.run(out,out/'coordinates')
  print('C624_EXACT_DETAILS_PASS',name,flush=True)
 elif which=='FINISH':
  a=json.loads((out/'A.json').read_text());validate(a,name);assert (out/'A.json').read_bytes()==(out/'B.json').read_bytes()
  for n,v in expected['files'].items():assert meta((out/n).read_bytes())==v,(name,n)
  if coordinates:
   for n,v in expected['coordinates'].items():assert meta((out/'coordinates'/n).read_bytes())==v,n
  gate=a['counts']==[1,1,0] and a['weak']==[0,0,0]
  rec=dict(status='COORD_STABLECAP_RL_C624_COMPLETE_EXACT_PASS',object=name,accepted_equilibrium_gate=gate,VEF=[a[k] for k in ('V','E','F')],C=2*a['E'],counts=a['counts'],weak=a['weak'],independent_A_B_identical=True,source_payload_files=sources(),files=expected['files'],fixtures=fixtures())
  save('RECEIPT.json',rec);print(rec['status'],name,'WINNER' if gate else 'PRESERVED_NONWINNER',flush=True)
 else:raise ValueError(which)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--object',choices=['G14','G10','G9','G9P','S8'],default='G9P');p.add_argument('--out',required=True,type=Path);p.add_argument('--stage',choices=['A','B','MASS','DETAILS','FINISH','ALL'],default='ALL');p.add_argument('--coordinates',action='store_true');a=p.parse_args()
 for st in (['A','B','MASS','DETAILS','FINISH'] if a.stage=='ALL' else [a.stage]):stage(a.object,a.out,st,a.coordinates)
