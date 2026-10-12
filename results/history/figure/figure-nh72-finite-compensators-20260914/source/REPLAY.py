"""Source-only exact replay, split into bounded stages for interruption safety.
The rational proxy has two independent complete audits; the isolated algebraic
root additionally has its own Krawczyk and uniform full-complex/mechanics proof.
"""
import sys,json,hashlib,argparse
from pathlib import Path
assert __debug__
sys.set_int_max_str_digits(0)
import RECONSTRUCT,check_A,check_B,BUILD,ROOT_VERIFY,FROZEN_STARS,VERIFY_COVERS,DETAILS
ROOT=Path(__file__).resolve().parent
STAGES=['BASE','PAIR99_BUILD','PAIR99_A','PAIR99_B','PAIR99_ROOT','PAIR99_DETAILS','TRIPLE117_BUILD','TRIPLE117_A','TRIPLE117_B','TRIPLE117_ROOT','TRIPLE117_DETAILS','COVERS','FINISH']
def dump(p,x):p.write_text(json.dumps(x,sort_keys=True,separators=(',',':')),encoding='utf-8')
def meta(p):b=p.read_bytes();return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def sources():
 for name,v in json.loads((ROOT/'MANIFEST.json').read_text()).items():assert meta(ROOT/name)==v,name

def stage(which,out):
 sources();par=json.loads((ROOT/'PARAMETERS.json').read_text())
 if which=='BASE':
  out.mkdir(parents=True,exist_ok=False);gen=ROOT/'BASE_GENERATOR.json';assert meta(gen)['sha256']=='bf9fdaf05231ceb11fba9fde10c8a638e664b52233b2da5cb11977b2f4ff27b2';H=RECONSTRUCT.recover(json.loads(gen.read_text()))['H'];assert len(H)==137
  for j in [99,117,84]:
   p=out/f'DEL{j}';p.mkdir();r={'H':[h for i,h in enumerate(H) if i!=j]};dump(p/'raw.json',r);a=check_B.run(r);assert a['counts']==[1,2,1] and a['weak']==[0,0,0];dump(p/'B.json',a)
  print('S8_DELETION_BASES_RECONSTRUCTED',flush=True)
 elif which=='COVERS':
  covers=json.loads((ROOT/'COVERS.json').read_text())
  for j in [99,117,84]:
   b=json.loads((out/f'DEL{j}/B.json').read_text());r=VERIFY_COVERS.verify(b,j,covers[str(j)]);dump(out/f'PERFECT_COVER_{j}.json',r)
  print('NINE_PERFECT_CENTROID_ARBITRARY_CAP_COVERS_PASS',flush=True)
 elif which=='FINISH':
  for fixture in [{'H':[[1,1,1,1],[1,-1,-1,1],[-1,1,-1,1],[-1,-1,1,1]]},{'H':[[1,0,0,1],[0,1,0,1],[-1,-1,0,1],[0,0,1,1],[0,0,-1,1]]}]:
   a=check_A.run(fixture);b=check_B.run(fixture);assert a==b and a['counts']!=[1,1,0]
  for fn in [check_A.run,check_B.run]:
   for raw in [{'H':[[1,0,0,0],[-1,0,0,1],[0,1,0,1],[0,0,1,1]]},{'H':[[1,1,1,1],[1,1,1,1],[-1,-1,-1,1],[0,0,1,1]]}]:
    try:fn(raw)
    except AssertionError:pass
    else:raise AssertionError('invalid input accepted')
  expected=json.loads((ROOT/'EXPECTED.json').read_text());assert len(expected)>=20
  for name,v in expected.items():assert meta(out/name)==v,name
  sources();dump(out/'RECEIPT.json',dict(status='NH72_TWO_FINITE_CAP_COMPENSATORS_ROOTS_AND_RATIONAL_AUDITS_COLD_PASS',new_own110=False,rational_nonwinners=2,isolated_algebraic_mass_closed_nonwinners=2,independent_rational_audits=4,finite_krawczyk_and_all_feature_proofs=2,arbitrary_cap_multivertex_exclusions=2,perfect_centroid_interval_exclusions=9,outputs=expected));print('NH72_TWO_FINITE_CAP_COMPENSATORS_ROOTS_AND_RATIONAL_AUDITS_COLD_PASS',flush=True)
 else:
  case,action=which.rsplit('_',1);j=BUILD.CASES[case]['deleted_support'];base=json.loads((out/f'DEL{j}/B.json').read_text());p=out/case;eta=[ROOT_VERIFY.Q(v,1<<par[case]['centre_bits']) for v in par[case]['eta_numerators']]
  if action=='BUILD':
   p.mkdir(exist_ok=False);r,lab=BUILD.raw(base,case,eta);dump(p/'raw.json',r);dump(p/'LABELS.json',lab);print(case,'EXACT_FINITE_RATIONAL_INPUT_BUILT',flush=True)
  elif action in ['A','B']:
   r=json.loads((p/'raw.json').read_text());a=(check_A.run if action=='A' else check_B.run)(r);dump(p/(action+'.json'),a);want=[9,2,9] if case=='PAIR99' else [10,3,11];assert a['counts']==want and a['weak']==[0,0,0] and a['edge_primitive_zero_count']==0
   if action=='B':assert (p/'A.json').read_bytes()==(p/'B.json').read_bytes()
   print(case,action,a['V'],a['E'],a['F'],a['counts'],flush=True)
  elif action=='ROOT':dump(p/'ROOT.json',ROOT_VERIFY.verify(base,case,par[case]))
  elif action=='DETAILS':
   a=json.loads((p/'A.json').read_text());rp=json.loads((p/'ROOT.json').read_text());dump(p/'DETAILS.json',DETAILS.run(base,case,par[case],a,rp));dump(p/'FROZEN_STARS.json',FROZEN_STARS.run(base,case));print(case,'THIRD_MASS_COMPLEX_MAP_AND_FINITE_OBSTRUCTION_PASS',flush=True)
  else:raise AssertionError(action)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);p.add_argument('--stage',choices=['ALL']+STAGES,default='ALL');a=p.parse_args()
 for s in STAGES if a.stage=='ALL' else [a.stage]:stage(s,a.out)
