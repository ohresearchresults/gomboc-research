# material-5cda590fc68f

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# BRIDGE79 recovery capsule part 3/3 — finite numerical methods and literal checkpoints

## Dependencies and evidence scope
Part1 [internal-source-reference] supplies the complete input.json. This part supplies all producing methods and literal optimizer endpoints for the OLD-reference bridge screen, six-point physical continuation and deletion experiments. Part2 [internal-source-reference] supplies the separate rigorous exactly-centred old-reference result. All three together form the complete original BRIDGE79 capsule. Later new-reference-chamber findings use additional separately named source materials; they are not silently substituted here.

The four ordered-witness eight-dimensional runs, three direct log-bar runs,200 specified reference-chamber LP probes, two65-step greedy deletion paths and three26-variable live six-point/metric/projective runs did not produce own110. These are finite searches, not orbit or architecture exclusions. Two fixed-root LP witness selections do NOT examine every possible stable carrier. Floating bar reports suppress relative depths<=1e-13; some new tiny equilibria remain in raw counts even when omitted from that diagnostic list. Therefore a small loss or a discrepancy between raw counts and bar-list cardinalities is not certification. The near-flat numerical222 endpoint has deep P/Q .9997365532636528/.9967723598043822 and is not improvement. The three free-six-point endpoints are numerical5/5/8,6/6/10,3/5/6, with major paired depths(.14981528020081597,.5918055700692122),(.43625205557710955,.7467041926136075),(.5772131433672684,.7024910316076672). No exact class is claimed for these floating endpoints. Part1 independently converts the selected16/46-row deletion controls into exact weak-free bodies.

The actual environment was CPython3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, OPENBLAS_NUM_THREADS=1, torch float64 and one thread. Commands for the finite producing runs:
```
python -B repair.py
python -B orbit_search.py 0 4 600
python -B bar_search.py 0 3 400 1.0
python -B reference_cells.py
python -B deletion.py count
python -B deletion.py joint
python -B free_bridge.py 0 3 300 0.5
python -B replay_checkpoints.py
```
All nondefault bounds, seeds, cutoffs, iteration limits and optimizer settings are in the complete sources below. Exact input rows are in part1. Each deletion path evaluated2795 candidates and retains all six bridge points. The literal removal orders and final best input subsets are included in the checkpoint file. Full optimization logs contain wall-clock times and are not promised bitwise reproducible. Literal endpoint replay avoids optimizer variability and produces replayed_numeric.json21071 bytes, SHA-256 c0bf868670d5284f7caa5399e525f8fb1563ec2a3bce5096f7b7ee6399783d46 in the stated environment. Terminal markers are NUMERIC_CHECKPOINT_REPLAY_PASS and FLOAT_COUNTS_ARE_NOT_EXACT_CERTIFICATES. Other architectures/BLAS versions may perturb fragile floating signs; the rational certificates in part1 do not have that limitation.

Source manifests:
repair.py6017B SHA e32068769b73ef7b4fa1c19230d0eeac0bfd3beea142a2273ee2333667544afc;
orbit_search.py4274B SHA ed9bce7a88ad81d11a70056e9d9dd3c0b4006eb026f1d77d7ffdcd7ae4e35522;
bar_search.py3288B SHA d21c5fc302d7e5d012ed6bfb443432177292a7c0c018a118b84391ead007f0a7;
reference_cells.py3368B SHA bbfc7e0185fa605da523f7b098029d002b0f583b52c6631ef7bb9590176b275d;
deletion.py2065B SHA a72cca2125e9d73faf1c864bd403e7bb79b983dfa69413a341a2b6fa6bee9620;
free_bridge.py3944B SHA2973ed83c306114f15f3057c672117e74308ab6ca95290059f47afa59ff57cf8;
numeric_checkpoints.json7027B SHA e4f3d3db2c361489851432edeb6e70ea7aaeb81d3239056bc276d54d32e14617;
replay_checkpoints.py1258B SHA4729263a23199518d2bb6985057a8e6ad75530cc5925aa12ae277c7873d668c0.

## File: repair.py
```python
"""Finite projective physical-mass repair screen. Numeric, not exact certification."""
import json,sys,platform,hashlib
from pathlib import Path
import numpy as np
import scipy
from scipy.spatial import ConvexHull

ROOT=Path(__file__).resolve().parent

def hull(X):
    h=ConvexHull(X)
    tri=h.simplices.copy()
    a,b,c=X[tri[:,0]],X[tri[:,1]],X[tri[:,2]]
    flip=np.einsum('ij,ij->i',np.cross(b-a,c-a),h.equations[:,:3])<0
    tri[flip]=tri[flip][:,[0,2,1]]
    return h,tri

def mass(X,tri=None):
    if tri is None:_,tri=hull(X)
    # Use an interior origin; positive tetrahedra, not cancellation of signed mass.
    origin=X.mean(axis=0)
    v=X[tri]-origin
    w=np.einsum('ij,ij->i',v[:,0],np.cross(v[:,1],v[:,2]))/6
    if min(w)<=0: raise ValueError('bad tetrahedron orientation')
    V=w.sum(); s=v.sum(axis=1)
    g=np.einsum('i,ij->j',w,s)/(4*V)
    raw2=np.einsum('i,ijk,ijl->kl',w,v,v)+np.einsum('i,ij,ik->jk',w,s,s)
    covariance=raw2/(20*V)-np.outer(g,g)
    return float(V),origin+g,covariance

def centre_projective(X,q,b0=None):
    _,tri=hull(X); L=X-q
    b=np.zeros(3) if b0 is None else np.array(b0,dtype=float)
    history=[]
    for step in range(100):
        den=1+L@b
        if min(den)<=0:raise ValueError('outside positive projective chart')
        Y=L/den[:,None]
        V,g,cov=mass(Y,tri)
        history.append([float(V),float(np.linalg.norm(g)),float(min(den))])
        if np.linalg.norm(g)<2e-13:break
        direction=np.linalg.solve(5*cov+np.outer(g,g),g)
        # d log V = -4 g.dot(direction). Newton+Armijo uses actual volume.
        rate=1.0
        for _ in range(50):
            bt=b+rate*direction;dt=1+L@bt
            if min(dt)>0:
                vn,gn,_=mass(L/dt[:,None],tri)
                if np.log(vn)<=np.log(V)-1e-4*rate*4*g.dot(direction)+1e-15:
                    b=bt;break
            rate*=.5
        else:raise RuntimeError('centering line search failed')
    else: raise RuntimeError('centering did not converge')
    return Y,b,history

def geometry(X,centre=None):
    h,tri=hull(X)
    V,g,cov=mass(X,tri)
    c=g if centre is None else centre
    P=X-c
    # Exact incidence in this numeric chart follows its simplicial hull.
    a,b,d=P[tri[:,0]],P[tri[:,1]],P[tri[:,2]]
    N=np.cross(b-a,d-a); offsets=np.einsum('ij,ij->i',N,a)
    if min(offsets)<=0:raise ValueError('centre not interior')
    Q=N/offsets[:,None]
    ed={}
    for fi,t in enumerate(tri):
        for j in range(3):ed.setdefault(tuple(sorted((int(t[j]),int(t[(j+1)%3])))),[]).append(fi)
    edges=np.array(list(ed),int);owners=np.array(list(ed.values()),int)
    if owners.shape[1]!=2: raise ValueError('not closed manifold')
    # All-vertex inequalities characterize strict unstable vertices without adjacency tolerance.
    rp=(P*P).sum(axis=1);rq=(Q*Q).sum(axis=1)
    pm=P@P.T-rp[:,None];np.fill_diagonal(pm,-np.inf)
    qm=Q@Q.T-rq[:,None];np.fill_diagonal(qm,-np.inf)
    umax=pm.max(axis=1);smax=qm.max(axis=1)
    U=np.where(umax<0)[0]; S=np.where(smax<0)[0]
    # Per edge segment interior and positive conormal coefficients.
    A=P[edges[:,0]];B=P[edges[:,1]];D=B-A
    t=-np.einsum('ij,ij->i',A,D)/np.einsum('ij,ij->i',D,D)
    p=A+t[:,None]*D
    n1=Q[owners[:,0]];n2=Q[owners[:,1]]
    aa=(n1*n1).sum(axis=1);bb=(n1*n2).sum(axis=1);dd=(n2*n2).sum(axis=1)
    y1=(p*n1).sum(axis=1);y2=(p*n2).sum(axis=1)
    det=aa*dd-bb*bb
    # Cross-product formula for determinant avoids cancellation at tiny dihedral angle.
    det=(np.cross(n1,n2)**2).sum(axis=1)
    l1=(dd*y1-bb*y2)/det;l2=(aa*y2-bb*y1)/det
    H=np.where((t>0)&(t<1)&(l1>0)&(l2>0))[0]
    # Counts use raw binary64 signs, zero/tiny screens are NOT weak certification.
    return {'X':X,'P':P,'Q':Q,'tri':tri,'edges':edges,'owners':owners,'g':g,'V':V,
            'cov':cov,'S':S,'U':U,'H':H,'umax':umax,'smax':smax}

def bars(P,edges):
    radius=(P*P).sum(axis=1);a=P[edges[:,0]];d=P[edges[:,1]]-a
    t=np.clip(-(a*d).sum(axis=1)/(d*d).sum(axis=1),0,1)
    gate=((a+t[:,None]*d)**2).sum(axis=1)
    # Forest maximum bottleneck merging; ignore only relative <=1e-13 roundoff for screen.
    parent=np.arange(len(P));root=np.arange(len(P));result=[]
    def find(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]];i=parent[i]
        return i
    for e in np.argsort(-gate,kind='stable'):
        i,j=map(find,edges[e])
        if i==j:continue
        if radius[root[i]]<radius[root[j]]:i,j=j,i
        birth=radius[root[j]];death=gate[e]
        depth=(birth-death)/birth
        if depth>1e-13:result.append((float(depth),int(root[j]),int(root[i]),edges[e].tolist()))
        parent[j]=i
    return sorted(result,reverse=True)

def summary(G):
    p=bars(G['P'],G['edges']);q=bars(G['Q'],G['owners'])
    return {'V':G['V'],'g':G['g'].tolist(),'VEF':[len(np.unique(G['tri'])),len(G['edges']),len(G['tri'])],
            'SUH':[len(G[k]) for k in ('S','U','H')], 'S':[G['tri'][i].tolist() for i in G['S']],
            'U':G['U'].tolist(),'Pbars':p,'Qbars':q,'morse_error':len(G['S'])+len(G['U'])-len(G['H'])-2}

def main():
    data=json.loads((ROOT/'input.json').read_text())
    X=np.array(data['I'])/data['D'];A=np.array(data['A'])/data['AD']
    q=np.array(data['centroid_numerators'],float)/data['centroid_denominator']
    Z=np.vstack([X,A]);report={'environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__}}
    report['primary']=summary(geometry(X));report['bridge_own']=summary(geometry(Z));report['bridge_reference']=summary(geometry(Z,q))
    Y,b,h=centre_projective(Z,q)
    report['bridge_centred']={**summary(geometry(Y)),'pole':b.tolist(),'centering_history':h}
    (ROOT/'baseline.json').write_text(json.dumps(report,indent=2)+'\n')
    np.save(ROOT/'centred_bridge.npy',Y)
    print(json.dumps({k:{j:v for j,v in d.items() if j not in ('Pbars','Qbars','centering_history','S')} for k,d in report.items()},indent=2))
    print('BRIDGE_PROJECTIVE_NUMERIC_SCREEN_NO_CERTIFICATION')
if __name__=='__main__':main()
```

## File: orbit_search.py
```python
"""Autodifferentiated finite projective/metric bridge search; numeric screen only."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import json,sys,time
import numpy as np
import torch
from scipy.optimize import minimize
from repair import ROOT,hull,geometry,summary

torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)

def source(which='bridge'):
    dat=json.loads((ROOT/'input.json').read_text());X=np.array(dat['I'])/dat['D']
    if which=='bridge':X=np.vstack([X,np.array(dat['A'])/dat['AD']])
    q=np.array(dat['centroid_numerators'],float)/dat['centroid_denominator']
    H,_=hull(X);X=X[H.vertices]-q
    H,tri=hull(X)
    V=X[tri];w=np.einsum('ij,ij->i',V[:,0],np.cross(V[:,1],V[:,2]))/6
    N=np.cross(V[:,1]-V[:,0],V[:,2]-V[:,0]);Q=N/np.einsum('ij,ij->i',N,V[:,0])[:,None]
    assert min(w)>0
    return X,tri,w,Q

class Model:
    def __init__(self,which='bridge'):
        X,t,w,Q=source(which);self.X=torch.tensor(X);self.t=torch.tensor(t)
        self.w=torch.tensor(w);self.Q=torch.tensor(Q);self.evals=0
    def transform(self,z):
        b=z[5:];den=1+self.X@b
        Y=self.X/den[:,None]
        weight=self.w/torch.prod(den[self.t],dim=1)
        g=torch.sum(weight[:,None]*Y[self.t].sum(dim=1),dim=0)/(4*weight.sum())
        P=Y-g
        Q=self.Q+b
        Q=Q/(1-Q@g)[:,None]
        zero=z[0]*0
        A=torch.stack([torch.stack([torch.exp(z[0]),zero,zero]),
          torch.stack([z[2],torch.exp(z[1]),zero]),torch.stack([z[3],z[4],torch.exp(-z[0]-z[1])])])
        return P@A.T,Q@torch.linalg.inv(A),den,g,A
    @staticmethod
    def deficits(V):
        r=(V*V).sum(dim=1)
        M=(V@V.T-r[:,None])/r[:,None]
        # Equal-radius ties broken by row index. Positive witness still increases radius.
        order=torch.argsort(r.detach(),stable=True);rank=torch.argsort(order)
        later=rank[None,:]>rank[:,None]
        M=M.masked_fill(~later,-1e6)
        esc=M.max(dim=1).values[order[:-1]]
        return torch.relu(1e-5-esc)
    def fun(self,p):
        self.evals+=1
        z=torch.tensor(p,requires_grad=True)
        den=1+self.X@z[5:]
        if float(den.detach().min())<.06:
            loss=1e3+1e4*torch.relu(.06-den).square().sum()
        else:
            P,Q,_,_,A=self.transform(z)
            dp=self.deficits(P);dq=self.deficits(Q)
            loss=dp.square().sum()+dq.square().sum()
        loss.backward()
        return float(loss.detach()),z.grad.detach().numpy()
    def report(self,p):
        with torch.no_grad():P,Q,den,g,A=self.transform(torch.tensor(p));dp=self.deficits(P);dq=self.deficits(Q)
        G=geometry(P.numpy());s=summary(G)
        return {'p':list(map(float,p)),'loss':float(dp.square().sum()+dq.square().sum()),
            'ordered_max_deficits':[float(dp.max()),float(dq.max())],
            'min_denominator':float(den.min()),'metric_eigenvalues':np.linalg.eigvalsh(A.numpy().T@A.numpy()).tolist(),
            'geometry':s}

def main():
    first=int(sys.argv[1]) if len(sys.argv)>1 else 0
    count=int(sys.argv[2]) if len(sys.argv)>2 else 4
    its=int(sys.argv[3]) if len(sys.argv)>3 else 600
    model=Model('bridge');baseline=json.loads((ROOT/'baseline.json').read_text());bc=baseline['bridge_centred']['pole']
    rng=np.random.default_rng(25625)
    starts=[np.r_[np.zeros(5),bc],np.zeros(8)]
    for i in range(30):starts.append(np.r_[rng.normal(0,.3,5),np.array(bc)+rng.normal(0,.13,3)])
    results=[]
    for j in range(first,first+count):
        p=starts[j];st=time.monotonic();model.evals=0
        r=minimize(model.fun,p,jac=True,method='L-BFGS-B',bounds=[(-1.8,1.8)]*2+[(-2.5,2.5)]*3+[(-.8,.8)]*3,
                   options={'maxiter':its,'maxfun':20000,'ftol':1e-14,'gtol':1e-9,'maxls':40,'maxcor':15})
        rec=model.report(r.x);rec.update({'start_index':j,'start':p.tolist(),'iterations':int(r.nit),'evals':model.evals,
            'optimizer_success':bool(r.success),'message':str(r.message),'seconds':time.monotonic()-st})
        results.append(rec)
        (ROOT/f'orbit_{first}_{count}.json').write_text(json.dumps(results,indent=2)+'\n')
        print(j,rec['geometry']['SUH'],rec['loss'],rec['ordered_max_deficits'],rec['iterations'],flush=True)
    print('FINITE_BRIDGE_ORBIT_SCREEN_NO_OWN110_CERTIFICATE')
if __name__=='__main__':main()
```

## File: bar_search.py
```python
"""Direct paired persistence in a fixed-incidence finite projective chart."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import json,sys,time
import numpy as np
import torch
from scipy.optimize import minimize
from orbit_search import Model,source
from repair import ROOT

class BarModel(Model):
    def __init__(self,power=1.):
        super().__init__('bridge');self.power=power
        t=self.t.numpy();edge={}
        for i,f in enumerate(t):
            for j in range(3):edge.setdefault(tuple(sorted((int(f[j]),int(f[(j+1)%3])))),[]).append(i)
        self.ep=torch.tensor(list(edge));self.eq=torch.tensor(list(edge.values()))
    def energy(self,P,E):
        r=(P*P).sum(dim=1);a=P[E[:,0]];d=P[E[:,1]]-a
        t=torch.clamp(-(a*d).sum(dim=1)/(d*d).sum(dim=1),0,1)
        gate=((a+t[:,None]*d)**2).sum(dim=1)
        rn=r.detach().numpy();gn=gate.detach().numpy();en=E.numpy()
        par=list(range(len(P)));root=list(range(len(P)));bi=[];gi=[]
        def find(i):
            while par[i]!=i:par[i]=par[par[i]];i=par[i]
            return i
        for ei in np.argsort(-gn,kind='stable'):
            i,j=map(find,en[ei])
            if i==j:continue
            if rn[root[i]]<rn[root[j]]:i,j=j,i
            if rn[root[j]]-gn[ei]>1e-13*rn[root[j]]:
                bi.append(root[j]);gi.append(ei)
            par[j]=i
        if not bi:return P.sum()*0
        z=torch.log(r[bi]/gate[gi])
        return z.pow(self.power).sum()
    def fun(self,p):
        self.evals+=1
        z=torch.tensor(p,requires_grad=True);den=1+self.X@z[5:]
        if float(den.detach().min())<.06:
            loss=1e3+1e4*torch.relu(.06-den).square().sum()
        else:
            P,Q,_,_,_=self.transform(z)
            loss=self.energy(P,self.ep)+self.energy(Q,self.eq)
        loss.backward();return float(loss.detach()),z.grad.detach().numpy()

def main():
    first=int(sys.argv[1]) if len(sys.argv)>1 else 0
    count=int(sys.argv[2]) if len(sys.argv)>2 else 3
    its=int(sys.argv[3]) if len(sys.argv)>3 else 400
    power=float(sys.argv[4]) if len(sys.argv)>4 else 1.
    model=BarModel(power);bc=json.loads((ROOT/'baseline.json').read_text())['bridge_centred']['pole']
    rng=np.random.default_rng(25627)
    starts=[np.r_[np.zeros(5),bc],np.zeros(8)]
    for i in range(20):starts.append(np.r_[rng.normal(0,.2,5),np.array(bc)+rng.normal(0,.12,3)])
    out=[]
    for j in range(first,first+count):
        p=starts[j];st=time.monotonic();model.evals=0
        r=minimize(model.fun,p,jac=True,method='L-BFGS-B',bounds=[(-1.8,1.8)]*2+[(-2.5,2.5)]*3+[(-.8,.8)]*3,
            options={'maxiter':its,'maxfun':20000,'ftol':1e-14,'gtol':1e-9,'maxls':40,'maxcor':15})
        rec=model.report(r.x);rec.update({'start_index':j,'power':power,'start':p.tolist(),'bar_objective':float(r.fun),
            'iterations':int(r.nit),'evals':model.evals,'optimizer_success':bool(r.success),'message':str(r.message),'seconds':time.monotonic()-st})
        out.append(rec)
        (ROOT/f'bars_{power}_{first}_{count}.json').write_text(json.dumps(out,indent=2)+'\n')
        g=rec['geometry'];print('BARS',power,j,g['SUH'],r.fun,[sum(x[0] for x in g[z]) for z in ['Pbars','Qbars']],r.nit,flush=True)
    print('FINITE_BAR_ORBIT_SCREEN_NO_OWN110_CERTIFICATE')
if __name__=='__main__':main()
```

## File: reference_cells.py
```python
"""Linear physical-reference chamber probes; not homogeneous-own solutions."""
import json,itertools
import numpy as np
from scipy.optimize import linprog
from repair import ROOT,hull,geometry,summary,centre_projective
from orbit_search import source

def forms(X):
    h,t=hull(X);Ns=h.equations[:,:3];offs=-h.equations[:,3]
    edge=set()
    for f in t:
        for k in range(3):edge.add(tuple(sorted((int(f[k]),int(f[(k+1)%3])))))
    adj=[[] for _ in X]
    for i,j in edge:adj[i].append(j);adj[j].append(i)
    uv=[];sf=[]
    for i,js in enumerate(adj):
        js=sorted(js);v=X[js]-X[i];v/=np.linalg.norm(v,axis=1)[:,None]
        uv.append((-v,(v*X[i]).sum(axis=1))) # all <0 is U; one >0 escape
    for fi,f in enumerate(t):
        vs=X[np.roll(f,-1)]-X[f];vs/=np.linalg.norm(vs,axis=1)[:,None]
        inside=np.cross(Ns[fi],vs)
        sf.append((-inside,(inside*X[f]).sum(axis=1))) # one >0 is not S
    return h,t,uv,sf

def probe(X,q0,rounds=100):
    h,t,uv,sf=forms(X);init=geometry(X,q0);stable=init['S'];unstable=init['U']
    rng=np.random.default_rng(25626);best=[]
    for ru in unstable:
      for rs in stable:
        for trial in range(rounds):
            # Explore guards with near-best alternatives; targeted stable must leave.
            rows=[];const=[]
            for feature,rt in [(uv,ru),(sf,rs)]:
                for i,(M,c) in enumerate(feature):
                    if i==rt:rows.extend(-M);const.extend(-c)
                    else:
                        vals=M@q0+c
                        if trial:
                            score=vals+rng.gumbel(size=len(vals))*.02
                            k=score.argmax()
                        else:k=vals.argmax()
                        rows.append(M[k]);const.append(c[k])
            rows=np.array(rows);const=np.array(const)
            # rows q + const >= eta, unit normalized geometric constraints.
            AU=np.c_[-rows,np.ones(len(rows))];bu=const
            AU=np.vstack([AU,np.c_[h.equations[:,:3],np.zeros(len(t))]])
            bu=np.r_[bu,-h.equations[:,3]-1e-5]
            bounds=[(None,None)]*3+[(0,.2)]
            lp=linprog([0,0,0,-1],A_ub=AU,b_ub=bu,bounds=bounds,method='highs')
            if lp.success and lp.x[3]>1e-10:
                q=lp.x[:3];G=geometry(X,q)
                rec={'rootU':int(ru),'rootS_triangle':t[rs].tolist(),'trial':trial,'margin':float(lp.x[3]),'q':q.tolist(),'reference':summary(G)}
                Y,b,history=centre_projective(X,q)
                rec['own_projective']=summary(geometry(Y));rec['pole']=b.tolist();rec['history']=history
                best.append(rec)
                print('CELL',ru,int(rs),trial,lp.x[3],rec['reference']['SUH'],rec['own_projective']['SUH'],flush=True)
                if len(best)>=10:return best
    return best

def main():
    dat=json.loads((ROOT/'input.json').read_text());X=np.array(dat['I'])/dat['D'];X=np.vstack([X,np.array(dat['A'])/dat['AD']])
    # Keep original material labels (includes interior points which are omitted by geometry roots).
    h,_=hull(X);X=X[h.vertices]
    q=np.array(dat['centroid_numerators'],float)/dat['centroid_denominator']
    report=probe(X,q,100)
    (ROOT/'reference_cells.json').write_text(json.dumps(report,indent=2)+'\n')
    print('FINITE_REFERENCE_CHAMBER_PROBE',len(report),'NO_OWN110_CERTIFICATE')
if __name__=='__main__':main()
```

## File: deletion.py
```python
"""Finite deletion-only mass replacement while retaining the six literal bridge points."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import json,sys,time
import numpy as np
from repair import ROOT,geometry,summary

def energy(s,mode):
    e=[sum(np.sqrt(-np.log1p(-min(t[0],1-1e-15))) for t in s[z]) for z in ('Pbars','Qbars')]
    if mode=='count':return (sum(s['SUH'][:2]),sum(e),max(e))
    if mode=='joint':return (sum(e),max(e),sum(s['SUH'][:2]))
    if mode=='max':return (max(e),sum(e),sum(s['SUH'][:2]))
    raise ValueError(mode)

def main():
    mode=sys.argv[1] if len(sys.argv)>1 else 'count'
    data=json.loads((ROOT/'input.json').read_text());X=np.vstack([np.array(data['I'])/data['D'],np.array(data['A'])/data['AD']])
    ids=list(range(len(X)));s=summary(geometry(X));history=[{'remove':None,'ids':ids.copy(),'geometry':s,'energy':energy(s,mode)}]
    evaluated=0
    for step in range(65):
        best=None
        for k in ids:
            if k>=75:continue
            trial=[j for j in ids if j!=k]
            try:s=summary(geometry(X[trial]))
            except Exception:continue
            if s['VEF'][0]<10:continue
            evaluated+=1;e=energy(s,mode)
            if best is None or e<best['energy']:best={'remove':k,'ids':trial,'geometry':s,'energy':e}
        if best is None:break
        ids=best['ids'];history.append(best)
        if step%5==0:print(mode,step,best['remove'],best['geometry']['VEF'],best['geometry']['SUH'],best['energy'],flush=True)
        if best['geometry']['SUH']==[1,1,0]:print('FLOAT_TARGET_REQUIRES_EXACT_AUDIT',flush=True);break
    report={'mode':mode,'minimum_extreme_vertices':10,'all_six_bridge_points_retained':True,'evaluated':evaluated,'history':history}
    (ROOT/f'deletion_{mode}.json').write_text(json.dumps(report,indent=2)+'\n')
    best=min(history,key=lambda r:r['energy'])
    print('BEST',mode,len(best['ids']),best['geometry']['VEF'],best['geometry']['SUH'],best['energy'],best['ids'])
    print('FINITE_DELETION_SCREEN_NO_EXACT_TARGET_CLAIM')
if __name__=='__main__':main()
```

## File: free_bridge.py
```python
"""Live-hull six-point physical bridge plus projective/metric deformation.
No existing primary material row is independently moved. All mass is uniform.
Numeric finite screen; changes of hull, roots, and current bar pairing are live.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import json,sys,time
import numpy as np
import torch
from scipy.optimize import minimize
from repair import ROOT,hull,geometry,summary
from bar_search import BarModel

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
class FreeBridge:
    def __init__(self,power=.5):
        d=json.loads((ROOT/'input.json').read_text());self.q=np.array(d['centroid_numerators'],float)/d['centroid_denominator']
        self.host=torch.tensor(np.array(d['I'])/d['D']-self.q);self.bridge=torch.tensor(np.array(d['A'])/d['AD']-self.q)
        self.power=power;self.evals=0;self.bad=0
    def transform(self,z):
        X=torch.cat([self.host,self.bridge+z[8:].reshape(6,3)])
        hn,tn=hull(X.detach().numpy());t=torch.tensor(tn)
        den=1+X@z[5:8];Y=X/den[:,None];v=Y[t]
        w=torch.sum(v[:,0]*torch.linalg.cross(v[:,1],v[:,2]),dim=1)/6
        g=torch.sum(w[:,None]*v.sum(dim=1),dim=0)/(4*w.sum());P=Y-g
        v=P[t];n=torch.linalg.cross(v[:,1]-v[:,0],v[:,2]-v[:,0]);Q=n/(n*v[:,0]).sum(dim=1)[:,None]
        ed={}
        for i,f in enumerate(tn):
            for j in range(3):ed.setdefault(tuple(sorted((int(f[j]),int(f[(j+1)%3])))),[]).append(i)
        ep=torch.tensor(list(ed));eq=torch.tensor(list(ed.values()))
        zero=z[0]*0
        A=torch.stack([torch.stack([torch.exp(z[0]),zero,zero]),torch.stack([z[2],torch.exp(z[1]),zero]),torch.stack([z[3],z[4],torch.exp(-z[0]-z[1])])])
        return P@A.T,Q@torch.linalg.inv(A),ep,eq,den
    def fun(self,p):
        self.evals+=1;z=torch.tensor(p,requires_grad=True)
        X=torch.cat([self.host,self.bridge+z[8:].reshape(6,3)]);den=1+X@z[5:8]
        if float(den.detach().min())<.06:
            loss=1000+10000*torch.relu(.06-den).square().sum()
        else:
            P,Q,ep,eq,_=self.transform(z)
            # Use only extreme primal rows in persistence implicitly via true edges;
            # interior rows have no edges, hence never produce finite bars.
            loss=BarModel.energy(self,P,ep)+BarModel.energy(self,Q,eq)
        loss.backward();return float(loss.detach()),z.grad.detach().numpy()
    def report(self,p):
        with torch.no_grad():P,Q,ep,eq,den=self.transform(torch.tensor(p))
        return {'parameters':list(map(float,p)),'geometry':summary(geometry(P.numpy())), 'min_denominator':float(den.min())}

def main():
    first=int(sys.argv[1]) if len(sys.argv)>1 else 0;count=int(sys.argv[2]) if len(sys.argv)>2 else 3
    its=int(sys.argv[3]) if len(sys.argv)>3 else 300;power=float(sys.argv[4]) if len(sys.argv)>4 else .5
    m=FreeBridge(power);bc=json.loads((ROOT/'baseline.json').read_text())['bridge_centred']['pole']
    starts=[np.r_[np.zeros(5),bc,np.zeros(18)],np.zeros(26)]
    bars=json.loads((ROOT/'bars_1.0_0_3.json').read_text());starts.extend(np.r_[r['p'],np.zeros(18)] for r in bars)
    out=[]
    for i in range(first,first+count):
        m.evals=0;st=time.monotonic();p=starts[i]
        r=minimize(m.fun,p,jac=True,method='L-BFGS-B',bounds=[(-1.8,1.8)]*2+[(-2.5,2.5)]*3+[(-.8,.8)]*3+[(-.4,.4)]*18,options={'maxiter':its,'maxfun':10000,'ftol':1e-13,'gtol':1e-8,'maxls':30,'maxcor':15})
        rec=m.report(r.x);rec.update({'start_index':i,'start':p.tolist(),'power':power,'objective':float(r.fun),'iterations':int(r.nit),'evals':m.evals,'success':bool(r.success),'message':str(r.message),'seconds':time.monotonic()-st})
        out.append(rec);(ROOT/f'free_bridge_{power}_{first}_{count}.json').write_text(json.dumps(out,indent=2)+'\n')
        print('FREE_BRIDGE',i,rec['geometry']['VEF'],rec['geometry']['SUH'],r.fun,r.nit,flush=True)
    print('FINITE_FREE_BRIDGE_SCREEN_NO_OWN110_CERTIFICATE')
if __name__=='__main__':main()
```

## File: numeric_checkpoints.json
```json
{"bars":[{"SUH":[23,29,50],"VEF":[79,231,154],"bar_counts_over_reporting_floor":[28,22],"evals":29,"iterations":25,"maximum_bar_depth":[0.04312723200474101,0.4242247286887407],"p":[0.07265790298530099,-0.18381340310657918,0.025966849157599774,-0.11133018799985757,-0.07521623198784472,0.10310989649748284,-0.2817555216052826,0.1066914755970532],"start":[0.0,0.0,0.0,0.0,0.0,0.051628708615618996,-0.27358063922348047,0.008862211184347577],"start_index":0},{"SUH":[17,33,48],"VEF":[79,231,154],"bar_counts_over_reporting_floor":[32,16],"evals":34,"iterations":27,"maximum_bar_depth":[0.040944956790298546,0.389580243744481],"p":[0.06649430352254257,-0.21296184688968706,-0.10600416912166861,-0.13060622614098216,0.00011237737366934027,0.29077292833719076,-0.4445267274481288,-0.10124012701024084],"start":[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],"start_index":1},{"SUH":[17,21,36],"VEF":[79,231,154],"bar_counts_over_reporting_floor":[20,16],"evals":57,"iterations":33,"maximum_bar_depth":[0.1743834410161332,0.4919526002776551],"p":[0.0560843251738085,-0.08205835074265742,-0.12129008187757315,-0.14689186491305573,-0.15145892375335182,0.5384991398086045,-0.8,0.40916758777230317],"start":[-0.02154804304890045,-0.10734604881985695,-0.15478512744352174,0.317844265641388,0.0747343179973473,0.10761997571789854,-0.3803224177352095,0.18218095170359636],"start_index":2}],"deletion":{"count":{"best_SUH":[4,8,10],"best_VEF":[16,42,28],"best_energy":[12,2.962112426147031,1.7442139352753152],"best_retained_input_ids":[6,14,15,20,23,31,38,49,51,61,75,76,77,78,79,80],"evaluated":2795,"removal_order":[65,22,70,73,0,11,41,37,44,5,74,3,34,30,26,55,72,58,62,13,63,19,48,28,27,40,42,43,57,60,59,33,39,32,64,46,24,52,25,8,9,2,7,71,17,69,67,1,47,68,10,50,12,16,56,53,36,21,35,54,45,18,4,29,66]},"joint":{"best_SUH":[15,30,43],"best_VEF":[46,132,88],"best_energy":[3.4831504046068575,1.8978003739097475,45],"best_retained_input_ids":[0,1,2,3,6,7,8,9,10,13,14,15,16,20,22,23,24,25,26,29,30,31,34,37,41,44,47,48,50,51,52,53,55,56,60,65,66,67,69,71,75,76,77,78,79,80],"evaluated":2795,"removal_order":[49,62,18,19,58,63,28,61,27,40,11,12,42,43,45,33,64,59,36,32,57,46,39,17,54,4,21,5,35,38,70,73,74,68,72,3,53,1,30,26,67,25,15,52,48,50,16,71,44,55,41,37,34,8,22,13,23,65,6,9,24,31,56,60,7]}},"environment":{"numpy":"2.3.5","python":"3.13.5","scipy":"1.17.0","torch":"2.10.0+cpu"},"free_bridge":[{"SUH":[5,5,8],"VEF":[77,225,150],"bar_counts_over_reporting_floor":[4,3],"evals":469,"iterations":114,"maximum_bar_depth":[0.14981528020081597,0.5918055700692122],"parameters":[0.24040285277586737,-0.3790248974701854,0.18808465380984668,-0.08346627526414176,0.03912769903354448,0.11131814946768047,0.18066289686298856,0.04969816393262251,0.012575431237403374,0.002741842853802011,0.0285913038727474,-0.07696098990372947,0.0471246152185625,0.03241269821107793,-0.03428143396462252,-0.05205385607416508,-0.06170814406056254,0.15764483317646266,0.17600152368214816,-0.11418662908372583,0.03791561928529456,0.10358234649913471,0.0957796496048839,0.02166838264151144,0.15152510748735096,-0.1090986785326668],"start":[0.0,0.0,0.0,0.0,0.0,0.051628708615618996,-0.27358063922348047,0.008862211184347577,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],"start_index":0},{"SUH":[6,6,10],"VEF":[80,234,156],"bar_counts_over_reporting_floor":[4,5],"evals":257,"iterations":73,"maximum_bar_depth":[0.43625205557710955,0.7467041926136075],"parameters":[0.30681066679953345,0.11711882661526392,0.12128946575582521,-0.04862324633781899,-0.1126909824385003,0.22706776782402,0.08035618329610034,-0.21094200012089856,-0.07306322991636972,0.024708534120331926,0.06144953201223498,0.021558338121926396,0.05587586582522725,0.028340729457741368,-0.10629647892286373,0.02341133261775309,0.05652224822302366,-0.0581294757493082,0.15094973038950316,-0.07461115797679481,-0.05272189209909394,-0.01308297958655276,-0.16227571102376293,0.2060474453563688,-0.10657192408750293,-0.3192221556297593],"start":[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],"start_index":1},{"SUH":[3,5,6],"VEF":[78,228,152],"bar_counts_over_reporting_floor":[3,2],"evals":123,"iterations":39,"maximum_bar_depth":[0.5772131433672684,0.7024910316076672],"parameters":[0.5156303059679243,-0.3911167533985371,0.17379661072132827,-0.11337924406438067,-0.3668479223723775,0.24015741267915175,-0.6614767812410551,0.5414009291845083,0.010537783187246842,-0.006035603912232236,-0.0042259599396368315,-0.02941708682483916,-0.014252319932831872,-0.022308698846974704,-0.07128518974663853,0.052923553242726254,0.030557300919993053,0.10257530978226653,0.044404486293791456,-0.02117502833055671,0.0328459409425976,0.05477051268561873,0.0037062764274761353,0.022212530477586867,-0.004739086739726687,0.15017706768231373],"start":[0.07265790298530099,-0.18381340310657918,0.025966849157599774,-0.11133018799985757,-0.07521623198784472,0.10310989649748284,-0.2817555216052826,0.1066914755970532,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],"start_index":2}],"old_reference_pole":[0.051628708615618996,-0.27358063922348047,0.008862211184347577],"orbit":[{"SUH":[29,21,48],"VEF":[79,231,154],"bar_counts_over_reporting_floor":[20,28],"evals":210,"iterations":7,"maximum_bar_depth":[0.304592478282602,0.5397820606440112],"p":[-0.0014363648790576052,0.0028229875369733125,0.0014680224634751726,-0.0026209131925562386,0.00218535461822853,0.05023015937342122,-0.2727088805227872,0.007410408981775249],"start":[0.0,0.0,0.0,0.0,0.0,0.051628708615618996,-0.27358063922348047,0.008862211184347577],"start_index":0},{"SUH":[27,26,51],"VEF":[79,231,154],"bar_counts_over_reporting_floor":[25,26],"evals":667,"iterations":24,"maximum_bar_depth":[0.14397724955347707,0.589349275543084],"p":[0.034460973040764606,-0.04333219515643984,0.09118892935658984,-0.05629353345546682,0.0527227553327431,0.062295999185724184,-0.0655411531541272,0.035260084432801354],"start":[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],"start_index":1},{"SUH":[2,2,2],"VEF":[79,231,154],"bar_counts_over_reporting_floor":[1,1],"evals":2206,"iterations":89,"maximum_bar_depth":[0.9997365532636528,0.9967723598043822],"p":[-1.8,-1.5336914361615885,0.5498457944721367,2.4991598727100857,1.4715645858506632,0.5718284778736001,-0.799830085257862,0.8],"start":[-0.5495905955182194,-0.05851223744658742,0.3264398538729866,0.17312926830914463,0.16506253317812253,0.010087975065211807,-0.16622651086724935,0.03296528439945778],"start_index":2},{"SUH":[12,6,16],"VEF":[79,231,154],"bar_counts_over_reporting_floor":[5,11],"evals":351,"iterations":14,"maximum_bar_depth":[0.7135912935286503,0.3798799243963891],"p":[-0.1791048217765202,-0.2629565420506279,-0.13697163219020023,0.09212432629405475,0.5598333955792468,-0.0694955426853269,-0.6308748057541084,-0.09343786246256668],"start":[-0.36007645497848995,-0.03688866151933463,-0.14566677276203419,-0.042270098531276355,0.394991512833295,0.06734511581848095,-0.21462982148181756,-0.20578567702204356],"start_index":3}]}
```

## File: replay_checkpoints.py
```python
"""Reconstruct literal numerical endpoints, without rerunning their optimizers."""
import json,hashlib,numpy as np
from repair import ROOT,geometry,summary
from orbit_search import Model
from bar_search import BarModel
from free_bridge import FreeBridge

def main():
    C=json.loads((ROOT/'numeric_checkpoints.json').read_text());out={}
    for name,model,param in [('orbit',Model('bridge'),'p'),('bars',BarModel(1.),'p'),('free_bridge',FreeBridge(.5),'parameters')]:
        out[name]=[]
        for r in C[name]:
            z=model.report(r[param]);assert z['geometry']['SUH']==r['SUH']
            out[name].append(z)
    D=json.loads((ROOT/'input.json').read_text());X=np.vstack([np.array(D['I'])/D['D'],np.array(D['A'])/D['AD']]);out['deletion']={}
    for mode,r in C['deletion'].items():
        ids=r['best_retained_input_ids'];s=summary(geometry(X[ids]));assert s['SUH']==r['best_SUH'];out['deletion'][mode]={'retained_input_ids':ids,'geometry':s}
    text=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n';(ROOT/'replayed_numeric.json').write_text(text)
    print('NUMERIC_CHECKPOINT_REPLAY_PASS',len(text.encode()),hashlib.sha256(text.encode()).hexdigest());print('FLOAT_COUNTS_ARE_NOT_EXACT_CERTIFICATES')
if __name__=='__main__':main()
```
