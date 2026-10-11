"""All asymmetric physical vertices free, uniform-centroid gauge eliminated.

The three coordinates of vertex0 are solved from the actual volume centroid.
Their implicit derivative is obtained from the full physical mass Jacobian.
All other vertices can move and the real hull can change. A hard unique-U
admission is imposed on that same body; only complete own110 is a nomination.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time,hashlib
import numpy as np,torch
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack,diags
from scipy.spatial import QhullError
from asymmetric_apex_mass_goal import close_mass
from free_primal_goal import mesh_points
from geometry import arrows
from bottleneck_capacity import capacities
from persistence_search import pairs
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def evaluate(z,apex,mode='local',jacobian=False):
    X=np.r_[[apex],z.reshape(-1,3)];X,_=close_mass(X);m=mesh_points(X);st=m['row']
    if not 17<=st['E']<=249 or st['U']!=1:raise ValueError('Physical hull outside budget or unique-U domain')
    if m['active'][0]!=0:raise ValueError('Implicit mass apex is not a hull vertex')
    sel=[];vv=[];bars=[]
    for side,(A,ed) in enumerate([(m['P'],m['ep']),(m['R'],m['eq'])]):
        W=arrows(A);root=int(np.argmax(np.sum(A*A,axis=1)))
        if side==0 and root!=0:raise ValueError('Unstable root identity changed')
        if side==0 or mode=='local':
            ii=np.arange(len(A));jj=W.argmax(1);sg=np.ones(len(A));sg[root]=-1;v=sg*W[ii,jj]
        elif mode=='capacity':v,ii,jj,sg=capacities(A,[root])
        else:raise ValueError('Unknown explicit polar escape merit')
        sel.append((ii,jj,sg));vv.append(v);pp,h=pairs(A,ed);bars.append(1-h[pp[:,1]]/np.sum(A[pp[:,0]]**2,axis=1))
    vals=np.r_[*vv];row=dict(**st,Pmax=float(max(bars[0],default=0)),Qmax=float(max(bars[1],default=0)),minimum_U=float(vv[0].min()),score=float(np.maximum(2e-8-vv[1],0).sum()))
    result=dict(X=X,m=m,v=vals,nP=len(vv[0]),row=row)
    if not jacobian:return result
    tt=torch.tensor(m['tri']);ti=torch.tensor(m['triples']);act=torch.tensor(m['active'])
    def physical(w):
        x=w.reshape(-1,3);a=x[tt];six=(a[:,0]*torch.linalg.cross(a[:,1],a[:,2])).sum(1);g=(six[:,None]*a.sum(1)).sum(0)/(4*six.sum());q=torch.linalg.solve(x[ti],torch.ones((len(ti),3,1)))[:,:,0];p=x[act]-g;r=q/(1-q@g)[:,None];values=[]
        for A,(ii,jj,sg) in zip([p,r],sel):
            src=A[torch.tensor(ii)];d=A[torch.tensor(jj)]-src;values.append(torch.tensor(sg)*(src*d).sum(1)/(src.norm(dim=1)*d.norm(dim=1)))
        return torch.cat([g,*values,p.flatten(),r.flatten()])
    w=torch.tensor(X.ravel());y=physical(w).detach().numpy();J=torch.func.jacrev(physical)(w).detach().numpy()
    if max(abs(y[3:3+len(vals)]-vals))>1e-7:raise ValueError('Differentiated complete physical hull disagrees with readback')
    Dg=J[:3];T=np.r_[-np.linalg.solve(Dg[:,:3],Dg[:,3:]),np.eye(len(z))];allJ=J[3:]@T;n=len(vals)
    scale=np.r_[np.full(m['P'].size,np.sqrt(np.mean(m['P']**2))),np.full(m['R'].size,np.sqrt(np.mean(m['R']**2)))]
    metric=allJ[n:]/scale[:,None];_,s,Vt=svd(metric,full_matrices=False,check_finite=False);keep=s>max(s[0]*1e-11,1e-11)
    if not np.any(keep):raise ValueError('No observable physical shape directions')
    result.update(J=allJ[:n],W=Vt[keep].T/s[keep]);return result

def run(source,out,mode='local',steps=1200,seed=934733):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);data=pathlib.Path(source).read_bytes();(out/'source_body.npz').write_bytes(data);X=np.load(out/'source_body.npz')['X'];m=mesh_points(X);X=X[m['active']]
    if len(X)>84:raise ValueError('Free-point branch requires at most84physical vertices')
    rng=np.random.default_rng(seed);release=1e-5*np.sqrt(np.mean(X*X));X[1:]+=release*rng.normal(size=X[1:].shape);X,_=close_mass(X)
    np.savez(out/'entrance.npz',X=X)
    z=X[1:].ravel();apex=X[0];trust=.035;eps=2e-8;start=time.time();hist=[];failures=[];best=float('inf')
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes());(out/'definition.json').write_text(json.dumps(dict(source=str(pathlib.Path(source).resolve()),sha256=hashlib.sha256(data).hexdigest(),mode=mode,steps=steps,seed=seed,explicit_physical_contact_release=release,
        scope='All physical asymmetric vertices free with implicit uniform mass and hard U1; only own110 nominates exact verification'),indent=2))
    first=evaluate(z,apex,mode,True);d=rng.normal(size=len(z));d/=np.linalg.norm(d);h=1e-8
    a=evaluate(z+h*d,apex,mode);b=evaluate(z-h*d,apex,mode);fd=(a['v']-b['v'])/(2*h);err=float(max(abs(fd-first['J']@d)))
    (out/'directional_check.json').write_text(json.dumps(dict(step=h,error=err),indent=2))
    if err>2e-5:raise ValueError('Implicit whole-body escape derivative check failed')
    def nominate(e,label):
        if e['row']['S']==e['row']['U']==1:
            np.savez(out/'POTENTIAL_OWN110.npz',X=e['X'],Q=e['m']['Q']);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(**label,**e['row']),indent=2));return True
        return False
    for it in range(steps):
        e=evaluate(z,apex,mode,True);apex=e['X'][0];row=dict(it=it,trust=trust,seconds=time.time()-start,**e['row']);hist.append(row);np.savez(out/'latest.npz',X=e['X'],Q=e['m']['Q']);(out/'history.json').write_text(json.dumps(hist,indent=2))
        if it%10==0:print('FREE_ASYMMETRIC_MASS_GOAL',json.dumps(row),flush=True)
        if nominate(e,dict(it=it,stage='accepted')):return
        if row['score']<best:best=row['score'];np.savez(out/'best.npz',X=e['X'],Q=e['m']['Q']);(out/'best.json').write_text(json.dumps(row,indent=2))
        W=e['W'];A=e['J']@W;n=W.shape[1];k=len(e['v']);np_=e['nP'];bound=trust/np.sqrt(n);scale=np.maximum(bound*np.abs(A).sum(1),1e-12)
        mat=diags(1/scale)@hstack([-csr_matrix(A),-eye(k)],format='csr');rhs=(e['v']-eps)/scale
        lp=linprog(np.r_[np.zeros(n),np.ones(k)],A_ub=mat,b_ub=rhs,bounds=[(-bound,bound)]*n+[(0,0)]*np_+[(0,None)]*(k-np_),method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        accepted=False
        if lp.success:
            dz=W@lp.x[:n]
            for level in range(17):
                zz=z+dz*2**-level
                try:
                    ee=evaluate(zz,apex,mode)
                    if nominate(ee,dict(it=it,stage='proposal')):return
                    if ee['row']['minimum_U']<.8*eps:continue
                    predicted=row['score']-float(np.maximum(eps-(e['v'][np_:]+(e['J']@dz)[np_:]*2**-level),0).sum())
                    if ee['row']['score']<row['score']-max(1e-14,1e-4*max(predicted,0)):
                        z=zz;apex=ee['X'][0];accepted=True;row.update(alpha=2**-level,predicted_progress=predicted,actual_progress=row['score']-ee['row']['score']);break
                except (ValueError,RuntimeError,AssertionError,QhullError,np.linalg.LinAlgError) as err:
                    if len(failures)<100:failures.append(dict(it=it,level=level,error=str(err)))
        if accepted and level==0:trust=min(.2,trust*1.2)
        elif not accepted:trust*=.4
        if trust<1e-10:break
    (out/'failed_proposals.json').write_text(json.dumps(failures,indent=2));(out/'FINITE_END.json').write_text(json.dumps(dict(iterations=len(hist),seconds=time.time()-start,best=best,scope='Finite full physical shape search ended without a qualifying body'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],sys.argv[2],sys.argv[3] if len(sys.argv)>3 else 'local',int(sys.argv[4]) if len(sys.argv)>4 else 1200)
