"""Exact single-exterior-point hull from its visible facets and horizon.
Usage: python -B -S augment_exact.py C592_PROOF NEW_OUTPUT
"""
import hashlib,json,sys
from pathlib import Path
from fractions import Fraction as Q
from math import gcd,lcm
assert __debug__
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
SHA=lambda b:hashlib.sha256(b).hexdigest()
CHILD='d200af2491ba532cd9307caceb4d780e9a661a4c9094da10e4e0c3562875204d'
TRIAL=(874577931702,454209162144,-558471315966)
D=10**12

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def point(row):
 p=tuple(map(Q,row));d=lcm(*(x.denominator for x in p))
 return tuple(int(x*d) for x in p)+(d,)
def plane(a,b,c):
 e=[b[j]*a[3]-a[j]*b[3] for j in range(3)]
 f=[c[j]*a[3]-a[j]*c[3] for j in range(3)]
 n=cross(e,f);assert n!=(0,0,0)
 h=dot(n,a[:3]);r=tuple(v*a[3] for v in n)+(h,)
 assert h!=0
 g=gcd(*r)*(1 if h>0 else -1)
 return tuple(v//g for v in r)
def run(root,out):
 raw=(root/'A.json').read_bytes();assert SHA(raw)==CHILD
 A=json.loads(raw);out.mkdir(parents=True,exist_ok=False)
 P=[point(x) for x in A['raw_vertices']]+[point(tuple(Q(x,D) for x in TRIAL))]
 a=P[-1];H0=[tuple(n)+(h,) for n,h in zip(A['normals'],A['offsets'])]
 gaps=[dot(h[:3],a[:3])-h[3]*a[3] for h in H0]
 assert all(gaps) and max(gaps)>0 and min(gaps)<0
 visible=[i for i,g in enumerate(gaps) if g>0];V=set(visible)
 incidence={tuple(e):[] for e in A['edges']}
 for f,cy in enumerate(A['faces']):
  for i,j in zip(cy,cy[1:]+cy[:1]):incidence[tuple(sorted((i,j)))].append(f)
 H={h:dict(old=i) for i,h in enumerate(H0) if i not in V};horizon=[]
 for e,ff in sorted(incidence.items()):
  assert len(ff)==2
  if (ff[0] in V)==(ff[1] in V):continue
  r=plane(P[e[0]],P[e[1]],a)
  assert all(dot(r[:3],p[:3])<=r[3]*p[3] for p in P)
  H.setdefault(r,dict(tri=[e[0],e[1],len(P)-1]));horizon.append(e)
 for r in H:assert r[3]>0 and all(dot(r[:3],p[:3])<=r[3]*p[3] for p in P)
 rows=sorted(H)
 cfg=dict(identity='COORD_C592_OPPOSITE_POINT_R12',parent_A_sha256=CHILD,grid=D,new_point=list(TRIAL),visible_facets=visible,horizon_edges=horizon,selectors=[H[r] for r in rows])
 for name,obj in [('raw.json',dict(H=rows)),('SELECTORS.json',cfg)]:
  b=B(obj);(out/name).write_bytes(b);print(name,len(b),SHA(b),flush=True)
 print('EXACT_HORIZON_AUGMENT_GENERATED',len(visible),len(horizon),len(rows),flush=True)
if __name__=='__main__':run(*map(Path,sys.argv[1:]))
