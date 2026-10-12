# material-22a7e81f129b

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Recovery capsule part 1/2: JOINT75_FLOAT_CUTS_AND_ENVELOPE_NOMINATION

Both parts are necessary to recover the complete computational method. These are unencoded literal source files, not a substitute for the separate exact envelope certificate. Save each Python block under its File heading. Part2 contains the independent replay command, all checkpoint parameters, dependency versions, manifests and limitations.

## File: inputs.py
```python
# Literal inputs reproduced from fully read immutable result
# figure-0552, sha256
# ad8dc7c434c78f9d6a7bbd334969fdbfdab83f3a56202484b2698ad9bf1c95d4
import numpy as np
I75 = [
[-11310213,-3802031,232661],[-11269293,-2834032,-2182730],
[-10855182,-2246500,-3911998],[-10128821,-1814868,-5467871],
[-9452382,-6834502,6456555],[-9308206,-1555414,-6662777],
[-8712882,-8006246,8846843],[-8693078,-1373304,-7380329],
[-7797905,-1286403,-8181129],[-6681453,-1307873,-8916622],
[-6352338,2020313,-1146993],[-5892536,2295258,-71116],
[-5592263,2241235,541206],[-5425338,-1474781,-9487378],
[-5280741,2171200,1073969],[-4959361,3312877,-1863739],
[-4453446,1994305,2115702],[-4311479,345947,4048866],
[-4305575,1694912,2608464],[-4237167,1203950,3206121],
[-3820955,4252385,-2139686],[-3661038,4074852,-884602],
[-3623465,-1644023,-10021566],[-3190033,811977,3827673],
[-3155609,4102561,85230],[-3074935,4483432,-2851622],
[-2953571,-1851896,-10161171],[-2718323,668005,3934224],
[-2651732,122199,4295157],[-2302445,4621821,-3324860],
[-2248430,-2037367,-10247983],[-2145336,4388373,461753],
[-1938256,3964861,1093487],[-1561887,3760992,1454978],
[-1502148,-2223378,-10275715],[-1278721,4758931,-3663608],
[-1049751,3727821,1606020],[-740759,-2457388,-10231458],
[-298044,4806779,-3669461],[-159770,3872224,1576892],
[-121991,838112,3483867],[39249,-2666243,-10115526],
[91753,589879,3521150],[725989,729286,3291554],
[822613,-2865673,-9923443],[847151,1601384,2948252],
[1257541,4150503,1429262],[1400720,4852019,-3212547],
[1599055,-3043575,-9655675],[2331916,-2317243,-9420429],
[2351892,-3267823,-9302290],[2947803,5018418,-438633],
[3091632,-3449326,-8871363],[3252567,4572542,973174],
[3518927,-4445832,-8207140],[3801752,-3598386,-8365506],
[3886092,3932529,1241770],[4317265,3420766,1352627],
[4466143,-3720508,-7791824],[4524082,-5334292,-6695320],
[4622668,3053371,1323427],[4905967,2678528,1274548],
[5061533,-3853293,-7158199],[5166891,2298083,1206990],
[5506198,-4926808,-5369878],[5525767,-801605,-6004784],
[5644371,1606910,926729],[6018142,937609,612094],
[6137534,-4326615,-4182924],[6330239,239389,230320],
[6547165,-3582767,-3087182],[6574260,-489010,-228500],
[6738672,-1246564,-776981],[6751376,-2814918,-2197016],
[6805726,-2026966,-1429050]]
A6 = [[54523165,-66300276,-55391279],
[49842012,-91287749,-32456638],[35949856,-110325885,-5024889],
[13236236,-120608734,24070669],[-16841661,-119820327,51618679],
[-51605841,-106402263,74185541]]
P75=np.array(I75,dtype=float)/10**7
A=np.array(A6,dtype=float)/10**8
J19=[22,26,30,34,37,41,44,48,49,50,52,54,55,58,59,62,64,68,70]
```

## File: onecut.py
```python
"""Floating finite-cut experiment; exact certification is a separate step.
No coplanar-facet merging after clipping: old faces are clipped individually,
and the new cap remains one maximal polygon. Generic planes only.
"""
from dataclasses import dataclass
import json
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
from inputs import P75,A

@dataclass
class Body:
    p: np.ndarray
    faces: list
    normals: np.ndarray
    origins: list
    def __post_init__(self):
        self.normals=np.asarray(self.normals,float)
        self.normals/=np.linalg.norm(self.normals,axis=1)[:,None]
        owners={}
        for k,f in enumerate(self.faces):
            for i,j in zip(f,f[1:]+f[:1]):
                owners.setdefault(tuple(sorted((i,j))),[]).append(k)
        assert all(len(x)==2 for x in owners.values())
        self.edges=np.array(list(owners),int)
        self.ef=np.array(list(owners.values()),int)
        assert len(self.p)-len(self.edges)+len(self.faces)==2
        # Positive integration about an interior reference.
        o=self.p.mean(axis=0)
        tris=[]
        for f in self.faces:
            tris.extend([[f[0],f[j],f[j+1]] for j in range(1,len(f)-1)])
        t=self.p[np.array(tris)]
        w=np.einsum('ij,ij->i',t[:,0]-o,np.cross(t[:,1]-o,t[:,2]-o))/6
        if w.min() < -1e-12: raise ValueError('Orientation')
        self.volume=float(w.sum())
        self.moment=np.sum(w[:,None]*(t.sum(axis=1)+o)/4,axis=0)
        self.g=self.moment/self.volume

    @staticmethod
    def hull(p):
        p=np.asarray(p,float); h=ConvexHull(p)
        keep=sorted(map(int,h.vertices)); mp={v:i for i,v in enumerate(keep)}
        fs=[]
        for f,n in zip(h.simplices,h.equations[:,:3]):
            f=list(f)
            if np.dot(np.cross(p[f[1]]-p[f[0]],p[f[2]]-p[f[0]]),n)<0:
                f[1],f[2]=f[2],f[1]
            fs.append([mp[i] for i in f])
        return Body(p[keep],fs,h.equations[:,:3],keep)

    def clip(self,q,c):
        # Retain q.(x-c)<=1. Original facet polygons persist exactly by incidence.
        q=np.asarray(q,float); c=np.asarray(c,float)
        s=(self.p-c)@q-1
        keep=np.flatnonzero(s<=0)
        if len(keep)==len(self.p): return self
        if len(keep)==0: raise ValueError('Empty clip')
        out=[self.p[i] for i in keep]; orig=[self.origins[i] for i in keep]
        mp={int(i):k for k,i in enumerate(keep)}; em={}
        for i,j in self.edges:
            if s[i]*s[j]<0:
                t=s[i]/(s[i]-s[j]); em[(i,j)]=len(out)
                out.append(self.p[i]+t*(self.p[j]-self.p[i])); orig.append([int(i),int(j)])
        fs=[]; ns=[]
        for f,n in zip(self.faces,self.normals):
            ff=[]
            for i,j in zip(f,f[1:]+f[:1]):
                if s[i]<=0: ff.append(mp[i])
                if s[i]*s[j]<0: ff.append(em[tuple(sorted((i,j)))])
            if len(ff)>=3: fs.append(ff); ns.append(n)
        if not em: raise ValueError('Nongeneric plane')
        # Sort cap round its outward normal, not independent coordinate rounding.
        pp=np.asarray(out); cap=list(em.values()); n=q/np.linalg.norm(q)
        e=np.eye(3)[np.argmin(abs(n))]; u=np.cross(e,n);u/=np.linalg.norm(u); v=np.cross(n,u)
        ctr=pp[cap].mean(axis=0)
        cap=sorted(cap,key=lambda i:np.arctan2(np.dot(pp[i]-ctr,v),np.dot(pp[i]-ctr,u)))
        fs.append(cap); ns.append(n)
        return Body(pp,fs,np.array(ns),orig)

    def census(self,c=None):
        if c is None:c=self.g
        x=self.p-c; ns=self.normals
        S=[]; U=[]; H=[]; margins=[]
        for k,f in enumerate(self.faces):
            vv=[]
            for i,j in zip(f,f[1:]+f[:1]):
                inward=np.cross(ns[k],self.p[j]-self.p[i]);inward/=np.linalg.norm(inward)
                vv.append(np.dot(inward,c-self.p[i]))
            if min(vv)>0:S.append(k)
            margins.extend(vv)
        nb=[[] for _ in self.p]
        for i,j in self.edges: nb[i].append(j);nb[j].append(i)
        for i in range(len(x)):
            vv=[-np.dot(x[i],self.p[j]-self.p[i])/np.linalg.norm(self.p[j]-self.p[i]) for j in nb[i]]
            if min(vv)>0:U.append(i)
            margins.extend(vv)
        for (i,j),(f,g) in zip(self.edges,self.ef):
            d=self.p[j]-self.p[i];dd=d@d;t=-x[i]@d/dd
            z=x[i]+t*d;n=ns[f];m=ns[g];ab=n@m
            alpha=(z@n-ab*(z@m))/(1-ab*ab); beta=(z@m-ab*(z@n))/(1-ab*ab)
            if min(t,1-t,alpha,beta)>0:H.append([int(i),int(j)])
            margins.extend([t,1-t,alpha,beta])
        return dict(V=len(x),E=len(self.edges),F=len(self.faces),C=2*len(self.edges),
                    S=len(S),U=len(U),H=len(H),stable=S,unstable=U,saddles=H,
                    min_abs_primitive=float(np.min(np.abs(margins))),
                    volume=self.volume,centroid=self.g.tolist())

    def surface_hessian(self,q,c):
        f=self.faces[-1]; pts=self.p[f]-c; u=pts[0]; H=np.zeros((3,3))
        for j in range(1,len(f)-1):
            vv=np.array([u,pts[j],pts[j+1]])
            ar=np.linalg.norm(np.cross(vv[1]-vv[0],vv[2]-vv[0]))/2
            sm=vv.sum(axis=0)
            H+=ar*(np.outer(sm,sm)+vv.T@vv)/12
        return H/np.linalg.norm(q)


def centercut(O,c,q0=None):
    c=np.asarray(c,float)
    def fun(q):
        K=O.clip(q,c); rel=K.moment-K.volume*c
        return K.volume-q@rel,-rel
    if q0 is None: q0=np.zeros(3)
    r=minimize(fun,q0,jac=True,method='BFGS',options=dict(gtol=1e-11,maxiter=250))
    q=r.x
    for _ in range(20):
        K=O.clip(q,c); rel=K.moment-K.volume*c
        if np.linalg.norm(rel)<1e-13:break
        Hess=K.surface_hessian(q,c)
        step=np.linalg.solve(Hess,rel)
        value=K.volume-q@rel
        for k in range(40):
            trial=q+step/2**k
            v,_=fun(trial)
            if v <= value+1e-14:
                q=trial;break
        else:break
    return q,O.clip(q,c),r

if __name__=='__main__':
    O=Body.hull(np.vstack((P75,A))); K=Body.hull(P75)
    report={'parent':K.census(),'bridge':O.census(),'cuts':[]}
    for name,B,c in [('bridge_old',O,K.g),('bridge_simple',O,[.4,.1,-.3]),('primary_simple',K,[.55,-.27,-.53])]:
        q,T,r=centercut(B,c)
        rec=dict(name=name,target=np.asarray(c).tolist(),q=q.tolist(),residual=float(np.linalg.norm(T.g-c)),census=T.census(),cap_stable=len(T.faces)-1 in T.census()['stable'],
                 removed_old=[i for i,p in enumerate(B.p) if (p-c)@q>1],origins=T.origins)
        report['cuts'].append(rec)
        print(json.dumps({k:v for k,v in rec.items() if k!='origins'}))
    with open('onecut_baselines.json','w') as f:json.dump(report,f,indent=2)
    print('FLOAT_ONECUT_BASELINES_FINISHED_NO_EXACT_CLAIM')
```
