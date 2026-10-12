"""Full exact uniform-volume-centred audit of an ordered rational pyramid.
Input: JSON list of ordered CCW base points followed by the apex, in 3D.
Both independent H-polytope auditors rebuild the complete hull from all
support triples or supporting lines, true edges, mass and every equilibrium.
No floating point, third-party package, or originating sandbox is needed.
"""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from itertools import combinations
from math import gcd,lcm
from pathlib import Path
import check_A,check_B,centred_mass
sys.set_int_max_str_digits(0)
def enc(o):return json.dumps(o,sort_keys=True,separators=(',',':'),default=str).encode()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def primitive(r):
 d=lcm(*(v.denominator for v in r));v=[int(x*d) for x in r];g=gcd(*v);return tuple(x//g for x in v)
def run(input_points):
 P=[tuple(map(F,p)) for p in input_points];n=len(P)-1;assert n>=8 and all(len(p)==3 for p in P)
 B=P[:-1];A=P[-1];assert all(p[2]==0 for p in B) and A[2]>0
 edges=list(zip(B,B[1:]+B[:1]));terms=[p[0]*q[1]-p[1]*q[0] for p,q in edges];area2=sum(terms);assert area2>0
 c=tuple(sum((p[k]+q[k])*v for (p,q),v in zip(edges,terms))/(3*area2) for k in range(3));g=tuple((3*x+y)/4 for x,y in zip(c,A));X=[sub(p,g) for p in P]
 for p,q in edges:
  e=sub(q,p);assert all(cross(e,sub(b,p))[2]>=0 for b in B)
 rows=set()
 for i,j,k in combinations(range(len(P)),3):
  normal=cross(sub(X[j],X[i]),sub(X[k],X[i]))
  if not any(normal):continue
  h=dot(normal,X[i]);slack=[h-dot(normal,x) for x in X]
  if all(s<=0 for s in slack):normal=tuple(-x for x in normal);h=-h
  elif not all(s>=0 for s in slack):continue
  assert h>0;rows.add(primitive(normal+(h,)))
 raw={'H':[list(r) for r in sorted(rows)]};aa=check_A.run(raw);bb=check_B.run(raw);assert aa==bb
 assert (aa['V'],aa['E'],aa['F'])==(n+1,2*n,n+1);assert {tuple(map(F,x)) for x in aa['raw_vertices']}==set(X)
 assert all(F(v)==0 for v in aa['raw_centroid']);mm=centred_mass.run(aa)
 # Geometric universal-base-vertex lemma checked directly at this exact state.
 root=max(range(n),key=lambda i:dot(X[i],X[i]));assert all(dot(X[root],sub(x,X[root]))<0 for i,x in enumerate(X) if i!=root)
 def bits(v):q=F(v);return(abs(q.numerator).bit_length(),q.denominator.bit_length())
 sizes=[bits(v) for x in aa['raw_vertices'] for v in x]
 summary={'V':aa['V'],'E':aa['E'],'F':aa['F'],'C':2*aa['E'],'strict':aa['counts'],'weak':aa['weak'],'stable_faces':aa['stable_face_ids'],'unstable_vertices':aa['unstable_vertices'],'saddle_edges':aa['saddle_edges'],'original_base_centroid':c,'original_filled_centroid':g,'raw_centred_num_max_bits':max(p for p,q in sizes),'raw_centred_den_max_bits':max(q for p,q in sizes),'support_integer_max_bits':max(abs(v).bit_length() for r in raw['H'] for v in r),'original_unstable_base_index':root,'A_B_equal':True,'third_centred_mass':mm,'terminal':'EXACT_PYRAMID_HULL_MASS_TRUE_EDGES_AND_ALL_EQUILIBRIA_PASS'}
 return {'POINTS.json':input_points,'RAW.json':raw,'A.json':aa,'B.json':bb,'MASS.json':mm,'SUMMARY.json':summary}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input',required=True,type=Path);ap.add_argument('--out',required=True,type=Path);ap.add_argument('--expect');a=ap.parse_args();assert __debug__
 result=run(json.loads(a.input.read_bytes()));a.out.mkdir(parents=True,exist_ok=False)
 for n,o in result.items():(a.out/n).write_bytes(enc(o))
 manifest={p.name:{'bytes':len(p.read_bytes()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(a.out.glob('*.json'))};(a.out/'MANIFEST.json').write_bytes(enc(manifest))
 s=result['SUMMARY.json'];print(s['terminal'],s['V'],s['E'],s['F'],s['strict'],s['weak'],flush=True)
 if a.expect:assert s['strict']==[int(x) for x in a.expect.split(',')] and s['weak']==[0,0,0]
if __name__=='__main__':main()
