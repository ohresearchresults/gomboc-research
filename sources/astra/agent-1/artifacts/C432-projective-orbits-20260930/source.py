"""Physical projective orbits of specified recent own-centroid bodies.

Each image is the actual homogeneous solid y=A p/(1+b.p). Its mass is
integrated again; the dual is A^{-T}(q+b) before translating by that new
centroid. No independent primal/dual metric relaxation is used.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,pathlib,json,time,hashlib
import numpy as np,torch
from scipy.optimize import minimize
from contact_forest import ContactModel
from geometry import arrows
from persistence_search import pairs

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def run(source,input,out,tries=48,seed=942781):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False)
    c=ContactModel(source,1,1,'local');e=c.evaluate(np.load(input)['z'],False)
    X=e['P'];Q=e['Q'];radius=np.sqrt(np.mean(np.sum(X*X,axis=1)))
    X=X/radius;Q=Q*radius;xt=torch.tensor(X);qt=torch.tensor(Q);tt=torch.tensor(c.tri)
    rng=np.random.default_rng(seed);history=[];start=time.time();best=np.inf;bestz=np.zeros(8)
    np.savez(out/'physical_parent.npz',X=X,Q=Q,triangles=c.tri,primal_edges=c.eu,polar_edges=c.es)
    (out/'definition.json').write_text(json.dumps(dict(source=str(pathlib.Path(source).resolve()),
        input=str(pathlib.Path(input).resolve()),source_hash=hashlib.sha256(pathlib.Path(input).read_bytes()).hexdigest(),
        tries=tries,seed=seed,E=c.meta['E'],physical_map='y=A p/(1+b.p), detA=1; new uniform mass integrated',
        scope='Finite physical projective search; all numerical candidates require same-body rational reconstruction'),indent=2))
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    def geo(z):
        zero=z[0]*0
        A=torch.stack([torch.stack([z[0].exp(),z[2],z[3]]),torch.stack([zero,z[1].exp(),z[4]]),
                       torch.stack([zero,zero,(-z[0]-z[1]).exp()])])
        b=z[5:];den=1+xt@b;Y=(xt@A.T)/den[:,None]
        H=torch.linalg.solve(A.T,(qt+b).T).T
        v=Y[tt];six=(v[:,0]*torch.linalg.cross(v[:,1],v[:,2])).sum(1)
        volume=six.sum()/6;g=(six[:,None]*v.sum(1)).sum(0)/(4*six.sum())
        return Y-g,H/(1-H@g)[:,None],Y,H,A,b,g,volume,den
    def loss(z,eta):
        zz=torch.tensor(z,requires_grad=True);den=1+xt@zz[5:]
        if float(den.min().detach())<.08:
            f=10+100*((.08-den).clamp(min=0)**2).sum()
        else:
            pp,qq,*_=geo(zz);f=zz.sum()*0
            for points,edges in [(pp,c.eu),(qq,c.es)]:
                pair,_=pairs(points.detach().numpy(),edges)
                if not len(pair):continue
                bi=torch.tensor(pair[:,0]);ed=torch.tensor(edges[pair[:,1]])
                a=points[ed[:,0]];d=points[ed[:,1]]-a
                t=(-(a*d).sum(1)/(d*d).sum(1)).clamp(0,1)
                depth=(1-((a+t[:,None]*d)**2).sum(1)/(points[bi]**2).sum(1)).clamp(min=0)
                f=f+eta*torch.log1p(depth/eta).sum()
        gradient=torch.autograd.grad(f,zz)[0].detach().numpy()
        return float(f.detach()),gradient
    def inspect(z):
        pp,qq,Y,H,A,b,g,volume,den=geo(torch.tensor(z))
        a=[v.detach().numpy() for v in (pp,qq,Y,H,A,b,g,volume,den)]
        if a[-1].min()<=0 or a[-2]<=0:raise ValueError('Projective denominator or integrated mass nonpositive')
        bars=[]
        for points,edges in [(a[0],c.eu),(a[1],c.es)]:
            pair,h=pairs(points,edges)
            bars.append((1-h[pair[:,1]]/np.sum(points[pair[:,0]]**2,axis=1)).tolist())
        U=int(np.sum(arrows(a[0]).max(1)<0));S=int(np.sum(arrows(a[1]).max(1)<0))
        return a,bars,S,U
    for trial in range(tries):
        if trial==0:z=np.zeros(8)
        elif trial%4==0:z=bestz+rng.normal(size=8)*.015
        else:
            size=[.04,.15,.4][trial%3]
            z=np.r_[rng.normal(0,size,5),rng.normal(0,size*.35,3)]
            while (1+X@z[5:]).min()<.15:z[5:]*=.5
        eta=[.01,.001,.0001,.04][trial%4]
        res=minimize(lambda v:loss(v,eta),z,jac=True,method='L-BFGS-B',bounds=[(-1.,1.)]*5+[(-.65,.65)]*3,
                     options={'maxiter':260,'maxls':30,'gtol':1e-10,'ftol':1e-13})
        try:
            data,bars,S,U=inspect(res.x)
            score=float(sum(np.log1p(np.array(v)/.001).sum() for v in bars)*.001)
            row=dict(trial=trial,eta=eta,S=S,U=U,E=c.meta['E'],score=score,
                     Pmax=max(bars[0],default=0),Qmax=max(bars[1],default=0),P=bars[0],Q=bars[1],
                     optimizer_success=bool(res.success),seconds=time.time()-start)
            if score<best:
                best=score;bestz=res.x.copy()
                np.savez(out/'best.npz',parameters=res.x,X=data[2],Q=data[3],A=data[4],b=data[5],g=data[6],volume=data[7])
                (out/'best.json').write_text(json.dumps(row,indent=2))
            if S==U==1:
                np.savez(out/'POTENTIAL_OWN110.npz',parameters=res.x,X=data[2],Q=data[3],A=data[4],b=data[5],g=data[6],volume=data[7])
                (out/'POTENTIAL_OWN110.json').write_text(json.dumps(row,indent=2));return
        except (ValueError,RuntimeError,AssertionError,np.linalg.LinAlgError) as error:
            row=dict(trial=trial,error=repr(error))
        history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2))
        print('PHYSICAL_PROJECTIVE',json.dumps({k:v for k,v in row.items() if k not in ('P','Q')}),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',required=True);p.add_argument('--input',required=True)
    p.add_argument('--out',required=True);p.add_argument('--tries',type=int,default=48);a=p.parse_args()
    run(a.source,a.input,a.out,a.tries)
