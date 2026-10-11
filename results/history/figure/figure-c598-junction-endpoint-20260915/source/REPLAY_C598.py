"""Source-only exact replay; requires the completely journaled FOUR_FRONTIERS core.
Usage: python -B -S REPLAY_C598.py CORE_DIRECTORY FRESH_OUTPUT_DIRECTORY
"""
import hashlib,json,sys
from pathlib import Path
from fractions import Fraction as Q
from math import gcd,lcm
import verify_candidate
sys.set_int_max_str_digits(0)
blob=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
sha=lambda b:hashlib.sha256(b).hexdigest()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def hpoint(r):
 d=lcm(*(t.denominator for t in r));return tuple(int(t*d) for t in r)+(d,)
def plane(a,b,c):
 e=[b[i]*a[3]-a[i]*b[3] for i in range(3)];f=[c[i]*a[3]-a[i]*c[3] for i in range(3)];n=cross(e,f);assert n!=(0,0,0)
 h=dot(n,a[:3]);r=tuple(v*a[3] for v in n)+(h,);d=gcd(*r)
 if h<0:d=-d
 return tuple(v//d for v in r)
def main():
 core,out=map(Path,sys.argv[1:]);out.mkdir(parents=True,exist_ok=False);here=Path(__file__).resolve().parent
 for n,r in json.loads((core/'CORE_MANIFEST.json').read_text()).items():
  b=(core/n).read_bytes();assert len(b)==r['bytes'] and sha(b)==r['sha256']
 sys.path.insert(0,str(core));import RECONSTRUCT,check_A,check_B
 cfg=json.loads((here/'SELECTORS.json').read_text());r=json.loads((core/'CASES.json').read_text())[cfg['parent_case']]
 full=RECONSTRUCT.recover(json.loads((core/r['generator']).read_text()));raw={'H':[h for i,h in enumerate(full['H']) if i not in r['deleted']]};assert sha(blob(raw))==r['raw_sha256']
 par=check_A.run(raw);pb=blob(par);assert sha(pb)==cfg['parent_audit_sha256'];(out/'PARENT_A.json').write_bytes(pb)
 P=[hpoint(tuple(map(Q,row))) for row in par['raw_vertices']]+[hpoint(tuple(Q(v,cfg['grid']) for v in row)) for row in cfg['new_raw_points']]
 H=[]
 for s in cfg['selectors']:
  if 'old' in s:i=s['old'];row=tuple(par['normals'][i])+(par['offsets'][i],)
  else:row=plane(*(P[i] for i in s['tri']))
  assert row[3]>0 and all(dot(row[:3],p[:3])<=row[3]*p[3] for p in P);H.append(row)
 raw={'H':H};rb=blob(raw);assert sha(rb)=='1286c05904d1aee57346b1bbeb200d8998b1656b0319d2cf56b2bfbb071c3599';(out/'raw.json').write_bytes(rb);(out/'SELECTORS.json').write_bytes(blob(cfg))
 for label,fn in [('A',check_A.run),('B',check_B.run)]:
  ab=blob(fn(raw));assert len(ab)==435251 and sha(ab)=='97e6687a0fd4a47515153da6efe8ed9168ea0e2b5ec603b2e1ef7c6b8bf230b9';(out/(label+'.json')).write_bytes(ab);print('FULL_EXACT_C598',label,flush=True)
 verify_candidate.run(out,out/'PARENT_A.json',core);print('SOURCE_ONLY_TO91_CHAIN6_C598_REPLAY_PASS',flush=True)
if __name__=='__main__':main()
