"""Source-only exact reconstruction of one new external-interface nonwinner.
No old coordinate or centroid record is an input. All assertions are required.
"""
import sys,json,hashlib,argparse
from pathlib import Path
assert __debug__
sys.set_int_max_str_digits(0)
import RECONSTRUCT,check_A,check_B,NEW_BUILD,NEW_REPORT,SLICE_CERT
ROOT=Path(__file__).resolve().parent
STAGES=['BASE','BUILD','A','B','REPORT','SLICE','FINISH']
def meta(p):
 b=p.read_bytes();return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def dump(p,x):p.write_text(json.dumps(x,sort_keys=True,separators=(',',':')),encoding='utf-8')
def sources():
 for n,s in json.loads((ROOT/'MANIFEST.json').read_text()).items():assert meta(ROOT/n)==s,n

def stage(name,out):
 sources();gen=json.loads((ROOT/'BASE_GENERATOR.json').read_text());param=json.loads((ROOT/'PARAMETERS.json').read_text());oldp=json.loads((ROOT/'OLD_PARAMETERS.json').read_text())
 if name=='BASE':
  out.mkdir(parents=True,exist_ok=False);p=out/'BASE';p.mkdir()
  assert meta(ROOT/'BASE_GENERATOR.json')['sha256']=='bf9fdaf05231ceb11fba9fde10c8a638e664b52233b2da5cb11977b2f4ff27b2'
  H=RECONSTRUCT.recover(gen)['H'];assert len(H)==137
  raw={'H':[row for i,row in enumerate(H) if i!=99]};dump(p/'raw.json',raw)
  a=check_B.run(raw);assert (a['V'],a['E'],a['F'],a['counts'],a['weak'])==(175,309,136,[1,2,1],[0,0,0]);dump(p/'B.json',a)
 elif name=='BUILD':
  b=json.loads((out/'BASE/B.json').read_text());r,l,d=NEW_BUILD.run(b,gen,param)
  for n,x in [('raw.json',r),('LABELS.json',l),('INTERFACE_GENERATOR.json',d)]:dump(out/n,x)
 elif name in ['A','B']:
  r=json.loads((out/'raw.json').read_text());a=(check_A.run if name=='A' else check_B.run)(r)
  assert (a['V'],a['E'],a['F'],a['counts'],a['weak'])==(173,309,138,[7,18,23],[0,0,0]);assert a['edge_primitive_zero_count']==0
  dump(out/(name+'.json'),a)
  if name=='B':assert (out/'A.json').read_bytes()==(out/'B.json').read_bytes()
 elif name=='REPORT':
  b=json.loads((out/'BASE/B.json').read_text());a=json.loads((out/'A.json').read_text());dump(out/'REPORT.json',NEW_REPORT.run(b,gen,param,oldp,a))
 elif name=='SLICE':
  b=json.loads((out/'BASE/B.json').read_text());a=json.loads((out/'A.json').read_text());dump(out/'SLICE_CERT.json',SLICE_CERT.run(b,gen,param,a))
 else:
  import FREEZE
  tests=[({'H':[[1,1,1,1],[1,-1,-1,1],[-1,1,-1,1],[-1,-1,1,1]]},[0,0,0]),({'H':[[0,-3,0,1],[3,6,0,1],[-3,-3,0,1],[0,0,1,1],[0,0,-1,1]]},[1,2,3])]
  for r,w in tests:
   a=check_A.run(r);b=check_B.run(r);assert a==b and a['counts']==[4,4,6] and a['weak']==w;assert a['counts']!=[1,1,0]
  for fn in [check_A.run,check_B.run]:
   for r in [{'H':[[1,0,0,0],[-1,0,0,1],[0,1,0,1],[0,0,1,1]]},{'H':[[1,1,1,1],[1,1,1,1],[-1,-1,-1,1],[0,0,1,1]]}]:
    try:fn(r)
    except AssertionError:pass
    else:raise AssertionError('Invalid input accepted')
  expected=json.loads((ROOT/'EXPECTED.json').read_text())
  for n,s in expected.items():assert meta(out/n)==s,n
  sources();dump(out/'RECEIPT.json',dict(status='NH72_EXTERNAL_INTERFACE_AND_LOW_CONNECTOR_SOURCE_ONLY_COLD_PASS',new_own110=False,new_f_vector=[173,309,138],strict=[7,18,23],weak=[0,0,0],independent_full_exact_audits=2,independent_centred_mass=True,conditional_fixed_fan_obstruction=True,expected_outputs=expected))
 print(name,'PASS',flush=True)
 if name=='FINISH':print('NH72_EXTERNAL_INTERFACE_AND_LOW_CONNECTOR_SOURCE_ONLY_COLD_PASS',flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);ap.add_argument('--stage',choices=['ALL']+STAGES,default='ALL');a=ap.parse_args()
 for s in STAGES if a.stage=='ALL' else [a.stage]:stage(s,a.out)
