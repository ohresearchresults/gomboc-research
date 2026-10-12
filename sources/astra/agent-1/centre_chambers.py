"""Search true off-centre 110 chambers by a finite mixed integer linear model.

For fixed physical hull geometry, every directed primal escape and every
directed polar escape is affine in the reference centre. Binary variables choose
an actually positive adjacent escape for each nonroot. This deliberately does
NOT replace the homogeneous centroid: it diagnoses the physical displacement
that a later deformation would have to achieve.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,pathlib,time,argparse
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix
from geometry import halfspace_mesh,census,arrows
from persistence_search import polar_edges

def inequalities(m):
    X=m['X']-m['g'];Q=m['Q']/(1-m['Q']@m['g'])[:,None]
    rows=[]
    for kind,A,edges in [('P',X,m['edges']),('Q',Q,polar_edges(m))]:
        for i,j in np.vstack([edges,edges[:,::-1]]):
            a=A[i];b=A[j];d=b-a;scale=np.linalg.norm(a)*np.linalg.norm(d)
            if kind=='P':constant=a@d;linear=-d
            else:constant=a@b-a@a;linear=(a@a)*b-(a@b)*a
            rows.append((kind,int(i),int(j),constant/scale,linear/scale))
    return X,Q,rows

def solve(Q,rootP,rootQ,box=1.,eps=1e-7,timelimit=20):
    m=halfspace_mesh(Q);X,R,rows=inequalities(m);scale=np.sqrt(np.mean(np.sum(X*X,1)))
    box*=scale;roots={'P':rootP,'Q':rootQ};need={('P',i) for i in range(len(X)) if i!=rootP}|{('Q',int(i)) for i in m['active'] if i!=rootQ}
    rootrows=[];candidates=[];guaranteed=set()
    for kind,i,j,b,a in rows:
        if i==roots[kind]:rootrows.append((b,a));continue
        lo=b-box*np.abs(a).sum();hi=b+box*np.abs(a).sum()
        if lo>=eps:guaranteed.add((kind,i))
        if hi>=eps:candidates.append((kind,i,j,b,a,lo))
    need-=guaranteed;candidates=[r for r in candidates if (r[0],r[1]) in need]
    by={key:[] for key in need}
    for k,r in enumerate(candidates):by[r[:2]].append(k)
    if any(not x for x in by.values()):return {'status':'impossible_escape_over_box','box':box}
    n=4+len(candidates);nr=len(rootrows)+len(candidates)+len(need)+len(R)+6
    A=lil_matrix((nr,n));low=np.full(nr,-np.inf);high=np.full(nr,np.inf);k=0
    for b,a in rootrows:A[k,:3]=a;high[k]=-eps-b;k+=1
    for z,(kind,i,j,b,a,lo) in enumerate(candidates):
        big=max(eps-lo,0);A[k,:3]=a;A[k,4+z]=-big;low[k]=eps-b-big;k+=1
    for zz in by.values():A[k,[4+j for j in zz]]=1;low[k]=1;k+=1
    for r in R:A[k,:3]=r;high[k]=1-1e-5;k+=1
    for j in range(3):
        for sign in [-1,1]:A[k,j]=sign;A[k,3]=-1;high[k]=0;k+=1
    assert k==nr
    cost=np.r_[np.zeros(3),1,np.zeros(len(candidates))];t0=time.time()
    result=milp(cost,integrality=np.r_[np.zeros(4),np.ones(len(candidates))],bounds=Bounds(np.r_[np.full(3,-box),0,np.zeros(len(candidates))],np.r_[np.full(4,box),np.ones(len(candidates))]),constraints=LinearConstraint(A.tocsr(),low,high),options={'time_limit':timelimit,'mip_rel_gap':1e-6,'mip_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
    out={'status':str(result.message),'solver_status':int(result.status),'seconds':time.time()-t0,'box':box,'rootP':rootP,'rootQ':rootQ,'binary_count':len(candidates),'own_census':census(m)}
    if result.x is not None:
        c=result.x[:3];p=X-c;q=R/(1-R@c)[:,None];wp=arrows(p);wq=arrows(q[m['active']]);u=np.flatnonzero(wp.max(1)<-1e-10);s=m['active'][np.flatnonzero(wq.max(1)<-1e-10)]
        out.update(relative_centre=c.tolist(),physical_centre=(c+m['g']).tolist(),distance=float(np.linalg.norm(c)),linf_distance=float(np.max(abs(c))),reference_S=s.tolist(),reference_U=u.tolist(),minimum_primal_nonroot=float(np.min(np.delete(wp.max(1),rootP))),minimum_polar_nonroot=float(np.min(np.delete(wq.max(1),np.flatnonzero(m['active']==rootQ)))))
        out['verified_reference110_numerically']=bool(len(s)==len(u)==1 and out['minimum_primal_nonroot']>0 and out['minimum_polar_nonroot']>0)
    return out

def run(input,out,box=.5,time_limit=20):
    Q=np.load(input)['Q'];m=halfspace_mesh(Q);own=census(m);p=pathlib.Path(out);p.mkdir(parents=True,exist_ok=True);hist=[]
    for u in own['U_ids']:
        for s in own['S_ids']:
            row=solve(Q,u,s,box=box,timelimit=time_limit);hist.append(row);print(json.dumps(row),flush=True);(p/'results.json').write_text(json.dumps(hist,indent=2))
    return hist

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--box',type=float,default=.5);ap.add_argument('--time-limit',type=float,default=20);a=ap.parse_args();run(a.input,a.out,a.box,a.time_limit)
