"""Exact source-only replay; dependencies are the journaled core and C598 raw H."""
import argparse,hashlib,importlib,json,sys
from pathlib import Path
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
S=lambda b:hashlib.sha256(b).hexdigest()

def main():
 p=argparse.ArgumentParser();p.add_argument('--core',type=Path,required=True);p.add_argument('--c598-raw',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--resume',action='store_true');p.add_argument('--third-mass',action='store_true');args=p.parse_args()
 expected=json.loads((ROOT/'EXPECTED.json').read_text());cuts=json.loads((ROOT/'CUTS.json').read_text())
 for name,r in expected['sources'].items():
  data=(ROOT/name).read_bytes();assert len(data)==r['bytes'] and S(data)==r['sha256']
 for name,r in expected['core_sources'].items():
  data=(args.core/name).read_bytes();assert len(data)==r['bytes'] and S(data)==r['sha256']
 data=args.c598_raw.read_bytes();assert len(data)==expected['c598_raw']['bytes'] and S(data)==expected['c598_raw']['sha256']
 args.out.mkdir(parents=True,exist_ok=args.resume)
 sys.path.insert(0,str(args.core.resolve()));reconstruct=importlib.import_module('RECONSTRUCT');check_A=importlib.import_module('check_A');check_B=importlib.import_module('check_B');mass=importlib.import_module('centred_mass')
 def obtain(name,make):
  path=args.out/name;path.parent.mkdir(parents=True,exist_ok=True);r=expected['outputs'][name]
  if args.resume and path.exists():
   data=path.read_bytes();assert len(data)==r['bytes'] and S(data)==r['sha256'];return json.loads(data)
  obj=make();data=B(obj);assert len(data)==r['bytes'] and S(data)==r['sha256'];path.write_bytes(data);return obj
 c598=json.loads(data);obtain('C598_raw.json',lambda:c598)
 parentraw=reconstruct.recover(json.loads((args.core/'BQ13_C602.json').read_text()))
 assert S(B(parentraw))=='5ad19a2833a43340303026d1b6a39feec8fa055320d89d56f3261a4720d83125'
 obtain('C602_A.json',lambda:check_B.run(parentraw))
 obtain('C598_A.json',lambda:check_B.run(c598))
 for name,spec in cuts.items():
  raw={'H':[row if i!=114 else spec['replacement'] for i,row in enumerate(c598['H'])]}
  obtain(name+'/raw.json',lambda raw=raw:raw)
  a=obtain(name+'/A.json',lambda raw=raw:check_A.run(raw));b=obtain(name+'/B.json',lambda raw=raw:check_B.run(raw));assert a==b
  assert [a[k] for k in ['V','E','F']]==spec['V_E_F'] and a['counts']==spec['counts'] and a['weak']==[0,0,0]
  if args.third_mass:obtain(name+'/MASS.json',lambda a=a:mass.run(a))
  print('EXACT_ONE_FACET_ENDPOINT_PASS',spec['identity'],flush=True)
 import certify_one_facet
 certify_one_facet.main(args.out)
 data=(args.out/'ONE_FACET_CERTIFICATE.json').read_bytes();r=expected['outputs']['ONE_FACET_CERTIFICATE.json'];assert len(data)==r['bytes'] and S(data)==r['sha256']
 import arithmetic_stats
 obtain('ARITHMETIC_REPORT.json',lambda:arithmetic_stats.run(args.out))
 print('C598_ONE_FACET_SOURCE_ONLY_REPLAY_PASS',flush=True)
if __name__=='__main__':main()
