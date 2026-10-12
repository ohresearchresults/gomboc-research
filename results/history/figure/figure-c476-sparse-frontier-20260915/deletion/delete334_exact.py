"""Exact local-horizon hull for three vertex deletions, then fixed affine334 map.
Usage python -B -S delete334_exact.py R12_PARENT_DIRECTORY OUT_DIRECTORY
Deleted indices are ORIGINAL rational C486 R12 raw-lex IDs, not affine334 IDs.
"""
import json,sys,math,hashlib,itertools
from fractions import Fraction as F
from pathlib import Path
import REPLAY_AFFINE334 as aff
assert __debug__;sys.set_int_max_str_digits(0)
DELETED=[42,63,83]
B=lambda o:json.dumps(o,sort_keys=True,separators=(',',':')).encode()
SHA=lambda b:hashlib.sha256(b).hexdigest()
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def primitive(v):
 d=math.lcm(*(x.denominator for x in v));z=[int(x*d) for x in v];g=math.gcd(*z);return tuple(x//g for x in z)
def main(parent,out):
 a=json.loads((parent/'A.json').read_bytes());assert SHA((parent/'A.json').read_bytes())==aff.SOURCES['A.json']
 old=json.loads((parent/'raw.json').read_bytes());assert SHA((parent/'raw.json').read_bytes())==aff.SOURCES['raw.json']
 P=[tuple(map(F,p)) for p in a['raw_vertices']];D=set(DELETED);keep=[i for i in range(len(P)) if i not in D]
 boundary=sorted({j for e in a['edges'] for i,j in [e,e[::-1]] if i in D and j not in D})
 H=set(tuple(r) for r in old['H']);new=[]
 for ids in itertools.combinations(boundary,3):
  p,q,r=[P[i] for i in ids];n=cross(sub(q,p),sub(r,p))
  if n==(0,0,0):continue
  h=dot(n,p)
  vals=[dot(n,P[i])-h for i in keep]
  if min(vals)<0 and max(vals)>0:continue
  if min(vals)>=0:n=tuple(-x for x in n);h=-h
  assert h>0
  row=primitive((*n,h))
  if row not in H:H.add(row);new.append(dict(row=list(row),selector=ids))
 # Every retained old vertex is still extreme. The exact audit must prove that
 # this halfspace intersection has no additional vertex, closing any local-horizon uncertainty.
 hh=[]
 for row in sorted(H):
  ids=[i for i in keep if dot(row[:3],P[i])==row[3]]
  if len(ids)<3:continue
  p=P[ids[0]]
  if not any(cross(sub(P[i],p),sub(P[j],p))!=(0,0,0) for i,j in itertools.combinations(ids[1:],2)):continue
  hh.append(list(row))
 out.mkdir(parents=True,exist_ok=False);un=out/'BEFORE';un.mkdir();(un/'raw.json').write_bytes(B(dict(H=hh)))
 # aff.construct only uses raw H; source identities are checked above, not re-aliased.
 raw=aff.construct(un);(out/'raw.json').write_bytes(B(raw));(out/'DEFINITION.json').write_bytes(B(dict(identity='COORD_C476_AFFINE_DELETE42_63_83',deleted_original_R12_ids=DELETED,boundary_original_R12_ids=boundary,retained_original_R12_ids=keep,new_local_planes=new,original_H_count=len(old['H']),retained_H_count=len(hh))))
 print('EXACT_PRIMAL_DELETION_H_GENERATED',len(hh),'boundary',boundary,'new',len(new),SHA((out/'raw.json').read_bytes()),flush=True)
if __name__=='__main__':main(*map(Path,sys.argv[1:]))
