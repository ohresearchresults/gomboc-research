# material-6364a5fdd035

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Reference-to-mass homotopy recovery part1/2

This is a useful finite method and three exact non-record control bodies, NOT own110. The whole numerical continuation requires both parts. Exact reconstruction of the rational physical/reference bodies needs only this part plus exact_audit.py ([internal-source-reference]) and reference_audit.py ([internal-source-reference]). The original literal W51 input is also in the latter material. No FULL76 or original sandbox is required.

## Findings and scope
A free110 cell with U0 and stable facet2 of the literal W51 body was used instead of the excluded original stable root3. In the central projective/affine chart, the reference is lambda times the actual homogeneous centroid, with the original prescribed point fixed at0. A local SLSQP continuation retained positive escape margins at the free reference and reached lambda .33705795265517735. This is NOT a completion fraction and NOT own110. Allowing free physical vertex deformation with an intrinsic affine reference anchor reached a retained lambda .4570579526551701. Only three completed local cycles of the latter run are claimed; the longer requested run was interrupted by the local tool time limit. A further smaller-trust attempt was also interrupted and did not preserve a better accepted point.

The intrinsic-anchor formulation is important: set a(p)=sum w_i p_i with fixed positive weights summing to1, and c_ref=lambda*c_uniform+(1-lambda)*a(p). Translation moves both a and c uniformly, so an arbitrary translation cannot counterfeit lambda progress. A formulation with freely moving vertices and a fixed ambient origin would have that defect. Mean and scale gauges, full triangle convexity inequalities and area lower bounds were used numerically. None of these finite experiments excludes larger deformations or another chart.

Every rational freeze below has V31/E87/F58,C174, prescribed-reference strict110, additional weak000 and all primitive zeros000. But at its ACTUAL homogeneous centroid the classes are respectively[5,12,15], [8,14,20], [8,14,20], all with weak000/primitive000. The last body's actual main P is .1367366534678078 and main Q .7449413758770113. Thus the reference homotopy did not remove the true own-mass landscape defects. Do not describe lambda gain as a record or a new own110 construction.

## Exact controls
Each compact JSON line is UTF-8/LF with final newline. Decimal denominator100000000 is literal, not an uncertainty tolerance.

mass_homotopy_raw_G8.json,1054bytes,SHA ca2311421cc372cae8fda045b6301d9a799257c824ada4b179daeaec666848af:
```json
{"denominator":100000000,"name":"mass_homotopy_raw_G8","points":[[-374073705,-213529433,-15174672],[-373512156,-170473388,-69229496],[-317985449,-159893949,-85316699],[-32250608,10380613,-32081336],[-74774445,-98842557,-121569131],[-50562259,-29818095,-88737175],[-65404385,-54392944,-107743540],[-48204919,2671229,-53614361],[-10041593,-29285110,-65361612],[-23456701,-160118295,-98145297],[11760567,-118599048,-78113089],[18450201,-69186690,-62923485],[24613918,-34009006,-38154202],[6724054,-7221819,-27349070],[45962070,-29732489,-6441371],[42198387,-6684867,37497838],[65958081,-34385252,25596706],[82345504,-44438753,57694064],[90258314,-52474000,86742726],[88463179,-107445725,29284580],[94838407,-64422036,113085063],[96130974,-79962663,138241073],[93093607,-100290471,164532271],[82448422,-127203326,192083175],[59963542,-160633538,217429755],[22349312,-194500042,234098035],[-26418726,-225555182,236843535],[-80922076,-248316186,225503962],[-137900426,-262000478,201992779],[-199684149,-266639243,164855526],[-268237564,-258332655,108405022]]}
```
mass_homotopy_raw_G8.reference.json,76bytes,SHA db4d5e47187c72cd10c20ad222509d12fa1b9ea4e91f44e497c3dcc2584f0a6c:
```json
{"reference":["-450179/2500000","-28289981/100000000","4396683/100000000"]}
```

mass_homotopy_trust_G8.json,1041bytes,SHA951c202847f68c674997df09bee1eee73bc7d0ec5217d8454fe99cf08ea94c96:
```json
{"denominator":100000000,"name":"mass_homotopy_trust_G8","points":[[-167454744,-153146418,64561871],[-180590855,-139398812,38150434],[-160118498,-132864540,22152929],[-30165092,5985819,-24027434],[-47940895,-88736165,-49873504],[-40262247,-37771168,-54256025],[-47739728,-59184671,-56341928],[-43184633,-5777213,-36768400],[-8238978,-31628911,-46185834],[-13289807,-115800742,-30670193],[7507762,-92872398,-34481007],[13581912,-60744142,-38611306],[20394889,-30996102,-31154982],[6057588,-6882642,-25157280],[39357759,-23758701,-10841993],[39451257,211465,25627071],[56572432,-25293529,12992699],[69277360,-32558191,38163143],[74583867,-38931003,61521477],[61249734,-80325382,20751190],[75837551,-48842666,82126099],[73483167,-61300432,100571321],[67052746,-76459672,118116502],[54936827,-94528909,134244504],[36363246,-114073579,146581566],[12333892,-131324771,153222482],[-13379738,-145136087,152951580],[-38347684,-154491294,147737317],[-62310820,-160241353,139036469],[-87376195,-163191819,126479006],[-115940041,-162733919,107909329]]}
```
mass_homotopy_trust_G8.reference.json,74bytes,SHA2d8050c4094d74c5c951ddca50cbcd56812fbe59cf85cdcfdc6f8d80529be627:
```json
{"reference":["-4498241/50000000","-1424899/5000000","5257587/50000000"]}
```

vertex_homotopy_G8.json,1037bytes,SHA aace9b609e9091306a42e095f74c97297dd9764b40aa0789ac1338cdc901c7b3:
```json
{"denominator":100000000,"name":"vertex_homotopy_G8","points":[[-167671540,-153108721,64312701],[-180187557,-138709419,37376845],[-160342100,-132864344,21464378],[-32258185,6632731,-24651637],[-48199339,-88400502,-48576218],[-41919188,-36368900,-56759335],[-49036594,-61452306,-57368328],[-41866176,-6148022,-37891291],[-8285523,-28302972,-48950410],[-16682671,-116842740,-23965092],[5883897,-91505254,-34202166],[18083181,-64632752,-39743340],[19239458,-29562634,-30113207],[3945718,-7271496,-28053501],[43255851,-26419788,-5959776],[37905237,-403764,24838427],[56371059,-25131319,13308567],[69610756,-32456014,38147328],[74814104,-38846700,61595887],[61499078,-76168631,24644785],[75958639,-48770007,82245880],[73504474,-61226132,100704221],[66973384,-76366546,118227889],[55117783,-95119304,133601324],[36806731,-115211845,145250511],[14779947,-134505512,154124796],[-12671998,-145914228,151852351],[-38260833,-154087118,147117498],[-62122528,-159433990,138364799],[-87040282,-162286077,125897828],[-115502745,-161913640,107685391]]}
```
vertex_homotopy_G8.reference.json,78bytes,SHA a74c8809828aa6fe309f12bacb0775e64d2ea566732660e1df3d264b0c2f28ab:
```json
{"reference":["-13551769/100000000","-19154347/50000000","1360333/10000000"]}
```

## Exact reconstruction/verification
Save the inputs and reference files, then run this complete source as verify_homotopy_controls.py:
```python
from pathlib import Path
import json
from exact_audit import audit
from reference_audit import reference_audit
names=['mass_homotopy_raw_G8','mass_homotopy_trust_G8','vertex_homotopy_G8']
for name,expected in zip(names,[[5,12,15],[8,14,20],[8,14,20]]):
    d=json.loads(Path(name+'.json').read_text());r=json.loads(Path(name+'.reference.json').read_text())
    a=audit(d['points'],d['denominator']);b=reference_audit(d,r['reference'])
    assert [a[k] for k in ['V','E','F']]==[31,87,58] and a['strict']==expected
    assert a['additional_weak']==a['primitive_zero']==[0,0,0]
    assert b['strict']==[1,1,0] and b['additional_weak']==b['primitive_zero']==[0,0,0]
    for suffix,obj in [('.audit.json',a),('.reference.audit.json',b)]:
        Path(name+suffix).write_text(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n')
    print('HOMOTOPY_CONTROL_EXACT_PASS',name,a['strict'],b['strict'])
```
Command: python -B -S verify_homotopy_controls.py.
Expected own audit files, bytes,SHA:
raw18597,005e2546fac2517bb32edbb320a5da4a73ed0d95117fb0d0383c518c6576c1d9;
trust21091,0693d470b672be53180b4ec94b0151b1270a66adc6fed4d9f80bdfb3475f00b1;
vertex21149,27c8dd795c6c5332a85b65cca1d6a32aa1df9145a3096f9b101deb0e1539f061.
Expected reference audits, bytes,SHA:
raw717,d5d4a4fc420cf1daacfbb2072f767230ede09501a0e025de2b4e5402e2cd07f7;
trust711,65392cd491de0cd16052ad46e90a5d8d6ecc399f84e6c6fdb1ba0e58aee0f6b6;
vertex715,02753996913c9b195ed922da31cd2f3214b1a610d32e66a3d743ff37cdfc015e.

## Complete reference_mass_homotopy.py
5126bytes,SHA1b863f92632fb7dfe3f554275d66c1f07f8589cf36388a91194338e8ab28771b.
The minimal exact input reference_raw_minimal.json is76bytes,SHA f8917c1641a3234a1aa92c04aa50b5ac6ea787700d219f055f17557c69c3de32:
```json
{"reference":["74124239/95515479","81020201/73473032","-7288828/45992441"]}
```
This preserves all fields used by the numerical code. Earlier reference_raw.json also contained unused cell-plane metadata; it is not claimed byte-identical to this minimal recovery input.

Numerical environment: Python3.13.5, NumPy2.3.5,SciPy1.17.0,Torch2.10.0+cpu, float64 andthreads1. Commands:
```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python reference_mass_homotopy.py --reference reference_raw_minimal.json --steps 250 --out mass_homotopy_raw
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python reference_mass_homotopy.py --reference reference_raw_minimal.json --steps 70 --cycles 18 --trust .05 --initial mass_homotopy_raw/theta.npy --out mass_homotopy_trust
```
Part2 supplies the exact binary64 input pins for the trust and vertex continuations, avoiding reliance on cross-version optimizer byte replay. The first unbounded-trust attempt stopped with a line-search failure; only its best feasible lambda .20785276920935 is retained. The trust sequence reached .33705795265517735, not1.
```python
"""Finite reference-to-own-mass homotopy in an incidence-preserving projective chart.
Discovery only: lambda<1 is a free-reference body, never an own110 construction.
Requires the literal W51 input, exact_audit.py, and a reference JSON.
NumPy/SciPy/Torch float64; every candidate needs an exact freeze/audit.
"""
from pathlib import Path
from fractions import Fraction
import argparse,json,time
import numpy as np
import scipy
from scipy.optimize import minimize
import torch
from exact_audit import audit

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def run(input,reference,out,steps=400,margin=1e-5,initial=None,cycles=1,trust=.08):
    data=json.loads(Path(input).read_text());ref=json.loads(Path(reference).read_text());c0=np.array([float(Fraction(v)) for v in ref['reference']]);au=audit(data['points'],data['denominator']);p=np.array(data['points'],float)/data['denominator']-c0
    ids=au['vertices'];mp={v:i for i,v in enumerate(ids)};faces=np.array([[mp[v] for v in f['vertices']] for f in au['facets']]);assert all(len(f['vertices'])==3 for f in au['facets']);base=torch.tensor(p[ids]);ur=mp[0];sr=2
    out=Path(out);out.mkdir(parents=True,exist_ok=True);history=[];cache={};best=-1;start=time.time()
    def quantities(t):
        zero=t[0]*0;A=torch.stack((torch.stack((t[0].exp(),zero,zero)),torch.stack((t[2],t[1].exp(),zero)),torch.stack((t[3],t[4],(-t[0]-t[1]).exp()))));b=t[5:8];lam=t[8];den=1+base@b;p=(base@A.T)/den[:,None]
        a,v,w=p[faces[:,0]],p[faces[:,1]],p[faces[:,2]];d=(a*torch.linalg.cross(v,w)).sum(1);c=((a+v+w)*d[:,None]).sum(0)/(4*d.sum());cr=lam*c;x=p-cr;n=torch.linalg.cross(v-a,w-a);h=(n*(a-cr)).sum(1);q=n/h[:,None]
        vals=[]
        for z,root in [(x,ur),(q,sr)]:
            r=(z*z).sum(1);M=z@z.T/r[:,None]-1-torch.eye(len(z))*1e12;mm=M.max(1).values;vals.append(torch.cat((mm[:root],mm[root+1:]))-margin)
        constraints=torch.cat((*vals,den-.02));return constraints,p,c,cr,A,b
    def evaluate(z):
        if cache.get('x') is not None and np.array_equal(cache['x'],z):return cache['v'],cache['j']
        t=torch.tensor(z,requires_grad=True);v=quantities(t)[0];j=torch.autograd.functional.jacobian(lambda s:quantities(s)[0],t,vectorize=True);cache.update(x=z.copy(),v=v.detach().numpy(),j=j.detach().numpy());return cache['v'],cache['j']
    def objective(z):return -z[8]+1e-7*np.dot(z[:8],z[:8])
    def gradient(z):return np.r_[2e-7*z[:8],-1.]
    def cb(z):
        nonlocal best
        vv=evaluate(z)[0];rec=dict(iteration=len(history),lambda_value=float(z[8]),min_constraint=float(vv.min()),norm=float(np.linalg.norm(z[:8])));history.append(rec)
        if vv.min()>=-1e-9 and z[8]>best:
            best=z[8];v,p,c,cr,A,b=quantities(torch.tensor(z));np.save(out/'theta.npy',z);np.save(out/'points.npy',p.detach().numpy());np.save(out/'centroid.npy',c.detach().numpy());np.save(out/'reference.npy',cr.detach().numpy());(out/'best.json').write_text(json.dumps(rec,sort_keys=True,indent=2))
        if len(history)%20==0:print('MASS_HOMOTOPY',json.dumps(rec),flush=True)
    z=np.zeros(9) if initial is None else np.load(initial);cb(z)
    bounds=[(-2,2)]*2+[(-5,5)]*3+[(-3,3)]*3+[(0,1)]
    for cycle in range(cycles):
        local=[(max(a,v-trust),min(b,v+trust)) for v,(a,b) in zip(z,bounds)] if cycles>1 else bounds
        result=minimize(objective,z,jac=gradient,method='SLSQP',bounds=local,constraints={'type':'ineq','fun':lambda z:evaluate(z)[0],'jac':lambda z:evaluate(z)[1]},callback=cb,options={'maxiter':steps,'ftol':1e-12,'disp':False})
        vv=evaluate(result.x)[0]
        if vv.min()>=-1e-9 and result.x[8]>=z[8]-1e-12:z=result.x.copy()
        else:
            d=result.x-z
            for k in range(1,24):
                trial=z+d*2**-k
                if evaluate(trial)[0].min()>=-1e-9 and trial[8]>z[8]:z=trial;break
        cb(z)
        print('HOMOTOPY_TRUST',cycle,float(z[8]),float(evaluate(z)[0].min()),flush=True)
        if z[8]>.99999999:break
    cb(z);(out/'history.json').write_text(json.dumps(history,sort_keys=True,separators=(',',':'))+'\n');ans=dict(success=bool(result.success),message=result.message,best_feasible_lambda=float(best),last_lambda=float(result.x[8]),last_slack=float(evaluate(result.x)[0].min()),iterations=int(result.nit),steps=steps,margin=margin,initial=initial,cycles=cycles,trust=trust,reference=ref,input=data,numpy=np.__version__,scipy=scipy.__version__,torch=torch.__version__,seconds=time.time()-start)
    (out/'run.json').write_text(json.dumps(ans,sort_keys=True,indent=2)+'\n');print('MASS_HOMOTOPY_FINITE',json.dumps({k:v for k,v in ans.items() if k not in ('input','reference')}),flush=True)
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',default='W51_ROBUST_G3.json');ap.add_argument('--reference',default='reference_raw.json');ap.add_argument('--out',default='mass_homotopy');ap.add_argument('--steps',type=int,default=400);ap.add_argument('--margin',type=float,default=1e-5);ap.add_argument('--initial');ap.add_argument('--cycles',type=int,default=1);ap.add_argument('--trust',type=float,default=.08);run(**vars(ap.parse_args()))
```
