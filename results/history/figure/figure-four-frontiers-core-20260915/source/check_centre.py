"""Standard-library exact verifier of the ten-guard C602 centre obstruction."""
import sys,json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def solve(rows,b):
 D=dot(rows[0],cross(rows[1],rows[2]));assert D
 cols=[cross(rows[1],rows[2]),cross(rows[2],rows[0]),cross(rows[0],rows[1])];return [sum(b[i]*cols[i][j]for i in range(3))/D for j in range(3)]
def run(z,cert):
 P=[tuple(map(F,p))for p in z['raw_vertices']];q=[tuple(F(x,h)for x in n)for n,h in zip(z['normals'],z['offsets'])];g=list(map(F,z['raw_centroid']));v=cert['bad'];assert z['counts']==[1,2,1]and z['weak']==[0,0,0];assert v in z['unstable_vertices']and P[v]!=(0,0,1)
 neigh=sorted((b if a==v else a)for a,b in z['edges']if v in [a,b]);assert neigh==[t['neighbour']for t in cert['triples']]
 GD=math.lcm(*(x.denominator for x in g));GI=[x.numerator*(GD//x.denominator)for x in g];cache={}
 def row(name):
  if name in cache:return cache[name]
  kind,i,j=name.split(':');i=int(i);j=int(j)
  if kind=='primal':n=tuple(P[j][k]-P[i][k]for k in range(3));b=dot(P[i],n)
  elif kind=='dual':
   aa=dot(q[i],q[i]);ab=dot(q[i],q[j]);n=tuple(ab*q[i][k]-aa*q[j][k]for k in range(3));b=ab-aa
  else:raise AssertionError('unsupported guard type')
  D=math.lcm(*(x.denominator for x in [*n,b]));val=sum(x.numerator*(D//x.denominator)*y for x,y in zip(n,GI))-b.numerator*(D//b.denominator)*GD;assert val<0,'guard cell must contain actual own centroid strictly'
  cache[name]=(n,b);return n,b
 receipts=[];maxbits=0
 def check_vertex(vertex,triples,upper_bound):
  nonlocal maxbits
  neigh=sorted((b if a==vertex else a)for a,b in z['edges']if vertex in [a,b])
  assert neigh==[t['neighbour']for t in triples]
  result=[]
  for t in triples:
   j=t['neighbour'];d=tuple(P[j][k]-P[vertex][k]for k in range(3));rows=[row(nm)for nm in t['guards']]
   lam=solve([[rows[k][0][r]for k in range(3)]for r in range(3)],tuple(-x for x in d));assert min(lam)>=0
   assert all(sum(lam[k]*rows[k][0][r]for k in range(3))==-d[r]for r in range(3))
   upper=dot(P[vertex],d)+sum(lam[k]*rows[k][1]for k in range(3));assert upper<upper_bound
   maxbits=max(maxbits,*[max(abs(x.numerator).bit_length(),x.denominator.bit_length())for x in [*lam,upper]])
   result.append(dict(neighbour=j,upper_decimal=float(upper),upper_floor_1e12=upper.numerator*10**12//upper.denominator,dual_weights_sha256=hashlib.sha256(json.dumps(list(map(str,lam)),separators=(',',':')).encode()).hexdigest()))
  return result
 receipts=check_vertex(v,cert['triples'],F(-3,1000));assert len(receipts)==15
 apex=cert['apex'];assert apex!=v and P[apex]==(0,0,1)
 ar=check_vertex(apex,cert['apex_triples'],F(-1,25));assert len(ar)==44 and len(cache)==10
 return dict(status='BQ13_C602_TEN_GUARD_TWO_UNSTABLE_VERTICES_EXACT_PASS',bad=v,apex=apex,guard_names=sorted(cache),bad_neighbours=[t['neighbour']for t in receipts],apex_neighbours=[t['neighbour']for t in ar],uniform_bad_upper_bound='-3/1000',uniform_apex_upper_bound='-1/25',actual_own_centroid_strictly_inside_guard_cell=True,certificate_fraction_bits=maxbits,bad_receipts=receipts,apex_receipts=ar,conclusion='Both distinct vertices are strictly unstable for every reference centre satisfying all ten closed linear guards. No strict110 reference centre in this guard cell.',scope='Fixed raw polyhedron and these ten closed linear centre guards only. No exclusion of other witness cells or physical redesign.')

if __name__=='__main__':
 p=Path(sys.argv[1]);c=json.loads(Path(sys.argv[2]).read_text());assert hashlib.sha256(p.read_bytes()).hexdigest()==c['source_audit_sha256'];z=run(json.loads(p.read_text()),c);Path(sys.argv[3]).write_text(json.dumps(z,sort_keys=True,separators=(',',':')));print(z['status'])
