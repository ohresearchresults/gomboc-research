# material-bdb5fe86802c

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

#!/usr/bin/env python3
"""Exact scalar spectral-map sharpening; Python 3.13 standard library.
Actual H5 geometry matches immutable parent minimum-0254.
No certificate atlas is recomputed or independently replayed here.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib,json
FACETS=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),(9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
EDGES=tuple(sorted({tuple(sorted((f[k],f[(k+1)%len(f)]))) for f in FACETS for k in range(len(f))}))
ARROWS=tuple(sorted(e for i,j in EDGES for e in ((i,j),(j,i))))
PAIRS=((0,0),(0,1),(0,2),(1,1),(1,2),(2,2))
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def mv(A,x):return tuple(dot(r,x) for r in A)
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def tr(A):return sum(A[i][i] for i in range(3))
def pairing(A,B):return sum(A[i][j]*B[i][j] for i in range(3) for j in range(3))
def mat(v):
 a,b,c,d,e,f=v;return((a,b,c),(b,d,e),(c,e,f))
def ident():return tuple(tuple(F(i==j) for j in range(3)) for i in range(3))
def add(A,B):return tuple(tuple(A[i][j]+B[i][j] for j in range(3)) for i in range(3))
def scale(c,A):return tuple(tuple(c*x for x in r) for r in A)
def outer(a,b):return tuple(tuple(x*y for y in b) for x in a)
def minors(A):
 a,b,c=A[0];_,d,e=A[1];_,_,f=A[2]
 return(a,a*d-b*b,a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b)
def inv(A):
 a,b,c=A[0];_,d,e=A[1];_,_,f=A[2];det=minors(A)[2];assert det>0
 B=scale(1/det,((d*f-e*e,c*e-b*f,b*e-c*d),(c*e-b*f,a*f-c*c,b*c-a*e),(b*e-c*d,b*c-a*e,a*d-b*b)))
 assert mm(A,B)==ident();return B
def vertices(theta):
 x,r,p,q,la=theta;s=1-la
 return((s/4,0,0),(s*(1-3*x/4),0,0),(s*(1-p),s*p,0),(s*q,s*(1-q),0),(0,s*(1-3*r/4),0),(0,s/4,0),(s/16,s/16,0),(0,0,1),(la,0,1),(0,la,1))
def moments(Z):
 D=F(0);K=[F(0)]*3;J=[[F(0)]*3 for _ in range(3)]
 for f in FACETS:
  for k in range(1,len(f)-1):
   a,b,c=(Z[i] for i in(f[0],f[k],f[k+1]));d=dot(a,cross(b,c));u=tuple(a[i]+b[i]+c[i] for i in range(3));D+=d
   for i in range(3):
    K[i]+=d*u[i]/4
    for j in range(3):J[i][j]+=d*(u[i]*u[j]+a[i]*a[j]+b[i]*b[j]+c[i]*c[j])/20
 assert D>0;g=tuple(x/D for x in K);S=tuple(tuple(J[i][j]/D-g[i]*g[j] for j in range(3)) for i in range(3));assert min(minors(S))>0
 return D/6,g,S
def arrows(Z,g):
 out=[]
 for i,j in ARROWS:
  a=sub(Z[i],g);e=sub(Z[j],Z[i]);out.append(scale(F(1,2),add(outer(a,e),outer(e,a))))
 return tuple(out)
def supports(Z,g):
 poles=[]
 for f in FACETS:
  a,b,c=(Z[i] for i in f[:3]);n=cross(sub(b,a),sub(c,a));h=dot(n,a)
  assert n!=(0,0,0) and all(dot(n,Z[i])==h if i in f else dot(n,Z[i])<h for i in range(10))
  h-=dot(n,g);assert h>0;poles.append(tuple(x/h for x in n))
 return tuple(poles)
def census(Z,g,M):
 Q=supports(Z,g);N=inv(M);A=arrows(Z,g);pp={e:pairing(M,a) for e,a in zip(ARROWS,A)}
 EF=tuple(tuple(k for k,f in enumerate(FACETS) if i in f and j in f) for i,j in EDGES)
 DUAL=tuple(sorted(e for i,j in EF for e in((i,j),(j,i))))
 dd={(i,j):dot(Q[i],mv(N,sub(Q[j],Q[i]))) for i,j in DUAL}
 uu=tuple(i for i in range(10) if all(pp[i,j]<0 for a,j in ARROWS if a==i));ss=tuple(i for i in range(9) if all(dd[i,j]<0 for a,j in DUAL if a==i))
 hh=tuple(e for e,(i,j) in zip(EDGES,EF) if max(pp[e],pp[e[::-1]],dd[i,j],dd[j,i])<0)
 assert len(ss)+len(uu)-len(hh)==2
 return {'S':ss,'U':uu,'H':hh,'primal':[(i,j,pp[i,j]) for i,j in ARROWS],'polar':[(i,j,dd[i,j]) for i,j in DUAL],'zero_primitives':sum(x==0 for x in tuple(pp.values())+tuple(dd.values()))}
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return{str(k):enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return[enc(v) for v in x]
 return x

def main():
 p=F(7024915,10**6);q=F(6832329,10**6);D=p*q+q+1;alpha=1/(D-3);floor=1/D;ceiling=p*q/D;middle=q/D
 assert floor+middle+ceiling==1 and 0<floor<F(1,3)<ceiling<1 and alpha/(1+3*alpha)==floor
 oldalpha=F(1,144);oldfloor=oldalpha/(1+3*oldalpha);assert oldfloor==F(1,147)
 assert 1/(2*F(73)+1)==oldfloor and F(1,94)/(1+3*F(1,94))==F(1,97)
 gain=F(48,49)/F(3,49*97);assert gain==1552 and gain/2**33>F(1,2**23)
 # Optimality counterexamples for each strict increase of the scalar alpha:
 # rank-one P, then a rational positive definite perturbation, at the extremal H.
 sharp=[]
 H=((floor,0,0),(0,middle,0),(0,0,ceiling))
 for eps in (F(1,100),F(1,10000),F(1,10**8)):
  a=alpha+eps;ell=a/(1+3*a);gap=ell-floor;assert gap>0
  delta=gap/(2*(1+3*ell));P=((F(1),0,0),(0,delta,0),(0,0,delta));T=add(P,scale(-ell*tr(P),ident()))
  assert add(T,scale(a*tr(T),ident()))==P and min(minors(P))>0 and pairing(H,T)<0
  sharp.append({'alpha':a,'delta':delta,'H':H,'T':T,'P':P,'pairing':pairing(H,T)})
 theta=tuple(map(F,('13/20','3/4','4/5','1/10','3/10')));Z=vertices(theta);V,g,S=moments(Z);SI=inv(S);AA=arrows(Z,g);supports(Z,g)
 packet=(((7,0),31),((8,7),24),((9,4),45));Q=tuple(tuple(-sum(w*AA[ARROWS.index(e)][i][j] for e,w in packet) for j in range(3)) for i in range(3));t=pairing(SI,Q)
 maps={'parent_1_144':oldalpha,'condition48_optimal':F(1,94),'finite_height_optimal':alpha}
 certs={}
 for name,a in maps.items():
  P=add(Q,scale(a*t,S));assert min(minors(P))>0
  certs[name]={'alpha':a,'P':P,'leading_minors':minors(P),'effective_floor':a/(1+3*a)}
 M=mat(tuple(F(x,10000) for x in(4,17,1,9993,26,4)));cc=census(Z,g,M);assert(len(cc['S']),len(cc['U']),len(cc['H']),cc['zero_primitives'])==(3,2,3,0)
 assert all(pairing(M,AA[ARROWS.index(e)])>0 for e,w in packet)
 # A new literal actual body, not an alias of the parent's lambda=3/10 body.
 theta2=tuple(map(F,('13/20','3/4','4/5','1/10','273/1000')));Z2=vertices(theta2);V2,g2,S2=moments(Z2);A2=arrows(Z2,g2);SI2=inv(S2)
 Q2=tuple(tuple(-sum(w*A2[ARROWS.index(e)][i][j] for e,w in packet) for j in range(3)) for i in range(3));t2=pairing(SI2,Q2);map2={}
 for name,a in maps.items():
  P2=add(Q2,scale(a*t2,S2));mm2=minors(P2)
  if name=='finite_height_optimal':assert min(mm2)>0
  else:assert mm2[1]<0 and mm2[2]<0
  map2[name]={'alpha':a,'P':P2,'leading_minors':mm2}
 cc2=census(Z2,g2,M);assert(len(cc2['S']),len(cc2['U']),len(cc2['H']),cc2['zero_primitives'])==(3,2,3,0)
 assert all(pairing(M,A2[ARROWS.index(e)])>0 for e,w in packet)
 newcontrol={'theta':theta2,'vertices':Z2,'volume':V2,'centroid':g2,'covariance':S2,'Q':Q2,'trace':t2,'packet':packet,'maps':map2,'M':M,'census':cc2,'scope':'New actual 323 weak000 body: this fixed weighted stress passes the optimal finite-height scalar map but fails both older scalar maps. Not an all-packet or whole-shape exclusion.'}
 out={'identity':'OPTIMAL_COVARIANCE_TRACE_FLOOR_MAP_AND_CAP73_V1' ,'p':p,'q':q,'D':D,'alpha_star':alpha,'relative_alpha_gain':alpha/oldalpha,'spectral_floor':floor,'spectral_middle':middle,'spectral_ceiling':ceiling,'parent_reinterpretation_cap':73,'parent_margin_factor':gain,'derived_uniform_margin':F(1,2**23),'scope':'Cap73 regional statement uses the accepted parent atlas, not a replay. These finite checks support the analytic optimal map proof, not a global H5 exclusion.','new_actual_separating_control':newcontrol,'strict_scalar_optimality_controls':sharp,'actual_control':{'theta':theta,'vertices':Z,'volume':V,'centroid':g,'covariance':S,'Q':Q,'trace':t,'packet':packet,'maps':certs,'M':M,'census':cc},'status':'PASS'}
 raw=(json.dumps(enc(out),sort_keys=True,indent=2)+'\n').encode();Path('spectral_floor_report.json').write_bytes(raw)
 print('spectral_floor_report.json',len(raw),hashlib.sha256(raw).hexdigest());print('OPTIMAL_COVARIANCE_TRACE_FLOOR_MAP_AND_CAP73_V1_PASS')
if __name__=='__main__':main()
