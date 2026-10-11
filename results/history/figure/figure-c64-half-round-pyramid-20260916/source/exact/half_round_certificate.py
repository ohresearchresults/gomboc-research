"""Exact hypotheses and deformation radii for the half-roundness theorem.
Only standard-library rational arithmetic; both complete original inputs inline.
No assertion that all pyramids are excluded, only the stated radius hypotheses.
"""
import argparse,json,hashlib
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
C80=[[-66294190,227941,2608697],[-66539507,227941,-12351907],[-63292228,227941,17048174],[-63717145,227941,-27612608],[-57823754,227941,30439587],[-57515357,227941,-42510726],[-50192873,227941,42502470],[-47518485,227941,-56391110],[-40722545,227941,52969394],[-33461658,227941,-68086491],[-15099182,227941,-76015914],[-29598263,227941,61750890],[7302524,227941,-77602682],[32327466,227941,106281898],[79500788,227941,46525186],[84345871,227941,39971911],[90059112,227941,29647108],[97069983,227941,-15011783],[94470034,227941,18198055],[97382431,227941,4337405]]
C138=[[-507,187,93],[-503,185,-16],[-491,182,204],[-479,176,-120],[-452,168,312],[-437,160,-215],[-394,146,411],[-379,139,-297],[-316,118,498],[-308,113,-363],[-229,83,-412],[-221,83,568],[-144,52,-442],[-112,43,617],[6,0,643],[38,-79,-367],[118,-41,616],[221,-79,568],[311,-113,502],[386,-141,420],[443,-162,327],[482,-177,226],[485,-179,-84],[502,-184,121],[503,-185,17]]
def enc(o):return json.dumps(o,sort_keys=True,separators=(',',':'),default=str).encode()
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det2(p,q):return p[0]*q[2]-p[2]*q[0]
def certificate(P):
 B=[tuple(map(F,p)) for p in P];ids=sorted(range(len(B)),key=lambda i:(B[i][0],B[i][2]));cycle=[]
 for seq in [ids,ids[::-1]]:
  cy=[]
  for i in seq:
   while len(cy)>1 and det2(sub(B[cy[-1]],B[cy[-2]]),sub(B[i],B[cy[-2]]))<=0:cy.pop()
   cy.append(i)
  cycle+=cy[:-1]
 assert len(cycle)==len(B) and len(set(cycle))==len(B)
 edges=[(B[i],B[j]) for i,j in zip(cycle,cycle[1:]+cycle[:1])];anchor=B[cycle[0]];shifted=[(sub(p,anchor),sub(q,anchor)) for p,q in edges];area2=sum(det2(p,q) for p,q in shifted);assert area2>0
 c=tuple(anchor[k]+sum((p[k]+q[k])*det2(p,q) for p,q in shifted)/(3*area2) for k in range(3));normal=cross(sub(B[cycle[1]],B[cycle[0]]),sub(B[cycle[2]],B[cycle[0]]));assert any(normal) and all(dot(normal,sub(p,c))==0 for p in B)
 inner=[];outer=[];anti_min=None;fan_sums=[]
 for p,q in edges:
  e=sub(q,p);w=sub(c,p);v=cross(e,w);assert dot(normal,v)>0
  inner.append(dot(v,v)/dot(e,e));outer.append(dot(sub(p,c),sub(p,c)))
  assert all(dot(normal,cross(e,sub(b,p)))>=0 for b in B)
  for b in B:
   anti=tuple(c[k]-(b[k]-c[k])/2 for k in range(3));s=dot(normal,cross(e,sub(anti,p)));assert s>=0;anti_min=s if anti_min is None else min(anti_min,s)
 for b in B:
  weights=[det2(sub(p,b),sub(q,b))/area2 for p,q in edges];assert all(w>=0 for w in weights) and sum(weights)==1
  avg=tuple(sum(w*(p[k]+q[k]) for w,(p,q) in zip(weights,edges)) for k in range(3));assert tuple(b[k]+avg[k]-3*c[k] for k in range(3))==(0,0,0);fan_sums.append(sum(weights))
 R=min(isqrt(v.numerator//v.denominator) for v in inner)-1;Q=max(isqrt(v.numerator//v.denominator)+1 for v in outer)
 assert R>0 and all(v>R*R for v in inner) and all(v<Q*Q for v in outer) and 2*R>=Q
 delta=F(2*R-Q,3);kappa=F(2*R,Q);assert delta>=0 and delta<R and 2*(R-delta)==Q+delta
 return {'base_points':B,'base_centroid':c,'cyclic_original_indices':cycle,'inner_squared':inner,'outer_squared':outer,'R':R,'Q':Q,'half_round_margin':2*R-Q,'area_centred_Hausdorff_radius':delta,'base_affine_condition_number_limit':kappa,'all_apex_excluded':True,'all_anti_half_vertices_inside':True,'anti_half_min_oriented_gap':anti_min,'all_vertex_fan_centroid_identities':True,'scope':'Uniform filled 3D pyramids over these fixed bases, also all area-centred planar base perturbations within the reported Hausdorff bound and all planar affine base changes up to the reported singular-value condition number; arbitrary apex. No claim for all base changes.'}
def run():
 n=(4,11,0);P96=[[137*p[k]-dot(n,p)*n[k] for k in range(3)] for i,p in enumerate(C138) if i!=15]
 out={'C80_BASE20':certificate(C80),'C96_BASE24':certificate(P96)}
 assert [(v['R'],v['Q']) for v in out.values()]==[(66612792,100852489),(58972,78849)]
 assert out['C80_BASE20']['area_centred_Hausdorff_radius']==F(32373095,3)
 assert out['C96_BASE24']['area_centred_Hausdorff_radius']==F(39095,3)
 return out
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True,type=Path);a=ap.parse_args();assert __debug__;a.out.mkdir(parents=True,exist_ok=False)
 for n,o in run().items():(a.out/(n+'.json')).write_bytes(enc(o));print(n,o['R'],o['Q'],o['area_centred_Hausdorff_radius'],o['base_affine_condition_number_limit'],flush=True)
 print('HALF_ROUND_ALL_APEX_AND_BASE_NEIGHBOURHOOD_EXACT_CERTIFICATES_PASS',flush=True)
