# material-0373c3595b1a

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J115 executed negative controls — complete additional sources

Requires the complete core [internal-source-reference], including J114B_G5.txt, geometry115.py, flow115.py and its versions. Save the two complete blocks with final newlines; their executed byte identities are stated below. These are finite numerical experiments, never general impossibility or exact absence certificates.

Commands: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python scout115.py`; first run the core's FLOW115.json generation in a fresh directory, then `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python nonlinear115.py FLOW115.json SQRT115.json 100 .5 1e-7 .25`.

Scout: junior high-superlevel component has43 vertices at death squared radius.558537847083172 (radius.7473538968140676). Forty-six physical vertices admit the nominated direct-root diameter-ball cut, but19 junior-component vertices do not. Simultaneously imposing all46 nominated cuts yields F103/E303, actual S48/U27 and centroid(.0418024,.0497910,.0036150) in the old-centred coordinate frame, volume1.07904645. This exceeds the target budget and creates many actual equilibria; it is not an exact general cut exclusion. SCOUT115.json contains all literal candidate normals, component/valid lists and actual numerical full-census data.

Nonlinear SLSQP control: actual-hull sqrt-P loss with all nonroot polar witnesses constrained at normalized margin1e-7, fixed root input15, relative normal bounds.25, maxiter100, ftol1e-11, power.5, regularizer1e-16. It ended after63 iterations/434 evaluations with 'Positive directional derivative for linesearch' (exit8), without any saved feasible best at that target margin. SQRT115.json was absent; SQRT115.json.run.json contains actual last normals and parameters. Last hull has S5/U4, main P~.4222528568 plus additional positive bars; these births are not rounded away. This is a bounded-policy failure, not exclusion of free-normal or nonsmooth whole-landscape descent. The source makes its1e-12 nomination floor explicit; use the exact auditor for any final rational body.

## FILE scout115.py — 1577 bytes; SHA256 f9905d7b4ab6517aaac3d2e9f1465f533aa72a1de404dc28e4275d1529b1e4ea
```python
"""Finite one-step polar cut availability scout on literal J114B_G5."""
import numpy as np,json
from geometry115 import *
from pathlib import Path
m=geometry(read_h(Path(__file__).with_name('J114B_G5.txt')))
p=m['p']; c=census(m); r=m['q'][15]; oldq=m['q']; U=c['U']; junior=c['P'][0][1];level=c['P'][0][4]
ed=m['edges'];a=p[ed[:,0]];d=p[ed[:,1]]-a;t=np.clip(-np.sum(a*d,axis=1)/np.sum(d*d,axis=1),0,1);lev=np.sum((a+t[:,None]*d)**2,axis=1)
nei={i:[] for i in range(len(p))}
for (i,j),h in zip(ed,lev):
    if h>level+1e-12:nei[i].append(j);nei[j].append(i)
comp={junior};todo=[junior]
while todo:
    i=todo.pop()
    for j in nei[i]:
        if j not in comp:comp.add(j);todo.append(j)
qs=r[None,:]/2+np.linalg.norm(r)/2*p/np.linalg.norm(p,axis=1)[:,None]
qs*=.999
support=np.einsum('ij,ij->i',qs,p)
print('junior component',len(comp),'vertices',sorted(comp));print('root length',np.linalg.norm(r),'S height',1/np.linalg.norm(r),'deathradius',level**.5)
print('component max allowed cut supports',[(i,float(support[i]),float(np.linalg.norm(p[i]))) for i in sorted(comp)])
valid=np.where(support>1+1e-8)[0];print('valid',len(valid),'comp invalid',comp-set(valid))
allm=geometry(np.r_[oldq,qs[valid]])
print('max-discrete',json.dumps({k:v for k,v in census(allm).items() if not k.endswith('scores')}))
Path(__file__).with_name('SCOUT115.json').write_text(json.dumps(dict(comp=sorted(map(int,comp)),valid=valid.tolist(),candidate_q=qs[valid].tolist(),parent_centroid=m['g'].tolist(),core_census={k:v for k,v in census(allm).items() if not k.endswith('scores')}),indent=2)+'\n')
```

## FILE nonlinear115.py — 3536 bytes; SHA256 71a62e9c4c0fe9f77777f721a6cc87a8af7bea83d44d7dfb6ff929b12d735edf
```python
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
```
