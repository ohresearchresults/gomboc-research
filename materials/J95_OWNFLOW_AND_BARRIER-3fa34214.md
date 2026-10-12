# material-3fa34214965b

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J95/J96: moving-centre support obstruction, compulsory mass, and own-mass continuation

## Analytic proposition: outer inclusion cannot join old low-support components

Let K and L be full-dimensional convex bodies, K subset L, with old centre0 inside K and new centre delta inside L. For unit n put h_K(n)=max(x.n:x in K) and A_K(r)={n on S2:h_K(n)<r}. If ||delta||_2<=epsilon, then h_(L-delta)(n)=h_L(n)-n.delta >= h_K(n)-epsilon. Consequently A_(L-delta)(r) subset A_K(r+epsilon). Each connected subset of the former is contained in one connected component of the latter. With epsilon0, pure outer enlargement cannot join distinct OLD low-support components at the same level. It can remove them or create further subcomponents. Each surviving component contains a local support minimum: minimize h on its compact closure; an interior value is below the boundary level. For a nondegenerate polyhedron these are stable equilibria. With degeneracy, state local minima rather than silently infer a strict census.

Assume an elder normal n_e of old height h_e is preserved exactly: h_L(n_e)=h_e. Let n_j be the old junior stable normal of height h_j, and r_d the first old support-sublevel merge level of the components containing n_e,n_j. Suppose epsilon<(r_d-h_e)/2. If h_L(n_j)<r_d-2epsilon, choose r just below r_d-epsilon but above h_e+epsilon and h_L(n_j)+epsilon. Both normals lie in A_(L-delta)(r) but in different components of A_K(r+epsilon). Thus a nondegenerate final S1 body retaining the elder support necessarily satisfies

h_L(n_j)-h_j >= r_d-h_j-2epsilon.

With delta's actual direction known, the sharper necessary inequality is h_L(n_j)>=r_d-epsilon+n_j.delta, under the same elder-survival condition. The symmetric2epsilon form is its worst-case relaxation. With no support rise at n_j, ||delta||_2 must be at least (r_d-h_j)/2 unless another hypothesis is escaped. This does not prove such a centre displacement is physically achievable. Raising this one normal is NOT sufficient: the entire old unwanted component must be emptied, and new components may appear. Discrete facet-normal sampling is not certified continuous angular coverage.

The scope matters: deleting old material or freely moving old supports need not preserve K subset L. Therefore new KH93 R82/LOW bodies do NOT inherit an exclusion from old C434 numbers. Replacing C434 by C390 plus a dome also cannot use K=C434. The support proposition does not assume a retained old U; the separate mass bound below does.

## Compulsory pyramid and opposite-mass lower bound

An old facet F has outward unit normal n, positive own-centred height h, and area A. If L contains K and h_L(n)>=h+Delta, some x in L has n.x>=h+Delta. The pyramid conv(F,x) lies in L and, except for its base, outside K. Its volume is at least V_p=A Delta/3, its centroid has n-coordinate at least h+Delta/4, and its n first moment is at least m_p=V_p(h+Delta/4).

If both bodies have centre0 and L retains the old unique unstable vertex u as its sole unstable vertex, R=||u|| bounds all of L: every globally farthest vertex is strictly unstable. Other added material has n-coordinate>=-R. Hence the remaining added volume is at least m_p/R and total added volume at least V_p+m_p/R. These weak necessary bounds are NOT impossibility statements. A changed unstable root or nonzero new centre changes the hypotheses; for g(L)=delta the required first moment is V(L)delta, not zero. Do not sum independently overlapping cap volumes; integrate the actual finite hull or use a disjoint decomposition.

## Numerical diagnostics and finite-amplitude test

On literal J91_REBALANCED_C434_G18, the executed binary64 diagnostic below gives junior face10, material labels[33,133,39], polar birth2.8112869832868146/death2.353201640814981, polar death edge48--52 corresponding to physical old40--109. Area=.0174641046494171,h_j=.5964134228840031,h_e=.43785736301207856,r_d=.651884160595367. Necessary fixed-centre support rise=.055470737711363904, relative=.09300719196280136 (about9.3%). With zero rise, the necessary centre displacement is .027735368855681952. R=1.579684376584463 gives compulsory volume .00032291558945720896, moment .00019706928350220237, opposite-volume bound .0001247523153506769 and total-added bound .00044766790480788585. These numbers are floating diagnostics, NOT rational interval certificates. The analytic proposition does not exclude this shape family.

Four least-added-volume scale1.1 chains were tested with each new chain held fixed and the existing five apexes repairing actual mass. All four closed numerical mass but acquired an unstable mass-controller at ORIGINAL MATERIAL132 in addition to old1. Their P depths are .20422430135390102,.20948455481150274,.21087383690063777,.21245632055758168. The second U is NOT on the protected new chain. Final V/E/F,S are110/210/102,S5;109/207/100,S5;110/210/102,S5;109/211/104,S9. The seven literal states below include these four failures. No exact strict/weak promotion is claimed. A distributed controller, finite opposed material, changed old boundary, or centre displacement remain live mechanisms; four failures do not exclude them.

## Actual-centre continuation and executed scope

ownflow95.py fixes old130 material vertices but moves all new apexes, differentiating the ACTUAL homogeneous centroid M/V and both centred landscapes in each topology chart. It imposes no M=0 equality. Every finite trial rebuilds its hull, own mass, proposed maximal counts and all reported numerical P/Q. Three30-step runs completed:

`python ownflow95.py J94_BACKOFF_0_9999_STATE.json 30 J95_C440_OWN two`: numerical136/220/86,S2/U1,P0,Q1, sumQ=.16179070428360076. It remains near the known tiny-bar boundary and is NOT promoted to exact211.

`python ownflow95.py J94_FIXEDCHAIN_0_3_STATE.json 30 J95_C444_OWN free`: numerical136/225/91,S32/U1,P0,Q31,sumQ=.16097896276278767. Own centre relative to old host approximately(7.753568687742083e-7,7.354464118740073e-7,-1.8357728286854956e-7). Free centre motion has not prevented stable-basin fragmentation.

`python ownflow95.py J94_C440_START_STATE.json 30 J95_SQRT_C440 free 0.5`: numerical136/220/86,S11/U1,P0, but only5 Q bars above nomination threshold, sum(sqrt(Q))=.4028151288192971. This S/Q discrepancy warns about tolerance-level equilibria; it is not an exact class. Relative centre approximately(2.3030010238892678e-8,1.4019286952256942e-7,7.509163906129323e-8). No S1 resulted. The first two runs used the alpha1 predecessor; the preserved final source adds loss_power and positive clamp/power before summation, default1. The complete literal endpoints permit direct numerical recount without optimizer-path portability. No claim is made that the final source reproduces every historical floating optimizer report byte.

For a peak q that is an endpoint of its death edge of direction d, with the perpendicular foot strictly inside, D=1-||q+t d||^2/||q||^2=(q.d)^2/(||q||^2||d||^2). Thus sqrt(D) is linear in the absolute normalized chord near cancellation, while D is quadratic. Concavity also penalizes splitting a fixed total depth among more bars. Neither observation guarantees S1. J94's exact positive6.6e-29 bar remains the acceptance warning.

## Complete recovery and commands

Dependencies: J94_METHODS_CONTINUATION [internal-source-reference] and its five complete J90/J91 source bundles [internal-source-reference], [internal-source-reference], [internal-source-reference], [internal-source-reference], [internal-source-reference]. Regenerating the fixed-chain searches additionally requires J94_METHODS_CHAINS [internal-source-reference]; recounting the literal states does not. Extract each complete code/data block below with its final newline beside those sources. Python3.13.5,NumPy2.3.5,SciPy1.17.0,PyTorch2.10.0+cpu,OPENBLAS_NUM_THREADS=1,OMP_NUM_THREADS=1 were used. Reconstruct J90_DETACHED_C390_G8_AUDIT.json via the full old J90 core. No sandbox-only construction is promoted.

`python recount95.py` reads all seven *_STATE.json below, writing J95_STORED_STATE_RECOUNTS.json (executed21360B,SHAe25b48a57bfe594154714794c196d8824690fe3b8c8daced7389563d0452fa2d), marker J95_STORED_NUMERICAL_STATES_RECOUNT_PASS_NOT_EXACT. Those output bytes depend on the numerical environment; no rational census is implied.

`python barrier95.py` diagnoses C434 and, when the original four fixed-chain report filenames exist, recounts their U labels. It was executed with those original reports, giving J95_BARRIER_DIAGNOSTICS.json8270B,SHA64878e9bd1ef6797ad7fed7a42a72dfa97555d12ccd96c09a4666f0332394cf2, marker J95_CONDITIONAL_BARRIER_NUMERICAL_DIAGNOSTICS_ONLY. Copying the supplied *_STATE.json to unsuffixed *.json also supplies the entire required apex state, but changes state_sha256 fields and therefore diagnostic bytes. Geometry and bound values agree; do NOT call the two byte objects identical. STATE files deliberately omit bulky report histories but omit no computational apex, centre frame, input or parameter.

## ownflow95.py
4483B; SHA256188b5052a4ed76bb57d5aef67547d4aaf364428e8020721e787b64265406d128.
```python
"""Finite outer shape continuation with the actual homogeneous centre free.
Old material points stay fixed, but all new apexes move. Every gradient includes
actual tetrahedral centroid motion; all finite candidates rebuild the hull.
This is numerical nomination, never an exact strict/weak equilibrium census.
"""
import sys,json
from pathlib import Path
import numpy as np,torch
from scipy.optimize import linprog,minimize
from surgery94 import initial,save
from outerflow91 import chart
from envelope91 import hullpoly
from j90 import report,score
ROOT=Path(__file__).resolve().parent
torch.set_default_dtype(torch.float64);torch.set_num_threads(1)

def run(source,steps=60,tag='J95_OWNFLOW',policy='free',resume=False,loss_power=1.):
 old,W,g=initial();W=np.array(json.loads(Path(source).read_text())['apexes'])
 hist=[];trust=.015;O=torch.tensor(old)
 if resume and (ROOT/(tag+'.json')).exists():
  d=json.loads((ROOT/(tag+'.json')).read_text());W=np.array(d['apexes']);hist=d['history'];trust=d['next_trust']
 start=len(hist);best=None
 for k in range(start,start+steps):
  zz,fields=chart(old,W);r=report(zz);q=zz['q'];bars=r['Q'];P=np.vstack([old,W])-zz['g'];labs=np.array(zz['labels']);root=int(labs[np.argmax((P[labs]**2).sum(1))])
  if not bars:print('NUMERICAL_S1_REQUIRES_EXACT_AUDIT',r,flush=True);break
  ui=np.array([i for i in labs if i!=root],int);votes=score(P);uj=votes.argmax(1)[ui]
  elder=int(np.argmax((q*q).sum(1)));roots={elder,*[b['root'] for b in bars]}
  qi=np.array([i for i in range(len(q)) if i not in roots],int);qj=score(q).argmax(1)[qi]
  def fun(w):
   Q0,M,V=fields(w);c=M/V;X=torch.cat([O,w]);Pc=X-c;Q=Q0/(1-Q0@c)[:,None]
   du=Pc[uj]-Pc[ui];us=(Pc[ui]*du).sum(1)/(torch.linalg.vector_norm(Pc[ui],dim=1)*torch.linalg.vector_norm(du,dim=1))
   dq=Q[qj]-Q[qi];qs=(Q[qi]*dq).sum(1)/(torch.linalg.vector_norm(Q[qi],dim=1)*torch.linalg.vector_norm(dq,dim=1))
   ls=[]
   for bar in bars:
    a,b=bar['edge'];peak=bar['root'];d=Q[b]-Q[a];t=torch.clamp(-(Q[a]*d).sum()/(d*d).sum(),0,1);f=Q[a]+t*d
    ls.append(1-(f*f).sum()/(Q[peak]*Q[peak]).sum())
   return torch.cat([us,qs,torch.clamp(torch.stack(ls),min=1e-30).pow(loss_power).sum()[None]])
  wt=torch.tensor(W);val=fun(wt).numpy();J=torch.func.jacrev(fun,chunk_size=64)(wt).numpy().reshape(len(val),-1);G=J[:-1];grad=J[-1]
  target=np.minimum(val[:-1],1e-7)
  if policy=='free':target[len(ui):]=-1000
  norm=np.linalg.norm(G,axis=1);keep=norm>1e-10;scale=np.maximum(norm[keep],1e-8);A=G[keep]/scale[:,None];rhs=(target-val[:-1])[keep]/scale
  lp=linprog(grad,A_ub=-A,b_ub=-rhs,bounds=[(-trust,trust)]*W.size,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
  rec=dict(k=k,old=float(val[-1]),trust=trust,lp=bool(lp.success),accepted=False)
  if lp.success and grad@lp.x<-1e-13:
   B=np.vstack([A,-grad]);lb=np.r_[rhs,-.7*grad@lp.x]
   opt=minimize(lambda d:(.5*d@d,d),lp.x,jac=True,method='SLSQP',bounds=[(-trust,trust)]*W.size,constraints=[{'type':'ineq','fun':lambda d:B@d-lb,'jac':lambda d:B}],options={'maxiter':100,'ftol':1e-17})
   delta=(opt.x if min(B@opt.x-lb)>-1e-8 else lp.x).reshape(W.shape)
   for bt in range(18):
    w=W+2**-bt*delta
    try:zt=hullpoly(np.vstack([old,w]));rt=report(zt)
    except Exception:continue
    loss=sum(x['depth']**loss_power for x in rt['Q'])
    if rt['E']>249 or len(rt['U'])!=1 or rt['P'] or loss>=rec['old']-1e-12:continue
    if policy=='two' and len(rt['S'])>2:continue
    W=w;rec.update(accepted=True,alpha=2**-bt,new=loss,report=rt);break
  hist.append(rec)
  if rec['accepted'] and rec['alpha']>=.5:trust=min(.12,trust*1.3)
  elif not rec['accepted']:trust*=.5
  rr=report(hullpoly(np.vstack([old,W])));key=(len(rr['S']),sum(b['depth'] for b in rr['Q']),rr['E'])
  if best is None or key<best:
   best=key;save(tag+'_BEST',old,W,g,dict(source=source,policy=policy,loss_power=loss_power,report=rr,iteration=k))
  save(tag,old,W,g,dict(source=source,policy=policy,loss_power=loss_power,history=hist,next_trust=trust,report=rr))
  print(tag,k,'objective',rec.get('new',rec['old']),'SU',len(rr['S']),len(rr['U']),'VEF',rr['V'],rr['E'],rr['F'],'g',rr['centroid'],'alpha',rec.get('alpha'),'trust',trust,flush=True)
  if trust<1e-8:break
 print('J95_OWN_CENTRE_FLOW_NUMERICAL_ONLY',flush=True)
if __name__=='__main__':run(sys.argv[1],int(sys.argv[2]),sys.argv[3],sys.argv[4] if len(sys.argv)>4 else 'free','--resume' in sys.argv,float(sys.argv[5]) if len(sys.argv)>5 and sys.argv[5]!='--resume' else 1.)
```

## barrier95.py
2209B; SHA2561bcb6069895ae3145d13692dd2f6b4b61acf1198c81dc0be4b6306d9cada4271.
```python
"""Numerical diagnostics for a conditional support-sublevel obstruction.
The analytic proposition is in J95_OWNFLOW_AND_BARRIER.md. This program
computes its geometric inputs on literal J91_REBALANCED_C434_G18 and
examines the executed fixed-chain4 states. It proves no exact class.
"""
from pathlib import Path
import json,hashlib
import numpy as np
from surgery94 import initial
from envelope91 import hullpoly
from j90 import report
ROOT=Path(__file__).resolve().parent

def main():
 old,W,g=initial();z=hullpoly(np.vstack([old,W]));r=report(z)
 b=r['Q'][0];j=b['root'];q=z['q'];n=q[j]/np.linalg.norm(q[j])
 cy=z['faces'][j];xx=z['x'][cy];a=xx[0]
 area=sum(np.linalg.norm(np.cross(xx[k]-a,xx[k+1]-a))/2 for k in range(1,len(xx)-1))
 hj=1/np.linalg.norm(q[j]);rd=1/np.sqrt(b['death']);gap=rd-hj
 he=1/np.sqrt(np.max(np.sum(q*q,axis=1)));R=np.sqrt(np.max(np.sum(z['p']**2,axis=1)))
 vp=area*gap/3;moment=vp*(hj+gap/4)
 out=dict(body='J91_REBALANCED_C434_G18',evidence='binary64 diagnostics, not exact intervals',root_face_index=j,root_material_labels=[z['labels'][i] for i in cy],bar=b,area=float(area),junior_support=float(hj),elder_support=float(he),merge_support=float(rd),necessary_raise_fixed_center=float(gap),necessary_relative_raise=float(gap/hj),zero_raise_necessary_center_motion=float(gap/2),old_U_radius=float(R),mandatory_pyramid_volume=float(vp),mandatory_pyramid_moment=float(moment),opposite_added_volume_lower_bound=float(moment/R),total_added_volume_lower_bound=float(vp+moment/R),fixedchain4=[])
 for k in range(4):
  name=f'J94_FIXEDCHAIN_4_{k}.json';path=ROOT/name
  if not path.exists():continue
  d=json.loads(path.read_text());w=np.array(d['apexes']);zz=hullpoly(np.vstack([old,w]));rr=report(zz)
  out['fixedchain4'].append(dict(state=name,state_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),V=rr['V'],E=rr['E'],F=rr['F'],stable_count=len(rr['S']),unstable_material_labels=[zz['labels'][i] for i in rr['U']],P=rr['P'],Q=rr['Q'],centroid=rr['centroid'],volume=rr['volume']))
 text=json.dumps(out,indent=2)+'\n';(ROOT/'J95_BARRIER_DIAGNOSTICS.json').write_text(text);print(text,end='')
 print('J95_CONDITIONAL_BARRIER_NUMERICAL_DIAGNOSTICS_ONLY')
if __name__=='__main__':main()
```

## recount95.py
853B; SHA2561e984896a8ca21352039adc60e852a4c69017fc1bb6609dfe6da50bd0afd249f.
```python
"""Recount stored numerical states; no strict/weak exact claim is made."""
from pathlib import Path
import json
import numpy as np
from surgery94 import initial
from envelope91 import hullpoly
from j90 import report
ROOT=Path(__file__).resolve().parent
NAMES=['J95_C440_OWN','J95_C444_OWN','J95_SQRT_C440']+[f'J94_FIXEDCHAIN_4_{k}' for k in range(4)]
old,_,_=initial()
out=[]
for name in NAMES:
 d=json.loads((ROOT/(name+'_STATE.json')).read_text())
 z=hullpoly(np.vstack([old,np.array(d['apexes'])]));r=report(z)
 out.append(dict(name=name,report=r,unstable_material_labels=[z['labels'][i] for i in r['U']]))
 print(name,'VEF',r['V'],r['E'],r['F'],'SU',len(r['S']),len(r['U']),'P',len(r['P']),'Q',len(r['Q']))
(ROOT/'J95_STORED_STATE_RECOUNTS.json').write_text(json.dumps(out,indent=2)+'\n')
print('J95_STORED_NUMERICAL_STATES_RECOUNT_PASS_NOT_EXACT')
```

## J95_C440_OWN_STATE.json
563B; SHA2566bd77511f193284b45e9c924f0118f5db382a16a84cd50a9982a572516210278.
```json
{"apexes":[[-0.7651236718223563,0.15640139403727057,0.0428107852946184],[0.29490817002268677,-0.47045442399515947,0.22011206299572744],[0.571151662480989,-0.34572691758323887,-0.7072962995479346],[-0.33239958024484934,0.45624097226979177,0.19674121393532626],[-0.36183324397761774,0.4490486352490561,0.1671120743268961],[-0.26434200772181327,0.5141883698709401,0.17388975946672858]],"base":"J90_DETACHED_C390_G8","frame_shift":[0.0014912244454173174,0.0001912863373598814,0.0004052204425441016],"loss_power":1.0,"policy":"two","source_state":"J95_C440_OWN.json"}
```

## J95_C444_OWN_STATE.json
628B; SHA256ee23eca8cf31f56c9726a6b8f43b2b834e2d0c41228e9e649d2877386c497a87.
```json
{"apexes":[[-0.7653838467959863,0.1564058685548689,0.042674972889633886],[0.2948128349801388,-0.47063061582829546,0.22048540084994928],[0.5755903315749471,-0.3465817076365398,-0.7056993517008625],[-0.34040443362635475,0.45127972123551485,0.19693040593401084],[-0.36913775768781093,0.44228610535007146,0.16618609661694705],[-0.30167706558758284,0.4660924691922235,0.22211382544341732],[-0.3150756777843668,0.48807584306097856,0.16084778220713275]],"base":"J90_DETACHED_C390_G8","frame_shift":[0.0014912244454173174,0.0001912863373598814,0.0004052204425441016],"loss_power":1.0,"policy":"free","source_state":"J95_C444_OWN.json"}
```

## J95_SQRT_C440_STATE.json
563B; SHA25606e5c240fa8fd94658e36dfa11c5c622c4ad2ffd813fdf276854f6122f552870.
```json
{"apexes":[[-0.7652586905263439,0.15625948436420198,0.042631582538920444],[0.29470836670222583,-0.4703318121176281,0.22038183791172317],[0.574117875916664,-0.3452731657172908,-0.7044042382514687],[-0.33510797540611825,0.4532700652511737,0.19846025718170948],[-0.36976918647699414,0.4430816098137929,0.1665664568926839],[-0.25014266744042873,0.5183268025836358,0.1845034122333013]],"base":"J90_DETACHED_C390_G8","frame_shift":[0.0014912244454173174,0.0001912863373598814,0.0004052204425441016],"loss_power":0.5,"policy":"free","source_state":"J95_SQRT_C440.json"}
```

## J94_FIXEDCHAIN_4_0_STATE.json
718B; SHA256c6591b43edfded62351e239fedb24b173d853eb8694fbb52bec52941257bd62a.
```json
{"apexes":[[-0.7652356987946278,0.15623283416186806,0.042623928839944],[0.5824991960022573,-0.32939601045476996,0.2698314452612679],[0.8227174582228788,-0.2791765248650003,-0.6936488705128653],[-0.3351589130454222,0.45339551045687226,0.19851259991671796],[-0.36985730823321517,0.44319839500303476,0.1666069122478483],[-0.3366811731788511,0.5056619937845976,0.24770868086144132],[-0.28936033492367125,0.5599310405857153,0.2041793581018491],[-0.23634199043486004,0.6060665149120391,0.15642872798549756],[-0.17838520407606198,0.6431483359511696,0.10515848143107186]],"base":"J90_DETACHED_C390_G8","frame_shift":[0.0014912244454173174,0.0001912863373598814,0.0004052204425441016],"source_state":"J94_FIXEDCHAIN_4_0.json"}
```

## J94_FIXEDCHAIN_4_1_STATE.json
653B; SHA2563bc15c92c8193c164923b05a22abac666d0a60466e570a99e7a56cbd4289a8c0.
```json
{"apexes":[[-0.7652356987946174,0.15623283416188188,0.042623928839944],[0.5753429804426221,-0.34505449585795767,0.2609961127327605],[0.81992756385154,-0.2896951848226842,-0.6991202042985162],[-0.3351589130454222,0.45339551045687226,0.19851259991671796],[-0.36985730823321517,0.44319839500303476,0.1666069122478483],[-0.3366811731788511,0.5056619937845976,0.24770868086144132],[-0.2647571157164484,0.5848186121327336,0.1907029506030009],[-0.18077827876645758,0.6473402380659018,0.12479596575666306]],"base":"J90_DETACHED_C390_G8","frame_shift":[0.0014912244454173174,0.0001912863373598814,0.0004052204425441016],"source_state":"J94_FIXEDCHAIN_4_1.json"}
```

## J94_FIXEDCHAIN_4_2_STATE.json
716B; SHA256961b7dc748860c5c700f752f1def1c7de9ed6b8c47605b9ab126b0303587b428.
```json
{"apexes":[[-0.7652356987946174,0.15623283416188205,0.042623928839944],[0.5744059704518115,-0.3474653038028298,0.2597426828783162],[0.8195407377943089,-0.29227648471627754,-0.7001620133062695],[-0.3351589130454222,0.45339551045687226,0.19851259991671796],[-0.36985730823321517,0.44319839500303476,0.1666069122478483],[-0.3366811731788511,0.5056619937845976,0.24770868086144132],[-0.2839500695159877,0.5664679689182375,0.205854388967876],[-0.22413791979095593,0.6183472972811318,0.15875299557330425],[-0.15816657526833963,0.6600283959465938,0.10714075796561746]],"base":"J90_DETACHED_C390_G8","frame_shift":[0.0014912244454173174,0.0001912863373598814,0.0004052204425441016],"source_state":"J94_FIXEDCHAIN_4_2.json"}
```

## J94_FIXEDCHAIN_4_3_STATE.json
717B; SHA2564efc1d8c74a4f7cd9b0f1503436da3ab22fa383eaee1e742a967be6200d0840e.
```json
{"apexes":[[-0.7652356987946249,0.1562328341618673,0.042623928839944],[0.586761714326385,-0.3483264049296481,0.2590212237055468],[0.8254735011899967,-0.2906117750270328,-0.6954736418450445],[-0.3351589130454222,0.45339551045687226,0.19851259991671796],[-0.36985730823321517,0.44319839500303476,0.1666069122478483],[-0.3366811731788511,0.5056619937845975,0.24770868086144132],[-0.27221893582537376,0.5834650624881977,0.18214262764172698],[-0.19598968235701647,0.6447292214895923,0.10780135426885538],[-0.11008980253781102,0.6867245852673567,0.026837885413904784]],"base":"J90_DETACHED_C390_G8","frame_shift":[0.0014912244454173174,0.0001912863373598814,0.0004052204425441016],"source_state":"J94_FIXEDCHAIN_4_3.json"}
```
