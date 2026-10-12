"""Source-only cold reconstruction of a new exact rational nonwinner and a
quantitative obstruction for arbitrary geometry in its ten-vertex patch.
The exact construction never depends on numerical reoptimization.
"""
import sys,json,hashlib,argparse
from pathlib import Path
assert __debug__
sys.set_int_max_str_digits(0)
import RECONSTRUCT,check_A,check_B,CRITICAL,REPORT,ENERGY_CERT
ROOT=Path(__file__).resolve().parent
STAGES=['BASE','BUILD','A','B','REPORT','ENERGY','FINISH']
def meta(p):
 b=p.read_bytes();return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def dump(p,x):p.write_text(json.dumps(x,sort_keys=True,separators=(',',':')),encoding='utf-8')
def sources():
 for name,spec in json.loads((ROOT/'MANIFEST.json').read_text()).items():assert meta(ROOT/name)==spec,name

def stage(name,out):
 sources();params=json.loads((ROOT/'PARAMETERS.json').read_text())
 if name=='BASE':
  out.mkdir(parents=True,exist_ok=False);p=out/'BASE';p.mkdir()
  src=ROOT/'BASE_GENERATOR.json';assert meta(src)['sha256']=='bf9fdaf05231ceb11fba9fde10c8a638e664b52233b2da5cb11977b2f4ff27b2'
  H=RECONSTRUCT.recover(json.loads(src.read_text()))['H'];assert len(H)==137
  raw={'H':[row for i,row in enumerate(H) if i!=99]};dump(p/'raw.json',raw)
  a=check_B.run(raw);assert (a['V'],a['E'],a['F'],a['counts'],a['weak'])==(175,309,136,[1,2,1],[0,0,0]);dump(p/'B.json',a)
 elif name=='BUILD':
  b=json.loads((out/'BASE/B.json').read_text());raw,lab=CRITICAL.build(b,params);dump(out/'raw.json',raw);dump(out/'LABELS.json',lab)
 elif name in ['A','B']:
  raw=json.loads((out/'raw.json').read_text());a=(check_A.run if name=='A' else check_B.run)(raw)
  assert (a['V'],a['E'],a['F'],a['counts'],a['weak'])==(173,309,138,[4,6,8],[0,0,0]);assert a['edge_primitive_zero_count']==0
  dump(out/(name+'.json'),a)
  if name=='B':assert (out/'A.json').read_bytes()==(out/'B.json').read_bytes()
 elif name=='REPORT':
  b=json.loads((out/'BASE/B.json').read_text());a=json.loads((out/'A.json').read_text());dump(out/'REPORT.json',REPORT.run(b,params,a))
 elif name=='ENERGY':dump(out/'ENERGY_CERT.json',ENERGY_CERT.run(json.loads((out/'BASE/B.json').read_text())))
 else:
  fixtures=[({'H':[[1,1,1,1],[1,-1,-1,1],[-1,1,-1,1],[-1,-1,1,1]]},[0,0,0]),({'H':[[0,-3,0,1],[3,6,0,1],[-3,-3,0,1],[0,0,1,1],[0,0,-1,1]]},[1,2,3])]
  for r,weak in fixtures:
   a=check_A.run(r);b=check_B.run(r);assert a==b and a['counts']==[4,4,6] and a['weak']==weak;assert a['counts']!=[1,1,0]
  for fn in [check_A.run,check_B.run]:
   for raw in [{'H':[[1,0,0,0],[-1,0,0,1],[0,1,0,1],[0,0,1,1]]},{'H':[[1,1,1,1],[1,1,1,1],[-1,-1,-1,1],[0,0,1,1]]}]:
    try:fn(raw)
    except AssertionError:pass
    else:raise AssertionError('Invalid input accepted')
  expected=json.loads((ROOT/'EXPECTED.json').read_text())
  for fn,spec in expected.items():assert meta(out/fn)==spec,fn
  sources();dump(out/'RECEIPT.json',dict(status='NH72_CRITICAL_DISK_AND_ENERGY_BARRIER_SOURCE_ONLY_COLD_PASS',new_own110=False,exact_new_nonwinner=dict(V=173,E=309,F=138,strict=[4,6,8],weak=[0,0,0]),independent_full_audits=2,third_centred_mass=True,ten_vertex_replacement_obstruction=True,expected_outputs=expected))
 print(name,'PASS',flush=True)
 if name=='FINISH':print('NH72_CRITICAL_DISK_AND_ENERGY_BARRIER_SOURCE_ONLY_COLD_PASS',flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);ap.add_argument('--stage',choices=['ALL']+STAGES,default='ALL');arg=ap.parse_args()
 for s in STAGES if arg.stage=='ALL' else [arg.stage]:stage(s,arg.out)
