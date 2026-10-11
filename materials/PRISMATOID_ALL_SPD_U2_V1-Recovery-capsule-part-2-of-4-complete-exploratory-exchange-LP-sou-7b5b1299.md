# material-7b5b129920f7

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Exploratory exchange-LP for all-metric certificates. Numeric discovery only;
accepted rows must pass the exact coefficient test. No geometry conclusion from failure.
CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0.
"""
from cap_geometry import *
from spectral_family import FACETS, EDGES, vertices, T
import sympy as sp
import numpy as np
from scipy.optimize import linprog
from pathlib import Path
from functools import reduce
from math import comb,gcd,lcm
import argparse,time
ARCS=sorted((i,j) for i,j in EDGES for i,j in ((i,j),(j,i)))

def coefficients():
    D=105-2*T
    g=sp.Matrix([(-2*T*T+15*T+133)/(4*D),(2*T+105)/(2*D),5*(215-6*T)/(8*D)])
    vv=list(map(sp.Matrix,vertices(T))); W=[(8*D*(v-g)).applyfunc(sp.cancel)for v in vv]
    out=[]
    for i,j in ARCS:
        e=vv[j]-vv[i];A=-(W[i]*e.T+e*W[i].T)
        pp=[A.applyfunc(lambda v:sp.Poly(v,T).nth(d)) for d in range(4)]
        bb=[]
        for k in range(4):
            C=sum((pp[d]*sp.Rational(comb(k,d),comb(3,d))*sp.Rational(1,2)**d for d in range(k+1)),sp.zeros(3))
            bb.append(tuple(tuple(Q(x)for x in C.row(a))for a in range(3)))
        out.append(bb)
    return out

def trees():
    E=sorted(EDGES);out=[]
    for ee in combinations(E,9):
        adj=[[]for _ in range(10)]
        for a,b in ee:adj[a].append(b);adj[b].append(a)
        seen={0};stack=[0]
        while stack:
            a=stack.pop()
            for b in adj[a]:
                if b not in seen:seen.add(b);stack.append(b)
        if len(seen)!=10:continue
        for root in range(10):
            parent={root:root};stack=[root]
            while stack:
                a=stack.pop()
                for b in adj[a]:
                    if b not in parent:parent[b]=a;stack.append(b)
            ids=tuple(sorted(ARCS.index((i,j))for i,j in parent.items()if i!=j))
            out.append((sum(1<<i for i in ids),root,ids))
    assert len(set(t[0]for t in out))==len(out)
    return out

def pd(C):
    return C[0][0]>0 and C[0][0]*C[1][1]-C[0][1]**2>0 and det(*C)>0

def exactrow(ids,lam,CC):
    for den in (10,30,100,300,1000,10000,1000000):
        ww=[Q(float(x)).limit_denominator(den) if x>1e-9 else Q(0)for x in lam]
        if min(ww)<0:continue
        dd=lcm(*(w.denominator for w in ww)); nums=[int(w*dd)for w in ww]
        gg=reduce(gcd,nums);nums=[n//gg for n in nums] if gg else nums
        row=[(i,w)for i,w in zip(ids,nums)if w]
        if not row:continue
        good=True
        for k in range(4):
            C=ZMAT
            for i,w in row:C=matadd(C,matscale(w,CC[i][k]))
            if not pd(C):good=False;break
        if good:return row
    return None

def solve(ids,CC, maxiter=100):
    C=np.array([CC[i]for i in ids],float)
    vectors=[np.eye(3)[i]for i in range(3)]
    for i,j in combinations(range(3),2):
        for s in (-1,1):
            v=np.zeros(3);v[i]=1;v[j]=s;vectors.append(v/np.linalg.norm(v))
    rows=[]
    for k in range(4):
        for v in vectors:rows.append(list(-np.einsum('i,aij,j->a',v,C[:,k],v))+[1.])
    n=len(ids);cost=[0.]*n+[-1.]
    for iteration in range(maxiter):
        lp=linprog(cost,A_ub=rows,b_ub=np.zeros(len(rows)),A_eq=[[1.]*n+[0.]],b_eq=[1.],bounds=[(0,None)]*n+[(None,None)],method='highs')
        if not lp.success:return None,('lp_failure',lp.message)
        lam=lp.x[:n];mu=lp.x[-1]
        if mu<=1e-8:return None,('coefficient_cone_no_PD',float(mu))
        mat=np.einsum('a,akij->kij',lam,C);new=[]
        low=1e100
        for k,Qm in enumerate(mat):
            eig,V=np.linalg.eigh(Qm);low=min(low,eig[0])
            if eig[0]<max(1e-7,mu*(1-1e-5)):
                v=V[:,0];new.append(list(-np.einsum('i,aij,j->a',v,C[:,k],v))+[1.])
        if low>max(1e-7,mu/10):
            exact=exactrow(ids,lam,CC)
            if exact:return exact,('PD_exact',float(low),iteration)
        if not new:return None,('rounding_fail',float(low),float(mu))
        rows.extend(new)
    return None,('iteration_limit',)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--limit',type=int,default=100000);ap.add_argument('--seconds',type=float,default=40);ap.add_argument('--output',default='joint_metric_probe.json');args=ap.parse_args()
    CC=coefficients();alltrees=trees();start=time.time();certs=[];fail=[]
    remaining=alltrees[:];solves=0
    while remaining and solves<args.limit and time.time()-start<args.seconds:
        mask,root,ids=remaining[0];solves+=1
        row,info=solve(ids,CC)
        if row:
            cm=sum(1<<i for i,w in row);old=len(remaining);remaining=[t for t in remaining if t[0]&cm!=cm]
            certs.append(dict(row=row,coverage=old-len(remaining),info=info))
        else:
            fail.append(dict(root=root,ids=ids,info=info));remaining=remaining[1:]
        if solves%20==0:print('solves',solves,'certificates',len(certs),'unprocessed',len(remaining),'failed',len(fail),flush=True)
    result=dict(identity='TWO_SINK_PRISMATOID_ALL_SPD_PRIMAL_PROBE_V1',arcs=ARCS,total_rooted_trees=len(alltrees),certificates=certs,failed=fail,remaining=[dict(root=r,ids=i)for m,r,i in remaining],elapsed=time.time()-start)
    Path(args.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('FINAL',len(alltrees),len(certs),len(fail),len(remaining),'seconds',time.time()-start,flush=True)
if __name__=='__main__':main()
