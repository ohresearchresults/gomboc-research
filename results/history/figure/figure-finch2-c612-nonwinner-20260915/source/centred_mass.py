"""Third integration: integer tetrahedra based at the object's exact filled centroid."""
import sys,json,time,hashlib
from fractions import Fraction as F
from math import lcm
from pathlib import Path
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def run(a):
 p=[tuple(map(F,row)) for row in a['raw_vertices']];g=tuple(map(F,a['raw_centroid']));h=lcm(*(v.denominator for row in p for v in row),*(v.denominator for v in g))
 X=[tuple(int(h*(v-c)) for v,c in zip(row,g)) for row in p]
 V6=0;M24=[0,0,0];num=0
 for cy in a['faces']:
  cy=cy[2:]+cy[:2]
  for j in range(1,len(cy)-1):
   x,y,z=[X[i] for i in (cy[0],cy[j],cy[j+1])];d=dot(x,cross(y,z));assert d>0;V6+=d;num+=1
   for k in range(3):M24[k]+=d*(x[k]+y[k]+z[k])
 assert M24==[0,0,0]
 W=F(V6,6*h**3);assert W==F(a['ordinary_volume'])
 return {'status':'EXACT_CENTRED_INTEGER_TETRAHEDRA_PASS','tetrahedra':num,'common_centred_denominator_bits':h.bit_length(),'common_centred_integer_coordinate_max_bits':max(abs(v).bit_length() for row in X for v in row),'filled_first_moments':[0,0,0],'volume_agrees_with_A_and_B':True}
if __name__=='__main__':
 p=Path(sys.argv[1]);s=run(json.loads(p.read_text()));print(json.dumps(s,sort_keys=True,separators=(',',':')))
