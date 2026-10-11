"""Complete exact supporting-plane enumeration from an integer point cloud."""
import argparse,hashlib,json,sys
from itertools import combinations
from math import gcd
from pathlib import Path
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def encoded(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def make(points):
 P=sorted(set(tuple(map(int,p)) for p in points));H=set()
 for a,b,c in combinations(P,3):
  n=cross(sub(b,a),sub(c,a))
  if n==(0,0,0):continue
  h=dot(n,a);positive=False;negative=False
  for x in P:
   z=dot(n,x)-h;positive|=z>0;negative|=z<0
   if positive and negative:break
  if positive and negative:continue
  assert positive or negative
  if positive:n=tuple(-t for t in n);h=-h
  assert h>0,'Origin must be interior; translate the input by an interior point.'
  d=gcd(*n,h);H.add(tuple(t//d for t in n)+(h//d,))
 return {'H':[list(r) for r in sorted(H)]}
def main():
 p=argparse.ArgumentParser();p.add_argument('points');p.add_argument('out');p.add_argument('--core',required=True);a=p.parse_args();out=Path(a.out);out.mkdir(parents=True,exist_ok=False)
 data=json.loads(Path(a.points).read_bytes());P=data['points'];raw=make(P);(out/'raw.json').write_bytes(encoded(raw));sys.path.insert(0,str(Path(a.core).resolve()));import check_A,check_B,centred_mass
 aa=check_A.run(raw);bb=check_B.run(raw);assert aa==bb
 pp=set(tuple(map(int,p)) for p in P);from fractions import Fraction as F
 assert all(tuple(map(F,v)) in pp for v in aa['raw_vertices'])
 for name,obj in [('A.json',aa),('B.json',bb),('MASS.json',centred_mass.run(aa))]:(out/name).write_bytes(encoded(obj))
 print('EXACT_INTEGER_POINT_HULL_AB_MASS_PASS',aa['V'],aa['E'],aa['F'],aa['counts'],aa['weak'],flush=True)
 for f in sorted(out.iterdir()):b=f.read_bytes();print(f.name,len(b),hashlib.sha256(b).hexdigest(),flush=True)
if __name__=='__main__':main()
