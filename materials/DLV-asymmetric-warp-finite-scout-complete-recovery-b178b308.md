# material-b178b30817fb

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# DLV asymmetric latitude warp: complete numerical method, frozen roots, and finite negative ledger
This capsule preserves a completed bounded numerical experiment, not an exact body, weak-equilibrium certificate, or family exclusion. It complements exact pole proof parts [internal-source-reference] and [internal-source-reference] but does not need them to run. Every computational source/input needed below is literal here. CPython3.13.5, NumPy2.3.5, SciPy1.17.0, SymPy1.14.0. Binary64 numerical trigonometry/hulls are not exact geometric proof; byte-identical outputs were observed on clean replay in this environment, not promised for arbitrary numerical libraries.

## Scientific result and scope
Thirty128x128 smooth-volume quadrature roots use d in[.05,.1,.2,.3,.4],warp in[.35,.4,.5,.6,.75,1]. Finer256x256 residuals range6.43273325046064e-11 to2.17139276024539e-5, not exact zero. These are distinct from the older192/256->384/512 DLV quadrature experiment. Six hundred finite reflection-symmetric hulls use each frozen root, nlat7/9/10/15/19,nph8 forfirstthree/4forlasttwo,top multipliers1/1.01/1.05/1.15,otherdefaults below. Each uses its numerical ACTUAL filled centroid, merged maximal facet planes and true edges; root decisions have tolerance1e-9. No sample has110. min(S+U,S,U)=(14,5,9); individualminS=minU=5; maximum observedE198. Both(5,9,12) and(9,5,12) occur at total14. Passing a numerical tolerance is not absence of weak equilibria.
A20001point scan of both axial meridians reports some negative curvature numerator in26/30 parameter pairs. This is a finite necessary-condition diagnostic, not a global convexity proof. The separate exact box certificate establishes only its own explicitly stated continuous box.
Representative numerical finite minima: d.2,warp1,a.05536296628904006,nlat15,nph4,top1.01 or1.05 gives41/80/41,5/9/12;top1.15 gives37/72/37,5/9/12. Other14total examples at d.3/warp1 andd.4/warp.75or1 have9/5/12. None is promoted as an exact construction.

## Recovery and output identities
Save the next three source blocks respectively as freeze_roots.py,scout.py,curvature.py in one directory. Run:
python -B freeze_roots.py
python -B scout.py finite
python -B curvature.py
The original root search is runnable as python -B scout.py roots, but finite replay intentionally uses the exact frozen binary64 input values, not a fresh optimizer/root-finder output.
Expected input smooth_roots.json4124B SHA25685b4114929c66c1128dd59b07d40aa305aa8c28c41cd4f73be51c67416681923.
Actual scout.py5190B SHA256baa2359c8277cda3e081d84cf11b6ff603272ec85ab0d3cfcbe5cf0e5d9fdaa4.
Actual curvature.py1317B SHA25677082b77ad5926b5522f8d3f8390e563d6994d75c8ddf83978664e733db9c34f.
Expected finite_trials.json135775B SHA25671d1d93d966f19876e130f83c6b1a7140ae2405394a6b5e1fec9f2a87caf3ea8,marker FINITE_TRIALS 600 (14, 5, 9).
Expected curvature_trials.json18714B SHA256e7a8f4ea246f2ef079505a41f8692a2b22e63e90ccfb83571d79afbceed238bc.
The exact file sizes/hashes above were observed on original and clean replay. Earlier ephemeral summaries listing other source sizes/hashes were erroneous and are not evidence.

### freeze_roots.py
```python
import json,hashlib
from pathlib import Path
pairs=[
(.012760797080339196,9.589931279227883e-6),(.018619957411149878,1.639730660194035e-6),(.030878042755137176,4.441847562783366e-8),(.04107004668051146,2.553775215969564e-9),(.05071492196334084,1.9948184041827266e-10),(.055613732434082255,6.43273325046064e-11),
(.012401768454059816,1.613862637703304e-5),(.01817675056235759,2.7519458042262776e-6),(.030420061788781816,7.863923349317922e-8),(.04071236264740268,5.064318661282346e-9),(.05050781032009283,4.602512117370033e-10),(.055562549136198194,1.6705068983197775e-10),
(.011718287620904324,2.17139276024539e-5),(.017304671757133214,3.928053906158617e-6),(.02946201632877198,1.730795741991557e-7),(.03992287082348141,1.5828620258497915e-8),(.050002982681175374,1.7344119813406974e-9),(.05536296628904006,6.485547157244119e-10),
(.011099820211971452,2.0854157384250808e-5),(.016482132875193064,4.9391432176146785e-6),(.028483413727254443,4.325677578345987e-7),(.03906185969563003,4.7196904914956094e-8),(.04939591979295409,5.157420703701226e-9),(.055047630136450344,1.787326218260664e-9),
(.010558946524457095,1.8074881239710568e-5),(.015735841911605788,7.4309285646204645e-6),(.02752576739080026,1.0514000059241292e-6),(.03816634535505968,1.189573950212267e-7),(.04871499876131283,1.2410058478982871e-8),(.05463919326015887,3.980485875517347e-9)]
rows=[]
for i,d in enumerate([.05,.1,.2,.3,.4]):
 for j,b in enumerate([.35,.4,.5,.6,.75,1.]):
  rows.append({'d':d,'warp':b,'roots':[list(pairs[6*i+j])]})
raw=json.dumps(rows,indent=2).encode();assert len(raw)==4124
assert hashlib.sha256(raw).hexdigest()=='85b4114929c66c1128dd59b07d40aa305aa8c28c41cd4f73be51c67416681923'
Path('smooth_roots.json').write_bytes(raw)
print('DLV_SCOUT_FROZEN_ROOTS_PASS',len(rows),len(raw))
```

### scout.py
```python
"""Finite D2 radial scouting with asymmetric latitude warp; numerical, not proof.
Python 3.13.5 / NumPy 2.3.5 / SciPy 1.17.0. CLI modes defined below.
"""
import json,sys,time,math
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss

def F(a,x):
    return (a*x*x+(1-a)*(1-x)**2*a*x/(a+x))/(a*x+(1-a)*(1-x)**2)

def rho(a,th,ph,warp=1.):
    x=th/np.pi+.5
    xx=warp*x/(1+(warp-1)*x)
    f=np.pi*F(a,xx)-np.pi/2
    g=-np.pi*F(a,1-xx)+np.pi/2
    u=np.cos(ph)**2*np.cos(f)**2
    v=np.sin(ph)**2*np.cos(g)**2
    return (u*np.sin(f)+v*np.sin(g))/(u+v)

def surface(a,d,warp,th,ph):
    r=1+d*rho(a,np.asarray(th),np.asarray(ph),warp)
    return np.stack([r*np.cos(th)*np.cos(ph),r*np.cos(th)*np.sin(ph),r*np.sin(th)],-1)

def smoothmass(a,d,warp,nz=128,nph=128):
    z,w=leggauss(nz)
    ph=(np.arange(nph)+.5)*2*np.pi/nph
    r=1+d*rho(a,np.arcsin(z[:,None]),ph[None,:],warp)
    V=(2*np.pi/3)*np.dot(w,np.mean(r**3,axis=1))
    M=(2*np.pi/4)*np.dot(w*z,np.mean(r**4,axis=1))
    return M/V

def roots(d,warp):
    ax=np.geomspace(.00001,.99999,32)
    out=[]
    for aa,bb in zip(ax,ax[1:]):
        fa,fb=smoothmass(aa,d,warp),smoothmass(bb,d,warp)
        if fa*fb<0:
            a=brentq(lambda a:smoothmass(a,d,warp),aa,bb,xtol=1e-12)
            out.append([a,smoothmass(a,d,warp,256,256)])
    return out

def audit(P,tol=1e-9):
    P=np.asarray(P,float);h=ConvexHull(P)
    tris=h.simplices.copy()
    for k,t in enumerate(tris):
        if np.dot(np.cross(P[t[1]]-P[t[0]],P[t[2]]-P[t[0]]),h.equations[k,:3])<0:tris[k,[1,2]]=tris[k,[2,1]]
    vol=np.einsum('ij,ij->i',P[tris[:,0]],np.cross(P[tris[:,1]],P[tris[:,2]]))/6
    V=np.sum(vol); c=np.sum(vol[:,None]*np.sum(P[tris],axis=1)/4,axis=0)/V
    active=sorted(h.vertices.tolist()); X=P-c
    # Maximal face grouping uses plane equality only as a numerical scout.
    faces=[];norms=[];hs=[];towner=[]
    for t,e in zip(tris,h.equations):
        own=next((j for j,(n,b) in enumerate(zip(norms,hs)) if np.linalg.norm(n-e[:3])<tol and abs(b+e[3])<tol),None)
        if own is None:
            own=len(faces);faces.append(set());norms.append(e[:3]);hs.append(-e[3])
        faces[own].update(t);towner.append(own)
    es={}
    for t,own in zip(tris,towner):
        for i,j in [(t[0],t[1]),(t[1],t[2]),(t[2],t[0])]:es.setdefault(tuple(sorted([int(i),int(j)])),set()).add(own)
    es={e:sorted(v) for e,v in es.items() if len(v)==2}
    norms=np.array(norms);H=np.array(hs)-norms@c
    Q=norms/H[:,None]
    pmax={i:-np.inf for i in active};qmax=np.full(len(faces),-np.inf)
    for (i,j),(k,l) in es.items():
        pmax[i]=max(pmax[i],float(X[i]@(X[j]-X[i])))
        pmax[j]=max(pmax[j],float(X[j]@(X[i]-X[j])))
        qmax[k]=max(qmax[k],float(Q[k]@(Q[l]-Q[k])))
        qmax[l]=max(qmax[l],float(Q[l]@(Q[k]-Q[l])))
    u=[i for i,v in pmax.items() if v<=tol]
    s=np.flatnonzero(qmax<=tol).tolist()
    ss=[]
    for (i,j),(k,l) in es.items():
        dd=X[j]-X[i]; t=-X[i]@dd/(dd@dd)
        if 0<t<1:
            w=X[i]+t*dd
            coeff=np.linalg.lstsq(norms[[k,l]].T,w,rcond=None)[0]
            if np.min(coeff)>tol:ss.append([i,j])
    return dict(V=len(active),E=len(es),F=len(faces),volume=V,centroid=c.tolist(),S=s,U=u,H=ss,physical_max=pmax,polar_max=qmax.tolist(),facets=[sorted(f) for f in faces],edges=[[i,j,k,l] for (i,j),(k,l) in es.items()],extreme=active)

def makepoints(a,d,warp,nlat=9,nph=8,top=1.,bottom=-1.,shift=0.,spread=1.):
    # nlat complete non-axial rings, nph divisible by 4; C2 reflections are exact.
    theta=np.linspace(-np.pi/2,np.pi/2,nlat+2)[1:-1]
    theta=np.arcsin(np.clip(spread*np.sin(theta)+shift,-.999,.999))
    ph=(np.arange(nph//4)+.5)*2*np.pi/nph
    quarter=surface(a,d,warp,theta[:,None],ph[None,:]).reshape(-1,3)
    P=np.vstack([quarter*sg for sg in [[1,1,1],[-1,1,1],[-1,-1,1],[1,-1,1]]]+[[[0,0,(1+d)*top]]])
    if bottom!=-1:
        P=np.vstack([P,[[0,0,bottom]]])
    return P

if __name__=='__main__':
    if sys.argv[1]=='roots':
        rows=[]
        for d in [.05,.1,.2,.3,.4]:
            for b in [.35,.4,.5,.6,.75,1.]:
                rs=roots(d,b);row={'d':d,'warp':b,'roots':rs};rows.append(row);print(row,flush=True)
        json.dump(rows,open('smooth_roots.json','w'),indent=2)
    elif sys.argv[1]=='finite':
        rows=[]
        for line in json.load(open('smooth_roots.json')):
            for a,res in line['roots']:
                d,b=line['d'],line['warp']
                for nlat in [7,9,10,15,19]:
                    nph=4 if nlat>10 else 8
                    for top in [1.,1.01,1.05,1.15]:
                        P=makepoints(a,d,b,nlat,nph,top)
                        au=audit(P)
                        rec={'a':a,'d':d,'warp':b,'nlat':nlat,'nph':nph,'top':top,'V':au['V'],'E':au['E'],'F':au['F'],'c':au['centroid'][2], 'S':len(au['S']),'U':len(au['U']),'H':len(au['H'])}
                        rows.append(rec)
                        if rec['S']+rec['U']<=10:print(rec,flush=True)
        json.dump(rows,open('finite_trials.json','w'),indent=2)
        print('FINITE_TRIALS',len(rows),min((r['S']+r['U'],r['S'],r['U']) for r in rows))
```

### curvature.py
```python
"""Numerical necessary meridian convexity diagnostic; no interval claims."""
import json
import numpy as np
import sympy as s
from scout import F
x,a=s.symbols('x a',positive=True)
f=(a*x*x+(1-a)*(1-x)**2*a*x/(a+x))/(a*x+(1-a)*(1-x)**2)
fd=s.lambdify((a,x),s.diff(f,x), 'numpy')
fdd=s.lambdify((a,x),s.diff(f,x,2), 'numpy')

def diagnose(a,d,b):
    xx=np.linspace(1e-6,1-1e-6,20001)
    den=1+(b-1)*xx
    w=b*xx/den;wp=b/den**2;wpp=-2*b*(b-1)/den**3/np.pi
    f=np.pi*F(a,w)-np.pi/2
    g=-np.pi*F(a,1-w)+np.pi/2
    fp=fd(a,w)*wp;gp=fd(a,1-w)*wp
    fpp=fdd(a,w)*wp**2/np.pi+fd(a,w)*wpp
    gpp=-fdd(a,1-w)*wp**2/np.pi+fd(a,1-w)*wpp
    ans=[]
    for phi,ff,f1,f2 in [(0.,f,fp,fpp),(np.pi/2,g,gp,gpp)]:
        r=1+d*np.sin(ff);r1=d*np.cos(ff)*f1;r2=d*(-np.sin(ff)*f1**2+np.cos(ff)*f2)
        B=r*r+2*r1*r1-r*r2
        idx=int(np.argmin(B));ans.append({'phi':phi,'theta':float(xx[idx]*np.pi-np.pi/2),'B':float(B[idx]),'r':float(r[idx]),'r1':float(r1[idx]),'r2':float(r2[idx])})
    return ans
rows=[]
for rec in json.load(open('smooth_roots.json')):
    for aa,res in rec['roots']:
        o={**rec,'a':aa,'meridians':diagnose(aa,rec['d'],rec['warp'])}; rows.append(o)
        print(o['a'],o['d'],o['warp'],[v['B'] for v in o['meridians']],flush=True)
json.dump(rows,open('curvature_trials.json','w'),indent=2)
```
