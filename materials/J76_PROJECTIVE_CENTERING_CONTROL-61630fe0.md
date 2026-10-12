# material-61630fe0d8c1

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J76 — canonical projective mass centering and an exact own457 control

## Scope and literature boundary
This is an explicit research implementation and a new finite control for literal R22-B7, not a claim to have invented projective centroid fitting. External primary-source check: Ivan Izmestiev, Fitting centroids by a projective transformation, arXiv:1409.6176, submitted22 September2014. Its abstract explicitly treats one point versus a convex body and relates existence and uniqueness to the Santalo point by polar duality. The abstract was read at https://arxiv.org/abs/1409.6176; the full paper was not read. The elementary formulas and proof below were derived directly in this coordinator turn. No external paper is required to execute these sources.

For a full-dimensional compact convex K with0 interior, put D={b:1+b.x>0 for every x in K} and T_b(x)=x/(1+b.x). D is bounded, open and convex. T_b is nonsingular on K, preserves convexity and its full face lattice, and has Jacobian (1+b.x)^-4 in dimension3. Consequently
Phi(b)=Vol(T_b K)=integral_K (1+b.x)^-4 dx,
grad Phi=-4 integral_K x(1+b.x)^-5 dx=-4 M(T_b K),
Hess Phi=20 integral_K xx^T(1+b.x)^-6 dx, positive definite.
The integral diverges at any boundary point of D: at a point where the denominator vanishes, an interior solid cone supplies a lower bound proportional to integral_0^r s^2/(epsilon+C s)^4 ds, which diverges as epsilon tends to0. Thus Phi has a unique global minimizer b*, and T_b*K has its own homogeneous centroid at0. For a prescribed interior reference c of an uncentered body, first use x=p-c. Its polar supports q=n/h become q+b after projectivity. Actual residual centroid g must still be subtracted for numerical or rational endpoints, making the final polar vertices (q+b)/(1-(q+b).g). This operation does NOT preserve equilibrium class.

Positive tetrahedra at0 give a finite convex objective: each parent tetrahedral volume w0 becomes w=w0/(d0*d1*d2), where d_i=1+b.x_i. With y_i=x_i/d_i and s=sum_i y_i, the tetrahedral gradient is -w*s and Hessian w*(s*s^T+sum_i y_i*y_i^T). The complete damped Newton implementation below uses these formulas. Strict convexity is a mathematical property, not evidence that any finite floating stop is exact centering.

## Finite numerical experiment
The same exact R22-B7 input as parent figure-0566, SHA1dd2a815454fdcdf5442f539f13181506b8ecd85c884a433f8061ea92c9f08be, was used. A completed163-query sweep evaluated65 equally spaced own-centroid-to-REF_NEAR points,65 own-centroid-to-REF_ROBUST points and33 points between the two exact reference110 centres. No query produced even a one-sided numerical S1 or U1. This excludes only those evaluated candidates; it is NOT a projective-orbit exclusion, nor a joint projective-plus-affine exclusion. Persistence depths in this floating sweep have an explicit1e-12 reporting cutoff and must not be called exact zero.

At REF_ROBUST the floating b was approximately(-.5745027694333341,28.535385466314604,11.218528100339297). Its nominal own S4/U5, not110. Rounding b alone to the literal exact checkpoint below leaves a nonzero own centroid around(1.77006296825e-11,-1.32063198098e-11,1.14609151440e-11). The exact control uses this actual centroid, never0.

## Exact finite control and meaning
J76_REFERENCE110_PROJECTIVE_G8_OWN457 is the density-one hull of y=(p-REF_ROBUST)/(1+B.(p-REF_ROBUST)) for all75 exact parent points, with
B=(-57450277,2853538547,1121852810)/10^8.
All denominators are strictly positive. Exact rebuilt maximal facets have the same vertex sets as the parent, every true edge is unchanged, V75/E204/F131,C408. Exact own(S,U,H)=(4,5,7), additionalweak000, primitivezero000. Four exact positive P bars have depths approximately .641699655910196,.3762995499914819,.022447273367606897,.00002173016031957729. Three Q bars have depths .8173606024101702,.06319504720739094,.0001463095472826427. Volume is approximately .0010598557774332549, ratio to the parent .0008222936726526778; this is a projective volume ratio, NOT a retained-material fraction. A second integration using positive tetrahedra at the actual own centroid agrees exactly. This is a useful nonwinning control: even a canonical, incidence-preserving homogeneous centering of the reference110 point changes the equilibrium landscape substantially. No new own110, broad impossibility or canonical record is claimed.

## Exact dependencies, commands and receipts
Required existing material [internal-source-reference] supplies all75 parent rows, planar correction and exact hull/mass/census helpers. Save its11412B/SHAe16788d0d477fef56c4a8ac979d2b201c9691d0f6ee302939f7699209a740b82 text as J75_REFERENCE110_CAP233.py. Save the two following code fences as the named files, with one terminating LF. No sandbox, old optimizer, other J76 control files or FULL76 is required.
Executed environment CPython3.13.5, NumPy2.3.5, SciPy1.17.0, OPENBLAS_NUM_THREADS=1.
projective76.py4017B SHA6a2db60d318dd36a2ddef9239e91c4b3f6db63b64b4eb39605968d7b06d674f3.
Run OPENBLAS_NUM_THREADS=1 python projective76.py. Observed output projective76.json165913B SHA306574966290d7aebf6379111e55929ccaffbe89686b11eeb90557fb80703483 and terminal J76_PROJECTIVE_CENTERING_SWEEP_DONE 163 one_sided 0 both 0. Floating serialization may be platform-sensitive; it is not the exact endpoint definition.
projective76_exact.py3579B SHA8289232779732ba507700552d646a5a63f759a8408f7656ef5a08715b8781ba0.
Run OPENBLAS_NUM_THREADS=1 python projective76_exact.py. Observed exact output J76_PROJECTIVE_EXACT.json252926B SHA958230b4c7a5757edde915db3de8c17e5c4076f089a75dd0db30106573057172 and terminal J76_REFERENCE110_PROJECTIVE_G8_OWN457_EXACT_PASS. The report includes all literal output points, maximal facets, true edges, exact volume/centroid, complete equilibrium census and every positive rational bar, without a cutoff. Fraction serialization exceeds Python's default4300-digit safety limit, so this trusted exact source explicitly removes that limit. The first preliminary report without bars was33969B/SHA1c5504f929a3e1a081d1d25b1f636789e6859c95fd6420682cb468a91377a99a; it is superseded by the full252926B report, not a different body.

## projective76.py
```python
"""Convex homogeneous-centering section of the projective orbit.
Numerical nomination, with a finite prescribed-centre sweep; no global exclusion.
Input dependency: exact J75_REFERENCE110_CAP233.py.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import json,hashlib
from pathlib import Path
import numpy as np
import J75_REFERENCE110_CAP233 as m

def setup():
 K=m.hull(m.points());V,M=m.mass(K);g=np.array(m.mul(M,1/V),float)
 p=np.array(K['points'],float)
 tri=np.array([(f[0],f[j],f[j+1]) for f in K['faces'] for j in range(1,len(f)-1)],int)
 ns=np.array([m.cross(m.sub(K['points'][f[1]],K['points'][f[0]]),m.sub(K['points'][f[2]],K['points'][f[0]])) for f in K['faces']],float)
 return K,p,g,tri,ns

def solve(p,c,tri,b0=None):
 x=p-c;t=x[tri];w0=np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2]))/6
 assert min(w0)>0
 b=np.zeros(3) if b0 is None else b0.copy()
 if min(1+x@b)<=0:b=np.zeros(3)
 def jet(b):
  d=1+x@b
  if min(d)<=0:return None
  y=x/d[:,None];yt=y[tri];w=w0/np.prod(d[tri],axis=1);s=yt.sum(1)
  V=w.sum();grad=-(w[:,None]*s).sum(0)
  H=np.einsum('i,ij,ik->jk',w,s,s)+np.einsum('i,iaj,iak->jk',w,yt,yt)
  return V,grad,H,y,-grad/(4*V),float(min(d))
 for it in range(150):
  J=jet(b);V,gr,H,y,g,dm=J
  if np.linalg.norm(g)<3e-13*max(1,np.max(np.linalg.norm(y,axis=1))):break
  step=np.linalg.solve(H,-gr);slope=gr@step;scale=1.
  for ls in range(80):
   nb=b+scale*step;N=jet(nb)
   if N is not None and N[0]<=V+1e-4*scale*slope:break
   scale*=.5
  else:break
  if np.linalg.norm(scale*step)<1e-14*(1+np.linalg.norm(b)):break
  b=nb
 J=jet(b)
 return b,J,it

def root_data(x,edges):
 nb=[[] for _ in x]
 for i,j in edges:nb[i].append(j);nb[j].append(i)
 scores=[max(float(x[i]@(x[j]-x[i]))/(np.linalg.norm(x[i])*np.linalg.norm(x[j]-x[i])) for j in js) for i,js in enumerate(nb)]
 return [i for i,v in enumerate(scores) if v<0],min(abs(v) for v in scores)

def depths(x,edges):
 edges=np.array(edges,int);u=x[edges[:,0]];v=x[edges[:,1]];d=v-u
 t=np.clip(-np.einsum('ij,ij->i',u,d)/np.einsum('ij,ij->i',d,d),0,1)
 r=u+t[:,None]*d;w=np.einsum('ij,ij->i',r,r);birth=np.einsum('ij,ij->i',x,x)
 parent=list(range(len(x)));peak=parent.copy();out=[]
 def find(i):
  while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
  return i
 for k in np.argsort(-w,kind='stable'):
  i,j=edges[k];a,b=find(int(i)),find(int(j))
  if a==b:continue
  if birth[peak[a]]<birth[peak[b]]:a,b=b,a
  dep=1-w[k]/birth[peak[b]]
  if dep>1e-12:out.append(float(dep))
  parent[b]=a
 return sorted(out,reverse=True)

def main():
 K,p,g,tri,ns=setup();out=[]
 near=np.array(m.REF_NEAR,float);robust=np.array(m.REF_ROBUST,float)
 queries=[('near-ray',t,g+t*(near-g)) for t in np.linspace(0,1,65)]+[('robust-ray',t,g+t*(robust-g)) for t in np.linspace(0,1,65)]+[('reference-segment',t,(1-t)*near+t*robust) for t in np.linspace(0,1,33)]
 previous=None;family=None
 for name,t,c in queries:
  if name!=family:previous=None;family=name
  b,J,it=solve(p,c,tri,previous);previous=b;V,gr,H,y,gp,den=J
  heights=np.einsum('ij,ij->i',ns,p[[f[0] for f in K['faces']]]-c)
  q0=ns/heights[:,None]+b
  q=q0/(1-q0@gp)[:,None];xx=y-gp
  U,um=root_data(xx,K['edges']);S,sm=root_data(q,K['edge_faces']);P=depths(xx,K['edges']);Q=depths(q,K['edge_faces'])
  row={'family':name,'t':float(t),'reference':c.tolist(),'b':b.tolist(),'volume':float(V),'own_centroid':gp.tolist(),'iterations':it,'minimum_denominator':den,'U':U,'S':S,'U_margin':um,'S_margin':sm,'P':P,'Q':Q}
  out.append(row)
  if len(out)%16==0 or len(U)<2 or len(S)<2:print('PROJECTIVE',name,t,'SU',len(S),len(U),'PQ',P[:2],Q[:2],'g',np.linalg.norm(gp),flush=True)
 raw=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode();Path('projective76.json').write_bytes(raw)
 print('RECEIPT',len(raw),hashlib.sha256(raw).hexdigest(),flush=True)
 print('J76_PROJECTIVE_CENTERING_SWEEP_DONE',len(out),'one_sided',sum(len(r['S'])==1 or len(r['U'])==1 for r in out),'both',sum(len(r['S'])==len(r['U'])==1 for r in out),flush=True)
if __name__=='__main__':main()
```

## projective76_exact.py
```python
"""Exact rational projective control of R22-B7, with unchanged incidence.
Dependency: J75_REFERENCE110_CAP233.py. No numerical minimizer is rerun.
"""
from fractions import Fraction as F
from itertools import groupby
from pathlib import Path
import json,hashlib,sys
sys.set_int_max_str_digits(0)
import J75_REFERENCE110_CAP233 as m

B=tuple(F(v,10**8) for v in (-57450277,2853538547,1121852810))

def gate(u,v):
 A=m.dot(u,u);B=m.dot(u,v);C=m.dot(v,v);D=A+C-2*B
 if D==0 or B>=A:return A
 if B>=C:return C
 return (A*C-B*B)/D

def all_positive_bars(x,edges):
 edges=sorted({tuple(sorted(e)) for e in edges});birth=[m.dot(v,v) for v in x]
 weight={e:gate(x[e[0]],x[e[1]]) for e in edges};par=list(range(len(x)));peak=par.copy();out=[]
 def find(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 for level,ee in groupby(sorted(edges,key=lambda e:(-weight[e],e)),key=lambda e:weight[e]):
  adj={}
  for i,j in ee:
   a,b=find(i),find(j)
   if a!=b:adj.setdefault(a,set()).add(b);adj.setdefault(b,set()).add(a)
  unseen=set(adj);groups=[]
  while unseen:
   a=min(unseen);unseen.remove(a);cc={a};todo=[a]
   while todo:
    for b in adj[todo.pop()]:
     if b in unseen:unseen.remove(b);cc.add(b);todo.append(b)
   groups.append(sorted(cc))
  for cc in groups:
   elder=max(cc,key=lambda a:(birth[peak[a]],-peak[a]))
   for a in cc:
    if a!=elder and birth[peak[a]]>level:
     out.append({'peak':peak[a],'elder':peak[elder],'birth':birth[peak[a]],'death':level,'depth':(birth[peak[a]]-level)/birth[peak[a]]})
   for a in cc:par[a]=elder
 assert len({find(i) for i in range(len(x))})==1
 return sorted(out,key=lambda b:(-b['depth'],b['peak']))

def main():
 K=m.hull(m.points());V0,M0=m.mass(K);c=m.REF_ROBUST
 assert m.inside(K,c)
 assert m.census(K,c)['strict']==[1,1,0]
 x=[m.sub(v,c) for v in K['points']]
 denominators=[1+m.dot(B,v) for v in x];assert min(denominators)>0
 y=[m.mul(v,1/d) for v,d in zip(x,denominators)]
 # Projectivity is globally nonsingular on K. Still rebuild and test exact supports.
 L=m.hull(y);assert L['material']==list(range(75))
 assert sorted(map(sorted,K['faces']))==sorted(map(sorted,L['faces']))
 assert K['edges']==L['edges']
 V,M=m.mass(L);g=m.mul(M,1/V)
 vv,mm=m.mass(L,g,positive=True);assert (vv,mm)==(V,M)
 C=m.census(L,g)
 xx=[m.sub(v,g) for v in L['points']]
 ns=[m.cross(m.sub(xx[f[1]],xx[f[0]]),m.sub(xx[f[2]],xx[f[0]])) for f in L['faces']]
 q=[m.mul(n,1/m.dot(n,xx[f[0]])) for n,f in zip(ns,L['faces'])]
 P=all_positive_bars(xx,L['edges']);Q=all_positive_bars(q,L['edge_faces'])
 assert len(P)==4 and len(Q)==3
 out={'name':'J76_REFERENCE110_PROJECTIVE_G8_OWN457','reference':c,'projective_b':B,
      'minimum_denominator':min(denominators),'density':1,'VEF':[len(y),len(L['edges']),len(L['faces'])],
      'volume':V,'volume_ratio':V/V0,'centroid':g,'census':C,
      'points':L['points'],'faces':L['faces'],'edges':L['edges'],'P_bars':P,'Q_bars':Q}
 assert C['strict']==[4,5,7] and C['weak']==C['primitive_zero']==[0,0,0]
 raw=(json.dumps(out,sort_keys=True,separators=(',',':'),default=str)+'\n').encode()
 Path('J76_PROJECTIVE_EXACT.json').write_bytes(raw)
 print('EXACT_PROJECTIVE',out['VEF'],C['strict'],C['weak'],C['primitive_zero'],flush=True)
 print('P_DEPTHS',[float(b['depth']) for b in P],'Q_DEPTHS',[float(b['depth']) for b in Q],flush=True)
 print('CENTROID',[float(v) for v in g],'VOLUME',float(V),'FRACTION',float(V/V0),flush=True)
 print('RECEIPT',len(raw),hashlib.sha256(raw).hexdigest(),flush=True)
 print('J76_REFERENCE110_PROJECTIVE_G8_OWN457_EXACT_PASS',flush=True)
if __name__=='__main__':main()
```
