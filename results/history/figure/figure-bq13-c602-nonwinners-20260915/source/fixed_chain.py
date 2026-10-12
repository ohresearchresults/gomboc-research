"""Exact rational interval evaluation of the fixed-centre radial chain bound.
This checks free-space link feasibility only, not convex exposure or filled mass.
"""
import json,sys,math
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
def T(n,x):
 a,b=F(1),x
 for k in range(2,n+1):a,b=b,2*x*b-a
 return b if n else a

def run(z):
 P=[tuple(map(F,p))for p in z['raw_vertices']];g=list(map(F,z['raw_centroid']));u,v=7,85;assert P[v]==(0,0,1) and z['counts']==[1,2,1]
 D=math.lcm(*(x.denominator for p in P+[tuple(g)]for x in p))
 U=[x.numerator*(D//x.denominator)-c.numerator*(D//c.denominator)for x,c in zip(P[u],g)]
 V=[x.numerator*(D//x.denominator)-c.numerator*(D//c.denominator)for x,c in zip(P[v],g)]
 A=sum(x*x for x in U);B=sum(x*x for x in V);C=sum(x*y for x,y in zip(U,V));assert A>0 and B>A and C<0 and C*C<A*B
 scale=1<<100;r=math.isqrt((B*scale**2)//A);rl,rh=F(r,scale),F(r+1,scale)
 assert A*r*r<=B*scale**2<A*(r+1)**2
 t=(C*scale)//A;cl,ch=F(t,scale),F(t+1,scale)
 gamma=(min(cl/rl,cl/rh,ch/rl,ch/rh),max(cl/rl,cl/rh,ch/rl,ch/rh));assert -1<gamma[0]<gamma[1]<0
 bounds={}
 # T4 is strictly increasing on [3/4,1]; T5 on [7/8,1].
 # Both intervals lie above cos(pi/n), so these are the largest roots.
 for n,left in [(4,F(3,4)),(5,F(7,8))]:
  rr=[]
  for y in gamma:
   lo,hi=left,F(1);assert T(n,lo)<y<T(n,hi)
   for k in range(110):
    mid=(lo+hi)/2
    if T(n,mid)<y:lo=mid
    else:hi=mid
   rr.append((lo,hi))
  lower,upper=rl*rr[0][0]**n,rh*rr[1][1]**n
  bounds[n]=[lower,upper]
 assert bounds[4][1]<1<bounds[5][0]
 own=[set()for p in P]
 for i,cy in enumerate(z['faces']):
  for j in cy:own[j].add(i)
 seq=[own.index(set(t))for t in [[56,70,133],[70,133,134],[70,134,135],[16,70,135]]]
 XI=[[x.numerator*(D//x.denominator)-c.numerator*(D//c.denominator)for x,c in zip(P[j],g)]for j in seq];escape=[]
 for k,(a,b)in enumerate(zip(seq,seq[1:])):
  assert sorted([a,b])in z['edges'];d=[y-x for x,y in zip(XI[k],XI[k+1])];n=sum(x*y for x,y in zip(XI[k],d));e=sum(y*y for y in d);assert n>0
  escape.append(n*10**12//e)
 return dict(protected_three_link_route=seq,protected_route_eta_floor_1e12=escape,status='BQ13_C602_FIXED_CENTRE_MINIMUM_FIVE_FREE_LINKS_PASS' ,source_vertex=u,target_vertex=v,angle_greater_than_pi_over_2=True,R_interval=list(map(str,[rl,rh])),cos_phi_interval=list(map(str,gamma)),four_link_product_interval=list(map(str,bounds[4])),five_link_product_interval=list(map(str,bounds[5])),four_link_product_decimal=[float(x)for x in bounds[4]],five_link_product_decimal=[float(x)for x in bounds[5]],scope='Fixed endpoints and the exact current filled centroid. Four or fewer strictly radial-ascending free links are impossible; five free links are feasible. No convex-hull, contact, edge-budget or new filled-centroid preservation is asserted.')
if __name__=='__main__':
 z=run(json.loads(Path(sys.argv[1]).read_text()));Path(sys.argv[2]).write_text(json.dumps(z,sort_keys=True,separators=(',',':')));print(z['status'],z['four_link_product_decimal'],z['five_link_product_decimal'])
