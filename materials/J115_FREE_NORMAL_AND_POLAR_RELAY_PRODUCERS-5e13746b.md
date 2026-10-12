# material-5e13746b25a6

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J115 finite own-mass free-normal flow and polar relays — complete producer core

This numerical search code is not an exact equilibrium verifier. Exact J115 C360/C372 recovery separately uses BOTH [internal-source-reference] and [internal-source-reference]. This document contains every source/input needed for numerical flow/relays, without any parent sandbox. Save each complete FILE block including a final newline. All hashes identify executed source bytes.

Observed versions: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu. Set OMP_NUM_THREADS=1 and OPENBLAS_NUM_THREADS=1 before import. Use a fresh directory: flow115.py resumes an existing output, which would not be a cold replay. Executed recipe:
```sh
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
python flow115.py J114B_G5.txt FLOW115.json 80 .006
python relay115.py FLOW115.json RELAY115_1.json
python flow115.py RELAY115_1.json FLOW115_2.json 120 .006
python relay115.py FLOW115_2.json RELAY115_2.json
python flow115.py RELAY115_2.json FLOW115_3.json 100 .006
python relay115.py FLOW115_3.json RELAY115_3.json
python flow115.py RELAY115_3.json FLOW115_4.json 100 .006
python relay115.py FLOW115_4.json RELAY115_4.json
python flow115.py RELAY115_4.json FLOW115_5.json 100 .006
python relay115.py FLOW115_5.json RELAY115_5.json
```
Flow accepted prefixes23,13,10,14,13 steps; requested limits80/120/100/100/100 were not reached. Each ends NO_ACCEPTED_STEP and DONE when its finite policy cannot advance. Insertion prints RELAY and saves complete new normals/all evaluated scans. NO_VALID_RELAY is failure,not a zero-bar body. No cold bit-identical optimizer replay is claimed; exact endpoint recovery does not depend on matching a floating path.
Numerical sequence: parent C354,own121,P.42828450528; flow1 P.42303820927,minQ5.4620e-11; relay1 i34→new→j17,lambda.35,fraction.3,P.42303505392,minQ2.792218269e-6,C360; flow2 P.42079681039 then relay2 i24→new→j32,lambda.35,fraction.1,P.42079898828,C366; flow3 P.41932767118 then relay3 i16→new→j13,lambda.05,fraction.6,P.41932503267,C372; flow4 P.41775434985 then relay4 i7→new→j6,lambda.05,fraction.002,P.41775434983,C378; flow5 P.41621092556 then relay5 i52→new→j15,lambda.05,fraction.002,P.41621092598,C384. All have numerical S1/U2,not110. Only separately stored rational freezes are exact claims; relay4/5 remain numerical checkpoints.
Mechanism: w=(1+eps)qi+lambda(qj-qi),eps=fraction*lambda*(1-lambda)|qj-qi|²/|qi|². Require reference qi→w→qj positive,convert to PHYSICAL cut normal w/(1+w.g),rebuild actual hull/reintegrate uniform mass. Old-reference recounting is insufficient. Relays pass through old nonroots and later flow moves old H,unlike fixed-host shallow direct-root cut theorems.
Limits: generic triangular polar facets only; merged facets rejected rather than counting triangulation diagonals,so nonsimple physical vertices are not handled. Numerical class threshold1e-10/bar floor1e-12 never certify exact absence. The exact auditor keeps every positive bar,including the G5 countercontrols. Flow guards do not require the unwanted U to persist. Bounded LP/line-search failure is not geometric impossibility.

## FILE J114B_G5.txt — 1260 bytes; SHA256 77dd8b29ce31a8e79c46352e5baf2896a7782cd3cd11831eb2a888b025ac1d4f
```text
61 100000
-79311 135187 79224
-156026 87031 -54144
-138933 111101 -47884
-118406 131334 -42546
-142875 114024 -17163
-80730 150828 40203
-110083 134594 42172
-96407 135321 61885
-43710 167688 -24259
-70067 159925 -30440
-60345 132791 94670
-95605 147774 -35505
73767 141876 7073
5355 170078 4737
70949 141161 19428
-63463 -192701 -84509
31019 163498 19253
140193 -109599 34142
96677 71477 -41743
103109 62383 47387
-39646 127915 108037
68321 135936 -49856
33470 -198347 -9235
-5693 120351 117432
31935 154817 -48333
-9745 -203989 -45376
-19827 171286 -10127
70338 -180892 19574
76298 -91405 129560
-50481 106255 122372
43090 112492 105679
61877 124453 64700
-5885 166640 -35453
110131 -148705 32062
148652 -83349 52023
-122495 130659 22343
-133397 123860 2348
-150643 101479 -35862
-163688 65927 -65993
-168329 43142 -77261
-169853 18069 -87946
-167517 -9054 -98036
-161321 -38720 -105887
-150147 -71192 -111039
-133960 -106000 -110616
-108194 -145300 -104162
82425 -157371 62707
85018 -127466 98986
53258 10338 -91415
64595 37069 -81948
100397 -21637 -61971
159826 -44552 21736
-9803 -203981 -45410
85197 -35507 114082
118679 -63270 99983
142446 -58548 80897
156779 -47338 59282
8243 46799 -100548
47381 -88109 -68540
-5560 -39579 -106187
46716 -40384 -89390
```

## FILE geometry115.py — 4471 bytes; SHA256 604a9d9e7dbb3703d3770e259f13b900ba467431fb0c15cc1acfce3d372de2c4
```python
"""Numerical true-face geometry, actual uniform mass and full radial graph bars.
For numerical search only; roundoff thresholds are explicit and no exact
strict/weak classification is claimed by this module.
"""
import numpy as np
from scipy.spatial import ConvexHull
from collections import defaultdict

def read_h(path):
    a=np.loadtxt(path,skiprows=1); header=open(path).readline().split()
    assert len(a)==int(header[0]); return a/float(header[1])

def geometry(n):
    n=np.asarray(n,dtype=float)
    qh=ConvexHull(n)
    if qh.equations[:,3].max()>=-1e-10: raise ValueError('origin not inside polar')
    # Generic input assumption: dual hull facets are triangles. Reject any
    # nontriangular polar facet rather than counting triangulation diagonals.
    normals=qh.equations[:,:3]; offs=qh.equations[:,3]
    vs=-normals/offs[:,None]
    if len(vs)>1:
        from scipy.spatial.distance import pdist
        if pdist(vs).min()<1e-9: raise ValueError('nongeneric input: merged dual facet')
    tri=qh.simplices.copy()
    faces={}; polys=[]; total=0.; first=np.zeros(3)
    for j in qh.vertices:
        inds=np.where(np.any(tri==j,axis=1))[0]
        a=n[j]; axis=np.eye(3)[np.argmin(abs(a))]
        e=np.cross(a,axis); e/=np.linalg.norm(e); f=np.cross(a,e)
        c=vs[inds].mean(axis=0); delta=vs[inds]-c
        inds=inds[np.argsort(np.arctan2(delta@f,delta@e))]
        faces[int(j)]=inds.tolist()
        for b,cidx in zip(inds[1:-1],inds[2:]):
            ids=[inds[0],b,cidx]; x=vs[ids]
            d=np.linalg.det(x)/6
            if d<=0: raise ValueError('nonpositive tetrahedron')
            total+=d;first+=d*x.sum(axis=0)/4;polys.append(ids)
    g=first/total
    ed={}
    for j,ids in faces.items():
        for a,b in zip(ids,ids[1:]+ids[:1]):ed.setdefault(tuple(sorted((a,b))),[]).append(j)
    if any(len(a)!=2 for a in ed.values()):raise ValueError('bad edge incidence')
    pe=np.array(sorted(ed),int); qe=np.array([ed[tuple(x)] for x in pe],int)
    assert len(vs)-len(ed)+len(faces)==2
    assert np.max(vs@n.T-1)<1e-7
    p=vs-g; q=n/(1-n@g)[:,None]
    return dict(n=n,vertices=vs,triples=tri,faces=faces,edges=pe,dual_edges=qe,
                tetrahedra=np.asarray(polys,int),g=g,volume=total,p=p,q=q,active=qh.vertices)

def bars(x,edges):
    """0D superlevel persistence of ||x||^2 on the continuous edge graph.
    Includes every positive float difference; consumers must state any cutoff.
    Returns [(depth, birth vertex, death edge, squared birth, squared death)].
    """
    sq=np.einsum('ij,ij->i',x,x)
    d=x[edges[:,1]]-x[edges[:,0]];dd=np.einsum('ij,ij->i',d,d)
    t=np.clip(-np.einsum('ij,ij->i',x[edges[:,0]],d)/dd,0,1)
    z=x[edges[:,0]]+t[:,None]*d;level=np.einsum('ij,ij->i',z,z)
    order=np.argsort(-level,kind='stable');parent=np.arange(len(x));birth=np.arange(len(x));out=[]
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    for k in order:
        a,b=map(int,edges[k]);ra,rb=find(a),find(b)
        if ra==rb:continue
        if (sq[birth[ra]],-birth[ra])<(sq[birth[rb]],-birth[rb]):ra,rb=rb,ra
        bi=int(birth[rb]);death=float(level[k]);dep=(float(sq[bi])-death)/float(sq[bi])
        if dep>0:out.append((dep,bi,[a,b],float(sq[bi]),death))
        parent[rb]=ra
    return sorted(out,reverse=True)

def census(m,tol=1e-10):
    p,q=m['p'],m['q']; pe,qe=m['edges'],m['dual_edges'];nr=len(q)
    def scores(x,ed,active):
        s=np.full(len(x),-np.inf)
        for a,b in ed:
            s[a]=max(s[a],x[a]@(x[b]-x[a]));s[b]=max(s[b],x[b]@(x[a]-x[b]))
        return s,np.array([i for i in active if s[i]<-tol],int)
    ps,u=scores(p,pe,range(len(p)));qs,s=scores(q,qe,m['active'])
    P=bars(p,pe);Q=bars(q,qe)
    return dict(V=len(p),E=len(pe),F=len(m['faces']),g=m['g'].tolist(),volume=m['volume'],
                U=u.tolist(),S=s.tolist(),P=[z for z in P if z[0]>1e-12],Q=[z for z in Q if z[0]>1e-12],
                rawPcount=len(P),rawQcount=len(Q),
                physical_scores=ps,polar_scores=qs)

if __name__=='__main__':
    import sys,json
    m=geometry(read_h(sys.argv[1])); c=census(m)
    print(json.dumps({k:v for k,v in c.items() if not k.endswith('scores')},indent=2))
    for i in c['U']:print('U',i,'triple',m['triples'][i].tolist(),'point',m['p'][i].tolist())
    s=c['S'][0];r=m['q'][s]
    for i in c['U']:
        p=m['p'][i];print('direct-stable-cut support',i,(r@p+np.linalg.norm(r)*np.linalg.norm(p))/2)
```

## FILE flow115.py — 5112 bytes; SHA256 5201895020bc776e66f8ffaf3d1458d15ba49aa028288062976da68b568756ef
```python
"""Finite free-normal own-mass continuation, with rebuilt fans and P/Q guards.
This produces numerical candidates only. It deliberately does not constrain
both unstable roots to remain unstable. Every accepted endpoint is recounted.
"""
import os
os.environ.setdefault('OMP_NUM_THREADS','1');os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import numpy as np,torch,json,sys,time
from scipy.optimize import linprog
from geometry115 import geometry,read_h,census,bars
from pathlib import Path
torch.set_num_threads(1); torch.set_default_dtype(torch.float64)

def properties(n,m):
    nt=n; vv=torch.linalg.solve(nt[m['triples']],torch.ones((len(m['triples']),3,1))).squeeze(-1)
    tet=vv[m['tetrahedra']];vol=torch.linalg.det(tet)/6
    g=(vol[:,None]*tet.sum(dim=1)/4).sum(dim=0)/vol.sum()
    p=vv-g; q=nt/(1-nt@g)[:,None]
    return p,q,g

def global_scores(x):
    A=x@x.T-np.sum(x*x,axis=1)[:,None];np.fill_diagonal(A,-np.inf)
    return np.max(A,axis=1),np.argmax(A,axis=1)

def diagnostics(n):
    m=geometry(n);pc,pw=global_scores(m['p']);qc,qw=global_scores(m['q']);act=m['active']
    proot=np.argmax(np.sum(m['p']**2,axis=1));qroot=np.argmax(np.sum(m['q']**2,axis=1))
    pb=bars(m['p'],m['edges']);qb=bars(m['q'],m['dual_edges'])
    P=[x for x in pb if x[0]>1e-12];Q=[x for x in qb if x[0]>1e-12]
    pi=np.argsort(pc);qids=[i for i in act if i!=qroot];pids=[i for i in range(len(pc)) if i not in pi[:2]]
    return m,dict(P=P,Q=Q,U=int(np.sum(pc<-1e-10)),S=int(np.sum(qc[act]<-1e-10)),E=len(m['edges']),F=len(act),
        volume=m['volume'],centroid=m['g'].tolist(),proot=int(proot),qroot=int(qroot),
        minP=float(np.min(pc[pids])),minQ=float(np.min(qc[qids])),pc=pc,pw=pw,qc=qc,qw=qw)

def run(source,out,steps=100,radius=.006):
    out=Path(out)
    if out.exists():saved=json.loads(out.read_text());n=np.asarray(saved['normals']);trace=saved['trace']
    else:n=np.asarray(json.loads(Path(source).read_text())['normals']) if str(source).endswith('.json') else read_h(source);trace=[]
    initial=n.copy();accepted=0;start=time.time()
    for it in range(steps):
        m,c=diagnostics(n);p,q=m['p'],m['q'];P=c['P']
        if len(P)==0 and len(c['Q'])==0:print('NUMERIC_ZERO_BARS_REQUIRES_EXACT_AUDIT',flush=True);break
        if len(P)!=1 or len(c['Q']):print('wrong entrance',len(P),len(c['Q']));break
        birth=P[0][1];a,b=P[0][2];proot=c['proot'];qroot=c['qroot']
        ip=np.array([i for i in range(len(p)) if i not in [birth,proot]]);iq=np.array([i for i in m['active'] if i!=qroot])
        wp=c['pw'][ip];wq=c['qw'][iq]
        ps=np.sum(p[ip]**2,axis=1);qs=np.sum(q[iq]**2,axis=1)
        def f(flat):
            nt=flat.reshape(n.shape);pt,qt,g=properties(nt,m)
            x,y=pt[a],pt[b];d=y-x;t=torch.clamp(-(x@d)/(d@d),0,1);dd=x+t*d
            loss=1-(dd@dd)/(pt[birth]@pt[birth])
            cp=(pt[ip]*(pt[wp]-pt[ip])).sum(dim=1)/torch.as_tensor(ps)
            cq=(qt[iq]*(qt[wq]-qt[iq])).sum(dim=1)/torch.as_tensor(qs)
            return torch.cat((loss.reshape(1),cp,cq))
        x=torch.tensor(n.flatten());val=f(x).detach().numpy();J=torch.func.jacrev(f)(x).detach().numpy()
        # Existing strict guards are protected; no guard preserves the unwanted U.
        target=np.minimum(val[1:]*.2,1e-7);target=np.maximum(target,1e-12)
        scale=np.repeat(np.linalg.norm(n,axis=1),3)
        r=radius;found=False
        for trial in range(5):
            opt=linprog(J[0]*scale,A_ub=-J[1:]*scale,b_ub=val[1:]-target,
                        bounds=[(-r,r)]*n.size,method='highs')
            if not opt.success: r*=.35;continue
            direction=(opt.x*scale).reshape(n.shape)
            pred=float(J[0]@direction.ravel())
            for alpha in [1,.5,.25,.125,.0625,.03125,.015625]:
                z=n+alpha*direction
                try:mm,cc=diagnostics(z)
                except (ValueError,AssertionError):continue
                score=sum(v[0] for v in cc['P']);old=P[0][0]
                if cc['E']<=249 and len(cc['Q'])==0 and cc['S']==1 and len(cc['P'])<=1 and cc['U']<=2 and cc['minQ']>1e-12 and cc['minP']>1e-12 and score<old-1e-11:
                    n=z;accepted+=1;found=True
                    trace.append(dict(step=len(trace),P=score,E=cc['E'],F=cc['F'],U=cc['U'],S=cc['S'],alpha=alpha,radius=r,predicted=pred,minP=cc['minP'],minQ=cc['minQ']))
                    out.write_text(json.dumps(dict(normals=n.tolist(),trace=trace,source=Path(source).name,parameters=dict(radius=radius,guard_target=1e-7,guard_floor=1e-12,classification_threshold=1e-10,bar_threshold=1e-12)),indent=2)+'\n')
                    if accepted%10==0:print(trace[-1],flush=True)
                    break
            if found:break
            r*=.35
        if not found:
            print('NO_ACCEPTED_STEP',it,c['P'],c['minQ'],c['minP'],flush=True);break
    _,cc=diagnostics(n);print('DONE',accepted,'P',cc['P'],'Q',cc['Q'],'SU',cc['S'],cc['U'],'EF',cc['E'],cc['F'],'sec',time.time()-start,flush=True)
if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 100,float(sys.argv[4]) if len(sys.argv)>4 else .006)
```

## FILE relay115.py — 1939 bytes; SHA256 16e9d06675f0d9471a08d5c0236955d115036ff2b51d65a63eb61a03733470da
```python
"""Insert a finite polar relay at an exposed S1 guard, with ACTUAL mass census.
The new point interpolates qi,qj plus an outward qi displacement. No old-centre
classification substitutes for the recomputed uniform-body census.
"""
import numpy as np,json,sys
from pathlib import Path
from flow115 import diagnostics

def relay(inp,out):
    n=np.asarray(json.loads(Path(inp).read_text())['normals']);m,c=diagnostics(n);q=m['q'];g=m['g']
    ids=[int(i) for i in np.argsort(c['qc']/np.sum(q*q,axis=1)) if i!=c['qroot']][:4]
    records=[];best=None
    for i in ids:
      j=int(c['qw'][i]);d=q[j]-q[i];A=q[i]@q[i];D=d@d
      for lam in [.05,.1,.2,.35,.5,.7,.9]:
       for fraction in [.002,.01,.03,.1,.3,.6]:
        eps=fraction*lam*(1-lam)*D/A
        w=(1+eps)*q[i]+lam*d
        if w@(q[j]-w)<=0 or q[i]@(w-q[i])<=0:continue
        z=np.r_[n,(w/(1+w@g))[None,:]]
        try:mm,cc=diagnostics(z)
        except (ValueError,AssertionError):continue
        rec=dict(i=i,j=j,lam=lam,fraction=fraction,eps=float(eps),E=cc['E'],F=cc['F'],S=cc['S'],U=cc['U'],P=sum(x[0] for x in cc['P']),Q=sum(x[0] for x in cc['Q']),minQ=cc['minQ'],minP=cc['minP'])
        records.append(rec)
        if cc['E']<=249 and cc['S']==1 and cc['U']==2 and len(cc['P'])==1 and len(cc['Q'])==0 and cc['minQ']>1e-10 and cc['minP']>1e-9 and rec['P']<sum(x[0] for x in c['P'])+.005:
          # Prefer a nonmicroscopic minimum Q, then smallest remaining P.
          score=rec['P'] + 1e-6/max(rec['minQ'],1e-12)**.25
          if best is None or score<best[0]:best=(score,z,rec)
    Path(str(out)+'.scan.json').write_text(json.dumps(records,indent=2)+'\n')
    if best is None:print('NO_VALID_RELAY',len(records),flush=True);return False
    Path(out).write_text(json.dumps(dict(normals=best[1].tolist(),relay=best[2],source=Path(inp).name),indent=2)+'\n')
    print('RELAY',best[2],flush=True);return True
if __name__=='__main__':relay(sys.argv[1],sys.argv[2])
```
