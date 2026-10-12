# material-59fd3c8dd429

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Recovery capsule part 3/3: fixed rational replay and two scoped obstructions

Complete dependencies: part1 [internal-source-reference], SHA64faf0d80f09e758bf0a1955d3cc3e34a78412f31d397b5d7b3e1f57605ee29f; part2 [internal-source-reference], SHA0844362db835b0b4fcda2b799b6cdea73f42a68f01169c747545a094c6bc1657. Together these three readable materials contain the complete literal input, original producer and helpers, both finite exact endpoint generators, non-default coefficients, and a new full-ray exclusion proof. No originating sandbox or old optimizer archive is required. No C622/FULL76 dependency. The analytic parent is accepted figure-0564, SHA43bfbd73da649bfd2b1e41bbec8082606ae7b95b4fbeab380c1d5c6a7672bd34; its original author reported unobserved execution. The finite computations below were actually executed by the coordinator on the 75-row L18, not that author's unobserved output.

## Results and scope
Both new endpoints have V75/E204/F131,C408, own strict(S,U,H)=(2,2,2), additionalweak000 and primitivezero000. Their actual homogeneous centroid is EXACTLY the parent's centroid, not a nominated reference point. Both are at rational t=1/16384. Parent positive depths are P=.10018756794854827,Q=.06712194454711798. L18_MASSLIFT_BASE_T14 has P=.10015004850234907,Q=.0670841567291111. L18_MASSLIFT62_T14 has P=.10012655168275562,Q=.06706118493912375. These are useful nonrecord finite mass-repair controls, NOT own110 and not better than the accepted F18 paired-depth control. The accepted own110 remains C622, outside the goal.

For the base chart primary[13,22,14,16,24], controller[10,23], every valid finite parameter leaves vertex62 and its neighbors[49,58,59,64,65,68,70] fixed, and leaves the actual centroid fixed. Thus62 remains strictly unstable. Fixed point6 is farther from the centroid than62. A farthest vertex v satisfies 2(v-c)·(w-v)=|w-c|²-|v-c|²-|w-v|²<0 for every distinct vertex w, so is strictly U and cannot be62. Consequently U>=2 throughout this particular entire fixed-complex chart. This is not an exclusion for other primary/controller stars, centroid changes or new incidence. The unwanted primal peak is62;6 is the surviving elder. Its bottleneck is13--22. The extra dual peak is triangle14,16,24; the other saddle is6--63.

The extended fixed rational ray includes primary62, so the preceding invariant-star proof does not apply. A NEW exact bound nonetheless excludes own110 on its entire positive old-complex domain. Supporting face{49,65,62} against point58 has an affine gap with positive intercept and negative slope. Hence every t>=0 retaining the original strict supporting complex necessarily satisfies t<T, where
T=6079490140/35608115190831 = .0001707332754743911 approximately.
For each of62's seven neighbors, its strict-U dot product is a concave rational quadratic in t. Exact maximization on the larger closed interval[0,T] is negative for all seven. The squared radius of62 is convex and both endpoint values are strictly below the fixed squared radius of6. Thus62 and a different farthest vertex are strict U throughout every valid positive t on this ray. This necessary support bound is NOT asserted to be the first geometry event. Changed-complex descendants and negative t are not excluded.

Larger sampled base steps t=1/1024,1/2048 have strict637;1/4096 has435;1/8192 has233, all with the old support complex valid. Extended t=1/8192 has strict424/weak000, new stable facets[20,21,24] and[16,18,31], and new saddles(21,24),(16,31), despite decreasing both largest depths. At t=1/4096 the extended old complex already fails. These samples are not full interval censuses. Maximum-depth descent alone is not a no-birth guard. Next useful freedom is motion of a broader current-root/interface block, support-wall transitions, and actual mass/critical-region tracking; continuing these excluded directions cannot finish the target.

## Recovery and verification
Save the fenced units with final LF beside the part1/2 files. Observed Python3.13.5, NumPy2.3.5, SciPy1.17.0. The fixed replay bypasses BLAS nomination and uses literal rational directions. Run:

`OPENBLAS_NUM_THREADS=1 python replay_l18_massrepair.py --input l18_exact_points.json --out fixed_replay`

Observed terminal markers:
L18_FIXED_FINITE_REPLAY_PASS base [2, 2, 2] 0.10015004850234907 0.0670841567291111
L18_FIXED_FINITE_REPLAY_PASS root62 [2, 2, 2] 0.10012655168275562 0.06706118493912375
L18_EXTENDED_RAY_U_GE_2_PASS 0.0001707332754743911
L18_FINITE_MASS_REPAIR_RECOVERY_PASS

The replay checks endpoint hashes, exact support, finite M=cV, full weak/primitive/strict census and all positive bars. It also generates the exact quadratic certificates for the full positive-ray obstruction. This is a replay of the coordinator's own computation, not claimed to be an independent physics engine.

Original producer command: `OPENBLAS_NUM_THREADS=1 python l18_masslift.py l18_exact_points.json --out masslift`. Expected terminal marker EXACT_FINITE_MASS_REPAIR_JOINT_DESCENT_PASS14 (printed with a space before14). The original extension script below retains its original /mnt/data default paths; with the source/input files there, run `OPENBLAS_NUM_THREADS=1 python /mnt/data/l18_extend.py --primary 13,22,14,16,24,62 --name masslift62`. Expected EXACT_EXTENDED_MASS_REPAIR_DESCENT_PASS14. The fixed replay is the portable reconstruction authority for exact endpoints.

Recovery source hashes: l18_extend.py2048B SHAaa161fce02edf086d29c9548c118095792f005dd4210728883a9b2cf1b1cad1c; replay_l18_massrepair.py4981B SHAf4028fb3941a156b841742484afb914d1048a9635cc286ab62f4b71866d14e1f.
Expected reproduced outputs:
base/endpoint.json4827B SHA683f8b7cc389bf2a16477e849f9abcc3bc176f2a693d8159e291c44c70ad597e;
base/endpoint_audit.json2163B SHAf82d4863aef3049ff252ddc15a5c1d670c7d20db43c76afbb6da128ab381e826;
root62/endpoint.json4863B SHA56f2afbb1fd7ae0f06733033ffbc3afb9d5b937f9c66f30a214866404a69b9ec;
root62/endpoint_audit.json2179B SHA3e689efb2d114b35c77f0564fd742b787710f4fa47e5b40a7082ca5d603931e3;
root62_ray_obstruction.json3440B SHA2253d75ca17cb80bb6cfbe11f193fcf73b32ee5b93bfff97d2998de61932a7f8.
Original scan output identities (regenerated by original producers; not endpoint authority if numeric nomination varies): masslift/tests.json26037B SHAb47d0c1bdbb078e9c97be45542d90af793550060b025b9757c295b076d7011e4; masslift62/tests.json7954B SHA6f6ced0c6058f451a91e79d78c18a19fd7cf4eaab5e7ae83f6d8a4e5fde348d4. Original chart hashes are5f14cbea1a801dae183b87b27b89923e49ddc089c14ec474ed62d55d296aa30c and84a9038ac639a420b070b254be3474b94e9e28bdc149c43d42bf614ed12e99fe respectively; their defining literal rational directions are all included below.

## l18_extend.py
```python
"""Recorded finite exact extensions of the L18 mass repair chart."""
from pathlib import Path
from fractions import Fraction as F
import argparse
import l18_masslift as lm

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--primary',required=True);ap.add_argument('--name',required=True);ap.add_argument('--pair');a=ap.parse_args()
 lm.PRIMARY=[int(s) for s in a.primary.split(',')];out=Path('/mnt/data')/a.name;out.mkdir(exist_ok=True)
 R=lm.load_source('/mnt/data/l18_exact_points.json');ch=lm.make_chart(R,pair=tuple(map(int,a.pair.split(','))) if a.pair else None);assert ch
 lm.dump(out/'chart.json',ch)
 print('CHART',lm.PRIMARY,ch['pair'],ch['selection'],'DERIV',float(ch['derivative_P']),float(ch['derivative_Q']),flush=True)
 nb={i:[] for i in [6,62]}
 for i,j in R['edges']:
  if i in nb:nb[i].append(j)
  if j in nb:nb[j].append(i)
 print('ROOT_STARS',nb,flush=True)
 for i in nb:print('ROOT',i,'RADIUS2',float(lm.dot(R['x'][i],R['x'][i])),'SCORES',[(j,float(lm.dot(R['x'][i],lm.sub(R['x'][j],R['x'][i])))) for j in nb[i]],flush=True)
 tests=[]
 for j in range(5,24):
  t=F(1,2**j);y,V=lm.construct(R,ch,t);bad=lm.valid_complex(y,R['faces']);row={'j':j,'t':t,'invalid_count':len(bad),'first_failures':bad[:3]}
  if bad:
   tests.append(row);print('STEP',j,'INVALID',len(bad),'FIRST',bad[0][:3],flush=True);continue
  A=lm.mechanics(y,R['faces'],R['edges'],R['owners'],R['c']);row.update(A);row['volume']=V;tests.append(row)
  print('STEP',j,A['strict'],'ROOTS',A['roots'],'H',A['saddles'],'P',[float(b['depth']) for b in A['P']],'Q',[float(b['depth']) for b in A['Q']],flush=True)
  if not any(A['additional_weak']) and not any(A['primitive_zero']) and len(A['P'])==len(A['Q'])==1 and A['P'][0]['depth']<R['P'][0]['depth'] and A['Q'][0]['depth']<R['Q'][0]['depth']:
   lm.dump(out/'endpoint.json',{'points':y,'centroid':R['c'],'density':1,'volume':V,'t':t});lm.dump(out/'endpoint_audit.json',A);print('EXACT_EXTENDED_MASS_REPAIR_DESCENT_PASS',j,flush=True);break
 lm.dump(out/'tests.json',tests)
if __name__=='__main__':main()
```

## replay_l18_massrepair.py
```python
"""Fixed-rational replay of two finite own-centroid charts and a ray obstruction.
Requires l18_masslift.py, l18_support_search.py and l18_exact_points.json.
No numeric coefficient nomination is performed by this replay.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib
import l18_masslift as lm
DIRECTIONS={
 'base':{13:['88721003/272000000','-91867/250000','681533/1000000'],14:['-4711/1000000','2393/50000','10947/250000'],16:['-172497/1000000','301729/1000000','112857/500000'],22:['-34301/136000','238801/500000','-1'],24:['47943/500000','-83887/500000','-23523/1000000']},
 'root62':{13:['26802223/272000000','-62267/500000','238953/1000000'],14:['80449/500000','-89111/1000000','-25353/200000'],16:['-386601/1000000','327053/500000','478681/1000000'],22:['-7561409/136000000','10183/100000','-105999/500000'],24:['117047/500000','-453659/1000000','-48789/500000'],62:['-205039/1000000','330711/1000000','399181/1000000']}}
EXPECTED={'base':{'endpoint.json':'683f8b7cc389bf2a16477e849f9abcc3bc176f2a693d8159e291c44c70ad597e','endpoint_audit.json':'f82d4863aef3049ff252ddc15a5c1d670c7d20db43c76afbb6da128ab381e826'},'root62':{'endpoint.json':'56f2afbb1fd7ae0f06733033ffbc3afb9d5b937f9c66f30a214866404a69b9ec','endpoint_audit.json':'3e689efb2d114b35c77f0564fd742b787710f4fa47e5b40a7082ca5d603931e3'}}

def fixed_chart(R,which):
 controls=[];images=[]
 for i in (10,23):
  a,basis,im=lm.star(R['p'],R['faces'],i)
  controls.extend((i,b) for b in basis);images.extend(im)
 C=images[:3];assert lm.det(*C)!=0
 primary=set(DIRECTIONS[which])
 for f in R['faces']:
  assert not (10 in f and 23 in f)
  assert not (set(f)&primary and (10 in f or 23 in f))
 d=[lm.ZERO for _ in R['p']]
 for i,raw in DIRECTIONS[which].items():d[i]=tuple(map(F,raw))
 return {'direction':d,'controls':controls[:3],'C':C}

def max_quadratic(coef,L,U):
 a,b,c=coef
 val=lambda t:a*t*t+b*t+c
 candidates=[(L,val(L)),(U,val(U))]
 if a<0:
  t=-b/(2*a)
  if L<t<U:candidates.append((t,val(t)))
 return max(candidates,key=lambda x:x[1])

def ray_obstruction(R,ch):
 p=R['p'];x=R['x'];d=ch['direction'];nb=sorted(j if i==62 else i for i,j in R['edges'] if 62 in (i,j))
 assert nb==[49,58,59,64,65,68,70]
 assert all(d[j]==lm.ZERO for j in nb) and d[6]==lm.ZERO
 f=next(f for f in R['faces'] if set(f)=={49,65,62})
 def gap(t):
  y={i:lm.add(p[i],lm.mul(d[i],t)) for i in set(f)|{58}}
  n=lm.cross(lm.sub(y[f[1]],y[f[0]]),lm.sub(y[f[2]],y[f[0]]))
  return lm.dot(n,lm.sub(y[f[0]],y[58]))
 g0=gap(F(0));slope=gap(F(1))-g0
 assert gap(F(2))==g0+2*slope and g0>0 and slope<0
 T=-g0/slope;dd=lm.dot(d[62],d[62]);checks=[]
 for j in nb:
  e=lm.sub(x[j],x[62]);coef=(-dd,lm.dot(d[62],e)-lm.dot(x[62],d[62]),lm.dot(x[62],e))
  t,m=max_quadratic(coef,F(0),T);assert m<0
  checks.append({'neighbor':j,'coefficients':coef,'maximizer':t,'maximum':m})
 # Squared radius of 62 is convex, so its maximum is at an endpoint.
 r6=lm.dot(x[6],x[6]);r62=[lm.dot(x[62],x[62]),lm.dot(lm.add(x[62],lm.mul(d[62],T)),lm.add(x[62],lm.mul(d[62],T)))]
 assert max(r62)<r6
 return {'face':f,'outside_point':58,'gap_intercept':g0,'gap_slope':slope,'necessary_positive_t_upper_bound':T,'root62_scores':checks,'radius6_squared':r6,'radius62_squared_endpoints':r62,'conclusion':'For every t>=0 with the original strict supporting complex, U>=2. The bound is necessary, not claimed to be the first geometry event; changed-complex descendants are not excluded.'}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input',default='l18_exact_points.json');ap.add_argument('--out',default='fixed_replay');a=ap.parse_args();out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
 R=lm.load_source(a.input);assert len(R['p'])==75 and len(R['edges'])==204 and len(R['faces'])==131
 baseline=lm.mechanics(R['p'],R['faces'],R['edges'],R['owners'],R['c']);assert baseline['strict']==[2,2,2] and baseline['additional_weak']==baseline['primitive_zero']==[0,0,0]
 for name in DIRECTIONS:
  ch=fixed_chart(R,name);dest=out/name;dest.mkdir(exist_ok=True)
  t=F(1,16384);y,V=lm.construct(R,ch,t);assert not lm.valid_complex(y,R['faces'])
  A=lm.mechanics(y,R['faces'],R['edges'],R['owners'],R['c']);assert A['strict']==[2,2,2] and A['additional_weak']==A['primitive_zero']==[0,0,0]
  assert A['P'][0]['depth']<R['P'][0]['depth'] and A['Q'][0]['depth']<R['Q'][0]['depth']
  lm.dump(dest/'endpoint.json',{'points':y,'centroid':R['c'],'density':1,'volume':V,'t':t});lm.dump(dest/'endpoint_audit.json',A)
  for fn,sha in EXPECTED[name].items():assert hashlib.sha256((dest/fn).read_bytes()).hexdigest()==sha
  print('L18_FIXED_FINITE_REPLAY_PASS',name,A['strict'],float(A['P'][0]['depth']),float(A['Q'][0]['depth']),flush=True)
  if name=='root62':
   proof=ray_obstruction(R,ch);lm.dump(out/'root62_ray_obstruction.json',proof);print('L18_EXTENDED_RAY_U_GE_2_PASS',float(proof['necessary_positive_t_upper_bound']),flush=True)
 print('L18_FINITE_MASS_REPAIR_RECOVERY_PASS',flush=True)
if __name__=='__main__':main()
```
