"""Actual-centroid search with freely moving physical hull vertices.

No prescribed integration triangulation is counted as a hull edge. Complete
maximal facets and true edges are rebuilt from the convex hull at each step.
V<=84 gives E<=246 even after generic contact release. Every derivative uses
the same body's uniform mass; rational certification is separate.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import json,pathlib,time
import numpy as np
import torch
from scipy.spatial import ConvexHull,QhullError
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,diags
from geometry import arrows
from persistence_search import pairs
from bottleneck_capacity import capacities

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def mesh_points(X):
    h=ConvexHull(X)
    if h.equations[:,3].max()>=-1e-9:raise ValueError('Reference origin outside literal point hull')
    # Coalescing is only a numerical search incidence oracle. Every accepted
    # body must be reconstructed from rational points and exactly rehulled.
    equations=[];groups=[];triples=[]
    for t,e in zip(h.simplices,h.equations):
        hit=next((i for i,q in enumerate(equations) if np.max(abs(e-q))<1e-9),None)
        if hit is None:equations.append(e);groups.append(set(map(int,t)));triples.append(t)
        else:
            groups[hit].update(map(int,t))
            if abs(np.linalg.det(X[t]))>abs(np.linalg.det(X[triples[hit]])):triples[hit]=t
    triples=np.array(triples);Q=np.linalg.solve(X[triples],np.ones((len(triples),3,1)))[:,:,0]
    active=np.array(sorted(set(h.vertices)),int);inv=np.full(len(X),-1,int);inv[active]=np.arange(len(active))
    faces=[];tri=[];edges={}
    for f,ids in enumerate(groups):
        ids=np.array(sorted(ids),int);p=X[ids];center=p.mean(0);a=p[0]-center;a/=np.linalg.norm(a);b=np.cross(Q[f],a);b/=np.linalg.norm(b)
        cy=ids[np.argsort(np.arctan2((p-center)@b,(p-center)@a))].tolist();faces.append(cy)
        tri.extend([cy[0],cy[k],cy[k+1]] for k in range(1,len(cy)-1))
        for i,j in zip(cy,cy[1:]+cy[:1]):edges.setdefault(tuple(sorted((i,j))),[]).append(f)
    if len(active)-len(edges)+len(faces)!=2 or any(len(e)!=2 for e in edges.values()):raise ValueError('Complete numerical hull boundary inconsistent')
    tri=np.array(tri);a=X[tri];six=np.einsum('ij,ij->i',a[:,0],np.cross(a[:,1],a[:,2]));V=six.sum()/6
    if min(six)<=0 or V<=0:raise ValueError('Nonpositive physical boundary volume')
    g=(six[:,None]*a.sum(1)).sum(0)/(4*six.sum());P=X[active]-g;R=Q/(1-Q@g)[:,None]
    ep=inv[np.array(list(edges))];eq=np.array(list(edges.values()));wp=arrows(P).max(1);wq=arrows(R).max(1)
    st=dict(V=len(active),E=len(edges),F=len(faces),C=2*len(edges),S=int(sum(wq<0)),U=int(sum(wp<0)),
            min_primal_nonroot=float(np.sort(wp)[1]),min_polar_nonroot=float(np.sort(wq)[1]),centroid=g.tolist(),volume=float(V))
    return dict(X=X,Q=Q,P=P,R=R,g=g,active=active,tri=tri,triples=triples,ep=ep,eq=eq,faces=faces,row=st)

def evaluate(z,mode='capacity',jacobian=False,epsilon=2e-7):
    X=z.reshape(-1,3);m=mesh_points(X);st=m['row']
    if not 17<=st['E']<=249:raise ValueError('Actual edge count outside target budget')
    selectors=[];values=[];bars=[]
    for A,ed in [(m['P'],m['ep']),(m['R'],m['eq'])]:
        pp,h=pairs(A,ed);b=1-h[pp[:,1]]/np.sum(A[pp[:,0]]**2,axis=1);bars.append(b)
        if mode=='bars':selectors.append((pp,ed));values.append(b)
        else:
            cap,ii,jj,sg=capacities(A,[int(np.argmax(np.sum(A*A,axis=1)))]);selectors.append((ii,jj,sg));values.append(cap)
    vals=np.r_[*values];score=float(vals.sum()) if mode=='bars' else float(np.maximum(epsilon-vals,0).sum())
    row=dict(**st,score=score,Pmax=float(max(bars[0],default=0)),Qmax=float(max(bars[1],default=0)),P=bars[0].tolist(),Qbars=bars[1].tolist())
    out=dict(m=m,v=vals,row=row)
    if not jacobian:return out
    ti=torch.tensor(m['triples']);tt=torch.tensor(m['tri']);act=torch.tensor(m['active'])
    def physical(w):
        x=w.reshape(-1,3);a=x[tt];six=(a[:,0]*torch.linalg.cross(a[:,1],a[:,2])).sum(1)
        g=(six[:,None]*a.sum(1)).sum(0)/(4*six.sum());q=torch.linalg.solve(x[ti],torch.ones((len(ti),3,1)))[:,:,0]
        p=x[act]-g;r=q/(1-q@g)[:,None];vv=[]
        for A,s in zip([p,r],selectors):
            if mode=='bars':
                pp,ed=s;bi=torch.tensor(pp[:,0]);ee=torch.tensor(ed[pp[:,1]])
                aa=A[ee[:,0]];dd=A[ee[:,1]]-aa;t=(-(aa*dd).sum(1)/(dd*dd).sum(1)).clamp(0,1)
                vv.append(1-((aa+t[:,None]*dd)**2).sum(1)/(A[bi]**2).sum(1))
            else:
                ii,jj,sg=s;src=A[torch.tensor(ii)];dd=A[torch.tensor(jj)]-src
                vv.append(torch.tensor(sg)*(src*dd).sum(1)/(src.norm(dim=1)*dd.norm(dim=1)))
        return torch.cat([*vv,p.flatten(),r.flatten()])
    w=torch.tensor(z);v=physical(w).detach().numpy();J=torch.func.jacrev(physical)(w).detach().numpy();n=len(vals)
    if np.max(abs(v[:n]-vals),initial=0)>1e-7:raise ValueError('Differentiated actual body disagrees with its numerical hull')
    scales=np.r_[np.full(m['P'].size,np.sqrt(np.mean(m['P']**2))),np.full(m['R'].size,np.sqrt(np.mean(m['R']**2)))]
    metric=J[n:]/scales[:,None];_,s,Vt=svd(metric,full_matrices=False,check_finite=False);keep=s>max(s[0]*1e-11,1e-11)
    if not np.any(keep):raise ValueError('No visible physical directions')
    out.update(J=J[:n],W=Vt[keep].T/s[keep]);return out

def run(X,out,mode='capacity',steps=1000,trust=.06,provenance=None):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);X=np.asarray(X).copy()
    if not 4<=len(X)<=84:raise ValueError('Explicit finite vertex budget exceeded')
    m=mesh_points(X);X-=m['g'];X/=np.sqrt(np.mean(np.sum(X*X,axis=1)));z=X.ravel()
    np.savez(out/'entrance.npz',X=X);(out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    (out/'definition.json').write_text(json.dumps(dict(mode=mode,steps=steps,trust=trust,provenance=provenance,
        scope='All physical vertices free, actual mass and complete dynamic hull; no partial census is accepted'),indent=2))
    hist=[];failures=[];start=time.time();best=np.inf
    def save_potential(ee,zz,row):
        np.savez(out/'POTENTIAL_OWN110.npz',X=zz.reshape(-1,3),Q=ee['m']['Q'])
        (out/'POTENTIAL_OWN110.json').write_text(json.dumps(row,indent=2))
    for it in range(steps):
        e=evaluate(z,mode,True);row=dict(it=it,trust=trust,seconds=time.time()-start,**e['row']);hist.append(row)
        np.savez(out/'latest.npz',X=z.reshape(-1,3),Q=e['m']['Q']);(out/'history.json').write_text(json.dumps(hist,indent=2))
        if it%10==0:print('FREE_PRIMAL_OWN110',json.dumps({k:v for k,v in row.items() if k not in ['P','Qbars']}),flush=True)
        if row['S']==row['U']==1:save_potential(e,z,row);return
        if row['score']<best:
            best=row['score'];np.savez(out/'best.npz',X=z.reshape(-1,3),Q=e['m']['Q']);(out/'best.json').write_text(json.dumps(row,indent=2))
        W=e['W'];A=e['J']@W;n=W.shape[1];k=len(e['v']);bound=trust/np.sqrt(n)
        if mode=='bars':mat=hstack([csr_matrix(A),-eye(k)],format='csr');rhs=-e['v']
        else:mat=hstack([-csr_matrix(A),-eye(k)],format='csr');rhs=e['v']-2e-7
        scale=np.maximum(np.abs(A).sum(1)*bound,1e-10);mat=diags(1/scale)@mat;rhs=rhs/scale
        lp=linprog(np.r_[np.zeros(n),np.ones(k)],A_ub=mat,b_ub=rhs,bounds=[(-bound,bound)]*n+[(0,None)]*k,
            method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        accepted=False
        if lp.success:
            dz=W@lp.x[:n]
            for level in range(16):
                zz=z+dz*2**-level
                try:
                    ee=evaluate(zz,mode)
                    if ee['row']['S']==ee['row']['U']==1:save_potential(ee,zz,dict(it=it,stage='proposal',**ee['row']));return
                    if ee['row']['score']<row['score']*(1-1e-6):z=zz;accepted=True;break
                except (ValueError,RuntimeError,AssertionError,QhullError,np.linalg.LinAlgError) as error:
                    if len(failures)<80:failures.append(dict(it=it,level=level,error=repr(error)))
        if accepted and level==0:trust=min(.25,trust*1.2)
        elif not accepted:trust*=.4
        if trust<1e-10:break
    (out/'failed_proposals.json').write_text(json.dumps(failures,indent=2))
    (out/'FINITE_END.json').write_text(json.dumps(dict(iterations=len(hist),best=best,seconds=time.time()-start,
        scope='Finite direct same-body search; no qualifying figure found'),indent=2))

if __name__=='__main__':
    import sys,gmpy2
    p=pathlib.Path(sys.argv[1]);mode=sys.argv[3] if len(sys.argv)>3 else 'capacity'
    if p.suffix=='.json':X=np.array([[float(gmpy2.mpq(v)) for v in row] for row in json.loads(p.read_text())['raw_vertices']])
    else:X=np.load(p)['X']
    run(X,sys.argv[2],mode,int(sys.argv[4]) if len(sys.argv)>4 else 1000,provenance=str(p.resolve()))
