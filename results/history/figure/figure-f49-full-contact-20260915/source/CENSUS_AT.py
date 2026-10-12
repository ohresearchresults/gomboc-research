"""Exact all-feature census at an explicit rational interior reference point.
Consumes a completely enumerated/audited maximal face complex, not an approximate hull.
No use of Euler to infer saddle counts. Standard library only; assertions must be enabled.
"""
import json,sys
from fractions import Fraction as Q
from pathlib import Path
sys.set_int_max_str_digits(0)
assert __debug__
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def mul(t,a):return tuple(t*x for x in a)
def sign(x):return int(x>0)-int(x<0)
def run(a,r):
 g=tuple(Q(int(x),int(r['denominator'])) for x in r['numerators']);assert len(g)==3
 X=[tuple(Q(x) for x in row) for row in a['raw_vertices']]
 x=[sub(p,g) for p in X];N=[tuple(map(int,row)) for row in a['normals']];D=list(map(int,a['offsets']));fs=a['faces']
 heights=[d-dot(n,g) for n,d in zip(N,D)];assert min(heights)>0
 sf=[];sw=[];uv=[];uw=[];eh=[];ew=[];edgefaces={};fsg=[];vsg=[];esg=[]
 for f,cy in enumerate(fs):
  ss=[sign(dot(N[f],cross(x[i],sub(X[j],X[i])))) for i,j in zip(cy,cy[1:]+cy[:1])];fsg.append(ss)
  if min(ss)>0:sf.append(f)
  elif min(ss)>=0:sw.append(f)
  for i,j in zip(cy,cy[1:]+cy[:1]):edgefaces.setdefault(tuple(sorted([i,j])),[]).append(f)
 for i,p in enumerate(x):
  v,j=max((dot(p,sub(q,p)),j) for j,q in enumerate(x) if j!=i);vsg.append([j,sign(v)])
  if v<0:uv.append(i)
  elif v==0:uw.append(i)
 for (i,j),ff in sorted(edgefaces.items()):
  assert len(ff)==2
  e=sub(x[j],x[i]);ee=dot(e,e);ze=dot(x[i],e);p=sub(mul(ee,x[i]),mul(ze,e));n,m=[N[f] for f in ff];nn=dot(n,n);mm=dot(m,m);nm=dot(n,m);assert nn*mm>nm*nm
  v=[-ze,ee+ze,dot(p,sub(mul(mm,n),mul(nm,m))),dot(p,sub(mul(nn,m),mul(nm,n)))];ss=list(map(sign,v));esg.append([i,j,*ss])
  if min(ss)>0:eh.append([i,j])
  elif min(ss)>=0:ew.append([i,j])
 assert sorted(edgefaces)==[tuple(e) for e in a['edges']]
 # Independent sufficient exclusion witnesses on the physical body and its centred polar.
 polar=[mul(1/h,n) for n,h in zip(N,heights)]
 ps=[]
 for i,p in enumerate(polar):
  v,j=max((dot(p,sub(q,p)),j) for j,q in enumerate(polar) if j!=i);ps.append([j,sign(v)])
 assert [i for i,(_,s) in enumerate(ps) if s<0]==sf
 return dict(reference=r,counts=[len(sf),len(uv),len(eh)],weak=[len(sw),len(uw),len(ew)],V=len(X),E=len(edgefaces),F=len(fs),stable_faces=sf,unstable_vertices=uv,saddle_edges=eh,weak_faces=sw,weak_vertices=uw,weak_edges=ew,face_signs=fsg,vertex_max_escape_signs=vsg,edge_signs=esg,polar_max_escape_signs=ps,edge_primitive_count=4*len(edgefaces),face_primitive_zero_count=sum(z.count(0) for z in fsg),edge_primitive_zero_count=sum(z[2:].count(0) for z in esg),min_interior_height=str(min(heights)))
if __name__=='__main__':
 a=json.loads(Path(sys.argv[1]).read_text());r=json.loads(Path(sys.argv[2]).read_text());out=run(a,r);Path(sys.argv[3]).write_text(json.dumps(out,sort_keys=True,separators=(',',':')));print('EXACT_REFERENCE_ALL_FEATURES',out['V'],out['E'],out['F'],out['counts'],out['weak'],flush=True)
