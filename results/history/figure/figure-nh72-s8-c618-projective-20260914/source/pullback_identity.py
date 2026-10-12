"""Exact finite verification of the bounded own-centroid pullback chart.
This is an algebraic/mass identity check, not an additional independent hull audit.
"""
from pathlib import Path
from fractions import Fraction as F
import json,sys
from endpoint import dot,det,inverse,mv,dump
from RECONSTRUCT import recover
sys.set_int_max_str_digits(0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(k,a):return tuple(k*x for x in a)
def run(out):
 a=json.loads((out/'A.json').read_text());p=json.loads((out/'INPUT.json').read_text());D=p['D'];t=tuple(F(x,D) for x in p['t']);A=[[F(x,D) for x in row] for row in p['A']];Ai=inverse(A)
 V=F(a['ordinary_volume'])/det(A);M=mul(1/det(A),mv(Ai,tuple(map(F,a['raw_first_moments']))));b=mv(Ai,tuple(map(F,a['raw_centroid'])));assert M==mul(V,b)
 delta=1-dot(t,b);assert delta>0;c=mul(1/delta,b);u=mul(delta,t)
 B=[[((1 if i==j else 0)+c[i]*t[j])/delta for j in range(3)] for i in range(3)]
 assert det(B)==1/delta**4
 assert 1-dot(u,c)==delta
 minimum=None
 for row in a['raw_vertices']:
  y=mv(Ai,tuple(map(F,row)));d=1-dot(t,y);assert d>0;x=mul(1/d,y);z=sub(x,c);q=1+dot(u,z);assert q>0
  w=mul(1/q,z);assert w==mv(B,sub(y,b));minimum=q if minimum is None else min(minimum,q)
 zM=mul(det(B),mv(B,sub(M,mul(V,b))));assert zM==(0,0,0)
 rows=recover(json.loads((Path(__file__).resolve().parent/'BASE_GENERATOR.json').read_text()))['H'];active=[row for i,row in enumerate(rows) if i!=p['delete']]
 maxL1=max(sum(abs(F(v,row[3])) for v in row[:3]) for row in active);assert maxL1<5
 result=dict(status='EXACT_OWN_CENTROID_PULLBACK_IDENTITY_PASS',vertex_identities=len(a['raw_vertices']),source_inner_cube_halfwidth='1/5',source_max_normal_L1=str(maxL1),pullback_parameter_u=list(map(str,u)),pullback_centre_c=list(map(str,c)),delta=str(delta),shifted_projective_minimum_denominator=str(minimum),shifted_centred_volume=str(V/delta**4),shifted_centred_first_moments=[0,0,0])
 dump(out/'PULLBACK_IDENTITY.json',result);print(result['status'],p['delete'],flush=True)
if __name__=='__main__':run(Path(sys.argv[1]))
