# material-d161d54b4145

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# New complete source units for physical complex growth

This is a newly reconstructed implementation, NOT a byte-identical recovery of the lost refine_caps.py or dynamic_cone.py. The earlier core joint solver remains independently preserved in [internal-source-reference]. These complete units use actual homogeneous volume and centroid, rebuild true simplicial hulls and P/Q merge forests, and never prescribe the old root or a virtual center. Output floating and rounded inputs are nominations until exact audit.

Exact starting input dependency: [internal-source-reference] contains the literal JB_REF48_TRUE53_G8.json1706B SHAef52650d1f2e0976e1ef05ae83ce842ae76b04607e60f9a910d4c743769b83a4, exact own211/C306. Exact verifier dependency: [internal-source-reference] contains complete exact_poly.py6134B SHA898f77989193886996d6f2dc121ccdfdf611b8a9ac52fd3207557eac6a69c0c4. Fresh workers must receive those full materials explicitly along with this source. The solver itself does not depend on prior joint solver code.

Write labelled files verbatim with final LF. Observed Python3.13.5,numpy2.3.5,scipy1.17.0,torch2.10.0+cpu,torchfloat64/threads1. Current source identities:joint_growth_v2.py6672B SHAee5fbc87020a94f7cd8a6c7f30e5799c38c5746b25d3471dcd6bd84dd390c0c3; whole_q_scout.py1598B SHA02375f2eb747135a41f689de9d0d7a8f87c5197efa8046e95a348ae7bdd514c5.

The scout has already executed:
```
OPENBLAS_NUM_THREADS=1 python whole_q_scout.py JB_REF48_TRUE53_G8_AUDIT.json
WHOLE_Q_LP 2.0 False None
WHOLE_Q_LP 10.0 False None
WHOLE_Q_LP 100.0 False None
```
These are three floating LP infeasibility reports with coordinate bounds, NOT an exact/global one-point-cover exclusion. The complete visibility method is retained for future use. The LP nominates a point, then all102 exact integer strict side signs are required before writing an exact point-insertion control. No new body was produced by this finite scout.

The growth method has not yet produced an accepted body when this source is stored. Example explicit experiment commands defining the next directions:
```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python joint_growth_v2.py JB_REF48_TRUE53_G8.json G2_REL --caps 30 --capheight .01 --order balanced --steps 1500 --lr .0008 --energy relative --pweight 3 --record 100 --digits 8
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python joint_growth_v2.py JB_REF48_TRUE53_G8.json G2_LOG --caps 30 --capheight .01 --order balanced --steps 1500 --lr .0008 --energy log --pweight 3 --record 100 --digits 8
python exact_poly.py G2_REL_BEST_G8.json
python exact_poly.py G2_REL_S2U1_G8.json
```
Expected search marker JOINT_GROWTH_V2_DONE and literal RATIONAL_NOMINATION rows do not imply exact110. Actual output hashes/bytes/classes belong in subsequent result capsules after execution. All non-default parameters are stated above; defaults seed0/noise0/epsilon1e-16 and gradientclip10/gauge1e-4 are explicit in full code. Cap count30 adds real outward points to53 truevertices, so at most83vertices/E243 under a simplicial hull. The code discards redundant points before normalization, which is inert geometry but alters optimizer variables and gauge relative to the lost78-input trajectory. Normals/caps are recomputed on the current actual body. Both sqrt(relative depth) and sqrt(log birth/death) are available; the log choice avoids saturation but is not a convergence theorem.

## joint_growth_v2.py
```python
"""Own-mass live-hull P/Q descent and real facet-cap enrichment.
Floating search only; final exact_poly audit is required. Python/numpy/scipy/torch.
"""
import argparse,json,hashlib,platform
from pathlib import Path
import numpy as np
import scipy
from scipy.spatial import ConvexHull
import torch

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
def geometry(x):
    raw=x.detach().numpy();hull=ConvexHull(raw);f=hull.simplices.copy()
    n=np.cross(raw[f[:,1]]-raw[f[:,0]],raw[f[:,2]]-raw[f[:,0]])
    flip=(n*hull.equations[:,:3]).sum(1)<0;f[flip]=f[flip][:,[0,2,1]]
    a,b,c=[x[f[:,k]] for k in range(3)];d=(a*torch.linalg.cross(b,c)).sum(1);vol=d.sum()/6
    g=(d[:,None]*(a+b+c)).sum(0)/(24*vol);z=x-g
    n=torch.linalg.cross(b-a,c-a);height=(n*z[f[:,0]]).sum(1);q=n/height[:,None]
    ef={}
    for j,t in enumerate(f.tolist()):
        for u,v in zip(t,t[1:]+t[:1]):ef.setdefault(tuple(sorted((u,v))),[]).append(j)
    pe=np.array(sorted(ef));qe=np.array([ef[tuple(e)] for e in pe]);assert qe.shape==(len(pe),2)
    return z,q,pe,qe,g,vol,f,hull.vertices

def bars(x,edges):
    R=(x*x).sum(1);a=x[edges[:,0]];d=x[edges[:,1]]-a
    t=torch.clamp(-(a*d).sum(1)/torch.clamp((d*d).sum(1),min=1e-280),0,1)
    H=((a+t[:,None]*d)**2).sum(1);r=R.detach().numpy();h=H.detach().numpy()
    parent=list(range(len(x)));root=parent[:];b=[];e=[]
    def find(u):
        while parent[u]!=u:parent[u]=parent[parent[u]];u=parent[u]
        return u
    for k in sorted(range(len(edges)),key=lambda k:(-h[k],*map(int,edges[k]))):
        u,v=map(lambda j:find(int(j)),edges[k])
        if u==v:continue
        if (r[root[u]],root[u])<(r[root[v]],root[v]):u,v=v,u
        b.append(root[v]);e.append(k);parent[v]=u
    B=R[b];D=H[e];return torch.relu((B-D)/B),B,D

def census(G):
    z,q,pe,qe,g,v,f,active=G
    def roots(x,edges,ids):
        x=x.detach().numpy();adj=[[] for _ in x]
        for a,b in edges:adj[a].append(b);adj[b].append(a)
        return [int(i) for i in ids if all(x[i]@(x[j]-x[i])<0 for j in adj[i])]
    U=roots(z,pe,active);S=roots(q,qe,range(len(q)));P=bars(z,pe)[0].detach().numpy();Q=bars(q,qe)[0].detach().numpy()
    return dict(V=len(active),E=len(pe),F=len(f),S=len(S),U=len(U),S_ids=S,U_ids=U,Psum=float(P.sum()),Qsum=float(Q.sum()),Pmax=float(P.max(initial=0)),Qmax=float(Q.max(initial=0)),Pbars=int((P>1e-12).sum()),Qbars=int((Q>1e-12).sum()),centroid=g.detach().tolist(),volume=float(v.detach()))

def write_json(path,data):
    b=(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n').encode();Path(path).write_bytes(b);return dict(filename=str(path),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())

def main(a):
    source=Path(a.input);raw=json.loads(source.read_text());p=np.array(raw['points'],float)/raw['denominator'] if isinstance(raw,dict) else np.array(raw,float)
    # Discard redundant points; this is inert geometry but changes optimization variables.
    p=p[ConvexHull(p).vertices];G=geometry(torch.tensor(p));g=G[4].numpy();scale=np.sqrt(np.mean(np.sum((p-g)**2,axis=1)));p=(p-g)/scale
    initial=dict(source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),centroid=g.tolist(),scale=scale)
    if a.caps:
        G=geometry(torch.tensor(p));f=G[6];normal=np.cross(p[f[:,1]]-p[f[:,0]],p[f[:,2]]-p[f[:,0]]);area=np.linalg.norm(normal,axis=1)/2;normal/=2*area[:,None];height=(normal*(p[f[:,0]]-G[4].numpy())).sum(1)
        score=area/height**2 if a.order=='balanced' else 1/height
        select=sorted(range(len(f)),key=lambda j:(-score[j],*sorted(f[j])))[:a.caps]
        added=p[f[select]].mean(1)+a.capheight*normal[select];p=np.concatenate([p,added])
        initial['selected_faces']=f[select].tolist()
    assert len(ConvexHull(p).vertices)<=85,'Initial simplicial budget exceeded'
    rng=np.random.default_rng(a.seed)
    if a.noise:p+=rng.normal(0,a.noise,p.shape)
    x=torch.tensor(p,requires_grad=True);opt=torch.optim.Adam([x],lr=a.lr);best=float('inf');best211=float('inf');records=[]
    def penalty(x,edges):
        depth,B,D=bars(x,edges)
        if a.energy=='log':depth=torch.relu(torch.log(B/torch.clamp(D,min=1e-280)))
        return (torch.sqrt(depth+a.epsilon)-np.sqrt(a.epsilon)).sum()
    for it in range(a.steps+1):
        opt.zero_grad();G=geometry(x);z,q,pe,qe,g,v,f,active=G;loss=a.pweight*penalty(z,pe)+penalty(q,qe);value=float(loss.detach())
        if value<best:
            best=value;bestx=x.detach().clone();bestdiag=census(G)
        if it%a.record==0 or it==a.steps:
            diag=census(G);records.append(dict(iteration=it,loss=value,**diag))
            if diag['S']==2 and diag['U']==1 and value<best211:
                best211=value;save211=x.detach().clone()
        if it==a.steps:break
        gauge=1e-4*((x.mean(0)**2).sum()+(((z*z).sum(1).mean()-1)**2));(loss+gauge).backward()
        if not torch.isfinite(x.grad).all():raise RuntimeError('Nonfinite gradient')
        torch.nn.utils.clip_grad_norm_([x],10);opt.step()
    prefix=a.output;manifest=[]
    manifest.append(write_json(prefix+'_BEST_FLOAT.json',bestx.tolist()))
    selections=[('BEST',bestx)]
    if best211<float('inf'):selections.append(('S2U1',save211))
    for label,pt in selections:
        rows=np.rint(pt.numpy()*10**a.digits).astype(np.int64).tolist();name=prefix+'_'+label+'_G'+str(a.digits);data=dict(name=Path(name).name,denominator=10**a.digits,points=rows);manifest.append(write_json(name+'.json',data))
        print('RATIONAL_NOMINATION',json.dumps(data,separators=(',',':')),flush=True)
    trace=dict(arguments=vars(a),versions=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,torch=torch.__version__),initial=initial,best_loss=best,best_diagnostics=bestdiag,records=records,manifest=manifest)
    write_json(prefix+'_TRACE.json',trace);print('JOINT_GROWTH_V2_DONE',json.dumps(dict(best=best,diagnostics=bestdiag,manifest=manifest),separators=(',',':')),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--caps',type=int,default=0);p.add_argument('--capheight',type=float,default=.01);p.add_argument('--order',choices=['balanced','polar'],default='balanced');p.add_argument('--steps',type=int,default=1500);p.add_argument('--lr',type=float,default=.0008);p.add_argument('--pweight',type=float,default=3);p.add_argument('--energy',choices=['relative','log'],default='relative');p.add_argument('--epsilon',type=float,default=1e-16);p.add_argument('--record',type=int,default=100);p.add_argument('--digits',type=int,default=8);p.add_argument('--noise',type=float,default=0);p.add_argument('--seed',type=int,default=0);main(p.parse_args())
```

## whole_q_scout.py
```python
"""Finite single-point visibility scout. LP nominates; exact audit decides.
Input is an exact_poly audit with points,faces,Q_bars and denominator.
"""
import json,sys,hashlib
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
A=json.loads(Path(sys.argv[1]).read_text());D=A['denominator'];X=np.array(A['points'],float)/D;faces=A['faces'];n=[];h=[]
for f in faces:
 u=np.cross(X[f[1]]-X[f[0]],X[f[2]]-X[f[0]]);u/=np.linalg.norm(u);n.append(u);h.append(u@X[f[0]])
n=np.array(n);h=np.array(h);q=max(A['Q_bars'],key=lambda a:a['depth_float']);I=set(q['component']);s=np.array([-1 if j in I else 1 for j in range(len(faces))]);M=np.column_stack([s[:,None]*n,np.ones(len(faces))]);rhs=s*h
for radius in [2.,10.,100.]:
 lp=linprog([0,0,0,-1],A_ub=M,b_ub=rhs,bounds=[(-radius,radius)]*3+[(0,None)],method='highs')
 print('WHOLE_Q_LP',radius,lp.success,None if lp.x is None else lp.x.tolist(),flush=True)
 if lp.success and lp.x[3]>1e-8:
  p=np.rint(lp.x[:3]*D).astype(np.int64).tolist();raw={'name':f'REF48_WHOLEQ_R{int(radius)}_G8','denominator':D,'points':A['points']+[p]};out=Path(raw['name']+'.json');b=(json.dumps(raw,sort_keys=True,separators=(',',':'))+'\n').encode();out.write_bytes(b)
  exact=[]
  for f in faces:
   a,bp,c=[np.array(A['points'][i],dtype=object) for i in f];nn=np.cross(bp-a,c-a);val=sum(nn[k]*(p[k]-a[k]) for k in range(3));exact.append(int(val))
  assert all((val>0)==(i in I) and val!=0 for i,val in enumerate(exact))
  print('WHOLE_Q_EXACT_VISIBILITY_PASS',out.name,p,'seen',len(I),'bytes',len(b),'sha256',hashlib.sha256(b).hexdigest(),flush=True)
```
