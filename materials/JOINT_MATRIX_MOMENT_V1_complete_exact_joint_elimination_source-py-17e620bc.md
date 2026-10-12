# material-17e620bc7822

AI research material

---

"""Joint matrix-valued elimination of unsupported affine-simplex moments.
Exploratory exact source; publication requires physical proof and durable storage.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction as F
from math import gcd,lcm
import time,json,sys,hashlib
import affine_moments as am
fm=am.fm
PAIRS=list(combinations(range(10),2))
PAIRS=sorted([(i,j) for i in range(10) for j in range(i,10)])
PI={p:i for i,p in enumerate(PAIRS)}

def axpy(v,w,s):
 for k,c in w.items():
  a=v.get(k,0)+s*c
  if a:v[k]=a
  elif k in v:del v[k]
 return v

def scalar_echelon(rows,order):
 pos={t:i for i,t in enumerate(order)};piv={}
 for row in rows:
  v={t:F(c) for t,c in row.items() if c}
  while v:
   t=min(v,key=pos.__getitem__)
   if t not in piv:
    a=v[t];piv[t]={k:c/a for k,c in v.items()};break
   axpy(v,piv[t],-v[t])
 return piv

def primitive(v):
 if not v:return v
 m=1
 for a in v.values():m=lcm(m,F(a).denominator)
 w={k:int(a*m) for k,a in v.items()};g=0
 for a in w.values():g=gcd(g,abs(a))
 if w[min(w)]<0:g=-g
 return {k:a//g for k,a in w.items()}

def lift(c,mode,i=None):
 v={}
 for t,s in c.items():
  if mode=='first':
   for j in t:
    k=(t,PI[tuple(sorted((i,j)))]);v[k]=v.get(k,0)+s*(2 if i==j else 1)
  else:
   assert mode=='second'
   for a in t:
    for b in t:
     if a<=b:v[(t,PI[a,b])]=s*(2 if a==b else 1)
 return v

def volume_reduce(v,piv,pivot_order):
 # Each subtraction is a scalar valid volume relation times one constant C.
 for t in pivot_order:
  block=[(k[1],c) for k,c in v.items() if k[0]==t]
  if block:
   for q,c in block:
    axpy(v,{(u,q):a for u,a in piv[t].items()},-c)
 return v

def quotient_echelon(rows,orderkey,allowed=None):
 piv={};out=[]
 for row in rows:
  v={k:F(c) for k,c in row.items() if c}
  while v:
   p=min(v,key=orderkey)
   if p not in piv:
    a=v[p];v={k:c/a for k,c in v.items()};piv[p]=v
    if allowed is None or p[0] in allowed:
     assert allowed is None or all(k[0] in allowed for k in v)
     out.append(primitive(v))
    break
   axpy(v,piv[p],-v[p])
 return out,piv

def build(index,verbose=True):
 start=time.time();d=am.system(fm.inputs()[index]);U=set(d['cells']);universe=list(combinations(range(10),4));outside=sorted(set(universe)-U)
 order=outside+sorted(U);positions={t:j for j,t in enumerate(order)}
 cycles=[]
 for q in combinations(range(1,10),4):
  S=(0,)+q;cycles.append({S[:j]+S[j+1:]:(-1)**j for j in range(5)})
 flats=[{tuple(t):1} for t in d['affine_metadata']['cofacial_flat_cells']]
 sp=scalar_echelon(cycles+flats,order);po=sorted(sp,key=positions.__getitem__)
 # Reduce ALL scalar-volume pivots. Supported volume identities are retained
 # separately, so no supported first/second identity is lost in this quotient.
 rem=[t for t in order if t not in sp];orderkey=lambda k:(positions[k[0]],k[1])
 if verbose:print('MATRIX_SCALAR',index,'U',len(U),'rank',len(sp),'outsidefree',len(set(rem)-U),'quotient',len(rem)*55,'time',time.time()-start,flush=True)
 ambient=[]
 for c in cycles+flats:
  for i in range(10):ambient.append(volume_reduce(lift(c,'first',i),sp,po))
  ambient.append(volume_reduce(lift(c,'second'),sp,po))
 if verbose:print('MATRIX_AMBIENT',index,len(ambient),'nnz',sum(len(v) for v in ambient),'time',time.time()-start,flush=True)
 supp,piv=quotient_echelon(ambient,orderkey,U)
 eps={tuple(t):s for t,s in d['affine_metadata']['epsilon']}
 # Legacy first/second moments translated into oriented masses, then quotiented.
 legacy=[]
 for h in d['basis']:
  c={t:s*eps[t] for t,s in h.items()}
  for i in range(10):legacy.append(volume_reduce(lift(c,'first',i),sp,po))
  legacy.append(volume_reduce(lift(c,'second'),sp,po))
 old,oldp=quotient_echelon(legacy,orderkey)
 allbasis,allp=quotient_echelon(legacy+supp,orderkey)
 assert len(allbasis)==len(supp)
 new=allbasis[len(old):]
 # Convert the exact supported identities from D_t to positive d_t.
 new=[primitive({k:c*eps[k[0]] for k,c in v.items()}) for v in new]
 # Exact rank of positive old matrix identities modulo volume must equal old.
 out={'identity':'JOINT_MATRIX_MOMENT_EXACT_CENSUS_V1','native_index':index,
  'scalar_system_pin':fm.pin(fm.enc(fm.description(d))),'cells':len(U),
  'scalar_rank':len(d['basis']),'full_scalar_rank':len(sp),
  'unsupported_scalar_nonpivots':len(set(rem)-U),'ambient_quotient_rank':len(piv),
  'legacy_quotient_rank':len(old),'supported_quotient_rank':len(supp),
  'new_matrix_relations':len(new),'new_nonzeros':sum(len(v) for v in new),
  'new_relations':[[[list(t),q,c] for (t,q),c in sorted(v.items())] for v in new]}
 if verbose:print('MATRIX_EXACT_GAIN',index,len(old),len(supp),len(new),out['new_nonzeros'],'time',time.time()-start,flush=True)
 return out

if __name__=='__main__':
 for idx in map(int,sys.argv[1:]):
  out=build(idx);b=fm.enc(out);(fm.HERE/f'matrix_moments_{idx}.json').write_bytes(b)
  print('MATRIX_MOMENT_CENSUS_WRITTEN',idx,*fm.pin(b),flush=True)
