"""Direct dynamic-hull search in literal C2 support coordinates.

Each objective and derivative uses the actual uniform centroid. Extra roots
are allowed along the search path; only complete actual own110 is nominated.
The fixed bottom support merely fixes a scale. The last two orbit z values
are identical, preserving a possible four-plane axial vertex.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time
import numpy as np
import torch
from scipy.optimize import linprog
from scipy.linalg import svd
from scipy.sparse import csr_matrix,eye,hstack
from scipy.spatial import QhullError
from geometry import halfspace_mesh,census
from persistence_search import pairs,polar_edges
from bottleneck_capacity import capacities
from free_centred_polar_flow import pack,unpack

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def evaluate(z,mode='bars',jacobian=False):
    Q=np.r_[[[0.,0.,-1.]],unpack(z)];m=halfspace_mesh(Q);st=census(m,0)
    if not 17<=st['E']<=249:raise ValueError('True numerical edge budget violated')
    active=m['active'];P=m['X']-m['g'];R=Q[active]/(1-Q[active]@m['g'])[:,None]
    edgeP=m['edges'];edgeQ=polar_edges(m);inv=np.full(len(Q),-1,int);inv[active]=np.arange(len(active));edgeQ=inv[edgeQ]
    selectors=[];vectors=[];bars=[]
    for side,(A,ed) in enumerate([(P,edgeP),(R,edgeQ)]):
        pp,h=pairs(A,ed);b=1-h[pp[:,1]]/np.sum(A[pp[:,0]]**2,axis=1);bars.append(b)
        if mode=='bars':selectors.append((pp,ed));vectors.append(b)
        else:
            root=int(np.argmax(np.sum(A*A,axis=1)))
            if mode in ['axis-capacity','axis-raw-capacity']:
                if side==0:
                    transverse=np.linalg.norm(A[:,:2],axis=1);root=int(np.argmin(transverse))
                    if transverse[root]>1e-8*np.max(np.linalg.norm(A,axis=1)):raise ValueError('Literal C2 axial unstable carrier absent')
                else:
                    ids=np.flatnonzero(active==0)
                    if len(ids)!=1:raise ValueError('Literal axial stable facet absent')
                    root=int(ids[0])
            cap,ii,jj,sg=capacities(A,[root],normalization='radius_squared' if 'raw-capacity' in mode else 'angular');selectors.append((ii,jj,sg));vectors.append(cap)
    values=np.r_[*vectors];eps=2e-7
    score=float(values.sum()) if mode=='bars' else float(np.maximum(eps-values,0).sum())
    row=dict(**st,score=score,Pmax=float(max(bars[0],default=0)),Qmax=float(max(bars[1],default=0)),
             P=bars[0].tolist(),Qbars=bars[1].tolist(),minimum=float(min(values,default=0)))
    out=dict(Q=Q,m=m,row=row,v=values)
    if not jacobian:return out
    ti=torch.tensor(m['triples']);tt=torch.tensor(m['triangles']);act=torch.tensor(active)
    def physical(w):
        q=torch.cat([w,w[-3:-2]]).reshape(-1,3)
        other=torch.stack([q,q*torch.tensor([-1.,-1.,1.])],dim=1).reshape(-1,3)
        qt=torch.cat([torch.tensor([[0.,0.,-1.]]),other]);x=torch.linalg.solve(qt[ti],torch.ones((len(ti),3,1)))[:,:,0]
        a=x[tt];six=(a[:,0]*torch.linalg.cross(a[:,1],a[:,2])).sum(1);g=(six[:,None]*a.sum(1)).sum(0)/(4*six.sum())
        p=x-g;r=qt[act]/(1-qt[act]@g)[:,None];vv=[]
        for A,s in zip([p,r],selectors):
            if mode=='bars':
                pp,ed=s;bi=torch.tensor(pp[:,0]);ee=torch.tensor(ed[pp[:,1]])
                aa=A[ee[:,0]];dd=A[ee[:,1]]-aa;frac=(-(aa*dd).sum(1)/(dd*dd).sum(1)).clamp(0,1)
                vv.append(1-((aa+frac[:,None]*dd)**2).sum(1)/(A[bi]**2).sum(1))
            else:
                ii,jj,sg=s;src=A[torch.tensor(ii)];dd=A[torch.tensor(jj)]-src
                den=(src*src).sum(1) if 'raw-capacity' in mode else src.norm(dim=1)*dd.norm(dim=1)
                vv.append(torch.tensor(sg)*(src*dd).sum(1)/den)
        # The joint primal/dual physical metric avoids turning a tiny support
        # move near a poorly conditioned vertex into an unrestricted body step.
        return torch.cat([*vv,p.flatten(),r.flatten()])
    w=torch.tensor(z);val=physical(w).detach().numpy();J=torch.func.jacrev(physical)(w).detach().numpy();n=len(values)
    if np.max(abs(val[:n]-values),initial=0)>1e-8:raise ValueError('Actual differentiated mechanics failed its independent readback')
    scales=np.r_[np.full(P.size,np.sqrt(np.mean(P*P))),np.full(R.size,np.sqrt(np.mean(R*R)))]
    metric=J[n:]/scales[:,None];_,s,Vt=svd(metric,full_matrices=False,check_finite=False)
    # Inactive input rows give exact null directions. Freeze only those
    # physically invisible directions in this step; their coordinates remain
    # explicit in the stored physical construction.
    keep=s>max(s[0]*1e-11,1e-11);W=Vt[keep].T/s[keep]
    if not np.any(keep):raise ValueError('No visible shape directions')
    out.update(J=J[:n],W=W)
    return out

def run(source,out,mode='bars',steps=800,trust=.08):
    source=pathlib.Path(source);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False)
    Q=np.load(source)['Q'];Q=Q/(-Q[0,2]);z=pack(Q)
    np.savez(out/'entrance.npz',Q=Q,z=z);(out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    (out/'definition.json').write_text(json.dumps(dict(source=str(source.resolve()),mode=mode,steps=steps,initial_trust=trust,
        scope='Same uniform physical body and fresh true hull at each proposal; only own110 nominated'),indent=2))
    hist=[];failures=[];start=time.time();best=np.inf
    def preserve(e,z,row):
        np.savez(out/'POTENTIAL_OWN110.npz',Q=e['Q'],X=e['m']['X'],z=z)
        (out/'POTENTIAL_OWN110.json').write_text(json.dumps(row,indent=2))
    for it in range(steps):
        e=evaluate(z,mode,True);row=dict(it=it,trust=trust,seconds=time.time()-start,**e['row']);hist.append(row)
        np.savez(out/'latest.npz',Q=e['Q'],X=e['m']['X'],z=z);(out/'history.json').write_text(json.dumps(hist,indent=2))
        if it%10==0:print('CYCLIC_ACTUAL_GOAL',json.dumps({k:v for k,v in row.items() if k not in ['S_ids','U_ids','P','Qbars']}),flush=True)
        if row['S']==row['U']==1:preserve(e,z,row);return
        if row['score']<best:
            best=row['score'];np.savez(out/'best.npz',Q=e['Q'],X=e['m']['X'],z=z);(out/'best.json').write_text(json.dumps(row,indent=2))
        W=e['W'];A=e['J']@W;n=W.shape[1];k=len(e['v']);bound=trust/np.sqrt(n)
        if mode=='bars':mat=hstack([csr_matrix(A),-eye(k)],format='csr');rhs=-e['v']
        else:mat=hstack([-csr_matrix(A),-eye(k)],format='csr');rhs=e['v']-2e-7
        # Per-row scaling preserves each linearized physical constraint while
        # avoiding solver feasibility tolerances larger than short-arrow rows.
        scale=np.maximum(np.abs(A).sum(1)*bound,1e-10)
        from scipy.sparse import diags
        mat=diags(1/scale)@mat;rhs=rhs/scale
        lp=linprog(np.r_[np.zeros(n),np.ones(k)],A_ub=mat,b_ub=rhs,bounds=[(-bound,bound)]*n+[(0,None)]*k,
                   method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        accepted=False
        if lp.success:
            dz=W@lp.x[:n]
            for level in range(15):
                zz=z+dz*2**-level
                try:
                    ee=evaluate(zz,mode)
                    if ee['row']['S']==ee['row']['U']==1:preserve(ee,zz,dict(it=it,stage='proposal',**ee['row']));return
                    if ee['row']['score']<row['score']*(1-1e-6):z=zz;accepted=True;break
                except (ValueError,RuntimeError,AssertionError,QhullError,np.linalg.LinAlgError) as error:
                    if len(failures)<80:failures.append(dict(it=it,level=level,error=repr(error)))
        if accepted and level==0:trust=min(.3,trust*1.2)
        elif not accepted:trust*=.4
        if trust<1e-10:break
    (out/'failed_proposals.json').write_text(json.dumps(failures,indent=2))
    (out/'FINITE_END.json').write_text(json.dumps(dict(iterations=len(hist),best=best,seconds=time.time()-start,
        scope='Finite numerical direct search ended without a qualifying figure'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],sys.argv[2],sys.argv[3] if len(sys.argv)>3 else 'bars',int(sys.argv[4]) if len(sys.argv)>4 else 800)
