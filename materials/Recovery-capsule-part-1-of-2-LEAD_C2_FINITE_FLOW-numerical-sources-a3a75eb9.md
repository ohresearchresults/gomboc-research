# material-a3a75eb943a3

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# LEAD_C2_FINITE_FLOW numerical producing methods, complete source units

Part1of2 of the NUMERICAL METHOD capsule; the separate three-part EXACT capsule reconstructs all six rational bodies without a floating optimizer. This method is a new actual-mass finite C2 search, not recovery of the missing original scout. The exact old RECT/MASS input rows below come from fully read [internal-source-reference]; original mass correction and limits are in [internal-source-reference]. Save the complete code blocks under their headings, with final newline. No omitted helper or external local file is required except the explicitly selected checkpoint in part2.

Environment actually used: Python3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, binary64; OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1, torch.set_num_threads(1). These installed-version observations are not recommendations about current package releases. Qhull and9-decimal plane merging are NUMERICAL NOMINATION ONLY; the exact capsule rebuilds the true maximal complex exhaustively. Numerical barcode uses1e-12 nomination threshold; exact audit uses NONE. Positive all-pair physical escape at the actual filled centroid is an admissible nomination guard; the accepted exact auditor proves a positive true-edge forest. C2 forces the mass to the y-axis, not to zero.

Observed commands and scope (paths below are relative reconstructed checkpoint names, not a dependency on an originating sandbox):
- v1pair: copy c2_search_v1.py to c2_search.py and c2_project_v1.py to c2_project.py in a separate directory with inputs.py. `python c2_search.py RECT run_rect --steps120 --guard.0001 --radius.1` (insert spaces after option names):120-iteration SLSQP terminal violated physical guard, not accepted. `python c2_project.py RECT project_rect --steps220 --guard.0001 --trust.02`:44iterations, then no accepted feasible decrease; produced C2_CHAIN73_G5 via exact freeze. Commands in ordinary executable spelling are `python c2_search.py RECT run_rect --steps 120 --guard 0.0001 --radius 0.1` and `python c2_project.py RECT project_rect --steps 220 --guard 0.0001 --trust 0.02`.
- v2pair: `python c2_project.py RECT project_rect2 --start project_rect/project_terminal.npz --steps 220 --guard 0.00005 --buffer 0.000002 --trust 0.02`; container45-second execution ended with a feasible best checkpoint, not a family exclusion or an ordinary optimizer terminal. `python c2_project.py RECT project_free --start project_rect2/best.npz --steps 80 --guard 0.00002 --buffer 0.00001 --trust 0.02 --mode extreme --power 1` likewise ended at the execution boundary with its stored feasible best. All35 possible single half-row plus C2-partner deletions of project_free/best were enumerated with physical guard5e-6;10were feasible and removal32gave the lowest sum-log barcode loss. Its literal retained vector is in part2; new recoverable enumerator below uses the same finite operation and current equivalent unsmax features, not an invented full historical binary64 trace.
- v2pair: `python c2_project.py MASS project_mass --steps 45 --guard 0.0000001 --buffer 0.0001 --trust 0.01 --mode extreme --power 1`:45iterations; lower main barcode depth, but exact child has25stable equilibria, a useful failure control, not progress to110.
- v3search/currentproject: `python c2_project.py RECT project_s3 --steps 50 --guard 0.00001 --buffer 0.0001 --trust 0.01 --mode extreme --power 1 --smax 3 --sguard 0.00000001`:execution boundary left a feasible checkpoint. Current pair then `python c2_project.py RECT project_s3b --start project_s3/best.npz --steps 100 --guard 0.00001 --buffer 0.0001 --trust 0.01 --mode extreme --power 1 --smax 3 --sguard 0.00000001`:21iterations, then no accepted feasible Armijo step. The G8/G6/G4 freezes of this literal endpoint are three distinct exact geometries; G4 loses U1.

The source patches reconstruct every five earlier complete saved source versions with exact output hashes. They are source fidelity, not a proof of deterministic historical optimization under every BLAS/Qhull build. To reconstruct exact endpoints, use part2 checkpoints and freeze_lead.py, or better the independent literal exact capsule. Do not infer scientific stagnation or a family exclusion from the timed/stalled trials.

## inputs.py
```python
"""Literal exact C2 G6 entrances from [internal-source-reference].
No historical numerical producer is claimed. Integer rows / 1000000.
"""
import numpy as np
RECT=[[261286,-338124,0],[285998,-330578,13703],[310607,-321245,23814],[335499,-310096,29408],[360816,-297106,29997],[386448,-282244,25301],[412072,-265466,15228],[437202,-246718,-127],[461254,-225935,-20471],[483615,-203047,-45323],[503709,-177982,-74014],[521051,-150674,-105722],[535294,-121069,-139502],[546254,-89127,-174333],[553918,-54829,-209170],[558428,-18177,-242991],[560057,20806,-274842],[559160,62074,-303868],[556130,105563,-329341],[551335,151188,-350669],[545076,198848,-367398],[537536,248426,-379210],[528747,299786,-385912],[518570,352768,-387429],[506680,407191,-383795],[492573,462838,-375138],[475578,519458,-361670],[454886,576750,-343663],[429574,634362,-321413],[398643,691877,-295174],[361028,748802,-265062],[315602,804546,-230894],[261087,858390,-191924],[195771,909429,-146324],[116265,956505,-89745]]
MASS=[[489200,-504141,0],[494933,-498580,149611],[471041,-487431,265809],[425635,-474388,370197],[360994,-459881,463111],[278959,-444042,542789],[181719,-426882,606804],[72169,-408351,652649],[-45962,-388348,678230],[-168195,-366742,682320],[-289592,-343387,664950],[-405222,-318137,627634],[-510703,-290870,573355],[-602710,-261501,506304],[-679305,-229995,431400],[-740038,-196368,353699],[-785773,-160682,277825],[-818329,-123025,207532],[-840018,-83498,145448],[-853205,-42185,93019],[-859959,852,50606],[-861855,45589,17661],[-859906,92036,-7043],[-854601,140233,-25191],[-845998,190247,-38707],[-833830,242159,-49542],[-817585,296073,-59474],[-796533,352114,-69921],[-769710,410445,-81756],[-735852,471277,-95147],[-693264,534898,-109412],[-639583,601726,-122848],[-571206,672445,-132467],[-481573,748426,-133276],[-354073,833668,-115307]]
def initial(name):
    if name=='RECT':h=RECT;t=[34692,-351591,6428]
    elif name=='MASS':h=MASS;t=[230979,-506519,441166]
    else:raise ValueError(name)
    return np.r_[np.array(h,dtype=float).ravel(),t]/1000000
```
## c2_search.py
```python
"""New actual-volume-centred C2 geometry search, NOT the lost original scout.
Python3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu; binary64, one thread.
SLSQP differentiates filled mass and physical escape guards, rebuilding the hull.
Float objectives nominate only; rational freezing/full exact audit is separate.
Usage: python c2_search.py RECT OUT --steps 400 --guard 0.0001
or --start exact-checkpoint.npz. All non-default parameters are printed/saved.
"""
import argparse,json,os,time
from pathlib import Path
import numpy as np
import torch
from scipy.spatial import ConvexHull
from scipy.optimize import minimize,Bounds
from inputs import initial
DT=torch.float64
torch.set_num_threads(1)
R=torch.tensor([-1.,1.,-1.],dtype=DT)
def body(z):
    n=(len(z)-3)//3;h=z[:3*n].reshape(n,3);a,y,b=z[-3:]
    tail=torch.stack((torch.stack((a,y,b)),torch.stack((-a,y,b)),torch.stack((-a,y,-b)),torch.stack((a,y,-b))))
    return torch.cat((h,h*R,torch.tensor([[0.,1.,0.]],dtype=DT),tail)),n

def topology(P):
    hull=ConvexHull(P)
    T=hull.simplices.copy();sgn=np.sign(np.einsum('ij,ij->i',np.cross(P[T[:,1]]-P[T[:,0]],P[T[:,2]]-P[T[:,0]]),hull.equations[:,:3]))
    T[sgn<0]=T[sgn<0][:,[0,2,1]]
    keys={};fid=[];rep=[]
    for k,e in enumerate(hull.equations):
        # Numerical nomination merge only; the exact auditor uses integer planes.
        key=tuple(np.round(e,9))
        if key not in keys:keys[key]=len(keys);rep.append(k)
        fid.append(keys[key])
    owners={}
    for f,t in enumerate(T):
        for i,j in ((t[0],t[1]),(t[1],t[2]),(t[2],t[0])):owners.setdefault(tuple(sorted((int(i),int(j)))),[]).append(fid[f])
    E=sorted(e for e,fs in owners.items() if len(set(fs))==2)
    QE=sorted({tuple(sorted(set(fs))) for fs in owners.values() if len(set(fs))==2})
    # Trial steps may retain flat non-extreme inputs; numerical counts nominate
    # only. Exact maximal polygons and true edges determine accepted counts.
    active=np.unique(np.array(E,dtype=int))
    return T,T[rep],np.array(E,dtype=int),np.array(QE,dtype=int),active

def geometry(z,top):
    P,n=body(z);T,FT,E,QE,active=top
    tr=P[T];dd=(tr[:,0]*torch.linalg.cross(tr[:,1],tr[:,2])).sum(1);v6=dd.sum()
    cen=(dd[:,None]*tr.sum(1)).sum(0)/(4*v6)
    # Exact model symmetry makes x,z moments zero; keep the computed y moment.
    c=torch.stack((cen[0]*0,cen[1],cen[2]*0));X=P-c
    tri=X[FT];nn=torch.linalg.cross(tri[:,1]-tri[:,0],tri[:,2]-tri[:,0]);hh=(nn*tri[:,0]).sum(1)
    Q=nn/hh[:,None]
    return P,X,Q,v6/6,c,n

def positive_bars(Q,edges):
    B=np.einsum('ij,ij->i',Q,Q);a=B[edges[:,0]];c=B[edges[:,1]];b=np.einsum('ij,ij->i',Q[edges[:,0]],Q[edges[:,1]])
    w=np.where(b>=a,a,np.where(b>=c,c,(a*c-b*b)/np.maximum(a+c-2*b,1e-300)))
    par=np.arange(len(Q));peak=np.arange(len(Q));bars=[]
    def find(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return i
    for k in np.argsort(-w,kind='stable'):
        i,j=edges[k];u,v=find(i),find(j)
        if u==v:continue
        if (B[peak[u]],-peak[u])<(B[peak[v]],-peak[v]):u,v=v,u
        p=peak[v]
        if B[p]>w[k]*(1+1e-12):bars.append((int(p),int(i),int(j),float(B[p]/w[k]-1)))
        par[v]=u
    return bars

def features(z,top,guard,mode="chain",power=2,smax=0,sguard=1e-8):
    P,X,Q,V,c,n=geometry(z,top);QE=top[3]
    # Every non-root source has an acyclic prescribed positive escape.
    aa=np.r_[np.arange(n),np.arange(n,2*n)]
    bb=np.r_[np.arange(1,n),2*n,np.arange(n+1,2*n),2*n]
    xb=X[2*n+1:];d=X[:2*n+1][None,:,:]-xb[:,None,:]
    val=(xb[:,None,:]*d).sum(2)/(torch.linalg.vector_norm(xb,dim=1)[:,None]*torch.linalg.vector_norm(d,dim=2).clamp_min(1e-30))
    targets=val.detach().argmax(1).numpy();aa=np.r_[aa,np.arange(2*n+1,2*n+5)];bb=np.r_[bb,targets]
    delta=X[bb]-X[aa];cos=(X[aa]*delta).sum(1)/(torch.linalg.vector_norm(X[aa],dim=1)*torch.linalg.vector_norm(delta,dim=1)).clamp_min(1e-30)
    h=z[:3*n].reshape(n,3);root_height=1-c[1]
    gc=cos
    if mode=="extreme":
        act=[int(i) for i in top[4] if i!=2*n]
        xa=X[act];diff=X[None,:,:]-xa[:,None,:]
        gc_all=(xa[:,None,:]*diff).sum(2)/(torch.linalg.vector_norm(xa,dim=1)[:,None]*torch.linalg.vector_norm(diff,dim=2)).clamp_min(1e-30)
        mask=torch.zeros_like(gc_all,dtype=torch.bool);mask[np.arange(len(act)),act]=True
        gt=gc_all.detach().masked_fill(mask,-1e6).argmax(1)
        gd=X[gt]-xa
        gc=(xa*gd).sum(1)/(torch.linalg.vector_norm(xa,dim=1)*torch.linalg.vector_norm(gd,dim=1)).clamp_min(1e-30)
    constraints=torch.cat((gc-guard,h[:,1]-z[-2]-0.0001,1-h[:,1]-0.0001,(V/root_height**3-0.01).reshape(1)))
    qn=(Q*Q).sum(1)
    qm=(Q@Q.T-qn[:,None])/qn[:,None]
    qm=qm.masked_fill(torch.eye(len(Q),dtype=torch.bool),-1e6)
    qt=qm.detach().argmax(1)
    qe=(Q*(Q[qt]-Q)).sum(1)/qn
    if smax:
        exempt=set(qe.detach().argsort()[:smax].tolist())
        keep=[i for i in range(len(Q)) if i not in exempt]
        constraints=torch.cat((constraints,1000*(qe[keep]-sguard)))
    bars=positive_bars(Q.detach().numpy(),QE)
    terms=[]
    for p,i,j,_ in bars:
        a=(Q[i]*Q[i]).sum();cc=(Q[j]*Q[j]).sum();b=(Q[i]*Q[j]).sum();birth=(Q[p]*Q[p]).sum()
        w=torch.where(b>=a,a,torch.where(b>=cc,cc,(a*cc-b*b)/(a+cc-2*b)))
        terms.append(torch.log(birth/w).clamp_min(0)**power)
    objective=torch.stack(terms).sum() if terms else z.sum()*0
    return objective,constraints,{'volume':float(V.detach()),'centroid':c.detach().tolist(),'chain_min_cos':float(cos.detach().min()),'physical_guard_min_cos':float(gc.detach().min()),'mode':mode,'power':power,'smax':smax,'numeric_S':int((qe.detach()<0).sum()),'Qbars':bars,'V':len(top[4]),'E':len(top[2]),'F':len(top[1]),'loss':float(objective.detach())}

class Search:
    def __init__(self,z,guard,out,mode="chain",power=2,smax=0,sguard=1e-8):self.smax=smax;self.sguard=sguard;self.mode=mode;self.power=power;self.guard=guard;self.out=Path(out);self.out.mkdir(exist_ok=True,parents=True);self.last=None;self.calls=0;self.best=float('inf');self.first=z.copy();self.started=time.time()
    def calc(self,z):
        if self.last is not None and np.array_equal(z,self.last[0]):return self.last[1]
        t=torch.tensor(z,dtype=DT,requires_grad=True);P,_=body(t);top=topology(P.detach().numpy());f,g,info=features(t,top,self.guard,self.mode,self.power,self.smax,self.sguard)
        df=torch.autograd.grad(f,t,retain_graph=True)[0].detach().numpy()
        J=torch.autograd.functional.jacobian(lambda u:features(u,top,self.guard,self.mode,self.power,self.smax,self.sguard)[1],t,vectorize=True).detach().numpy()
        gv=g.detach().numpy();fv=float(f.detach());self.calls+=1
        if min(gv)>-1e-10 and fv<self.best:
            self.best=fv;info.update(calls=self.calls,guard=self.guard,elapsed=time.time()-self.started)
            np.savez(self.out/'best.npz',z=z);(self.out/'best.json').write_text(json.dumps(info,indent=2)+'\n')
            if self.calls==1 or self.calls%10==0 or fv<0.00001:print(json.dumps(info),flush=True)
        self.last=(z.copy(),(fv,df,gv,J,info));return self.last[1]
    def fun(self,z):return self.calc(z)[0]
    def jac(self,z):return self.calc(z)[1]
    def con(self,z):return self.calc(z)[2]
    def cjac(self,z):return self.calc(z)[3]

def run(args):
    z=np.load(args.start)['z'] if args.start else initial(args.entrance);n=(len(z)-3)//3
    s=Search(z,args.guard,args.out);f,df,g,J,info=s.calc(z);print('START',json.dumps(info),'constraint_min',min(g),flush=True)
    lb=np.full(len(z),-3.);ub=np.full(len(z),3.);ub[np.arange(n)*3+1]=.9999
    lb[-3]=lb[-1]=.0005;ub[-2]=.9
    lb=np.maximum(lb,z-args.radius);ub=np.minimum(ub,z+args.radius)
    result=minimize(s.fun,z,jac=s.jac,method='SLSQP',constraints={'type':'ineq','fun':s.con,'jac':s.cjac},bounds=Bounds(lb,ub),options={'maxiter':args.steps,'ftol':args.ftol,'disp':True})
    np.savez(Path(args.out)/'terminal.npz',z=result.x)
    (Path(args.out)/'parameters.json').write_text(json.dumps(vars(args),sort_keys=True,indent=2)+'\n')
    print('TERMINAL',result.success,result.message,s.calc(result.x)[4],flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('entrance',choices=['RECT','MASS']);p.add_argument('out');p.add_argument('--start');p.add_argument('--steps',type=int,default=400);p.add_argument('--guard',type=float,default=.0001);p.add_argument('--radius',type=float,default=.1);p.add_argument('--ftol',type=float,default=1e-12);run(p.parse_args())
```
## c2_project.py
```python
"""Feasible projected descent with an actual-centroid physical escape forest.
Uses complete c2_search.py and inputs.py. Numerical nomination, not exact proof.
Usage: python c2_project.py RECT OUT --steps 300 --guard .0001 --trust .02
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize,Bounds
from c2_search import Search,initial

def run(a):
    z=np.load(a.start)['z'] if a.start else initial(a.entrance);n=(len(z)-3)//3
    s=Search(z,a.guard,a.out,a.mode,a.power,a.smax,a.sguard);out=Path(a.out);lb=np.full(len(z),-3.);ub=np.full(len(z),3.)
    ub[np.arange(n)*3+1]=.9999;lb[-3]=lb[-1]=.0005;ub[-2]=.9
    f,df,g,J,info=s.calc(z);assert min(g)>0,'need an interior feasible starting point'
    print('PROJECT_START',json.dumps(info),flush=True);history=[];started=time.time()
    for k in range(a.steps):
        f,df,g,J,info=s.calc(z)
        desired=-a.trust*df/max(np.max(np.abs(df)),1e-30)
        dlo=np.maximum(lb-z,-a.trust);dhi=np.minimum(ub-z,a.trust)
        q=minimize(lambda d:.5*np.dot(d-desired,d-desired),np.zeros(len(z)),jac=lambda d:d-desired,
            method='SLSQP',bounds=Bounds(dlo,dhi),constraints={'type':'ineq','fun':lambda d:g*.75-a.buffer+J@d,'jac':lambda d:J},
            options={'maxiter':150,'ftol':1e-13})
        d=q.x;accepted=False
        for j in range(25):
            t=2.**(-j);zz=z+t*d
            try:ff,ddf,gg,JJ,ii=s.calc(zz)
            except (ValueError,AssertionError):continue
            if min(gg)>=-1e-10 and ff<f+min(-1e-15,1e-4*t*float(df@d)):
                z=zz;accepted=True;break
        row={'iteration':k,'loss':f,'minimum_constraint':float(min(g)),'step':t if accepted else 0,'qp_success':bool(q.success),'step_norm':float(np.linalg.norm(d))}
        history.append(row)
        if k%10==0 or not accepted:print('PROJECT',json.dumps(row),flush=True)
        if not accepted:break
    f,df,g,J,info=s.calc(z);np.savez(out/'project_terminal.npz',z=z)
    info.update(iterations=len(history),elapsed=time.time()-started,minimum_constraint=float(min(g)))
    (out/'project_summary.json').write_text(json.dumps(info,sort_keys=True,indent=2)+'\n')
    (out/'project_history.json').write_text(json.dumps(history,sort_keys=True,indent=2)+'\n')
    (out/'project_parameters.json').write_text(json.dumps(vars(a),sort_keys=True,indent=2)+'\n')
    print('PROJECT_FINISHED',json.dumps(info),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('entrance',choices=['RECT','MASS']);p.add_argument('out');p.add_argument('--start');p.add_argument('--steps',type=int,default=300);p.add_argument('--guard',type=float,default=.0001);p.add_argument('--smax',type=int,default=0);p.add_argument('--sguard',type=float,default=1e-8);p.add_argument('--buffer',type=float,default=.000002);p.add_argument('--mode',choices=['chain','extreme'],default='chain');p.add_argument('--power',type=int,choices=[1,2],default=2);p.add_argument('--trust',type=float,default=.02);run(p.parse_args())
```
## freeze_lead.py
```python
"""Freeze a saved finite numerical nomination, preserving C2 exactly.
Python3.13.5/NumPy2.3.5. Literal output integers, not optimizer replay,
are the exact construction. All scalar rounding is Python ties-to-even.
Usage: python freeze_lead.py checkpoint.npz G identity out.json
"""
import sys,json,hashlib
from pathlib import Path
import numpy as np

def freeze(path,g,identity):
    z=np.load(path)['z'];scale=10**g;assert len(z)%3==0
    h=[[round(float(v)*scale) for v in row] for row in z[:-3].reshape(-1,3)]
    xb,yb,zb=[round(float(v)*scale) for v in z[-3:]]
    rows=h+[[-x,y,-zz] for x,y,zz in h]+[[0,scale,0],[xb,yb,zb],[-xb,yb,zb],[-xb,yb,-zb],[xb,yb,-zb]]
    return dict(identity=identity,scale=scale,rows=rows,rounding='Python round nearest ties-to-even; literal integer rows authoritative',half_count=len(h))
if __name__=='__main__':
    path,g,name,out=sys.argv[1:];d=freeze(path,int(g),name);raw=(json.dumps(d,sort_keys=True,indent=2)+'\n').encode();Path(out).write_bytes(raw)
    print(name,len(raw),hashlib.sha256(raw).hexdigest())
```
## recover_versions.py
```python
"""Exact earlier complete source versions from the stored current units.
Python3.13.5 standard library. Run python -B -S recover_versions.py.
Apply every character replacement to its unmodified matching base.
"""
from pathlib import Path
import hashlib
PATCHES = {'c2_search_v1.py': ['c2_search.py', '3e22209bd3dd89ed5d6ac4e5b33f4f0fd12d66e857dfebb5ac1c852f12ba0e7d', [[3218, 3258, ''], [3946, 4502, ''], [4525, 4526, ''], [4527, 4527, 'os'], [4603, 4981, ''], [5290, 5295, '2'], [5495, 5622, ''], [5764, 5804, ''], [5806, 5872, ''], [6290, 6333, ''], [6483, 6526, '']], 7151, 'b89f9eba2b09835e0bf591b64b11e61dffcc93b5736975fdacbe07466cd7b57b'], 'c2_search_v2.py': ['c2_search.py', '3e22209bd3dd89ed5d6ac4e5b33f4f0fd12d66e857dfebb5ac1c852f12ba0e7d', [[3239, 3258, ''], [4312, 4313, 'c'], [4320, 4329, ''], [4353, 4356, ''], [4362, 4401, ''], [4402, 4419, 'v'], [4421, 4424, 'u'], [4425, 4497, 's'], [4603, 4981, ''], [5571, 5622, ''], [5785, 5804, ''], [5806, 5840, ''], [6311, 6333, ''], [6509, 6531, '']], 7762, '0457c2fa24131c25ca453b5e20420e001aea9fa2876ac95df36c40a24bdbb071'], 'c2_search_v3.py': ['c2_search.py', '3e22209bd3dd89ed5d6ac4e5b33f4f0fd12d66e857dfebb5ac1c852f12ba0e7d', [[4312, 4313, 'c'], [4320, 4329, ''], [4353, 4356, ''], [4362, 4401, ''], [4402, 4419, 'v'], [4421, 4424, 'u'], [4425, 4497, 's'], [4732, 4733, 'e'], [4737, 4749, ''], [4755, 4761, '.valu'], [4762, 4777, ''], [4778, 4786, '']], 8271, '7603ee8ac8c1a9a762e17519f4a9eb6d538a08240b6e9573647808dfd9192fe2'], 'c2_project_v1.py': ['c2_project.py', '26b717708867dbf551844d936e332bfbc91c4a8049436257e0e6a945ce247453', [[509, 540, ''], [1220, 1229, ''], [2690, 2967, '']], 2701, '0c6736648dca180e57c1b1a8475a87a1cbd54982ecb82782c4b427b3b94a8bab'], 'c2_project_v2.py': ['c2_project.py', '26b717708867dbf551844d936e332bfbc91c4a8049436257e0e6a945ce247453', [[524, 540, ''], [2690, 2785, '']], 2907, '4a6155dde9a3359826deefbdd1d9da97d71dc3d5067767224bb93d708138836a']}
for name,(base,sha,ops,size,target_sha) in PATCHES.items():
    s=Path(base).read_text();assert hashlib.sha256(s.encode()).hexdigest()==sha
    for i,j,text in reversed(ops):s=s[:i]+text+s[j:]
    b=s.encode();assert len(b)==size and hashlib.sha256(b).hexdigest()==target_sha
    Path(name).write_bytes(b)
print('LEAD_C2_FIVE_HISTORICAL_SOURCE_VERSIONS_RECOVERED',len(PATCHES))
```

## delete_pairs.py — complete reusable finite operation
The historical inline enumeration is reconstructed here as a runnable source unit using the same literal project_free checkpoint and current equivalent unrestricted-S features. It is not a claim that the new file existed during the inline trial. Row deletion changes actual mass and rebuilds the hull; no arrow inheritance is assumed.
```python
import sys,json
from pathlib import Path
import numpy as np
import torch
from c2_search import body,topology,features,DT
z=np.load(sys.argv[1])['z'];h=z[:-3].reshape(-1,3);out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
feasible=[]
for i in range(len(h)):
    w=np.r_[np.delete(h,i,axis=0).ravel(),z[-3:]]
    try:
        t=torch.tensor(w,dtype=DT);P,n=body(t)
        f,g,info=features(t,topology(P.numpy()),5e-6,'extreme',1)
        if float(g.min())>0:feasible.append((float(f),i,w,info))
    except (ValueError,AssertionError):pass
assert feasible
f,i,w,info=min(feasible,key=lambda row:(row[0],row[1]))
np.savez(out/'delete_best.npz',z=w)
(out/'delete_best.json').write_text(json.dumps(dict(removed_half_index=i,summary=info,feasible_deletions=len(feasible)),sort_keys=True,indent=2)+'\n')
print('LEAD_C2_SINGLE_PAIR_DELETION_FINITE_REPLAY',len(h),len(feasible),i,f)
```
