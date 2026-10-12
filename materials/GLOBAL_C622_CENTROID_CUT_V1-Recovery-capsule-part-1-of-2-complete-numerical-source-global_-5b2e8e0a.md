# material-5b2e8e0ac2a2

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Numerical global centroid cuts of canonical C622; NOT an exact certificate.
Inputs are the exact canonical A.json and raw.json recovered from scoped16.
All moment evaluations integrate the actual newly clipped hull, crossing cells.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json,hashlib,platform,itertools
sys.set_int_max_str_digits(0)
from pathlib import Path
from fractions import Fraction as F
import numpy as np
import scipy
from scipy.spatial import HalfspaceIntersection,ConvexHull,QhullError
PARS=dict(max_steps=100,root_tol=2e-13,active_tol=2e-8,dedup_decimals=10,
          armijo=1e-4,max_halvings=35,spectral_floor=1e-12,max_step=0.2)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(a_path,r_path):
    assert sha(a_path)=='142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0'
    assert sha(r_path)=='ac01d1625274b64f336a715e1f5462f40686f647f0b7d1a4d90a5ee21765adb5'
    a=json.loads(Path(a_path).read_text());r=json.loads(Path(r_path).read_text())
    x=[tuple(map(F,v)) for v in a['raw_vertices']];g=tuple(map(F,a['raw_centroid']))
    # Normalize each raw support about the EXACT original mass center.
    q=np.array([[float(F(n)/(F(row[3])-sum(F(m)*z for m,z in zip(row[:3],g)))) for n in row[:3]] for row in r['H']])
    adj=[set() for _ in x]
    for i,j in a['edges']:adj[i].add(j);adj[j].add(i)
    ears=[]
    for i,ne in enumerate(adj):
        if len(ne)!=3:continue
        ids=sorted(ne);aa,bb,cc=[x[j] for j in ids]
        u=[b-a for a,b in zip(aa,bb)];v=[c-a for a,c in zip(aa,cc)]
        n=[u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]]
        h=sum(z*a for z,a in zip(n,aa))
        if sum(z*t for z,t in zip(n,x[i]))<h:n=[-z for z in n];h=-h
        assert sum(z*t for z,t in zip(n,x[i]))>h
        assert all(sum(z*t for z,t in zip(n,x[j]))<h for j in range(len(x)) if j not in [i,*ids])
        d=h-sum(z*t for z,t in zip(n,g));assert d>0
        t=sum(i in c and len(c)==3 for c in a['faces'])
        ears.append(dict(vertex=i,neighbors=ids,triangles=t,q=[float(z/d) for z in n]))
    facets=[j for j,c in enumerate(a['faces']) if all(len(adj[i])==3 for i in c)]
    assert len(ears)==133 and facets==[48,55,69,70,89,93,99,100,101,105,110,112,113,114,115,117,120,123,124,125]
    return a,q,ears,facets

def geometry(planes,q=None,want_hess=True):
    Q=planes if q is None else np.vstack([planes,q])
    xx=HalfspaceIntersection(np.c_[Q,-np.ones(len(Q))],np.zeros(3)).intersections
    # Qhull can repeat a physical nonsimple intersection. Never split it by triangulation.
    _,ii=np.unique(np.round(xx,PARS['dedup_decimals']),axis=0,return_index=True);X=xx[np.sort(ii)]
    hull=ConvexHull(X);tr=hull.simplices.copy()
    cross=np.cross(X[tr[:,1]],X[tr[:,2]])
    d=np.einsum('ij,ij->i',X[tr[:,0]],cross)
    flip=d<0;tr[flip,1],tr[flip,2]=tr[flip,2].copy(),tr[flip,1].copy();d=np.abs(d)
    assert d.min()>0 and np.max(X@Q.T-1)<1e-7
    V=d.sum()/6;J=(d[:,None]*X[tr].sum(axis=1)).sum(axis=0)/24
    H=np.zeros((3,3))
    if q is not None and want_hess:
        active=np.all(np.abs(X[tr]@q-1)<PARS['active_tol'],axis=1)
        for row,di in zip(tr[active],d[active]):
            pts=X[row];su=pts.sum(axis=0)
            H+=di*(np.outer(su,su)+pts.T@pts)/24
    return dict(X=X,triangles=tr,V=V,J=J,H=H,Q=Q,
                phi=V if q is None else V-q@J)

def census(z):
    X=z['X']-z['J']/z['V'];Q=z['Q']/(1-z['Q']@(z['J']/z['V']))[:,None]
    active=[];cycles=[];edges=set()
    for j,q in enumerate(Q):
        ids=np.flatnonzero(np.abs(X@q-1)<PARS['active_tol'])
        if len(ids)<3:continue
        pts=X[ids];c=pts.mean(axis=0);axis=np.eye(3)[np.argmin(np.abs(q))]
        u=np.cross(q,axis);u/=np.linalg.norm(u);v=np.cross(q,u);v/=np.linalg.norm(v)
        angle=np.arctan2((pts-c)@v,(pts-c)@u);cy=ids[np.argsort(angle)].tolist()
        # planar convex hull removes non-extreme collinear points, if any
        xy=np.c_[(pts-c)@u,(pts-c)@v]
        try:cy=ids[ConvexHull(xy).vertices].tolist()
        except QhullError:continue
        active.append(j);cycles.append(cy)
        for a,b in zip(cy,cy[1:]+cy[:1]):edges.add(tuple(sorted((a,b))))
    PP=Q[active];used=sorted(set(itertools.chain.from_iterable(cycles)))
    X=X[used]
    D=X@X.T-np.sum(X*X,axis=1)[:,None];np.fill_diagonal(D,-np.inf);umax=D.max(axis=1)
    D=PP@PP.T-np.sum(PP*PP,axis=1)[:,None];np.fill_diagonal(D,-np.inf);smax=D.max(axis=1)
    return dict(V=len(X),E=len(edges),F=len(active),C=2*len(edges),
      S=int((smax< -1e-12).sum()),U=int((umax< -1e-12).sum()),
      possible_zero_S=int((np.abs(smax)<=1e-12).sum()),possible_zero_U=int((np.abs(umax)<=1e-12).sum()),
      euler=len(X)-len(edges)+len(active),active=active,
      min_abs_U=float(np.min(np.abs(umax))),min_abs_S=float(np.min(np.abs(smax))))

def solve(planes,q0):
    q=q0.copy();history=[];z=geometry(planes,q)
    for it in range(PARS['max_steps']):
        err=float(np.linalg.norm(z['J'])/z['V']);history.append([it,err,float(z['phi']),len(z['X'])])
        if err<PARS['root_tol']:return q,z,'numerical_root',history
        H=z['H'];e,W=np.linalg.eigh(H);floor=max(float(e[-1])*PARS['spectral_floor'],1e-16)
        step=W@((W.T@z['J'])/np.maximum(e,floor))
        sn=np.linalg.norm(step)
        if sn>PARS['max_step']:step*=PARS['max_step']/sn
        descent=float(z['J']@step);best=None
        for k in range(PARS['max_halvings']):
            alpha=2.**(-k);qq=q+alpha*step
            try:zz=geometry(planes,qq)
            except (QhullError,AssertionError):continue
            # Armijo for the globally convex potential, with root-error tie-break
            bound=z['phi']-PARS['armijo']*alpha*descent
            newerr=float(np.linalg.norm(zz['J'])/zz['V'])
            if zz['phi']<bound or (abs(zz['phi']-z['phi'])<3e-14 and newerr<err*.999):
                best=qq,zz;break
        if best is None:return q,z,'line_search_failed',history
        q,z=best
    return q,z,'iteration_limit',history

def main():
    assert __debug__ and len(sys.argv)==7,'A.json raw.json OUTPUT START STOP MODE'
    a,q,ears,facets=load(sys.argv[1],sys.argv[2]);start,stop=map(int,sys.argv[4:6]);mode=sys.argv[6]
    if mode=='reducing':ears=[e for e in ears if e['triangles']>0]
    elif mode!='all':raise ValueError(mode)
    base=census(geometry(q));assert [base[k] for k in ('V','E','F','S','U')]==[176,311,137,1,1]
    report=dict(status='NUMERICAL_LOCATOR_NOT_CERTIFICATE',versions=[platform.python_version(),np.__version__,scipy.__version__],parameters=PARS,
     inputs=[dict(file=Path(p).name,bytes=Path(p).stat().st_size,sha256=sha(p)) for p in sys.argv[1:3]],
     range=[start,stop],mode=mode,baseline=base,trials=[])
    for ear in ears[start:stop]:
        for f in facets:
            K=np.vstack([np.delete(q,f,axis=0),ear['q']])
            try:
                qq,z,status,his=solve(K,q[f]);ct=census(z)
                record=dict(ear=ear['vertex'],deleted_triangles=ear['triangles'],released=f,q=qq.tolist(),status=status,centroid=(z['J']/z['V']).tolist(),census=ct,history=his)
            except (QhullError,AssertionError,np.linalg.LinAlgError) as exc:
                record=dict(ear=ear['vertex'],released=f,status='geometry_exception',detail=str(exc))
            report['trials'].append(record)
        Path(sys.argv[3]).write_text(json.dumps(report,sort_keys=True,separators=(',',':'))+'\n')
        print('EAR',ear['vertex'],[(r['released'],r['status'],[r.get('census',{}).get(k) for k in ('C','S','U')]) for r in report['trials'][-len(facets):]],flush=True)
    print('GLOBAL_C622_CENTROID_CUT_LOCATOR_FINISHED_NOT_CERTIFICATE',len(report['trials']),flush=True)
if __name__=='__main__':main()
