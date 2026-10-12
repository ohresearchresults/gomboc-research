# material-41112d93ab63

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J84 convex-union and one-apex nomination — complete source and exact inputs

Scientific parent: N40 literal result figure-0568, fully read SHA2d3cd172d29b4f51eb682c0209272705ebab78420e17c1504c75dee71dabc09d. All36472 bytes of its decoded N40_RECOVER.py were read. The three inputs below exactly match the author's canonical body hashes; these are not new geometries or claims to have replayed all17 older endpoints. A fourth required input, J82_S1_ROBUST_G6_INPUT.json1153B/SHA753b899123a05588f7a566b8f08d08cc6e72636fdbd59bca5c7f465f32bea3ab, is completely preserved in [internal-source-reference]. Supply that material too. No FULL76 or unprovided optimizer is required.

The family is conv(A union(lambda R B+t)), centring each input at its actual filled centroid before transformation. For A45+B22 the combinatorial bound V<=67 implies E<=195,C<=390; for A45+B36, V<=81 implies E<=237,C<=474. For B47 no automatic bound is asserted; the nominator rejects E>249. Classes do not pass to a convex union, and the numerical transition often creates many extra roots.

Completed finite experiments, NOT family exclusions: each B22/B36/B47 scan evaluated2425 points. B22 run0 DE7644 evaluations; B36 run0 DE7644; B47 run0 DE1344 and run3 DE7644. Other programmed runs are not claimed completed. No110. B47 run3's useful own211 nominee retains A material32 plus all47 B material rows, motivating a separate one-apex search. The final source below generalizes the earlier B22/B36 script to all three inputs and imposes E<=249; earlier B22/B36 bodies automatically obeyed that bound. File naming changed from the earlier scripts but the parameter families, seeds, formulas and performed runs are specified here.

One-apex script completed1900 initial probes (90 facet normals times10 heights plus1000 seeded points), then all four programmed DE runs. Total23326 evaluations, no110. Its best numerical211 apex is z=(.9224360479698328,.1762520176600193,.17891477603007044), with remaining Q~.33666580780359767. A competing all-class loss nominee was222 with actual numerical positive P~2.336075777e-11; do not discard that bar. Exact G9 freezes of the union and apex bodies are separately preserved in [internal-source-reference], including their actual own211/weak000 census and exact replay. They are not better than the existing RA40 one-U Q~.328381.

## Environment, commands and evidence boundary
CPython3.13.5,NumPy2.3.5,SciPy1.17.0,one BLAS/OMP thread. These are numerical nomination methods. The1e-13 bar floor and cosine guards are NOT certification tolerances. General nonsimplicial facets are not resolved here; only known inherited B caps are merged. Every promoted endpoint requires the separate exact hull/maximal-facet/mass/SUH/weak/all-positive-bar audit.

Save all fenced sources with final LF. Run:
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python union84.py --body 22 --phase scan
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python union84.py --body 22 --phase de --run 0
Repeat those two commands for --body36; for --body47 run scan and DE --run0 and --run3.
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python apex84.py

Observed markers: J84_UNION_NOMINATION_DONE for the stated seven scan/DE combinations; J84_ONE_APEX_NOMINATION_DONE23326. The source accepts --body 36 with a space, as shown by its parser. Solver outputs include elapsed time, so whole floating report byte hashes are not asserted portable. Seed/range/init formulas and literal exact inputs suffice to repeat the defined search; floating trajectories across environments are not promised identical.

Source manifest:
union84.py7571B/SHA38df89b82ab85714ddf6b01927625b7b758de6a8b70c85254bbad9723df28a2b
apex84.py2125B/SHA6efd97c1240d18752e1735dbd8e74a5869a87bb76ac67e7cc36a923bd202261e
N40_V22_INPUT.json1629B/SHA73d03038beeea75928b5a9335dbcc296338e751be2b5bd873d00e950701ee417
N40_V36_INPUT.json2518B/SHA30473e6bb8927e9e14a7d08b602b30e7b09339204fc9692de65acbe2bffe22bb
N40_V47_INPUT.json2985B/SHA222e77d0d97b19a45432464c0707b4c30ead746e3dda5d9e43ad9e11c259be42
APEX84_CONTINUATION_SEED.json186B/SHAeaf638f6edfffb2c2b37c03aecadab452c3dcb1de96ea932abe85729970865ad
The last file is an explicitly reduced consumer input with the exact actual apex, not the complete original apex84.json report.

## union84.py
```python
"""Seven-parameter convex-union search; all results are numerical nominations."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import sys,json,time
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from scipy.spatial.transform import Rotation
from scipy.optimize import differential_evolution,minimize
ROOT=Path(__file__).resolve().parent

def radial_bars(x,edges):
    e=np.asarray(edges,int);rr=np.einsum('ij,ij->i',x,x);a=x[e[:,0]];d=x[e[:,1]]-a
    t=np.clip(-np.einsum('ij,ij->i',a,d)/np.einsum('ij,ij->i',d,d),0,1)
    lev=np.einsum('ij,ij->i',a+t[:,None]*d,a+t[:,None]*d);par=list(range(len(x)));out=[]
    def find(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return i
    for k in np.argsort(-lev,kind='stable'):
        i,j=find(e[k,0]),find(e[k,1])
        if i==j:continue
        if (rr[i],-i)<(rr[j],-j):i,j=j,i
        dep=max(0.,1-lev[k]/rr[j])
        if dep>1e-13:out.append(dep)
        par[j]=i
    return sorted(out,reverse=True)

def properties(P,cap=None,bars=True):
    H=ConvexHull(P);ts=H.simplices.copy();eq=H.equations
    ri=P.mean(axis=0);v=P[ts]-ri
    d=np.einsum('ij,ij->i',v[:,0],np.cross(v[:,1],v[:,2]))
    sign=np.einsum('ij,ij->i',np.cross(v[:,1]-v[:,0],v[:,2]-v[:,0]),eq[:,:3])
    d*=np.sign(sign)
    if min(d)<=0:raise ValueError('degenerate volume')
    V=d.sum()/6;g=(d[:,None]*(P[ts].sum(axis=1)+ri)).sum(axis=0)/(4*d.sum())
    # The only guaranteed inherited nonsimplicial facet is the known B cap.
    # Generic parameter points are used; all final freezes need an exact hull.
    ti=np.arange(len(ts));captris=[]
    if cap is not None:
        cc=set(map(int,cap));captris=[k for k,t in enumerate(ts) if all(int(i) in cc for i in t)]
        if captris:ti[captris]=captris[0]
    uniq,inv=np.unique(ti,return_inverse=True);nn=eq[uniq,:3];hh=-eq[uniq,3]
    supp=hh-nn@g
    if min(supp)<=0:raise ValueError('outside centroid')
    q=nn/supp[:,None];ids=np.array(H.vertices,int);rem={i:k for k,i in enumerate(ids)};p=P[ids]-g
    ed={}
    for k,t in enumerate(ts):
        for i,j in [(t[0],t[1]),(t[1],t[2]),(t[2],t[0])]:ed.setdefault(tuple(sorted((i,j))),[]).append(int(inv[k]))
    edge=[(rem[i],rem[j]) for (i,j),own in ed.items() if own[0]!=own[1]]
    dual=[tuple(own) for own in ed.values() if own[0]!=own[1]]
    assert len(ids)-len(edge)+len(q)==2
    def guards(x):
        rr=np.einsum('ij,ij->i',x,x);d=x[None,:,:]-x[:,None,:]
        norm=np.sqrt(rr)[:,None]*np.linalg.norm(d,axis=2);np.fill_diagonal(norm,1.)
        s=np.einsum('ik,ijk->ij',x,d)/norm;np.fill_diagonal(s,-np.inf)
        guard=s.max(axis=1);root=np.argmax(rr);defect=np.maximum(1e-6-guard,0);defect[root]=0
        return guard,float(defect@defect),int(root)
    pg,lp,rp=guards(p);qg,lq,rq=guards(q)
    out={'V':len(ids),'E':len(edge),'F':len(q),'C':2*len(edge),'volume':V,'centroid':g.tolist(),
         'S':int(np.sum(qg<0)),'U':int(np.sum(pg<0)),'lossP':lp,'lossQ':lq,
         'guardP':float(np.partition(pg,1)[1]),'guardQ':float(np.partition(qg,1)[1]),
         'U_material':[int(ids[i]) for i in np.flatnonzero(pg<0)],'S_ids':np.flatnonzero(qg<0).tolist()}
    if bars:
        out['P']=radial_bars(p,edge);out['Q']=radial_bars(q,dual)
    return out

def inputs(body=22):
    from fractions import Fraction as F
    data=json.loads((ROOT/'J82_S1_ROBUST_G6_INPUT.json').read_text());A=np.array(data['points'])/data['denominator']
    bb=json.loads((ROOT/f'N40_V{body}_INPUT.json').read_text());B=np.array([[float(F(t)) for t in row] for row in bb['points']])
    a=properties(A);b=properties(B,list(range({22:12,36:14,47:0}[body])))
    return A-np.array(a['centroid']),B-np.array(b['centroid']),bb,a,b

def make(A,B,z):
    R=Rotation.from_rotvec(z[1:4]).as_matrix()
    return np.vstack([A,np.exp(z[0])*B@R.T+z[4:7]])

def align(a,b):
    a=a/np.linalg.norm(a);b=b/np.linalg.norm(b);v=np.cross(a,b);s=np.linalg.norm(v);c=a@b
    if s<1e-14:
        return np.eye(3) if c>0 else Rotation.from_rotvec(np.pi*np.cross(a,np.eye(3)[np.argmin(abs(a))])/np.linalg.norm(np.cross(a,np.eye(3)[np.argmin(abs(a))]))).as_matrix()
    W=np.array([[0,-v[2],v[1]],[v[2],0,-v[0]],[-v[1],v[0],0]])
    return np.eye(3)+W+W@W/(1+c)

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--phase',choices=['scan','de'],default='scan');ap.add_argument('--run',type=int,default=0);ap.add_argument('--body',type=int,choices=[22,36,47],default=22);args=ap.parse_args()
    A,B,bb,ba,bbp=inputs(args.body);cap=list(range(45,45+({22:12,36:14,47:0}[args.body])));records=[];counts={};best={};evals=0;found=False;t0=time.time()
    def evaluate(z,mode='bar',weight=1.):
        global evals,found
        evals+=1
        try:s=properties(make(A,B,z),cap)
        except (ValueError,AssertionError,np.linalg.LinAlgError):return 1e4
        if s['E']>249:return 1e4
        if mode=='bar':val=sum(np.sqrt(s['P']))+weight*sum(np.sqrt(s['Q']))
        else:val=np.sqrt(s['lossP'])+weight*np.sqrt(s['lossQ'])
        key=f"{s['S']},{s['U']}";counts[key]=counts.get(key,0)+1
        item={**s,'z':np.asarray(z).tolist(),'value':float(val),'mode':mode,'weight':weight}
        score=sum(np.sqrt(s['P']))+sum(np.sqrt(s['Q']))
        for k,ok,v in [('all',True,score),('S1',s['S']==1,sum(np.sqrt(s['P']))),('U1',s['U']==1,sum(np.sqrt(s['Q']))),('222',s['S']==2 and s['U']==2,score)]:
            if ok and (k not in best or v<best[k]['rank']):best[k]={'rank':v,**item};records.append({'category':k,**item})
        if s['S']==s['U']==1:
            found=True;(ROOT/f'UNION84_B{args.body}_110_NOMINATION_{args.phase}_{args.run}.json').write_text(json.dumps(item,indent=2)+'\n')
        return float(val)
    if args.phase=='scan':
        R0=align(B[bbp['U_material'][0]],A[0]);axes=[np.eye(3)]
        u=A[0]/np.linalg.norm(A[0])
        for t in np.linspace(0,2*np.pi,24,endpoint=False):axes.append(Rotation.from_rotvec(t*u).as_matrix()@R0)
        for R in axes:
            rv=Rotation.from_matrix(R).as_rotvec()
            for scale in np.geomspace(.15,6.,97):evaluate(np.r_[np.log(scale),rv,[0.,0.,0.]])
        result={'evals':evals,'counts':counts,'best':best,'records':records,'found':found,'elapsed':time.time()-t0}
    else:
        weights=[.25,1.,4.,1.];w=weights[args.run%4];mode='witness' if args.run>=3 else 'bar'
        start=json.loads((ROOT/f'union84_b{args.body}_scan.json').read_text())['best']
        rng=np.random.default_rng(840726+args.run)
        bounds=[(-1.5,1.5)]+[(-np.pi,np.pi)]*3+[(-.8,.8)]*3
        init=np.array([rng.uniform(np.array(bounds)[:,0],np.array(bounds)[:,1]) for _ in range(84)])
        for i,k in enumerate(['all','S1','U1','222']):
            if k in start:init[i]=start[k]['z']
        res=differential_evolution(lambda z:evaluate(z,mode,w),bounds,seed=840726+args.run,init=init,maxiter=90,tol=1e-8,polish=False,workers=1)
        result={'evals':evals,'counts':counts,'best':best,'records':records,'found':found,'elapsed':time.time()-t0,'solver':{'fun':float(res.fun),'x':res.x.tolist(),'success':bool(res.success),'message':str(res.message)}}
    (ROOT/f'union84_b{args.body}_{args.phase}{"_"+str(args.run) if args.phase=="de" else ""}.json').write_text(json.dumps(result,indent=2)+'\n')
    print('J84_UNION_NOMINATION_DONE',args.phase,args.run,evals,found,time.time()-t0,flush=True)
    print('COUNTS',counts,flush=True)
    for k,r in best.items():print('BEST',k,'S/U',r['S'],r['U'],'V/E/F',r['V'],r['E'],r['F'],'P/Q',r['P'],r['Q'],'z',r['z'],flush=True)
```

## apex84.py
```python
"""Finite one-apex continuation of the actual N40 V47 homogeneous U1 body."""
import json,time
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import differential_evolution,minimize
from union84 import ROOT,inputs,properties
A,B,*_=inputs(47);base=properties(B);H=ConvexHull(B);rng=np.random.default_rng(840826)
records=[];best={};counts={};evals=0;t0=time.time()

def evaluate(z,weight=4.):
    global evals
    evals+=1
    try:s=properties(np.vstack([B,z]))
    except (ValueError,AssertionError):return 100.
    pp=sum(np.sqrt(s['P']));qq=sum(np.sqrt(s['Q']));val=weight*pp+qq
    key=f"{s['S']},{s['U']}";counts[key]=counts.get(key,0)+1
    item={**s,'z':np.asarray(z).tolist(),'P_penalty':pp,'Q_penalty':qq}
    for k,ok,rank in [('all',True,pp+qq),('U1',s['U']==1,qq),('S1',s['S']==1,pp),('211',s['U']==1 and s['S']==2,qq)]:
        if ok and (k not in best or rank<best[k]['rank']):best[k]={'rank':rank,**item};records.append({'category':k,**item})
    if s['S']==s['U']==1:(ROOT/'APEX84_110_NOMINATION.json').write_text(json.dumps(item,indent=2)+'\n')
    return val

# Normal rays of every original facet, including both stable carriers, and seed directions.
for n,h in zip(H.equations[:,:3],-H.equations[:,3]):
    for scale in [1.00001,1.001,1.01,1.03,1.07,1.15,1.3,1.6,2.,3.]:evaluate(n*h*scale)
for _ in range(1000):evaluate(rng.uniform(-2.5,2.5,3))
print('SCAN',evals,time.time()-t0,flush=True)
solvers=[]
for k,w in enumerate([.25,1.,4.,16.]):
    rr=differential_evolution(lambda z:evaluate(z,w),[(-3.,3.)]*3,seed=840926+k,popsize=14,maxiter=160,tol=1e-10,polish=True,workers=1)
    solvers.append({'weight':w,'fun':float(rr.fun),'x':rr.x.tolist(),'success':bool(rr.success),'nit':rr.nit,'message':str(rr.message)})
    print('DE',k,solvers[-1],'elapsed',time.time()-t0,flush=True)
    (ROOT/'apex84.json').write_text(json.dumps({'evals':evals,'records':records,'best':best,'counts':counts,'solvers':solvers},indent=2)+'\n')
print('J84_ONE_APEX_NOMINATION_DONE',evals,flush=True)
for k,r in best.items():print(k,r['S'],r['U'],r['V'],r['E'],r['F'],r['P'],r['Q'],r['z'],flush=True)
```

## N40_V22_INPUT.json
```json
{"density":1,"points":[["-34879109/20000000","-4500811598851957/10000000000000000","31230973/50000000"],["-46211053/25000000","-7809342408261419/50000000000000000","16885821/50000000"],["-37166483/20000000","272289103396313/4000000000000000","8285781/100000000"],["-45077793/25000000","25389590343117257/100000000000000000","-16093847/100000000"],["-6793977/4000000","8008179249386749/20000000000000000","-38458643/100000000"],["-124671369/100000000","-28610099075198419/25000000000000000","3667521/3125000"],["-38927769/25000000","25480542736522753/50000000000000000","-29195063/50000000"],["-139037737/100000000","58368039360258767/100000000000000000","-3022141/4000000"],["-60283171/50000000","62587038904996937/100000000000000000","-89946751/100000000"],["-20156731/20000000","1277186694424921/2000000000000000","-50799509/50000000"],["-20012017/25000000","62315575932779033/100000000000000000","-110477383/100000000"],["-58887403/100000000","29025587696574079/50000000000000000","-58210447/50000000"],["-3757611/10000000","51866221/100000000","-29702871/25000000"],["-2146217/12500000","1463883/3125000","-29036919/25000000"],["1341727/50000000","36468447/100000000","-6982639/6250000"],["1260819/6250000","23557651/100000000","-26081769/25000000"],["35537361/100000000","9261489/100000000","-92546511/100000000"],["1876293/4000000","-1506279/20000000","-3869527/5000000"],["12749489/25000000","-14087971/50000000","-12614823/20000000"],["658577/1250000","-1558777/20000000","-6911997/50000000"],["53177043/100000000","-20454059/50000000","-2579151/6250000"],["2200183/4000000","-37867533/100000000","-10997351/50000000"]]}
```

## N40_V36_INPUT.json
```json
{"density":1,"points":[["-157487491/100000000","-45712288343418747/100000000000000000","852427/1562500"],["-41959973/25000000","-15051148591012639/50000000000000000","12899559/50000000"],["-34103481/20000000","-598219035382157/3125000000000000","2495897/100000000"],["-166430903/100000000","-8331907409439821/100000000000000000","-12528283/50000000"],["-162795121/100000000","-3660355829828781/100000000000000000","-1911541/5000000"],["-110144251/100000000","-86945540055491823/100000000000000000","29236709/25000000"],["-156013397/100000000","105446229161881/10000000000000000","-53638541/100000000"],["-147045897/100000000","938128635716947/20000000000000000","-4253551/6250000"],["-34106331/25000000","3571745171486383/50000000000000000","-8088427/10000000"],["-4977789/4000000","1690712846537779/20000000000000000","-4600753/5000000"],["-55526651/50000000","4320655214594661/50000000000000000","-6345657/6250000"],["-2435721/2500000","7804210806590927/100000000000000000","-108855021/100000000"],["-10523961/12500000","6167744877395627/100000000000000000","-22816909/20000000"],["-13779469/20000000","3289389572523601/100000000000000000","-58931599/50000000"],["-50146141/100000000","-233873/50000000","-119153019/100000000"],["-16743747/50000000","-2200947/50000000","-37659/32000"],["2756713/25000000","1450581/3125000","-24859417/100000000"],["-20475339/100000000","-7547859/100000000","-28704153/25000000"],["-201851/2500000","-5521117/50000000","-55136579/50000000"],["26610673/100000000","19106701/50000000","-351699/100000000"],["3767353/100000000","-15054187/100000000","-26012379/25000000"],["-163461/6250000","46958953/100000000","14874099/100000000"],["75661/500000","-10089779/50000000","-19140521/20000000"],["12561/50000","-6450627/25000000","-3416649/4000000"],["28444893/100000000","32458807/100000000","18507101/100000000"],["16774729/50000000","-6380183/20000000","-14655977/20000000"],["1725659/5000000","23799429/100000000","2086483/12500000"],["37446433/100000000","-21574961/50000000","-59768279/100000000"],["1275103/3125000","-3521423/50000000","-57321499/100000000"],["4946277/12500000","3667347/25000000","7047543/50000000"],["8806733/20000000","282817/6250000","10285559/100000000"],["42835307/100000000","-9029833/20000000","-8633303/20000000"],["75079/160000","-6044249/100000000","819733/12500000"],["48737913/100000000","-942593/6250000","-22023/20000000"],["4940473/10000000","-4806531/20000000","-2303707/25000000"],["1496927/3125000","-36970363/100000000","-12420631/50000000"]]}
```

## N40_V47_INPUT.json
```json
{"density":1,"points":[["-156078803/100000000","-23025937/50000000","53016491/100000000"],["-10383543/6250000","-17227549/50000000","25247207/100000000"],["-42298419/25000000","-1682511/6250000","1535243/50000000"],["-165777103/100000000","-17442179/100000000","-25158883/100000000"],["-117671491/100000000","-77514717/100000000","21653057/20000000"],["-161907347/100000000","-12559851/100000000","-39749321/100000000"],["-105917453/100000000","-41770281/50000000","112972653/100000000"],["-3117101/2000000","-52591/625000","-6762521/12500000"],["-73646889/50000000","-498263/10000000","-17065983/25000000"],["-34233673/25000000","-21199/800000","-80998789/100000000"],["-62276831/50000000","-65837/5000000","-92448031/100000000"],["-111382067/100000000","-271563/25000000","-101683763/100000000"],["-19554247/20000000","-906069/50000000","-21758999/20000000"],["-42149607/50000000","-206739/6250000","-22764377/20000000"],["-71048833/100000000","-5600551/100000000","-585071/500000"],["-3654867/6250000","-51907/625000","-189639/160000"],["-935719/25000000","16775217/50000000","-24230281/50000000"],["-45859259/100000000","-10941321/100000000","-592611/500000"],["-33200989/100000000","-2678701/20000000","-2339599/2000000"],["15113861/100000000","23369101/50000000","-1034781/4000000"],["-10341413/50000000","-3981361/25000000","-14231759/12500000"],["4416907/100000000","-2435461/100000000","-100225577/100000000"],["-8491591/100000000","-72891/390625","-109097259/100000000"],["28708669/100000000","39116043/100000000","-675229/20000000"],["610133/20000000","-22293021/100000000","-1603887/1562500"],["-17871663/100000000","2724303/4000000","289093/2000000"],["965063/12500000","-35405937/100000000","-96232853/100000000"],["6926177/50000000","-26057889/100000000","-18892957/20000000"],["1001271/100000000","60161037/100000000","19063779/100000000"],["1709583/12500000","6432949/12500000","20188627/100000000"],["23637171/100000000","-29852153/100000000","-21138429/25000000"],["1732137/6250000","-27454083/50000000","-30910317/50000000"],["22731071/100000000","2696807/6250000","3953119/20000000"],["6073993/20000000","6871337/20000000","18364361/100000000"],["4025957/12500000","-33530241/100000000","-36410219/50000000"],["1799997/5000000","1050391/4000000","16381231/100000000"],["2358819/6250000","-10475997/25000000","-3650599/6250000"],["39447523/100000000","-3808333/50000000","-28886639/50000000"],["41186067/100000000","17039969/100000000","13523503/100000000"],["22715527/50000000","7166233/100000000","9823519/100000000"],["20122439/50000000","-10021399/20000000","-21435633/50000000"],["6047767/12500000","-1336279/50000000","2756647/50000000"],["4483339/10000000","-22596767/50000000","-6342217/20000000"],["12578737/25000000","-11883557/100000000","-1142577/100000000"],["25455997/50000000","-20927239/100000000","-4164081/50000000"],["9644277/20000000","-18677651/50000000","-2903689/12500000"],["50185721/100000000","-14684341/50000000","-15615129/100000000"]]}
```

## APEX84_CONTINUATION_SEED.json
```json
{"best":{"211":{"z":[0.9224360479698328,0.1762520176600193,0.17891477603007044]}},"scope":"Exact numerical seed extracted from completed apex84.json; not the complete producer report."}
```
