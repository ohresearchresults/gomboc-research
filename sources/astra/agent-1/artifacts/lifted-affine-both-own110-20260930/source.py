"""Free heights on a fixed projected grid, plus one physical affine map.

Releasing the heights deliberately releases the fibre-volume identities. The
convex hull, uniform volume centroid and both polar/primal escape landscapes
are recomputed on every body. At most84inputpoints ensure E<=246. No integration
triangulation is counted as true edges. Exact same-body certification is separate.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time,hashlib
import numpy as np,torch
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,eye,diags
from scipy.spatial import QhullError
from free_primal_goal import mesh_points
from shortest_escape_forest import shortest_forest
from geometry import arrows
from persistence_search import pairs
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def run(source,out,steps=1600,hard_side='Q',seed=932415):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);data=pathlib.Path(source).read_bytes();(out/'source_body.npz').write_bytes(data);src=np.load(out/'source_body.npz');A=src['matrix'];v=src['direction'];v=v/np.linalg.norm(v);raw=np.linalg.solve(A,src['X'].T).T
    if not 4<=len(raw)<=84:raise ValueError('Lifted height family requires4..84literal input points')
    heights=raw@v;B=raw-heights[:,None]*v;pars=src['parameters'][1:];rng=np.random.default_rng(seed);release=1e-7*np.sqrt(np.mean(raw*raw));heights+=release*rng.normal(size=len(heights));z=np.r_[heights,pars];N=len(heights);eps=2e-8;start=time.time();hist=[];failures=[];trust=.025
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes());np.savez(out/'family.npz',fixed_projection=B,direction=v);(out/'definition.json').write_text(json.dumps(dict(source=str(pathlib.Path(source).resolve()),sha256=hashlib.sha256(data).hexdigest(),seed=seed,steps=steps,hard_side=hard_side,explicit_height_release=release,
        scope='Literal free-height convex hull with common A and inverse-transpose polar, own uniform mass reintegrated; no fixed-centroid claim is transferred from the source'),indent=2))
    def points(zz):
        a=zz[N:];mat=np.array([[np.exp(a[0]),a[2],a[3]],[0,np.exp(a[1]),a[4]],[0,0,np.exp(-a[0]-a[1])]])
        if not np.isfinite(mat).all():raise ValueError('Nonfinite physical affine matrix')
        return (B+zz[:N,None]*v)@mat.T
    def evaluate(zz,jacobian=False):
        X=points(zz);m=mesh_points(X);st=m['row']
        if not 17<=st['E']<=249:raise ValueError('True physical complexity outside goal')
        if hard_side=='Q' and st['S']!=1:raise ValueError('Explicit unique-stable domain lost')
        if hard_side=='P' and st['U']!=1:raise ValueError('Explicit unique-unstable domain lost')
        selectors=[];values=[];bs=[]
        for pts,ed in [(m['P'],m['ep']),(m['R'],m['eq'])]:
            root=[int(np.argmax(np.sum(pts*pts,axis=1)))];pa,w,sg,_=shortest_forest(pts,root,eps);W=arrows(pts);values.append(w*(sg*W[np.arange(len(pts)),pa]-eps)+eps);selectors.append((pa,w,sg));pp,h=pairs(pts,ed);bs.append(1-h[pp[:,1]]/np.sum(pts[pp[:,0]]**2,axis=1))
        vals=np.r_[*values];nP=len(values[0]);hard=np.zeros(len(vals),bool)
        if hard_side=='P':hard[:nP]=True
        if hard_side=='Q':hard[nP:]=True
        score=float(np.maximum(eps-vals[~hard],0).sum());row=dict(**st,score=score,Pmax=float(max(bs[0],default=0)),Qmax=float(max(bs[1],default=0)),hard_minimum=float(min(vals[hard])) if hard.any() else None)
        res=dict(X=X,m=m,v=vals,hard=hard,nP=nP,row=row)
        if not jacobian:return res
        tt=torch.tensor(m['tri']);ti=torch.tensor(m['triples']);act=torch.tensor(m['active']);bt=torch.tensor(B);vt=torch.tensor(v)
        def physical(w):
            a=w[N:];zero=w.new_zeros(());mat=torch.stack([torch.stack([torch.exp(a[0]),a[2],a[3]]),torch.stack([zero,torch.exp(a[1]),a[4]]),torch.stack([zero,zero,torch.exp(-a[0]-a[1])])]);x=(bt+w[:N,None]*vt)@mat.T;t=x[tt];six=(t[:,0]*torch.linalg.cross(t[:,1],t[:,2])).sum(1);g=(six[:,None]*t.sum(1)).sum(0)/(4*six.sum());q=torch.linalg.solve(x[ti],torch.ones((len(ti),3,1)))[:,:,0];p=x[act]-g;r=q/(1-q@g)[:,None];vv=[]
            for pts,(pa,weights,sg) in zip([p,r],selectors):
                delta=pts[torch.tensor(pa)]-pts;angular=(pts*delta).sum(1)/(pts.norm(dim=1)*delta.norm(dim=1));vv.append(torch.tensor(weights)*(torch.tensor(sg)*angular-eps)+eps)
            return torch.cat([*vv,(x-g).flatten(),r.flatten()])
        tz=torch.tensor(zz);vv=physical(tz).detach().numpy();J=torch.func.jacrev(physical)(tz).detach().numpy();k=len(vals)
        if max(abs(vv[:k]-vals))>1e-6:raise ValueError('Differentiated lifted physical body disagrees with full hull')
        scales=np.r_[np.full(X.size,np.sqrt(np.mean((X-m['g'])**2))),np.full(m['R'].size,np.sqrt(np.mean(m['R']**2)))];metric=J[k:]/scales[:,None];_,s,Vt=svd(metric,full_matrices=False,check_finite=False);keep=s>max(s[0]*1e-11,1e-11)
        if not keep.any():raise ValueError('No observable lifted physical degrees of freedom')
        res.update(J=J[:k],W=Vt[keep].T/s[keep]);return res
    e=evaluate(z,True);np.savez(out/'entrance.npz',parameters=z,X=e['X'],Q=e['m']['Q']);d=rng.normal(size=len(z));d/=np.linalg.norm(d);mask=(e['v']<eps)&(~e['hard']);analytic=float(-e['J'][mask].sum(0)@d);checks=[]
    for h in [1e-7,1e-8,1e-9]:
        aa=evaluate(z+h*d);bb=evaluate(z-h*d);fd=(aa['row']['score']-bb['row']['score'])/(2*h);checks.append(dict(step=h,finite_difference=float(fd),analytic=analytic,error=float(abs(fd-analytic))))
    (out/'directional_check.json').write_text(json.dumps(checks,indent=2))
    if min(c['error'] for c in checks)>max(1e-4,abs(analytic)*1e-5):raise ValueError('Lifted actual-mass scalar objective derivative failed validation')
    def nominate(e,zz,label):
        if e['row']['S']==e['row']['U']==1:
            np.savez(out/'POTENTIAL_OWN110.npz',X=e['X'],Q=e['m']['Q'],parameters=zz,fixed_projection=B,direction=v);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(**label,**e['row']),indent=2));return True
        return False
    best=float('inf')
    for it in range(steps):
        e=evaluate(z,True);row=dict(it=it,trust=trust,seconds=time.time()-start,**e['row']);hist.append(row);np.savez(out/'latest.npz',parameters=z,X=e['X'],Q=e['m']['Q'],direction=v,fixed_projection=B);(out/'history.json').write_text(json.dumps(hist,indent=2))
        if it%10==0:print('LIFTED_FIBRE_OWN110_GOAL',json.dumps(row),flush=True)
        if nominate(e,z,dict(it=it,stage='accepted')):return
        if row['score']<best:best=row['score'];np.savez(out/'best.npz',parameters=z,X=e['X'],Q=e['m']['Q']);(out/'best.json').write_text(json.dumps(row,indent=2))
        W=e['W'];A=e['J']@W;n=W.shape[1];k=len(e['v']);bound=trust/np.sqrt(n);scale=np.maximum(bound*np.abs(A).sum(1),1e-12);mat=diags(1/scale)@hstack([-csr_matrix(A),-eye(k)],format='csr');rhs=(e['v']-eps)/scale
        lp=linprog(np.r_[np.zeros(n),np.ones(k)],A_ub=mat,b_ub=rhs,bounds=[(-bound,bound)]*n+[(0,0) if x else (0,None) for x in e['hard']],method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9});accepted=False
        if lp.success:
            dz=W@lp.x[:n]
            for level in range(18):
                zz=z+dz*2**-level
                try:
                    ee=evaluate(zz)
                    if nominate(ee,zz,dict(it=it,stage='proposal')):return
                    if ee['hard'].any() and min(ee['v'][ee['hard']])<.8*eps:continue
                    predicted=row['score']-float(np.maximum(eps-(e['v']+e['J']@dz*2**-level)[~e['hard']],0).sum())
                    if ee['row']['score']<row['score']-max(1e-14,1e-4*max(predicted,0)):z=zz;accepted=True;row.update(alpha=2**-level,predicted_progress=predicted,actual_progress=row['score']-ee['row']['score']);break
                except (ValueError,RuntimeError,AssertionError,QhullError,np.linalg.LinAlgError) as err:
                    if len(failures)<100:failures.append(dict(it=it,level=level,error=str(err)))
        if accepted and level==0:trust=min(.15,trust*1.2)
        elif not accepted:trust*=.4
        if trust<1e-10:break
    (out/'failed_proposals.json').write_text(json.dumps(failures,indent=2));(out/'FINITE_END.json').write_text(json.dumps(dict(iterations=len(hist),best=best,seconds=time.time()-start,scope='Finite free-height physical family ended without a qualifying body'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 1600,hard_side=None if len(sys.argv)>4 and sys.argv[4]=='none' else 'Q')
