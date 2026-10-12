"""Exact dyadic certificate for one-facet mass closure of journaled C598.
No floating arithmetic determines a pass. Requires the exact parent C602 audit,
C598 supports, and the exact FACET_CHECKPOINT_20 audit as named below.
See ONE_FACET_THEOREM.md for the geometric argument connected to these tests.
"""
import sys,json,hashlib
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
D=1<<128

def ceildiv(a,b):return -((-a)//b)
class I:
 __slots__=('lo','hi')
 def __init__(self,x=0):
  if isinstance(x,I):self.lo=x.lo;self.hi=x.hi;return
  s=str(x).split('/');n=int(s[0]);d=int(s[1]) if len(s)==2 else 1
  assert d>0;self.lo=n*D//d;self.hi=ceildiv(n*D,d)
 @classmethod
 def pair(cls,lo,hi):
  assert lo<=hi;r=cls.__new__(cls);r.lo=lo;r.hi=hi;return r
 def __add__(a,b):b=I(b);return I.pair(a.lo+b.lo,a.hi+b.hi)
 __radd__=__add__
 def __neg__(a):return I.pair(-a.hi,-a.lo)
 def __sub__(a,b):return a+-I(b)
 def __rsub__(a,b):return I(b)+-a
 def __mul__(a,b):
  b=I(b);p=[a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi];return I.pair(min(p)//D,ceildiv(max(p),D))
 __rmul__=__mul__
 def __truediv__(a,b):
  b=I(b);assert not b.lo<=0<=b.hi
  return I.pair(min(D*x//y for x in (a.lo,a.hi) for y in (b.lo,b.hi)),max(ceildiv(D*x,y) for x in (a.lo,a.hi) for y in (b.lo,b.hi)))
 def __abs__(a):return I.pair(0 if a.lo<=0<=a.hi else min(abs(a.lo),abs(a.hi)),max(abs(a.lo),abs(a.hi)))
 def gt(a,b):return a.lo>I(b).hi
 def lt(a,b):return a.hi<I(b).lo
 def interval(a):return [str(F(a.lo,D)),str(F(a.hi,D))]

def dot(a,b):return sum((x*y for x,y in zip(a,b)),I(0))
def add(a,b):return [x+y for x,y in zip(a,b)]
def sub(a,b):return [x-y for x,y in zip(a,b)]
def scale(a,s):return [x*s for x in a]
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def det(A):return dot(A[0],cross(A[1],A[2]))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main(root):
 paths=[root/'C602_A.json',root/'C598_raw.json',root/'FACET_CHECKPOINT_20'/'raw.json',root/'FACET_CHECKPOINT_20'/'A.json',root/'FACET_CHECKPOINT_20'/'B.json']
 hashes=['2426da394eda9520bd30b2b8b3e1f00d043697353bb6bc73658f5983653c11ec','1286c05904d1aee57346b1bbeb200d8998b1656b0319d2cf56b2bfbb071c3599','d10e77389f3aa0c40661761a94f525378d9f9cc5c0c5b91b077a3c867e366156','c94f962ccab4f5b00bea1f4ec508d639864fc36fb5d85784bba782b90428c49b','c94f962ccab4f5b00bea1f4ec508d639864fc36fb5d85784bba782b90428c49b']
 for p,h in zip(paths,hashes):assert sha(p)==h
 parent=json.loads(paths[0].read_text());raw=json.loads(paths[1].read_text());rnew=json.loads(paths[2].read_text());audit=json.loads(paths[3].read_text())
 assert len(raw['H'])==137 and len(rnew['H'])==137
 row=[-195174862984739,88750730014496,123423398976022,82718382259850]
 assert rnew['H']==[p if j!=114 else row for j,p in enumerate(raw['H'])]
 assert [audit[k] for k in ['V','E','F']]==[201,332,133] and audit['counts']==[5,6,9] and audit['weak']==[0,0,0]
 H=raw['H'];normals=[[I(n)/I(p[3]) for n in p[:3]] for p in H]
 m=list(map(I,parent['raw_centroid']));c=list(map(I,audit['raw_centroid']));V=I(audit['ordinary_volume']);M=scale(sub(c,m),V)
 residual=sum(map(abs,M),I(0));assert residual.lt('1/1000000000000')
 # Exact positive cones of unchanged normals certify that Q is bounded.
 cones=[(0,-1,[0,1,8]),(1,-1,[0,1,74]),(1,1,[0,1,77]),(0,1,[0,1,103]),(2,-1,[0,2,78]),(2,1,[0,8,132])]
 for ax,s,idx in cones:
  A=[H[j][:3] for j in idx];u=cross(A[1],A[2]);v=cross(A[2],A[0]);w=cross(A[0],A[1])
  # These integer computations use a separate scalar product, not rounded signs.
  d=sum(A[0][i]*u[i] for i in range(3));assert d!=0
  assert all(s*z[ax]*d>=0 for z in [u,v,w]) and 114 not in idx
 # In the preceding integer branch cross() preserves integer arithmetic.
 # Interior at m and normalization of the moving plane.
 assert all((I(1)-dot(n,m)).gt(0) for j,n in enumerate(normals) if j!=114)
 nn=list(map(I,row[:3]));off=I(row[3])-dot(nn,m);assert off.gt(0)
 a0=[z/off for z in nn];assert abs(a0[0]).gt(2) and abs(a0[0]).lt(3)
 X=[list(map(I,p)) for p in audit['raw_vertices']];fi=audit['active_input_indices'].index(114);cy=audit['faces'][fi]
 assert cy==[0,1,2,3,4,5,8,9,10,11,17,20,26,29,30,49,60,62,63,67,73,92,106,109,110,111,112,115,117,118,119,120,121,122,124,140,77,50,37,33,24,23,19,13,7,6]
 mean=[sum((X[i][k] for i in cy),I(0))/I(len(cy)) for k in range(3)]
 T=[sub(scale(add(X[i],mean),I('1/2')),m) for i in [11,140,24]]
 assert all(abs(x).lt(1) for p in T for x in p)
 for j,n in enumerate(normals):
  if j==114:continue
  assert abs(n[0]).lt(3)
  assert all((I(1)-dot(n,add(p,m))).gt('1/5') for p in T)
 e=sub(T[1],T[0]);f=sub(T[2],T[0]);area=abs(e[1]*f[2]-e[2]*f[1])/I(2);assert area.gt(0) and area.lt(1)
 S=[sum((p[k] for p in T),I(0)) for k in range(3)]
 G=[[area*(sum((p[i]*p[j] for p in T),I(0))+S[i]*S[j])/I(12) for j in range(3)] for i in range(3)]
 determinant=det(G);trace=G[0][0]+G[1][1]+G[2][2]
 assert G[0][0].gt(0) and (G[0][0]*G[1][1]-G[0][1]*G[1][0]).gt(0) and determinant.gt(0)
 lower=determinant/(trace*trace);assert lower.gt('1/40000')
 # Ball is Euclidean radius r; the containing coordinate cube has the same r.
 r=F(1,10**6);tau=3*r/(2-r);error=3*(2*tau+tau*tau);lam=(F(1,40000)-error)/(3+r)
 assert 3*tau<F(1,5) and lam>0 and lam*r>F(1,10**12)
 witnesses=[]
 for j in [9,104]:
  n=normals[j];distance=I(1)-dot(n,m);assert distance.gt(0)
  y=scale(n,distance/dot(n,n));q=add(m,y)
  slacks=[I(1)-dot(n2,q) for k,n2 in enumerate(normals) if k not in [114,j]]
  assert all(s.gt('1/100000') for s in slacks)
  moving=I(1)-dot(a0,y);assert moving.gt('1/1000') and sum(map(abs,y),I(0)).lt(2)
  witnesses.append({'face_input':j,'old_cut_slack':moving.interval(),'minimum_other_fixed_slack':min(slacks,key=lambda z:z.lo).interval()})
 assert F(1,1000)>2*r
 out={'status':'C598_ONE_FACET_CENTROID_UNIQUE_AND_NOT_MONOSTABLE_PASS','scope':'Only input support 114 varies; every other C598 support is fixed; prescribed centre is the exact original C602 filled-volume centroid. This does not exclude joint geometry changes or other target centres.','dyadic_bits':128,'radius':str(r),'moving_plane_checkpoint':row,'patch_vertex_ids':[11,140,24],'patch_shrink':'1/2','mass_residual_L1_interval':residual.interval(),'projected_area_interval':area.interval(),'gram_eigenvalue_lower_interval':lower.interval(),'uniform_Hessian_eigenvalue_lower':str(lam),'lambda_times_radius':str(lam*r),'boundedness_cones':cones,'stable_witnesses':witnesses,'input_hashes':dict(zip([str(p.relative_to(root)) for p in paths],hashes))}
 path=root/'ONE_FACET_CERTIFICATE.json';path.write_text(json.dumps(out,sort_keys=True,separators=(',',':')));print(out['status']);print('certificate',sha(path),'bytes',path.stat().st_size)
 print('numerical displays only: residual upper',float(F(residual.hi,D)),'lambda',float(lam),'lambda*r',float(lam*r))
if __name__=='__main__':main(Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent)
