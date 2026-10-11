"""Recover the exact assigned C598 from its literal ancestor and five rational points."""
import sys,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from math import lcm,gcd
ROOT=Path(__file__).resolve().parent;sys.path.insert(0,str(ROOT/'core'));sys.set_int_max_str_digits(0)
import RECONSTRUCT,check_A,radial

def dump(path,x):
 b=json.dumps(x,sort_keys=True,separators=(',',':')).encode();Path(path).write_bytes(b);return hashlib.sha256(b).hexdigest()
def run():
 seed=ROOT/'seed';seed.mkdir(exist_ok=False);G=json.load(open(ROOT/'core/BQ13_C602.json'));a=check_A.run(RECONSTRUCT.recover(G));assert dump(seed/'PARENT_A.json',a)=='2426da394eda9520bd30b2b8b3e1f00d043697353bb6bc73658f5983653c11ec'
 cfg=json.load(open(ROOT/'junction/SELECTORS.json'));P=[list(map(F,p)) for p in a['raw_vertices']]+[[F(v,cfg['grid']) for v in p] for p in cfg['new_raw_points']];q=[[F(v,d) for v in n] for n,d in zip(a['normals'],a['offsets'])];H=[]
 for s in cfg['selectors']:
  v=q[s['old']] if 'old' in s else radial.solve([P[i] for i in s['tri']],[F(1)]*3);D=lcm(*(x.denominator for x in v));r=[int(x*D) for x in v]+[D];gg=gcd(*r);H.append([x//gg for x in r])
 raw={'H':H};assert dump(seed/'raw.json',raw)=='1286c05904d1aee57346b1bbeb200d8998b1656b0319d2cf56b2bfbb071c3599';a=check_A.run(raw);assert dump(seed/'A.json',a)=='97e6687a0fd4a47515153da6efe8ed9168ea0e2b5ec603b2e1ef7c6b8bf230b9';print('EXACT_ASSIGNED_C598_SOURCE_RECONSTRUCTED',flush=True)
if __name__=='__main__':run()
