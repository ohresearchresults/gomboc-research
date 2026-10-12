# material-3c85287035cb

AI research material

---

"""RECIPROCAL_SCALAR_PAIR_AND_TRUE_FOUR_ARROW_V1.
Exact recovery/verification: Python 3.11+ standard library; assertions enabled.
python -B -S reciprocal_four_arrow.py build
python -B -S reciprocal_four_arrow.py check
No external input files, random seed, or floating acceptance tests.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib, json, sys
assert __debug__
U=((-4,-4,-3),(-4,-4,4),(-4,-3,-4),(-4,4,-4),(-4,4,4),
   (4,-4,-3),(4,-4,4),(4,-3,-4),(4,4,-4),(4,8,12))
FACES=((0,1,4,3,2),(1,9,4),(3,4,9),(0,5,6,1),(1,6,9),
       (2,3,8,7),(3,9,8),(5,7,8,9,6),(0,2,7,5))
SUPPORT=(((-1,0,0),1),((-2,0,2),4),((-1,2,0),3),((0,-1,0),1),
         ((0,-2,3),5),((0,0,-1),1),((0,4,-1),5),((1,0,0),1),((0,-4,-4),7))
P0=(F(1,5),F(-1,6),F(1,7)); EPS=F(1,4000); SCALE=1<<100
EDGES=tuple(sorted({tuple(sorted((f[i],f[(i+1)%len(f)]))) for f in FACES for i in range(len(f))}))
EDGE_FACES=tuple(tuple(k for k,f in enumerate(FACES) if i in f and j in f) for i,j in EDGES)
assert len(EDGES)==17 and all(len(x)==2 for x in EDGE_FACES)

def add(x,y): return tuple(a+b for a,b in zip(x,y))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))
def scale(x,c): return tuple(c*a for a in x)
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def cross(x,y): return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])
def tr(A): return tuple(zip(*A))
def mv(A,x): return tuple(dot(r,x) for r in A)
def mm(A,B): return tuple(tuple(dot(r,c) for c in tr(B)) for r in A)
def ma(A,B): return tuple(add(r,s) for r,s in zip(A,B))
def ms(A,c): return tuple(scale(r,c) for r in A)
def det(A): return dot(A[0],cross(A[1],A[2]))
def adj(A):
 return tuple(tuple(A[(j+1)%3][(i+1)%3]*A[(j+2)%3][(i+2)%3]-A[(j+1)%3][(i+2)%3]*A[(j+2)%3][(i+1)%3] for j in range(3)) for i in range(3))
def inverse(A): return ms(adj(A),1/det(A))
def sym(x,y): return tuple(tuple((x[i]*y[j]+y[i]*x[j])/2 for j in range(3)) for i in range(3))
def arrow(Z,i,j): return sym(Z[i],sub(Z[j],Z[i]))
def leading(A): return (A[0][0],A[0][0]*A[1][1]-A[0][1]*A[1][0],det(A))
def pairing(A,B): return sum(A[i][j]*B[i][j] for i in range(3) for j in range(3))
def eye(): return tuple(tuple(F(i==j) for j in range(3)) for i in range(3))

class I:
 """Every result outward-rounded to the fixed dyadic grid, including inputs."""
 def __init__(self,a,b=None):
  a=F(a); b=F(a if b is None else b); assert a<=b
  self.lo=F((a.numerator*SCALE)//a.denominator,SCALE)
  self.hi=F(-((-b.numerator*SCALE)//b.denominator),SCALE)
 @staticmethod
 def cv(x): return x if isinstance(x,I) else I(x)
 def __add__(a,b):
  b=I.cv(b); return I(a.lo+b.lo,a.hi+b.hi)
 __radd__=__add__
 def __neg__(a): return I(-a.hi,-a.lo)
 def __sub__(a,b): return a+-I.cv(b)
 def __rsub__(a,b): return I.cv(b)+-a
 def __mul__(a,b):
  b=I.cv(b); t=(a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi); return I(min(t),max(t))
 __rmul__=__mul__
 def __truediv__(a,b):
  b=I.cv(b); assert b.lo*b.hi>0; return a*I(1/b.hi,1/b.lo)
 def __rtruediv__(a,b): return I.cv(b)/a

def geometry(p):
 h=tuple(4+dot(p,u) for u in U); Y=tuple(scale(u,1/hi) for u,hi in zip(U,h))
 D=0; J=(0,0,0); ds=[]
 for f in FACES:
  for k in range(1,len(f)-1):
   t=tuple(Y[j] for j in (f[0],f[k],f[k+1])); d=det(t); ds.append(d)
   D+=d; J=add(J,scale(add(add(t[0],t[1]),t[2]),d))
 g=scale(J,1/(4*D)); Z=tuple(sub(y,g) for y in Y)
 ns=tuple(add(a,scale(p,b)) for a,b in SUPPORT)
 hs=tuple(b-dot(n,g) for n,(a,b) in zip(ns,SUPPORT))
 q=tuple(scale(n,1/s) for n,s in zip(ns,hs))
 A=ma(arrow(Z,8,9),ms(arrow(Z,9,1),F(1,2)))
 B=ma(arrow(q,5,6),ms(arrow(q,6,2),F(2)))
 W=ma(ms(adj(A),F(1,12)),ms(B,-1))
 X=tr((Z[8],Z[9],Z[1])); Q=tr((q[5],q[6],q[2])); R=mm(tr(X),Q)
 return dict(p=p,h=h,Y=Y,ds=tuple(ds),D=D,V=D/6,g=g,Z=Z,hs=hs,q=q,A=A,B=B,W=W,X=X,Q=Q,R=R)

def exact_check(z):
 assert min(z['h']+z['ds']+z['hs'])>0 and len(z['ds'])==16
 found=set()
 for i,j,k in combinations(range(10),3):
  n=cross(sub(z['Y'][j],z['Y'][i]),sub(z['Y'][k],z['Y'][i]))
  if n==(0,0,0): continue
  s=tuple(dot(n,sub(y,z['Y'][i])) for y in z['Y'])
  if min(s)>=0 or max(s)<=0: found.add(tuple(i for i,t in enumerate(s) if t==0))
 assert found=={tuple(sorted(f)) for f in FACES}
 assert min(b-dot(a,scale(U[i],F(1,4))) for a,b in SUPPORT for i in range(10) if dot(a,scale(U[i],F(1,4)))!=b)>0
 for f,q in zip(FACES,z['q']):
  assert all(dot(q,x)==1 if i in f else dot(q,x)<1 for i,x in enumerate(z['Z']))
 assert det(z['A'])>0 and z['A'][0][0]<0
 assert min(leading(z['W']))>0 and det(z['X'])!=0 and det(z['Q'])!=0
 for A in (z['A'],z['X'],z['Q']): assert mm(A,inverse(A))==eye()
 primal=((8,9),(9,1)); dual=((5,6),(6,2))
 assert all(tuple(sorted(e)) in EDGES for e in primal)
 dual_true=tuple(EDGES[next(k for k,fh in enumerate(EDGE_FACES) if set(fh)==set(e))] for e in dual)
 assert len(set(tuple(sorted(e)) for e in primal)|set(dual_true))==4
 u=(F(1),F(2),F(4)); G=ma(sym(u,u),ms(eye(),F(1,2)))
 IX=inverse(z['X']); IQ=inverse(z['Q'])
 M=mm(mm(tr(IX),G),IX); N=mm(mm(tr(IQ),G),IQ)
 assert min(leading(M)+leading(N))>0
 assert tuple(pairing(arrow(z['Z'],i,j),M) for i,j in primal)==(F(1,2),F(7,2))
 assert tuple(pairing(arrow(z['q'],i,j),N) for i,j in dual)==(F(1,2),F(7,2))
 H=((-F(1),F(1,2),F(0)),(F(1,2),-F(1,2),F(1,4)),(F(0),F(1,4),F(0)))
 K=((-F(1),F(1,2),F(0)),(F(1,2),-F(2),F(1)),(F(0),F(1),F(0)))
 assert mm(mm(z['X'],H),tr(z['X']))==z['A']
 assert mm(mm(z['Q'],K),tr(z['Q']))==z['B']
 # Invariant certificate uses c*det(X)^2 after congruence by X^T.
 invariant=ma(ms(adj(H),det(z['X'])*det(z['X'])/12),ms(mm(mm(z['R'],K),tr(z['R'])),-1))
 assert invariant==mm(mm(tr(z['X']),z['W']),z['X'])
 assert min(leading(invariant))>0
 return dict(primal=primal,dual=dual,dual_true_edges=dual_true,
             primal_only_M=M,dual_only_N=N,separate_arrow_values=(F(1,2),F(7,2)),
             A_inertia_guards=(det(z['A']),-z['A'][0][0]),W_leading_minors=leading(z['W']),
             invariant_W=invariant,invariant_leading_minors=leading(invariant))

def box_check():
 z=geometry(tuple(I(x-EPS,x+EPS) for x in P0)); ref=geometry(P0); guards=[]
 def positive(name,x):
  x=I.cv(x); assert x.lo>0,(name,str(x.lo),str(x.hi)); guards.append((name,x.lo,x.hi))
 for key in ('h','ds','hs'):
  for k,x in enumerate(z[key]): positive(key+str(k),x)
 positive('det_A',det(z['A'])); positive('negative_A00',-z['A'][0][0])
 for k,x in enumerate(leading(z['W'])): positive('W_leading_'+str(k+1),x)
 for key in ('X','Q'):
  s=1 if det(ref[key])>0 else -1; positive('nonzero_det_'+key,s*det(z[key]))
 positive('outside_old_C9_pz',z['p'][2]-F(21,200))
 return dict(epsilon=EPS,interval_grid=SCALE,dimension=3,guards=guards,count=len(guards))

def enc(x):
 if isinstance(x,F): return str(x)
 if isinstance(x,dict): return {str(k):enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)): return [enc(v) for v in x]
 return x

def main():
 assert sys.argv[1:] in (['build'],['check'])
 z=geometry(P0); checks=exact_check(z); box=box_check()
 out=dict(name='RECIPROCAL_SCALAR_PAIR_AND_TRUE_FOUR_ARROW_V1',U=U,facets=FACES,edges=EDGES,
          support=SUPPORT,point=z,checks=checks,box=box)
 raw=(json.dumps(enc(out),sort_keys=True,separators=(',',':'))+'\n').encode()
 path=Path(__file__).with_suffix('.json')
 if sys.argv[1]=='build': path.write_bytes(raw)
 else: assert path.read_bytes()==raw
 print('TRUE_10_17_9_PROJECTIVE_HULL_OWN_COM_PASS')
 print('DISJOINT_TWO_PRIMAL_TWO_DUAL_TRUE_ARROWS_PASS')
 print('EACH_CHAIN_SEPARATELY_STRICT_FEASIBLE_HALF_SEVEN_HALVES_PASS')
 print('ADJ_A_OVER_12_MINUS_B_EXACT_POSITIVE_DEFINITE_PASS')
 print('WHOLE_PROJECTIVE_BOX_RECIPROCAL_FOUR_ARROW_OBSTRUCTION_PASS',box['count'])
 print(path.name,len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__': main()
