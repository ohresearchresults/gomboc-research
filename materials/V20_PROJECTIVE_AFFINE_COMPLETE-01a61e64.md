# material-01a61e64e6c3

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# V20 projective-affine actual-centroid search: complete recovery capsule

## Identity and evidence boundary
Finite coordinator experiment on THREE distinct rational seeds COS10G5, COS100G5, RAD100G5, not aliases. The complete 60 coordinate rows and denominator100000 are literal below. Source fully read: [internal-source-reference], SHA256 b9f00fe751e074e4d6a1dbabbbdbafaa51fb931f0d38eca0260504603f872775. Parent direction [internal-source-reference]. Earlier projective-affine experiments on other bodies exist; this does not introduce the family. No new strict110 body or global exclusion. Accepted C622 endpoint unchanged.

Complete runnable method and literal inputs, not an accepted new construction. Binary64 S/U screens are not rational certification of H or weak equilibria. Facets use SciPy oriented triangulation; these were the simplicial V20/C108 source seeds, and no new exact facet census was performed here.

## Reconstruction
Write each source block to its indicated UTF-8 filename with final newline. Directly observed runtime Python3.13.5, NumPy2.3.5, SciPy1.17.0. Earlier transient summaries naming Python3.11.8/NumPy1.24/SciPy1.14 or different hashes/totals are superseded by actual file/JSON inspection.
```
OPENBLAS_NUM_THREADS=1 python search.py --runs 24 --iterations 150 --seed 20260921 --out first
OPENBLAS_NUM_THREADS=1 python basin_search.py --runs 12 --iterations 180 --seed 20260922 --out basin
sha256sum search.py basin_search.py first/inputs.json first/initial.json first/runs.json first/best.json basin/runs.json basin/best.json
```
First execution completed24, marker FINITE_PROJECTIVE_AFFINE_SEARCH_COMPLETE24,1908 iterations,32697 evaluations. Second actual command requested18 but interrupted after12 completed rows0..11:946 iterations,28728 evaluations. --runs12 reconstructs this completed window, expected FINITE_BASIN_SEARCH_COMPLETE12. Timing not in JSON. Platform-independent last-bit optimizer trajectories/Qhull ordering not asserted. Output hashes identify observed runtime outputs.

Observed bytes/SHA256:
search.py 7664 5194bdbf8f68d0db8126c1a12f2c4f343b39c039844c66b95d4a98fa97998d2f
basin_search.py 2757 43ae6a7ff20455a6ef89c0465055948f9149a96869d67711807bc55e3c3fee91
first/inputs.json 1287 25d2d885fd4bba10beff915e4166935a85585f9932b4d939ea767cb0e31632bb
first/initial.json 8404 6cf532498e51c476121dc6fdf4e93231567c4d658e92542b26c0f8a925a82c5a
first/runs.json 86458 7c1e9a733808a7f852fed855c7f87228f3761080da34fca6b3322d8b5fbc2e06
first/best.json 639 5afa18ec6b64c6bbae81554b7582792d3778ac88b2f52ca05c30d62fcc0ec578
basin/runs.json 51840 c21b41ed7777153fa77226c7f1664aa695cd86883740137e159d87e2168fd2ba
basin/best.json 609 ee164aef589481c6a8b13288c8e226099f315663d8eb673eb271ba914aedeb1f

## Findings
No numerical110 in either window. Local cosine escape constraints can nearly be satisfied while a deep polar full-chord persistence bar remains: first row4 COS100G5 S3/U1,minP3.812163070660867e-5,minQ-1.184802395584893e-5,largest polar log birth/death3.137493443333897. Runtime triangulation indices are not canonical exact face IDs.

Basin objective reduced the large polar bar but produced many physical/polar roots. EP/EQ=sum squared log persistence ratios. Actual selected basin rows: row0 COS10G5 weight1 S10/U9 EP0.16787933765505858 EQ0.17334754288650375; row3 COS10G5 weight10 S7/U14 EP0.02804787299764847 EQ0.8332244507572616; row6 COS10G5 weight100 S4/U13 EP0.006154711146833082 EQ2.0551550712923143; row11 RAD100G5 weight1 S12/U8 EP0.1496919940217892 EQ0.12251129416243538. Finite failure, not family exclusion. Transient summaries reporting basin S3/U2,S5/U5,1031iterations/24813evaluations or incompatible rows are not source evidence.

## search.py
```python
#!/usr/bin/env python3
"""Finite actual-centroid projective/affine search of three exact V20 solids.
Reconstruct inputs from the literal DATA below. No external data or network.
python search.py --runs 24 --iterations 150 --seed 20260921
Produces inputs.json, initial.json, runs.json and best.json; numeric screening only.
"""
import argparse,json,math,time
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize

DATA={
'COS10G5':[[-98118,8147,-10630],[-66044,-26891,28593],[-46032,-38770,40224],[-38738,41027,-36892],[-28872,-43776,46305],[-10902,-45866,48514],[-2274,43778,-36138],[8119,-44109,47046],[20942,26392,-28295],[22866,-39785,43375],[35135,-35371,35997],[38358,2434,-28194],[45064,-26662,28595],[46973,15575,-14388],[51213,-20968,5182],[51037,-21191,19147],[50617,15839,-1153],[54367,-15980,10230],[54644,3922,-806],[55269,-3532,8135]],
'COS100G5':[[-98061,8200,-10689],[-66037,-26956,28621],[-46027,-38814,40230],[-38778,41049,-36924],[-28877,-43883,46243],[-10872,-45707,48677],[-2277,43821,-36158],[8108,-44165,47014],[20992,26427,-28362],[22866,-39841,43329],[35141,-35325,36025],[38200,2595,-27938],[45042,-26701,28588],[46932,15478,-14409],[51256,-20962,5170],[51018,-21200,19157],[50707,15714,-1367],[54357,-15891,10313],[54650,3959,-742],[55284,-3586,8066]],
'RAD100G5':[[-98268,8337,-10637],[-65722,-27213,28769],[-46058,-38923,40132],[-38883,41183,-36933],[-28852,-43678,46422],[-10845,-45797,48550],[-2319,43834,-36160],[8068,-44096,47032],[21053,26468,-28449],[22830,-39874,43237],[35086,-35233,36015],[38936,2326,-27779],[44937,-26714,28532],[46944,15577,-14413],[51272,-20893,5195],[50900,-21180,19135],[50607,15632,-1432],[54234,-15825,10352],[54536,3904,-746],[55168,-3620,8024]]}

def mass(x,f):
    t=x[f]; ds=np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2])); d=ds.sum()
    if not d>0:raise ValueError('nonpositive oriented volume')
    return d/6, (ds[:,None]*t.sum(axis=1)).sum(axis=0)/(4*d)

def graph(f,n):
    owners={}
    for fi,tri in enumerate(f):
        for a,b in zip(tri,np.roll(tri,-1)):
            owners.setdefault(tuple(sorted((int(a),int(b)))),[]).append(fi)
    if any(len(v)!=2 for v in owners.values()):raise ValueError('non-manifold hull')
    e=np.array(list(owners),int); qe=np.array(list(owners.values()),int)
    def adj(es,N):
        mat=np.full((N,max(np.bincount(es.ravel(),minlength=N))),-1,int)
        ls=[[] for _ in range(N)]
        for a,b in es:ls[a].append(b);ls[b].append(a)
        for i,z in enumerate(ls):mat[i,:len(z)]=z
        return mat
    return e,qe,adj(e,n),adj(qe,len(f))

def escape(x,ad):
    d=x[ad]-x[:,None,:]
    co=np.einsum('ij,ikj->ik',x,d)/(np.linalg.norm(x,axis=1)[:,None]*np.linalg.norm(d,axis=2))
    co[ad<0]=-np.inf
    vals=co.max(axis=1); root=int(np.argmax(np.einsum('ij,ij->i',x,x)))
    return vals,root

def persistence(x):
    # Full chord graph, exact mathematical formula evaluated in binary64.
    n=len(x); i,j=np.triu_indices(n,1); b=np.einsum('ij,ij->i',x,x)
    a=b[i]; c=b[j]; z=np.einsum('ij,ij->i',x[i],x[j]); d=a+c-2*z
    w=np.where(z>=a,a,np.where(z>=c,c,np.maximum(0,(a*c-z*z)/np.maximum(d,1e-300))))
    pa=list(range(n)); pk=list(range(n)); bars=[]
    def root(k):
        while pa[k]!=k:pa[k]=pa[pa[k]];k=pa[k]
        return k
    for k in np.argsort(-w,kind='stable'):
        u,v=root(int(i[k])),root(int(j[k]))
        if u==v:continue
        if (b[pk[u]],-pk[u])<(b[pk[v]],-pk[v]):u,v=v,u
        birth=float(b[pk[v]]); death=float(w[k]); gap=max(0,math.log(birth/max(death,1e-300)))
        if gap>1e-12:bars.append({'peak':pk[v],'edge':[int(i[k]),int(j[k])],'log_ratio':gap})
        pa[v]=u
    return bars

class Model:
    def __init__(self,name):
        self.name=name; x=np.asarray(DATA[name],float)/100000
        h=ConvexHull(x); f=h.simplices.copy()
        for k,tri in enumerate(f):
            if np.dot(np.cross(x[tri[1]]-x[tri[0]],x[tri[2]]-x[tri[0]]),h.equations[k,:3])<0:f[k,[1,2]]=f[k,[2,1]]
        self.f=f; self.raw=x; self.v,self.c=mass(x,f); self.x=x-self.c
        self.e,self.qe,self.ad,self.qad=graph(f,len(x))
    def body(self,z):
        r=np.asarray(z[:3]); q=r/(1+max(0,float(np.max(self.x@r))))
        den=1-self.x@q
        y=self.x/den[:,None];vol,c=mass(y,self.f);y-=c
        a,b,s,t,u=z[3:]
        A=np.array([[math.exp(a),s,t],[0,math.exp(b),u],[0,0,math.exp(-a-b)]])
        y=y@A.T
        tri=y[self.f]; n=np.cross(tri[:,1]-tri[:,0],tri[:,2]-tri[:,0]);h=np.einsum('ij,ij->i',n,tri[:,0])
        if min(h)<=0:raise ValueError('centroid/support numerical failure')
        Q=n/h[:,None]
        return y,Q,dict(q=q.tolist(),A=A.tolist(),minimum_denominator=float(min(den)),projective_centroid=c.tolist(),projective_volume=float(vol))
    def assess(self,z,detail=False):
        y,Q,info=self.body(z); p,pr=escape(y,self.ad);s,sr=escape(Q,self.qad)
        pm=np.delete(p,pr);sm=np.delete(s,sr)
        out=dict(S=int(sum(s< -1e-10)),U=int(sum(p< -1e-10)),minP=float(pm.min()),minQ=float(sm.min()))
        if detail:out.update(info,points=y.tolist(),Pbars=persistence(y),Qbars=persistence(Q),physical_scores=p.tolist(),polar_scores=s.tolist())
        return pm,sm,out

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--runs',type=int,default=24);ap.add_argument('--iterations',type=int,default=150);ap.add_argument('--seed',type=int,default=20260921);ap.add_argument('--out',default='.');args=ap.parse_args()
    dest=Path(args.out);dest.mkdir(parents=True,exist_ok=True);rng=np.random.default_rng(args.seed)
    models=[Model(k) for k in DATA];base={m.name:m.assess(np.zeros(8),True)[2] for m in models}
    (dest/'inputs.json').write_text(json.dumps(DATA,separators=(',',':')))
    (dest/'initial.json').write_text(json.dumps(base,sort_keys=True,separators=(',',':')))
    best={m.name:(float('inf'),np.zeros(8)) for m in models};records=[];started=time.time()
    for run in range(args.runs):
        m=models[run%3];weight=[.1,1,10,100][(run//3)%4];margin=[1e-5,1e-4][(run//12)%2]
        z=np.zeros(8) if run<12 else best[m.name][1]+rng.normal(0,[.8,.8,.8,.2,.2,.3,.3,.3])
        def fun(t):
            try:
                p,s,_=m.assess(t);val=weight*np.square(np.minimum(p-margin,0)).sum()+np.square(np.minimum(s-margin,0)).sum()
                return float(val)
            except (ValueError,FloatingPointError):return 1e9
        res=minimize(fun,z,method='L-BFGS-B',bounds=[(-12,12)]*3+[(-2,2)]*2+[(-4,4)]*3,options={'maxiter':args.iterations,'ftol':1e-15,'gtol':1e-9,'maxls':40})
        _,_,audit=m.assess(res.x,True);quality=max(0,-audit['minP'])+max(0,-audit['minQ'])
        if quality<best[m.name][0]:best[m.name]=(quality,res.x.copy())
        row=dict(run=run,body=m.name,weight=weight,margin=margin,start=z.tolist(),x=res.x.tolist(),objective=float(res.fun),iterations=int(res.nit),evaluations=int(res.nfev),success=bool(res.success),message=str(res.message),audit=audit)
        records.append(row);(dest/'runs.json').write_text(json.dumps(records,sort_keys=True,separators=(',',':')))
        print(json.dumps({k:row[k] for k in ['run','body','weight','objective','iterations','evaluations']}),json.dumps({k:audit[k] for k in ['S','U','minP','minQ']}),flush=True)
        (dest/'best.json').write_text(json.dumps({k:{'quality':v[0],'x':v[1].tolist()} for k,v in best.items()},sort_keys=True,separators=(',',':')))
        if audit['S']==audit['U']==1 and min(audit['minP'],audit['minQ'])>1e-8:print('NUMERIC_110_CANDIDATE_REQUIRES_EXACT_AUDIT',flush=True);break
    print('FINITE_PROJECTIVE_AFFINE_SEARCH_COMPLETE',len(records),'elapsed',time.time()-started,flush=True)
```

## basin_search.py
```python
#!/usr/bin/env python3
"""Basin-aware finite projective-affine continuation. Requires exact search.py.
python basin_search.py --runs 18 --iterations 180 --seed 20260922 --out basin
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from search import Model,DATA,persistence

def energy(model,z,weight,margin=1e-5):
    p,s,a=model.assess(z,True)
    P=sum(b['log_ratio']**2 for b in a['Pbars']);Q=sum(b['log_ratio']**2 for b in a['Qbars'])
    hinge=float(weight*np.square(np.minimum(p-margin,0)).sum()+np.square(np.minimum(s-margin,0)).sum())
    return weight*P+Q+hinge*1e-5

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--runs',type=int,default=18);ap.add_argument('--iterations',type=int,default=180);ap.add_argument('--seed',type=int,default=20260922);ap.add_argument('--out',default='basin');args=ap.parse_args()
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True);rng=np.random.default_rng(args.seed)
    models=[Model(k) for k in DATA];best={m.name:(float('inf'),np.zeros(8)) for m in models};results=[];start=time.time()
    for r in range(args.runs):
        model=models[r%3];w=[1,10,100][(r//3)%3];x=np.zeros(8) if r<9 else best[model.name][1]+rng.normal(0,[.2,.2,.2,.05,.05,.1,.1,.1])
        def fun(z):
            try:return energy(model,z,w)
            except (ValueError,FloatingPointError):return 1e9
        result=minimize(fun,x,method='L-BFGS-B',bounds=[(-20,20)]*3+[(-3,3)]*2+[(-6,6)]*3,options={'maxiter':args.iterations,'maxls':40,'gtol':1e-10,'ftol':1e-15})
        audit=model.assess(result.x,True)[2];EP=sum(b['log_ratio']**2 for b in audit['Pbars']);EQ=sum(b['log_ratio']**2 for b in audit['Qbars']);quality=EP+EQ
        if quality<best[model.name][0]:best[model.name]=(quality,result.x.copy())
        row=dict(run=r,body=model.name,weight=w,start=x.tolist(),x=result.x.tolist(),objective=float(result.fun),EP=EP,EQ=EQ,iterations=int(result.nit),evaluations=int(result.nfev),success=bool(result.success),message=str(result.message),audit=audit)
        results.append(row);(out/'runs.json').write_text(json.dumps(results,sort_keys=True,separators=(',',':')))
        (out/'best.json').write_text(json.dumps({k:{'quality':v[0],'x':v[1].tolist()} for k,v in best.items()},sort_keys=True,separators=(',',':')))
        print(json.dumps({k:row[k] for k in ['run','body','weight','EP','EQ','iterations','evaluations']}),json.dumps({k:audit[k] for k in ['S','U','minP','minQ']}),flush=True)
        if audit['S']==audit['U']==1 and min(audit['minP'],audit['minQ'])>1e-8:print('NUMERIC_110_CANDIDATE_REQUIRES_EXACT_AUDIT',flush=True);break
    print('FINITE_BASIN_SEARCH_COMPLETE',len(results),'elapsed',time.time()-start,flush=True)
```
