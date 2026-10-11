"""Complete deterministic rational case definitions. No floating construction needed."""
import copy,json,hashlib
from pathlib import Path
from derive import blob,quantize,close82_85
ROOT=Path(__file__).resolve().parent

def generator(name):
 data=json.loads((ROOT/'GENERATOR_DATA.json').read_text());recipes=json.loads((ROOT/'RECIPES.json').read_text())
 def get(n):
  if n in data:return copy.deepcopy(data[n])
  r=recipes[n];g=get(r['parent'])
  if r['operation']=='quantize':return quantize(g,r['power'])
  if r['operation']=='close82_85':return close82_85(g)
  if r['operation']=='plane117':g['controls'][117]=r['controls'];return g
  raise ValueError(r)
 return get(name)

def prepare(reports=False):
 import RECONSTRUCT
 cases=json.loads((ROOT/'NEW_CASES.json').read_text())
 for name in sorted(set(json.loads((ROOT/'GENERATOR_DATA.json').read_text()))|set(json.loads((ROOT/'RECIPES.json').read_text()))):
  (ROOT/(name+'_GENERATOR.json')).write_bytes(blob(generator(name)))
 if reports:
  import check_A
  for name in ['FINCH_SEQUENTIAL','CLOSED_EDGE1','INHERIT1','MARGIN2','MARGIN2_GRID6_DELETE16','D16_ONE_GRID7']:
   c=cases[name];g=generator(c['generator']);H=RECONSTRUCT.recover(g)['H'];assert len(H)==137
   raw={'H':[r for i,r in enumerate(H) if i not in c['deleted']]};a=check_A.run(raw);b=blob(a);assert hashlib.sha256(b).hexdigest()==c['report_sha256'];(ROOT/(name+'_A.json')).write_bytes(b)
 print('EXACT_INPUTS_PREPARED')
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--reports',action='store_true');a=p.parse_args();prepare(a.reports)
