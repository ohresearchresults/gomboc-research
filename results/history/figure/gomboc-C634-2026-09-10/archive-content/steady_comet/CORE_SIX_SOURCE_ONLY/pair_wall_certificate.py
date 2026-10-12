"""Standard-library exact Bernstein/Descartes isolation of the own-centroid pair wall.
Input polynomial coefficients are deterministically produced by symbolic_pair.py.
No numerical root finder is used by this certificate.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb,lcm
import json,sys,hashlib
sys.set_int_max_str_digits(0);R=Path(__file__).parent

def bernstein_signs(a):
 n=len(a)-1;den=lcm(*(comb(n,j) for j in range(n+1)));b=[sum(a[j]*comb(k,j)*(den//comb(n,j)) for j in range(k+1)) for k in range(n+1)];return [(z>0)-(z<0) for z in b]
def variations(signs):
 s=[z for z in signs if z];return sum(x!=y for x,y in zip(s,s[1:]))
def evalp(a,x):
 y=Q(0)
 for c in a[::-1]:y=y*x+c
 return y
if __name__=='__main__':
 d=json.loads((R/'SYMBOLIC_PAIR_WALL.json').read_text());a=list(map(int,d['numerator_ascending']));b=list(map(int,d['denominator_ascending']));sa=bernstein_signs(a);sb=bernstein_signs(b);assert variations(sa)==1;assert len(set(sb))==1 and sb[0]!=0;assert evalp(a,Q(0))*evalp(a,Q(1))<0
 lo=Q(0);hi=Q(1);sg=(evalp(a,lo)>0)-(evalp(a,lo)<0)
 for _ in range(64):
  mid=(lo+hi)/2;z=evalp(a,mid)
  if (z>0)-(z<0)==sg:lo=mid
  else:hi=mid
 assert evalp(a,lo)*evalp(a,hi)<0
 out=dict(numerator_degree=len(a)-1,denominator_degree=len(b)-1,numerator_bernstein_signs=sa,denominator_bernstein_signs=sb,bernstein_variations=variations(sa),isolating_interval=[str(lo),str(hi)],root_midpoint_float=float((lo+hi)/2),wall_sign_at_zero=((evalp(a,Q(0))*evalp(b,Q(0)))>0)*2-1,wall_sign_at_one=((evalp(a,Q(1))*evalp(b,Q(1)))>0)*2-1,polynomial_sha256=hashlib.sha256((R/'SYMBOLIC_PAIR_WALL.json').read_bytes()).hexdigest())
 (R/'PAIR_WALL_CERTIFICATE.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':')));print(out);print('EXACT_UNIQUE_OWN_CENTROID_PAIR_ESCAPE_WALL_IN_0_1_PASS')
