from __future__ import annotations
import numpy as np
from scipy.spatial import ConvexHull, QhullError
from collections import defaultdict
from dataclasses import dataclass

@dataclass
class EvalResult:
    valid: bool
    error: str|None
    active: list[int]
    faces: list[dict]
    edges: list[tuple[int,int]]
    edge_faces: dict[tuple[int,int],list[int]]
    centroid: np.ndarray
    volume: float
    stable: list[tuple[int,float]]
    unstable: list[tuple[int,float]]
    saddles: list[tuple[tuple[int,int],float]]
    face_decisions: list[float]
    vertex_decisions: dict[int,float]
    edge_decisions: dict[tuple[int,int],float]
    neighbors: dict[int,set[int]]
    topology_margin: float
    inactive_margin: float


def _group_facets(hull:ConvexHull, pts:np.ndarray, plane_tol=2e-8):
    groups=[]
    # equations normalized by qhull: n*x+off=0, inside <=0
    for si,(tri,eq) in enumerate(zip(hull.simplices,hull.equations)):
        n=np.asarray(eq[:3],float); off=float(eq[3])
        # qhull should normalize, but force
        ln=np.linalg.norm(n); n=n/ln;off=off/ln
        found=None
        for gi,g in enumerate(groups):
            if np.dot(n,g['n'])>1-plane_tol and abs(off-g['off'])<plane_tol:
                found=gi;break
        if found is None:
            groups.append({'n':n,'off':off,'tris':[tuple(map(int,tri))]})
        else: groups[found]['tris'].append(tuple(map(int,tri)))
    return groups

def _boundary_cycle(tris,n,pts):
    cnt=defaultdict(int)
    for tri in tris:
        for a,b in ((tri[0],tri[1]),(tri[1],tri[2]),(tri[2],tri[0])):
            cnt[tuple(sorted((a,b)))]+=1
    bedges=[e for e,c in cnt.items() if c==1]
    adj=defaultdict(list)
    for a,b in bedges: adj[a].append(b);adj[b].append(a)
    if not adj or any(len(v)!=2 for v in adj.values()):
        raise ValueError(f'bad boundary degrees {sorted((k,len(v)) for k,v in adj.items() if len(v)!=2)[:8]}')
    start=min(adj)
    cyc=[start];prev=None;cur=start
    while True:
        nxts=adj[cur]
        nxt=nxts[0] if nxts[0]!=prev else nxts[1]
        if nxt==start: break
        if nxt in cyc: raise ValueError('cycle repeats')
        cyc.append(nxt);prev,cur=cur,nxt
        if len(cyc)>len(adj)+2: raise ValueError('cycle long')
    if len(cyc)!=len(adj): raise ValueError('multiple boundary components')
    # orient so polygon area vector points along outward n
    area=np.zeros(3)
    for a,b in zip(cyc,cyc[1:]+cyc[:1]): area+=np.cross(pts[a],pts[b])
    if np.dot(area,n)<0: cyc=[cyc[0]]+list(reversed(cyc[1:]))
    return cyc

def evaluate(points:dict[int,np.ndarray]|np.ndarray, plane_tol=2e-8, qhull_options='Qt Qx', strict_tol=1e-10)->EvalResult:
    if isinstance(points,dict):
        ids=sorted(points);P=np.asarray([points[i] for i in ids],float)
    else:
        P=np.asarray(points,float);ids=list(range(len(P)))
    try:
        hull=ConvexHull(P,qhull_options=qhull_options)
        groups=_group_facets(hull,P,plane_tol)
        faces=[]
        for g in groups:
            cyc_local=_boundary_cycle(g['tris'],g['n'],P)
            faces.append({'cycle_local':cyc_local,'cycle':[ids[i] for i in cyc_local], 'n':g['n'], 'off':g['off'],'tris':g['tris']})
        # exact-ish mass from oriented triangles, use each maximal face fan; orient with outward n
        D6=0.0;M24=np.zeros(3)
        for f in faces:
            c=f['cycle_local']
            for j in range(1,len(c)-1):
                ia,ib,ic=c[0],c[j],c[j+1]
                a,b,z=P[ia],P[ib],P[ic]
                d=float(np.dot(a,np.cross(b,z)))
                # cycle outward ensures d contributes; closed surface sum positive, but local d can neg
                D6+=d;M24+=d*(a+b+z)
        V=D6/6.0
        if not np.isfinite(V) or V<=1e-14: raise ValueError(f'bad volume {V}')
        C=M24/(4*D6)
        X=P-C
        # topology and inactive margin based on all point-plane slacks in original coordinates
        topo=[];inact=[]
        active_local=sorted(set(hull.vertices.tolist()))
        inactive_local=sorted(set(range(len(P)))-set(active_local))
        for f in faces:
            vals=-(P@f['n']+f['off'])
            cset=set(f['cycle_local'])
            topo.extend(vals[i] for i in range(len(P)) if i not in cset)
            inact.extend(vals[i] for i in inactive_local)
        topology_margin=float(min(topo)) if topo else float('inf')
        inactive_margin=float(min(inact)) if inact else float('inf')
        # face edges / true edges
        EF=defaultdict(list)
        for fi,f in enumerate(faces):
            c=f['cycle_local']
            for a,b in zip(c,c[1:]+c[:1]): EF[tuple(sorted((a,b)))].append(fi)
        if any(len(v)!=2 for v in EF.values()): raise ValueError('nonmanifold true edge')
        neighbors=defaultdict(set)
        for a,b in EF: neighbors[a].add(b);neighbors[b].add(a)
        # faces stable components as in-plane signed distance to polygon edges
        face_dec=[];stable=[]
        for fi,f in enumerate(faces):
            c=f['cycle_local'];n=f['n'];h=-(f['off']+np.dot(n,C));proj=h*n # n unit
            ref=np.mean(X[c],axis=0);vals=[]
            for a,b in zip(c,c[1:]+c[:1]):
                e=X[b]-X[a]
                z=np.dot(np.cross(e,proj-X[a]),n)/max(np.linalg.norm(e),1e-300)
                rz=np.dot(np.cross(e,ref-X[a]),n)
                if rz<0:z=-z
                vals.append(z)
            dec=float(min(vals));face_dec.append(dec)
            if dec>strict_tol:stable.append((fi,dec))
        # vertices supports normalized by |x||edge| for scale invariance
        vdec={};unst=[]
        for i in active_local:
            vals=[]
            for j in neighbors[i]:
                d=X[j]-X[i]
                vals.append(-np.dot(X[i],d)/(max(np.linalg.norm(X[i])*np.linalg.norm(d),1e-300)))
            dec=float(min(vals));vdec[ids[i]]=dec
            if dec>strict_tol:unst.append((ids[i],dec))
        # edges
        edec={};sadd=[]
        for (a,b),inc in EF.items():
            d=X[b]-X[a];dd=np.dot(d,d);t=-np.dot(X[a],d)/dd;p=X[a]+t*d
            n1=faces[inc[0]]['n'];n2=faces[inc[1]]['n']
            aa=np.dot(n1,n1);bb=np.dot(n1,n2);cc=np.dot(n2,n2);r1=np.dot(p,n1);r2=np.dot(p,n2);den=aa*cc-bb*bb
            if den<=1e-14: raise ValueError('parallel face normals')
            l1=(r1*cc-r2*bb)/den;l2=(r2*aa-r1*bb)/den
            pn=max(np.linalg.norm(p),1e-300)
            vals=[t,1-t,l1/pn,l2/pn]
            dec=float(min(vals));e=(ids[a],ids[b]) if ids[a]<ids[b] else (ids[b],ids[a]);edec[e]=dec
            if dec>strict_tol:sadd.append((e,dec))
        return EvalResult(True,None,[ids[i] for i in active_local],faces,sorted((min(ids[a],ids[b]),max(ids[a],ids[b])) for a,b in EF),{(min(ids[a],ids[b]),max(ids[a],ids[b])):inc for (a,b),inc in EF.items()},C,V,stable,unst,sadd,face_dec,vdec,edec,{ids[i]:{ids[j] for j in ns} for i,ns in neighbors.items()},topology_margin,inactive_margin)
    except Exception as e:
        return EvalResult(False,repr(e),[],[],[],{},np.full(3,np.nan),float('nan'),[],[],[],[],{}, {},{},float('-inf'),float('-inf'))


def score_target(res:EvalResult,target_face=set(range(17)),target_vertex=8):
    if not res.valid:return -1e9,{}
    # identify target face
    tf=[(fi,d) for fi,d in res.stable if set(res.faces[fi]['cycle'])==set(target_face)]
    tv=[d for i,d in res.unstable if i==target_vertex]
    if not tf or not tv:return -1e5,{'class':(len(res.stable),len(res.unstable),len(res.saddles))}
    extra_f=[d for fi,d in res.stable if set(res.faces[fi]['cycle'])!=set(target_face)]
    extra_v=[d for i,d in res.unstable if i!=target_vertex]
    extra_e=[d for e,d in res.saddles]
    # For non-equilibria, dynamic decisions need max across all non-target items, not only positives
    target_face_idx=next((fi for fi,f in enumerate(res.faces) if set(f['cycle'])==set(target_face)),None)
    face_bad=max([d for fi,d in enumerate(res.face_decisions) if fi!=target_face_idx],default=-1)
    vert_bad=max([d for i,d in res.vertex_decisions.items() if i!=target_vertex],default=-1)
    edge_bad=max(res.edge_decisions.values(),default=-1)
    hard=min(tf[0][1],tv[0],-face_bad,-vert_bad,-edge_bad,res.topology_margin,res.inactive_margin)
    return float(hard),{'class':(len(res.stable),len(res.unstable),len(res.saddles)),'target_face':tf[0][1],'target_vertex':tv[0], 'face_bad':face_bad,'vert_bad':vert_bad,'edge_bad':edge_bad,'topology':res.topology_margin,'inactive':res.inactive_margin}
