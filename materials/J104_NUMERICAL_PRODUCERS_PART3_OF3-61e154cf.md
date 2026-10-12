# material-61e154cfa5a5

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Recovery capsule part 3/3 — J104 numerical producers

This completes the J104 numerical producer archive. Part1 supplies metric_search.py and the exact49-row input; this part supplies complete own-mass projective and physical common-face bridge producers. Numerical classifications are nominations only, not strict/weak exact certificates. None of these searches produced a target. The exact affine-component theorem is a separate source-complete material [internal-source-reference].

Executed: Python3.13.5, NumPy2.3.5, SciPy1.17.0, OPENBLAS_NUM_THREADS=1.
python projective_metric.py --starts 4 --maxiter 600 --output projective_class1.json
python projective_joint.py --starts 10 --maxiter 600 --warm projective_class1.json --output projective_joint1.json
python shared_face_bridge.py --output shared_face_bridge1.json

The constrained projective run recomputes the exact-form numerical uniform mass of the transported physical triangulation before every landscape evaluation; it does not transport the old mass distribution. Four starts converge to P~.51171064663068, S1/U2, Q[],E141. Its gradient check gave maximum absolute errors~9.19e-11 for the bar objective and9.56e-8 for all normalized chord constraints. The fixed U2 guards are an explicit policy and preclude crossing U-cancellation while retained; the later joint run removes that restriction. Ten joint free-root starts found noS1/U1 and sometimes very small angular hinge loss with deep P/Q, so that loss cannot be reported as basin cancellation. No root floor is used in the bar census.

The common-face bridge is a separate physical convex-hull addition, not a projective map. The author-labeled U80/U0 are support-triple lex43/57 and share physical face47. Relative to the perpendicular foot on its plane, the tangent-radius ratio is~1.50064568221157 and short angular separation~2.98997229150734. Twelve links suffice for positive tangent radial chords. The96 executed combinations use n in[10,12,14,16,20,24,30,36],two arc orientations,and heights[1,.95,.8,.5,0,-1]. All rebuild the true maximal facets numerically with explicitly stated1e-8 grouping tolerance and actual uniform mass. None had ownS1 or ownU1. The short planar12-link specimen has72/128/58,referenceS4/U1 but actualS8/U16,volume~1.699683973167273 versus parent1.308458351834595, and actual centre~(-.149514257754868,.057310876690996,-.019486734996466) in parent-centred coordinates. Its minimum reference path score~.00220761738218 is genuinely positive, and its new points remain below old stable support15. This is not reference110; extra S already exist before the centre drift. No exact rational realization of this bridge was claimed or promoted.

## File: frozen_checkpoints.json
```json
{"primary_input":"KF27D_QCANCEL_ROBUST_G4.txt","evidence":"floating parameter checkpoints, not exact bodies","affine_S1_U2":{"theta":[0.0005299986934548338,-0.00010249903541180838,0.00006876269359626139,0.0001907257410458494,0.00008997145078687739],"P":0.5125640528091413},"projective_S1_U2":{"theta":[-0.00003176260627192199,-0.00020905142645410312,-0.0006928772395288795,0.0005654217020864045,0.00036443492551281934,-0.0005712981382174204,-0.002896826036767027,-0.0017285689255505513],"rho":0.9,"P":0.5117106466306773,"b":[-0.0005130552087293125,-0.002601499265485782,-0.0015523440942211337]},"joint_small_loss_nonwinner":{"theta":[-0.35536662157871296,3.0,-1.9775133791364932,-2.9788877341623974,-2.839849741905618,0.43927498711942486,-1.1226601372888987,-2.6949771003833565],"rho":0.9,"S":3,"U":3,"P":0.960702028567485,"Q":0.9999675731335959,"loss":0.000001027310712722194},"delete5_affine_nonwinner":{"deleted_original_input_rows":[5],"theta":[0.00020377634755956646,-0.00002503943883384,-0.00032899001552750596,0.0005506100634273096,0.00008806785493023931],"P":0.512685248823646,"S":1,"U":2}}
```

## File: projective_metric.py
```python
#!/usr/bin/env python3
"""Own-mass projective plus affine geometry of the literal C282 parent.
Numerical nomination only. The entire facet triangulation is transported;
a positive projective denominator retains convexity/incidence, not equilibria.
"""
import json,argparse,platform
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from metric_search import geometry,matrices,INPUT

class Dynamic:
    def __init__(self,geo,rho=.9):
        self.geo=geo;self.P=geo['P'];self.Q=geo['Y'];self.rho=rho
        self.tris=np.array([(f[0],f[j],f[j+1]) for f in geo['facets'] for j in range(1,len(f)-1)],int)
        self.edges=geo['edges'];self.pedges=geo['pedges'];self.last=None
        self.arcs=[np.array([(a,b) for i,j in ee for a,b in ((i,j),(j,i))]) for ee in (self.edges,self.pedges)]
        self.groups=[[np.where(aa[:,0]==i)[0] for i in range(n)] for aa,n in zip(self.arcs,(len(self.P),len(self.Q)))]
    def geom(self,t):
        # This exact differentiable-piecewise parameterization gives |P_i.b|<rho.
        z=t[5:];v=self.P@z;ix=int(np.argmax(np.abs(v)));rad=abs(v[ix]);dr=np.sign(v[ix])*self.P[ix]
        b=self.rho*z/(1+rad);Db=self.rho*(np.eye(3)/(1+rad)-np.outer(z,dr)/(1+rad)**2)
        den=1+self.P@b;assert den.min()>1-self.rho-1e-10
        Y=self.P/den[:,None];DY=-np.einsum('ni,nk->kni',self.P/den[:,None]**2,self.P@Db)
        a,c,d=Y[self.tris[:,0]],Y[self.tris[:,1]],Y[self.tris[:,2]]
        da,dc,dd=DY[:,self.tris[:,0]],DY[:,self.tris[:,1]],DY[:,self.tris[:,2]]
        volumes=np.einsum('ni,ni->n',a,np.cross(c,d))/6
        dvol=(np.einsum('kni,ni->kn',da,np.cross(c,d))+np.einsum('ni,kni->kn',a,np.cross(dc,d[None,:,:])+np.cross(c[None,:,:],dd)))/6
        assert volumes.min()>0
        V=volumes.sum();dV=dvol.sum(axis=1);cent=(a+c+d)/4;dcent=(da+dc+dd)/4
        M=np.einsum('n,ni->i',volumes,cent);dM=np.einsum('kn,ni->ki',dvol,cent)+np.einsum('n,kni->ki',volumes,dcent)
        g=M/V;Dg=(dM-dV[:,None]*g)/V;X=Y-g;DX=DY-Dg[:,None,:]
        R=self.Q+b;DR=np.repeat(Db.T[:,None,:],len(R),axis=1)
        h=1-R@g;Dh=-np.einsum('kni,i->kn',DR,g)-np.einsum('ni,ki->kn',R,Dg)
        Z=R/h[:,None];DZ=DR/h[None,:,None]-R[None,:,:]*Dh[:,:,None]/h[None,:,None]**2
        out=[]
        for xx,dx in ((X,DX),(Z,DZ)):
            ds=np.zeros((8,len(xx),3));ds[5:]=dx;out.append((xx,ds))
        A,G,DG,J,DJ=matrices(t[:5]);dg=np.zeros((8,3,3));dj=dg.copy();dg[:5]=DG;dj[:5]=DJ
        return out,A,G,dg,J,dj,dict(b=b.tolist(),projective_volume=float(V),projective_centroid=g.tolist(),min_projective_denominator=float(den.min()))
    def landscape(self,X,DX,G,DG,side):
        aa=self.arcs[side];z=X[aa[:,0]];d=X[aa[:,1]]-z;dz=DX[:,aa[:,0]];dd=DX[:,aa[:,1]]-dz
        zg=z@G;dg=d@G;u=np.einsum('ni,ni->n',zg,d);s=np.einsum('ni,ni->n',zg,z);h=np.einsum('ni,ni->n',dg,d)
        du=np.einsum('kni,ni->nk',dz,dg)+np.einsum('ni,kij,nj->nk',z,DG,d)+np.einsum('ni,kni->nk',zg,dd)
        ds=2*np.einsum('kni,ni->nk',dz,zg)+np.einsum('ni,kij,nj->nk',z,DG,z)
        dh=2*np.einsum('kni,ni->nk',dd,dg)+np.einsum('ni,kij,nj->nk',d,DG,d)
        den=np.sqrt(s*h);score=u/den;der=du/den[:,None]-.5*score[:,None]*(ds/s[:,None]+dh/h[:,None])
        pick=np.array([ix[np.argmax(score[ix])] for ix in self.groups[side]])
        return score[pick],der[pick],int(np.argmax(np.einsum('ni,ij,nj->n',X,G,X))),pick
    def bars(self,X,DX,edges,G,DG):
        birth=np.einsum('ni,ij,nj->n',X,G,X)
        db=np.einsum('ni,kij,nj->nk',X,DG,X)+2*np.einsum('kni,ni->nk',DX,X@G)
        ev=[]
        for i,j in edges:
            a=X[i];d=X[j]-a;t=float(np.clip(-(a@G@d)/(d@G@d),0,1));s=a+t*d;ds=DX[:,i]+t*(DX[:,j]-DX[:,i])
            if t==0:h=birth[i];dh=db[i]
            elif t==1:h=birth[j];dh=db[j]
            else:h=s@G@s;dh=np.einsum('i,kij,j->k',s,DG,s)+2*ds@(G@s)
            ev.append((float(h),i,j,dh))
        ev.sort(key=lambda e:(-e[0],e[1],e[2]));parent=list(range(len(X)))
        def find(i):
            while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
            return i
        bars=[]
        for h,i,j,dh in ev:
            u=find(i);v=find(j)
            if u==v:continue
            if (birth[u],-u)<(birth[v],-v):u,v=v,u
            depth=1-h/birth[v]
            if depth>0:bars.append(dict(depth=float(depth),root=v,edge=[i,j],birth=float(birth[v]),death=h,gradient=(h*db[v]/birth[v]**2-dh/birth[v]).tolist()))
            parent[v]=u
        return sorted(bars,key=lambda r:-r['depth'])
    def calc(self,t):
        if self.last is not None and np.array_equal(t,self.last[0]):return self.last[1]
        pairs,A,G,DG,J,DJ,meta=self.geom(t)
        p=self.landscape(*pairs[0],G,DG,0);q=self.landscape(*pairs[1],J,DJ,1)
        result=(pairs,A,G,DG,J,DJ,meta,p,q);self.last=(np.asarray(t).copy(),result);return result
    def report(self,t):
        pairs,A,G,DG,J,DJ,meta,p,q=self.calc(t)
        return dict(theta=np.asarray(t).tolist(),A=A.tolist(),G_eigenvalues=np.linalg.eigvalsh(G).tolist(),S=np.where(q[0]<0)[0].tolist(),U=np.where(p[0]<0)[0].tolist(),S_best=q[0].tolist(),U_best=p[0].tolist(),P=self.bars(*pairs[0],self.edges,G,DG),Q=self.bars(*pairs[1],self.pedges,J,DJ),**meta)

class Constrained(Dynamic):
    def __init__(self,geo,eps=1e-7,rho=.9):
        super().__init__(geo,rho);self.eps=eps;p,q=self.calc(np.zeros(8))[-2:];self.ur=np.where(p[0]<0)[0];self.sr=np.where(q[0]<0)[0];self.um=np.ones(len(p[0]),bool);self.um[self.ur]=False;self.sm=np.ones(len(q[0]),bool);self.sm[self.sr]=False
    def objective(self,t):
        pairs,A,G,DG,J,DJ,meta,p,q=self.calc(t);bb=self.bars(*pairs[0],self.edges,G,DG)
        return (bb[0]['depth'],np.array(bb[0]['gradient'])) if bb else (0.,np.zeros(8))
    def constraints(self,t,jac=False):
        p,q=self.calc(t)[-2:]
        if jac:return np.vstack((p[1][self.um],q[1][self.sm],-p[1][self.ur],-q[1][self.sr]))
        return np.r_[p[0][self.um],q[0][self.sm],-p[0][self.ur],-q[0][self.sr]]-self.eps

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--starts',type=int,default=3);ap.add_argument('--maxiter',type=int,default=500);ap.add_argument('--eps',type=float,default=1e-7);ap.add_argument('--rho',type=float,default=.9);ap.add_argument('--seed',type=int,default=280105);ap.add_argument('--bound',type=float,default=3);ap.add_argument('--output',default='projective_class.json');a=ap.parse_args();co=Constrained(geometry(),a.eps,a.rho)
    z=np.array([.07,-.05,.08,-.1,.03,.12,-.07,.08]);val,grad=co.objective(z);e=1e-6;basis=np.eye(8);fd=np.array([(co.objective(z+e*v)[0]-co.objective(z-e*v)[0])/(2*e) for v in basis]);cg=co.constraints(z,True);cf=np.stack([(co.constraints(z+e*v)-co.constraints(z-e*v))/(2*e) for v in basis],axis=1)
    check=dict(objective_max_error=float(np.max(np.abs(grad-fd))),constraints_max_error=float(np.max(np.abs(cg-cf))))
    print('GRAD',check,flush=True);assert max(check.values())<1e-6
    data=dict(config=vars(a),gradient_check=check,baseline=co.report(np.zeros(8)),runs=[]);rng=np.random.default_rng(a.seed)
    for k in range(a.starts):
        start=np.zeros(8) if k==0 else rng.normal(0,.015,size=8)
        res=minimize(co.objective,start,jac=True,method='SLSQP',bounds=[(-a.bound,a.bound)]*8,constraints={'type':'ineq','fun':co.constraints,'jac':lambda z:co.constraints(z,True)},options=dict(maxiter=a.maxiter,ftol=1e-13))
        r=co.report(res.x);r.update(start=start.tolist(),status=int(res.status),message=str(res.message),nit=int(res.nit),nfev=int(res.nfev),minimum_constraint=float(co.constraints(res.x).min()));data['runs'].append(r);Path(a.output).write_text(json.dumps(data,indent=2));print('RESULT',r['status'],'S/U',len(r['S']),len(r['U']),'P',r['P'][0]['depth'] if r['P'] else 0,'min',r['minimum_constraint'],'b',r['b'],'nit',r['nit'],flush=True)
    Path(a.output).write_text(json.dumps(data,indent=2))
if __name__=='__main__':main()
```

## File: projective_joint.py
```python
#!/usr/bin/env python3
"""Free-root joint projective/affine numerical search, complete bounded producer."""
import json,argparse
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from metric_search import geometry
from projective_metric import Dynamic

class Joint(Dynamic):
    def __init__(self,geo,rho=.9,tau=1e-5,weights=(1.,1.)):
        super().__init__(geo,rho);self.tau=tau;self.weights=weights
    def objective(self,t):
        p,q=self.calc(t)[-2:];loss=0.;grad=np.zeros(8)
        for rr,w in zip((p,q),self.weights):
            best,der,root,pick=rr;v=np.minimum(best-self.tau,0);v[root]=0;loss+=w*(v@v);grad+=2*w*(v@der)
        return loss,grad

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--starts',type=int,default=10);ap.add_argument('--maxiter',type=int,default=600);ap.add_argument('--bound',type=float,default=3);ap.add_argument('--rho',type=float,default=.9);ap.add_argument('--tau',type=float,default=1e-5);ap.add_argument('--weights',type=float,nargs=2,default=[1,1]);ap.add_argument('--seed',type=int,default=280106);ap.add_argument('--warm');ap.add_argument('--output',default='projective_joint.json');a=ap.parse_args();obj=Joint(geometry(),a.rho,a.tau,tuple(a.weights));rng=np.random.default_rng(a.seed);starts=[np.zeros(8)]
    if a.warm:starts.extend(np.array(r['theta']) for r in json.loads(Path(a.warm).read_text())['runs'][:1])
    while len(starts)<a.starts:starts.append(np.clip(rng.normal(0,[.05,.2,.7,1.5][len(starts)%4],size=8),-a.bound,a.bound))
    data=dict(config=vars(a),runs=[])
    for s in starts[:a.starts]:
        res=minimize(obj.objective,s,jac=True,method='SLSQP',bounds=[(-a.bound,a.bound)]*8,options=dict(maxiter=a.maxiter,ftol=1e-14))
        r=obj.report(res.x);r.update(start=s.tolist(),loss=float(obj.objective(res.x)[0]),nit=int(res.nit),nfev=int(res.nfev),status=int(res.status),message=str(res.message));data['runs'].append(r);Path(a.output).write_text(json.dumps(data,indent=2));print('RUN',len(data['runs']),'loss',r['loss'],'S/U',len(r['S']),len(r['U']),'Pmax',r['P'][0]['depth'] if r['P'] else 0,'Qmax',r['Q'][0]['depth'] if r['Q'] else 0,'nit',r['nit'],flush=True)
    print('END_NO_EXACT_CERTIFICATE',flush=True)
if __name__=='__main__':main()
```

## File: shared_face_bridge.py
```python
#!/usr/bin/env python3
"""Finite physical point additions along the current common U-carrier plane.
All tests are floating nominations; facet grouping tolerance is explicit.
"""
import argparse,json,itertools
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from metric_search import geometry

def roots(X):
    scores=X@X.T-np.sum(X*X,axis=1)[:,None];np.fill_diagonal(scores,-np.inf)
    return np.where(np.max(scores,axis=1)<0)[0]

def audit_points(X):
    hull=ConvexHull(X);vol=0.;M=np.zeros(3)
    groups=[];ids=[]
    for t,eq in zip(hull.simplices,hull.equations):
        a,b,c=X[t];w=np.dot(a,np.cross(b,c))/6
        if np.dot(np.cross(b-a,c-a),eq[:3])<0:w=-w
        assert w>0;vol+=w;M+=w*(a+b+c)/4
        k=next((j for j,q in enumerate(groups) if np.max(np.abs(q-eq))<1e-8),len(groups))
        if k==len(groups):groups.append(eq);ids.append(set())
        ids[k].update(map(int,t))
    g=M/vol;N=np.array(groups);Z=N[:,:3]/(-N[:,3]-N[:,:3]@g)[:,None]
    active=sorted(hull.vertices);P=X[active]-g
    E=set();faces=[]
    for ss,eq in zip(ids,groups):
        ss=sorted(ss);c=X[ss].mean(axis=0);u=X[ss[0]]-c;u/=np.linalg.norm(u);v=np.cross(eq[:3],u)
        ss=sorted(ss,key=lambda i:np.arctan2((X[i]-c)@v,(X[i]-c)@u));faces.append(ss)
        E.update(tuple(sorted((ss[i],ss[(i+1)%len(ss)]))) for i in range(len(ss)))
    assert len(active)-len(E)+len(groups)==2
    referenceZ=N[:,:3]/(-N[:,3])[:,None]
    return dict(V=len(active),E=len(E),F=len(groups),volume=float(vol),centroid=g.tolist(),S=roots(Z).tolist(),U=[int(active[i]) for i in roots(P)],referenceS=roots(referenceZ).tolist(),referenceU=[int(active[i]) for i in roots(X[active])],maximum_facet_size=max(map(len,faces)),facets=[list(map(int,f)) for f in faces])

def bridge(geo,n,orientation,height=1.,bend=0.):
    P=geo['P'];q=geo['Y'][47];normal=q/np.linalg.norm(q);foot=q/(q@q);u=P[43]-foot;v=P[57]-foot
    ru,rv=np.linalg.norm(u),np.linalg.norm(v);e1=u/ru;phi=np.arccos(np.clip(u@v/ru/rv,-1,1));e2=(v/rv-np.cos(phi)*e1)/np.sin(phi)
    angle=phi if orientation==1 else phi-2*np.pi
    t=np.arange(1,n)/n;r=ru*(rv/ru)**t
    nodes=foot+np.array([r0*(np.cos(angle*t0)*e1+np.sin(angle*t0)*e2) for r0,t0 in zip(r,t)])
    # Tangential curvature is fixed; height may retract interior nodes only.
    nodes-=((1-height)*np.sin(np.pi*t)**2)[:,None]*foot
    nodes+=bend*np.sin(np.pi*t)[:,None]*(P[57]-P[43])
    path=np.vstack((P[43],nodes,P[57]));scores=np.sum(path[:-1]*(path[1:]-path[:-1]),axis=1)
    return nodes,float(scores.min()),dict(angle=float(angle),tangent_ratio=float(rv/ru),min_old_S_plane_slack=float(np.min(1-nodes@geo['Y'][15])))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='shared_face_bridge.json');a=ap.parse_args();G=geometry();out=[]
    for n,orientation,height in itertools.product([10,12,14,16,20,24,30,36],[1,-1],[1.,.95,.8,.5,0.,-1.]):
        nodes,score,meta=bridge(G,n,orientation,height)
        try:r=audit_points(np.vstack((G['P'],nodes)));r.update(n=n,orientation=orientation,height=height,min_path_score=score,**meta)
        except (ValueError,AssertionError,np.linalg.LinAlgError) as e:r=dict(n=n,orientation=orientation,height=height,error=str(e))
        out.append(r)
        if 'S' in r and (len(r['S'])==1 or len(r['U'])==1 or (len(r['referenceS'])==len(r['referenceU'])==1)):
            print('BRIDGE',n,orientation,height,'V/E/F',r['V'],r['E'],r['F'],'ownS/U',len(r['S']),len(r['U']),'reference',len(r['referenceS']),len(r['referenceU']),'min',score,flush=True)
    Path(a.output).write_text(json.dumps(dict(facet_group_tolerance=1e-8,results=out),indent=2));print('TOTAL',len(out),'own110',sum('S'in r and len(r['S'])==len(r['U'])==1 for r in out),flush=True)
if __name__=='__main__':main()
```
