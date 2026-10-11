"""Complete exact fixed-complex and equilibrium-cell certificate, parameter 0<=t<=1.
Consumes only the symbolic family constructed from the two literal rational endpoint
controls by symbolic_pair.py. Polynomial signs use exact Bernstein coefficients.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from math import comb,lcm,gcd
import sympy as sp,json,pickle,time,sys,collections
sys.set_int_max_str_digits(0);R=Path(__file__).parent;start=time.time()
def say(*a):print(round(time.time()-start,2),*a,flush=True)
d=pickle.load(open(R/'SYMBOLIC_PAIR.pkl','rb'));t=d['t'];Z=sp.Poly(0,t,domain=sp.ZZ);O=sp.Poly(1,t,domain=sp.ZZ)
def integral_polys(expressions):
 ps=[sp.Poly(sp.cancel(e),t,domain=sp.QQ) for e in expressions];den=lcm(*(int(c.q) for p in ps for c in p.all_coeffs()));out=[sp.Poly(p.as_expr()*den,t,domain=sp.ZZ) for p in ps];fac=gcd(*(int(c) for p in out for c in p.all_coeffs()));return [p.exquo_ground(fac) for p in out]
def homogeneous(vec):
 den=sp.lcm([sp.fraction(sp.cancel(z))[1] for z in vec]);out=integral_polys([sp.cancel(z*den) for z in vec]+[den]);
 if out[-1].eval(0)<0:out=[-p for p in out]
 return out[:3],out[3]
def signs(p):
 if p.is_zero:return [0]
 n=p.degree();a=[int(p.nth(j)) for j in range(n+1)];D=lcm(*(comb(n,j) for j in range(n+1)));b=[sum(a[j]*comb(k,j)*(D//comb(n,j)) for j in range(k+1)) for k in range(n+1)];return [(z>0)-(z<0) for z in b]
def variations(s):
 q=[z for z in s if z];return sum(a!=b for a,b in zip(q,q[1:]))
def uniform_sign(p):
 s=signs(p);u=set(s)
 if u=={1}:return 1
 if u=={-1}:return -1
 if u=={0}:return 0
 return None
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Z)
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def add(a,b):return [x+y for x,y in zip(a,b)]
def sub(a,b):return [x-y for x,y in zip(a,b)]
def mul(p,a):return [p*x for x in a]
H=[integral_polys(h) for h in d['H']];P=[homogeneous(p) for p in d['P']];cv,cd=homogeneous([sp.cancel(x/d['V']) for x in d['M']]);say('common centroid degree',cd.degree(),'bits',max(abs(int(c)).bit_length() for c in cd.all_coeffs()))
assert uniform_sign(cd)==1
for h in H:assert uniform_sign(h[3])==1
for av,bv in P:assert uniform_sign(bv)==1
hv=[h[3]*cd-dot(h[:3],cv) for h in H];assert all(uniform_sign(v)==1 for v in hv);say('origin and true-centroid strict interior all parameters')
incidence_count=0;nonincidence_count=0
for v,(av,bv) in enumerate(P):
 for i,h in enumerate(H):
  slack=h[3]*bv-dot(h[:3],av)
  if i in d['owners'][v]:assert slack.is_zero;incidence_count+=1
  else:assert uniform_sign(slack)==1,(v,i,signs(slack));nonincidence_count+=1
say('all exact incidences and strict nonincidences',incidence_count,nonincidence_count)
faces=d['faces'];ef=collections.defaultdict(list);convex_corners=0;fan_count=0
for i,cy in enumerate(faces):
 for a,b,c in zip(cy,cy[1:]+cy[:1],cy[2:]+cy[:2]):
  A,Da=P[a];B,Db=P[b];C,Dc=P[c];e=sub(mul(Da,B),mul(Db,A));f=sub(mul(Db,C),mul(Dc,B));p=dot(H[i][:3],cross(e,f));assert uniform_sign(p)==1,(i,a,b,c,signs(p));convex_corners+=1
 for a,b in zip(cy,cy[1:]+cy[:1]):ef[tuple(sorted((a,b)))].append(i)
 for k in range(1,len(cy)-1):
  p=dot(P[cy[0]][0],cross(P[cy[k]][0],P[cy[k+1]][0]));assert uniform_sign(p)==1;fan_count+=1
assert len(P)-len(ef)+len(faces)==2 and all(len(v)==2 for v in ef.values());say('all maximal face corners and integration fans positive',convex_corners,fan_count)
# Six signed coordinate axes lie in nonnegative cones of UNCHANGED normals.
const=[i for i,h in enumerate(H) if all(v.degree()<=0 for v in h[:3])];norms={i:[int(v.eval(0)) for v in H[i][:3]] for i in const};bounded={}
def ci(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
for a,b,c in combinations(const,3):
 u=ci(norms[b],norms[c]);v=ci(norms[c],norms[a]);w=ci(norms[a],norms[b]);det=sum(x*y for x,y in zip(norms[a],u))
 if not det:continue
 for axis in range(3):
  for s in [-1,1]:
   if (axis,s) not in bounded and all(s*vec[axis]*det>=0 for vec in [u,v,w]):bounded[axis,s]=[a,b,c]
 if len(bounded)==6:break
assert len(bounded)==6;say('boundedness with fixed normals',bounded)
# Centered physical vectors Z_v/(Cden*B_v), and unscaled stable primitives.
zv=[sub(mul(cd,av),mul(bv,cv)) for av,bv in P];vertex={};facet={};poladj=[set() for _ in H];vadj=[set() for _ in P];changing=[];classes={}
for (v,w),(i,j) in sorted(ef.items()):
 poladj[i].add(j);poladj[j].add(i);vadj[v].add(w);vadj[w].add(v)
 for a,b in [(v,w),(w,v)]:
  if (a,b) not in vertex:
   aa,ba=P[a];ab,bb=P[b];e=sub(mul(ba,ab),mul(bb,aa));p=-dot(zv[a],e);vertex[a,b]=p
 for a,b in [(i,j),(j,i)]:
  if (a,b) not in facet:facet[a,b]=dot(H[a][:3],H[a][:3])*hv[b]-dot(H[a][:3],H[b][:3])*hv[a]
for kind,dd in [('vertex',vertex),('face',facet)]:
 hist=collections.Counter()
 for pair,p in sorted(dd.items()):
  sg=uniform_sign(p)
  if sg is None:
   ss=signs(p);var=variations(ss);changing.append((kind,list(pair),p.degree(),var,ss));assert var==1 and p.eval(0)*p.eval(1)<0
  else:assert sg in [-1,1];hist[sg]+=1
  classes[kind,pair]=sg
 say('primitive spectrum',kind,dict(hist),'changing',[(a,b,c,v) for a,b,c,v,_ in changing])
assert len(vertex)==len(facet)==2*len(ef)
assert len(changing)==1 and changing[0][:2]==('vertex',[169,167]),changing
# The changing numerator is a positive/negative multiple of the already isolated wall.
wall_num=sp.Poly(sp.fraction(d['wall'])[0],t,domain=sp.ZZ);gcdwall=sp.gcd(vertex[169,167],wall_num);assert gcdwall.degree()>=1
assert sp.cancel(vertex[169,167].as_expr()+d['wall']*cd.as_expr()*P[169][1].as_expr()**2*P[167][1].as_expr()/d['V'])==0

def census(right,weak=False):
 vs={pair:((1 if not right else -1) if sg is None else sg) for (kind,pair),sg in classes.items() if kind=='vertex'};ss={pair:sg for (kind,pair),sg in classes.items() if kind=='face'}
 if weak:vs[169,167]=0
 S=[i for i in range(len(H)) if min(ss[i,j] for j in poladj[i])>0];U=[v for v in range(len(P)) if min(vs[v,w] for w in vadj[v])>0];E=[list(e) for e,(i,j) in sorted(ef.items()) if min(vs[e],vs[e[::-1]],ss[i,j],ss[j,i])>0]
 SW=[i for i in range(len(H)) if min(ss[i,j] for j in poladj[i])==0];UW=[v for v in range(len(P)) if min(vs[v,w] for w in vadj[v])==0];EW=[list(e) for e,(i,j) in sorted(ef.items()) if min(vs[e],vs[e[::-1]],ss[i,j],ss[j,i])==0]
 return dict(S=S,U=U,H=E,weakS=SW,weakU=UW,weakH=EW)
left=census(False);right=census(True);at=census(False,True);assert left['S']==right['S']==[3] and left['U']==[99,169] and right['U']==[99];assert left['H']==[[167,169]] and right['H']==[];assert at['weakU']==[169] and at['weakH']==[[167,169]]
cert=json.loads((R/'PAIR_WALL_CERTIFICATE.json').read_text());out=dict(V=len(P),E=len(ef),F=len(H),incidences=incidence_count,strict_nonincidences=nonincidence_count,strict_convex_face_corners=convex_corners,positive_integration_fans=fan_count,boundedness={f'{a},{s}':v for (a,s),v in bounded.items()},primitive_count=len(vertex)+len(facet),constant_sign_primitive_count=len(vertex)+len(facet)-1,sole_changing_primitive=['vertex',169,167],wall_root=cert['isolating_interval'],root_float=cert['root_midpoint_float'],left=left,right=right,at_wall=at)
(R/'PAIR_INTERVAL_CERTIFICATE.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':')));say(out);say('EXACT_COMPLETE_FILLED_CENTROID_PAIR_DEATH_INTERVAL_PASS')
