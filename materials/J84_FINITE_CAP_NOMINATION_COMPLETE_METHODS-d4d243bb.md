# material-d4d243bba725

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J84 finite single-halfspace and coupled affine nomination — complete source units

Dependency: the literal J82_S1_ROBUST_G6_INPUT.json,1153B/SHA753b899123a05588f7a566b8f08d08cc6e72636fdbd59bca5c7f465f32bea3ab, already completely preserved in [internal-source-reference]. No other input workspace is needed. This source bundle preserves the actual reusable methods, including the numerical failure mechanisms. It is NOT a new110 construction or a global family exclusion. The exact two cap controls and the much larger fixed-surface centre-cube obstruction are independently reconstructed from the main J84 material, not inferred from these floating searches.

## Performed experiments and limitations
geometry84.py clips the actual45-vertex hull, retains maximal old face polygons plus one cap polygon, integrates actual filled mass and computes global chord guards. The earlier version exempted the most negative normalized guard on each side; the corrected version exempts a farthest primal/polar vector. A hash-checked exact reverse patch below recovers the earlier source. The old and corrected witness searches each completed20548 evaluations, with no110. A tiny cap can make the unnormalized witness loss~2e-14 while a finite P basin survives; the exact G8 small-witness control remained121 and slightly worsened P.

barsearch84.py uses numerical full-bar square-root penalties but excludes depths<=1e-12. Only three DE runs completed, with16388 evaluations recorded through those completions; the fourth programmed run was interrupted. Do not assert its final marker or all four runs completed. The exact frozen bar-cap control is own(1,6,5),weak000 and has five positive P bars including two near/below the floating floor. Its full exact data are in [internal-source-reference].

minimax84.py uses centre-escape threshold graphs on the live cut geometry. All three DE runs completed,14204 evaluations; no110. A clean numerical121 nominee at53/138/87 reduced the necessary escape bound to~.312578 from~.388356. A smaller necessary graph threshold does NOT establish a common centre or disappearance of a basin; potential edges may require incompatible centres. The exact fixed-surface cube proof has its separate exact negative-cut inequalities.

affine_cap84.py combines one physical cap with five upper-triangular affine shape parameters (rotations and uniform scale are immaterial to the census). Four of12 programmed SLSQP starts completed,17588 evaluations recorded; later execution was interrupted. No110. Best numerical12153/138/87 has P~.5627616526729531, not an improvement over the RA40_LATTICE220 basin. Its literal eight-parameter checkpoint is included below; some save-eligible points miss the nominal1e-8 constraint margin (here by5.515952197541265e-9), so solver conditions are not exact strict certificates. The sources do not prove impossibility of any cap/affine family.

Environment: CPython3.13.5,NumPy2.3.5,SciPy1.17.0,one BLAS/OMP thread. Save all fenced files with final LF. Commands are python search84.py; python barsearch84.py; python minimax84.py; python affine_cap84.py. They are complete producing searches; running a full programmed script beyond the stated interrupted prefix is NEW work, not a replay of a claimed old completion. Observed completed markers only: J84_SINGLE_CAP_NOMINATION_DONE20548 for both versions, J84_MINIMAX_CAP_SEARCH_DONE14204 false. Full floating reports contain variable elapsed times; fixed source/input hashes and exact cap-control outputs are the durable identities.

## Source manifest
geometry84.py3989B/SHA14bfc64a76bcba17b65ebaffab9145b4b9dfb5ebecff61d4e53e6be73b13e44c
geometry84_old.py3865B/SHAe80b6d1f44694ddc53ebd5c562177879f3110e5a7739636aee87b01c13994562
search84.py2824B/SHAf325b24a7959415bd469d85cd21fc6829dd42650343a05fc31b88a5b15d4e7c7
barsearch84.py3472B/SHA6b23f5d4e17f09c649a09f71ab2a47d014f49d77be4754510e127c6c594b05c9
minimax84.py3759B/SHA6cf0aae9481bf5697effd376878f3bb8fa7d2e8ab987bb9aa55012a3e6bd2b96
affine_cap84.py3915B/SHA101c615b36ddfb5d348e1df88b5be2a5385facb3967be0184fe3d5fdc9fef528

## geometry84.py
```python
"""Finite single-plane cuts; numerical nomination, not exact certification."""
import json
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull

ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT/'J82_S1_ROBUST_G6_INPUT.json').read_text())
P=np.asarray(DATA['points'],float)/DATA['denominator']
H=ConvexHull(P)
F=[]
for tri,eq in zip(H.simplices,H.equations):
    tri=list(map(int,tri))
    if np.cross(P[tri[1]]-P[tri[0]],P[tri[2]]-P[tri[0]])@eq[:3]<0:
        tri[1],tri[2]=tri[2],tri[1]
    F.append(tri)
F.sort(key=lambda f:tuple(sorted(f)))
EDGES=sorted({tuple(sorted((f[k],f[(k+1)%len(f)]))) for f in F for k in range(len(f))})
EARRAY=np.array(EDGES)

def cut(u,h):
    """Keep u.x<=h. Generic planes only; degeneracies deliberately rejected."""
    u=np.asarray(u,float)
    d=P@u-h
    if np.max(d)<-1e-12: return P.copy(),[f[:] for f in F]
    if np.min(d)>-1e-12 or np.min(abs(d))<1e-11: return None
    kept=np.flatnonzero(d<0)
    crossing=np.flatnonzero(d[EARRAY[:,0]]*d[EARRAY[:,1]]<0)
    if len(kept)==0 or len(crossing)<3: return None
    Q=list(P[kept]); old={int(v):i for i,v in enumerate(kept)}; ix={}
    for eidx in crossing:
        a,b=EDGES[eidx]
        ix[(a,b)]=len(Q)
        Q.append((d[a]*P[b]-d[b]*P[a])/(d[a]-d[b]))
    faces=[]
    for f in F:
        row=[]
        for a,b in zip(f,f[1:]+f[:1]):
            if d[a]<0:row.append(old[a])
            if d[a]*d[b]<0:row.append(ix[tuple(sorted((a,b)))])
        if len(row)>=3:faces.append(row)
    Q=np.array(Q)
    cap=list(ix.values()); cen=Q[cap].mean(axis=0)
    normal=u/np.linalg.norm(u)
    axis=np.eye(3)[np.argmin(abs(normal))]; e1=np.cross(axis,normal);e1/=np.linalg.norm(e1);e2=np.cross(normal,e1)
    theta=np.arctan2((Q[cap]-cen)@e2,(Q[cap]-cen)@e1)
    faces.append([cap[k] for k in np.argsort(theta)])
    return Q,faces

def properties(Q,faces,full=False):
    tris=np.array([(f[0],f[k],f[k+1]) for f in faces for k in range(1,len(f)-1)])
    r=Q.mean(axis=0);v=Q[tris]-r
    det=np.einsum('ij,ij->i',v[:,0],np.cross(v[:,1],v[:,2]))
    if np.min(det)<=0:raise ValueError('Nonpositive oriented tetrahedron')
    vol=det.sum()/6; g=(det[:,None]*(Q[tris].sum(axis=1)+r)).sum(axis=0)/(4*det.sum())
    inds=np.array([f[:3] for f in faces]); nn=np.cross(Q[inds[:,1]]-Q[inds[:,0]],Q[inds[:,2]]-Q[inds[:,0]])
    nn/=np.linalg.norm(nn,axis=1)[:,None]
    supp=np.einsum('ij,ij->i',nn,Q[inds[:,0]]-g)
    if np.min(supp)<=0:raise ValueError('Centre not interior')
    q=nn/supp[:,None];p=Q-g
    def guards(x):
        rr=np.einsum('ij,ij->i',x,x)
        scores=(x@x.T-rr[:,None])/rr[:,None]
        np.fill_diagonal(scores,-np.inf)
        return scores.max(axis=1),scores
    pg,ps=guards(p);qg,qs=guards(q)
    # Exempt a farthest primal/polar point, never the most negative normalized guard.
    # Every farthest point is strictly unstable; on success it must be the unique root.
    dp=np.maximum(1e-7-pg,0);dq=np.maximum(1e-7-qg,0)
    dp[np.argmax(np.einsum('ij,ij->i',p,p))]=0;dq[np.argmax(np.einsum('ij,ij->i',q,q))]=0
    out={'V':len(Q),'F':len(faces),'volume':float(vol),'centroid':g.tolist(),
         'U':np.flatnonzero(pg<0).tolist(),'S':np.flatnonzero(qg<0).tolist(),
         'lossP':float(dp@dp),'lossQ':float(dq@dq),'secondP':float(np.partition(pg,1)[1]),'secondQ':float(np.partition(qg,1)[1]),
         'min_abs_P':float(np.min(abs(pg))),'min_abs_Q':float(np.min(abs(qg)))}
    if full:
        edges={tuple(sorted((a,b))):[] for f in faces for a,b in zip(f,f[1:]+f[:1])}
        for fi,f in enumerate(faces):
            for a,b in zip(f,f[1:]+f[:1]):edges[tuple(sorted((a,b)))].append(fi)
        assert all(len(v)==2 for v in edges.values())
        out['E']=len(edges);out['C']=2*len(edges);out['faces']=faces
        out['pg']=pg.tolist();out['qg']=qg.tolist();out['polar']=q.tolist();out['normals']=nn.tolist();out['supports']=(supp+nn@g).tolist()
    return out

if __name__=='__main__':
    print(json.dumps(properties(P,F,True)))
```

## recover_geometry84_old.py — complete exact reverse patch
Run in the same directory; to repeat the historical old search, place its resulting geometry84_old.py under the name geometry84.py in a SEPARATE working directory with search84.py and the literal input. Do not overwrite the corrected source while running other methods.
```python
from pathlib import Path
import hashlib
p=Path(__file__).resolve().parent
raw=(p/'geometry84.py').read_bytes()
assert hashlib.sha256(raw).hexdigest()=='14bfc64a76bcba17b65ebaffab9145b4b9dfb5ebecff61d4e53e6be73b13e44c'
s=raw.decode()
s=s.replace('    # Exempt a farthest primal/polar point, never the most negative normalized guard.\n    # Every farthest point is strictly unstable; on success it must be the unique root.\n','    # Remove one most negative (dynamic root) on each side. Positive loss is not a certificate.\n')
s=s.replace("    dp[np.argmax(np.einsum('ij,ij->i',p,p))]=0;dq[np.argmax(np.einsum('ij,ij->i',q,q))]=0\n","    dp[np.argmin(pg)]=0;dq[np.argmin(qg)]=0\n")
b=s.encode()
assert len(b)==3865 and hashlib.sha256(b).hexdigest()=='e80b6d1f44694ddc53ebd5c562177879f3110e5a7739636aee87b01c13994562'
(p/'geometry84_old.py').write_bytes(b)
print('J84_HISTORICAL_ROOT_SELECTION_SOURCE_RECOVERED')
```

## search84.py
```python
"""Reproducible finite single-plane nomination on the literal J82_G6 body."""
import json,time
import numpy as np
from scipy.optimize import differential_evolution, minimize
from geometry84 import P,F,cut,properties,ROOT
rng=np.random.default_rng(840126)
base=properties(P,F,True);g=np.array(base['centroid']);V0=base['volume']
records=[]; counts={};best_s1=None;best_u1=None;best=None;evals=0

def evaluate(u,a,tag):
    global best_s1,best_u1,best,evals
    u=np.asarray(u);u=u/np.linalg.norm(u)
    pro=P@u;h=pro.min()+a*np.ptp(pro)
    c=cut(u,h)
    evals+=1
    if c is None:return 100.
    try:s=properties(*c)
    except (ValueError,FloatingPointError):return 100.
    ratio=s['volume']/V0
    if ratio<.01:return 100.+(.01-ratio)*100
    score=s['lossP']+s['lossQ']
    key=f"{len(s['S'])},{len(s['U'])}"
    counts[key]=counts.get(key,0)+1
    s.update({'normal':u.tolist(),'height':float(h),'alpha':float(a),'volume_ratio':ratio,'tag':tag,'score':score})
    improved=False
    if best is None or score<best['score']:best=s.copy();improved=True
    if len(s['S'])==1 and (best_s1 is None or s['lossP']<best_s1['lossP']):best_s1=s.copy();improved=True
    if len(s['U'])==1 and (best_u1 is None or s['lossQ']<best_u1['lossQ']):best_u1=s.copy();improved=True
    if improved:records.append(s.copy())
    if len(s['S'])==len(s['U'])==1:
        (ROOT/'candidate110.json').write_text(json.dumps(s,indent=2)+'\n')
    return score

axes=[np.array(n) for n in base['normals']]
axes += [P[i]-g for i in range(len(P))]
axes += [rng.normal(size=3) for _ in range(128)]
alphas=[.10,.20,.35,.5,.65,.75,.85,.9,.94,.97,.99,.999]
t0=time.time()
for u in axes:
    for a in alphas:evaluate(u,a,'fixed_axes')
print('SCAN',evals,'elapsed',time.time()-t0,flush=True)
print('BEST',best,flush=True);print('BEST_S1',best_s1,flush=True);print('BEST_U1',best_u1,flush=True)

def obj(z,weight):
    theta,phi,a=z
    u=np.array([np.cos(phi)*np.cos(theta),np.cos(phi)*np.sin(theta),np.sin(phi)])
    # evaluate updates the global full census; extra weight only changes search preference.
    val=evaluate(u,a,'DE')
    if val>=100:return val
    pro=P@u; c=cut(u,pro.min()+a*np.ptp(pro))
    s=properties(*c)
    return s['lossP']+weight*s['lossQ']
for k,w in enumerate([.25,1.,4.,16.]):
    res=differential_evolution(lambda z:obj(z,w),[(-np.pi,np.pi),(-np.pi/2,np.pi/2),(.03,.9999)],
        seed=840226+k,popsize=12,maxiter=120,tol=1e-9,polish=True,workers=1)
    print('DE',w,float(res.fun),res.x.tolist(),'elapsed',time.time()-t0,flush=True)
    output={'seed_axes':840126,'naxes':len(axes),'alphas':alphas,'evals':evals,'counts':counts,'records':records,'best':best,'best_s1':best_s1,'best_u1':best_u1}
    (ROOT/'search84.json').write_text(json.dumps(output,indent=2)+'\n')
print('J84_SINGLE_CAP_NOMINATION_DONE',evals,flush=True)
```

## barsearch84.py
```python
"""Finite halfspace continuation nominated by full radial-bar penalties."""
import json,time
import numpy as np
from scipy.optimize import differential_evolution
from geometry84 import P,F,cut,properties,ROOT
base=properties(P,F,True);V0=base['volume'];g0=np.array(base['centroid'])
rng=np.random.default_rng(840126);records=[];best_s1=None;best_u1=None;best=None;evals=0;found110=False;counts={}

def bars(x,edges):
    radii=np.einsum('ij,ij->i',x,x);ee=np.array(edges);a=x[ee[:,0]];d=x[ee[:,1]]-a
    t=np.clip(-np.einsum('ij,ij->i',a,d)/np.einsum('ij,ij->i',d,d),0,1);q=a+t[:,None]*d
    lev=np.einsum('ij,ij->i',q,q);par=list(range(len(x)));res=[]
    def find(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return i
    for z in np.argsort(-lev,kind='stable'):
        i,j=map(find,ee[z])
        if i==j:continue
        if (radii[i],-i)<(radii[j],-j):i,j=j,i
        dep=max(0.,1-lev[z]/radii[j])
        if dep>1e-12:res.append(dep)
        par[j]=i
    return sorted(res,reverse=True)

def evaluate(z,weight,tag):
    global best_s1,best_u1,best,evals,found110
    theta,phi,alpha=z;u=np.array([np.cos(phi)*np.cos(theta),np.cos(phi)*np.sin(theta),np.sin(phi)])
    pro=P@u;h=pro.min()+alpha*np.ptp(pro);cc=cut(u,h);evals+=1
    if cc is None:return 100.
    Q,ff=cc
    try:s=properties(Q,ff,True)
    except (ValueError,FloatingPointError):return 100.
    ratio=s['volume']/V0
    if ratio<.01:return 100.
    ed={}
    for i,f in enumerate(ff):
        for a,b in zip(f,f[1:]+f[:1]):ed.setdefault(tuple(sorted((a,b))),[]).append(i)
    bp=bars(Q-np.array(s['centroid']),list(ed));bq=bars(np.array(s['polar']),list(ed.values()))
    pp=sum(np.sqrt(bp));qq=sum(np.sqrt(bq));score=pp+weight*qq
    key=f"{len(s['S'])},{len(s['U'])}";counts[key]=counts.get(key,0)+1
    r={k:s[k] for k in ['V','E','F','C','centroid','U','S','min_abs_P','min_abs_Q']}
    r.update({'P':bp,'Q':bq,'P_penalty':pp,'Q_penalty':qq,'normal':u.tolist(),'height':float(h),'alpha':float(alpha),'volume_ratio':ratio,'tag':tag,'score':pp+qq})
    changed=False
    if best is None or r['score']<best['score']:best=r.copy();changed=True
    if len(s['S'])==1 and (best_s1 is None or pp<best_s1['P_penalty']):best_s1=r.copy();changed=True
    if len(s['U'])==1 and (best_u1 is None or qq<best_u1['Q_penalty']):best_u1=r.copy();changed=True
    if changed:records.append(r.copy())
    if len(s['S'])==len(s['U'])==1:
        found110=True;(ROOT/'barcandidate110.json').write_text(json.dumps(r,indent=2)+'\n')
    return score
axes=[np.array(n) for n in base['normals']]+[p-g0 for p in P]+[rng.normal(size=3) for _ in range(128)]
alphas=[.1,.2,.35,.5,.65,.75,.85,.9,.94,.97,.99,.999]
t0=time.time()
for u in axes:
    u/=np.linalg.norm(u);theta=np.arctan2(u[1],u[0]);phi=np.arcsin(u[2])
    for alpha in alphas:evaluate([theta,phi,alpha],1.,'fixed_axes')
print('SCAN',evals,time.time()-t0,'best_s1',best_s1,flush=True)
for k,w in enumerate([.25,1.,4.,16.]):
    res=differential_evolution(lambda z:evaluate(z,w,'DE'),[(-np.pi,np.pi),(-np.pi/2,np.pi/2),(.03,.9999)],
        seed=840326+k,popsize=12,maxiter=120,tol=1e-9,polish=True,workers=1)
    print('DE',w,float(res.fun),res.x.tolist(),'elapsed',time.time()-t0,flush=True)
    (ROOT/'barsearch84.json').write_text(json.dumps({'evals':evals,'counts':counts,'records':records,'best':best,'best_s1':best_s1,'best_u1':best_u1,'found110':found110},indent=2)+'\n')
print('J84_BAR_SINGLE_CAP_SEARCH_DONE',evals,found110,flush=True)
```

## minimax84.py
```python
"""Whole-graph centre-escape bottlenecks for live homogeneous finite caps."""
import json,heapq,time
import numpy as np
from scipy.optimize import differential_evolution
from geometry84 import P,F,cut,properties,ROOT

def bottleneck(n,edges,cost,root):
    rev=[[] for i in range(n)]
    for (i,j),t in zip(edges,cost):rev[j].append((i,float(t)))
    dd=np.full(n,np.inf);dd[root]=0.;heap=[(0.,root)]
    while heap:
        d,j=heapq.heappop(heap)
        if d!=dd[j]:continue
        for i,t in rev[j]:
            nd=max(d,t)
            if nd<dd[i]:dd[i]=nd;heapq.heappush(heap,(nd,i))
    return float(dd.max()),dd

def measures(Q,ff):
    s=properties(Q,ff,True);g=np.array(s['centroid']);x=Q-g;ns=np.array(s['normals']);hs=np.array(s['supports']);aa=hs-ns@g
    ed={}
    for i,f in enumerate(ff):
        for a,b in zip(f,f[1:]+f[:1]):ed.setdefault(tuple(sorted((a,b))),[]).append(i)
    pe=np.array([(i,j) for a,b in ed for i,j in [(a,b),(b,a)]])
    qe=np.array([(i,j) for a,b in ed.values() for i,j in [(a,b),(b,a)]])
    d=x[pe[:,1]]-x[pe[:,0]];pc=np.maximum(0,-np.einsum('ij,ij->i',x[pe[:,0]],d)/abs(d).sum(axis=1))
    i,j=qe[:,0],qe[:,1];nm=np.einsum('ij,ij->i',ns[i],ns[j]);nn=np.einsum('ij,ij->i',ns[i],ns[i])
    N=nm*aa[i]-nn*aa[j];B=nn[:,None]*ns[j]-nm[:,None]*ns[i]
    qc=np.maximum(0,-N/abs(B).sum(axis=1))
    dp,pdist=bottleneck(len(Q),pe,pc,int(np.argmax(np.einsum('ij,ij->i',x,x))))
    q=np.array(s['polar']);dq,qdist=bottleneck(len(ff),qe,qc,int(np.argmax(np.einsum('ij,ij->i',q,q))))
    s.update({'escapeP':dp,'escapeQ':dq})
    return s

if __name__=='__main__':
    base=measures(P,F);print('BASE',base['escapeP'],base['escapeQ'],flush=True)
    rng=np.random.default_rng(840126);V0=base['volume'];evals=0;best=None;clean=None;records=[];found=False
    def obj(z,w,tag='DE'):
        global evals,best,clean,found
        theta,phi,a=z;u=np.array([np.cos(phi)*np.cos(theta),np.cos(phi)*np.sin(theta),np.sin(phi)])
        pro=P@u;h=pro.min()+a*np.ptp(pro);c=cut(u,h);evals+=1
        if c is None:return 100.
        try:s=measures(*c)
        except (ValueError,FloatingPointError):return 100.
        if s['volume']/V0<.01:return 100.
        score=s['escapeP']+w*s['escapeQ']
        r={k:s[k] for k in ['V','E','F','C','centroid','S','U','escapeP','escapeQ','min_abs_P','min_abs_Q']}
        r.update({'normal':u.tolist(),'height':float(h),'alpha':float(a),'score':s['escapeP']+s['escapeQ'],'volume_ratio':s['volume']/V0,'tag':tag})
        improved=False
        if best is None or r['score']<best['score']:best=r.copy();improved=True
        if len(s['S'])==1 and len(s['U'])==2 and (clean is None or s['escapeP']<clean['escapeP']):clean=r.copy();improved=True
        if improved:records.append(r.copy())
        if len(s['S'])==len(s['U'])==1:found=True;(ROOT/'minimax_candidate110.json').write_text(json.dumps(r,indent=2)+'\n')
        return score
    axes=[np.array(n) for n in base['normals']]+[p-np.array(base['centroid']) for p in P]+[rng.normal(size=3) for _ in range(128)]
    for u in axes:
        u/=np.linalg.norm(u);theta=np.arctan2(u[1],u[0]);phi=np.arcsin(u[2])
        for a in [.1,.2,.35,.5,.65,.75,.85,.9,.94,.97,.99,.999]:obj([theta,phi,a],1.,'fixed_axes')
    print('SCAN',evals,'BEST',best,'CLEAN',clean,flush=True)
    for k,w in enumerate([.25,1.,4.]):
        rr=differential_evolution(lambda z:obj(z,w),[(-np.pi,np.pi),(-np.pi/2,np.pi/2),(.03,.9999)],seed=840426+k,popsize=12,maxiter=100,tol=1e-9,polish=True,workers=1)
        print('DE',w,float(rr.fun),rr.x.tolist(),flush=True)
        (ROOT/'minimax84.json').write_text(json.dumps({'evals':evals,'best':best,'clean':clean,'records':records,'found110':found},indent=2)+'\n')
    print('J84_MINIMAX_CAP_SEARCH_DONE',evals,found,flush=True)
```

## affine_cap84.py
```python
"""Live homogeneous material cut plus full affine shape freedom; numerical nomination."""
import json,time
import numpy as np
from scipy.optimize import minimize
from geometry84 import P,F,cut,properties,ROOT

def bars(x,edges):
    r=np.einsum('ij,ij->i',x,x);parent=list(range(len(x)));ee=np.array(edges)
    d=x[ee[:,1]]-x[ee[:,0]];t=np.clip(-np.einsum('ij,ij->i',x[ee[:,0]],d)/np.einsum('ij,ij->i',d,d),0,1)
    y=x[ee[:,0]]+t[:,None]*d;lev=np.einsum('ij,ij->i',y,y)
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    res=[]
    for k in np.argsort(-lev,kind='stable'):
        i,j=map(find,ee[k])
        if i==j:continue
        if (r[i],-i)<(r[j],-j):i,j=j,i
        dep=max(0.,1-lev[k]/r[j])
        if dep>1e-13:res.append(dep)
        parent[j]=i
    return sorted(res,reverse=True)

base=properties(P,F,True);V0=base['volume'];evals=0;cache={};best=None;records=[];roots110=[]

def evaluate(z):
    global cache,evals,best
    if 'z' in cache and np.array_equal(z,cache['z']):return cache
    theta,phi,alpha,d1,d2,s12,s13,s23=map(float,z)
    u=np.array([np.cos(phi)*np.cos(theta),np.cos(phi)*np.sin(theta),np.sin(phi)])
    pro=P@u;h=pro.min()+alpha*np.ptp(pro);cc=cut(u,h);evals+=1
    bad={'z':np.array(z),'objective':100.,'constraints':np.array([-1.,-1.,-1.])}
    if cc is None:cache=bad;return cache
    Q,ff=cc;A=np.array([[np.exp(d1),s12,s13],[0,np.exp(d2),s23],[0,0,1.]])
    Q=Q@A.T
    try:s=properties(Q,ff,True)
    except (ValueError,FloatingPointError):cache=bad;return cache
    ed={}
    for i,f in enumerate(ff):
        for a,b in zip(f,f[1:]+f[:1]):ed.setdefault(tuple(sorted((a,b))),[]).append(i)
    bp=bars(Q-np.array(s['centroid']),list(ed));bq=bars(np.array(s['polar']),list(ed.values()))
    objective=sum(np.sqrt(bp))
    pg=np.sort(s['pg']);qg=np.sort(s['qg']);fraction=s['volume']/np.linalg.det(A)/V0
    cons=np.array([qg[1]-1e-8,pg[2]-1e-8,fraction-.01])
    r={k:s[k] for k in ['V','E','F','C','S','U','centroid','min_abs_P','min_abs_Q']}
    r.update({'z':list(map(float,z)),'normal':u.tolist(),'height':float(h),'affine':A.tolist(),'P':bp,'Q':bq,
              'objective':float(objective),'constraints':cons.tolist(),'volume_ratio':float(fraction)})
    if len(s['S'])==1 and len(s['U'])<=2 and (best is None or objective<best['objective']):
        best=r.copy();records.append(r.copy())
        (ROOT/'affine_cap84_best.json').write_text(json.dumps(best,indent=2)+'\n')
    if len(s['S'])==len(s['U'])==1:
        roots110.append(r.copy());(ROOT/'affine_cap84_candidate110.json').write_text(json.dumps(r,indent=2)+'\n')
    cache={'z':np.array(z),'objective':objective,'constraints':cons,'summary':r};return cache

rng=np.random.default_rng(840526);theta=np.arctan2(.9156286205725626,.4010858792676914);phi=np.arcsin(.02746537166049664)
seed=np.array([theta,phi,.9939019841372534,0,0,0,0,0.])
bounds=[(-np.pi,np.pi),(-np.pi/2+.001,np.pi/2-.001),(.4,.9999)]+[(-1.5,1.5)]*5
outcomes=[];t0=time.time()
for k in range(12):
    z=seed.copy() if k==0 else seed+rng.normal(size=8)*np.array([.08,.08,.01,.08,.08,.08,.08,.08])
    z=np.clip(z,np.array(bounds)[:,0],np.array(bounds)[:,1])
    rr=minimize(lambda t:evaluate(t)['objective'],z,method='SLSQP',bounds=bounds,
       constraints={'type':'ineq','fun':lambda t:evaluate(t)['constraints']},options={'maxiter':250,'ftol':1e-11,'eps':1e-7})
    r=evaluate(rr.x);outcomes.append({'status':int(rr.status),'message':rr.message,'nit':int(rr.nit),'result':r.get('summary')})
    print('RUN',k,'status',rr.status,'iter',rr.nit,'objective',float(rr.fun),'cons',r['constraints'].tolist(),'elapsed',time.time()-t0,flush=True)
    (ROOT/'affine_cap84_summary.json').write_text(json.dumps({'evals':evals,'outcomes':outcomes,'records':records,'best':best,'candidate110_count':len(roots110)},indent=2)+'\n')
print('J84_AFFINE_CAP_NOMINATION_DONE',evals,len(roots110),flush=True)
```

## Literal affine-cap numerical checkpoint (not exact211/121 certification)
```json
{"z":[1.1317299339334796,0.022815387260798937,0.9998198706161652,-0.005667013767909273,-0.003387960307804518,0.006234922393727488,0.003967534153035439,0.006170397460118675],"V":53,"E":138,"F":87,"S":[16],"U":[0,39],"P":[0.5627616526729531],"Q":[],"constraints":[2.510824772488815e-7,-5.515952197541265e-9,0.9899999988106468],"volume_ratio":0.9999999988106468}
```
