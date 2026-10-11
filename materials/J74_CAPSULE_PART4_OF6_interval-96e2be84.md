# material-96e2be84886d

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Exact polynomial sign certificate on a finite controller segment.
No sampling is accepted as proof. Integer Bernstein coefficients on [0,L]
certify support inequalities and witnesses excluding every other equilibrium.
"""
from math import lcm,comb,gcd
from functools import reduce
from pathlib import Path
import json,pickle,sys
FACTOR=16 if '--factor16' in sys.argv else 1
import core as c

def trim(a):
 a=list(a)
 while len(a)>1 and not a[-1]:a.pop()
 return a

def add(a,b):
 z=[0]*max(len(a),len(b))
 for i,x in enumerate(a):z[i]+=x
 for i,x in enumerate(b):z[i]+=x
 return trim(z)
def neg(a):return [-x for x in a]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 z=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):z[i+j]+=x*y
 return trim(z)
def dot(a,b):
 s=[0]
 for x,y in zip(a,b):s=add(s,mul(x,y))
 return s
def cross(a,b):return [sub(mul(a[1],b[2]),mul(a[2],b[1])),sub(mul(a[2],b[0]),mul(a[0],b[2])),sub(mul(a[0],b[1]),mul(a[1],b[0]))]
def vs(a,b):return [sub(x,y) for x,y in zip(a,b)]
def va(a,b):return [add(x,y) for x,y in zip(a,b)]
def vm(a,b):return [mul(x,b) for x in a]
def vn(a):return [neg(x) for x in a]

def primitive(p):
 g=reduce(gcd,(abs(v) for v in p),0)
 return [v//g for v in p] if g else p
def vector_primitive(p):
 g=reduce(gcd,(abs(v) for a in p for v in a),0)
 return [[v//g for v in a] for a in p] if g else p

def bern_positive(p,L):
 n=len(p)-1
 # n! is a positive common multiplier for every Bernstein coefficient.
 from math import factorial
 return all(sum(p[j]*L**j*(factorial(k)//factorial(k-j))*factorial(n-j) for j in range(k+1))>0 for k in range(n+1))

def build():
 K=c.convert(json.loads(Path('postcontact_input.json').read_text()));X=K['points'];Y=c.convert(json.loads(Path('capacity_output/mechanical_factor16_candidate.json' if FACTOR==16 else 'capacity_output/distributed_body.json').read_text()))['points'];R=c.mechanics(K);V,M=c.mass(X,K['faces']);c0=c.mul(M,1/V);d=[c.sub(y,x) for x,y in zip(X,Y)]
 receipt=c.convert(json.loads(Path('capacity_output/distributed_receipt.json').read_text()));mov=receipt['controller_indices']
 assert R['VEF']==[74,201,129] and R['strict']==[5,2,5] and R['weak']==[0,0,0]
 assert all(v==c.ZERO for i,v in enumerate(d) if i not in mov)
 assert all(sum(i in f for i in mov)<=1 for f in K['faces'])
 for i in mov:
  # Every finite movement is in its exact star volume-preserving tangent plane.
  b,ims=c.star(X,K['faces'],i);n=c.cross(*b);assert c.dot(n,d[i])==0
 assert c.mass(Y,K['faces'])==(V,c.mul(M,1-FACTOR))
 D=lcm(*(a.denominator for p in X+d+[c0] for a in p))
 raw=[[[int(p[k]*D),int(v[k]*D)] for k in range(3)] for p,v in zip(X,d)]
 # Own centre at lambda is exactly (1-FACTOR*lambda)c0 by finite star identity.
 xx=[[[int((p[k]-c0[k])*D),int((v[k]+FACTOR*c0[k])*D)] for k in range(3)] for p,v in zip(X,d)]
 faces=K['faces'];normals=[vector_primitive(cross(vs(raw[f[1]],raw[f[0]]),vs(raw[f[2]],raw[f[0]]))) for f in faces]
 groups=[]
 for fi,f in enumerate(faces):
  n=normals[fi];h=dot(n,raw[f[0]])
  groups.append(('all','height:'+str(fi),[dot(n,xx[f[0]])]))
  pp=[]
  for i,p in enumerate(raw):
   gap=sub(h,dot(n,p))
   if i in f:assert gap==[0]
   else:assert gap[0]>0;pp.append(gap)
  groups.append(('all','support:'+str(fi),pp))
  # Polygon convexity. Moving vertices are never on nontriangular facets.
  if len(f)>3:
   for i,j in zip(f,f[1:]+f[:1]):
    g=cross(n,vs(raw[j],raw[i]))
    for k in f:
     if k not in (i,j):groups.append(('all','polygon', [dot(g,vs(raw[k],raw[i]))]))
  p=[dot(cross(n,vs(xx[j],xx[i])),vn(xx[i])) for i,j in zip(f,f[1:]+f[:1])]
  desired=all(q[0]>0 for q in p)
  groups.append(('all' if desired else 'any','S:'+str(fi),p if desired else [neg(q) for q in p if q[0]<0]))
 print('POLY_FACES_BUILT',len(faces),flush=True)
 Path('interval_faces'+str(FACTOR)+'.pkl').write_bytes(pickle.dumps((K,X,xx,normals,groups)))
 return finish()

def finish():
 K,X,xx,normals,groups=pickle.loads(Path('interval_faces'+str(FACTOR)+'.pkl').read_bytes())
 nb=[set() for p in X]
 for i,j in K['edges']:nb[i].add(j);nb[j].add(i)
 for i in range(len(X)):
  p=[neg(dot(xx[i],vs(xx[j],xx[i]))) for j in sorted(nb[i])];desired=all(q[0]>0 for q in p)
  groups.append(('all' if desired else 'any','U:'+str(i),p if desired else [neg(q) for q in p if q[0]<0]))
 for ei,((i,j),(f,g)) in enumerate(zip(K['edges'],K['owners'])):
  dd=vs(xx[j],xx[i]);l=dot(dd,dd);t=neg(dot(xx[i],dd));RR=vector_primitive(va(vm(xx[i],l),vm(dd,t)));a,b=normals[f],normals[g];aa=dot(a,a);ab=dot(a,b);bb=dot(b,b)
  p=[t,sub(l,t),sub(mul(bb,dot(RR,a)),mul(ab,dot(RR,b))),sub(mul(aa,dot(RR,b)),mul(ab,dot(RR,a)))];desired=all(q[0]>0 for q in p)
  groups.append(('all' if desired else 'any','H:'+str(ei),p if desired else [neg(q) for q in p if q[0]<0]))
  groups.append(('all','Gram:'+str(ei),[sub(mul(aa,bb),mul(ab,ab))]))
 groups=[(kind,label,[primitive(p) for p in pp]) for kind,label,pp in groups]
 assert all(pp and all(p[0]>0 for p in pp) for kind,label,pp in groups)
 Path('interval_cache'+str(FACTOR)+'.pkl').write_bytes(pickle.dumps(groups))
 print('POLY_GROUPS_BUILT',len(groups),'scalar',sum(len(pp) for kind,label,pp in groups),flush=True)
 return groups

def run():
 # Pickle is a disposable accelerator generated only by this local script.
 groups=finish() if '--resume' in __import__('sys').argv else build()
 results=[]
 for L in [1,2,4,8,16,32,64,128,256,512,1024]:
  bad=[]
  for kind,label,pp in groups:
   verdict=[bern_positive(p,L) for p in pp]
   if not (all(verdict) if kind=='all' else any(verdict)):bad.append(label)
  results.append(dict(L=L,uncertified_groups=bad))
  print('BERNSTEIN_SEGMENT',L,'uncertified',len(bad),bad[:8],flush=True)
  if bad:break
 c.dump('capacity_output/interval_factor'+str(FACTOR)+'_certificate.json',dict(moment_factor=FACTOR,input_strict=[5,2,5],input_VEF=[74,201,129],groups=len(groups),scalar_polynomials=sum(len(pp) for kind,label,pp in groups),tests=results,claim='Each zero-failure interval [0,L] has the same actual own525 and no additional weak equilibria. A failed sign test is NOT an exclusion.'))

if __name__=='__main__':run()
