# material-361c7ae72140

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

"""Numerical own-centroid H-polyhedron probe; NOT an exact certificate.
Input H44 G6 is copied literally from figure-0531.
Uses NumPy/SciPy; commands: python h44_lead_probe.py --self-test.
"""
import argparse, hashlib, itertools, json, sys
from pathlib import Path
import numpy as np
from scipy.spatial import HalfspaceIntersection, ConvexHull

H44 = [[-910728,789910,-290980,1000000],[-815027,1495305,26495,1000000],[-862516,479207,-458064,1000000],[-893470,1111850,-141095,1000000],[-617519,2021021,650689,1000000],[-655450,1962149,248395,1000000],[-142760,-912800,-734235,1000000],[-333584,937912,-1102726,1000000],[-100531,-157666,-955666,1000000],[449937,1176903,-1530338,1000000],[-440133,1910662,1460261,1000000],[-241218,2053446,-733049,1000000],[-71846,1705776,-1150719,1000000],[414758,-1541987,-70898,1000000],[142699,-1250380,-512623,1000000],[838678,-1819380,829457,1000000],[-474041,2104433,-226173,1000000],[-545740,2008697,1050447,1000000],[-292461,1740742,1851404,1000000],[-97947,1497603,2214614,1000000],[-133899,1592168,1834462,1000000],[129678,1158344,2515502,1000000],[379534,726572,2717864,1000000],[622488,207097,2771305,1000000],[822136,-360098,2633928,1000000],[944206,-932947,2275965,1000000],[947991,-1421527,1702571,1000000],[-616338,233717,-655870,1000000],[-366546,-122629,-788911,1000000],[-48051,-192200,-969504,1000000],[191867,-689682,-879888,1000000],[-131202,514325,-1099556,1000000],[39829,1634533,-1166733,1000000],[35281,1605926,-168952,1000000],[310924,-837450,-624566,1000000],[567816,-1018677,-104222,1000000],[961592,-748577,476916,1000000],[353858,1009696,1191052,1000000],[566062,692408,1277821,1000000],[844972,298639,1185414,1000000],[990151,-6950,874001,1000000],[1014262,-472136,664725,1000000],[-178306,1616491,1964304,1000000],[-34361,1418442,2181920,1000000]]

def seed():
    x=np.asarray(H44,dtype=float)
    return x[:,:3]/x[:,3,None]

def barcodes(V,E):
    """Superlevel 0-persistence of radial distance squared on true 1-skeleton."""
    vv=np.einsum('ij,ij->i',V,V)
    E=np.asarray(E,dtype=int)
    a=V[E[:,0]]; d=V[E[:,1]]-a
    t=np.clip(-np.einsum('ij,ij->i',a,d)/np.einsum('ij,ij->i',d,d),0.,1.)
    foot=a+t[:,None]*d
    ew=np.einsum('ij,ij->i',foot,foot)
    parent=list(range(len(V)))
    def root(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]]; a=parent[a]
        return a
    bars=[]
    for k in np.argsort(-ew,kind='stable'):
        i,j=map(root,E[k])
        if i==j: continue
        if vv[i]<vv[j]: i,j=j,i
        depth=(vv[j]-ew[k])/vv[j]
        if depth>1e-13:
            bars.append({'peak':int(j),'elder':int(i),'edge':E[k].tolist(),'depth':float(depth),'birth':float(vv[j]),'death':float(ew[k])})
        parent[j]=i
    return sorted(bars,key=lambda z:-z['depth'])

def geometry(N,tol=2e-8):
    N=np.asarray(N,dtype=float)
    if N.ndim!=2 or N.shape[1]!=3: raise ValueError('N must have shape (F,3)')
    # A positive-spanning normal hull proves boundedness numerically, independent of finite vertices.
    dualh=ConvexHull(N)
    if np.max(dualh.equations[:,3])>=-1e-9: raise ValueError('normal hull does not enclose zero strictly')
    raw=HalfspaceIntersection(np.c_[N,-np.ones(len(N))],np.zeros(3)).intersections
    # Order is diagnostic only; exact source uses lexicographic rational sorting.
    V=raw[np.lexsort((raw[:,2],raw[:,1],raw[:,0]))]
    if not np.all(np.isfinite(V)): raise ValueError('nonfinite hull')
    slack=1-N@V.T
    scale=np.linalg.norm(N,axis=1)
    faces=[]; rows=[]
    for i in range(len(N)):
        ix=np.flatnonzero(np.abs(slack[i])/scale[i]<tol)
        if len(ix)<3: continue
        pts=V[ix]; mid=pts.mean(axis=0); n=N[i]/scale[i]
        e=pts[0]-mid; e=e/np.linalg.norm(e); f=np.cross(n,e)
        ang=np.arctan2((pts-mid)@f,(pts-mid)@e)
        faces.append(ix[np.argsort(ang)].tolist()); rows.append(i)
    edgeowners={};vol6=0.;mom24=np.zeros(3)
    for fi,face in enumerate(faces):
        for j in range(len(face)):
            edge=tuple(sorted((face[j],face[(j+1)%len(face)])))
            edgeowners.setdefault(edge,[]).append(fi)
        a=V[face[0]]
        for j in range(1,len(face)-1):
            b,c=V[face[j]],V[face[j+1]]
            det=float(np.dot(a,np.cross(b,c)))
            vol6+=det;mom24+=det*(a+b+c)
    if vol6<=0 or len(V)-len(edgeowners)+len(faces)!=2: raise ValueError('bad mass or Euler')
    if any(len(v)!=2 for v in edgeowners.values()): raise ValueError('nonmanifold edge or numerical incidence')
    g=mom24/(4*vol6)
    if np.min(1-N@g)<=0: raise ValueError('centroid is outside')
    return V,faces,np.array(rows,dtype=int),edgeowners,vol6/6,g

def audit(N,tol=1e-9,with_bars=True):
    V,faces,rows,owners,vol,g=geometry(N)
    N=np.asarray(N,dtype=float)[rows]
    norm=np.linalg.norm(N,axis=1); nn=N/norm[:,None]
    y=V-g; h=(1-N@g)/norm
    R=float(np.max(np.linalg.norm(y,axis=1)))
    feet=h[:,None]*nn
    ss=h[None,:]-feet@nn.T
    np.fill_diagonal(ss,np.inf)
    sm=ss.min(axis=1)/R
    S=np.flatnonzero(sm>tol).tolist()
    E=list(owners)
    um=np.full(len(V),-np.inf)
    for a,b in E:
        d=y[b]-y[a];d/=np.linalg.norm(d)
        um[a]=max(um[a],float(y[a]@d)/np.linalg.norm(y[a]))
        um[b]=max(um[b],float(-y[b]@d)/np.linalg.norm(y[b]))
    U=np.flatnonzero(um < -tol).tolist()
    H=[];weakH=[]
    for a,b in E:
        d=y[b]-y[a];t=-float(y[a]@d)/float(d@d)
        p=y[a]+t*d;i,j=owners[a,b]
        A=np.stack((nn[i],nn[j]),axis=1)
        lam=np.linalg.lstsq(A,p,rcond=None)[0]/R
        cond=np.r_[t,1-t,lam]
        if np.all(cond>tol):H.append([a,b])
        elif np.all(cond>=-tol):weakH.append([a,b])
    weakS=np.flatnonzero((sm>=-tol)&(sm<=tol)).tolist()
    weakU=np.flatnonzero((um>=-tol)&(um<=tol)).tolist()
    r={'V':len(V),'E':len(E),'F':len(faces),'C':2*len(E),'S':S,'U':U,'H':H,'weak':[weakS,weakU,weakH], 'volume':vol,'centroid':g.tolist(),'stable_input_rows':rows[S].tolist(), 'min_abs_vertex_escape':float(np.min(abs(um)))}
    if with_bars:
        r['P']=barcodes(y,E)
        dual=nn/h[:,None]
        de=[ij for ij in owners.values()]
        r['Q']=barcodes(dual,de)
    return r

def self_test():
    cube=np.r_[np.eye(3),-np.eye(3)]
    r=audit(cube);assert (r['V'],r['E'],r['F'])==(8,12,6)
    assert (len(r['S']),len(r['U']),len(r['H']))==(6,8,12)
    r=audit(seed())
    assert (r['V'],r['E'],r['F'])==(84,126,44)
    assert (len(r['S']),len(r['U']),len(r['H']))==(1,2,1)
    assert r['stable_input_rows']==[15]
    assert len(r['P'])==1 and len(r['Q'])==0
    assert abs(r['P'][0]['depth']-.7379371658078545)<1e-10
    print('NUMERICAL_H44_OWN121_CONTROL_PASS')
    print(json.dumps(r,sort_keys=True))
    return r

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--self-test',action='store_true');p.add_argument('--input');p.add_argument('--out')
    a=p.parse_args()
    r=self_test() if a.self_test else audit(np.array(json.loads(Path(a.input).read_text())['normals']) if a.input else seed())
    if a.out:Path(a.out).write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
    elif not a.self_test:print(json.dumps(r,indent=2,sort_keys=True))
