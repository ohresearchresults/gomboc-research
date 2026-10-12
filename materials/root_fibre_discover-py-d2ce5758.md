# material-d2ce5758acd2

AI research material

---

#!/usr/bin/env python3
"""Floating locator, NOT an acceptance proof.

Run in a directory containing root_fibre_exact.py:
OPENBLAS_NUM_THREADS=1 python -B root_fibre_discover.py

Inputs and non-default parameters are literal below. NumPy 2.3.5, SciPy 1.17.0,
SymPy 1.14.0, CPython 3.13.5 were used for the recorded discovery. The immutable
accepted construction is the rational control in root_fibre_exact.py, which has
no NumPy or SciPy dependency. Half-space intersections and stationary tests in
THIS file are only numerical discovery aids, never rigorous infeasibility.
"""
from __future__ import annotations
from itertools import combinations
from pathlib import Path
import json
import numpy as np
from scipy.optimize import linprog
from scipy.linalg import null_space
from scipy.spatial import HalfspaceIntersection,QhullError
from root_fibre_exact import build_geometry
GEO=build_geometry()
NAMES=GEO['names']
ROWS=np.array(GEO['E'],dtype=float)
ROWS/=np.linalg.norm(ROWS,axis=1)[:,None]
BOUNDS=np.array(GEO['exact_bounds'],dtype=float)
H=np.array([[0.,0.,1.,0.],[0.,-2.,0.,0.],[1.,0.,0.,0.],[0.,0.,0.,0.]])
l=np.array([0.,0.,0.,-1.])
def q(x):return x[0]*x[2]-x[1]*x[1]-x[3]
BOX=[]
for j,(lo,hi) in enumerate(BOUNDS):
    r=np.zeros(5);r[j]=1.;r[4]=-lo;BOX.append(r)
    r=np.zeros(5);r[j]=-1.;r[4]=hi;BOX.append(r)
BOX=np.array(BOX)

def extrema(packet):
    R=np.vstack([sgn*ROWS[j] for j,sgn in packet]+[r for r in BOX])
    norms=np.linalg.norm(R[:,:4],axis=1)
    R=R[norms>1e-12];norms=norms[norms>1e-12]
    R=R/norms[:,None]
    A=-R[:,:4];b=R[:,4]
    lc=np.zeros(5);lc[4]=-1
    res=linprog(lc,A_ub=np.column_stack((A,np.ones(len(A)))),b_ub=b,bounds=[(None,None)]*4+[(0,None)],method='highs')
    if not res.success or res.x[-1]<1e-9:return None
    try:
        hs=HalfspaceIntersection(np.column_stack((A,-b)),res.x[:4])
    except QhullError:return None
    vals=[(q(x),x) for x in hs.intersections]
    faces=set()
    for x in hs.intersections:
        active=np.where(np.abs(A@x-b)<1e-6*(1+np.abs(b)))[0].tolist()
        for k in (1,2,3):
            for I in combinations(active,k):faces.add(I)
    for I in faces:
        C=A[list(I)]
        if np.linalg.matrix_rank(C,tol=1e-9)<len(I):continue
        N=null_space(C,rcond=1e-10)
        E=np.vstack((C,N.T@H));r=np.r_[b[list(I)],-N.T@l]
        sol,_,rank,_=np.linalg.lstsq(E,r,rcond=1e-10)
        if np.linalg.norm(E@sol-r)>1e-6*(1+np.linalg.norm(r)):continue
        if rank<4:
            sr=linprog(np.zeros(4),A_ub=A,b_ub=b,A_eq=E,b_eq=r,bounds=[(None,None)]*4,method='highs')
            if not sr.success:continue
            sol=sr.x
        if np.all(A@sol<=b+1e-7*(1+abs(b))):vals.append((q(sol),sol))
    return min(vals,key=lambda z:z[0]),max(vals,key=lambda z:z[0]),len(hs.intersections),len(faces)


rootH=np.array(GEO['H'],float);Si=np.array(GEO['Sigma'].inv(),float);Sigma=np.array(GEO['Sigma'],float)
rootHi=np.linalg.inv(rootH);B=rootH.T@Si@rootH;Gref=B[:2,:2]/B[2,2]
e,U=np.linalg.eigh(Gref);root=(U*np.sqrt(e))@U.T

def physical(G):
    M=rootHi.T@np.block([[G,np.zeros((2,1))],[np.zeros((1,2)),np.ones((1,1))]])@rootHi
    ev=np.linalg.eigvals(Sigma@M)
    return M,max(ev)/min(ev)
def hullpass(M,N):
    A=M/np.trace(Sigma@M);B=Si@N@Si/np.trace(Si@N)
    mats=[26*Si/31-A-B,5*A+B-30*Si/31,A+5*B-30*Si/31]
    return all(min(np.linalg.eigvalsh(X))>1e-6 for X in mats)
rng=np.random.default_rng(943012)
for trial in range(250):
    eig=np.exp(rng.uniform(-1.5,1.5,size=2));t=rng.uniform(-np.pi,np.pi)
    O=np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
    G=root@(O*eig)@O.T@root
    ratio=np.exp(rng.uniform(-1.5,1.5));delta=np.linalg.det(G)*ratio
    M,k0=physical(G);Mr,k1=physical(ratio*G)
    if max(k0,k1)>35 or not hullpass(M,np.linalg.inv(Mr)):continue
    x=np.array([G[0,0],G[0,1],G[1,1],delta])
    if not all(lo<xj<hi for xj,(lo,hi) in zip(x,BOUNDS)):continue
    val=ROWS[:,:4]@x+ROWS[:,4]
    # Start with positive escape arrows; then use the entire strict chamber if needed.
    for positive in (True,False):
        packet=[(i,1 if y>0 else -1) for i,y in enumerate(val) if abs(y)>1e-8 and (y>0 or not positive)]
        e=extrema(packet)
        if e is None:continue
        if e[0][0]>1e-5 or e[1][0]<-1e-5:
            print('FOUND',trial,'positive',positive,'sample',x.tolist(),'k',k0,k1,'range',e[0][0],e[1][0],flush=True)
            rng.shuffle(packet)
            for it in range(2):
                for pair in packet[:]:
                    pp=packet.copy();pp.remove(pair);ee=extrema(pp)
                    if ee is not None and (ee[0][0]>1e-5 or ee[1][0]<-1e-5):packet=pp;e=ee
            print('PACKET',[(NAMES[i],sgn) for i,sgn in packet],'range',e[0][0],e[1][0],e[2:],flush=True)
            out=dict(trial=trial,sample=x.tolist(),packet=[(int(i),int(s)) for i,s in packet],names=[(NAMES[i],int(s)) for i,s in packet],min=(float(e[0][0]),e[0][1].tolist()),max=(float(e[1][0]),e[1][1].tolist()),k=[float(k0),float(k1)],positive=positive)
            Path('root_fibre_discovery.json').write_text(json.dumps(out,indent=2)+'\n')
            raise SystemExit
    if trial%10==0:print('trial',trial,'k',k0,k1,flush=True)
print('none')
