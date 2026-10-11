"""Exact C602 endpoint-global free-chain lower bound at the parent own centroid.

For an ascending chain a_0,...,a_n, a_i dot (a_{i+1}-a_i)>0 implies
r_{i+1}/r_i > sec(theta_i) and theta_i<pi/2.  Angular triangle inequality
and strict convexity of -log(cos(theta)) imply R*cos(phi/n)**n>1.
Equal angles and equal log-radius increments prove the converse.
The rational interval tests here isolate the largest Chebyshev roots and do
not use floating point to decide any inequality.  This is a fixed-centre,
free-space statement; it does not certify a convex exposed hull or density.
"""
import json,math,sys
from fractions import Fraction as F
from pathlib import Path
from BUILD import dot,sub,mul,homogeneous,canon,encode
sys.set_int_max_str_digits(0);ROOT=Path(__file__).resolve().parent

def T(n,x):
 a,b=F(1),x
 for k in range(2,n+1):a,b=b,2*x*b-a
 return b if n else a

def bounds(A,B,C,n):
 scale=1<<80;r=math.isqrt((B*scale**2)//A);rl,rh=F(r,scale),F(r+1,scale)
 assert A*r*r<=B*scale**2<A*(r+1)**2
 q=(C*scale)//A;cl,ch=F(q,scale),F(q+1,scale)
 gamma=(min(cl/rl,cl/rh,ch/rl,ch/rh),max(cl/rl,cl/rh,ch/rl,ch/rh));assert -1<gamma[0]<gamma[1]<0
 left={4:F(71,100),5:F(81,100)}[n]
 # T4' > 0 on [0.71,1] since 2*x*x>1.  T5' > 0 on [0.81,1]
 # since 80*x^4-60*x^2+5 is positive there and increasing for x>=0.81.
 assert (2*left**2>1 if n==4 else (80*left**4-60*left**2+5>0 and left**2>F(3,8)))
 rr=[]
 for y in gamma:
  lo,hi=left,F(1);assert T(n,lo)<y<T(n,hi)
  for _ in range(85):
   mid=(lo+hi)/2
   if T(n,mid)<y:lo=mid
   else:hi=mid
  rr.append((lo,hi))
 return (rl*rr[0][0]**n,rh*rr[1][1]**n)

def main():
 p=json.loads((ROOT/'PARENT_COMPLEX.json').read_text());b=json.loads((ROOT/'BUILD_REPORT.json').read_text());X=[tuple(map(F,v)) for v in p['vertices']];g=tuple(map(F,b['old_centroid']))
 C0=math.lcm(*(v.denominator for v in g));G=tuple(int(v*C0) for v in g);hp=[homogeneous(x) for x in X];Z=[sub(mul(C0,p[:3]),mul(p[3],G)) for p in hp];q=[dot(z,z) for z in Z];j0=7;t0=hp[j0][3]
 higher=[j for j in range(len(X)) if q[j]*t0*t0>q[j0]*hp[j][3]**2];assert higher==[85,91,145,147,150]
 # A strict global supporting gap gives the geometric exterior-first-step obstruction.
 for j in range(len(X)):
  if j==j0:continue
  d=sub(mul(t0,hp[j][:3]),mul(hp[j][3],hp[j0][:3]));num=dot(Z[j0],d);den=C0*t0*t0*hp[j][3]
  assert 1000*num < -3*den
 results=[]
 for j in higher:
  tj=hp[j][3];A=q[j0]*tj*tj;B=q[j]*t0*t0;C=dot(Z[j0],Z[j])*t0*tj
  assert A>0 and B>A and C<0 and C*C<A*B
  four=bounds(A,B,C,4);five=bounds(A,B,C,5);assert four[1]<1
  if j==85:assert five[0]>1
  else:assert five[1]<1
  results.append(dict(old_target=j,four=tuple(map(str,four)),five=tuple(map(str,five)),four_float=tuple(map(float,four)),five_float=tuple(map(float,five))))
 out=dict(status='COORD_C602_ENDPOINT_GLOBAL_MINIMUM_FIVE_LINKS_PASS',source_old_vertex=7,higher_radius_old_vertices=higher,minimum_free_links_to_any_other_old_vertex=5,only_old_target_attainable_in_five_links=85,all_other_old_vertices_have_radius_not_greater=True,old_global_strict_unstable_gap_upper_bound='-3/1000',endpoint_bounds=results,scope='Old C602 own centroid held fixed; every chain must end at an old vertex. Arbitrary new final unstable roots, moved old vertices and moved centres are outside this assertion.')
 (ROOT/'MIN_LINKS_REPORT.json').write_bytes(canon(out));print(out['status'],flush=True)
 for row in results:print(row['old_target'],row['four_float'],row['five_float'])
if __name__=='__main__':main()
