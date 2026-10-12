"""No-cutoff exact radial superlevel bars for audit_exact.py output."""
import sys,json,math,pathlib
from audit_exact import R,dot,cross,sub,encode
sys.set_int_max_str_digits(0)
def hom(v):
 d=math.lcm(*(int(a.denominator) for a in v));n=tuple(int(a*d) for a in v);gg=math.gcd(*n,d);return tuple(a//gg for a in n),d//gg

def bars(V,edges):
 h=[hom(v) for v in V];A=[dot(n,n) for n,d in h];r=[R(a,d*d) for a,(n,d) in zip(A,h)];events=[]
 for ai,bi in edges:
  a,d=h[ai];b,f=h[bi];C=dot(a,b)
  if C*d>=A[ai]*f:level=r[ai]
  elif C*f>=A[bi]*d:level=r[bi]
  else:
   cr=cross(a,b);level=R(dot(cr,cr),A[ai]*f*f+A[bi]*d*d-2*C*d*f)
  events.append((level,ai,bi))
 events.sort(key=lambda z:(-z[0],z[1],z[2]));par=list(range(len(V)));out=[]
 def root(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 for level,ai,bi in events:
  a,b=root(ai),root(bi)
  if a==b:continue
  if (r[a],-a)<(r[b],-b):a,b=b,a
  assert r[b]>=level
  if r[b]>level:out.append(dict(root=b,edge=[ai,bi],birth=r[b],death=level,depth=1-level/r[b]))
  par[b]=a
 return sorted(out,key=lambda z:-z['depth'])
def run(path,out):
 a=json.load(open(path));X=[tuple(R(v) for v in row) for row in a['raw_vertices']];g=tuple(R(v) for v in a['centroid']);P=[sub(v,g) for v in X];Q=[]
 for f in a['active']:
  n=tuple(R(v) for v in a['raw_halfspaces'][f][:3]);h=R(a['raw_halfspaces'][f][3])-dot(n,g);Q.append(tuple(v/h for v in n))
 ef={}
 for f,cy in enumerate(a['faces']):
  for i,j in zip(cy,cy[1:]+cy[:1]):ef.setdefault(tuple(sorted((i,j))),[]).append(f)
 dp=bars(P,a['edges']);dq=bars(Q,list(ef.values()))
 assert len(dp)+1==a['counts'][1] and len(dq)+1==a['counts'][0]
 r=encode(dict(P=dp,Q=dq));pathlib.Path(out).write_text(json.dumps(r,separators=(',',':')))
 print('EXACT_BAR_COUNTS',len(dp),len(dq),'DEPTHS',[[float(v['depth']) for v in ss] for ss in [dp,dq]])
if __name__=='__main__':run(sys.argv[1],sys.argv[2])
