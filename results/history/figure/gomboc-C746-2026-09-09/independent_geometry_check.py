import json,time,sys
from pathlib import Path
from functools import reduce
from gmpy2 import mpq,mpz,lcm,gcd
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
st=time.time();g=json.loads(Path('geometry-exact.json').read_text());raw=json.loads(Path('source/RAW.json').read_text())
X=[tuple(mpq(x)for x in p)for p in g['raw_vertices']];F=g['faces'];E=g['edges'];N=[tuple(map(mpz,n))for n in raw['I']];D=mpz(raw['D'])
assert len(X)==235 and len(F)==140 and len(E)==373
for n,cy in zip(N,F):
 vals=[D-dot(n,x)for x in X]
 assert min(vals)==0 and {i for i,v in enumerate(vals)if not v}==set(cy)
 for i,j in zip(cy,cy[1:]+cy[:1]):
  inward=cross(n,sub(X[j],X[i]));assert all(dot(inward,sub(X[k],X[i]))>0 for k in cy if k not in(i,j))
T=[(cy[0],cy[j],cy[j+1])for cy in F for j in range(1,len(cy)-1)]
vol=mpq(0);mom=[mpq(0)]*3
for i,j,k in T:
 a,b,c=X[i],X[j],X[k];v=dot(a,cross(b,c))/6;assert v>0;vol+=v
 for h in range(3):mom[h]+=v*(a[h]+b[h]+c[h])/4
center=tuple(v/vol for v in mom)
assert center==tuple(mpq(x)for x in g['raw_centroid']) and vol==mpq(g['raw_volume'])
print('Exact support and volume centroid pass',flush=True)
q=reduce(lcm,(x.denominator for p in X for x in p));q=lcm(q,*(x.denominator for x in center));P=[tuple(mpz((p[k]-center[k])*q)for k in range(3))for p in X]
U=[];S=[];H=[];weak=[]
for i,p in enumerate(P):
 z=max(dot(p,sub(w,p))for j,w in enumerate(P)if j!=i)
 if z<0:U.append(i)
 if z==0:weak.append(['vertex',i])
supports=[mpz(q*(D-dot(n,center)))for n in N]
for i,(n,h)in enumerate(zip(N,supports)):
 nn=dot(n,n);vals=[hh*nn-h*dot(m,n)for j,(m,hh)in enumerate(zip(N,supports))if j!=i]
 if min(vals)>0:S.append(i)
 if min(vals)==0:weak.append(['face',i])
for i,j in E:
 p=P[i];e=sub(P[j],p);ll=dot(e,e);t=-dot(p,e)
 if not 0<=t<=ll:continue
 foot=tuple(ll*p[k]+t*e[k]for k in range(3));z=max(dot(foot,sub(w,p))for k,w in enumerate(P)if k not in(i,j))
 if z<0 and 0<t<ll:H.append([i,j])
 elif z<=0:weak.append(['edge',i,j])
r=dict(V=len(X),E=len(E),F=len(F),C=len(X)+len(E)+len(F)-2,counts=[len(S),len(U),len(H)],stable_face_ids=S,unstable_vertices=U,saddles=H,weak=weak,centroid_matches=True,volume=float(vol),seconds=time.time()-st)
assert r['counts']==[1,1,0] and not weak
Path('independent-geometry-report.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2),flush=True)
