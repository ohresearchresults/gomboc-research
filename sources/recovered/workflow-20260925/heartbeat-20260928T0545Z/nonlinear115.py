"""Actual-hull nonlinear continuation with rooted polar guards and sqrt-bar loss.
All radial bars above the explicitly reported numerical floor are penalized.
No claim of exact equilibrium classification is made by this optimizer.
"""
import os
os.environ.setdefault('OMP_NUM_THREADS','1');os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import numpy as np,torch,json,sys,time
from scipy.optimize import minimize
from geometry115 import read_h,geometry,bars
from flow115 import properties,diagnostics
from pathlib import Path
torch.set_default_dtype(torch.float64);torch.set_num_threads(1)
class Objective:
    def __init__(self,base,output,power=.5,margin=1e-7):
        self.base=base;self.output=Path(output);self.power=power;self.margin=margin;self.last=None;self.best=1e9;self.trace=[];self.calls=0
    def run(self,x):
        if self.last is not None and np.array_equal(x,self.last[0]):return self.last[1:]
        self.calls+=1;n=x.reshape(self.base.shape);m=geometry(n)
        pn=m['p'];P=bars(pn,m['edges']);P=[a for a in P if a[0]>1e-12]
        idx=np.array([i for i in range(len(n)) if i!=15]);q=m['q'];A=q@q.T-np.sum(q*q,axis=1)[:,None];np.fill_diagonal(A,-np.inf);wi=np.argmax(A,axis=1)[idx]
        def f(flat):
            p,q,g=properties(flat.reshape(n.shape),m)
            loss=torch.zeros(())
            for _,bi,(a,b),_,_ in P:
                d=p[b]-p[a];t=torch.clamp(-(p[a]@d)/(d@d),0,1);u=p[a]+t*d
                dep=torch.clamp(1-(u@u)/(p[bi]@p[bi]),min=0)
                loss=loss+((dep+1e-16)**self.power-(1e-16)**self.power)
            val=(q[idx]*(q[wi]-q[idx])).sum(dim=1)/(q[idx]*q[idx]).sum(dim=1)
            return torch.cat((loss.reshape(1),val))
        xx=torch.tensor(x);v=f(xx).detach().numpy();J=torch.func.jacrev(f)(xx).detach().numpy()
        if v[1:].min()>self.margin*.99 and v[0]<self.best:
            self.best=float(v[0]);_,c=diagnostics(n)
            rec=dict(call=self.calls,loss=self.best,P=c['P'],Q=c['Q'],S=c['S'],U=c['U'],E=c['E'],F=c['F'],minQ=c['minQ'],minP=c['minP'])
            self.trace.append(rec);self.output.write_text(json.dumps(dict(normals=n.tolist(),trace=self.trace,power=self.power,margin=self.margin),indent=2)+'\n')
            if len(self.trace)%10==0:print(rec,flush=True)
        self.last=(x.copy(),v,J);return v,J

def run(inp,out,iterations=100,power=.5,margin=1e-7,width=.25):
    n=np.array(json.loads(Path(inp).read_text())['normals']);o=Objective(n,out,power,margin)
    scale=np.repeat(np.linalg.norm(n,axis=1),3);x0=n.flatten()
    fun=lambda x:o.run(x)[0][0];jac=lambda x:o.run(x)[1][0]
    cons=dict(type='ineq',fun=lambda x:o.run(x)[0][1:]-margin,jac=lambda x:o.run(x)[1][1:])
    res=minimize(fun,x0,jac=jac,constraints=[cons],method='SLSQP',bounds=list(zip(x0-width*scale,x0+width*scale)),options=dict(maxiter=iterations,ftol=1e-11,disp=True))
    report=dict(success=bool(res.success),message=str(res.message),iterations=int(res.nit),evaluations=o.calls,objective=float(res.fun),best=o.best,last_normals=res.x.reshape(n.shape).tolist(),parameters=dict(power=power,margin=margin,width=width,iterations=iterations,bar_cutoff=1e-12,sqrt_regularizer=1e-16))
    Path(str(out)+'.run.json').write_text(json.dumps(report,indent=2)+'\n');print(report['message'],'best',o.best,'nfev',o.calls,flush=True)
if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 100,float(sys.argv[4]) if len(sys.argv)>4 else .5,float(sys.argv[5]) if len(sys.argv)>5 else 1e-7,float(sys.argv[6]) if len(sys.argv)>6 else .25)
