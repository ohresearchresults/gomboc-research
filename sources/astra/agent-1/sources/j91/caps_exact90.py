"""Reconstruct exact nonsimple mass-cap bodies. Inputs are base exact auditor JSON
and a literal dictionary of rational apex coordinates keyed by INPUT plane index.
All old vertices/facet coplanarity remain EXACT. No normal-fan release occurs.
python caps_exact90.py BASE_AUDIT.json CAPS.json OUT_H.txt
"""
import json,sys,math
from fractions import Fraction as F
from functools import reduce
from pathlib import Path
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def plane(a,b,c):
 n=cross(sub(b,a),sub(c,a));h=dot(n,a)
 if h<0:n=tuple(-v for v in n);h=-h
 assert h>0
 row=(*n,h);d=math.lcm(*(x.denominator for x in row));z=[int(x*d) for x in row];k=reduce(math.gcd,z);return [a//k for a in z]
def build(base,caps):
 x=[tuple(map(F,r)) for r in base['vertices']];original=len(x);ap={int(k):tuple(F(v) for v in r) for k,r in caps['apexes'].items()};faces=[]
 for i,cy in enumerate(base['faces']):
  fi=base['active_input_planes'][i]
  if fi not in ap:faces.append(cy);continue
  new=len(x);x.append(ap[fi])
  faces.extend([[a,b,new] for a,b in zip(cy,cy[1:]+cy[:1])])
 rows=[plane(*(x[v] for v in cy[:3])) for cy in faces]
 for cy,row in zip(faces,rows):
  for v in cy:assert dot(row[:3],x[v])==row[3]
  for v,p in enumerate(x):
   d=row[3]-dot(row[:3],p);assert d>=0
   assert (d==0)==(v in cy), 'new unintended contact/coplanarity'
 edges=sorted({tuple(sorted([a,b])) for cy in faces for a,b in zip(cy,cy[1:]+cy[:1])})
 assert len(x)-len(edges)+len(faces)==2 and len(edges)<=249
 return rows,dict(V=len(x),E=len(edges),F=len(faces),base_vertices=original,added_vertices=len(ap),planes=rows,apexes=caps['apexes'])
if __name__=='__main__':
 b=json.loads(Path(sys.argv[1]).read_text());c=json.loads(Path(sys.argv[2]).read_text());rows,meta=build(b,c);out=Path(sys.argv[3]);out.write_text(f'{len(rows)} 0\n'+'\n'.join(' '.join(map(str,r)) for r in rows)+'\n');out.with_suffix('.geometry.json').write_text(json.dumps(meta,sort_keys=True,separators=(',',':'))+'\n');print('J90_EXACT_CAP_GEOMETRY',meta['V'],meta['E'],meta['F'])
