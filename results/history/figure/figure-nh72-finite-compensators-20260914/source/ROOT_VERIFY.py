"""Standard-library outward-dyadic interval proof of finite physical mass closure.
The isolated algebraic parameters solve all three ACTUAL first-moment equations.
The same parameter box certifies full supporting geometry and all-feature census.
"""
import json,sys,itertools
from fractions import Fraction as Q
from pathlib import Path
import BUILD
sys.set_int_max_str_digits(0)
BITS=220;SCALE=1<<BITS
class I:
 __slots__=('lo','hi')
 def __init__(self,x=0,hi=None,raw=False):
  if raw:self.lo=int(x);self.hi=int(hi);return
  if isinstance(x,I):self.lo=x.lo;self.hi=x.hi;return
  x=Q(x);self.lo=x.numerator*SCALE//x.denominator;self.hi=-((-x.numerator*SCALE)//x.denominator)
 @classmethod
 def box(cls,lo,hi):return cls(I(lo).lo,I(hi).hi,raw=True)
 def __add__(self,b):b=I(b);return I(self.lo+b.lo,self.hi+b.hi,raw=True)
 __radd__=__add__
 def __neg__(self):return I(-self.hi,-self.lo,raw=True)
 def __sub__(self,b):return self+-I(b)
 def __rsub__(self,b):return I(b)+-self
 def __mul__(self,b):
  b=I(b);v=[self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi]
  return I(min(v)//SCALE,-((-max(v))//SCALE),raw=True)
 __rmul__=__mul__
 def reciprocal(self):
  assert self.lo>0 or self.hi<0,'interval division by zero'
  return I((SCALE*SCALE)//self.hi,-((-SCALE*SCALE)//self.lo),raw=True)
 def __truediv__(self,b):return self*I(b).reciprocal()
 def __rtruediv__(self,b):return I(b)*self.reciprocal()
 def midpoint(self):return Q(self.lo+self.hi,2*SCALE)
 def absupper(self):return Q(max(abs(self.lo),abs(self.hi)),SCALE)
 def sign(self):
  if self.lo>0:return 1
  if self.hi<0:return -1
  raise AssertionError('sign not isolated')
 def data(self):return [str(Q(self.lo,SCALE)),str(Q(self.hi,SCALE))]
class AD:
 __slots__=('v','d')
 def __init__(self,x=0,d=None):
  if isinstance(x,AD):self.v=x.v;self.d=x.d;return
  self.v=I(x);self.d=[I(0),I(0),I(0)] if d is None else list(map(I,d))
 def __add__(self,b):b=AD(b);return AD(self.v+b.v,[x+y for x,y in zip(self.d,b.d)])
 __radd__=__add__
 def __neg__(self):return AD(-self.v,[-x for x in self.d])
 def __sub__(self,b):return self+-AD(b)
 def __rsub__(self,b):return AD(b)+-self
 def __mul__(self,b):b=AD(b);return AD(self.v*b.v,[x*b.v+self.v*y for x,y in zip(self.d,b.d)])
 __rmul__=__mul__
 def reciprocal(self):r=self.v.reciprocal();return AD(r,[-x*r*r for x in self.d])
 def __truediv__(self,b):return self*AD(b).reciprocal()
 def __rtruediv__(self,b):return AD(b)*self.reciprocal()

def fields(base,case,eta,dual=False):
 P,keep,faces,labels,beta=BUILD.setup(base,case);cast=AD if dual else I
 X=[tuple(cast(x) for x in p) for p in P];out=X.copy();dens=[]
 for ci,cap in enumerate(BUILD.CASES[case]['caps']):
  for i in cap['vertices']:
   den=cast(1);num=X[i]
   for k,(cc,j) in enumerate(BUILD.SELECT):
    if cc==ci:
     w=eta[k]*cast(beta[ci,i][j]);den+=w;num=BUILD.add(num,BUILD.mul(w,X[cap['boundary'][j]]))
   v=den.v if dual else den;assert v.lo>0;dens.append(v)
   out[i]=tuple(x/den for x in num)
 return out,keep,faces,labels,dens

def moments(P,faces):
 V=0;M=(0,0,0)
 for cy in faces:
  for k in range(1,len(cy)-1):
   a,b,c=[P[i] for i in (cy[0],cy[k],cy[k+1])];v=BUILD.det(a,b,c)/6
   vv=v.v if isinstance(v,AD) else v;assert vv.lo>0
   V+=v;M=BUILD.add(M,BUILD.mul(v/4,BUILD.add(BUILD.add(a,b),c)))
 return V,M

def equations(base,case,eta):
 P,keep,faces,labels,den=fields(base,case,eta,True);V,M=moments(P,faces);g=list(map(Q,base['raw_centroid']))
 return [M[i]-V*g[i] for i in range(3)]

def verify(base,case,param):
 center=[Q(v,1<<param['centre_bits']) for v in param['eta_numerators']];r=Q(1,1<<param['radius_bits']);box=[I.box(v-r,v+r) for v in center]
 assert all(x.lo+SCALE>0 for x in box)
 # Direct Krawczyk inclusion for three rational equations, not floating Newton.
 fc=equations(base,case,[AD(v) for v in center]);dx=[AD(box[i],[int(i==j) for j in range(3)]) for i in range(3)];fx=equations(base,case,dx);J=[v.d for v in fx]
 C=BUILD.inverse([[v.midpoint() for v in row] for row in J]);R=[[I(int(i==j))-sum(C[i][k]*J[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
 norm=max(sum(v.absupper() for v in row) for row in R);assert norm<Q(1,2)
 K=[-sum(C[i][j]*fc[j].v for j in range(3))+sum(R[i][j]*I.box(-r,r) for j in range(3)) for i in range(3)]
 assert all(x.lo>-(r*SCALE) and x.hi<r*SCALE for x in K),'no strict Krawczyk inclusion'
 # Exact support/planarity structure at eta0 and disjoint projective cap identity.
 BUILD.raw(base,case,[Q(0)]*3)
 P,keep,faces,labels,den=fields(base,case,box);g=list(map(Q,base['raw_centroid']));Z=[BUILD.sub(p,g) for p in P];normals=[];offsets=[];edgeowners={};adj={i:set() for i in keep};support_min=None;face_signs=[]
 for f,cy in enumerate(faces):
  a,b,c=[P[i] for i in cy[:3]];n=BUILD.cross(BUILD.sub(b,a),BUILD.sub(c,a));h=BUILD.dot(n,a);assert h.lo>0;normals.append(n);offsets.append(h)
  for i in keep:
   if i not in cy:
    gap=h-BUILD.dot(n,P[i]);assert gap.lo>0,(f,i,'support')
    support_min=gap.lo if support_min is None else min(support_min,gap.lo)
  for i,j in zip(cy,cy[1:]+cy[:1]):
   edgeowners.setdefault(tuple(sorted((i,j))),[]).append((f,i,j));adj[i].add(j);adj[j].add(i)
   for k in cy:
    if k not in (i,j):assert BUILD.dot(n,BUILD.cross(BUILD.sub(P[j],P[i]),BUILD.sub(P[k],P[i]))).lo>0
  face_signs.append([BUILD.dot(n,BUILD.cross(Z[i],BUILD.sub(P[j],P[i]))).sign() for i,j in zip(cy,cy[1:]+cy[:1])])
 assert len(keep)-len(edgeowners)+len(faces)==2
 assert all(len(v)==2 and v[0][1:]==v[1][1:][::-1] for v in edgeowners.values())
 # Rank3 at each actual vertex; no merely collinear graph nodes.
 for i in keep:
  inc=[f for f,cy in enumerate(faces) if i in cy];ok=False
  for a,b,c in itertools.combinations(inc,3):
   z=BUILD.det(normals[a],normals[b],normals[c])
   if z.lo>0 or z.hi<0:ok=True;break
  assert ok,('normal rank',i)
 stable=[f for f,s in enumerate(face_signs) if min(s)>0];unstable=[];vertex_signs={};saddles=[];edge_signs=[]
 for i in keep:
  s=[BUILD.dot(Z[i],BUILD.sub(P[j],P[i])).sign() for j in sorted(adj[i])];vertex_signs[str(i)]=s
  if max(s)<0:unstable.append(i)
 for (i,j),owners in sorted(edgeowners.items()):
  e=BUILD.sub(P[j],P[i]);ell=BUILD.dot(e,e);ze=BUILD.dot(Z[i],e);pn=BUILD.sub(BUILD.mul(ell,Z[i]),BUILD.mul(ze,e));n,m=[normals[x[0]] for x in owners];nn=BUILD.dot(n,n);mm=BUILD.dot(m,m);nm=BUILD.dot(n,m);assert (nn*mm-nm*nm).lo>0
  vals=[-ze,ell+ze,BUILD.dot(pn,BUILD.sub(BUILD.mul(mm,n),BUILD.mul(nm,m))),BUILD.dot(pn,BUILD.sub(BUILD.mul(nn,m),BUILD.mul(nm,n)))];sg=[v.sign() for v in vals];edge_signs.append([i,j,*sg])
  if min(sg)>0:saddles.append([i,j])
 V,M=moments(P,faces)
 # Complete new primal and polar root basins use all and only actual adjacencies.
 r2={i:BUILD.dot(Z[i],Z[i]) for i in keep};proot=max(keep,key=lambda i:r2[i].midpoint())
 assert all((r2[proot]-r2[i]).lo>0 for i in keep if i!=proot)
 poles=[tuple(v/(offsets[f]-BUILD.dot(normals[f],g)) for v in normals[f]) for f in range(len(faces))]
 pr2=[BUILD.dot(y,y) for y in poles];droot=max(range(len(faces)),key=lambda f:pr2[f].midpoint())
 assert all((pr2[droot]-pr2[f]).lo>0 for f in range(len(faces)) if f!=droot)
 pg={i:set() for i in keep};dg={f:set() for f in range(len(faces))};dpairs=[]
 for (i,j),owners in sorted(edgeowners.items()):
  if BUILD.dot(Z[i],BUILD.sub(P[j],P[i])).sign()>0:pg[i].add(j)
  if BUILD.dot(Z[j],BUILD.sub(P[i],P[j])).sign()>0:pg[j].add(i)
  f,h=[o[0] for o in owners];dpairs.append((f,h))
  if BUILD.dot(poles[f],BUILD.sub(poles[h],poles[f])).sign()>0:dg[f].add(h)
  if BUILD.dot(poles[h],BUILD.sub(poles[f],poles[h])).sign()>0:dg[h].add(f)
 def basin(graph,root):
  good={root}
  while True:
   new=good|{i for i,aa in graph.items() if aa&good}
   if new==good:break
   good=new
  bad=set(graph)-good
  assert all(graph[i]<=bad for i in bad)
  return sorted(good),sorted(bad)
 pgood,pbad=basin(pg,proot);dgood,dbad=basin(dg,droot)
 basins=dict(primal_root=proot,primal_root_reaching=pgood,primal_closed_unwanted=pbad,primal_boundary=[list(e) for e in sorted(edgeowners) if (e[0] in pbad)!=(e[1] in pbad)],polar_root_label=labels[droot],polar_root_reaching_labels=[labels[f] for f in dgood],polar_closed_unwanted_labels=[labels[f] for f in dbad],polar_boundary=[[labels[f],labels[h]] for f,h in dpairs if (f in dbad)!=(h in dbad)])
 ans=dict(basins=basins,status='FINITE_TWO_CAP_EXACT_CENTROID_ISOLATED_ROOT_AND_FULL_CENSUS_PASS',case=case,parameter_center=[str(v) for v in center],radius=str(r),krawczyk_displacement=[x.data() for x in K],contraction_norm_upper=str(norm),V=len(keep),E=len(edgeowners),F=len(faces),counts=[len(stable),len(unstable),len(saddles)],weak=[0,0,0],original_vertex_ids=keep,original_support_labels=labels,stable_faces=stable,unstable_vertices=unstable,saddle_edges=saddles,face_signs=face_signs,vertex_neighbor_signs=vertex_signs,edge_signs=edge_signs,edge_primitive_count=4*len(edgeowners),edge_primitive_zero_count=0,volume_interval=V.data(),moment_intervals=[v.data() for v in M],exact_root_centroid=base['raw_centroid'],root_centred_moments=['0','0','0'],min_denominator_lower=str(Q(min(v.lo for v in den),SCALE)),min_unnormalized_support_gap_lower=str(Q(support_min,SCALE)),proof='Unique real parameter root in the rational box of F_i=M_i-c0_i V=0; positive denominators; exact facet planarity by disjoint cap projectivities; all other geometric/mechanical signs certified uniformly on the whole box. Vertices indexed by original deletion-base Cartesian lex IDs.')
 print(ans['status'],case,ans['counts'],'E',ans['E'],flush=True)
 return ans
if __name__=='__main__':
 base,case,param,out=sys.argv[1:];a=json.loads(Path(base).read_text());p=json.loads(Path(param).read_text())[case];ans=verify(a,case,p);Path(out).write_text(json.dumps(ans,sort_keys=True,separators=(',',':')))
