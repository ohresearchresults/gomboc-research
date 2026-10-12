# material-cb4d6d897bef

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Complete recovery capsule: J107 finite free-carrier numerical experiments

Evidence: executed numerical actual-mass experiments on literal KF27D_QCANCEL_ROBUST_G4, NOT exact equilibrium certificates and NOT family-wide impossibility. No own110 was found. The separate exact 43-envelope theorem is in [internal-source-reference] and does not depend on these numerical experiments.

Save the four complete File sections below in one directory, preserving their final newlines. Dependencies used: Python3.13.5, NumPy2.3.5, SciPy1.17.0, OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1. The original finite producer runs were:

python free_carrier107.py --starts 4 --maxiter 60 --output free47.json
python free_carrier107.py --rows 12 15 31 46 47 --starts 4 --maxiter 80 --bound .6 --output free_five.json
python free_carrier107.py --rows 12 15 31 46 47 --metric --starts 3 --maxiter 90 --bound .6 --output free_five_metric.json

All other parameters are the complete source defaults: seed280107,tau1e-8,no warm file,SLSQP finite difference eps2e-7,ftol1e-12. The output path in the originating run was absolute; it has no effect on the model. Numerical optimizer trajectories and hull orderings can depend on platform. FROZEN107.json preserves every final binary64 parameter vector as a round-tripping decimal, all eleven finite results, all positive P/Q depths and their observed counts. Reconstruct the eleven actual finite inputs and numerical reports without optimization with:

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python replay107.py

Expected executed marker: J107_ELEVEN_FROZEN_FREE_CARRIER_NOMINATIONS_REPLAYED_NO_110_NUMERICAL_ONLY. It writes J107_FROZEN_REPORT.json,85821B,SHA4626f7e4cf7fc9869dbe6bc84e1687f14d0da1a1ae3585cdd316a292f9686c6d in the stated environment. The replay explicitly uses numerical tolerances only to compare numerical results, not to certify weak-free equilibrium. The free producer's terminal marker is J107_NUMERICAL_FREE_CARRIER_FINISHED_NOT_AN_EXACT_CERTIFICATE.

Input/source manifest:
KF27D_QCANCEL_ROBUST_G4.txt859B/SHA52a71e8f9dbfe781d3a0aeafe053045e7cedb2fa588661f822d05990c5a86421.
free_carrier107.py7708B/SHAcb31a61af235b79f719ce3a6610a45291fd154d093c8283de7d3f6044221fc9a.
FROZEN107.json6208B/SHAe3b43f57418fa0a64e8d9298cb81b1737c22c2dbd677e7bb6fadf2d3fcafc19f.
replay107.py1239B/SHA13b60eb6930b2427172457155a8ad789cb127da56b096f11fb4038a4bf81a992.

All three runs allow new primal roots and minimize the SUM of every positive P depth under dynamically chosen unique-S chord constraints. They do not retain both original U by constraint. The four common-carrier47 trials reach numerical S1/U4, totalP about.5126172. Freeing all five root-carrier normals gives S1/U10 in three runs and S1/U9 in the fourth, where row48 retires and V/E/F=92/138/48,mainP.4969487620659485,totalP.5053248310421748. Adding the shared affine map in three further runs gives S1/U11,totalP about.50791805. Every Q list is empty numerically. The lowered main depth is accompanied by new positive P branches, not whole-basin cancellation. None of these outcomes is promoted as exact121 or110. Source inspiration for actual-mass support/metric evaluation is the fully read J104 part1 material [internal-source-reference]; this complete new source has no runtime dependency on its code.

## File: KF27D_QCANCEL_ROBUST_G4.txt
```text
49 10000
-5079 13732 9267
-14396 11026 -3218
-12466 13017 -2373
-10223 14660 -1659
-12371 13207 485
-5511 15313 6055
-8438 14243 6102
-6944 14003 7847
-2416 17109 -242
-5135 16720 -706
-3100 13245 10467
-7743 15902 -1141
5950 3897 -9129
7859 14371 112
7631 1392 -8083
-7105 -20060 -8288
3029 16527 756
10270 12338 -490
5553 15635 147
13447 -12400 4798
10989 9339 -4734
8969 11100 5188
-1080 12497 11470
5972 13236 -6394
3314 -20677 -1248
2405 11856 11399
2827 16105 -3395
-1372 -21226 -4632
337 17042 309
6856 -18977 2259
8235 -11672 11211
-1912 9348 13526
3963 10154 12299
6264 11222 9621
-48 16910 -1981
9667 -16286 5360
13499 -8728 8488
-9829 14213 4254
-11155 13859 2378
-13471 12248 -1382
-15456 9243 -4601
-16262 7227 -5952
-16803 4959 -7230
-17054 2425 -8392
-16933 -367 -9448
-16470 -4196 -10134
-15277 -8346 -10358
-12715 -13423 -10051
2909 -2 -9206
```

## File: free_carrier107.py
```python
#!/usr/bin/env python3
"""Actual-mass finite free-support search; numerical nominations, never a certificate.
Defaults change all three coefficients of common U carrier47. Optionally more
rows and one shared invertible affine map are changed. All positive bars count.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse,hashlib,itertools,json,platform,time
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import minimize
HERE=Path(__file__).resolve().parent
INPUT=HERE/'KF27D_QCANCEL_ROBUST_G4.txt'
SHA='52a71e8f9dbfe781d3a0aeafe053045e7cedb2fa588661f822d05990c5a86421'
assert hashlib.sha256(INPUT.read_bytes()).hexdigest()==SHA
N0=np.loadtxt(INPUT,skiprows=1)/10000

def geometry(N):
    ph=ConvexHull(N)
    if max(ph.equations[:,-1])>=-1e-7:raise ValueError('not bounded')
    tri=np.array(ph.simplices)
    X=np.linalg.solve(N[tri],np.ones((len(tri),3,1)))[:,:,0]
    if max((N@X.T-1).ravel())>1e-7:raise ValueError('bad primal geometry')
    # Primal edges are true dual facet adjacencies for the generic simplicial
    # polar fan. Reject any coincident dual intersections instead of pretending
    # triangulation diagonals are true primal edges.
    edges=np.array(sorted({tuple(sorted((i,int(j)))) for i,nb in enumerate(ph.neighbors) for j in nb if j>=0}))
    if np.min(np.linalg.norm(X[edges[:,1]]-X[edges[:,0]],axis=1))<1e-9:raise ValueError('nongeneric polar facet')
    ch=ConvexHull(X);t=ch.simplices.copy();p=X[t]
    swap=np.einsum('ij,ij->i',np.cross(p[:,1]-p[:,0],p[:,2]-p[:,0]),ch.equations[:,:3])<0
    t[swap]=t[swap][:,[0,2,1]];p=X[t]
    W=np.einsum('ij,ij->i',p[:,0],np.cross(p[:,1],p[:,2]));V=W.sum()/6
    if W.min()<=0 or V<=0:raise ValueError('mass orientation')
    g=(W[:,None]*p.sum(axis=1)).sum(axis=0)/(4*W.sum())
    if max(N@g)>=1:raise ValueError('centroid outside')
    pe=np.array(sorted({tuple(sorted((int(i),int(j)))) for f in tri for i,j in itertools.combinations(f,2)}))
    active=np.array(sorted(ph.vertices));assert len(X)-len(edges)+len(active)==2
    return dict(X=X,edges=edges,pedges=pe,g=g,V=V,active=active,triples=tri)

def bars(X,ee):
    birth=np.einsum('ij,ij->i',X,X)
    a=X[ee[:,0]];d=X[ee[:,1]]-a
    t=np.clip(-np.einsum('ij,ij->i',a,d)/np.einsum('ij,ij->i',d,d),0,1)
    s=a+t[:,None]*d;death=np.einsum('ij,ij->i',s,s)
    # Exactly reuse endpoint squared norm for endpoint minima: numerical roundoff
    # is not allowed to manufacture positive zero-length bars.
    death=np.where(t==0,birth[ee[:,0]],np.where(t==1,birth[ee[:,1]],death))
    order=sorted(range(len(ee)),key=lambda k:(-death[k],int(ee[k,0]),int(ee[k,1])))
    parents=np.arange(len(X));out=[]
    def find(i):
        while parents[i]!=i:parents[i]=parents[parents[i]];i=parents[i]
        return i
    for k in order:
        u,v=map(find,ee[k])
        if u==v:continue
        if (birth[u],-u)<(birth[v],-v):u,v=v,u
        delta=1-death[k]/birth[v]
        if delta>0:out.append(dict(depth=float(delta),root=int(v),edge=ee[k].tolist(),birth=float(birth[v]),death=float(death[k])))
        parents[v]=u
    return sorted(out,key=lambda z:-z['depth'])

def scores(X,edges=None):
    if edges is None:
        ii,jj=np.where(~np.eye(len(X),dtype=bool));arcs=np.c_[ii,jj]
    else:arcs=np.vstack((edges,edges[:,::-1]))
    z=X[arcs[:,0]];d=X[arcs[:,1]]-z
    norm=np.linalg.norm(z,axis=1)*np.linalg.norm(d,axis=1)
    if min(norm)<1e-16:raise ValueError('degenerate score')
    c=np.einsum('ij,ij->i',z,d)/norm
    best=np.full(len(X),-np.inf);np.maximum.at(best,arcs[:,0],c)
    root=int(np.argmax(np.einsum('ij,ij->i',X,X)))
    return best,root

def affine(x):
    a,b,p,q,r=x
    return np.array([[np.exp(a),p,q],[0,np.exp(b),r],[0,0,np.exp(-a-b)]])

class Model:
    def __init__(self,rows,metric,tau):self.rows=rows;self.metric=metric;self.tau=tau;self.cache=None
    def calc(self,x):
        if self.cache is not None and np.array_equal(x,self.cache[0]):return self.cache[1]
        N=N0.copy();n=3*len(self.rows);N[self.rows]+=np.array(x[:n]).reshape(-1,3)
        A=affine(x[n:]) if self.metric else np.eye(3)
        K=geometry(N);P=(K['X']-K['g'])@A.T
        Y=(N/(1-N@K['g'])[:,None])@np.linalg.inv(A)
        sm,sroot=scores(Y);um,uroot=scores(P,K['edges'])
        sg=sm.copy();sg[sroot]=1.;sg-=self.tau
        pb=bars(P,K['edges']);qb=bars(Y,K['pedges'])
        # Inactive points have no true polar edges and cannot contribute a bar.
        # In bars(), all edges only touch active polar vertices; their isolated
        # DSU entries cannot create reported intervals.
        out=dict(N=N,A=A,K=K,P=pb,Q=qb,sg=sg,sm=sm,um=um,S=np.flatnonzero(sm<0),U=np.flatnonzero(um<0),sroot=sroot,uroot=uroot)
        self.cache=(np.array(x).copy(),out);return out
    def objective(self,x):
        try:r=self.calc(x);return sum(z['depth'] for z in r['P'])
        except (ValueError,QhullError,np.linalg.LinAlgError,AssertionError):return 1e3+float(x@x)
    def cons(self,x):
        try:return self.calc(x)['sg']
        except (ValueError,QhullError,np.linalg.LinAlgError,AssertionError):return np.full(49,-100.)
    def report(self,x):
        r=self.calc(x);K=r['K']
        return dict(theta=np.asarray(x).tolist(),N=r['N'].tolist(),A=r['A'].tolist(),counts=[len(K['X']),len(K['edges']),len(K['active'])],S=r['S'].tolist(),U=[K['triples'][i].tolist() for i in r['U']],P=r['P'],Q=r['Q'],constraints_min=float(min(r['sg'])),g=K['g'].tolist(),volume=float(K['V']),inactive=[i for i in range(49) if i not in K['active']])

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--rows',type=int,nargs='+',default=[47]);ap.add_argument('--metric',action='store_true');ap.add_argument('--starts',type=int,default=6);ap.add_argument('--maxiter',type=int,default=100);ap.add_argument('--bound',type=float,default=.5);ap.add_argument('--tau',type=float,default=1e-8);ap.add_argument('--seed',type=int,default=280107);ap.add_argument('--warm');ap.add_argument('--output',default='free_carrier107.json');args=ap.parse_args()
    model=Model(args.rows,args.metric,args.tau);d=3*len(args.rows)+5*args.metric;zero=np.zeros(d);rng=np.random.default_rng(args.seed)
    starts=[zero];
    if args.warm:
        old=json.loads(Path(args.warm).read_text());starts.extend(np.array(r['theta']) for r in old['runs'] if len(r.get('theta',[]))==d)
    while len(starts)<args.starts:
        scales=[1e-4,1e-3,.01,.05,.15];starts.append(np.clip(rng.normal(size=d)*scales[(len(starts)-1)%len(scales)],-args.bound,args.bound))
    data=dict(arguments=vars(args),input_sha256=SHA,versions=dict(python=platform.python_version(),numpy=np.__version__,scipy=__import__('scipy').__version__),baseline=model.report(zero),runs=[])
    print('BASE',data['baseline'],flush=True)
    for k,start in enumerate(starts[:args.starts]):
        res=minimize(model.objective,start,method='SLSQP',bounds=[(-args.bound,args.bound)]*d,constraints={'type':'ineq','fun':model.cons},options=dict(maxiter=args.maxiter,ftol=1e-12,eps=2e-7))
        try:r=model.report(res.x)
        except Exception as exc:r=dict(theta=res.x.tolist(),failure=str(exc))
        r.update(start=start.tolist(),status=int(res.status),message=str(res.message),nit=int(res.nit),nfev=int(res.nfev));data['runs'].append(r)
        Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
        print('RUN',k,'P',sum(z['depth'] for z in r.get('P',[])),'S/U',len(r.get('S',[])),len(r.get('U',[])),'min',r.get('constraints_min'),'status',res.status,'iter',res.nit,flush=True)
    print('J107_NUMERICAL_FREE_CARRIER_FINISHED_NOT_AN_EXACT_CERTIFICATE',flush=True)
if __name__=='__main__':main()
```

## File: FROZEN107.json
```json
[{"case":"free47_0","rows":[47],"metric":false,"tau":1e-08,"theta":[0.002252925252038121,0.004238161488637505,-0.006201882748338039],"counts":[94,141,49],"S_count":1,"U_count":4,"P":[0.5123700324641891,0.000213859553186313,3.33066967054263e-05],"Q":[],"retired":[]},{"case":"free47_1","rows":[47],"metric":false,"tau":1e-08,"theta":[0.00225292525209617,0.004238161488485392,-0.00620188274831765],"counts":[94,141,49],"S_count":1,"U_count":4,"P":[0.5123700324641911,0.00021385955318509176,3.330669670598141e-05],"Q":[],"retired":[]},{"case":"free47_2","rows":[47],"metric":false,"tau":1e-08,"theta":[0.002252925251999061,0.004238161488743641,-0.006201882748356352],"counts":[94,141,49],"S_count":1,"U_count":4,"P":[0.5123700324641869,0.00021385955318753425,3.330669670598141e-05],"Q":[],"retired":[]},{"case":"free47_3","rows":[47],"metric":false,"tau":1e-08,"theta":[0.00225292525228678,0.0042381614879571814,-0.006201882748240617],"counts":[94,141,49],"S_count":1,"U_count":4,"P":[0.5123700324641993,0.00021385955318009575,3.330669670520425e-05],"Q":[],"retired":[]},{"case":"free_five_0","rows":[12,15,31,46,47],"metric":false,"tau":1e-08,"theta":[-0.055926952130828794,0.013870051663627916,-0.013230089543121437,0.008012711212692702,0.0006973747233198732,-0.006081794585189846,-0.005799325949000462,-0.020917694264761224,0.007056004304075416,0.016572740510579866,-0.017633329360050732,-0.01889382672021945,0.012407610009741775,0.007457589233423292,-0.020188108912781295],"counts":[94,141,49],"S_count":1,"U_count":10,"P":[0.5068180007596546,0.0006506317419922025,0.0004392782631559289,0.00023677595855398081,0.00019254217865893875,0.00010632572846513977,3.4448563114519715e-05,3.120402942891065e-05,2.5980303024475404e-05],"Q":[],"retired":[]},{"case":"free_five_1","rows":[12,15,31,46,47],"metric":false,"tau":1e-08,"theta":[-0.05592700426529262,0.013870205497404592,-0.01323011971141247,0.008014556805590949,0.0006971247749375073,-0.006081210336811404,-0.005799129718186204,-0.020918127278077382,0.007056189299615685,0.01657291056152265,-0.01763364924456302,-0.018893954552792074,0.012411029291132246,0.007450574946027307,-0.02018727315940357],"counts":[94,141,49],"S_count":1,"U_count":10,"P":[0.5068179612808321,0.0006506112004814879,0.00043931255077678255,0.00023678210343436312,0.00019255299936316028,0.00010633201517307178,3.444844401789826e-05,3.120215693119821e-05,2.5984775493648193e-05],"Q":[],"retired":[]},{"case":"free_five_2","rows":[12,15,31,46,47],"metric":false,"tau":1e-08,"theta":[-0.05592684772899444,0.013869949612200136,-0.013230139905007605,0.008014191215231217,0.0006970773039497751,-0.006080881080540307,-0.005799109238282282,-0.020917578041169786,0.00705599309894803,0.016573069809117665,-0.01763436443136383,-0.018893919501950688,0.012410502545987521,0.007451201322454567,-0.02018697764891262],"counts":[94,141,49],"S_count":1,"U_count":10,"P":[0.5068179991313324,0.0006506164922979174,0.00043928797589998236,0.00023678800423010404,0.0001925410437956243,0.00010631975356167889,3.444995415358143e-05,3.120320265714849e-05,2.5981967983534915e-05],"Q":[],"retired":[]},{"case":"free_five_3","rows":[12,15,31,46,47],"metric":false,"tau":1e-08,"theta":[-0.16664533045911442,-0.06376035905478195,-0.043897835898754685,0.009341841717823634,0.0016170147825761974,-0.010464995193026351,0.012080246903459052,-0.04132646483118531,0.0173834875473284,0.009159800634540768,-0.0008577010895103974,-0.01399228878549222,0.014278652481315863,0.0036308007007150797,-0.021888524791368658],"counts":[92,138,48],"S_count":1,"U_count":9,"P":[0.4969487620659485,0.00452581725114487,0.001729733975758374,0.0011653738557990678,0.00039651444207977615,0.00026731605337593223,0.00020350174427807843,8.781165379023737e-05],"Q":[],"retired":[48]},{"case":"free_five_metric_0","rows":[12,15,31,46,47],"metric":true,"tau":1e-08,"theta":[-0.06573607950660322,0.0035525738151267064,-0.013650939528188135,0.013455668483530882,0.0004989697120106634,-0.005687196345174685,-0.006896325254584936,-0.021086543722626448,0.0076755379179267655,0.017282937484710516,-0.022875767356789766,-0.017296822758524257,0.016227917627660092,-0.0020891928101394964,-0.016058791989207732,-0.00017882535854471158,-0.00033947415762597963,0.00036211782133279514,0.0004341555590543599,-0.001404993563884507],"counts":[94,141,49],"S_count":1,"U_count":11,"P":[0.5060104442493756,0.0006276881815938662,0.00047456173672233426,0.0002666748132711394,0.00019784910448994442,0.00013578430558225385,0.00010364614182034604,7.266589031762472e-05,2.8623563398944007e-05,1.1536277499946124e-07],"Q":[],"retired":[]},{"case":"free_five_metric_1","rows":[12,15,31,46,47],"metric":true,"tau":1e-08,"theta":[-0.0657359917755729,0.0035525992664744003,-0.013650926690254113,0.013455623353515593,0.0004989703376202775,-0.005687185546709874,-0.006896303455081766,-0.021086573245635724,0.007675552641564203,0.017282973401757155,-0.02287582152088446,-0.017296858943537604,0.01622786373613724,-0.002089049439466098,-0.01605882860680207,-0.00017882529107061138,-0.0003394740169992531,0.000362117600693421,0.00043415567080081104,-0.0014049931778142549],"counts":[94,141,49],"S_count":1,"U_count":11,"P":[0.5060104432401711,0.0006276868403848335,0.0004745604724947228,0.000266678118376773,0.000197849923298965,0.00013578342656894726,0.00010364574219678957,7.266663574145849e-05,2.8623585532683293e-05,1.1536252397803537e-07],"Q":[],"retired":[]},{"case":"free_five_metric_2","rows":[12,15,31,46,47],"metric":true,"tau":1e-08,"theta":[-0.06573608408317333,0.00355256719169642,-0.013650937769867786,0.01345560640020487,0.0004989792821625303,-0.0056872225990232785,-0.006896358561254048,-0.02108651280020521,0.0076755201226028375,0.0172829166838915,-0.022875692120758864,-0.01729682077459901,0.016227801447376795,-0.0020889495523698106,-0.016058830916420644,-0.00017882528672915121,-0.0003394739766361238,0.00036211767720506526,0.0004341555945810938,-0.0014049929405358615],"counts":[94,141,49],"S_count":1,"U_count":11,"P":[0.5060104455720364,0.0006276888097613842,0.00047456112725319244,0.0002666745558631556,0.0001978481770532614,0.00013578424854965299,0.0001036461264241062,7.26657812912812e-05,2.862358871891235e-05,1.1536241661946889e-07],"Q":[],"retired":[]}]
```

## File: replay107.py
```python
"""Replay eleven exact binary64 parameter checkpoints; numerical evidence only."""
import hashlib,json
from pathlib import Path
import numpy as np
from free_carrier107 import Model
HERE=Path(__file__).resolve().parent
f=HERE/'FROZEN107.json'
assert hashlib.sha256(f.read_bytes()).hexdigest()=='e3b43f57418fa0a64e8d9298cb81b1737c22c2dbd677e7bb6fadf2d3fcafc19f'
rows=json.loads(f.read_text());assert len(rows)==11
out=[]
for c in rows:
    r=Model(c['rows'],c['metric'],c['tau']).report(np.array(c['theta']))
    assert r['counts']==c['counts']
    assert len(r['S'])==c['S_count'] and len(r['U'])==c['U_count']
    assert r['inactive']==c['retired']
    for side in ('P','Q'):
        depths=[x['depth'] for x in r[side]]
        assert len(depths)==len(c[side])
        assert all(abs(a-b)<1e-12 for a,b in zip(depths,c[side]))
    assert len(r['S'])==1 and len(r['U'])>1
    assert r['constraints_min']>-1e-10
    out.append(dict(case=c['case'],report=r))
raw=(json.dumps(dict(evidence='NUMERICAL_ONLY_NOT_EXACT_CENSUS',cases=out),indent=2)+'\n').encode()
(HERE/'J107_FROZEN_REPORT.json').write_bytes(raw)
print(len(raw),hashlib.sha256(raw).hexdigest())
print('J107_ELEVEN_FROZEN_FREE_CARRIER_NOMINATIONS_REPLAYED_NO_110_NUMERICAL_ONLY')
```
