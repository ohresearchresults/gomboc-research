# material-704991b0d29b

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""J74 exact computational core. Input literal L18 from accepted R22 payload.
Fractions establish actual support complex, own mass and equilibrium census;
SciPy proposes supporting triples only. No numeric tolerance certifies signs.
"""
from fractions import Fraction as F
from itertools import combinations
from functools import reduce
from math import gcd,lcm
import json,sys
import numpy as np
from scipy.spatial import ConvexHull
if hasattr(sys,'set_int_max_str_digits'): sys.set_int_max_str_digits(0)
TEXT='''
-114525,0,2815;-114408,0,-21012;-110220,0,-38817;-102074,0,-55623;-95244,0,65065
-93745,0,-67376;-84871,0,89483;-83812,0,-77505;-76508,0,-83525;-64581,0,-90582
-61476,25894,-14839;-62395,23368,463;-56261,23741,8340;-52412,0,-95480;-51315,23453,14016
-52494,34497,-19706;-42771,21590,23057;-42863,2890,42398;-41427,18386,27657;-41360,12530,33866
-41047,44227,-22695;-39278,42001,-8155;-34778,0,-100114;-33227,5517,41437;-34030,41543,3065
-32655,47126,-31146;-27505,0,-101349;-26092,6359,40643;-29349,-3094,46727;-23601,48813,-36091
-20202,0,-101916;-22835,44187,7116;-19759,39126,14237;-15413,37019,17653;-12669,0,-101808
-11758,47157,-43142;-9937,36825,18784;-5171,0,-100970;-4354,45931,-43781;-656,39016,17643
-285,7861,35467;2454,-27623,-99473;1609,5616,35659;7524,7250,33248;9975,-29293,-97278
8760,16281,29866;12615,42039,15586;23787,44736,-31885;17334,-30836,-94391;30460,-17220,-87918
24468,-32254,-90824;38470,40587,-9618;31322,-33549,-86591;29555,47228,10455;33038,0,-80951
37731,-34969,-81714;36888,40349,12838;41804,34722,13816;43728,-36211,-76251;41605,0,-68494
44676,31334,13390;47360,27874,12796;49134,-37619,-70267;49897,24291,12029;52973,-47543,-55156
53765,-8364,-59155;55076,17110,8707;59503,9479,4527;58901,-42244,-45006;63005,1560,-490
63029,-35973,-35698;65329,-6139,-5970;66608,-13854,-12187;65610,-28928,-27007;66746,-21494,-19185
'''
PATCH=[0,1,2,3,4,5,6,7,8,9,13,22,26,30,34,37,54,59]
PRIMARY=[13,22,14,16,24]
ZERO=(F(0),)*3
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
mul=lambda a,s:tuple(x*s for x in a)
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def parent_points():
 rows=[list(map(int,r.split(','))) for r in TEXT.replace('\n',';').split(';') if r.strip()]
 assert len(rows)==75
 p=[tuple(F(t,100000) for t in r) for r in rows]
 for i in PATCH:
  x,_,z=p[i];p[i]=(x,(-F(68526367,100000)-272*x-409*z)/1000,z)
 return p

def polygon(ids,p,n):
 drop=max(range(3),key=lambda k:abs(n[k]));u,v=[k for k in range(3) if k!=drop]
 ids=sorted(ids,key=lambda i:(p[i][u],p[i][v]))
 def turn(i,j,k):return (p[j][u]-p[i][u])*(p[k][v]-p[i][v])-(p[j][v]-p[i][v])*(p[k][u]-p[i][u])
 def half(seq):
  out=[]
  for i in seq:
   while len(out)>1 and turn(out[-2],out[-1],i)<=0:out.pop()
   out.append(i)
  return out
 f=half(ids)[:-1]+half(reversed(ids))[:-1]
 assert len(f)>=3
 if dot(cross(sub(p[f[1]],p[f[0]]),sub(p[f[2]],p[f[0]])),n)<0:f.reverse()
 k=f.index(min(f));return f[k:]+f[:k]

def hull(points):
 p=list(dict.fromkeys(tuple(F(x) for x in q) for q in points));D=lcm(*(x.denominator for q in p for x in q));z=[tuple(int(x*D) for x in q) for q in p];planes=set()
 for ids in ConvexHull(np.array(p,dtype=float)).simplices:
  i,j,k=map(int,ids);n=cross(sub(z[j],z[i]),sub(z[k],z[i]))
  if not any(n):continue
  h=dot(n,z[i]);ss=[dot(n,q)-h for q in z]
  if min(ss)<0<max(ss) or min(ss)==max(ss):continue
  a=tuple(n)+(h,)
  if max(ss)>0:a=tuple(-x for x in a)
  g=reduce(gcd,(abs(x) for x in a),0);planes.add(tuple(x//g for x in a))
 assert len(planes)>=4
 faces=[polygon([i for i,q in enumerate(z) if dot(a[:3],q)==a[3]],z,a[:3]) for a in sorted(planes)]
 keep=sorted({i for f in faces for i in f});remap={i:j for j,i in enumerate(keep)};faces=[[remap[i] for i in f] for f in faces]
 owners={};directions={}
 for fi,f in enumerate(faces):
  for i,j in zip(f,f[1:]+f[:1]):
   e=tuple(sorted((i,j)));owners.setdefault(e,[]).append(fi);directions.setdefault(e,[]).append(i<j)
 edges=sorted(owners)
 assert all(len(owners[e])==2 and directions[e][0]!=directions[e][1] for e in edges),'Unclosed nomination, not a hull certificate'
 adj=[set() for f in faces]
 for e in edges:
  a,b=owners[e];adj[a].add(b);adj[b].add(a)
 reach={0};todo=[0]
 while todo:
  for j in adj[todo.pop()]:
   if j not in reach:reach.add(j);todo.append(j)
 assert len(reach)==len(faces) and len(keep)-len(edges)+len(faces)==2
 return dict(points=[p[i] for i in keep],material=keep,faces=faces,edges=edges,owners=[owners[e] for e in edges])

def triangles(faces):
 for f in faces:
  for j in range(1,len(f)-1):yield (f[0],f[j],f[j+1])
def mass(p,faces,o=ZERO,positive=False):
 V=F(0);M=ZERO
 for ids in triangles(faces):
  a,b,c=[p[i] for i in ids];w=det(sub(a,o),sub(b,o),sub(c,o))/6
  if positive:assert w>0
  V+=w;M=add(M,mul(add(add(o,a),add(b,c)),w/4))
 return V,M

def mechanics(K):
 p=K['points'];faces=K['faces'];edges=K['edges'];V,M=mass(p,faces);assert V>0
 o=tuple(sum(q[k] for q in p)/len(p) for k in range(3));assert mass(p,faces,o,True)==(V,M)
 c=mul(M,1/V);x=[sub(q,c) for q in p];normals=[cross(sub(x[f[1]],x[f[0]]),sub(x[f[2]],x[f[0]])) for f in faces]
 strict=[[],[],[]];weak=[[],[],[]];zeros=[0,0,0];nb=[set() for _ in p]
 for i,j in edges:nb[i].add(j);nb[j].add(i)
 def record(k,label,values):
  zeros[k]+=sum(a==0 for a in values)
  if all(a>0 for a in values):strict[k].append(label)
  elif all(a>=0 for a in values):weak[k].append(label)
 for fi,f in enumerate(faces):
  n=normals[fi];assert dot(n,x[f[0]])>0
  record(0,fi,[dot(cross(n,sub(x[j],x[i])),mul(x[i],-1)) for i,j in zip(f,f[1:]+f[:1])])
 for i in range(len(p)):record(1,i,[-dot(x[i],sub(x[j],x[i])) for j in sorted(nb[i])])
 for (i,j),(f,g) in zip(edges,K['owners']):
  d=sub(x[j],x[i]);dd=dot(d,d);t=-dot(x[i],d);R=add(mul(x[i],dd),mul(d,t));a,b=normals[f],normals[g];aa=dot(a,a);ab=dot(a,b);bb=dot(b,b);assert aa*bb-ab*ab>0
  record(2,[i,j],[t,dd-t,bb*dot(R,a)-ab*dot(R,b),aa*dot(R,b)-ab*dot(R,a)])
 census=list(map(len,strict));assert census[0]+census[1]-census[2]==2 or any(map(len,weak))
 return dict(VEF=[len(p),len(edges),len(faces)],volume=V,moment=M,centroid=c,strict=census,weak=list(map(len,weak)),zeros=zeros,S=[faces[i] for i in strict[0]],U=strict[1],H=strict[2])

def null_plane(a):
 k=next(i for i in range(3) if a[i]!=0);out=[]
 for j in range(3):
  if j==k:continue
  v=[F(0)]*3;v[j]=F(1);v[k]=-F(a[j],a[k]);out.append(tuple(v))
 return out

def solve_columns(C,b):
 D=det(*C);assert D!=0
 return [det(*(b if j==k else C[j] for j in range(3)))/D for k in range(3)]

def star(x,faces,i):
 a=ZERO;B=[[F(0) for _ in range(3)] for _ in range(3)]
 for f in faces:
  if i not in f:continue
  assert len(f)==3
  k=f.index(i);b=x[f[(k+1)%3]];c=x[f[(k+2)%3]];w=cross(b,c);a=add(a,mul(w,F(1,6)))
  for r in range(3):
   for s in range(3):B[r][s]+=(b[r]+c[r])*w[s]/24
 tau=dot(a,x[i]);assert tau>0;D=[[B[r][s]+(tau/4 if r==s else 0) for s in range(3)] for r in range(3)]
 basis=null_plane(a);images=[tuple(dot(row,v) for row in D) for v in basis]
 return basis,images

def valid_complex(x,faces):
 for f in faces:
  n=cross(sub(x[f[1]],x[f[0]]),sub(x[f[2]],x[f[0]]));h=dot(n,x[f[0]])
  if h<=0:return False
  sf=set(f)
  for j,p in enumerate(x):
   gap=h-dot(n,p)
   if (j in sf and gap!=0) or (j not in sf and gap<=0):return False
  for i,j in zip(f,f[1:]+f[:1]):
   ni=cross(n,sub(x[j],x[i]))
   for k in f:
    if k not in (i,j) and dot(ni,sub(x[k],x[i]))<=0:return False
 return mass(x,faces)[0]>0

def moment_derivative(x,d,faces):
 out=ZERO
 for ids in triangles(faces):
  a,b,c=[x[i] for i in ids];da,db,dc=[d[i] for i in ids];w=det(a,b,c);dw=det(da,b,c)+det(a,db,c)+det(a,b,dc)
  out=add(out,mul(add(mul(add(add(a,b),c),dw),mul(add(add(da,db),dc),w)),F(1,24)))
 return out

def polar_velocity(x,d,faces):
 q=[];dq=[]
 for f in faces:
  a,b,c=[x[i] for i in f[:3]];da,db,dc=[d[i] for i in f[:3]];n=cross(sub(b,a),sub(c,a));dn=add(cross(sub(db,da),sub(c,a)),cross(sub(b,a),sub(dc,da)));h=dot(n,a);dh=dot(dn,a)+dot(n,da)
  q.append(mul(n,1/h));dq.append(mul(sub(mul(dn,h),mul(n,dh)),1/(h*h)))
 return q,dq

def depth_derivative(x,d,edge,peak):
 i,j=edge;u,v=x[i],x[j];du,dv=d[i],d[j];A=dot(u,u);B=dot(u,v);C=dot(v,v);dA=2*dot(u,du);dB=dot(du,v)+dot(u,dv);dC=2*dot(v,dv);D=A+C-2*B
 if D==0 or B>=A:g,dg=A,dA
 elif B>=C:g,dg=C,dC
 else:
  N=A*C-B*B;dN=dA*C+A*dC-2*B*dB;dD=dA+dC-2*dB;g,dg=N/D,(dN*D-N*dD)/(D*D)
 r=dot(x[peak],x[peak]);dr=2*dot(x[peak],d[peak]);return -dg/r+g*dr/(r*r)

def original_chart(K):
 V,M=mass(K['points'],K['faces']);c=mul(M,1/V);x=[sub(p,c) for p in K['points']];faces=K['faces'];big=max(faces,key=len);n=cross(sub(x[big[1]],x[big[0]]),sub(x[big[2]],x[big[0]]));axes=[tuple(F(i==j) for i in range(3)) for j in range(3)];modes=[]
 for i in PRIMARY:
  for v in (null_plane(n) if i in [13,22] else axes):
   d=[ZERO for _ in x];d[i]=v;modes.append(d)
 controls=[];images=[]
 for i in [10,23]:
  basis,im=star(x,faces,i);controls.extend((i,b) for b in basis);images.extend(im)
 sel=next(s for s in combinations(range(4),3) if det(*(images[j] for j in s))!=0);C=[images[j] for j in sel];selected=[controls[j] for j in sel];gp=[];gq=[];full=[];qe=K['owners'][K['edges'].index((6,63))];qpeak=next(i for i,f in enumerate(faces) if set(f)=={14,16,24})
 for d0 in modes:
  d=list(d0);coeff=solve_columns(C,mul(moment_derivative(x,d0,faces),-1))
  for a,(i,b) in zip(coeff,selected):d[i]=add(d[i],mul(b,a))
  assert moment_derivative(x,d,faces)==ZERO
  q,dq=polar_velocity(x,d,faces);gp.append(depth_derivative(x,d,(13,22),62));gq.append(depth_derivative(q,dq,qe,qpeak));full.append(d)
 aa=dot(gp,gp);ab=dot(gp,gq);bb=dot(gq,gq);G=aa*bb-ab*ab;assert G>0
 wa,wb=(ab-bb)/G,(ab-aa)/G;weights=[wa*p+wb*q for p,q in zip(gp,gq)];primary=[ZERO for _ in x];full_direction=[ZERO for _ in x]
 for w,d0,df in zip(weights,modes,full):
  for i in range(len(x)):primary[i]=add(primary[i],mul(d0[i],w));full_direction[i]=add(full_direction[i],mul(df[i],w))
 scale=max([F(1)]+[abs(a) for p in full_direction for a in p]);primary=[mul(p,1/scale) for p in primary]
 return x,dict(direction=primary,C=C,controls=selected,derivatives=[dot(gp,weights)/scale,dot(gq,weights)/scale],centroid=c)

def construct(x,faces,ch,t):
 y=[add(p,mul(d,t)) for p,d in zip(x,ch['direction'])];V0,M0=mass(y,faces);coeff=solve_columns(ch['C'],mul(M0,-1))
 for a,(i,b) in zip(coeff,ch['controls']):y[i]=add(y[i],mul(b,a))
 assert mass(y,faces)==(V0,ZERO)
 return y

def dump(path,value):
 from pathlib import Path
 raw=(json.dumps(value,sort_keys=True,separators=(',',':'),default=str)+'\n').encode();Path(path).write_bytes(raw)
 return raw

def convert(x):
 if isinstance(x,str):
  try:return F(x)
  except ValueError:return x
 if isinstance(x,list):return [convert(t) for t in x]
 if isinstance(x,dict):return {k:convert(v) for k,v in x.items()}
 return x

if __name__=='__main__':
 K=hull(parent_points());R=mechanics(K);assert R['VEF']==[75,204,131] and R['strict']==[2,2,2];x,ch=original_chart(K);print('ORIGINAL_CHART',list(map(float,ch['derivatives'])),flush=True)
 y=construct(x,K['faces'],ch,F(1,32));A=hull(y);R=mechanics(A);assert A['material']==[i for i in range(75) if i!=27] and R['VEF']==[74,201,129] and R['strict']==[5,2,5]
 dump('postcontact_input.json',A);dump('postcontact_report.json',R);dump('original_chart.json',ch);print('POSTCONTACT_INPUT',R['VEF'],R['strict'],list(map(float,R['centroid'])),flush=True)
