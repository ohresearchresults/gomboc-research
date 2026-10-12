#!/usr/bin/env python3
"""Exact audit for the cut-stack tetrahedral-shell theorem; Python stdlib only.
Run: python -B -S positive_shell.py
The continuous proof is analytic; finite controls do not replace it.
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import sys

Z = [(F(1),F(1),F(1)), (F(1),F(-1),F(-1)),
     (F(-1),F(1),F(-1)), (F(-1),F(-1),F(1))]
CELLS = [(0,1,2,5),(0,1,4,5),(0,3,4,5),(3,4,5,9),
         (0,1,2,8),(0,1,7,8),(0,6,7,8)]
M = [[F(7),F(1),F(2)], [F(1),F(5),F(-1)], [F(2),F(-1),F(6)]]
ZERO = (F(0),F(0),F(0))

def add(x,y): return tuple(a+b for a,b in zip(x,y))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))
def scale(a,x): return tuple(a*b for b in x)
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def cross(x,y): return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])
def det(A): return dot(A[0],cross(A[1],A[2]))
def mv(A,x): return tuple(dot(r,x) for r in A)
def transpose(A): return list(map(list,zip(*A)))
def mm(A,B): return [[dot(r,c) for c in zip(*B)] for r in A]
def outer(x,y): return [[a*b for b in y] for a in x]
def matadd(A,B): return [[A[i][j]+B[i][j] for j in range(3)] for i in range(3)]
def matscale(a,A): return [[a*x for x in r] for r in A]
def zero_matrix(): return [[F(0) for _ in range(3)] for _ in range(3)]
def symouter(x,y): return matscale(F(1,2),matadd(outer(x,y),outer(y,x)))
def inverse(A):
    n=len(A)
    B=[list(r)+[F(i==j) for j in range(n)] for i,r in enumerate(A)]
    for j in range(n):
        k=next((k for k in range(j,n) if B[k][j]),None)
        if k is None: raise ValueError('singular matrix')
        B[j],B[k]=B[k],B[j]
        z=B[j][j]; B[j]=[x/z for x in B[j]]
        for i in range(n):
            if i!=j:
                z=B[i][j]; B[i]=[x-z*y for x,y in zip(B[i],B[j])]
    return [r[n:] for r in B]
def rank(A):
    B=[list(r) for r in A]; r=0
    for j in range(3):
        k=next((k for k in range(r,len(B)) if B[k][j]),None)
        if k is None: continue
        B[r],B[k]=B[k],B[r]; z=B[r][j]; B[r]=[x/z for x in B[r]]
        for i in range(len(B)):
            if i!=r:
                z=B[i][j]; B[i]=[x-z*y for x,y in zip(B[i],B[r])]
        r+=1
    return r
def minors(A): return [A[0][0],A[0][0]*A[1][1]-A[0][1]**2,det(A)]
def six(T): return abs(det([sub(T[i],T[0]) for i in (1,2,3)]))
def moments(tets):
    D=F(0); J=ZERO; W=zero_matrix()
    for T in tets:
        w=six(T); assert w>0
        C=tuple(sum(x[j] for x in T) for j in range(3))
        Q=zero_matrix()
        for x in T: Q=matadd(Q,outer(x,x))
        D+=w; J=add(J,scale(w,C)); W=matadd(W,matscale(w,matadd(outer(C,C),Q)))
    g=scale(1/(4*D),J)
    cov=matadd(matscale(1/(20*D),W),matscale(-1,outer(g,g)))
    return D,g,cov

def corner_check():
    records=[]
    for root in range(4):
        others=[i for i in range(4) if i!=root]
        for dest in product(range(4),repeat=3):
            parent=dict(zip(others,dest)); good=True
            for i in others:
                seen=set(); j=i
                while j!=root and j not in seen:
                    seen.add(j); j=parent[j]
                if j!=root: good=False; break
            if not good: continue
            Q=zero_matrix()
            for i,j in parent.items(): Q=matadd(Q,symouter(Z[i],sub(Z[i],Z[j])))
            shifted=[[Q[i][j]-(F(5,8) if i==j else 0) for j in range(3)] for i in range(3)]
            mi=minors(shifted); assert min(mi)>0
            records.append({'root':root,'parent':parent,'Q':Q,'minors':mi})
    assert len(records)==64
    delta=F(1,8192); gap=F(25,4608)-42*delta-48*delta**2
    assert gap==F(11237,37748736)
    assert gap>F(1,4096) and gap>18*F(1,65536)
    eps=F(1,131072)
    eta=(1+2*eps)*3*eps/(1-eps)
    assert 4*eta<delta
    tail_eps=F(1,262144)
    assert (1+tail_eps)*(F(1,65536)+2*tail_eps)<F(1,32768)
    covariance_bound=F(1,5)+9*delta*(1+delta)**2
    assert covariance_bound<F(1,4)
    return {'trees':records,'delta':delta,'gap':gap,'tree_gamma':F(1,65536),
            'whole_pencil_eta_bound':eta,'covariance_bound':covariance_bound}

def raw_chart(beta,s,p,q,u,a):
    assert 0<beta<1 and s>0 and min(p+q)>0 and min(u)>=0 and sum(u)==1
    assert s>dot(u,p)
    b=[(F(0),-beta,F(0)),(F(0),1-beta,F(0)),(F(0),F(0),F(1))]
    d=[1+a*x for x in p]; e=[1+(1-a)*x for x in q]; ds=1+a*s
    assert min(d+e+[ds])>0
    X=b+[scale(1/d[j],(-p[j],b[j][1],b[j][2])) for j in range(3)]
    X += [scale(1/e[j],(q[j],b[j][1],b[j][2])) for j in range(3)]
    ub=tuple(sum(u[j]*b[j][k] for j in range(3)) for k in range(3))
    X += [scale(1/ds,(-s,ub[1],ub[2]))]
    prod_d=d[0]*d[1]*d[2]
    weights=[p[2]/d[2],p[1]/(d[1]*d[2]),p[0]/prod_d,
             (s-dot(u,p))/(ds*prod_d),q[2]/e[2],q[1]/(e[1]*e[2]),q[0]/(e[0]*e[1]*e[2])]
    for C,w in zip(CELLS,weights): assert six([X[i] for i in C])==w
    o=(1-beta,beta,F(0)); v=add(u,scale(s,o))
    H=s+dot(q,v); zeta=dot(o,q)
    bary=[]
    for j in range(3):
        bary.append(tuple([e[i]*(F(i==j)-v[i]*q[j]/H) for i in range(3)]+[ds*q[j]/H]))
    for j in range(3):
        A=p[j]*(1+zeta)+q[j]
        bary.append(tuple([e[i]*(F(i==j)+p[j]*o[i]-v[i]*A/H)/d[j] for i in range(3)]+[ds*A/(H*d[j])]))
    bary += [tuple(F(i==j) for i in range(4)) for j in range(3)]
    bary += [(F(0),F(0),F(0),F(1))]
    vertices=[X[6],X[7],X[8],X[9]]
    for x,lam in zip(X,bary):
        assert sum(lam)==1 and lam[3]>=0
        assert x==tuple(sum(lam[i]*vertices[i][j] for i in range(4)) for j in range(3))
    K=[tuple(sum(lam[i]*Z[i][j] for i in range(4)) for j in range(3)) for lam in bary]
    eta=max(F(0),-min(t for lam in bary for t in lam))
    assert eta<=F(1,32768)
    W=transpose([sub(X[i],X[9]) for i in (6,7,8)])
    A=mm(transpose([sub(Z[i],Z[3]) for i in range(3)]),inverse(W))
    shift=sub(Z[3],mv(A,X[9]))
    assert K==[add(mv(A,x),shift) for x in X]
    assert six(vertices)==H/(ds*e[0]*e[1]*e[2])
    rawD,rawg,rawcov=moments([[X[i] for i in C] for C in CELLS])
    D,g,cov=moments([[K[i] for i in C] for C in CELLS])
    assert D==abs(det(A))*rawD and g==add(mv(A,rawg),shift)
    assert cov==mm(mm(A,rawcov),transpose(A))
    return K,D,g,cov,bary,eta

def hull(K):
    supports={}
    for i,j,k in combinations(range(len(K)),3):
        n=cross(sub(K[j],K[i]),sub(K[k],K[i]))
        if n==ZERO: continue
        h=dot(n,K[i]); signs=[h-dot(n,x) for x in K]
        if min(signs)<0 and max(signs)>0: continue
        if max(signs)<=0: n=scale(-1,n); h=-h
        div=abs(next(x for x in n if x)); n=scale(1/div,n); h/=div
        supports[tuple(n)+(h,)]=(n,h)
    S=sorted(supports.values(),key=lambda nh:tuple(nh[0])+(nh[1],))
    active=[{i for i,(n,h) in enumerate(S) if dot(n,x)==h} for x in K]
    true=[j for j,A in enumerate(active) if rank([S[i][0] for i in A])==3]
    E=[(i,j) for i,j in combinations(true,2) if len(active[i]&active[j])>=2]
    facets=[]; fan=[]
    for f,(n,h) in enumerate(S):
        V=[i for i in true if f in active[i]]
        adjacency={i:sorted(j for j in V if (min(i,j),max(i,j)) in E) for i in V}
        assert all(len(v)==2 for v in adjacency.values())
        C=[min(V),adjacency[min(V)][0]]
        while len(C)<len(V): C.append(next(j for j in adjacency[C[-1]] if j!=C[-2]))
        assert C[0] in adjacency[C[-1]]
        if dot(cross(sub(K[C[1]],K[C[0]]),sub(K[C[2]],K[C[0]])),n)<0:
            C=[C[0]]+list(reversed(C[1:]))
        facets.append(C)
        for k in range(1,len(C)-1): fan.append([ZERO,K[C[0]],K[C[k]],K[C[k+1]]])
    assert len(true)-len(E)+len(S)==2
    return S,active,true,E,facets,fan

def mechanics(K,g,S,active,true,E):
    X=[sub(x,g) for x in K]; N=inverse(M)
    poles=[scale(1/(h-dot(n,g)),n) for n,h in S]
    assert min(minors(M))>0
    P={(i,j):dot(X[i],mv(M,sub(X[j],X[i]))) for e in E for i,j in (e,e[::-1])}
    dual_edges={tuple(sorted(active[i]&active[j])) for i,j in E}
    assert all(len(t)==2 for t in dual_edges)
    Q={(i,j):dot(poles[i],mv(N,sub(poles[j],poles[i]))) for e in dual_edges for i,j in (e,e[::-1])}
    U=[i for i in true if all(v<0 for (a,b),v in P.items() if a==i)]
    stable=[i for i in range(len(S)) if all(v<0 for (a,b),v in Q.items() if a==i)]
    saddles=[]; weak={}; rows=[]; physical_zero=0
    for a,b in E:
        i,j=sorted(active[a]&active[b]); r=[P[a,b],P[b,a],Q[i,j],Q[j,i]]
        rows.append({'edge':[a,b],'facets':[i,j],'primitives':r})
        if max(r)<0: saddles.append([a,b])
        if max(r)<=0 and 0 in r:
            physical_zero+=r.count(0)
            if r[0]==0: point=X[a]
            elif r[1]==0: point=X[b]
            else:
                k=i if r[2]==0 else j
                point=scale(1/dot(poles[k],mv(N,poles[k])),mv(N,poles[k]))
            weak.setdefault(point,[]).append([a,b])
    zeros=sum(v==0 for v in list(P.values())+list(Q.values()))
    assert len(stable)+len(U)-len(saddles)==2
    return {'strict_SUH':[len(stable),len(U),len(saddles)],'U_labels':U,
            'S_facets':stable,'saddles':saddles,'weak_points':len(weak),
            'zero_primitives':zeros,'harmless_zeros':zeros-physical_zero,'edge_rows':rows}

def control(name,beta,s,p,q,u,a):
    K,D,g,cov,bary,eta=raw_chart(beta,s,p,q,u,a)
    S,active,true,E,facets,fan=hull(K)
    assert moments(fan)==(D,g,cov)
    census=mechanics(K,g,S,active,true,E)
    assert census['strict_SUH'][1]>=2
    neg=sum(x==0 for x in u)
    expected=[10,17,9] if neg==0 else ([10,16,8] if neg==1 else [9,14,7])
    assert [len(true),len(E),len(facets)]==expected
    distances=[min(dot(sub(K[j],z),sub(K[j],z)) for z in Z) for j in range(3)]
    return {'name':name,'input':{'beta':beta,'s':s,'p':p,'q':q,'u':u,'a':a},
            'vertices':K,'true_labels':true,'facets':facets,'edges':E,
            'f_vector':expected,'volume':D/6,'centroid':g,'covariance':cov,
            'barycentric_rows':bary,'eta':eta,'base_nearest_corner_distance_squared':distances,
            'metric':M,'census':census}

def encode(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [encode(v) for v in x]
    return x

def main():
    eps=F(1,131072); beta=F(2,5); s=F(1)
    p=(eps/2,2*eps/3,3*eps/4); q=(eps,3*eps/4,eps/2)
    u=(F(1,5),F(2,5),F(2,5)); controls=[]
    for name,a in [('negative',F(-1,2)),('zero',F(0)),('one',F(1)),
                   ('positive_middle',F(65536)),('right_near_horizon',F(131072))]:
        controls.append(control(name,beta,s,p,q,u,a))
    weights=[(0,F(2,5),F(3,5)),(F(2,5),0,F(3,5)),(F(2,5),F(3,5),0),
             (1,0,0),(0,1,0),(0,0,1)]
    for j,w in enumerate(weights):
        controls.append(control('weight_boundary_'+str(j),beta,s,p,q,tuple(map(F,w)),F(65536)))
    controls.append(control('interior_edge_refinement',F(1,2),s,(eps,)*3,(eps,)*3,
                            (F(1,3),)*3,F(131073,2)))
    assert min(controls[-1]['base_nearest_corner_distance_squared'])>1
    controls.append(control('large_left_tail',beta,s,(F(1,2),F(2,3),F(3,4)),
                            (F(1,262144),F(1,524288),F(3,1048576)),u,F(65536)))
    report=encode({'schema':'FULL_CUT_STACK_POSITIVE_SHELL_V1','corner_and_scalar_checks':corner_check(),
                   'controls':controls})
    out=(json.dumps(report,sort_keys=True,separators=(',',':'))+'\n').encode()
    Path('positive_shell_report.json').write_bytes(out)
    for C in controls:
        print(C['name'],'f='+str(C['f_vector']),'SUH='+str(C['census']['strict_SUH']),
              'weak='+str(C['census']['weak_points']),'zeros='+str(C['census']['zero_primitives']))
    print('REPORT_BYTES',len(out))
    print('REPORT_SHA256',hashlib.sha256(out).hexdigest())
    print('PYTHON',sys.version.split()[0])
    print('ALL_64_CORNER_TREES_AND_SHELL_CONSTANTS_PASS')
    print('ALL_13_ACTUAL_REFILLS_HULLS_MOMENTS_AND_CENSUSES_PASS')
    print('FULL_CUT_STACK_POSITIVE_SHELL_ANALYTICAL_AUDIT_PASS')

if __name__=='__main__': main()
