# material-a88704ccc793

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J124 finite contact cuts: nine exact useful nonwinners and a whole-interval mass obstruction

This complete delta requires BOTH previously preserved J124 common-apex recovery parts, [internal-source-reference] (SHA00c8fba78bc8ab57b0fcd23a0435582536b3551fd23a64a346626d9da850d331) and [internal-source-reference] (SHAa1480109f3e78676a2bb770d273338513fab88172438a79b7671c94efb0b39ce), plus their complete exact115.cpp dependency [internal-source-reference] (material SHAac3226f5ae6212be2bedfa4f5797dbd7fa9f4d0f1e3969c3753825a98b9ba4fc). Supply all these complete sources to a computational successor. No original sandbox is needed. The optional floating scouts require geometry121.py from the separate J124 numerical methods; exact reconstruction does not.

Save each named fenced unit below with its terminal newline. First reconstruct the six-body base using its complete capsule, then run `python replay_finite.py`. Expected terminal marker: J124_NINE_FINITE_CONTACT_EXACT_NONWINNERS_PASS. Nine individual exact audits, the whole-interval certificate and the eight mass-identity comparisons were actually executed; the newly assembled replay wrapper is not claimed as a separately observed cold replay. The exact audit is the reused J115 engine, not a second independent physics implementation. Environment Python3.13.5, C++17/GMP6.3.0; all new exact generators use Python standard-library rational arithmetic.

## Scientific result and scope

For APEX2_MATCH_G6, let a be its first exact common apex, n0=(N81+N24)/2 and T=a cross(N24-N81), oriented toward old vertex38. The cut is K_epsilon=K0 intersect{(n0+epsilon*T).x<=1}. The first additional old-vertex contact is an exact rational epsilon_* approximately .11873168072086462, at old vertex32. Until that contact the removed region is exactly the tetrahedron formed by a, old vertex38 and its two moving edge intersections. The code computes its positive volume and first moment, then the actual remaining homogeneous centroid, without a frozen-centre assumption.

Eight rational samples epsilon/epsilon_* in {1,10,100,500,900,990,999,1000}/1000 are all exact OWN strict121, additionalweak000, primitive000, one positive P and Q[]. Samples1 through999 have V165/E249/F86. At the contact, FINITE_RELAY_1000 has V164/E248/F86: adding this facet costs just ONE net true edge rather than the two-edge interior relay. Its P is approximately .1601782177012123, versus base .1601784921212976. This is geometric edge economy, not cancellation. At contact removed volume is approximately4.9463267286481e-7. The exact tetrahedral volume and centroid formula agrees with the rebuilt-hull audit at all eight samples.

The entire first interval, not merely the samples, cannot reach own110. The two original strict U, indices10 and28 in the exact base audit, survive the contact cut. Their exact common L-infinity centre chamber radius is approximately .04840394178797283. Nestedness bounds the whole-interval centre shift by delta=m_* R_infty/(V0-m_*) approximately2.6779603056601925e-7. The ratio rho_U/delta exceeds180749. Every new point lies in the old body, so the original global strict support inequalities for both retained U remain strict at every actual centre in this interval. This excludes this fixed rotating first-contact family only, not other directions, later fan cells or arbitrary common-apex changes.

A second exact contact-ended cut is reconstructed from FINITE_RELAY_1000 through the same original apex using H rows28 and76. CONTACT2/CAND0 has V164/E249/F87, own121/weak000/primitive000, P approximately .16017824549941373 and Q[]. Two extra facets have now cost only two edges relative to APEX2_MATCH_G6. The new87-facet host lies within E249 but is not own110; its P is slightly worse than the first-contact parent. Other scout contacts are numerical only: source81->85 gives165/250/87(overbudget); source85->24 gives164/248/86 with twoS. No finite-contact optimum or universal exclusion is claimed.

The optional16-sample continuation beyond the first contact is numerical exploration only. It loses S1 before eventually reaching U1; at epsilon220 and400 it has E23,S5,U1 and no numerical P. These are not promoted exact endpoints. All complete positive floating landscapes are written by rotating_scan.py, including tiny positive bars rather than an absence assertion from filtering.

## finite_relay.py
```python
"""Exact one-vertex coplanar cut and finite filled-mass response.
Run in the six-body J124 reconstruction directory. Standard-library core;
optional floating diagnostics use the preserved geometry121 search module.
"""
import json,math,sys
from pathlib import Path
from fractions import Fraction as F
from freeze_apex import build
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(s,a):return tuple(s*x for x in a)
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):enc(v)for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [enc(v)for v in x]
 return x

def data(base='APEX2_MATCH_G6',source=81,target=24,apex=0):
 obj=json.loads(Path(base+'_INPUT.json').read_text());h,A=build(obj);audit=json.loads(Path(base+'_AUDIT.json').read_text())
 assert h==Path(base+'.txt').read_bytes();rows=[tuple(map(int,l.split()))for l in h.decode().splitlines()[1:]];N=[tuple(F(x,r[3])for x in r[:3])for r in rows]
 v=[tuple(map(F,x))for x in audit['vertices']];a=tuple(A[apex]);ai=v.index(a);n0=scale(F(1,2),add(N[source],N[target]));T=cross(a,sub(N[target],N[source]));assert dot(n0,a)==1 and dot(T,a)==0
 touched=[i for i,x in enumerate(v)if dot(n0,x)==1];assert len(touched)==2 and ai in touched;bi=next(i for i in touched if i!=ai);b=v[bi]
 if dot(T,b)<0:T=scale(-1,T)
 assert dot(T,b)>0
 candidates=[((1-dot(n0,x))/dot(T,x),i)for i,x in enumerate(v)if i not in touched and dot(T,x)>0]
 limit=min(t for t,i in candidates);hits=[i for t,i in candidates if t==limit];assert limit>0
 neighbors=[e[0]if e[1]==bi else e[1]for e in audit['edges']if bi in e];assert len(neighbors)==3 and ai in neighbors;c,d=[i for i in neighbors if i!=ai]
 return dict(base=base,raw=h,rows=rows,N=N,vertices=v,a=a,ai=ai,bi=bi,c=c,d=d,n0=n0,T=T,limit=limit,hits=hits,V=F(audit['volume']),g=tuple(map(F,audit['centroid'])),audit=audit)

def at(D,eps):
 assert 0<eps<=D['limit'];n=add(D['n0'],scale(eps,D['T']));v=D['vertices'];a=D['a'];b=v[D['bi']];new=[]
 for i in (D['c'],D['d']):
  t=(dot(n,b)-1)/dot(n,sub(b,v[i]));assert 0<t<=1;new.append(add(b,scale(t,sub(v[i],b))))
 dm=abs(dot(sub(a,b),cross(sub(new[0],b),sub(new[1],b))))/6;rm=scale(F(1,4),add(add(a,b),add(*new)));vol=D['V']-dm;g=scale(1/vol,sub(scale(D['V'],D['g']),scale(dm,rm)))
 den=math.lcm(*(x.denominator for x in n));r=[int(x*den)for x in n]+[den];div=math.gcd(*r);r=[x//div for x in r];h=(str(len(D['rows'])+1)+' 0\n'+'\n'.join(' '.join(map(str,x))for x in D['rows']+[tuple(r)])+'\n').encode()
 return dict(epsilon=eps,volume=vol,centroid=g,removed_volume=dm,removed_mass_centroid=rm,new_vertices=new,normal=n),h

def main():
 D=data();report={k:D[k]for k in ['base','ai','bi','c','d','n0','T','limit','hits']};report['samples']=[]
 for k in [1,10,100,500,900,990,999,1000]:
  r,h=at(D,D['limit']*F(k,1000));name=f'FINITE_RELAY_{k:04d}';Path(name+'.txt').write_bytes(h);Path(name+'_MASS.json').write_text(json.dumps(enc(r),sort_keys=True,separators=(',',':'))+'\n');report['samples'].append(dict(name=name,ratio=F(k,1000),**r))
 Path('FINITE_RELAY_FAMILY.json').write_text(json.dumps(enc(report),sort_keys=True,separators=(',',':'))+'\n')
 print('FINITE_RELAY_EXACT_FIRST_GEOMETRIC_CONTACT',D['ai'],D['bi'],D['c'],D['d'],float(D['limit']),D['hits'])
 for r in report['samples']:print(r['name'],float(r['removed_volume']),list(map(float,r['centroid'])))
if __name__=='__main__':main()
```

## finite_relay_certificate.py
```python
"""Exact entire-first-interval retention of two old unstable equilibria.
The reconstructed cut is nested. Its removed mass is bounded by the endpoint
removed mass, and that mass lies in the old body. The resulting uniform-centre
bound lies strictly in the common exact old-U support chamber.
"""
from finite_relay import *
def main():
 D=data();r,h=at(D,D['limit']);v=D['vertices'];g=D['g'];U=D['audit']['U'];assert len(U)==2
 rho=min(-dot(sub(v[i],g),sub(w,v[i]))/sum(map(abs,sub(w,v[i])))for i in U for j,w in enumerate(v)if i!=j)
 radius=max(abs(x-y)for p in v for x,y in zip(p,g));delta=r['removed_volume']*radius/(D['V']-r['removed_volume']);assert 0<delta<rho
 assert all(dot(r['normal'],v[i])<1 for i in U)
 report=dict(scope='All epsilon in (0,first geometric contact], two original strict U persist at each actual homogeneous centre. This finite nested one-vertex cut family cannot reach own110. No exclusion beyond that first contact or other normal directions.',U=U,first_contact=D['limit'],rho_U=rho,max_origin_radius_infty=radius,max_removed_volume=r['removed_volume'],uniform_centroid_shift_bound=delta,strict_gap=rho-delta,retained_U_at_contact=True)
 Path('FINITE_RELAY_U2_INTERVAL_CERTIFICATE.json').write_text(json.dumps(enc(report),sort_keys=True,separators=(',',':'))+'\n')
 print('FINITE_RELAY_ALL_PARAMETER_U2_MASS_GATE_PASS')
if __name__=='__main__':main()
```

## contact_relay.py
```python
"""Exact contact-ended coplanar relay on a supplied exact H hull.
Every candidate is a new rational body. Floating reports nominate only.
"""
from finite_relay import *

def input_rows(path):
 ls=Path(path).read_text().splitlines();m,D=map(int,ls[0].split());assert D==0;rows=[tuple(map(int,l.split()))for l in ls[1:]];assert len(rows)==m
 return rows,[tuple(F(x,r[3])for x in r[:3])for r in rows]
def candidate(hpath,apath,apex,source,target):
 rows,N=input_rows(hpath);aud=json.loads(Path(apath).read_text());v=[tuple(map(F,p))for p in aud['vertices']];a=v[apex];n0=scale(F(1,2),add(N[source],N[target]));T=cross(a,sub(N[target],N[source]));assert dot(n0,a)==1 and dot(T,a)==0
 touch=[i for i,p in enumerate(v)if dot(n0,p)==1];assert len(touch)==2 and apex in touch;b=next(i for i in touch if i!=apex)
 if dot(T,v[b])<0:T=scale(-1,T)
 assert dot(T,v[b])>0
 events=[((1-dot(n0,p))/dot(T,p),i)for i,p in enumerate(v)if i not in touch and dot(T,p)>0];limit=min(t for t,i in events);hits=[i for t,i in events if t==limit];assert limit>0
 n=add(n0,scale(limit,T));den=math.lcm(*(x.denominator for x in n));row=[int(x*den)for x in n]+[den];g=math.gcd(*row);row=[x//g for x in row];raw=(str(len(rows)+1)+' 0\n'+'\n'.join(' '.join(map(str,r))for r in rows+[tuple(row)])+'\n').encode()
 return dict(apex=apex,source=source,target=target,retired_vertex=b,contact_vertices=hits,epsilon=limit,normal=n),raw

def run(base='FINITE_RELAY_1000',out='CONTACT2'):
 from geometry121 import describe,read_h
 rows,N=input_rows(base+'.txt');aud=json.loads(Path(base+'_AUDIT.json').read_text());v=[tuple(map(F,p))for p in aud['vertices']];g=tuple(map(F,aud['centroid']));original=json.loads(Path('APEX2_MATCH_G6_INPUT.json').read_text());_,A=build(original);records=[];out=Path(out);out.mkdir(exist_ok=True)
 for a in A:
  if tuple(a)not in v:continue
  ai=v.index(tuple(a));incident=[j for j,n in enumerate(N)if dot(n,a)==1];q=[scale(1/(1-dot(n,g)),n)for n in N]
  for source in incident:
   for target in incident:
    if source==target or dot(q[source],sub(q[target],q[source]))<=0:continue
    try:r,h=candidate(base+'.txt',base+'_AUDIT.json',ai,source,target)
    except (ValueError,AssertionError):continue
    name='CAND'+str(len(records));hp=out/(name+'.txt');hp.write_bytes(h);rep=describe(read_h(hp));r.update(name=name,report=rep);records.append(r)
    print('CONTACT_RELAY',name,source,target,rep['VEF'],len(rep['S']),len(rep['U']),[b['depth']for b in rep['P']],flush=True)
 (out/'SCAN.json').write_text(json.dumps(enc(records),sort_keys=True,separators=(',',':'))+'\n')
if __name__=='__main__':run()
```

## rotating_scan.py
```python
"""Finite 16-sample scout beyond the first contact; not an interval proof.
Floating complete landscapes are retained, including numerical tiny bars.
"""
from finite_relay import *
import numpy as np
from geometry121 import describe
def main():
 D=data();out=[]
 for eps in np.r_[0.12,0.2,0.5,1.,2.,5.,10.,20.,40.,60.,80.,100.,150.,180.,220.,400.]:
  n=np.vstack([np.array(D['N'],float),np.array(D['n0'],float)+eps*np.array(D['T'],float)]);r=describe(n);out.append(dict(epsilon=float(eps),report=r))
 Path('ROTATING_RELAY_SCAN.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
 print('ROTATING_RELAY_16_NUMERICAL_PROBES_ONLY')
if __name__=='__main__':main()
```

## replay_finite.py
```python
"""Reconstruct nine finite-contact exact nonwinners and the interval mass gate.
Requires the complete J124 six-body recovery, its exact115.cpp engine, and this
material's complete source. No floating search is needed for these nine bodies.
"""
from finite_relay import *
from finite_relay import main as generate
from finite_relay_certificate import main as certificate
from contact_relay import candidate
import subprocess,hashlib

def identity(p):
 b=Path(p).read_bytes();return [len(b),hashlib.sha256(b).hexdigest()]
def audit(name):
 with open(name+'.txt','rb')as inp,open(name+'_AUDIT.json','wb')as out,open(name+'_AUDIT.log','wb')as err:subprocess.run(['./exact115'],stdin=inp,stdout=out,stderr=err,check=True)
 a=json.loads(Path(name+'_AUDIT.json').read_text());assert a['strict']==[1,2,1]and a['weak']==[0,0,0]and a['primitive_zeros']==[0,0,0]and len(a['P'])==1 and not a['Q'];return a

def main():
 manifest=json.loads(Path('FINITE_RELAY_MANIFEST.json').read_text())
 generate();certificate()
 for k in [1,10,100,500,900,990,999,1000]:
  name=f'FINITE_RELAY_{k:04d}';a=audit(name);m=json.loads(Path(name+'_MASS.json').read_text());assert F(a['volume'])==F(m['volume'])and list(map(F,a['centroid']))==list(map(F,m['centroid']))
  assert [a[t]for t in ['V','E','F']]==([164,248,86]if k==1000 else[165,249,86])
 print('FINITE_RELAY_EIGHT_EXACT_MASS_IDENTITIES_PASS')
 old=json.loads(Path('FINITE_RELAY_1000_AUDIT.json').read_text());v=[tuple(map(F,p))for p in old['vertices']];_,A=build(json.loads(Path('APEX2_MATCH_G6_INPUT.json').read_text()));ai=v.index(tuple(A[0]));r,h=candidate('FINITE_RELAY_1000.txt','FINITE_RELAY_1000_AUDIT.json',ai,28,76)
 Path('CONTACT2').mkdir(exist_ok=True);Path('CONTACT2/CAND0.txt').write_bytes(h);a=audit('CONTACT2/CAND0');assert [a[t]for t in ['V','E','F']]==[164,249,87]
 for p,want in manifest.items():assert identity(p)==want,p
 print('J124_NINE_FINITE_CONTACT_EXACT_NONWINNERS_PASS')
if __name__=='__main__':main()
```

## FINITE_RELAY_MANIFEST.json
```json
{"CONTACT2/CAND0.txt":[3401,"6587292dcdd9d1ddbe813c07011a216c2998105b9b2fb3cba6b7cabbff7e590b"],"CONTACT2/CAND0_AUDIT.json":[142618,"d9f1d4f70a094d184e0c433e0d3767b23e5898bc9a4763540f57ca0311d3da66"],"FINITE_RELAY_0001.txt":[3207,"75901ef85a5b2be01ed50e22ae072acc571e5f1ac79fa1e5e9bf7b14ab7a06f6"],"FINITE_RELAY_0001_AUDIT.json":[143759,"7cde460535923715cf18ceb629c4278a7593d023a5b127e2e66baac04a89b4dd"],"FINITE_RELAY_0001_MASS.json":[45096,"83fe3e113e5ad84530350cd0a3476c44c6a48c05d8a5d63a3887e867d385207c"],"FINITE_RELAY_0010.txt":[3203,"c73e8a3517c66985e25b3c5531d4a4842fbbfeea7a5ebdb6f29fdb5fd9f0ce1d"],"FINITE_RELAY_0010_AUDIT.json":[143537,"f6627e17daa234c3ba574b7346bb28bd6d24eb3f1b35bdac82e1d449ff08dab3"],"FINITE_RELAY_0010_MASS.json":[44984,"f42a1db59acee23e6a531d23819b08028b86a1f99a5006a3e818efb2744b1c78"],"FINITE_RELAY_0100.txt":[3195,"f6924492b20c5f1dd1fda294785597d72000b216f317f5146f26f52f557768e9"],"FINITE_RELAY_0100_AUDIT.json":[143540,"09460f2c5e15a0d44be8c9a874d8d4097515b8b73b8f6c1b0637cf2b8e752290"],"FINITE_RELAY_0100_MASS.json":[44929,"c30d41cc532fb22039155c5f094a7b94e710f01bac2811af81f7999ba304257a"],"FINITE_RELAY_0500.txt":[3199,"7035ef8ad49ba61dc2c2ffe6ae00a8c335d41c38ecf423e2fa24a15b43720b58"],"FINITE_RELAY_0500_AUDIT.json":[143383,"64f2ed680df953cc4ca820280f0e43db48af7e157b80f8c6cf0e5cf3e4fefdd9"],"FINITE_RELAY_0500_MASS.json":[44891,"c1d7178458e186705f3b9cb34cb5ba6b426fb31dd43286ba63b18c48595abd6f"],"FINITE_RELAY_0900.txt":[3199,"2123a97a5769cd5ee777e9dc6273e417280932fe8acadfce058c9534b9c6027a"],"FINITE_RELAY_0900_AUDIT.json":[143521,"7f181f21617b690f84f83a298cf6ba17bff8b7528a124adf6cef8826ed4721b5"],"FINITE_RELAY_0900_MASS.json":[44943,"a80d055136dc8db6b7564683700fb77f646889e7c2cdbad37851fb22ac93eb6c"],"FINITE_RELAY_0990.txt":[3203,"5f23185eb8dfd02eb3b2c86c3fadec1e6b69f1c9f88a1a01288bc6791cd8159f"],"FINITE_RELAY_0990_AUDIT.json":[143651,"7ddae36ab12d55df3268a88ba4b5ca0f760c31f0dfb43778d61b1a04638ab0a7"],"FINITE_RELAY_0990_MASS.json":[45028,"56a60321de3c05dd2e90af01ba0b37549cb09bc145ceda139c9da5829a358985"],"FINITE_RELAY_0999.txt":[3207,"877463b31276b65bfaf89b118e019cefd711bea4ae668da5273668ae6b18fbb4"],"FINITE_RELAY_0999_AUDIT.json":[143610,"a1b6bfb2a24cffc192024e85bad5e2d8a0ef0260cdfcdfd7710c7342bcdb7f34"],"FINITE_RELAY_0999_MASS.json":[45038,"d1c802e8c8d3109c6de09457625e4fb766a442f97aba47a20e0de29ba13e68cd"],"FINITE_RELAY_1000.txt":[3199,"dcb5ed835a5dc9649be11cde576dab563bef3ffd5de831f844b8d273ae7314c0"],"FINITE_RELAY_1000_AUDIT.json":[141187,"1dd28fc6343ff98c4029c24c899ea798a4a19da3dd50e15007fb2c8e76841b2e"],"FINITE_RELAY_1000_MASS.json":[43844,"24f8940e0307b69925607ca271c7c9cf68c0d46536bb4847727846feddcedb1d"],"FINITE_RELAY_FAMILY.json":[359461,"1f37d9de99183d379f3eee34481ea50d872f9c4dddc98ad7a19c5f23a641d0d1"],"FINITE_RELAY_U2_INTERVAL_CERTIFICATE.json":[54438,"a4d38a4d80333f8a3807e33c87951fa8c56360a538b814ec405a34c8b541c39f"],"contact_relay.py":[2592,"283e30864ac917bdb5e2e5f2a9afb20a7583da89eba17a675f9499fbb254f0c7"],"finite_relay.py":[3580,"e947e9740aefd1c843a7ad0bd11913dcf99d88c4f1f7fff62a65f2aa252a7d8d"],"finite_relay_certificate.py":[1380,"a6d3770cb82b8b791d8e9475243ba6630ad000ec460d3698f79dd423c810e3c3"],"replay_finite.py":[1959,"22abe772c4aaa81ba4be5721b354ba6c8db782efa811b63bc9ffb0c492f7d3b7"],"rotating_scan.py":[668,"f1421ae5bd3f5a377848e6890c2aa9152b053ba13de666585b410e1af2327908"]}
```
