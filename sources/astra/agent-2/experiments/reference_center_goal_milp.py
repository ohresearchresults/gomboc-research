"""Nearest fixed-root reference110 chamber of a single physical polyhedron.
Vertex and facet escape inequalities are linear in the reference center.
Binary witnesses encode the disjunction over actual incident neighbors.
This is only a discovery seed: the returned center is NOT substituted for
the homogeneous mass centroid. A separate physical deformation must close it.
"""
import sys,json,time,hashlib
from pathlib import Path
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint,linprog
from scipy.sparse import lil_matrix
from apex_polygon_supports import ApexFamily
from geometry import angular_scores
from support_persistence import ROOT

def chamber_branch(X,H,g,ur,sr,blocks,rootrows,eps,limit):
    import heapq
    from types import SimpleNamespace
    lo=X.min(0);hi=X.max(0);A=[];b=[]
    for k in range(3):
        row=np.zeros(4);row[k]=1;row[3]=-1;A.append(row);b.append(g[k]);row=np.zeros(4);row[k]=-1;row[3]=-1;A.append(row);b.append(-g[k])
    for h in H:A.append(np.r_[h,0]);b.append(1-eps*np.linalg.norm(h))
    for r in rootrows:A.append(np.r_[r[:3],0]);b.append(-eps-r[3])
    # Necessary farthest-vertex and nearest-plane Voronoi cells tighten the
    # search, without prescribing the witnesses of the remaining features.
    for i in range(len(X)):
        if i!=ur:A.append(np.r_[-2*(X[i]-X[ur]),0]);b.append(X[ur]@X[ur]-X[i]@X[i])
    hn=np.linalg.norm(H,axis=1)
    for i in range(len(H)):
        if i!=sr:A.append(np.r_[H[i]/hn[i]-H[sr]/hn[sr],0]);b.append(1/hn[i]-1/hn[sr])
    baseA=np.array(A);baseb=np.array(b);blocks=[np.asarray(z) for z in blocks];heap=[];serial=0;calls=0;start=time.time();seen=set()
    def push(chosen):
        nonlocal serial,calls
        key=tuple(sorted(chosen))
        if key in seen:return
        seen.add(key);C=[];d=[]
        for i,j in chosen:r=blocks[i][j];C.append(np.r_[-r[:3],0]);d.append(r[3]-eps)
        AA=np.r_[baseA,np.asarray(C).reshape(-1,4)];bb=np.r_[baseb,d]
        result=linprog([0,0,0,1],A_ub=AA,b_ub=bb,bounds=list(zip(lo,hi))+[(0,None)],method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10));calls+=1
        if result.success:heapq.heappush(heap,(result.fun,serial,chosen,result.x));serial+=1
    push(())
    while heap and time.time()-start<limit:
        value,_,chosen,x=heapq.heappop(heap);violated=[i for i,z in enumerate(blocks) if (z[:,:3]@x[:3]+z[:,3]).max()<eps*.95]
        if not violated:return SimpleNamespace(x=x,status=0,message=f'found reference chamber by adaptive linear branching; {calls} LPs, {len(heap)} remaining nodes')
        fixed={i for i,j in chosen};options=[i for i in violated if i not in fixed]
        if not options:continue
        i=min(options,key=lambda i:(len(blocks[i]),float((blocks[i][:,:3]@x[:3]+blocks[i][:,3]).max())))
        for j in range(len(blocks[i])):push(chosen+((i,j),))
    return SimpleNamespace(x=None,status=1 if heap else 2,message=f'no chamber found in this finite branch search; {calls} LPs, {len(heap)} pending nodes')

def run(src,out,m=42,eps=1e-8,limit=45,strategy='milp',root_vertex=0,root_face=None):
    import io
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);source_bytes=src.read_bytes();q=np.load(io.BytesIO(source_bytes));(out/'source_q.npy').write_bytes(source_bytes);s=ApexFamily(m,allow_top_retirement=True,edge_limit=249).state(q);X=s['X'];H=s['H'][s['A']];g=s['g'];V,F=len(X),len(H);ur=int(root_vertex);sr=int(np.argmax(np.sum(s['Y']**2,1))) if root_face is None else int(root_face);blocks=[];rootrows=[]
    vu=[[] for _ in range(V)];fs=[[] for _ in range(F)]
    for a,b in s['eu']:vu[a].append(int(b));vu[b].append(int(a))
    for a,b in s['es']:fs[a].append(int(b));fs[b].append(int(a))
    for i in range(V):
        rows=[]
        for j in vu[i]:
            d=X[j]-X[i];scale=np.linalg.norm(d);rows.append(np.r_[-d/scale,X[i]@d/scale])
        (rootrows if i==ur else blocks).extend(rows if i==ur else [rows])
    for i in range(F):
        rows=[]
        for j in fs[i]:
            ri=H[i]@H[i];ij=H[i]@H[j];a=ri*H[j]-ij*H[i];b=ij-ri;scale=np.linalg.norm(a)
            if scale==0:raise ValueError('parallel incident facets')
            rows.append(np.r_[a/scale,b/scale])
        (rootrows if i==sr else blocks).extend(rows if i==sr else [rows])
    binary_count=sum(map(len,blocks));D=4+binary_count;lo=X.min(0);hi=X.max(0);rows=[];lower=[];upper=[]
    def add(entries,l=-np.inf,u=np.inf):rows.append(entries);lower.append(l);upper.append(u)
    for a in range(3):
        add({a:1,3:-1},u=g[a]);add({a:-1,3:-1},u=-g[a])
    for h in H:add({i:float(h[i]) for i in range(3)},u=1-eps*np.linalg.norm(h))
    for r in rootrows:add({i:float(r[i]) for i in range(3)},u=-eps-r[3])
    at=4
    for block in blocks:
        choices=[]
        for r in block:
            a,b=r[:3],r[3];minimum=b+np.sum(np.where(a>=0,a*lo,a*hi));M=max(eps-minimum,0.)+1e-10;entry={i:float(-a[i]) for i in range(3)};entry[at]=M;add(entry,u=b-eps+M);choices.append(at);at+=1
        add({i:1 for i in choices},l=1)
    A=lil_matrix((len(rows),D))
    for j,row in enumerate(rows):
        for i,v in row.items():A[j,i]=v
    c=np.zeros(D);c[3]=1.;integrality=np.r_[np.zeros(4),np.ones(binary_count)];lb=np.r_[lo,0.,np.zeros(binary_count)];ub=np.r_[hi,np.inf,np.ones(binary_count)];start=time.time()
    if strategy=='branch':result=chamber_branch(X,H,g,ur,sr,blocks,rootrows,eps,limit)
    elif strategy=='milp':result=milp(c,integrality=integrality,bounds=Bounds(lb,ub),constraints=LinearConstraint(A.tocsr(),lower,upper),options=dict(time_limit=limit,mip_rel_gap=0.,primal_feasibility_tolerance=1e-9,mip_feasibility_tolerance=1e-9))
    else:raise ValueError('unknown declared reference search')
    report=dict(source=str(src),sha256=hashlib.sha256(source_bytes).hexdigest(),apex_candidates=m,eps=eps,strategy=strategy,root_vertex=ur,root_face=sr,raw_root_face=int(s['A'][sr]),status=int(result.status),message=str(result.message),seconds=time.time()-start,scope=__doc__)
    if result.x is not None:
        center=result.x[:3];Z=X-center;Y=H/(1-H@center)[:,None];us=angular_scores(Z).max(1);ss=angular_scores(Y).max(1);report.update(center=center.tolist(),actual_centroid=g.tolist(),distance_Linf=float(np.max(abs(center-g))),referenceS=int((ss<0).sum()),referenceU=int((us<0).sum()),Uguard=float(np.delete(us,ur).min()),Sguard=float(np.delete(ss,sr).min()),actualS=s['S'],actualU=s['U'],V=V,E=s['E'],F=F);np.save(out/'reference_center.npy',center);np.save(out/'source_q.npy',q)
    (out/'result.json').write_text(json.dumps(report,indent=2)+'\n');print('REFERENCE_CHAMBER_ONLY',report,flush=True);return report

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 42,strategy=sys.argv[4] if len(sys.argv)>4 else 'milp')
