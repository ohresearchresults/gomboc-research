"""Exact round-base obstruction for all homogeneous pyramids on two fixed bases.
The theorem and proof are in ROUND_BASE_PROOF.md; checks certify its hypotheses.
"""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
sys.set_int_max_str_digits(0)
C138=[[-507,187,93],[-503,185,-16],[-491,182,204],[-479,176,-120],[-452,168,312],[-437,160,-215],[-394,146,411],[-379,139,-297],[-316,118,498],[-308,113,-363],[-229,83,-412],[-221,83,568],[-144,52,-442],[-112,43,617],[6,0,643],[38,-79,-367],[118,-41,616],[221,-79,568],[311,-113,502],[386,-141,420],[443,-162,327],[482,-177,226],[485,-179,-84],[502,-184,121],[503,-185,17]]
def enc(o):return json.dumps(o,sort_keys=True,separators=(',',':'),default=str).encode()
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det2(p,q):return p[0]*q[2]-p[2]*q[0]
def certificate(P,apex):
 B=[tuple(map(F,p)) for i,p in enumerate(P) if i!=apex];ids=sorted(range(len(B)),key=lambda i:(B[i][0],B[i][2]));cycle=[]
 for seq in [ids,ids[::-1]]:
  cy=[]
  for i in seq:
   while len(cy)>1 and det2(sub(B[cy[-1]],B[cy[-2]]),sub(B[i],B[cy[-2]]))<=0:cy.pop()
   cy.append(i)
  cycle+=cy[:-1]
 assert len(cycle)==len(B)
 edges=[(B[i],B[j]) for i,j in zip(cycle,cycle[1:]+cycle[:1])];anchor=B[cycle[0]];shifted=[(sub(p,anchor),sub(q,anchor)) for p,q in edges];area2=sum(det2(p,q) for p,q in shifted);assert area2>0
 b=tuple(anchor[k]+sum((p[k]+q[k])*det2(p,q) for p,q in shifted)/(3*area2) for k in range(3));n=cross(sub(B[cycle[1]],B[cycle[0]]),sub(B[cycle[2]],B[cycle[0]]));assert any(n);assert all(dot(n,sub(p,b))==0 for p in B)
 inner=[];outer=[]
 for p,q in edges:
  e=sub(q,p);w=sub(b,p);c=cross(e,w);assert dot(n,c)>0;inner.append(dot(c,c)/dot(e,e));outer.append(dot(sub(p,b),sub(p,b)))
 R=min(isqrt(v.numerator//v.denominator) for v in inner)-1;Q=max(isqrt(v.numerator//v.denominator)+1 for v in outer);assert R>0
 assert all(v>R*R for v in inner) and all(v<Q*Q for v in outer)
 passes=20*R>=13*Q
 if passes:assert 4*R*R>Q*Q and 5869*R*R>2400*Q*Q
 return {'base_centroid':b,'base_points':B,'cycle_base_indices':cycle,'inradius_lower_integer':R,'circumradius_upper_integer':Q,'inner_squared':inner,'outer_squared':outer,'roundness_integer_margin':20*R-13*Q,'large_t_margin':5869*R*R-2400*Q*Q,'passes_all_apex_exclusion':passes,'scope':'ALL noncoplanar apex positions with the fixed planar base; uniform filled volume, exact own centroid. Not all deformations of the base and not arbitrary density.'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();assert __debug__;a.out.mkdir(parents=True,exist_ok=False)
 import c80_gate
 P96=[];n=(4,11,0)
 for i,p in enumerate(C138):
  s=0 if i==15 else dot(n,p);P96.append([137*p[k]-s*n[k] for k in range(3)])
 out={name:certificate(P,i) for name,P,i in [('C80_BASE20',c80_gate.POINTS,14),('C96_BASE24',P96,15)]}
 for name,r in out.items():
  (a.out/(name+'.json')).write_bytes(enc(r));print(name,r['inradius_lower_integer'],r['circumradius_upper_integer'],r['passes_all_apex_exclusion'],flush=True)
 (a.out/'SUMMARY.json').write_bytes(enc({k:{i:v for i,v in r.items() if i not in ['base_points','cycle_base_indices','inner_squared','outer_squared']} for k,r in out.items()}))
 mf={p.name:{'bytes':len(p.read_bytes()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(a.out.glob('*.json'))};(a.out/'OUTPUT_MANIFEST.json').write_bytes(enc(mf));print('ROUND_BASE_EXACT_HYPOTHESIS_CHECKS_FINISHED',flush=True)
if __name__=='__main__':main()
